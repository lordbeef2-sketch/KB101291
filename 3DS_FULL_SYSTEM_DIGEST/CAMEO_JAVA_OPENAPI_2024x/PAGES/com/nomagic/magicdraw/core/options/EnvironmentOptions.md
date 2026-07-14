# JAVA OPENAPI: EnvironmentOptions (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/core/options/EnvironmentOptions.html
- source_path: `com/nomagic/magicdraw/core/options/EnvironmentOptions.html`
- source_sha256: `87d398af8f741fa4156ffa88d6608c70c57abc91cba7d804d7b86e0d237858a8`
- captured_utc: `2026-07-14T16:51:15.147125+00:00`

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
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addEnvironmentChangeListener](#addEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener))([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)`
Adds environment change listener to environment options.
`void`
`[addGroup](#addGroup(com.nomagic.magicdraw.core.options.OptionsGroup))([OptionsGroup](OptionsGroup.html) group)`
Adds an option group to the environment options.
`[PathVariablesOptionsGroup](PathVariablesOptionsGroup.html)`
`[getPathVariablesOptions](#getPathVariablesOptions())()`
Get path variables options.
`void`
`[removeEnvironmentChangeListener](#removeEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener))([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)`
Removes environment change listener.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
addGroup
@OpenApipublic void addGroup([OptionsGroup](OptionsGroup.html) group)
Adds an option group to the environment options.
Parameters:
`group` - option group to add.
getPathVariablesOptions
@OpenApipublic [PathVariablesOptionsGroup](PathVariablesOptionsGroup.html) getPathVariablesOptions()
Get path variables options.
Returns:
path variables options group.
addEnvironmentChangeListener
@OpenApipublic void addEnvironmentChangeListener([EnvironmentOptions.EnvironmentChangeListener](EnvironmentOptions.EnvironmentChangeListener.html) listener)
Adds environment change listener to environment options.
 Make sure to have a strong reference to the listener in the client code,
 because listeners are managed through weak references to avoid memory leaks.
Parameters:
`listener` - listener to add.
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
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="PathVariablesOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">PathVariablesOptionsGroup</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPathVariablesOptions()">getPathVariablesOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get path variables options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeEnvironmentChangeListener(com.nomagic.magicdraw.core.options.EnvironmentOptions.EnvironmentChangeListener)">removeEnvironmentChangeListener</a><wbr/>(<a href="EnvironmentOptions.EnvironmentChangeListener.html" title="interface in com.nomagic.magicdraw.core.options">EnvironmentOptions.EnvironmentChangeListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes environment change listener.</div>
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
