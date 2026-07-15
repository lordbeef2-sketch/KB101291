# JAVA OPENAPI: DependencyCheckerHelper (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/dependency/DependencyCheckerHelper.html
- source_path: `com/nomagic/magicdraw/dependency/DependencyCheckerHelper.html`
- source_sha256: `e8fc9726b2be277f86b0ca12bccd3d246c76292f47d599b057d1a3c864426396`
- captured_utc: `2026-07-14T16:51:16.479140+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.dependency](package-summary.html)

## Class DependencyCheckerHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.dependency.DependencyCheckerHelper

@OpenApipublic final classDependencyCheckerHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Utility class that allows to check dependencies between modules of a project.

Example:

````java
Project project = Application.getInstance.getProject();
 DependencyCheckResult result = DependencyCheckerHelper.checkDependencies(project);
 if (result.hasDependencies()) {
     System.out.println("Modules of the project has dependencies");
     System.out.println("Cyclic dependencies: " + result.hasCyclicDependencies());
     System.out.println("Number of dependencies between modules/project: " + result.getDependencies().size());
 }
 else {
     System.out.println("Modules of the project has no dependencies");
 }
````

Version:
1.0

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [DependencyCheckResult](DependencyCheckResult.html)`
`[checkDependencies](#checkDependencies(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Checks dependencies between modules and project in the specified project.
`static [DependencyCheckResult](DependencyCheckResult.html)`
`[checkDependencies](#checkDependencies(com.nomagic.magicdraw.core.Project,java.util.Collection))([Project](../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> importantPackages)`
Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages.
`static [DependencyCheckResult](DependencyCheckResult.html)`
`[checkDependencies](#checkDependencies(com.nomagic.magicdraw.core.Project,java.util.Collection,boolean))([Project](../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> importantPackages,
 boolean ignoreSystemProfiles)`
Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
checkDependencies
@OpenApipublic static [DependencyCheckResult](DependencyCheckResult.html) checkDependencies([Project](../core/Project.html) project)
Checks dependencies between modules and project in the specified project. Dependencies of the system profiles
 will not be analyzed.
 
**Note: Project can be active or not active BUT if the project is not active then
 the method will set the specified project as active and after dependencies checking previous
 active project will be set as active.**
Parameters:
`project` - a project.
Returns:
result of dependency checking.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if project is null.
checkDependencies
@OpenApipublic static [DependencyCheckResult](DependencyCheckResult.html) checkDependencies([Project](../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> importantPackages)
Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages. The specified important packages
 must be from the specified project. Dependencies of the system profiles
 will not be analyzed.
 
**Note: Project can be active or not active BUT if the project is not active then
 the method will set the specified project as active and after dependencies checking previous
 active project will be set as active.**
Parameters:
`project` - a project.
`importantPackages` - packages(modules) which dependencies are important. null - means that all packages are
 important.
Returns:
result of dependency checking.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if project is null or if at least one package is not from the specified project.
checkDependencies
@OpenApipublic static [DependencyCheckResult](DependencyCheckResult.html) checkDependencies([Project](../core/Project.html) project,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> importantPackages,
 boolean ignoreSystemProfiles)
Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages. The specified important packages
 must be from the specified project.
 
**Note: Project can be active or not active BUT if the project is not active then
 the method will set the specified project as active and after dependencies checking previous
 active project will be set as active.**
Parameters:
`project` - a project.
`importantPackages` - packages(modules) which dependencies are important. null - means that all packages are
 important.
`ignoreSystemProfiles` - specifies that system profiles must be ignored or not in dependency analysis.
Returns:
result of dependency checking.
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if project is null or if at least one package is not from the specified project.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.dependency</a></div>
<h1 class="title" title="Class DependencyCheckerHelper">Class DependencyCheckerHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.dependency.DependencyCheckerHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">DependencyCheckerHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class that allows to check dependencies between modules of a project.<br/>Example:<br/>
<pre>
 Project project = Application.getInstance.getProject();
 DependencyCheckResult result = DependencyCheckerHelper.checkDependencies(project);
 if (result.hasDependencies()) {
     System.out.println("Modules of the project has dependencies");
     System.out.println("Cyclic dependencies: " + result.hasCyclicDependencies());
     System.out.println("Number of dependencies between modules/project: " + result.getDependencies().size());
 }
 else {
     System.out.println("Modules of the project has no dependencies");
 }
 </pre></div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyCheckResult.html" title="interface in com.nomagic.magicdraw.dependency">DependencyCheckResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkDependencies(com.nomagic.magicdraw.core.Project)">checkDependencies</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks dependencies between modules and project in the specified project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyCheckResult.html" title="interface in com.nomagic.magicdraw.dependency">DependencyCheckResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkDependencies(com.nomagic.magicdraw.core.Project,java.util.Collection)">checkDependencies</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; importantPackages)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="DependencyCheckResult.html" title="interface in com.nomagic.magicdraw.dependency">DependencyCheckResult</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkDependencies(com.nomagic.magicdraw.core.Project,java.util.Collection,boolean)">checkDependencies</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; importantPackages,
 boolean ignoreSystemProfiles)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages.</div>
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
<section class="detail" id="checkDependencies(com.nomagic.magicdraw.core.Project)">
<h3>checkDependencies</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyCheckResult.html" title="interface in com.nomagic.magicdraw.dependency">DependencyCheckResult</a></span> <span class="element-name">checkDependencies</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Checks dependencies between modules and project in the specified project. Dependencies of the system profiles
 will not be analyzed.
 <br/><b>Note: Project can be active or not active BUT if the project is not active then
 the method will set the specified project as active and after dependencies checking previous
 active project will be set as active.</b></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dt>Returns:</dt>
<dd>result of dependency checking.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if project is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkDependencies(com.nomagic.magicdraw.core.Project,java.util.Collection)">
<h3>checkDependencies</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyCheckResult.html" title="interface in com.nomagic.magicdraw.dependency">DependencyCheckResult</a></span> <span class="element-name">checkDependencies</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; importantPackages)</span></div>
<div class="block">Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages. The specified important packages
 must be from the specified project. Dependencies of the system profiles
 will not be analyzed.
 <br/><b>Note: Project can be active or not active BUT if the project is not active then
 the method will set the specified project as active and after dependencies checking previous
 active project will be set as active.</b><br/></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dd><code>importantPackages</code> - packages(modules) which dependencies are important. null - means that all packages are
                          important.</dd>
<dt>Returns:</dt>
<dd>result of dependency checking.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if project is null or if at least one package is not from the specified project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkDependencies(com.nomagic.magicdraw.core.Project,java.util.Collection,boolean)">
<h3>checkDependencies</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="DependencyCheckResult.html" title="interface in com.nomagic.magicdraw.dependency">DependencyCheckResult</a></span> <span class="element-name">checkDependencies</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; importantPackages,
 boolean ignoreSystemProfiles)</span></div>
<div class="block">Checks dependencies between modules and project in the specified project and returns
 dependencies only between specified important packages. The specified important packages
 must be from the specified project.
 <br/><b>Note: Project can be active or not active BUT if the project is not active then
 the method will set the specified project as active and after dependencies checking previous
 active project will be set as active.</b><br/></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - a project.</dd>
<dd><code>importantPackages</code> - packages(modules) which dependencies are important. null - means that all packages are
                             important.</dd>
<dd><code>ignoreSystemProfiles</code> - specifies that system profiles must be ignored or not in dependency analysis.</dd>
<dt>Returns:</dt>
<dd>result of dependency checking.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if project is null or if at least one package is not from the specified project.</dd>
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
