# JAVA OPENAPI: Flows (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/model/Flows.html
- source_path: `com/dassault_systemes/modeler/kerml/model/Flows.html`
- source_sha256: `b94eac3394579a4af9e9707de08120127d250e1dd850d0ed509091c20155ace0`
- captured_utc: `2026-07-14T16:44:47.628838+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.model](package-summary.html)

## Class Flows

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.model.Flows

@OpenApiAllpublic classFlows
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Utility class to work with [`Flow`](kerml/Flow.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Flows](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Feature](kerml/Feature.html)`
`[getFirstOwnedFeature](#getFirstOwnedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) end)`
Returns the first owned feature of the given flow end.
`static [Feature](kerml/Feature.html)`
`[getRedefinedFeature](#getRedefinedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) end)`
Returns the redefined feature of the given flow end.
`static [Feature](kerml/Feature.html)`
`[getRedefinedSourceOutputFeature](#getRedefinedSourceOutputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow))([Flow](kerml/Flow.html) flow)`
Returns the redefined source output feature of the flow.
`static [Feature](kerml/Feature.html)`
`[getRedefinedTargetInputFeature](#getRedefinedTargetInputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow))([Flow](kerml/Flow.html) flow)`
Returns the redefined target input feature of the flow.
`static [Feature](kerml/Feature.html)`
`[getSourceFlowEnd](#getSourceFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Flow))([Flow](kerml/Flow.html) flow)`
Returns the source end feature of the given flow.
`static [Feature](kerml/Feature.html)`
`[getTargetFlowEnd](#getTargetFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Flow))([Flow](kerml/Flow.html) flow)`
Returns the target end feature of the given flow.
`static boolean`
`[isFlowEnd](#isFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Feature](kerml/Feature.html) feature)`
Checks whether the given feature is a flow end.
`static boolean`
`[isMessage](#isMessage(com.dassault_systemes.modeler.kerml.model.kerml.Flow))([Flow](kerml/Flow.html) type)`
Checks whether the flow represents a message.
`static void`
`[refactorFromFullNotationToShorthandNotation](#refactorFromFullNotationToShorthandNotation(com.dassault_systemes.modeler.kerml.model.kerml.Flow))([Flow](kerml/Flow.html) flow)`
Converts full flow notation to shorthand notation for all end features.
`static void`
`[refactorFromShorthandNotationToFullNotation](#refactorFromShorthandNotationToFullNotation(com.dassault_systemes.modeler.kerml.model.kerml.Flow))([Flow](kerml/Flow.html) flow)`
Converts shorthand flow notation to full notation for all end features.
`static void`
`[setRedefinedFeature](#setRedefinedFeature(int,com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature))(int endIndex,
 [Flow](kerml/Flow.html) flow,
 [Feature](kerml/Feature.html) feature)`
Sets or clears the redefined feature for the given flow end.
`static boolean`
`[setRedefinedSourceOutputFeature](#setRedefinedSourceOutputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Flow](kerml/Flow.html) flow,
 [Feature](kerml/Feature.html) feature)`
Sets the redefined source output feature of the flow.
`static boolean`
`[setRedefinedTargetInputFeature](#setRedefinedTargetInputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature))([Flow](kerml/Flow.html) flow,
 [Feature](kerml/Feature.html) feature)`
Sets the redefined target input feature of the flow.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Flows
public Flows()
 ============ METHOD DETAIL ========== 
Method Details
getSourceFlowEnd
@CheckForNullpublic static [Feature](kerml/Feature.html) getSourceFlowEnd([Flow](kerml/Flow.html) flow)
Returns the source end feature of the given flow.
Parameters:
`flow` - the flow
Returns:
source flow end, or null if not present
getTargetFlowEnd
@CheckForNullpublic static [Feature](kerml/Feature.html) getTargetFlowEnd([Flow](kerml/Flow.html) flow)
Returns the target end feature of the given flow.
Parameters:
`flow` - the flow
Returns:
target flow end, or null if not present
getFirstOwnedFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getFirstOwnedFeature([Feature](kerml/Feature.html) end)
Returns the first owned feature of the given flow end.
Parameters:
`end` - the flow end
Returns:
first owned feature, or null
getRedefinedFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getRedefinedFeature([Feature](kerml/Feature.html) end)
Returns the redefined feature of the given flow end.
Parameters:
`end` - the flow end
Returns:
redefined feature, or null
setRedefinedSourceOutputFeature
public static boolean setRedefinedSourceOutputFeature([Flow](kerml/Flow.html) flow,
 @CheckForNull
 [Feature](kerml/Feature.html) feature)
Sets the redefined source output feature of the flow.
Parameters:
`flow` - the flow
`feature` - feature to redefine to, or null
Returns:
always true
getRedefinedSourceOutputFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getRedefinedSourceOutputFeature([Flow](kerml/Flow.html) flow)
Returns the redefined source output feature of the flow.
Parameters:
`flow` - the flow
Returns:
redefined feature, or null
setRedefinedTargetInputFeature
public static boolean setRedefinedTargetInputFeature([Flow](kerml/Flow.html) flow,
 @CheckForNull
 [Feature](kerml/Feature.html) feature)
Sets the redefined target input feature of the flow.
Parameters:
`flow` - the flow
`feature` - feature to redefine to, or null
Returns:
always true
getRedefinedTargetInputFeature
@CheckForNullpublic static [Feature](kerml/Feature.html) getRedefinedTargetInputFeature([Flow](kerml/Flow.html) flow)
Returns the redefined target input feature of the flow.
Parameters:
`flow` - the flow
Returns:
redefined feature, or null
setRedefinedFeature
public static void setRedefinedFeature(int endIndex,
 [Flow](kerml/Flow.html) flow,
 @CheckForNull
 [Feature](kerml/Feature.html) feature)
Sets or clears the redefined feature for the given flow end.
Parameters:
`endIndex` - index of the flow end
`flow` - the flow
`feature` - feature to redefine to, or null to remove
isMessage
public static boolean isMessage([Flow](kerml/Flow.html) type)
Checks whether the flow represents a message.
Parameters:
`type` - the flow
Returns:
true if the flow has no end features
isFlowEnd
public static boolean isFlowEnd([Feature](kerml/Feature.html) feature)
Checks whether the given feature is a flow end.
Parameters:
`feature` - the feature
Returns:
true if the feature is a flow end
refactorFromShorthandNotationToFullNotation
public static void refactorFromShorthandNotationToFullNotation([Flow](kerml/Flow.html) flow)
Converts shorthand flow notation to full notation for all end features.
Parameters:
`flow` - the flow
refactorFromFullNotationToShorthandNotation
public static void refactorFromFullNotationToShorthandNotation([Flow](kerml/Flow.html) flow)
Converts full flow notation to shorthand notation for all end features.
Parameters:
`flow` - the flow

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.model</a></div>
<h1 class="title" title="Class Flows">Class Flows</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.model.Flows</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Flows</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility class to work with <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>Flow</code></a></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Flows</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFirstOwnedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getFirstOwnedFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the first owned feature of the given flow end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">getRedefinedFeature</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the redefined feature of the given flow end.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinedSourceOutputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">getRedefinedSourceOutputFeature</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the redefined source output feature of the flow.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getRedefinedTargetInputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">getRedefinedTargetInputFeature</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the redefined target input feature of the flow.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSourceFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">getSourceFlowEnd</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the source end feature of the given flow.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTargetFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">getTargetFlowEnd</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the target end feature of the given flow.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">isFlowEnd</a><wbr/>(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the given feature is a flow end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isMessage(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">isMessage</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> type)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks whether the flow represents a message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#refactorFromFullNotationToShorthandNotation(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">refactorFromFullNotationToShorthandNotation</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts full flow notation to shorthand notation for all end features.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#refactorFromShorthandNotationToFullNotation(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">refactorFromShorthandNotationToFullNotation</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Converts shorthand flow notation to full notation for all end features.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setRedefinedFeature(int,com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setRedefinedFeature</a><wbr/>(int endIndex,
 <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets or clears the redefined feature for the given flow end.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setRedefinedSourceOutputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setRedefinedSourceOutputFeature</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the redefined source output feature of the flow.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setRedefinedTargetInputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">setRedefinedTargetInputFeature</a><wbr/>(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow,
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the redefined target input feature of the flow.</div>
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
<h3>Flows</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Flows</span>()</div>
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
<section class="detail" id="getSourceFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">
<h3>getSourceFlowEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getSourceFlowEnd</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</span></div>
<div class="block">Returns the source end feature of the given flow.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
<dt>Returns:</dt>
<dd>source flow end, or null if not present</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTargetFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">
<h3>getTargetFlowEnd</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getTargetFlowEnd</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</span></div>
<div class="block">Returns the target end feature of the given flow.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
<dt>Returns:</dt>
<dd>target flow end, or null if not present</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFirstOwnedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getFirstOwnedFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getFirstOwnedFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</span></div>
<div class="block">Returns the first owned feature of the given flow end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>end</code> - the flow end</dd>
<dt>Returns:</dt>
<dd>first owned feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedFeature(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>getRedefinedFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRedefinedFeature</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> end)</span></div>
<div class="block">Returns the redefined feature of the given flow end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>end</code> - the flow end</dd>
<dt>Returns:</dt>
<dd>redefined feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefinedSourceOutputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setRedefinedSourceOutputFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setRedefinedSourceOutputFeature</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow,
 @CheckForNull
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Sets the redefined source output feature of the flow.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
<dd><code>feature</code> - feature to redefine to, or null</dd>
<dt>Returns:</dt>
<dd>always true</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedSourceOutputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">
<h3>getRedefinedSourceOutputFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRedefinedSourceOutputFeature</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</span></div>
<div class="block">Returns the redefined source output feature of the flow.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
<dt>Returns:</dt>
<dd>redefined feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefinedTargetInputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setRedefinedTargetInputFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">setRedefinedTargetInputFeature</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow,
 @CheckForNull
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Sets the redefined target input feature of the flow.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
<dd><code>feature</code> - feature to redefine to, or null</dd>
<dt>Returns:</dt>
<dd>always true</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRedefinedTargetInputFeature(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">
<h3>getRedefinedTargetInputFeature</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a></span> <span class="element-name">getRedefinedTargetInputFeature</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</span></div>
<div class="block">Returns the redefined target input feature of the flow.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
<dt>Returns:</dt>
<dd>redefined feature, or null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRedefinedFeature(int,com.dassault_systemes.modeler.kerml.model.kerml.Flow,com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>setRedefinedFeature</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setRedefinedFeature</span><wbr/><span class="parameters">(int endIndex,
 <a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow,
 @CheckForNull
 <a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Sets or clears the redefined feature for the given flow end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>endIndex</code> - index of the flow end</dd>
<dd><code>flow</code> - the flow</dd>
<dd><code>feature</code> - feature to redefine to, or null to remove</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMessage(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">
<h3>isMessage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isMessage</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> type)</span></div>
<div class="block">Checks whether the flow represents a message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - the flow</dd>
<dt>Returns:</dt>
<dd>true if the flow has no end features</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFlowEnd(com.dassault_systemes.modeler.kerml.model.kerml.Feature)">
<h3>isFlowEnd</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFlowEnd</span><wbr/><span class="parameters">(<a href="kerml/Feature.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Feature</a> feature)</span></div>
<div class="block">Checks whether the given feature is a flow end.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - the feature</dd>
<dt>Returns:</dt>
<dd>true if the feature is a flow end</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refactorFromShorthandNotationToFullNotation(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">
<h3>refactorFromShorthandNotationToFullNotation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">refactorFromShorthandNotationToFullNotation</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</span></div>
<div class="block">Converts shorthand flow notation to full notation for all end features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refactorFromFullNotationToShorthandNotation(com.dassault_systemes.modeler.kerml.model.kerml.Flow)">
<h3>refactorFromFullNotationToShorthandNotation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">refactorFromFullNotationToShorthandNotation</span><wbr/><span class="parameters">(<a href="kerml/Flow.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Flow</a> flow)</span></div>
<div class="block">Converts full flow notation to shorthand notation for all end features.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>flow</code> - the flow</dd>
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
