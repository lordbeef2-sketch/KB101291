# JAVA OPENAPI: PluginDescriptor (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/plugins/PluginDescriptor.html
- source_path: `com/nomagic/magicdraw/plugins/PluginDescriptor.html`
- source_sha256: `5e08a2016225fab4c7f55ba879f8a4ec780f345f0911f1e52cf5f224e7cd0fe5`
- captured_utc: `2026-07-14T16:55:27.667150+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.plugins](package-summary.html)

## Class PluginDescriptor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.plugins.PluginDescriptor

@OpenApiAllpublic classPluginDescriptor
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The plugin descriptor class.
 Contains all information about plugin. This information is taken from `plugin.xml` file.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[PluginDescriptor.ClassLookupStrategy](PluginDescriptor.ClassLookupStrategy.html)`
Class lookup strategy.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[PluginDescriptor](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addRequiredPlugin](#addRequiredPlugin(java.lang.String,com.nomagic.magicdraw.plugins.RequiredPlugin))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pluginID,
 [RequiredPlugin](RequiredPlugin.html) requiredPlugin)`
Adds record about required plugin.
`void`
`[addVMOption](#addVMOption(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) option)`
Add vm option.
`[PluginDescriptor.ClassLookupStrategy](PluginDescriptor.ClassLookupStrategy.html)`
`[getClassLookupStrategy](#getClassLookupStrategy())()`
Get class lookup strategy.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassName](#getClassName())()`
Returns plugin class name.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getID](#getID())()`
Returns plugin id.
`int`
`[getInternalVersion](#getInternalVersion())()`
Returns plugin internal version number
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLicenseID](#getLicenseID())()`
Returns plugin license id.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Returns plugin name.
`[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)`
`[getPluginDirectory](#getPluginDirectory())()`
Returns the plugin installation directory.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getProvider](#getProvider())()`
Returns plugin provider.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getRequiresAPI](#getRequiresAPI())()`
Returns the required MagicDraw Open API version.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[RequiredPlugin](RequiredPlugin.html)>`
`[getRequiresPlugins](#getRequiresPlugins())()`
Returns record about required plugins.
`[URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html)[]`
`[getRuntimeLibraries](#getRuntimeLibraries())()`
Returns an array of required jars for this plugin.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getVersion](#getVersion())()`
Return plugin version.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getVmOptions](#getVmOptions())()`
Get all vm option that should be used when loading the plugin.
`boolean`
`[isEnabled](#isEnabled())()`
Returns true, if this plugin is enabled by user.
`boolean`
`[isLoaded](#isLoaded())()`
Returns true, if this plugin is loaded.
`boolean`
`[isSeparateClassloader](#isSeparateClassloader())()`
Checks if plugin needs separate classloader.
`void`
`[setClassLookupStrategy](#setClassLookupStrategy(com.nomagic.magicdraw.plugins.PluginDescriptor.ClassLookupStrategy))([PluginDescriptor.ClassLookupStrategy](PluginDescriptor.ClassLookupStrategy.html) lookupStrategy)`
Set class lookup strategy.
`void`
`[setClassName](#setClassName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) aClass)`
Sets plugin class name.
`void`
`[setEnabled](#setEnabled(boolean))(boolean enabled)`
Sets enabled flag.
`void`
`[setID](#setID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets plugin id.
`void`
`[setInternalVersion](#setInternalVersion(int))(int internalVersion)`
Sets plugin internal version number
`void`
`[setLicenseID](#setLicenseID(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Sets plugin license id.
`void`
`[setLoaded](#setLoaded(boolean))(boolean loaded)`
Sets loaded flag.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`
Sets the name of the plugin.
`void`
`[setPluginDirectory](#setPluginDirectory(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) directory)`
Sets the plugin installation directory.
`void`
`[setProvider](#setProvider(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) provider)`
Sets plugin provider.
`void`
`[setRequiresAPI](#setRequiresAPI(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Sets the required MagicDraw Open API version.
`void`
`[setRuntimeLibraries](#setRuntimeLibraries(java.net.URL%5B%5D))([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html)[] libraries)`
Sets an array of required jars for this plugin.
`void`
`[setSeparateClassloader](#setSeparateClassloader(boolean))(boolean separateClassloader)`
Set to use separate classloader.
`void`
`[setVersion](#setVersion(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)`
Sets the plugin version.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Provides some useful information about this class attributes.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PluginDescriptor
public PluginDescriptor()
 ============ METHOD DETAIL ========== 
Method Details
setClassName
public void setClassName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) aClass)
Sets plugin class name.
Parameters:
`aClass` - the plugin class name.
getClassName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassName()
Returns plugin class name.
Returns:
plugin class name.
setID
public void setID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Sets plugin id.
Parameters:
`id` - the plugin id.
getID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getID()
Returns plugin id.
Returns:
plugins id.
setLicenseID
public void setLicenseID([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Sets plugin license id.
Parameters:
`id` - the plugin license id.
getLicenseID
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLicenseID()
Returns plugin license id.
Returns:
plugins license id.
getInternalVersion
public int getInternalVersion()
Returns plugin internal version number
Returns:
internal version number
setInternalVersion
public void setInternalVersion(int internalVersion)
Sets plugin internal version number
Parameters:
`internalVersion` - plugin internal version number
setName
public void setName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
Sets the name of the plugin.
Parameters:
`name` - the plugin name.
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Returns plugin name.
Returns:
name of the plugin.
setProvider
public void setProvider([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) provider)
Sets plugin provider.
Parameters:
`provider` - the plugin provider.
getProvider
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getProvider()
Returns plugin provider.
Returns:
the plugin provider name(company or person).
setRequiresAPI
public void setRequiresAPI(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Sets the required MagicDraw Open API version.
Parameters:
`version` - the required version number. Must be double.
getRequiresAPI
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getRequiresAPI()
Returns the required MagicDraw Open API version.
Returns:
the required version number.
setRuntimeLibraries
public void setRuntimeLibraries([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html)[] libraries)
Sets an array of required jars for this plugin.
Parameters:
`libraries` - the array of required libraries.
getRuntimeLibraries
public [URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html)[] getRuntimeLibraries()
Returns an array of required jars for this plugin.
Returns:
the array of required libraries.
setVersion
public void setVersion([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) version)
Sets the plugin version.
Parameters:
`version` - the plugin version.
getVersion
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getVersion()
Return plugin version.
Returns:
the plugin version.
setPluginDirectory
public void setPluginDirectory([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) directory)
Sets the plugin installation directory.
 This is a directory there plugin descriptor xml file was found.
Parameters:
`directory` - the plugin directory.
getPluginDirectory
public [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) getPluginDirectory()
Returns the plugin installation directory.
 This is a directory there plugin descriptor xml file was found.
Returns:
the plugin directory.
getRequiresPlugins
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[RequiredPlugin](RequiredPlugin.html)> getRequiresPlugins()
Returns record about required plugins.
Returns:
map of required plugins(key - plugin id, value - required plugin).
addRequiredPlugin
public void addRequiredPlugin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pluginID,
 [RequiredPlugin](RequiredPlugin.html) requiredPlugin)
Adds record about required plugin.
Parameters:
`pluginID` - the id of the plugin.
`requiredPlugin` - the required plugin descriptor
isEnabled
public boolean isEnabled()
Returns true, if this plugin is enabled by user.
Returns:
true, if this plugin is enabled by user.
setEnabled
public void setEnabled(boolean enabled)
Sets enabled flag.
Parameters:
`enabled` - the new value of enabled flag.
isLoaded
public boolean isLoaded()
Returns true, if this plugin is loaded.
Returns:
true, if this plugin is loaded.
setLoaded
public void setLoaded(boolean loaded)
Sets loaded flag.
Parameters:
`loaded` - the new value of loaded flag.
setSeparateClassloader
public void setSeparateClassloader(boolean separateClassloader)
Set to use separate classloader.
Parameters:
`separateClassloader` - use separate classloader
isSeparateClassloader
public boolean isSeparateClassloader()
Checks if plugin needs separate classloader.
Returns:
true if plugin needs separate classloader.
getClassLookupStrategy
public [PluginDescriptor.ClassLookupStrategy](PluginDescriptor.ClassLookupStrategy.html) getClassLookupStrategy()
Get class lookup strategy.
Returns:
lookup strategy.
setClassLookupStrategy
public void setClassLookupStrategy([PluginDescriptor.ClassLookupStrategy](PluginDescriptor.ClassLookupStrategy.html) lookupStrategy)
Set class lookup strategy.
Parameters:
`lookupStrategy` - lookup strategy.
addVMOption
public void addVMOption([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) option)
Add vm option.
Parameters:
`option` - a new vm option.
getVmOptions
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getVmOptions()
Get all vm option that should be used when loading the plugin.
Returns:
a collection of vm options.
toString
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Provides some useful information about this class attributes.
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
Returns:
the string representation.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.plugins</a></div>
<h1 class="title" title="Class PluginDescriptor">Class PluginDescriptor</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.plugins.PluginDescriptor</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PluginDescriptor</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The plugin descriptor class.
 Contains all information about plugin. This information is taken from <code>plugin.xml</code> file.</div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="PluginDescriptor.ClassLookupStrategy.html" title="enum class in com.nomagic.magicdraw.plugins">PluginDescriptor.ClassLookupStrategy</a></code></div>
<div class="col-last even-row-color">
<div class="block">Class lookup strategy.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PluginDescriptor</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRequiredPlugin(java.lang.String,com.nomagic.magicdraw.plugins.RequiredPlugin)">addRequiredPlugin</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pluginID,
 <a href="RequiredPlugin.html" title="class in com.nomagic.magicdraw.plugins">RequiredPlugin</a> requiredPlugin)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds record about required plugin.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addVMOption(java.lang.String)">addVMOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> option)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add vm option.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PluginDescriptor.ClassLookupStrategy.html" title="enum class in com.nomagic.magicdraw.plugins">PluginDescriptor.ClassLookupStrategy</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassLookupStrategy()">getClassLookupStrategy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get class lookup strategy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassName()">getClassName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin class name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getID()">getID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInternalVersion()">getInternalVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin internal version number</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLicenseID()">getLicenseID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin license id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPluginDirectory()">getPluginDirectory</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the plugin installation directory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProvider()">getProvider</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns plugin provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiresAPI()">getRequiresAPI</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the required MagicDraw Open API version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="RequiredPlugin.html" title="class in com.nomagic.magicdraw.plugins">RequiredPlugin</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiresPlugins()">getRequiresPlugins</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns record about required plugins.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRuntimeLibraries()">getRuntimeLibraries</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns an array of required jars for this plugin.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion()">getVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return plugin version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVmOptions()">getVmOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all vm option that should be used when loading the plugin.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnabled()">isEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if this plugin is enabled by user.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isLoaded()">isLoaded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true, if this plugin is loaded.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSeparateClassloader()">isSeparateClassloader</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if plugin needs separate classloader.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClassLookupStrategy(com.nomagic.magicdraw.plugins.PluginDescriptor.ClassLookupStrategy)">setClassLookupStrategy</a><wbr/>(<a href="PluginDescriptor.ClassLookupStrategy.html" title="enum class in com.nomagic.magicdraw.plugins">PluginDescriptor.ClassLookupStrategy</a> lookupStrategy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set class lookup strategy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClassName(java.lang.String)">setClassName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> aClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets plugin class name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnabled(boolean)">setEnabled</a><wbr/>(boolean enabled)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets enabled flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setID(java.lang.String)">setID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets plugin id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInternalVersion(int)">setInternalVersion</a><wbr/>(int internalVersion)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets plugin internal version number</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLicenseID(java.lang.String)">setLicenseID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets plugin license id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoaded(boolean)">setLoaded</a><wbr/>(boolean loaded)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets loaded flag.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the name of the plugin.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setPluginDirectory(java.io.File)">setPluginDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> directory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the plugin installation directory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProvider(java.lang.String)">setProvider</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> provider)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets plugin provider.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRequiresAPI(java.lang.String)">setRequiresAPI</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the required MagicDraw Open API version.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRuntimeLibraries(java.net.URL%5B%5D)">setRuntimeLibraries</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[] libraries)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets an array of required jars for this plugin.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeparateClassloader(boolean)">setSeparateClassloader</a><wbr/>(boolean separateClassloader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set to use separate classloader.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVersion(java.lang.String)">setVersion</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the plugin version.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Provides some useful information about this class attributes.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>PluginDescriptor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PluginDescriptor</span>()</div>
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
<section class="detail" id="setClassName(java.lang.String)">
<h3>setClassName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClassName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> aClass)</span></div>
<div class="block">Sets plugin class name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aClass</code> - the plugin class name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassName()">
<h3>getClassName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassName</span>()</div>
<div class="block">Returns plugin class name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>plugin class name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setID(java.lang.String)">
<h3>setID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets plugin id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the plugin id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getID()">
<h3>getID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getID</span>()</div>
<div class="block">Returns plugin id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>plugins id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLicenseID(java.lang.String)">
<h3>setLicenseID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLicenseID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Sets plugin license id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - the plugin license id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLicenseID()">
<h3>getLicenseID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLicenseID</span>()</div>
<div class="block">Returns plugin license id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>plugins license id.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInternalVersion()">
<h3>getInternalVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getInternalVersion</span>()</div>
<div class="block">Returns plugin internal version number</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>internal version number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInternalVersion(int)">
<h3>setInternalVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInternalVersion</span><wbr/><span class="parameters">(int internalVersion)</span></div>
<div class="block">Sets plugin internal version number</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>internalVersion</code> - plugin internal version number</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Sets the name of the plugin.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the plugin name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Returns plugin name.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of the plugin.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProvider(java.lang.String)">
<h3>setProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProvider</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> provider)</span></div>
<div class="block">Sets plugin provider.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>provider</code> - the plugin provider.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProvider()">
<h3>getProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getProvider</span>()</div>
<div class="block">Returns plugin provider.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the plugin provider name(company or person).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRequiresAPI(java.lang.String)">
<h3>setRequiresAPI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRequiresAPI</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Sets the required MagicDraw Open API version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - the required version number. Must be double.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiresAPI()">
<h3>getRequiresAPI</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getRequiresAPI</span>()</div>
<div class="block">Returns the required MagicDraw Open API version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the required version number.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRuntimeLibraries(java.net.URL[])">
<h3>setRuntimeLibraries</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRuntimeLibraries</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[] libraries)</span></div>
<div class="block">Sets an array of required jars for this plugin.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>libraries</code> - the array of required libraries.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRuntimeLibraries()">
<h3>getRuntimeLibraries</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[]</span> <span class="element-name">getRuntimeLibraries</span>()</div>
<div class="block">Returns an array of required jars for this plugin.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the array of required libraries.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVersion(java.lang.String)">
<h3>setVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVersion</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Sets the plugin version.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - the plugin version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion()">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVersion</span>()</div>
<div class="block">Return plugin version.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the plugin version.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPluginDirectory(java.io.File)">
<h3>setPluginDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPluginDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> directory)</span></div>
<div class="block">Sets the plugin installation directory.
 This is a directory there plugin descriptor xml file was found.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>directory</code> - the plugin directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPluginDirectory()">
<h3>getPluginDirectory</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getPluginDirectory</span>()</div>
<div class="block">Returns the plugin installation directory.
 This is a directory there plugin descriptor xml file was found.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the plugin directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiresPlugins()">
<h3>getRequiresPlugins</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="RequiredPlugin.html" title="class in com.nomagic.magicdraw.plugins">RequiredPlugin</a>&gt;</span> <span class="element-name">getRequiresPlugins</span>()</div>
<div class="block">Returns record about required plugins.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of required plugins(key - plugin id, value - required plugin).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addRequiredPlugin(java.lang.String,com.nomagic.magicdraw.plugins.RequiredPlugin)">
<h3>addRequiredPlugin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addRequiredPlugin</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pluginID,
 <a href="RequiredPlugin.html" title="class in com.nomagic.magicdraw.plugins">RequiredPlugin</a> requiredPlugin)</span></div>
<div class="block">Adds record about required plugin.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pluginID</code> - the id of the plugin.</dd>
<dd><code>requiredPlugin</code> - the required plugin descriptor</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnabled()">
<h3>isEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnabled</span>()</div>
<div class="block">Returns true, if this plugin is enabled by user.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if this plugin is enabled by user.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnabled(boolean)">
<h3>setEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnabled</span><wbr/><span class="parameters">(boolean enabled)</span></div>
<div class="block">Sets enabled flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enabled</code> - the new value of enabled flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isLoaded()">
<h3>isLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isLoaded</span>()</div>
<div class="block">Returns true, if this plugin is loaded.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if this plugin is loaded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLoaded(boolean)">
<h3>setLoaded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoaded</span><wbr/><span class="parameters">(boolean loaded)</span></div>
<div class="block">Sets loaded flag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>loaded</code> - the new value of loaded flag.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSeparateClassloader(boolean)">
<h3>setSeparateClassloader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeparateClassloader</span><wbr/><span class="parameters">(boolean separateClassloader)</span></div>
<div class="block">Set to use separate classloader.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>separateClassloader</code> - use separate classloader</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSeparateClassloader()">
<h3>isSeparateClassloader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSeparateClassloader</span>()</div>
<div class="block">Checks if plugin needs separate classloader.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if plugin needs separate classloader.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassLookupStrategy()">
<h3>getClassLookupStrategy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="PluginDescriptor.ClassLookupStrategy.html" title="enum class in com.nomagic.magicdraw.plugins">PluginDescriptor.ClassLookupStrategy</a></span> <span class="element-name">getClassLookupStrategy</span>()</div>
<div class="block">Get class lookup strategy.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>lookup strategy.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassLookupStrategy(com.nomagic.magicdraw.plugins.PluginDescriptor.ClassLookupStrategy)">
<h3>setClassLookupStrategy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClassLookupStrategy</span><wbr/><span class="parameters">(<a href="PluginDescriptor.ClassLookupStrategy.html" title="enum class in com.nomagic.magicdraw.plugins">PluginDescriptor.ClassLookupStrategy</a> lookupStrategy)</span></div>
<div class="block">Set class lookup strategy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lookupStrategy</code> - lookup strategy.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addVMOption(java.lang.String)">
<h3>addVMOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addVMOption</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> option)</span></div>
<div class="block">Add vm option.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>option</code> - a new vm option.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVmOptions()">
<h3>getVmOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getVmOptions</span>()</div>
<div class="block">Get all vm option that should be used when loading the plugin.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a collection of vm options.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<div class="block">Provides some useful information about this class attributes.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Returns:</dt>
<dd>the string representation.</dd>
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
