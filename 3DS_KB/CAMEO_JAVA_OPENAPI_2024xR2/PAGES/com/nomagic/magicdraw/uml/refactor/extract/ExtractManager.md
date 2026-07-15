# JAVA OPENAPI: ExtractManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/uml/refactor/extract/ExtractManager.html
- source_path: `com/nomagic/magicdraw/uml/refactor/extract/ExtractManager.html`
- source_sha256: `d497cd4b5cf6ac2c93fad0239673ed0ec55af02b3c4e060c281d535bac36acbe`
- captured_utc: `2026-07-14T16:55:54.412447+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.refactor.extract](package-summary.html)

## Interface ExtractManager

@OpenApiAllpublic interfaceExtractManager

A class responsible for extract refactoring. Use the

Refactoring.Extracting

class to create the extract
 manager for a symbol which you want to extract. Configure the extract refactoring by changing

ExtractSource

and

ExtractTarget

. Invoke the refactoring with RefactorManager.refactor().
 Review refactoring results by inspecting

ExtractSource

and

ExtractTarget

.

````java
// Creates extract refactor manager.
 ExtractManager extractManager = Refactoring.Extracting.createExtractManager(symbols);

 if (extractManager != null)
 {
     // A session has to be started before refactoring.
     SessionManager sessionManager = SessionManager.getInstance();
     sessionManager.createSession("Extract Refactor Symbols");

     // We may control the extract refactor result by modifying extract target.
     ExtractTarget extractTarget = extractManager.getExtractTarget();

     // Create a namespace to which we are going to refactor.
     Project project = Project.getProject(symbols[0]);
     Package package1 = project.getElementsFactory().createPackageInstance();
     package1.setOwner(project.getModel());

     // Set the namespace to which the extract result will go.
     extractTarget.setTargetNamespace(package1);

     // Choose target diagram type from allowed diagram types if the default type does not suite.
     List
 allowedTargetDiagramTypes = extractTarget.getAllowedTargetDiagramTypes();
     extractTarget.setTargetDiagramType(allowedTargetDiagramTypes.get(0));

     // Modify reference names which link the extract refactor source to the target.
     List<? extends ExtractReference> references = extractTarget.getReferences();

     for (int i = 0; i < references.size(); i++)
     {
         ExtractReference reference = references.get(i);
         reference.setName(Integer.toString(i));
     }

     // We may control the extract refactor source by modifying the extract source.
     ExtractSource extractSource = extractManager.getExtractSource();
     extractSource.setElementName("sourceElementName");

     // Perform actual refactoring.
     extractManager.extract();

     sessionManager.closeSession();

     // The element which was created in the source during refactoring.
     Element sourceElement = extractSource.getElement();

     // The element which was created in the target during refactoring.
     Element targetElement = extractTarget.getElement();

     // The diagram which was created in the target during refactoring.
    DiagramPresentationElement targetDiagram = extractTarget.getDiagram();
 }
````

See Also:
[`ExtractSource`](ExtractSource.html)
[`ExtractTarget`](ExtractTarget.html)
[`Refactoring.Extracting`](../../Refactoring.Extracting.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[extract](#extract())()`
Performs actual extract refactoring of the model.
`[ExtractSource](ExtractSource.html)`
`[getExtractSource](#getExtractSource())()`
Gets extract refactor source end of extract refactoring.
`[ExtractTarget](ExtractTarget.html)`
`[getExtractTarget](#getExtractTarget())()`
Gets extract refactor target which is used to customize the extracted result.

============ METHOD DETAIL ========== 
Method Details
extract
boolean extract()
Performs actual extract refactoring of the model.
 Wrap the call of this method with session create/close.
Returns:
true if refactoring was successful, false otherwise.
getExtractTarget
[ExtractTarget](ExtractTarget.html) getExtractTarget()
Gets extract refactor target which is used to customize the extracted result.
Returns:
extract refactor target.
getExtractSource
[ExtractSource](ExtractSource.html) getExtractSource()
Gets extract refactor source end of extract refactoring.
Returns:
extract refactor source.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.refactor.extract</a></div>
<h1 class="title" title="Interface ExtractManager">Interface ExtractManager</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ExtractManager</span></div>
<div class="block">A class responsible for extract refactoring. Use the <a href="../../Refactoring.Extracting.html" title="class in com.nomagic.magicdraw.uml"><code>Refactoring.Extracting</code></a> class to create the extract
 manager for a symbol which you want to extract. Configure the extract refactoring by changing
 <a href="ExtractSource.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractSource</code></a> and <a href="ExtractTarget.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractTarget</code></a>. Invoke the refactoring with RefactorManager.refactor().
 Review refactoring results by inspecting <a href="ExtractSource.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractSource</code></a> and <a href="ExtractTarget.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractTarget</code></a>.
 <p></p>
<pre>
 // Creates extract refactor manager.
 ExtractManager extractManager = Refactoring.Extracting.createExtractManager(symbols);

 if (extractManager != null)
 {
     // A session has to be started before refactoring.
     SessionManager sessionManager = SessionManager.getInstance();
     sessionManager.createSession("Extract Refactor Symbols");

     // We may control the extract refactor result by modifying extract target.
     ExtractTarget extractTarget = extractManager.getExtractTarget();

     // Create a namespace to which we are going to refactor.
     Project project = Project.getProject(symbols[0]);
     Package package1 = project.getElementsFactory().createPackageInstance();
     package1.setOwner(project.getModel());

     // Set the namespace to which the extract result will go.
     extractTarget.setTargetNamespace(package1);

     // Choose target diagram type from allowed diagram types if the default type does not suite.
     List<string> allowedTargetDiagramTypes = extractTarget.getAllowedTargetDiagramTypes();
     extractTarget.setTargetDiagramType(allowedTargetDiagramTypes.get(0));

     // Modify reference names which link the extract refactor source to the target.
     List&lt;? extends ExtractReference&gt; references = extractTarget.getReferences();

     for (int i = 0; i &lt; references.size(); i++)
     {
         ExtractReference reference = references.get(i);
         reference.setName(Integer.toString(i));
     }

     // We may control the extract refactor source by modifying the extract source.
     ExtractSource extractSource = extractManager.getExtractSource();
     extractSource.setElementName("sourceElementName");

     // Perform actual refactoring.
     extractManager.extract();

     sessionManager.closeSession();

     // The element which was created in the source during refactoring.
     Element sourceElement = extractSource.getElement();

     // The element which was created in the target during refactoring.
     Element targetElement = extractTarget.getElement();

     // The diagram which was created in the target during refactoring.
    DiagramPresentationElement targetDiagram = extractTarget.getDiagram();
 }
 </string></pre></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ExtractSource.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractSource</code></a></li>
<li><a href="ExtractTarget.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract"><code>ExtractTarget</code></a></li>
<li><a href="../../Refactoring.Extracting.html" title="class in com.nomagic.magicdraw.uml"><code>Refactoring.Extracting</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#extract()">extract</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Performs actual extract refactoring of the model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ExtractSource.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract">ExtractSource</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExtractSource()">getExtractSource</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets extract refactor source end of extract refactoring.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="ExtractTarget.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract">ExtractTarget</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getExtractTarget()">getExtractTarget</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets extract refactor target which is used to customize the extracted result.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="extract()">
<h3>extract</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">extract</span>()</div>
<div class="block">Performs actual extract refactoring of the model.
 Wrap the call of this method with session create/close.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if refactoring was successful, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtractTarget()">
<h3>getExtractTarget</h3>
<div class="member-signature"><span class="return-type"><a href="ExtractTarget.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract">ExtractTarget</a></span> <span class="element-name">getExtractTarget</span>()</div>
<div class="block">Gets extract refactor target which is used to customize the extracted result.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>extract refactor target.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtractSource()">
<h3>getExtractSource</h3>
<div class="member-signature"><span class="return-type"><a href="ExtractSource.html" title="interface in com.nomagic.magicdraw.uml.refactor.extract">ExtractSource</a></span> <span class="element-name">getExtractSource</span>()</div>
<div class="block">Gets extract refactor source end of extract refactoring.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>extract refactor source.</dd>
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
