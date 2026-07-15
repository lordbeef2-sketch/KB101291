# JAVA OPENAPI: DefaultTemplateEngine (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/velocity/DefaultTemplateEngine.html
- source_path: `com/nomagic/magicreport/engine/velocity/DefaultTemplateEngine.html`
- source_sha256: `d0254a66b0ba69b7f719c4f18edd5165acd9798660b27972e0e606d51c0ba5d8`
- captured_utc: `2026-07-14T16:58:37.855292+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class DefaultTemplateEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.AbstractTemplateEngine](../AbstractTemplateEngine.html)
com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine

All Implemented Interfaces:
`[IExtensionTemplateEngine](../IExtensionTemplateEngine.html)`, `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`, `[ITemplateEngine](../ITemplateEngine.html)`

Direct Known Subclasses:
`[DOCXEngine](DOCXEngine.html)`, `[HTMLEngine](HTMLEngine.html)`, `[LaTeXEngine](LaTeXEngine.html)`, `[PPTXEngine](PPTXEngine.html)`, `[RTFEngine](RTFEngine.html)`, `[TextEngine](TextEngine.html)`, `[XLSXEngine](XLSXEngine.html)`, `[XMLEngine](XMLEngine.html)`

@OpenApiAllpublic classDefaultTemplateEngine
extends [AbstractTemplateEngine](../AbstractTemplateEngine.html)
implements [IExtensionTemplateEngine](../IExtensionTemplateEngine.html)

Provide standard template engine for MagicReport. This engine performs directives translation during
 pre-processing, invoke Velocity evaluate method, and perform post-processing.

Since:
Mar 13, 2008

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected org.apache.velocity.VelocityContext`
`[velocityContext](#velocityContext)`
Hold velocity context to abort engine.
Fields inherited from class com.nomagic.magicreport.engine.[AbstractTemplateEngine](../AbstractTemplateEngine.html)
`[context](../AbstractTemplateEngine.html#context), [isAborted](../AbstractTemplateEngine.html#isAborted), [preProcessFile](../AbstractTemplateEngine.html#preProcessFile), [processFile](../AbstractTemplateEngine.html#processFile), [properties](../AbstractTemplateEngine.html#properties)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[DefaultTemplateEngine](#%3Cinit%3E())()`
Create an instance of engine.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[abort](#abort())()`
Call to abort Velocity context.
`protected void`
`[checkFileNotFoundException](#checkFileNotFoundException(java.lang.Exception,java.io.File))([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`

`void`
`[clearTools](#clearTools())()`

`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createComment](#createComment(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)`
Return a formatted comment from given message.
`[Template](../../Template.html)`
`[createTemplate](#createTemplate())()`
Creates a new and empty [`Template`](../../Template.html) for generating report by this engine.
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
`[destroy](#destroy())()`
Called by the application or [`TemplateEngineFactory`](../../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
`[ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html)`
`[getClassLoader](#getClassLoader())()`
Returns the class loader for the engine.
`[IFormatter](../../format/IFormatter.html)`
`[getFormatter](#getFormatter())()`
Returns a formatter that can be used to create the object layout, and formats of state
 [`InsertionHandler`](InsertionHandler.html).
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getResolvedSectionName](#getResolvedSectionName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sectionName)`

`protected void`
`[handleForPage](#handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #forpage directive.
`protected void`
`[handleForRow](#handleForRow(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #forrow directive.
`protected void`
`[handleImport](#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #include directive.
`protected void`
`[handleIncludeSection](#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #includeSection directive.
`protected void`
`[handleSectionBegin](#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Handle the #sectionBegin directive.
`protected boolean`
`[isNoSpaceException](#isNoSpaceException(java.lang.Exception))([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)`

`protected int`
`[lineCount](#lineCount(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)`
Count number of line from given content string.
`protected void`
`[postProcess](#postProcess(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Perform a post-processing after the template has been evaluated.
`protected void`
`[preProcess](#preProcess(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Perform a pre-processing before evaluate template.
`void`
`[process](#process(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`
Process a template.
`void`
`[process](#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine))([Template](../../Template.html) template,
 [ITemplateEngine](../ITemplateEngine.html) parentEngine)`
Process a template.
`protected [TemplateException](../../TemplateException.html)`
`[processException](#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException))([Template](../../Template.html) template,
 [ParseErrorException](../../ParseErrorException.html) e)`
Call this method to process a [`ParseErrorException`](../../ParseErrorException.html).
`protected [TemplateException](../../TemplateException.html)`
`[processVelocityException](#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException))([Template](../../Template.html) template,
 org.apache.velocity.exception.MethodInvocationException e)`
Call this method to process an Velocity exception and return in new format ([`ParseErrorException`](../../ParseErrorException.html)).
`protected [TemplateException](../../TemplateException.html)`
`[processVelocityException](#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException))([Template](../../Template.html) template,
 org.apache.velocity.exception.ParseErrorException e)`
Call this method to process an Velocity exception and return in new format ([`ParseErrorException`](../../ParseErrorException.html)).
`void`
`[setClassLoader](#setClassLoader(java.lang.ClassLoader))([ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) loader)`
Sets the class loader for this engine.
`void`
`[setFormatter](#setFormatter(com.nomagic.magicreport.format.IFormatter))([IFormatter](../../format/IFormatter.html) formatter)`
Set the formatter to be used with this template engine.
`protected void`
`[setLatestLocation](#setLatestLocation(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)`
Call this method to set the latest input and output location from given `input` and `output`
 file.
`protected void`
`[setLocation](#setLocation(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)`
Call this method to set the input and output location from given `input` and `output`
 file.
`void`
`[setProperty](#setProperty(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Set an engine Runtime property.
`protected [BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)`
`[setWriterForEvaluate](#setWriterForEvaluate(com.nomagic.magicreport.Template))([Template](../../Template.html) template)`

`protected void`
`[translate](#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder))([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Process the template in `inProcessBuffer` into valid format.
`int`
`[trimTrailSpace](#trimTrailSpace(int,java.lang.StringBuilder))(int currentEndCursor,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)`
Calculate and return the new cursor at the end of #hash statement after trim.
Methods inherited from class com.nomagic.magicreport.engine.[AbstractTemplateEngine](../AbstractTemplateEngine.html)
`[addContext](../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)), [addInvalidReferenceHandler](../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)), [addObserver](../AbstractTemplateEngine.html#addObserver(java.util.Observer)), [addReferenceInsertionHandler](../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)), [evaluate](../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template)), [evaluate](../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)), [getConcurrentToolException](../AbstractTemplateEngine.html#getConcurrentToolException()), [getContext](../AbstractTemplateEngine.html#getContext()), [getCurrentRuntimeInstance](../AbstractTemplateEngine.html#getCurrentRuntimeInstance()), [getInvalidReferenceHandler](../AbstractTemplateEngine.html#getInvalidReferenceHandler()), [getProcessSize](../AbstractTemplateEngine.html#getProcessSize()), [getProperties](../AbstractTemplateEngine.html#getProperties()), [getProperty](../AbstractTemplateEngine.html#getProperty(java.lang.String)), [getReferenceInsertionHandler](../AbstractTemplateEngine.html#getReferenceInsertionHandler()), [isMemoryMode](../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)), [notifyObservers](../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)), [observers](../AbstractTemplateEngine.html#observers()), [setConcurrentToolException](../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)), [setContext](../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)), [setCurrentRuntimeInstance](../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
velocityContext
protected org.apache.velocity.VelocityContext velocityContext
Hold velocity context to abort engine.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DefaultTemplateEngine
protected DefaultTemplateEngine()
Create an instance of engine.
 ============ METHOD DETAIL ========== 
Method Details
createTemplate
public [Template](../../Template.html) createTemplate()
Creates a new and empty [`Template`](../../Template.html) for generating report by this engine.
Specified by:
`[createTemplate](../ITemplateEngine.html#createTemplate())` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Returns:
an instance of [`Template`](../../Template.html)
See Also:
[`createTemplate(File, File)`](#createTemplate(java.io.File,java.io.File))
createTemplate
public [Template](../../Template.html) createTemplate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Creates a new [`Template`](../../Template.html) object.
Specified by:
`[createTemplate](../ITemplateEngine.html#createTemplate(java.io.File,java.io.File))` in interface `[ITemplateEngine](../ITemplateEngine.html)`
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
checkFileNotFoundException
protected void checkFileNotFoundException([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
 throws [FileNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html)
Throws:
`[FileNotFoundException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html)`
isNoSpaceException
protected boolean isNoSpaceException([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)
setLocation
protected void setLocation([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)
Call this method to set the input and output location from given `input` and `output`
 file.
Parameters:
`input` - input template file
`output` - output report file
See Also:
[`TemplateConstants.TEMPLATE_INPUT_FILE`](../TemplateConstants.html#TEMPLATE_INPUT_FILE)
[`TemplateConstants.TEMPLATE_INPUT_LOCATION`](../TemplateConstants.html#TEMPLATE_INPUT_LOCATION)
[`TemplateConstants.TEMPLATE_OUTPUT_FILE`](../TemplateConstants.html#TEMPLATE_OUTPUT_FILE)
[`TemplateConstants.TEMPLATE_OUTPUT_LOCATION`](../TemplateConstants.html#TEMPLATE_OUTPUT_LOCATION)
[`setProperty(String, Object)`](#setProperty(java.lang.String,java.lang.Object))
setLatestLocation
protected void setLatestLocation([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) input,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) output)
Call this method to set the latest input and output location from given `input` and `output`
 file.
Parameters:
`input` - input template file
`output` - output report file
setProperty
public void setProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Set an engine Runtime property.
Specified by:
`[setProperty](../ITemplateEngine.html#setProperty(java.lang.String,java.lang.Object))` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Overrides:
`[setProperty](../AbstractTemplateEngine.html#setProperty(java.lang.String,java.lang.Object))` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
Parameters:
`key` - the key to be placed into this property list.
`value` - the value corresponding to key.
See Also:
[`ITemplateEngine.getProperty(String)`](../ITemplateEngine.html#getProperty(java.lang.String))
getFormatter
public [IFormatter](../../format/IFormatter.html) getFormatter()
Returns a formatter that can be used to create the object layout, and formats of state
 [`InsertionHandler`](InsertionHandler.html).
 By default this class returns a [`DefaultFormatter`](../../format/DefaultFormatter.html). This formatter handle common text and no Bookmark,
 Link and Image support. The engine should override this method and return proper formatter implementation.
Specified by:
`[getFormatter](../ITemplateEngine.html#getFormatter())` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Returns:
a formatter
setFormatter
public void setFormatter([IFormatter](../../format/IFormatter.html) formatter)
Set the formatter to be used with this template engine.
Parameters:
`formatter` - a formatter
preProcess
protected void preProcess([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Perform a pre-processing before evaluate template. This step will translate the template into valid velocity
 format with additional directive recognize.
Specified by:
`[preProcess](../AbstractTemplateEngine.html#preProcess(com.nomagic.magicreport.Template))` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
Parameters:
`template` - template before evaluated.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`AbstractTemplateEngine.preProcess(com.nomagic.magicreport.Template)`](../AbstractTemplateEngine.html#preProcess(com.nomagic.magicreport.Template))
translate
protected void translate([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html),
[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Process the template in `inProcessBuffer` into valid format.
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if IO Error occurs while reading template.
handleForPage
protected void handleForPage([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #forpage directive.
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
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
handleImport
protected void handleImport([Template](../../Template.html) template,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
 throws [ParseErrorException](../../ParseErrorException.html)
Handle the #include directive.
Parameters:
`template` - Template source.
`inProcessBuffer` - in process buffer.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when error while translation, or syntax not recognized.
trimTrailSpace
public int trimTrailSpace(int currentEndCursor,
 [StringBuilder](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html) inProcessBuffer)
Calculate and return the new cursor at the end of #hash statement after trim.
Parameters:
`currentEndCursor` - current end statement cursor
`inProcessBuffer` - in process buffer
Returns:
new cursor at the end of #hash statement
createComment
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createComment([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) message)
Return a formatted comment from given message. The default comment format return from this method is "# {0}"
 where {0} is message;
Parameters:
`message` - message to put in document comment
Returns:
comment
process
public void process([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Process a template. By default this method will call velocity engine to renders the input reader using the
 context into the output writer.
Specified by:
`[process](../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template))` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
Parameters:
`template` - template being evaluated.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`AbstractTemplateEngine.process(com.nomagic.magicreport.Template)`](../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template))
process
public void process([Template](../../Template.html) template,
 [ITemplateEngine](../ITemplateEngine.html) parentEngine)
 throws [TemplateException](../../TemplateException.html)
Process a template. By default this method will call velocity engine to renders the input reader using the
 context into the output writer.
Specified by:
`[process](../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine))` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
Parameters:
`template` - template being evaluated.
`parentEngine` - an engine to shared a runtime instance for evaluate
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`AbstractTemplateEngine.process(com.nomagic.magicreport.Template)`](../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template))
setWriterForEvaluate
protected [BufferedWriter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html) setWriterForEvaluate([Template](../../Template.html) template)
postProcess
protected void postProcess([Template](../../Template.html) template)
 throws [TemplateException](../../TemplateException.html)
Perform a post-processing after the template has been evaluated. This process just copy output file directly
 from processing location to final output.
Specified by:
`[postProcess](../AbstractTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
Parameters:
`template` - template after evaluated.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../../TemplateException.html)` - other error while processing the template
See Also:
[`AbstractTemplateEngine.postProcess(com.nomagic.magicreport.Template)`](../AbstractTemplateEngine.html#postProcess(com.nomagic.magicreport.Template))
processVelocityException
protected [TemplateException](../../TemplateException.html) processVelocityException([Template](../../Template.html) template,
 org.apache.velocity.exception.MethodInvocationException e)
Call this method to process an Velocity exception and return in new format ([`ParseErrorException`](../../ParseErrorException.html)). By
 default, we can't get a nice error message from Velocity (Velocity error message containing in plain text
 and not readable by non-programmer.) And velocity itself doesn't provide any mechanism to get an message
 from ParseErrorException. This method will format the error message, remove unstructured text from velocity
 message e.g. "of" (with out appending text)
Parameters:
`template` - Template
`e` - MethodInvocationException
Returns:
TemplateException
processVelocityException
protected [TemplateException](../../TemplateException.html) processVelocityException([Template](../../Template.html) template,
 org.apache.velocity.exception.ParseErrorException e)
Call this method to process an Velocity exception and return in new format ([`ParseErrorException`](../../ParseErrorException.html)). By
 default, we can't get a nice error message from Velocity (Velocity error message containing in plain text
 and not readable by non-programmer.) And velocity itself doesn't provide any mechanism to get an message
 from ParseErrorException. This method will format the error message, remove unstructured text from velocity
 message e.g. "of" (with out appending text)
Parameters:
`template` - Template
`e` - Velocity exception
Returns:
TemplateException
processException
protected [TemplateException](../../TemplateException.html) processException([Template](../../Template.html) template,
 [ParseErrorException](../../ParseErrorException.html) e)
Call this method to process a [`ParseErrorException`](../../ParseErrorException.html). This method call internally by
 [`postProcess(Template)`](#postProcess(com.nomagic.magicreport.Template)). If code was performed by Velocity ([`process(Template)`](#process(com.nomagic.magicreport.Template))), uses method
 [`processVelocityException(Template, org.apache.velocity.exception.ParseErrorException)`](#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)). By default
 this method try to calculate line number from [`ParseErrorException.getSource()`](../../ParseErrorException.html#getSource()).
Parameters:
`template` - Template
`e` - MagicReport parse error exception
Returns:
TemplateException
lineCount
protected int lineCount([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)
Count number of line from given content string.
Parameters:
`content` - the input string
Returns:
number of line
getClassLoader
public [ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) getClassLoader()
Returns the class loader for the engine. This method will return null in such implementations if this class
 was loaded by the application class loader.
Specified by:
`[getClassLoader](../IExtensionTemplateEngine.html#getClassLoader())` in interface `[IExtensionTemplateEngine](../IExtensionTemplateEngine.html)`
Returns:
the class loader that loaded the class or interface represented by this object.
setClassLoader
public void setClassLoader([ClassLoader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html) loader)
Sets the class loader for this engine. The class loader must be set before a template is evaluated. This
 method allows the creator of the template to provide the appropriate class loader to code running in the
 template when loading classes and resources.
Specified by:
`[setClassLoader](../IExtensionTemplateEngine.html#setClassLoader(java.lang.ClassLoader))` in interface `[IExtensionTemplateEngine](../IExtensionTemplateEngine.html)`
Parameters:
`loader` - Class loader for this engine
destroy
public void destroy()
Called by the application or [`TemplateEngineFactory`](../../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
 A subclass of engine should override this method if it has any operation that it wants to perform before it
 is destroyed.
Specified by:
`[destroy](../ITemplateEngine.html#destroy())` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Overrides:
`[destroy](../AbstractTemplateEngine.html#destroy())` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
abort
public void abort()
Call to abort Velocity context.
Specified by:
`[abort](../ITemplateEngine.html#abort())` in interface `[ITemplateEngine](../ITemplateEngine.html)`
Overrides:
`[abort](../AbstractTemplateEngine.html#abort())` in class `[AbstractTemplateEngine](../AbstractTemplateEngine.html)`
getResolvedSectionName
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getResolvedSectionName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sectionName)
clearTools
public void clearTools()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class DefaultTemplateEngine">Class DefaultTemplateEngine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.AbstractTemplateEngine</a>
<div class="inheritance">com.nomagic.magicreport.engine.velocity.DefaultTemplateEngine</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../IExtensionTemplateEngine.html" title="interface in com.nomagic.magicreport.engine">IExtensionTemplateEngine</a></code>, <code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code>, <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="DOCXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DOCXEngine</a></code>, <code><a href="HTMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">HTMLEngine</a></code>, <code><a href="LaTeXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">LaTeXEngine</a></code>, <code><a href="PPTXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">PPTXEngine</a></code>, <code><a href="RTFEngine.html" title="class in com.nomagic.magicreport.engine.velocity">RTFEngine</a></code>, <code><a href="TextEngine.html" title="class in com.nomagic.magicreport.engine.velocity">TextEngine</a></code>, <code><a href="XLSXEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XLSXEngine</a></code>, <code><a href="XMLEngine.html" title="class in com.nomagic.magicreport.engine.velocity">XMLEngine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DefaultTemplateEngine</span>
<span class="extends-implements">extends <a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a>
implements <a href="../IExtensionTemplateEngine.html" title="interface in com.nomagic.magicreport.engine">IExtensionTemplateEngine</a></span></div>
<div class="block">Provide standard template engine for MagicReport. This engine performs directives translation during
 pre-processing, invoke Velocity evaluate method, and perform post-processing.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 13, 2008</dd>
</dl>
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
<div class="col-first even-row-color"><code>protected org.apache.velocity.VelocityContext</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#velocityContext">velocityContext</a></code></div>
<div class="col-last even-row-color">
<div class="block">Hold velocity context to abort engine.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.AbstractTemplateEngine">Fields inherited from class com.nomagic.magicreport.engine.<a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></h3>
<code><a href="../AbstractTemplateEngine.html#context">context</a>, <a href="../AbstractTemplateEngine.html#isAborted">isAborted</a>, <a href="../AbstractTemplateEngine.html#preProcessFile">preProcessFile</a>, <a href="../AbstractTemplateEngine.html#processFile">processFile</a>, <a href="../AbstractTemplateEngine.html#properties">properties</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">DefaultTemplateEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create an instance of engine.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#abort()">abort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call to abort Velocity context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkFileNotFoundException(java.lang.Exception,java.io.File)">checkFileNotFoundException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearTools()">clearTools</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createComment(java.lang.String)">createComment</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a formatted comment from given message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createTemplate()">createTemplate</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a new and empty <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> for generating report by this engine.</div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called by the application or <a href="../../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassLoader()">getClassLoader</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the class loader for the engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFormatter()">getFormatter</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a formatter that can be used to create the object layout, and formats of state
 <a href="InsertionHandler.html" title="class in com.nomagic.magicreport.engine.velocity"><code>InsertionHandler</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResolvedSectionName(java.lang.String)">getResolvedSectionName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sectionName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleImport</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #include directive.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleIncludeSection(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleIncludeSection</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #includeSection directive.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#handleSectionBegin(com.nomagic.magicreport.Template,java.lang.StringBuilder)">handleSectionBegin</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Handle the #sectionBegin directive.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isNoSpaceException(java.lang.Exception)">isNoSpaceException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#preProcess(com.nomagic.magicreport.Template)">preProcess</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Perform a pre-processing before evaluate template.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#process(com.nomagic.magicreport.Template)">process</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Process a template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">process</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Process a template.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)">processException</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to process a <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)">processVelocityException</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 org.apache.velocity.exception.MethodInvocationException e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to process an Velocity exception and return in new format (<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)">processVelocityException</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 org.apache.velocity.exception.ParseErrorException e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to process an Velocity exception and return in new format (<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClassLoader(java.lang.ClassLoader)">setClassLoader</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the class loader for this engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFormatter(com.nomagic.magicreport.format.IFormatter)">setFormatter</a><wbr/>(<a href="../../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a> formatter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the formatter to be used with this template engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLatestLocation(java.io.File,java.io.File)">setLatestLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to set the latest input and output location from given <code>input</code> and <code>output</code>
 file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLocation(java.io.File,java.io.File)">setLocation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call this method to set the input and output location from given <code>input</code> and <code>output</code>
 file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperty(java.lang.String,java.lang.Object)">setProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an engine Runtime property.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setWriterForEvaluate(com.nomagic.magicreport.Template)">setWriterForEvaluate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#translate(com.nomagic.magicreport.Template,java.lang.StringBuilder)">translate</a><wbr/>(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Process the template in <code>inProcessBuffer</code> into valid format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#trimTrailSpace(int,java.lang.StringBuilder)">trimTrailSpace</a><wbr/>(int currentEndCursor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calculate and return the new cursor at the end of #hash statement after trim.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.AbstractTemplateEngine">Methods inherited from class com.nomagic.magicreport.engine.<a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></h3>
<code><a href="../AbstractTemplateEngine.html#addContext(java.lang.String,java.lang.Object)">addContext</a>, <a href="../AbstractTemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">addInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#addObserver(java.util.Observer)">addObserver</a>, <a href="../AbstractTemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">addReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template)">evaluate</a>, <a href="../AbstractTemplateEngine.html#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">evaluate</a>, <a href="../AbstractTemplateEngine.html#getConcurrentToolException()">getConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#getContext()">getContext</a>, <a href="../AbstractTemplateEngine.html#getCurrentRuntimeInstance()">getCurrentRuntimeInstance</a>, <a href="../AbstractTemplateEngine.html#getInvalidReferenceHandler()">getInvalidReferenceHandler</a>, <a href="../AbstractTemplateEngine.html#getProcessSize()">getProcessSize</a>, <a href="../AbstractTemplateEngine.html#getProperties()">getProperties</a>, <a href="../AbstractTemplateEngine.html#getProperty(java.lang.String)">getProperty</a>, <a href="../AbstractTemplateEngine.html#getReferenceInsertionHandler()">getReferenceInsertionHandler</a>, <a href="../AbstractTemplateEngine.html#isMemoryMode(com.nomagic.magicreport.Template)">isMemoryMode</a>, <a href="../AbstractTemplateEngine.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../AbstractTemplateEngine.html#observers()">observers</a>, <a href="../AbstractTemplateEngine.html#setConcurrentToolException(java.lang.Exception)">setConcurrentToolException</a>, <a href="../AbstractTemplateEngine.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../AbstractTemplateEngine.html#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance)">setCurrentRuntimeInstance</a></code></div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="velocityContext">
<h3>velocityContext</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">org.apache.velocity.VelocityContext</span> <span class="element-name">velocityContext</span></div>
<div class="block">Hold velocity context to abort engine.</div>
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
<h3>DefaultTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">DefaultTemplateEngine</span>()</div>
<div class="block">Create an instance of engine.</div>
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
<div class="block">Creates a new and empty <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a> for generating report by this engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#createTemplate()">createTemplate</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>an instance of <a href="../../Template.html" title="class in com.nomagic.magicreport"><code>Template</code></a></dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createTemplate(java.io.File,java.io.File)"><code>createTemplate(File, File)</code></a></li>
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
<section class="detail" id="checkFileNotFoundException(java.lang.Exception,java.io.File)">
<h3>checkFileNotFoundException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">checkFileNotFoundException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html" title="class or interface in java.io">FileNotFoundException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/FileNotFoundException.html" title="class or interface in java.io">FileNotFoundException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNoSpaceException(java.lang.Exception)">
<h3>isNoSpaceException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isNoSpaceException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLocation(java.io.File,java.io.File)">
<h3>setLocation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</span></div>
<div class="block">Call this method to set the input and output location from given <code>input</code> and <code>output</code>
 file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input template file</dd>
<dd><code>output</code> - output report file</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../TemplateConstants.html#TEMPLATE_INPUT_FILE"><code>TemplateConstants.TEMPLATE_INPUT_FILE</code></a></li>
<li><a href="../TemplateConstants.html#TEMPLATE_INPUT_LOCATION"><code>TemplateConstants.TEMPLATE_INPUT_LOCATION</code></a></li>
<li><a href="../TemplateConstants.html#TEMPLATE_OUTPUT_FILE"><code>TemplateConstants.TEMPLATE_OUTPUT_FILE</code></a></li>
<li><a href="../TemplateConstants.html#TEMPLATE_OUTPUT_LOCATION"><code>TemplateConstants.TEMPLATE_OUTPUT_LOCATION</code></a></li>
<li><a href="#setProperty(java.lang.String,java.lang.Object)"><code>setProperty(String, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLatestLocation(java.io.File,java.io.File)">
<h3>setLatestLocation</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setLatestLocation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> output)</span></div>
<div class="block">Call this method to set the latest input and output location from given <code>input</code> and <code>output</code>
 file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - input template file</dd>
<dd><code>output</code> - output report file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperty(java.lang.String,java.lang.Object)">
<h3>setProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Set an engine Runtime property.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#setProperty(java.lang.String,java.lang.Object)">setProperty</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#setProperty(java.lang.String,java.lang.Object)">setProperty</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - the key to be placed into this property list.</dd>
<dd><code>value</code> - the value corresponding to key.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../ITemplateEngine.html#getProperty(java.lang.String)"><code>ITemplateEngine.getProperty(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFormatter()">
<h3>getFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a></span> <span class="element-name">getFormatter</span>()</div>
<div class="block">Returns a formatter that can be used to create the object layout, and formats of state
 <a href="InsertionHandler.html" title="class in com.nomagic.magicreport.engine.velocity"><code>InsertionHandler</code></a>.
 <p>
 By default this class returns a <a href="../../format/DefaultFormatter.html" title="class in com.nomagic.magicreport.format"><code>DefaultFormatter</code></a>. This formatter handle common text and no Bookmark,
 Link and Image support. The engine should override this method and return proper formatter implementation.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#getFormatter()">getFormatter</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>a formatter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFormatter(com.nomagic.magicreport.format.IFormatter)">
<h3>setFormatter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFormatter</span><wbr/><span class="parameters">(<a href="../../format/IFormatter.html" title="interface in com.nomagic.magicreport.format">IFormatter</a> formatter)</span></div>
<div class="block">Set the formatter to be used with this template engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>formatter</code> - a formatter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preProcess(com.nomagic.magicreport.Template)">
<h3>preProcess</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">preProcess</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                   throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Perform a pre-processing before evaluate template. This step will translate the template into valid velocity
 format with additional directive recognize.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)">preProcess</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - template before evaluated.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../AbstractTemplateEngine.html#preProcess(com.nomagic.magicreport.Template)"><code>AbstractTemplateEngine.preProcess(com.nomagic.magicreport.Template)</code></a></li>
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
<section class="detail" id="handleForPage(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleForPage</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleForPage</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                      throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #forpage directive.</div>
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
<dt>Parameters:</dt>
<dd><code>template</code> - Template source.</dd>
<dd><code>inProcessBuffer</code> - in process buffer.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when error while translation, or syntax not recognized.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="handleImport(com.nomagic.magicreport.Template,java.lang.StringBuilder)">
<h3>handleImport</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">handleImport</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span>
                     throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Handle the #include directive.</div>
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
<section class="detail" id="trimTrailSpace(int,java.lang.StringBuilder)">
<h3>trimTrailSpace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">trimTrailSpace</span><wbr/><span class="parameters">(int currentEndCursor,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/StringBuilder.html" title="class or interface in java.lang">StringBuilder</a> inProcessBuffer)</span></div>
<div class="block">Calculate and return the new cursor at the end of #hash statement after trim.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>currentEndCursor</code> - current end statement cursor</dd>
<dd><code>inProcessBuffer</code> - in process buffer</dd>
<dt>Returns:</dt>
<dd>new cursor at the end of #hash statement</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createComment(java.lang.String)">
<h3>createComment</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createComment</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> message)</span></div>
<div class="block">Return a formatted comment from given message. The default comment format return from this method is "# {0}"
 where {0} is message;</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>message</code> - message to put in document comment</dd>
<dt>Returns:</dt>
<dd>comment</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="process(com.nomagic.magicreport.Template)">
<h3>process</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">process</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
             throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Process a template. By default this method will call velocity engine to renders the input reader using the
 context into the output writer.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template)">process</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - template being evaluated.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template)"><code>AbstractTemplateEngine.process(com.nomagic.magicreport.Template)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>process</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">process</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</span>
             throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Process a template. By default this method will call velocity engine to renders the input reader using the
 context into the output writer.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">process</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - template being evaluated.</dd>
<dd><code>parentEngine</code> - an engine to shared a runtime instance for evaluate</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../AbstractTemplateEngine.html#process(com.nomagic.magicreport.Template)"><code>AbstractTemplateEngine.process(com.nomagic.magicreport.Template)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWriterForEvaluate(com.nomagic.magicreport.Template)">
<h3>setWriterForEvaluate</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html" title="class or interface in java.io">BufferedWriter</a></span> <span class="element-name">setWriterForEvaluate</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span></div>
</section>
</li>
<li>
<section class="detail" id="postProcess(com.nomagic.magicreport.Template)">
<h3>postProcess</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">postProcess</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                    throws <span class="exceptions"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Perform a post-processing after the template has been evaluated. This process just copy output file directly
 from processing location to final output.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#postProcess(com.nomagic.magicreport.Template)">postProcess</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
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
<li><a href="../AbstractTemplateEngine.html#postProcess(com.nomagic.magicreport.Template)"><code>AbstractTemplateEngine.postProcess(com.nomagic.magicreport.Template)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.MethodInvocationException)">
<h3>processVelocityException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span> <span class="element-name">processVelocityException</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 org.apache.velocity.exception.MethodInvocationException e)</span></div>
<div class="block">Call this method to process an Velocity exception and return in new format (<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>). By
 default, we can't get a nice error message from Velocity (Velocity error message containing in plain text
 and not readable by non-programmer.) And velocity itself doesn't provide any mechanism to get an message
 from ParseErrorException. This method will format the error message, remove unstructured text from velocity
 message e.g. "of" (with out appending text)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template</dd>
<dd><code>e</code> - MethodInvocationException</dd>
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
<div class="block">Call this method to process an Velocity exception and return in new format (<a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>). By
 default, we can't get a nice error message from Velocity (Velocity error message containing in plain text
 and not readable by non-programmer.) And velocity itself doesn't provide any mechanism to get an message
 from ParseErrorException. This method will format the error message, remove unstructured text from velocity
 message e.g. "of" (with out appending text)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template</dd>
<dd><code>e</code> - Velocity exception</dd>
<dt>Returns:</dt>
<dd>TemplateException</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="processException(com.nomagic.magicreport.Template,com.nomagic.magicreport.ParseErrorException)">
<h3>processException</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="../../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span> <span class="element-name">processException</span><wbr/><span class="parameters">(<a href="../../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a> e)</span></div>
<div class="block">Call this method to process a <a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport"><code>ParseErrorException</code></a>. This method call internally by
 <a href="#postProcess(com.nomagic.magicreport.Template)"><code>postProcess(Template)</code></a>. If code was performed by Velocity (<a href="#process(com.nomagic.magicreport.Template)"><code>process(Template)</code></a>), uses method
 <a href="#processVelocityException(com.nomagic.magicreport.Template,org.apache.velocity.exception.ParseErrorException)"><code>processVelocityException(Template, org.apache.velocity.exception.ParseErrorException)</code></a>. By default
 this method try to calculate line number from <a href="../../ParseErrorException.html#getSource()"><code>ParseErrorException.getSource()</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template</dd>
<dd><code>e</code> - MagicReport parse error exception</dd>
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
<dt>Parameters:</dt>
<dd><code>content</code> - the input string</dd>
<dt>Returns:</dt>
<dd>number of line</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassLoader()">
<h3>getClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a></span> <span class="element-name">getClassLoader</span>()</div>
<div class="block">Returns the class loader for the engine. This method will return null in such implementations if this class
 was loaded by the application class loader.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IExtensionTemplateEngine.html#getClassLoader()">getClassLoader</a></code> in interface <code><a href="../IExtensionTemplateEngine.html" title="interface in com.nomagic.magicreport.engine">IExtensionTemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>the class loader that loaded the class or interface represented by this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClassLoader(java.lang.ClassLoader)">
<h3>setClassLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClassLoader</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/ClassLoader.html" title="class or interface in java.lang">ClassLoader</a> loader)</span></div>
<div class="block">Sets the class loader for this engine. The class loader must be set before a template is evaluated. This
 method allows the creator of the template to provide the appropriate class loader to code running in the
 template when loading classes and resources.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../IExtensionTemplateEngine.html#setClassLoader(java.lang.ClassLoader)">setClassLoader</a></code> in interface <code><a href="../IExtensionTemplateEngine.html" title="interface in com.nomagic.magicreport.engine">IExtensionTemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>loader</code> - Class loader for this engine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block">Called by the application or <a href="../../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.
 <p>
 A subclass of engine should override this method if it has any operation that it wants to perform before it
 is destroyed.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#destroy()">destroy</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#destroy()">destroy</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="abort()">
<h3>abort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">abort</span>()</div>
<div class="block">Call to abort Velocity context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ITemplateEngine.html#abort()">abort</a></code> in interface <code><a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Overrides:</dt>
<dd><code><a href="../AbstractTemplateEngine.html#abort()">abort</a></code> in class <code><a href="../AbstractTemplateEngine.html" title="class in com.nomagic.magicreport.engine">AbstractTemplateEngine</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResolvedSectionName(java.lang.String)">
<h3>getResolvedSectionName</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResolvedSectionName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sectionName)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearTools()">
<h3>clearTools</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearTools</span>()</div>
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
