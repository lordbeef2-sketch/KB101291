# JAVA OPENAPI: IXmlExport (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/cbm/exporter/IXmlExport.html
- source_path: `com/nomagic/magicdraw/cbm/exporter/IXmlExport.html`
- source_sha256: `639283ade5646bbaf91ae29efb2e581391d9a506c239ef32cbeb8af5dd901277`
- captured_utc: `2026-07-14T16:45:09.664132+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.cbm.exporter](package-summary.html)

## Interface IXmlExport

All Known Implementing Classes:
`com.nomagic.magicdraw.cbm.exporter.BaseXmlExport`, `[Bpmn20Export](Bpmn20Export.html)`

@OpenApiAllpublic interfaceIXmlExport

A simple interface to get access to the internal IXmlExporter instance.

Since:
Mar 12, 2012

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getMappedElements](#getMappedElements())()`
The model elements that are to be exported
`jakarta.xml.bind.Marshaller`
`[getMarshaller](#getMarshaller())()`
This will give access to the Marshaller object used to serialize the Model
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](../../validation/RuleViolationResult.html)>`
`[getViolations](#getViolations())()`
If the BPMN model elements were validated,
 this is where the results will be available.
`void`
`[write](#write())()`
This method will serialize the JAXB object tree to an Outputstream
 silently exits if all goes well

============ METHOD DETAIL ========== 
Method Details
getMappedElements
[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getMappedElements()
The model elements that are to be exported
Returns:
the elements
getViolations
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](../../validation/RuleViolationResult.html)> getViolations()
If the BPMN model elements were validated,
 this is where the results will be available.
Returns:
the Validation Rule Violations
getMarshaller
jakarta.xml.bind.Marshaller getMarshaller()
 throws jakarta.xml.bind.JAXBException
This will give access to the Marshaller object used to serialize the Model
Returns:
the Marshaller
Throws:
`jakarta.xml.bind.JAXBException`
write
void write()
 throws jakarta.xml.bind.JAXBException,
[SAXParseException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXParseException.html)
This method will serialize the JAXB object tree to an Outputstream
 silently exits if all goes well
Throws:
`jakarta.xml.bind.JAXBException`
`[SAXParseException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXParseException.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.cbm.exporter</a></div>
<h1 class="title" title="Interface IXmlExport">Interface IXmlExport</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code>com.nomagic.magicdraw.cbm.exporter.BaseXmlExport</code>, <code><a href="Bpmn20Export.html" title="class in com.nomagic.magicdraw.cbm.exporter">Bpmn20Export</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IXmlExport</span></div>
<div class="block">A simple interface to get access to the internal IXmlExporter instance.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 12, 2012</dd>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMappedElements()">getMappedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The model elements that are to be exported</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>jakarta.xml.bind.Marshaller</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMarshaller()">getMarshaller</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This will give access to the Marshaller object used to serialize the Model</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../validation/RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getViolations()">getViolations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If the BPMN model elements were validated,
 this is where the results will be available.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#write()">write</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method will serialize the JAXB object tree to an Outputstream
 silently exits if all goes well</div>
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
<section class="detail" id="getMappedElements()">
<h3>getMappedElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getMappedElements</span>()</div>
<div class="block">The model elements that are to be exported</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the elements</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getViolations()">
<h3>getViolations</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../validation/RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</span> <span class="element-name">getViolations</span>()</div>
<div class="block">If the BPMN model elements were validated,
 this is where the results will be available.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the Validation Rule Violations</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMarshaller()">
<h3>getMarshaller</h3>
<div class="member-signature"><span class="return-type">jakarta.xml.bind.Marshaller</span> <span class="element-name">getMarshaller</span>()
                                   throws <span class="exceptions">jakarta.xml.bind.JAXBException</span></div>
<div class="block">This will give access to the Marshaller object used to serialize the Model</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the Marshaller</dd>
<dt>Throws:</dt>
<dd><code>jakarta.xml.bind.JAXBException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="write()">
<h3>write</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">write</span>()
    throws <span class="exceptions">jakarta.xml.bind.JAXBException,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXParseException.html" title="class or interface in org.xml.sax">SAXParseException</a></span></div>
<div class="block">This method will serialize the JAXB object tree to an Outputstream
 silently exits if all goes well</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>jakarta.xml.bind.JAXBException</code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXParseException.html" title="class or interface in org.xml.sax">SAXParseException</a></code></dd>
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
