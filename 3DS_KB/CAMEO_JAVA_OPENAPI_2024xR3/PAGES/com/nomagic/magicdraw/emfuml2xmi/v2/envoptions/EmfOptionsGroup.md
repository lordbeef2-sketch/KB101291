# JAVA OPENAPI: EmfOptionsGroup (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/v2/envoptions/EmfOptionsGroup.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/envoptions/EmfOptionsGroup.html`
- source_sha256: `7dce7b495b8c9baa1ed301372a7578d1656e43e0a5b9b24493bdfdc81b3593d3`
- captured_utc: `2026-07-14T16:55:18.497043+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.v2.envoptions](package-summary.html)

## Class EmfOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](../../../core/options/OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](../../../core/options/AbstractPropertyOptionsGroup.html)
com.nomagic.magicdraw.core.options.VersionedOptionsGroup
[com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)
com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.EmfOptionsGroup

All Implemented Interfaces:
`[BaseOptions](../../envoptions/BaseOptions.html)`, `[Options](Options.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApipublic classEmfOptionsGroup
extends [BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)
implements [Options](Options.html)

Eclipse UML2 XMI v2.x export/import environment options.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`
Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)
`[EMF_OPTIONS_GROUP_ID](../../envoptions/BaseEmfOptionsGroup.html#EMF_OPTIONS_GROUP_ID), [MOVE_STEREOTYPE_TO_NESTING_PROFILE](../../envoptions/BaseEmfOptionsGroup.html#MOVE_STEREOTYPE_TO_NESTING_PROFILE), [OPTION_ASK_BEFORE_EXPORT](../../envoptions/BaseEmfOptionsGroup.html#OPTION_ASK_BEFORE_EXPORT), [OPTION_EXPORT_ALWAYS](../../envoptions/BaseEmfOptionsGroup.html#OPTION_EXPORT_ALWAYS), [OPTION_NEVER](../../envoptions/BaseEmfOptionsGroup.html#OPTION_NEVER)`
Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`CURRENT_EXPORTER_VERSION`
Fields inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](../../../core/options/OptionsGroup.html)
`[ICON_ENVIRONMENT_OPTIONS](../../../core/options/OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS)`
Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](../../envoptions/BaseOptions.html)
`[ID_EXPORT_POLICY_GENERATE_ID](../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID), [ID_EXPORT_POLICY_USE_ELEMENT_ID](../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID), [ID_EXPORT_POLICY_USE_SERVER_ID](../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID), [OPTION_ASK_BEFORE_EXPORT](../../envoptions/BaseOptions.html#OPTION_ASK_BEFORE_EXPORT), [OPTION_EXPORT_ALWAYS](../../envoptions/BaseOptions.html#OPTION_EXPORT_ALWAYS), [OPTION_NEVER](../../envoptions/BaseOptions.html#OPTION_NEVER)`
Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.[Options](Options.html)
`[CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS), [CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE), [CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EmfOptionsGroup](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[afterLoad](#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean))(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)`

`protected com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider`
`[createPropertyResourceProvider](#createPropertyResourceProvider())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getChangeStereotypePropertyTypeStereotype](#getChangeStereotypePropertyTypeStereotype())()`
Get "Change stereotype property type stereotype" option value.
`static [EmfOptionsGroup](EmfOptionsGroup.html)`
`[getEMFOptions](#getEMFOptions())()`
Get the Eclipse UML2 XMI v2.x export/import options.
`boolean`
`[isChangeNotEcoreDataTypeToString](#isChangeNotEcoreDataTypeToString())()`
Checks if to change stereotype property type not eCore datatype to String on export.
`boolean`
`[isChangeStereotypePropertyTypeStereotype](#isChangeStereotypePropertyTypeStereotype())()`
Checks if to change stereotype property type stereotype to metaclass on export.
`void`
`[setChangeNotEcoreDataTypeToString](#setChangeNotEcoreDataTypeToString(boolean))(boolean change)`
Set if to change stereotype property type not eCore datatype to String on export.
`void`
`[setChangeStereotypePropertyTypeStereotype](#setChangeStereotypePropertyTypeStereotype(boolean))(boolean change)`
Set if to change stereotype property type stereotype to metaclass on export.
`void`
`[setChangeStereotypePropertyTypeStereotype](#setChangeStereotypePropertyTypeStereotype(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Set "Change stereotype property type stereotype" option value.
`void`
`[setDefaultValues](#setDefaultValues())()`
Sets default values for the properties contained in this group.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)
`[addBooleanProperty](../../envoptions/BaseEmfOptionsGroup.html#addBooleanProperty(java.lang.String,java.lang.String)), [addBooleanProperty](../../envoptions/BaseEmfOptionsGroup.html#addBooleanProperty(java.lang.String,java.lang.String,boolean)), [addChoiceProperty](../../envoptions/BaseEmfOptionsGroup.html#addChoiceProperty(java.lang.String,java.lang.String%5B%5D,java.lang.String,java.lang.String)), [addProperty](../../envoptions/BaseEmfOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)), [getAutoExportOption](../../envoptions/BaseEmfOptionsGroup.html#getAutoExportOption()), [getBanner](../../envoptions/BaseEmfOptionsGroup.html#getBanner()), [getBaseEMFOptions](../../envoptions/BaseEmfOptionsGroup.html#getBaseEMFOptions(java.lang.String)), [getBooleanProperty](../../envoptions/BaseEmfOptionsGroup.html#getBooleanProperty(java.lang.String)), [getBooleanPropertyValue](../../envoptions/BaseEmfOptionsGroup.html#getBooleanPropertyValue(java.lang.String)), [getChoice](../../envoptions/BaseEmfOptionsGroup.html#getChoice(java.lang.String)), [getGroupIcon](../../envoptions/BaseEmfOptionsGroup.html#getGroupIcon()), [getIDExportPolicy](../../envoptions/BaseEmfOptionsGroup.html#getIDExportPolicy()), [getName](../../envoptions/BaseEmfOptionsGroup.html#getName()), [getPropertyGroupName](../../envoptions/BaseEmfOptionsGroup.html#getPropertyGroupName(boolean,boolean)), [isApplyAllProfilesToRootModel](../../envoptions/BaseEmfOptionsGroup.html#isApplyAllProfilesToRootModel()), [isAskBeforeExport](../../envoptions/BaseEmfOptionsGroup.html#isAskBeforeExport()), [isAskToOverwriteExportedFiles](../../envoptions/BaseEmfOptionsGroup.html#isAskToOverwriteExportedFiles()), [isAutoExport](../../envoptions/BaseEmfOptionsGroup.html#isAutoExport()), [isDisplayWarnings](../../envoptions/BaseEmfOptionsGroup.html#isDisplayWarnings()), [isMoveStereotypeToNestingProfile](../../envoptions/BaseEmfOptionsGroup.html#isMoveStereotypeToNestingProfile()), [isPreserveIDsOnImport](../../envoptions/BaseEmfOptionsGroup.html#isPreserveIDsOnImport()), [isShowMappinWarning](../../envoptions/BaseEmfOptionsGroup.html#isShowMappinWarning()), [isShowStereotypeFromSameWarning](../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypeFromSameWarning()), [isShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypePropertyTypeChangeWarning()), [isUseKeywordAsStereotypeName](../../envoptions/BaseEmfOptionsGroup.html#isUseKeywordAsStereotypeName()), [loadOptions](../../envoptions/BaseEmfOptionsGroup.html#loadOptions(com.nomagic.magicdraw.properties.Style,boolean)), [registerOptions](../../envoptions/BaseEmfOptionsGroup.html#registerOptions(com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup)), [setApplyAllProfilesToRootModel](../../envoptions/BaseEmfOptionsGroup.html#setApplyAllProfilesToRootModel(boolean)), [setAskToOverwriteExportedFiles](../../envoptions/BaseEmfOptionsGroup.html#setAskToOverwriteExportedFiles(boolean)), [setAutoExportOption](../../envoptions/BaseEmfOptionsGroup.html#setAutoExportOption(java.lang.String)), [setBooleanPropertyValue](../../envoptions/BaseEmfOptionsGroup.html#setBooleanPropertyValue(java.lang.String,boolean)), [setDisplayWarnings](../../envoptions/BaseEmfOptionsGroup.html#setDisplayWarnings(boolean)), [setIDExportPolicy](../../envoptions/BaseEmfOptionsGroup.html#setIDExportPolicy(java.lang.String)), [setMoveStereotypeToNestingProfile](../../envoptions/BaseEmfOptionsGroup.html#setMoveStereotypeToNestingProfile(boolean)), [setPreserveIDsOnImport](../../envoptions/BaseEmfOptionsGroup.html#setPreserveIDsOnImport(boolean)), [setShowMappinWarning](../../envoptions/BaseEmfOptionsGroup.html#setShowMappinWarning(boolean)), [setShowStereotypeFromSameWarning](../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypeFromSameWarning(boolean)), [setShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypePropertyTypeChangeWarning(boolean)), [setUseKeywordAsStereotypeName](../../envoptions/BaseEmfOptionsGroup.html#setUseKeywordAsStereotypeName(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](../../../core/options/AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](../../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [afterLoadAdditionalAction](../../../core/options/AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)), [clone](../../../core/options/AbstractPropertyOptionsGroup.html#clone()), [createDefault](../../../core/options/AbstractPropertyOptionsGroup.html#createDefault()), [createOptions](../../../core/options/AbstractPropertyOptionsGroup.html#createOptions()), [createOptionsPanel](../../../core/options/AbstractPropertyOptionsGroup.html#createOptionsPanel()), [fixProperty](../../../core/options/AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)), [getCopy](../../../core/options/AbstractPropertyOptionsGroup.html#getCopy()), [getOptions](../../../core/options/AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](../../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](../../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()), [hasVisibleOptions](../../../core/options/AbstractPropertyOptionsGroup.html#hasVisibleOptions()), [removeProperty](../../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](../../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](../../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](../../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](../../../core/options/OptionsGroup.html)
`[add](../../../core/options/OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)), [afterSave](../../../core/options/OptionsGroup.html#afterSave()), [canDisplay](../../../core/options/OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)), [firstInit](../../../core/options/OptionsGroup.html#firstInit(boolean)), [getChildren](../../../core/options/OptionsGroup.html#getChildren()), [getIcon](../../../core/options/OptionsGroup.html#getIcon()), [getId](../../../core/options/OptionsGroup.html#getId()), [getModelingLanguage](../../../core/options/OptionsGroup.html#getModelingLanguage()), [getParent](../../../core/options/OptionsGroup.html#getParent()), [isEnabled](../../../core/options/OptionsGroup.html#isEnabled()), [isVisible](../../../core/options/OptionsGroup.html#isVisible()), [remove](../../../core/options/OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)), [resetCachedValues](../../../core/options/OptionsGroup.html#resetCachedValues()), [setEnabled](../../../core/options/OptionsGroup.html#setEnabled(boolean)), [setVisible](../../../core/options/OptionsGroup.html#setVisible(boolean)), [sortChildren](../../../core/options/OptionsGroup.html#sortChildren(java.util.Comparator))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](../../envoptions/BaseOptions.html)
`[getAutoExportOption](../../envoptions/BaseOptions.html#getAutoExportOption()), [getIDExportPolicy](../../envoptions/BaseOptions.html#getIDExportPolicy()), [isApplyAllProfilesToRootModel](../../envoptions/BaseOptions.html#isApplyAllProfilesToRootModel()), [isAskBeforeExport](../../envoptions/BaseOptions.html#isAskBeforeExport()), [isAskToOverwriteExportedFiles](../../envoptions/BaseOptions.html#isAskToOverwriteExportedFiles()), [isAutoExport](../../envoptions/BaseOptions.html#isAutoExport()), [isDisplayWarnings](../../envoptions/BaseOptions.html#isDisplayWarnings()), [isMoveStereotypeToNestingProfile](../../envoptions/BaseOptions.html#isMoveStereotypeToNestingProfile()), [isPreserveIDsOnImport](../../envoptions/BaseOptions.html#isPreserveIDsOnImport()), [isShowMappinWarning](../../envoptions/BaseOptions.html#isShowMappinWarning()), [isShowStereotypeFromSameWarning](../../envoptions/BaseOptions.html#isShowStereotypeFromSameWarning()), [isShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseOptions.html#isShowStereotypePropertyTypeChangeWarning()), [isUseKeywordAsStereotypeName](../../envoptions/BaseOptions.html#isUseKeywordAsStereotypeName()), [setApplyAllProfilesToRootModel](../../envoptions/BaseOptions.html#setApplyAllProfilesToRootModel(boolean)), [setAskToOverwriteExportedFiles](../../envoptions/BaseOptions.html#setAskToOverwriteExportedFiles(boolean)), [setAutoExportOption](../../envoptions/BaseOptions.html#setAutoExportOption(java.lang.String)), [setDisplayWarnings](../../envoptions/BaseOptions.html#setDisplayWarnings(boolean)), [setIDExportPolicy](../../envoptions/BaseOptions.html#setIDExportPolicy(java.lang.String)), [setMoveStereotypeToNestingProfile](../../envoptions/BaseOptions.html#setMoveStereotypeToNestingProfile(boolean)), [setShowMappinWarning](../../envoptions/BaseOptions.html#setShowMappinWarning(boolean)), [setShowStereotypeFromSameWarning](../../envoptions/BaseOptions.html#setShowStereotypeFromSameWarning(boolean)), [setShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean)), [setUseKeywordAsStereotypeName](../../envoptions/BaseOptions.html#setUseKeywordAsStereotypeName(boolean))`

============ FIELD DETAIL =========== 
Field Details
ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ID
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.EmfOptionsGroup.ID)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EmfOptionsGroup
public EmfOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)
 ============ METHOD DETAIL ========== 
Method Details
getEMFOptions
@OpenApipublic static [EmfOptionsGroup](EmfOptionsGroup.html) getEMFOptions()
Get the Eclipse UML2 XMI v2.x export/import options. Options must accessed only after the application is started.
Returns:
loaded options.
setDefaultValues
public void setDefaultValues()
Description copied from class: `[AbstractPropertyOptionsGroup](../../../core/options/AbstractPropertyOptionsGroup.html#setDefaultValues())`
Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.
Overrides:
`[setDefaultValues](../../envoptions/BaseEmfOptionsGroup.html#setDefaultValues())` in class `[BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)`
afterLoad
protected void afterLoad(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)
Overrides:
`[afterLoad](../../envoptions/BaseEmfOptionsGroup.html#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean))` in class `[BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)`
setChangeStereotypePropertyTypeStereotype
@OpenApipublic void setChangeStereotypePropertyTypeStereotype(boolean change)
Set if to change stereotype property type stereotype to metaclass on export.
Specified by:
`[setChangeStereotypePropertyTypeStereotype](Options.html#setChangeStereotypePropertyTypeStereotype(boolean))` in interface `[Options](Options.html)`
Parameters:
`change` -
isChangeStereotypePropertyTypeStereotype
@OpenApipublic boolean isChangeStereotypePropertyTypeStereotype()
Checks if to change stereotype property type stereotype to metaclass on export.
Specified by:
`[isChangeStereotypePropertyTypeStereotype](Options.html#isChangeStereotypePropertyTypeStereotype())` in interface `[Options](Options.html)`
Returns:
true if stereotype property type stereotype should be changed to metaclass.
setChangeStereotypePropertyTypeStereotype
public void setChangeStereotypePropertyTypeStereotype([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Description copied from interface: `[Options](Options.html#setChangeStereotypePropertyTypeStereotype(java.lang.String))`
Set "Change stereotype property type stereotype" option value.
Specified by:
`[setChangeStereotypePropertyTypeStereotype](Options.html#setChangeStereotypePropertyTypeStereotype(java.lang.String))` in interface `[Options](Options.html)`
Parameters:
`value` - value to set ([`Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE`](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE), [`Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS`](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS), [`Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS`](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS)).
getChangeStereotypePropertyTypeStereotype
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getChangeStereotypePropertyTypeStereotype()
Description copied from interface: `[Options](Options.html#getChangeStereotypePropertyTypeStereotype())`
Get "Change stereotype property type stereotype" option value.
Specified by:
`[getChangeStereotypePropertyTypeStereotype](Options.html#getChangeStereotypePropertyTypeStereotype())` in interface `[Options](Options.html)`
Returns:
value ([`Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE`](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE), [`Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS`](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS), [`Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS`](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS))
setChangeNotEcoreDataTypeToString
public void setChangeNotEcoreDataTypeToString(boolean change)
Description copied from interface: `[Options](Options.html#setChangeNotEcoreDataTypeToString(boolean))`
Set if to change stereotype property type not eCore datatype to String on export.
Specified by:
`[setChangeNotEcoreDataTypeToString](Options.html#setChangeNotEcoreDataTypeToString(boolean))` in interface `[Options](Options.html)`
Parameters:
`change` - true - change.
isChangeNotEcoreDataTypeToString
public boolean isChangeNotEcoreDataTypeToString()
Description copied from interface: `[Options](Options.html#isChangeNotEcoreDataTypeToString())`
Checks if to change stereotype property type not eCore datatype to String on export.
Specified by:
`[isChangeNotEcoreDataTypeToString](Options.html#isChangeNotEcoreDataTypeToString())` in interface `[Options](Options.html)`
Returns:
true if stereotype property type not eCore datatype should be changed to String.
createPropertyResourceProvider
protected com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider createPropertyResourceProvider()
Overrides:
`[createPropertyResourceProvider](../../envoptions/BaseEmfOptionsGroup.html#createPropertyResourceProvider())` in class `[BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.v2.envoptions</a></div>
<h1 class="title" title="Class EmfOptionsGroup">Class EmfOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="../../../core/options/AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.VersionedOptionsGroup
<div class="inheritance"><a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.EmfOptionsGroup</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code>, <code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">EmfOptionsGroup</span>
<span class="extends-implements">extends <a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a>
implements <a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></span></div>
<div class="block">Eclipse UML2 XMI v2.x export/import environment options.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID">ID</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup">Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></h3>
<code><a href="../../envoptions/BaseEmfOptionsGroup.html#EMF_OPTIONS_GROUP_ID">EMF_OPTIONS_GROUP_ID</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#MOVE_STEREOTYPE_TO_NESTING_PROFILE">MOVE_STEREOTYPE_TO_NESTING_PROFILE</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#OPTION_NEVER">OPTION_NEVER</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>CURRENT_EXPORTER_VERSION</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="../../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="../../../core/options/OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS">ICON_ENVIRONMENT_OPTIONS</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID">ID_EXPORT_POLICY_GENERATE_ID</a>, <a href="../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID">ID_EXPORT_POLICY_USE_ELEMENT_ID</a>, <a href="../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID">ID_EXPORT_POLICY_USE_SERVER_ID</a>, <a href="../../envoptions/BaseOptions.html#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a>, <a href="../../envoptions/BaseOptions.html#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a>, <a href="../../envoptions/BaseOptions.html#OPTION_NEVER">OPTION_NEVER</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.Options">Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.<a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></h3>
<code><a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS</a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE</a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">EmfOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">afterLoad</a><wbr/>(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyResourceProvider()">createPropertyResourceProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChangeStereotypePropertyTypeStereotype()">getChangeStereotypePropertyTypeStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get "Change stereotype property type stereotype" option value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="EmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">EmfOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEMFOptions()">getEMFOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get the Eclipse UML2 XMI v2.x export/import options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChangeNotEcoreDataTypeToString()">isChangeNotEcoreDataTypeToString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if to change stereotype property type not eCore datatype to String on export.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChangeStereotypePropertyTypeStereotype()">isChangeStereotypePropertyTypeStereotype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if to change stereotype property type stereotype to metaclass on export.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangeNotEcoreDataTypeToString(boolean)">setChangeNotEcoreDataTypeToString</a><wbr/>(boolean change)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if to change stereotype property type not eCore datatype to String on export.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangeStereotypePropertyTypeStereotype(boolean)">setChangeStereotypePropertyTypeStereotype</a><wbr/>(boolean change)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if to change stereotype property type stereotype to metaclass on export.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangeStereotypePropertyTypeStereotype(java.lang.String)">setChangeStereotypePropertyTypeStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set "Change stereotype property type stereotype" option value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultValues()">setDefaultValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default values for the properties contained in this group.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></h3>
<code><a href="../../envoptions/BaseEmfOptionsGroup.html#addBooleanProperty(java.lang.String,java.lang.String)">addBooleanProperty</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#addBooleanProperty(java.lang.String,java.lang.String,boolean)">addBooleanProperty</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#addChoiceProperty(java.lang.String,java.lang.String%5B%5D,java.lang.String,java.lang.String)">addChoiceProperty</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getAutoExportOption()">getAutoExportOption</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getBanner()">getBanner</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getBaseEMFOptions(java.lang.String)">getBaseEMFOptions</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getBooleanProperty(java.lang.String)">getBooleanProperty</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getBooleanPropertyValue(java.lang.String)">getBooleanPropertyValue</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getChoice(java.lang.String)">getChoice</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getGroupIcon()">getGroupIcon</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getIDExportPolicy()">getIDExportPolicy</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getName()">getName</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getPropertyGroupName(boolean,boolean)">getPropertyGroupName</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isAskBeforeExport()">isAskBeforeExport</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isAutoExport()">isAutoExport</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isDisplayWarnings()">isDisplayWarnings</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isPreserveIDsOnImport()">isPreserveIDsOnImport</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isShowMappinWarning()">isShowMappinWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#loadOptions(com.nomagic.magicdraw.properties.Style,boolean)">loadOptions</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#registerOptions(com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup)">registerOptions</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setAutoExportOption(java.lang.String)">setAutoExportOption</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setBooleanPropertyValue(java.lang.String,boolean)">setBooleanPropertyValue</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setDisplayWarnings(boolean)">setDisplayWarnings</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setPreserveIDsOnImport(boolean)">setPreserveIDsOnImport</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setShowMappinWarning(boolean)">setShowMappinWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="../../../core/options/AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="../../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)">afterLoadAdditionalAction</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#clone()">clone</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#createDefault()">createDefault</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#createOptions()">createOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#createOptionsPanel()">createOptionsPanel</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)">fixProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#getCopy()">getCopy</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#hasVisibleOptions()">hasVisibleOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="../../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="../../../core/options/OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)">add</a>, <a href="../../../core/options/OptionsGroup.html#afterSave()">afterSave</a>, <a href="../../../core/options/OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)">canDisplay</a>, <a href="../../../core/options/OptionsGroup.html#firstInit(boolean)">firstInit</a>, <a href="../../../core/options/OptionsGroup.html#getChildren()">getChildren</a>, <a href="../../../core/options/OptionsGroup.html#getIcon()">getIcon</a>, <a href="../../../core/options/OptionsGroup.html#getId()">getId</a>, <a href="../../../core/options/OptionsGroup.html#getModelingLanguage()">getModelingLanguage</a>, <a href="../../../core/options/OptionsGroup.html#getParent()">getParent</a>, <a href="../../../core/options/OptionsGroup.html#isEnabled()">isEnabled</a>, <a href="../../../core/options/OptionsGroup.html#isVisible()">isVisible</a>, <a href="../../../core/options/OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)">remove</a>, <a href="../../../core/options/OptionsGroup.html#resetCachedValues()">resetCachedValues</a>, <a href="../../../core/options/OptionsGroup.html#setEnabled(boolean)">setEnabled</a>, <a href="../../../core/options/OptionsGroup.html#setVisible(boolean)">setVisible</a>, <a href="../../../core/options/OptionsGroup.html#sortChildren(java.util.Comparator)">sortChildren</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="../../envoptions/BaseOptions.html#getAutoExportOption()">getAutoExportOption</a>, <a href="../../envoptions/BaseOptions.html#getIDExportPolicy()">getIDExportPolicy</a>, <a href="../../envoptions/BaseOptions.html#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseOptions.html#isAskBeforeExport()">isAskBeforeExport</a>, <a href="../../envoptions/BaseOptions.html#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseOptions.html#isAutoExport()">isAutoExport</a>, <a href="../../envoptions/BaseOptions.html#isDisplayWarnings()">isDisplayWarnings</a>, <a href="../../envoptions/BaseOptions.html#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseOptions.html#isPreserveIDsOnImport()">isPreserveIDsOnImport</a>, <a href="../../envoptions/BaseOptions.html#isShowMappinWarning()">isShowMappinWarning</a>, <a href="../../envoptions/BaseOptions.html#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseOptions.html#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseOptions.html#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a>, <a href="../../envoptions/BaseOptions.html#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseOptions.html#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseOptions.html#setAutoExportOption(java.lang.String)">setAutoExportOption</a>, <a href="../../envoptions/BaseOptions.html#setDisplayWarnings(boolean)">setDisplayWarnings</a>, <a href="../../envoptions/BaseOptions.html#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a>, <a href="../../envoptions/BaseOptions.html#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseOptions.html#setShowMappinWarning(boolean)">setShowMappinWarning</a>, <a href="../../envoptions/BaseOptions.html#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseOptions.html#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a></code></div>
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
<section class="detail" id="ID">
<h3>ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.EmfOptionsGroup.ID">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>EmfOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EmfOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</span></div>
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
<section class="detail" id="getEMFOptions()">
<h3>getEMFOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="EmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">EmfOptionsGroup</a></span> <span class="element-name">getEMFOptions</span>()</div>
<div class="block">Get the Eclipse UML2 XMI v2.x export/import options. Options must accessed only after the application is started.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>loaded options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefaultValues()">
<h3>setDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultValues</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../../core/options/AbstractPropertyOptionsGroup.html#setDefaultValues()">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../envoptions/BaseEmfOptionsGroup.html#setDefaultValues()">setDefaultValues</a></code> in class <code><a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">
<h3>afterLoad</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">afterLoad</span><wbr/><span class="parameters">(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../envoptions/BaseEmfOptionsGroup.html#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">afterLoad</a></code> in class <code><a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeStereotypePropertyTypeStereotype(boolean)">
<h3>setChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChangeStereotypePropertyTypeStereotype</span><wbr/><span class="parameters">(boolean change)</span></div>
<div class="block">Set if to change stereotype property type stereotype to metaclass on export.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Options.html#setChangeStereotypePropertyTypeStereotype(boolean)">setChangeStereotypePropertyTypeStereotype</a></code> in interface <code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></dd>
<dt>Parameters:</dt>
<dd><code>change</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChangeStereotypePropertyTypeStereotype()">
<h3>isChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChangeStereotypePropertyTypeStereotype</span>()</div>
<div class="block">Checks if to change stereotype property type stereotype to metaclass on export.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Options.html#isChangeStereotypePropertyTypeStereotype()">isChangeStereotypePropertyTypeStereotype</a></code> in interface <code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></dd>
<dt>Returns:</dt>
<dd>true if stereotype property type stereotype should be changed to metaclass.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeStereotypePropertyTypeStereotype(java.lang.String)">
<h3>setChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChangeStereotypePropertyTypeStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="Options.html#setChangeStereotypePropertyTypeStereotype(java.lang.String)">Options</a></code></span></div>
<div class="block">Set "Change stereotype property type stereotype" option value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Options.html#setChangeStereotypePropertyTypeStereotype(java.lang.String)">setChangeStereotypePropertyTypeStereotype</a></code> in interface <code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></dd>
<dt>Parameters:</dt>
<dd><code>value</code> - value to set (<a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE"><code>Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE</code></a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS"><code>Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS</code></a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS"><code>Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS</code></a>).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangeStereotypePropertyTypeStereotype()">
<h3>getChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getChangeStereotypePropertyTypeStereotype</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="Options.html#getChangeStereotypePropertyTypeStereotype()">Options</a></code></span></div>
<div class="block">Get "Change stereotype property type stereotype" option value.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Options.html#getChangeStereotypePropertyTypeStereotype()">getChangeStereotypePropertyTypeStereotype</a></code> in interface <code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></dd>
<dt>Returns:</dt>
<dd>value (<a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE"><code>Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE</code></a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS"><code>Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS</code></a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS"><code>Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS</code></a>)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeNotEcoreDataTypeToString(boolean)">
<h3>setChangeNotEcoreDataTypeToString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChangeNotEcoreDataTypeToString</span><wbr/><span class="parameters">(boolean change)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="Options.html#setChangeNotEcoreDataTypeToString(boolean)">Options</a></code></span></div>
<div class="block">Set if to change stereotype property type not eCore datatype to String on export.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Options.html#setChangeNotEcoreDataTypeToString(boolean)">setChangeNotEcoreDataTypeToString</a></code> in interface <code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></dd>
<dt>Parameters:</dt>
<dd><code>change</code> - true - change.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChangeNotEcoreDataTypeToString()">
<h3>isChangeNotEcoreDataTypeToString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isChangeNotEcoreDataTypeToString</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="Options.html#isChangeNotEcoreDataTypeToString()">Options</a></code></span></div>
<div class="block">Checks if to change stereotype property type not eCore datatype to String on export.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="Options.html#isChangeNotEcoreDataTypeToString()">isChangeNotEcoreDataTypeToString</a></code> in interface <code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></dd>
<dt>Returns:</dt>
<dd>true if stereotype property type not eCore datatype should be changed to String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPropertyResourceProvider()">
<h3>createPropertyResourceProvider</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider</span> <span class="element-name">createPropertyResourceProvider</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../envoptions/BaseEmfOptionsGroup.html#createPropertyResourceProvider()">createPropertyResourceProvider</a></code> in class <code><a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></dd>
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
