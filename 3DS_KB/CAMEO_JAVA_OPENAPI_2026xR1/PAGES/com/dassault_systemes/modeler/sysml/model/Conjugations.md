# JAVA OPENAPI: Conjugations (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/model/Conjugations.html
- source_path: `com/dassault_systemes/modeler/sysml/model/Conjugations.html`
- source_sha256: `e5ae1a85b069d45fb01c87709cc4b9bbb8977dcf73cf8e6fd6a92df1dfe4897d`
- captured_utc: `2026-07-14T16:45:02.312033+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.model](package-summary.html)

## Class Conjugations

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.sysml.model.Conjugations

@OpenApiAllpublic classConjugations
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility methods for conjugation

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Conjugations](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[addConjugatedPortTyping](#addConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.List))([PortUsage](sysml/PortUsage.html) port,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html)> definitions)`
Adds conjugated port definitions
`static void`
`[addPortTyping](#addPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.Collection))([PortUsage](sysml/PortUsage.html) port,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PortDefinition](sysml/PortDefinition.html)> definitions)`
Adds port definitions.
`static [PortDefinition](sysml/PortDefinition.html)`
`[createConjugatedPortDefinition](#createConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition))([PortDefinition](sysml/PortDefinition.html) portDefinition)`
Creates ConjugatedPortDefinition for PortDefinition
`static [PortDefinition](sysml/PortDefinition.html)`
`[getOppositePortDefinition](#getOppositePortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition))([PortDefinition](sysml/PortDefinition.html) portDefinition)`
Gets opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.
`static [PortDefinition](sysml/PortDefinition.html)`
`[getOrCreateOppositePortDefinition](#getOrCreateOppositePortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition))([PortDefinition](sysml/PortDefinition.html) portDefinition)`
Gets or creates opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.
`static void`
`[setConjugatedPortTyping](#setConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.List))([PortUsage](sysml/PortUsage.html) port,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html)> definitions)`
Sets conjugated port definitions
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Conjugations
public Conjugations()
 ============ METHOD DETAIL ========== 
Method Details
addConjugatedPortTyping
public static void addConjugatedPortTyping([PortUsage](sysml/PortUsage.html) port,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html)> definitions)
Adds conjugated port definitions
Parameters:
`port` - port to add definitions to
`definitions` - conjugated port definitions to add
setConjugatedPortTyping
public static void setConjugatedPortTyping([PortUsage](sysml/PortUsage.html) port,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[ConjugatedPortDefinition](sysml/ConjugatedPortDefinition.html)> definitions)
Sets conjugated port definitions
Parameters:
`port` - port to set definitions to
`definitions` - conjugated port definitions to set
addPortTyping
public static void addPortTyping([PortUsage](sysml/PortUsage.html) port,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[PortDefinition](sysml/PortDefinition.html)> definitions)
Adds port definitions. Handles mixed list of port definitions and conjugated port definitions
Parameters:
`port` - port to add definitions to
`definitions` - port definitions to add
getOppositePortDefinition
@CheckForNullpublic static [PortDefinition](sysml/PortDefinition.html) getOppositePortDefinition([PortDefinition](sysml/PortDefinition.html) portDefinition)
Gets opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.
Parameters:
`portDefinition` - Port definition to get opposite of
Returns:
Opposite port definition or null if opposite does not exist
getOrCreateOppositePortDefinition
@CheckForNullpublic static [PortDefinition](sysml/PortDefinition.html) getOrCreateOppositePortDefinition([PortDefinition](sysml/PortDefinition.html) portDefinition)
Gets or creates opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.
 Does not support PortDefinition creation for ConjugatedPortDefinition
Parameters:
`portDefinition` - Port definition to get or create opposite of
Returns:
Found or created PortDefinition, or null if it could not be created, or if ConjugatedPortDefinition was provided.
createConjugatedPortDefinition
@CheckForNullpublic static [PortDefinition](sysml/PortDefinition.html) createConjugatedPortDefinition([PortDefinition](sysml/PortDefinition.html) portDefinition)
Creates ConjugatedPortDefinition for PortDefinition
Parameters:
`portDefinition` - PortDefinition to create ConjugatedPortDefinition for
Returns:
created ConjugatedPortDefinition or original portDefinition if provided portDefinition is ConjugatedPortDefinition

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.model</a></div>
<h1 class="title" title="Class Conjugations">Class Conjugations</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.model.Conjugations</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Conjugations</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for conjugation</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Conjugations</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.List)">addConjugatedPortTyping</a><wbr/>(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> port,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a>&gt; definitions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds conjugated port definitions</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.Collection)">addPortTyping</a><wbr/>(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> port,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a>&gt; definitions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds port definitions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition)">createConjugatedPortDefinition</a><wbr/>(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> portDefinition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates ConjugatedPortDefinition for PortDefinition</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOppositePortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition)">getOppositePortDefinition</a><wbr/>(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> portDefinition)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getOrCreateOppositePortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition)">getOrCreateOppositePortDefinition</a><wbr/>(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> portDefinition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets or creates opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.List)">setConjugatedPortTyping</a><wbr/>(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> port,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a>&gt; definitions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets conjugated port definitions</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>Conjugations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Conjugations</span>()</div>
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
<section class="detail" id="addConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.List)">
<h3>addConjugatedPortTyping</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addConjugatedPortTyping</span><wbr/><span class="parameters">(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> port,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a>&gt; definitions)</span></div>
<div class="block">Adds conjugated port definitions</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>port</code> - port to add definitions to</dd>
<dd><code>definitions</code> - conjugated port definitions to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConjugatedPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.List)">
<h3>setConjugatedPortTyping</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setConjugatedPortTyping</span><wbr/><span class="parameters">(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> port,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sysml/ConjugatedPortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">ConjugatedPortDefinition</a>&gt; definitions)</span></div>
<div class="block">Sets conjugated port definitions</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>port</code> - port to set definitions to</dd>
<dd><code>definitions</code> - conjugated port definitions to set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addPortTyping(com.dassault_systemes.modeler.sysml.model.sysml.PortUsage,java.util.Collection)">
<h3>addPortTyping</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addPortTyping</span><wbr/><span class="parameters">(<a href="sysml/PortUsage.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortUsage</a> port,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a>&gt; definitions)</span></div>
<div class="block">Adds port definitions. Handles mixed list of port definitions and conjugated port definitions</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>port</code> - port to add definitions to</dd>
<dd><code>definitions</code> - port definitions to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOppositePortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition)">
<h3>getOppositePortDefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></span> <span class="element-name">getOppositePortDefinition</span><wbr/><span class="parameters">(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> portDefinition)</span></div>
<div class="block">Gets opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>portDefinition</code> - Port definition to get opposite of</dd>
<dt>Returns:</dt>
<dd>Opposite port definition or null if opposite does not exist</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOrCreateOppositePortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition)">
<h3>getOrCreateOppositePortDefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></span> <span class="element-name">getOrCreateOppositePortDefinition</span><wbr/><span class="parameters">(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> portDefinition)</span></div>
<div class="block">Gets or creates opposite PortDefinition of provided one - PortDefinition for ConjugatedPortDefinition
 and ConjugatedPortDefinition for PortDefinition.
 <p>
 Does not support PortDefinition creation for ConjugatedPortDefinition</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>portDefinition</code> - Port definition to get or create opposite of</dd>
<dt>Returns:</dt>
<dd>Found or created PortDefinition, or null if it could not be created, or if ConjugatedPortDefinition was provided.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createConjugatedPortDefinition(com.dassault_systemes.modeler.sysml.model.sysml.PortDefinition)">
<h3>createConjugatedPortDefinition</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a></span> <span class="element-name">createConjugatedPortDefinition</span><wbr/><span class="parameters">(<a href="sysml/PortDefinition.html" title="interface in com.dassault_systemes.modeler.sysml.model.sysml">PortDefinition</a> portDefinition)</span></div>
<div class="block">Creates ConjugatedPortDefinition for PortDefinition</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>portDefinition</code> - PortDefinition to create ConjugatedPortDefinition for</dd>
<dt>Returns:</dt>
<dd>created ConjugatedPortDefinition or original portDefinition if provided portDefinition is ConjugatedPortDefinition</dd>
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
