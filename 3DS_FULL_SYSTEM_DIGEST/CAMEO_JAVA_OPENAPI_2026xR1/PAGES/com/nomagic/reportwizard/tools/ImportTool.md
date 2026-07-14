# JAVA OPENAPI: ImportTool (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/reportwizard/tools/ImportTool.html
- source_path: `com/nomagic/reportwizard/tools/ImportTool.html`
- source_sha256: `12d5e2e271c0b9877a9a8c69254c6a4538197de135113921a49757cd05bde46f`
- captured_utc: `2026-07-14T16:46:14.917999+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools](package-summary.html)

## Class ImportTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../magicreport/engine/Tool.html)
com.nomagic.reportwizard.tools.ImportTool

All Implemented Interfaces:
`[IChildEngine](../../magicreport/engine/IChildEngine.html)`, `[ITool](../../magicreport/engine/ITool.html)`, `[IVariable](../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`, `[Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html)`

Direct Known Subclasses:
`[DefaultImporterTool](importer/DefaultImporterTool.html)`

@OpenApiAllpublic classImportTool
extends [Tool](../../magicreport/engine/Tool.html)
implements [Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html), [IChildEngine](../../magicreport/engine/IChildEngine.html)

This tool will allow us to import Child-Templates at Velocity Runtime.

Since:
Dec 11, 2008
See Also:
[Serialized Form](../../../../serialized-form.html#com.nomagic.reportwizard.tools.ImportTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static org.apache.logging.log4j.Logger`
`[log](#log)`
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[context](../../magicreport/engine/Tool.html#context), [properties](../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[VOID](../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ImportTool](#%3Cinit%3E())()`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[fileImporter](#fileImporter(java.lang.Object,java.lang.String))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
Gets the String content of the import.
`[ITemplateEngine](../../magicreport/engine/ITemplateEngine.html)`
`[getParentEngine](#getParentEngine())()`
Get parent engine.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[importer](#importer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
Gets the String content of a specific attached file element.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[importer](#importer(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
Gets the String content of a specific import file path.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[include](#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
This method will include all the content of a specific attached file element.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[include](#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
This method will include the subSection of a specific attached file element. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[include](#include(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName)`
This method will include all the content of a child template.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[include](#include(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
This method will include the subSection of the ChildTemplate. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[includeSection](#includeSection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
This method will include the subSection of a specific attached file element. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.
`[CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html)`
`[includeSection](#includeSection(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)`
This method will include the subSection of the ChildTemplate. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives as introduced in MagicReport 14.0.
`boolean`
`[isParentSupportChild](#isParentSupportChild(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) engineType)`

`void`
`[setParentEngine](#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](../../magicreport/engine/ITemplateEngine.html) parentEngine)`
Set parent engine.
`void`
`[setupTool](#setupTool(com.nomagic.reportwizard.tools.importer.DefaultImporterTool))([DefaultImporterTool](importer/DefaultImporterTool.html) importerTool)`
Set required properties and observer to importer tool.
`void`
`[update](#update(java.util.Observable,java.lang.Object))([Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html) o,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) arg)`
This method is called whenever the template engine is changed.
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../magicreport/engine/Tool.html)
`[clone](../../magicreport/engine/Tool.html#clone()), [getContext](../../magicreport/engine/Tool.html#getContext()), [getProperties](../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../../magicreport/engine/Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../magicreport/engine/ITool.html)
`[clearTool](../../magicreport/engine/ITool.html#clearTool())`

============ FIELD DETAIL =========== 
Field Details
log
public static org.apache.logging.log4j.Logger log
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ImportTool
public ImportTool()
Constructor.
 ============ METHOD DETAIL ========== 
Method Details
include
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) include([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
This method will include all the content of a specific attached file element.
Parameters:
`element` - the attached element
Returns:
the correctly formated Text from the ChildTemplate
include
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) include([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName)
This method will include all the content of a child template.
Parameters:
`templateFileName` - the path of childTemplate
Returns:
the correctly formated Text from the ChildTemplate
include
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) include([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
This method will include the subSection of a specific attached file element. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.
Parameters:
`element` - the attached element
`section` - the section to be included
Returns:
the correctly formated Section Text from the ChildTemplate
include
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) include([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
This method will include the subSection of the ChildTemplate. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.
Parameters:
`templateFileName` - the path of childTemplate
`section` - the section to be included
Returns:
the correctly formated Section Text from the ChildTemplate
includeSection
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) includeSection([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
This method will include the subSection of a specific attached file element. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.
Parameters:
`element` - the attached element
`section` - the section to be included
Returns:
the correctly formated Section Text from the ChildTemplate
includeSection
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) includeSection([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
This method will include the subSection of the ChildTemplate. 

 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives as introduced in MagicReport 14.0.
Parameters:
`templateFileName` - the path of childTemplate
`section` - the section to be included
Returns:
the correctly formated Section Text from the ChildTemplate
importer
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) importer([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
Gets the String content of a specific attached file element. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.
Parameters:
`element` - the attached element
`section` - if there is a section else this is null
Returns:
the evaluated and validated output from childTemplate
importer
public [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) importer([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
Gets the String content of a specific import file path. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.
Parameters:
`templateFileName` - the path of childTemplate to be evaluated
`section` - if there is a section else this is null
Returns:
the evaluated and validated output from childTemplate
fileImporter
protected [CharSequence](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html) fileImporter([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) section)
Gets the String content of the import. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.
Parameters:
`template` - the template path or attached file
`section` - if there is a section else this is null
Returns:
the evaluated and validated output from childTemplate
setupTool
public void setupTool([DefaultImporterTool](importer/DefaultImporterTool.html) importerTool)
Set required properties and observer to importer tool.
Parameters:
`importerTool` - current importer tool
update
public void update([Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html) o,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) arg)
This method is called whenever the template engine is changed. An template engine calls an Observable
 object's notifyObservers method to have all the object's observers notified of the change.
Specified by:
`[update](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html#update(java.util.Observable,java.lang.Object))` in interface `[Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html)`
Parameters:
`o` - the observable object
`arg` - an argument passed to the notifyObservers method.
getParentEngine
public [ITemplateEngine](../../magicreport/engine/ITemplateEngine.html) getParentEngine()
Description copied from interface: `[IChildEngine](../../magicreport/engine/IChildEngine.html#getParentEngine())`
Get parent engine.
Specified by:
`[getParentEngine](../../magicreport/engine/IChildEngine.html#getParentEngine())` in interface `[IChildEngine](../../magicreport/engine/IChildEngine.html)`
Returns:
parent engine
setParentEngine
public void setParentEngine([ITemplateEngine](../../magicreport/engine/ITemplateEngine.html) parentEngine)
Description copied from interface: `[IChildEngine](../../magicreport/engine/IChildEngine.html#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine))`
Set parent engine.
Specified by:
`[setParentEngine](../../magicreport/engine/IChildEngine.html#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine))` in interface `[IChildEngine](../../magicreport/engine/IChildEngine.html)`
Parameters:
`parentEngine` - parent engine
isParentSupportChild
public boolean isParentSupportChild([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) engineType)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools</a></div>
<h1 class="title" title="Class ImportTool">Class ImportTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.ImportTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../magicreport/engine/IChildEngine.html" title="interface in com.nomagic.magicreport.engine">IChildEngine</a></code>, <code><a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="importer/DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ImportTool</span>
<span class="extends-implements">extends <a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a>, <a href="../../magicreport/engine/IChildEngine.html" title="interface in com.nomagic.magicreport.engine">IChildEngine</a></span></div>
<div class="block">This tool will allow us to import Child-Templates at Velocity Runtime.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Dec 11, 2008</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../serialized-form.html#com.nomagic.reportwizard.tools.ImportTool">Serialized Form</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">
<h2>Nested Class Summary</h2>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static org.apache.logging.log4j.Logger</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#log">log</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#context">context</a>, <a href="../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ImportTool</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor.</div>
</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fileImporter(java.lang.Object,java.lang.String)">fileImporter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the String content of the import.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentEngine()">getParentEngine</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get parent engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">importer</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the String content of a specific attached file element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#importer(java.lang.String,java.lang.String)">importer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the String content of a specific import file path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">include</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method will include all the content of a specific attached file element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">include</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method will include the subSection of a specific attached file  element.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#include(java.lang.String)">include</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method will include all the content of a child template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#include(java.lang.String,java.lang.String)">include</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method will include the subSection of the ChildTemplate.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#includeSection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">includeSection</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method will include the subSection of a specific attached file  element.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#includeSection(java.lang.String,java.lang.String)">includeSection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method will include the subSection of the ChildTemplate.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives as introduced in MagicReport 14.0.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isParentSupportChild(java.lang.String)">isParentSupportChild</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> engineType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)">setParentEngine</a><wbr/>(<a href="../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set parent engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setupTool(com.nomagic.reportwizard.tools.importer.DefaultImporterTool)">setupTool</a><wbr/>(<a href="importer/DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a> importerTool)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set required properties and observer to importer tool.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#update(java.util.Observable,java.lang.Object)">update</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a> o,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> arg)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method is called whenever the template engine is changed.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="log">
<h3>log</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">org.apache.logging.log4j.Logger</span> <span class="element-name">log</span></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ImportTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ImportTool</span>()</div>
<div class="block">Constructor.</div>
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
<section class="detail" id="include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>include</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">include</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">This method will include all the content of a specific attached file element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the attached element</dd>
<dt>Returns:</dt>
<dd>the correctly formated Text from the ChildTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="include(java.lang.String)">
<h3>include</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">include</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName)</span></div>
<div class="block">This method will include all the content of a child template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - the path of childTemplate</dd>
<dt>Returns:</dt>
<dd>the correctly formated Text from the ChildTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="include(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>include</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">include</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span></div>
<div class="block">This method will include the subSection of a specific attached file  element.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the attached element</dd>
<dd><code>section</code> - the section to be included</dd>
<dt>Returns:</dt>
<dd>the correctly formated Section Text from the ChildTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="include(java.lang.String,java.lang.String)">
<h3>include</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">include</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span></div>
<div class="block">This method will include the subSection of the ChildTemplate.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - the path of childTemplate</dd>
<dd><code>section</code> - the section to be included</dd>
<dt>Returns:</dt>
<dd>the correctly formated Section Text from the ChildTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="includeSection(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>includeSection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">includeSection</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span></div>
<div class="block">This method will include the subSection of a specific attached file  element.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the attached element</dd>
<dd><code>section</code> - the section to be included</dd>
<dt>Returns:</dt>
<dd>the correctly formated Section Text from the ChildTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="includeSection(java.lang.String,java.lang.String)">
<h3>includeSection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">includeSection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span></div>
<div class="block">This method will include the subSection of the ChildTemplate.<br/>
 The ChildTemplate has to be formatted according to the already existing #sectionBegin and #sectionEnd
 directives as introduced in MagicReport 14.0.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - the path of childTemplate</dd>
<dd><code>section</code> - the section to be included</dd>
<dt>Returns:</dt>
<dd>the correctly formated Section Text from the ChildTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importer(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>importer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">importer</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span></div>
<div class="block">Gets the String content of a specific attached file element. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the attached element</dd>
<dd><code>section</code> - if there is a section else this is null</dd>
<dt>Returns:</dt>
<dd>the evaluated and validated output from childTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importer(java.lang.String,java.lang.String)">
<h3>importer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">importer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span></div>
<div class="block">Gets the String content of a specific import file path. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - the path of childTemplate to be evaluated</dd>
<dd><code>section</code> - if there is a section else this is null</dd>
<dt>Returns:</dt>
<dd>the evaluated and validated output from childTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fileImporter(java.lang.Object,java.lang.String)">
<h3>fileImporter</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/CharSequence.html" title="class or interface in java.lang">CharSequence</a></span> <span class="element-name">fileImporter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> section)</span></div>
<div class="block">Gets the String content of the import. This will do all the importTool's work. It is called by both public
 methods, with the difference that section is null if we want to include the whole file. Else it has a
 section name and only that subsection will be included.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - the template path or attached file</dd>
<dd><code>section</code> - if there is a section else this is null</dd>
<dt>Returns:</dt>
<dd>the evaluated and validated output from childTemplate</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setupTool(com.nomagic.reportwizard.tools.importer.DefaultImporterTool)">
<h3>setupTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setupTool</span><wbr/><span class="parameters">(<a href="importer/DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a> importerTool)</span></div>
<div class="block">Set required properties and observer to importer tool.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>importerTool</code> - current importer tool</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="update(java.util.Observable,java.lang.Object)">
<h3>update</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">update</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a> o,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> arg)</span></div>
<div class="block">This method is called whenever the template engine is changed. An template engine calls an Observable
 object's notifyObservers method to have all the object's observers notified of the change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html#update(java.util.Observable,java.lang.Object)" title="class or interface in java.util">update</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - the observable object</dd>
<dd><code>arg</code> - an argument passed to the notifyObservers method.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getParentEngine()">
<h3>getParentEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></span> <span class="element-name">getParentEngine</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="../../magicreport/engine/IChildEngine.html#getParentEngine()">IChildEngine</a></code></span></div>
<div class="block">Get parent engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../magicreport/engine/IChildEngine.html#getParentEngine()">getParentEngine</a></code> in interface <code><a href="../../magicreport/engine/IChildEngine.html" title="interface in com.nomagic.magicreport.engine">IChildEngine</a></code></dd>
<dt>Returns:</dt>
<dd>parent engine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>setParentEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentEngine</span><wbr/><span class="parameters">(<a href="../../magicreport/engine/ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code><a href="../../magicreport/engine/IChildEngine.html#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)">IChildEngine</a></code></span></div>
<div class="block">Set parent engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../magicreport/engine/IChildEngine.html#setParentEngine(com.nomagic.magicreport.engine.ITemplateEngine)">setParentEngine</a></code> in interface <code><a href="../../magicreport/engine/IChildEngine.html" title="interface in com.nomagic.magicreport.engine">IChildEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>parentEngine</code> - parent engine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isParentSupportChild(java.lang.String)">
<h3>isParentSupportChild</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isParentSupportChild</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> engineType)</span></div>
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
