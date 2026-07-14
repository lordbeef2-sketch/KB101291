# JAVA OPENAPI: IJavaNumberPart (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/autoid/IJavaNumberPart.html
- source_path: `com/nomagic/magicdraw/autoid/IJavaNumberPart.html`
- source_sha256: `91bdf2b13818556f38b559ad065b5073f0a30130a3646433d1258f12416417d4`
- captured_utc: `2026-07-14T16:45:08.323114+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.autoid](package-summary.html)

## Interface IJavaNumberPart

@OpenApiAllpublic interfaceIJavaNumberPart

If this interface is implemented for an Expression invalid input: '<'>
 then the AutoNumber-Framework will call the class methods and use the
 Strings produced as slices for the complete AutoNumber,
 as it is defined in the invalid input: '<'>

 These methods should return equal values for equal input.

Since:
Jan 18, 2011

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[generateNextId](#generateNextId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) lastNumberPart)`
Generate a new ID.

============ METHOD DETAIL ========== 
Method Details
generateNextId
[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) generateNextId([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) lastNumberPart)
Generate a new ID.

 The new ID logically increases the value of the lastNumberPart
Parameters:
`lastNumberPart` - the last significant NumberPart of the previous Id
Returns:
the last significant Number Part in the new Element ID.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.autoid</a></div>
<h1 class="title" title="Interface IJavaNumberPart">Interface IJavaNumberPart</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IJavaNumberPart</span></div>
<div class="block">If this interface is implemented for an Expression <span class="invalid-tag">invalid input: '&lt;'</span><numberpart>&gt;
 then the AutoNumber-Framework will call the class methods and use the
 Strings produced as slices for the complete AutoNumber,
 as it is defined in the <span class="invalid-tag">invalid input: '&lt;'</span><numberingscheme>&gt;

 These methods should return equal values for equal input.</numberingscheme></numberpart></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jan 18, 2011</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#generateNextId(java.lang.String)">generateNextId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lastNumberPart)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Generate a new ID.</div>
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
<section class="detail" id="generateNextId(java.lang.String)">
<h3>generateNextId</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">generateNextId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lastNumberPart)</span></div>
<div class="block">Generate a new ID.

 The new ID logically increases the value of the lastNumberPart</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lastNumberPart</code> - the last significant NumberPart of the previous Id</dd>
<dt>Returns:</dt>
<dd>the last significant Number Part in the new Element ID.</dd>
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
