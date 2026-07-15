# JAVA OPENAPI: ViewsLibrary (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/dassault_systemes/modeler/sysml/libraries/standard/ViewsLibrary.html
- source_path: `com/dassault_systemes/modeler/sysml/libraries/standard/ViewsLibrary.html`
- source_sha256: `2b6ab345d7b0499e5f84f121d16427c99f3f47f56190ae26fa104cc1968abbd3`
- captured_utc: `2026-07-14T16:45:02.126035+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.dassault_systemes.modeler.sysml.libraries.standard](package-summary.html)

## Class ViewsLibrary

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService<[ModelElementProject](../../../foundation/project/ModelElementProject.html)>
[com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
com.dassault_systemes.modeler.sysml.libraries.standard.ViewsLibrary

All Implemented Interfaces:
`com.dassault_systemes.modeler.foundation.project.service.DisposableService`

@OpenApiAllpublic classViewsLibrary
extends [AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)

Access helper for the views standard library.

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ViewsLibrary.AsInterconnectionDiagramRenderingUsage](ViewsLibrary.AsInterconnectionDiagramRenderingUsage.html)`
Wrapper for the as interconnection diagram rendering usage library element.
`static class`
`[ViewsLibrary.AsTextualNotationRenderingUsage](ViewsLibrary.AsTextualNotationRenderingUsage.html)`
Wrapper for the as textual notation rendering usage library element.
`static class`
`[ViewsLibrary.AsTreeDiagramRenderingUsage](ViewsLibrary.AsTreeDiagramRenderingUsage.html)`
Wrapper for the as tree diagram rendering usage library element.
`static class`
`[ViewsLibrary.GraphicalRenderingRenderingDefinition](ViewsLibrary.GraphicalRenderingRenderingDefinition.html)`
Wrapper for the graphical rendering rendering definition library element.
`static class`
`[ViewsLibrary.RenderingRenderingDefinition](ViewsLibrary.RenderingRenderingDefinition.html)`
Wrapper for the rendering rendering definition library element.
`static class`
`[ViewsLibrary.RenderingsRenderingUsage](ViewsLibrary.RenderingsRenderingUsage.html)`
Wrapper for the renderings rendering usage library element.
`static class`
`[ViewsLibrary.TabularRenderingRenderingDefinition](ViewsLibrary.TabularRenderingRenderingDefinition.html)`
Wrapper for the tabular rendering rendering definition library element.
`static class`
`[ViewsLibrary.TextualRenderingRenderingDefinition](ViewsLibrary.TextualRenderingRenderingDefinition.html)`
Wrapper for the textual rendering rendering definition library element.
`static class`
`[ViewsLibrary.ViewpointChecksViewpointUsage](ViewsLibrary.ViewpointChecksViewpointUsage.html)`
Wrapper for the viewpoint checks viewpoint usage library element.
`static class`
`[ViewsLibrary.ViewpointCheckViewpointDefinition](ViewsLibrary.ViewpointCheckViewpointDefinition.html)`
Wrapper for the viewpoint check viewpoint definition library element.
`static class`
`[ViewsLibrary.ViewsViewUsage](ViewsLibrary.ViewsViewUsage.html)`
Wrapper for the views view usage library element.
`static class`
`[ViewsLibrary.ViewViewDefinition](ViewsLibrary.ViewViewDefinition.html)`
Wrapper for the view view definition library element.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ViewsLibrary](#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Creates a new views library instance.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[ViewsLibrary.AsInterconnectionDiagramRenderingUsage](ViewsLibrary.AsInterconnectionDiagramRenderingUsage.html)`
`[asInterconnectionDiagram](#asInterconnectionDiagram())()`
Returns as interconnection diagram.
`[ViewsLibrary.AsTextualNotationRenderingUsage](ViewsLibrary.AsTextualNotationRenderingUsage.html)`
`[asTextualNotation](#asTextualNotation())()`
Returns as textual notation.
`[ViewsLibrary.AsTreeDiagramRenderingUsage](ViewsLibrary.AsTreeDiagramRenderingUsage.html)`
`[asTreeDiagram](#asTreeDiagram())()`
Returns as tree diagram.
`static [ViewsLibrary](ViewsLibrary.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)`
Returns the library instance for the project that owns the given element.
`static [ViewsLibrary](ViewsLibrary.html)`
`[getInstanceByProject](#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject))([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)`
Returns the library instance for the given project.
`protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper>`
`[getTypeWrappers](#getTypeWrappers())()`
Returns get type wrappers.
`[ViewsLibrary.GraphicalRenderingRenderingDefinition](ViewsLibrary.GraphicalRenderingRenderingDefinition.html)`
`[GraphicalRendering](#GraphicalRendering())()`
Returns graphical rendering.
`boolean`
`[isSemantic](#isSemantic())()`
Returns whether this library is semantic.
`protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[packagesNames](#packagesNames())()`
Returns the names of the packages that belong to this library.
`[ViewsLibrary.RenderingRenderingDefinition](ViewsLibrary.RenderingRenderingDefinition.html)`
`[Rendering](#Rendering())()`
Returns rendering.
`[ViewsLibrary.RenderingsRenderingUsage](ViewsLibrary.RenderingsRenderingUsage.html)`
`[renderings](#renderings())()`
Returns renderings.
`[ViewsLibrary.TabularRenderingRenderingDefinition](ViewsLibrary.TabularRenderingRenderingDefinition.html)`
`[TabularRendering](#TabularRendering())()`
Returns tabular rendering.
`[ViewsLibrary.TextualRenderingRenderingDefinition](ViewsLibrary.TextualRenderingRenderingDefinition.html)`
`[TextualRendering](#TextualRendering())()`
Returns textual rendering.
`[ViewsLibrary.ViewViewDefinition](ViewsLibrary.ViewViewDefinition.html)`
`[View](#View())()`
Returns view.
`[ViewsLibrary.ViewpointCheckViewpointDefinition](ViewsLibrary.ViewpointCheckViewpointDefinition.html)`
`[ViewpointCheck](#ViewpointCheck())()`
Returns viewpoint check.
`[ViewsLibrary.ViewpointChecksViewpointUsage](ViewsLibrary.ViewpointChecksViewpointUsage.html)`
`[viewpointChecks](#viewpointChecks())()`
Returns viewpoint checks.
`[ViewsLibrary.ViewsViewUsage](ViewsLibrary.ViewsViewUsage.html)`
`[views](#views())()`
Returns views.
Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)
`[findFunctionInLibrary](../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)), [findLibraryPackage](../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)), [findPackage](../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)), [getLibraryPackages](../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()), [getNamespace](../../../kerml/libraries/AbstractLibrary.html#getNamespace()), [initialized](../../../kerml/libraries/AbstractLibrary.html#initialized())`
Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService
`disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ViewsLibrary
public ViewsLibrary([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Creates a new views library instance.
Parameters:
`project` - the project
 ============ METHOD DETAIL ========== 
Method Details
getInstanceByProject
public static [ViewsLibrary](ViewsLibrary.html) getInstanceByProject([ModelElementProject](../../../foundation/project/ModelElementProject.html) project)
Returns the library instance for the given project.
Parameters:
`project` - the project
Returns:
get instance by project
getInstance
public static [ViewsLibrary](ViewsLibrary.html) getInstance([BaseElement](../../../../../nomagic/magicdraw/uml/BaseElement.html) element)
Returns the library instance for the project that owns the given element.
Parameters:
`element` - the element
Returns:
get instance
isSemantic
public boolean isSemantic()
Returns whether this library is semantic.
Specified by:
`[isSemantic](../../../kerml/libraries/AbstractLibrary.html#isSemantic())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
`true` if semantic; `false` otherwise
packagesNames
protected [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> packagesNames()
Returns the names of the packages that belong to this library.
Specified by:
`[packagesNames](../../../kerml/libraries/AbstractLibrary.html#packagesNames())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
packages names
View
public [ViewsLibrary.ViewViewDefinition](ViewsLibrary.ViewViewDefinition.html) View()
Returns view.
Returns:
view
ViewpointCheck
public [ViewsLibrary.ViewpointCheckViewpointDefinition](ViewsLibrary.ViewpointCheckViewpointDefinition.html) ViewpointCheck()
Returns viewpoint check.
Returns:
viewpoint check
Rendering
public [ViewsLibrary.RenderingRenderingDefinition](ViewsLibrary.RenderingRenderingDefinition.html) Rendering()
Returns rendering.
Returns:
rendering
TextualRendering
public [ViewsLibrary.TextualRenderingRenderingDefinition](ViewsLibrary.TextualRenderingRenderingDefinition.html) TextualRendering()
Returns textual rendering.
Returns:
textual rendering
GraphicalRendering
public [ViewsLibrary.GraphicalRenderingRenderingDefinition](ViewsLibrary.GraphicalRenderingRenderingDefinition.html) GraphicalRendering()
Returns graphical rendering.
Returns:
graphical rendering
TabularRendering
public [ViewsLibrary.TabularRenderingRenderingDefinition](ViewsLibrary.TabularRenderingRenderingDefinition.html) TabularRendering()
Returns tabular rendering.
Returns:
tabular rendering
views
public [ViewsLibrary.ViewsViewUsage](ViewsLibrary.ViewsViewUsage.html) views()
Returns views.
Returns:
views
viewpointChecks
public [ViewsLibrary.ViewpointChecksViewpointUsage](ViewsLibrary.ViewpointChecksViewpointUsage.html) viewpointChecks()
Returns viewpoint checks.
Returns:
viewpoint checks
renderings
public [ViewsLibrary.RenderingsRenderingUsage](ViewsLibrary.RenderingsRenderingUsage.html) renderings()
Returns renderings.
Returns:
renderings
asTextualNotation
public [ViewsLibrary.AsTextualNotationRenderingUsage](ViewsLibrary.AsTextualNotationRenderingUsage.html) asTextualNotation()
Returns as textual notation.
Returns:
as textual notation
asTreeDiagram
public [ViewsLibrary.AsTreeDiagramRenderingUsage](ViewsLibrary.AsTreeDiagramRenderingUsage.html) asTreeDiagram()
Returns as tree diagram.
Returns:
as tree diagram
asInterconnectionDiagram
public [ViewsLibrary.AsInterconnectionDiagramRenderingUsage](ViewsLibrary.AsInterconnectionDiagramRenderingUsage.html) asInterconnectionDiagram()
Returns as interconnection diagram.
Returns:
as interconnection diagram
getTypeWrappers
protected final [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.dassault_systemes.modeler.kerml.libraries.TypeWrapper> getTypeWrappers()
Returns get type wrappers.
Specified by:
`[getTypeWrappers](../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers())` in class `[AbstractLibrary](../../../kerml/libraries/AbstractLibrary.html)`
Returns:
get type wrappers

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.dassault_systemes.modeler.sysml.libraries.standard</a></div>
<h1 class="title" title="Class ViewsLibrary">Class ViewsLibrary</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService&lt;<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a>&gt;
<div class="inheritance"><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary</a>
<div class="inheritance">com.dassault_systemes.modeler.sysml.libraries.standard.ViewsLibrary</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.dassault_systemes.modeler.foundation.project.service.DisposableService</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ViewsLibrary</span>
<span class="extends-implements">extends <a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></span></div>
<div class="block">Access helper for the views standard library.</div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="ViewsLibrary.AsInterconnectionDiagramRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsInterconnectionDiagramRenderingUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the as interconnection diagram rendering usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ViewsLibrary.AsTextualNotationRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsTextualNotationRenderingUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the as textual notation rendering usage library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ViewsLibrary.AsTreeDiagramRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsTreeDiagramRenderingUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the as tree diagram rendering usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ViewsLibrary.GraphicalRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.GraphicalRenderingRenderingDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the graphical rendering rendering definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ViewsLibrary.RenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.RenderingRenderingDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the rendering rendering definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ViewsLibrary.RenderingsRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.RenderingsRenderingUsage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the renderings rendering usage library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ViewsLibrary.TabularRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.TabularRenderingRenderingDefinition</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the tabular rendering rendering definition library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ViewsLibrary.TextualRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.TextualRenderingRenderingDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the textual rendering rendering definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ViewsLibrary.ViewpointChecksViewpointUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewpointChecksViewpointUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the viewpoint checks viewpoint usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ViewsLibrary.ViewpointCheckViewpointDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewpointCheckViewpointDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the viewpoint check viewpoint definition library element.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ViewsLibrary.ViewsViewUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewsViewUsage</a></code></div>
<div class="col-last even-row-color">
<div class="block">Wrapper for the views view usage library element.</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ViewsLibrary.ViewViewDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewViewDefinition</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Wrapper for the view view definition library element.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">ViewsLibrary</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new views library instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.AsInterconnectionDiagramRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsInterconnectionDiagramRenderingUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#asInterconnectionDiagram()">asInterconnectionDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns as interconnection diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.AsTextualNotationRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsTextualNotationRenderingUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#asTextualNotation()">asTextualNotation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns as textual notation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.AsTreeDiagramRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsTreeDiagramRenderingUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#asTreeDiagram()">asTreeDiagram</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns as tree diagram.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ViewsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the project that owns the given element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ViewsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">getInstanceByProject</a><wbr/>(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the library instance for the given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTypeWrappers()">getTypeWrappers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns get type wrappers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.GraphicalRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.GraphicalRenderingRenderingDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#GraphicalRendering()">GraphicalRendering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns graphical rendering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSemantic()">isSemantic</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns whether this library is semantic.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#packagesNames()">packagesNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the names of the packages that belong to this library.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.RenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.RenderingRenderingDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#Rendering()">Rendering</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns rendering.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.RenderingsRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.RenderingsRenderingUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#renderings()">renderings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns renderings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.TabularRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.TabularRenderingRenderingDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#TabularRendering()">TabularRendering</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns tabular rendering.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.TextualRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.TextualRenderingRenderingDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#TextualRendering()">TextualRendering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns textual rendering.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.ViewViewDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewViewDefinition</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#View()">View</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns view.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.ViewpointCheckViewpointDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewpointCheckViewpointDefinition</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#ViewpointCheck()">ViewpointCheck</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns viewpoint check.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.ViewpointChecksViewpointUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewpointChecksViewpointUsage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#viewpointChecks()">viewpointChecks</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns viewpoint checks.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ViewsLibrary.ViewsViewUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewsViewUsage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#views()">views</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns views.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.kerml.libraries.AbstractLibrary">Methods inherited from class com.dassault_systemes.modeler.kerml.libraries.<a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></h3>
<code><a href="../../../kerml/libraries/AbstractLibrary.html#findFunctionInLibrary(java.lang.String)">findFunctionInLibrary</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findLibraryPackage(java.lang.String)">findLibraryPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#findPackage(java.lang.String,java.lang.String)">findPackage</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getLibraryPackages()">getLibraryPackages</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#getNamespace()">getNamespace</a>, <a href="../../../kerml/libraries/AbstractLibrary.html#initialized()">initialized</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService">Methods inherited from class com.dassault_systemes.modeler.foundation.project.service.ModelElementProjectService</h3>
<code>disposeService, getIfPresent, getOrCreateInstance, getOrCreateInstanceWithNullSupport, getReferencedProject</code></div>
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
<section class="detail" id="&lt;init&gt;(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>ViewsLibrary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ViewsLibrary</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Creates a new views library instance.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
</dl>
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
<section class="detail" id="getInstanceByProject(com.dassault_systemes.modeler.foundation.project.ModelElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ViewsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(<a href="../../../foundation/project/ModelElementProject.html" title="interface in com.dassault_systemes.modeler.foundation.project">ModelElementProject</a> project)</span></div>
<div class="block">Returns the library instance for the given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - the project</dd>
<dt>Returns:</dt>
<dd>get instance by project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ViewsLibrary.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../../../../nomagic/magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> element)</span></div>
<div class="block">Returns the library instance for the project that owns the given element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element</dd>
<dt>Returns:</dt>
<dd>get instance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSemantic()">
<h3>isSemantic</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSemantic</span>()</div>
<div class="block">Returns whether this library is semantic.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#isSemantic()">isSemantic</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd><code>true</code> if semantic; <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="packagesNames()">
<h3>packagesNames</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">packagesNames</span>()</div>
<div class="block">Returns the names of the packages that belong to this library.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#packagesNames()">packagesNames</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>packages names</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="View()">
<h3>View</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.ViewViewDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewViewDefinition</a></span> <span class="element-name">View</span>()</div>
<div class="block">Returns view.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>view</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ViewpointCheck()">
<h3>ViewpointCheck</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.ViewpointCheckViewpointDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewpointCheckViewpointDefinition</a></span> <span class="element-name">ViewpointCheck</span>()</div>
<div class="block">Returns viewpoint check.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>viewpoint check</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="Rendering()">
<h3>Rendering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.RenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.RenderingRenderingDefinition</a></span> <span class="element-name">Rendering</span>()</div>
<div class="block">Returns rendering.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>rendering</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TextualRendering()">
<h3>TextualRendering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.TextualRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.TextualRenderingRenderingDefinition</a></span> <span class="element-name">TextualRendering</span>()</div>
<div class="block">Returns textual rendering.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>textual rendering</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="GraphicalRendering()">
<h3>GraphicalRendering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.GraphicalRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.GraphicalRenderingRenderingDefinition</a></span> <span class="element-name">GraphicalRendering</span>()</div>
<div class="block">Returns graphical rendering.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>graphical rendering</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TabularRendering()">
<h3>TabularRendering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.TabularRenderingRenderingDefinition.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.TabularRenderingRenderingDefinition</a></span> <span class="element-name">TabularRendering</span>()</div>
<div class="block">Returns tabular rendering.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>tabular rendering</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="views()">
<h3>views</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.ViewsViewUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewsViewUsage</a></span> <span class="element-name">views</span>()</div>
<div class="block">Returns views.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>views</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="viewpointChecks()">
<h3>viewpointChecks</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.ViewpointChecksViewpointUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.ViewpointChecksViewpointUsage</a></span> <span class="element-name">viewpointChecks</span>()</div>
<div class="block">Returns viewpoint checks.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>viewpoint checks</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="renderings()">
<h3>renderings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.RenderingsRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.RenderingsRenderingUsage</a></span> <span class="element-name">renderings</span>()</div>
<div class="block">Returns renderings.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>renderings</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="asTextualNotation()">
<h3>asTextualNotation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.AsTextualNotationRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsTextualNotationRenderingUsage</a></span> <span class="element-name">asTextualNotation</span>()</div>
<div class="block">Returns as textual notation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>as textual notation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="asTreeDiagram()">
<h3>asTreeDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.AsTreeDiagramRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsTreeDiagramRenderingUsage</a></span> <span class="element-name">asTreeDiagram</span>()</div>
<div class="block">Returns as tree diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>as tree diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="asInterconnectionDiagram()">
<h3>asInterconnectionDiagram</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ViewsLibrary.AsInterconnectionDiagramRenderingUsage.html" title="class in com.dassault_systemes.modeler.sysml.libraries.standard">ViewsLibrary.AsInterconnectionDiagramRenderingUsage</a></span> <span class="element-name">asInterconnectionDiagram</span>()</div>
<div class="block">Returns as interconnection diagram.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>as interconnection diagram</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTypeWrappers()">
<h3>getTypeWrappers</h3>
<div class="member-signature"><span class="modifiers">protected final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.dassault_systemes.modeler.kerml.libraries.TypeWrapper&gt;</span> <span class="element-name">getTypeWrappers</span>()</div>
<div class="block">Returns get type wrappers.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../../kerml/libraries/AbstractLibrary.html#getTypeWrappers()">getTypeWrappers</a></code> in class <code><a href="../../../kerml/libraries/AbstractLibrary.html" title="class in com.dassault_systemes.modeler.kerml.libraries">AbstractLibrary</a></code></dd>
<dt>Returns:</dt>
<dd>get type wrappers</dd>
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
