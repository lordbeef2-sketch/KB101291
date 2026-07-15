# JAVA OPENAPI: SmartEventSupport (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/uml2/ext/jmi/smartlistener/SmartEventSupport.html
- source_path: `com/nomagic/uml2/ext/jmi/smartlistener/SmartEventSupport.html`
- source_sha256: `2fa177b81ff0b679dd4dd2d606cb98e4061f0a548c50525163a8174a4e82cb88`
- captured_utc: `2026-07-14T16:56:10.660628+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.smartlistener](package-summary.html)

## Interface SmartEventSupport

@OpenApipublic interfaceSmartEventSupport
Defines an interface form registering smart listeners.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`default void`
`[register](#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration))([Registration](Registration.html) registration)`
Registers smart listener configurations to the specified type objects.
`void`
`[registerConfig](#registerConfig(java.lang.Class,java.util.Collection,java.beans.PropertyChangeListener))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> aClass,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configs,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Deprecated, for removal: This API element is subject to removal in a future version.
[`register(Registration)`](#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)) method should be used instead of this method.
`default void`
`[unregister](#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration))([Registration](Registration.html) registration)`
Unregisters smart listener configurations from the specified type of objects.
`void`
`[unregisterConfig](#unregisterConfig(java.lang.Class,java.util.Collection,java.beans.PropertyChangeListener))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> aClass,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configs,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)`
Deprecated, for removal: This API element is subject to removal in a future version.
[`unregister(Registration)`](#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)) method should be used instead of this method.

============ METHOD DETAIL ========== 
Method Details
register
@OpenApidefault void register([Registration](Registration.html) registration)
Registers smart listener configurations to the specified type objects. Creates smart listeners for
 all existing model elements of the specified type.
Parameters:
`registration` - registration object.
unregister
@OpenApidefault void unregister([Registration](Registration.html) registration)
Unregisters smart listener configurations from the specified type of objects.
Parameters:
`registration` - registration.
registerConfig
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2022x Refresh1",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)void registerConfig([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> aClass,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configs,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Deprecated, for removal: This API element is subject to removal in a future version.
[`register(Registration)`](#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)) method should be used instead of this method.
Registers smart listener configurations to the specified type objects. Creates smart listeners for
 all existing model elements of the specified type.
Parameters:
`aClass` - type of objects to that the smart listener configurations must be registered.
`configs` - smart listener configurations.
`listener` - property change listener that will receive property change events according to specified
 smart listener configurations.
unregisterConfig
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since())="2022x Refresh1",
 [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval())=true)void unregisterConfig([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<? extends [Element](../../magicdraw/classes/mdkernel/Element.html)> aClass,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configs,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener)
Deprecated, for removal: This API element is subject to removal in a future version.
[`unregister(Registration)`](#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)) method should be used instead of this method.
Unregisters smart listener configurations from the specified type of objects.
Parameters:
`aClass` - type of object.
`configs` - smart listener configurations.
`listener` - property change listener.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.smartlistener</a></div>
<h1 class="title" title="Interface SmartEventSupport">Interface SmartEventSupport</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">SmartEventSupport</span></div>
<div class="block">Defines an interface form registering smart listeners.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">register</a><wbr/>(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Registers smart listener configurations to the specified type objects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#registerConfig(java.lang.Class,java.util.Collection,java.beans.PropertyChangeListener)">registerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; aClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment"><a href="#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)"><code>register(Registration)</code></a> method should be used instead of this method.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">unregister</a><wbr/>(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Unregisters smart listener configurations from the specified type of objects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#unregisterConfig(java.lang.Class,java.util.Collection,java.beans.PropertyChangeListener)">unregisterConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; aClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment"><a href="#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)"><code>unregister(Registration)</code></a> method should be used instead of this method.</div>
</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">
<h3>register</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">register</span><wbr/><span class="parameters">(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</span></div>
<div class="block">Registers smart listener configurations to the specified type objects. Creates smart listeners for
 all existing model elements of the specified type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>registration</code> - registration object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)">
<h3>unregister</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">unregister</span><wbr/><span class="parameters">(<a href="Registration.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">Registration</a> registration)</span></div>
<div class="block">Unregisters smart listener configurations from the specified type of objects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>registration</code> - registration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="registerConfig(java.lang.Class,java.util.Collection,java.beans.PropertyChangeListener)">
<h3>registerConfig</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2022x Refresh1",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type">void</span> <span class="element-name">registerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; aClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment"><a href="#register(com.nomagic.uml2.ext.jmi.smartlistener.Registration)"><code>register(Registration)</code></a> method should be used instead of this method.</div>
</div>
<div class="block">Registers smart listener configurations to the specified type objects. Creates smart listeners for
 all existing model elements of the specified type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aClass</code> - type of objects to that the smart listener configurations must be registered.</dd>
<dd><code>configs</code> - smart listener configurations.</dd>
<dd><code>listener</code> - property change listener that will receive property change events according to specified
                 smart listener configurations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="unregisterConfig(java.lang.Class,java.util.Collection,java.beans.PropertyChangeListener)">
<h3>unregisterConfig</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since()" title="class or interface in java.lang">since</a>="2022x Refresh1",
            <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval()" title="class or interface in java.lang">forRemoval</a>=true)
</span><span class="return-type">void</span> <span class="element-name">unregisterConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;? extends <a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; aClass,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configs,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated, for removal: This API element is subject to removal in a future version.</span>
<div class="deprecation-comment"><a href="#unregister(com.nomagic.uml2.ext.jmi.smartlistener.Registration)"><code>unregister(Registration)</code></a> method should be used instead of this method.</div>
</div>
<div class="block">Unregisters smart listener configurations from the specified type of objects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aClass</code> - type of object.</dd>
<dd><code>configs</code> - smart listener configurations.</dd>
<dd><code>listener</code> - property change listener.</dd>
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
