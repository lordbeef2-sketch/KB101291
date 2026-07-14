# JAVA OPENAPI: BaseEmfOptionsGroup (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/emfuml2xmi/envoptions/BaseEmfOptionsGroup.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/envoptions/BaseEmfOptionsGroup.html`
- source_sha256: `ff7395572418a26aca5c48dfcc46588ef16140ae75433e87bed8e43b38698268`
- captured_utc: `2026-07-14T16:45:33.858452+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.envoptions](package-summary.html)

## Class BaseEmfOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](../../core/options/OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](../../core/options/AbstractPropertyOptionsGroup.html)
com.nomagic.magicdraw.core.options.VersionedOptionsGroup
com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup

All Implemented Interfaces:
`[BaseOptions](BaseOptions.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

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
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPTION_ASK_BEFORE_EXPORT](#OPTION_ASK_BEFORE_EXPORT)`
Auto-export to Eclipse UML2 XMI option.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPTION_EXPORT_ALWAYS](#OPTION_EXPORT_ALWAYS)`
Auto-export to Eclipse UML2 XMI option.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPTION_NEVER](#OPTION_NEVER)`
Auto-export to Eclipse UML2 XMI option.
Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`CURRENT_EXPORTER_VERSION`
Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](BaseOptions.html)
`[ID_EXPORT_POLICY_GENERATE_ID](BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID), [ID_EXPORT_POLICY_USE_ELEMENT_ID](BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID), [ID_EXPORT_POLICY_USE_SERVER_ID](BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getAutoExportOption](#getAutoExportOption())()`
Get auto-export to Eclipse UML2 XMI option.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getIDExportPolicy](#getIDExportPolicy())()`
Get current ID export choice.
`boolean`
`[isApplyAllProfilesToRootModel](#isApplyAllProfilesToRootModel())()`
Checks if to apply all profiles to root Model on export.
`boolean`
`[isAskToOverwriteExportedFiles](#isAskToOverwriteExportedFiles())()`
Chekcks if ask to overwrite exported files.
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
`[setApplyAllProfilesToRootModel](#setApplyAllProfilesToRootModel(boolean))(boolean apply)`
Set if to apply all profiles to root Model on export.
`void`
`[setAskToOverwriteExportedFiles](#setAskToOverwriteExportedFiles(boolean))(boolean ask)`
Set if ask to overwrite exported files.
`void`
`[setAutoExportOption](#setAutoExportOption(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) choice)`
Set auto-export to Eclipse UML2 XMI on project save option.
`void`
`[setDisplayWarnings](#setDisplayWarnings(boolean))(boolean display)`
Set if to show warnings in Message Window on export/import.
`void`
`[setIDExportPolicy](#setIDExportPolicy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) choice)`
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
`[addInvisibleProperty](../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [getOptions](../../core/options/AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()), [removeProperty](../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
OPTION_EXPORT_ALWAYS
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPTION_EXPORT_ALWAYS
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_EXPORT_ALWAYS)
OPTION_ASK_BEFORE_EXPORT
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPTION_ASK_BEFORE_EXPORT
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_ASK_BEFORE_EXPORT)
OPTION_NEVER
@OpenApipublic static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPTION_NEVER
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_NEVER)
 ============ METHOD DETAIL ========== 
Method Details
setAutoExportOption
@OpenApipublic void setAutoExportOption([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) choice)
Set auto-export to Eclipse UML2 XMI on project save option.
Specified by:
`[setAutoExportOption](BaseOptions.html#setAutoExportOption(java.lang.String))` in interface `[BaseOptions](BaseOptions.html)`
Parameters:
`choice` -
See Also:
[`OPTION_ASK_BEFORE_EXPORT`](#OPTION_ASK_BEFORE_EXPORT)
[`OPTION_EXPORT_ALWAYS`](#OPTION_EXPORT_ALWAYS)
[`OPTION_NEVER`](#OPTION_NEVER)
getAutoExportOption
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getAutoExportOption()
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
@OpenApipublic void setIDExportPolicy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) choice)
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
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getIDExportPolicy()
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
Parameters:
`show` -
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
Parameters:
`show` -
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
Parameters:
`show` -
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
Parameters:
`use` -
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
Parameters:
`display` -
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
isPreserveIDsOnImport
@OpenApipublic boolean isPreserveIDsOnImport()
Returns:
true if preserve imported ids.
setPreserveIDsOnImport
@OpenApipublic void setPreserveIDsOnImport(boolean preserve)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.envoptions</a></div>
<h1 class="title" title="Class BaseEmfOptionsGroup">Class BaseEmfOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
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
<dd><code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPTION_NEVER">OPTION_NEVER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>CURRENT_EXPORTER_VERSION</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID">ID_EXPORT_POLICY_GENERATE_ID</a>, <a href="BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID">ID_EXPORT_POLICY_USE_ELEMENT_ID</a>, <a href="BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID">ID_EXPORT_POLICY_USE_SERVER_ID</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAutoExportOption()">getAutoExportOption</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIDExportPolicy()">getIDExportPolicy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get current ID export choice.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if to apply all profiles to root Model on export.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Chekcks if ask to overwrite exported files.</div>
</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoExportOption(java.lang.String)">setAutoExportOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set auto-export to Eclipse UML2 XMI on project save option.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDisplayWarnings(boolean)">setDisplayWarnings</a><wbr/>(boolean display)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if to show warnings in Message Window on export/import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</code></div>
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
<code><a href="../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_EXPORT_ALWAYS</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_ASK_BEFORE_EXPORT</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_NEVER</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup.OPTION_NEVER">Constant Field Values</a></li>
</ul>
</dd>
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
<section class="detail" id="setAutoExportOption(java.lang.String)">
<h3>setAutoExportOption</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoExportOption</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</span></div>
<div class="block">Set auto-export to Eclipse UML2 XMI on project save option.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setAutoExportOption(java.lang.String)">setAutoExportOption</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Parameters:</dt>
<dd><code>choice</code> - </dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAutoExportOption</span>()</div>
<div class="block">Get auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#getAutoExportOption()">getAutoExportOption</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Returns:</dt>
<dd>current auto-export choice.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
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
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIDExportPolicy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</span></div>
<div class="block">Set ID export policy</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>Parameters:</dt>
<dd><code>choice</code> - choice</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
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
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIDExportPolicy</span>()</div>
<div class="block">Get current ID export choice.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="BaseOptions.html#getIDExportPolicy()">getIDExportPolicy</a></code> in interface <code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
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
<dt>Parameters:</dt>
<dd><code>show</code> - </dd>
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
<dt>Parameters:</dt>
<dd><code>show</code> - </dd>
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
<dt>Parameters:</dt>
<dd><code>show</code> - </dd>
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
<dt>Parameters:</dt>
<dd><code>use</code> - </dd>
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
<dt>Parameters:</dt>
<dd><code>display</code> - </dd>
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
<section class="detail" id="isPreserveIDsOnImport()">
<h3>isPreserveIDsOnImport</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPreserveIDsOnImport</span>()</div>
<dl class="notes">
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
