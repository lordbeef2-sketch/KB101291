# JAVA OPENAPI: SpecificationDialogManager (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/dialogs/specifications/SpecificationDialogManager.html
- source_path: `com/nomagic/magicdraw/ui/dialogs/specifications/SpecificationDialogManager.html`
- source_sha256: `31539ffb642a851bd140c997886351dea3756202e3b97753150b783387424d38`
- captured_utc: `2026-07-14T16:58:25.582152+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.dialogs.specifications](package-summary.html)

## Class SpecificationDialogManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)
com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager

All Implemented Interfaces:
`[ProjectEventListener](../../../core/project/ProjectEventListener.html)`

@OpenApipublic final classSpecificationDialogManager
extends [ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)

The manager of specification windows for all types of model elements.
 This manager knows exactly what specification dialog to open for every specific element.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addConfigurator](#addConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)`
Adds specification node configurator for given Element type
`void`
`[editSpecification](#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord))([SpecificationRecord](SpecificationRecord.html) record)`
Opens non-modal specification dialog activated pane specified by record.
`void`
`[editSpecification](#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord,boolean))([SpecificationRecord](SpecificationRecord.html) record,
 boolean modal)`
Opens specification dialog and activated pane specified by record.
`void`
`[editSpecification](#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Opens specification dialog for given ModelElement.
`void`
`[editSpecification](#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean modal)`
Opens specification dialog for given ModelElement.
`static [SpecificationDialogManager](SpecificationDialogManager.html)`
`[getManager](#getManager())()`
Returns shared instance of this manager.
`[SpecificationTitleCreator](SpecificationTitleCreator.html)`
`[getTitleCreator](#getTitleCreator())()`
Returns current specification dialog title creator.
`void`
`[removeConfigurator](#removeConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)`
Removes specification dialog node configurator for given Element type.
`void`
`[setTitleCreator](#setTitleCreator(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationTitleCreator))([SpecificationTitleCreator](SpecificationTitleCreator.html) titleCreator)`
Sets specification dialog title creator
Methods inherited from class com.nomagic.magicdraw.core.project.[ProjectEventListenerAdapter](../../../core/project/ProjectEventListenerAdapter.html)
`[projectActivatedFromGUI](../../../core/project/ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](../../../core/project/ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](../../../core/project/ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](../../../core/project/ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](../../../core/project/ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](../../../core/project/ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](../../../core/project/ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreSaved](../../../core/project/ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](../../../core/project/ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](../../../core/project/ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectEventListener](../../../core/project/ProjectEventListener.html)
`[projectPreOpenedFromGUI](../../../core/project/ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectUsedFromGUI](../../../core/project/ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))`

============ METHOD DETAIL ========== 
Method Details
getManager
@OpenApipublic static [SpecificationDialogManager](SpecificationDialogManager.html) getManager()
Returns shared instance of this manager.
Returns:
instance of this manager.
editSpecification
@OpenApipublic void editSpecification([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Opens specification dialog for given ModelElement. Dialog is not modal.
Parameters:
`element` - the given Element.
editSpecification
@OpenApipublic void editSpecification([Element](../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 boolean modal)
Opens specification dialog for given ModelElement.
Parameters:
`element` - the given Element.
`modal` - open modal specification window
editSpecification
@OpenApipublic void editSpecification([SpecificationRecord](SpecificationRecord.html) record)
Opens non-modal specification dialog activated pane specified by record.
Parameters:
`record` - specification dialog record containing a reference to element and pane to activate
editSpecification
@OpenApipublic void editSpecification([SpecificationRecord](SpecificationRecord.html) record,
 boolean modal)
Opens specification dialog and activated pane specified by record.
Parameters:
`record` - specification dialog record containing a reference to element and pane to activate
`modal` - open modal specification window
addConfigurator
@OpenApipublic void addConfigurator([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)
Adds specification node configurator for given Element type
Parameters:
`elementClass` - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)
`configurator` - the given configurator.
removeConfigurator
@OpenApipublic void removeConfigurator([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> elementClass,
 [ISpecificationNodeConfigurator](configurator/ISpecificationNodeConfigurator.html) configurator)
Removes specification dialog node configurator for given Element type.
Parameters:
`elementClass` - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)
`configurator` - the given configurator.
getTitleCreator
@OpenApipublic [SpecificationTitleCreator](SpecificationTitleCreator.html) getTitleCreator()
Returns current specification dialog title creator.
Returns:
title creator
setTitleCreator
@OpenApipublic void setTitleCreator([SpecificationTitleCreator](SpecificationTitleCreator.html) titleCreator)
Sets specification dialog title creator
Parameters:
`titleCreator` - title creator.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.dialogs.specifications</a></div>
<h1 class="title" title="Class SpecificationDialogManager">Class SpecificationDialogManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter</a>
<div class="inheritance">com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationDialogManager</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">SpecificationDialogManager</span>
<span class="extends-implements">extends <a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></span></div>
<div class="block">The manager of specification windows for all types of model elements.
 This manager knows exactly what specification dialog to open for every specific element.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">addConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds specification node configurator for given Element type</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord)">editSpecification</a><wbr/>(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens non-modal specification dialog activated pane specified by record.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord,boolean)">editSpecification</a><wbr/>(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record,
 boolean modal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens specification dialog and activated pane specified by record.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">editSpecification</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens specification dialog for given ModelElement.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">editSpecification</a><wbr/>(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean modal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Opens specification dialog for given ModelElement.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SpecificationDialogManager.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationDialogManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getManager()">getManager</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns shared instance of this manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTitleCreator()">getTitleCreator</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns current specification dialog title creator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">removeConfigurator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes specification dialog node configurator for given Element type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTitleCreator(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationTitleCreator)">setTitleCreator</a><wbr/>(<a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a> titleCreator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets specification dialog title creator</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter">Methods inherited from class com.nomagic.magicdraw.core.project.<a href="../../../core/project/ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></h3>
<code><a href="../../../core/project/ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a>, <a href="../../../core/project/ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListener">Methods inherited from interface com.nomagic.magicdraw.core.project.<a href="../../../core/project/ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></h3>
<code><a href="../../../core/project/ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectPreOpenedFromGUI</a>, <a href="../../../core/project/ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">projectUsedFromGUI</a></code></div>
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
<section class="detail" id="getManager()">
<h3>getManager</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public static</span> <span class="return-type"><a href="SpecificationDialogManager.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationDialogManager</a></span> <span class="element-name">getManager</span>()</div>
<div class="block">Returns shared instance of this manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of this manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Opens specification dialog for given ModelElement. Dialog is not modal.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given Element.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="../../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 boolean modal)</span></div>
<div class="block">Opens specification dialog for given ModelElement.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given Element.</dd>
<dd><code>modal</code> - open modal specification window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record)</span></div>
<div class="block">Opens non-modal specification dialog activated pane specified by record.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>record</code> - specification dialog record containing a reference to element and pane to activate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="editSpecification(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationRecord,boolean)">
<h3>editSpecification</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">editSpecification</span><wbr/><span class="parameters">(<a href="SpecificationRecord.html" title="class in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationRecord</a> record,
 boolean modal)</span></div>
<div class="block">Opens specification dialog and activated pane specified by record.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>record</code> - specification dialog record containing a reference to element and pane to activate</dd>
<dd><code>modal</code> - open modal specification window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">
<h3>addConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</span></div>
<div class="block">Adds specification node configurator for given Element type</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementClass</code> - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)</dd>
<dd><code>configurator</code> - the given configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeConfigurator(java.lang.Class,com.nomagic.magicdraw.ui.dialogs.specifications.configurator.ISpecificationNodeConfigurator)">
<h3>removeConfigurator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeConfigurator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; elementClass,
 <a href="configurator/ISpecificationNodeConfigurator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications.configurator">ISpecificationNodeConfigurator</a> configurator)</span></div>
<div class="block">Removes specification dialog node configurator for given Element type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elementClass</code> - the specific class of Element(for example com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Classifier)</dd>
<dd><code>configurator</code> - the given configurator.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTitleCreator()">
<h3>getTitleCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a></span> <span class="element-name">getTitleCreator</span>()</div>
<div class="block">Returns current specification dialog title creator.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>title creator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTitleCreator(com.nomagic.magicdraw.ui.dialogs.specifications.SpecificationTitleCreator)">
<h3>setTitleCreator</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTitleCreator</span><wbr/><span class="parameters">(<a href="SpecificationTitleCreator.html" title="interface in com.nomagic.magicdraw.ui.dialogs.specifications">SpecificationTitleCreator</a> titleCreator)</span></div>
<div class="block">Sets specification dialog title creator</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>titleCreator</code> - title creator.</dd>
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
