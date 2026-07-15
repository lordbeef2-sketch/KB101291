# JAVA OPENAPI: ByEClassRecursively (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/kerml/find/ByEClassRecursively.html
- source_path: `com/dassault_systemes/modeler/kerml/find/ByEClassRecursively.html`
- source_sha256: `603ed64192e1d8e3ba1bb81fcad327c0f9952102cd9fb00e6bf9c284c31e0bed`
- captured_utc: `2026-07-14T16:44:44.764799+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.kerml.find](package-summary.html)

## Class ByEClassRecursively

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.kerml.find.AbstractFinder
com.dassault_systemes.modeler.kerml.find.ByEClassRecursively

@OpenApiAllpublic classByEClassRecursively
extends com.dassault_systemes.modeler.kerml.find.AbstractFinder
Finder implementation that locates [`elements`](../model/kerml/Element.html) by their
 `EClass`.

 This finder searches through the contents of a Project/IProject or given context
 Elements, visiting all nested elements and returning those that match
 the specified `EClass` or filtering criteria.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ByEClassRecursively](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[exactFind](#exactFind(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.util.Set))([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)`
Finds elements whose EClass exactly matches one of the given EClasses in project and all modules
 Subclasses are not included.
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[exactFind](#exactFind(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Set))([Element](../model/kerml/Element.html) context,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)`
Finds elements whose EClass exactly matches one of the given EClasses in Element context
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[exactFind](#exactFind(java.util.Collection,java.util.Set))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../model/kerml/Element.html)> contexts,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)`
Finds elements whose EClass exactly matches one of the given EClasses in Element contexts
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[exactFindInIProject](#exactFindInIProject(com.nomagic.ci.persistence.IProject,java.util.Set))(com.nomagic.ci.persistence.IProject contextIProject,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)`
Finds elements whose EClass exactly matches one of the given EClasses in the provided IProject
 Subclasses are not included.
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[exactFindInIProjects](#exactFindInIProjects(java.util.Collection,java.util.Set))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends com.nomagic.ci.persistence.IProject> contextIProjects,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)`
Finds elements whose EClass exactly matches one of the given EClasses in the provided IProjects
 Subclasses are not included.
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[find](#find(com.dassault_systemes.modeler.foundation.project.ModelElementProject,org.eclipse.emf.ecore.EClass))([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 org.eclipse.emf.ecore.EClass eClass)`
Finds elements matching the given EClass within the project.
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[find](#find(com.dassault_systemes.modeler.kerml.model.kerml.Element,org.eclipse.emf.ecore.EClass))([Element](../model/kerml/Element.html) context,
 org.eclipse.emf.ecore.EClass elementEClass)`
Finds elements matching the given EClass starting from the provided context.
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[find](#find(java.util.Collection,org.eclipse.emf.ecore.EClass))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../model/kerml/Element.html)> contexts,
 org.eclipse.emf.ecore.EClass elementEClass)`
Finds elements matching the given EClass starting from the provided contexts.
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[findInIProject](#findInIProject(com.nomagic.ci.persistence.IProject,org.eclipse.emf.ecore.EClass))(com.nomagic.ci.persistence.IProject contextIProject,
 org.eclipse.emf.ecore.EClass eClass)`
Finds elements whose EClass matches one of the given EClasses in the provided IProject
`<T extends [Element](../model/kerml/Element.html)> 
[Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T>`
`[findInIProjects](#findInIProjects(java.util.Collection,org.eclipse.emf.ecore.EClass))([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends com.nomagic.ci.persistence.IProject> contextIProjects,
 org.eclipse.emf.ecore.EClass eClass)`
Finds elements whose EClass matches one of the given EClasses in the provided IProjects
Methods inherited from class com.dassault_systemes.modeler.kerml.find.AbstractFinder
`find, streamOf`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ByEClassRecursively
public ByEClassRecursively()
 ============ METHOD DETAIL ========== 
Method Details
exactFind
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> exactFind([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)
Finds elements whose EClass exactly matches one of the given EClasses in project and all modules
 Subclasses are not included.
Type Parameters:
`T` - element type
Parameters:
`project` - the project to search in
`eClasses` - set of exact EClasses to match
Returns:
stream of matching elements
exactFind
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> exactFind([Element](../model/kerml/Element.html) context,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)
Finds elements whose EClass exactly matches one of the given EClasses in Element context
Type Parameters:
`T` - element type
Parameters:
`context` - the context to search in
`eClasses` - set of exact EClasses to match
Returns:
stream of matching elements
exactFind
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> exactFind([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../model/kerml/Element.html)> contexts,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)
Finds elements whose EClass exactly matches one of the given EClasses in Element contexts
Type Parameters:
`T` - element type
Parameters:
`contexts` - the contexts to search in
`eClasses` - set of exact EClasses to match
Returns:
stream of matching elements
exactFindInIProject
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> exactFindInIProject(com.nomagic.ci.persistence.IProject contextIProject,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)
Finds elements whose EClass exactly matches one of the given EClasses in the provided IProject
 Subclasses are not included.
Type Parameters:
`T` - element type
Parameters:
`contextIProject` - the context IProject to search in
`eClasses` - set of exact EClasses to match
Returns:
stream of matching elements
exactFindInIProjects
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> exactFindInIProjects([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends com.nomagic.ci.persistence.IProject> contextIProjects,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<org.eclipse.emf.ecore.EClass> eClasses)
Finds elements whose EClass exactly matches one of the given EClasses in the provided IProjects
 Subclasses are not included.
Type Parameters:
`T` - element type
Parameters:
`contextIProjects` - the context IProjects to search in
`eClasses` - set of exact EClasses to match
Returns:
stream of matching elements
find
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> find([ModelElementProject](../../foundation/project/ModelElementProject.html) project,
 org.eclipse.emf.ecore.EClass eClass)
Finds elements matching the given EClass within the project.
Type Parameters:
`T` - element type
Parameters:
`project` - the project to search in
`eClass` - the EClass to match
Returns:
stream of matching elements
find
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> find([Element](../model/kerml/Element.html) context,
 org.eclipse.emf.ecore.EClass elementEClass)
Finds elements matching the given EClass starting from the provided context.
Type Parameters:
`T` - element type
Parameters:
`context` - context object to start search in
`elementEClass` - the EClass to match
Returns:
stream of matching elements
find
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> find([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends [Element](../model/kerml/Element.html)> contexts,
 org.eclipse.emf.ecore.EClass elementEClass)
Finds elements matching the given EClass starting from the provided contexts.
Type Parameters:
`T` - element type
Parameters:
`contexts` - contexts object to start search in
`elementEClass` - the EClass to match
Returns:
stream of matching elements
findInIProject
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> findInIProject(com.nomagic.ci.persistence.IProject contextIProject,
 org.eclipse.emf.ecore.EClass eClass)
Finds elements whose EClass matches one of the given EClasses in the provided IProject
Type Parameters:
`T` - element type
Parameters:
`contextIProject` - the context IProject to search in
`eClass` - the EClass to match
Returns:
stream of matching elements
findInIProjects
public <T extends [Element](../model/kerml/Element.html)> [Stream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html)<T> findInIProjects([Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<? extends com.nomagic.ci.persistence.IProject> contextIProjects,
 org.eclipse.emf.ecore.EClass eClass)
Finds elements whose EClass matches one of the given EClasses in the provided IProjects
Type Parameters:
`T` - element type
Parameters:
`contextIProjects` - the context IProjects to search in
`eClass` - the EClass to match
Returns:
stream of matching elements

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.kerml.find</a></div>
<h1 class="title" title="Class ByEClassRecursively">Class ByEClassRecursively</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.kerml.find.AbstractFinder
<div class="inheritance">com.dassault_systemes.modeler.kerml.find.ByEClassRecursively</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ByEClassRecursively</span>
<span class="extends-implements">extends com.dassault_systemes.modeler.kerml.find.AbstractFinder</span></div>
<div class="block">Finder implementation that locates <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml"><code>elements</code></a> by their
 <code>EClass</code>.

 <p>
 This finder searches through the contents of a Project/IProject or given context
 Elements, visiting all nested elements and returning those that match
 the specified <code>EClass</code> or filtering criteria.
 </p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ByEClassRecursively</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exactFind(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.util.Set)">exactFind</a><wbr/>(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in project and all modules
 Subclasses are not included.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exactFind(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Set)">exactFind</a><wbr/>(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in Element context</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exactFind(java.util.Collection,java.util.Set)">exactFind</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; contexts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in Element contexts</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exactFindInIProject(com.nomagic.ci.persistence.IProject,java.util.Set)">exactFindInIProject</a><wbr/>(com.nomagic.ci.persistence.IProject contextIProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in the provided IProject
 Subclasses are not included.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exactFindInIProjects(java.util.Collection,java.util.Set)">exactFindInIProjects</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.nomagic.ci.persistence.IProject&gt; contextIProjects,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in the provided IProjects
 Subclasses are not included.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.dassault_systemes.modeler.foundation.project.ModelElementProject,org.eclipse.emf.ecore.EClass)">find</a><wbr/>(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements matching the given EClass within the project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(com.dassault_systemes.modeler.kerml.model.kerml.Element,org.eclipse.emf.ecore.EClass)">find</a><wbr/>(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 org.eclipse.emf.ecore.EClass elementEClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements matching the given EClass starting from the provided context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#find(java.util.Collection,org.eclipse.emf.ecore.EClass)">find</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; contexts,
 org.eclipse.emf.ecore.EClass elementEClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements matching the given EClass starting from the provided contexts.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findInIProject(com.nomagic.ci.persistence.IProject,org.eclipse.emf.ecore.EClass)">findInIProject</a><wbr/>(com.nomagic.ci.persistence.IProject contextIProject,
 org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements whose EClass matches one of the given EClasses in the provided IProject</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;<br/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a><wbr/>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#findInIProjects(java.util.Collection,org.eclipse.emf.ecore.EClass)">findInIProjects</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.nomagic.ci.persistence.IProject&gt; contextIProjects,
 org.eclipse.emf.ecore.EClass eClass)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Finds elements whose EClass matches one of the given EClasses in the provided IProjects</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.find.AbstractFinder">Methods inherited from class com.dassault_systemes.modeler.kerml.find.AbstractFinder</h3>
<code>find, streamOf</code></div>
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
<h3>ByEClassRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ByEClassRecursively</span>()</div>
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
<section class="detail" id="exactFind(com.dassault_systemes.modeler.foundation.project.ModelElementProject,java.util.Set)">
<h3>exactFind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">exactFind</span><wbr/><span class="parameters">(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</span></div>
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in project and all modules
 Subclasses are not included.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>project</code> - the project to search in</dd>
<dd><code>eClasses</code> - set of exact EClasses to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exactFind(com.dassault_systemes.modeler.kerml.model.kerml.Element,java.util.Set)">
<h3>exactFind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">exactFind</span><wbr/><span class="parameters">(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</span></div>
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in Element context</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>context</code> - the context to search in</dd>
<dd><code>eClasses</code> - set of exact EClasses to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exactFind(java.util.Collection,java.util.Set)">
<h3>exactFind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">exactFind</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; contexts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</span></div>
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in Element contexts</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>contexts</code> - the contexts to search in</dd>
<dd><code>eClasses</code> - set of exact EClasses to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exactFindInIProject(com.nomagic.ci.persistence.IProject,java.util.Set)">
<h3>exactFindInIProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">exactFindInIProject</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject contextIProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</span></div>
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in the provided IProject
 Subclasses are not included.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>contextIProject</code> - the context IProject to search in</dd>
<dd><code>eClasses</code> - set of exact EClasses to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exactFindInIProjects(java.util.Collection,java.util.Set)">
<h3>exactFindInIProjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">exactFindInIProjects</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.nomagic.ci.persistence.IProject&gt; contextIProjects,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;org.eclipse.emf.ecore.EClass&gt; eClasses)</span></div>
<div class="block">Finds elements whose EClass exactly matches one of the given EClasses in the provided IProjects
 Subclasses are not included.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>contextIProjects</code> - the context IProjects to search in</dd>
<dd><code>eClasses</code> - set of exact EClasses to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.dassault_systemes.modeler.foundation.project.ModelElementProject,org.eclipse.emf.ecore.EClass)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project,
 org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Finds elements matching the given EClass within the project.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>project</code> - the project to search in</dd>
<dd><code>eClass</code> - the EClass to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(com.dassault_systemes.modeler.kerml.model.kerml.Element,org.eclipse.emf.ecore.EClass)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a> context,
 org.eclipse.emf.ecore.EClass elementEClass)</span></div>
<div class="block">Finds elements matching the given EClass starting from the provided context.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>context</code> - context object to start search in</dd>
<dd><code>elementEClass</code> - the EClass to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="find(java.util.Collection,org.eclipse.emf.ecore.EClass)">
<h3>find</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">find</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt; contexts,
 org.eclipse.emf.ecore.EClass elementEClass)</span></div>
<div class="block">Finds elements matching the given EClass starting from the provided contexts.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>contexts</code> - contexts object to start search in</dd>
<dd><code>elementEClass</code> - the EClass to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findInIProject(com.nomagic.ci.persistence.IProject,org.eclipse.emf.ecore.EClass)">
<h3>findInIProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">findInIProject</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject contextIProject,
 org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Finds elements whose EClass matches one of the given EClasses in the provided IProject</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>contextIProject</code> - the context IProject to search in</dd>
<dd><code>eClass</code> - the EClass to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="findInIProjects(java.util.Collection,org.eclipse.emf.ecore.EClass)">
<h3>findInIProjects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T extends <a href="../model/kerml/Element.html" title="interface in com.dassault_systemes.modeler.kerml.model.kerml">Element</a>&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt;</span> <span class="element-name">findInIProjects</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends com.nomagic.ci.persistence.IProject&gt; contextIProjects,
 org.eclipse.emf.ecore.EClass eClass)</span></div>
<div class="block">Finds elements whose EClass matches one of the given EClasses in the provided IProjects</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - element type</dd>
<dt>Parameters:</dt>
<dd><code>contextIProjects</code> - the context IProjects to search in</dd>
<dd><code>eClass</code> - the EClass to match</dd>
<dt>Returns:</dt>
<dd>stream of matching elements</dd>
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
