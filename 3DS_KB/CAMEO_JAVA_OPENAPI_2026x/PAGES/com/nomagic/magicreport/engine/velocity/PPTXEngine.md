# JAVA OPENAPI: PPTXEngine (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/velocity/PPTXEngine.html
- source_path: `com/nomagic/magicreport/engine/velocity/PPTXEngine.html`
- source_sha256: `b7a1f1bf32695454feeadea88cc2be5c69a3913a779056fbbc0c686e4a61f865`
- captured_utc: `2026-07-14T16:58:38.116293+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class PPTXEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.AbstractTemplateEngine](../AbstractTemplateEngine.html)
[com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine](DefaultTemplateEngine.html)
com.nomagic.magicreport.engine.velocity.PPTXEngine

All Implemented Interfaces:
`[IExtensionTemplateEngine](../IExtensionTemplateEngine.html)`, `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`, `[ITemplateEngine](../ITemplateEngine.html)`, `[StyledDocument](../../format/html/StyledDocument.html)`

@OpenApiAllpublic classPPTXEngine
extends [DefaultTemplateEngine](DefaultTemplateEngine.html)
implements [StyledDocument](../../format/html/StyledDocument.html)

The Velocity engine for OpenXML PowerPoint Presentation (PPTX).

Since:
Dec 28, 2009

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
`[PPTXEngine](#%3Cinit%3E())()`
A class constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`int`
`[addColor](#addColor(java.awt.Color))([Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)`
Add color for html to PPTX.
`int`
`[addFont](#addFont(java.awt.Font))([Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font)`
Add font for html to PPTX.
`void`
`[addImage](#addImage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) format)`
Add image format to list.
`int`
`[addList](#addList(com.nomagic.magicreport.format.html.List))([List](../../format/html/List.html) list)`
Add list for html to PPTX.
`int`
`[addObject](#addObject(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)`
Appends object content into the document.
`void`
`[addRowSpanID](#addRowSpanID(java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 int value)`
Add rowspan id and its value to map
`int`
`[addStyle](#addStyle(javax.swing.text.Style))([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) style)`
Add style for html to PPTX.
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
`void`
`[evaluate](#evaluate(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Merge a template with current context and rendered stream into the writer.
`[Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[getEntrySet](#getEntrySet())()`
Return PPTX entry set.
`[Template](../../Template.html)`
`[getTemplate](#getTemplate())()`
Return template.
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
`[handleIncludeSection](#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #includeSection directive.
`protected void`
`[handleMergeColumns](#handleMergeColumns(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle $tableprop.mergeColumns directive
`protected void`
`[handleMergeRows](#handleMergeRows(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle $tableprop.mergeRows directive
`protected void`
`[handleSectionBegin](#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #sectionBegin directive.
`protected int`
`[lineCount](#lineCount(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)`
Count number of line from given content string.
`protected void`
`[postProcess](#postProcess(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Perform a post-processing after the template has been evaluated.
`protected [TemplateException](../../TemplateException.html)`
`[processException](#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException))([Template](../../Template.html) template,
 [ParseErrorException](../../ParseErrorException.html) e)`
Call this method to process a [`ParseErrorException`](../../ParseErrorException.html).
`protected [TemplateException](../../TemplateException.html)`
`[processVelocityException](#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException))([Template](../../Template.html) template,
 org.apache.velocity.exception.ParseErrorException e)`
Call this method to process an Velocity exception and return in new format.
`protected void`
`[translate](#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Process the template in `inProcessBuffer` into valid format.
Methods inherited from class com.nomagic.magicreport.engine.velocity.[DefaultTemplateEngine](DefaultTemplateEngine.html)
`[abort](DefaultTemplateEngine.html#abort()), [checkFileNotFoundException](DefaultTemplateEngine.html#checkFileNotFoundException(java.lang.Exception,java.io.File)), [clearTools](DefaultTemplateEngine.html#clearTools()), [createComment](DefaultTemplateEngine.html#createComment(java.lang.String)), [destroy](DefaultTemplateEngine.html#destroy()), [getClassLoader](DefaultTemplateEngine.html#getClassLoader()), [getFormatter](DefaultTemplateEngine.html#getFormatter()), [getResolvedSectionName](DefaultTemplateEngine.html#getResolvedSectionName(java.lang.String)), [handleImport](DefaultTemplateEngine.html#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)), [isNoSpaceException](DefaultTemplateEngine.html#isNoSpaceException(java.lang.Exception)), [preProcess](DefaultTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)), [process](DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template)), [process](DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)), [processVelocityException](DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)), [setClassLoader](DefaultTemplateEngine.html#setClassLoader(java.lang.ClassLoader)), [setFormatter](DefaultTemplateEngine.html#setFormatter(com.nomagic.magicreport.format.IFormatter)), [setLatestLocation](DefaultTemplateEngine.html#setLatestLocation(java.io.File,java.io.File)), [setLocation](DefaultTemplateEngine.html#setLocation(java.io.File,java.io.File)), [setProperty](DefaultTemplateEngine.html#setProperty(java.lang.String,java.lang.Object)), [setWriterForEvaluate](DefaultTemplateEngine.html#setWriterForEvaluate(com.nomagic.magicreport.Template)), [trimTrailSpace](DefaultTemplateEngine.html#trimTrailSpace(int,java.lang.StringBuilder))`
Methods inherited from class com.nomagic.magicreport.engine.[AbstractTemplateEngine](../AbstractTemplateEngine.html)
`[addContext](../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)), [addInvalidReferenceHandler](../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)), [addObserver](../AbstractTemplateEngine.html#addObserver(java.util.Observer)), [addReferenceInsertionHandler](../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)), [evaluate](../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)), [getConcurrentToolException](../AbstractTemplateEngine.html#getConcurrentToolException()), [getContext](../AbstractTemplateEngine.html#getContext()), [getCurrentRuntimeInstance](../AbstractTemplateEngine.html#getCurrentRuntimeInstance()), [getInvalidReferenceHandler](../AbstractTemplateEngine.html#getInvalidReferenceHandler()), [getProcessSize](../AbstractTemplateEngine.html#getProcessSize()), [getProperties](../AbstractTemplateEngine.html#getProperties()), [getProperty](../AbstractTemplateEngine.html#getProperty(java.lang.String)), [getReferenceInsertionHandler](../AbstractTemplateEngine.html#getReferenceInsertionHandler()), [isMemoryMode](../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)), [notifyObservers](../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)), [observers](../AbstractTemplateEngine.html#observers()), [setConcurrentToolException](../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)), [setContext](../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)), [setCurrentRuntimeInstance](../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
PPTXEngine
public PPTXEngine()
A class constructor.
 ============ METHOD DETAIL ========== 
Method Details
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
getTemplate
public [Template](../../Template.html) getTemplate()
Return template.
Returns:
a PPTX template
getEntrySet
public [Set](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> getEntrySet()
Return PPTX entry set.
Returns:
PPTX entry set.
addImage
public void addImage([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) format)
Add image format to list.
Parameters:
`format` - format of image
addRowSpanID
public void addRowSpanID([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id,
 int value)
Add rowspan id and its value to map
Parameters:
`id` - rowspan id
`value` - number of rows to be merged
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
translate
protected void translate([Template](../../Template.html) template,
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
createParseErrorWrapper
protected [ParseErrorException](../../ParseErrorException.html) createParseErrorWrapper([ParseErrorException](../../ParseErrorException.html) parseError,
 [Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) source)
Create a ParseErrorException from the message.
Parameters:
`parseError` - root cause
`source` - source template
Returns:
instance of ParseErrorException
processException
protected [TemplateException](../../TemplateException.html) processException([Template](../../Template.html) template,
 [ParseErrorException](../../ParseErrorException.html) e)
Call this method to process a [`ParseErrorException`](../../ParseErrorException.html). This method call internally by
 [`postProcess(Template)`](#postProcess(com.nomagic.magicreport.Template)). If code was performed by Velocity ([`DefaultTemplateEngine.process(Template)`](DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template))), uses method
 [`processVelocityException(Template, org.apache.velocity.exception.ParseErrorException)`](#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)). By default
 this method try to calculate line number from [`ParseErrorException.getSource()`](../../ParseErrorException.html#getSource()).
Overrides:
`[processException](DefaultTemplateEngine.html#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - Template
`e` - MagicReport parse error exception
Returns:
TemplateException
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
protected int lineCount([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)
Count number of line from given content string.
Overrides:
`[lineCount](DefaultTemplateEngine.html#lineCount(java.lang.String))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`content` - the input string
Returns:
number of line
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
postProcess
protected void postProcess([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Perform a post-processing after the template has been evaluated.
Overrides:
`[postProcess](DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))` in class `[DefaultTemplateEngine](DefaultTemplateEngine.html)`
Parameters:
`template` - template after evaluated.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`DefaultTemplateEngine.postProcess(com.nomagic.magicreport.Template)`](DefaultTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))
addFont
public int addFont([Font](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html) font)
Add font for html to PPTX.
Specified by:
`[addFont](../../format/html/StyledDocument.html#addFont(java.awt.Font))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`font` - font
Returns:
font id
addList
public int addList([List](../../format/html/List.html) list)
Add list for html to PPTX.
Specified by:
`[addList](../../format/html/StyledDocument.html#addList(com.nomagic.magicreport.format.html.List))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`list` - list
Returns:
list id
addStyle
public int addStyle([Style](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html) style)
Add style for html to PPTX.
Specified by:
`[addStyle](../../format/html/StyledDocument.html#addStyle(javax.swing.text.Style))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`style` - style
Returns:
style id
addColor
public int addColor([Color](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html) color)
Add color for html to PPTX.
Specified by:
`[addColor](../../format/html/StyledDocument.html#addColor(java.awt.Color))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`color` - color
Returns:
color id
addObject
public int addObject([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object)
Appends object content into the document.
Specified by:
`[addObject](../../format/html/StyledDocument.html#addObject(java.lang.Object))` in interface `[StyledDocument](../../format/html/StyledDocument.html)`
Parameters:
`object` - adding object
Returns:
index to object

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class PPTXEngine">Class PPTXEngine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.AbstractTemplateEngine</a>
<div class="inheritance"><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine</a>
<div class="inheritance">com.nomagic.magicreport.engine.velocity.PPTXEngine</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">PPTXEngine</span>
<span class="extends-implements">extends <a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a>
implements <a href="../../format/html/StyledDocument.html" title="interface in com.nomagic.magicreport.format.html">StyledDocument</a></span></div>
<div class="block">The Velocity engine for OpenXML PowerPoint Presentation (PPTX).</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Dec 28, 2009</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">PPTXEngine</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addColor(java.awt.Color)">addColor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Color.html" title="class or interface in java.awt">Color</a> color)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add color for html to PPTX.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addFont(java.awt.Font)">addFont</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add font for html to PPTX.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addImage(java.lang.String)">addImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add image format to list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addList(com.nomagic.magicreport.format.html.List)">addList</a><wbr/>(<a href="../../format/html/List.html" title="interface in com.nomagic.magicreport.format.html">List</a> list)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add list for html to PPTX.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addObject(java.lang.Object)">addObject</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Appends object content into the document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addRowSpanID(java.lang.String,int)">addRowSpanID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add rowspan id and its value to map</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addStyle(javax.swing.text.Style)">addStyle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/javax/swing/text/Style.html" title="class or interface in javax.swing.text">Style</a> style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add style for html to PPTX.</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#evaluate(com.nomagic.magicreport.Template)">evaluate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getEntrySet()">getEntrySet</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return PPTX entry set.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplate()">getTemplate</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return template.</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleIncludeSection</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleSectionBegin</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #sectionBegin directive.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)">processException</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to process a <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)">processVelocityException</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 org.apache.velocity.exception.ParseErrorException e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to process an Velocity exception and return in new format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)">translate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine">Methods inherited from class com.nomagic.magicreport.engine.velocity.<a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></h3>
<code><a href="DefaultTemplateEngine.html#abort()">abort</a>, <a href="DefaultTemplateEngine.html#checkFileNotFoundException(java.lang.Exception,java.io.File)">checkFileNotFoundException</a>, <a href="DefaultTemplateEngine.html#clearTools()">clearTools</a>, <a href="DefaultTemplateEngine.html#createComment(java.lang.String)">createComment</a>, <a href="DefaultTemplateEngine.html#destroy()">destroy</a>, <a href="DefaultTemplateEngine.html#getClassLoader()">getClassLoader</a>, <a href="DefaultTemplateEngine.html#getFormatter()">getFormatter</a>, <a href="DefaultTemplateEngine.html#getResolvedSectionName(java.lang.String)">getResolvedSectionName</a>, <a href="DefaultTemplateEngine.html#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleImport</a>, <a href="DefaultTemplateEngine.html#isNoSpaceException(java.lang.Exception)">isNoSpaceException</a>, <a href="DefaultTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)">preProcess</a>, <a href="DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template)">process</a>, <a href="DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">process</a>, <a href="DefaultTemplateEngine.html#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)">processVelocityException</a>, <a href="DefaultTemplateEngine.html#setClassLoader(java.lang.ClassLoader)">setClassLoader</a>, <a href="DefaultTemplateEngine.html#setFormatter(com.nomagic.magicreport.format.IFormatter)">setFormatter</a>, <a href="DefaultTemplateEngine.html#setLatestLocation(java.io.File,java.io.File)">setLatestLocation</a>, <a href="DefaultTemplateEngine.html#setLocation(java.io.File,java.io.File)">setLocation</a>, <a href="DefaultTemplateEngine.html#setProperty(java.lang.String,java.lang.Object)">setProperty</a>, <a href="DefaultTemplateEngine.html#setWriterForEvaluate(com.nomagic.magicreport.Template)">setWriterForEvaluate</a>, <a href="DefaultTemplateEngine.html#trimTrailSpace(int,java.lang.StringBuilder)">trimTrailSpace</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.AbstractTemplateEngine">Methods inherited from class com.nomagic.magicreport.engine.<a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></h3>
<code><a href="../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)">addContext</a>, <a href="../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">addInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#addObserver(java.util.Observer)">addObserver</a>, <a href="../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">addReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">evaluate</a>, <a href="../AbstractTemplateEngine.html#getConcurrentToolException()">getConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#getContext()">getContext</a>, <a href="../AbstractTemplateEngine.html#getCurrentRuntimeInstance()">getCurrentRuntimeInstance</a>, <a href="../AbstractTemplateEngine.html#getInvalidReferenceHandler()">getInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#getProcessSize()">getProcessSize</a>, <a href="../AbstractTemplateEngine.html#getProperties()">getProperties</a>, <a href="../AbstractTemplateEngine.html#getProperty(java.lang.String)">getProperty</a>, <a href="../AbstractTemplateEngine.html#getReferenceInsertionHandler()">getReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)">isMemoryMode</a>, <a href="../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../AbstractTemplateEngine.html#observers()">observers</a>, <a href="../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)">setConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance)">setCurrentRuntimeInstance</a></code></div>
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
<h3>PPTXEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PPTXEngine</span>()</div>
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
<section class="detail" id="getTemplate()">
<h3>getTemplate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></span> <span class="element-name">getTemplate</span>()</div>
<div class="block">Return template.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a PPTX template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEntrySet()">
<h3>getEntrySet</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">getEntrySet</span>()</div>
<div class="block">Return PPTX entry set.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>PPTX entry set.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addImage(java.lang.String)">
<h3>addImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addImage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> format)</span></div>
<div class="block">Add image format to list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>format</code> - format of image</dd>
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
<section class="detail" id="translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>translate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">translate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
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
<section class="detail" id="processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)">
<h3>processException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span> <span class="element-name">processException</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> e)</span></div>
<div class="block">Call this method to process a <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>. This method call internally by
 <a href="#postProcess(com.nomagic.magicreport.Template)"><code>postProcess(Template)</code></a>. If code was performed by Velocity (<a href="DefaultTemplateEngine.html#process(com.nomagic.magicreport.Template)"><code>DefaultTemplateEngine.process(Template)</code></a>), uses method
 <a href="#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)"><code>processVelocityException(Template, org.apache.velocity.exception.ParseErrorException)</code></a>. By default
 this method try to calculate line number from <a href="../../ParseErrorException.html#getSource()"><code>ParseErrorException.getSource()</code></a>.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a href="DefaultTemplateEngine.html#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)">processException</a></code> in class <code><a href="DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template</dd>
<dd><code>e</code> - MagicReport parse error exception</dd>
<dt>Returns:</dt>
<dd>TemplateException</dd>
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
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">lineCount</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</span></div>
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
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
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
<section class="detail" id="addFont(java.awt.Font)">
<h3>addFont</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">addFont</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Font.html" title="class or interface in java.awt">Font</a> font)</span></div>
<div class="block">Add font for html to PPTX.</div>
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
<div class="block">Add list for html to PPTX.</div>
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
<div class="block">Add style for html to PPTX.</div>
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
<div class="block">Add color for html to PPTX.</div>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
