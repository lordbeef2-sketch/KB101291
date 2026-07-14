# JAVA OPENAPI: Finder.ByTypeFinder (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/uml/Finder.ByTypeFinder.html
- source_path: `com/nomagic/magicdraw/uml/Finder.ByTypeFinder.html`
- source_sha256: `fb13c8a3e4609b6859d95692470784d2c2d208cf8c532e646c9acaac56fe2a5b`
- captured_utc: `2026-07-14T16:52:07.357816+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Finder.ByTypeFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.Finder.ByTypeFinder

Enclosing class:
[Finder](Finder.html)

public static final classFinder.ByTypeFinder
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Search for all elements by element type in the given root element(s) and direct children of root element(s)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project,java.lang.Class))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)`
Collects owned elements of the given project root models.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Collects owned elements of the given project root models.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D,boolean))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)`
Collects owned elements of the given project root models.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project,java.lang.Class,boolean))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type,
 boolean includeRoots)`
Collects owned elements of the given project root models.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)`
Collects owned elements of the given root elements of specified types.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Collects owned elements of the given root elements of specified types.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)`
Collects owned elements of the given root elements of specified types.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type,
 boolean includeRoot)`
Collects owned elements of the given root elements of specified types.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,java.lang.Class))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)`
Collects owned elements of the given root elements.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,java.lang.Class%5B%5D))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Collects owned elements of the given root elements.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,java.lang.Class%5B%5D,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)`
Collects owned elements of the given root elements.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,java.lang.Class,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type,
 boolean includeRoot)`
Collects owned elements of the given root elements.
`static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T>`
`[findInCollection](#findInCollection(java.util.Collection,java.lang.Class))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)`
Search by type for elements in the given Collection
`static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T>`
`[findInCollection](#findInCollection(java.util.Collection,java.lang.Class%5B%5D))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Search by type for elements in the given Collection
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)
Collects owned elements of the given root elements of specified types. Includes root itself.
Parameters:
`root` - root element
`type` - Element class types (Class.class, Package.class, Property.class and etc). Null means any type
Returns:
elements
findInCollection
public static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T> findInCollection([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)
Search by type for elements in the given Collection
Parameters:
`elements` - elements
`type` - element metatype
Returns:
found elements of given type
findInCollection
public static <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T> findInCollection([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Search by type for elements in the given Collection
Parameters:
`elements` - elements
`types` - element meta types
Returns:
found elements of given type
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type,
 boolean includeRoot)
Collects owned elements of the given root elements of specified types.
Parameters:
`root` - root element
`type` - Element class types (Class.class, Package.class, Property.class and etc). Null means any type
`includeRoot` - include root elements into search results
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)
Collects owned elements of the given project root models. Roots are also included.
Parameters:
`project` - project
`type` - Element class types (Class.class, Package.class, Property.class and etc). Null means any type
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type,
 boolean includeRoots)
Collects owned elements of the given project root models.
Parameters:
`project` - project
`type` - Element class types (Class.class, Package.class, Property.class and etc). Null means any type
`includeRoots` - include root elements of the project
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type)
Collects owned elements of the given root elements. Roots are also included.
Parameters:
`roots` - root elements
`type` - Element class types (Class.class, Package.class, Property.class and etc). Null means any type
Returns:
roots
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) type,
 boolean includeRoot)
Collects owned elements of the given root elements.
Parameters:
`roots` - root elements
`type` - Element class types (Class.class, Package.class, Property.class and etc). Null means any type
`includeRoot` - include root elements into search results
Returns:
roots
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Collects owned elements of the given root elements of specified types. Includes root itself.
Parameters:
`root` - root element
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)
Collects owned elements of the given root elements of specified types.
Parameters:
`root` - root element
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type
`includeRoot` - include root elements into search results
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Collects owned elements of the given project root models. Roots are also included.
Parameters:
`project` - project
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)
Collects owned elements of the given project root models.
Parameters:
`project` - project
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type
`includeRoots` - include root elements of the project
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Collects owned elements of the given root elements. Roots are also included.
Parameters:
`roots` - root elements
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type
Returns:
roots
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)
Collects owned elements of the given root elements.
Parameters:
`roots` - root elements
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type
`includeRoot` - include root elements into search results
Returns:
roots

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Finder.ByTypeFinder">Class Finder.ByTypeFinder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.Finder.ByTypeFinder</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="Finder.html" title="class in com.nomagic.magicdraw.uml">Finder</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">Finder.ByTypeFinder</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Search for all elements by element type in the given root element(s) and direct children of root element(s)</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project,java.lang.Class)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given project root models.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given project root models.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D,boolean)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given project root models.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project,java.lang.Class,boolean)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 boolean includeRoots)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given project root models.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements of specified types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements of specified types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements of specified types.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements of specified types.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.Class)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.Class%5B%5D)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.Class%5B%5D,boolean)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.Class,boolean)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects owned elements of the given root elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findInCollection(java.util.Collection,java.lang.Class)">findInCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search by type for elements in the given Collection</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#findInCollection(java.util.Collection,java.lang.Class%5B%5D)">findInCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Search by type for elements in the given Collection</div>
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
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</span></div>
<div class="block">Collects owned elements of the given root elements of specified types. Includes root itself.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dd><code>type</code> - Element class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findInCollection(java.util.Collection,java.lang.Class)">
<h3>findInCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt;</span> <span class="element-name">findInCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</span></div>
<div class="block">Search by type for elements in the given Collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>type</code> - element metatype</dd>
<dt>Returns:</dt>
<dd>found elements of given type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findInCollection(java.util.Collection,java.lang.Class[])">
<h3>findInCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt;</span> <span class="element-name">findInCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Search by type for elements in the given Collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - elements</dd>
<dd><code>types</code> - element meta types</dd>
<dt>Returns:</dt>
<dd>found elements of given type</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 boolean includeRoot)</span></div>
<div class="block">Collects owned elements of the given root elements of specified types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dd><code>type</code> - Element class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dd><code>includeRoot</code> - include root elements into search results</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.magicdraw.core.Project,java.lang.Class)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</span></div>
<div class="block">Collects owned elements of the given project root models. Roots are also included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>type</code> - Element class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.magicdraw.core.Project,java.lang.Class,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 boolean includeRoots)</span></div>
<div class="block">Collects owned elements of the given project root models.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>type</code> - Element class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dd><code>includeRoots</code> - include root elements of the project</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.Class)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type)</span></div>
<div class="block">Collects owned elements of the given root elements. Roots are also included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dd><code>type</code> - Element class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dt>Returns:</dt>
<dd>roots</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.Class,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> type,
 boolean includeRoot)</span></div>
<div class="block">Collects owned elements of the given root elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dd><code>type</code> - Element class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dd><code>includeRoot</code> - include root elements into search results</dd>
<dt>Returns:</dt>
<dd>roots</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[])">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Collects owned elements of the given root elements of specified types. Includes root itself.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</span></div>
<div class="block">Collects owned elements of the given root elements of specified types.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dd><code>includeRoot</code> - include root elements into search results</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.magicdraw.core.Project,java.lang.Class[])">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Collects owned elements of the given project root models. Roots are also included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.magicdraw.core.Project,java.lang.Class[],boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots)</span></div>
<div class="block">Collects owned elements of the given project root models.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dd><code>includeRoots</code> - include root elements of the project</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.Class[])">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Collects owned elements of the given root elements. Roots are also included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dt>Returns:</dt>
<dd>roots</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.Class[],boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</span></div>
<div class="block">Collects owned elements of the given root elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc). Null means any type</dd>
<dd><code>includeRoot</code> - include root elements into search results</dd>
<dt>Returns:</dt>
<dd>roots</dd>
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
