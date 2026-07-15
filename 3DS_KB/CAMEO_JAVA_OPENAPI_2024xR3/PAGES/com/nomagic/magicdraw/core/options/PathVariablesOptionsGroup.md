# JAVA OPENAPI: PathVariablesOptionsGroup (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/options/PathVariablesOptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/PathVariablesOptionsGroup.html`
- source_sha256: `4b4452c92b8c4cff586098f1d1f18a264373c5e3132dda5b428514f98c0ad770`
- captured_utc: `2026-07-14T16:55:12.796979+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class PathVariablesOptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.options.OptionsGroup](OptionsGroup.html)
[com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
com.nomagic.magicdraw.core.options.VersionedOptionsGroup
com.nomagic.magicdraw.core.options.PathVariablesOptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApipublic classPathVariablesOptionsGroup
extends com.nomagic.magicdraw.core.options.VersionedOptionsGroup

Path variables options group.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ID](#ID)`
Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`CURRENT_EXPORTER_VERSION`
Fields inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[ICON_ENVIRONMENT_OPTIONS](OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PathVariablesOptionsGroup](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addIgnoredVariable](#addIgnoredVariable(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) variable)`

`void`
`[addPathVariable](#addPathVariable(com.nomagic.magicdraw.pathvariables.PathVariable))([PathVariable](../../pathvariables/PathVariable.html) variable)`

`com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel`
`[createOptionsPanel](#createOptionsPanel())()`
Creates options panel for editing the properties.
`com.nomagic.ui.banners.Banner`
`[getBanner](#getBanner())()`

`[Style](../../properties/Style.html)`
`[getOptionsToSave](#getOptionsToSave())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PathVariable](../../pathvariables/PathVariable.html)>`
`[getPathVariables](#getPathVariables())()`
Get path variables.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[getVariables](#getVariables())()`

`boolean`
`[isIgnoredVariable](#isIgnoredVariable(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) variable)`

`boolean`
`[isSuggestUsePathVariables](#isSuggestUsePathVariables())()`

`static [PathVariable](../../pathvariables/PathVariable.html)`
`[parsePropertyString](#parsePropertyString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pathVariable)`

`void`
`[setDefaultValues](#setDefaultValues())()`
Sets default values for the properties contained in this group.
`void`
`[setPathVariables](#setPathVariables(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PathVariable](../../pathvariables/PathVariable.html)> pathVariables)`

`void`
`[setSuggestUsePathVariables](#setSuggestUsePathVariables(boolean))(boolean value)`

`void`
`[setVariables](#setVariables(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] variables)`
Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup
`afterLoad, beforeLoad, getExporterVersion, isExporterVersionEarlier, isExporterVersionEarlier, loadOptions`
Methods inherited from class com.nomagic.magicdraw.core.options.[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)
`[addInvisibleProperty](AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)), [addProperty](AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)), [afterLoadAdditionalAction](AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)), [clone](AbstractPropertyOptionsGroup.html#clone()), [createDefault](AbstractPropertyOptionsGroup.html#createDefault()), [createOptions](AbstractPropertyOptionsGroup.html#createOptions()), [fixProperty](AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)), [getCopy](AbstractPropertyOptionsGroup.html#getCopy()), [getOptions](AbstractPropertyOptionsGroup.html#getOptions()), [getProperty](AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)), [getVisibleOptions](AbstractPropertyOptionsGroup.html#getVisibleOptions()), [hasVisibleOptions](AbstractPropertyOptionsGroup.html#hasVisibleOptions()), [removeProperty](AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)), [setOptions](AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)), [setPropertiesInvisible](AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)), [setPropertyInvisible](AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean))`
Methods inherited from class com.nomagic.magicdraw.core.options.[OptionsGroup](OptionsGroup.html)
`[add](OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)), [afterSave](OptionsGroup.html#afterSave()), [canDisplay](OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)), [firstInit](OptionsGroup.html#firstInit(boolean)), [getChildren](OptionsGroup.html#getChildren()), [getGroupIcon](OptionsGroup.html#getGroupIcon()), [getIcon](OptionsGroup.html#getIcon()), [getId](OptionsGroup.html#getId()), [getModelingLanguage](OptionsGroup.html#getModelingLanguage()), [getName](OptionsGroup.html#getName()), [getParent](OptionsGroup.html#getParent()), [isEnabled](OptionsGroup.html#isEnabled()), [isVisible](OptionsGroup.html#isVisible()), [remove](OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)), [resetCachedValues](OptionsGroup.html#resetCachedValues()), [setEnabled](OptionsGroup.html#setEnabled(boolean)), [setVisible](OptionsGroup.html#setVisible(boolean)), [sortChildren](OptionsGroup.html#sortChildren(java.util.Comparator))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ID
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ID
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.core.options.PathVariablesOptionsGroup.ID)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PathVariablesOptionsGroup
public PathVariablesOptionsGroup()
 ============ METHOD DETAIL ========== 
Method Details
createOptionsPanel
public com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel createOptionsPanel()
Description copied from class: `[OptionsGroup](OptionsGroup.html#createOptionsPanel())`
Creates options panel for editing the properties.
Overrides:
`[createOptionsPanel](AbstractPropertyOptionsGroup.html#createOptionsPanel())` in class `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)`
Returns:
created options panel.
setDefaultValues
public void setDefaultValues()
Description copied from class: `[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html#setDefaultValues())`
Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.
Overrides:
`setDefaultValues` in class `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`
getVariables
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] getVariables()
getPathVariables
@OpenApipublic [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PathVariable](../../pathvariables/PathVariable.html)> getPathVariables()
Get path variables.
Returns:
path variables.
setVariables
public void setVariables([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] variables)
setPathVariables
public void setPathVariables([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PathVariable](../../pathvariables/PathVariable.html)> pathVariables)
parsePropertyString
public static [PathVariable](../../pathvariables/PathVariable.html) parsePropertyString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pathVariable)
addPathVariable
@OpenApipublic void addPathVariable([PathVariable](../../pathvariables/PathVariable.html) variable)
isSuggestUsePathVariables
public boolean isSuggestUsePathVariables()
setSuggestUsePathVariables
public void setSuggestUsePathVariables(boolean value)
addIgnoredVariable
public void addIgnoredVariable([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) variable)
isIgnoredVariable
public boolean isIgnoredVariable([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) variable)
getOptionsToSave
public [Style](../../properties/Style.html) getOptionsToSave()
Overrides:
`getOptionsToSave` in class `com.nomagic.magicdraw.core.options.VersionedOptionsGroup`
getBanner
public com.nomagic.ui.banners.Banner getBanner()
Overrides:
`[getBanner](OptionsGroup.html#getBanner())` in class `[OptionsGroup](OptionsGroup.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class PathVariablesOptionsGroup">Class PathVariablesOptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.OptionsGroup</a>
<div class="inheritance"><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.VersionedOptionsGroup
<div class="inheritance">com.nomagic.magicdraw.core.options.PathVariablesOptionsGroup</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PathVariablesOptionsGroup</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.options.VersionedOptionsGroup</span></div>
<div class="block">Path variables options group.</div>
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
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>CURRENT_EXPORTER_VERSION</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Fields inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#ICON_ENVIRONMENT_OPTIONS">ICON_ENVIRONMENT_OPTIONS</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PathVariablesOptionsGroup</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addIgnoredVariable(java.lang.String)">addIgnoredVariable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPathVariable(com.nomagic.magicdraw.pathvariables.PathVariable)">addPathVariable</a><wbr/>(<a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a> variable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createOptionsPanel()">createOptionsPanel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates options panel for editing the properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.banners.Banner</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBanner()">getBanner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptionsToSave()">getOptionsToSave</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathVariables()">getPathVariables</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get path variables.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVariables()">getVariables</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isIgnoredVariable(java.lang.String)">isIgnoredVariable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSuggestUsePathVariables()">isSuggestUsePathVariables</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parsePropertyString(java.lang.String)">parsePropertyString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathVariable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDefaultValues()">setDefaultValues</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets default values for the properties contained in this group.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPathVariables(java.util.Collection)">setPathVariables</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a>&gt; pathVariables)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSuggestUsePathVariables(boolean)">setSuggestUsePathVariables</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVariables(java.lang.String%5B%5D)">setVariables</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] variables)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.VersionedOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.VersionedOptionsGroup</h3>
<code>afterLoad, beforeLoad, getExporterVersion, isExporterVersionEarlier, isExporterVersionEarlier, loadOptions</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.AbstractPropertyOptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></h3>
<code><a href="AbstractPropertyOptionsGroup.html#addInvisibleProperty(com.nomagic.magicdraw.properties.Property)">addInvisibleProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,boolean)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#addProperty(com.nomagic.magicdraw.properties.Property,java.lang.String)">addProperty</a>, <a href="AbstractPropertyOptionsGroup.html#afterLoadAdditionalAction(boolean)">afterLoadAdditionalAction</a>, <a href="AbstractPropertyOptionsGroup.html#clone()">clone</a>, <a href="AbstractPropertyOptionsGroup.html#createDefault()">createDefault</a>, <a href="AbstractPropertyOptionsGroup.html#createOptions()">createOptions</a>, <a href="AbstractPropertyOptionsGroup.html#fixProperty(java.lang.String,java.lang.Runnable)">fixProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getCopy()">getCopy</a>, <a href="AbstractPropertyOptionsGroup.html#getOptions()">getOptions</a>, <a href="AbstractPropertyOptionsGroup.html#getProperty(java.lang.String)">getProperty</a>, <a href="AbstractPropertyOptionsGroup.html#getVisibleOptions()">getVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#hasVisibleOptions()">hasVisibleOptions</a>, <a href="AbstractPropertyOptionsGroup.html#removeProperty(java.lang.String)">removeProperty</a>, <a href="AbstractPropertyOptionsGroup.html#setOptions(com.nomagic.magicdraw.properties.PropertyManager)">setOptions</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertiesInvisible(java.lang.String%5B%5D,boolean)">setPropertiesInvisible</a>, <a href="AbstractPropertyOptionsGroup.html#setPropertyInvisible(java.lang.String,boolean)">setPropertyInvisible</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.options.OptionsGroup">Methods inherited from class com.nomagic.magicdraw.core.options.<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></h3>
<code><a href="OptionsGroup.html#add(com.nomagic.magicdraw.core.options.OptionsGroup)">add</a>, <a href="OptionsGroup.html#afterSave()">afterSave</a>, <a href="OptionsGroup.html#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)">canDisplay</a>, <a href="OptionsGroup.html#firstInit(boolean)">firstInit</a>, <a href="OptionsGroup.html#getChildren()">getChildren</a>, <a href="OptionsGroup.html#getGroupIcon()">getGroupIcon</a>, <a href="OptionsGroup.html#getIcon()">getIcon</a>, <a href="OptionsGroup.html#getId()">getId</a>, <a href="OptionsGroup.html#getModelingLanguage()">getModelingLanguage</a>, <a href="OptionsGroup.html#getName()">getName</a>, <a href="OptionsGroup.html#getParent()">getParent</a>, <a href="OptionsGroup.html#isEnabled()">isEnabled</a>, <a href="OptionsGroup.html#isVisible()">isVisible</a>, <a href="OptionsGroup.html#remove(com.nomagic.magicdraw.core.options.OptionsGroup)">remove</a>, <a href="OptionsGroup.html#resetCachedValues()">resetCachedValues</a>, <a href="OptionsGroup.html#setEnabled(boolean)">setEnabled</a>, <a href="OptionsGroup.html#setVisible(boolean)">setVisible</a>, <a href="OptionsGroup.html#sortChildren(java.util.Comparator)">sortChildren</a></code></div>
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
<section class="detail" id="ID">
<h3>ID</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ID</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.core.options.PathVariablesOptionsGroup.ID">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>PathVariablesOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PathVariablesOptionsGroup</span>()</div>
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
<section class="detail" id="createOptionsPanel()">
<h3>createOptionsPanel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel</span> <span class="element-name">createOptionsPanel</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="OptionsGroup.html#createOptionsPanel()">OptionsGroup</a></code></span></div>
<div class="block">Creates options panel for editing the properties.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="AbstractPropertyOptionsGroup.html#createOptionsPanel()">createOptionsPanel</a></code> in class <code><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></code></dd>
<dt>Returns:</dt>
<dd>created options panel.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDefaultValues()">
<h3>setDefaultValues</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDefaultValues</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="AbstractPropertyOptionsGroup.html#setDefaultValues()">AbstractPropertyOptionsGroup</a></code></span></div>
<div class="block">Sets default values for the properties contained in this group.
 Overriding classes should set default values to the properties.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>setDefaultValues</code> in class <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVariables()">
<h3>getVariables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">getVariables</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPathVariables()">
<h3>getPathVariables</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a>&gt;</span> <span class="element-name">getPathVariables</span>()</div>
<div class="block">Get path variables.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>path variables.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVariables(java.lang.String[])">
<h3>setVariables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVariables</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] variables)</span></div>
</section>
</li>
<li>
<section class="detail" id="setPathVariables(java.util.Collection)">
<h3>setPathVariables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPathVariables</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a>&gt; pathVariables)</span></div>
</section>
</li>
<li>
<section class="detail" id="parsePropertyString(java.lang.String)">
<h3>parsePropertyString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a></span> <span class="element-name">parsePropertyString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathVariable)</span></div>
</section>
</li>
<li>
<section class="detail" id="addPathVariable(com.nomagic.magicdraw.pathvariables.PathVariable)">
<h3>addPathVariable</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addPathVariable</span><wbr/><span class="parameters">(<a href="../../pathvariables/PathVariable.html" title="class in com.nomagic.magicdraw.pathvariables">PathVariable</a> variable)</span></div>
</section>
</li>
<li>
<section class="detail" id="isSuggestUsePathVariables()">
<h3>isSuggestUsePathVariables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSuggestUsePathVariables</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setSuggestUsePathVariables(boolean)">
<h3>setSuggestUsePathVariables</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSuggestUsePathVariables</span><wbr/><span class="parameters">(boolean value)</span></div>
</section>
</li>
<li>
<section class="detail" id="addIgnoredVariable(java.lang.String)">
<h3>addIgnoredVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addIgnoredVariable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variable)</span></div>
</section>
</li>
<li>
<section class="detail" id="isIgnoredVariable(java.lang.String)">
<h3>isIgnoredVariable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isIgnoredVariable</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> variable)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOptionsToSave()">
<h3>getOptionsToSave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getOptionsToSave</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code>getOptionsToSave</code> in class <code>com.nomagic.magicdraw.core.options.VersionedOptionsGroup</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBanner()">
<h3>getBanner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.banners.Banner</span> <span class="element-name">getBanner</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="OptionsGroup.html#getBanner()">getBanner</a></code> in class <code><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></code></dd>
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
