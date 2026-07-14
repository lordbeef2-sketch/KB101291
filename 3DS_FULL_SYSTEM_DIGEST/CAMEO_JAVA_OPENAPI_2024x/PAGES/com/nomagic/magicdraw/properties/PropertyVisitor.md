# JAVA OPENAPI: PropertyVisitor (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/properties/PropertyVisitor.html
- source_path: `com/nomagic/magicdraw/properties/PropertyVisitor.html`
- source_sha256: `59140dc98dd659a7748450f37e69976a0b0ae3efc871f1b863a61f691ff2ec18`
- captured_utc: `2026-07-14T16:51:27.180283+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.properties](package-summary.html)

## Interface PropertyVisitor

All Known Implementing Classes:
`[PropertyVisitorAdapter](PropertyVisitorAdapter.html)`

@OpenApiAllpublic interfacePropertyVisitor

Visitor for all types of properties, property managers, styles and etc used in MagicDraw application.
 See Visitor pattern for more details.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[visit](#visit(com.nomagic.magicdraw.properties.BooleanProperty))([BooleanProperty](BooleanProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ChoiceListProperty))(com.nomagic.magicdraw.properties.ChoiceListProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ChoiceProperty))([ChoiceProperty](ChoiceProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty))([ClassPathEntriesListProperty](ClassPathEntriesListProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ColorProperty))([ColorProperty](ColorProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ConstraintProperty))(com.nomagic.magicdraw.properties.ConstraintProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.DateTimeProperty))([DateTimeProperty](DateTimeProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ElementInstanceProperty))(com.nomagic.magicdraw.properties.ElementInstanceProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ElementListProperty))([ElementListProperty](ElementListProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ElementProperty))([ElementProperty](ElementProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager))([ExtendablePropertyManager](ExtendablePropertyManager.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ExternalToolProperty))(com.nomagic.magicdraw.properties.ExternalToolProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.FileProperty))([FileProperty](FileProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.FontProperty))([FontProperty](FontProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ImageProperty))(com.nomagic.magicdraw.properties.ImageProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.JarEntryProperty))([JarEntryProperty](JarEntryProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty))([JDBCDriverClassNameProperty](JDBCDriverClassNameProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ListProperty))([ListProperty](ListProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.LocaleProperty))([LocaleProperty](LocaleProperty.html) p)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.MapProperty))(com.nomagic.magicdraw.properties.MapProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.NumberProperty))([NumberProperty](NumberProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PageFormatProperty))([PageFormatProperty](PageFormatProperty.html) p)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PasswordProperty))([PasswordProperty](PasswordProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.Property))([Property](Property.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PropertyManager))([PropertyManager](PropertyManager.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram))([PropertyManagerByDiagram](PropertyManagerByDiagram.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype))([PropertyManagerByStereotype](PropertyManagerByStereotype.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.SpecificElementProperty))(com.nomagic.magicdraw.properties.SpecificElementProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.StringProperty))([StringProperty](StringProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.Style))([Style](Style.html) p)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.StyleManager))([StyleManager](StyleManager.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.TypeProperty))([TypeProperty](TypeProperty.html) o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty))(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)`

`void`
`[visit](#visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty))(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)`

============ METHOD DETAIL ========== 
Method Details
visit
void visit([Property](Property.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([ColorProperty](ColorProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([ChoiceProperty](ChoiceProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.ChoiceListProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([FontProperty](FontProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([FileProperty](FileProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([BooleanProperty](BooleanProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([NumberProperty](NumberProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([StyleManager](StyleManager.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([PropertyManager](PropertyManager.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([PropertyManagerByDiagram](PropertyManagerByDiagram.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([PropertyManagerByStereotype](PropertyManagerByStereotype.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([StringProperty](StringProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([LocaleProperty](LocaleProperty.html) p)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([PageFormatProperty](PageFormatProperty.html) p)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([Style](Style.html) p)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([JarEntryProperty](JarEntryProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([JDBCDriverClassNameProperty](JDBCDriverClassNameProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([PasswordProperty](PasswordProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([ClassPathEntriesListProperty](ClassPathEntriesListProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([TypeProperty](TypeProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([ElementProperty](ElementProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.SpecificElementProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.ConstraintProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([ElementListProperty](ElementListProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.ElementInstanceProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([ListProperty](ListProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([ExtendablePropertyManager](ExtendablePropertyManager.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.ExternalToolProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.ImageProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit(com.nomagic.magicdraw.properties.MapProperty o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`
visit
void visit([DateTimeProperty](DateTimeProperty.html) o)
 throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.properties</a></div>
<h1 class="title" title="Interface PropertyVisitor">Interface PropertyVisitor</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="PropertyVisitorAdapter.html" title="class in com.nomagic.magicdraw.properties">PropertyVisitorAdapter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">PropertyVisitor</span></div>
<div class="block">Visitor for all types of properties, property managers, styles and etc used in MagicDraw application.
 See Visitor pattern for more details.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.BooleanProperty)">visit</a><wbr/>(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ChoiceListProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ChoiceListProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ChoiceProperty)">visit</a><wbr/>(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty)">visit</a><wbr/>(<a href="ClassPathEntriesListProperty.html" title="class in com.nomagic.magicdraw.properties">ClassPathEntriesListProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ColorProperty)">visit</a><wbr/>(<a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ConstraintProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ConstraintProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.DateTimeProperty)">visit</a><wbr/>(<a href="DateTimeProperty.html" title="class in com.nomagic.magicdraw.properties">DateTimeProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ElementInstanceProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ElementInstanceProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ElementListProperty)">visit</a><wbr/>(<a href="ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ElementProperty)">visit</a><wbr/>(<a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager)">visit</a><wbr/>(<a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties">ExtendablePropertyManager</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ExternalToolProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ExternalToolProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.FileProperty)">visit</a><wbr/>(<a href="FileProperty.html" title="class in com.nomagic.magicdraw.properties">FileProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.FontProperty)">visit</a><wbr/>(<a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ImageProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ImageProperty o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.JarEntryProperty)">visit</a><wbr/>(<a href="JarEntryProperty.html" title="class in com.nomagic.magicdraw.properties">JarEntryProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty)">visit</a><wbr/>(<a href="JDBCDriverClassNameProperty.html" title="class in com.nomagic.magicdraw.properties">JDBCDriverClassNameProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ListProperty)">visit</a><wbr/>(<a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.LocaleProperty)">visit</a><wbr/>(<a href="LocaleProperty.html" title="class in com.nomagic.magicdraw.properties">LocaleProperty</a> p)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.MapProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.MapProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.NumberProperty)">visit</a><wbr/>(<a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PageFormatProperty)">visit</a><wbr/>(<a href="PageFormatProperty.html" title="class in com.nomagic.magicdraw.properties">PageFormatProperty</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PasswordProperty)">visit</a><wbr/>(<a href="PasswordProperty.html" title="class in com.nomagic.magicdraw.properties">PasswordProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.Property)">visit</a><wbr/>(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PropertyManager)">visit</a><wbr/>(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram)">visit</a><wbr/>(<a href="PropertyManagerByDiagram.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByDiagram</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype)">visit</a><wbr/>(<a href="PropertyManagerByStereotype.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByStereotype</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.SpecificElementProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.SpecificElementProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.StringProperty)">visit</a><wbr/>(<a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.Style)">visit</a><wbr/>(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> p)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.StyleManager)">visit</a><wbr/>(<a href="StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.TypeProperty)">visit</a><wbr/>(<a href="TypeProperty.html" title="class in com.nomagic.magicdraw.properties">TypeProperty</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty)">visit</a><wbr/>(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"> </div>
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
<section class="detail" id="visit(com.nomagic.magicdraw.properties.Property)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="Property.html" title="class in com.nomagic.magicdraw.properties">Property</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ColorProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ColorProperty.html" title="class in com.nomagic.magicdraw.properties">ColorProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ChoiceProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ChoiceProperty.html" title="class in com.nomagic.magicdraw.properties">ChoiceProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ChoiceListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ChoiceListProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.FontProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="FontProperty.html" title="class in com.nomagic.magicdraw.properties">FontProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.FileProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="FileProperty.html" title="class in com.nomagic.magicdraw.properties">FileProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.BooleanProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="BooleanProperty.html" title="class in com.nomagic.magicdraw.properties">BooleanProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.NumberProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="NumberProperty.html" title="class in com.nomagic.magicdraw.properties">NumberProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.StyleManager)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="StyleManager.html" title="class in com.nomagic.magicdraw.properties">StyleManager</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PropertyManager)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PropertyManager.html" title="class in com.nomagic.magicdraw.properties">PropertyManager</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PropertyManagerByDiagram)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PropertyManagerByDiagram.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByDiagram</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PropertyManagerByStereotype)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PropertyManagerByStereotype.html" title="class in com.nomagic.magicdraw.properties">PropertyManagerByStereotype</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.StringProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="StringProperty.html" title="class in com.nomagic.magicdraw.properties">StringProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.LocaleProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="LocaleProperty.html" title="class in com.nomagic.magicdraw.properties">LocaleProperty</a> p)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PageFormatProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PageFormatProperty.html" title="class in com.nomagic.magicdraw.properties">PageFormatProperty</a> p)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.Style)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="Style.html" title="class in com.nomagic.magicdraw.properties">Style</a> p)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.JarEntryProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="JarEntryProperty.html" title="class in com.nomagic.magicdraw.properties">JarEntryProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.JDBCDriverClassNameProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="JDBCDriverClassNameProperty.html" title="class in com.nomagic.magicdraw.properties">JDBCDriverClassNameProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.PasswordProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="PasswordProperty.html" title="class in com.nomagic.magicdraw.properties">PasswordProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ClassPathEntriesListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ClassPathEntriesListProperty.html" title="class in com.nomagic.magicdraw.properties">ClassPathEntriesListProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.TypeProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="TypeProperty.html" title="class in com.nomagic.magicdraw.properties">TypeProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ElementProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ElementProperty.html" title="class in com.nomagic.magicdraw.properties">ElementProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ValueSpecificationProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ValueSpecificationProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.SpecificElementProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.SpecificElementProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ConstraintProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ConstraintProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ElementListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ElementListProperty.html" title="class in com.nomagic.magicdraw.properties">ElementListProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ElementInstanceProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ElementInstanceProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ListProperty.html" title="class in com.nomagic.magicdraw.properties">ListProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ExtendablePropertyManager)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="ExtendablePropertyManager.html" title="class in com.nomagic.magicdraw.properties">ExtendablePropertyManager</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ui.ObjectListProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ui.ObjectListProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ExternalToolProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ExternalToolProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.ImageProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.ImageProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.MapProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(com.nomagic.magicdraw.properties.MapProperty o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="visit(com.nomagic.magicdraw.properties.DateTimeProperty)">
<h3>visit</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">visit</span><wbr/><span class="parameters">(<a href="DateTimeProperty.html" title="class in com.nomagic.magicdraw.properties">DateTimeProperty</a> o)</span>
    throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
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
