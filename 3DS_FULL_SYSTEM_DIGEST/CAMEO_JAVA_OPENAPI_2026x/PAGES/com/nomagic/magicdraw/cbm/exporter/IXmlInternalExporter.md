# JAVA OPENAPI: IXmlInternalExporter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/cbm/exporter/IXmlInternalExporter.html
- source_path: `com/nomagic/magicdraw/cbm/exporter/IXmlInternalExporter.html`
- source_sha256: `22a8d75feb4dc7ce28c8d2d4daf00fd16b472ebbc0b46623aab971c13a3748ae`
- captured_utc: `2026-07-14T16:57:44.386383+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.cbm.exporter](package-summary.html)

## Interface IXmlInternalExporter

@OpenApiAllpublic interfaceIXmlInternalExporter
An Interface for BPMN -> XML Exporters.
 Exporters are xsd schema based, and export Object trees created from compiled xjc classes.
 The bpmn model elements can be checked with the BPMN validation rules, if required.
 And of course the generated xml can be validated against the original schemas
 and then written to an OutputStream.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`boolean`
`[doValidateModel](#doValidateModel())()`
the Exporter framework will call this method to test
 if the BPMN model elements should be validated.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getJAXBRootElement](#getJAXBRootElement())()`
Mapping model elements to JAXB objects.
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getMappedElements](#getMappedElements())()`
The model elements that are to be validated with CBM internal rules
`jakarta.xml.bind.Marshaller`
`[getMarshaller](#getMarshaller())()`
Creates the Marshaller used by this exporter
`[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?>`
`[getObjectFactoryClass](#getObjectFactoryClass())()`
The particular JAXB Object factory needed for this exporter.
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getRefElements](#getRefElements())()`
The reference of model elements that are to be validated with CBM internal rules
`[LSResourceResolver](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/ls/LSResourceResolver.html)`
`[getResolver](#getResolver())()`
if dependent schemas are jarred, a custom Resolver is needed
 to locate them at xml validation time.
`[StreamSource](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/transform/stream/StreamSource.html)[]`
`[getSchemaSources](#getSchemaSources())()`
The Schema sources needed to validate the resulting xml file
 This method can return null if xml validation is not needed.
`[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](../../validation/RuleViolationResult.html)>`
`[getViolations](#getViolations())()`
If the BPMN model elements were validated,
 this is where the results will be available.
`void`
`[setMarshallerProperties](#setMarshallerProperties(jakarta.xml.bind.Marshaller))(jakarta.xml.bind.Marshaller m)`
Sets special properties for the marshaller before actual export.
`void`
`[write](#write())()`
This method will serialize the JAXB object tree to an OutputStream
 silently exits if all goes well

============ METHOD DETAIL ========== 
Method Details
getJAXBRootElement
[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getJAXBRootElement()
Mapping model elements to JAXB objects.
 This must return the root of the JAXB object tree.
Returns:
the root of the mapped model, a JAXB object
doValidateModel
boolean doValidateModel()
the Exporter framework will call this method to test
 if the BPMN model elements should be validated.
Returns:
true if the model is to be validated
getMappedElements
[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getMappedElements()
The model elements that are to be validated with CBM internal rules
Returns:
the elements that have to be validated
getRefElements
[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getRefElements()
The reference of model elements that are to be validated with CBM internal rules
Returns:
the elements that have to be validated
getViolations
[Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[RuleViolationResult](../../validation/RuleViolationResult.html)> getViolations()
If the BPMN model elements were validated,
 this is where the results will be available.
Returns:
the Validation Rule Violations
getObjectFactoryClass
[Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> getObjectFactoryClass()
The particular JAXB Object factory needed for this exporter.
Returns:
the JAXB ObjectFactory class
getSchemaSources
[StreamSource](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/transform/stream/StreamSource.html)[] getSchemaSources()
The Schema sources needed to validate the resulting xml file
 This method can return null if xml validation is not needed.
Returns:
all schemas needed for xml validation
setMarshallerProperties
void setMarshallerProperties(jakarta.xml.bind.Marshaller m)
 throws jakarta.xml.bind.JAXBException
Sets special properties for the marshaller before actual export.
Parameters:
`m` - the marshaller that can be customized
Throws:
`jakarta.xml.bind.JAXBException`
getMarshaller
jakarta.xml.bind.Marshaller getMarshaller()
 throws jakarta.xml.bind.JAXBException
Creates the Marshaller used by this exporter
Returns:
the Marshaller
Throws:
`jakarta.xml.bind.JAXBException`
write
void write()
 throws jakarta.xml.bind.JAXBException,
[SAXParseException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXParseException.html)
This method will serialize the JAXB object tree to an OutputStream
 silently exits if all goes well
Throws:
`jakarta.xml.bind.JAXBException`
`[SAXParseException](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXParseException.html)`
getResolver
[LSResourceResolver](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/ls/LSResourceResolver.html) getResolver()
if dependent schemas are jarred, a custom Resolver is needed
 to locate them at xml validation time.
Returns:
the custom Resource Resolver

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.cbm.exporter</a></div>
<h1 class="title" title="Interface IXmlInternalExporter">Interface IXmlInternalExporter</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IXmlInternalExporter</span></div>
<div class="block">An Interface for BPMN -&gt; XML Exporters.
 Exporters are xsd schema based, and export Object trees created from compiled xjc classes.
 The bpmn model elements can be checked with the BPMN validation rules, if required.
 And of course the generated xml can be validated against the original schemas
 and then written to an OutputStream.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#doValidateModel()">doValidateModel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">the Exporter framework will call this method to test
 if the BPMN model elements should be validated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getJAXBRootElement()">getJAXBRootElement</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Mapping model elements to JAXB objects.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMappedElements()">getMappedElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The model elements that are to be validated with CBM internal rules</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>jakarta.xml.bind.Marshaller</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMarshaller()">getMarshaller</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Creates the  Marshaller used by this exporter</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a><wbr/>&lt;?&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getObjectFactoryClass()">getObjectFactoryClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The particular JAXB Object factory needed for this exporter.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRefElements()">getRefElements</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The reference of model elements that are to be validated with CBM internal rules</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/ls/LSResourceResolver.html" title="class or interface in org.w3c.dom.ls">LSResourceResolver</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getResolver()">getResolver</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">if dependent schemas are jarred, a custom Resolver is needed
 to locate them at xml validation time.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/transform/stream/StreamSource.html" title="class or interface in javax.xml.transform.stream">StreamSource</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSchemaSources()">getSchemaSources</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The Schema sources needed to validate the resulting xml file
 This method can return null if xml validation is not needed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a><wbr/>&lt;<a href="../../validation/RuleViolationResult.html" title="class in com.nomagic.magicdraw.validation">RuleViolationResult</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getViolations()">getViolations</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">If the BPMN model elements were validated,
 this is where the results will be available.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMarshallerProperties(jakarta.xml.bind.Marshaller)">setMarshallerProperties</a><wbr/>(jakarta.xml.bind.Marshaller m)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets special properties for the marshaller before actual export.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#write()">write</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method will serialize the JAXB object tree to an OutputStream
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
<section class="detail" id="getJAXBRootElement()">
<h3>getJAXBRootElement</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getJAXBRootElement</span>()</div>
<div class="block">Mapping model elements to JAXB objects.
 This must return the root of the JAXB object tree.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the root of the mapped model, a JAXB object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="doValidateModel()">
<h3>doValidateModel</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">doValidateModel</span>()</div>
<div class="block">the Exporter framework will call this method to test
 if the BPMN model elements should be validated.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if the model is to be validated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMappedElements()">
<h3>getMappedElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getMappedElements</span>()</div>
<div class="block">The model elements that are to be validated with CBM internal rules</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the elements that have to be validated</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRefElements()">
<h3>getRefElements</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getRefElements</span>()</div>
<div class="block">The reference of model elements that are to be validated with CBM internal rules</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the elements that have to be validated</dd>
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
<section class="detail" id="getObjectFactoryClass()">
<h3>getObjectFactoryClass</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt;</span> <span class="element-name">getObjectFactoryClass</span>()</div>
<div class="block">The particular JAXB Object factory needed for this exporter.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the JAXB ObjectFactory class</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSchemaSources()">
<h3>getSchemaSources</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/transform/stream/StreamSource.html" title="class or interface in javax.xml.transform.stream">StreamSource</a>[]</span> <span class="element-name">getSchemaSources</span>()</div>
<div class="block">The Schema sources needed to validate the resulting xml file
 This method can return null if xml validation is not needed.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>all schemas needed for xml validation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMarshallerProperties(jakarta.xml.bind.Marshaller)">
<h3>setMarshallerProperties</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMarshallerProperties</span><wbr/><span class="parameters">(jakarta.xml.bind.Marshaller m)</span>
                      throws <span class="exceptions">jakarta.xml.bind.JAXBException</span></div>
<div class="block">Sets special properties for the marshaller before actual export.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>m</code> - the marshaller that can be customized</dd>
<dt>Throws:</dt>
<dd><code>jakarta.xml.bind.JAXBException</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMarshaller()">
<h3>getMarshaller</h3>
<div class="member-signature"><span class="return-type">jakarta.xml.bind.Marshaller</span> <span class="element-name">getMarshaller</span>()
                                   throws <span class="exceptions">jakarta.xml.bind.JAXBException</span></div>
<div class="block">Creates the  Marshaller used by this exporter</div>
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
<div class="block">This method will serialize the JAXB object tree to an OutputStream
 silently exits if all goes well</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code>jakarta.xml.bind.JAXBException</code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/SAXParseException.html" title="class or interface in org.xml.sax">SAXParseException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResolver()">
<h3>getResolver</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/ls/LSResourceResolver.html" title="class or interface in org.w3c.dom.ls">LSResourceResolver</a></span> <span class="element-name">getResolver</span>()</div>
<div class="block">if dependent schemas are jarred, a custom Resolver is needed
 to locate them at xml validation time.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>the custom Resource Resolver</dd>
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
