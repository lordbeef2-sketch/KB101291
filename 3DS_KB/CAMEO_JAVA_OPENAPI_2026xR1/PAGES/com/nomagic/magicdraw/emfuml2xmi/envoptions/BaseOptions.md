# JAVA OPENAPI: BaseOptions (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/emfuml2xmi/envoptions/BaseOptions.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/envoptions/BaseOptions.html`
- source_sha256: `0816a87fd4728af07ad0dd50fc87ec12a52c9a97e99902303066f1a4bd876449`
- captured_utc: `2026-07-14T16:45:34.301461+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.envoptions](package-summary.html)

## Interface BaseOptions

All Known Subinterfaces:
`[Options](Options.html)`, `[Options](../v2/envoptions/Options.html)`

All Known Implementing Classes:
`[BaseEmfOptionsGroup](BaseEmfOptionsGroup.html)`, `[EmfOptionsGroup](../v2/envoptions/EmfOptionsGroup.html)`

@OpenApipublic interfaceBaseOptions

Eclipse UML2 XMI export/import environment options.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ID_EXPORT_POLICY_GENERATE_ID](#ID_EXPORT_POLICY_GENERATE_ID)`
ID export policy generate id choice.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ID_EXPORT_POLICY_USE_ELEMENT_ID](#ID_EXPORT_POLICY_USE_ELEMENT_ID)`
ID export policy use element id choice.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[ID_EXPORT_POLICY_USE_SERVER_ID](#ID_EXPORT_POLICY_USE_SERVER_ID)`
ID export policy use server id choice.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPTION_ASK_BEFORE_EXPORT](#OPTION_ASK_BEFORE_EXPORT)`
Auto-export to Eclipse UML2 XMI option.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPTION_EXPORT_ALWAYS](#OPTION_EXPORT_ALWAYS)`
Auto-export to Eclipse UML2 XMI option.
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[OPTION_NEVER](#OPTION_NEVER)`
Auto-export to Eclipse UML2 XMI option.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
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

============ FIELD DETAIL =========== 
Field Details
OPTION_EXPORT_ALWAYS
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPTION_EXPORT_ALWAYS
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.OPTION_EXPORT_ALWAYS)
OPTION_ASK_BEFORE_EXPORT
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPTION_ASK_BEFORE_EXPORT
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.OPTION_ASK_BEFORE_EXPORT)
OPTION_NEVER
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) OPTION_NEVER
Auto-export to Eclipse UML2 XMI option.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.OPTION_NEVER)
ID_EXPORT_POLICY_GENERATE_ID
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ID_EXPORT_POLICY_GENERATE_ID
ID export policy generate id choice.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.ID_EXPORT_POLICY_GENERATE_ID)
ID_EXPORT_POLICY_USE_ELEMENT_ID
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ID_EXPORT_POLICY_USE_ELEMENT_ID
ID export policy use element id choice.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.ID_EXPORT_POLICY_USE_ELEMENT_ID)
ID_EXPORT_POLICY_USE_SERVER_ID
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) ID_EXPORT_POLICY_USE_SERVER_ID
ID export policy use server id choice.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.ID_EXPORT_POLICY_USE_SERVER_ID)
 ============ METHOD DETAIL ========== 
Method Details
setAutoExportOption
@OpenApivoid setAutoExportOption([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) choice)
Set auto-export to Eclipse UML2 XMI on project save option.
Parameters:
`choice` -
See Also:
[`OPTION_ASK_BEFORE_EXPORT`](#OPTION_ASK_BEFORE_EXPORT)
[`OPTION_EXPORT_ALWAYS`](#OPTION_EXPORT_ALWAYS)
[`OPTION_NEVER`](#OPTION_NEVER)
getAutoExportOption
@OpenApi[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getAutoExportOption()
Get auto-export to Eclipse UML2 XMI option.
Returns:
current auto-export choice.
See Also:
[`OPTION_ASK_BEFORE_EXPORT`](#OPTION_ASK_BEFORE_EXPORT)
[`OPTION_EXPORT_ALWAYS`](#OPTION_EXPORT_ALWAYS)
[`OPTION_NEVER`](#OPTION_NEVER)
setAskToOverwriteExportedFiles
@OpenApivoid setAskToOverwriteExportedFiles(boolean ask)
Set if ask to overwrite exported files.
Parameters:
`ask` - true - ask to overwrite, otherwise - overwrite without asking.
isAskToOverwriteExportedFiles
@OpenApiboolean isAskToOverwriteExportedFiles()
Chekcks if ask to overwrite exported files.
Returns:
true if ask to overwrite exported files.
setIDExportPolicy
@OpenApivoid setIDExportPolicy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) choice)
Set ID export policy
Parameters:
`choice` - choice
See Also:
[`ID_EXPORT_POLICY_GENERATE_ID`](#ID_EXPORT_POLICY_GENERATE_ID)
[`ID_EXPORT_POLICY_USE_ELEMENT_ID`](#ID_EXPORT_POLICY_USE_ELEMENT_ID)
[`ID_EXPORT_POLICY_USE_SERVER_ID`](#ID_EXPORT_POLICY_USE_SERVER_ID)
getIDExportPolicy
@OpenApi[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getIDExportPolicy()
Get current ID export choice.
See Also:
[`ID_EXPORT_POLICY_GENERATE_ID`](#ID_EXPORT_POLICY_GENERATE_ID)
[`ID_EXPORT_POLICY_USE_ELEMENT_ID`](#ID_EXPORT_POLICY_USE_ELEMENT_ID)
[`ID_EXPORT_POLICY_USE_SERVER_ID`](#ID_EXPORT_POLICY_USE_SERVER_ID)
setShowMappinWarning
@OpenApivoid setShowMappinWarning(boolean show)
Set if show warnings about (datatypes, metaclasses) mappings.
Parameters:
`show` -
isShowMappinWarning
@OpenApiboolean isShowMappinWarning()
Checks if show warnings about (datatypes, metaclasses) mappings.
Returns:
true if warnings about (datatypes, metaclasses) mapping should be displayed.
setShowStereotypePropertyTypeChangeWarning
@OpenApivoid setShowStereotypePropertyTypeChangeWarning(boolean show)
Set if show warnings about stereotype property type change.
Parameters:
`show` -
isShowStereotypePropertyTypeChangeWarning
@OpenApiboolean isShowStereotypePropertyTypeChangeWarning()
Check if show warnings about stereotype property type change.
Returns:
true if warnings about stereotype property type change is displayed.
setShowStereotypeFromSameWarning
@OpenApivoid setShowStereotypeFromSameWarning(boolean show)
Set if show warnings about not applied stereotypes (from the same profile).
Parameters:
`show` -
isShowStereotypeFromSameWarning
@OpenApiboolean isShowStereotypeFromSameWarning()
Checks if show warnings about not applied stereotypes (from the same profile).
Returns:
true if warnings about not applied stereotype should be displayed.
setUseKeywordAsStereotypeName
@OpenApivoid setUseKeywordAsStereotypeName(boolean use)
Set if stereotype keyword is used as stereotype name on import.
Parameters:
`use` -
isUseKeywordAsStereotypeName
@OpenApiboolean isUseKeywordAsStereotypeName()
Checks if stereotype keyword is used as stereotype name on import.
Returns:
true if stereotype keyword is used as stereotype name on import.
setDisplayWarnings
@OpenApivoid setDisplayWarnings(boolean display)
Set if to show warnings in Message Window on export/import.
Parameters:
`display` -
isDisplayWarnings
@OpenApiboolean isDisplayWarnings()
Checks if to show warnings in Message Window on export/import.
Returns:
true if warnings shoud be displayed in Message Window.
setApplyAllProfilesToRootModel
@OpenApivoid setApplyAllProfilesToRootModel(boolean apply)
Set if to apply all profiles to root Model on export.
Parameters:
`apply` - true to apply all profiles to root Model (on export).
isApplyAllProfilesToRootModel
@OpenApiboolean isApplyAllProfilesToRootModel()
Checks if to apply all profiles to root Model on export.
Returns:
true on export all profiles will be applied to root Model.
setMoveStereotypeToNestingProfile
@OpenApivoid setMoveStereotypeToNestingProfile(boolean move)
Set if move stereotype to nesting profile if stereotype is not directly contained by profile.
Parameters:
`move` - true move stereotype to nesting profile (on export).
isMoveStereotypeToNestingProfile
@OpenApiboolean isMoveStereotypeToNestingProfile()
Checks if move stereotype to nesting profile if stereotype is not directly contained by profile.
Returns:
true move stereotype to nesting profile (on export).

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.envoptions</a></div>
<h1 class="title" title="Interface BaseOptions">Interface BaseOptions</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">Options</a></code>, <code><a href="../v2/envoptions/Options.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">Options</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="BaseEmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseEmfOptionsGroup</a></code>, <code><a href="../v2/envoptions/EmfOptionsGroup.html" title="class in com.nomagic.magicdraw.emfuml2xmi.v2.envoptions">EmfOptionsGroup</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">BaseOptions</span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID_EXPORT_POLICY_GENERATE_ID">ID_EXPORT_POLICY_GENERATE_ID</a></code></div>
<div class="col-last even-row-color">
<div class="block">ID export policy generate id choice.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ID_EXPORT_POLICY_USE_ELEMENT_ID">ID_EXPORT_POLICY_USE_ELEMENT_ID</a></code></div>
<div class="col-last odd-row-color">
<div class="block">ID export policy use element id choice.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ID_EXPORT_POLICY_USE_SERVER_ID">ID_EXPORT_POLICY_USE_SERVER_ID</a></code></div>
<div class="col-last even-row-color">
<div class="block">ID export policy use server id choice.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#OPTION_NEVER">OPTION_NEVER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getAutoExportOption()">getAutoExportOption</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get auto-export to Eclipse UML2 XMI option.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getIDExportPolicy()">getIDExportPolicy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get current ID export choice.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if to apply all profiles to root Model on export.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Chekcks if ask to overwrite exported files.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isDisplayWarnings()">isDisplayWarnings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if to show warnings in Message Window on export/import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isShowMappinWarning()">isShowMappinWarning</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if show warnings about (datatypes, metaclasses) mappings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if show warnings about not applied stereotypes (from the same profile).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Check if show warnings about stereotype property type change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if stereotype keyword is used as stereotype name on import.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a><wbr/>(boolean apply)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if to apply all profiles to root Model on export.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a><wbr/>(boolean ask)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if ask to overwrite exported files.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setAutoExportOption(java.lang.String)">setAutoExportOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set auto-export to Eclipse UML2 XMI on project save option.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDisplayWarnings(boolean)">setDisplayWarnings</a><wbr/>(boolean display)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if to show warnings in Message Window on export/import.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set ID export policy</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a><wbr/>(boolean move)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setShowMappinWarning(boolean)">setShowMappinWarning</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if show warnings about (datatypes, metaclasses) mappings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a><wbr/>(boolean show)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if show warnings about not applied stereotypes (from the same profile).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a><wbr/>(boolean show)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if show warnings about stereotype property type change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a><wbr/>(boolean use)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if stereotype keyword is used as stereotype name on import.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="OPTION_EXPORT_ALWAYS">
<h3>OPTION_EXPORT_ALWAYS</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_EXPORT_ALWAYS</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.OPTION_EXPORT_ALWAYS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPTION_ASK_BEFORE_EXPORT">
<h3>OPTION_ASK_BEFORE_EXPORT</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_ASK_BEFORE_EXPORT</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.OPTION_ASK_BEFORE_EXPORT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="OPTION_NEVER">
<h3>OPTION_NEVER</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTION_NEVER</span></div>
<div class="block">Auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.OPTION_NEVER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ID_EXPORT_POLICY_GENERATE_ID">
<h3>ID_EXPORT_POLICY_GENERATE_ID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID_EXPORT_POLICY_GENERATE_ID</span></div>
<div class="block">ID export policy generate id choice.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.ID_EXPORT_POLICY_GENERATE_ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ID_EXPORT_POLICY_USE_ELEMENT_ID">
<h3>ID_EXPORT_POLICY_USE_ELEMENT_ID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID_EXPORT_POLICY_USE_ELEMENT_ID</span></div>
<div class="block">ID export policy use element id choice.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.ID_EXPORT_POLICY_USE_ELEMENT_ID">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ID_EXPORT_POLICY_USE_SERVER_ID">
<h3>ID_EXPORT_POLICY_USE_SERVER_ID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID_EXPORT_POLICY_USE_SERVER_ID</span></div>
<div class="block">ID export policy use server id choice.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions.ID_EXPORT_POLICY_USE_SERVER_ID">Constant Field Values</a></li>
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
</span><span class="return-type">void</span> <span class="element-name">setAutoExportOption</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</span></div>
<div class="block">Set auto-export to Eclipse UML2 XMI on project save option.</div>
<dl class="notes">
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
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAutoExportOption</span>()</div>
<div class="block">Get auto-export to Eclipse UML2 XMI option.</div>
<dl class="notes">
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
</span><span class="return-type">void</span> <span class="element-name">setAskToOverwriteExportedFiles</span><wbr/><span class="parameters">(boolean ask)</span></div>
<div class="block">Set if ask to overwrite exported files.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ask</code> - true - ask to overwrite, otherwise - overwrite without asking.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAskToOverwriteExportedFiles()">
<h3>isAskToOverwriteExportedFiles</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isAskToOverwriteExportedFiles</span>()</div>
<div class="block">Chekcks if ask to overwrite exported files.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if ask to overwrite exported files.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIDExportPolicy(java.lang.String)">
<h3>setIDExportPolicy</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setIDExportPolicy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> choice)</span></div>
<div class="block">Set ID export policy</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>choice</code> - choice</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#ID_EXPORT_POLICY_GENERATE_ID"><code>ID_EXPORT_POLICY_GENERATE_ID</code></a></li>
<li><a href="#ID_EXPORT_POLICY_USE_ELEMENT_ID"><code>ID_EXPORT_POLICY_USE_ELEMENT_ID</code></a></li>
<li><a href="#ID_EXPORT_POLICY_USE_SERVER_ID"><code>ID_EXPORT_POLICY_USE_SERVER_ID</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIDExportPolicy()">
<h3>getIDExportPolicy</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIDExportPolicy</span>()</div>
<div class="block">Get current ID export choice.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#ID_EXPORT_POLICY_GENERATE_ID"><code>ID_EXPORT_POLICY_GENERATE_ID</code></a></li>
<li><a href="#ID_EXPORT_POLICY_USE_ELEMENT_ID"><code>ID_EXPORT_POLICY_USE_ELEMENT_ID</code></a></li>
<li><a href="#ID_EXPORT_POLICY_USE_SERVER_ID"><code>ID_EXPORT_POLICY_USE_SERVER_ID</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowMappinWarning(boolean)">
<h3>setShowMappinWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setShowMappinWarning</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set if show warnings about (datatypes, metaclasses) mappings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowMappinWarning()">
<h3>isShowMappinWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isShowMappinWarning</span>()</div>
<div class="block">Checks if show warnings about (datatypes, metaclasses) mappings.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if warnings about (datatypes, metaclasses) mapping should be displayed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowStereotypePropertyTypeChangeWarning(boolean)">
<h3>setShowStereotypePropertyTypeChangeWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setShowStereotypePropertyTypeChangeWarning</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set if show warnings about stereotype property type change.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowStereotypePropertyTypeChangeWarning()">
<h3>isShowStereotypePropertyTypeChangeWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isShowStereotypePropertyTypeChangeWarning</span>()</div>
<div class="block">Check if show warnings about stereotype property type change.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if warnings about stereotype property type change is displayed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setShowStereotypeFromSameWarning(boolean)">
<h3>setShowStereotypeFromSameWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setShowStereotypeFromSameWarning</span><wbr/><span class="parameters">(boolean show)</span></div>
<div class="block">Set if show warnings about not applied stereotypes (from the same profile).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>show</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isShowStereotypeFromSameWarning()">
<h3>isShowStereotypeFromSameWarning</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isShowStereotypeFromSameWarning</span>()</div>
<div class="block">Checks if show warnings about not applied stereotypes (from the same profile).</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if warnings about not applied stereotype should be displayed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUseKeywordAsStereotypeName(boolean)">
<h3>setUseKeywordAsStereotypeName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setUseKeywordAsStereotypeName</span><wbr/><span class="parameters">(boolean use)</span></div>
<div class="block">Set if stereotype keyword is used as stereotype name on import.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>use</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseKeywordAsStereotypeName()">
<h3>isUseKeywordAsStereotypeName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isUseKeywordAsStereotypeName</span>()</div>
<div class="block">Checks if stereotype keyword is used as stereotype name on import.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if stereotype keyword is used as stereotype name on import.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDisplayWarnings(boolean)">
<h3>setDisplayWarnings</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setDisplayWarnings</span><wbr/><span class="parameters">(boolean display)</span></div>
<div class="block">Set if to show warnings in Message Window on export/import.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>display</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDisplayWarnings()">
<h3>isDisplayWarnings</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isDisplayWarnings</span>()</div>
<div class="block">Checks if to show warnings in Message Window on export/import.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if warnings shoud be displayed in Message Window.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setApplyAllProfilesToRootModel(boolean)">
<h3>setApplyAllProfilesToRootModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setApplyAllProfilesToRootModel</span><wbr/><span class="parameters">(boolean apply)</span></div>
<div class="block">Set if to apply all profiles to root Model on export.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>apply</code> - true to apply all profiles to root Model (on export).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isApplyAllProfilesToRootModel()">
<h3>isApplyAllProfilesToRootModel</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isApplyAllProfilesToRootModel</span>()</div>
<div class="block">Checks if to apply all profiles to root Model on export.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true on export all profiles will be applied to root Model.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMoveStereotypeToNestingProfile(boolean)">
<h3>setMoveStereotypeToNestingProfile</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setMoveStereotypeToNestingProfile</span><wbr/><span class="parameters">(boolean move)</span></div>
<div class="block">Set if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>move</code> - true move stereotype to nesting profile (on export).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMoveStereotypeToNestingProfile()">
<h3>isMoveStereotypeToNestingProfile</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isMoveStereotypeToNestingProfile</span>()</div>
<div class="block">Checks if move stereotype to nesting profile if stereotype is not directly contained by profile.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true move stereotype to nesting profile (on export).</dd>
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
