# JAVA OPENAPI: SimulationHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/simulation/SimulationHelper.html
- source_path: `com/nomagic/magicdraw/simulation/SimulationHelper.html`
- source_sha256: `efa0fe751657dbe66d0ddb8890f0faf8fd00415d4491013a703189c734325c7f`
- captured_utc: `2026-07-14T16:55:30.878183+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.simulation](package-summary.html)

## Class SimulationHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.simulation.SimulationHelper

@OpenApiAllpublic final classSimulationHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The helper class of the cameo simulation toolkit.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SimulationHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.FeatureValue>`
`[findFeatureValue](#findFeatureValue(fUML.Semantics.Classes.Kernel.CompoundValue,java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property))(fUML.Semantics.Classes.Kernel.CompoundValue runtimeContext,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)> propertyPath,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) target)`
Collect all featureValue objects which are matching with the given nested property path
 in the given runtime object.
`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Signal](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)>`
`[getAvailableSignals](#getAvailableSignals(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.magicdraw.simulation.engine.ExecutionEngine))(fUML.Semantics.Classes.Kernel.StructuredValue target,
 [ExecutionEngine](engine/ExecutionEngine.html) engine)`
Get availableSignals from the specified StructuredValue.
`static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getConfigElement](#getConfigElement(com.nomagic.magicdraw.simulation.execution.SimulationExecution))([SimulationExecution](execution/SimulationExecution.html) execution)`
Gets simulation config element from simulation execution.
`static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getSimulationOptionValue](#getSimulationOptionValue(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context)`
Get the simulation option value
 In case there is no execution, will try to return the option value from project or environment options of the tool
`static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)`
`[isFeatureValueInvalid](#isFeatureValueInvalid(fUML.Semantics.Classes.Kernel.FeatureValue,int))(fUML.Semantics.Classes.Kernel.FeatureValue featureValue,
 int index)`
Check the specified FeautureValue is invalid value or not.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SimulationHelper
public SimulationHelper()
 ============ METHOD DETAIL ========== 
Method Details
findFeatureValue
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<fUML.Semantics.Classes.Kernel.FeatureValue> findFeatureValue(fUML.Semantics.Classes.Kernel.CompoundValue runtimeContext,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html)> propertyPath,
 [Property](../../uml2/ext/magicdraw/classes/mdkernel/Property.html) target)
Collect all featureValue objects which are matching with the given nested property path
 in the given runtime object.
Parameters:
`runtimeContext` - is the runtime object which is the owner of the returned runtime values,
 specified by propertyPath.
`propertyPath` - is the property path to the requires runtime values. The first property
 in the propertyPath must be owned by the classifier that type the owner.
 to be found.
`target` - target Property
Returns:
list of runtime values which are reside in the given 'owner' and matching to
 the given nested propertyPath.
getConfigElement
@CheckForNullpublic static [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getConfigElement(@CheckForNull
 [SimulationExecution](execution/SimulationExecution.html) execution)
Gets simulation config element from simulation execution.
Parameters:
`execution` - SimulationExecution
Returns:
Simulation config element or null.
isFeatureValueInvalid
@CheckForNullpublic static [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) isFeatureValueInvalid(fUML.Semantics.Classes.Kernel.FeatureValue featureValue,
 int index)
Check the specified FeautureValue is invalid value or not.
Parameters:
`featureValue` - the specified FeautureValue
`index` - index of the value
Returns:
Boolean.TRUE if featureValue is invalid.
 Boolean.FALSE if featureValue is valid.
 null if featureValue is not evaluated.
getAvailableSignals
public static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Signal](../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html)> getAvailableSignals(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue target,
 @CheckForNull
 [ExecutionEngine](engine/ExecutionEngine.html) engine)
Get availableSignals from the specified StructuredValue.
Parameters:
`target` - the specified StructuredValue
`engine` - ExecutionEngine
Returns:
Set
getSimulationOptionValue
@CheckForNullpublic static [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getSimulationOptionValue([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) context)
Get the simulation option value
 In case there is no execution, will try to return the option value from project or environment options of the tool
Parameters:
`name` - the simulation option name constant (usually from [`SimulationOptions`](execution/SimulationOptions.html))
Returns:
the simulation option value, if exists

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.simulation</a></div>
<h1 class="title" title="Class SimulationHelper">Class SimulationHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.simulation.SimulationHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">SimulationHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The helper class of the cameo simulation toolkit.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SimulationHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.FeatureValue&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findFeatureValue(fUML.Semantics.Classes.Kernel.CompoundValue,java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">findFeatureValue</a><wbr/>(fUML.Semantics.Classes.Kernel.CompoundValue runtimeContext,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; propertyPath,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collect all featureValue objects which are matching with the given nested property path
 in the given runtime object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAvailableSignals(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.magicdraw.simulation.engine.ExecutionEngine)">getAvailableSignals</a><wbr/>(fUML.Semantics.Classes.Kernel.StructuredValue target,
 <a href="engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a> engine)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get availableSignals from the specified StructuredValue.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getConfigElement(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">getConfigElement</a><wbr/>(<a href="execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets simulation config element from simulation execution.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSimulationOptionValue(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSimulationOptionValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get the simulation option value
 In case there is no execution, will try to return the option value from project or environment options of the tool</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFeatureValueInvalid(fUML.Semantics.Classes.Kernel.FeatureValue,int)">isFeatureValueInvalid</a><wbr/>(fUML.Semantics.Classes.Kernel.FeatureValue featureValue,
 int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check the specified FeautureValue is invalid value or not.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>SimulationHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SimulationHelper</span>()</div>
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
<section class="detail" id="findFeatureValue(fUML.Semantics.Classes.Kernel.CompoundValue,java.util.List,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Property)">
<h3>findFeatureValue</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;fUML.Semantics.Classes.Kernel.FeatureValue&gt;</span> <span class="element-name">findFeatureValue</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.CompoundValue runtimeContext,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a>&gt; propertyPath,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a> target)</span></div>
<div class="block">Collect all featureValue objects which are matching with the given nested property path
 in the given runtime object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runtimeContext</code> - is the runtime object which is the owner of the returned runtime values,
 specified by propertyPath.</dd>
<dd><code>propertyPath</code> - is the property path to the requires runtime values. The first property
 in the propertyPath must be owned by the classifier that type the owner.
 to be found.</dd>
<dd><code>target</code> - target Property</dd>
<dt>Returns:</dt>
<dd>list of runtime values which are reside in the given 'owner' and matching to
 the given nested propertyPath.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConfigElement(com.nomagic.magicdraw.simulation.execution.SimulationExecution)">
<h3>getConfigElement</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getConfigElement</span><wbr/><span class="parameters">(@CheckForNull
 <a href="execution/SimulationExecution.html" title="class in com.nomagic.magicdraw.simulation.execution">SimulationExecution</a> execution)</span></div>
<div class="block">Gets simulation config element from simulation execution.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>execution</code> - SimulationExecution</dd>
<dt>Returns:</dt>
<dd>Simulation config element or null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFeatureValueInvalid(fUML.Semantics.Classes.Kernel.FeatureValue,int)">
<h3>isFeatureValueInvalid</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isFeatureValueInvalid</span><wbr/><span class="parameters">(fUML.Semantics.Classes.Kernel.FeatureValue featureValue,
 int index)</span></div>
<div class="block">Check the specified FeautureValue is invalid value or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>featureValue</code> - the specified FeautureValue</dd>
<dd><code>index</code> - index of the value</dd>
<dt>Returns:</dt>
<dd>Boolean.TRUE if featureValue is invalid.
                   Boolean.FALSE if featureValue is valid.
                   null if featureValue is not evaluated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAvailableSignals(fUML.Semantics.Classes.Kernel.StructuredValue,com.nomagic.magicdraw.simulation.engine.ExecutionEngine)">
<h3>getAvailableSignals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../uml2/ext/magicdraw/commonbehaviors/mdcommunications/Signal.html" title="interface in com.nomagic.uml2.ext.magicdraw.commonbehaviors.mdcommunications">Signal</a>&gt;</span> <span class="element-name">getAvailableSignals</span><wbr/><span class="parameters">(@CheckForNull
 fUML.Semantics.Classes.Kernel.StructuredValue target,
 @CheckForNull
 <a href="engine/ExecutionEngine.html" title="class in com.nomagic.magicdraw.simulation.engine">ExecutionEngine</a> engine)</span></div>
<div class="block">Get availableSignals from the specified StructuredValue.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - the specified StructuredValue</dd>
<dd><code>engine</code> - ExecutionEngine</dd>
<dt>Returns:</dt>
<dd>Set<signal></signal></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSimulationOptionValue(java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSimulationOptionValue</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getSimulationOptionValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> context)</span></div>
<div class="block">Get the simulation option value
 In case there is no execution, will try to return the option value from project or environment options of the tool</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the simulation option name constant (usually from <a href="execution/SimulationOptions.html" title="class in com.nomagic.magicdraw.simulation.execution"><code>SimulationOptions</code></a>)</dd>
<dt>Returns:</dt>
<dd>the simulation option value, if exists</dd>
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
