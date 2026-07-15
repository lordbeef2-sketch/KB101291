# JAVA OPENAPI: IVariable (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/IVariable.html
- source_path: `com/nomagic/magicreport/IVariable.html`
- source_sha256: `add3f22c428ae51cb037e08fd2b1dbb8c394aae19dbb00e29530394ea0d587dd`
- captured_utc: `2026-07-14T16:58:36.440275+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport](package-summary.html)

## Interface IVariable

All Superinterfaces:
`[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`

All Known Subinterfaces:
`[ITool](engine/ITool.html)`

All Known Implementing Classes:
`[ArrayTool](engine/tools/ArrayTool.html)`, `[Bookmark](Bookmark.html)`, `[BookmarkTool](engine/tools/BookmarkTool.html)`, `[ChartTool](../reportwizard/tools/ChartTool.html)`, `[Column](Column.html)`, `[ConcurrentTool](engine/ConcurrentTool.html)`, `[DefaultImporterTool](../reportwizard/tools/importer/DefaultImporterTool.html)`, `[DependencyMatrixTool](../reportwizard/tools/DependencyMatrixTool.html)`, `[DialogTool](../reportwizard/tools/DialogTool.html)`, `[Directive](parser/Directive.html)`, `[DocBookTool](../reportwizard/tools/DocBookTool.html)`, `[DOCXImporterTool](../reportwizard/tools/importer/DOCXImporterTool.html)`, `[ExportTool2](../magicdraw/magicreport/tools/ExportTool2.html)`, `[ExportTool3](../magicdraw/magicreport/tools/ExportTool3.html)`, `[FileTool](engine/tools/FileTool.html)`, `[GenericTableTool](../reportwizard/tools/GenericTableTool.html)`, `[GridRowSpan](GridRowSpan.html)`, `[GridSpan](GridSpan.html)`, `[GroovyTool](../reportwizard/tools/script/GroovyTool.html)`, `[GroupTool](engine/tools/GroupTool.html)`, `[Image](Image.html)`, `[ImageTool](engine/tools/ImageTool.html)`, `[ImportTool](../reportwizard/tools/ImportTool.html)`, `[ITool.HTMLString](engine/ITool.HTMLString.html)`, `[ITool.RetainedString](engine/ITool.RetainedString.html)`, `[ITool.Void](engine/ITool.Void.html)`, `[JavaDocTool](../reportwizard/tools/doc/JavaDocTool.html)`, `[JavaScriptTool](../reportwizard/tools/script/JavaScriptTool.html)`, `[Link](Link.html)`, `[MapTool](engine/tools/MapTool.html)`, `[MathTool](../reportwizard/tools/MathTool.html)`, `[ModelValidationTool](../reportwizard/tools/ModelValidationTool.html)`, `[OOXMLTagString](engine/ooxml/OOXMLTagString.html)`, `[ProfilingTool](../magicdraw/magicreport/tools/ProfilingTool.html)`, `[ProjectTool](../magicdraw/magicreport/tools/ProjectTool.html)`, `[QueryTool](../reportwizard/tools/QueryTool.html)`, `[ReportFileTool](../magicdraw/magicreport/tools/ReportFileTool.html)`, `[ReportHelper](../magicdraw/magicreport/helper/ReportHelper.html)`, `[ReportSVGIcon](ReportSVGIcon.html)`, `[Row](Row.html)`, `[SorterTool](../magicdraw/magicreport/tools/SorterTool.html)`, `[SortTable](../reportwizard/tools/dialog/SortTable.html)`, `[SortTool](engine/tools/SortTool.html)`, `[SVGIcon](SVGIcon.html)`, `[TemplateTool](../magicdraw/magicreport/tools/TemplateTool.html)`, `[TemplateTool](engine/tools/TemplateTool.html)`, `[TextReference](TextReference.html)`, `[TextTool](../reportwizard/tools/TextTool.html)`, `[Tool](engine/Tool.html)`

@OpenApiAllpublic interfaceIVariableextends [Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)

Interface for report variable object. All report variable object *should* implements this interface.

Since:
Feb 16, 2010 12:17:30 PM

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport</a></div>
<h1 class="title" title="Interface IVariable">Interface IVariable</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="engine/tools/ArrayTool.html" title="class in com.nomagic.magicreport.engine.tools">ArrayTool</a></code>, <code><a href="Bookmark.html" title="class in com.nomagic.magicreport">Bookmark</a></code>, <code><a href="engine/tools/BookmarkTool.html" title="class in com.nomagic.magicreport.engine.tools">BookmarkTool</a></code>, <code><a href="../reportwizard/tools/ChartTool.html" title="class in com.nomagic.reportwizard.tools">ChartTool</a></code>, <code><a href="Column.html" title="class in com.nomagic.magicreport">Column</a></code>, <code><a href="engine/ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></code>, <code><a href="../reportwizard/tools/importer/DefaultImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DefaultImporterTool</a></code>, <code><a href="../reportwizard/tools/DependencyMatrixTool.html" title="class in com.nomagic.reportwizard.tools">DependencyMatrixTool</a></code>, <code><a href="../reportwizard/tools/DialogTool.html" title="class in com.nomagic.reportwizard.tools">DialogTool</a></code>, <code><a href="parser/Directive.html" title="class in com.nomagic.magicreport.parser">Directive</a></code>, <code><a href="../reportwizard/tools/DocBookTool.html" title="class in com.nomagic.reportwizard.tools">DocBookTool</a></code>, <code><a href="../reportwizard/tools/importer/DOCXImporterTool.html" title="class in com.nomagic.reportwizard.tools.importer">DOCXImporterTool</a></code>, <code><a href="../magicdraw/magicreport/tools/ExportTool2.html" title="class in com.nomagic.magicdraw.magicreport.tools">ExportTool2</a></code>, <code><a href="../magicdraw/magicreport/tools/ExportTool3.html" title="class in com.nomagic.magicdraw.magicreport.tools">ExportTool3</a></code>, <code><a href="engine/tools/FileTool.html" title="class in com.nomagic.magicreport.engine.tools">FileTool</a></code>, <code><a href="../reportwizard/tools/GenericTableTool.html" title="class in com.nomagic.reportwizard.tools">GenericTableTool</a></code>, <code><a href="GridRowSpan.html" title="class in com.nomagic.magicreport">GridRowSpan</a></code>, <code><a href="GridSpan.html" title="class in com.nomagic.magicreport">GridSpan</a></code>, <code><a href="../reportwizard/tools/script/GroovyTool.html" title="class in com.nomagic.reportwizard.tools.script">GroovyTool</a></code>, <code><a href="engine/tools/GroupTool.html" title="class in com.nomagic.magicreport.engine.tools">GroupTool</a></code>, <code><a href="Image.html" title="class in com.nomagic.magicreport">Image</a></code>, <code><a href="engine/tools/ImageTool.html" title="class in com.nomagic.magicreport.engine.tools">ImageTool</a></code>, <code><a href="../reportwizard/tools/ImportTool.html" title="class in com.nomagic.reportwizard.tools">ImportTool</a></code>, <code><a href="engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a></code>, <code><a href="engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a></code>, <code><a href="engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code>, <code><a href="../reportwizard/tools/doc/JavaDocTool.html" title="class in com.nomagic.reportwizard.tools.doc">JavaDocTool</a></code>, <code><a href="../reportwizard/tools/script/JavaScriptTool.html" title="class in com.nomagic.reportwizard.tools.script">JavaScriptTool</a></code>, <code><a href="Link.html" title="class in com.nomagic.magicreport">Link</a></code>, <code><a href="engine/tools/MapTool.html" title="class in com.nomagic.magicreport.engine.tools">MapTool</a></code>, <code><a href="../reportwizard/tools/MathTool.html" title="class in com.nomagic.reportwizard.tools">MathTool</a></code>, <code><a href="../reportwizard/tools/ModelValidationTool.html" title="class in com.nomagic.reportwizard.tools">ModelValidationTool</a></code>, <code><a href="engine/ooxml/OOXMLTagString.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLTagString</a></code>, <code><a href="../magicdraw/magicreport/tools/ProfilingTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProfilingTool</a></code>, <code><a href="../magicdraw/magicreport/tools/ProjectTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ProjectTool</a></code>, <code><a href="../reportwizard/tools/QueryTool.html" title="class in com.nomagic.reportwizard.tools">QueryTool</a></code>, <code><a href="../magicdraw/magicreport/tools/ReportFileTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ReportFileTool</a></code>, <code><a href="../magicdraw/magicreport/helper/ReportHelper.html" title="class in com.nomagic.magicdraw.magicreport.helper">ReportHelper</a></code>, <code><a href="ReportSVGIcon.html" title="class in com.nomagic.magicreport">ReportSVGIcon</a></code>, <code><a href="Row.html" title="class in com.nomagic.magicreport">Row</a></code>, <code><a href="../magicdraw/magicreport/tools/SorterTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">SorterTool</a></code>, <code><a href="../reportwizard/tools/dialog/SortTable.html" title="class in com.nomagic.reportwizard.tools.dialog">SortTable</a></code>, <code><a href="engine/tools/SortTool.html" title="class in com.nomagic.magicreport.engine.tools">SortTool</a></code>, <code><a href="SVGIcon.html" title="class in com.nomagic.magicreport">SVGIcon</a></code>, <code><a href="../magicdraw/magicreport/tools/TemplateTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">TemplateTool</a></code>, <code><a href="engine/tools/TemplateTool.html" title="class in com.nomagic.magicreport.engine.tools">TemplateTool</a></code>, <code><a href="TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></code>, <code><a href="../reportwizard/tools/TextTool.html" title="class in com.nomagic.reportwizard.tools">TextTool</a></code>, <code><a href="engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">IVariable</span><span class="extends-implements">
extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></span></div>
<div class="block">Interface for report variable object. All report variable object <i>should</i> implements this interface.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Feb 16, 2010 12:17:30 PM</dd>
</dl>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
