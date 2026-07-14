# JAVA OPENAPI: EnvironmentOptions (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/options/EnvironmentOptions.html
- source_path: `com/nomagic/magicdraw/core/options/EnvironmentOptions.html`
- source_sha256: `f32876e9e9054ade26e7861d6063af997f6fe60e4518557f734eba80942460e5`
- captured_utc: `2026-07-14T16:55:11.938973+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Class EnvironmentOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.core.options.EnvironmentOptions

@OpenApipublic classEnvironmentOptions
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Represents application environment options.

Application-related options are referred to as environment options.
 They are saved in the `global.opt` file that is located in `<USER_HOME_DIR>/.magicdraw/<VERSION_NUMBER>/data`.

You can add custom environment options for MagicDraw.

To add your own environment options
 1. Extend the AbstractPropertyOptionsGroup class.
 2. Add the extending class to application environment options.

##### Example: Adding custom environment options

````java
class MyOptionsGroup extends AbstractPropertyOptionsGroup
 {
     ...
 }

 Application application = Application.getInstance();
 EnvironmentOptions options = application.getEnvironmentOptions();
 options.addGroup(new ExampleOptionsGroup());
````

See Also:
[`OptionsGroup`](OptionsGroup.html)
[`AbstractPropertyOptionsGroup`](AbstractPropertyOptionsGroup.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static interface`
`[EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html)`
Receives events when environment options change
 in the environment options dialog after "Ok" is pressed.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[OPTIONS_FILE_PATH](#OPTIONS_FILE_PATH)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[EnvironmentOptions](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addEnvironmentChangeListener](#addEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener))([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)`
Adds environment change listener to environment options.
`void`
`[addGroup](#addGroup(com.nomagic.magicdraw.core.options.OptionsGroup))([OptionsGroup](OptionsGroup.html) group)`
Adds an option group to the environment options.
`void`
`[applyLoadedData](#applyLoadedData(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.properties.StyleManager,boolean))(com.nomagic.magicdraw.lic.MDVersion version,
 [StyleManager](../../properties/StyleManager.html) styleManager,
 boolean pluginsLoaded)`

`com.nomagic.magicdraw.core.options.BrowserOptionsGroup`
`[getBrowserOptions](#getBrowserOptions())()`

`[CircularLayouterOptionsGroup](CircularLayouterOptionsGroup.html)`
`[getCircularLayouterOptionsGroup](#getCircularLayouterOptionsGroup())()`

`[ClassDiagramLayouterOptionsGroup](ClassDiagramLayouterOptionsGroup.html)`
`[getClassDiagramLayouterOptionsGroup](#getClassDiagramLayouterOptionsGroup())()`

`com.nomagic.magicdraw.core.options.CompositionInspectionGroup`
`[getCompositionInspectionOptions](#getCompositionInspectionOptions())()`

`com.nomagic.magicdraw.core.options.CustomMetalThemeOptionsGroup`
`[getCustomMetalThemeOptions](#getCustomMetalThemeOptions())()`

`com.nomagic.magicdraw.core.options.DiagramOptionsGroup`
`[getDiagramOptions](#getDiagramOptions())()`

`com.nomagic.magicdraw.core.options.ExperienceOptionsGroup`
`[getExperienceOptionsGroup](#getExperienceOptionsGroup())()`

`com.nomagic.magicdraw.core.options.ExternalToolsOptionsGroup`
`[getExternalToolsOptions](#getExternalToolsOptions())()`

`com.nomagic.magicdraw.core.options.FloatingOptionsGroup`
`[getFloatingOptions](#getFloatingOptions())()`

`com.nomagic.magicdraw.core.options.GeneralOptionsGroup`
`[getGeneralOptions](#getGeneralOptions())()`

`[OptionsGroup](OptionsGroup.html)`
`[getGroup](#getGroup(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[OptionsGroup](OptionsGroup.html)>`
`[getGroups](#getGroups())()`

`[HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html)`
`[getHierarchicLayouterOptionsGroup](#getHierarchicLayouterOptionsGroup())()`

`com.nomagic.magicdraw.core.options.KeyboardOptionsGroup`
`[getKeyboardOptions](#getKeyboardOptions())()`

`com.nomagic.magicdraw.core.options.LaunchersOptionsGroup`
`[getLaunchersOptionsGroup](#getLaunchersOptionsGroup())()`

`[OrganicRouterOptionsGroup](OrganicRouterOptionsGroup.html)`
`[getLinkRouterOptionsGroup](#getLinkRouterOptionsGroup())()`

`com.nomagic.magicdraw.core.options.NetworkOptionsGroup`
`[getNetworkOptions](#getNetworkOptions())()`

`com.nomagic.magicdraw.core.options.NotificationOptionsGroup`
`[getNotificationOptions](#getNotificationOptions())()`
Returns notification options group
`[OrganicLayouterOptionsGroup](OrganicLayouterOptionsGroup.html)`
`[getOrganicLayouterOptionsGroup](#getOrganicLayouterOptionsGroup())()`

`[OrthogonalLayouterOptionsGroup](OrthogonalLayouterOptionsGroup.html)`
`[getOrthogonalLayouterOptionsGroup](#getOrthogonalLayouterOptionsGroup())()`

`[PathVariablesOptionsGroup](PathVariablesOptionsGroup.html)`
`[getPathVariablesOptions](#getPathVariablesOptions())()`
Get path variables options.
`com.nomagic.magicdraw.core.options.ResourcesOptionsGroup`
`[getResourcesOptions](#getResourcesOptions())()`

`com.nomagic.magicdraw.core.options.SpecificationPropertiesOptionsGroup`
`[getSpecificationPropertiesOptionsGroup](#getSpecificationPropertiesOptionsGroup())()`

`com.nomagic.magicdraw.spellchecker.SpellingOptionsGroup`
`[getSpellingOptions](#getSpellingOptions())()`

`com.nomagic.magicdraw.core.options.SymbolPropertiesOptionsGroup`
`[getSymbolPropertiesOptionsGroup](#getSymbolPropertiesOptionsGroup())()`

`[TeamworkOptionsGroup](TeamworkOptionsGroup.html)`
`[getTeamworkOptions](#getTeamworkOptions())()`

`[TreeLayouterOptionsGroup](TreeLayouterOptionsGroup.html)`
`[getTreeLayouterOptionsGroup](#getTreeLayouterOptionsGroup())()`

`void`
`[insertEnvironmentChangeListener](#insertEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener))([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)`
Adds environment change listener to environment options.
`static [StyleManager](../../properties/StyleManager.html)`
`[load](#load(boolean))(boolean silent)`
Load properties
`void`
`[optionsChanged](#optionsChanged(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)> props)`

`void`
`[removeEnvironmentChangeListener](#removeEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener))([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)`
Removes environment change listener.
`void`
`[removeGroup](#removeGroup(com.nomagic.magicdraw.core.options.OptionsGroup))([OptionsGroup](OptionsGroup.html) group)`

`void`
`[save](#save())()`
Saves properties
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
OPTIONS_FILE_PATH
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) OPTIONS_FILE_PATH
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
EnvironmentOptions
public EnvironmentOptions()
 ============ METHOD DETAIL ========== 
Method Details
addGroup
@OpenApipublic void addGroup([OptionsGroup](OptionsGroup.html) group)
Adds an option group to the environment options.
Parameters:
`group` - option group to add.
removeGroup
public void removeGroup([OptionsGroup](OptionsGroup.html) group)
getGroups
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[OptionsGroup](OptionsGroup.html)> getGroups()
getGroup
public [OptionsGroup](OptionsGroup.html) getGroup([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
getDiagramOptions
public com.nomagic.magicdraw.core.options.DiagramOptionsGroup getDiagramOptions()
getNotificationOptions
public com.nomagic.magicdraw.core.options.NotificationOptionsGroup getNotificationOptions()
Returns notification options group
Returns:
notification options group
getGeneralOptions
public com.nomagic.magicdraw.core.options.GeneralOptionsGroup getGeneralOptions()
getBrowserOptions
public com.nomagic.magicdraw.core.options.BrowserOptionsGroup getBrowserOptions()
getCompositionInspectionOptions
public com.nomagic.magicdraw.core.options.CompositionInspectionGroup getCompositionInspectionOptions()
getTeamworkOptions
public [TeamworkOptionsGroup](TeamworkOptionsGroup.html) getTeamworkOptions()
getFloatingOptions
public com.nomagic.magicdraw.core.options.FloatingOptionsGroup getFloatingOptions()
getExternalToolsOptions
public com.nomagic.magicdraw.core.options.ExternalToolsOptionsGroup getExternalToolsOptions()
getExperienceOptionsGroup
public com.nomagic.magicdraw.core.options.ExperienceOptionsGroup getExperienceOptionsGroup()
getNetworkOptions
public com.nomagic.magicdraw.core.options.NetworkOptionsGroup getNetworkOptions()
getKeyboardOptions
public com.nomagic.magicdraw.core.options.KeyboardOptionsGroup getKeyboardOptions()
getResourcesOptions
public com.nomagic.magicdraw.core.options.ResourcesOptionsGroup getResourcesOptions()
getPathVariablesOptions
@OpenApipublic [PathVariablesOptionsGroup](PathVariablesOptionsGroup.html) getPathVariablesOptions()
Get path variables options.
Returns:
path variables options group.
getSpellingOptions
public com.nomagic.magicdraw.spellchecker.SpellingOptionsGroup getSpellingOptions()
getCustomMetalThemeOptions
public com.nomagic.magicdraw.core.options.CustomMetalThemeOptionsGroup getCustomMetalThemeOptions()
getLaunchersOptionsGroup
public com.nomagic.magicdraw.core.options.LaunchersOptionsGroup getLaunchersOptionsGroup()
getOrganicLayouterOptionsGroup
public [OrganicLayouterOptionsGroup](OrganicLayouterOptionsGroup.html) getOrganicLayouterOptionsGroup()
getHierarchicLayouterOptionsGroup
public [HierarchicLayouterOptionsGroup](HierarchicLayouterOptionsGroup.html) getHierarchicLayouterOptionsGroup()
getCircularLayouterOptionsGroup
public [CircularLayouterOptionsGroup](CircularLayouterOptionsGroup.html) getCircularLayouterOptionsGroup()
getClassDiagramLayouterOptionsGroup
public [ClassDiagramLayouterOptionsGroup](ClassDiagramLayouterOptionsGroup.html) getClassDiagramLayouterOptionsGroup()
getOrthogonalLayouterOptionsGroup
public [OrthogonalLayouterOptionsGroup](OrthogonalLayouterOptionsGroup.html) getOrthogonalLayouterOptionsGroup()
getTreeLayouterOptionsGroup
public [TreeLayouterOptionsGroup](TreeLayouterOptionsGroup.html) getTreeLayouterOptionsGroup()
getLinkRouterOptionsGroup
public [OrganicRouterOptionsGroup](OrganicRouterOptionsGroup.html) getLinkRouterOptionsGroup()
getSpecificationPropertiesOptionsGroup
public com.nomagic.magicdraw.core.options.SpecificationPropertiesOptionsGroup getSpecificationPropertiesOptionsGroup()
getSymbolPropertiesOptionsGroup
public com.nomagic.magicdraw.core.options.SymbolPropertiesOptionsGroup getSymbolPropertiesOptionsGroup()
load
@CheckForNullpublic static [StyleManager](../../properties/StyleManager.html) load(boolean silent)
Load properties
Parameters:
`silent` - silent load mode
Returns:
loaded properties
applyLoadedData
public void applyLoadedData(@CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version,
 @CheckForNull
 [StyleManager](../../properties/StyleManager.html) styleManager,
 boolean pluginsLoaded)
save
public void save()
Saves properties
optionsChanged
public void optionsChanged([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Property](../../properties/Property.html)> props)
Parameters:
`props` - changed properties
addEnvironmentChangeListener
@OpenApipublic void addEnvironmentChangeListener([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)
Adds environment change listener to environment options.
 Make sure to have a strong reference to the listener in the client code,
 because listeners are managed through weak references to avoid memory leaks.
Parameters:
`listener` - listener to add.
insertEnvironmentChangeListener
public void insertEnvironmentChangeListener([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)
Adds environment change listener to environment options.
 NOTE: Make sure to have a strong reference to the listener in the client code,
 because listeners are managed through weak references to avoid memory leaks.
Parameters:
`listener` - instance of [`EnvironmentOptions.EnvironmentChangeListener`](EnvironmentOptions.EnvironmentChangeListener.html)
removeEnvironmentChangeListener
@OpenApipublic void removeEnvironmentChangeListener([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)
Removes environment change listener.
Parameters:
`listener` - listener to remove.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Class EnvironmentOptions">Class EnvironmentOptions</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.core.options.EnvironmentOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">EnvironmentOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 Represents application environment options.
 </p>
<p>
 Application-related options are referred to as environment options.
 They are saved in the <code>global.opt</code> file that is located in <code>&lt;USER_HOME_DIR&gt;/.magicdraw/&lt;VERSION_NUMBER&gt;/data</code>.
 </p>
<p>
 You can add custom environment options for MagicDraw.
 </p>
<p>
 To add your own environment options
 <ul>
<li> 1. Extend the AbstractPropertyOptionsGroup class.
 <li> 2. Add the extending class to application environment options.
 </li></li></ul>
</p>
<h4>Example: Adding custom environment options</h4>
<pre>
 class MyOptionsGroup extends AbstractPropertyOptionsGroup
 {
     ...
 }

 Application application = Application.getInstance();
 EnvironmentOptions options = application.getEnvironmentOptions();
 options.addGroup(new ExampleOptionsGroup());
 </pre></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>OptionsGroup</code></a></li>
<li><a href="AbstractPropertyOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>AbstractPropertyOptionsGroup</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a></code></div>
<div class="col-last even-row-color">
<div class="block">Receives events when environment options change
 in the environment options dialog after "Ok" is pressed.</div>
</div>
</div>
</section>
</li>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#OPTIONS_FILE_PATH">OPTIONS_FILE_PATH</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">EnvironmentOptions</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener)">addEnvironmentChangeListener</a><wbr/>(<a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds environment change listener to environment options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addGroup(com.nomagic.magicdraw.core.options.OptionsGroup)">addGroup</a><wbr/>(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds an option group to the environment options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#applyLoadedData(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.properties.StyleManager,boolean)">applyLoadedData</a><wbr/>(com.nomagic.magicdraw.lic.MDVersion version,
 <a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> styleManager,
 boolean pluginsLoaded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.BrowserOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBrowserOptions()">getBrowserOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="CircularLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">CircularLayouterOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCircularLayouterOptionsGroup()">getCircularLayouterOptionsGroup</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ClassDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">ClassDiagramLayouterOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassDiagramLayouterOptionsGroup()">getClassDiagramLayouterOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.CompositionInspectionGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCompositionInspectionOptions()">getCompositionInspectionOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.CustomMetalThemeOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomMetalThemeOptions()">getCustomMetalThemeOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.DiagramOptionsGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiagramOptions()">getDiagramOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.ExperienceOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExperienceOptionsGroup()">getExperienceOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.ExternalToolsOptionsGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getExternalToolsOptions()">getExternalToolsOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.FloatingOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFloatingOptions()">getFloatingOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.GeneralOptionsGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeneralOptions()">getGeneralOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroup(java.lang.String)">getGroup</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGroups()">getGroups</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHierarchicLayouterOptionsGroup()">getHierarchicLayouterOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.KeyboardOptionsGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getKeyboardOptions()">getKeyboardOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.LaunchersOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLaunchersOptionsGroup()">getLaunchersOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OrganicRouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrganicRouterOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLinkRouterOptionsGroup()">getLinkRouterOptionsGroup</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.NetworkOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNetworkOptions()">getNetworkOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.NotificationOptionsGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNotificationOptions()">getNotificationOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns notification options group</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OrganicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrganicLayouterOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrganicLayouterOptionsGroup()">getOrganicLayouterOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="OrthogonalLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrthogonalLayouterOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrthogonalLayouterOptionsGroup()">getOrthogonalLayouterOptionsGroup</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PathVariablesOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">PathVariablesOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathVariablesOptions()">getPathVariablesOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get path variables options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.ResourcesOptionsGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResourcesOptions()">getResourcesOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.SpecificationPropertiesOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSpecificationPropertiesOptionsGroup()">getSpecificationPropertiesOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.spellchecker.SpellingOptionsGroup</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSpellingOptions()">getSpellingOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicdraw.core.options.SymbolPropertiesOptionsGroup</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSymbolPropertiesOptionsGroup()">getSymbolPropertiesOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TeamworkOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">TeamworkOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTeamworkOptions()">getTeamworkOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="TreeLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">TreeLayouterOptionsGroup</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTreeLayouterOptionsGroup()">getTreeLayouterOptionsGroup</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#insertEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener)">insertEnvironmentChangeListener</a><wbr/>(<a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds environment change listener to environment options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#load(boolean)">load</a><wbr/>(boolean silent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Load properties</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#optionsChanged(java.util.List)">optionsChanged</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; props)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener)">removeEnvironmentChangeListener</a><wbr/>(<a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes environment change listener.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeGroup(com.nomagic.magicdraw.core.options.OptionsGroup)">removeGroup</a><wbr/>(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#save()">save</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves properties</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="OPTIONS_FILE_PATH">
<h3>OPTIONS_FILE_PATH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">OPTIONS_FILE_PATH</span></div>
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
<h3>EnvironmentOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EnvironmentOptions</span>()</div>
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
<section class="detail" id="addGroup(com.nomagic.magicdraw.core.options.OptionsGroup)">
<h3>addGroup</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addGroup</span><wbr/><span class="parameters">(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</span></div>
<div class="block">Adds an option group to the environment options.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>group</code> - option group to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeGroup(com.nomagic.magicdraw.core.options.OptionsGroup)">
<h3>removeGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeGroup</span><wbr/><span class="parameters">(<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a> group)</span></div>
</section>
</li>
<li>
<section class="detail" id="getGroups()">
<h3>getGroups</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a>&gt;</span> <span class="element-name">getGroups</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getGroup(java.lang.String)">
<h3>getGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OptionsGroup</a></span> <span class="element-name">getGroup</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDiagramOptions()">
<h3>getDiagramOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.DiagramOptionsGroup</span> <span class="element-name">getDiagramOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNotificationOptions()">
<h3>getNotificationOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.NotificationOptionsGroup</span> <span class="element-name">getNotificationOptions</span>()</div>
<div class="block">Returns notification options group</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>notification options group</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeneralOptions()">
<h3>getGeneralOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.GeneralOptionsGroup</span> <span class="element-name">getGeneralOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getBrowserOptions()">
<h3>getBrowserOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.BrowserOptionsGroup</span> <span class="element-name">getBrowserOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCompositionInspectionOptions()">
<h3>getCompositionInspectionOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.CompositionInspectionGroup</span> <span class="element-name">getCompositionInspectionOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTeamworkOptions()">
<h3>getTeamworkOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TeamworkOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">TeamworkOptionsGroup</a></span> <span class="element-name">getTeamworkOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getFloatingOptions()">
<h3>getFloatingOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.FloatingOptionsGroup</span> <span class="element-name">getFloatingOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExternalToolsOptions()">
<h3>getExternalToolsOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.ExternalToolsOptionsGroup</span> <span class="element-name">getExternalToolsOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getExperienceOptionsGroup()">
<h3>getExperienceOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.ExperienceOptionsGroup</span> <span class="element-name">getExperienceOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNetworkOptions()">
<h3>getNetworkOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.NetworkOptionsGroup</span> <span class="element-name">getNetworkOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getKeyboardOptions()">
<h3>getKeyboardOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.KeyboardOptionsGroup</span> <span class="element-name">getKeyboardOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getResourcesOptions()">
<h3>getResourcesOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.ResourcesOptionsGroup</span> <span class="element-name">getResourcesOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getPathVariablesOptions()">
<h3>getPathVariablesOptions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="PathVariablesOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">PathVariablesOptionsGroup</a></span> <span class="element-name">getPathVariablesOptions</span>()</div>
<div class="block">Get path variables options.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>path variables options group.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpellingOptions()">
<h3>getSpellingOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.spellchecker.SpellingOptionsGroup</span> <span class="element-name">getSpellingOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCustomMetalThemeOptions()">
<h3>getCustomMetalThemeOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.CustomMetalThemeOptionsGroup</span> <span class="element-name">getCustomMetalThemeOptions</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLaunchersOptionsGroup()">
<h3>getLaunchersOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.LaunchersOptionsGroup</span> <span class="element-name">getLaunchersOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOrganicLayouterOptionsGroup()">
<h3>getOrganicLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OrganicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrganicLayouterOptionsGroup</a></span> <span class="element-name">getOrganicLayouterOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getHierarchicLayouterOptionsGroup()">
<h3>getHierarchicLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">HierarchicLayouterOptionsGroup</a></span> <span class="element-name">getHierarchicLayouterOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getCircularLayouterOptionsGroup()">
<h3>getCircularLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="CircularLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">CircularLayouterOptionsGroup</a></span> <span class="element-name">getCircularLayouterOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getClassDiagramLayouterOptionsGroup()">
<h3>getClassDiagramLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ClassDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">ClassDiagramLayouterOptionsGroup</a></span> <span class="element-name">getClassDiagramLayouterOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getOrthogonalLayouterOptionsGroup()">
<h3>getOrthogonalLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OrthogonalLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrthogonalLayouterOptionsGroup</a></span> <span class="element-name">getOrthogonalLayouterOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getTreeLayouterOptionsGroup()">
<h3>getTreeLayouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="TreeLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">TreeLayouterOptionsGroup</a></span> <span class="element-name">getTreeLayouterOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getLinkRouterOptionsGroup()">
<h3>getLinkRouterOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="OrganicRouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">OrganicRouterOptionsGroup</a></span> <span class="element-name">getLinkRouterOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSpecificationPropertiesOptionsGroup()">
<h3>getSpecificationPropertiesOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.SpecificationPropertiesOptionsGroup</span> <span class="element-name">getSpecificationPropertiesOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSymbolPropertiesOptionsGroup()">
<h3>getSymbolPropertiesOptionsGroup</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicdraw.core.options.SymbolPropertiesOptionsGroup</span> <span class="element-name">getSymbolPropertiesOptionsGroup</span>()</div>
</section>
</li>
<li>
<section class="detail" id="load(boolean)">
<h3>load</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></span> <span class="element-name">load</span><wbr/><span class="parameters">(boolean silent)</span></div>
<div class="block">Load properties</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>silent</code> - silent load mode</dd>
<dt>Returns:</dt>
<dd>loaded properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="applyLoadedData(com.nomagic.magicdraw.lic.MDVersion,com.nomagic.magicdraw.properties.StyleManager,boolean)">
<h3>applyLoadedData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">applyLoadedData</span><wbr/><span class="parameters">(@CheckForNull
 com.nomagic.magicdraw.lic.MDVersion version,
 @CheckForNull
 <a href="../../properties/StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> styleManager,
 boolean pluginsLoaded)</span></div>
</section>
</li>
<li>
<section class="detail" id="save()">
<h3>save</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">save</span>()</div>
<div class="block">Saves properties</div>
</section>
</li>
<li>
<section class="detail" id="optionsChanged(java.util.List)">
<h3>optionsChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">optionsChanged</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../properties/Property.html" title="class in com.nomagic.magicdraw.properties">Property</a>&gt; props)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>props</code> - changed properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener)">
<h3>addEnvironmentChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addEnvironmentChangeListener</span><wbr/><span class="parameters">(<a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a> listener)</span></div>
<div class="block">Adds environment change listener to environment options.
 Make sure to have a strong reference to the listener in the client code,
 because listeners are managed through weak references to avoid memory leaks.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to add.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener)">
<h3>insertEnvironmentChangeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">insertEnvironmentChangeListener</span><wbr/><span class="parameters">(<a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a> listener)</span></div>
<div class="block">Adds environment change listener to environment options.
 NOTE: Make sure to have a strong reference to the listener in the client code,
 because listeners are managed through weak references to avoid memory leaks.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - instance of <a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options"><code>EnvironmentOptions.EnvironmentChangeListener</code></a></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener)">
<h3>removeEnvironmentChangeListener</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeEnvironmentChangeListener</span><wbr/><span class="parameters">(<a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a> listener)</span></div>
<div class="block">Removes environment change listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - listener to remove.</dd>
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
