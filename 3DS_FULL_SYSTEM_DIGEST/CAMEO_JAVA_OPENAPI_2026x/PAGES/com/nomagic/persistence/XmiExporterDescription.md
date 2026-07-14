# JAVA OPENAPI: XmiExporterDescription (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/persistence/XmiExporterDescription.html
- source_path: `com/nomagic/persistence/XmiExporterDescription.html`
- source_sha256: `592916c64d8d0ca1ebdb68790283101dfe5d6baeacd67b16de3ee38d5efc0f7c`
- captured_utc: `2026-07-14T16:58:39.540308+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.persistence](package-summary.html)

## Class XmiExporterDescription

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.persistence.XmiExporterDescription

All Implemented Interfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

@OpenApiAllpublic classXmiExporterDescription
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
implements [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

Project version and required resources/plugins information.

See Also:
[Serialized Form](../../../serialized-form.html#com.nomagic.persistence.XmiExporterDescription)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[XmiExporterDescription](#%3Cinit%3E(java.lang.String,com.nomagic.persistence.FormatVersion))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [FormatVersion](FormatVersion.html) formatVersion)`
Constructor
`[XmiExporterDescription](#%3Cinit%3E(java.lang.String,com.nomagic.persistence.FormatVersion,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [FormatVersion](FormatVersion.html) formatVersion,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) umlURI)`
Constructor
`[XmiExporterDescription](#%3Cinit%3E(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) version)`
Deprecated.
use constructor with FileFormat arguments
`[XmiExporterDescription](#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) version,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) umlURI)`
Deprecated.
use constructor with FileFormat arguments
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addRequiredPlugin](#addRequiredPlugin(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) version)`
Adds required plugin into map.
`void`
`[addRequiredResource](#addRequiredResource(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suggestedId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`
Adds resource as required for project.
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)`

`[FormatVersion](FormatVersion.html)`
`[getFormatVersion](#getFormatVersion())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getRequiredPluginMap](#getRequiredPluginMap())()`
Returns list of map which plugins and version, which are required for project loading.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.persistence.RequiredResourceDescriptor>`
`[getRequiredResources](#getRequiredResources())()`
Returns list of required resources IDs
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getUMLNamespaceURI](#getUMLNamespaceURI())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getVersion](#getVersion())()`

`int`
`[hashCode](#hashCode())()`

`void`
`[setRequiredPluginMap](#setRequiredPluginMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> requiredPlugins)`
Set required plugins information
`void`
`[setRequiredResources](#setRequiredResources(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.persistence.RequiredResourceDescriptor> requiredResources)`
Set required resources
`void`
`[setUMLNamespaceURI](#setUMLNamespaceURI(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) umlNamespaceURI)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString())()`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
XmiExporterDescription
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public XmiExporterDescription([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) version)
Deprecated.
use constructor with FileFormat arguments
Constructor
Parameters:
`name` - exporter name
`version` - exported version
XmiExporterDescription
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public XmiExporterDescription([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) version,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) umlURI)
Deprecated.
use constructor with FileFormat arguments
Constructor
Parameters:
`name` - exported name
`version` - exported version
`umlURI` - uml metamodel uri
XmiExporterDescription
public XmiExporterDescription([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [FormatVersion](FormatVersion.html) formatVersion)
Constructor
Parameters:
`name` - exported name
`formatVersion` - fileFormat version
XmiExporterDescription
public XmiExporterDescription([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [FormatVersion](FormatVersion.html) formatVersion,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) umlURI)
Constructor
Parameters:
`name` - exported name
`formatVersion` - fileFormat version
`umlURI` - uml metamodel uri
 ============ METHOD DETAIL ========== 
Method Details
getName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Returns:
exported name
getVersion
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getVersion()
Returns:
exporter application version. For full version check use #getFileFormat
getRequiredPluginMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getRequiredPluginMap()
Returns list of map which plugins and version, which are required for project loading.
Returns:
map of pluginName->Version, that is required for project loading
setRequiredPluginMap
public void setRequiredPluginMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> requiredPlugins)
Set required plugins information
Parameters:
`requiredPlugins` - required plugins
addRequiredPlugin
public void addRequiredPlugin([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) version)
Adds required plugin into map.
Parameters:
`name` - name of plugin
`version` - required version of plugin.
getRequiredResources
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.persistence.RequiredResourceDescriptor> getRequiredResources()
Returns list of required resources IDs
Returns:
list of required resources IDs.
setRequiredResources
public void setRequiredResources([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<com.nomagic.persistence.RequiredResourceDescriptor> requiredResources)
Set required resources
Parameters:
`requiredResources` - required resources
addRequiredResource
public void addRequiredResource([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suggestedId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
Adds resource as required for project. resource ID, name and value are passed to create resource ID.
Parameters:
`suggestedId` - id of resource.
`name` - name of resource.
`value` - value of resource.
toString
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString()
Overrides:
`[toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
getUMLNamespaceURI
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getUMLNamespaceURI()
Returns:
uml metamodel uri
setUMLNamespaceURI
public void setUMLNamespaceURI([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) umlNamespaceURI)
getFormatVersion
public [FormatVersion](FormatVersion.html) getFormatVersion()
Returns:
file format version.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.persistence</a></div>
<h1 class="title" title="Class XmiExporterDescription">Class XmiExporterDescription</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.persistence.XmiExporterDescription</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">XmiExporterDescription</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">Project version and required resources/plugins information.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../serialized-form.html#com.nomagic.persistence.XmiExporterDescription">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.persistence.FormatVersion)">XmiExporterDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="FormatVersion.html" title="class in com.nomagic.persistence">FormatVersion</a> formatVersion)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.persistence.FormatVersion,java.lang.String)">XmiExporterDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="FormatVersion.html" title="class in com.nomagic.persistence">FormatVersion</a> formatVersion,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlURI)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String)">XmiExporterDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use constructor with FileFormat arguments</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.lang.String)">XmiExporterDescription</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlURI)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use constructor with FileFormat arguments</div>
</div>
</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRequiredPlugin(java.lang.String,java.lang.String)">addRequiredPlugin</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds required plugin into map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRequiredResource(java.lang.String,java.lang.String,java.lang.String)">addRequiredResource</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suggestedId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds resource as required for project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="FormatVersion.html" title="class in com.nomagic.persistence">FormatVersion</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFormatVersion()">getFormatVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredPluginMap()">getRequiredPluginMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of map which plugins and version, which are required for project loading.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;com.nomagic.persistence.RequiredResourceDescriptor&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRequiredResources()">getRequiredResources</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns list of required resources IDs</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUMLNamespaceURI()">getUMLNamespaceURI</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersion()">getVersion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRequiredPluginMap(java.util.Map)">setRequiredPluginMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; requiredPlugins)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set required plugins information</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRequiredResources(java.util.List)">setRequiredResources</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.persistence.RequiredResourceDescriptor&gt; requiredResources)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set required resources</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUMLNamespaceURI(java.lang.String)">setUMLNamespaceURI</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlNamespaceURI)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString()">toString</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String)">
<h3>XmiExporterDescription</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">XmiExporterDescription</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use constructor with FileFormat arguments</div>
</div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - exporter name</dd>
<dd><code>version</code> - exported version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.lang.String)">
<h3>XmiExporterDescription</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">XmiExporterDescription</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlURI)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use constructor with FileFormat arguments</div>
</div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - exported name</dd>
<dd><code>version</code> - exported version</dd>
<dd><code>umlURI</code> - uml metamodel uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.persistence.FormatVersion)">
<h3>XmiExporterDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XmiExporterDescription</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="FormatVersion.html" title="class in com.nomagic.persistence">FormatVersion</a> formatVersion)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - exported name</dd>
<dd><code>formatVersion</code> - fileFormat version</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.persistence.FormatVersion,java.lang.String)">
<h3>XmiExporterDescription</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">XmiExporterDescription</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="FormatVersion.html" title="class in com.nomagic.persistence">FormatVersion</a> formatVersion,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlURI)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - exported name</dd>
<dd><code>formatVersion</code> - fileFormat version</dd>
<dd><code>umlURI</code> - uml metamodel uri</dd>
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
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>exported name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersion()">
<h3>getVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVersion</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>exporter application version. For full version check use #getFileFormat</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredPluginMap()">
<h3>getRequiredPluginMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getRequiredPluginMap</span>()</div>
<div class="block">Returns list of map which plugins and version, which are required for project loading.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of pluginName-&gt;Version, that is required for project loading</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRequiredPluginMap(java.util.Map)">
<h3>setRequiredPluginMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRequiredPluginMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; requiredPlugins)</span></div>
<div class="block">Set required plugins information</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>requiredPlugins</code> - required plugins</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addRequiredPlugin(java.lang.String,java.lang.String)">
<h3>addRequiredPlugin</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addRequiredPlugin</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> version)</span></div>
<div class="block">Adds required plugin into map.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of plugin</dd>
<dd><code>version</code> - required version of plugin.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequiredResources()">
<h3>getRequiredResources</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.persistence.RequiredResourceDescriptor&gt;</span> <span class="element-name">getRequiredResources</span>()</div>
<div class="block">Returns list of required resources IDs</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of required resources IDs.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRequiredResources(java.util.List)">
<h3>setRequiredResources</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRequiredResources</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.persistence.RequiredResourceDescriptor&gt; requiredResources)</span></div>
<div class="block">Set required resources</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>requiredResources</code> - required resources</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addRequiredResource(java.lang.String,java.lang.String,java.lang.String)">
<h3>addRequiredResource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addRequiredResource</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suggestedId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Adds resource as required for project. resource ID, name and value are passed to create resource ID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suggestedId</code> - id of resource.</dd>
<dd><code>name</code> - name of resource.</dd>
<dd><code>value</code> - value of resource.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString()">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUMLNamespaceURI()">
<h3>getUMLNamespaceURI</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUMLNamespaceURI</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>uml metamodel uri</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUMLNamespaceURI(java.lang.String)">
<h3>setUMLNamespaceURI</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUMLNamespaceURI</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> umlNamespaceURI)</span></div>
</section>
</li>
<li>
<section class="detail" id="getFormatVersion()">
<h3>getFormatVersion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="FormatVersion.html" title="class in com.nomagic.persistence">FormatVersion</a></span> <span class="element-name">getFormatVersion</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>file format version.</dd>
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
