# JAVA OPENAPI: JavaCodeEngineeringManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/ce/JavaCodeEngineeringManager.html
- source_path: `com/nomagic/magicdraw/ce/JavaCodeEngineeringManager.html`
- source_sha256: `afef2077e68fe063d5b339bceb4e557878e96aaf5fc547f48b104ec70dd8ebc0`
- captured_utc: `2026-07-14T16:55:10.813958+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ce](package-summary.html)

## Class JavaCodeEngineeringManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.ce.JavaCodeEngineeringManager

@OpenApiAllpublic classJavaCodeEngineeringManager
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Dedicated to JAVA code engineering sets. Provides specific options setters for Java language.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[JavaCodeEngineeringManager](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[getJavaClasspath](#getJavaClasspath(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Given a project, returns applied array of classpaths.
`static void`
`[setJavaClasspath](#setJavaClasspath(com.nomagic.magicdraw.core.Project,java.lang.String%5B%5D))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] classpaths)`
Applies given array of classpaths to java language options in provided project.
`static void`
`[setResolveCollectionGenerics](#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean resolve)`
Deprecated.
Use [`CodeEngineeringManager.setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project, boolean)`](CodeEngineeringManager.html#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean))
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
JavaCodeEngineeringManager
public JavaCodeEngineeringManager()
 ============ METHOD DETAIL ========== 
Method Details
setJavaClasspath
@OpenApipublic static void setJavaClasspath([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] classpaths)
Applies given array of classpaths to java language options in provided project.
Parameters:
`project` - MagicDraw project, which has java code engineering sets.
`classpaths` - array of classpaths.
getJavaClasspath
@OpenApipublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] getJavaClasspath([Project](../core/Project.html) project)
Given a project, returns applied array of classpaths.
Parameters:
`project` - MagicDraw project that has applied java classpaths.
Returns:
Array of classpath, which was applied for project.
setResolveCollectionGenerics
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void setResolveCollectionGenerics([Project](../core/Project.html) project,
 boolean resolve)
Deprecated.
Use [`CodeEngineeringManager.setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project, boolean)`](CodeEngineeringManager.html#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean))
Reverse engineering option, to enable resolve collection generic. Applies for all project's
 code engineering sets.
Parameters:
`project` - MD project.
`resolve` - True, to resolve, false to not resolve.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ce</a></div>
<h1 class="title" title="Class JavaCodeEngineeringManager">Class JavaCodeEngineeringManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.ce.JavaCodeEngineeringManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">JavaCodeEngineeringManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Dedicated to JAVA code engineering sets. Provides specific options setters for Java language.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">JavaCodeEngineeringManager</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getJavaClasspath(com.nomagic.magicdraw.core.Project)">getJavaClasspath</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a project, returns applied array of classpaths.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setJavaClasspath(com.nomagic.magicdraw.core.Project,java.lang.String%5B%5D)">setJavaClasspath</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] classpaths)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Applies given array of classpaths to java language options in provided project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean)">setResolveCollectionGenerics</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean resolve)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CodeEngineeringManager.html#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean)"><code>CodeEngineeringManager.setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project, boolean)</code></a></div>
</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>JavaCodeEngineeringManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">JavaCodeEngineeringManager</span>()</div>
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
<section class="detail" id="setJavaClasspath(com.nomagic.magicdraw.core.Project,java.lang.String[])">
<h3>setJavaClasspath</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setJavaClasspath</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] classpaths)</span></div>
<div class="block">Applies given array of classpaths to java language options in provided project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MagicDraw project, which has java code engineering sets.</dd>
<dd><code>classpaths</code> - array of classpaths.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJavaClasspath(com.nomagic.magicdraw.core.Project)">
<h3>getJavaClasspath</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">getJavaClasspath</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Given a project, returns applied array of classpaths.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MagicDraw project that has applied java classpaths.</dd>
<dt>Returns:</dt>
<dd>Array of classpath, which was applied for project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean)">
<h3>setResolveCollectionGenerics</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setResolveCollectionGenerics</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean resolve)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CodeEngineeringManager.html#setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project,boolean)"><code>CodeEngineeringManager.setResolveCollectionGenerics(com.nomagic.magicdraw.core.Project, boolean)</code></a></div>
</div>
<div class="block">Reverse engineering option, to enable resolve collection generic. Applies for all project's
 code engineering sets.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - MD project.</dd>
<dd><code>resolve</code> - True, to resolve, false to not resolve.</dd>
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
