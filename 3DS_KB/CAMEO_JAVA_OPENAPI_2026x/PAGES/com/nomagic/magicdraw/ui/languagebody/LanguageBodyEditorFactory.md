# JAVA OPENAPI: LanguageBodyEditorFactory (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/ui/languagebody/LanguageBodyEditorFactory.html
- source_path: `com/nomagic/magicdraw/ui/languagebody/LanguageBodyEditorFactory.html`
- source_sha256: `8b9906d9a8ff6038211b18a14c00850f1df5da3aecb177ad63fa9dec09e9f52b`
- captured_utc: `2026-07-14T16:58:25.897156+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui.languagebody](package-summary.html)

## Interface LanguageBodyEditorFactory

@OpenApiAllpublic interfaceLanguageBodyEditorFactory

Language body editor factory. Should be registered in [`LanguageBodyEditorManager`](LanguageBodyEditorManager.html).

See Also:
[`LanguageBodyEditor`](LanguageBodyEditor.html)
[`LanguageBodyEditorManager`](LanguageBodyEditorManager.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault Methods
Modifier and Type
Method
Description
`[LanguageBodyEditor](LanguageBodyEditor.html)`
`[createEditor](#createEditor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Create body editor.
`default [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getInstructions](#getInstructions())()`
Optional language editor instructions.

============ METHOD DETAIL ========== 
Method Details
createEditor
[LanguageBodyEditor](LanguageBodyEditor.html) createEditor(@CheckForNull
 [Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Create body editor.
Parameters:
`element` - language body owning element.
Returns:
body editor.
getInstructions
@CheckForNulldefault [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getInstructions()
Optional language editor instructions.
Returns:
instructions.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui.languagebody</a></div>
<h1 class="title" title="Interface LanguageBodyEditorFactory">Interface LanguageBodyEditorFactory</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">LanguageBodyEditorFactory</span></div>
<div class="block">Language body editor factory. Should be registered in <a href="LanguageBodyEditorManager.html" title="class in com.nomagic.magicdraw.ui.languagebody"><code>LanguageBodyEditorManager</code></a>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="LanguageBodyEditor.html" title="interface in com.nomagic.magicdraw.ui.languagebody"><code>LanguageBodyEditor</code></a></li>
<li><a href="LanguageBodyEditorManager.html" title="class in com.nomagic.magicdraw.ui.languagebody"><code>LanguageBodyEditorManager</code></a></li>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="LanguageBodyEditor.html" title="interface in com.nomagic.magicdraw.ui.languagebody">LanguageBodyEditor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#createEditor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createEditor</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Create body editor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code>default <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5"><code><a class="member-name-link" href="#getInstructions()">getInstructions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5">
<div class="block">Optional language editor instructions.</div>
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
<section class="detail" id="createEditor(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>createEditor</h3>
<div class="member-signature"><span class="return-type"><a href="LanguageBodyEditor.html" title="interface in com.nomagic.magicdraw.ui.languagebody">LanguageBodyEditor</a></span> <span class="element-name">createEditor</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Create body editor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - language body owning element.</dd>
<dt>Returns:</dt>
<dd>body editor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInstructions()">
<h3>getInstructions</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">default</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getInstructions</span>()</div>
<div class="block">Optional language editor instructions.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instructions.</dd>
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
