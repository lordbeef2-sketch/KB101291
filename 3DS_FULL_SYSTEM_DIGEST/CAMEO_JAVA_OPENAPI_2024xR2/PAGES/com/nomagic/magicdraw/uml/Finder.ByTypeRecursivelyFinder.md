# JAVA OPENAPI: Finder.ByTypeRecursivelyFinder (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/Finder.ByTypeRecursivelyFinder.html
- source_path: `com/nomagic/magicdraw/uml/Finder.ByTypeRecursivelyFinder.html`
- source_sha256: `93c072b3f3dbe9f269ed2aece3d6249e516a4917af076af2ddb10fd4ba000733`
- captured_utc: `2026-07-14T16:55:54.003443+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Finder.ByTypeRecursivelyFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.Finder.ByTypeRecursivelyFinder

Enclosing class:
[Finder](Finder.html)

public static final classFinder.ByTypeRecursivelyFinder
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Collect all elements of given specific type (not super class or interface) from the project.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D,boolean))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)`
Collect all elements of given specific type (not super class or interface) from the project
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Collect all elements of given specific type (not super class or interface) from the root element.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)`
Collect all elements of given specific type (not super class or interface) from the root element.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean,boolean,com.nomagic.task.ProgressStatus))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot,
 boolean includeAdditionalContents,
 [ProgressStatus](../../task/ProgressStatus.html) monitor)`
Collect all elements of given specific type (not super class or interface) from the root element.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,java.lang.Class%5B%5D,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)`
Collect all elements of given specific type (not super class or interface) from the root element.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,java.lang.Class%5B%5D,boolean,boolean,com.nomagic.task.ProgressStatus))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots,
 boolean includeAdditionalContents,
 [ProgressStatus](../../task/ProgressStatus.html) monitor)`
Collect all elements of given specific type (not super class or interface) from the root element.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Returns iterator which contains elements of given specific type (not super class or interface).
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D,boolean))([Project](../core/Project.html) project,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)`
Returns iterator which contains elements of given specific type (not super class or interface).
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Returns iterator which contains elements of given specific type (not super class or interface).
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)`
Returns iterator which contains elements of given specific type (not super class or interface).
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(java.util.Collection,java.lang.Class%5B%5D))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)`
Returns iterator which contains elements of given specific type (not super class or interface).
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(java.util.Collection,java.lang.Class%5B%5D,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)`
Returns iterator which contains elements of given specific type (not super class or interface).
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element.
Parameters:
`root` - root element.
`types` - element type. Null means any element
Returns:
iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)
Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element.
Parameters:
`root` - root element.
`types` - element type. Null means any element
`includeRoot` - include root into result
Returns:
iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element. Roots are included also.
Parameters:
`roots` - root elements.
`types` - element type. Null means any element
Returns:
iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)
Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element.
Parameters:
`roots` - root elements.
`types` - element type. Null means any element
`includeRoot` - include root elements into result
Returns:
iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done in whole project. Root models of project are included.
Parameters:
`project` - project
`types` - element type. Null means any element
Returns:
iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot)
Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done in whole project
Parameters:
`project` - project
`types` - element type. Null means any element
`includeRoot` - include project root models into result
Returns:
iterator
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Collect all elements of given specific type (not super class or interface) from the root element. Roots are also included
Parameters:
`root` - the root element for searching
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc)
Returns:
found elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)
Collect all elements of given specific type (not super class or interface) from the root element.
Parameters:
`root` - the root element for searching
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc)
`includeRoots` - include root elements into search results
Returns:
found elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types)
Collect all elements of given specific type (not super class or interface) from the project. Roots are also included.
Parameters:
`project` - project
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc)
Returns:
found elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)
Collect all elements of given specific type (not super class or interface) from the project
Parameters:
`project` - project
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc)
`includeRoots` - include root models of project into search results
Returns:
found elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoot,
 boolean includeAdditionalContents,
 @CheckForNull
 [ProgressStatus](../../task/ProgressStatus.html) monitor)
Collect all elements of given specific type (not super class or interface) from the root element.
Parameters:
`root` - the root element for searching
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc)
`includeRoot` - include root elements into search results
`includeAdditionalContents` - include additional content of Element defined in DSL
`monitor` - progress monitor
Returns:
found elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots)
Collect all elements of given specific type (not super class or interface) from the root element.
Parameters:
`roots` - the root element for searching
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc)
`includeRoots` - include root elements into search results
Returns:
found elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 @CheckForNull
 [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)[] types,
 boolean includeRoots,
 boolean includeAdditionalContents,
 @CheckForNull
 [ProgressStatus](../../task/ProgressStatus.html) monitor)
Collect all elements of given specific type (not super class or interface) from the root element.
Parameters:
`roots` - the root element for searching
`types` - an array of Element's class types (Class.class, Package.class, Property.class and etc)
`includeRoots` - include root elements into search results
`includeAdditionalContents` - include additional content of Element defined in DSL
`monitor` - progress monitor
Returns:
found elements

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Finder.ByTypeRecursivelyFinder">Class Finder.ByTypeRecursivelyFinder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.Finder.ByTypeRecursivelyFinder</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="Finder.html" title="class in com.nomagic.magicdraw.uml">Finder</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">Finder.ByTypeRecursivelyFinder</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Search for all elements by element type in the given root element(s) and all(direct and indirect) children of root element(s)</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all elements of given specific type (not super class or interface) from the project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D,boolean)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all elements of given specific type (not super class or interface) from the project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean,boolean,com.nomagic.task.ProgressStatus)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot,
 boolean includeAdditionalContents,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.Class%5B%5D,boolean)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,java.lang.Class%5B%5D,boolean,boolean,com.nomagic.task.ProgressStatus)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots,
 boolean includeAdditionalContents,
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D)">iterator</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.magicdraw.core.Project,java.lang.Class%5B%5D,boolean)">iterator</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D)">iterator</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class%5B%5D,boolean)">iterator</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(java.util.Collection,java.lang.Class%5B%5D)">iterator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(java.util.Collection,java.lang.Class%5B%5D,boolean)">iterator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).</div>
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
<section class="detail" id="iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[])">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element.</dd>
<dd><code>types</code> - element type. Null means any element</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],boolean)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</span></div>
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element.</dd>
<dd><code>types</code> - element type. Null means any element</dd>
<dd><code>includeRoot</code> - include root into result</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(java.util.Collection,java.lang.Class[])">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element. Roots are included also.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements.</dd>
<dd><code>types</code> - element type. Null means any element</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(java.util.Collection,java.lang.Class[],boolean)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</span></div>
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done from a given root element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements.</dd>
<dd><code>types</code> - element type. Null means any element</dd>
<dd><code>includeRoot</code> - include root elements into result</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(com.nomagic.magicdraw.core.Project,java.lang.Class[])">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done in whole project. Root models of project are included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>types</code> - element type. Null means any element</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(com.nomagic.magicdraw.core.Project,java.lang.Class[],boolean)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot)</span></div>
<div class="block">Returns iterator which contains elements of given specific type (not super class or interface).
 Search of elements is done in whole project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>types</code> - element type. Null means any element</dd>
<dd><code>includeRoot</code> - include project root models into result</dd>
<dt>Returns:</dt>
<dd>iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[])">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element. Roots are also included</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - the root element for searching</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc)</dd>
<dt>Returns:</dt>
<dd>found elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots)</span></div>
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - the root element for searching</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc)</dd>
<dd><code>includeRoots</code> - include root elements into search results</dd>
<dt>Returns:</dt>
<dd>found elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.magicdraw.core.Project,java.lang.Class[])">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types)</span></div>
<div class="block">Collect all elements of given specific type (not super class or interface) from the project. Roots are also included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc)</dd>
<dt>Returns:</dt>
<dd>found elements</dd>
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
<div class="block">Collect all elements of given specific type (not super class or interface) from the project</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc)</dd>
<dd><code>includeRoots</code> - include root models of project into search results</dd>
<dt>Returns:</dt>
<dd>found elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Class[],boolean,boolean,com.nomagic.task.ProgressStatus)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoot,
 boolean includeAdditionalContents,
 @CheckForNull
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span></div>
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - the root element for searching</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc)</dd>
<dd><code>includeRoot</code> - include root elements into search results</dd>
<dd><code>includeAdditionalContents</code> - include additional content of Element defined in DSL</dd>
<dd><code>monitor</code> - progress monitor</dd>
<dt>Returns:</dt>
<dd>found elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.Class[],boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots)</span></div>
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - the root element for searching</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc)</dd>
<dd><code>includeRoots</code> - include root elements into search results</dd>
<dt>Returns:</dt>
<dd>found elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,java.lang.Class[],boolean,boolean,com.nomagic.task.ProgressStatus)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>[] types,
 boolean includeRoots,
 boolean includeAdditionalContents,
 @CheckForNull
 <a href="../../task/ProgressStatus.html" title="interface in com.nomagic.task">ProgressStatus</a> monitor)</span></div>
<div class="block">Collect all elements of given specific type (not super class or interface) from the root element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - the root element for searching</dd>
<dd><code>types</code> - an array of Element's class types (Class.class, Package.class, Property.class and etc)</dd>
<dd><code>includeRoots</code> - include root elements into search results</dd>
<dd><code>includeAdditionalContents</code> - include additional content of Element defined in DSL</dd>
<dd><code>monitor</code> - progress monitor</dd>
<dt>Returns:</dt>
<dd>found elements</dd>
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
