# JAVA OPENAPI: SmartPropertyChangeListener (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ext/jmi/smartlistener/SmartPropertyChangeListener.html
- source_path: `com/nomagic/uml2/ext/jmi/smartlistener/SmartPropertyChangeListener.html`
- source_sha256: `fd5d5dbf17c041c00b4264495cfeddc096f2c7e03848c7e1240177f70128de36`
- captured_utc: `2026-07-14T16:56:16.468692+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.smartlistener](package-summary.html)

## Class SmartPropertyChangeListener

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeListener

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener`, `com.nomagic.uml2.ext.jmi.NonMaskedPropertyChangeListener`, `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`, `[EventListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html)`

@OpenApiAllpublic classSmartPropertyChangeListener
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements com.nomagic.uml2.ext.jmi.NonMaskedPropertyChangeListener

[`SmartPropertyChangeListener`](SmartPropertyChangeListener.html) is "smarter" than standard [`PropertyChangeListener`](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html),
 because it allows to listen not only to properties of a single model element,
 but also to related model element properties in the model.
 Given a model element, it is possible to listen to changes in the model which occur outside the element.
 These changes are related through a chain of element properties.

General idea: to create a smart listener for an element, you have to pass in a
 collection of smart listener configurations which describe how to reach the changes
 in the model which are of interest to you.

A single configuration contains the element's class and references to other elements
 which are of interest to us (a reference in this case is a property name).

Remark: if you want to listen for a specific property of a single model element without listening to
 properties outside the model element, use [`BaseElement.addPropertyChangeListener(java.beans.PropertyChangeListener)`](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)).

##### Example 1: listen to element owner's name

````java
Element element = ...; // some element

 SmartListenerConfig config = new SmartListenerConfig();
 config.listenTo(PropertyNames.NAME); // listen to element's name
 config.listenToNested(PropertyNames.OWNER).listenTo(PropertyNames.NAME); // listen to element owner's name

 // create the listener
 SmartPropertyChangeListener.createSmartPropertyListener(element, new PropertyChangeListener()
 {
     public void propertyChange(PropertyChangeEvent evt)
     {
         // change event comes here
     }
 }, config);
````

##### Example 2: listen recursively to owner's name and "Is Abstract" property

````java
Element element = ...; // some element

 SmartListenerConfig config = new SmartListenerConfig();
 config.listenTo(PropertyNames.NAME);
 config.listenTo(PropertyNames.IS_ABSTRACT);
 config.listenTo(PropertyNames.OWNER, config);

 SmartPropertyChangeListener.createSmartPropertyListener(element, new PropertyChangeListener()
 {
     public void propertyChange(PropertyChangeEvent evt)
     {
         // change event comes here
     }
 }, config);
````

See Also:
[`SmartListenerConfig`](SmartListenerConfig.html)
[`BaseElement.addPropertyChangeListener(java.beans.PropertyChangeListener)`](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener))

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SMART_LISTENER_PROPAGATION_ID](#SMART_LISTENER_PROPAGATION_ID)`
Constant ID of the property which is used in property names for smart listener events.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[SmartPropertyChangeListener](#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [SmartListenerConfig](SmartListenerConfig.html) configuration)`
Constructs the smart property change listener.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [SmartPropertyChangeListener](SmartPropertyChangeListener.html)`
`[createSmartPropertyListener](#createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [SmartListenerConfig](SmartListenerConfig.html) config)`
Factory method for creating a smart property change listener.
`static [SmartPropertyChangeListener](SmartPropertyChangeListener.html)`
`[createSmartPropertyListener](#createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,java.util.Collection))(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)`
Factory method for creating a smart property change listener.
`static [SmartPropertyChangeListener](SmartPropertyChangeListener.html)`
`[createSmartPropertyListener](#createSmartPropertyListener(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([Element](../../magicdraw/classes/mdkernel/Element.html) target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [SmartListenerConfig](SmartListenerConfig.html) config)`
Factory method for creating a smart property change listener.
`static [SmartPropertyChangeListener](SmartPropertyChangeListener.html)`
`[createSmartPropertyListener](#createSmartPropertyListener(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeListener,java.util.Collection))([Element](../../magicdraw/classes/mdkernel/Element.html) target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)`
Factory method for creating a smart property change listener.
`void`
`[dispose](#dispose())()`
Disposes and cleans up.
`void`
`[eventDeliveryRestored](#eventDeliveryRestored())()`
Notifies the listener that event delivery has been restored
`void`
`[eventDeliveryStopped](#eventDeliveryStopped())()`
Notifies the listener that event delivery has been stopped temporarily.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[getConfig](#getConfig())()`

`[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
`[getListener](#getListener())()`

`com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject`
`[getTarget](#getTarget())()`

`static [SmartListenerConfig](SmartListenerConfig.html)`
`[mergeConfigurations](#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([SmartListenerConfig](SmartListenerConfig.html) c1,
 [SmartListenerConfig](SmartListenerConfig.html) c2)`
Deprecated.
use [`SmartListenerConfig.mergeConfigurations(SmartListenerConfig, SmartListenerConfig)`](SmartListenerConfig.html#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))
`static [SmartListenerConfig](SmartListenerConfig.html)`
`[mergeConfigurations](#mergeConfigurations(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)`
Deprecated.
use [`SmartListenerConfig.mergeConfigurations(Collection)`](SmartListenerConfig.html#mergeConfigurations(java.util.Collection))
`void`
`[propertyChange](#propertyChange(java.beans.PropertyChangeEvent))([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
SMART_LISTENER_PROPAGATION_ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SMART_LISTENER_PROPAGATION_ID
Constant ID of the property which is used in property names for smart listener events.
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeListener.SMART_LISTENER_PROPAGATION_ID)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SmartPropertyChangeListener
protected SmartPropertyChangeListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [SmartListenerConfig](SmartListenerConfig.html) configuration)
Constructs the smart property change listener.
Parameters:
`target` - target to which smart listener is attached.
`listener` - listener to which elements are being delegated.
`configuration` - configuration to apply to the given element.
 ============ METHOD DETAIL ========== 
Method Details
mergeConfigurations
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [SmartListenerConfig](SmartListenerConfig.html) mergeConfigurations([SmartListenerConfig](SmartListenerConfig.html) c1,
 [SmartListenerConfig](SmartListenerConfig.html) c2)
Deprecated.
use [`SmartListenerConfig.mergeConfigurations(SmartListenerConfig, SmartListenerConfig)`](SmartListenerConfig.html#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))
Merges two configurations into a single configuration.
Parameters:
`c1` - first configuration to merge
`c2` - second configuration to merge
Returns:
merged configuration
mergeConfigurations
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [SmartListenerConfig](SmartListenerConfig.html) mergeConfigurations([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)
Deprecated.
use [`SmartListenerConfig.mergeConfigurations(Collection)`](SmartListenerConfig.html#mergeConfigurations(java.util.Collection))
Merges given configurations into a single configuration.
Parameters:
`configurations` - configurations to merge
Returns:
merged configuration
propertyChange
public void propertyChange([PropertyChangeEvent](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html) e)
Specified by:
`[propertyChange](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent))` in interface `[PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html)`
dispose
public void dispose()
Disposes and cleans up.
createSmartPropertyListener
public static [SmartPropertyChangeListener](SmartPropertyChangeListener.html) createSmartPropertyListener([Element](../../magicdraw/classes/mdkernel/Element.html) target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)
Factory method for creating a smart property change listener.
Parameters:
`target` - element to which to attach the listener.
`listener` - wrapped listener to which events should be delegated.
`configurations` - configurations with which to configure the smart listener.
Returns:
created smart property change listener.
createSmartPropertyListener
public static [SmartPropertyChangeListener](SmartPropertyChangeListener.html) createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)
Factory method for creating a smart property change listener.
Parameters:
`target` - target to which to attach the listener.
`listener` - wrapped listener to which events should be delegated.
`configurations` - configurations with which to configure the smart listener.
Returns:
created smart property change listener.
createSmartPropertyListener
public static [SmartPropertyChangeListener](SmartPropertyChangeListener.html) createSmartPropertyListener([Element](../../magicdraw/classes/mdkernel/Element.html) target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [SmartListenerConfig](SmartListenerConfig.html) config)
Factory method for creating a smart property change listener.
Parameters:
`target` - target to which to attach the listener.
`listener` - wrapped listener to which events should be delegated.
`config` - configuration with which to configure the smart listener.
Returns:
created smart property change listener.
createSmartPropertyListener
public static [SmartPropertyChangeListener](SmartPropertyChangeListener.html) createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) listener,
 [SmartListenerConfig](SmartListenerConfig.html) config)
Factory method for creating a smart property change listener.
Parameters:
`target` - target to which to attach the listener.
`listener` - wrapped listener to which events should be delegated.
`config` - configuration with which to configure the smart listener.
Returns:
created smart property change listener.
getConfig
public [SmartListenerConfig](SmartListenerConfig.html) getConfig()
getTarget
public com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject getTarget()
getListener
public [PropertyChangeListener](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html) getListener()
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
eventDeliveryStopped
public void eventDeliveryStopped()
Description copied from interface: `com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener`
Notifies the listener that event delivery has been stopped temporarily.
 Changes may take place before event delivery is restored but events will
 not be delivered for these changes
Specified by:
`eventDeliveryStopped` in interface `com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener`
eventDeliveryRestored
public void eventDeliveryRestored()
Description copied from interface: `com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener`
Notifies the listener that event delivery has been restored
Specified by:
`eventDeliveryRestored` in interface `com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.smartlistener</a></div>
<h1 class="title" title="Class SmartPropertyChangeListener">Class SmartPropertyChangeListener</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeListener</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener</code>, <code>com.nomagic.uml2.ext.jmi.NonMaskedPropertyChangeListener</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/EventListener.html" title="class or interface in java.util">EventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SmartPropertyChangeListener</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements com.nomagic.uml2.ext.jmi.NonMaskedPropertyChangeListener</span></div>
<div class="block"><p>
<a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartPropertyChangeListener</code></a> is "smarter" than standard <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans"><code>PropertyChangeListener</code></a>,
 because it allows to listen not only to properties of a single model element,
 but also to related model element properties in the model.
 Given a model element, it is possible to listen to changes in the model which occur outside the element.
 These changes are related through a chain of element properties.
 </p>
<p>
 General idea: to create a smart listener for an element, you have to pass in a
 collection of smart listener configurations which describe how to reach the changes
 in the model which are of interest to you.
 </p>
<p>
 A single configuration contains the element's class and references to other elements
 which are of interest to us (a reference in this case is a property name).
 </p>
<p>
 Remark: if you want to listen for a specific property of a single model element without listening to
 properties outside the model element, use <a href="../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)"><code>BaseElement.addPropertyChangeListener(java.beans.PropertyChangeListener)</code></a>.
 </p>
<h4>Example 1: listen to element owner's name</h4>
<pre>
 Element element = ...; // some element

 SmartListenerConfig config = new SmartListenerConfig();
 config.listenTo(PropertyNames.NAME); // listen to element's name
 config.listenToNested(PropertyNames.OWNER).listenTo(PropertyNames.NAME); // listen to element owner's name

 // create the listener
 SmartPropertyChangeListener.createSmartPropertyListener(element, new PropertyChangeListener()
 {
     public void propertyChange(PropertyChangeEvent evt)
     {
         // change event comes here
     }
 }, config);
 </pre>
<h4>Example 2: listen recursively to owner's name and "Is Abstract" property</h4>
<pre>
 Element element = ...; // some element

 SmartListenerConfig config = new SmartListenerConfig();
 config.listenTo(PropertyNames.NAME);
 config.listenTo(PropertyNames.IS_ABSTRACT);
 config.listenTo(PropertyNames.OWNER, config);

 SmartPropertyChangeListener.createSmartPropertyListener(element, new PropertyChangeListener()
 {
     public void propertyChange(PropertyChangeEvent evt)
     {
         // change event comes here
     }
 }, config);
 </pre></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartListenerConfig</code></a></li>
<li><a href="../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener)"><code>BaseElement.addPropertyChangeListener(java.beans.PropertyChangeListener)</code></a></li>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SMART_LISTENER_PROPAGATION_ID">SMART_LISTENER_PROPAGATION_ID</a></code></div>
<div class="col-last even-row-color">
<div class="block">Constant ID of the property which is used in property names for smart listener events.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">SmartPropertyChangeListener</a><wbr/>(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> configuration)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs the smart property change listener.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">createSmartPropertyListener</a><wbr/>(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Factory method for creating a smart property change listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,java.util.Collection)">createSmartPropertyListener</a><wbr/>(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Factory method for creating a smart property change listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartPropertyListener(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">createSmartPropertyListener</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Factory method for creating a smart property change listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createSmartPropertyListener(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeListener,java.util.Collection)">createSmartPropertyListener</a><wbr/>(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Factory method for creating a smart property change listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dispose()">dispose</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disposes and cleans up.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eventDeliveryRestored()">eventDeliveryRestored</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies the listener that event delivery has been restored</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eventDeliveryStopped()">eventDeliveryStopped</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Notifies the listener that event delivery has been stopped temporarily.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConfig()">getConfig</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getListener()">getListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTarget()">getTarget</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">mergeConfigurations</a><wbr/>(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c1,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="SmartListenerConfig.html#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)"><code>SmartListenerConfig.mergeConfigurations(SmartListenerConfig, SmartListenerConfig)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#mergeConfigurations(java.util.Collection)">mergeConfigurations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="SmartListenerConfig.html#mergeConfigurations(java.util.Collection)"><code>SmartListenerConfig.mergeConfigurations(Collection)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#propertyChange(java.beans.PropertyChangeEvent)">propertyChange</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="SMART_LISTENER_PROPAGATION_ID">
<h3>SMART_LISTENER_PROPAGATION_ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SMART_LISTENER_PROPAGATION_ID</span></div>
<div class="block">Constant ID of the property which is used in property names for smart listener events.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.uml2.ext.jmi.smartlistener.SmartPropertyChangeListener.SMART_LISTENER_PROPAGATION_ID">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>SmartPropertyChangeListener</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">SmartPropertyChangeListener</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> configuration)</span></div>
<div class="block">Constructs the smart property change listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target to which smart listener is attached.</dd>
<dd><code>listener</code> - listener to which elements are being delegated.</dd>
<dd><code>configuration</code> - configuration to apply to the given element.</dd>
</dl>
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
<section class="detail" id="mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>mergeConfigurations</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">mergeConfigurations</span><wbr/><span class="parameters">(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c1,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c2)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="SmartListenerConfig.html#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)"><code>SmartListenerConfig.mergeConfigurations(SmartListenerConfig, SmartListenerConfig)</code></a></div>
</div>
<div class="block">Merges two configurations into a single configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>c1</code> - first configuration to merge</dd>
<dd><code>c2</code> - second configuration to merge</dd>
<dt>Returns:</dt>
<dd>merged configuration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mergeConfigurations(java.util.Collection)">
<h3>mergeConfigurations</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">mergeConfigurations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="SmartListenerConfig.html#mergeConfigurations(java.util.Collection)"><code>SmartListenerConfig.mergeConfigurations(Collection)</code></a></div>
</div>
<div class="block">Merges given configurations into a single configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurations</code> - configurations to merge</dd>
<dt>Returns:</dt>
<dd>merged configuration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="propertyChange(java.beans.PropertyChangeEvent)">
<h3>propertyChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">propertyChange</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeEvent.html" title="class or interface in java.beans">PropertyChangeEvent</a> e)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)" title="class or interface in java.beans">propertyChange</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block">Disposes and cleans up.</div>
</section>
</li>
<li>
<section class="detail" id="createSmartPropertyListener(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeListener,java.util.Collection)">
<h3>createSmartPropertyListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></span> <span class="element-name">createSmartPropertyListener</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<div class="block">Factory method for creating a smart property change listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - element to which to attach the listener.</dd>
<dd><code>listener</code> - wrapped listener to which events should be delegated.</dd>
<dd><code>configurations</code> - configurations with which to configure the smart listener.</dd>
<dt>Returns:</dt>
<dd>created smart property change listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,java.util.Collection)">
<h3>createSmartPropertyListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></span> <span class="element-name">createSmartPropertyListener</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
<div class="block">Factory method for creating a smart property change listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target to which to attach the listener.</dd>
<dd><code>listener</code> - wrapped listener to which events should be delegated.</dd>
<dd><code>configurations</code> - configurations with which to configure the smart listener.</dd>
<dt>Returns:</dt>
<dd>created smart property change listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartPropertyListener(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>createSmartPropertyListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></span> <span class="element-name">createSmartPropertyListener</span><wbr/><span class="parameters">(<a href="../../magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="block">Factory method for creating a smart property change listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target to which to attach the listener.</dd>
<dd><code>listener</code> - wrapped listener to which events should be delegated.</dd>
<dd><code>config</code> - configuration with which to configure the smart listener.</dd>
<dt>Returns:</dt>
<dd>created smart property change listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSmartPropertyListener(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject,java.beans.PropertyChangeListener,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>createSmartPropertyListener</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartPropertyChangeListener</a></span> <span class="element-name">createSmartPropertyListener</span><wbr/><span class="parameters">(com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> listener,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="block">Factory method for creating a smart property change listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - target to which to attach the listener.</dd>
<dd><code>listener</code> - wrapped listener to which events should be delegated.</dd>
<dd><code>config</code> - configuration with which to configure the smart listener.</dd>
<dt>Returns:</dt>
<dd>created smart property change listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConfig()">
<h3>getConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">getConfig</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTarget()">
<h3>getTarget</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.uml2.ext.jmi.reflect.AbstractRefObject</span> <span class="element-name">getTarget</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getListener()">
<h3>getListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a></span> <span class="element-name">getListener</span>()</div>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eventDeliveryStopped()">
<h3>eventDeliveryStopped</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">eventDeliveryStopped</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener</code></span></div>
<div class="block">Notifies the listener that event delivery has been stopped temporarily.
 Changes may take place before event delivery is restored but events will
 not be delivered for these changes</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>eventDeliveryStopped</code> in interface <code>com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eventDeliveryRestored()">
<h3>eventDeliveryRestored</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">eventDeliveryRestored</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code>com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener</code></span></div>
<div class="block">Notifies the listener that event delivery has been restored</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>eventDeliveryRestored</code> in interface <code>com.dassault_systemes.modeler.foundation.events.NonMaskedPropertyChangeListener</code></dd>
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
