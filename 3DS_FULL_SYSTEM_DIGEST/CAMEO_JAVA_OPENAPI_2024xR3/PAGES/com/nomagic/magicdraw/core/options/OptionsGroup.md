# JAVA OPENAPI: OptionsGroup (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/options/OptionsGroup.html
- source_path: `com/nomagic/magicdraw/core/options/OptionsGroup.html`
- source_sha256: `6c7dd4bc505b88d29238fbdc7d7fea59f2365f9ed0ff044344f597bb2450ef0b`
- captured_utc: `2026-07-14T16:55:12.470977+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class OptionsGroup

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.options.OptionsGroup

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[AbstractPropertyOptionsGroup](AbstractPropertyOptionsGroup.html)`

@OpenApipublic abstract classOptionsGroup
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)

Represents general application options.

See Also:
[`AbstractPropertyOptionsGroup`](AbstractPropertyOptionsGroup.html)
[`EnvironmentOptions`](EnvironmentOptions.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[ICON_ENVIRONMENT_OPTIONS](#ICON_ENVIRONMENT_OPTIONS)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[OptionsGroup](#%3Cinit%3E(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 boolean visible)`

`protected`
`[OptionsGroup](#%3Cinit%3E(java.lang.String,javax.swing.Icon,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 boolean visible)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[add](#add(com.nomagic.magicdraw.core.options.OptionsGroup))([OptionsGroup](OptionsGroup.html) group)`

`protected void`
`[afterLoad](#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean))(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)`

`void`
`[afterSave](#afterSave())()`

`void`
`[beforeLoad](#beforeLoad(boolean))(boolean pluginsLoaded)`

`boolean`
`[canDisplay](#canDisplay(com.nomagic.magicdraw.usermodes.UserMode))(com.nomagic.magicdraw.usermodes.UserMode mode)`

`protected [OptionsGroup](OptionsGroup.html)`
`[clone](#clone())()`

`abstract com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel`
`[createOptionsPanel](#createOptionsPanel())()`
Creates options panel for editing the properties.
`void`
`[firstInit](#firstInit(boolean))(boolean pluginsLoaded)`

`com.nomagic.ui.banners.Banner`
`[getBanner](#getBanner())()`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[OptionsGroup](OptionsGroup.html)>`
`[getChildren](#getChildren())()`

`[Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html)`
`[getGroupIcon](#getGroupIcon())()`
Returns icon to display with options.
`[SwingImageIcon](../../../ui/SwingImageIcon.html)`
`[getIcon](#getIcon())()`
Deprecated.
use #getGroupIcon()
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getId](#getId())()`

`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getModelingLanguage](#getModelingLanguage())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Gets human-readable name of options.
`[Style](../../properties/Style.html)`
`[getOptionsToSave](#getOptionsToSave())()`

`[OptionsGroup](OptionsGroup.html)`
`[getParent](#getParent())()`

`boolean`
`[isEnabled](#isEnabled())()`

`boolean`
`[isVisible](#isVisible())()`

`void`
`[loadOptions](#loadOptions(com.nomagic.magicdraw.properties.Style,boolean))([Style](../../properties/Style.html) style,
 boolean pluginsLoaded)`

`void`
`[remove](#remove(com.nomagic.magicdraw.core.options.OptionsGroup))([OptionsGroup](OptionsGroup.html) group)`

`protected void`
`[resetCachedValues](#resetCachedValues())()`

`void`
`[setEnabled](#setEnabled(boolean))(boolean enabled)`

`void`
`[setVisible](#setVisible(boolean))(boolean visible)`

`void`
`[sortChildren](#sortChildren(java.util.Comparator))([Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[OptionsGroup](OptionsGroup.html)> comparator)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
ICON_ENVIRONMENT_OPTIONS
protected static [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) ICON_ENVIRONMENT_OPTIONS
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OptionsGroup
protected OptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 @CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 boolean visible)
OptionsGroup
protected OptionsGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 boolean visible)
 ============ METHOD DETAIL ========== 
Method Details
getId
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()
getGroupIcon
@CheckForNull
@OpenApipublic [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) getGroupIcon()
Returns icon to display with options.
Returns:
icon to display with options.
getIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNull
@OpenApipublic [SwingImageIcon](../../../ui/SwingImageIcon.html) getIcon()
Deprecated.
use #getGroupIcon()
Returns icon to display with options.
Returns:
icon to display with options
createOptionsPanel
@CheckForNullpublic abstract com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel createOptionsPanel()
Creates options panel for editing the properties.
Returns:
created options panel.
isVisible
public boolean isVisible()
setVisible
public void setVisible(boolean visible)
isEnabled
public boolean isEnabled()
setEnabled
public void setEnabled(boolean enabled)
getOptionsToSave
@CheckForNullpublic [Style](../../properties/Style.html) getOptionsToSave()
firstInit
public void firstInit(boolean pluginsLoaded)
afterSave
public void afterSave()
loadOptions
public void loadOptions([Style](../../properties/Style.html) style,
 boolean pluginsLoaded)
beforeLoad
public void beforeLoad(boolean pluginsLoaded)
afterLoad
protected void afterLoad(@CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)
getName
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Gets human-readable name of options.
Returns:
human-readable name of options.
getBanner
@CheckForNullpublic com.nomagic.ui.banners.Banner getBanner()
getParent
@CheckForNullpublic [OptionsGroup](OptionsGroup.html) getParent()
add
public void add([OptionsGroup](OptionsGroup.html) group)
remove
public void remove([OptionsGroup](OptionsGroup.html) group)
getChildren
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[OptionsGroup](OptionsGroup.html)> getChildren()
sortChildren
public void sortChildren([Comparator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)<[OptionsGroup](OptionsGroup.html)> comparator)
resetCachedValues
protected void resetCachedValues()
clone
protected [OptionsGroup](OptionsGroup.html) clone()
Overrides:
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
canDisplay
public boolean canDisplay(com.nomagic.magicdraw.usermodes.UserMode mode)
getModelingLanguage
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getModelingLanguage()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class OptionsGroup">Class OptionsGroup</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.OptionsGroup</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractPropertyOptionsGroup</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">OptionsGroup</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></span></div>
<div class="block">Represents general application options.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>AbstractPropertyOptionsGroup</code></a></li>
<li><a href="EnvironmentOptions.html" title="class in com.nomagic.magicdraw.core.options"><code>EnvironmentOptions</code></a></li>
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
<div class="col-first even-row-color"><code>protected static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ICON_ENVIRONMENT_OPTIONS">ICON_ENVIRONMENT_OPTIONS</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,boolean)">OptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean visible)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>protected </code></div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,javax.swing.Icon,boolean)">OptionsGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 boolean visible)</code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.nomagic.magicdraw.core.options.OptionsGroup)">add</a><wbr/>(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">afterLoad</a><wbr/>(com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#afterSave()">afterSave</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#beforeLoad(boolean)">beforeLoad</a><wbr/>(boolean pluginsLoaded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#canDisplay(com.nomagic.magicdraw.usermodes.UserMode)">canDisplay</a><wbr/>(com.nomagic.magicdraw.usermodes.UserMode mode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clone()">clone</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>abstract com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createOptionsPanel()">createOptionsPanel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates options panel for editing the properties.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#firstInit(boolean)">firstInit</a><wbr/>(boolean pluginsLoaded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.ui.banners.Banner</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBanner()">getBanner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildren()">getChildren</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroupIcon()">getGroupIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns icon to display with options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../../ui/SwingImageIcon.html" title="class in com.nomagic.ui">SwingImageIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getIcon()">getIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #getGroupIcon()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getModelingLanguage()">getModelingLanguage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets human-readable name of options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOptionsToSave()">getOptionsToSave</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnabled()">isEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isVisible()">isVisible</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#loadOptions(com.nomagic.magicdraw.properties.Style,boolean)">loadOptions</a><wbr/>(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style,
 boolean pluginsLoaded)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.nomagic.magicdraw.core.options.OptionsGroup)">remove</a><wbr/>(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resetCachedValues()">resetCachedValues</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnabled(boolean)">setEnabled</a><wbr/>(boolean enabled)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisible(boolean)">setVisible</a><wbr/>(boolean visible)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#sortChildren(java.util.Comparator)">sortChildren</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a>&gt; comparator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
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
<section class="detail" id="ICON_ENVIRONMENT_OPTIONS">
<h3>ICON_ENVIRONMENT_OPTIONS</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">ICON_ENVIRONMENT_OPTIONS</span></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,javax.swing.Icon,boolean)">
<h3>OptionsGroup</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">OptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 boolean visible)</span></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,boolean)">
<h3>OptionsGroup</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">OptionsGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 boolean visible)</span></div>
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
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getGroupIcon()">
<h3>getGroupIcon</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a></span> <span class="element-name">getGroupIcon</span>()</div>
<div class="block">Returns icon to display with options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>icon to display with options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIcon()">
<h3>getIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../../ui/SwingImageIcon.html" title="class in com.nomagic.ui">SwingImageIcon</a></span> <span class="element-name">getIcon</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use #getGroupIcon()</div>
</div>
<div class="block">Returns icon to display with options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>icon to display with options</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createOptionsPanel()">
<h3>createOptionsPanel</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public abstract</span> <span class="return-type">com.nomagic.magicdraw.ui.dialogs.options.BaseOptionsPanel</span> <span class="element-name">createOptionsPanel</span>()</div>
<div class="block">Creates options panel for editing the properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>created options panel.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVisible()">
<h3>isVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVisible</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setVisible(boolean)">
<h3>setVisible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisible</span><wbr/><span class="parameters">(boolean visible)</span></div>
</section>
</li>
<li>
<section class="detail" id="isEnabled()">
<h3>isEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnabled</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setEnabled(boolean)">
<h3>setEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnabled</span><wbr/><span class="parameters">(boolean enabled)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOptionsToSave()">
<h3>getOptionsToSave</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></span> <span class="element-name">getOptionsToSave</span>()</div>
</section>
</li>
<li>
<section class="detail" id="firstInit(boolean)">
<h3>firstInit</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">firstInit</span><wbr/><span class="parameters">(boolean pluginsLoaded)</span></div>
</section>
</li>
<li>
<section class="detail" id="afterSave()">
<h3>afterSave</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">afterSave</span>()</div>
</section>
</li>
<li>
<section class="detail" id="loadOptions(com.nomagic.magicdraw.properties.Style,boolean)">
<h3>loadOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadOptions</span><wbr/><span class="parameters">(<a href="../../properties/Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> style,
 boolean pluginsLoaded)</span></div>
</section>
</li>
<li>
<section class="detail" id="beforeLoad(boolean)">
<h3>beforeLoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">beforeLoad</span><wbr/><span class="parameters">(boolean pluginsLoaded)</span></div>
</section>
</li>
<li>
<section class="detail" id="afterLoad(com.nomagic.magicdraw.lic.MDVersion,boolean)">
<h3>afterLoad</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">afterLoad</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version,
 boolean pluginsLoaded)</span></div>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Gets human-readable name of options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>human-readable name of options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBanner()">
<h3>getBanner</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type">com.nomagic.ui.banners.Banner</span> <span class="element-name">getBanner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></span> <span class="element-name">getParent</span>()</div>
</section>
</li>
<li>
<section class="detail" id="add(com.nomagic.magicdraw.core.options.OptionsGroup)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="remove(com.nomagic.magicdraw.core.options.OptionsGroup)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">remove</span><wbr/><span class="parameters">(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="getChildren()">
<h3>getChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a>&gt;</span> <span class="element-name">getChildren</span>()</div>
</section>
</li>
<li>
<section class="detail" id="sortChildren(java.util.Comparator)">
<h3>sortChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">sortChildren</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html" title="class or interface in java.util">Comparator</a>&lt;<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a>&gt; comparator)</span></div>
</section>
</li>
<li>
<section class="detail" id="resetCachedValues()">
<h3>resetCachedValues</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">resetCachedValues</span>()</div>
</section>
</li>
<li>
<section class="detail" id="clone()">
<h3>clone</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></span> <span class="element-name">clone</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="canDisplay(com.nomagic.magicdraw.usermodes.UserMode)">
<h3>canDisplay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">canDisplay</span><wbr/><span class="parameters">(com.nomagic.magicdraw.usermodes.UserMode mode)</span></div>
</section>
</li>
<li>
<section class="detail" id="getModelingLanguage()">
<h3>getModelingLanguage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getModelingLanguage</span>()</div>
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
