# JAVA OPENAPI: ReportFileTool (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/magicreport/tools/ReportFileTool.html
- source_path: `com/nomagic/magicdraw/magicreport/tools/ReportFileTool.html`
- source_sha256: `7fabaa1d8bc3a42c456b6ff0c967652fb6ed3e2b1c2d326ab13dafb7c007140d`
- captured_utc: `2026-07-14T16:55:23.090094+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.magicreport.tools](package-summary.html)

## Class ReportFileTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
com.nomagic.magicreport.engine.Tool
com.nomagic.magicreport.engine.ConcurrentTool
com.nomagic.magicreport.engine.tools.FileTool
com.nomagic.magicdraw.magicreport.tools.ReportFileTool

All Implemented Interfaces:
`com.nomagic.magicreport.engine.ITool`, `com.nomagic.magicreport.IVariable`, `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classReportFileTool
extends com.nomagic.magicreport.engine.tools.FileTool

See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ReportFileTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.ConcurrentTool
`com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject`
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool
`com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Fields inherited from class com.nomagic.magicreport.engine.Tool
`context, properties`
Fields inherited from interface com.nomagic.magicreport.engine.ITool
`VOID`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ReportFileTool](#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine))(com.nomagic.magicreport.engine.ITemplateEngine engine)`
Constructor
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[copy](#copy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Copy the file that is extracted from attached file element to output file in binary format.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[copy](#copy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName)`
Copy the file that is extracted from attached file element to output file in binary format.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[create](#create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element. 

 No import context object
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[create](#create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)`
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[create](#create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)`
Generate the report output from given attached file element.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) contextName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.util.Map))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> context)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Map))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> context)`
Invoke a new template engine to generate a report and return the path to output file.
`com.nomagic.magicreport.engine.ITool.Void`
`[silentCreate](#silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element.
`com.nomagic.magicreport.engine.ITool.Void`
`[silentCreate](#silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)`
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element.
`com.nomagic.magicreport.engine.ITool.Void`
`[silentCreate](#silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)`
Generate the report output from given attached file element.
Methods inherited from class com.nomagic.magicreport.engine.tools.FileTool
`computeName, computeName, consume, copy, copy, copy, copy, copy, copy, create, create, create, create, create, create, create, create, create, create, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createDir, exists, getResultPath, isEmpty, resolveOutputFileName, silentCreate, silentCreate, silentCreate, silentCreate, silentCreate, silentCreate, silentCreate`
Methods inherited from class com.nomagic.magicreport.engine.ConcurrentTool
`destroy, getCustomPoolSize, isNoSpaceException, isRunning, offer`
Methods inherited from class com.nomagic.magicreport.engine.Tool
`clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.ITool
`clearTool`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ReportFileTool.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ReportFileTool
public ReportFileTool(com.nomagic.magicreport.engine.ITemplateEngine engine)
Constructor
Parameters:
`engine` - template engine
 ============ METHOD DETAIL ========== 
Method Details
silentCreate
public com.nomagic.magicreport.engine.ITool.Void silentCreate([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws com.nomagic.magicreport.ParseErrorException
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element.
 For example: `$file.silentCreate($anAttachedFileElement)`
Parameters:
`element` - an AttachedFile element
Returns:
void
Throws:
`com.nomagic.magicreport.ParseErrorException` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
public com.nomagic.magicreport.engine.ITool.Void silentCreate([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)
 throws com.nomagic.magicreport.ParseErrorException
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element.
 
 For example: `$file.silentCreate($anAttachedFileElement,'')`
If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`element` - an AttachedFile element
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
void
Throws:
`com.nomagic.magicreport.ParseErrorException` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
public com.nomagic.magicreport.engine.ITool.Void silentCreate([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)
 throws com.nomagic.magicreport.ParseErrorException
Generate the report output from given attached file element.
 For example: `$file.silentCreate($anAttachedFileElement,'overview.html','')`
If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`element` - an AttachedFile element
`outputFileName` - the output file name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
void
Throws:
`com.nomagic.magicreport.ParseErrorException` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) create([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws com.nomagic.magicreport.ParseErrorException
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element. 

 No import context object
 
 For example: `<a href="$file.create($anAttachedFileElement)">attachedFile.html</a>`
Parameters:
`element` - an AttachedFile element
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`com.nomagic.magicreport.ParseErrorException` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) create([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)
 throws com.nomagic.magicreport.ParseErrorException
A shortcut to create file from specific element. 

 The output filename is same the extracted file name from attached element.
 
 For example: `<a href="$file.create($anAttachedFileElement,'')">attachedFile.html</a>`
If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`element` - an AttachedFile element
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`com.nomagic.magicreport.ParseErrorException` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) create([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) importObject)
 throws com.nomagic.magicreport.ParseErrorException
Generate the report output from given attached file element.
 For example: `<a href="$file.create($anAttachedFileElement,'attachedFile.html','')">attachedFile.html</a>`
If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`element` - an AttachedFile element
`outputFileName` - the output file name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`com.nomagic.magicreport.ParseErrorException` - when template has a syntax or other error which prevents it from being parsed.
copy
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) copy([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Copy the file that is extracted from attached file element to output file in binary format.
 For example: `<img src="$file.copy($anAttachedFileElement)">`
Parameters:
`element` - an AttachedFile element
Returns:
the output pathname. It will return empty string, if there is any error.
copy
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) copy([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName)
Copy the file that is extracted from attached file element to output file in binary format.
 For example: `<img src="$file.copy($anAttachedFileElement,'icon.gif')">`
Parameters:
`element` - an AttachedFile element
`outputFileName` - the output filename
Returns:
the output pathname. It will return empty string, if there is any error.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createAndWait([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by the extracted file from attached element.
Parameters:
`element` - an AttachedFile element
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createAndWait([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by the extracted file from attached element.
Parameters:
`element` - an AttachedFile element
`contextValue` - additional object adding to new template context with default $importer name.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createAndWait([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file.
 "importer" will be used as a name of context value.
Parameters:
`element` - an AttachedFile element
`outputFileName` - an output report file name.
`contextValue` - additional object adding to new template context with default $importer name.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createAndWait([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) contextName,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file.
Parameters:
`element` - an AttachedFile element
`outputFileName` - an output report file name.
`contextName` - adding object context's name.
`contextValue` - additional object adding to new template context.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createAndWait([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> context)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.
Parameters:
`templateFile` - an input template file.
`context` - additional context adding to new template.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createAndWait([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) outputFileName,
 [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)> context)
Invoke a new template engine to generate a report and return the path to output file.
Parameters:
`element` - an AttachedFile element
`outputFileName` - an output report file name.
`context` - additional context adding to new template.
Returns:
an absolute path to output file.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.magicreport.tools</a></div>
<h1 class="title" title="Class ReportFileTool">Class ReportFileTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance">com.nomagic.magicreport.engine.Tool
<div class="inheritance">com.nomagic.magicreport.engine.ConcurrentTool
<div class="inheritance">com.nomagic.magicreport.engine.tools.FileTool
<div class="inheritance">com.nomagic.magicdraw.magicreport.tools.ReportFileTool</div>
</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicreport.engine.ITool</code>, <code>com.nomagic.magicreport.IVariable</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ReportFileTool</span>
<span class="extends-implements">extends com.nomagic.magicreport.engine.tools.FileTool</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicdraw.magicreport.tools.ReportFileTool">Serialized Form</a></li>
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
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ConcurrentTool">Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.ConcurrentTool</h2>
<code>com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject</code></div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.ITool</h2>
<code>com.nomagic.magicreport.engine.ITool.HTMLString, com.nomagic.magicreport.engine.ITool.RetainedString, com.nomagic.magicreport.engine.ITool.Void</code></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>context, properties</code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>VOID</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine)">ReportFileTool</a><wbr/>(com.nomagic.magicreport.engine.ITemplateEngine engine)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">copy</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy the file that is extracted from attached file element to output file in binary format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">copy</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy the file that is extracted from attached file element to output file in binary format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">create</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.<br/>
 No import context object</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">create</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object)">create</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output from given attached file element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createAndWait</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">createAndWait</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object)">createAndWait</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.Object)">createAndWait</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contextName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.util.Map)">createAndWait</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Map)">createAndWait</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.engine.ITool.Void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">silentCreate</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.engine.ITool.Void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">silentCreate</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>com.nomagic.magicreport.engine.ITool.Void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object)">silentCreate</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output from given attached file element.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.tools.FileTool">Methods inherited from class com.nomagic.magicreport.engine.tools.FileTool</h3>
<code>computeName, computeName, consume, copy, copy, copy, copy, copy, copy, create, create, create, create, create, create, create, create, create, create, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createAndWait, createDir, exists, getResultPath, isEmpty, resolveOutputFileName, silentCreate, silentCreate, silentCreate, silentCreate, silentCreate, silentCreate, silentCreate</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ConcurrentTool">Methods inherited from class com.nomagic.magicreport.engine.ConcurrentTool</h3>
<code>destroy, getCustomPoolSize, isNoSpaceException, isRunning, offer</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.Tool</h3>
<code>clone, getContext, getProperties, getProperty, getProperty, notifyObservers, setContext, setProperties</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.ITool</h3>
<code>clearTool</code></div>
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
<section class="detail" id="CONTEXT_NAME">
<h3>CONTEXT_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTEXT_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.magicreport.tools.ReportFileTool.CONTEXT_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>ReportFileTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ReportFileTool</span><wbr/><span class="parameters">(com.nomagic.magicreport.engine.ITemplateEngine engine)</span></div>
<div class="block">Constructor</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - template engine</dd>
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
<section class="detail" id="silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.engine.ITool.Void</span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                                                       throws <span class="exceptions">com.nomagic.magicreport.ParseErrorException</span></div>
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.
 <p>
 For example: <code><pre>
    $file.silentCreate($anAttachedFileElement)
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.magicreport.ParseErrorException</code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.engine.ITool.Void</span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
                                                       throws <span class="exceptions">com.nomagic.magicreport.ParseErrorException</span></div>
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.
 
 <p>
 For example: <code><pre>
    $file.silentCreate($anAttachedFileElement,'')
 </pre></code>
<p>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.magicreport.ParseErrorException</code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">com.nomagic.magicreport.engine.ITool.Void</span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
                                                       throws <span class="exceptions">com.nomagic.magicreport.ParseErrorException</span></div>
<div class="block">Generate the report output from given attached file element.
 <p>
 For example: <code><pre>
    $file.silentCreate($anAttachedFileElement,'overview.html','')
 </pre></code>
<p>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>outputFileName</code> - the output file name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.magicreport.ParseErrorException</code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
              throws <span class="exceptions">com.nomagic.magicreport.ParseErrorException</span></div>
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.<br/>
 No import context object
 
 <p>
 For example: <code><pre>
    &lt;a href="$file.create($anAttachedFileElement)"&gt;attachedFile.html&lt;/a&gt;
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.magicreport.ParseErrorException</code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
              throws <span class="exceptions">com.nomagic.magicreport.ParseErrorException</span></div>
<div class="block">A shortcut to create file from specific element.<br/>
 The output filename is same the extracted file name from attached element.
 
 <p>
 For example: <code><pre>
    &lt;a href="$file.create($anAttachedFileElement,'')"&gt;attachedFile.html&lt;/a&gt;
 </pre></code>
<p>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.magicreport.ParseErrorException</code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
              throws <span class="exceptions">com.nomagic.magicreport.ParseErrorException</span></div>
<div class="block">Generate the report output from given attached file element.
 <p>
 For example: <code><pre>
    &lt;a href="$file.create($anAttachedFileElement,'attachedFile.html','')"&gt;attachedFile.html&lt;/a&gt;
 </pre></code>
<p>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>outputFileName</code> - the output file name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code>com.nomagic.magicreport.ParseErrorException</code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Copy the file that is extracted from attached file element to output file in binary format.
 <p>
 For example: <code><pre>
   &lt;img src="$file.copy($anAttachedFileElement)"&gt;
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName)</span></div>
<div class="block">Copy the file that is extracted from attached file element to output file in binary format.
 <p>
 For example: <code><pre>
   &lt;img src="$file.copy($anAttachedFileElement,'icon.gif')"&gt;
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>outputFileName</code> - the output filename</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by the extracted file from attached element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by the extracted file from attached element.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>contextValue</code> - additional object adding to new template context with default $importer name.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.
 <p>
 "importer" will be used as a name of context value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context with default $importer name.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.lang.String,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contextName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>contextName</code> - adding object context's name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.Map)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - an input template file.</dd>
<dd><code>context</code> - additional context adding to new template.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,java.util.Map)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - an AttachedFile element</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>context</code> - additional context adding to new template.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
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
