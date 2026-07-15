# JAVA OPENAPI: SmartListenerConfig (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/uml2/ext/jmi/smartlistener/SmartListenerConfig.html
- source_path: `com/nomagic/uml2/ext/jmi/smartlistener/SmartListenerConfig.html`
- source_sha256: `4e9909854117e78d32e664eed1004e98ec5dbf4a80652c8b40ef91ce4b4d2f93`
- captured_utc: `2026-07-14T16:58:47.333401+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2.ext.jmi.smartlistener](package-summary.html)

## Class SmartListenerConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig

@OpenApiAllpublic classSmartListenerConfig
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Smart listener configuration describes how to reach a specific property in the model from a given model element.
 Smart listener uses the configuration to create a chain of properties through which listener events map.
This class also contains predefined smart listener configurations which can be widely reused.
 Reusable smart listener configurations cannot be modified.

See Also:
[`SmartPropertyChangeListener`](SmartPropertyChangeListener.html)
[`BaseElement.addPropertyChangeListener(java.beans.PropertyChangeListener)`](../../../../magicdraw/uml/BaseElement.html#addPropertyChangeListener(java.beans.PropertyChangeListener))

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG](#APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG)`
Listens to applied stereotypes and tagged values values.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[APPLIED_STEREOTYPE_CONFIG](#APPLIED_STEREOTYPE_CONFIG)`
Listen to the applied stereotype.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG](#APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG)`
Listens to applied stereotype's name, tagged value values and tag definition properties.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[APPLIED_STEREOTYPE_NAME_CONFIG](#APPLIED_STEREOTYPE_NAME_CONFIG)`
Listen to the applied stereotype's name.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG](#APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG)`
Listens to applied stereotype (name and icon), tagged values (value and names of values), tag definition's name.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG](#APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG)`
Listens to applied stereotype (name and icon), tagged values values.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[APPLIED_STEREOTYPE_NAME_ICON_CONFIG](#APPLIED_STEREOTYPE_NAME_ICON_CONFIG)`
Listen to the applied stereotype's name and icon
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[COMBINED_FRAGMENT_CONFIG](#COMBINED_FRAGMENT_CONFIG)`
Listens to combined fragment.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[CONVEYED_INFORMATION_CONFIG](#CONVEYED_INFORMATION_CONFIG)`
Listens to conveyed information.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[DIAGRAM_CONTEXT_CONFIG](#DIAGRAM_CONTEXT_CONFIG)`
Listens to diagram context.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[DOCUMENTATION_CONFIG](#DOCUMENTATION_CONFIG)`
Listen to the documentation of the element.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[EMPTY_CONFIG](#EMPTY_CONFIG)`
Configuration that does not listen to any properties
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[INSTANCE_SLOT_VALUE_CONFIG](#INSTANCE_SLOT_VALUE_CONFIG)`
Listen to properties of Slot of InstanceSpecification.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[MESSAGE_CONFIG](#MESSAGE_CONFIG)`
Listens to the message.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[MESSAGE_SIGNATURE_CONFIG](#MESSAGE_SIGNATURE_CONFIG)`
Listens to message signature.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[MULTIPLICITY_CONFIG](#MULTIPLICITY_CONFIG)`
Listens to the multiplicity.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[NAME_CONFIG](#NAME_CONFIG)`
Listen to the name of the element.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[PARAMETER_SUBSTITUTION_CONFIG](#PARAMETER_SUBSTITUTION_CONFIG)`
Listens to parameter substitution.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[QUALIFIED_NAME_CONFIG](#QUALIFIED_NAME_CONFIG)`
Listen to the qualified name of the element.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[SLOT_VALUE_CONFIG](#SLOT_VALUE_CONFIG)`
Listen to the value of Slot.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[STEREOTYPE_METACLASS_CONFIG](#STEREOTYPE_METACLASS_CONFIG)`
Listen to the metaclass of Stereotype.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[TAGGED_VALUE_DEEP_CONFIG](#TAGGED_VALUE_DEEP_CONFIG)`
Listens to applied tagged values properties.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[TAGGED_VALUE_SHALLOW_CONFIG](#TAGGED_VALUE_SHALLOW_CONFIG)`
Listens to applied tagged values values.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[TRANSITION_CONFIG](#TRANSITION_CONFIG)`
Listens to transition.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[TRIGGER_CONFIG](#TRIGGER_CONFIG)`
Listens to trigger.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[VALUE_OF_TAGGED_VALUE_CONFIG](#VALUE_OF_TAGGED_VALUE_CONFIG)`
Listen to the properties of values of TaggedValue.
`static final [SmartListenerConfig](SmartListenerConfig.html)`
`[VALUE_SPECIFICATION_CONFIG](#VALUE_SPECIFICATION_CONFIG)`
Listen to properties of ValueSpecification.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[SmartListenerConfig](#%3Cinit%3E())()`
Constructs empty configuration.
`[SmartListenerConfig](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Constructs the configuration with a property name.
`[SmartListenerConfig](#%3Cinit%3E(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [SmartListenerConfig](SmartListenerConfig.html) config)`
Constructs the configuration.
`[SmartListenerConfig](#%3Cinit%3E(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[SmartListenerConfig](SmartListenerConfig.html)> references)`
Constructs the configuration.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[copy](#copy(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([SmartListenerConfig](SmartListenerConfig.html) config)`
Makes a shallow copy of the passed config to this config.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[deepCopy](#deepCopy())()`
Creates a deep copy of the specified smart listener config.
`void`
`[deepCopy](#deepCopy(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([SmartListenerConfig](SmartListenerConfig.html) config)`
Deep copies a passed config to this config.
`void`
`[dump](#dump())()`
Dumps property configuration to the standard output.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[getPropertyConfig](#getPropertyConfig(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Gets property config which is used for a particular property.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[SmartListenerConfig](SmartListenerConfig.html)>`
`[getReferences](#getReferences())()`
Gets references of this configuration.
`static void`
`[initValueSpecificationConfig](#initValueSpecificationConfig(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([SmartListenerConfig](SmartListenerConfig.html) valueSpecificationConfig,
 [SmartListenerConfig](SmartListenerConfig.html) elementAsValueConfig)`
Initializes value specification config.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[listenTo](#listenTo(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([SmartListenerConfig](SmartListenerConfig.html) config)`
Merges information from given config.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[listenTo](#listenTo(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Listens to a given property name.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[listenTo](#listenTo(java.lang.String...))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)... propertyNames)`
Listens to given properties' names.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[listenTo](#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) referenceName,
 [SmartListenerConfig](SmartListenerConfig.html) config)`
Listens to a given property and passes a smart listener configuration for it to
 apply if references are found among property values.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[listenTo](#listenTo(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)`
Listens to given properties' names.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[listenTo2](#listenTo2(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) referenceName,
 [SmartListenerConfig](SmartListenerConfig.html) config)`
Deprecated.
use [`listenTo(String, SmartListenerConfig)`](#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)), because it merges configs too.
`[SmartListenerConfig](SmartListenerConfig.html)`
`[listenToNested](#listenToNested(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Listens to a nested property configuration.
`void`
`[makeUnmodifiable](#makeUnmodifiable())()`
Make config unmodifiable.
`static [SmartListenerConfig](SmartListenerConfig.html)`
`[mergeConfigurations](#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))([SmartListenerConfig](SmartListenerConfig.html) c1,
 [SmartListenerConfig](SmartListenerConfig.html) c2)`
Merges two configurations into a single configuration.
`static [SmartListenerConfig](SmartListenerConfig.html)`
`[mergeConfigurations](#mergeConfigurations(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)`
Merges given configurations into a single configuration.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
NAME_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) NAME_CONFIG
Listen to the name of the element.
DOCUMENTATION_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) DOCUMENTATION_CONFIG
Listen to the documentation of the element.
QUALIFIED_NAME_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) QUALIFIED_NAME_CONFIG
Listen to the qualified name of the element.
VALUE_SPECIFICATION_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) VALUE_SPECIFICATION_CONFIG
Listen to properties of ValueSpecification.
SLOT_VALUE_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) SLOT_VALUE_CONFIG
Listen to the value of Slot.
INSTANCE_SLOT_VALUE_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) INSTANCE_SLOT_VALUE_CONFIG
Listen to properties of Slot of InstanceSpecification.
STEREOTYPE_METACLASS_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) STEREOTYPE_METACLASS_CONFIG
Listen to the metaclass of Stereotype.
APPLIED_STEREOTYPE_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) APPLIED_STEREOTYPE_CONFIG
Listen to the applied stereotype.
APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG
Listens to applied stereotypes and tagged values values.
APPLIED_STEREOTYPE_NAME_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) APPLIED_STEREOTYPE_NAME_CONFIG
Listen to the applied stereotype's name.
APPLIED_STEREOTYPE_NAME_ICON_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) APPLIED_STEREOTYPE_NAME_ICON_CONFIG
Listen to the applied stereotype's name and icon
APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG
Listens to applied stereotype's name, tagged value values and tag definition properties.
APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG
Listens to applied stereotype (name and icon), tagged values (value and names of values), tag definition's name.
APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG
Listens to applied stereotype (name and icon), tagged values values. Does not listen deeper (properties of values).
TAGGED_VALUE_SHALLOW_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) TAGGED_VALUE_SHALLOW_CONFIG
Listens to applied tagged values values. Does not listen deeper (properties of values).
TAGGED_VALUE_DEEP_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) TAGGED_VALUE_DEEP_CONFIG
Listens to applied tagged values properties.
VALUE_OF_TAGGED_VALUE_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) VALUE_OF_TAGGED_VALUE_CONFIG
Listen to the properties of values of TaggedValue.
PARAMETER_SUBSTITUTION_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) PARAMETER_SUBSTITUTION_CONFIG
Listens to parameter substitution.
TRIGGER_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) TRIGGER_CONFIG
Listens to trigger.
TRANSITION_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) TRANSITION_CONFIG
Listens to transition.
MESSAGE_SIGNATURE_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) MESSAGE_SIGNATURE_CONFIG
Listens to message signature.
MESSAGE_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) MESSAGE_CONFIG
Listens to the message.
COMBINED_FRAGMENT_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) COMBINED_FRAGMENT_CONFIG
Listens to combined fragment.
CONVEYED_INFORMATION_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) CONVEYED_INFORMATION_CONFIG
Listens to conveyed information.
DIAGRAM_CONTEXT_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) DIAGRAM_CONTEXT_CONFIG
Listens to diagram context.
MULTIPLICITY_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) MULTIPLICITY_CONFIG
Listens to the multiplicity.
EMPTY_CONFIG
public static final [SmartListenerConfig](SmartListenerConfig.html) EMPTY_CONFIG
Configuration that does not listen to any properties
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
SmartListenerConfig
public SmartListenerConfig()
Constructs empty configuration.
SmartListenerConfig
public SmartListenerConfig([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Constructs the configuration with a property name.
Parameters:
`propertyName` - property name to use as a reference
See Also:
[`listenTo(String)`](#listenTo(java.lang.String))
SmartListenerConfig
public SmartListenerConfig([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName,
 [SmartListenerConfig](SmartListenerConfig.html) config)
Constructs the configuration.
Parameters:
`propertyName` - property name to use as a reference
`config` - config to use with a property reference
See Also:
[`listenTo(String, SmartListenerConfig)`](#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig))
SmartListenerConfig
public SmartListenerConfig([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[SmartListenerConfig](SmartListenerConfig.html)> references)
Constructs the configuration.
Parameters:
`references` - map of references to use
 ============ METHOD DETAIL ========== 
Method Details
initValueSpecificationConfig
public static void initValueSpecificationConfig([SmartListenerConfig](SmartListenerConfig.html) valueSpecificationConfig,
 [SmartListenerConfig](SmartListenerConfig.html) elementAsValueConfig)
Initializes value specification config.
Parameters:
`valueSpecificationConfig` - config to initialize.
`elementAsValueConfig` - element config to use.
makeUnmodifiable
public void makeUnmodifiable()
Make config unmodifiable.
 This means that new references can not be added or existing can not be changed.
 Any attempt to change unmodifiable config will end up with runtime exception.
copy
public void copy([SmartListenerConfig](SmartListenerConfig.html) config)
Makes a shallow copy of the passed config to this config.
 Instances of configs in the tree are reused and not re-created.
Parameters:
`config` - passed configuration for copying.
deepCopy
public void deepCopy([SmartListenerConfig](SmartListenerConfig.html) config)
Deep copies a passed config to this config.
 Whole config tree is copied by recreating referenced config instances.
Parameters:
`config` - config to copy
deepCopy
public [SmartListenerConfig](SmartListenerConfig.html) deepCopy()
Creates a deep copy of the specified smart listener config.
Returns:
copy
getReferences
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[SmartListenerConfig](SmartListenerConfig.html)> getReferences()
Gets references of this configuration.
Returns:
references of this configuration
getPropertyConfig
public [SmartListenerConfig](SmartListenerConfig.html) getPropertyConfig([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Gets property config which is used for a particular property.
Parameters:
`propertyName` - property for which to get property config
Returns:
property config for a given property
listenTo
public [SmartListenerConfig](SmartListenerConfig.html) listenTo([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) referenceName,
 @CheckForNull
 [SmartListenerConfig](SmartListenerConfig.html) config)
Listens to a given property and passes a smart listener configuration for it to
 apply if references are found among property values.
Parameters:
`referenceName` - property name for which configuration should be applied.
`config` - passed configuration for the property. If for a given property an existing
 configuration is found, the two configurations will be merged and the merged
 configuration will be stored.
Returns:
self or a merged config if the configurations had to be merged
listenTo2
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [SmartListenerConfig](SmartListenerConfig.html) listenTo2([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) referenceName,
 [SmartListenerConfig](SmartListenerConfig.html) config)
Deprecated.
use [`listenTo(String, SmartListenerConfig)`](#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)), because it merges configs too.
Makes the same thing as [`listenTo(String, SmartListenerConfig)`](#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)).
 Only if founds already registered property
 doesn't emit warning, but makes merge with already registered configuration. If configurations are merged, then
 passed `config` VALUE is replaced with a contents of merge result.
Parameters:
`referenceName` - property name for which configuration is applicable
`config` - passed configuration. It's VALUE will be edited if another configuration will be found already
 registered by given reference name. VALUE of passed reference will be changed to the merged one
Returns:
self or a merged config if the configurations had to be merged
listenTo
public [SmartListenerConfig](SmartListenerConfig.html) listenTo([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Listens to a given property name.
Parameters:
`propertyName` - property name ot listen to.
Returns:
self or a merged config if the configurations had to be merged
listenTo
public [SmartListenerConfig](SmartListenerConfig.html) listenTo([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)
Listens to given properties' names.
Parameters:
`propertyNames` - properties' names to listen to
Returns:
self
listenTo
public [SmartListenerConfig](SmartListenerConfig.html) listenTo([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)... propertyNames)
Listens to given properties' names.
Parameters:
`propertyNames` - properties' names to listen to
Returns:
self
listenToNested
public [SmartListenerConfig](SmartListenerConfig.html) listenToNested([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Listens to a nested property configuration.
Parameters:
`propertyName` - property name to listen to.
Returns:
property config of a given property, allows performing nested calls.
listenTo
public [SmartListenerConfig](SmartListenerConfig.html) listenTo([SmartListenerConfig](SmartListenerConfig.html) config)
Merges information from given config.
Parameters:
`config` - config
Returns:
self
mergeConfigurations
public static [SmartListenerConfig](SmartListenerConfig.html) mergeConfigurations([SmartListenerConfig](SmartListenerConfig.html) c1,
 [SmartListenerConfig](SmartListenerConfig.html) c2)
Merges two configurations into a single configuration.
Parameters:
`c1` - first configuration to merge.
`c2` - second configuration to merge.
Returns:
merged configuration.
mergeConfigurations
public static [SmartListenerConfig](SmartListenerConfig.html) mergeConfigurations([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[SmartListenerConfig](SmartListenerConfig.html)> configurations)
Merges given configurations into a single configuration.
Parameters:
`configurations` - configurations to merge
Returns:
merged configuration
dump
public void dump()
Dumps property configuration to the standard output.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2.ext.jmi.smartlistener</a></div>
<h1 class="title" title="Class SmartListenerConfig">Class SmartListenerConfig</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SmartListenerConfig</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 Smart listener configuration describes how to reach a specific property in the model from a given model element.
 Smart listener uses the configuration to create a chain of properties through which listener events map.
 </p>
<p>
 This class also contains predefined smart listener configurations which can be widely reused.
 Reusable smart listener configurations cannot be modified.
 </p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="SmartPropertyChangeListener.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener"><code>SmartPropertyChangeListener</code></a></li>
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
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG">APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listens to applied stereotypes and tagged values values.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#APPLIED_STEREOTYPE_CONFIG">APPLIED_STEREOTYPE_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listen to the applied stereotype.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG">APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listens to applied stereotype's name, tagged value values and tag definition properties.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#APPLIED_STEREOTYPE_NAME_CONFIG">APPLIED_STEREOTYPE_NAME_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listen to the applied stereotype's name.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG">APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listens to applied stereotype (name and icon), tagged values (value and names of values), tag definition's name.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG">APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to applied stereotype (name and icon), tagged values values.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#APPLIED_STEREOTYPE_NAME_ICON_CONFIG">APPLIED_STEREOTYPE_NAME_ICON_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listen to the applied stereotype's name and icon</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#COMBINED_FRAGMENT_CONFIG">COMBINED_FRAGMENT_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to combined fragment.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONVEYED_INFORMATION_CONFIG">CONVEYED_INFORMATION_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listens to conveyed information.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DIAGRAM_CONTEXT_CONFIG">DIAGRAM_CONTEXT_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to diagram context.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DOCUMENTATION_CONFIG">DOCUMENTATION_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listen to the documentation of the element.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EMPTY_CONFIG">EMPTY_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Configuration that does not listen to any properties</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INSTANCE_SLOT_VALUE_CONFIG">INSTANCE_SLOT_VALUE_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listen to properties of Slot of InstanceSpecification.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MESSAGE_CONFIG">MESSAGE_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to the message.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#MESSAGE_SIGNATURE_CONFIG">MESSAGE_SIGNATURE_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listens to message signature.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MULTIPLICITY_CONFIG">MULTIPLICITY_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to the multiplicity.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NAME_CONFIG">NAME_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listen to the name of the element.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PARAMETER_SUBSTITUTION_CONFIG">PARAMETER_SUBSTITUTION_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to parameter substitution.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#QUALIFIED_NAME_CONFIG">QUALIFIED_NAME_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listen to the qualified name of the element.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SLOT_VALUE_CONFIG">SLOT_VALUE_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listen to the value of Slot.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STEREOTYPE_METACLASS_CONFIG">STEREOTYPE_METACLASS_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listen to the metaclass of Stereotype.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TAGGED_VALUE_DEEP_CONFIG">TAGGED_VALUE_DEEP_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to applied tagged values properties.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TAGGED_VALUE_SHALLOW_CONFIG">TAGGED_VALUE_SHALLOW_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listens to applied tagged values values.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TRANSITION_CONFIG">TRANSITION_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listens to transition.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRIGGER_CONFIG">TRIGGER_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listens to trigger.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VALUE_OF_TAGGED_VALUE_CONFIG">VALUE_OF_TAGGED_VALUE_CONFIG</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Listen to the properties of values of TaggedValue.</div>
</div>
<div class="col-first even-row-color"><code>static final <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUE_SPECIFICATION_CONFIG">VALUE_SPECIFICATION_CONFIG</a></code></div>
<div class="col-last even-row-color">
<div class="block">Listen to properties of ValueSpecification.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">SmartListenerConfig</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs empty configuration.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">SmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs the configuration with a property name.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">SmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs the configuration.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Map)">SmartListenerConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; references)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs the configuration.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">copy</a><wbr/>(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Makes a shallow copy of the passed config to this config.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deepCopy()">deepCopy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a deep copy of the specified smart listener config.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#deepCopy(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">deepCopy</a><wbr/>(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Deep copies a passed config to this config.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#dump()">dump</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Dumps property configuration to the standard output.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyConfig(java.lang.String)">getPropertyConfig</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets property config which is used for a particular property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReferences()">getReferences</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets references of this configuration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#initValueSpecificationConfig(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">initValueSpecificationConfig</a><wbr/>(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> valueSpecificationConfig,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> elementAsValueConfig)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Initializes value specification config.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#listenTo(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">listenTo</a><wbr/>(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Merges information from given config.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#listenTo(java.lang.String)">listenTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens to a given property name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#listenTo(java.lang.String...)">listenTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... propertyNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens to given properties' names.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">listenTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceName,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens to a given property and passes a smart listener configuration for it to
 apply if references are found among property values.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#listenTo(java.util.Collection)">listenTo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens to given properties' names.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#listenTo2(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">listenTo2</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceName,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)"><code>listenTo(String, SmartListenerConfig)</code></a>, because it merges configs too.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#listenToNested(java.lang.String)">listenToNested</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Listens to a nested property configuration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#makeUnmodifiable()">makeUnmodifiable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Make config unmodifiable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">mergeConfigurations</a><wbr/>(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c1,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Merges two configurations into a single configuration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeConfigurations(java.util.Collection)">mergeConfigurations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Merges given configurations into a single configuration.</div>
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
<section class="detail" id="NAME_CONFIG">
<h3>NAME_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">NAME_CONFIG</span></div>
<div class="block">Listen to the name of the element.</div>
</section>
</li>
<li>
<section class="detail" id="DOCUMENTATION_CONFIG">
<h3>DOCUMENTATION_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">DOCUMENTATION_CONFIG</span></div>
<div class="block">Listen to the documentation of the element.</div>
</section>
</li>
<li>
<section class="detail" id="QUALIFIED_NAME_CONFIG">
<h3>QUALIFIED_NAME_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">QUALIFIED_NAME_CONFIG</span></div>
<div class="block">Listen to the qualified name of the element.</div>
</section>
</li>
<li>
<section class="detail" id="VALUE_SPECIFICATION_CONFIG">
<h3>VALUE_SPECIFICATION_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">VALUE_SPECIFICATION_CONFIG</span></div>
<div class="block">Listen to properties of ValueSpecification.</div>
</section>
</li>
<li>
<section class="detail" id="SLOT_VALUE_CONFIG">
<h3>SLOT_VALUE_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">SLOT_VALUE_CONFIG</span></div>
<div class="block">Listen to the value of Slot.</div>
</section>
</li>
<li>
<section class="detail" id="INSTANCE_SLOT_VALUE_CONFIG">
<h3>INSTANCE_SLOT_VALUE_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">INSTANCE_SLOT_VALUE_CONFIG</span></div>
<div class="block">Listen to properties of Slot of InstanceSpecification.</div>
</section>
</li>
<li>
<section class="detail" id="STEREOTYPE_METACLASS_CONFIG">
<h3>STEREOTYPE_METACLASS_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">STEREOTYPE_METACLASS_CONFIG</span></div>
<div class="block">Listen to the metaclass of Stereotype.</div>
</section>
</li>
<li>
<section class="detail" id="APPLIED_STEREOTYPE_CONFIG">
<h3>APPLIED_STEREOTYPE_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">APPLIED_STEREOTYPE_CONFIG</span></div>
<div class="block">Listen to the applied stereotype.</div>
</section>
</li>
<li>
<section class="detail" id="APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG">
<h3>APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">APPLIED_STEREOTYPE_AND_TAGGED_VALUE_SHALLOW_CONFIG</span></div>
<div class="block">Listens to applied stereotypes and tagged values values.</div>
</section>
</li>
<li>
<section class="detail" id="APPLIED_STEREOTYPE_NAME_CONFIG">
<h3>APPLIED_STEREOTYPE_NAME_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">APPLIED_STEREOTYPE_NAME_CONFIG</span></div>
<div class="block">Listen to the applied stereotype's name.</div>
</section>
</li>
<li>
<section class="detail" id="APPLIED_STEREOTYPE_NAME_ICON_CONFIG">
<h3>APPLIED_STEREOTYPE_NAME_ICON_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">APPLIED_STEREOTYPE_NAME_ICON_CONFIG</span></div>
<div class="block">Listen to the applied stereotype's name and icon</div>
</section>
</li>
<li>
<section class="detail" id="APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG">
<h3>APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">APPLIED_STEREOTYPE_NAME_AND_TAGGED_VALUE_DEEP_CONFIG</span></div>
<div class="block">Listens to applied stereotype's name, tagged value values and tag definition properties.</div>
</section>
</li>
<li>
<section class="detail" id="APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG">
<h3>APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_DEEP_CONFIG</span></div>
<div class="block">Listens to applied stereotype (name and icon), tagged values (value and names of values), tag definition's name.</div>
</section>
</li>
<li>
<section class="detail" id="APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG">
<h3>APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">APPLIED_STEREOTYPE_NAME_ICON_AND_TAGGED_VALUE_SHALLOW_CONFIG</span></div>
<div class="block">Listens to applied stereotype (name and icon), tagged values values. Does not listen deeper (properties of values).</div>
</section>
</li>
<li>
<section class="detail" id="TAGGED_VALUE_SHALLOW_CONFIG">
<h3>TAGGED_VALUE_SHALLOW_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">TAGGED_VALUE_SHALLOW_CONFIG</span></div>
<div class="block">Listens to applied tagged values values. Does not listen deeper (properties of values).</div>
</section>
</li>
<li>
<section class="detail" id="TAGGED_VALUE_DEEP_CONFIG">
<h3>TAGGED_VALUE_DEEP_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">TAGGED_VALUE_DEEP_CONFIG</span></div>
<div class="block">Listens to applied tagged values properties.</div>
</section>
</li>
<li>
<section class="detail" id="VALUE_OF_TAGGED_VALUE_CONFIG">
<h3>VALUE_OF_TAGGED_VALUE_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">VALUE_OF_TAGGED_VALUE_CONFIG</span></div>
<div class="block">Listen to the properties of values of TaggedValue.</div>
</section>
</li>
<li>
<section class="detail" id="PARAMETER_SUBSTITUTION_CONFIG">
<h3>PARAMETER_SUBSTITUTION_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">PARAMETER_SUBSTITUTION_CONFIG</span></div>
<div class="block">Listens to parameter substitution.</div>
</section>
</li>
<li>
<section class="detail" id="TRIGGER_CONFIG">
<h3>TRIGGER_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">TRIGGER_CONFIG</span></div>
<div class="block">Listens to trigger.</div>
</section>
</li>
<li>
<section class="detail" id="TRANSITION_CONFIG">
<h3>TRANSITION_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">TRANSITION_CONFIG</span></div>
<div class="block">Listens to transition.</div>
</section>
</li>
<li>
<section class="detail" id="MESSAGE_SIGNATURE_CONFIG">
<h3>MESSAGE_SIGNATURE_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">MESSAGE_SIGNATURE_CONFIG</span></div>
<div class="block">Listens to message signature.</div>
</section>
</li>
<li>
<section class="detail" id="MESSAGE_CONFIG">
<h3>MESSAGE_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">MESSAGE_CONFIG</span></div>
<div class="block">Listens to the message.</div>
</section>
</li>
<li>
<section class="detail" id="COMBINED_FRAGMENT_CONFIG">
<h3>COMBINED_FRAGMENT_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">COMBINED_FRAGMENT_CONFIG</span></div>
<div class="block">Listens to combined fragment.</div>
</section>
</li>
<li>
<section class="detail" id="CONVEYED_INFORMATION_CONFIG">
<h3>CONVEYED_INFORMATION_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">CONVEYED_INFORMATION_CONFIG</span></div>
<div class="block">Listens to conveyed information.</div>
</section>
</li>
<li>
<section class="detail" id="DIAGRAM_CONTEXT_CONFIG">
<h3>DIAGRAM_CONTEXT_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">DIAGRAM_CONTEXT_CONFIG</span></div>
<div class="block">Listens to diagram context.</div>
</section>
</li>
<li>
<section class="detail" id="MULTIPLICITY_CONFIG">
<h3>MULTIPLICITY_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">MULTIPLICITY_CONFIG</span></div>
<div class="block">Listens to the multiplicity.</div>
</section>
</li>
<li>
<section class="detail" id="EMPTY_CONFIG">
<h3>EMPTY_CONFIG</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">EMPTY_CONFIG</span></div>
<div class="block">Configuration that does not listen to any properties</div>
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
<h3>SmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SmartListenerConfig</span>()</div>
<div class="block">Constructs empty configuration.</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>SmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Constructs the configuration with a property name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - property name to use as a reference</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#listenTo(java.lang.String)"><code>listenTo(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>SmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="block">Constructs the configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - property name to use as a reference</dd>
<dd><code>config</code> - config to use with a property reference</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)"><code>listenTo(String, SmartListenerConfig)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Map)">
<h3>SmartListenerConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SmartListenerConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; references)</span></div>
<div class="block">Constructs the configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>references</code> - map of references to use</dd>
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
<section class="detail" id="initValueSpecificationConfig(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>initValueSpecificationConfig</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">initValueSpecificationConfig</span><wbr/><span class="parameters">(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> valueSpecificationConfig,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> elementAsValueConfig)</span></div>
<div class="block">Initializes value specification config.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecificationConfig</code> - config to initialize.</dd>
<dd><code>elementAsValueConfig</code> - element config to use.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeUnmodifiable()">
<h3>makeUnmodifiable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">makeUnmodifiable</span>()</div>
<div class="block">Make config unmodifiable.
 This means that new references can not be added or existing can not be changed.
 Any attempt to change unmodifiable config will end up with runtime exception.</div>
</section>
</li>
<li>
<section class="detail" id="copy(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="block">Makes a shallow copy of the passed config to this config.
 Instances of configs in the tree are reused and not re-created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>config</code> - passed configuration for copying.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deepCopy(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>deepCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deepCopy</span><wbr/><span class="parameters">(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="block">Deep copies a passed config to this config.
 Whole config tree is copied by recreating referenced config instances.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>config</code> - config to copy</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deepCopy()">
<h3>deepCopy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">deepCopy</span>()</div>
<div class="block">Creates a deep copy of the specified smart listener config.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>copy</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferences()">
<h3>getReferences</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt;</span> <span class="element-name">getReferences</span>()</div>
<div class="block">Gets references of this configuration.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>references of this configuration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyConfig(java.lang.String)">
<h3>getPropertyConfig</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">getPropertyConfig</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Gets property config which is used for a particular property.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - property for which to get property config</dd>
<dt>Returns:</dt>
<dd>property config for a given property</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>listenTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">listenTo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceName,
 @CheckForNull
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="block">Listens to a given property and passes a smart listener configuration for it to
 apply if references are found among property values.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referenceName</code> - property name for which configuration should be applied.</dd>
<dd><code>config</code> - passed configuration for the property. If for a given property an existing
                      configuration is found, the two configurations will be merged and the merged
                      configuration will be stored.</dd>
<dt>Returns:</dt>
<dd>self or a merged config if the configurations had to be merged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listenTo2(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>listenTo2</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">listenTo2</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> referenceName,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)"><code>listenTo(String, SmartListenerConfig)</code></a>, because it merges configs too.</div>
</div>
<div class="block">Makes the same thing as <a href="#listenTo(java.lang.String,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)"><code>listenTo(String, SmartListenerConfig)</code></a>.
 Only if founds already registered property
 doesn't emit warning, but makes merge with already registered configuration. If configurations are merged, then
 passed <code>config</code> VALUE is replaced with a contents of merge result.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referenceName</code> - property name for which configuration is applicable</dd>
<dd><code>config</code> - passed configuration. It's VALUE will be edited if another configuration will be found already
                      registered by given reference name. VALUE of passed reference will be changed to the merged one</dd>
<dt>Returns:</dt>
<dd>self or a merged config if the configurations had to be merged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listenTo(java.lang.String)">
<h3>listenTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">listenTo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Listens to a given property name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - property name ot listen to.</dd>
<dt>Returns:</dt>
<dd>self or a merged config if the configurations had to be merged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listenTo(java.util.Collection)">
<h3>listenTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">listenTo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</span></div>
<div class="block">Listens to given properties' names.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyNames</code> - properties' names to listen to</dd>
<dt>Returns:</dt>
<dd>self</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listenTo(java.lang.String...)">
<h3>listenTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">listenTo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... propertyNames)</span></div>
<div class="block">Listens to given properties' names.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyNames</code> - properties' names to listen to</dd>
<dt>Returns:</dt>
<dd>self</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listenToNested(java.lang.String)">
<h3>listenToNested</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">listenToNested</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Listens to a nested property configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>propertyName</code> - property name to listen to.</dd>
<dt>Returns:</dt>
<dd>property config of a given property, allows performing nested calls.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="listenTo(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>listenTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">listenTo</span><wbr/><span class="parameters">(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> config)</span></div>
<div class="block">Merges information from given config.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>config</code> - config</dd>
<dt>Returns:</dt>
<dd>self</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mergeConfigurations(com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig,com.nomagic.uml2.ext.jmi.smartlistener.SmartListenerConfig)">
<h3>mergeConfigurations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">mergeConfigurations</span><wbr/><span class="parameters">(<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c1,
 <a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a> c2)</span></div>
<div class="block">Merges two configurations into a single configuration.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>c1</code> - first configuration to merge.</dd>
<dd><code>c2</code> - second configuration to merge.</dd>
<dt>Returns:</dt>
<dd>merged configuration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="mergeConfigurations(java.util.Collection)">
<h3>mergeConfigurations</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a></span> <span class="element-name">mergeConfigurations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="SmartListenerConfig.html" title="class in com.nomagic.uml2.ext.jmi.smartlistener">SmartListenerConfig</a>&gt; configurations)</span></div>
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
<section class="detail" id="dump()">
<h3>dump</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dump</span>()</div>
<div class="block">Dumps property configuration to the standard output.</div>
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
