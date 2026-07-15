# JAVA OPENAPI: ScenarioNode (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioNode.html
- source_path: `com/nomagic/magicdraw/usecasescenarios/scenarios/ScenarioNode.html`
- source_sha256: `adbbffad8ef1ccdd71aab35ceef18d1cddbe3c8fd116fcf67241b0033956aa4d`
- captured_utc: `2026-07-14T16:46:10.521941+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.usecasescenarios.scenarios](package-summary.html)

## Interface ScenarioNode

All Known Subinterfaces:
`[AlternativeCondition](AlternativeCondition.html)`, `[ExceptionType](ExceptionType.html)`, `[FlowStep](FlowStep.html)`, `[Scenario](Scenario.html)`, `[ScenarioNodeEnd](ScenarioNodeEnd.html)`, `[ScenarioNodeStart](ScenarioNodeStart.html)`

@OpenApiAllpublic interfaceScenarioNode

General node in the scenario. All specific nodes in scenario derive from it.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[belongsToIncludedExtending](#belongsToIncludedExtending())()`
Indicates if node belongs to included/extending use case.
`[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)`
`[getElement](#getElement())()`
Gets element which represents this node.
`[ScenarioNodeEnd](ScenarioNodeEnd.html)`
`[getEnd](#getEnd())()`
Gets scenario node end.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getHumanType](#getHumanType())()`
Gets human-readable representation of scenario node.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Gets name of the node.
`[ScenarioNode](ScenarioNode.html)`
`[getParent](#getParent())()`
Gets parent of the scenario node.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [ScenarioNode](ScenarioNode.html)>`
`[getParentContainer](#getParentContainer())()`
Gets container in the parent to which this node belongs.
`[ScenarioNodeStart](ScenarioNodeStart.html)`
`[getStart](#getStart())()`
Gets scenario node start.
`boolean`
`[isEditable](#isEditable())()`
Indicates if node is editable.
`void`
`[setName](#setName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Sets name for the scenario node.

============ METHOD DETAIL ========== 
Method Details
getElement
[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) getElement()
Gets element which represents this node.
Returns:
element which represents this node.
belongsToIncludedExtending
boolean belongsToIncludedExtending()
Indicates if node belongs to included/extending use case.
Returns:
true if node belongs to included/extending use case, false otherwise.
setName
void setName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Sets name for the scenario node.
Parameters:
`name` - name to set.
getName
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName()
Gets name of the node.
Returns:
node name.
getParent
[ScenarioNode](ScenarioNode.html) getParent()
Gets parent of the scenario node.
Returns:
parent of the scenario node.
isEditable
boolean isEditable()
Indicates if node is editable.
Returns:
true if node is editable, false otherwise.
getStart
[ScenarioNodeStart](ScenarioNodeStart.html) getStart()
Gets scenario node start.
Returns:
scenario node start.
getEnd
[ScenarioNodeEnd](ScenarioNodeEnd.html) getEnd()
Gets scenario node end.
Returns:
scenario node end.
getHumanType
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getHumanType()
Gets human-readable representation of scenario node.
Returns:
human-readable representation of scenario node.
getParentContainer
[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<? extends [ScenarioNode](ScenarioNode.html)> getParentContainer()
Gets container in the parent to which this node belongs.
 Parent container can be used for changing position of the node
 or figuring out the number of node.
Returns:
parent container to which this node belongs.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.usecasescenarios.scenarios</a></div>
<h1 class="title" title="Interface ScenarioNode">Interface ScenarioNode</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="AlternativeCondition.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">AlternativeCondition</a></code>, <code><a href="ExceptionType.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ExceptionType</a></code>, <code><a href="FlowStep.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">FlowStep</a></code>, <code><a href="Scenario.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">Scenario</a></code>, <code><a href="ScenarioNodeEnd.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeEnd</a></code>, <code><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeStart</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ScenarioNode</span></div>
<div class="block">General node in the scenario. All specific nodes in scenario derive from it.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#belongsToIncludedExtending()">belongsToIncludedExtending</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if node belongs to included/extending use case.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getElement()">getElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets element which represents this node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ScenarioNodeEnd.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeEnd</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEnd()">getEnd</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets scenario node end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getHumanType()">getHumanType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets human-readable representation of scenario node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets name of the node.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParent()">getParent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets parent of the scenario node.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;? extends <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getParentContainer()">getParentContainer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets container in the parent to which this node belongs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeStart</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getStart()">getStart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets scenario node start.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEditable()">isEditable</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates if node is editable.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setName(java.lang.String)">setName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets name for the scenario node.</div>
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
<section class="detail" id="getElement()">
<h3>getElement</h3>
<div class="member-signature"><span class="return-type"><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getElement</span>()</div>
<div class="block">Gets element which represents this node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>element which represents this node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="belongsToIncludedExtending()">
<h3>belongsToIncludedExtending</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">belongsToIncludedExtending</span>()</div>
<div class="block">Indicates if node belongs to included/extending use case.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if node belongs to included/extending use case, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setName(java.lang.String)">
<h3>setName</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Sets name for the scenario node.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name to set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Gets name of the node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>node name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParent()">
<h3>getParent</h3>
<div class="member-signature"><span class="return-type"><a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a></span> <span class="element-name">getParent</span>()</div>
<div class="block">Gets parent of the scenario node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent of the scenario node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEditable()">
<h3>isEditable</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEditable</span>()</div>
<div class="block">Indicates if node is editable.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if node is editable, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStart()">
<h3>getStart</h3>
<div class="member-signature"><span class="return-type"><a href="ScenarioNodeStart.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeStart</a></span> <span class="element-name">getStart</span>()</div>
<div class="block">Gets scenario node start.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario node start.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnd()">
<h3>getEnd</h3>
<div class="member-signature"><span class="return-type"><a href="ScenarioNodeEnd.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNodeEnd</a></span> <span class="element-name">getEnd</span>()</div>
<div class="block">Gets scenario node end.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scenario node end.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHumanType()">
<h3>getHumanType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHumanType</span>()</div>
<div class="block">Gets human-readable representation of scenario node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>human-readable representation of scenario node.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentContainer()">
<h3>getParentContainer</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="ScenarioNode.html" title="interface in com.nomagic.magicdraw.usecasescenarios.scenarios">ScenarioNode</a>&gt;</span> <span class="element-name">getParentContainer</span>()</div>
<div class="block">Gets container in the parent to which this node belongs.
 Parent container can be used for changing position of the node
 or figuring out the number of node.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>parent container to which this node belongs.</dd>
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
