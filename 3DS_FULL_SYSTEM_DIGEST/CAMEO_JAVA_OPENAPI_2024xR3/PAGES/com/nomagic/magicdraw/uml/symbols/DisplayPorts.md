# JAVA OPENAPI: DisplayPorts (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/DisplayPorts.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DisplayPorts.html`
- source_sha256: `0105e0dc979fc4eeb40980fc44583520b834e2e404e53637d408d22d23af7a60`
- captured_utc: `2026-07-14T16:55:55.902462+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class DisplayPorts

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.DisplayPorts

@OpenApiAllpublic classDisplayPorts
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The utility class for showing ports on Symbol.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DisplayPorts](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html)>`
`[collectAvailablePorts](#collectAvailablePorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,boolean))([PresentationElement](PresentationElement.html) presentationElement,
 boolean includeInherited,
 boolean includePrivateInherited)`
Collects all available ports for Symbol.
`static void`
`[displayAllPorts](#displayAllPorts(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> targets,
 boolean showNotification)`
Displays all available ports on Symbol.
`static void`
`[displayPorts](#displayPorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List))([PresentationElement](PresentationElement.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html)> ports)`
Display chosen ports on Symbol.
`static void`
`[displayPorts](#displayPorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,boolean,boolean,boolean))([PresentationElement](PresentationElement.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html)> ports,
 boolean selectCreatedPorts,
 boolean doNotResizeParent,
 boolean createPaths)`
Display chosen ports on Symbol.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DisplayPorts
public DisplayPorts()
 ============ METHOD DETAIL ========== 
Method Details
collectAvailablePorts
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html)> collectAvailablePorts([PresentationElement](PresentationElement.html) presentationElement,
 boolean includeInherited,
 boolean includePrivateInherited)
Collects all available ports for Symbol.
Parameters:
`presentationElement` - the given Symbol to collect all available ports for.
`includeInherited` - should add inherited public ports.
`includePrivateInherited` - should add inherited private ports.
Returns:
list of available ports.
displayAllPorts
public static void displayAllPorts([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[PresentationElement](PresentationElement.html)> targets,
 boolean showNotification)
 throws [ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)
Displays all available ports on Symbol.
Parameters:
`targets` - collection of Symbols to show all ports for.
`showNotification` - true if notification should be shown when no ports are to be shown.
Throws:
`[ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
displayPorts
public static void displayPorts([PresentationElement](PresentationElement.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html)> ports)
 throws [ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)
Display chosen ports on Symbol.
 

 This method can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.
Parameters:
`target` - Symbol to show ports for.
`ports` - list of ports to be shown.
Throws:
`[ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.
displayPorts
public static void displayPorts([PresentationElement](PresentationElement.html) target,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Port](../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html)> ports,
 boolean selectCreatedPorts,
 boolean doNotResizeParent,
 boolean createPaths)
 throws [ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)
Display chosen ports on Symbol.
 

 This method can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.
Parameters:
`target` - Symbol to show ports for.
`ports` - list of ports to be shown.
`selectCreatedPorts` - select created ports
`doNotResizeParent` - do not resize Symbol to fit ports
`createPaths` - add paths connected to ports
Throws:
`[ReadOnlyElementException](../../openapi/uml/ReadOnlyElementException.html)` - if element permissions prohibited to perform this operation.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class DisplayPorts">Class DisplayPorts</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.DisplayPorts</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DisplayPorts</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The utility class for showing ports on Symbol.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DisplayPorts</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectAvailablePorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,boolean)">collectAvailablePorts</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement,
 boolean includeInherited,
 boolean includePrivateInherited)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Collects all available ports for Symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#displayAllPorts(java.util.Collection,boolean)">displayAllPorts</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; targets,
 boolean showNotification)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Displays all available ports on Symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#displayPorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List)">displayPorts</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt; ports)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Display chosen ports on Symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#displayPorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,boolean,boolean,boolean)">displayPorts</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt; ports,
 boolean selectCreatedPorts,
 boolean doNotResizeParent,
 boolean createPaths)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Display chosen ports on Symbol.</div>
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
<h3>DisplayPorts</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DisplayPorts</span>()</div>
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
<section class="detail" id="collectAvailablePorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,boolean,boolean)">
<h3>collectAvailablePorts</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt;</span> <span class="element-name">collectAvailablePorts</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> presentationElement,
 boolean includeInherited,
 boolean includePrivateInherited)</span></div>
<div class="block">Collects all available ports for Symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>presentationElement</code> - the given Symbol to collect all available ports for.</dd>
<dd><code>includeInherited</code> - should add inherited public ports.</dd>
<dd><code>includePrivateInherited</code> - should add inherited private ports.</dd>
<dt>Returns:</dt>
<dd>list of available ports.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="displayAllPorts(java.util.Collection,boolean)">
<h3>displayAllPorts</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">displayAllPorts</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt; targets,
 boolean showNotification)</span>
                            throws <span class="exceptions"><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Displays all available ports on Symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>targets</code> - collection of Symbols to show all ports for.</dd>
<dd><code>showNotification</code> - true if notification should be shown when no ports are to be shown.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="displayPorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List)">
<h3>displayPorts</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">displayPorts</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt; ports)</span>
                         throws <span class="exceptions"><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Display chosen ports on Symbol.
 <br/>
 This method can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - Symbol to show ports for.</dd>
<dd><code>ports</code> - list of ports to be shown.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="displayPorts(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List,boolean,boolean,boolean)">
<h3>displayPorts</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">displayPorts</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> target,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/compositestructures/mdports/Port.html" title="interface in com.nomagic.uml2.ext.magicdraw.compositestructures.mdports">Port</a>&gt; ports,
 boolean selectCreatedPorts,
 boolean doNotResizeParent,
 boolean createPaths)</span>
                         throws <span class="exceptions"><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Display chosen ports on Symbol.
 <br/>
 This method can be used only if some session was created with SessionManager. See code sample in SessionManager
 description for more details.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - Symbol to show ports for.</dd>
<dd><code>ports</code> - list of ports to be shown.</dd>
<dd><code>selectCreatedPorts</code> - select created ports</dd>
<dd><code>doNotResizeParent</code> - do not resize Symbol to fit ports</dd>
<dd><code>createPaths</code> - add paths connected to ports</dd>
<dt>Throws:</dt>
<dd><code><a href="../../openapi/uml/ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - if element permissions prohibited to perform this operation.</dd>
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
