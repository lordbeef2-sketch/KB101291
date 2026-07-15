# JAVA OPENAPI: ProjectOptionsConfigurator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/options/ProjectOptionsConfigurator.html
- source_path: `com/nomagic/magicdraw/core/options/ProjectOptionsConfigurator.html`
- source_sha256: `5fddae8168ccedf8834c93d061aad3f5dccacda6502b8a4fc820e933afe4e1e7`
- captured_utc: `2026-07-14T16:51:15.923134+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.options](package-summary.html)

## Interface ProjectOptionsConfigurator

@OpenApiAllpublic interfaceProjectOptionsConfigurator
Project options configurator. Configurators are registered by [`ProjectOptions.addConfigurator(ProjectOptionsConfigurator)`](ProjectOptions.html#addConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator)).

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`default void`
`[afterLoad](#afterLoad(com.nomagic.magicdraw.core.options.ProjectOptions))([ProjectOptions](ProjectOptions.html) options)`
Configure given project options after project load.
`void`
`[configure](#configure(com.nomagic.magicdraw.core.options.ProjectOptions))([ProjectOptions](ProjectOptions.html) options)`
Configure the default values for given options.
`default void`
`[configureLoadedOptions](#configureLoadedOptions(com.nomagic.magicdraw.core.options.ProjectOptions))([ProjectOptions](ProjectOptions.html) options)`
Configure the real values for given options.

============ METHOD DETAIL ========== 
Method Details
configure
void configure([ProjectOptions](ProjectOptions.html) options)
Configure the default values for given options.
Parameters:
`options` - to configure.
afterLoad
default void afterLoad([ProjectOptions](ProjectOptions.html) options)
Configure given project options after project load.
Parameters:
`options` - options to configure.
configureLoadedOptions
default void configureLoadedOptions([ProjectOptions](ProjectOptions.html) options)
Configure the real values for given options.
Parameters:
`options` - options to configure.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.options</a></div>
<h1 class="title" title="Interface ProjectOptionsConfigurator">Interface ProjectOptionsConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectOptionsConfigurator</span></div>
<div class="block">Project options configurator. Configurators are registered by <a href="ProjectOptions.html#addConfigurator(com.nomagic.magicdraw.core.options.ProjectOptionsConfigurator)"><code>ProjectOptions.addConfigurator(ProjectOptionsConfigurator)</code></a>.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#afterLoad(com.nomagic.magicdraw.core.options.ProjectOptions)">afterLoad</a><wbr/>(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Configure given project options after project load.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configure(com.nomagic.magicdraw.core.options.ProjectOptions)">configure</a><wbr/>(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Configure the default values for given options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#configureLoadedOptions(com.nomagic.magicdraw.core.options.ProjectOptions)">configureLoadedOptions</a><wbr/>(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Configure the real values for given options.</div>
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
<section class="detail" id="configure(com.nomagic.magicdraw.core.options.ProjectOptions)">
<h3>configure</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</span></div>
<div class="block">Configure the default values for given options.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - to configure.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="afterLoad(com.nomagic.magicdraw.core.options.ProjectOptions)">
<h3>afterLoad</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">afterLoad</span><wbr/><span class="parameters">(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</span></div>
<div class="block">Configure given project options after project load.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - options to configure.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureLoadedOptions(com.nomagic.magicdraw.core.options.ProjectOptions)">
<h3>configureLoadedOptions</h3>
<div class="member-signature"><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">configureLoadedOptions</span><wbr/><span class="parameters">(<a href="ProjectOptions.html" title="class in com.nomagic.magicdraw.core.options">ProjectOptions</a> options)</span></div>
<div class="block">Configure the real values for given options.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - options to configure.</dd>
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
