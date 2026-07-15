# JAVA OPENAPI: DOCXEngine (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/velocity/DOCXEngine.html
- source_path: `com/nomagic/magicreport/engine/velocity/DOCXEngine.html`
- source_sha256: `49a853f540fec8ea5a37c1cdb71a52e2cdad3988af2e730d091375cb943c29b5`
- captured_utc: `2026-07-14T16:46:13.219977+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class DOCXEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.AbstractTemplateEngine](../AbstractTemplateEngine.html)
[com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine](DefaultTemplateEngine.html)
com.nomagic.magicreport.engine.velocity.DOCXEngine

All Implemented Interfaces:
`[IExtensionTemplateEngine](../IExtensionTemplateEngine.html)`, `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`, `[ITemplateEngine](../ITemplateEngine.html)`, `[StyledDocument](../../format/html/StyledDocument.html)`

@OpenApiAllpublic classDOCXEngine
extends [DefaultTemplateEngine](DefaultTemplateEngine.html)
implements [StyledDocument](../../format/html/StyledDocument.html)

The Velocity engine for OpenXML Word Document (DOCX).

Since:
Oct 19, 2009

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[DOCXEngine.ContentTypeProcess](DOCXEngine.ContentTypeProcess.html)`
Handle content type
`static class`
`[DOCXEngine.DocumentRelationshipProcess](DOCXEngine.DocumentRelationshipProcess.html)`
Handle document relationship
`static class`
`[DOCXEngine.NumberingProcess](DOCXEngine.NumberingProcess.html)`
Handle numbering File
`static class`
`[DOCXEngine.NumberingUpdateProcess](DOCXEngine.NumberingUpdateProcess.html)`
Handle numbering for child document
 This abstractNumId and numId in this file should be updated
`static class`
`[DOCXEngine.StyleProcess](DOCXEngine.StyleProcess.html)`
Handle style File
`static class`
`[DOCXEngine.StyleUpdateProcess](DOCXEngine.StyleUpdateProcess.html)`
Handle style for child document
 This id and name in this file may be updated
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.velocity.[DefaultTemplateEngine](DefaultTemplateEngine.html)
`[velocityContext](DefaultTemplateEngine.html#velocityContext)`
Fields inherited from class com.nomagic.magicreport.engine.[AbstractTemplateEngine](../AbstractTemplateEngine.html)
`[context](../AbstractTemplateEngine.html#context), [isAborted](../AbstractTemplateEngine.html#isAborted), [preProcessFile](../AbstractTemplateEngine.html#preProcessFile), [processFile](../AbstractTemplateEngine.html#processFile), [properties](../AbstractTemplateEngine.html#properties)`
Fields inherited from interface com.nomagic.magicreport.format.html.[StyledDocument](../../format/html/StyledDocument.html)
`[CHARACTER](../../format/html/StyledDocument.html#CHARACTER), [COLOR](../../format/html/StyledDocument.html#COLOR), [FONT](../../format/html/StyledDocument.html#FONT), [PARAGRAPH](../../format/html/StyledDocument.html#PARAGRAPH), [TABLE](../../format/html/StyledDocument.html#TABLE)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DOCXEngine](#%3Cinit%3E())()`
A class constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addChart](#addChart())()`

`int`
`[addColor](#addColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)`
Add color for HTML to DOCX.
`int`
`[addFont](#addFont(java.awt.Font))([Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font)`
Add font for HTML to DOCX.
`void`
`[addHyperLink](#addHyperLink(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) rId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url)`
Add rId for hyper link.
`void`
`[addImage](#addImage(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) rId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageType)`
Add rId for hyper link.
`int`
`[addList](#addList(com.nomagic.magicreport.format.html.List))([List](../../format/html/List.html) list)`
Add list for HTML to DOCX.
`int`
`[addObject](#addObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)`
Appends object content into the document.
`int`
`[addPageSections](#addPageSections(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str)`

`void`
`[addRowSpanID](#addRowSpanID(java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 int value)`
Add rowspan id and its value to map
`int`
`[addStyle](#addStyle(javax.swing.text.Style))([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) style)`
Add style for HTML to DOCX.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createComment](#createComment(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Return a formatted comment from given message.
`protected [ParseErrorException](../../ParseErrorException.html)`
`[createParseErrorWrapper](#createParseErrorWrapper(com.nomagic.magicreport.ParseErrorException,java.io.Reader))([ParseErrorException](../../ParseErrorException.html) parseError,
 [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) source)`
Create a ParseErrorException from the message.
`[Template](../../Template.html)`
`[createTemplate](#createTemplate())()`
Creates a new [`Template`](../../Template.html) object for generating report by this engine.
`[Template](../../Template.html)`
`[createTemplate](#createTemplate(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)`
Creates a new [`Template`](../../Template.html) object.
`[Template](../../Template.html)`
`[createTemplate](#createTemplate(java.io.File,java.io.File,boolean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output,
 boolean ignoreLocation)`
Creates a new [`Template`](../../Template.html) object.
`[Template](../../Template.html)`
`[createTemplate](#createTemplate(java.io.File,java.io.File,boolean,boolean))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output,
 boolean ignoreDocInfo,
 boolean ignoreLocation)`
Creates a new [`Template`](../../Template.html) object.
`void`
`[destroy](#destroy())()`
Called by the application or [`TemplateEngineFactory`](../../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
`void`
`[evaluate](#evaluate(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Merge a template with current context and rendered stream into the writer.
`int`
`[getAbStractId](#getAbStractId())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[]>>`
`[getAbstractNumbering](#getAbstractNumbering())()`

`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getBookmarkList](#getBookmarkList())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark>`
`[getBookmarkListMap](#getBookmarkListMap())()`

`int`
`[getBookmarkN](#getBookmarkN())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getCharsetName](#getCharsetName())()`

`[DocumentInfo](../ooxml/child/docx/DocumentInfo.html)`
`[getDocInfo](#getDocInfo())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getDocProp](#getDocProp())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getDocPropList](#getDocPropList())()`

`[Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html)`
`[getDocument](#getDocument())()`

`void`
`[getDocumentSubFileInfo](#getDocumentSubFileInfo(com.nomagic.magicreport.Template,java.lang.String,org.xml.sax.helpers.DefaultHandler))([Template](../../Template.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) handler)`
Get content of sub file before evaluate
`void`
`[getEntryContent](#getEntryContent(com.nomagic.magicreport.Template,java.lang.String))([Template](../../Template.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)`
Get entry from input file and entryName.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)>`
`[getEntryMap](#getEntryMap())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getEntryName](#getEntryName())()`

`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getEntryNameSet](#getEntryNameSet())()`

`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getEntrySet](#getEntrySet())()`
Return DOCX entry set.
`com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument`
`[getEvaluatedDocument](#getEvaluatedDocument())()`

`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getEvaluatedDocumentBuffer](#getEvaluatedDocumentBuffer())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getHyperLinkMap](#getHyperLinkMap())()`

`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getImageFormat](#getImageFormat())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getImageMap](#getImageMap())()`

`[DocumentInfo](../ooxml/child/docx/DocumentInfo.html)`
`[getMainDocInfo](#getMainDocInfo())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getNumberingDef](#getNumberingDef())()`

`int`
`[getNumId](#getNumId())()`

`[OOXMLTemplate](../../OOXMLTemplate.html)`
`[getOoxmlTemplate](#getOoxmlTemplate())()`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getPageSections](#getPageSections(int))(int index)`

`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getStyleIds](#getStyleIds())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getStyleNameMap](#getStyleNameMap())()`

`[Template](../../Template.html)`
`[getTemplate](#getTemplate())()`
Return template.
`protected void`
`[handleContentType](#handleContentType(java.util.Set,java.util.Set,java.lang.StringBuilder,java.util.Map))([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType> contentTypes,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType> sectionContentTypes,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) contentTypeContentBuilder,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>> newFilesInZip)`
Handle [Content_Type].xml after evaluate.
`protected void`
`[handleForColumn](#handleForColumn(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #forcol directive.
`protected void`
`[handleForPage](#handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #forpage directive.
`protected void`
`[handleForRow](#handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #forrow directive.
`protected void`
`[handleGridCol](#handleGridCol(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Add id to w:gridCol tag.
`protected void`
`[handleIncludeSection](#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #includeSection directive.
`protected void`
`[handleIncludeSection](#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer,
 [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) child)`
Handle the #includeSection directive.
`protected void`
`[handleMergeColumns](#handleMergeColumns(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle $tableprop.mergeColumns directive
`protected void`
`[handleMergeRows](#handleMergeRows(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle $tableprop.mergeRows directive
`protected [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html)`
`[handleNumbering](#handleNumbering(javax.xml.parsers.DocumentBuilder,org.w3c.dom.Document,java.io.File,java.lang.StringBuilder,java.util.List,java.util.List,java.util.Map))([DocumentBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html) docBuilder,
 [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) baseNumberingDocument,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) sectionZipFile,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) numberingContent,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> abstractNumIds,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numIds,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numberingNamespaceMap)`
Handle numbering.xml.
`protected void`
`[handleRelationship](#handleRelationship(com.nomagic.magicreport.engine.ooxml.OOXMLStreamWriter,java.io.File,java.util.Map,java.lang.String,java.util.Map,java.lang.StringBuilder))([OOXMLStreamWriter](../ooxml/OOXMLStreamWriter.html) ooxmlWriter,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) sectionZipFile,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),? extends com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> relationshipMap,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) relationshipPrefix,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>> newFilesInZip,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) relationContentBuilder)`
Handle relationship file after evaluate.
`protected void`
`[handleSectionBegin](#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #sectionBegin directive.
`protected void`
`[handleSharedFiles](#handleSharedFiles())()`
Handle document.xml.rels, [Content_Types].xml, styles.xml, and numbering.xml
`protected [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html)`
`[handleStyle](#handleStyle(javax.xml.parsers.DocumentBuilder,org.w3c.dom.Document,java.io.File,java.lang.StringBuilder,java.util.List,java.util.List,java.util.Map))([DocumentBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html) docBuilder,
 [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) baseStyleDocument,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) sectionZipFile,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) styleContent,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleIds,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleLatents,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> namespaceMap)`
Handle styles.xml after evaluate.
`void`
`[intenalEvaluate](#intenalEvaluate(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`

`boolean`
`[isHasNumbering](#isHasNumbering())()`

`boolean`
`[isInMultipleLineComment](#isInMultipleLineComment())()`

`boolean`
`[isMemoryMode](#isMemoryMode(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Tests if this template should process in memory mode. 

 This method is similar to code:
`int`
`[lineCount](#lineCount(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)`
Count number of line from given content string.
`protected void`
`[postProcess](#postProcess(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Perform a post-processing after the template has been evaluated.
`protected [TemplateException](../../TemplateException.html)`
`[processVelocityException](#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException))([Template](../../Template.html) template,
 org.apache.velocity.exception.ParseErrorException e)`
Call this method to process an Velocity exception and return in new format.
`void`
`[setAbStractId](#setAbStractId(int))(int abStractId)`

`void`
`[setAbstractNumbering](#setAbstractNumbering(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[]>> abstractNumbering)`

`void`
`[setBookmarkList](#setBookmarkList(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> bookmarkList)`

`void`
`[setBookmarkListMap](#setBookmarkListMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark> bookmarkListMap)`

`void`
`[setBookmarkN](#setBookmarkN(int))(int bookmarkN)`

`void`
`[setCharsetName](#setCharsetName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName)`

`void`
`[setCheckSize](#setCheckSize(boolean))(boolean isCheckFileSize)`

`void`
`[setDocInfo](#setDocInfo(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo))([DocumentInfo](../ooxml/child/docx/DocumentInfo.html) docInfo)`

`void`
`[setDocProp](#setDocProp(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> docProp)`

`void`
`[setDocPropList](#setDocPropList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> docPropList)`

`void`
`[setDocument](#setDocument(org.w3c.dom.Document))([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document)`

`void`
`[setEntryMap](#setEntryMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)> entryMap)`

`void`
`[setEntryName](#setEntryName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)`

`void`
`[setEntryNameSet](#setEntryNameSet(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> entryNameSet)`

`void`
`[setEvaluatedDocument](#setEvaluatedDocument(com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument))(com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument evaluatedDocument)`

`void`
`[setHasNumbering](#setHasNumbering(boolean))(boolean hasNumbering)`

`void`
`[setHyperLinkMap](#setHyperLinkMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> hyperLinkMap)`

`void`
`[setImageFormat](#setImageFormat(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> imageFormat)`

`void`
`[setImageMap](#setImageMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> imageMap)`

`void`
`[setInMultipleLineComment](#setInMultipleLineComment(boolean))(boolean inMultipleLineComment)`

`void`
`[setNumberingDef](#setNumberingDef(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numberingDef)`

`void`
`[setNumId](#setNumId(int))(int numId)`

`void`
`[setOoxmlTemplate](#setOoxmlTemplate(com.nomagic.magicreport.OOXMLTemplate))([OOXMLTemplate](../../OOXMLTemplate.html) ooxmlTemplate)`

`void`
`[setStyleIds](#setStyleIds(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleIds)`

`void`
`[setStyleNameMap](#setStyleNameMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleNameMap)`

`protected [BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)`
`[setWriterForEvaluate](#setWriterForEvaluate(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`

`void`
`[translate](#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Process the template in `inProcessBuffer` into valid format.
`void`
`[translate](#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer,
 [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) child)`
Process the template in `inProcessBuffer` into valid format.
`void`
`[translate](#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder,java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) child)`
Process the template in `inProcessBuffer` into valid format.
`void`
`[updateSize](#updateSize(long))(long size)`

`void`
`[updateStyleIds](#updateStyleIds(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) styleId)`

`void`
`[updateStyleNameMap](#updateStyleNameMap(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Methods inherited from class com.nomagic.magicreport.engine.velocity.[DefaultTemplateEngine](DefaultTemplateEngine.html)
`[abort](DefaultTemplateEngine.html#abort()), [checkFileNotFoundException](DefaultTemplateEngine.html#checkFileNotFoundException(java.lang.Exception,java.io.File)), [clearTools](DefaultTemplateEngine.html#clearTools()), [getClassLoader](DefaultTemplateEngine.html#getClassLoader()), [getFormatter](DefaultTemplateEngine.html#getFormatter()), [getResolvedSectionName](DefaultTemplateEngine.html#getResolvedSectionName(java.lang.String)), [handleImport](DefaultTemplateEngine.html#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [isNoSpaceException](DefaultTemplateEngine.html#isNoSpaceException(java.lang.Exception)), [preProcess](DefaultTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)), [process](DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template)), [process](DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)), [processException](DefaultTemplateEngine.html#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)), [processVelocityException](DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)), [setClassLoader](DefaultTemplateEngine.html#setClassLoader(java.lang.ClassLoader)), [setFormatter](DefaultTemplateEngine.html#setFormatter(com.nomagic.magicreport.format.IFormatter)), [setLatestLocation](DefaultTemplateEngine.html#setLatestLocation(java.io.File,java.io.File)), [setLocation](DefaultTemplateEngine.html#setLocation(java.io.File,java.io.File)), [setProperty](DefaultTemplateEngine.html#setProperty(java.lang.String,java.lang.Object)), [trimTrailSpace](DefaultTemplateEngine.html#trimTrailSpace(int,java.lang.StringBuilder))`
Methods inherited from class com.nomagic.magicreport.engine.[AbstractTemplateEngine](../AbstractTemplateEngine.html)
`[addContext](../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)), [addInvalidReferenceHandler](../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)), [addObserver](../AbstractTemplateEngine.html#addObserver(java.util.Observer)), [addReferenceInsertionHandler](../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)), [evaluate](../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)), [getConcurrentToolException](../AbstractTemplateEngine.html#getConcurrentToolException()), [getContext](../AbstractTemplateEngine.html#getContext()), [getCurrentRuntimeInstance](../AbstractTemplateEngine.html#getCurrentRuntimeInstance()), [getInvalidReferenceHandler](../AbstractTemplateEngine.html#getInvalidReferenceHandler()), [getProcessSize](../AbstractTemplateEngine.html#getProcessSize()), [getProperties](../AbstractTemplateEngine.html#getProperties()), [getProperty](../AbstractTemplateEngine.html#getProperty(java.lang.String)), [getReferenceInsertionHandler](../AbstractTemplateEngine.html#getReferenceInsertionHandler()), [notifyObservers](../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)), [observers](../AbstractTemplateEngine.html#observers()), [setConcurrentToolException](../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)), [setContext](../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)), [setCurrentRuntimeInstance](../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DOCXEngine
public DOCXEngine()
A class constructor.
 ============ METHOD DETAIL ========== 
Method Details
isInMultipleLineComment
public boolean isInMultipleLineComment()
setInMultipleLineComment
public void setInMultipleLineComment(boolean inMultipleLineComment)
isHasNumbering
public boolean isHasNumbering()
setHasNumbering
public void setHasNumbering(boolean hasNumbering)
getAbStractId
public int getAbStractId()
setAbStractId
public void setAbStractId(int abStractId)
getNumId
public int getNumId()
setNumId
public void setNumId(int numId)
getBookmarkN
public int getBookmarkN()
setBookmarkN
public void setBookmarkN(int bookmarkN)
getDocument
public [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) getDocument()
setDocument
public void setDocument([Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) document)
getImageFormat
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getImageFormat()
setImageFormat
public void setImageFormat([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> imageFormat)
getHyperLinkMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getHyperLinkMap()
setHyperLinkMap
public void setHyperLinkMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> hyperLinkMap)
getImageMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getImageMap()
setImageMap
public void setImageMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> imageMap)
getEntryNameSet
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getEntryNameSet()
setEntryNameSet
public void setEntryNameSet([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> entryNameSet)
getEntryMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)> getEntryMap()
setEntryMap
public void setEntryMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)> entryMap)
getBookmarkList
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getBookmarkList()
setBookmarkList
public void setBookmarkList([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> bookmarkList)
getBookmarkListMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark> getBookmarkListMap()
setBookmarkListMap
public void setBookmarkListMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark> bookmarkListMap)
getNumberingDef
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getNumberingDef()
setNumberingDef
public void setNumberingDef([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numberingDef)
getAbstractNumbering
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[]>> getAbstractNumbering()
setAbstractNumbering
public void setAbstractNumbering([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)[]>> abstractNumbering)
getDocProp
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getDocProp()
setDocProp
public void setDocProp([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> docProp)
getEntryName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getEntryName()
setEntryName
public void setEntryName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)
getCharsetName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getCharsetName()
setCharsetName
public void setCharsetName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) charsetName)
getOoxmlTemplate
public [OOXMLTemplate](../../OOXMLTemplate.html) getOoxmlTemplate()
setOoxmlTemplate
public void setOoxmlTemplate([OOXMLTemplate](../../OOXMLTemplate.html) ooxmlTemplate)
getDocPropList
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getDocPropList()
setDocPropList
public void setDocPropList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> docPropList)
getStyleNameMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getStyleNameMap()
setStyleNameMap
public void setStyleNameMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleNameMap)
updateStyleNameMap
public void updateStyleNameMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
getStyleIds
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getStyleIds()
setStyleIds
public void setStyleIds([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleIds)
updateStyleIds
public void updateStyleIds([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) styleId)
getPageSections
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getPageSections(int index)
addPageSections
public int addPageSections([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) str)
createTemplate
public [Template](../../Template.html) createTemplate()
Creates a new [`Template`](../../Template.html) object for generating report by this engine.
Specified by:
`[createTemplate](../ITemplateEngine.html#createTemplate())` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Overrides:
`[createTemplate](DefaultTemplateEngine.html#createTemplate())` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Returns:
an instance of [`Template`](../../Template.html)
See Also:
[`DefaultTemplateEngine.createTemplate(File, File)`](DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File))
createTemplate
public [Template](../../Template.html) createTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Creates a new [`Template`](../../Template.html) object.
Specified by:
`[createTemplate](../ITemplateEngine.html#createTemplate(java.io.File,java.io.File))` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Overrides:
`[createTemplate](DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`input` - template file.
`output` - output file.
Returns:
an instance of [`Template`](../../Template.html)
Throws:
`[FileNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html)` - if the file does not exist, is a directory rather than a regular file,
 or for some other reason cannot be opened.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
createTemplate
public [Template](../../Template.html) createTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output,
 boolean ignoreLocation)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Creates a new [`Template`](../../Template.html) object.
Overrides:
`[createTemplate](DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File,boolean))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`input` - template file.
`output` - output file.
`ignoreLocation` - true to ignore location property for child document
Returns:
an instance of [`Template`](../../Template.html)
Throws:
`[FileNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html)` - if the file does not exist, is a directory rather than a regular file,
 or for some other reason cannot be opened.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
createTemplate
public [Template](../../Template.html) createTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output,
 boolean ignoreDocInfo,
 boolean ignoreLocation)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Creates a new [`Template`](../../Template.html) object.
Parameters:
`input` - template file.
`output` - output file.
`ignoreDocInfo` - true to ignore create document info. this parameter should be true for creating template of child document
`ignoreLocation` - true to ignore location property for child document
Returns:
an instance of [`Template`](../../Template.html)
Throws:
`[FileNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html)` - if the file does not exist, is a directory rather than a regular file,
 or for some other reason cannot be opened.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If an I/O error occurs
evaluate
public void evaluate([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Merge a template with current context and rendered stream into the writer.
Specified by:
`[evaluate](../ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template))` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Overrides:
`[evaluate](../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template))` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
Parameters:
`template` - Template being evaluated
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`ITemplateEngine.evaluate(Template)`](../ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template))
setWriterForEvaluate
protected [BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html) setWriterForEvaluate([Template](../../Template.html) template)
Overrides:
`[setWriterForEvaluate](DefaultTemplateEngine.html#setWriterForEvaluate(com.nomagic.magicreport.Template))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
handleSharedFiles
protected void handleSharedFiles()
Handle document.xml.rels, [Content_Types].xml, styles.xml, and numbering.xml
handleRelationship
protected void handleRelationship([OOXMLStreamWriter](../ooxml/OOXMLStreamWriter.html) ooxmlWriter,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) sectionZipFile,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),? extends com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> relationshipMap,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) relationshipPrefix,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>> newFilesInZip,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) relationContentBuilder)
Handle relationship file after evaluate.
Parameters:
`ooxmlWriter` - writer
`sectionZipFile` - zip file of child template
`relationshipMap` - map of relationship and id
`relationshipPrefix` - prefix path for relationship
`newFilesInZip` - map of new files that are created after generated
`relationContentBuilder` - stringbuilder to keep relationship content
handleContentType
protected void handleContentType([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType> contentTypes,
 [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType> sectionContentTypes,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) contentTypeContentBuilder,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>> newFilesInZip)
Handle [Content_Type].xml after evaluate.
Parameters:
`contentTypes` - content type in main document
`sectionContentTypes` - content type in child document
`contentTypeContentBuilder` - Stringbuilder to create new content of [Content_Type].xml
`newFilesInZip` - map of partname and new target path
handleStyle
protected [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) handleStyle([DocumentBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html) docBuilder,
 [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) baseStyleDocument,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) sectionZipFile,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) styleContent,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleIds,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> styleLatents,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> namespaceMap)
Handle styles.xml after evaluate.
Parameters:
`docBuilder` - DocumentBuilder
`baseStyleDocument` - base document
`sectionZipFile` - zip file to be added
`styleContent` - all content of style
`styleIds` - existing style
`styleLatents` - existing latents
`namespaceMap` - namespaces of style
Returns:
base document
handleNumbering
protected [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) handleNumbering([DocumentBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html) docBuilder,
 [Document](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html) baseNumberingDocument,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) sectionZipFile,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) numberingContent,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> abstractNumIds,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numIds,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numberingNamespaceMap)
Handle numbering.xml.
Parameters:
`docBuilder` - DocumentBuilder
`baseNumberingDocument` - base document
`sectionZipFile` - zip file
`numberingContent` - numbering content
`abstractNumIds` - list of existing abstractNumId
`numIds` - list of existing numId
`numberingNamespaceMap` - namespaces of numbering
Returns:
base document
getDocumentSubFileInfo
public void getDocumentSubFileInfo([Template](../../Template.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [DefaultHandler](https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html) handler)
Get content of sub file before evaluate
Parameters:
`template` - a template
`name` - entry name
`handler` - file handler
getEntryContent
public void getEntryContent([Template](../../Template.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName)
Get entry from input file and entryName. Then set reader to template.
Parameters:
`template` - OOXML template
`entryName` - entry file name
intenalEvaluate
public void intenalEvaluate([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Throws:
`[TemplateException](../../TemplateException.html)`
translate
public void translate([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html),
[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Process the template in `inProcessBuffer` into valid format.
Overrides:
`[translate](DefaultTemplateEngine.html#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if IO Error occurs while reading template.
translate
public void translate([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer,
 [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) child)
 throws [ParseErrorException](../../ParseErrorException.html),
[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Process the template in `inProcessBuffer` into valid format.
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
`child` - document information to update some value in template
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if IO Error occurs while reading template.
translate
public void translate([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) entryName,
 [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) child)
 throws [ParseErrorException](../../ParseErrorException.html),
[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Process the template in `inProcessBuffer` into valid format.
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
`entryName` - entry name
`child` - document information to update some value in template
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if IO Error occurs while reading template.
createParseErrorWrapper
protected [ParseErrorException](../../ParseErrorException.html) createParseErrorWrapper([ParseErrorException](../../ParseErrorException.html) parseError,
 [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) source)
Create a ParseErrorException from the message.
Parameters:
`parseError` - root cause
`source` - source template
Returns:
instance of ParseErrorException
processVelocityException
protected [TemplateException](../../TemplateException.html) processVelocityException([Template](../../Template.html) template,
 org.apache.velocity.exception.ParseErrorException e)
Call this method to process an Velocity exception and return in new format. Override
 [`DefaultTemplateEngine.processVelocityException(Template, org.apache.velocity.exception.ParseErrorException)`](DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException))
 to return exception with valid ODF line count.
Overrides:
`[processVelocityException](DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - Template
`e` - Velocity exception
Returns:
TemplateException
lineCount
public int lineCount([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)
Count number of line from given content string.
Overrides:
`[lineCount](DefaultTemplateEngine.html#lineCount(java.lang.String))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`content` - the input string
Returns:
number of line
getEntrySet
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getEntrySet()
Return DOCX entry set.
Returns:
DOCX entry set.
getTemplate
public [Template](../../Template.html) getTemplate()
Return template.
Returns:
a DOCX template
handleForPage
protected void handleForPage([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #forpage directive.
Overrides:
`[handleForPage](DefaultTemplateEngine.html#handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleForRow
protected void handleForRow([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #forrow directive.
Overrides:
`[handleForRow](DefaultTemplateEngine.html#handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleGridCol
protected void handleGridCol([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
Add id to w:gridCol tag.
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
handleForColumn
protected void handleForColumn([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #forcol directive.
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleMergeColumns
protected void handleMergeColumns([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle $tableprop.mergeColumns directive
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleMergeRows
protected void handleMergeRows([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle $tableprop.mergeRows directive
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleIncludeSection
protected void handleIncludeSection([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #includeSection directive.
Overrides:
`[handleIncludeSection](DefaultTemplateEngine.html#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleIncludeSection
protected void handleIncludeSection([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer,
 [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) child)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #includeSection directive.
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
`child` - DocumentInfo of child template
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleSectionBegin
protected void handleSectionBegin([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #sectionBegin directive.
Overrides:
`[handleSectionBegin](DefaultTemplateEngine.html#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
createComment
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createComment([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Return a formatted comment from given message. The default comment format return from this method is
 " {0} " where {0} is message;
Overrides:
`[createComment](DefaultTemplateEngine.html#createComment(java.lang.String))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`message` - message to put in document comment
Returns:
comment
postProcess
protected void postProcess([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Perform a post-processing after the template has been evaluated.
Overrides:
`[postProcess](DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - template after evaluated.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`DefaultTemplateEngine.postProcess(com.nomagic.magicreport.Template)`](DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))
destroy
public void destroy()
Description copied from class: `[DefaultTemplateEngine](DefaultTemplateEngine.html#destroy())`
Called by the application or [`TemplateEngineFactory`](../../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
 A subclass of engine should override this method if it has any operation that it wants to perform before it
 is destroyed.
Specified by:
`[destroy](../ITemplateEngine.html#destroy())` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Overrides:
`[destroy](DefaultTemplateEngine.html#destroy())` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
addFont
public int addFont([Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font)
Add font for HTML to DOCX.
Specified by:
`[addFont](../../format/html/StyledDocument.html#addFont(java.awt.Font))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`font` - font
Returns:
font id
addList
public int addList([List](../../format/html/List.html) list)
Add list for HTML to DOCX.
Specified by:
`[addList](../../format/html/StyledDocument.html#addList(com.nomagic.magicreport.format.html.List))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`list` - list
Returns:
list id
addStyle
public int addStyle([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) style)
Add style for HTML to DOCX.
Specified by:
`[addStyle](../../format/html/StyledDocument.html#addStyle(javax.swing.text.Style))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`style` - style
Returns:
style id
addColor
public int addColor([Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)
Add color for HTML to DOCX.
Specified by:
`[addColor](../../format/html/StyledDocument.html#addColor(java.awt.Color))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`color` - color
Returns:
color id
addHyperLink
public void addHyperLink([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) rId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url)
Add rId for hyper link.
Parameters:
`rId` - rId
`url` - URL
addImage
public void addImage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) rId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) imageType)
Add rId for hyper link.
Parameters:
`rId` - rId
`url` - URL
`imageType` - imageType
addRowSpanID
public void addRowSpanID([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 int value)
Add rowspan id and its value to map
Parameters:
`id` - rowspan id
`value` - number of rows to be merged
addObject
public int addObject([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)
Appends object content into the document.
Specified by:
`[addObject](../../format/html/StyledDocument.html#addObject(java.lang.Object))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`object` - adding object
Returns:
index to object
getDocInfo
public [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) getDocInfo()
setDocInfo
public void setDocInfo([DocumentInfo](../ooxml/child/docx/DocumentInfo.html) docInfo)
getMainDocInfo
public [DocumentInfo](../ooxml/child/docx/DocumentInfo.html) getMainDocInfo()
getEvaluatedDocument
public com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument getEvaluatedDocument()
setEvaluatedDocument
public void setEvaluatedDocument(com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument evaluatedDocument)
getEvaluatedDocumentBuffer
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getEvaluatedDocumentBuffer()
isMemoryMode
public boolean isMemoryMode([Template](../../Template.html) template)
Description copied from class: `[AbstractTemplateEngine](../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template))`
Tests if this template should process in memory mode. 

 This method is similar to code: `template.getSize() > properties.getProperty(TemplateConstants.TEMPLATE_PROCESS_SIZE, "0")`
Overrides:
`[isMemoryMode](../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template))` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
Parameters:
`template` - a test Template
Returns:
true if template size is less than TEMPLATE_PROCESS_SIZE
updateSize
public void updateSize(long size)
setCheckSize
public void setCheckSize(boolean isCheckFileSize)
addChart
public void addChart()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class DOCXEngine">Class DOCXEngine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.AbstractTemplateEngine</a>
<div class="inheritance"><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine</a>
<div class="inheritance">com.nomagic.magicreport.engine.velocity.DOCXEngine</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../IExtensionTemplateEngine.html" title="interface in com.nomagic.magicreport.engine">IExtensionTemplateEngine</a></code>, <code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code>, <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code>, <code><a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DOCXEngine</span>
<span class="extends-implements">extends <a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a>
implements <a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></span></div>
<div class="block">The Velocity engine for OpenXML Word Document (DOCX).</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Oct 19, 2009</dd>
</dl>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="DOCXEngine.ContentTypeProcess.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine.ContentTypeProcess</a></code></div>
<div class="col-last even-row-color">
<div class="block">Handle content type</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DOCXEngine.DocumentRelationshipProcess.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine.DocumentRelationshipProcess</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Handle document relationship</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DOCXEngine.NumberingProcess.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine.NumberingProcess</a></code></div>
<div class="col-last even-row-color">
<div class="block">Handle numbering File</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DOCXEngine.NumberingUpdateProcess.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine.NumberingUpdateProcess</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Handle numbering for child document
 This abstractNumId and numId in this file should be updated</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="DOCXEngine.StyleProcess.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine.StyleProcess</a></code></div>
<div class="col-last even-row-color">
<div class="block">Handle style File</div>
</div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="DOCXEngine.StyleUpdateProcess.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine.StyleUpdateProcess</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Handle style for child document
 This id and name in this file may be updated</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine">Fields inherited from class com.nomagic.magicreport.engine.velocity.<a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></h3>
<code><a href="DefaultTemplateEngine.html#velocityContext">velocityContext</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.AbstractTemplateEngine">Fields inherited from class com.nomagic.magicreport.engine.<a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></h3>
<code><a href="../AbstractTemplateEngine.html#context">context</a>, <a href="../AbstractTemplateEngine.html#isAborted">isAborted</a>, <a href="../AbstractTemplateEngine.html#preProcessFile">preProcessFile</a>, <a href="../AbstractTemplateEngine.html#processFile">processFile</a>, <a href="../AbstractTemplateEngine.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.format.html.StyledDocument">Fields inherited from interface com.nomagic.magicreport.format.html.<a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></h3>
<code><a href="../../format/html/StyledDocument.html#CHARACTER">CHARACTER</a>, <a href="../../format/html/StyledDocument.html#COLOR">COLOR</a>, <a href="../../format/html/StyledDocument.html#FONT">FONT</a>, <a href="../../format/html/StyledDocument.html#PARAGRAPH">PARAGRAPH</a>, <a href="../../format/html/StyledDocument.html#TABLE">TABLE</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DOCXEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">A class constructor.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addChart()">addChart</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addColor(java.awt.Color)">addColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add color for HTML to DOCX.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addFont(java.awt.Font)">addFont</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add font for HTML to DOCX.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addHyperLink(java.lang.String,java.lang.String)">addHyperLink</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add rId for hyper link.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addImage(java.lang.String,java.lang.String,java.lang.String)">addImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add rId for hyper link.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addList(com.nomagic.magicreport.format.html.List)">addList</a><wbr/>(<a href="../../format/html/List.html" title="interface in com.nomagic.magicreport.format.html">List</a> list)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add list for HTML to DOCX.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addObject(java.lang.Object)">addObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends object content into the document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addPageSections(java.lang.String)">addPageSections</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRowSpanID(java.lang.String,int)">addRowSpanID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add rowspan id and its value to map</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addStyle(javax.swing.text.Style)">addStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add style for HTML to DOCX.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComment(java.lang.String)">createComment</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a formatted comment from given message.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createParseErrorWrapper(com.nomagic.magicreport.ParseErrorException,java.io.Reader)">createParseErrorWrapper</a><wbr/>(<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> parseError,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> source)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create a ParseErrorException from the message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplate()">createTemplate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object for generating report by this engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplate(java.io.File,java.io.File)">createTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplate(java.io.File,java.io.File,boolean)">createTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output,
 boolean ignoreLocation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplate(java.io.File,java.io.File,boolean,boolean)">createTemplate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output,
 boolean ignoreDocInfo,
 boolean ignoreLocation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called by the application or <a href="../../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#evaluate(com.nomagic.magicreport.Template)">evaluate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbStractId()">getAbStractId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbstractNumbering()">getAbstractNumbering</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBookmarkList()">getBookmarkList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBookmarkListMap()">getBookmarkListMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBookmarkN()">getBookmarkN</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCharsetName()">getCharsetName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocInfo()">getDocInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocProp()">getDocProp</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocPropList()">getDocPropList</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocument()">getDocument</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocumentSubFileInfo(com.nomagic.magicreport.Template,java.lang.String,org.xml.sax.helpers.DefaultHandler)">getDocumentSubFileInfo</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get content of sub file before evaluate</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEntryContent(com.nomagic.magicreport.Template,java.lang.String)">getEntryContent</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get entry from input file and entryName.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEntryMap()">getEntryMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEntryName()">getEntryName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEntryNameSet()">getEntryNameSet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEntrySet()">getEntrySet</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return DOCX entry set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEvaluatedDocument()">getEvaluatedDocument</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEvaluatedDocumentBuffer()">getEvaluatedDocumentBuffer</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHyperLinkMap()">getHyperLinkMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageFormat()">getImageFormat</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImageMap()">getImageMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainDocInfo()">getMainDocInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberingDef()">getNumberingDef</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumId()">getNumId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../OOXMLTemplate.html" title="class in com.nomagic.magicreport">OOXMLTemplate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOoxmlTemplate()">getOoxmlTemplate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getPageSections(int)">getPageSections</a><wbr/>(int index)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyleIds()">getStyleIds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyleNameMap()">getStyleNameMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplate()">getTemplate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleContentType(java.util.Set,java.util.Set,java.lang.StringBuilder,java.util.Map)">handleContentType</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt; contentTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt; sectionContentTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> contentTypeContentBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;&gt; newFilesInZip)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle [Content_Type].xml after evaluate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleForColumn(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleForColumn</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #forcol directive.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleForPage</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #forpage directive.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleForRow</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #forrow directive.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleGridCol(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleGridCol</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add id to w:gridCol tag.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleIncludeSection</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #includeSection directive.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">handleIncludeSection</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer,
 <a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #includeSection directive.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleMergeColumns(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleMergeColumns</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle $tableprop.mergeColumns directive</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleMergeRows(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleMergeRows</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle $tableprop.mergeRows directive</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleNumbering(javax.xml.parsers.DocumentBuilder,org.w3c.dom.Document,java.io.File,java.lang.StringBuilder,java.util.List,java.util.List,java.util.Map)">handleNumbering</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html" title="class or interface in javax.xml.parsers">DocumentBuilder</a> docBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> baseNumberingDocument,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> sectionZipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> numberingContent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; abstractNumIds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numIds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numberingNamespaceMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle numbering.xml.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleRelationship(com.nomagic.magicreport.engine.ooxml.OOXMLStreamWriter,java.io.File,java.util.Map,java.lang.String,java.util.Map,java.lang.StringBuilder)">handleRelationship</a><wbr/>(<a href="../ooxml/OOXMLStreamWriter.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLStreamWriter</a> ooxmlWriter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> sectionZipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>? extends com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt; relationshipMap,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relationshipPrefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;&gt; newFilesInZip,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> relationContentBuilder)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle relationship file after evaluate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleSectionBegin</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #sectionBegin directive.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleSharedFiles()">handleSharedFiles</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle document.xml.rels, [Content_Types].xml, styles.xml, and numbering.xml</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleStyle(javax.xml.parsers.DocumentBuilder,org.w3c.dom.Document,java.io.File,java.lang.StringBuilder,java.util.List,java.util.List,java.util.Map)">handleStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html" title="class or interface in javax.xml.parsers">DocumentBuilder</a> docBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> baseStyleDocument,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> sectionZipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> styleContent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleIds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleLatents,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; namespaceMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle styles.xml after evaluate.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#intenalEvaluate(com.nomagic.magicreport.Template)">intenalEvaluate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isHasNumbering()">isHasNumbering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isInMultipleLineComment()">isInMultipleLineComment</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMemoryMode(com.nomagic.magicreport.Template)">isMemoryMode</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests if this template should process in memory mode.<br/>
 This method is similar to code:</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#lineCount(java.lang.String)">lineCount</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Count number of line from given content string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#postProcess(com.nomagic.magicreport.Template)">postProcess</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Perform a post-processing after the template has been evaluated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)">processVelocityException</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 org.apache.velocity.exception.ParseErrorException e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to process an Velocity exception and return in new format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAbStractId(int)">setAbStractId</a><wbr/>(int abStractId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAbstractNumbering(java.util.Map)">setAbstractNumbering</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]&gt;&gt; abstractNumbering)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBookmarkList(java.util.Set)">setBookmarkList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; bookmarkList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBookmarkListMap(java.util.Map)">setBookmarkListMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark&gt; bookmarkListMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setBookmarkN(int)">setBookmarkN</a><wbr/>(int bookmarkN)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCharsetName(java.lang.String)">setCharsetName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCheckSize(boolean)">setCheckSize</a><wbr/>(boolean isCheckFileSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocInfo(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">setDocInfo</a><wbr/>(<a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> docInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocProp(java.util.List)">setDocProp</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; docProp)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocPropList(java.util.List)">setDocPropList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; docPropList)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocument(org.w3c.dom.Document)">setDocument</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEntryMap(java.util.Map)">setEntryMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; entryMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEntryName(java.lang.String)">setEntryName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEntryNameSet(java.util.Set)">setEntryNameSet</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; entryNameSet)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEvaluatedDocument(com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument)">setEvaluatedDocument</a><wbr/>(com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument evaluatedDocument)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHasNumbering(boolean)">setHasNumbering</a><wbr/>(boolean hasNumbering)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setHyperLinkMap(java.util.Map)">setHyperLinkMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; hyperLinkMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageFormat(java.util.List)">setImageFormat</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; imageFormat)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImageMap(java.util.Map)">setImageMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; imageMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInMultipleLineComment(boolean)">setInMultipleLineComment</a><wbr/>(boolean inMultipleLineComment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberingDef(java.util.Map)">setNumberingDef</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numberingDef)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumId(int)">setNumId</a><wbr/>(int numId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOoxmlTemplate(com.nomagic.magicreport.OOXMLTemplate)">setOoxmlTemplate</a><wbr/>(<a href="../../OOXMLTemplate.html" title="class in com.nomagic.magicreport">OOXMLTemplate</a> ooxmlTemplate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyleIds(java.util.Set)">setStyleIds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleIds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyleNameMap(java.util.Map)">setStyleNameMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleNameMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWriterForEvaluate(com.nomagic.magicreport.Template)">setWriterForEvaluate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)">translate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">translate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer,
 <a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> child)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder,java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">translate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateSize(long)">updateSize</a><wbr/>(long size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateStyleIds(java.lang.String)">updateStyleIds</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> styleId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateStyleNameMap(java.lang.String,java.lang.String)">updateStyleNameMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine">Methods inherited from class com.nomagic.magicreport.engine.velocity.<a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></h3>
<code><a href="DefaultTemplateEngine.html#abort()">abort</a>, <a href="DefaultTemplateEngine.html#checkFileNotFoundException(java.lang.Exception,java.io.File)">checkFileNotFoundException</a>, <a href="DefaultTemplateEngine.html#clearTools()">clearTools</a>, <a href="DefaultTemplateEngine.html#getClassLoader()">getClassLoader</a>, <a href="DefaultTemplateEngine.html#getFormatter()">getFormatter</a>, <a href="DefaultTemplateEngine.html#getResolvedSectionName(java.lang.String)">getResolvedSectionName</a>, <a href="DefaultTemplateEngine.html#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleImport</a>, <a href="DefaultTemplateEngine.html#isNoSpaceException(java.lang.Exception)">isNoSpaceException</a>, <a href="DefaultTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)">preProcess</a>, <a href="DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template)">process</a>, <a href="DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">process</a>, <a href="DefaultTemplateEngine.html#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)">processException</a>, <a href="DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)">processVelocityException</a>, <a href="DefaultTemplateEngine.html#setClassLoader(java.lang.ClassLoader)">setClassLoader</a>, <a href="DefaultTemplateEngine.html#setFormatter(com.nomagic.magicreport.format.IFormatter)">setFormatter</a>, <a href="DefaultTemplateEngine.html#setLatestLocation(java.io.File,java.io.File)">setLatestLocation</a>, <a href="DefaultTemplateEngine.html#setLocation(java.io.File,java.io.File)">setLocation</a>, <a href="DefaultTemplateEngine.html#setProperty(java.lang.String,java.lang.Object)">setProperty</a>, <a href="DefaultTemplateEngine.html#trimTrailSpace(int,java.lang.StringBuilder)">trimTrailSpace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.AbstractTemplateEngine">Methods inherited from class com.nomagic.magicreport.engine.<a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></h3>
<code><a href="../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)">addContext</a>, <a href="../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">addInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#addObserver(java.util.Observer)">addObserver</a>, <a href="../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">addReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">evaluate</a>, <a href="../AbstractTemplateEngine.html#getConcurrentToolException()">getConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#getContext()">getContext</a>, <a href="../AbstractTemplateEngine.html#getCurrentRuntimeInstance()">getCurrentRuntimeInstance</a>, <a href="../AbstractTemplateEngine.html#getInvalidReferenceHandler()">getInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#getProcessSize()">getProcessSize</a>, <a href="../AbstractTemplateEngine.html#getProperties()">getProperties</a>, <a href="../AbstractTemplateEngine.html#getProperty(java.lang.String)">getProperty</a>, <a href="../AbstractTemplateEngine.html#getReferenceInsertionHandler()">getReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../AbstractTemplateEngine.html#observers()">observers</a>, <a href="../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)">setConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance)">setCurrentRuntimeInstance</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>DOCXEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DOCXEngine</span>()</div>
<div class="block">A class constructor.</div>
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
<section class="detail" id="isInMultipleLineComment()">
<h3>isInMultipleLineComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isInMultipleLineComment</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setInMultipleLineComment(boolean)">
<h3>setInMultipleLineComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInMultipleLineComment</span><wbr/><span class="parameters">(boolean inMultipleLineComment)</span></div>
</section>
</li>
<li>
<section class="detail" id="isHasNumbering()">
<h3>isHasNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHasNumbering</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHasNumbering(boolean)">
<h3>setHasNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHasNumbering</span><wbr/><span class="parameters">(boolean hasNumbering)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAbStractId()">
<h3>getAbStractId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getAbStractId</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAbStractId(int)">
<h3>setAbStractId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAbStractId</span><wbr/><span class="parameters">(int abStractId)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumId()">
<h3>getNumId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNumId</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNumId(int)">
<h3>setNumId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumId</span><wbr/><span class="parameters">(int numId)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBookmarkN()">
<h3>getBookmarkN</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getBookmarkN</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setBookmarkN(int)">
<h3>setBookmarkN</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBookmarkN</span><wbr/><span class="parameters">(int bookmarkN)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDocument()">
<h3>getDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a></span> <span class="element-name">getDocument</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDocument(org.w3c.dom.Document)">
<h3>setDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocument</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> document)</span></div>
</section>
</li>
<li>
<section class="detail" id="getImageFormat()">
<h3>getImageFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getImageFormat</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setImageFormat(java.util.List)">
<h3>setImageFormat</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageFormat</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; imageFormat)</span></div>
</section>
</li>
<li>
<section class="detail" id="getHyperLinkMap()">
<h3>getHyperLinkMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getHyperLinkMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setHyperLinkMap(java.util.Map)">
<h3>setHyperLinkMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setHyperLinkMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; hyperLinkMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="getImageMap()">
<h3>getImageMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getImageMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setImageMap(java.util.Map)">
<h3>setImageMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImageMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; imageMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEntryNameSet()">
<h3>getEntryNameSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getEntryNameSet</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setEntryNameSet(java.util.Set)">
<h3>setEntryNameSet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEntryNameSet</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; entryNameSet)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEntryMap()">
<h3>getEntryMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt;</span> <span class="element-name">getEntryMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setEntryMap(java.util.Map)">
<h3>setEntryMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEntryMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; entryMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBookmarkList()">
<h3>getBookmarkList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getBookmarkList</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setBookmarkList(java.util.Set)">
<h3>setBookmarkList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBookmarkList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; bookmarkList)</span></div>
</section>
</li>
<li>
<section class="detail" id="getBookmarkListMap()">
<h3>getBookmarkListMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark&gt;</span> <span class="element-name">getBookmarkListMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setBookmarkListMap(java.util.Map)">
<h3>setBookmarkListMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setBookmarkListMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.velocity.DOCXEngine.Bookmark&gt; bookmarkListMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="getNumberingDef()">
<h3>getNumberingDef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNumberingDef</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setNumberingDef(java.util.Map)">
<h3>setNumberingDef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberingDef</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numberingDef)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAbstractNumbering()">
<h3>getAbstractNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]&gt;&gt;</span> <span class="element-name">getAbstractNumbering</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAbstractNumbering(java.util.Map)">
<h3>setAbstractNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAbstractNumbering</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]&gt;&gt; abstractNumbering)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDocProp()">
<h3>getDocProp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getDocProp</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDocProp(java.util.List)">
<h3>setDocProp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocProp</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; docProp)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEntryName()">
<h3>getEntryName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getEntryName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setEntryName(java.lang.String)">
<h3>setEntryName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEntryName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCharsetName()">
<h3>getCharsetName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCharsetName</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCharsetName(java.lang.String)">
<h3>setCharsetName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCharsetName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> charsetName)</span></div>
</section>
</li>
<li>
<section class="detail" id="getOoxmlTemplate()">
<h3>getOoxmlTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../OOXMLTemplate.html" title="class in com.nomagic.magicreport">OOXMLTemplate</a></span> <span class="element-name">getOoxmlTemplate</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setOoxmlTemplate(com.nomagic.magicreport.OOXMLTemplate)">
<h3>setOoxmlTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOoxmlTemplate</span><wbr/><span class="parameters">(<a href="../../OOXMLTemplate.html" title="class in com.nomagic.magicreport">OOXMLTemplate</a> ooxmlTemplate)</span></div>
</section>
</li>
<li>
<section class="detail" id="getDocPropList()">
<h3>getDocPropList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getDocPropList</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDocPropList(java.util.List)">
<h3>setDocPropList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocPropList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; docPropList)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStyleNameMap()">
<h3>getStyleNameMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStyleNameMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setStyleNameMap(java.util.Map)">
<h3>setStyleNameMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyleNameMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleNameMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateStyleNameMap(java.lang.String,java.lang.String)">
<h3>updateStyleNameMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateStyleNameMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
</section>
</li>
<li>
<section class="detail" id="getStyleIds()">
<h3>getStyleIds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getStyleIds</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setStyleIds(java.util.Set)">
<h3>setStyleIds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyleIds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleIds)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateStyleIds(java.lang.String)">
<h3>updateStyleIds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateStyleIds</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> styleId)</span></div>
</section>
</li>
<li>
<section class="detail" id="getPageSections(int)">
<h3>getPageSections</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getPageSections</span><wbr/><span class="parameters">(int index)</span></div>
</section>
</li>
<li>
<section class="detail" id="addPageSections(java.lang.String)">
<h3>addPageSections</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">addPageSections</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</span></div>
</section>
</li>
<li>
<section class="detail" id="createTemplate()">
<h3>createTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">createTemplate</span>()</div>
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object for generating report by this engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#createTemplate()">createTemplate</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#createTemplate()">createTemplate</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>an instance of <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File)"><code>DefaultTemplateEngine.createTemplate(File, File)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplate(java.io.File,java.io.File)">
<h3>createTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">createTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#createTemplate(java.io.File,java.io.File)">createTemplate</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File)">createTemplate</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>input</code> - template file.</dd>
<dd><code>output</code> - output file.</dd>
<dt>Returns:</dt>
<dd>an instance of <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html" title="class or interface in java.io">FileNotFoundException</a></code> - if the file does not exist, is a directory rather than a regular file,
            or for some other reason cannot be opened.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplate(java.io.File,java.io.File,boolean)">
<h3>createTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">createTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output,
 boolean ignoreLocation)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#createTemplate(java.io.File,java.io.File,boolean)">createTemplate</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>input</code> - template file.</dd>
<dd><code>output</code> - output file.</dd>
<dd><code>ignoreLocation</code> - true to ignore location property for child document</dd>
<dt>Returns:</dt>
<dd>an instance of <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html" title="class or interface in java.io">FileNotFoundException</a></code> - if the file does not exist, is a directory rather than a regular file,
            or for some other reason cannot be opened.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTemplate(java.io.File,java.io.File,boolean,boolean)">
<h3>createTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">createTemplate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output,
 boolean ignoreDocInfo,
 boolean ignoreLocation)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Creates a new <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - template file.</dd>
<dd><code>output</code> - output file.</dd>
<dd><code>ignoreDocInfo</code> - true to ignore create document info. this parameter should be true for creating template of child document</dd>
<dd><code>ignoreLocation</code> - true to ignore location property for child document</dd>
<dt>Returns:</dt>
<dd>an instance of <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html" title="class or interface in java.io">FileNotFoundException</a></code> - if the file does not exist, is a directory rather than a regular file,
            or for some other reason cannot be opened.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="evaluate(com.nomagic.magicreport.Template)">
<h3>evaluate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
              throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template)">evaluate</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template)">evaluate</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template being evaluated</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template)"><code>ITemplateEngine.evaluate(Template)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWriterForEvaluate(com.nomagic.magicreport.Template)">
<h3>setWriterForEvaluate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></span> <span class="element-name">setWriterForEvaluate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#setWriterForEvaluate(com.nomagic.magicreport.Template)">setWriterForEvaluate</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleSharedFiles()">
<h3>handleSharedFiles</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleSharedFiles</span>()</div>
<div class="block">Handle document.xml.rels, [Content_Types].xml, styles.xml, and numbering.xml</div>
</section>
</li>
<li>
<section class="detail" id="handleRelationship(com.nomagic.magicreport.engine.ooxml.OOXMLStreamWriter,java.io.File,java.util.Map,java.lang.String,java.util.Map,java.lang.StringBuilder)">
<h3>handleRelationship</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleRelationship</span><wbr/><span class="parameters">(<a href="../ooxml/OOXMLStreamWriter.html" title="class in com.nomagic.magicreport.engine.ooxml">OOXMLStreamWriter</a> ooxmlWriter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> sectionZipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>? extends com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt; relationshipMap,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> relationshipPrefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;&gt; newFilesInZip,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> relationContentBuilder)</span></div>
<div class="block">Handle relationship file after evaluate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ooxmlWriter</code> - writer</dd>
<dd><code>sectionZipFile</code> - zip file of child template</dd>
<dd><code>relationshipMap</code> - map of relationship and id</dd>
<dd><code>relationshipPrefix</code> - prefix path for relationship</dd>
<dd><code>newFilesInZip</code> - map of new files that are created after generated</dd>
<dd><code>relationContentBuilder</code> - stringbuilder to keep relationship content</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleContentType(java.util.Set,java.util.Set,java.lang.StringBuilder,java.util.Map)">
<h3>handleContentType</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleContentType</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt; contentTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt; sectionContentTypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> contentTypeContentBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;&gt; newFilesInZip)</span></div>
<div class="block">Handle [Content_Type].xml after evaluate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contentTypes</code> - content type in main document</dd>
<dd><code>sectionContentTypes</code> - content type in child document</dd>
<dd><code>contentTypeContentBuilder</code> - Stringbuilder to create new content of [Content_Type].xml</dd>
<dd><code>newFilesInZip</code> - map of partname and new target path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleStyle(javax.xml.parsers.DocumentBuilder,org.w3c.dom.Document,java.io.File,java.lang.StringBuilder,java.util.List,java.util.List,java.util.Map)">
<h3>handleStyle</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a></span> <span class="element-name">handleStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html" title="class or interface in javax.xml.parsers">DocumentBuilder</a> docBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> baseStyleDocument,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> sectionZipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> styleContent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleIds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; styleLatents,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; namespaceMap)</span></div>
<div class="block">Handle styles.xml after evaluate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>docBuilder</code> - DocumentBuilder</dd>
<dd><code>baseStyleDocument</code> - base document</dd>
<dd><code>sectionZipFile</code> - zip file to be added</dd>
<dd><code>styleContent</code> - all content of style</dd>
<dd><code>styleIds</code> - existing style</dd>
<dd><code>styleLatents</code> - existing latents</dd>
<dd><code>namespaceMap</code> - namespaces of style</dd>
<dt>Returns:</dt>
<dd>base document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleNumbering(javax.xml.parsers.DocumentBuilder,org.w3c.dom.Document,java.io.File,java.lang.StringBuilder,java.util.List,java.util.List,java.util.Map)">
<h3>handleNumbering</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a></span> <span class="element-name">handleNumbering</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/javax/xml/parsers/DocumentBuilder.html" title="class or interface in javax.xml.parsers">DocumentBuilder</a> docBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/w3c/dom/Document.html" title="class or interface in org.w3c.dom">Document</a> baseNumberingDocument,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> sectionZipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> numberingContent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; abstractNumIds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numIds,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numberingNamespaceMap)</span></div>
<div class="block">Handle numbering.xml.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>docBuilder</code> - DocumentBuilder</dd>
<dd><code>baseNumberingDocument</code> - base document</dd>
<dd><code>sectionZipFile</code> - zip file</dd>
<dd><code>numberingContent</code> - numbering content</dd>
<dd><code>abstractNumIds</code> - list of existing abstractNumId</dd>
<dd><code>numIds</code> - list of existing numId</dd>
<dd><code>numberingNamespaceMap</code> - namespaces of numbering</dd>
<dt>Returns:</dt>
<dd>base document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentSubFileInfo(com.nomagic.magicreport.Template,java.lang.String,org.xml.sax.helpers.DefaultHandler)">
<h3>getDocumentSubFileInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getDocumentSubFileInfo</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.xml/org/xml/sax/helpers/DefaultHandler.html" title="class or interface in org.xml.sax.helpers">DefaultHandler</a> handler)</span></div>
<div class="block">Get content of sub file before evaluate</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - a template</dd>
<dd><code>name</code> - entry name</dd>
<dd><code>handler</code> - file handler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEntryContent(com.nomagic.magicreport.Template,java.lang.String)">
<h3>getEntryContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">getEntryContent</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName)</span></div>
<div class="block">Get entry from input file and entryName. Then set reader to template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - OOXML template</dd>
<dd><code>entryName</code> - entry file name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intenalEvaluate(com.nomagic.magicreport.Template)">
<h3>intenalEvaluate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">intenalEvaluate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                     throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>translate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">translate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
               throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)">translate</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if IO Error occurs while reading template.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="translate(com.nomagic.magicreport.Template,java.lang.StringBuilder,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">
<h3>translate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">translate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer,
 <a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> child)</span>
               throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dd><code>child</code> - document information to update some value in template</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if IO Error occurs while reading template.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="translate(com.nomagic.magicreport.Template,java.lang.StringBuilder,java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">
<h3>translate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">translate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> entryName,
 <a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> child)</span>
               throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dd><code>entryName</code> - entry name</dd>
<dd><code>child</code> - document information to update some value in template</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if IO Error occurs while reading template.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createParseErrorWrapper(com.nomagic.magicreport.ParseErrorException,java.io.Reader)">
<h3>createParseErrorWrapper</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span> <span class="element-name">createParseErrorWrapper</span><wbr/><span class="parameters">(<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> parseError,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> source)</span></div>
<div class="block">Create a ParseErrorException from the message.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parseError</code> - root cause</dd>
<dd><code>source</code> - source template</dd>
<dt>Returns:</dt>
<dd>instance of ParseErrorException</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)">
<h3>processVelocityException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span> <span class="element-name">processVelocityException</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 org.apache.velocity.exception.ParseErrorException e)</span></div>
<div class="block">Call this method to process an Velocity exception and return in new format. Override
 <a href="DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)"><code>DefaultTemplateEngine.processVelocityException(Template, org.apache.velocity.exception.ParseErrorException)</code></a>
 to return exception with valid ODF line count.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)">processVelocityException</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template</dd>
<dd><code>e</code> - Velocity exception</dd>
<dt>Returns:</dt>
<dd>TemplateException</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lineCount(java.lang.String)">
<h3>lineCount</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">lineCount</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</span></div>
<div class="block">Count number of line from given content string.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#lineCount(java.lang.String)">lineCount</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>content</code> - the input string</dd>
<dt>Returns:</dt>
<dd>number of line</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEntrySet()">
<h3>getEntrySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getEntrySet</span>()</div>
<div class="block">Return DOCX entry set.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>DOCX entry set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplate()">
<h3>getTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">getTemplate</span>()</div>
<div class="block">Return template.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a DOCX template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleForPage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleForPage</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                      throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #forpage directive.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleForPage</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleForRow</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleForRow</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                     throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #forrow directive.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleForRow</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleGridCol(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleGridCol</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleGridCol</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span></div>
<div class="block">Add id to w:gridCol tag.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleForColumn(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleForColumn</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleForColumn</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #forcol directive.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleMergeColumns(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleMergeColumns</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleMergeColumns</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                           throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle $tableprop.mergeColumns directive</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleMergeRows(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleMergeRows</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleMergeRows</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle $tableprop.mergeRows directive</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleIncludeSection</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleIncludeSection</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                             throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #includeSection directive.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleIncludeSection</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">
<h3>handleIncludeSection</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleIncludeSection</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer,
 <a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> child)</span>
                             throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #includeSection directive.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dd><code>child</code> - DocumentInfo of child template</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleSectionBegin</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleSectionBegin</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                           throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #sectionBegin directive.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleSectionBegin</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComment(java.lang.String)">
<h3>createComment</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createComment</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Return a formatted comment from given message. The default comment format return from this method is
 "<!-- {0} -->" where {0} is message;</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#createComment(java.lang.String)">createComment</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>message</code> - message to put in document comment</dd>
<dt>Returns:</dt>
<dd>comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postProcess(com.nomagic.magicreport.Template)">
<h3>postProcess</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">postProcess</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                    throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Perform a post-processing after the template has been evaluated.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template)">postProcess</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - template after evaluated.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being parsed.</dd>
<dd><code><a href="../../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template)"><code>DefaultTemplateEngine.postProcess(com.nomagic.magicreport.Template)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="DefaultTemplateEngine.html#destroy()">DefaultTemplateEngine</a></code></span></div>
<div class="block">Called by the application or <a href="../../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.
 <p>
 A subclass of engine should override this method if it has any operation that it wants to perform before it
 is destroyed.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#destroy()">destroy</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#destroy()">destroy</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addFont(java.awt.Font)">
<h3>addFont</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">addFont</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</span></div>
<div class="block">Add font for HTML to DOCX.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../format/html/StyledDocument.html#addFont(java.awt.Font)">addFont</a></code> in interface <code><a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></dd>
<dt>Parameters:</dt>
<dd><code>font</code> - font</dd>
<dt>Returns:</dt>
<dd>font id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addList(com.nomagic.magicreport.format.html.List)">
<h3>addList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">addList</span><wbr/><span class="parameters">(<a href="../../format/html/List.html" title="interface in com.nomagic.magicreport.format.html">List</a> list)</span></div>
<div class="block">Add list for HTML to DOCX.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../format/html/StyledDocument.html#addList(com.nomagic.magicreport.format.html.List)">addList</a></code> in interface <code><a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></dd>
<dt>Parameters:</dt>
<dd><code>list</code> - list</dd>
<dt>Returns:</dt>
<dd>list id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addStyle(javax.swing.text.Style)">
<h3>addStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">addStyle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> style)</span></div>
<div class="block">Add style for HTML to DOCX.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../format/html/StyledDocument.html#addStyle(javax.swing.text.Style)">addStyle</a></code> in interface <code><a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></dd>
<dt>Parameters:</dt>
<dd><code>style</code> - style</dd>
<dt>Returns:</dt>
<dd>style id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addColor(java.awt.Color)">
<h3>addColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">addColor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</span></div>
<div class="block">Add color for HTML to DOCX.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../format/html/StyledDocument.html#addColor(java.awt.Color)">addColor</a></code> in interface <code><a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></dd>
<dt>Parameters:</dt>
<dd><code>color</code> - color</dd>
<dt>Returns:</dt>
<dd>color id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addHyperLink(java.lang.String,java.lang.String)">
<h3>addHyperLink</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addHyperLink</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url)</span></div>
<div class="block">Add rId for hyper link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rId</code> - rId</dd>
<dd><code>url</code> - URL</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addImage(java.lang.String,java.lang.String,java.lang.String)">
<h3>addImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> rId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> imageType)</span></div>
<div class="block">Add rId for hyper link.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rId</code> - rId</dd>
<dd><code>url</code> - URL</dd>
<dd><code>imageType</code> - imageType</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addRowSpanID(java.lang.String,int)">
<h3>addRowSpanID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addRowSpanID</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int value)</span></div>
<div class="block">Add rowspan id and its value to map</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - rowspan id</dd>
<dd><code>value</code> - number of rows to be merged</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addObject(java.lang.Object)">
<h3>addObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">addObject</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</span></div>
<div class="block">Appends object content into the document.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../format/html/StyledDocument.html#addObject(java.lang.Object)">addObject</a></code> in interface <code><a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></code></dd>
<dt>Parameters:</dt>
<dd><code>object</code> - adding object</dd>
<dt>Returns:</dt>
<dd>index to object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocInfo()">
<h3>getDocInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a></span> <span class="element-name">getDocInfo</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDocInfo(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">
<h3>setDocInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocInfo</span><wbr/><span class="parameters">(<a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> docInfo)</span></div>
</section>
</li>
<li>
<section class="detail" id="getMainDocInfo()">
<h3>getMainDocInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ooxml/child/docx/DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a></span> <span class="element-name">getMainDocInfo</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getEvaluatedDocument()">
<h3>getEvaluatedDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument</span> <span class="element-name">getEvaluatedDocument</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setEvaluatedDocument(com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument)">
<h3>setEvaluatedDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEvaluatedDocument</span><wbr/><span class="parameters">(com.nomagic.magicreport.engine.ooxml.child.docx.IEvaluatedDocument evaluatedDocument)</span></div>
</section>
</li>
<li>
<section class="detail" id="getEvaluatedDocumentBuffer()">
<h3>getEvaluatedDocumentBuffer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getEvaluatedDocumentBuffer</span>()</div>
</section>
</li>
<li>
<section class="detail" id="isMemoryMode(com.nomagic.magicreport.Template)">
<h3>isMemoryMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMemoryMode</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from class: <code><a href="../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)">AbstractTemplateEngine</a></code></span></div>
<div class="block">Tests if this template should process in memory mode.<br/>
 This method is similar to code: <pre>
 <code>
 template.getSize() &gt; properties.getProperty(TemplateConstants.TEMPLATE_PROCESS_SIZE, "0")
 </code>
 </pre></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)">isMemoryMode</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - a test Template</dd>
<dt>Returns:</dt>
<dd>true if template size is less than TEMPLATE_PROCESS_SIZE</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateSize(long)">
<h3>updateSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateSize</span><wbr/><span class="parameters">(long size)</span></div>
</section>
</li>
<li>
<section class="detail" id="setCheckSize(boolean)">
<h3>setCheckSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCheckSize</span><wbr/><span class="parameters">(boolean isCheckFileSize)</span></div>
</section>
</li>
<li>
<section class="detail" id="addChart()">
<h3>addChart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addChart</span>()</div>
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
