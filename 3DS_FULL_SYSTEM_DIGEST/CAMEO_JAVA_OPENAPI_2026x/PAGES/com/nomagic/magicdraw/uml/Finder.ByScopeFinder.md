# JAVA OPENAPI: Finder.ByScopeFinder (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/Finder.ByScopeFinder.html
- source_path: `com/nomagic/magicdraw/uml/Finder.ByScopeFinder.html`
- source_sha256: `2b02e00efb2e40a16b947cb0d4bb2950945af31d05516689207a35c9f19afd55`
- captured_utc: `2026-07-14T16:58:27.690174+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml](package-summary.html)

## Class Finder.ByScopeFinder

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.Finder.ByScopeFinder

Enclosing class:
`[Finder](Finder.html)`

public static final classFinder.ByScopeFinder
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Collects all elements from a given project.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean includeRoot)`
Collects all elements from a given project.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)`
Collects all elements from a given root.Root element is included
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)`
Collects all elements from a given root
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)`
Collects all elements from a given root.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[find](#find(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)`
Collects all elements from a given root
`<T extends [BaseElement](BaseElement.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[findIncludingPresentationElements](#findIncludingPresentationElements(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Collects all elements from a given project including PresentationElements.
`<T extends [BaseElement](BaseElement.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[findIncludingPresentationElements](#findIncludingPresentationElements(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean includeRoot)`
Collects all elements from a given project including PresentationElements
`<T extends [BaseElement](BaseElement.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[findIncludingPresentationElements](#findIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)`
Collects all elements from a given root including PresentationElements.
`<T extends [BaseElement](BaseElement.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[findIncludingPresentationElements](#findIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)`
Collects all elements from a given root including PresentationElements
`<T extends [BaseElement](BaseElement.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[findIncludingPresentationElements](#findIncludingPresentationElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)`
Collects all elements from a given root including PresentationElements.
`<T extends [BaseElement](BaseElement.html)> 
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T>`
`[findIncludingPresentationElements](#findIncludingPresentationElements(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)`
Collects all elements from a given root including PresentationElements
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Create iterator for iterating content of given project including root models of project.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean includeRoot)`
Create iterator for iterating content from a given root.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)`
Create iterator for iterating content from a given root including it.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)`
Create iterator for iterating content from a given root.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)`
Create iterator for iterating content from a given roots including them.
`<T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iterator](#iterator(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)`
Create iterator for iterating content from a given root.
`<T extends [BaseElement](BaseElement.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iteratorIncludingPresentationElements](#iteratorIncludingPresentationElements(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
Create iterator for iterating content of given Project including PresentationElements and project root models
`<T extends [BaseElement](BaseElement.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iteratorIncludingPresentationElements](#iteratorIncludingPresentationElements(com.nomagic.magicdraw.core.Project,boolean))([Project](../core/Project.html) project,
 boolean includeRoot)`
Create iterator for iterating content of whole Project including PresentationElements
`<T extends [BaseElement](BaseElement.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iteratorIncludingPresentationElements](#iteratorIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)`
Create iterator for iterating content from a given root including PresentationElements and root
`<T extends [BaseElement](BaseElement.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iteratorIncludingPresentationElements](#iteratorIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)`
Create iterator for iterating content from a given root including PresentationElements
`<T extends [BaseElement](BaseElement.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iteratorIncludingPresentationElements](#iteratorIncludingPresentationElements(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)`
Create iterator for iterating content from a given root including PresentationElements and roots
`<T extends [BaseElement](BaseElement.html)> 
com.nomagic.ci.persistence.local.query.CloseableIterator<T>`
`[iteratorIncludingPresentationElements](#iteratorIncludingPresentationElements(java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)`
Create iterator for iterating content from a given root including PresentationElements
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)
Create iterator for iterating content from a given root including it.
Parameters:
`root` - root elements
Returns:
elements iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Project](../core/Project.html) project)
Create iterator for iterating content of given project including root models of project.
Parameters:
`project` - project
Returns:
elements iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)
Create iterator for iterating content from a given roots including them.
Parameters:
`roots` - root elements
Returns:
elements iterator
iteratorIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iteratorIncludingPresentationElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)
Create iterator for iterating content from a given root including PresentationElements and root
Parameters:
`root` - root elements
Returns:
elements iterator
iteratorIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iteratorIncludingPresentationElements([Project](../core/Project.html) project)
Create iterator for iterating content of given Project including PresentationElements and project root models
Returns:
elements iterator
iteratorIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iteratorIncludingPresentationElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)
Create iterator for iterating content from a given root including PresentationElements and roots
Parameters:
`roots` - root elements
Returns:
elements iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)
Create iterator for iterating content from a given root.
Parameters:
`root` - root element
`includeRoot` - include roots
Returns:
elements iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Project](../core/Project.html) project,
 boolean includeRoot)
Create iterator for iterating content from a given root.
Parameters:
`project` - project
`includeRoot` - include roots
Returns:
elements iterator
iterator
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iterator([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)
Create iterator for iterating content from a given root.
Parameters:
`roots` - root elements
`includeRoot` - include roots
Returns:
elements iterator
iteratorIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iteratorIncludingPresentationElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)
Create iterator for iterating content from a given root including PresentationElements
Parameters:
`root` - root elements
`includeRoot` - include roots
Returns:
elements iterator
iteratorIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iteratorIncludingPresentationElements([Project](../core/Project.html) project,
 boolean includeRoot)
Create iterator for iterating content of whole Project including PresentationElements
Parameters:
`project` - project
`includeRoot` - include roots
Returns:
elements iterator
iteratorIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)>
com.nomagic.ci.persistence.local.query.CloseableIterator<T> iteratorIncludingPresentationElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)
Create iterator for iterating content from a given root including PresentationElements
Parameters:
`roots` - root elements
`includeRoot` - include roots
Returns:
elements iterator
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project,
 boolean includeRoot)
Collects all elements from a given project.
Parameters:
`project` - project
`includeRoot` - include project root models
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)
Collects all elements from a given root
Parameters:
`root` - root element
`includeRoot` - include root into result
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)
Collects all elements from a given root
Parameters:
`roots` - root elements
`includeRoot` - includes root into result
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> find([Project](../core/Project.html) project)
Collects all elements from a given project. Project root models are included.
Parameters:
`project` - project
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> find([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)
Collects all elements from a given root.Root element is included
Parameters:
`root` - root element
Returns:
elements
find
public <T extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)
Collects all elements from a given root. Root elements are included
Parameters:
`roots` - root elements
Returns:
elements
findIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> findIncludingPresentationElements([Project](../core/Project.html) project)
Collects all elements from a given project including PresentationElements. Project root models are included.
Parameters:
`project` - project
Returns:
elements
findIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> findIncludingPresentationElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root)
Collects all elements from a given root including PresentationElements. Root element is included.
Parameters:
`root` - root element
Returns:
elements
findIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> findIncludingPresentationElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots)
Collects all elements from a given root including PresentationElements. Root elements are included.
Parameters:
`roots` - roots element
Returns:
elements
findIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> findIncludingPresentationElements([Project](../core/Project.html) project,
 boolean includeRoot)
Collects all elements from a given project including PresentationElements
Parameters:
`project` - project
`includeRoot` - include project root models
Returns:
elements
findIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> findIncludingPresentationElements([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) root,
 boolean includeRoot)
Collects all elements from a given root including PresentationElements
Parameters:
`root` - root element
`includeRoot` - include project root models
Returns:
elements
findIncludingPresentationElements
public <T extends [BaseElement](BaseElement.html)> [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<T> findIncludingPresentationElements([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> roots,
 boolean includeRoot)
Collects all elements from a given root including PresentationElements
Parameters:
`roots` - roots element
`includeRoot` - include project root models
Returns:
elements

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml</a></div>
<h1 class="title" title="Class Finder.ByScopeFinder">Class Finder.ByScopeFinder</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.Finder.ByScopeFinder</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><code><a href="Finder.html" title="class in com.nomagic.magicdraw.uml">Finder</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">Finder.ByScopeFinder</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Search for all elements in the given root element(s) and all(direct and indirect) children of root element(s)</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.magicdraw.core.Project,boolean)">find</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root.Root element is included</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">find</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,boolean)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIncludingPresentationElements(com.nomagic.magicdraw.core.Project)">findIncludingPresentationElements</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given project including PresentationElements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIncludingPresentationElements(com.nomagic.magicdraw.core.Project,boolean)">findIncludingPresentationElements</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given project including PresentationElements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">findIncludingPresentationElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root including PresentationElements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">findIncludingPresentationElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root including PresentationElements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIncludingPresentationElements(java.util.Collection)">findIncludingPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root including PresentationElements.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findIncludingPresentationElements(java.util.Collection,boolean)">findIncludingPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collects all elements from a given root including PresentationElements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.magicdraw.core.Project)">iterator</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content of given project including root models of project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.magicdraw.core.Project,boolean)">iterator</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">iterator</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root including it.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">iterator</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(java.util.Collection)">iterator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given roots including them.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iterator(java.util.Collection,boolean)">iterator</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iteratorIncludingPresentationElements(com.nomagic.magicdraw.core.Project)">iteratorIncludingPresentationElements</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content of given Project including PresentationElements and project root models</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iteratorIncludingPresentationElements(com.nomagic.magicdraw.core.Project,boolean)">iteratorIncludingPresentationElements</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content of whole Project including PresentationElements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iteratorIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">iteratorIncludingPresentationElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root including PresentationElements and root</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iteratorIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">iteratorIncludingPresentationElements</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root including PresentationElements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iteratorIncludingPresentationElements(java.util.Collection)">iteratorIncludingPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root including PresentationElements and roots</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;<br/>com.nomagic.ci.persistence.local.query.CloseableIterator<wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#iteratorIncludingPresentationElements(java.util.Collection,boolean)">iteratorIncludingPresentationElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create iterator for iterating content from a given root including PresentationElements</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</span></div>
<div class="block">Create iterator for iterating content from a given root including it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root elements</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(com.nomagic.magicdraw.core.Project)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Create iterator for iterating content of given project including root models of project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(java.util.Collection)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</span></div>
<div class="block">Create iterator for iterating content from a given roots including them.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iteratorIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>iteratorIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iteratorIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</span></div>
<div class="block">Create iterator for iterating content from a given root including PresentationElements and root</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root elements</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iteratorIncludingPresentationElements(com.nomagic.magicdraw.core.Project)">
<h3>iteratorIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iteratorIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Create iterator for iterating content of given Project including PresentationElements and project root models</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iteratorIncludingPresentationElements(java.util.Collection)">
<h3>iteratorIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iteratorIncludingPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</span></div>
<div class="block">Create iterator for iterating content from a given root including PresentationElements and roots</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</span></div>
<div class="block">Create iterator for iterating content from a given root.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dd><code>includeRoot</code> - include roots</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(com.nomagic.magicdraw.core.Project,boolean)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</span></div>
<div class="block">Create iterator for iterating content from a given root.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>includeRoot</code> - include roots</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iterator(java.util.Collection,boolean)">
<h3>iterator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iterator</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</span></div>
<div class="block">Create iterator for iterating content from a given root.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dd><code>includeRoot</code> - include roots</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iteratorIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>iteratorIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iteratorIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</span></div>
<div class="block">Create iterator for iterating content from a given root including PresentationElements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root elements</dd>
<dd><code>includeRoot</code> - include roots</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iteratorIncludingPresentationElements(com.nomagic.magicdraw.core.Project,boolean)">
<h3>iteratorIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iteratorIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</span></div>
<div class="block">Create iterator for iterating content of whole Project including PresentationElements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>includeRoot</code> - include roots</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="iteratorIncludingPresentationElements(java.util.Collection,boolean)">
<h3>iteratorIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span>
<span class="return-type">com.nomagic.ci.persistence.local.query.CloseableIterator&lt;T&gt;</span> <span class="element-name">iteratorIncludingPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</span></div>
<div class="block">Create iterator for iterating content from a given root including PresentationElements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dd><code>includeRoot</code> - include roots</dd>
<dt>Returns:</dt>
<dd>elements iterator</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.magicdraw.core.Project,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</span></div>
<div class="block">Collects all elements from a given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>includeRoot</code> - include project root models</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</span></div>
<div class="block">Collects all elements from a given root</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dd><code>includeRoot</code> - include root into result</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,boolean)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</span></div>
<div class="block">Collects all elements from a given root</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dd><code>includeRoot</code> - includes root into result</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.magicdraw.core.Project)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Collects all elements from a given project. Project root models are included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</span></div>
<div class="block">Collects all elements from a given root.Root element is included</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</span></div>
<div class="block">Collects all elements from a given root. Root elements are included</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - root elements</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIncludingPresentationElements(com.nomagic.magicdraw.core.Project)">
<h3>findIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">findIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Collects all elements from a given project including PresentationElements. Project root models are included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>findIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">findIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root)</span></div>
<div class="block">Collects all elements from a given root including PresentationElements. Root element is included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIncludingPresentationElements(java.util.Collection)">
<h3>findIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">findIncludingPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots)</span></div>
<div class="block">Collects all elements from a given root including PresentationElements. Root elements are included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - roots element</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIncludingPresentationElements(com.nomagic.magicdraw.core.Project,boolean)">
<h3>findIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">findIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 boolean includeRoot)</span></div>
<div class="block">Collects all elements from a given project including PresentationElements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>includeRoot</code> - include project root models</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIncludingPresentationElements(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,boolean)">
<h3>findIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">findIncludingPresentationElements</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> root,
 boolean includeRoot)</span></div>
<div class="block">Collects all elements from a given root including PresentationElements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>root</code> - root element</dd>
<dd><code>includeRoot</code> - include project root models</dd>
<dt>Returns:</dt>
<dd>elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findIncludingPresentationElements(java.util.Collection,boolean)">
<h3>findIncludingPresentationElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">findIncludingPresentationElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; roots,
 boolean includeRoot)</span></div>
<div class="block">Collects all elements from a given root including PresentationElements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roots</code> - roots element</dd>
<dd><code>includeRoot</code> - include project root models</dd>
<dt>Returns:</dt>
<dd>elements</dd>
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
