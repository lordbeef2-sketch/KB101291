# JAVA OPENAPI: ScriptHelper (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/modelmetrics/ScriptHelper.html
- source_path: `com/nomagic/magicdraw/modelmetrics/ScriptHelper.html`
- source_sha256: `d2667d02f0250a8fede7220f57ee45964dd6a9a7965756c3793dd5f735d8231d`
- captured_utc: `2026-07-14T16:55:28.838160+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.modelmetrics](package-summary.html)

## Class ScriptHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.modelmetrics.ScriptHelper

@OpenApiAllpublic classScriptHelper
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Helper methods for calculating metrics.

Since:
13.12.5 (15:19)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ScriptHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static double`
`[calcAverageForList](#calcAverageForList(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html)> items)`
Calculates average for a list of numbers.
`static double`
`[calcPercentage](#calcPercentage(int,int))(int all,
 int covered)`
Calculates percentage.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getElementsRecursively](#getElementsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owningPackage)`
Returns all elements in a package recursively.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getElementsRecursively](#getElementsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owningPackage,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns all elements in a package recursively.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getElementsRecursively](#getElementsRecursively(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> owningPackages)`
Returns all elements in given packages recursively.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[getElementsRecursively](#getElementsRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> owningPackages,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)`
Returns all elements in given packages recursively.
`static boolean`
`[isParentOf](#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) possibleParent,
 [BaseElement](../uml/BaseElement.html) possibleChild)`
Checks if given object is child of given parent object.
`static boolean`
`[isParentOf](#isParentOf(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> possibleParents,
 [BaseElement](../uml/BaseElement.html) possibleChild)`
Checks if given object is child of any element in a given list of possible parents.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ScriptHelper
public ScriptHelper()
 ============ METHOD DETAIL ========== 
Method Details
getElementsRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getElementsRecursively([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owningPackage)
Returns all elements in a package recursively.
Parameters:
`owningPackage` - package to collect the elements.
Returns:
all owned elements recursively. The input owningPackage is excluded.
getElementsRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getElementsRecursively([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> owningPackages)
Returns all elements in given packages recursively.
Parameters:
`owningPackages` - collection of packages to collect the elements
Returns:
all owned elements recursively. Given packages are excluded
getElementsRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getElementsRecursively([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owningPackage,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns all elements in a package recursively.
Parameters:
`owningPackage` - package to collect the elements.
`stereotype` - stereotype of elements to collect.
Returns:
all owned elements recursively. The input owningPackage is excluded.
getElementsRecursively
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) getElementsRecursively([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> owningPackages,
 [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype)
Returns all elements in given packages recursively.
Parameters:
`owningPackages` - collection of packages to collect the elements
`stereotype` - stereotype of elements to collect.
Returns:
all owned elements recursively. Given packages are excluded
isParentOf
public static boolean isParentOf([BaseElement](../uml/BaseElement.html) possibleParent,
 [BaseElement](../uml/BaseElement.html) possibleChild)
Checks if given object is child of given parent object.
Parameters:
`possibleParent` - possible parent
`possibleChild` - possible child
Returns:
true if possibleChild is child of possibleParent.
isParentOf
public static boolean isParentOf([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [BaseElement](../uml/BaseElement.html)> possibleParents,
 [BaseElement](../uml/BaseElement.html) possibleChild)
Checks if given object is child of any element in a given list of possible parents.
Parameters:
`possibleParents` - possible parent
`possibleChild` - possible child
Returns:
true if possibleChild is child of possibleParent.
calcPercentage
public static double calcPercentage(int all,
 int covered)
Calculates percentage.
Parameters:
`all` - denominator
`covered` - nominator
Returns:
percentage value or 0 if denominator <= 0
calcAverageForList
public static double calcAverageForList(@CheckForNull
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [Number](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html)> items)
Calculates average for a list of numbers.
Parameters:
`items` - list of numbers
Returns:
average value for the given list of numbers or 0 by default

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.modelmetrics</a></div>
<h1 class="title" title="Class ScriptHelper">Class ScriptHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.modelmetrics.ScriptHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ScriptHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Helper methods for calculating metrics.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>13.12.5 (15:19)</dd>
</dl>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ScriptHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#calcAverageForList(java.util.List)">calcAverageForList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a>&gt; items)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculates average for a list of numbers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#calcPercentage(int,int)">calcPercentage</a><wbr/>(int all,
 int covered)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculates percentage.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getElementsRecursively</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owningPackage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements in a package recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getElementsRecursively</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owningPackage,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements in a package recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsRecursively(java.util.Collection)">getElementsRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owningPackages)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements in given packages recursively.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getElementsRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">getElementsRecursively</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owningPackages,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns all elements in given packages recursively.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleParent,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given object is child of given parent object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentOf(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">isParentOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; possibleParents,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given object is child of any element in a given list of possible parents.</div>
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
<h3>ScriptHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ScriptHelper</span>()</div>
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
<section class="detail" id="getElementsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getElementsRecursively</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owningPackage)</span></div>
<div class="block">Returns all elements in a package recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owningPackage</code> - package to collect the elements.</dd>
<dt>Returns:</dt>
<dd>all owned elements recursively. The input owningPackage is excluded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsRecursively(java.util.Collection)">
<h3>getElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getElementsRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owningPackages)</span></div>
<div class="block">Returns all elements in given packages recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owningPackages</code> - collection of packages to collect the elements</dd>
<dt>Returns:</dt>
<dd>all owned elements recursively. Given packages are excluded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsRecursively(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getElementsRecursively</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owningPackage,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns all elements in a package recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owningPackage</code> - package to collect the elements.</dd>
<dd><code>stereotype</code> - stereotype of elements to collect.</dd>
<dt>Returns:</dt>
<dd>all owned elements recursively. The input owningPackage is excluded.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElementsRecursively(java.util.Collection,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">
<h3>getElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">getElementsRecursively</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; owningPackages,
 <a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype)</span></div>
<div class="block">Returns all elements in given packages recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owningPackages</code> - collection of packages to collect the elements</dd>
<dd><code>stereotype</code> - stereotype of elements to collect.</dd>
<dt>Returns:</dt>
<dd>all owned elements recursively. Given packages are excluded</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.uml.BaseElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleParent,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</span></div>
<div class="block">Checks if given object is child of given parent object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleParent</code> - possible parent</dd>
<dd><code>possibleChild</code> - possible child</dd>
<dt>Returns:</dt>
<dd>true if possibleChild is child of possibleParent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentOf(java.util.Collection,com.nomagic.magicdraw.uml.BaseElement)">
<h3>isParentOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isParentOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt; possibleParents,
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> possibleChild)</span></div>
<div class="block">Checks if given object is child of any element in a given list of possible parents.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>possibleParents</code> - possible parent</dd>
<dd><code>possibleChild</code> - possible child</dd>
<dt>Returns:</dt>
<dd>true if possibleChild is child of possibleParent.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calcPercentage(int,int)">
<h3>calcPercentage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">calcPercentage</span><wbr/><span class="parameters">(int all,
 int covered)</span></div>
<div class="block">Calculates percentage.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>all</code> - denominator</dd>
<dd><code>covered</code> - nominator</dd>
<dt>Returns:</dt>
<dd>percentage value or 0 if denominator &lt;= 0</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calcAverageForList(java.util.List)">
<h3>calcAverageForList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">double</span> <span class="element-name">calcAverageForList</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Number.html" title="class or interface in java.lang">Number</a>&gt; items)</span></div>
<div class="block">Calculates average for a list of numbers.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>items</code> - list of numbers</dd>
<dt>Returns:</dt>
<dd>average value for the given list of numbers or 0 by default</dd>
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
