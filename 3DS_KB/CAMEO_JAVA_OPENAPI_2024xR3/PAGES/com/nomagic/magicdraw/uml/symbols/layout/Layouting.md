# JAVA OPENAPI: Layouting (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/uml/symbols/layout/Layouting.html
- source_path: `com/nomagic/magicdraw/uml/symbols/layout/Layouting.html`
- source_sha256: `dac6691ab7198585ee4a328e509da6fe088f59d03efac4a990828895b592932a`
- captured_utc: `2026-07-14T16:55:57.873487+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols.layout](package-summary.html)

## Class Layouting

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.layout.Layouting

@OpenApiAllpublic classLayouting
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Provides API for layouting diagrams.
 
Example 1: Layout a diagram using the default diagram layouter
AbstractDiagramPresentationElement diagram = ...; // Diagram to layout
 diagram.open();
 Layouting.layout(diagram);
Example 2: Layout a diagram using any diagram layouter

 The available diagram layouter constant is provided in the [`class`](Layouting.html). e.g. [`HIERARCHIC_DIAGRAM_LAYOUTER`](#HIERARCHIC_DIAGRAM_LAYOUTER)
AbstractDiagramPresentationElement diagram = ...; // Diagram to layout
 diagram.open()
 Layouting.layout(diagram, Layouting.HIERARCHIC_DIAGRAM_LAYOUTER);
Example 3: Layout a diagram using any diagram layouter, and appropriate options

 The available diagram layouter constant are provided in the [`class`](Layouting.html). e.g. [`HIERARCHIC_DIAGRAM_LAYOUTER`](#HIERARCHIC_DIAGRAM_LAYOUTER)
AbstractDiagramPresentationElement diagram = ...; // Diagram to layout
 diagram.open()
 //modify the environment options
 HierarchicLayouterOptionsGroup optionsGroup = (HierarchicLayouterOptionsGroup) Application.getInstance().getEnvironmentOptions().getGroup(HierarchicLayouterOptionsGroup.ID);
 String orientationBefore = optionsGroup.getOrientation();
 optionsGroup.setOrientation(OrientationOptions.LEFT_TO_RIGHT);

 Layouting.layout(diagram, Layouting.HIERARCHIC_DIAGRAM_LAYOUTER, optionsGroup);
 //set orientation back
 optionsGroup.setOrientation(orientationBefore);
Options for layouters:
 [`HIERARCHIC_DIAGRAM_LAYOUTER`](#HIERARCHIC_DIAGRAM_LAYOUTER) - [`HierarchicLayouterOptionsGroup`](../../../core/options/HierarchicLayouterOptionsGroup.html)
 [`STATE_DIAGRAM_LAYOUTER`](#STATE_DIAGRAM_LAYOUTER) - [`StateMachineLayouterOptionsGroup`](../../../core/options/StateMachineLayouterOptionsGroup.html)
 [`ACTIVITY_DIAGRAM_LAYOUTER`](#ACTIVITY_DIAGRAM_LAYOUTER) - [`ActivityLayouterOptionsGroup`](../../../core/options/ActivityLayouterOptionsGroup.html)
 [`BUSINESS_PROCESS_DIAGRAM_LAYOUTER`](#BUSINESS_PROCESS_DIAGRAM_LAYOUTER) - [`BusinessProcessLayouterOptionsGroup`](../../../core/options/BusinessProcessLayouterOptionsGroup.html)
 [`CLASS_DIAGRAM_LAYOUTER`](#CLASS_DIAGRAM_LAYOUTER) - [`ClassDiagramLayouterOptionsGroup`](../../../core/options/ClassDiagramLayouterOptionsGroup.html)
 [`ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER`](#ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER) - `OrderedHierarchicDiagramLayouterOptionsGroup`
 [`COMPOSITE_DIAGRAM_LAYOUTER`](#COMPOSITE_DIAGRAM_LAYOUTER) - [`CompositeLayouterOptionsGroup`](../../../core/options/CompositeLayouterOptionsGroup.html)
 [`TREE_DIAGRAM_LAYOUTER`](#TREE_DIAGRAM_LAYOUTER) - [`TreeLayouterOptionsGroup`](../../../core/options/TreeLayouterOptionsGroup.html)
 [`ORTHOGONAL_DIAGRAM_LAYOUTER`](#ORTHOGONAL_DIAGRAM_LAYOUTER) - [`OrthogonalLayouterOptionsGroup`](../../../core/options/OrthogonalLayouterOptionsGroup.html)
 [`GRID_DIAGRAM_LAYOUTER`](#GRID_DIAGRAM_LAYOUTER) - `GridLayouterOptionsGroup`
 [`CIRCULAR_DIAGRAM_LAYOUTER`](#CIRCULAR_DIAGRAM_LAYOUTER) - [`CircularLayouterOptionsGroup`](../../../core/options/CircularLayouterOptionsGroup.html)
 [`ORGANIC_DIAGRAM_LAYOUTER`](#ORGANIC_DIAGRAM_LAYOUTER) - [`OrganicLayouterOptionsGroup`](../../../core/options/OrganicLayouterOptionsGroup.html)

 [`ORTHOGONAL_DIAGRAM_ROUTER`](#ORTHOGONAL_DIAGRAM_ROUTER) - [`OrthogonalRouterOptionsGroup`](../../../core/options/OrthogonalRouterOptionsGroup.html)
 [`ORGANIC_DIAGRAM_ROUTER`](#ORGANIC_DIAGRAM_ROUTER) - [`OrganicRouterOptionsGroup`](../../../core/options/OrganicRouterOptionsGroup.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTIVITY_DIAGRAM_LAYOUTER](#ACTIVITY_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[BUSINESS_PROCESS_DIAGRAM_LAYOUTER](#BUSINESS_PROCESS_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CIRCULAR_DIAGRAM_LAYOUTER](#CIRCULAR_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CLASS_DIAGRAM_LAYOUTER](#CLASS_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[COMPOSITE_DIAGRAM_LAYOUTER](#COMPOSITE_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[GRID_DIAGRAM_LAYOUTER](#GRID_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[HIERARCHIC_DIAGRAM_LAYOUTER](#HIERARCHIC_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER](#ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ORGANIC_DIAGRAM_LAYOUTER](#ORGANIC_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ORGANIC_DIAGRAM_ROUTER](#ORGANIC_DIAGRAM_ROUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ORTHOGONAL_DIAGRAM_LAYOUTER](#ORTHOGONAL_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ORTHOGONAL_DIAGRAM_ROUTER](#ORTHOGONAL_DIAGRAM_ROUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STATE_DIAGRAM_LAYOUTER](#STATE_DIAGRAM_LAYOUTER)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TREE_DIAGRAM_LAYOUTER](#TREE_DIAGRAM_LAYOUTER)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Layouting](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[layout](#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram)`
Layout a diagram(or selected symbols, if any) using its default layouter using a new session or inside an already existing session.
`static boolean`
`[layout](#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) layouterID)`
Layout a diagram(or selected symbols, if any) using provided layouter and its default options using a new session or inside an already existing session.
`static boolean`
`[layout](#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup))([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) layouterID,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) optionsGroup)`
Layout a diagram(or selected symbols, if any) using provided layouter using a new session or inside an already existing session.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
HIERARCHIC_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) HIERARCHIC_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.HIERARCHIC_DIAGRAM_LAYOUTER)
STATE_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STATE_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.STATE_DIAGRAM_LAYOUTER)
ACTIVITY_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTIVITY_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ACTIVITY_DIAGRAM_LAYOUTER)
BUSINESS_PROCESS_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_PROCESS_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.BUSINESS_PROCESS_DIAGRAM_LAYOUTER)
CLASS_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CLASS_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.CLASS_DIAGRAM_LAYOUTER)
ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER)
COMPOSITE_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) COMPOSITE_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.COMPOSITE_DIAGRAM_LAYOUTER)
TREE_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TREE_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.TREE_DIAGRAM_LAYOUTER)
ORTHOGONAL_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ORTHOGONAL_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORTHOGONAL_DIAGRAM_LAYOUTER)
GRID_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GRID_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.GRID_DIAGRAM_LAYOUTER)
CIRCULAR_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CIRCULAR_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.CIRCULAR_DIAGRAM_LAYOUTER)
ORGANIC_DIAGRAM_LAYOUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ORGANIC_DIAGRAM_LAYOUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORGANIC_DIAGRAM_LAYOUTER)
ORTHOGONAL_DIAGRAM_ROUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ORTHOGONAL_DIAGRAM_ROUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORTHOGONAL_DIAGRAM_ROUTER)
ORGANIC_DIAGRAM_ROUTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ORGANIC_DIAGRAM_ROUTER
See Also:
[Constant Field Values](../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORGANIC_DIAGRAM_ROUTER)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Layouting
public Layouting()
 ============ METHOD DETAIL ========== 
Method Details
layout
public static boolean layout([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram)
Layout a diagram(or selected symbols, if any) using its default layouter using a new session or inside an already existing session.
Parameters:
`diagram` - the diagram to layout
Returns:
true if layout was a success, false otherwise
layout
public static boolean layout([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) layouterID)
Layout a diagram(or selected symbols, if any) using provided layouter and its default options using a new session or inside an already existing session.
Parameters:
`diagram` - the diagram to layout
`layouterID` - layouter to use
Returns:
true if layout was a success, false otherwise
layout
public static boolean layout([AbstractDiagramPresentationElement](../AbstractDiagramPresentationElement.html) diagram,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) layouterID,
 [AbstractDiagramLayouterOptionsGroup](../../../core/options/AbstractDiagramLayouterOptionsGroup.html) optionsGroup)
Layout a diagram(or selected symbols, if any) using provided layouter using a new session or inside an already existing session.
Parameters:
`diagram` - the diagram to layout
`layouterID` - layouter to use
`optionsGroup` - the layouters options
Returns:
true if layout was a success, false otherwise

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols.layout</a></div>
<h1 class="title" title="Class Layouting">Class Layouting</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.layout.Layouting</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Layouting</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Provides API for layouting diagrams.
 
<h4> Example 1: Layout a diagram using the default diagram layouter </h4>
<pre>
 AbstractDiagramPresentationElement diagram  = ...; // Diagram to layout
 diagram.open();
 Layouting.layout(diagram);
 </pre>
<h4> Example 2: Layout a diagram using any diagram layouter</h4>

 The available diagram layouter constant is provided in the <a href="Layouting.html" title="class in com.nomagic.magicdraw.uml.symbols.layout"><code>class</code></a>. e.g. <a href="#HIERARCHIC_DIAGRAM_LAYOUTER"><code>HIERARCHIC_DIAGRAM_LAYOUTER</code></a>
<pre>
 AbstractDiagramPresentationElement diagram  = ...; // Diagram to layout
 diagram.open()
 Layouting.layout(diagram, Layouting.HIERARCHIC_DIAGRAM_LAYOUTER);
 </pre>
<h4> Example 3: Layout a diagram using any diagram layouter, and appropriate options </h4>

 The available diagram layouter constant are provided in the <a href="Layouting.html" title="class in com.nomagic.magicdraw.uml.symbols.layout"><code>class</code></a>. e.g. <a href="#HIERARCHIC_DIAGRAM_LAYOUTER"><code>HIERARCHIC_DIAGRAM_LAYOUTER</code></a>
<pre>
 AbstractDiagramPresentationElement diagram  = ...; // Diagram to layout
 diagram.open()
 //modify the environment options
 HierarchicLayouterOptionsGroup optionsGroup = (HierarchicLayouterOptionsGroup) Application.getInstance().getEnvironmentOptions().getGroup(HierarchicLayouterOptionsGroup.ID);
 String orientationBefore = optionsGroup.getOrientation();
 optionsGroup.setOrientation(OrientationOptions.LEFT_TO_RIGHT);

 Layouting.layout(diagram, Layouting.HIERARCHIC_DIAGRAM_LAYOUTER, optionsGroup);
 //set orientation back
 optionsGroup.setOrientation(orientationBefore);
 </pre>
<p>
<p>
 Options for layouters:
 <pre>
 <a href="#HIERARCHIC_DIAGRAM_LAYOUTER"><code>HIERARCHIC_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/HierarchicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>HierarchicLayouterOptionsGroup</code></a>
 <a href="#STATE_DIAGRAM_LAYOUTER"><code>STATE_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/StateMachineLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>StateMachineLayouterOptionsGroup</code></a>
 <a href="#ACTIVITY_DIAGRAM_LAYOUTER"><code>ACTIVITY_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/ActivityLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>ActivityLayouterOptionsGroup</code></a>
 <a href="#BUSINESS_PROCESS_DIAGRAM_LAYOUTER"><code>BUSINESS_PROCESS_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/BusinessProcessLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>BusinessProcessLayouterOptionsGroup</code></a>
 <a href="#CLASS_DIAGRAM_LAYOUTER"><code>CLASS_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/ClassDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>ClassDiagramLayouterOptionsGroup</code></a>
 <a href="#ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER"><code>ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER</code></a> - <code>OrderedHierarchicDiagramLayouterOptionsGroup</code>
 <a href="#COMPOSITE_DIAGRAM_LAYOUTER"><code>COMPOSITE_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/CompositeLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>CompositeLayouterOptionsGroup</code></a>
 <a href="#TREE_DIAGRAM_LAYOUTER"><code>TREE_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/TreeLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>TreeLayouterOptionsGroup</code></a>
 <a href="#ORTHOGONAL_DIAGRAM_LAYOUTER"><code>ORTHOGONAL_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/OrthogonalLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>OrthogonalLayouterOptionsGroup</code></a>
 <a href="#GRID_DIAGRAM_LAYOUTER"><code>GRID_DIAGRAM_LAYOUTER</code></a> - <code>GridLayouterOptionsGroup</code>
 <a href="#CIRCULAR_DIAGRAM_LAYOUTER"><code>CIRCULAR_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/CircularLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>CircularLayouterOptionsGroup</code></a>
 <a href="#ORGANIC_DIAGRAM_LAYOUTER"><code>ORGANIC_DIAGRAM_LAYOUTER</code></a> - <a href="../../../core/options/OrganicLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>OrganicLayouterOptionsGroup</code></a>

 <a href="#ORTHOGONAL_DIAGRAM_ROUTER"><code>ORTHOGONAL_DIAGRAM_ROUTER</code></a> - <a href="../../../core/options/OrthogonalRouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>OrthogonalRouterOptionsGroup</code></a>
 <a href="#ORGANIC_DIAGRAM_ROUTER"><code>ORGANIC_DIAGRAM_ROUTER</code></a> - <a href="../../../core/options/OrganicRouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options"><code>OrganicRouterOptionsGroup</code></a>
 </pre></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTIVITY_DIAGRAM_LAYOUTER">ACTIVITY_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUSINESS_PROCESS_DIAGRAM_LAYOUTER">BUSINESS_PROCESS_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CIRCULAR_DIAGRAM_LAYOUTER">CIRCULAR_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CLASS_DIAGRAM_LAYOUTER">CLASS_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#COMPOSITE_DIAGRAM_LAYOUTER">COMPOSITE_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GRID_DIAGRAM_LAYOUTER">GRID_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#HIERARCHIC_DIAGRAM_LAYOUTER">HIERARCHIC_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER">ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ORGANIC_DIAGRAM_LAYOUTER">ORGANIC_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ORGANIC_DIAGRAM_ROUTER">ORGANIC_DIAGRAM_ROUTER</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ORTHOGONAL_DIAGRAM_LAYOUTER">ORTHOGONAL_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ORTHOGONAL_DIAGRAM_ROUTER">ORTHOGONAL_DIAGRAM_ROUTER</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STATE_DIAGRAM_LAYOUTER">STATE_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TREE_DIAGRAM_LAYOUTER">TREE_DIAGRAM_LAYOUTER</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Layouting</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">layout</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Layout a diagram(or selected symbols, if any) using its default layouter using a new session or inside an already existing session.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String)">layout</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> layouterID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Layout a diagram(or selected symbols, if any) using provided layouter and its default options using a new session or inside an already existing session.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">layout</a><wbr/>(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> layouterID,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> optionsGroup)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Layout a diagram(or selected symbols, if any) using provided layouter using a new session or inside an already existing session.</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="HIERARCHIC_DIAGRAM_LAYOUTER">
<h3>HIERARCHIC_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">HIERARCHIC_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.HIERARCHIC_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_DIAGRAM_LAYOUTER">
<h3>STATE_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STATE_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.STATE_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTIVITY_DIAGRAM_LAYOUTER">
<h3>ACTIVITY_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTIVITY_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ACTIVITY_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUSINESS_PROCESS_DIAGRAM_LAYOUTER">
<h3>BUSINESS_PROCESS_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUSINESS_PROCESS_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.BUSINESS_PROCESS_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CLASS_DIAGRAM_LAYOUTER">
<h3>CLASS_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CLASS_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.CLASS_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER">
<h3>ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORDERED_HIERARCHIC_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="COMPOSITE_DIAGRAM_LAYOUTER">
<h3>COMPOSITE_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">COMPOSITE_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.COMPOSITE_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TREE_DIAGRAM_LAYOUTER">
<h3>TREE_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TREE_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.TREE_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORTHOGONAL_DIAGRAM_LAYOUTER">
<h3>ORTHOGONAL_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ORTHOGONAL_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORTHOGONAL_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GRID_DIAGRAM_LAYOUTER">
<h3>GRID_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">GRID_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.GRID_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CIRCULAR_DIAGRAM_LAYOUTER">
<h3>CIRCULAR_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CIRCULAR_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.CIRCULAR_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORGANIC_DIAGRAM_LAYOUTER">
<h3>ORGANIC_DIAGRAM_LAYOUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ORGANIC_DIAGRAM_LAYOUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORGANIC_DIAGRAM_LAYOUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORTHOGONAL_DIAGRAM_ROUTER">
<h3>ORTHOGONAL_DIAGRAM_ROUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ORTHOGONAL_DIAGRAM_ROUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORTHOGONAL_DIAGRAM_ROUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ORGANIC_DIAGRAM_ROUTER">
<h3>ORGANIC_DIAGRAM_ROUTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ORGANIC_DIAGRAM_ROUTER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../../constant-values.html#com.nomagic.magicdraw.uml.symbols.layout.Layouting.ORGANIC_DIAGRAM_ROUTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>Layouting</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Layouting</span>()</div>
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
<section class="detail" id="layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>layout</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Layout a diagram(or selected symbols, if any) using its default layouter using a new session or inside an already existing session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram to layout</dd>
<dt>Returns:</dt>
<dd>true if layout was a success, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String)">
<h3>layout</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> layouterID)</span></div>
<div class="block">Layout a diagram(or selected symbols, if any) using provided layouter and its default options using a new session or inside an already existing session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram to layout</dd>
<dd><code>layouterID</code> - layouter to use</dd>
<dt>Returns:</dt>
<dd>true if layout was a success, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="layout(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.lang.String,com.nomagic.magicdraw.core.options.AbstractDiagramLayouterOptionsGroup)">
<h3>layout</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">layout</span><wbr/><span class="parameters">(<a href="../AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> layouterID,
 <a href="../../../core/options/AbstractDiagramLayouterOptionsGroup.html" title="class in com.nomagic.magicdraw.core.options">AbstractDiagramLayouterOptionsGroup</a> optionsGroup)</span></div>
<div class="block">Layout a diagram(or selected symbols, if any) using provided layouter using a new session or inside an already existing session.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagram</code> - the diagram to layout</dd>
<dd><code>layouterID</code> - layouter to use</dd>
<dd><code>optionsGroup</code> - the layouters options</dd>
<dt>Returns:</dt>
<dd>true if layout was a success, false otherwise</dd>
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
