# JAVA OPENAPI: DiagramComparatorImpl (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/tests/common/comparators/DiagramComparatorImpl.html
- source_path: `com/nomagic/magicdraw/tests/common/comparators/DiagramComparatorImpl.html`
- source_sha256: `38794b0fd0abd100ba9ab3538963dd25e63fc4d6a4e744502566a241b4e4d4f0`
- captured_utc: `2026-07-14T16:55:39.109273+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.tests.common.comparators](package-summary.html)

## Class DiagramComparatorImpl

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.tests.common.comparators.DiagramComparatorImpl

All Implemented Interfaces:
`[DiagramComparator](DiagramComparator.html)`

@OpenApipublic classDiagramComparatorImpl
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
implements [DiagramComparator](DiagramComparator.html)

Implementation of diagram comparator.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected int`
`[BOUNDS_TOLERANCE](#BOUNDS_TOLERANCE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramComparatorImpl](#%3Cinit%3E())()`

`[DiagramComparatorImpl](#%3Cinit%3E(boolean))(boolean compareSymbolProperties)`

`[DiagramComparatorImpl](#%3Cinit%3E(int,boolean))(int boundsTolerance,
 boolean compareSymbolProperties)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[addChange](#addChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String))([PresentationElement](../../../uml/symbols/PresentationElement.html) original,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) modified,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) info)`

`protected static void`
`[addMarker](#addMarker(java.util.Map,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.tests.common.comparators.DiffMarker))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.tests.common.comparators.DiffMarker>> map,
 [AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 com.nomagic.magicdraw.tests.common.comparators.DiffMarker marker)`

`void`
`[clear](#clear())()`

`boolean`
`[compareDiagrams](#compareDiagrams(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))([AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagrams1,
 [AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagrams2)`
Check if two diagrams are equals by comparing their graphical representations.
`boolean`
`[compareDiagrams](#compareDiagrams(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams2)`
Compare diagrams in two parallel collections.
`boolean`
`[compareRecursively](#compareRecursively(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../../uml/symbols/PresentationElement.html) p1,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) p2)`

`protected boolean`
`[compareSymbols](#compareSymbols(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../../uml/symbols/PresentationElement.html) pe1,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) pe2)`
Check if two presentation elements bounds are equals.
`protected com.nomagic.magicdraw.tests.common.comparators.DiffMarker`
`[createMarker](#createMarker(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Color,boolean))([PresentationElement](../../../uml/symbols/PresentationElement.html) changed,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) original,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color,
 boolean useNames)`
Forms shape which draw around element.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../../../uml/symbols/PresentationElement.html)>`
`[getAdded](#getAdded())()`
Presentation elements which are added to second compared diagram and do not exist on the
 first compared diagram.
`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../../../uml/symbols/PresentationElement.html),com.nomagic.magicdraw.tests.common.comparators.DiagramComparatorImpl.Diff>`
`[getChanged](#getChanged())()`
Changed presentation elements and their difference information found in compared diagrams.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getDiffInfo](#getDiffInfo())()`
Formats textual information about differences found in compared diagrams.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getPath](#getPath(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../../uml/symbols/PresentationElement.html) element)`
Creates "kind of qualified name" for presentation element in diagram.
`protected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>`
`[getPointsOfShape](#getPointsOfShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,int))([PathElement](../../../uml/symbols/paths/PathElement.html) element,
 int delta)`
Forms a points around the elements by making a poly line.
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../../../uml/symbols/PresentationElement.html)>`
`[getRemoved](#getRemoved())()`
Presentation elements which exist on first compared diagrams and do not exist on the second
 compared diagram.
`protected boolean`
`[isNotCopyBoundsEquals](#isNotCopyBoundsEquals(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../../../uml/symbols/PresentationElement.html) a1,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) a2)`

`protected void`
`[saveDiffToImage](#saveDiffToImage(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.io.File))([AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`

`void`
`[saveDiffToImageFiles](#saveDiffToImageFiles(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Creates graphical differences on compared diagrams and save it to graphical file.
`protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
BOUNDS_TOLERANCE
protected int BOUNDS_TOLERANCE
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramComparatorImpl
@OpenApipublic DiagramComparatorImpl(int boundsTolerance,
 boolean compareSymbolProperties)
Constructor.
Parameters:
`boundsTolerance` - tolerance of bounds difference.
`compareSymbolProperties` - if compare symbol properties.
DiagramComparatorImpl
public DiagramComparatorImpl()
DiagramComparatorImpl
public DiagramComparatorImpl(boolean compareSymbolProperties)
 ============ METHOD DETAIL ========== 
Method Details
clear
public void clear()
compareRecursively
public boolean compareRecursively([PresentationElement](../../../uml/symbols/PresentationElement.html) p1,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) p2)
isNotCopyBoundsEquals
protected boolean isNotCopyBoundsEquals([PresentationElement](../../../uml/symbols/PresentationElement.html) a1,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) a2)
compareSymbols
protected boolean compareSymbols([PresentationElement](../../../uml/symbols/PresentationElement.html) pe1,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) pe2)
Check if two presentation elements bounds are equals. Two presentations elements are equals
 if their bounds difference is not more than 1 pixel.
Parameters:
`pe1` - first presentation element to compare.
`pe2` - second presentation element to compare.
Returns:
true if compared presentation elements are equals, false otherwise
toString
protected [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) r)
compareDiagrams
public boolean compareDiagrams([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html)> diagrams2)
Compare diagrams in two parallel collections.
Specified by:
`[compareDiagrams](DiagramComparator.html#compareDiagrams(java.util.Collection,java.util.Collection))` in interface `[DiagramComparator](DiagramComparator.html)`
Parameters:
`diagrams1` - first diagram to compare.
`diagrams2` - second diagram to compare.
Returns:
true if diagrams in both collections are equals, false otherwise.
compareDiagrams
public boolean compareDiagrams([AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagrams1,
 [AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagrams2)
Check if two diagrams are equals by comparing their graphical representations.
Parameters:
`diagrams1` - first diagram to compare.
`diagrams2` - second diagram to compare.
Returns:
true if compared diagrams graphical presentation is equals.
getDiffInfo
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getDiffInfo()
Formats textual information about differences found in compared diagrams. Formatted text
 contains information about new, removed, and changed symbols in compared diagrams.
Specified by:
`[getDiffInfo](DiagramComparator.html#getDiffInfo())` in interface `[DiagramComparator](DiagramComparator.html)`
Returns:
String information about differences found in compared diagrams or empty String if no differences found.
saveDiffToImage
protected void saveDiffToImage([AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
getPath
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getPath([PresentationElement](../../../uml/symbols/PresentationElement.html) element)
Creates "kind of qualified name" for presentation element in diagram. Such "qualified name"
 starts with diagram name and all nested presentation elements where given element is nested.
Parameters:
`element` - presentation element to create "qualified name" for.
Returns:
String formed from elements parent names separated by semicolon ':'.
addChange
protected void addChange([PresentationElement](../../../uml/symbols/PresentationElement.html) original,
 [PresentationElement](../../../uml/symbols/PresentationElement.html) modified,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) info)
getAdded
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../../../uml/symbols/PresentationElement.html)> getAdded()
Presentation elements which are added to second compared diagram and do not exist on the
 first compared diagram.
Returns:
Set of presentation elements which exist only on second compared diagram.
getRemoved
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[PresentationElement](../../../uml/symbols/PresentationElement.html)> getRemoved()
Presentation elements which exist on first compared diagrams and do not exist on the second
 compared diagram.
Returns:
Set of presentation elements which exist only on first compared diagrams.
getChanged
public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[PresentationElement](../../../uml/symbols/PresentationElement.html),com.nomagic.magicdraw.tests.common.comparators.DiagramComparatorImpl.Diff> getChanged()
Changed presentation elements and their difference information found in compared diagrams.
Returns:
Map with changed presentation elements as keys and their differences specified as
 Diff values.
addMarker
protected static void addMarker([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html),[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<com.nomagic.magicdraw.tests.common.comparators.DiffMarker>> map,
 [AbstractDiagramPresentationElement](../../../uml/symbols/AbstractDiagramPresentationElement.html) diagram,
 com.nomagic.magicdraw.tests.common.comparators.DiffMarker marker)
saveDiffToImageFiles
public void saveDiffToImageFiles([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Creates graphical differences on compared diagrams and save it to graphical file. Graphical
 differences are presented as rectangles on diagrams.
Specified by:
`[saveDiffToImageFiles](DiagramComparator.html#saveDiffToImageFiles(java.io.File))` in interface `[DiagramComparator](DiagramComparator.html)`
Parameters:
`file` - graphical file to save compared diagram graphical differences to.
createMarker
protected com.nomagic.magicdraw.tests.common.comparators.DiffMarker createMarker([PresentationElement](../../../uml/symbols/PresentationElement.html) changed,
 @CheckForNull
 [PresentationElement](../../../uml/symbols/PresentationElement.html) original,
 [Color](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html) color,
 boolean useNames)
Forms shape which draw around element.
Parameters:
`changed` - changes element
`original` - original element
`color` - of rectangle.
`useNames` - true if needed names for shape, false otherwise.
Returns:
DiffMarker storing shape, text and color.
getPointsOfShape
@CheckForNullprotected [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> getPointsOfShape([PathElement](../../../uml/symbols/paths/PathElement.html) element,
 int delta)
Forms a points around the elements by making a poly line.
Parameters:
`element` - PathElement.
`delta` - pixels from element till formed polyline around element.
Returns:
List of points going around element.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.tests.common.comparators</a></div>
<h1 class="title" title="Class DiagramComparatorImpl">Class DiagramComparatorImpl</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.tests.common.comparators.DiagramComparatorImpl</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramComparatorImpl</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a></span></div>
<div class="block">Implementation of diagram comparator.</div>
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
<div class="col-first even-row-color"><code>protected int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#BOUNDS_TOLERANCE">BOUNDS_TOLERANCE</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DiagramComparatorImpl</a>()</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean)">DiagramComparatorImpl</a><wbr/>(boolean compareSymbolProperties)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int,boolean)">DiagramComparatorImpl</a><wbr/>(int boundsTolerance,
 boolean compareSymbolProperties)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">addChange</a><wbr/>(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> original,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> modified,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addMarker(java.util.Map,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.tests.common.comparators.DiffMarker)">addMarker</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.tests.common.comparators.DiffMarker&gt;&gt; map,
 <a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 com.nomagic.magicdraw.tests.common.comparators.DiffMarker marker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareDiagrams(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">compareDiagrams</a><wbr/>(<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagrams1,
 <a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagrams2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if two diagrams are equals by comparing their graphical representations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareDiagrams(java.util.Collection,java.util.Collection)">compareDiagrams</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Compare diagrams in two parallel collections.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareRecursively(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">compareRecursively</a><wbr/>(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> p1,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> p2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareSymbols(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">compareSymbols</a><wbr/>(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe1,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if two presentation elements bounds are equals.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected com.nomagic.magicdraw.tests.common.comparators.DiffMarker</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createMarker(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Color,boolean)">createMarker</a><wbr/>(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> changed,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color,
 boolean useNames)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Forms shape which draw around element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAdded()">getAdded</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Presentation elements which are added to second compared diagram and do not exist on the
 first compared diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/>com.nomagic.magicdraw.tests.common.comparators.DiagramComparatorImpl.Diff&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChanged()">getChanged</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Changed presentation elements and their difference information found in compared diagrams.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDiffInfo()">getDiffInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Formats textual information about differences found in compared diagrams.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPath(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getPath</a><wbr/>(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates "kind of qualified name" for presentation element in diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPointsOfShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,int)">getPointsOfShape</a><wbr/>(<a href="../../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 int delta)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Forms a points around the elements by making a poly line.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRemoved()">getRemoved</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Presentation elements which exist on first compared diagrams and do not exist on the second
 compared diagram.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNotCopyBoundsEquals(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">isNotCopyBoundsEquals</a><wbr/>(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> a1,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> a2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveDiffToImage(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.io.File)">saveDiffToImage</a><wbr/>(<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#saveDiffToImageFiles(java.io.File)">saveDiffToImageFiles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates graphical differences on compared diagrams and save it to graphical file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(java.awt.Rectangle)">toString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="BOUNDS_TOLERANCE">
<h3>BOUNDS_TOLERANCE</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">BOUNDS_TOLERANCE</span></div>
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
<section class="detail" id="&lt;init&gt;(int,boolean)">
<h3>DiagramComparatorImpl</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">DiagramComparatorImpl</span><wbr/><span class="parameters">(int boundsTolerance,
 boolean compareSymbolProperties)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>boundsTolerance</code> - tolerance of bounds difference.</dd>
<dd><code>compareSymbolProperties</code> - if compare symbol properties.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>DiagramComparatorImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramComparatorImpl</span>()</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean)">
<h3>DiagramComparatorImpl</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DiagramComparatorImpl</span><wbr/><span class="parameters">(boolean compareSymbolProperties)</span></div>
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
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
</section>
</li>
<li>
<section class="detail" id="compareRecursively(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>compareRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">compareRecursively</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> p1,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> p2)</span></div>
</section>
</li>
<li>
<section class="detail" id="isNotCopyBoundsEquals(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>isNotCopyBoundsEquals</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isNotCopyBoundsEquals</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> a1,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> a2)</span></div>
</section>
</li>
<li>
<section class="detail" id="compareSymbols(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>compareSymbols</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">compareSymbols</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe1,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> pe2)</span></div>
<div class="block">Check if two presentation elements bounds are equals. Two presentations elements are equals
 if their bounds difference is not more than 1 pixel.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pe1</code> - first presentation element to compare.</dd>
<dd><code>pe2</code> - second presentation element to compare.</dd>
<dt>Returns:</dt>
<dd>true if compared presentation elements are equals, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString(java.awt.Rectangle)">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> r)</span></div>
</section>
</li>
<li>
<section class="detail" id="compareDiagrams(java.util.Collection,java.util.Collection)">
<h3>compareDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">compareDiagrams</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>&gt; diagrams2)</span></div>
<div class="block">Compare diagrams in two parallel collections.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="DiagramComparator.html#compareDiagrams(java.util.Collection,java.util.Collection)">compareDiagrams</a></code> in interface <code><a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>diagrams1</code> - first diagram to compare.</dd>
<dd><code>diagrams2</code> - second diagram to compare.</dd>
<dt>Returns:</dt>
<dd>true if diagrams in both collections are equals, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareDiagrams(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>compareDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">compareDiagrams</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagrams1,
 <a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagrams2)</span></div>
<div class="block">Check if two diagrams are equals by comparing their graphical representations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>diagrams1</code> - first diagram to compare.</dd>
<dd><code>diagrams2</code> - second diagram to compare.</dd>
<dt>Returns:</dt>
<dd>true if compared diagrams graphical presentation is equals.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDiffInfo()">
<h3>getDiffInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDiffInfo</span>()</div>
<div class="block">Formats textual information about differences found in compared diagrams. Formatted text
 contains information about new, removed, and changed symbols in compared diagrams.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="DiagramComparator.html#getDiffInfo()">getDiffInfo</a></code> in interface <code><a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a></code></dd>
<dt>Returns:</dt>
<dd>String information about differences found in compared diagrams or empty String if no differences found.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="saveDiffToImage(com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,java.io.File)">
<h3>saveDiffToImage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">saveDiffToImage</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPath(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getPath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPath</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> element)</span></div>
<div class="block">Creates "kind of qualified name" for presentation element in diagram. Such "qualified name"
 starts with diagram name and all nested presentation elements where given element is nested.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - presentation element to create "qualified name" for.</dd>
<dt>Returns:</dt>
<dd>String formed from elements parent names separated by semicolon ':'.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addChange(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.lang.String)">
<h3>addChange</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">addChange</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> original,
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> modified,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> info)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAdded()">
<h3>getAdded</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getAdded</span>()</div>
<div class="block">Presentation elements which are added to second compared diagram and do not exist on the
 first compared diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Set of presentation elements which exist only on second compared diagram.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRemoved()">
<h3>getRemoved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>&gt;</span> <span class="element-name">getRemoved</span>()</div>
<div class="block">Presentation elements which exist on first compared diagrams and do not exist on the second
 compared diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Set of presentation elements which exist only on first compared diagrams.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChanged()">
<h3>getChanged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a>,<wbr/>com.nomagic.magicdraw.tests.common.comparators.DiagramComparatorImpl.Diff&gt;</span> <span class="element-name">getChanged</span>()</div>
<div class="block">Changed presentation elements and their difference information found in compared diagrams.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Map with changed presentation elements as keys and their differences specified as
 Diff values.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addMarker(java.util.Map,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement,com.nomagic.magicdraw.tests.common.comparators.DiffMarker)">
<h3>addMarker</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">void</span> <span class="element-name">addMarker</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;com.nomagic.magicdraw.tests.common.comparators.DiffMarker&gt;&gt; map,
 <a href="../../../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram,
 com.nomagic.magicdraw.tests.common.comparators.DiffMarker marker)</span></div>
</section>
</li>
<li>
<section class="detail" id="saveDiffToImageFiles(java.io.File)">
<h3>saveDiffToImageFiles</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">saveDiffToImageFiles</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Creates graphical differences on compared diagrams and save it to graphical file. Graphical
 differences are presented as rectangles on diagrams.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="DiagramComparator.html#saveDiffToImageFiles(java.io.File)">saveDiffToImageFiles</a></code> in interface <code><a href="DiagramComparator.html" title="interface in com.nomagic.magicdraw.tests.common.comparators">DiagramComparator</a></code></dd>
<dt>Parameters:</dt>
<dd><code>file</code> - graphical file to save compared diagram graphical differences to.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMarker(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.uml.symbols.PresentationElement,java.awt.Color,boolean)">
<h3>createMarker</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">com.nomagic.magicdraw.tests.common.comparators.DiffMarker</span> <span class="element-name">createMarker</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> changed,
 @CheckForNull
 <a href="../../../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> original,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color,
 boolean useNames)</span></div>
<div class="block">Forms shape which draw around element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>changed</code> - changes element</dd>
<dd><code>original</code> - original element</dd>
<dd><code>color</code> - of rectangle.</dd>
<dd><code>useNames</code> - true if needed names for shape, false otherwise.</dd>
<dt>Returns:</dt>
<dd>DiffMarker storing shape, text and color.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPointsOfShape(com.nomagic.magicdraw.uml.symbols.paths.PathElement,int)">
<h3>getPointsOfShape</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">getPointsOfShape</span><wbr/><span class="parameters">(<a href="../../../uml/symbols/paths/PathElement.html" title="class in com.nomagic.magicdraw.uml.symbols.paths">PathElement</a> element,
 int delta)</span></div>
<div class="block">Forms a points around the elements by making a poly line.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - PathElement.</dd>
<dd><code>delta</code> - pixels from element till formed polyline around element.</dd>
<dt>Returns:</dt>
<dd>List of points going around element.</dd>
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
