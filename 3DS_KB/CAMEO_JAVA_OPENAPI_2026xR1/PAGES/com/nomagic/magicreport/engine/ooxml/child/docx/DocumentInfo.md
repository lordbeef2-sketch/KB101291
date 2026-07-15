# JAVA OPENAPI: DocumentInfo (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/ooxml/child/docx/DocumentInfo.html
- source_path: `com/nomagic/magicreport/engine/ooxml/child/docx/DocumentInfo.html`
- source_sha256: `22e00bc49a47399466f0a43a9d5d8c79cc7f05d30eef6d9f0ef96217e0f98bd0`
- captured_utc: `2026-07-14T16:46:12.483970+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.ooxml.child.docx](package-summary.html)

## Class DocumentInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo

@OpenApiAllpublic classDocumentInfo
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Handle document information. 

 The DOCX template contains files in zip. 

 For example: 

 - [Content_Type].xml 

 - word/document.xml 

 - word/_rels/document.xml.rels 

 - word/styles.xml 

 - etc.
 
 When it include content from another template, the related file should be included.

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[reservedContentType](#reservedContentType)`
List of ContentType attribute value in [Content_Type].xml that should be at most one can have the value in the file
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[reservedRelationshipType](#reservedRelationshipType)`
List of Type attribute value in word/_rels/document.xml.rels that should be at most one in the file
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DocumentInfo](#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [DocumentInfo](DocumentInfo.html) mainDocInfo,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filePath)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[addContentTypes](#addContentTypes(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType))(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType contentTypes)`
Add a DocumentContentType object to set of DocumentContentType.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getAbstractNumberingMap](#getAbstractNumberingMap())()`
Get map of old id and new id to handle w:abstractNumId.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[DocumentInfo](DocumentInfo.html)>`
`[getChildDocumentInfoMap](#getChildDocumentInfoMap())()`
Get map of child id and child DocumentInfo.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getChildPathAndIDMap](#getChildPathAndIDMap())()`
Get map of child path and child id.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getChildStyleIdMap](#getChildStyleIdMap())()`

`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getContentTypeContent](#getContentTypeContent())()`
Get content of [Content_Type].xml
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getContentTypeNameSpaceMap](#getContentTypeNameSpaceMap())()`

`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType>`
`[getContentTypes](#getContentTypes())()`
Get set of DocumentContentType.
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getDocumentBuffer](#getDocumentBuffer())()`
Get documentation content.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getDocumentNameSpaceMap](#getDocumentNameSpaceMap())()`

`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship>`
`[getDynamicRelationshipMap](#getDynamicRelationshipMap())()`
Get map of dynamic relationship. 

 {dynamic relationship id, DocumentRelationship}
`[File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getFile](#getFile())()`
Get document file
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getFilePath](#getFilePath())()`
Get path of document
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getId](#getId())()`
Get document id
`[DocumentInfo](DocumentInfo.html)`
`[getMainDocInfo](#getMainDocInfo())()`
Get main document
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getNumberingContent](#getNumberingContent())()`
Get content of word/numbering.xml
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getNumberingMap](#getNumberingMap())()`
Get map of old id and new id to handle w:numId.
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getRelationshipContent](#getRelationshipContent())()`
Get content of word/_rels/document.xml.rels.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship>`
`[getRelationshipMap](#getRelationshipMap())()`
Get map of relationship. 

 {relationship id, DocumentRelationship}
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection>`
`[getSectionInfoMap](#getSectionInfoMap())()`
Get map of section id and DocumentSection.
`[Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship>`
`[getStaticRelationshipMap](#getStaticRelationshipMap())()`
Get map of static relationship. 

 {static relationship id, DocumentRelationship}
`[StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html)`
`[getStyleContent](#getStyleContent())()`
Get content of word/styles.xml
`boolean`
`[isUpdateChildStyleAndNumbering](#isUpdateChildStyleAndNumbering())()`
Check if child style has been updated or not.
`void`
`[setAbstractNumberingMap](#setAbstractNumberingMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> abstractNumberingMap)`
Set map of old id and new id from w:abstractNumId in numbering.xml.
`void`
`[setChildDocumentInfoMap](#setChildDocumentInfoMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[DocumentInfo](DocumentInfo.html)> childDocumentInfoMap)`
Set map of child id and child DocumentInfo.
`void`
`[setChildPathAndIDMap](#setChildPathAndIDMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> childPathAndIDMap)`
Set map of child path and child id.
`void`
`[setChildStyleIdMap](#setChildStyleIdMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> childStyleIdMap)`

`void`
`[setContentTypeContent](#setContentTypeContent(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) contentTypeContent)`
Set content of [Content_Type].xml
`void`
`[setContentTypeNameSpaceMap](#setContentTypeNameSpaceMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> contentTypeNameSpaceMap)`

`void`
`[setContentTypes](#setContentTypes(java.util.Set))([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType> contentTypes)`
Set set of DocumentContentType.
`void`
`[setDocumentBuffer](#setDocumentBuffer(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) documentBuffer)`
Set documentation content.
`void`
`[setDocumentNameSpaceMap](#setDocumentNameSpaceMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> documentNameSpaceMap)`

`void`
`[setDynamicRelationshipMap](#setDynamicRelationshipMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship> dynamicRelationshipMap)`
Set map of dynamic relationship.
`void`
`[setFilePath](#setFilePath(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filePath)`
Set path of document
`void`
`[setId](#setId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Set document id
`void`
`[setMainDocInfo](#setMainDocInfo(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo))([DocumentInfo](DocumentInfo.html) mainDocInfo)`
set main document
`void`
`[setNumberingContent](#setNumberingContent(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) numberingContent)`
Set content of word/numbering.xml
`void`
`[setNumberingMap](#setNumberingMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numberingMap)`
Set map of old id and new id from w:numId in numbering.xml.
`void`
`[setRelationshipContent](#setRelationshipContent(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) relationshipContent)`
Set content of word/_rels/document.xml.rels.
`void`
`[setRelationshipMap](#setRelationshipMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> relationshipMap)`
Set map of relationship.
`void`
`[setSectionInfoMap](#setSectionInfoMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection> sectionInfoMap)`
Set map of section id and DocumentSection.
`void`
`[setStaticRelationshipMap](#setStaticRelationshipMap(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> staticRelationshipMap)`
Set map of static relationship.
`void`
`[setStyleContent](#setStyleContent(java.lang.StringBuilder))([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) styleContent)`
Set content of word/styles.xml
`void`
`[setUpdateChildStyleAndNumbering](#setUpdateChildStyleAndNumbering(boolean))(boolean updateChildStyleAndNumbering)`

`void`
`[upateSectionChildMap](#upateSectionChildMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) childid,
 [DocumentInfo](DocumentInfo.html) childDocumentInfo)`
Update map of child id and child DocumentInfo. 

 When the engine found child template, child DocumentInfo will be created. 

 The child id and child DocumentInfo will be added to this map of Main DocumentInfo. 

 
 
 For example: 

 #includeSection("child.docx", "A") 

 child path = "child.docx" 

 child id = "sectionChild1" 

 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo. 

 The child DocumentInfo of "child.docx" template will be created. 

 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo.
`void`
`[updateAbstractNumberingMap](#updateAbstractNumberingMap(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) oldId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newId)`
Add or update old id and new id from w:abstractNumId
`void`
`[updateChildPathAndIDMap](#updateChildPathAndIDMap(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) childPath,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) childId)`
Update map of child path and child id.
`void`
`[updateChildStyleIdMap](#updateChildStyleIdMap(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) oldStyleId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newStyleId)`

`void`
`[updateContentTypeNameSpaceMap](#updateContentTypeNameSpaceMap(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[updateDocumentNameSpaceMap](#updateDocumentNameSpaceMap(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)`

`void`
`[updateDynamicRelationshipMap](#updateDynamicRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship documentRelationship)`
Update map of dynamic relationship.
`void`
`[updateNumberingMap](#updateNumberingMap(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) oldId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newId)`
Add or update old id and new id from w:numId.
`void`
`[updateRelationshipMap](#updateRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship relationship)`
Update map of relationship.
`void`
`[updateSectionInfoMap](#updateSectionInfoMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sectionName,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection documentSection)`
Update map of section id and DocumentSection. 

 When the engine found section of child document, DocumentSection will be created. 

 The sectionName and DocumentSection will be added to this map of child DocumentInfo. 

 
 
 For example: 

 #includeSection("child.docx", "A") 

 child path = "child.docx" 

 child id = "sectionChild1" 

 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo. 

 The child DocumentInfo of "child.docx" template will be created. 

 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo. 

 The DocumentSection of section A will be created. 

 The pair of {"A", aDocumentSection} will be added to sectionInfoMap of childDocumentInfo.
`void`
`[updateStaticRelationshipMap](#updateStaticRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship documentRelationship)`
Update map of static relationship.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
reservedRelationshipType
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> reservedRelationshipType
List of Type attribute value in word/_rels/document.xml.rels that should be at most one in the file
reservedContentType
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> reservedContentType
List of ContentType attribute value in [Content_Type].xml that should be at most one can have the value in the file
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DocumentInfo
public DocumentInfo([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 [DocumentInfo](DocumentInfo.html) mainDocInfo,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filePath)
Constructor
Parameters:
`id` - document id
`mainDocInfo` - main document info
`filePath` - file path of document
 ============ METHOD DETAIL ========== 
Method Details
getId
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getId()
Get document id
Returns:
document id
setId
public void setId([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Set document id
Parameters:
`id` - document id
getFile
public [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getFile()
Get document file
Returns:
document file
getFilePath
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getFilePath()
Get path of document
Returns:
path of document
setFilePath
public void setFilePath([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filePath)
Set path of document
Parameters:
`filePath` - path of document
getMainDocInfo
public [DocumentInfo](DocumentInfo.html) getMainDocInfo()
Get main document
Returns:
main document
setMainDocInfo
public void setMainDocInfo([DocumentInfo](DocumentInfo.html) mainDocInfo)
set main document
Parameters:
`mainDocInfo` - document
getDocumentBuffer
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getDocumentBuffer()
Get documentation content.
Returns:
documentation content
setDocumentBuffer
public void setDocumentBuffer([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) documentBuffer)
Set documentation content.
Parameters:
`documentBuffer` - documentation content
getDocumentNameSpaceMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getDocumentNameSpaceMap()
setDocumentNameSpaceMap
public void setDocumentNameSpaceMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> documentNameSpaceMap)
updateDocumentNameSpaceMap
public void updateDocumentNameSpaceMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getContentTypes
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType> getContentTypes()
Get set of DocumentContentType.
 DocumentContentType contains key and value of each attribute in [Content_Type].xml
Returns:
list of content type objects
setContentTypes
public void setContentTypes([Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType> contentTypes)
Set set of DocumentContentType.
Parameters:
`contentTypes` - set of DocumentContentType
addContentTypes
public void addContentTypes(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType contentTypes)
Add a DocumentContentType object to set of DocumentContentType.
Parameters:
`contentTypes` - content type object
getContentTypeNameSpaceMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getContentTypeNameSpaceMap()
setContentTypeNameSpaceMap
public void setContentTypeNameSpaceMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> contentTypeNameSpaceMap)
updateContentTypeNameSpaceMap
public void updateContentTypeNameSpaceMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) value)
getRelationshipMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> getRelationshipMap()
Get map of relationship. 

 {relationship id, DocumentRelationship}
Returns:
map of relationship
setRelationshipMap
public void setRelationshipMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> relationshipMap)
Set map of relationship.
Parameters:
`relationshipMap` - map of relationship
updateRelationshipMap
public void updateRelationshipMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship relationship)
Update map of relationship.
Parameters:
`id` - relationship id
`relationship` - DocumentRelationship object
getStaticRelationshipMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> getStaticRelationshipMap()
Get map of static relationship. 

 {static relationship id, DocumentRelationship}
Returns:
map of static relationship id and related DocumentRelationship object
setStaticRelationshipMap
public void setStaticRelationshipMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship> staticRelationshipMap)
Set map of static relationship.
Parameters:
`staticRelationshipMap` - map of static relationship
updateStaticRelationshipMap
public void updateStaticRelationshipMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship documentRelationship)
Update map of static relationship.
Parameters:
`id` - static relationship id
`documentRelationship` - DocumentRelationship object
getDynamicRelationshipMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship> getDynamicRelationshipMap()
Get map of dynamic relationship. 

 {dynamic relationship id, DocumentRelationship}
Returns:
map of dynamic relationship
setDynamicRelationshipMap
public void setDynamicRelationshipMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship> dynamicRelationshipMap)
Set map of dynamic relationship.
Parameters:
`dynamicRelationshipMap` - map of dynamic relationship
updateDynamicRelationshipMap
public void updateDynamicRelationshipMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship documentRelationship)
Update map of dynamic relationship.
Parameters:
`id` - dynamic relationship id
`documentRelationship` - DocumentRelationship object
getChildPathAndIDMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getChildPathAndIDMap()
Get map of child path and child id.
Returns:
map of child path and child id
setChildPathAndIDMap
public void setChildPathAndIDMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> childPathAndIDMap)
Set map of child path and child id.
Parameters:
`childPathAndIDMap` - map of child path and child id
updateChildPathAndIDMap
public void updateChildPathAndIDMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) childPath,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) childId)
Update map of child path and child id.
 

 When the engine found child template, child id will be created. 

 The child template file path and child id will be added to this map. 

 
 
 For example: 

 #includeSection("child.docx", "A") 

 child path = "child.docx" 

 child id = "sectionChild1" 

 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo.
Parameters:
`childPath` - child path
`childId` - child id
getChildDocumentInfoMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[DocumentInfo](DocumentInfo.html)> getChildDocumentInfoMap()
Get map of child id and child DocumentInfo.
Returns:
map of child id and DocumentInfo of child
setChildDocumentInfoMap
public void setChildDocumentInfoMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[DocumentInfo](DocumentInfo.html)> childDocumentInfoMap)
Set map of child id and child DocumentInfo.
Parameters:
`childDocumentInfoMap` - map of child id and DocumentInfo of child
upateSectionChildMap
public void upateSectionChildMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) childid,
 [DocumentInfo](DocumentInfo.html) childDocumentInfo)
Update map of child id and child DocumentInfo. 

 When the engine found child template, child DocumentInfo will be created. 

 The child id and child DocumentInfo will be added to this map of Main DocumentInfo. 

 
 
 For example: 

 #includeSection("child.docx", "A") 

 child path = "child.docx" 

 child id = "sectionChild1" 

 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo. 

 The child DocumentInfo of "child.docx" template will be created. 

 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo.
Parameters:
`childid` - child template id
`childDocumentInfo` - child DocumentInfo
getSectionInfoMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection> getSectionInfoMap()
Get map of section id and DocumentSection.
Returns:
map of section id and DocumentSection.
setSectionInfoMap
public void setSectionInfoMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection> sectionInfoMap)
Set map of section id and DocumentSection.
Parameters:
`sectionInfoMap` - map of section id and DocumentSection.
updateSectionInfoMap
public void updateSectionInfoMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sectionName,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection documentSection)
Update map of section id and DocumentSection. 

 When the engine found section of child document, DocumentSection will be created. 

 The sectionName and DocumentSection will be added to this map of child DocumentInfo. 

 
 
 For example: 

 #includeSection("child.docx", "A") 

 child path = "child.docx" 

 child id = "sectionChild1" 

 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo. 

 The child DocumentInfo of "child.docx" template will be created. 

 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo. 

 The DocumentSection of section A will be created. 

 The pair of {"A", aDocumentSection} will be added to sectionInfoMap of childDocumentInfo.
Parameters:
`sectionName` - section name
`documentSection` - DocumentSection
getRelationshipContent
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getRelationshipContent()
Get content of word/_rels/document.xml.rels.
Returns:
content of word/_rels/document.xml.rels
setRelationshipContent
public void setRelationshipContent([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) relationshipContent)
Set content of word/_rels/document.xml.rels.
Parameters:
`relationshipContent` - content of word/_rels/document.xml.rels
getContentTypeContent
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getContentTypeContent()
Get content of [Content_Type].xml
Returns:
content of [Content_Type].xml
setContentTypeContent
public void setContentTypeContent([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) contentTypeContent)
Set content of [Content_Type].xml
Parameters:
`contentTypeContent` - content of [Content_Type].xml
getStyleContent
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getStyleContent()
Get content of word/styles.xml
Returns:
content of word/styles.xml
setStyleContent
public void setStyleContent([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) styleContent)
Set content of word/styles.xml
Parameters:
`styleContent` - content of word/styles.xml
getAbstractNumberingMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getAbstractNumberingMap()
Get map of old id and new id to handle w:abstractNumId.
Returns:
map of abstractNumId
setAbstractNumberingMap
public void setAbstractNumberingMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> abstractNumberingMap)
Set map of old id and new id from w:abstractNumId in numbering.xml.
 The w:abstractNumId of child template may duplicate to main template.
 So, the value should be updated
Parameters:
`abstractNumberingMap` - map of abstractNumId
updateAbstractNumberingMap
public void updateAbstractNumberingMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) oldId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newId)
Add or update old id and new id from w:abstractNumId
Parameters:
`oldId` - original value id of w:abstractNumId
`newId` - new value id of w:abstractNumId
getNumberingMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getNumberingMap()
Get map of old id and new id to handle w:numId.
Returns:
map of w:numId
setNumberingMap
public void setNumberingMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> numberingMap)
Set map of old id and new id from w:numId in numbering.xml.
 The w:numId of child template may duplicate to main template.
 So, the value should be updated
Parameters:
`numberingMap` - map of numId
updateNumberingMap
public void updateNumberingMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) oldId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newId)
Add or update old id and new id from w:numId.
Parameters:
`oldId` - original value id of w:numId
`newId` - new value id of w:numId
getNumberingContent
public [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) getNumberingContent()
Get content of word/numbering.xml
Returns:
content of word/numbering.xml
setNumberingContent
public void setNumberingContent([StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) numberingContent)
Set content of word/numbering.xml
Parameters:
`numberingContent` - content of word/numbering.xml
getChildStyleIdMap
public [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getChildStyleIdMap()
setChildStyleIdMap
public void setChildStyleIdMap([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> childStyleIdMap)
updateChildStyleIdMap
public void updateChildStyleIdMap([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) oldStyleId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) newStyleId)
isUpdateChildStyleAndNumbering
public boolean isUpdateChildStyleAndNumbering()
Check if child style has been updated or not.
 This value help us to avoid updating same style.
Returns:
true if child style has already been updated.
setUpdateChildStyleAndNumbering
public void setUpdateChildStyleAndNumbering(boolean updateChildStyleAndNumbering)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.ooxml.child.docx</a></div>
<h1 class="title" title="Class DocumentInfo">Class DocumentInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DocumentInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Handle document information.<br/>
 The DOCX template contains files in zip.<br/>
 For example:<br/>
  - [Content_Type].xml<br/>
  - word/document.xml<br/>
  - word/_rels/document.xml.rels<br/>
  - word/styles.xml<br/>
  - etc.
  
 When it include content from another template, the related file should be included.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#reservedContentType">reservedContentType</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of ContentType attribute value in [Content_Type].xml that should be at most one can have the value in the file</div>
</div>
<div class="col-first odd-row-color"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#reservedRelationshipType">reservedRelationshipType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of Type attribute value in word/_rels/document.xml.rels that should be at most one in the file</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo,java.lang.String)">DocumentInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> mainDocInfo,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContentTypes(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType)">addContentTypes</a><wbr/>(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType contentTypes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add a DocumentContentType object to set of DocumentContentType.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbstractNumberingMap()">getAbstractNumberingMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of old id and new id to handle w:abstractNumId.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildDocumentInfoMap()">getChildDocumentInfoMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of child id and child DocumentInfo.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildPathAndIDMap()">getChildPathAndIDMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of child path and child id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getChildStyleIdMap()">getChildStyleIdMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContentTypeContent()">getContentTypeContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get content of [Content_Type].xml</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContentTypeNameSpaceMap()">getContentTypeNameSpaceMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContentTypes()">getContentTypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get set of DocumentContentType.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocumentBuffer()">getDocumentBuffer</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get documentation content.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDocumentNameSpaceMap()">getDocumentNameSpaceMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDynamicRelationshipMap()">getDynamicRelationshipMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of dynamic relationship.<br/>
 {dynamic relationship id, DocumentRelationship}</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFile()">getFile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get document file</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFilePath()">getFilePath</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get path of document</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get document id</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMainDocInfo()">getMainDocInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get main document</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberingContent()">getNumberingContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get content of word/numbering.xml</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberingMap()">getNumberingMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of old id and new id to handle w:numId.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipContent()">getRelationshipContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get content of word/_rels/document.xml.rels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRelationshipMap()">getRelationshipMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of relationship.<br/>
 {relationship id, DocumentRelationship}</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSectionInfoMap()">getSectionInfoMap</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of section id and DocumentSection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStaticRelationshipMap()">getStaticRelationshipMap</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get map of static relationship.<br/>
 {static relationship id, DocumentRelationship}</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStyleContent()">getStyleContent</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get content of word/styles.xml</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUpdateChildStyleAndNumbering()">isUpdateChildStyleAndNumbering</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if child style has been updated or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAbstractNumberingMap(java.util.Map)">setAbstractNumberingMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; abstractNumberingMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of old id and new id from w:abstractNumId in numbering.xml.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChildDocumentInfoMap(java.util.Map)">setChildDocumentInfoMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a>&gt; childDocumentInfoMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of child id and child DocumentInfo.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChildPathAndIDMap(java.util.Map)">setChildPathAndIDMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; childPathAndIDMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of child path and child id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setChildStyleIdMap(java.util.Map)">setChildStyleIdMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; childStyleIdMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContentTypeContent(java.lang.StringBuilder)">setContentTypeContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> contentTypeContent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set content of [Content_Type].xml</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContentTypeNameSpaceMap(java.util.Map)">setContentTypeNameSpaceMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; contentTypeNameSpaceMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContentTypes(java.util.Set)">setContentTypes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt; contentTypes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set set of DocumentContentType.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocumentBuffer(java.lang.StringBuilder)">setDocumentBuffer</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> documentBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set documentation content.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDocumentNameSpaceMap(java.util.Map)">setDocumentNameSpaceMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; documentNameSpaceMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDynamicRelationshipMap(java.util.Map)">setDynamicRelationshipMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship&gt; dynamicRelationshipMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of dynamic relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFilePath(java.lang.String)">setFilePath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set path of document</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setId(java.lang.String)">setId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set document id</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMainDocInfo(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">setMainDocInfo</a><wbr/>(<a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> mainDocInfo)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">set main document</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberingContent(java.lang.StringBuilder)">setNumberingContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> numberingContent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set content of word/numbering.xml</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setNumberingMap(java.util.Map)">setNumberingMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numberingMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of old id and new id from w:numId in numbering.xml.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRelationshipContent(java.lang.StringBuilder)">setRelationshipContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> relationshipContent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set content of word/_rels/document.xml.rels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setRelationshipMap(java.util.Map)">setRelationshipMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt; relationshipMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSectionInfoMap(java.util.Map)">setSectionInfoMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection&gt; sectionInfoMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of section id and DocumentSection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStaticRelationshipMap(java.util.Map)">setStaticRelationshipMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt; staticRelationshipMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set map of static relationship.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setStyleContent(java.lang.StringBuilder)">setStyleContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> styleContent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set content of word/styles.xml</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUpdateChildStyleAndNumbering(boolean)">setUpdateChildStyleAndNumbering</a><wbr/>(boolean updateChildStyleAndNumbering)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#upateSectionChildMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">upateSectionChildMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> childid,
 <a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> childDocumentInfo)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update map of child id and child DocumentInfo.<br/>
 When the engine found child template, child DocumentInfo will be created.<br/>
 The child id and child DocumentInfo will be added to this map of Main DocumentInfo.<br/>
<br/> 
 For example: <br/>
 #includeSection("child.docx", "A")<br/>
 child path = "child.docx"<br/>
 child id = "sectionChild1"<br/>
 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo.<br/>
 The child DocumentInfo of "child.docx" template will be created.<br/>
 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateAbstractNumberingMap(java.lang.String,java.lang.String)">updateAbstractNumberingMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add or update old id and new id from w:abstractNumId</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateChildPathAndIDMap(java.lang.String,java.lang.String)">updateChildPathAndIDMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> childPath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> childId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update map of child path and child id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateChildStyleIdMap(java.lang.String,java.lang.String)">updateChildStyleIdMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldStyleId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newStyleId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateContentTypeNameSpaceMap(java.lang.String,java.lang.String)">updateContentTypeNameSpaceMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateDocumentNameSpaceMap(java.lang.String,java.lang.String)">updateDocumentNameSpaceMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateDynamicRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship)">updateDynamicRelationshipMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship documentRelationship)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update map of dynamic relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateNumberingMap(java.lang.String,java.lang.String)">updateNumberingMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add or update old id and new id from w:numId.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship)">updateRelationshipMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship relationship)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update map of relationship.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateSectionInfoMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection)">updateSectionInfoMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sectionName,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection documentSection)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update map of section id and DocumentSection.<br/>
 When the engine found section of child document, DocumentSection will be created.<br/>
 The sectionName and DocumentSection will be added to this map of child DocumentInfo.<br/>
<br/> 
 For example: <br/>
 #includeSection("child.docx", "A")<br/>
 child path = "child.docx"<br/>
 child id = "sectionChild1"<br/>
 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo.<br/>
 The child DocumentInfo of "child.docx" template will be created.<br/>
 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo.<br/>
 The DocumentSection of section A will be created.<br/>
 The pair of {"A", aDocumentSection} will be added to sectionInfoMap of childDocumentInfo.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateStaticRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship)">updateStaticRelationshipMap</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship documentRelationship)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Update map of static relationship.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="reservedRelationshipType">
<h3>reservedRelationshipType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">reservedRelationshipType</span></div>
<div class="block">List of Type attribute value in word/_rels/document.xml.rels that should be at most one in the file</div>
</section>
</li>
<li>
<section class="detail" id="reservedContentType">
<h3>reservedContentType</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">reservedContentType</span></div>
<div class="block">List of ContentType attribute value in [Content_Type].xml that should be at most one can have the value in the file</div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo,java.lang.String)">
<h3>DocumentInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DocumentInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> mainDocInfo,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - document id</dd>
<dd><code>mainDocInfo</code> - main document info</dd>
<dd><code>filePath</code> - file path of document</dd>
</dl>
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
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block">Get document id</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>document id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setId(java.lang.String)">
<h3>setId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Set document id</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - document id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFile()">
<h3>getFile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getFile</span>()</div>
<div class="block">Get document file</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>document file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFilePath()">
<h3>getFilePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFilePath</span>()</div>
<div class="block">Get path of document</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>path of document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFilePath(java.lang.String)">
<h3>setFilePath</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFilePath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath)</span></div>
<div class="block">Set path of document</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filePath</code> - path of document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMainDocInfo()">
<h3>getMainDocInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a></span> <span class="element-name">getMainDocInfo</span>()</div>
<div class="block">Get main document</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>main document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMainDocInfo(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">
<h3>setMainDocInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMainDocInfo</span><wbr/><span class="parameters">(<a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> mainDocInfo)</span></div>
<div class="block">set main document</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mainDocInfo</code> - document</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentBuffer()">
<h3>getDocumentBuffer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getDocumentBuffer</span>()</div>
<div class="block">Get documentation content.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>documentation content</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDocumentBuffer(java.lang.StringBuilder)">
<h3>setDocumentBuffer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocumentBuffer</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> documentBuffer)</span></div>
<div class="block">Set documentation content.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>documentBuffer</code> - documentation content</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDocumentNameSpaceMap()">
<h3>getDocumentNameSpaceMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getDocumentNameSpaceMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setDocumentNameSpaceMap(java.util.Map)">
<h3>setDocumentNameSpaceMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDocumentNameSpaceMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; documentNameSpaceMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateDocumentNameSpaceMap(java.lang.String,java.lang.String)">
<h3>updateDocumentNameSpaceMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateDocumentNameSpaceMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getContentTypes()">
<h3>getContentTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt;</span> <span class="element-name">getContentTypes</span>()</div>
<div class="block">Get set of DocumentContentType.
 DocumentContentType contains key and value of each attribute in [Content_Type].xml</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>list of content type objects</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContentTypes(java.util.Set)">
<h3>setContentTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContentTypes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType&gt; contentTypes)</span></div>
<div class="block">Set set of DocumentContentType.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contentTypes</code> - set of DocumentContentType</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContentTypes(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType)">
<h3>addContentTypes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addContentTypes</span><wbr/><span class="parameters">(com.nomagic.magicreport.engine.ooxml.child.docx.DocumentContentType contentTypes)</span></div>
<div class="block">Add a DocumentContentType object to set of DocumentContentType.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contentTypes</code> - content type object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContentTypeNameSpaceMap()">
<h3>getContentTypeNameSpaceMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getContentTypeNameSpaceMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setContentTypeNameSpaceMap(java.util.Map)">
<h3>setContentTypeNameSpaceMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContentTypeNameSpaceMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; contentTypeNameSpaceMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateContentTypeNameSpaceMap(java.lang.String,java.lang.String)">
<h3>updateContentTypeNameSpaceMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateContentTypeNameSpaceMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="getRelationshipMap()">
<h3>getRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt;</span> <span class="element-name">getRelationshipMap</span>()</div>
<div class="block">Get map of relationship.<br/>
 {relationship id, DocumentRelationship}</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRelationshipMap(java.util.Map)">
<h3>setRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRelationshipMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt; relationshipMap)</span></div>
<div class="block">Set map of relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationshipMap</code> - map of relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship)">
<h3>updateRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateRelationshipMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship relationship)</span></div>
<div class="block">Update map of relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - relationship id</dd>
<dd><code>relationship</code> - DocumentRelationship object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStaticRelationshipMap()">
<h3>getStaticRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt;</span> <span class="element-name">getStaticRelationshipMap</span>()</div>
<div class="block">Get map of static relationship.<br/>
 {static relationship id, DocumentRelationship}</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of static relationship id and related DocumentRelationship object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStaticRelationshipMap(java.util.Map)">
<h3>setStaticRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStaticRelationshipMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship&gt; staticRelationshipMap)</span></div>
<div class="block">Set map of static relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>staticRelationshipMap</code> - map of static relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateStaticRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship)">
<h3>updateStaticRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateStaticRelationshipMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentRelationship documentRelationship)</span></div>
<div class="block">Update map of static relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - static relationship id</dd>
<dd><code>documentRelationship</code> - DocumentRelationship object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDynamicRelationshipMap()">
<h3>getDynamicRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship&gt;</span> <span class="element-name">getDynamicRelationshipMap</span>()</div>
<div class="block">Get map of dynamic relationship.<br/>
 {dynamic relationship id, DocumentRelationship}</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of dynamic relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDynamicRelationshipMap(java.util.Map)">
<h3>setDynamicRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDynamicRelationshipMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship&gt; dynamicRelationshipMap)</span></div>
<div class="block">Set map of dynamic relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dynamicRelationshipMap</code> - map of dynamic relationship</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateDynamicRelationshipMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship)">
<h3>updateDynamicRelationshipMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateDynamicRelationshipMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 com.nomagic.magicreport.engine.ooxml.child.docx.DynamicDocumentRelationship documentRelationship)</span></div>
<div class="block">Update map of dynamic relationship.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - dynamic relationship id</dd>
<dd><code>documentRelationship</code> - DocumentRelationship object</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildPathAndIDMap()">
<h3>getChildPathAndIDMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getChildPathAndIDMap</span>()</div>
<div class="block">Get map of child path and child id.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of child path and child id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChildPathAndIDMap(java.util.Map)">
<h3>setChildPathAndIDMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChildPathAndIDMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; childPathAndIDMap)</span></div>
<div class="block">Set map of child path and child id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>childPathAndIDMap</code> - map of child path and child id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateChildPathAndIDMap(java.lang.String,java.lang.String)">
<h3>updateChildPathAndIDMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateChildPathAndIDMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> childPath,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> childId)</span></div>
<div class="block">Update map of child path and child id.
 <br/>
 When the engine found child template, child id will be created.<br/>
 The child template file path and child id will be added to this map.<br/>
<br/> 
 For example: <br/>
 #includeSection("child.docx", "A")<br/>
 child path = "child.docx"<br/>
 child id = "sectionChild1"<br/>
 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>childPath</code> - child path</dd>
<dd><code>childId</code> - child id</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildDocumentInfoMap()">
<h3>getChildDocumentInfoMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a>&gt;</span> <span class="element-name">getChildDocumentInfoMap</span>()</div>
<div class="block">Get map of child id and child DocumentInfo.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of child id and DocumentInfo of child</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setChildDocumentInfoMap(java.util.Map)">
<h3>setChildDocumentInfoMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChildDocumentInfoMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a>&gt; childDocumentInfoMap)</span></div>
<div class="block">Set map of child id and child DocumentInfo.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>childDocumentInfoMap</code> - map of child id and DocumentInfo of child</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="upateSectionChildMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentInfo)">
<h3>upateSectionChildMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">upateSectionChildMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> childid,
 <a href="DocumentInfo.html" title="class in com.nomagic.magicreport.engine.ooxml.child.docx">DocumentInfo</a> childDocumentInfo)</span></div>
<div class="block">Update map of child id and child DocumentInfo.<br/>
 When the engine found child template, child DocumentInfo will be created.<br/>
 The child id and child DocumentInfo will be added to this map of Main DocumentInfo.<br/>
<br/> 
 For example: <br/>
 #includeSection("child.docx", "A")<br/>
 child path = "child.docx"<br/>
 child id = "sectionChild1"<br/>
 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo.<br/>
 The child DocumentInfo of "child.docx" template will be created.<br/>
 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>childid</code> - child template id</dd>
<dd><code>childDocumentInfo</code> - child DocumentInfo</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSectionInfoMap()">
<h3>getSectionInfoMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection&gt;</span> <span class="element-name">getSectionInfoMap</span>()</div>
<div class="block">Get map of section id and DocumentSection.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of section id and DocumentSection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSectionInfoMap(java.util.Map)">
<h3>setSectionInfoMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSectionInfoMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/>com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection&gt; sectionInfoMap)</span></div>
<div class="block">Set map of section id and DocumentSection.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sectionInfoMap</code> - map of section id and DocumentSection.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateSectionInfoMap(java.lang.String,com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection)">
<h3>updateSectionInfoMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateSectionInfoMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sectionName,
 com.nomagic.magicreport.engine.ooxml.child.docx.DocumentSection documentSection)</span></div>
<div class="block">Update map of section id and DocumentSection.<br/>
 When the engine found section of child document, DocumentSection will be created.<br/>
 The sectionName and DocumentSection will be added to this map of child DocumentInfo.<br/>
<br/> 
 For example: <br/>
 #includeSection("child.docx", "A")<br/>
 child path = "child.docx"<br/>
 child id = "sectionChild1"<br/>
 The pair of {"child.docx", "sectionChild1"} will be added to childPathAndIDMap of Main DocumentInfo.<br/>
 The child DocumentInfo of "child.docx" template will be created.<br/>
 The pair of {"sectionChild1", childDocumentInfo} will be added to childDocumentInfoMap of Main DocumentInfo.<br/>
 The DocumentSection of section A will be created.<br/>
 The pair of {"A", aDocumentSection} will be added to sectionInfoMap of childDocumentInfo.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sectionName</code> - section name</dd>
<dd><code>documentSection</code> - DocumentSection</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRelationshipContent()">
<h3>getRelationshipContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getRelationshipContent</span>()</div>
<div class="block">Get content of word/_rels/document.xml.rels.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>content of word/_rels/document.xml.rels</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRelationshipContent(java.lang.StringBuilder)">
<h3>setRelationshipContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRelationshipContent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> relationshipContent)</span></div>
<div class="block">Set content of word/_rels/document.xml.rels.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>relationshipContent</code> - content of word/_rels/document.xml.rels</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContentTypeContent()">
<h3>getContentTypeContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getContentTypeContent</span>()</div>
<div class="block">Get content of [Content_Type].xml</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>content of [Content_Type].xml</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setContentTypeContent(java.lang.StringBuilder)">
<h3>setContentTypeContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setContentTypeContent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> contentTypeContent)</span></div>
<div class="block">Set content of [Content_Type].xml</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>contentTypeContent</code> - content of [Content_Type].xml</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStyleContent()">
<h3>getStyleContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getStyleContent</span>()</div>
<div class="block">Get content of word/styles.xml</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>content of word/styles.xml</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStyleContent(java.lang.StringBuilder)">
<h3>setStyleContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStyleContent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> styleContent)</span></div>
<div class="block">Set content of word/styles.xml</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>styleContent</code> - content of word/styles.xml</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbstractNumberingMap()">
<h3>getAbstractNumberingMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getAbstractNumberingMap</span>()</div>
<div class="block">Get map of old id and new id to handle w:abstractNumId.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of abstractNumId</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAbstractNumberingMap(java.util.Map)">
<h3>setAbstractNumberingMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAbstractNumberingMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; abstractNumberingMap)</span></div>
<div class="block">Set map of old id and new id from w:abstractNumId in numbering.xml.
 The w:abstractNumId of child template may duplicate to main template.
 So, the value should be updated</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>abstractNumberingMap</code> - map of abstractNumId</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateAbstractNumberingMap(java.lang.String,java.lang.String)">
<h3>updateAbstractNumberingMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateAbstractNumberingMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newId)</span></div>
<div class="block">Add or update old id and new id from w:abstractNumId</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldId</code> - original value id of w:abstractNumId</dd>
<dd><code>newId</code> - new value id of w:abstractNumId</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNumberingMap()">
<h3>getNumberingMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getNumberingMap</span>()</div>
<div class="block">Get map of old id and new id to handle w:numId.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>map of w:numId</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNumberingMap(java.util.Map)">
<h3>setNumberingMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberingMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; numberingMap)</span></div>
<div class="block">Set map of old id and new id from w:numId in numbering.xml.
 The w:numId of child template may duplicate to main template.
 So, the value should be updated</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>numberingMap</code> - map of numId</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateNumberingMap(java.lang.String,java.lang.String)">
<h3>updateNumberingMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateNumberingMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newId)</span></div>
<div class="block">Add or update old id and new id from w:numId.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldId</code> - original value id of w:numId</dd>
<dd><code>newId</code> - new value id of w:numId</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNumberingContent()">
<h3>getNumberingContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a></span> <span class="element-name">getNumberingContent</span>()</div>
<div class="block">Get content of word/numbering.xml</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>content of word/numbering.xml</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNumberingContent(java.lang.StringBuilder)">
<h3>setNumberingContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setNumberingContent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> numberingContent)</span></div>
<div class="block">Set content of word/numbering.xml</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>numberingContent</code> - content of word/numbering.xml</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getChildStyleIdMap()">
<h3>getChildStyleIdMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getChildStyleIdMap</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setChildStyleIdMap(java.util.Map)">
<h3>setChildStyleIdMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setChildStyleIdMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; childStyleIdMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="updateChildStyleIdMap(java.lang.String,java.lang.String)">
<h3>updateChildStyleIdMap</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateChildStyleIdMap</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> oldStyleId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> newStyleId)</span></div>
</section>
</li>
<li>
<section class="detail" id="isUpdateChildStyleAndNumbering()">
<h3>isUpdateChildStyleAndNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUpdateChildStyleAndNumbering</span>()</div>
<div class="block">Check if child style has been updated or not.
 This value help us to avoid updating same style.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if child style has already been updated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUpdateChildStyleAndNumbering(boolean)">
<h3>setUpdateChildStyleAndNumbering</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUpdateChildStyleAndNumbering</span><wbr/><span class="parameters">(boolean updateChildStyleAndNumbering)</span></div>
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
