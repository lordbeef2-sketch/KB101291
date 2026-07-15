# JAVA OPENAPI: EmfOptionsGroup (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/emfuml2xmi/v2/envoptions/EmfOptionsGroup.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/v2/envoptions/EmfOptionsGroup.html`
- source_sha256: `143f66775f0ee90a4eaa27fc39cdc62ff9698793c9e81c2ec2dafb0df27069c0`
- captured_utc: `2026-07-14T16:51:19.050176+00:00`

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
Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)
`[OPTION_ASK_BEFORE_EXPORT](../../envoptions/BaseEmfOptionsGroup.html#OPTION_ASK_BEFORE_EXPORT), [OPTION_EXPORT_ALWAYS](../../envoptions/BaseEmfOptionsGroup.html#OPTION_EXPORT_ALWAYS), [OPTION_NEVER](../../envoptions/BaseEmfOptionsGroup.html#OPTION_NEVER)`
Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`CURRENT_EXPORTER_VERSION`
Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](../../envoptions/BaseOptions.html)
`[ID_EXPORT_POLICY_GENERATE_ID](../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID), [ID_EXPORT_POLICY_USE_ELEMENT_ID](../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID), [ID_EXPORT_POLICY_USE_SERVER_ID](../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID), [OPTION_ASK_BEFORE_EXPORT](../../envoptions/BaseOptions.html#OPTION_ASK_BEFORE_EXPORT), [OPTION_EXPORT_ALWAYS](../../envoptions/BaseOptions.html#OPTION_EXPORT_ALWAYS), [OPTION_NEVER](../../envoptions/BaseOptions.html#OPTION_NEVER)`
Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.[Options](Options.html)
`[CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS), [CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE), [CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS](Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`static [EmfOptionsGroup](EmfOptionsGroup.html)`
`[getEMFOptions](#getEMFOptions())()`
Get the Eclipse UML2 XMI v2.x export/import options.
`boolean`
`[isChangeStereotypePropertyTypeStereotype](#isChangeStereotypePropertyTypeStereotype())()`
Checks if to change stereotype property type stereotype to metaclass on export.
`void`
`[setChangeStereotypePropertyTypeStereotype](#setChangeStereotypePropertyTypeStereotype(boolean))(boolean change)`
Set if to change stereotype property type stereotype to metaclass on export.
Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseEmfOptionsGroup](../../envoptions/BaseEmfOptionsGroup.html)
`[getAutoExportOption](../../envoptions/BaseEmfOptionsGroup.html#getAutoExportOption()), [getIDExportPolicy](../../envoptions/BaseEmfOptionsGroup.html#getIDExportPolicy()), [isApplyAllProfilesToRootModel](../../envoptions/BaseEmfOptionsGroup.html#isApplyAllProfilesToRootModel()), [isAskToOverwriteExportedFiles](../../envoptions/BaseEmfOptionsGroup.html#isAskToOverwriteExportedFiles()), [isDisplayWarnings](../../envoptions/BaseEmfOptionsGroup.html#isDisplayWarnings()), [isMoveStereotypeToNestingProfile](../../envoptions/BaseEmfOptionsGroup.html#isMoveStereotypeToNestingProfile()), [isPreserveIDsOnImport](../../envoptions/BaseEmfOptionsGroup.html#isPreserveIDsOnImport()), [isShowMappinWarning](../../envoptions/BaseEmfOptionsGroup.html#isShowMappinWarning()), [isShowStereotypeFromSameWarning](../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypeFromSameWarning()), [isShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypePropertyTypeChangeWarning()), [isUseKeywordAsStereotypeName](../../envoptions/BaseEmfOptionsGroup.html#isUseKeywordAsStereotypeName()), [setApplyAllProfilesToRootModel](../../envoptions/BaseEmfOptionsGroup.html#setApplyAllProfilesToRootModel(boolean)), [setAskToOverwriteExportedFiles](../../envoptions/BaseEmfOptionsGroup.html#setAskToOverwriteExportedFiles(boolean)), [setAutoExportOption](../../envoptions/BaseEmfOptionsGroup.html#setAutoExportOption(java.lang.String)), [setDisplayWarnings](../../envoptions/BaseEmfOptionsGroup.html#setDisplayWarnings(boolean)), [setIDExportPolicy](../../envoptions/BaseEmfOptionsGroup.html#setIDExportPolicy(java.lang.String)), [setMoveStereotypeToNestingProfile](../../envoptions/BaseEmfOptionsGroup.html#setMoveStereotypeToNestingProfile(boolean)), [setPreserveIDsOnImport](../../envoptions/BaseEmfOptionsGroup.html#setPreserveIDsOnImport(boolean)), [setShowMappinWarning](../../envoptions/BaseEmfOptionsGroup.html#setShowMappinWarning(boolean)), [setShowStereotypeFromSameWarning](../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypeFromSameWarning(boolean)), [setShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypePropertyTypeChangeWarning(boolean)), [setUseKeywordAsStereotypeName](../../envoptions/BaseEmfOptionsGroup.html#setUseKeywordAsStereotypeName(boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](../../../core/options/AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](../../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [getOptions](../../../core/options/AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](../../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](../../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()), [removeProperty](../../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](../../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](../../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](../../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](../../../core/options/OptionsGroup.html)
`[getIcon](../../../core/options/OptionsGroup.html#getIcon())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](../../envoptions/BaseOptions.html)
`[getAutoExportOption](../../envoptions/BaseOptions.html#getAutoExportOption()), [getIDExportPolicy](../../envoptions/BaseOptions.html#getIDExportPolicy()), [isApplyAllProfilesToRootModel](../../envoptions/BaseOptions.html#isApplyAllProfilesToRootModel()), [isAskToOverwriteExportedFiles](../../envoptions/BaseOptions.html#isAskToOverwriteExportedFiles()), [isDisplayWarnings](../../envoptions/BaseOptions.html#isDisplayWarnings()), [isMoveStereotypeToNestingProfile](../../envoptions/BaseOptions.html#isMoveStereotypeToNestingProfile()), [isShowMappinWarning](../../envoptions/BaseOptions.html#isShowMappinWarning()), [isShowStereotypeFromSameWarning](../../envoptions/BaseOptions.html#isShowStereotypeFromSameWarning()), [isShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseOptions.html#isShowStereotypePropertyTypeChangeWarning()), [isUseKeywordAsStereotypeName](../../envoptions/BaseOptions.html#isUseKeywordAsStereotypeName()), [setApplyAllProfilesToRootModel](../../envoptions/BaseOptions.html#setApplyAllProfilesToRootModel(boolean)), [setAskToOverwriteExportedFiles](../../envoptions/BaseOptions.html#setAskToOverwriteExportedFiles(boolean)), [setAutoExportOption](../../envoptions/BaseOptions.html#setAutoExportOption(java.lang.String)), [setDisplayWarnings](../../envoptions/BaseOptions.html#setDisplayWarnings(boolean)), [setIDExportPolicy](../../envoptions/BaseOptions.html#setIDExportPolicy(java.lang.String)), [setMoveStereotypeToNestingProfile](../../envoptions/BaseOptions.html#setMoveStereotypeToNestingProfile(boolean)), [setShowMappinWarning](../../envoptions/BaseOptions.html#setShowMappinWarning(boolean)), [setShowStereotypeFromSameWarning](../../envoptions/BaseOptions.html#setShowStereotypeFromSameWarning(boolean)), [setShowStereotypePropertyTypeChangeWarning](../../envoptions/BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean)), [setUseKeywordAsStereotypeName](../../envoptions/BaseOptions.html#setUseKeywordAsStereotypeName(boolean))`

============ METHOD DETAIL ========== 
Method Details
getEMFOptions
@OpenApipublic static [EmfOptionsGroup](EmfOptionsGroup.html) getEMFOptions()
Get the Eclipse UML2 XMI v2.x export/import options. Options must accessed only after the application is started.
Returns:
loaded options.
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
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup">Fields inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></h3>
<code><a href="../../envoptions/BaseEmfOptionsGroup.html#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#OPTION_NEVER">OPTION_NEVER</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>CURRENT_EXPORTER_VERSION</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID">ID_EXPORT_POLICY_GENERATE_ID</a>, <a href="../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID">ID_EXPORT_POLICY_USE_ELEMENT_ID</a>, <a href="../../envoptions/BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID">ID_EXPORT_POLICY_USE_SERVER_ID</a>, <a href="../../envoptions/BaseOptions.html#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a>, <a href="../../envoptions/BaseOptions.html#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a>, <a href="../../envoptions/BaseOptions.html#OPTION_NEVER">OPTION_NEVER</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.Options">Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.v2.envoptions.<a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></h3>
<code><a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS</a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE</a>, <a href="Options.html#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="EmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">EmfOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getEMFOptions()">getEMFOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get the Eclipse UML2 XMI v2.x export/import options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isChangeStereotypePropertyTypeStereotype()">isChangeStereotypePropertyTypeStereotype</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if to change stereotype property type stereotype to metaclass on export.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangeStereotypePropertyTypeStereotype(boolean)">setChangeStereotypePropertyTypeStereotype</a><wbr/>(boolean change)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set if to change stereotype property type stereotype to metaclass on export.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseEmfOptionsGroup">Methods inherited from class com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></h3>
<code><a href="../../envoptions/BaseEmfOptionsGroup.html#getAutoExportOption()">getAutoExportOption</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#getIDExportPolicy()">getIDExportPolicy</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isDisplayWarnings()">isDisplayWarnings</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isPreserveIDsOnImport()">isPreserveIDsOnImport</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isShowMappinWarning()">isShowMappinWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setAutoExportOption(java.lang.String)">setAutoExportOption</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setDisplayWarnings(boolean)">setDisplayWarnings</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setPreserveIDsOnImport(boolean)">setPreserveIDsOnImport</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setShowMappinWarning(boolean)">setShowMappinWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseEmfOptionsGroup.html#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>beforeLoad, getExporterVersion, getOptionsToSave, isExporterVersionEarlier, isExporterVersionEarlier</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="../../../core/options/AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="../../../core/options/AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="../../../core/options/AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="../../../core/options/OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="../../../core/options/OptionsGroup.html#getIcon()">getIcon</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="../../envoptions/BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="../../envoptions/BaseOptions.html#getAutoExportOption()">getAutoExportOption</a>, <a href="../../envoptions/BaseOptions.html#getIDExportPolicy()">getIDExportPolicy</a>, <a href="../../envoptions/BaseOptions.html#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseOptions.html#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseOptions.html#isDisplayWarnings()">isDisplayWarnings</a>, <a href="../../envoptions/BaseOptions.html#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseOptions.html#isShowMappinWarning()">isShowMappinWarning</a>, <a href="../../envoptions/BaseOptions.html#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseOptions.html#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseOptions.html#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a>, <a href="../../envoptions/BaseOptions.html#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a>, <a href="../../envoptions/BaseOptions.html#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a>, <a href="../../envoptions/BaseOptions.html#setAutoExportOption(java.lang.String)">setAutoExportOption</a>, <a href="../../envoptions/BaseOptions.html#setDisplayWarnings(boolean)">setDisplayWarnings</a>, <a href="../../envoptions/BaseOptions.html#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a>, <a href="../../envoptions/BaseOptions.html#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a>, <a href="../../envoptions/BaseOptions.html#setShowMappinWarning(boolean)">setShowMappinWarning</a>, <a href="../../envoptions/BaseOptions.html#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a>, <a href="../../envoptions/BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a>, <a href="../../envoptions/BaseOptions.html#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a></code></div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
