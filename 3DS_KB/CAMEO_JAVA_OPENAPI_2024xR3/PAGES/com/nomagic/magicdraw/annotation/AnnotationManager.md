# JAVA OPENAPI: AnnotationManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/annotation/AnnotationManager.html
- source_path: `com/nomagic/magicdraw/annotation/AnnotationManager.html`
- source_sha256: `0fbb736798ff1d44dd43fd729ce32cd3356d20410c3d4b287e12a13ddba06b5e`
- captured_utc: `2026-07-14T16:55:03.303876+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.annotation](package-summary.html)

## Class AnnotationManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[Project](../core/Project.html)>
com.nomagic.magicdraw.core.project.service.ProjectService
com.nomagic.magicdraw.annotation.AnnotationManager

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`, `[ProjectProvider](../uml/ProjectProvider.html)`

@OpenApiAllpublic final classAnnotationManager
extends com.nomagic.magicdraw.core.project.service.ProjectService
implements [ProjectProvider](../uml/ProjectProvider.html)

Handles annotations visualization on diagrams and other UI components. It takes care of
 drawing decorations around symbols with annotations and provides annotation actions for manipulators.
 Users are responsible for adding annotations and removing added annotations afterwards.
 Users is responsible to call update() method when some annotation is added or removed.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[add](#add(com.nomagic.magicdraw.annotation.Annotation))([Annotation](Annotation.html) annotation)`
Add single annotation.
`boolean`
`[add](#add(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.magicdraw.annotation.AnnotationCategory))([Annotation](Annotation.html) annotation,
 [AnnotationCategory](AnnotationCategory.html) category)`
Add single annotation.
`static void`
`[addAnnotationParentTargetProvider](#addAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider))([AnnotationTargetParentProvider](AnnotationTargetParentProvider.html) provider)`

`void`
`[addListener](#addListener(com.nomagic.magicdraw.annotation.AnnotationManagerListener))([AnnotationManagerListener](AnnotationManagerListener.html) listener)`

`void`
`[disposeService](#disposeService())()`
Designed to be overridden in derived classes
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)>`
`[getAnnotatedElements](#getAnnotatedElements())()`
Returns a collection of annotated elements
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)>`
`[getAnnotatedElements](#getAnnotatedElements(com.nomagic.magicdraw.annotation.AnnotationSubset))([AnnotationSubset](AnnotationSubset.html) subset)`
Returns a collection of annotated elements
`[Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)>`
`[getAnnotatedTargets](#getAnnotatedTargets(com.nomagic.magicdraw.annotation.AnnotationSubset))([AnnotationSubset](AnnotationSubset.html) subset)`
Returns targets of the registered annotations.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotations](#getAnnotations(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Get all annotations for particular element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotations](#getAnnotations(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset))([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotations](#getAnnotations(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotations](#getAnnotations(java.lang.Object,com.nomagic.magicdraw.annotation.AnnotationSubset))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [AnnotationSubset](AnnotationSubset.html) subset)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotationsOfChildren](#getAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotationsOfChildren](#getAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset))([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)`
Get all annotations of children of given element.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotationsOfHiddenChildren](#getAnnotationsOfHiddenChildren(com.nomagic.magicdraw.uml.symbols.PresentationElement))([PresentationElement](../uml/symbols/PresentationElement.html) view)`
Get all annotations of closest hidden children(recursively) of given symbol.
`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)>`
`[getAnnotationsOfHiddenChildren](#getAnnotationsOfHiddenChildren(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.annotation.AnnotationSubset))([PresentationElement](../uml/symbols/PresentationElement.html) view,
 [AnnotationSubset](AnnotationSubset.html) subset)`
Get all annotations of closest hidden children(recursively) of given symbol.
`static [AnnotationManager](AnnotationManager.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.core.Project))([Project](../core/Project.html) project)`

`static [AnnotationManager](AnnotationManager.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`

`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[BaseElement](../uml/BaseElement.html)>`
`[getIteratorOfAnnotatedElements](#getIteratorOfAnnotatedElements(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) owner)`
Returns a collection of annotated elements
`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Annotation](Annotation.html)>`
`[getIteratorOfAnnotationsOfChildren](#getIteratorOfAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`

`[Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Annotation](Annotation.html)>`
`[getIteratorOfAnnotationsOfChildren](#getIteratorOfAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset))([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)`

`[Project](../core/Project.html)`
`[getProject](#getProject())()`

`static [Project](../core/Project.html)`
`[getProject](#getProject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) annotationTarget)`
Used to retrieve project from element or parent target providers if given object is not element.
`boolean`
`[hasAnnotatedChildren](#hasAnnotatedChildren(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../uml/BaseElement.html) element)`
Test if given element has children (recursively) with some annotations.
`boolean`
`[hasAnnotatedChildren](#hasAnnotatedChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset))([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)`
Test if given element has children (recursively) with some annotations.
`boolean`
`[hasAnnotations](#hasAnnotations())()`

`boolean`
`[hasAnnotations](#hasAnnotations(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset))([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)`

`boolean`
`[hasAnnotations](#hasAnnotations(java.lang.Object,com.nomagic.magicdraw.annotation.AnnotationSubset))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [AnnotationSubset](AnnotationSubset.html) subset)`

`void`
`[registerSubset](#registerSubset(com.nomagic.magicdraw.annotation.AnnotationSubset))([AnnotationSubset](AnnotationSubset.html) subset)`
Register subset (part) of annotations.
`boolean`
`[remove](#remove(com.nomagic.magicdraw.annotation.Annotation))([Annotation](Annotation.html) annotation)`
Remove single annotation.
`static void`
`[removeAnnotationParentTargetProvider](#removeAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider))([AnnotationTargetParentProvider](AnnotationTargetParentProvider.html) provider)`

`void`
`[removeListener](#removeListener(com.nomagic.magicdraw.annotation.AnnotationManagerListener))([AnnotationManagerListener](AnnotationManagerListener.html) listener)`

`void`
`[unregisterSubset](#unregisterSubset(com.nomagic.magicdraw.annotation.AnnotationSubset))([AnnotationSubset](AnnotationSubset.html) subset)`

`void`
`[update](#update())()`
Repaint opened diagrams and active browser tree.
`void`
`[update](#update(boolean))(boolean repaintBrowserTree)`
Repaint opened diagrams and (optionally) active browser tree.
`void`
`[update](#update(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Annotation](Annotation.html)> removed,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> added)`
Updates annotation manager using specified data.
`void`
`[update](#update(java.util.Collection,java.util.Collection,com.nomagic.magicdraw.annotation.AnnotationCategory))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Annotation](Annotation.html)> removed,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> added,
 [AnnotationCategory](AnnotationCategory.html) category)`
Updates annotation manager using specified data.
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
addAnnotationParentTargetProvider
public static void addAnnotationParentTargetProvider([AnnotationTargetParentProvider](AnnotationTargetParentProvider.html) provider)
removeAnnotationParentTargetProvider
public static void removeAnnotationParentTargetProvider([AnnotationTargetParentProvider](AnnotationTargetParentProvider.html) provider)
getInstance
public static [AnnotationManager](AnnotationManager.html) getInstance([BaseElement](../uml/BaseElement.html) element)
getInstance
public static [AnnotationManager](AnnotationManager.html) getInstance([Project](../core/Project.html) project)
add
public boolean add([Annotation](Annotation.html) annotation)
Add single annotation. Annotation may not be visible
 until the [`update()`](#update()) method has been called.
Parameters:
`annotation` - annotation to add
Returns:
true if annotation was added, false if such annotation already exists
add
public boolean add([Annotation](Annotation.html) annotation,
 [AnnotationCategory](AnnotationCategory.html) category)
Add single annotation. Annotation may not be visible
 until the [`update()`](#update()) method has been called.
Parameters:
`annotation` - annotation to add
`category` - category to which this annotation belongs. Each category can be part of various AnnotationSubsets
Returns:
true if annotation was added, false if such annotation already exists
remove
public boolean remove([Annotation](Annotation.html) annotation)
Remove single annotation. Changes may not be visible
 until the [`update()`](#update()) method has been called.
Parameters:
`annotation` - annotation to remove
Returns:
true if annotation was removed, false if such annotation was not added before
hasAnnotatedChildren
public boolean hasAnnotatedChildren(@CheckForNull
 [BaseElement](../uml/BaseElement.html) element)
Test if given element has children (recursively) with some annotations.
Parameters:
`element` - given element
Returns:
true if there are at least one annotated child of given element
hasAnnotatedChildren
public boolean hasAnnotatedChildren(@CheckForNull
 [BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)
Test if given element has children (recursively) with some annotations.
Parameters:
`element` - given element
`subset` - subset (part) of all currently registered annotations to check.
Returns:
true if there are at least one annotated child of given element
getAnnotationsOfChildren
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotationsOfChildren([BaseElement](../uml/BaseElement.html) element)
getAnnotationsOfChildren
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotationsOfChildren([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)
Get all annotations of children of given element. Also includes informationFlows for given element.
Parameters:
`element` - given element
`subset` - subset (part) of all currently registered children annotations to retrieve
Returns:
list of annotations sorted by severity.
getAnnotationsOfHiddenChildren
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotationsOfHiddenChildren([PresentationElement](../uml/symbols/PresentationElement.html) view)
Get all annotations of closest hidden children(recursively) of given symbol. Also includes InformationFlows of
 given element, that has conveyed Info.
Parameters:
`view` - symbol of starting PE. dedicated to find closest hidden elements for diagrams.
Returns:
list of annotations sorted by severity.
getAnnotationsOfHiddenChildren
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotationsOfHiddenChildren([PresentationElement](../uml/symbols/PresentationElement.html) view,
 [AnnotationSubset](AnnotationSubset.html) subset)
Get all annotations of closest hidden children(recursively) of given symbol. Also includes InformationFlows of
 given element, that has conveyed Info.
Parameters:
`view` - symbol of starting PE. dedicated to find closest hidden elements for diagrams.
`subset` - subset (part) of all currently registered hidden children annotations to check.
Returns:
list of annotations sorted by severity.
getAnnotations
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotations([BaseElement](../uml/BaseElement.html) element)
Get all annotations for particular element.
Parameters:
`element` - element to get annotations for
Returns:
unmodifiable list of annotations
getAnnotations
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotations([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)
Parameters:
`element` - element to get annotations for
`subset` - subset (part) of all currently registered annotations to retrieve.
Returns:
unmodifiable subset of element's annotations
getAnnotations
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotations([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target)
getAnnotations
public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Annotation](Annotation.html)> getAnnotations([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [AnnotationSubset](AnnotationSubset.html) subset)
hasAnnotations
public boolean hasAnnotations([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)
Returns:
true if there is one or more annotation added for the given element
hasAnnotations
public boolean hasAnnotations([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) target,
 [AnnotationSubset](AnnotationSubset.html) subset)
update
public void update()
Repaint opened diagrams and active browser tree.
 Fires updated event to registered listeners.
update
public void update(boolean repaintBrowserTree)
Repaint opened diagrams and (optionally) active browser tree.
 Fires updated event to registered listeners.
Parameters:
`repaintBrowserTree` - true to repaint active browser tree (e.g. containment).
disposeService
public void disposeService()
Description copied from class: `com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService`
Designed to be overridden in derived classes
Specified by:
`disposeService` in interface `com.dassault_systemes.modeler.foundation.project.service.DisposableService`
Overrides:
`disposeService` in class `com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[Project](../core/Project.html)>`
getProject
public static [Project](../core/Project.html) getProject([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) annotationTarget)
Used to retrieve project from element or parent target providers if given object is not element.
Parameters:
`annotationTarget` - annotation target
Returns:
project which annotation target exists in
getAnnotatedElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)> getAnnotatedElements()
Returns a collection of annotated elements
Returns:
all annotated elements
getAnnotatedElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[BaseElement](../uml/BaseElement.html)> getAnnotatedElements([AnnotationSubset](AnnotationSubset.html) subset)
Returns a collection of annotated elements
Parameters:
`subset` - subset (part) of all currently registered annotations to take into account.
Returns:
elements that have registered annotations belonging to the given subset
getAnnotatedTargets
public [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> getAnnotatedTargets([AnnotationSubset](AnnotationSubset.html) subset)
Returns targets of the registered annotations.
Parameters:
`subset` - subset (part) of all currently registered annotations to take into account.
Returns:
all targets that have registered annotations belonging to the given subset
getIteratorOfAnnotatedElements
public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[BaseElement](../uml/BaseElement.html)> getIteratorOfAnnotatedElements(@CheckForNull
 [BaseElement](../uml/BaseElement.html) owner)
Returns a collection of annotated elements
Returns:
all annotated elements
update
public void update([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Annotation](Annotation.html)> removed,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> added)
Updates annotation manager using specified data. No need to call update() method.
Parameters:
`removed` - collection of removed annotations.
`added` - collection of added annotations.
update
public void update([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Annotation](Annotation.html)> removed,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Annotation](Annotation.html)> added,
 [AnnotationCategory](AnnotationCategory.html) category)
Updates annotation manager using specified data. No need to call update() method.
Parameters:
`removed` - collection of removed annotations.
`added` - collection of added annotations.
`category` - category to which annotations belongs
addListener
public void addListener([AnnotationManagerListener](AnnotationManagerListener.html) listener)
removeListener
public void removeListener([AnnotationManagerListener](AnnotationManagerListener.html) listener)
hasAnnotations
public boolean hasAnnotations()
getIteratorOfAnnotationsOfChildren
public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Annotation](Annotation.html)> getIteratorOfAnnotationsOfChildren([BaseElement](../uml/BaseElement.html) element)
getIteratorOfAnnotationsOfChildren
public [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<[Annotation](Annotation.html)> getIteratorOfAnnotationsOfChildren([BaseElement](../uml/BaseElement.html) element,
 [AnnotationSubset](AnnotationSubset.html) subset)
registerSubset
public void registerSubset([AnnotationSubset](AnnotationSubset.html) subset)
Register subset (part) of annotations. This enables caching annotations by all the containing subsets.
 Only subsets, registered using this method, should be be used when retrieving annotations from the manager.
unregisterSubset
public void unregisterSubset([AnnotationSubset](AnnotationSubset.html) subset)
getProject
public [Project](../core/Project.html) getProject()
Specified by:
`[getProject](../uml/ProjectProvider.html#getProject())` in interface `[ProjectProvider](../uml/ProjectProvider.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.annotation</a></div>
<h1 class="title" title="Class AnnotationManager">Class AnnotationManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;
<div class="inheritance">com.nomagic.magicdraw.core.project.service.ProjectService
<div class="inheritance">com.nomagic.magicdraw.annotation.AnnotationManager</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code>, <code><a href="../uml/ProjectProvider.html" title="interface in com.nomagic.magicdraw.uml">ProjectProvider</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">AnnotationManager</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.project.service.ProjectService
implements <a href="../uml/ProjectProvider.html" title="interface in com.nomagic.magicdraw.uml">ProjectProvider</a></span></div>
<div class="block">Handles annotations visualization on diagrams and other UI components. It takes care of
 drawing decorations around symbols with annotations and provides annotation actions for manipulators.
 Users are responsible for adding annotations and removing added annotations afterwards.
 Users is responsible to call update() method when some annotation is added or removed.</div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.nomagic.magicdraw.annotation.Annotation)">add</a><wbr/>(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add single annotation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#add(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.magicdraw.annotation.AnnotationCategory)">add</a><wbr/>(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 <a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a> category)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add single annotation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider)">addAnnotationParentTargetProvider</a><wbr/>(<a href="AnnotationTargetParentProvider.html" title="interface in com.nomagic.magicdraw.annotation">AnnotationTargetParentProvider</a> provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addListener(com.nomagic.magicdraw.annotation.AnnotationManagerListener)">addListener</a><wbr/>(<a href="AnnotationManagerListener.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManagerListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disposeService()">disposeService</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Designed to be overridden in derived classes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotatedElements()">getAnnotatedElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a collection of annotated elements</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotatedElements(com.nomagic.magicdraw.annotation.AnnotationSubset)">getAnnotatedElements</a><wbr/>(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a collection of annotated elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotatedTargets(com.nomagic.magicdraw.annotation.AnnotationSubset)">getAnnotatedTargets</a><wbr/>(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns targets of the registered annotations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotations(com.nomagic.magicdraw.uml.BaseElement)">getAnnotations</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all annotations for particular element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotations(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">getAnnotations</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotations(java.lang.Object)">getAnnotations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotations(java.lang.Object,com.nomagic.magicdraw.annotation.AnnotationSubset)">getAnnotations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement)">getAnnotationsOfChildren</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">getAnnotationsOfChildren</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all annotations of children of given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotationsOfHiddenChildren(com.nomagic.magicdraw.uml.symbols.PresentationElement)">getAnnotationsOfHiddenChildren</a><wbr/>(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all annotations of closest hidden children(recursively) of given symbol.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnnotationsOfHiddenChildren(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">getAnnotationsOfHiddenChildren</a><wbr/>(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get all annotations of closest hidden children(recursively) of given symbol.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.core.Project)">getInstance</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIteratorOfAnnotatedElements(com.nomagic.magicdraw.uml.BaseElement)">getIteratorOfAnnotatedElements</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a collection of annotated elements</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIteratorOfAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement)">getIteratorOfAnnotationsOfChildren</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIteratorOfAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">getIteratorOfAnnotationsOfChildren</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject(java.lang.Object)">getProject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> annotationTarget)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Used to retrieve project from element or parent target providers if given object is not element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasAnnotatedChildren(com.nomagic.magicdraw.uml.BaseElement)">hasAnnotatedChildren</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test if given element has children (recursively) with some annotations.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasAnnotatedChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">hasAnnotatedChildren</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Test if given element has children (recursively) with some annotations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasAnnotations()">hasAnnotations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasAnnotations(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">hasAnnotations</a><wbr/>(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hasAnnotations(java.lang.Object,com.nomagic.magicdraw.annotation.AnnotationSubset)">hasAnnotations</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#registerSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">registerSubset</a><wbr/>(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Register subset (part) of annotations.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#remove(com.nomagic.magicdraw.annotation.Annotation)">remove</a><wbr/>(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Remove single annotation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider)">removeAnnotationParentTargetProvider</a><wbr/>(<a href="AnnotationTargetParentProvider.html" title="interface in com.nomagic.magicdraw.annotation">AnnotationTargetParentProvider</a> provider)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeListener(com.nomagic.magicdraw.annotation.AnnotationManagerListener)">removeListener</a><wbr/>(<a href="AnnotationManagerListener.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManagerListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#unregisterSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">unregisterSubset</a><wbr/>(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#update()">update</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Repaint opened diagrams and active browser tree.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#update(boolean)">update</a><wbr/>(boolean repaintBrowserTree)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Repaint opened diagrams and (optionally) active browser tree.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#update(java.util.Collection,java.util.Collection)">update</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; removed,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; added)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates annotation manager using specified data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#update(java.util.Collection,java.util.Collection,com.nomagic.magicdraw.annotation.AnnotationCategory)">update</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; removed,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; added,
 <a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a> category)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Updates annotation manager using specified data.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
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
<section class="detail" id="addAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider)">
<h3>addAnnotationParentTargetProvider</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">addAnnotationParentTargetProvider</span><wbr/><span class="parameters">(<a href="AnnotationTargetParentProvider.html" title="interface in com.nomagic.magicdraw.annotation">AnnotationTargetParentProvider</a> provider)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeAnnotationParentTargetProvider(com.nomagic.magicdraw.annotation.AnnotationTargetParentProvider)">
<h3>removeAnnotationParentTargetProvider</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeAnnotationParentTargetProvider</span><wbr/><span class="parameters">(<a href="AnnotationTargetParentProvider.html" title="interface in com.nomagic.magicdraw.annotation">AnnotationTargetParentProvider</a> provider)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManager</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.core.Project)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="AnnotationManager.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManager</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
</section>
</li>
<li>
<section class="detail" id="add(com.nomagic.magicdraw.annotation.Annotation)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</span></div>
<div class="block">Add single annotation. Annotation may not be visible
 until the <a href="#update()"><code>update()</code></a> method has been called.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - annotation to add</dd>
<dt>Returns:</dt>
<dd>true if annotation was added, false if such annotation already exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="add(com.nomagic.magicdraw.annotation.Annotation,com.nomagic.magicdraw.annotation.AnnotationCategory)">
<h3>add</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">add</span><wbr/><span class="parameters">(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation,
 <a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a> category)</span></div>
<div class="block">Add single annotation. Annotation may not be visible
 until the <a href="#update()"><code>update()</code></a> method has been called.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - annotation to add</dd>
<dd><code>category</code> - category to which this annotation belongs. Each category can be part of various AnnotationSubsets</dd>
<dt>Returns:</dt>
<dd>true if annotation was added, false if such annotation already exists</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="remove(com.nomagic.magicdraw.annotation.Annotation)">
<h3>remove</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">remove</span><wbr/><span class="parameters">(<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a> annotation)</span></div>
<div class="block">Remove single annotation. Changes may not be visible
 until the <a href="#update()"><code>update()</code></a> method has been called.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotation</code> - annotation to remove</dd>
<dt>Returns:</dt>
<dd>true if annotation was removed, false if such annotation was not added before</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasAnnotatedChildren(com.nomagic.magicdraw.uml.BaseElement)">
<h3>hasAnnotatedChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAnnotatedChildren</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Test if given element has children (recursively) with some annotations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dt>Returns:</dt>
<dd>true if there are at least one annotated child of given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasAnnotatedChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>hasAnnotatedChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAnnotatedChildren</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<div class="block">Test if given element has children (recursively) with some annotations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dd><code>subset</code> - subset (part) of all currently registered annotations to check.</dd>
<dt>Returns:</dt>
<dd>true if there are at least one annotated child of given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getAnnotationsOfChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotationsOfChildren</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>getAnnotationsOfChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotationsOfChildren</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<div class="block">Get all annotations of children of given element. Also includes informationFlows for given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - given element</dd>
<dd><code>subset</code> - subset (part) of all currently registered children annotations to retrieve</dd>
<dt>Returns:</dt>
<dd>list of annotations sorted by severity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotationsOfHiddenChildren(com.nomagic.magicdraw.uml.symbols.PresentationElement)">
<h3>getAnnotationsOfHiddenChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotationsOfHiddenChildren</span><wbr/><span class="parameters">(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view)</span></div>
<div class="block">Get all annotations of closest hidden children(recursively) of given symbol. Also includes InformationFlows of
 given element, that has conveyed Info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol of starting PE. dedicated to find closest hidden elements for diagrams.</dd>
<dt>Returns:</dt>
<dd>list of annotations sorted by severity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotationsOfHiddenChildren(com.nomagic.magicdraw.uml.symbols.PresentationElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>getAnnotationsOfHiddenChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotationsOfHiddenChildren</span><wbr/><span class="parameters">(<a href="../uml/symbols/PresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols">PresentationElement</a> view,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<div class="block">Get all annotations of closest hidden children(recursively) of given symbol. Also includes InformationFlows of
 given element, that has conveyed Info.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>view</code> - symbol of starting PE. dedicated to find closest hidden elements for diagrams.</dd>
<dd><code>subset</code> - subset (part) of all currently registered hidden children annotations to check.</dd>
<dt>Returns:</dt>
<dd>list of annotations sorted by severity.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotations(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotations</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Get all annotations for particular element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to get annotations for</dd>
<dt>Returns:</dt>
<dd>unmodifiable list of annotations</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotations(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>getAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotations</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to get annotations for</dd>
<dd><code>subset</code> - subset (part) of all currently registered annotations to retrieve.</dd>
<dt>Returns:</dt>
<dd>unmodifiable subset of element's annotations</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotations(java.lang.Object)">
<h3>getAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAnnotations(java.lang.Object,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>getAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getAnnotations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasAnnotations(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>hasAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAnnotations</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if there is one or more annotation added for the given element</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasAnnotations(java.lang.Object,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>hasAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAnnotations</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> target,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
</section>
</li>
<li>
<section class="detail" id="update()">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span>()</div>
<div class="block">Repaint opened diagrams and active browser tree.
 Fires updated event to registered listeners.</div>
</section>
</li>
<li>
<section class="detail" id="update(boolean)">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span><wbr/><span class="parameters">(boolean repaintBrowserTree)</span></div>
<div class="block">Repaint opened diagrams and (optionally) active browser tree.
 Fires updated event to registered listeners.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>repaintBrowserTree</code> - true to repaint active browser tree (e.g. containment).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disposeService()">
<h3>disposeService</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disposeService</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code>com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</code></span></div>
<div class="block">Designed to be overridden in derived classes</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>disposeService</code> in interface <code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
<dt>Overrides:</dt>
<dd><code>disposeService</code> in class <code>com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject(java.lang.Object)">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> annotationTarget)</span></div>
<div class="block">Used to retrieve project from element or parent target providers if given object is not element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>annotationTarget</code> - annotation target</dd>
<dt>Returns:</dt>
<dd>project which annotation target exists in</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotatedElements()">
<h3>getAnnotatedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getAnnotatedElements</span>()</div>
<div class="block">Returns a collection of annotated elements</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all annotated elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotatedElements(com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>getAnnotatedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getAnnotatedElements</span><wbr/><span class="parameters">(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<div class="block">Returns a collection of annotated elements</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subset</code> - subset (part) of all currently registered annotations to take into account.</dd>
<dt>Returns:</dt>
<dd>elements that have registered annotations belonging to the given subset</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnnotatedTargets(com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>getAnnotatedTargets</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt;</span> <span class="element-name">getAnnotatedTargets</span><wbr/><span class="parameters">(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<div class="block">Returns targets of the registered annotations.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>subset</code> - subset (part) of all currently registered annotations to take into account.</dd>
<dt>Returns:</dt>
<dd>all targets that have registered annotations belonging to the given subset</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIteratorOfAnnotatedElements(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getIteratorOfAnnotatedElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a>&gt;</span> <span class="element-name">getIteratorOfAnnotatedElements</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> owner)</span></div>
<div class="block">Returns a collection of annotated elements</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all annotated elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="update(java.util.Collection,java.util.Collection)">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; removed,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; added)</span></div>
<div class="block">Updates annotation manager using specified data. No need to call update() method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>removed</code> - collection of removed annotations.</dd>
<dd><code>added</code> - collection of added annotations.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="update(java.util.Collection,java.util.Collection,com.nomagic.magicdraw.annotation.AnnotationCategory)">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; removed,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt; added,
 <a href="AnnotationCategory.html" title="class in com.nomagic.magicdraw.annotation">AnnotationCategory</a> category)</span></div>
<div class="block">Updates annotation manager using specified data. No need to call update() method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>removed</code> - collection of removed annotations.</dd>
<dd><code>added</code> - collection of added annotations.</dd>
<dd><code>category</code> - category to which annotations belongs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addListener(com.nomagic.magicdraw.annotation.AnnotationManagerListener)">
<h3>addListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addListener</span><wbr/><span class="parameters">(<a href="AnnotationManagerListener.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManagerListener</a> listener)</span></div>
</section>
</li>
<li>
<section class="detail" id="removeListener(com.nomagic.magicdraw.annotation.AnnotationManagerListener)">
<h3>removeListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeListener</span><wbr/><span class="parameters">(<a href="AnnotationManagerListener.html" title="class in com.nomagic.magicdraw.annotation">AnnotationManagerListener</a> listener)</span></div>
</section>
</li>
<li>
<section class="detail" id="hasAnnotations()">
<h3>hasAnnotations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">hasAnnotations</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getIteratorOfAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getIteratorOfAnnotationsOfChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getIteratorOfAnnotationsOfChildren</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getIteratorOfAnnotationsOfChildren(com.nomagic.magicdraw.uml.BaseElement,com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>getIteratorOfAnnotationsOfChildren</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a href="Annotation.html" title="class in com.nomagic.magicdraw.annotation">Annotation</a>&gt;</span> <span class="element-name">getIteratorOfAnnotationsOfChildren</span><wbr/><span class="parameters">(<a href="../uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element,
 <a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
</section>
</li>
<li>
<section class="detail" id="registerSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>registerSubset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">registerSubset</span><wbr/><span class="parameters">(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
<div class="block">Register subset (part) of annotations. This enables caching annotations by all the containing subsets.
 Only subsets, registered using this method, should be be used when retrieving annotations from the manager.</div>
</section>
</li>
<li>
<section class="detail" id="unregisterSubset(com.nomagic.magicdraw.annotation.AnnotationSubset)">
<h3>unregisterSubset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">unregisterSubset</span><wbr/><span class="parameters">(<a href="AnnotationSubset.html" title="class in com.nomagic.magicdraw.annotation">AnnotationSubset</a> subset)</span></div>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../uml/ProjectProvider.html#getProject()">getProject</a></code> in interface <code><a href="../uml/ProjectProvider.html" title="interface in com.nomagic.magicdraw.uml">ProjectProvider</a></code></dd>
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
