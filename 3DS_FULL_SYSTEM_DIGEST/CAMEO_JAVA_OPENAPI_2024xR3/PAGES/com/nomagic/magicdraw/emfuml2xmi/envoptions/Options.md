# JAVA OPENAPI: Options (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/emfuml2xmi/envoptions/Options.html
- source_path: `com/nomagic/magicdraw/emfuml2xmi/envoptions/Options.html`
- source_sha256: `537507b1e3b75281e039b7d2e2feedb7558c94d402c3f37cad6c758cec8cbcaf`
- captured_utc: `2026-07-14T16:55:18.074038+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.emfuml2xmi.envoptions](package-summary.html)

## Interface Options

All Superinterfaces:
`[BaseOptions](BaseOptions.html)`

@OpenApiAllpublic interfaceOptionsextends [BaseOptions](BaseOptions.html)

Eclipse UML2 XMI export/import environment options.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS](#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS)`
Change type to stereotype metaclass.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE](#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE)`
Do not change type.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS](#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS)`
Change type to stereotype metaclass only if stereotype extends single metaclass.
Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](BaseOptions.html)
`[ID_EXPORT_POLICY_GENERATE_ID](BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID), [ID_EXPORT_POLICY_USE_ELEMENT_ID](BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID), [ID_EXPORT_POLICY_USE_SERVER_ID](BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID), [OPTION_ASK_BEFORE_EXPORT](BaseOptions.html#OPTION_ASK_BEFORE_EXPORT), [OPTION_EXPORT_ALWAYS](BaseOptions.html#OPTION_EXPORT_ALWAYS), [OPTION_NEVER](BaseOptions.html#OPTION_NEVER)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDeprecated Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getChangeStereotypePropertyTypeStereotype](#getChangeStereotypePropertyTypeStereotype())()`
Get "Change stereotype property type stereotype" option value.
`boolean`
`[isChangeNotEcoreDataTypeToString](#isChangeNotEcoreDataTypeToString())()`
Checks if to change stereotype property type not eCore datatype to String on export.
`boolean`
`[isChangeStereotypePropertyTypeStereotype](#isChangeStereotypePropertyTypeStereotype())()`
Deprecated.
Use [`getChangeStereotypePropertyTypeStereotype()`](#getChangeStereotypePropertyTypeStereotype())
`void`
`[setChangeNotEcoreDataTypeToString](#setChangeNotEcoreDataTypeToString(boolean))(boolean change)`
Set if to change stereotype property type not eCore datatype to String on export.
`void`
`[setChangeStereotypePropertyTypeStereotype](#setChangeStereotypePropertyTypeStereotype(boolean))(boolean change)`
Deprecated.
Use [`setChangeStereotypePropertyTypeStereotype(String)`](#setChangeStereotypePropertyTypeStereotype(java.lang.String))
`void`
`[setChangeStereotypePropertyTypeStereotype](#setChangeStereotypePropertyTypeStereotype(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Set "Change stereotype property type stereotype" option value.
Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.[BaseOptions](BaseOptions.html)
`[getAutoExportOption](BaseOptions.html#getAutoExportOption()), [getIDExportPolicy](BaseOptions.html#getIDExportPolicy()), [isApplyAllProfilesToRootModel](BaseOptions.html#isApplyAllProfilesToRootModel()), [isAskBeforeExport](BaseOptions.html#isAskBeforeExport()), [isAskToOverwriteExportedFiles](BaseOptions.html#isAskToOverwriteExportedFiles()), [isAutoExport](BaseOptions.html#isAutoExport()), [isDisplayWarnings](BaseOptions.html#isDisplayWarnings()), [isMoveStereotypeToNestingProfile](BaseOptions.html#isMoveStereotypeToNestingProfile()), [isPreserveIDsOnImport](BaseOptions.html#isPreserveIDsOnImport()), [isShowMappinWarning](BaseOptions.html#isShowMappinWarning()), [isShowStereotypeFromSameWarning](BaseOptions.html#isShowStereotypeFromSameWarning()), [isShowStereotypePropertyTypeChangeWarning](BaseOptions.html#isShowStereotypePropertyTypeChangeWarning()), [isUseKeywordAsStereotypeName](BaseOptions.html#isUseKeywordAsStereotypeName()), [setApplyAllProfilesToRootModel](BaseOptions.html#setApplyAllProfilesToRootModel(boolean)), [setAskToOverwriteExportedFiles](BaseOptions.html#setAskToOverwriteExportedFiles(boolean)), [setAutoExportOption](BaseOptions.html#setAutoExportOption(java.lang.String)), [setDisplayWarnings](BaseOptions.html#setDisplayWarnings(boolean)), [setIDExportPolicy](BaseOptions.html#setIDExportPolicy(java.lang.String)), [setMoveStereotypeToNestingProfile](BaseOptions.html#setMoveStereotypeToNestingProfile(boolean)), [setShowMappinWarning](BaseOptions.html#setShowMappinWarning(boolean)), [setShowStereotypeFromSameWarning](BaseOptions.html#setShowStereotypeFromSameWarning(boolean)), [setShowStereotypePropertyTypeChangeWarning](BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean)), [setUseKeywordAsStereotypeName](BaseOptions.html#setUseKeywordAsStereotypeName(boolean))`

============ FIELD DETAIL =========== 
Field Details
CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE
Do not change type.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE)
CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS
Change type to stereotype metaclass only if stereotype extends single metaclass.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS)
CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS
@OpenApistatic final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS
Change type to stereotype metaclass. If stereotype extends multiple metaclasses find a common super metaclass.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS)
 ============ METHOD DETAIL ========== 
Method Details
setChangeStereotypePropertyTypeStereotype
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)void setChangeStereotypePropertyTypeStereotype(boolean change)
Deprecated.
Use [`setChangeStereotypePropertyTypeStereotype(String)`](#setChangeStereotypePropertyTypeStereotype(java.lang.String))
Set if to change stereotype property type stereotype to metaclass on export.
Parameters:
`change` - true - change.
isChangeStereotypePropertyTypeStereotype
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)boolean isChangeStereotypePropertyTypeStereotype()
Deprecated.
Use [`getChangeStereotypePropertyTypeStereotype()`](#getChangeStereotypePropertyTypeStereotype())
Checks if to change stereotype property type stereotype to metaclass on export.
Returns:
true if stereotype property type stereotype should be changed to metaclass.
getChangeStereotypePropertyTypeStereotype
@OpenApi[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getChangeStereotypePropertyTypeStereotype()
Get "Change stereotype property type stereotype" option value.
Returns:
value.
setChangeStereotypePropertyTypeStereotype
@OpenApivoid setChangeStereotypePropertyTypeStereotype([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Set "Change stereotype property type stereotype" option value.
Parameters:
`value` - value to set.
setChangeNotEcoreDataTypeToString
@OpenApivoid setChangeNotEcoreDataTypeToString(boolean change)
Set if to change stereotype property type not eCore datatype to String on export.
Parameters:
`change` - true - change.
isChangeNotEcoreDataTypeToString
@OpenApiboolean isChangeNotEcoreDataTypeToString()
Checks if to change stereotype property type not eCore datatype to String on export.
Returns:
true if stereotype property type not eCore datatype should be changed to String.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.emfuml2xmi.envoptions</a></div>
<h1 class="title" title="Interface Options">Interface Options</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Options</span><span class="extends-implements">
extends <a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Change type to stereotype metaclass.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Do not change type.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Change type to stereotype metaclass only if stereotype extends single metaclass.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Fields inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="BaseOptions.html#ID_EXPORT_POLICY_GENERATE_ID">ID_EXPORT_POLICY_GENERATE_ID</a>, <a href="BaseOptions.html#ID_EXPORT_POLICY_USE_ELEMENT_ID">ID_EXPORT_POLICY_USE_ELEMENT_ID</a>, <a href="BaseOptions.html#ID_EXPORT_POLICY_USE_SERVER_ID">ID_EXPORT_POLICY_USE_SERVER_ID</a>, <a href="BaseOptions.html#OPTION_ASK_BEFORE_EXPORT">OPTION_ASK_BEFORE_EXPORT</a>, <a href="BaseOptions.html#OPTION_EXPORT_ALWAYS">OPTION_EXPORT_ALWAYS</a>, <a href="BaseOptions.html#OPTION_NEVER">OPTION_NEVER</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChangeStereotypePropertyTypeStereotype()">getChangeStereotypePropertyTypeStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Get "Change stereotype property type stereotype" option value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isChangeNotEcoreDataTypeToString()">isChangeNotEcoreDataTypeToString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Checks if to change stereotype property type not eCore datatype to String on export.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#isChangeStereotypePropertyTypeStereotype()">isChangeStereotypePropertyTypeStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#getChangeStereotypePropertyTypeStereotype()"><code>getChangeStereotypePropertyTypeStereotype()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setChangeNotEcoreDataTypeToString(boolean)">setChangeNotEcoreDataTypeToString</a><wbr/>(boolean change)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set if to change stereotype property type not eCore datatype to String on export.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#setChangeStereotypePropertyTypeStereotype(boolean)">setChangeStereotypePropertyTypeStereotype</a><wbr/>(boolean change)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#setChangeStereotypePropertyTypeStereotype(java.lang.String)"><code>setChangeStereotypePropertyTypeStereotype(String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setChangeStereotypePropertyTypeStereotype(java.lang.String)">setChangeStereotypePropertyTypeStereotype</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set "Change stereotype property type stereotype" option value.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.emfuml2xmi.envoptions.BaseOptions">Methods inherited from interface com.nomagic.magicdraw.emfuml2xmi.envoptions.<a href="BaseOptions.html" title="interface in com.nomagic.magicdraw.emfuml2xmi.envoptions">BaseOptions</a></h3>
<code><a href="BaseOptions.html#getAutoExportOption()">getAutoExportOption</a>, <a href="BaseOptions.html#getIDExportPolicy()">getIDExportPolicy</a>, <a href="BaseOptions.html#isApplyAllProfilesToRootModel()">isApplyAllProfilesToRootModel</a>, <a href="BaseOptions.html#isAskBeforeExport()">isAskBeforeExport</a>, <a href="BaseOptions.html#isAskToOverwriteExportedFiles()">isAskToOverwriteExportedFiles</a>, <a href="BaseOptions.html#isAutoExport()">isAutoExport</a>, <a href="BaseOptions.html#isDisplayWarnings()">isDisplayWarnings</a>, <a href="BaseOptions.html#isMoveStereotypeToNestingProfile()">isMoveStereotypeToNestingProfile</a>, <a href="BaseOptions.html#isPreserveIDsOnImport()">isPreserveIDsOnImport</a>, <a href="BaseOptions.html#isShowMappinWarning()">isShowMappinWarning</a>, <a href="BaseOptions.html#isShowStereotypeFromSameWarning()">isShowStereotypeFromSameWarning</a>, <a href="BaseOptions.html#isShowStereotypePropertyTypeChangeWarning()">isShowStereotypePropertyTypeChangeWarning</a>, <a href="BaseOptions.html#isUseKeywordAsStereotypeName()">isUseKeywordAsStereotypeName</a>, <a href="BaseOptions.html#setApplyAllProfilesToRootModel(boolean)">setApplyAllProfilesToRootModel</a>, <a href="BaseOptions.html#setAskToOverwriteExportedFiles(boolean)">setAskToOverwriteExportedFiles</a>, <a href="BaseOptions.html#setAutoExportOption(java.lang.String)">setAutoExportOption</a>, <a href="BaseOptions.html#setDisplayWarnings(boolean)">setDisplayWarnings</a>, <a href="BaseOptions.html#setIDExportPolicy(java.lang.String)">setIDExportPolicy</a>, <a href="BaseOptions.html#setMoveStereotypeToNestingProfile(boolean)">setMoveStereotypeToNestingProfile</a>, <a href="BaseOptions.html#setShowMappinWarning(boolean)">setShowMappinWarning</a>, <a href="BaseOptions.html#setShowStereotypeFromSameWarning(boolean)">setShowStereotypeFromSameWarning</a>, <a href="BaseOptions.html#setShowStereotypePropertyTypeChangeWarning(boolean)">setShowStereotypePropertyTypeChangeWarning</a>, <a href="BaseOptions.html#setUseKeywordAsStereotypeName(boolean)">setUseKeywordAsStereotypeName</a></code></div>
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
<section class="detail" id="CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE">
<h3>CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE</span></div>
<div class="block">Do not change type.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_NOT_CHANGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS">
<h3>CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS</span></div>
<div class="block">Change type to stereotype metaclass only if stereotype extends single metaclass.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_SINGLE_EXTENDED_METACLASS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS">
<h3>CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS</span></div>
<div class="block">Change type to stereotype metaclass. If stereotype extends multiple metaclasses find a common super metaclass.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.emfuml2xmi.envoptions.Options.CHANGE_STEREOTYPE_PROPERTY_TYPE_STEREOTYPE_MULTIPLE_EXTENDED_METACLASS">Constant Field Values</a></li>
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
<section class="detail" id="setChangeStereotypePropertyTypeStereotype(boolean)">
<h3>setChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">void</span> <span class="element-name">setChangeStereotypePropertyTypeStereotype</span><wbr/><span class="parameters">(boolean change)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#setChangeStereotypePropertyTypeStereotype(java.lang.String)"><code>setChangeStereotypePropertyTypeStereotype(String)</code></a></div>
</div>
<div class="block">Set if to change stereotype property type stereotype to metaclass on export.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>change</code> - true - change.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChangeStereotypePropertyTypeStereotype()">
<h3>isChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">boolean</span> <span class="element-name">isChangeStereotypePropertyTypeStereotype</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#getChangeStereotypePropertyTypeStereotype()"><code>getChangeStereotypePropertyTypeStereotype()</code></a></div>
</div>
<div class="block">Checks if to change stereotype property type stereotype to metaclass on export.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if stereotype property type stereotype should be changed to metaclass.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangeStereotypePropertyTypeStereotype()">
<h3>getChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getChangeStereotypePropertyTypeStereotype</span>()</div>
<div class="block">Get "Change stereotype property type stereotype" option value.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeStereotypePropertyTypeStereotype(java.lang.String)">
<h3>setChangeStereotypePropertyTypeStereotype</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setChangeStereotypePropertyTypeStereotype</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Set "Change stereotype property type stereotype" option value.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - value to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangeNotEcoreDataTypeToString(boolean)">
<h3>setChangeNotEcoreDataTypeToString</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">void</span> <span class="element-name">setChangeNotEcoreDataTypeToString</span><wbr/><span class="parameters">(boolean change)</span></div>
<div class="block">Set if to change stereotype property type not eCore datatype to String on export.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>change</code> - true - change.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isChangeNotEcoreDataTypeToString()">
<h3>isChangeNotEcoreDataTypeToString</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="return-type">boolean</span> <span class="element-name">isChangeNotEcoreDataTypeToString</span>()</div>
<div class="block">Checks if to change stereotype property type not eCore datatype to String on export.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if stereotype property type not eCore datatype should be changed to String.</dd>
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
