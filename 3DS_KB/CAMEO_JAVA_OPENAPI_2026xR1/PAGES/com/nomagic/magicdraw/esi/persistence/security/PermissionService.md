# JAVA OPENAPI: PermissionService (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/esi/persistence/security/PermissionService.html
- source_path: `com/nomagic/magicdraw/esi/persistence/security/PermissionService.html`
- source_sha256: `04266858837d9304c5522e989c9f912591b9da213f1fd2d7ac89aa81d46b8ee1`
- captured_utc: `2026-07-14T16:45:36.016482+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi.persistence.security](package-summary.html)

## Interface PermissionService

All Superinterfaces:
`com.nomagic.ci.persistence.services.IProjectService`

@OpenApiAllpublic interfacePermissionServiceextends com.nomagic.ci.persistence.services.IProjectService

An interface for manipulation of package level permissions. This allows clients
 to query existing permissions, modify or add new permissions accordingly.
 In order to start manipulating or reading permissions, one must obtain an implementation
 of [`service`](PermissionService.html) first. This can be achieved by calling
 `Serviceable.getService(Class)` method on an
 instance of `IPrimaryProject`:

 `IPrimaryProject project = Application.getInstance().getProjectsManager()
 .getActiveProject().getPrimaryProject();
 PermissionService service = project.getService(PermissionService.class);`
To modify [`permissions`](../../../security/PackagePermissions.html) client should use setters that are exposed
 in [`PackageAccessPermission`](../../../security/PackageAccessPermission.html). Code
 below iterates over all [`permissions`](../../../security/PackageAccessPermission.html)
 of an arbitrary [`package`](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) and sets access mode of each permission to
 [`read-write`](../../../security/Action.html#READ_WRITE):

 `Package pack = ... // some arbitrary package
 PackagePermissions permissions = service.getPermissions(pack);

 for (PackageAccessPermission p : permissions.getAccessPermissions())
 {
 p.setAction(Action.READ_WRITE);
 }`
[`SecurityFactory`](../../../security/SecurityFactory.html) can be used to create new
 [`package permissions`](../../../security/PackageAccessPermission.html). Just created [`package permission`](../../../security/PackageAccessPermission.html)
 should be added to a package [`permissions list`](../../../security/PackagePermissions.html#getAccessPermissions()):

 `PackageAccessPermission newPermission = SecurityFactory.eINSTANCE.createPackageAccessPermission();

 newPermission.setAction(Action.READ_WRITE);
 newPermission.setApplication(com.nomagic.magicdraw.security.Application.PACKAGE_AND_SUBPACKAGES);
 newPermission.setPrincipal(SecurityFactory.eINSTANCE.createEveryonePrincipal());

 service.getPermissions(pack).getAccessPermissions().add(newPermission);`

Version:
1.0
See Also:
[`SecurityFactory`](../../../security/SecurityFactory.html)
[`PackageAccessPermission`](../../../security/PackageAccessPermission.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`int`
`[getChangeNumber](#getChangeNumber())()`
Returns number how many times permissions were locally changed.
`[PackagePermissions](../../../security/PackagePermissions.html)`
`[getPermissions](#getPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) aPackage)`
Returns current permissions of the specified package.
`<T extends [Principal](../../../security/Principal.html)> 
T`
`[getPrincipal](#getPrincipal(java.lang.String,java.lang.Class))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)`
Returns a principal of the specified name and type.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[PackagePermissions](../../../security/PackagePermissions.html)>`
`[getProjectPermissions](#getProjectPermissions())()`
Method returns all permissions from the currently active project.
`boolean`
`[hasPermissions](#hasPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package))([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) aPackage)`
Returns whether the specified package has permissions set.
`void`
`[setChanged](#setChanged())()`
Sets that package permissions has changed
`void`
`[setPermissions](#setPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.security.PackagePermissions))([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) aPackage,
 [PackagePermissions](../../../security/PackagePermissions.html) permissions)`
Sets permissions for the specified package.
Methods inherited from interface com.nomagic.ci.persistence.services.IProjectService
`getProject`

============ METHOD DETAIL ========== 
Method Details
getPermissions
[PackagePermissions](../../../security/PackagePermissions.html) getPermissions([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) aPackage)
 throws [PermissionException](PermissionException.html)
Returns current permissions of the specified package. The returned object
 is persistent and any modification will persisted on the project resource commit.
Parameters:
`aPackage` - a package.
Returns:
list of permissions.
Throws:
`[PermissionException](PermissionException.html)`
hasPermissions
boolean hasPermissions([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) aPackage)
 throws [PermissionException](PermissionException.html)
Returns whether the specified package has permissions set.
Parameters:
`aPackage` - a package.
Returns:
true if the package has permissions.
Throws:
`[PermissionException](PermissionException.html)`
setPermissions
void setPermissions([Package](../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html) aPackage,
 @CheckForNull
 [PackagePermissions](../../../security/PackagePermissions.html) permissions)
 throws [PermissionException](PermissionException.html)
Sets permissions for the specified package. After the completion the specified permissions become
 persistent and any modification of the permissions will be saved on the project resource commit.
Parameters:
`aPackage` - a package.
`permissions` - a package permissions.
Throws:
`[PermissionException](PermissionException.html)` - identifies that the method invocation failed. The message or the cause can be
 checked to find the reason of the problem.
getPrincipal
<T extends [Principal](../../../security/Principal.html)> T getPrincipal([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<T> type)
 throws [PermissionException](PermissionException.html)
Returns a principal of the specified name and type.
Type Parameters:
`T` - any object that extends [`Principal`](../../../security/Principal.html) class.
Parameters:
`name` - name of the principal.
`type` - type of the principal.
Returns:
a principal.
Throws:
`[PermissionException](PermissionException.html)` - identifies that the method invocation failed. The message or the cause can be
 checked to find the reason of the problem.
getProjectPermissions
[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[PackagePermissions](../../../security/PackagePermissions.html)> getProjectPermissions()
 throws [PermissionException](PermissionException.html)
Method returns all permissions from the currently active project.
Returns:
map of current project permissions
Throws:
`[PermissionException](PermissionException.html)` - identifies that method invocation failed. The message or the cause can be
 checked to find the reason of the problem.
getChangeNumber
int getChangeNumber()
 throws [PermissionException](PermissionException.html)
Returns number how many times permissions were locally changed.
Returns:
number how many times permissions were locally changed
Throws:
`[PermissionException](PermissionException.html)` - identifies that method invocation failed. The message or the cause can be
 checked to find the reason of the problem.
setChanged
void setChanged()
 throws [PermissionException](PermissionException.html)
Sets that package permissions has changed
Throws:
`[PermissionException](PermissionException.html)` - identifies that method invocation failed. The message or the cause can be
 checked to find the reason of the problem.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi.persistence.security</a></div>
<h1 class="title" title="Interface PermissionService">Interface PermissionService</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code>com.nomagic.ci.persistence.services.IProjectService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PermissionService</span><span class="extends-implements">
extends com.nomagic.ci.persistence.services.IProjectService</span></div>
<div class="block"><p>An interface for manipulation of package level permissions. This allows clients
 to query existing permissions, modify or add new permissions accordingly.
 <p>In order to start manipulating or reading permissions, one must obtain an implementation
 of <a href="PermissionService.html" title="interface in com.nomagic.magicdraw.esi.persistence.security"><code>service</code></a> first. This can be achieved by calling
 <code>Serviceable.getService(Class)</code> method on an
 instance of <code>IPrimaryProject</code>:

 <pre><code>
 IPrimaryProject project = Application.getInstance().getProjectsManager()
     .getActiveProject().getPrimaryProject();
 PermissionService service = project.getService(PermissionService.class);
 </code></pre>
<p>To modify <a href="../../../security/PackagePermissions.html" title="interface in com.nomagic.magicdraw.security"><code>permissions</code></a> client should use setters that are exposed
 in <a href="../../../security/PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>PackageAccessPermission</code></a>. Code
 below iterates over all <a href="../../../security/PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>permissions</code></a>
 of an arbitrary <a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>package</code></a> and sets access mode of each permission to
 <a href="../../../security/Action.html#READ_WRITE"><code>read-write</code></a>:

 <pre><code>
 Package pack = ... // some arbitrary package
 PackagePermissions permissions = service.getPermissions(pack);

 for (PackageAccessPermission p : permissions.getAccessPermissions())
 {
     p.setAction(Action.READ_WRITE);
 }
 </code></pre>
<a href="../../../security/SecurityFactory.html" title="interface in com.nomagic.magicdraw.security"><code>SecurityFactory</code></a> can be used to create new
 <a href="../../../security/PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>package permissions</code></a>. Just created <a href="../../../security/PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>package permission</code></a>
 should be added to a package <a href="../../../security/PackagePermissions.html#getAccessPermissions()"><code>permissions list</code></a>:

 <pre><code>
 PackageAccessPermission newPermission = SecurityFactory.eINSTANCE.createPackageAccessPermission();

 newPermission.setAction(Action.READ_WRITE);
 newPermission.setApplication(com.nomagic.magicdraw.security.Application.PACKAGE_AND_SUBPACKAGES);
 newPermission.setPrincipal(SecurityFactory.eINSTANCE.createEveryonePrincipal());

 service.getPermissions(pack).getAccessPermissions().add(newPermission);
 </code></pre></p></p></p></div>
<dl class="notes">
<dt>Version:</dt>
<dd>1.0</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../security/SecurityFactory.html" title="interface in com.nomagic.magicdraw.security"><code>SecurityFactory</code></a></li>
<li><a href="../../../security/PackageAccessPermission.html" title="interface in com.nomagic.magicdraw.security"><code>PackageAccessPermission</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getChangeNumber()">getChangeNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns number how many times permissions were locally changed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../security/PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">getPermissions</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> aPackage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns current permissions of the specified package.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>&lt;T extends <a href="../../../security/Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPrincipal(java.lang.String,java.lang.Class)">getPrincipal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a principal of the specified name and type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="../../../security/PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getProjectPermissions()">getProjectPermissions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method returns all permissions from the currently active project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hasPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">hasPermissions</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> aPackage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns whether the specified package has permissions set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setChanged()">setChanged</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets that package permissions has changed</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.security.PackagePermissions)">setPermissions</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> aPackage,
 <a href="../../../security/PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a> permissions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets permissions for the specified package.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.ci.persistence.services.IProjectService">Methods inherited from interface com.nomagic.ci.persistence.services.IProjectService</h3>
<code>getProject</code></div>
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
<section class="detail" id="getPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>getPermissions</h3>
<div class="member-signature"><span class="return-type"><a href="../../../security/PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a></span> <span class="element-name">getPermissions</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> aPackage)</span>
                           throws <span class="exceptions"><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></span></div>
<div class="block">Returns current permissions of the specified package. The returned object
 is persistent and any modification will persisted on the project resource commit.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aPackage</code> - a package.</dd>
<dt>Returns:</dt>
<dd>list of permissions.</dd>
<dt>Throws:</dt>
<dd><code><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package)">
<h3>hasPermissions</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">hasPermissions</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> aPackage)</span>
                throws <span class="exceptions"><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></span></div>
<div class="block">Returns whether the specified package has permissions set.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aPackage</code> - a package.</dd>
<dt>Returns:</dt>
<dd>true if the package has permissions.</dd>
<dt>Throws:</dt>
<dd><code><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPermissions(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.magicdraw.security.PackagePermissions)">
<h3>setPermissions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPermissions</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> aPackage,
 @CheckForNull
 <a href="../../../security/PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a> permissions)</span>
             throws <span class="exceptions"><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></span></div>
<div class="block">Sets permissions for the specified package. After the completion the specified permissions become
 persistent and any modification of the permissions will be saved on the project resource commit.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aPackage</code> - a package.</dd>
<dd><code>permissions</code> - a package permissions.</dd>
<dt>Throws:</dt>
<dd><code><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></code> - identifies that the method invocation failed. The message or the cause can be
                             checked to find the reason of the problem.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrincipal(java.lang.String,java.lang.Class)">
<h3>getPrincipal</h3>
<div class="member-signature"><span class="type-parameters">&lt;T extends <a href="../../../security/Principal.html" title="interface in com.nomagic.magicdraw.security">Principal</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">getPrincipal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;T&gt; type)</span>
                              throws <span class="exceptions"><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></span></div>
<div class="block">Returns a principal of the specified name and type.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - any object that extends <a href="../../../security/Principal.html" title="interface in com.nomagic.magicdraw.security"><code>Principal</code></a> class.</dd>
<dt>Parameters:</dt>
<dd><code>name</code> - name of the principal.</dd>
<dd><code>type</code> - type of the principal.</dd>
<dt>Returns:</dt>
<dd>a principal.</dd>
<dt>Throws:</dt>
<dd><code><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></code> - identifies that the method invocation failed. The message or the cause can be
                             checked to find the reason of the problem.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProjectPermissions()">
<h3>getProjectPermissions</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="../../../security/PackagePermissions.html" title="interface in com.nomagic.magicdraw.security">PackagePermissions</a>&gt;</span> <span class="element-name">getProjectPermissions</span>()
                                              throws <span class="exceptions"><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></span></div>
<div class="block">Method returns all permissions from the currently active project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of current project permissions</dd>
<dt>Throws:</dt>
<dd><code><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></code> - identifies that method invocation failed. The message or the cause can be
                                                                checked to find the reason of the problem.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangeNumber()">
<h3>getChangeNumber</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getChangeNumber</span>()
             throws <span class="exceptions"><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></span></div>
<div class="block">Returns number how many times permissions were locally changed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>number how many times permissions were locally changed</dd>
<dt>Throws:</dt>
<dd><code><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></code> - identifies that method invocation failed. The message or the cause can be
                                                                checked to find the reason of the problem.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChanged()">
<h3>setChanged</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setChanged</span>()
         throws <span class="exceptions"><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></span></div>
<div class="block">Sets that package permissions has changed</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="PermissionException.html" title="class in com.nomagic.magicdraw.esi.persistence.security">PermissionException</a></code> - identifies that method invocation failed. The message or the cause can be
                                                                checked to find the reason of the problem.</dd>
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
