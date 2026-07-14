# JAVA OPENAPI: StateChangeHandler (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/utils/StateChangeHandler.html
- source_path: `com/nomagic/magicdraw/utils/StateChangeHandler.html`
- source_sha256: `895168da30ecc096ee56a9f8207aa7c9206c7e3e3140a1dc9804e4fb7a7db80c`
- captured_utc: `2026-07-14T16:56:08.374602+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.utils](package-summary.html)

## Class StateChangeHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.utils.StateChangeHandler

@OpenApipublic classStateChangeHandler
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Class handling state changes in model and symbols.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[StateChangeHandler.DirtyType](StateChangeHandler.DirtyType.html)`
Defines how much dirty is project.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[StateChangeHandler](#%3Cinit%3E(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addListener](#addListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener))(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)`
Adds specified listener.
`void`
`[addToLoadedChangedElementsIDS](#addToLoadedChangedElementsIDS(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)`

`<T> T`
`[callWithEnabled](#callWithEnabled(boolean,java.util.concurrent.Callable))(boolean enable,
 [Callable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html)<T> supplier)`

`void`
`[clearDirty](#clearDirty())()`
Clear dirty state of all elements.
`void`
`[clearDirty](#clearDirty(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject iProject)`
Marks all elements from given IProject as non-dirty.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getAllChangedElementsIDS](#getAllChangedElementsIDS())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[getChangedElementsIDS](#getChangedElementsIDS())()`

`[StateChangeHandler.DirtyType](StateChangeHandler.DirtyType.html)`
`[getDirtyType](#getDirtyType(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`

`[Project](../core/Project.html)`
`[getProject](#getProject())()`

`void`
`[handleViewChange](#handleViewChange(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../uml/symbols/PresentationElement.html) symbol)`
Marks object diagram as dirty.
`boolean`
`[isAutoSaveDirty](#isAutoSaveDirty())()`

`boolean`
`[isDirty](#isDirty(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`

`boolean`
`[isDirty](#isDirty(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Returns true if given element has been modified and is not yet saved.
`boolean`
`[isDirty](#isDirty(org.eclipse.emf.ecore.resource.Resource))(org.eclipse.emf.ecore.resource.Resource resource)`
Check if given resource is dirty in the given project context.
`void`
`[removeListener](#removeListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener))(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)`
Removes the specified listener.
`void`
`[reSetDirty](#reSetDirty(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 [StateChangeHandler.DirtyType](StateChangeHandler.DirtyType.html) dirtyType)`

`void`
`[runWithEnabled](#runWithEnabled(boolean,java.lang.Runnable))(boolean enable,
 [Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)`

`void`
`[setAutoSaveDirty](#setAutoSaveDirty(boolean))(boolean autoSaveDirty)`

`void`
`[setChangedElementsIDS](#setChangedElementsIDS(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)`

`void`
`[setDirty](#setDirty(boolean,com.dassault_systemes.modeler.foundation.model.ModelElement))(boolean dirty,
 com.dassault_systemes.modeler.foundation.model.ModelElement element)`
Marks element as changed/unchanged.
`void`
`[setDirty](#setDirty(boolean,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement))(boolean dirty,
 [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)`
Marks diagram presentation element and diagram element as changed/unchanged.
`void`
`[setDirty](#setDirty(com.nomagic.ci.persistence.features.FeatureDataSet,boolean))(com.nomagic.ci.persistence.features.FeatureDataSet fd,
 boolean dirty)`
Marks given resource dirty
`void`
`[setDirty](#setDirty(com.nomagic.ci.persistence.IProject,boolean))(com.nomagic.ci.persistence.IProject project,
 boolean dirty)`

`void`
`[setDirty](#setDirty(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType))(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 [StateChangeHandler.DirtyType](StateChangeHandler.DirtyType.html) dirtyType)`

`void`
`[setDirty](#setDirty(org.eclipse.emf.ecore.resource.Resource,boolean))(org.eclipse.emf.ecore.resource.Resource resource,
 boolean dirty)`
Marks given resource dirty
`boolean`
`[setEnable](#setEnable(boolean))(boolean enable)`
Enables or disabled handler
`void`
`[trackModificationForResource](#trackModificationForResource(org.eclipse.emf.ecore.resource.Resource))(org.eclipse.emf.ecore.resource.Resource resource)`
Registers URI for which default dirty resource tracking will be enabled.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
StateChangeHandler
public StateChangeHandler([Project](../core/Project.html) project)
 ============ METHOD DETAIL ========== 
Method Details
addListener
public void addListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)
Adds specified listener.
Parameters:
`listener` - a new listener.
removeListener
public void removeListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)
Removes the specified listener.
Parameters:
`listener` - the listener which should be removed.
setEnable
public boolean setEnable(boolean enable)
Enables or disabled handler
Parameters:
`enable` - true if changes should be registered, false otherwise
Returns:
previous state
runWithEnabled
public void runWithEnabled(boolean enable,
 [Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable)
callWithEnabled
public <T> T callWithEnabled(boolean enable,
 [Callable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html)<T> supplier)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
handleViewChange
public void handleViewChange([PresentationElement](../uml/symbols/PresentationElement.html) symbol)
Marks object diagram as dirty.
Parameters:
`symbol` - symbol to mark as dirty
clearDirty
public void clearDirty()
Clear dirty state of all elements.
clearDirty
public void clearDirty(com.nomagic.ci.persistence.IProject iProject)
Marks all elements from given IProject as non-dirty.
Parameters:
`iProject` - project to clear
setDirty
public void setDirty(boolean dirty,
 com.dassault_systemes.modeler.foundation.model.ModelElement element)
Marks element as changed/unchanged.
Parameters:
`dirty` - dirty flag
`element` - element
setDirty
public void setDirty(boolean dirty,
 [AbstractDiagramPresentationElement](../uml/symbols/AbstractDiagramPresentationElement.html) diagram)
Marks diagram presentation element and diagram element as changed/unchanged.
 Diagram and DiagramPresentationElement is always marked together. Marking diagram as dirty updates its modification time, and resets content hash.
Parameters:
`dirty` - dirty flag
`diagram` - diagram
setDirty
public void setDirty(@Nonnull
 org.eclipse.emf.ecore.resource.Resource resource,
 boolean dirty)
Marks given resource dirty
Parameters:
`resource` - target element which will become dirty
setDirty
public void setDirty(@Nonnull
 com.nomagic.ci.persistence.features.FeatureDataSet fd,
 boolean dirty)
Marks given resource dirty
Parameters:
`fd` - target element which will become dirty
isDirty
public boolean isDirty(@Nonnull
 org.eclipse.emf.ecore.resource.Resource resource)
Check if given resource is dirty in the given project context. Even if
 `Resource.isModified()` == `false`, this method can return `true`
Returns:
true if resource is dirty
isDirty
@OpenApipublic boolean isDirty([BaseElement](../uml/BaseElement.html) element)
Returns true if given element has been modified and is not yet saved.
 Individual [`PresentationElement`](../uml/symbols/PresentationElement.html) is not tracked, its [`AbstractDiagramPresentationElement`](../uml/symbols/AbstractDiagramPresentationElement.html) is used instead.
Parameters:
`element` - element
Returns:
true if element is dirty
setChangedElementsIDS
public void setChangedElementsIDS([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)
getAllChangedElementsIDS
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getAllChangedElementsIDS()
Returns:
changed during this session + loaded changed ids.
getChangedElementsIDS
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> getChangedElementsIDS()
addToLoadedChangedElementsIDS
public void addToLoadedChangedElementsIDS([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> ids)
setDirty
public void setDirty(com.nomagic.ci.persistence.IProject project,
 boolean dirty)
setDirty
public void setDirty(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 @CheckForNull
 [StateChangeHandler.DirtyType](StateChangeHandler.DirtyType.html) dirtyType)
isDirty
public boolean isDirty(com.nomagic.ci.persistence.IProject project)
getDirtyType
@CheckForNullpublic [StateChangeHandler.DirtyType](StateChangeHandler.DirtyType.html) getDirtyType(com.nomagic.ci.persistence.IProject project)
reSetDirty
public void reSetDirty(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 @CheckForNull
 [StateChangeHandler.DirtyType](StateChangeHandler.DirtyType.html) dirtyType)
isAutoSaveDirty
public boolean isAutoSaveDirty()
setAutoSaveDirty
public void setAutoSaveDirty(boolean autoSaveDirty)
trackModificationForResource
public void trackModificationForResource(@Nonnull
 org.eclipse.emf.ecore.resource.Resource resource)
Registers URI for which default dirty resource tracking will be enabled.
 Note, this mechanism is based on EMF track changes
Parameters:
`resource` - resource to track changes
getProject
public [Project](../core/Project.html) getProject()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.utils</a></div>
<h1 class="title" title="Class StateChangeHandler">Class StateChangeHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.utils.StateChangeHandler</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">StateChangeHandler</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Class handling state changes in model and symbols.</div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines how much dirty is project.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project)">StateChangeHandler</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener)">addListener</a><wbr/>(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds specified listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addToLoadedChangedElementsIDS(java.util.Collection)">addToLoadedChangedElementsIDS</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;T&gt; T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callWithEnabled(boolean,java.util.concurrent.Callable)">callWithEnabled</a><wbr/>(boolean enable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;T&gt; supplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDirty()">clearDirty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Clear dirty state of all elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearDirty(com.nomagic.ci.persistence.IProject)">clearDirty</a><wbr/>(com.nomagic.ci.persistence.IProject iProject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks all elements from given IProject as non-dirty.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAllChangedElementsIDS()">getAllChangedElementsIDS</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChangedElementsIDS()">getChangedElementsIDS</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDirtyType(com.nomagic.ci.persistence.IProject)">getDirtyType</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleViewChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">handleViewChange</a><wbr/>(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks object  diagram as dirty.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAutoSaveDirty()">isAutoSaveDirty</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty(com.nomagic.ci.persistence.IProject)">isDirty</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty(com.nomagic.magicdraw.uml.BaseElement)">isDirty</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if given element has been modified and is not yet saved.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isDirty(org.eclipse.emf.ecore.resource.Resource)">isDirty</a><wbr/>(org.eclipse.emf.ecore.resource.Resource resource)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if given resource is dirty in the given project context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener)">removeListener</a><wbr/>(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes the specified listener.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#reSetDirty(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">reSetDirty</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 <a href="StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#runWithEnabled(boolean,java.lang.Runnable)">runWithEnabled</a><wbr/>(boolean enable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAutoSaveDirty(boolean)">setAutoSaveDirty</a><wbr/>(boolean autoSaveDirty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChangedElementsIDS(java.util.Collection)">setChangedElementsIDS</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(boolean,com.dassault_systemes.modeler.foundation.model.ModelElement)">setDirty</a><wbr/>(boolean dirty,
 com.dassault_systemes.modeler.foundation.model.ModelElement element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks element as changed/unchanged.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(boolean,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">setDirty</a><wbr/>(boolean dirty,
 <a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks diagram presentation element and diagram element as changed/unchanged.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(com.nomagic.ci.persistence.features.FeatureDataSet,boolean)">setDirty</a><wbr/>(com.nomagic.ci.persistence.features.FeatureDataSet fd,
 boolean dirty)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks given resource dirty</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(com.nomagic.ci.persistence.IProject,boolean)">setDirty</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 boolean dirty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">setDirty</a><wbr/>(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 <a href="StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDirty(org.eclipse.emf.ecore.resource.Resource,boolean)">setDirty</a><wbr/>(org.eclipse.emf.ecore.resource.Resource resource,
 boolean dirty)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Marks given resource dirty</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnable(boolean)">setEnable</a><wbr/>(boolean enable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables or disabled handler</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#trackModificationForResource(org.eclipse.emf.ecore.resource.Resource)">trackModificationForResource</a><wbr/>(org.eclipse.emf.ecore.resource.Resource resource)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Registers URI for which default dirty resource tracking will be enabled.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project)">
<h3>StateChangeHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">StateChangeHandler</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
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
<section class="detail" id="addListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener)">
<h3>addListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)</span></div>
<div class="block">Adds specified listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - a new listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeListener(com.nomagic.magicdraw.utils.StatusChangeHandlerListener)">
<h3>removeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListener</span><wbr/><span class="parameters">(com.nomagic.magicdraw.utils.StatusChangeHandlerListener listener)</span></div>
<div class="block">Removes the specified listener.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>listener</code> - the listener which should be removed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnable(boolean)">
<h3>setEnable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setEnable</span><wbr/><span class="parameters">(boolean enable)</span></div>
<div class="block">Enables or disabled handler</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enable</code> - true if changes should be registered, false otherwise</dd>
<dt>Returns:</dt>
<dd>previous state</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runWithEnabled(boolean,java.lang.Runnable)">
<h3>runWithEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">runWithEnabled</span><wbr/><span class="parameters">(boolean enable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
</section>
</li>
<li>
<section class="detail" id="callWithEnabled(boolean,java.util.concurrent.Callable)">
<h3>callWithEnabled</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">T</span> <span class="element-name">callWithEnabled</span><wbr/><span class="parameters">(boolean enable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;T&gt; supplier)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleViewChange(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>handleViewChange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">handleViewChange</span><wbr/><span class="parameters">(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> symbol)</span></div>
<div class="block">Marks object  diagram as dirty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>symbol</code> - symbol to mark as dirty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearDirty()">
<h3>clearDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDirty</span>()</div>
<div class="block">Clear dirty state of all elements.</div>
</section>
</li>
<li>
<section class="detail" id="clearDirty(com.nomagic.ci.persistence.IProject)">
<h3>clearDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearDirty</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject iProject)</span></div>
<div class="block">Marks all elements from given IProject as non-dirty.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>iProject</code> - project to clear</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirty(boolean,com.dassault_systemes.modeler.foundation.model.ModelElement)">
<h3>setDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(boolean dirty,
 com.dassault_systemes.modeler.foundation.model.ModelElement element)</span></div>
<div class="block">Marks element as changed/unchanged.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dirty</code> - dirty flag</dd>
<dd><code>element</code> - element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirty(boolean,com.nomagic.magicdraw.uml.symbols.AbstractDiagramPresentationElement)">
<h3>setDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(boolean dirty,
 <a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">AbstractDiagramPresentationElement</a> diagram)</span></div>
<div class="block">Marks diagram presentation element and diagram element as changed/unchanged.
 Diagram and DiagramPresentationElement is always marked together. Marking diagram as dirty updates its modification time, and resets content hash.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dirty</code> - dirty flag</dd>
<dd><code>diagram</code> - diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirty(org.eclipse.emf.ecore.resource.Resource,boolean)">
<h3>setDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(@Nonnull
 org.eclipse.emf.ecore.resource.Resource resource,
 boolean dirty)</span></div>
<div class="block">Marks given resource dirty</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resource</code> - target element which will become dirty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDirty(com.nomagic.ci.persistence.features.FeatureDataSet,boolean)">
<h3>setDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(@Nonnull
 com.nomagic.ci.persistence.features.FeatureDataSet fd,
 boolean dirty)</span></div>
<div class="block">Marks given resource dirty</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fd</code> - target element which will become dirty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirty(org.eclipse.emf.ecore.resource.Resource)">
<h3>isDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirty</span><wbr/><span class="parameters">(@Nonnull
 org.eclipse.emf.ecore.resource.Resource resource)</span></div>
<div class="block">Check if given resource is dirty in the given project context. Even if
 <code>Resource.isModified()</code> == <code>false</code>, this method can return <code>true</code></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if resource is dirty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isDirty(com.nomagic.magicdraw.uml.BaseElement)">
<h3>isDirty</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirty</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns true if given element has been modified and is not yet saved.
 Individual <a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>PresentationElement</code></a> is not tracked, its <a href="../uml/symbols/AbstractDiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>AbstractDiagramPresentationElement</code></a> is used instead.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element</dd>
<dt>Returns:</dt>
<dd>true if element is dirty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChangedElementsIDS(java.util.Collection)">
<h3>setChangedElementsIDS</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChangedElementsIDS</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAllChangedElementsIDS()">
<h3>getAllChangedElementsIDS</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAllChangedElementsIDS</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>changed during this session + loaded changed ids.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChangedElementsIDS()">
<h3>getChangedElementsIDS</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getChangedElementsIDS</span>()</div>
</section>
</li>
<li>
<section class="detail" id="addToLoadedChangedElementsIDS(java.util.Collection)">
<h3>addToLoadedChangedElementsIDS</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addToLoadedChangedElementsIDS</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; ids)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDirty(com.nomagic.ci.persistence.IProject,boolean)">
<h3>setDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 boolean dirty)</span></div>
</section>
</li>
<li>
<section class="detail" id="setDirty(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">
<h3>setDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirty</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 @CheckForNull
 <a href="StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</span></div>
</section>
</li>
<li>
<section class="detail" id="isDirty(com.nomagic.ci.persistence.IProject)">
<h3>isDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirty</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDirtyType(com.nomagic.ci.persistence.IProject)">
<h3>getDirtyType</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a></span> <span class="element-name">getDirtyType</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="reSetDirty(com.nomagic.ci.persistence.IProject,boolean,com.nomagic.magicdraw.utils.StateChangeHandler.DirtyType)">
<h3>reSetDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reSetDirty</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project,
 boolean dirty,
 @CheckForNull
 <a href="StateChangeHandler.DirtyType.html" title="enum class in com.nomagic.magicdraw.utils">StateChangeHandler.DirtyType</a> dirtyType)</span></div>
</section>
</li>
<li>
<section class="detail" id="isAutoSaveDirty()">
<h3>isAutoSaveDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAutoSaveDirty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAutoSaveDirty(boolean)">
<h3>setAutoSaveDirty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAutoSaveDirty</span><wbr/><span class="parameters">(boolean autoSaveDirty)</span></div>
</section>
</li>
<li>
<section class="detail" id="trackModificationForResource(org.eclipse.emf.ecore.resource.Resource)">
<h3>trackModificationForResource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">trackModificationForResource</span><wbr/><span class="parameters">(@Nonnull
 org.eclipse.emf.ecore.resource.Resource resource)</span></div>
<div class="block">Registers URI for which default dirty resource tracking will be enabled.
 <p>Note, this mechanism is based on EMF track changes</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resource</code> - resource to track changes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
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
