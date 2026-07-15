# JAVA OPENAPI: ProjectEventListenerAdapter2 (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/core/project/ProjectEventListenerAdapter2.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectEventListenerAdapter2.html`
- source_sha256: `78d5ba96aafd186b60f92526140cc2132e8c37549041c27e5492304eb0a7e823`
- captured_utc: `2026-07-14T16:51:15.726131+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Class ProjectEventListenerAdapter2

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter](ProjectEventListenerAdapter.html)
com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter2

All Implemented Interfaces:
`[ProjectEventListener](ProjectEventListener.html)`, `com.nomagic.magicdraw.core.project.ProjectEventListener2`

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@OpenApiAllpublic classProjectEventListenerAdapter2
extends [ProjectEventListenerAdapter](ProjectEventListenerAdapter.html)
implements com.nomagic.magicdraw.core.project.ProjectEventListener2

Deprecated.
all methods are implemented in super class [`ProjectEventListenerAdapter`](ProjectEventListenerAdapter.html), use [`ProjectEventListenerAdapter`](ProjectEventListenerAdapter.html)

Empty implementation of ProjectEventListener2 interface

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectEventListenerAdapter2](#%3Cinit%3E())()`
Deprecated.
 ========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from class com.nomagic.magicdraw.core.project.[ProjectEventListenerAdapter](ProjectEventListenerAdapter.html)
`[projectActivated](ProjectEventListenerAdapter.html#projectActivated(com.nomagic.magicdraw.core.Project)), [projectActivatedFromGUI](ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectDeActivated](ProjectEventListenerAdapter.html#projectDeActivated(com.nomagic.magicdraw.core.Project)), [projectOpened](ProjectEventListenerAdapter.html#projectOpened(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosed](ProjectEventListenerAdapter.html#projectPreClosed(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreSaved](ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectEventListener](ProjectEventListener.html)
`[projectActivated](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)), [projectActivatedFromGUI](ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectDeActivated](ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)), [projectOpened](ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosed](ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreOpenedFromGUI](ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreSaved](ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectUsedFromGUI](ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectEventListenerAdapter2
public ProjectEventListenerAdapter2()
Deprecated.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Class ProjectEventListenerAdapter2">Class ProjectEventListenerAdapter2</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter</a>
<div class="inheritance">com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter2</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code>, <code>com.nomagic.magicdraw.core.project.ProjectEventListener2</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectEventListenerAdapter2</span>
<span class="extends-implements">extends <a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a>
implements com.nomagic.magicdraw.core.project.ProjectEventListener2</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">all methods are implemented in super class <a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project"><code>ProjectEventListenerAdapter</code></a>, use <a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project"><code>ProjectEventListenerAdapter</code></a></div>
</div>
<div class="block">Empty implementation of ProjectEventListener2 interface</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectEventListenerAdapter2</a>()</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter">Methods inherited from class com.nomagic.magicdraw.core.project.<a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></h3>
<code><a href="ProjectEventListenerAdapter.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a>, <a href="ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a>, <a href="ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a>, <a href="ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a>, <a href="ProjectEventListenerAdapter.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a>, <a href="ProjectEventListenerAdapter.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a>, <a href="ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a>, <a href="ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a>, <a href="ProjectEventListenerAdapter.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a>, <a href="ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a>, <a href="ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a>, <a href="ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a>, <a href="ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a>, <a href="ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListener">Methods inherited from interface com.nomagic.magicdraw.core.project.<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></h3>
<code><a href="ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a>, <a href="ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a>, <a href="ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a>, <a href="ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a>, <a href="ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a>, <a href="ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a>, <a href="ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a>, <a href="ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a>, <a href="ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a>, <a href="ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a>, <a href="ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a>, <a href="ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectPreOpenedFromGUI</a>, <a href="ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a>, <a href="ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a>, <a href="ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a>, <a href="ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">projectUsedFromGUI</a></code></div>
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
<h3>ProjectEventListenerAdapter2</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectEventListenerAdapter2</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
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
