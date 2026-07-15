# JAVA OPENAPI: ActionsCreator (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/actions/ActionsCreator.html
- source_path: `com/nomagic/magicdraw/actions/ActionsCreator.html`
- source_sha256: `c0ec9d42071bc2583a7bb03712de6721d11cba5d74162bd0ee033ab2a57c7e72`
- captured_utc: `2026-07-14T16:51:00.967935+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.actions](package-summary.html)

## Class ActionsCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.actions.ActionsCreator

@OpenApipublic classActionsCreator
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The helper class used for creating and holding all MagicDraw actions.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[MDActionsManager](MDActionsManager.html)`
`[createActivityDiagramActions](#createActivityDiagramActions())()`
Creates the actions for activity diagram
`[MDActionsManager](MDActionsManager.html)`
`[createAnyDiagramActions](#createAnyDiagramActions())()`
Creates the actions for any abstract diagram.
`[MDActionsManager](MDActionsManager.html)`
`[createClassDiagramActions](#createClassDiagramActions())()`
Creates the actions for class diagram.
`void`
`[createCommonDiagramsActions](#createCommonDiagramsActions(com.nomagic.actions.ActionsCategory))([ActionsCategory](../../actions/ActionsCategory.html) category)`
Creates actions common for all diagrams.
`[MDActionsManager](MDActionsManager.html)`
`[createCommunicationDiagramActions](#createCommunicationDiagramActions())()`
Creates the actions for collaboration diagram
`[MDActionsManager](MDActionsManager.html)`
`[createComponentDiagramActions](#createComponentDiagramActions())()`
Creates the actions for component diagram
`[MDActionsManager](MDActionsManager.html)`
`[createCompositeStructureDiagramActions](#createCompositeStructureDiagramActions())()`
Creates the actions for composite structure diagram
`[MDActionsManager](MDActionsManager.html)`
`[createDeploymentDiagramActions](#createDeploymentDiagramActions())()`
Creates the actions for deployment diagram
`[MDActionsManager](MDActionsManager.html)`
`[createGeneralActions](#createGeneralActions())()`
Creates the general actions.
`[MDActionsManager](MDActionsManager.html)`
`[createImplementationDiagramActions](#createImplementationDiagramActions())()`
Deprecated.
use [`createComponentDiagramActions()`](#createComponentDiagramActions())
`[MDActionsManager](MDActionsManager.html)`
`[createInteractionOverviewDiagramActions](#createInteractionOverviewDiagramActions())()`
Creates the actions for activity diagram
`[MDActionsManager](MDActionsManager.html)`
`[createObjectDiagramActions](#createObjectDiagramActions())()`
Creates the actions for object diagram
`[MDActionsManager](MDActionsManager.html)`
`[createPackageDiagramActions](#createPackageDiagramActions())()`
Creates the actions for package diagram
`[MDActionsManager](MDActionsManager.html)`
`[createProfileDiagramActions](#createProfileDiagramActions())()`
Creates the actions for profile diagram
`[MDActionsManager](MDActionsManager.html)`
`[createProtocolStateDiagramActions](#createProtocolStateDiagramActions())()`
Creates the actions for protocol state machine diagram
`[MDActionsManager](MDActionsManager.html)`
`[createSequenceDiagramActions](#createSequenceDiagramActions())()`
Creates the actions for collaboration diagram
`[MDActionsManager](MDActionsManager.html)`
`[createStateDiagramActions](#createStateDiagramActions())()`
Creates the actions for state diagram
`[MDActionsManager](MDActionsManager.html)`
`[createUseCaseDiagramActions](#createUseCaseDiagramActions())()`
Creates the actions for use case diagram
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
createGeneralActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createGeneralActions()
Creates the general actions.
Returns:
create general actions.
createCommonDiagramsActions
@OpenApipublic void createCommonDiagramsActions([ActionsCategory](../../actions/ActionsCategory.html) category)
Creates actions common for all diagrams.
 This method will always create new instances of the actions.
Parameters:
`category` - the category to add created actions into.
createClassDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createClassDiagramActions()
Creates the actions for class diagram.
Returns:
the class diagram actions.
createUseCaseDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createUseCaseDiagramActions()
Creates the actions for use case diagram
Returns:
the use case diagram actions.
createCommunicationDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createCommunicationDiagramActions()
Creates the actions for collaboration diagram
Returns:
the collaboration diagram actions.
createSequenceDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createSequenceDiagramActions()
Creates the actions for collaboration diagram
Returns:
the sequence diagram actions.
createStateDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createStateDiagramActions()
Creates the actions for state diagram
Returns:
the state diagram actions.
createProtocolStateDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createProtocolStateDiagramActions()
Creates the actions for protocol state machine diagram
Returns:
the protocol state machine diagram actions.
createActivityDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createActivityDiagramActions()
Creates the actions for activity diagram
Returns:
the activity diagram actions.
createInteractionOverviewDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createInteractionOverviewDiagramActions()
Creates the actions for activity diagram
Returns:
the activity diagram actions.
createImplementationDiagramActions
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [MDActionsManager](MDActionsManager.html) createImplementationDiagramActions()
Deprecated.
use [`createComponentDiagramActions()`](#createComponentDiagramActions())
Creates the actions for implementation diagram
Returns:
the implementation diagram actions.
createObjectDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createObjectDiagramActions()
Creates the actions for object diagram
Returns:
the object diagram actions.
createPackageDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createPackageDiagramActions()
Creates the actions for package diagram
Returns:
the package diagram actions.
createComponentDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createComponentDiagramActions()
Creates the actions for component diagram
Returns:
the component diagram actions.
createDeploymentDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createDeploymentDiagramActions()
Creates the actions for deployment diagram
Returns:
the deployment diagram actions.
createProfileDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createProfileDiagramActions()
Creates the actions for profile diagram
Returns:
the profile diagram actions.
createCompositeStructureDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createCompositeStructureDiagramActions()
Creates the actions for composite structure diagram
Returns:
the composite structure diagram actions.
createAnyDiagramActions
@OpenApipublic [MDActionsManager](MDActionsManager.html) createAnyDiagramActions()
Creates the actions for any abstract diagram.
Returns:
the abstract diagram actions.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.actions</a></div>
<h1 class="title" title="Class ActionsCreator">Class ActionsCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.actions.ActionsCreator</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ActionsCreator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The helper class used for creating and holding all MagicDraw actions.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createActivityDiagramActions()">createActivityDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for activity diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAnyDiagramActions()">createAnyDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for any abstract diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createClassDiagramActions()">createClassDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for class diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommonDiagramsActions(com.nomagic.actions.ActionsCategory)">createCommonDiagramsActions</a><wbr/>(<a href="../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates actions common for all diagrams.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCommunicationDiagramActions()">createCommunicationDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for collaboration diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComponentDiagramActions()">createComponentDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for component diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createCompositeStructureDiagramActions()">createCompositeStructureDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for composite structure diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDeploymentDiagramActions()">createDeploymentDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for deployment diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createGeneralActions()">createGeneralActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the general actions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createImplementationDiagramActions()">createImplementationDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createComponentDiagramActions()"><code>createComponentDiagramActions()</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createInteractionOverviewDiagramActions()">createInteractionOverviewDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for activity diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createObjectDiagramActions()">createObjectDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for object diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createPackageDiagramActions()">createPackageDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for package diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProfileDiagramActions()">createProfileDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for profile diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createProtocolStateDiagramActions()">createProtocolStateDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for protocol state machine diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSequenceDiagramActions()">createSequenceDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for collaboration diagram</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createStateDiagramActions()">createStateDiagramActions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for state diagram</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createUseCaseDiagramActions()">createUseCaseDiagramActions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates the actions for use case diagram</div>
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
<section class="detail" id="createGeneralActions()">
<h3>createGeneralActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createGeneralActions</span>()</div>
<div class="block">Creates the general actions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>create general actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommonDiagramsActions(com.nomagic.actions.ActionsCategory)">
<h3>createCommonDiagramsActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createCommonDiagramsActions</span><wbr/><span class="parameters">(<a href="../../actions/ActionsCategory.html" title="class in com.nomagic.actions">ActionsCategory</a> category)</span></div>
<div class="block">Creates actions common for all diagrams.
 This method will always create new instances of the actions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>category</code> - the category to add created actions into.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createClassDiagramActions()">
<h3>createClassDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createClassDiagramActions</span>()</div>
<div class="block">Creates the actions for class diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the class diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createUseCaseDiagramActions()">
<h3>createUseCaseDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createUseCaseDiagramActions</span>()</div>
<div class="block">Creates the actions for use case diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the use case diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCommunicationDiagramActions()">
<h3>createCommunicationDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createCommunicationDiagramActions</span>()</div>
<div class="block">Creates the actions for collaboration diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the collaboration diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSequenceDiagramActions()">
<h3>createSequenceDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createSequenceDiagramActions</span>()</div>
<div class="block">Creates the actions for collaboration diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the sequence diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStateDiagramActions()">
<h3>createStateDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createStateDiagramActions</span>()</div>
<div class="block">Creates the actions for state diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the state diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProtocolStateDiagramActions()">
<h3>createProtocolStateDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createProtocolStateDiagramActions</span>()</div>
<div class="block">Creates the actions for protocol state machine diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the protocol state machine diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createActivityDiagramActions()">
<h3>createActivityDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createActivityDiagramActions</span>()</div>
<div class="block">Creates the actions for activity diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the activity diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createInteractionOverviewDiagramActions()">
<h3>createInteractionOverviewDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createInteractionOverviewDiagramActions</span>()</div>
<div class="block">Creates the actions for activity diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the activity diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createImplementationDiagramActions()">
<h3>createImplementationDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createImplementationDiagramActions</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createComponentDiagramActions()"><code>createComponentDiagramActions()</code></a></div>
</div>
<div class="block">Creates the actions for implementation diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the implementation diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createObjectDiagramActions()">
<h3>createObjectDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createObjectDiagramActions</span>()</div>
<div class="block">Creates the actions for object diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the object diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createPackageDiagramActions()">
<h3>createPackageDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createPackageDiagramActions</span>()</div>
<div class="block">Creates the actions for package diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the package diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComponentDiagramActions()">
<h3>createComponentDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createComponentDiagramActions</span>()</div>
<div class="block">Creates the actions for component diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the component diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDeploymentDiagramActions()">
<h3>createDeploymentDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createDeploymentDiagramActions</span>()</div>
<div class="block">Creates the actions for deployment diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the deployment diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createProfileDiagramActions()">
<h3>createProfileDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createProfileDiagramActions</span>()</div>
<div class="block">Creates the actions for profile diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the profile diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCompositeStructureDiagramActions()">
<h3>createCompositeStructureDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createCompositeStructureDiagramActions</span>()</div>
<div class="block">Creates the actions for composite structure diagram</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the composite structure diagram actions.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAnyDiagramActions()">
<h3>createAnyDiagramActions</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a href="MDActionsManager.html" title="class in com.nomagic.magicdraw.actions">MDActionsManager</a></span> <span class="element-name">createAnyDiagramActions</span>()</div>
<div class="block">Creates the actions for any abstract diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the abstract diagram actions.</dd>
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
