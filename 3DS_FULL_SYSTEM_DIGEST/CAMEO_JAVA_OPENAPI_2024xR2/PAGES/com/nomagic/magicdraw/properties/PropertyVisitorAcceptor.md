# JAVA OPENAPI: PropertyVisitorAcceptor (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/properties/PropertyVisitorAcceptor.html
- source_path: `com/nomagic/magicdraw/properties/PropertyVisitorAcceptor.html`
- source_sha256: `47a092d474f325a2178c0af453a9dc0028cb57c80a7dbadc3275c7b0e3351353`
- captured_utc: `2026-07-14T16:55:26.246131+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Interface PropertyVisitorAcceptor

All Known Implementing Classes:
`[AbstractChoiceProperty](AbstractChoiceProperty.html)`, `[BooleanProperty](BooleanProperty.html)`, `[ChoiceProperty](ChoiceProperty.html)`, `[ClassPathEntriesListProperty](ClassPathEntriesListProperty.html)`, `[ColorProperty](ColorProperty.html)`, `[DateTimeProperty](DateTimeProperty.html)`, `[ElementListProperty](ElementListProperty.html)`, `[ElementProperty](ElementProperty.html)`, `[ExtendablePropertyManager](ExtendablePropertyManager.html)`, `[FileProperty](FileProperty.html)`, `[FontProperty](FontProperty.html)`, `[JarEntryProperty](JarEntryProperty.html)`, `[JDBCDriverClassNameProperty](JDBCDriverClassNameProperty.html)`, `[ListProperty](ListProperty.html)`, `[LocaleProperty](LocaleProperty.html)`, `[NumberProperty](NumberProperty.html)`, `[PageFormatProperty](PageFormatProperty.html)`, `[PasswordProperty](PasswordProperty.html)`, `[Property](Property.html)`, `[PropertyManager](PropertyManager.html)`, `[PropertyManagerByDiagram](PropertyManagerByDiagram.html)`, `[PropertyManagerByStereotype](PropertyManagerByStereotype.html)`, `[StringProperty](StringProperty.html)`, `[Style](Style.html)`, `[StyleManager](StyleManager.html)`, `[TypeProperty](TypeProperty.html)`

@OpenApiAllpublic interfacePropertyVisitorAcceptor

The interface for object that can be visited with
 `PropertyVisitor`.

See Also:
[`PropertyVisitor`](PropertyVisitor.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[accept](#accept(com.nomagic.magicdraw.properties.PropertyVisitor))([PropertyVisitor](PropertyVisitor.html) visitor)`
The accept method.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassType](#getClassType())()`
Returns class type as string.

============ METHOD DETAIL ========== 
Method Details
accept
void accept([PropertyVisitor](PropertyVisitor.html) visitor)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
The accept method.
Parameters:
`visitor` - the given visitor.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
getClassType
[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassType()
Returns class type as string.
 Class type must be different for different type of properties.
Returns:
class type.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Interface PropertyVisitorAcceptor">Interface PropertyVisitorAcceptor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="AbstractChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">AbstractChoiceProperty</a></code>, <code><a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a></code>, <code><a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a></code>, <code><a href="ClassPathEntriesListProperty.html" title="class in com.nomagic.magicdraw.properties">ClassPathEntriesListProperty</a></code>, <code><a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a></code>, <code><a href="DateTimeProperty.html" title="class in com.nomagic.magicdraw.properties">DateTimeProperty</a></code>, <code><a href="ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a></code>, <code><a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a></code>, <code><a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties">ExtendablePropertyManager</a></code>, <code><a href="FileProperty.html" title="class in com.nomagic.magicdraw.properties">FileProperty</a></code>, <code><a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a></code>, <code><a href="JarEntryProperty.html" title="class in com.nomagic.magicdraw.properties">JarEntryProperty</a></code>, <code><a href="JDBCDriverClassNameProperty.html" title="class in com.nomagic.magicdraw.properties">JDBCDriverClassNameProperty</a></code>, <code><a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a></code>, <code><a href="LocaleProperty.html" title="class in com.nomagic.magicdraw.properties">LocaleProperty</a></code>, <code><a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a></code>, <code><a href="PageFormatProperty.html" title="class in com.nomagic.magicdraw.properties">PageFormatProperty</a></code>, <code><a href="PasswordProperty.html" title="class in com.nomagic.magicdraw.properties">PasswordProperty</a></code>, <code><a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a></code>, <code><a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a></code>, <code><a href="PropertyManagerByDiagram.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByDiagram</a></code>, <code><a href="PropertyManagerByStereotype.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByStereotype</a></code>, <code><a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a></code>, <code><a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a></code>, <code><a href="StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a></code>, <code><a href="TypeProperty.html" title="class in com.nomagic.magicdraw.properties">TypeProperty</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PropertyVisitorAcceptor</span></div>
<div class="block">The interface for object that can be visited with
 <code>PropertyVisitor</code>.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties"><code>PropertyVisitor</code></a></li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#accept(com.nomagic.magicdraw.properties.PropertyVisitor)">accept</a><wbr/>(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The accept method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getClassType()">getClassType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns class type as string.</div>
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
<section class="detail" id="accept(com.nomagic.magicdraw.properties.PropertyVisitor)">
<h3>accept</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">accept</span><wbr/><span class="parameters">(<a href="PropertyVisitor.html" title="interface in com.nomagic.magicdraw.properties">PropertyVisitor</a> visitor)</span>
     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">The accept method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visitor</code> - the given visitor.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassType()">
<h3>getClassType</h3>
<div class="member-signature"><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassType</span>()</div>
<div class="block">Returns class type as string.
 Class type must be different for different type of properties.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>class type.</dd>
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
