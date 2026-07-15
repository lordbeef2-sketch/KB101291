# JAVA OPENAPI: BaseEmfOptionsGroup (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/envoptions/BaseEmfOptionsGroup.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/envoptions/BaseEmfOptionsGroup.html`
- source_sha256: `df0ce100e802ee3bbba4b44275c3667b25018509c1ec65917b10b31d13af057f`
- captured_utc: `2026-07-14T16:55:18.265041+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.envoptions](package-summary.html)

## Class BaseEmfOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](../../core/options/OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](../../core/options/AbstractPropertyOptionsGroup.html)
com.nomagic.magicdraw.core.options.VersionedOptionsGroup
com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup

All Implemented Interfaces:
`[BaseOptions](BaseOptions.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[EmfOptionsGroup](../v2/envoptions/EmfOptionsGroup.html)`

@OpenApipublic abstract classBaseEmfOptionsGroup
extends com.nomagic.magicdraw.core.options.VersionedOptionsGroup
implements [BaseOptions](BaseOptions.html)

Eclipse UML2 XMI export/import environment options.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[EMF_OPTIONS_GROUP_ID](#EMF_OPTIONS_GROUP_ID)`

`protected static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[MOVE_STEREOTYPE_TO_NESTING_PROFILE](#MOVE_STEREOTYPE_TO_NESTING_PROFILE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPTION_ASK_BEFORE_EXPORT](#OPTION_ASK_BEFORE_EXPORT)`
Auto-export to Eclipse UML2 XMI option.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPTION_EXPORT_ALWAYS](#OPTION_EXPORT_ALWAYS)`
Auto-export to Eclipse UML2 XMI option.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPTION_NEVER](#OPTION_NEVER)`
Auto-export to Eclipse UML2 XMI option.
Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`CURRENT_EXPORTER_VERSION`
Fields inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](../../core/options/OptionsGroup.html)
`[ICON_ENVIRONMENT_OPTIONS](../../core/options/OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS)`
Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](BaseOptions.html)
`[ID_EXPORT_POLICY_GENERATE_ID](BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID), [ID_EXPORT_POLICY_USE_ELEMENT_ID](BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID), [ID_EXPORT_POLICY_USE_SERVER_ID](BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[BaseEmfOptionsGroup](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected final void`
`[addBooleanProperty](#addBooleanProperty(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`protected final void`
`[addBooleanProperty](#addBooleanProperty(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean value)`

`protected final void`
`[addChoiceProperty](#addChoiceProperty(java.lang.String,java.lang.String%5B%5D,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] choice,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) selected,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)`

`void`
`[addProperty](#addProperty(com.nomagic.magicdraw.properties.Property))([Property](../../properties/Property.html) property)`
Adds property to this group.
`protected void`
`[afterLoad](#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean))(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)`

`protected com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider`
`[createPropertyResourceProvider](#createPropertyResourceProvider())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAutoExportOption](#getAutoExportOption())()`
Get auto-export to Eclipse UML2 XMI option.
`com.nomagic.ui.banners.Banner`
`[getBanner](#getBanner())()`

`static [BaseEmfOptionsGroup](BaseEmfOptionsGroup.html)`
`[getBaseEMFOptions](#getBaseEMFOptions(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)`

`protected final [BooleanProperty](../../properties/BooleanProperty.html)`
`[getBooleanProperty](#getBooleanProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`protected final boolean`
`[getBooleanPropertyValue](#getBooleanPropertyValue(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`protected final [ChoiceProperty](../../properties/ChoiceProperty.html)`
`[getChoice](#getChoice(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getGroupIcon](#getGroupIcon())()`
Returns icon to display with options.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getIDExportPolicy](#getIDExportPolicy())()`
Get current ID export choice.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Gets human-readable name of options.
`protected static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPropertyGroupName](#getPropertyGroupName(boolean,boolean))(boolean exportb,
 boolean importb)`

`boolean`
`[isApplyAllProfilesToRootModel](#isApplyAllProfilesToRootModel())()`
Checks if to apply all profiles to root Model on export.
`boolean`
`[isAskBeforeExport](#isAskBeforeExport())()`

`boolean`
`[isAskToOverwriteExportedFiles](#isAskToOverwriteExportedFiles())()`
Chekcks if ask to overwrite exported files.
`boolean`
`[isAutoExport](#isAutoExport())()`

`boolean`
`[isDisplayWarnings](#isDisplayWarnings())()`
Checks if to show warnings in Message Window on export/import.
`boolean`
`[isMoveStereotypeToNestingProfile](#isMoveStereotypeToNestingProfile())()`
Checks if move stereotype to nesting profile if stereotype is not directly contained by profile.
`boolean`
`[isPreserveIDsOnImport](#isPreserveIDsOnImport())()`

`boolean`
`[isShowMappinWarning](#isShowMappinWarning())()`
Checks if show warnings about (datatypes, metaclasses) mappings.
`boolean`
`[isShowStereotypeFromSameWarning](#isShowStereotypeFromSameWarning())()`
Checks if show warnings about not applied stereotypes (from the same profile).
`boolean`
`[isShowStereotypePropertyTypeChangeWarning](#isShowStereotypePropertyTypeChangeWarning())()`
Check if show warnings about stereotype property type change.
`boolean`
`[isUseKeywordAsStereotypeName](#isUseKeywordAsStereotypeName())()`
Checks if stereotype keyword is used as stereotype name on import.
`void`
`[loadOptions](#loadOptions(com.nomagic.magicdraw.properties.Style,boolean))([Style](../../properties/Style.html) style,
 boolean pluginsLoaded)`

`static [BaseEmfOptionsGroup](BaseEmfOptionsGroup.html)`
`[registerOptions](#registerOptions(com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup))([BaseEmfOptionsGroup](BaseEmfOptionsGroup.html) options)`

`void`
`[setApplyAllProfilesToRootModel](#setApplyAllProfilesToRootModel(boolean))(boolean apply)`
Set if to apply all profiles to root Model on export.
`void`
`[setAskToOverwriteExportedFiles](#setAskToOverwriteExportedFiles(boolean))(boolean ask)`
Set if ask to overwrite exported files.
`void`
`[setAutoExportOption](#setAutoExportOption(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) choice)`
Set auto-export to Eclipse UML2 XMI on project save option.
`protected final void`
`[setBooleanPropertyValue](#setBooleanPropertyValue(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 boolean value)`

`void`
`[setDefaultValues](#setDefaultValues())()`
Sets default values for the properties contained in this group.
`void`
`[setDisplayWarnings](#setDisplayWarnings(boolean))(boolean display)`
Set if to show warnings in Message Window on export/import.
`void`
`[setIDExportPolicy](#setIDExportPolicy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) choice)`
Set ID export policy
`void`
`[setMoveStereotypeToNestingProfile](#setMoveStereotypeToNestingProfile(boolean))(boolean move)`
Set if move stereotype to nesting profile if stereotype is not directly contained by profile.
`void`
`[setPreserveIDsOnImport](#setPreserveIDsOnImport(boolean))(boolean preserve)`

`void`
`[setShowMappinWarning](#setShowMappinWarning(boolean))(boolean show)`
Set if show warnings about (datatypes, metaclasses) mappings.
`void`
`[setShowStereotypeFromSameWarning](#setShowStereotypeFromSameWarning(boolean))(boolean show)`
Set if show warnings about not applied stereotypes (from the same profile).
`void`
`[setShowStereotypePropertyTypeChangeWarning](#setShowStereotypePropertyTypeChangeWarning(boolean))(boolean show)`
Set if show warnings about stereotype property type change.
`void`
`[setUseKeywordAsStereotypeName](#setUseKeywordAsStereotypeName(boolean))(boolean use)`
Set if stereotype keyword is used as stereotype name on import.
Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](../../core/options/AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [afterLoadAdditionalAction](../../core/options/AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)), [clone](../../core/options/AbstractPropertyOptionsGroup.html#clone()), [createDefault](../../core/options/AbstractPropertyOptionsGroup.html#createDefault()), [createOptions](../../core/options/AbstractPropertyOptionsGroup.html#createOptions()), [createOptionsPanel](../../core/options/AbstractPropertyOptionsGroup.html#createOptionsPanel()), [fixProperty](../../core/options/AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)), [getCopy](../../core/options/AbstractPropertyOptionsGroup.html#getCopy()), [getOptions](../../core/options/AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()), [hasVisibleOptions](../../core/options/AbstractPropertyOptionsGroup.html#hasVisibleOptions()), [removeProperty](../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](../../core/options/OptionsGroup.html)
`[add](../../core/options/OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)), [afterSave](../../core/options/OptionsGroup.html#afterSave()), [canDisplay](../../core/options/OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)), [firstInit](../../core/options/OptionsGroup.html#firstInit(boolean)), [getChildren](../../core/options/OptionsGroup.html#getChildren()), [getIcon](../../core/options/OptionsGroup.html#getIcon()), [getId](../../core/options/OptionsGroup.html#getId()), [getModelingLanguage](../../core/options/OptionsGroup.html#getModelingLanguage()), [getParent](../../core/options/OptionsGroup.html#getParent()), [isEnabled](../../core/options/OptionsGroup.html#isEnabled()), [isVisible](../../core/options/OptionsGroup.html#isVisible()), [remove](../../core/options/OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)), [resetCachedValues](../../core/options/OptionsGroup.html#resetCachedValues()), [setEnabled](../../core/options/OptionsGroup.html#setEnabled(boolean)), [setVisible](../../core/options/OptionsGroup.html#setVisible(boolean)), [sortChildren](../../core/options/OptionsGroup.html#sortChildren(java.util.Comparator))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
OPTION_EXPORT_ALWAYS
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPTION_EXPORT_ALWAYS
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_EXPORT_ALWAYS)
OPTION_ASK_BEFORE_EXPORT
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPTION_ASK_BEFORE_EXPORT
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_ASK_BEFORE_EXPORT)
OPTION_NEVER
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPTION_NEVER
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_NEVER)
MOVE_STEREOTYPE_TO_NESTING_PROFILE
protected static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) MOVE_STEREOTYPE_TO_NESTING_PROFILE
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.MOVE_STEREOTYPE_TO_NESTING_PROFILE)
EMF_OPTIONS_GROUP_ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EMF_OPTIONS_GROUP_ID
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.EMF_OPTIONS_GROUP_ID)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BaseEmfOptionsGroup
public BaseEmfOptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) format)
 ============ METHOD DETAIL ========== 
Method Details
registerOptions
public static [BaseEmfOptionsGroup](BaseEmfOptionsGroup.html) registerOptions([BaseEmfOptionsGroup](BaseEmfOptionsGroup.html) options)
getBaseEMFOptions
public static [BaseEmfOptionsGroup](BaseEmfOptionsGroup.html) getBaseEMFOptions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) optionsGroupID)
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Description copied from class: `[OptionsGroup](../../core/options/OptionsGroup.html#getName())`
Gets human-readable name of options.
Overrides:
`[getName](../../core/options/OptionsGroup.html#getName())` in class `[OptionsGroup](../../core/options/OptionsGroup.html)`
Returns:
human-readable name of options.
loadOptions
public void loadOptions([Style](../../properties/Style.html) style,
 boolean pluginsLoaded)
Overrides:
`loadOptions` in class `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`
afterLoad
protected void afterLoad(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)
Overrides:
`afterLoad` in class `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`
getGroupIcon
public [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getGroupIcon()
Description copied from class: `[OptionsGroup](../../core/options/OptionsGroup.html#getGroupIcon())`
Returns icon to display with options.
Overrides:
`[getGroupIcon](../../core/options/OptionsGroup.html#getGroupIcon())` in class `[OptionsGroup](../../core/options/OptionsGroup.html)`
Returns:
icon to display with options.
getPropertyGroupName
protected static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPropertyGroupName(boolean exportb,
 boolean importb)
setDefaultValues
public void setDefaultValues()
Description copied from class: `[AbstractPropertyOptionsGroup](../../core/options/AbstractPropertyOptionsGroup.html#setDefaultValues())`
Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.
Overrides:
`setDefaultValues` in class `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`
addChoiceProperty
protected final void addChoiceProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] choice,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) selected,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
setAutoExportOption
@OpenApipublic void setAutoExportOption([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) choice)
Set auto-export to Eclipse UML2 XMI on project save option.
Specified by:
`[setAutoExportOption](BaseOptions.html#setAutoExportOption(java.lang.String))` in interface `[BaseOptions](BaseOptions.html)`
See Also:
[`OPTION_ASK_BEFORE_EXPORT`](#OPTION_ASK_BEFORE_EXPORT)
[`OPTION_EXPORT_ALWAYS`](#OPTION_EXPORT_ALWAYS)
[`OPTION_NEVER`](#OPTION_NEVER)
getAutoExportOption
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAutoExportOption()
Get auto-export to Eclipse UML2 XMI option.
Specified by:
`[getAutoExportOption](BaseOptions.html#getAutoExportOption())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
current auto-export choice.
See Also:
[`OPTION_ASK_BEFORE_EXPORT`](#OPTION_ASK_BEFORE_EXPORT)
[`OPTION_EXPORT_ALWAYS`](#OPTION_EXPORT_ALWAYS)
[`OPTION_NEVER`](#OPTION_NEVER)
setAskToOverwriteExportedFiles
@OpenApipublic void setAskToOverwriteExportedFiles(boolean ask)
Set if ask to overwrite exported files.
Specified by:
`[setAskToOverwriteExportedFiles](BaseOptions.html#setAskToOverwriteExportedFiles(boolean))` in interface `[BaseOptions](BaseOptions.html)`
Parameters:
`ask` - true - ask to overwrite, otherwise - overwrite without asking.
isAskToOverwriteExportedFiles
@OpenApipublic boolean isAskToOverwriteExportedFiles()
Chekcks if ask to overwrite exported files.
Specified by:
`[isAskToOverwriteExportedFiles](BaseOptions.html#isAskToOverwriteExportedFiles())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true if ask to overwrite exported files.
setIDExportPolicy
@OpenApipublic void setIDExportPolicy([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) choice)
Set ID export policy
Specified by:
`[setIDExportPolicy](BaseOptions.html#setIDExportPolicy(java.lang.String))` in interface `[BaseOptions](BaseOptions.html)`
Parameters:
`choice` - choice
See Also:
[`BaseOptions.ID_EXPORT_POLICY_GENERATE_ID`](BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID)
[`BaseOptions.ID_EXPORT_POLICY_USE_ELEMENT_ID`](BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID)
[`BaseOptions.ID_EXPORT_POLICY_USE_SERVER_ID`](BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID)
getIDExportPolicy
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getIDExportPolicy()
Get current ID export choice.
Specified by:
`[getIDExportPolicy](BaseOptions.html#getIDExportPolicy())` in interface `[BaseOptions](BaseOptions.html)`
See Also:
[`BaseOptions.ID_EXPORT_POLICY_GENERATE_ID`](BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID)
[`BaseOptions.ID_EXPORT_POLICY_USE_ELEMENT_ID`](BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID)
[`BaseOptions.ID_EXPORT_POLICY_USE_SERVER_ID`](BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID)
setShowMappinWarning
@OpenApipublic void setShowMappinWarning(boolean show)
Set if show warnings about (datatypes, metaclasses) mappings.
Specified by:
`[setShowMappinWarning](BaseOptions.html#setShowMappinWarning(boolean))` in interface `[BaseOptions](BaseOptions.html)`
isShowMappinWarning
@OpenApipublic boolean isShowMappinWarning()
Checks if show warnings about (datatypes, metaclasses) mappings.
Specified by:
`[isShowMappinWarning](BaseOptions.html#isShowMappinWarning())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true if warnings about (datatypes, metaclasses) mapping should be displayed.
setShowStereotypePropertyTypeChangeWarning
@OpenApipublic void setShowStereotypePropertyTypeChangeWarning(boolean show)
Set if show warnings about stereotype property type change.
Specified by:
`[setShowStereotypePropertyTypeChangeWarning](BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean))` in interface `[BaseOptions](BaseOptions.html)`
isShowStereotypePropertyTypeChangeWarning
@OpenApipublic boolean isShowStereotypePropertyTypeChangeWarning()
Check if show warnings about stereotype property type change.
Specified by:
`[isShowStereotypePropertyTypeChangeWarning](BaseOptions.html#isShowStereotypePropertyTypeChangeWarning())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true if warnings about stereotype property type change is displayed.
setShowStereotypeFromSameWarning
@OpenApipublic void setShowStereotypeFromSameWarning(boolean show)
Set if show warnings about not applied stereotypes (from the same profile).
Specified by:
`[setShowStereotypeFromSameWarning](BaseOptions.html#setShowStereotypeFromSameWarning(boolean))` in interface `[BaseOptions](BaseOptions.html)`
isShowStereotypeFromSameWarning
@OpenApipublic boolean isShowStereotypeFromSameWarning()
Checks if show warnings about not applied stereotypes (from the same profile).
Specified by:
`[isShowStereotypeFromSameWarning](BaseOptions.html#isShowStereotypeFromSameWarning())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true if warnings about not applied stereotype should be displayed.
setUseKeywordAsStereotypeName
@OpenApipublic void setUseKeywordAsStereotypeName(boolean use)
Set if stereotype keyword is used as stereotype name on import.
Specified by:
`[setUseKeywordAsStereotypeName](BaseOptions.html#setUseKeywordAsStereotypeName(boolean))` in interface `[BaseOptions](BaseOptions.html)`
isUseKeywordAsStereotypeName
@OpenApipublic boolean isUseKeywordAsStereotypeName()
Checks if stereotype keyword is used as stereotype name on import.
Specified by:
`[isUseKeywordAsStereotypeName](BaseOptions.html#isUseKeywordAsStereotypeName())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true if stereotype keyword is used as stereotype name on import.
setDisplayWarnings
@OpenApipublic void setDisplayWarnings(boolean display)
Set if to show warnings in Message Window on export/import.
Specified by:
`[setDisplayWarnings](BaseOptions.html#setDisplayWarnings(boolean))` in interface `[BaseOptions](BaseOptions.html)`
isDisplayWarnings
@OpenApipublic boolean isDisplayWarnings()
Checks if to show warnings in Message Window on export/import.
Specified by:
`[isDisplayWarnings](BaseOptions.html#isDisplayWarnings())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true if warnings shoud be displayed in Message Window.
setApplyAllProfilesToRootModel
@OpenApipublic void setApplyAllProfilesToRootModel(boolean apply)
Set if to apply all profiles to root Model on export.
Specified by:
`[setApplyAllProfilesToRootModel](BaseOptions.html#setApplyAllProfilesToRootModel(boolean))` in interface `[BaseOptions](BaseOptions.html)`
Parameters:
`apply` - true to apply all profiles to root Model (on export).
isApplyAllProfilesToRootModel
@OpenApipublic boolean isApplyAllProfilesToRootModel()
Checks if to apply all profiles to root Model on export.
Specified by:
`[isApplyAllProfilesToRootModel](BaseOptions.html#isApplyAllProfilesToRootModel())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true on export all profiles will be applied to root Model.
setMoveStereotypeToNestingProfile
@OpenApipublic void setMoveStereotypeToNestingProfile(boolean move)
Set if move stereotype to nesting profile if stereotype is not directly contained by profile.
Specified by:
`[setMoveStereotypeToNestingProfile](BaseOptions.html#setMoveStereotypeToNestingProfile(boolean))` in interface `[BaseOptions](BaseOptions.html)`
Parameters:
`move` - true move stereotype to nesting profile (on export).
isMoveStereotypeToNestingProfile
@OpenApipublic boolean isMoveStereotypeToNestingProfile()
Checks if move stereotype to nesting profile if stereotype is not directly contained by profile.
Specified by:
`[isMoveStereotypeToNestingProfile](BaseOptions.html#isMoveStereotypeToNestingProfile())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true move stereotype to nesting profile (on export).
isAskBeforeExport
public boolean isAskBeforeExport()
Specified by:
`[isAskBeforeExport](BaseOptions.html#isAskBeforeExport())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true when after each project save user is asked if he wants to export to emf.
isAutoExport
public boolean isAutoExport()
Specified by:
`[isAutoExport](BaseOptions.html#isAutoExport())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true when after each save emf export is performed without any questions.
isPreserveIDsOnImport
@OpenApipublic boolean isPreserveIDsOnImport()
Specified by:
`[isPreserveIDsOnImport](BaseOptions.html#isPreserveIDsOnImport())` in interface `[BaseOptions](BaseOptions.html)`
Returns:
true if preserve imported ids.
setPreserveIDsOnImport
@OpenApipublic void setPreserveIDsOnImport(boolean preserve)
addBooleanProperty
protected final void addBooleanProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)
addBooleanProperty
protected final void addBooleanProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group,
 boolean value)
addProperty
public void addProperty([Property](../../properties/Property.html) property)
Description copied from class: `[AbstractPropertyOptionsGroup](../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))`
Adds property to this group. DescriptionID will be reset. To add property with description use
 [`AbstractPropertyOptionsGroup.addProperty(Property, String)`](../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)) method.
Overrides:
`[addProperty](../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property))` in class `[AbstractPropertyOptionsGroup](../../core/options/AbstractPropertyOptionsGroup.html)`
Parameters:
`property` - property to be added.
setBooleanPropertyValue
protected final void setBooleanPropertyValue([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 boolean value)
getBooleanPropertyValue
protected final boolean getBooleanPropertyValue([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
getBooleanProperty
protected final [BooleanProperty](../../properties/BooleanProperty.html) getBooleanProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
getChoice
protected final [ChoiceProperty](../../properties/ChoiceProperty.html) getChoice([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
createPropertyResourceProvider
protected com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider createPropertyResourceProvider()
getBanner
public com.nomagic.ui.banners.Banner getBanner()
Overrides:
`[getBanner](../../core/options/OptionsGroup.html#getBanner())` in class `[OptionsGroup](../../core/options/OptionsGroup.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.envoptions</a></div>
<h1 class="title" title="Class BaseEmfOptionsGroup">Class BaseEmfOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="../../core/options/AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.VersionedOptionsGroup
<div class="inheritance">com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../v2/envoptions/EmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">EmfOptionsGroup</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">BaseEmfOptionsGroup</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.options.VersionedOptionsGroup
implements <a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></span></div>
<div class="block">Eclipse UML2 XMI export/import environment options.</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EMF_OPTIONS_GROUP_ID">EMF_OPTIONS_GROUP_ID</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>protected static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#MOVE_STEREOTYPE_TO_NESTING_PROFILE">MOVE_STEREOTYPE_TO_NESTING_PROFILE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPTION_NEVER">OPTION_NEVER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>CURRENT_EXPORTER_VERSION</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="../../core/options/OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS">ICON_ENVIRONMENT_OPTIONS</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID">ID_EXPORT_POLICY_GENERATE_ID</a>, <a href="BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID">ID_EXPORT_POLICY_USE_ELEMENT_ID</a>, <a href="BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID">ID_EXPORT_POLICY_USE_SERVER_ID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">BaseEmfOptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addBooleanProperty(java.lang.String,java.lang.String)">addBooleanProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addBooleanProperty(java.lang.String,java.lang.String,boolean)">addBooleanProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addChoiceProperty(java.lang.String,java.lang.String%5B%5D,java.lang.String,java.lang.String)">addChoiceProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] choice,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> selected,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a><wbr/>(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds property to this group.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">afterLoad</a><wbr/>(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPropertyResourceProvider()">createPropertyResourceProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoExportOption()">getAutoExportOption</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.banners.Banner</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBanner()">getBanner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseEMFOptions(java.lang.String)">getBaseEMFOptions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a href="../../properties/BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBooleanProperty(java.lang.String)">getBooleanProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBooleanPropertyValue(java.lang.String)">getBooleanPropertyValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a href="../../properties/ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChoice(java.lang.String)">getChoice</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupIcon()">getGroupIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns icon to display with options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIDExportPolicy()">getIDExportPolicy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get current ID export choice.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets human-readable name of options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getPropertyGroupName(boolean,boolean)">getPropertyGroupName</a><wbr/>(boolean exportb,
 boolean importb)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if to apply all profiles to root Model on export.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAskBeforeExport()">isAskBeforeExport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Chekcks if ask to overwrite exported files.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoExport()">isAutoExport</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDisplayWarnings()">isDisplayWarnings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if to show warnings in Message Window on export/import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isPreserveIDsOnImport()">isPreserveIDsOnImport</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowMappinWarning()">isShowMappinWarning</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if show warnings about (datatypes, metaclasses) mappings.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if show warnings about not applied stereotypes (from the same profile).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if show warnings about stereotype property type change.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if stereotype keyword is used as stereotype name on import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadOptions(com.nomagic.magicdraw.properties.Style,boolean)">loadOptions</a><wbr/>(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style,
 boolean pluginsLoaded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#registerOptions(com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup)">registerOptions</a><wbr/>(<a href="BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a><wbr/>(boolean apply)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if to apply all profiles to root Model on export.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a><wbr/>(boolean ask)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if ask to overwrite exported files.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoExportOption(java.lang.String)">setAutoExportOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set auto-export to Eclipse UML2 XMI on project save option.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBooleanPropertyValue(java.lang.String,boolean)">setBooleanPropertyValue</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultValues()">setDefaultValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default values for the properties contained in this group.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayWarnings(boolean)">setDisplayWarnings</a><wbr/>(boolean display)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if to show warnings in Message Window on export/import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set ID export policy</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a><wbr/>(boolean move)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPreserveIDsOnImport(boolean)">setPreserveIDsOnImport</a><wbr/>(boolean preserve)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowMappinWarning(boolean)">setShowMappinWarning</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if show warnings about (datatypes, metaclasses) mappings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if show warnings about not applied stereotypes (from the same profile).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if show warnings about stereotype property type change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a><wbr/>(boolean use)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if stereotype keyword is used as stereotype name on import.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="../../core/options/AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)">afterLoadAdditionalAction</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#clone()">clone</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#createDefault()">createDefault</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#createOptions()">createOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#createOptionsPanel()">createOptionsPanel</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)">fixProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#getCopy()">getCopy</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#hasVisibleOptions()">hasVisibleOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="../../core/options/OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)">add</a>, <a href="../../core/options/OptionsGroup.html#afterSave()">afterSave</a>, <a href="../../core/options/OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)">canDisplay</a>, <a href="../../core/options/OptionsGroup.html#firstInit(boolean)">firstInit</a>, <a href="../../core/options/OptionsGroup.html#getChildren()">getChildren</a>, <a href="../../core/options/OptionsGroup.html#getIcon()">getIcon</a>, <a href="../../core/options/OptionsGroup.html#getId()">getId</a>, <a href="../../core/options/OptionsGroup.html#getModelingLanguage()">getModelingLanguage</a>, <a href="../../core/options/OptionsGroup.html#getParent()">getParent</a>, <a href="../../core/options/OptionsGroup.html#isEnabled()">isEnabled</a>, <a href="../../core/options/OptionsGroup.html#isVisible()">isVisible</a>, <a href="../../core/options/OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)">remove</a>, <a href="../../core/options/OptionsGroup.html#resetCachedValues()">resetCachedValues</a>, <a href="../../core/options/OptionsGroup.html#setEnabled(boolean)">setEnabled</a>, <a href="../../core/options/OptionsGroup.html#setVisible(boolean)">setVisible</a>, <a href="../../core/options/OptionsGroup.html#sortChildren(java.util.Comparator)">sortChildren</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="OPTION_EXPORT_ALWAYS">
<h3>OPTION_EXPORT_ALWAYS</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_EXPORT_ALWAYS</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_EXPORT_ALWAYS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPTION_ASK_BEFORE_EXPORT">
<h3>OPTION_ASK_BEFORE_EXPORT</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_ASK_BEFORE_EXPORT</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_ASK_BEFORE_EXPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPTION_NEVER">
<h3>OPTION_NEVER</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_NEVER</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_NEVER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="MOVE_STEREOTYPE_TO_NESTING_PROFILE">
<h3>MOVE_STEREOTYPE_TO_NESTING_PROFILE</h3>
<div class="member-signature"><span class="modifiers">protected static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">MOVE_STEREOTYPE_TO_NESTING_PROFILE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.MOVE_STEREOTYPE_TO_NESTING_PROFILE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EMF_OPTIONS_GROUP_ID">
<h3>EMF_OPTIONS_GROUP_ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EMF_OPTIONS_GROUP_ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.EMF_OPTIONS_GROUP_ID">Constant Field Values</a></li>
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
<h3>BaseEmfOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BaseEmfOptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
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
<section class="detail" id="registerOptions(com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup)">
<h3>registerOptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></span> <span class="element-name">registerOptions</span><wbr/><span class="parameters">(<a href="BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a> options)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBaseEMFOptions(java.lang.String)">
<h3>getBaseEMFOptions</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></span> <span class="element-name">getBaseEMFOptions</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> optionsGroupID)</span></div>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../core/options/OptionsGroup.html#getName()">OptionsGroup</a></code></span></div>
<div class="block">Gets human-readable name of options.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../core/options/OptionsGroup.html#getName()">getName</a></code> in class <code><a href="../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></code></dd>
<dt>Returns:</dt>
<dd>human-readable name of options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadOptions(com.nomagic.magicdraw.properties.Style,boolean)">
<h3>loadOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadOptions</span><wbr/><span class="parameters">(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style,
 boolean pluginsLoaded)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>loadOptions</code> in class <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
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
<dd><code>afterLoad</code> in class <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGroupIcon()">
<h3>getGroupIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getGroupIcon</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../core/options/OptionsGroup.html#getGroupIcon()">OptionsGroup</a></code></span></div>
<div class="block">Returns icon to display with options.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../core/options/OptionsGroup.html#getGroupIcon()">getGroupIcon</a></code> in class <code><a href="../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></code></dd>
<dt>Returns:</dt>
<dd>icon to display with options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPropertyGroupName(boolean,boolean)">
<h3>getPropertyGroupName</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPropertyGroupName</span><wbr/><span class="parameters">(boolean exportb,
 boolean importb)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDefaultValues()">
<h3>setDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultValues</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../core/options/AbstractPropertyOptionsGroup.html#setDefaultValues()">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>setDefaultValues</code> in class <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addChoiceProperty(java.lang.String,java.lang.String[],java.lang.String,java.lang.String)">
<h3>addChoiceProperty</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">addChoiceProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] choice,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> selected,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="setAutoExportOption(java.lang.String)">
<h3>setAutoExportOption</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoExportOption</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</span></div>
<div class="block">Set auto-export to Eclipse UML2 XMI on project save option.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setAutoExportOption(java.lang.String)">setAutoExportOption</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#OPTION_ASK_BEFORE_EXPORT"><code>OPTION_ASK_BEFORE_EXPORT</code></a></li>
<li><a href="#OPTION_EXPORT_ALWAYS"><code>OPTION_EXPORT_ALWAYS</code></a></li>
<li><a href="#OPTION_NEVER"><code>OPTION_NEVER</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAutoExportOption()">
<h3>getAutoExportOption</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAutoExportOption</span>()</div>
<div class="block">Get auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#getAutoExportOption()">getAutoExportOption</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>current auto-export choice.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="#OPTION_ASK_BEFORE_EXPORT"><code>OPTION_ASK_BEFORE_EXPORT</code></a></li>
<li><a href="#OPTION_EXPORT_ALWAYS"><code>OPTION_EXPORT_ALWAYS</code></a></li>
<li><a href="#OPTION_NEVER"><code>OPTION_NEVER</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAskToOverwriteExportedFiles(boolean)">
<h3>setAskToOverwriteExportedFiles</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAskToOverwriteExportedFiles</span><wbr/><span class="parameters">(boolean ask)</span></div>
<div class="block">Set if ask to overwrite exported files.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Parameters:</dt>
<dd><code>ask</code> - true - ask to overwrite, otherwise - overwrite without asking.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAskToOverwriteExportedFiles()">
<h3>isAskToOverwriteExportedFiles</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAskToOverwriteExportedFiles</span>()</div>
<div class="block">Chekcks if ask to overwrite exported files.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true if ask to overwrite exported files.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIDExportPolicy(java.lang.String)">
<h3>setIDExportPolicy</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIDExportPolicy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</span></div>
<div class="block">Set ID export policy</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Parameters:</dt>
<dd><code>choice</code> - choice</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID"><code>BaseOptions.ID_EXPORT_POLICY_GENERATE_ID</code></a></li>
<li><a href="BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID"><code>BaseOptions.ID_EXPORT_POLICY_USE_ELEMENT_ID</code></a></li>
<li><a href="BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID"><code>BaseOptions.ID_EXPORT_POLICY_USE_SERVER_ID</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIDExportPolicy()">
<h3>getIDExportPolicy</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIDExportPolicy</span>()</div>
<div class="block">Get current ID export choice.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#getIDExportPolicy()">getIDExportPolicy</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID"><code>BaseOptions.ID_EXPORT_POLICY_GENERATE_ID</code></a></li>
<li><a href="BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID"><code>BaseOptions.ID_EXPORT_POLICY_USE_ELEMENT_ID</code></a></li>
<li><a href="BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID"><code>BaseOptions.ID_EXPORT_POLICY_USE_SERVER_ID</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowMappinWarning(boolean)">
<h3>setShowMappinWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowMappinWarning</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set if show warnings about (datatypes, metaclasses) mappings.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setShowMappinWarning(boolean)">setShowMappinWarning</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowMappinWarning()">
<h3>isShowMappinWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowMappinWarning</span>()</div>
<div class="block">Checks if show warnings about (datatypes, metaclasses) mappings.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isShowMappinWarning()">isShowMappinWarning</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true if warnings about (datatypes, metaclasses) mapping should be displayed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowStereotypePropertyTypeChangeWarning(boolean)">
<h3>setShowStereotypePropertyTypeChangeWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowStereotypePropertyTypeChangeWarning</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set if show warnings about stereotype property type change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowStereotypePropertyTypeChangeWarning()">
<h3>isShowStereotypePropertyTypeChangeWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowStereotypePropertyTypeChangeWarning</span>()</div>
<div class="block">Check if show warnings about stereotype property type change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true if warnings about stereotype property type change is displayed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowStereotypeFromSameWarning(boolean)">
<h3>setShowStereotypeFromSameWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowStereotypeFromSameWarning</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set if show warnings about not applied stereotypes (from the same profile).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowStereotypeFromSameWarning()">
<h3>isShowStereotypeFromSameWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShowStereotypeFromSameWarning</span>()</div>
<div class="block">Checks if show warnings about not applied stereotypes (from the same profile).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true if warnings about not applied stereotype should be displayed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseKeywordAsStereotypeName(boolean)">
<h3>setUseKeywordAsStereotypeName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUseKeywordAsStereotypeName</span><wbr/><span class="parameters">(boolean use)</span></div>
<div class="block">Set if stereotype keyword is used as stereotype name on import.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseKeywordAsStereotypeName()">
<h3>isUseKeywordAsStereotypeName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseKeywordAsStereotypeName</span>()</div>
<div class="block">Checks if stereotype keyword is used as stereotype name on import.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true if stereotype keyword is used as stereotype name on import.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayWarnings(boolean)">
<h3>setDisplayWarnings</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDisplayWarnings</span><wbr/><span class="parameters">(boolean display)</span></div>
<div class="block">Set if to show warnings in Message Window on export/import.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setDisplayWarnings(boolean)">setDisplayWarnings</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayWarnings()">
<h3>isDisplayWarnings</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDisplayWarnings</span>()</div>
<div class="block">Checks if to show warnings in Message Window on export/import.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isDisplayWarnings()">isDisplayWarnings</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true if warnings shoud be displayed in Message Window.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplyAllProfilesToRootModel(boolean)">
<h3>setApplyAllProfilesToRootModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setApplyAllProfilesToRootModel</span><wbr/><span class="parameters">(boolean apply)</span></div>
<div class="block">Set if to apply all profiles to root Model on export.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Parameters:</dt>
<dd><code>apply</code> - true to apply all profiles to root Model (on export).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isApplyAllProfilesToRootModel()">
<h3>isApplyAllProfilesToRootModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isApplyAllProfilesToRootModel</span>()</div>
<div class="block">Checks if to apply all profiles to root Model on export.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true on export all profiles will be applied to root Model.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMoveStereotypeToNestingProfile(boolean)">
<h3>setMoveStereotypeToNestingProfile</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMoveStereotypeToNestingProfile</span><wbr/><span class="parameters">(boolean move)</span></div>
<div class="block">Set if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Parameters:</dt>
<dd><code>move</code> - true move stereotype to nesting profile (on export).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMoveStereotypeToNestingProfile()">
<h3>isMoveStereotypeToNestingProfile</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMoveStereotypeToNestingProfile</span>()</div>
<div class="block">Checks if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true move stereotype to nesting profile (on export).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAskBeforeExport()">
<h3>isAskBeforeExport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAskBeforeExport</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isAskBeforeExport()">isAskBeforeExport</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true when after each project save user is asked if he wants to export to emf.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAutoExport()">
<h3>isAutoExport</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutoExport</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isAutoExport()">isAutoExport</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true when after each save emf export is performed without any questions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPreserveIDsOnImport()">
<h3>isPreserveIDsOnImport</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPreserveIDsOnImport</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#isPreserveIDsOnImport()">isPreserveIDsOnImport</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>true if preserve imported ids.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPreserveIDsOnImport(boolean)">
<h3>setPreserveIDsOnImport</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPreserveIDsOnImport</span><wbr/><span class="parameters">(boolean preserve)</span></div>
</section>
</li>
<li>
<section class="detail" id="addBooleanProperty(java.lang.String,java.lang.String)">
<h3>addBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">addBooleanProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="addBooleanProperty(java.lang.String,java.lang.String,boolean)">
<h3>addBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">addBooleanProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> group,
 boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="addProperty(com.nomagic.magicdraw.properties.Property)">
<h3>addProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addProperty</span><wbr/><span class="parameters">(<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> property)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Adds property to this group. DescriptionID will be reset. To add property with description use
 <a href="../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)"><code>AbstractPropertyOptionsGroup.addProperty(Property, String)</code></a> method.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a></code> in class <code><a href="../../core/options/AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></code></dd>
<dt>Parameters:</dt>
<dd><code>property</code> - property to be added.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBooleanPropertyValue(java.lang.String,boolean)">
<h3>setBooleanPropertyValue</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">void</span> <span class="element-name">setBooleanPropertyValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBooleanPropertyValue(java.lang.String)">
<h3>getBooleanPropertyValue</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type">boolean</span> <span class="element-name">getBooleanPropertyValue</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBooleanProperty(java.lang.String)">
<h3>getBooleanProperty</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a href="../../properties/BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></span> <span class="element-name">getBooleanProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="getChoice(java.lang.String)">
<h3>getChoice</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a href="../../properties/ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></span> <span class="element-name">getChoice</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="createPropertyResourceProvider()">
<h3>createPropertyResourceProvider</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.BaseEmfOptionsPropertyResourceProvider</span> <span class="element-name">createPropertyResourceProvider</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getBanner()">
<h3>getBanner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.banners.Banner</span> <span class="element-name">getBanner</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../../core/options/OptionsGroup.html#getBanner()">getBanner</a></code> in class <code><a href="../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></code></dd>
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
