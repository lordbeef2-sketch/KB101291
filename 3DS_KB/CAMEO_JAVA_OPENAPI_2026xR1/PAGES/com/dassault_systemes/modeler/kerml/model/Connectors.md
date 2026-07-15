# JAVA OPENAPI: Connectors (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Connectors.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Connectors.html`
- source_sha256: `a654eaddcb1e2e054df9cbf678ff9933da0ec994d0503ee2cdb41e193c97dfb8`
- captured_utc: `2026-07-14T16:44:47.558836+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Connectors

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Connectors

@OpenApiAllpublic classConnectors
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Connector`](kerml/Connector.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[SOURCE_INDEX](#SOURCE_INDEX)`
Index of the source end feature for the connector.
`static final int`
`[TARGET_INDEX](#TARGET_INDEX)`
Index of the target end feature for the connector
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Connectors](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Connector](kerml/Connector.html)>`
`[getConnectedConnectors](#getConnectedConnectors(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Returns all connectors connected to the given feature.
`static [Feature](kerml/Feature.html)`
`[getConnectorEndSourceFeature](#getConnectorEndSourceFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the source feature of the connector end.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getConnectorEndTargetFeature](#getConnectorEndTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the target features of the connector end.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getEndChain](#getEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int))([Connector](kerml/Connector.html) connector,
 int endIndex)`
Returns the feature chain for the specified connector end.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getEndChain](#getEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) end)`
Returns the feature chain for the given end feature.
`static [Feature](kerml/Feature.html)`
`[getEndChainFirstFeature](#getEndChainFirstFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int))([Connector](kerml/Connector.html) connector,
 int endIndex)`
Returns the first feature in the chain of the specified connector end.
`static [Feature](kerml/Feature.html)`
`[getEndChainLastFeature](#getEndChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int))([Connector](kerml/Connector.html) connector,
 int endIndex)`
Returns the last feature in the chain of the specified connector end.
`static [Feature](kerml/Feature.html)`
`[getEndChainLastFeature](#getEndChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) end)`
Returns the last feature in the chain of the given end feature.
`static [Feature](kerml/Feature.html)`
`[getEndFeature](#getEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,int))([Type](kerml/Type.html) type,
 int endIndex)`
Returns the end feature at the given index of the type.
`static <T extends [Feature](kerml/Feature.html)> 
T`
`[getOrCreateEndFeature](#getOrCreateEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int))([Connector](kerml/Connector.html) connector,
 int endIndex)`
Returns the end feature at the given index, creating it if necessary.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getSourceChain](#getSourceChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the source end chain of the connector.
`static [Feature](kerml/Feature.html)`
`[getSourceChainLastFeature](#getSourceChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the last feature in the source end chain of the connector.
`static [Feature](kerml/Feature.html)`
`[getSourceEnd](#getSourceEnd(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the source end feature of the connector.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)>`
`[getTargetChain](#getTargetChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the target end chain of the connector.
`static [Feature](kerml/Feature.html)`
`[getTargetChainLastFeature](#getTargetChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the last feature in the target end chain of the connector.
`static [Feature](kerml/Feature.html)`
`[getTargetEnd](#getTargetEnd(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Returns the target end feature of the connector.
`static boolean`
`[isConnectorOrRepresentsConnector](#isConnectorOrRepresentsConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element))([Element](kerml/Element.html) element)`
Checks whether the element is a connector or represents one via relationship mapping.
`static boolean`
`[isContext](#isContext(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Type](kerml/Type.html) context,
 [Connector](kerml/Connector.html) connector)`
Checks whether the given type is the context of the connector.
`static boolean`
`[isNaryConnector](#isNaryConnector(com.dassault_systemes.modeler.foundation.model.ModelElement))([ModelElement](../../foundation/model/ModelElement.html) element)`
Checks whether the given model element is an n‑ary connector.
`static boolean`
`[isPackageLevel](#isPackageLevel(com.dassault_systemes.modeler.kerml.model.kerml.Connector))([Connector](kerml/Connector.html) connector)`
Checks whether the connector is defined at package level.
`static boolean`
`[setEndChain](#setEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int,java.util.List))([Connector](kerml/Connector.html) connector,
 int endIndex,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)`
Sets the feature chain for the specified connector end.
`static boolean`
`[setEndChain](#setEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List))([Feature](kerml/Feature.html) end,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)`
Sets the feature chain for the given end feature.
`static boolean`
`[setSourceChain](#setSourceChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,java.util.List))([Connector](kerml/Connector.html) connector,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)`
Sets the source end chain of the connector.
`static boolean`
`[setTargetChain](#setTargetChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,java.util.List))([Connector](kerml/Connector.html) connector,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)`
Sets the target end chain of the connector.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SOURCE_INDEX
public static final int SOURCE_INDEX
Index of the source end feature for the connector.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Connectors.SOURCE_INDEX)
TARGET_INDEX
public static final int TARGET_INDEX
Index of the target end feature for the connector
See Also:
[Constant Field Values](../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Connectors.TARGET_INDEX)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Connectors
public Connectors()
 ============ METHOD DETAIL ========== 
Method Details
getSourceChainLastFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getSourceChainLastFeature([Connector](kerml/Connector.html) connector)
Returns the last feature in the source end chain of the connector.
Parameters:
`connector` - the connector
Returns:
last feature of the source chain, or null
getTargetChainLastFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getTargetChainLastFeature([Connector](kerml/Connector.html) connector)
Returns the last feature in the target end chain of the connector.
Parameters:
`connector` - the connector
Returns:
last feature of the target chain, or null
getEndChainLastFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getEndChainLastFeature([Connector](kerml/Connector.html) connector,
 int endIndex)
Returns the last feature in the chain of the specified connector end.
Parameters:
`connector` - the connector
`endIndex` - index of the end (0 = source, 1 = target)
Returns:
last feature of the chain, or null
getEndChainLastFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getEndChainLastFeature([Feature](kerml/Feature.html) end)
Returns the last feature in the chain of the given end feature.
Parameters:
`end` - the end feature
Returns:
last feature of the chain, or null
getEndChainFirstFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getEndChainFirstFeature([Connector](kerml/Connector.html) connector,
 int endIndex)
Returns the first feature in the chain of the specified connector end.
Parameters:
`connector` - the connector
`endIndex` - index of the end (0 = source, 1 = target)
Returns:
first feature of the chain, or null
setSourceChain
public static boolean setSourceChain([Connector](kerml/Connector.html) connector,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)
Sets the source end chain of the connector.
Parameters:
`connector` - the connector
`chain` - feature chain
Returns:
true if updated
getSourceChain
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getSourceChain([Connector](kerml/Connector.html) connector)
Returns the source end chain of the connector.
Parameters:
`connector` - the connector
Returns:
source chain
setTargetChain
public static boolean setTargetChain([Connector](kerml/Connector.html) connector,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)
Sets the target end chain of the connector.
Parameters:
`connector` - the connector
`chain` - feature chain
Returns:
true if updated
getTargetChain
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getTargetChain([Connector](kerml/Connector.html) connector)
Returns the target end chain of the connector.
Parameters:
`connector` - the connector
Returns:
target chain
getSourceEnd
@CheckForNullpublic static [Feature](kerml/Feature.html) getSourceEnd([Connector](kerml/Connector.html) connector)
Returns the source end feature of the connector.
Parameters:
`connector` - the connector
Returns:
source end feature, or null
getTargetEnd
@CheckForNullpublic static [Feature](kerml/Feature.html) getTargetEnd([Connector](kerml/Connector.html) connector)
Returns the target end feature of the connector.
Parameters:
`connector` - the connector
Returns:
target end feature, or null
getEndChain
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getEndChain([Connector](kerml/Connector.html) connector,
 int endIndex)
Returns the feature chain for the specified connector end.
Parameters:
`connector` - the connector
`endIndex` - index of the end
Returns:
feature chain
getEndChain
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getEndChain([Feature](kerml/Feature.html) end)
Returns the feature chain for the given end feature.
Parameters:
`end` - the end feature
Returns:
feature chain
getEndFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getEndFeature([Type](kerml/Type.html) type,
 int endIndex)
Returns the end feature at the given index of the type.
Parameters:
`type` - the type
`endIndex` - index of the end
Returns:
end feature, or null
setEndChain
public static boolean setEndChain([Connector](kerml/Connector.html) connector,
 int endIndex,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)
Sets the feature chain for the specified connector end.
Parameters:
`connector` - the connector
`endIndex` - index of the end
`chain` - feature chain
Returns:
true if updated
setEndChain
public static boolean setEndChain([Feature](kerml/Feature.html) end,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [Feature](kerml/Feature.html)> chain)
Sets the feature chain for the given end feature.
Parameters:
`end` - the end feature
`chain` - feature chain
Returns:
true if updated
getOrCreateEndFeature
public static <T extends [Feature](kerml/Feature.html)> T getOrCreateEndFeature([Connector](kerml/Connector.html) connector,
 int endIndex)
Returns the end feature at the given index, creating it if necessary.
Type Parameters:
`T` - feature type
Parameters:
`connector` - the connector
`endIndex` - index of the end
Returns:
existing or newly created end feature
getConnectorEndSourceFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getConnectorEndSourceFeature([Connector](kerml/Connector.html) connector)
Returns the source feature of the connector end.
Parameters:
`connector` - the connector
Returns:
source feature, or null
getConnectorEndTargetFeature
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Feature](kerml/Feature.html)> getConnectorEndTargetFeature([Connector](kerml/Connector.html) connector)
Returns the target features of the connector end.
Parameters:
`connector` - the connector
Returns:
list of target features
getConnectedConnectors
public static [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[Connector](kerml/Connector.html)> getConnectedConnectors([Feature](kerml/Feature.html) feature)
Returns all connectors connected to the given feature.
Parameters:
`feature` - the feature
Returns:
connected connectors
isPackageLevel
public static boolean isPackageLevel([Connector](kerml/Connector.html) connector)
Checks whether the connector is defined at package level.
Parameters:
`connector` - the connector
Returns:
true if package‑level
isContext
public static boolean isContext([Type](kerml/Type.html) context,
 [Connector](kerml/Connector.html) connector)
Checks whether the given type is the context of the connector.
Parameters:
`context` - the type
`connector` - the connector
Returns:
true if the type is the connector's context
isConnectorOrRepresentsConnector
public static boolean isConnectorOrRepresentsConnector([Element](kerml/Element.html) element)
Checks whether the element is a connector or represents one via relationship mapping.
Parameters:
`element` - the element
Returns:
true if connector or represents a connector
isNaryConnector
public static boolean isNaryConnector([ModelElement](../../foundation/model/ModelElement.html) element)
Checks whether the given model element is an n‑ary connector.
Parameters:
`element` - the model element
Returns:
true if n‑ary connector

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Connectors">Class Connectors</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Connectors</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Connectors</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Connector</code></a></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SOURCE_INDEX">SOURCE_INDEX</a></code></div>
<div class="col-last even-row-color">
<div class="block">Index of the source end feature for the connector.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TARGET_INDEX">TARGET_INDEX</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Index of the target end feature for the connector</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Connectors</a>()</code></div>
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
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectedConnectors(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getConnectedConnectors</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all connectors connected to the given feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectorEndSourceFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getConnectorEndSourceFeature</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source feature of the connector end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectorEndTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getConnectorEndTargetFeature</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target features of the connector end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">getEndChain</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the feature chain for the specified connector end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getEndChain</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the feature chain for the given end feature.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndChainFirstFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">getEndChainFirstFeature</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first feature in the chain of the specified connector end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">getEndChainLastFeature</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the last feature in the chain of the specified connector end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getEndChainLastFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the last feature in the chain of the given end feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,int)">getEndFeature</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 int endIndex)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the end feature at the given index of the type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;<br/>T</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">getOrCreateEndFeature</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the end feature at the given index, creating it if necessary.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getSourceChain</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source end chain of the connector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getSourceChainLastFeature</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the last feature in the source end chain of the connector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceEnd(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getSourceEnd</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source end feature of the connector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getTargetChain</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target end chain of the connector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getTargetChainLastFeature</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the last feature in the target end chain of the connector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetEnd(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">getTargetEnd</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target end feature of the connector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isConnectorOrRepresentsConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element)">isConnectorOrRepresentsConnector</a><wbr/>(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the element is a connector or represents one via relationship mapping.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isContext(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Connector)">isContext</a><wbr/>(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context,
 <a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given type is the context of the connector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNaryConnector(com.dassault_systemes.modeler.foundation.model.ModelElement)">isNaryConnector</a><wbr/>(<a href="../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given model element is an n‑ary connector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPackageLevel(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">isPackageLevel</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the connector is defined at package level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int,java.util.List)">setEndChain</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the feature chain for the specified connector end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">setEndChain</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the feature chain for the given end feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setSourceChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,java.util.List)">setSourceChain</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the source end chain of the connector.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setTargetChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,java.util.List)">setTargetChain</a><wbr/>(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the target end chain of the connector.</div>
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
<section class="detail" id="SOURCE_INDEX">
<h3>SOURCE_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">SOURCE_INDEX</span></div>
<div class="block">Index of the source end feature for the connector.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Connectors.SOURCE_INDEX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TARGET_INDEX">
<h3>TARGET_INDEX</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">TARGET_INDEX</span></div>
<div class="block">Index of the target end feature for the connector</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.dassault_systemes.modeler.kerml.model.Connectors.TARGET_INDEX">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>Connectors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Connectors</span>()</div>
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
<section class="detail" id="getSourceChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getSourceChainLastFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getSourceChainLastFeature</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the last feature in the source end chain of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>last feature of the source chain, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getTargetChainLastFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getTargetChainLastFeature</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the last feature in the target end chain of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>last feature of the target chain, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">
<h3>getEndChainLastFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getEndChainLastFeature</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</span></div>
<div class="block">Returns the last feature in the chain of the specified connector end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dd><code>endIndex</code> - index of the end (0 = source, 1 = target)</dd>
<dt>Returns:</dt>
<dd>last feature of the chain, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndChainLastFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getEndChainLastFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getEndChainLastFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</span></div>
<div class="block">Returns the last feature in the chain of the given end feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>end</code> - the end feature</dd>
<dt>Returns:</dt>
<dd>last feature of the chain, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndChainFirstFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">
<h3>getEndChainFirstFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getEndChainFirstFeature</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</span></div>
<div class="block">Returns the first feature in the chain of the specified connector end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dd><code>endIndex</code> - index of the end (0 = source, 1 = target)</dd>
<dt>Returns:</dt>
<dd>first feature of the chain, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSourceChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,java.util.List)">
<h3>setSourceChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setSourceChain</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</span></div>
<div class="block">Sets the source end chain of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dd><code>chain</code> - feature chain</dd>
<dt>Returns:</dt>
<dd>true if updated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getSourceChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getSourceChain</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the source end chain of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>source chain</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTargetChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,java.util.List)">
<h3>setTargetChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setTargetChain</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</span></div>
<div class="block">Sets the target end chain of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dd><code>chain</code> - feature chain</dd>
<dt>Returns:</dt>
<dd>true if updated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getTargetChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getTargetChain</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the target end chain of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>target chain</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSourceEnd(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getSourceEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getSourceEnd</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the source end feature of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>source end feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetEnd(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getTargetEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getTargetEnd</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the target end feature of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>target end feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">
<h3>getEndChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getEndChain</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</span></div>
<div class="block">Returns the feature chain for the specified connector end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dd><code>endIndex</code> - index of the end</dd>
<dt>Returns:</dt>
<dd>feature chain</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getEndChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getEndChain</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</span></div>
<div class="block">Returns the feature chain for the given end feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>end</code> - the end feature</dd>
<dt>Returns:</dt>
<dd>feature chain</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Type,int)">
<h3>getEndFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getEndFeature</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> type,
 int endIndex)</span></div>
<div class="block">Returns the end feature at the given index of the type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the type</dd>
<dd><code>endIndex</code> - index of the end</dd>
<dt>Returns:</dt>
<dd>end feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int,java.util.List)">
<h3>setEndChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setEndChain</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</span></div>
<div class="block">Sets the feature chain for the specified connector end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dd><code>endIndex</code> - index of the end</dd>
<dd><code>chain</code> - feature chain</dd>
<dt>Returns:</dt>
<dd>true if updated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEndChain(com.dassault_systemes.modeler.kerml.model.kerml.Feature,java.util.List)">
<h3>setEndChain</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setEndChain</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt; chain)</span></div>
<div class="block">Sets the feature chain for the given end feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>end</code> - the end feature</dd>
<dd><code>chain</code> - feature chain</dd>
<dt>Returns:</dt>
<dd>true if updated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateEndFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector,int)">
<h3>getOrCreateEndFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">getOrCreateEndFeature</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector,
 int endIndex)</span></div>
<div class="block">Returns the end feature at the given index, creating it if necessary.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - feature type</dd>
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dd><code>endIndex</code> - index of the end</dd>
<dt>Returns:</dt>
<dd>existing or newly created end feature</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectorEndSourceFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getConnectorEndSourceFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getConnectorEndSourceFeature</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the source feature of the connector end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>source feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectorEndTargetFeature(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>getConnectorEndTargetFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a>&gt;</span> <span class="element-name">getConnectorEndTargetFeature</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Returns the target features of the connector end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>list of target features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectedConnectors(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getConnectedConnectors</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a>&gt;</span> <span class="element-name">getConnectedConnectors</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Returns all connectors connected to the given feature.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>connected connectors</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPackageLevel(com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>isPackageLevel</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPackageLevel</span><wbr/><span class="parameters">(<a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Checks whether the connector is defined at package level.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>true if package‑level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isContext(com.dassault_systemes.modeler.kerml.model.kerml.Type,com.dassault_systemes.modeler.kerml.model.kerml.Connector)">
<h3>isContext</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isContext</span><wbr/><span class="parameters">(<a href="kerml/Type.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Type</a> context,
 <a href="kerml/Connector.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Connector</a> connector)</span></div>
<div class="block">Checks whether the given type is the context of the connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - the type</dd>
<dd><code>connector</code> - the connector</dd>
<dt>Returns:</dt>
<dd>true if the type is the connector's context</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isConnectorOrRepresentsConnector(com.dassault_systemes.modeler.kerml.model.kerml.Element)">
<h3>isConnectorOrRepresentsConnector</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isConnectorOrRepresentsConnector</span><wbr/><span class="parameters">(<a href="kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> element)</span></div>
<div class="block">Checks whether the element is a connector or represents one via relationship mapping.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>true if connector or represents a connector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNaryConnector(com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>isNaryConnector</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNaryConnector</span><wbr/><span class="parameters">(<a href="../../foundation/model/ModelElement.html" title="interface in com.dassault_systemes.modeler.foundation.model">ModelElement</a> element)</span></div>
<div class="block">Checks whether the given model element is an n‑ary connector.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the model element</dd>
<dt>Returns:</dt>
<dd>true if n‑ary connector</dd>
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
