# JAVA OPENAPI: ResourceDependentPlugin (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/plugins/ResourceDependentPlugin.html
- source_path: `com/nomagic/magicdraw/plugins/ResourceDependentPlugin.html`
- source_sha256: `10e814e1ced90a6c269728c51c67855654269cb03d60ddc0752d6bf3aaf70e48`
- captured_utc: `2026-07-14T16:51:26.092267+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.plugins](package-summary.html)

## Interface ResourceDependentPlugin

@OpenApiAllpublic interfaceResourceDependentPlugin
This interface is for plugins, which have profile dependencies in project. The method #isRequiredPlugin is invoked on
 every project save. If plugin is required for project, it should return True. In XMI plugin name and version is saved
 to provide info which plugin version is required for project on load.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPluginName](#getPluginName())()`
Returns name of plugin
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPluginVersion](#getPluginVersion())()`
Returns version of plugin
`default boolean`
`[isPluginRequired](#isPluginRequired(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Given a project, returns true if this project requires this plugin.
`boolean`
`[isPluginRequired](#isPluginRequired(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Given a project, returns true if this project requires this plugin.

============ METHOD DETAIL ========== 
Method Details
isPluginRequired
boolean isPluginRequired([Project](../core/Project.html) project)
Given a project, returns true if this project requires this plugin.
Parameters:
`project` - to be evaluated.
Returns:
true if given project requires plugin.
isPluginRequired
default boolean isPluginRequired(com.nomagic.ci.persistence.IProject project)
Given a project, returns true if this project requires this plugin.
Parameters:
`project` - to be evaluated.
Returns:
true if given project requires plugin.
getPluginName
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPluginName()
Returns name of plugin
Returns:
name of plugin.
getPluginVersion
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPluginVersion()
Returns version of plugin
Returns:
plugin version.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.plugins</a></div>
<h1 class="title" title="Interface ResourceDependentPlugin">Interface ResourceDependentPlugin</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ResourceDependentPlugin</span></div>
<div class="block">This interface is for plugins, which have profile dependencies in project. The method #isRequiredPlugin is invoked on
 every project save. If plugin is required for project, it should return True. In XMI plugin name and version is saved
 to provide info which plugin version is required for project on load.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPluginName()">getPluginName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns name of plugin</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPluginVersion()">getPluginVersion</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns version of plugin</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#isPluginRequired(com.nomagic.ci.persistence.IProject)">isPluginRequired</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Given a project, returns true if this project requires this plugin.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isPluginRequired(com.nomagic.magicdraw.core.Project)">isPluginRequired</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Given a project, returns true if this project requires this plugin.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="isPluginRequired(com.nomagic.magicdraw.core.Project)">
<h3>isPluginRequired</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isPluginRequired</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Given a project, returns true if this project requires this plugin.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - to be evaluated.</dd>
<dt>Returns:</dt>
<dd>true if given project requires plugin.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPluginRequired(com.nomagic.ci.persistence.IProject)">
<h3>isPluginRequired</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">boolean</span> <span class="element-name">isPluginRequired</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Given a project, returns true if this project requires this plugin.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - to be evaluated.</dd>
<dt>Returns:</dt>
<dd>true if given project requires plugin.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPluginName()">
<h3>getPluginName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPluginName</span>()</div>
<div class="block">Returns name of plugin</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of plugin.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPluginVersion()">
<h3>getPluginVersion</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPluginVersion</span>()</div>
<div class="block">Returns version of plugin</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>plugin version.</dd>
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
