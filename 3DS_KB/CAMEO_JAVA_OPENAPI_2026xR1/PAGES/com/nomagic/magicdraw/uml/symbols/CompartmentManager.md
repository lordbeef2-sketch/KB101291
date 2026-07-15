# JAVA OPENAPI: CompartmentManager (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/uml/symbols/CompartmentManager.html
- source_path: `com/nomagic/magicdraw/uml/symbols/CompartmentManager.html`
- source_sha256: `2136333c1410e002838b5bf25f476f1a322f753e170d3758c8cd6490f75b568d`
- captured_utc: `2026-07-14T16:46:06.017881+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class CompartmentManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.CompartmentManager

@OpenApiAllpublic classCompartmentManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Utility methods for showing/hiding elements on compartments.

This class provides helper APIs for showing and hiding model elements and
 element properties within diagram compartments (for example, attributes,
 tagged values, or property compartments on shapes).

#### Example 1: Display a property in a compartment

````java
Property property = ...;   // Property model element
 ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(property),
     "Show Property",
     () -> CompartmentManager.showCompartmentElement(
         classView, CompartmentID.ATTRIBUTES, property)
 );
````

#### Example 2: Hide a slot on a class shape

````java
Slot slot = ...;           // Slot model element
 ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(slot),
     "Hide Slot",
     () -> CompartmentManager.hideCompartmentElement(
         classView, CompartmentID.TAGGED_VALUES_ON_SHAPE, slot)
 );
````

#### Example 3: Show element properties on a class shape

````java
ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(classView),
     "Show Properties",
     () -> CompartmentManager.showCompartmentElementProperties(
         classView,
         Arrays.asList(
             PropertyNames.OWNER,
             PropertyNames.VISIBILITY,
             PropertyNames.APPLIED_STEREOTYPE
         )
     )
 );
````

#### Example 4: Hide an element property from a class shape

````java
ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(classView),
     "Hide Property",
     () -> CompartmentManager.hideCompartmentElementProperty(
         classView, PropertyNames.IS_ABSTRACT)
 );
````

See Also:
[`CompartmentID`](CompartmentID.html)
[`SessionManager`](../../openapi/uml/SessionManager.html)
[`PresentationElement`](PresentationElement.html)
[`Element`](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CompartmentManager](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static void`
`[hideCompartmentElement](#hideCompartmentElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Hides an element in a compartment.
`static void`
`[hideCompartmentElementProperties](#hideCompartmentElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List))([PresentationElement](PresentationElement.html) view,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)`
Hides the specified properties from the element's property compartment
 on the given symbol.
`static void`
`[hideCompartmentElementProperty](#hideCompartmentElementProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Hides a property from the element's property compartment on the given symbol.
`static void`
`[hideCompartmentElements](#hideCompartmentElements(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.util.List))([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Hides elements in a compartment.
`static void`
`[showCompartmentElement](#showCompartmentElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Shows element in a compartment.
`static void`
`[showCompartmentElementProperties](#showCompartmentElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List))([PresentationElement](PresentationElement.html) view,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)`
Displays the specified properties in the element's property compartment
 on the given symbol.
`static void`
`[showCompartmentElementProperty](#showCompartmentElementProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)`
Displays a property in the element's property compartment on the given symbol.
`static void`
`[showCompartmentElements](#showCompartmentElements(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.util.List))([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)`
Shows elements in a compartment.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CompartmentManager
public CompartmentManager()
 ============ METHOD DETAIL ========== 
Method Details
showCompartmentElement
public static void showCompartmentElement([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Shows element in a compartment.
Parameters:
`view` - symbol which contains the compartment.
`compartmentID` - id of the compartment.
`element` - element to show.
showCompartmentElements
public static void showCompartmentElements([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Shows elements in a compartment.
Parameters:
`view` - symbol which contains the compartment.
`compartmentID` - id of the compartment.
`elements` - elements to show.
hideCompartmentElement
public static void hideCompartmentElement([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Hides an element in a compartment.
Parameters:
`view` - symbol which contains the compartment.
`compartmentID` - id of the compartment.
`element` - element to hide.
hideCompartmentElements
public static void hideCompartmentElements([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) compartmentID,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements)
Hides elements in a compartment.
Parameters:
`view` - symbol which contains the compartment.
`compartmentID` - id of the compartment.
`elements` - elements to hide.
showCompartmentElementProperty
public static void showCompartmentElementProperty([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Displays a property in the element's property compartment on the given symbol.
Parameters:
`view` - the symbol on which the property should be displayed
`propertyName` - the name of the property to display
showCompartmentElementProperties
public static void showCompartmentElementProperties([PresentationElement](PresentationElement.html) view,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)
Displays the specified properties in the element's property compartment
 on the given symbol.
Parameters:
`view` - the symbol on which the properties should be displayed
`propertyNames` - the names of the properties to display
hideCompartmentElementProperty
public static void hideCompartmentElementProperty([PresentationElement](PresentationElement.html) view,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) propertyName)
Hides a property from the element's property compartment on the given symbol.
Parameters:
`view` - the symbol from which the property should be hidden
`propertyName` - the name of the property to hide
hideCompartmentElementProperties
public static void hideCompartmentElementProperties([PresentationElement](PresentationElement.html) view,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> propertyNames)
Hides the specified properties from the element's property compartment
 on the given symbol.
Parameters:
`view` - the symbol from which the properties should be hidden
`propertyNames` - the names of the properties to hide

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class CompartmentManager">Class CompartmentManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.CompartmentManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CompartmentManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Utility methods for showing/hiding elements on compartments.

 <p>
 This class provides helper APIs for showing and hiding model elements and
 element properties within diagram compartments (for example, attributes,
 tagged values, or property compartments on shapes).
 </p>
<h3 id="example-1-display-a-property-in-a-compartment-heading">Example 1: Display a property in a compartment</h3>
<pre><code>
 Property property = ...;   // Property model element
 ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(property),
     "Show Property",
     () -&gt; CompartmentManager.showCompartmentElement(
         classView, CompartmentID.ATTRIBUTES, property)
 );
 </code></pre>
<h3 id="example-2-hide-a-slot-on-a-class-shape-heading">Example 2: Hide a slot on a class shape</h3>
<pre><code>
 Slot slot = ...;           // Slot model element
 ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(slot),
     "Hide Slot",
     () -&gt; CompartmentManager.hideCompartmentElement(
         classView, CompartmentID.TAGGED_VALUES_ON_SHAPE, slot)
 );
 </code></pre>
<h3 id="example-3-show-element-properties-on-a-class-shape-heading">Example 3: Show element properties on a class shape</h3>
<pre><code>
 ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(classView),
     "Show Properties",
     () -&gt; CompartmentManager.showCompartmentElementProperties(
         classView,
         Arrays.asList(
             PropertyNames.OWNER,
             PropertyNames.VISIBILITY,
             PropertyNames.APPLIED_STEREOTYPE
         )
     )
 );
 </code></pre>
<h3 id="example-4-hide-an-element-property-from-a-class-shape-heading">Example 4: Hide an element property from a class shape</h3>
<pre><code>
 ClassView classView = ...; // Class symbol

 SessionManager.getInstance().executeInsideSession(
     Project.getProject(classView),
     "Hide Property",
     () -&gt; CompartmentManager.hideCompartmentElementProperty(
         classView, PropertyNames.IS_ABSTRACT)
 );
 </code></pre></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="CompartmentID.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>CompartmentID</code></a></li>
<li><a href="../../openapi/uml/SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml"><code>SessionManager</code></a></li>
<li><a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElement</code></a></li>
<li><a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>Element</code></a></li>
</ul>
</dd>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CompartmentManager</a>()</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hideCompartmentElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">hideCompartmentElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Hides an element in a compartment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hideCompartmentElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List)">hideCompartmentElementProperties</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Hides the specified properties from the element's property compartment
 on the given symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hideCompartmentElementProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">hideCompartmentElementProperty</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Hides a property from the element's property compartment on the given symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hideCompartmentElements(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.util.List)">hideCompartmentElements</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Hides elements in a compartment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#showCompartmentElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">showCompartmentElement</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Shows element in a compartment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#showCompartmentElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List)">showCompartmentElementProperties</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Displays the specified properties in the element's property compartment
 on the given symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#showCompartmentElementProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">showCompartmentElementProperty</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Displays a property in the element's property compartment on the given symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#showCompartmentElements(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.util.List)">showCompartmentElements</a><wbr/>(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Shows elements in a compartment.</div>
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
<h3>CompartmentManager</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CompartmentManager</span>()</div>
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
<section class="detail" id="showCompartmentElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>showCompartmentElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">showCompartmentElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Shows element in a compartment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol which contains the compartment.</dd>
<dd><code>compartmentID</code> - id of the compartment.</dd>
<dd><code>element</code> - element to show.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showCompartmentElements(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.util.List)">
<h3>showCompartmentElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">showCompartmentElements</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Shows elements in a compartment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol which contains the compartment.</dd>
<dd><code>compartmentID</code> - id of the compartment.</dd>
<dd><code>elements</code> - elements to show.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideCompartmentElement(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>hideCompartmentElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">hideCompartmentElement</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Hides an element in a compartment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol which contains the compartment.</dd>
<dd><code>compartmentID</code> - id of the compartment.</dd>
<dd><code>element</code> - element to hide.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideCompartmentElements(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String,java.util.List)">
<h3>hideCompartmentElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">hideCompartmentElements</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> compartmentID,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements)</span></div>
<div class="block">Hides elements in a compartment.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol which contains the compartment.</dd>
<dd><code>compartmentID</code> - id of the compartment.</dd>
<dd><code>elements</code> - elements to hide.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showCompartmentElementProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>showCompartmentElementProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">showCompartmentElementProperty</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Displays a property in the element's property compartment on the given symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - the symbol on which the property should be displayed</dd>
<dd><code>propertyName</code> - the name of the property to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="showCompartmentElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List)">
<h3>showCompartmentElementProperties</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">showCompartmentElementProperties</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</span></div>
<div class="block">Displays the specified properties in the element's property compartment
 on the given symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - the symbol on which the properties should be displayed</dd>
<dd><code>propertyNames</code> - the names of the properties to display</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideCompartmentElementProperty(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>hideCompartmentElementProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">hideCompartmentElementProperty</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> propertyName)</span></div>
<div class="block">Hides a property from the element's property compartment on the given symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - the symbol from which the property should be hidden</dd>
<dd><code>propertyName</code> - the name of the property to hide</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideCompartmentElementProperties(com.nomagic.magicdraw.uml.symbols.PresentationElement,java.util.List)">
<h3>hideCompartmentElementProperties</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">hideCompartmentElementProperties</span><wbr/><span class="parameters">(<a href="PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; propertyNames)</span></div>
<div class="block">Hides the specified properties from the element's property compartment
 on the given symbol.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - the symbol from which the properties should be hidden</dd>
<dd><code>propertyNames</code> - the names of the properties to hide</dd>
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
