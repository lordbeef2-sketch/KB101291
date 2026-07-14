# JAVA OPENAPI: Finder (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/Finder.html
- source_path: `com/nomagic/magicdraw/uml/Finder.html`
- source_sha256: `c9dfaa0124ad4be8c2416458b0445a37625ef3c579a1d179e5bd6d9bc66e7810`
- captured_utc: `2026-07-14T16:55:53.653438+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Finder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.uml2.finder.BaseFinder
com.nomagic.magicdraw.uml.Finder

@OpenApiAllpublic classFinder
extends com.nomagic.uml2.finder.BaseFinder
This utility class should be used for searching element(s) in the model using various criteria.
 Search criteria are organized in several inner finders.

 

 
To retrieve Element metatype, use [`BaseElement.getClassType()`](BaseElement.html#getClassType())
 
Use [`ClassTypes.getSubtypesArray(Class)`](../../uml2/ext/jmi/reflect/ClassTypes.html#getSubtypesArray(java.lang.Class)) to collect all subtypes as array of given metatype
 

 Use methods below to get instances of these finders:
 [`byName()`](#byName())
[`byNameRecursively()`](#byNameRecursively())
[`byNameAll()`](#byNameAll())
[`byNameAllRecursively()`](#byNameAllRecursively())
[`byQualifiedName()`](#byQualifiedName())
[`byHyperlink()`](#byHyperlink())
[`byType()`](#byType())
[`byTypeRecursively()`](#byTypeRecursively())
[`byScope()`](#byScope())

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[Finder.ByHyperlinkFinder](Finder.ByHyperlinkFinder.html)`
Search element by element hyperlink.
`static final class`
`[Finder.ByNameAllFinder](Finder.ByNameAllFinder.html)`
Search for all elements by simple name among the given root element(s) and direct children of root element(s)
`static final class`
`[Finder.ByNameAllRecursivelyFinder](Finder.ByNameAllRecursivelyFinder.html)`
Search for all elements by simple name among the given root element(s) and all(direct and indirect) children of root element(s)
`static final class`
`[Finder.ByNameFinder](Finder.ByNameFinder.html)`
Search for any first element by simple name among the given root element(s) and direct children of root element(s)
`static final class`
`[Finder.ByNameRecursivelyFinder](Finder.ByNameRecursivelyFinder.html)`
Search for any first element by simple name among the given root element(s) and all(direct and indirect) children of root element(s)
`static final class`
`[Finder.ByQualifiedNameFinder](Finder.ByQualifiedNameFinder.html)`
Search for elements by qualified name
`static final class`
`[Finder.ByScopeFinder](Finder.ByScopeFinder.html)`
Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)
`static final class`
`[Finder.ByTypeFinder](Finder.ByTypeFinder.html)`
Search for all elements by element type in the given root element(s) and direct children of root element(s)
`static final class`
`[Finder.ByTypeRecursivelyFinder](Finder.ByTypeRecursivelyFinder.html)`
Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Finder](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Finder.ByHyperlinkFinder](Finder.ByHyperlinkFinder.html)`
`[byHyperlink](#byHyperlink())()`
Search for elements by element hyperlink.
`static [Finder.ByNameFinder](Finder.ByNameFinder.html)`
`[byName](#byName())()`
Search for any first element by simple name among the given root element(s) and direct children of root element(s)
`static [Finder.ByNameAllFinder](Finder.ByNameAllFinder.html)`
`[byNameAll](#byNameAll())()`
Search for all elements by simple name among the given root element(s) and direct children of root element(s)
`static [Finder.ByNameAllRecursivelyFinder](Finder.ByNameAllRecursivelyFinder.html)`
`[byNameAllRecursively](#byNameAllRecursively())()`
Search for all elements by simple name among the given root element(s) and all(direct and indirect) children of root element(s)
`static [Finder.ByNameRecursivelyFinder](Finder.ByNameRecursivelyFinder.html)`
`[byNameRecursively](#byNameRecursively())()`
Search for any first element by simple name among the given root element(s) and all(direct and indirect) children of root element(s)
`static [Finder.ByQualifiedNameFinder](Finder.ByQualifiedNameFinder.html)`
`[byQualifiedName](#byQualifiedName())()`
Search for elements by qualified name
`static [Finder.ByScopeFinder](Finder.ByScopeFinder.html)`
`[byScope](#byScope())()`
Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)
`static [Finder.ByTypeFinder](Finder.ByTypeFinder.html)`
`[byType](#byType())()`
Search for all elements by element type in the given root element(s) and direct children of root element(s)
`static [Finder.ByTypeRecursivelyFinder](Finder.ByTypeRecursivelyFinder.html)`
`[byTypeRecursively](#byTypeRecursively())()`
Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)
Methods inherited from class com.nomagic.uml2.finder.BaseFinder
`hasName, toRoots, toRoots, toSet, toTypes`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Finder
public Finder()
 ============ METHOD DETAIL ========== 
Method Details
byName
public static [Finder.ByNameFinder](Finder.ByNameFinder.html) byName()
Search for any first element by simple name among the given root element(s) and direct children of root element(s)
Returns:
finder by element name
byNameAll
public static [Finder.ByNameAllFinder](Finder.ByNameAllFinder.html) byNameAll()
Search for all elements by simple name among the given root element(s) and direct children of root element(s)
Returns:
finder of all elements by name
byNameRecursively
public static [Finder.ByNameRecursivelyFinder](Finder.ByNameRecursivelyFinder.html) byNameRecursively()
Search for any first element by simple name among the given root element(s) and all(direct and indirect) children of root element(s)
Returns:
finder by element name recursively
byNameAllRecursively
public static [Finder.ByNameAllRecursivelyFinder](Finder.ByNameAllRecursivelyFinder.html) byNameAllRecursively()
Search for all elements by simple name among the given root element(s) and all(direct and indirect) children of root element(s)
Returns:
finder of all elements recursively
byQualifiedName
public static [Finder.ByQualifiedNameFinder](Finder.ByQualifiedNameFinder.html) byQualifiedName()
Search for elements by qualified name
Returns:
finder by qualified name
byHyperlink
public static [Finder.ByHyperlinkFinder](Finder.ByHyperlinkFinder.html) byHyperlink()
Search for elements by element hyperlink.
Returns:
finder by qualified name
byType
public static [Finder.ByTypeFinder](Finder.ByTypeFinder.html) byType()
Search for all elements by element type in the given root element(s) and direct children of root element(s)
Returns:
finder by element meta type
byTypeRecursively
public static [Finder.ByTypeRecursivelyFinder](Finder.ByTypeRecursivelyFinder.html) byTypeRecursively()
Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)
Returns:
finder by element metatype recursively
byScope
public static [Finder.ByScopeFinder](Finder.ByScopeFinder.html) byScope()
Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)
Returns:
finder by scope

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Finder">Class Finder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.uml2.finder.BaseFinder
<div class="inheritance">com.nomagic.magicdraw.uml.Finder</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Finder</span>
<span class="extends-implements">extends com.nomagic.uml2.finder.BaseFinder</span></div>
<div class="block">This utility class should be used for searching element(s) in the model using various criteria.
 Search criteria are organized in several inner finders.

 <br/>
<br/>To retrieve Element metatype, use <a href="BaseElement.html#getClassType()"><code>BaseElement.getClassType()</code></a>
<br/>Use <a href="../../uml2/ext/jmi/reflect/ClassTypes.html#getSubtypesArray(java.lang.Class)"><code>ClassTypes.getSubtypesArray(Class)</code></a> to collect all subtypes as array of given metatype
 <br/>
 Use methods below to get instances of these finders:
 <ul>
<li><a href="#byName()"><code>byName()</code></a></li>
<li><a href="#byNameRecursively()"><code>byNameRecursively()</code></a></li>
<li><a href="#byNameAll()"><code>byNameAll()</code></a></li>
<li><a href="#byNameAllRecursively()"><code>byNameAllRecursively()</code></a></li>
<li><a href="#byQualifiedName()"><code>byQualifiedName()</code></a></li>
<li><a href="#byHyperlink()"><code>byHyperlink()</code></a></li>
<li><a href="#byType()"><code>byType()</code></a></li>
<li><a href="#byTypeRecursively()"><code>byTypeRecursively()</code></a></li>
<li><a href="#byScope()"><code>byScope()</code></a></li>
</ul></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Finder.ByHyperlinkFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByHyperlinkFinder</a></code></div>
<div class="col-last even-row-color">
<div class="block">Search element by element hyperlink.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Finder.ByNameAllFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameAllFinder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Search for all elements by simple name among the given root element(s) and direct children of root element(s)</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Finder.ByNameAllRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameAllRecursivelyFinder</a></code></div>
<div class="col-last even-row-color">
<div class="block">Search for all elements by simple name among the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Finder.ByNameFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameFinder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Search for any first element by simple name among the given root element(s) and direct children of root element(s)</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Finder.ByNameRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameRecursivelyFinder</a></code></div>
<div class="col-last even-row-color">
<div class="block">Search for any first element by simple name among the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Finder.ByQualifiedNameFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByQualifiedNameFinder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Search for elements by qualified name</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Finder.ByScopeFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByScopeFinder</a></code></div>
<div class="col-last even-row-color">
<div class="block">Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="Finder.ByTypeFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByTypeFinder</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Search for all elements by element type in the given root element(s) and direct children of root element(s)</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="Finder.ByTypeRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByTypeRecursivelyFinder</a></code></div>
<div class="col-last even-row-color">
<div class="block">Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Finder</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByHyperlinkFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByHyperlinkFinder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byHyperlink()">byHyperlink</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for elements by element hyperlink.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByNameFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameFinder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byName()">byName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for any first element by simple name among the given root element(s) and direct children of root element(s)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByNameAllFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameAllFinder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byNameAll()">byNameAll</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for all elements by simple name among the given root element(s) and direct children of root element(s)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByNameAllRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameAllRecursivelyFinder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byNameAllRecursively()">byNameAllRecursively</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for all elements by simple name among the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByNameRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameRecursivelyFinder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byNameRecursively()">byNameRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for any first element by simple name among the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByQualifiedNameFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByQualifiedNameFinder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byQualifiedName()">byQualifiedName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for elements by qualified name</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByScopeFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByScopeFinder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byScope()">byScope</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByTypeFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByTypeFinder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byType()">byType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for all elements by element type in the given root element(s) and direct children of root element(s)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="Finder.ByTypeRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByTypeRecursivelyFinder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#byTypeRecursively()">byTypeRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.uml2.finder.BaseFinder">Methods inherited from class com.nomagic.uml2.finder.BaseFinder</h3>
<code>hasName, toRoots, toRoots, toSet, toTypes</code></div>
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
<h3>Finder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Finder</span>()</div>
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
<section class="detail" id="byName()">
<h3>byName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByNameFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameFinder</a></span> <span class="element-name">byName</span>()</div>
<div class="block">Search for any first element by simple name among the given root element(s) and direct children of root element(s)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder by element name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byNameAll()">
<h3>byNameAll</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByNameAllFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameAllFinder</a></span> <span class="element-name">byNameAll</span>()</div>
<div class="block">Search for all elements by simple name among the given root element(s) and direct children of root element(s)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder of all elements by name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byNameRecursively()">
<h3>byNameRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByNameRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameRecursivelyFinder</a></span> <span class="element-name">byNameRecursively</span>()</div>
<div class="block">Search for any first element by simple name among the given root element(s) and all(direct and indirect) children of root element(s)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder by element name recursively</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byNameAllRecursively()">
<h3>byNameAllRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByNameAllRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByNameAllRecursivelyFinder</a></span> <span class="element-name">byNameAllRecursively</span>()</div>
<div class="block">Search for all elements by simple name among the given root element(s) and all(direct and indirect) children of root element(s)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder of all elements recursively</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byQualifiedName()">
<h3>byQualifiedName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByQualifiedNameFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByQualifiedNameFinder</a></span> <span class="element-name">byQualifiedName</span>()</div>
<div class="block">Search for elements by qualified name</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder by qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byHyperlink()">
<h3>byHyperlink</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByHyperlinkFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByHyperlinkFinder</a></span> <span class="element-name">byHyperlink</span>()</div>
<div class="block">Search for elements by element hyperlink.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder by qualified name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byType()">
<h3>byType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByTypeFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByTypeFinder</a></span> <span class="element-name">byType</span>()</div>
<div class="block">Search for all elements by element type in the given root element(s) and direct children of root element(s)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder by element meta type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byTypeRecursively()">
<h3>byTypeRecursively</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByTypeRecursivelyFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByTypeRecursivelyFinder</a></span> <span class="element-name">byTypeRecursively</span>()</div>
<div class="block">Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder by element metatype recursively</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="byScope()">
<h3>byScope</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="Finder.ByScopeFinder.html" title="class in com.nomagic.magicdraw.uml">Finder.ByScopeFinder</a></span> <span class="element-name">byScope</span>()</div>
<div class="block">Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>finder by scope</dd>
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
