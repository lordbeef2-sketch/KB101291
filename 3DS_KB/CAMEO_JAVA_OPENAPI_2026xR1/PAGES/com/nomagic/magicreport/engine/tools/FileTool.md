# JAVA OPENAPI: FileTool (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/tools/FileTool.html
- source_path: `com/nomagic/magicreport/engine/tools/FileTool.html`
- source_sha256: `7e591bc09c9ba30d43edb7a3a4c82121492684ccf1f5114ed999d011d952d9bd`
- captured_utc: `2026-07-14T16:46:12.957973+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Class FileTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../Tool.html)
[com.nomagic.magicreport.engine.ConcurrentTool](../ConcurrentTool.html)
com.nomagic.magicreport.engine.tools.FileTool

All Implemented Interfaces:
`[ITool](../ITool.html)`, `[IVariable](../../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

Direct Known Subclasses:
`[ReportFileTool](../../../magicdraw/magicreport/tools/ReportFileTool.html)`

@OpenApiAllpublic classFileTool
extends [ConcurrentTool](../ConcurrentTool.html)

This class enables to generate output report file in the template file.

Since:
Jul 2, 2007
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.FileTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.[ConcurrentTool](../ConcurrentTool.html)
`[ConcurrentTool.ConsumeObject](../ConcurrentTool.ConsumeObject.html)`
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[ITool.HTMLString](../ITool.HTMLString.html), [ITool.RetainedString](../ITool.RetainedString.html), [ITool.Void](../ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[CONTEXT_NAME](#CONTEXT_NAME)`
Contains a context name.
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../Tool.html)
`[context](../Tool.html#context), [properties](../Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[VOID](../ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FileTool](#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](../ITemplateEngine.html) engine)`
Create a file tool with default global engine.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[computeName](#computeName(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) directory,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Create pathname string from given directory, name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[computeName](#computeName(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) directory,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileType)`
Create pathname string from given directory, name, and file type.
`void`
`[consume](#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))([ConcurrentTool.ConsumeObject](../ConcurrentTool.ConsumeObject.html) consumeObject)`
Consumes this object so that it will be processed in the default manner.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[copy](#copy(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) inputFile)`
Copy an input file to output file with the same name in binary format.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[copy](#copy(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) inputFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile)`
Copy an input file to output file in binary format.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[copy](#copy(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) inputFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName)`
Copy an input file to output file in binary format.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[copy](#copy(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) inputFileName)`
Copy an input file to output file with the same name in binary format.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[copy](#copy(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) inputFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName)`
Copy an input file to output file in binary format.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)>`
`[copy](#copy(java.util.Map))([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fileMap)`

`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)`
A shortcut to create file which output filename is same as a name of template file and no import context object.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.io.File,java.io.File,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importedObject)`
Generate the report output by using the template file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.io.File,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
A shortcut to create file which output filename is same as a name of template file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.io.File,java.lang.String,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
Generate the report output from given template file.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.io.File,java.lang.String,java.lang.String,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputDir,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importedObject)`
Generate the report output by using the template file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template)`
A shortcut to create file which output filename is template name and no import context object.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
A shortcut to create file which output filename is template name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
Generate the report output from given template name.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.lang.String,java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputname,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
Deprecated.
see [`create(String, String, Object)`](#create(java.lang.String,java.lang.String,java.lang.Object))
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[create](#create(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateDir,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputDir,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importedObject)`
Generate the report output by using the template file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)`
Invoke a new template engine to generate a report and return the path to output file.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.io.File,java.io.File,java.util.Map))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.io.File,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.io.File,java.lang.String,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.io.File,java.lang.String,java.lang.String,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) contextName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.io.File,java.lang.String,java.util.Map))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.io.File,java.util.Map))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.lang.String,java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) contextName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.lang.String,java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)`
Invoke a new template engine to generate a report and return the path to output file.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[createAndWait](#createAndWait(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)`
Invoke a new template engine to generate a report and return the path to output file.
`protected void`
`[createDir](#createDir(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputDirectory)`
Create directory
`boolean`
`[exists](#exists(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pathname)`
Tests whether the file denoted by `pathname` exists.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getResultPath](#getResultPath(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resultFromProcess,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) originalPath)`
Get result path.
`protected boolean`
`[isEmpty](#isEmpty(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`
Check null object or empty string.
`protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[resolveOutputFileName](#resolveOutputFileName(java.lang.String,java.lang.String,java.io.File))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)`
Sometime the name of real template file is not match to original template file name. 

 In case user does not specify output file name, we cannot assign the templateFileName to be outputFileName without checking. 

 e.g., templateFileName = "mdp://attachedFile#_1234" 

 templateFile = C://tmp//test.docx 

 So, outputFileName should be 'test.docx' not 'mdp://attachedFile#_1234'
`[ITool.Void](../ITool.Void.html)`
`[silentCreate](#silentCreate(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)`
A shortcut to create file which output filename is same as a name of input template file and no import context object.
`[ITool.Void](../ITool.Void.html)`
`[silentCreate](#silentCreate(java.io.File,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
A shortcut to create file which output filename is same as a name of input template file.
`[ITool.Void](../ITool.Void.html)`
`[silentCreate](#silentCreate(java.io.File,java.lang.String,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
Generate the report output from given template file.
`[ITool.Void](../ITool.Void.html)`
`[silentCreate](#silentCreate(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template)`
A shortcut to create file which output filename is template name and no import context object.
`[ITool.Void](../ITool.Void.html)`
`[silentCreate](#silentCreate(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
A shortcut to create file which output filename is template name.
`[ITool.Void](../ITool.Void.html)`
`[silentCreate](#silentCreate(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
Generate the report output from given template name.
`[ITool.Void](../ITool.Void.html)`
`[silentCreate](#silentCreate(java.lang.String,java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputname,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)`
Deprecated.
Sees [`silentCreate(String, String, Object)`](#silentCreate(java.lang.String,java.lang.String,java.lang.Object))
Methods inherited from class com.nomagic.magicreport.engine.[ConcurrentTool](../ConcurrentTool.html)
`[destroy](../ConcurrentTool.html#destroy()), [getCustomPoolSize](../ConcurrentTool.html#getCustomPoolSize()), [isNoSpaceException](../ConcurrentTool.html#isNoSpaceException(java.lang.Exception)), [isRunning](../ConcurrentTool.html#isRunning()), [offer](../ConcurrentTool.html#offer(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))`
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../Tool.html)
`[clone](../Tool.html#clone()), [getContext](../Tool.html#getContext()), [getProperties](../Tool.html#getProperties()), [getProperty](../Tool.html#getProperty(java.lang.String)), [getProperty](../Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../Tool.html#notifyObservers(java.lang.Object)), [setContext](../Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../ITool.html)
`[clearTool](../ITool.html#clearTool())`

============ FIELD DETAIL =========== 
Field Details
CONTEXT_NAME
public static final [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) CONTEXT_NAME
Contains a context name.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.FileTool.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FileTool
public FileTool([ITemplateEngine](../ITemplateEngine.html) engine)
Create a file tool with default global engine.
Parameters:
`engine` - default global engine
 ============ METHOD DETAIL ========== 
Method Details
silentCreate
public [ITool.Void](../ITool.Void.html) silentCreate([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is template name and no import context object.
 For example: `$file.silentCreate('overview.html')`
Parameters:
`template` - the input template name
Returns:
void
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
public [ITool.Void](../ITool.Void.html) silentCreate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is same as a name of input template file and no import context object.
 

 For example: `$file.silentCreate($iFile)`
Parameters:
`templateFile` - the input template file
Returns:
void
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
public [ITool.Void](../ITool.Void.html) silentCreate([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is template name.
 

 For example: `$file.silentCreate('overview.html','')`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`template` - the input template name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
void
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
public [ITool.Void](../ITool.Void.html) silentCreate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is same as a name of input template file.
 

 For example: `$file.silentCreate($iFile,'')`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`templateFile` - the input template file
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
void
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
public [ITool.Void](../ITool.Void.html) silentCreate([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Generate the report output from given template name.
 

 For example: `$file.silentCreate('overview.html','overview.html','')`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`template` - the input template name
`outputFileName` - the output file name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
void
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
public [ITool.Void](../ITool.Void.html) silentCreate([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Generate the report output from given template file.
 

 For example: `$file.silentCreate($iFile,'overview.html','')`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`templateFile` - the input template file
`outputFileName` - the output file name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
void
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
silentCreate
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [ITool.Void](../ITool.Void.html) silentCreate([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputname,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Deprecated.
Sees [`silentCreate(String, String, Object)`](#silentCreate(java.lang.String,java.lang.String,java.lang.Object))
Generate the report output from given template name.
 

 For example: `$file.silentCreate('html','overview','overview','')`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`templateType` - the template type such rtf, html, htm.
`template` - the input pathname string without extension
`outputname` - the output file name, not include any extension.
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
void
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is template name and no import context object.
 

 For example: `<a href="$file.create('overview.html')">overview.html</a>`
Parameters:
`template` - the input template name
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is same as a name of template file and no import context object.
 

 For example: `<a href="$file.create($aFile)">overview.html</a>`
Parameters:
`templateFile` - the input template file
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is template name.
 

 For example: `<a href="$file.create('overview.html','')">overview.html</a>`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`template` - the input template name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
A shortcut to create file which output filename is same as a name of template file.
 

 For example: `<a href="$file.create($iFile,'')">overview.html</a>`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`templateFile` - the input template file
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Generate the report output from given template name.
 

 For example: `<a href="$file.create('overview.html','overview.html','')">overview.html</a>`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`templateFileName` - the input template file name
`outputFileName` - the output file name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Generate the report output from given template file.
 

 For example: `<a href="$file.create($iFile,'overview.html','')">overview.html</a>`
 

 If `importObject` is an instance of `java.util.Map`, key-value of Map will be used as
 name-value of context.
Parameters:
`templateFile` - the input template file
`outputFileName` - the output file name
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateType,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) template,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputname,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Deprecated.
see [`create(String, String, Object)`](#create(java.lang.String,java.lang.String,java.lang.Object))
Generate the report output from given template name.
 

 For example: `<a href="$file.create('html','overview','overview','')">overview.html</a>`
Parameters:
`templateType` - the template type such rtf, html, htm.
`template` - the input pathname string without extension
`outputname` - the output file name, not include any extension.
`importObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateDir,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputDir,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importedObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Generate the report output by using the template file.
Parameters:
`templateDir` - the directory of the template.
`templateFileName` - the template file name.
`outputDir` - the directory of the output report.
`outputFileName` - the output file name, not include any extension.
`importedObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputDir,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importedObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Generate the report output by using the template file.
Parameters:
`templateFile` - the template file.
`outputDir` - the directory of the output report.
`outputFileName` - the output file name, not include any extension.
`importedObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
create
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) create([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) importedObject)
 throws [ParseErrorException](../../ParseErrorException.html)
Generate the report output by using the template file.
Parameters:
`templateFile` - the template file.
`outputFile` - the output file.
`importedObject` - the object reference, which will be DefaultElement in the template file. You can use
 DefaultElement variable in the template file for getting the data.
Returns:
the output pathname. It will return empty string, if there is any error.
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - when template has a syntax or other error which prevents it from being parsed.
consume
public void consume([ConcurrentTool.ConsumeObject](../ConcurrentTool.ConsumeObject.html) consumeObject)
Consumes this object so that it will be processed in the default manner.
Specified by:
`[consume](../ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))` in class `[ConcurrentTool](../ConcurrentTool.html)`
Parameters:
`consumeObject` - consume object
See Also:
[`ConcurrentTool.consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)`](../ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject))
copy
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) copy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) inputFileName)
Copy an input file to output file with the same name in binary format.
 

 For example: `<img src="$file.copy('icon.gif')">`
Parameters:
`inputFileName` - the input filename
Returns:
the output pathname. It will return empty string, if there is any error.
copy
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) copy([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) inputFile)
Copy an input file to output file with the same name in binary format.
 

 For example: `<img src="$file.copy($iFile)">`
Parameters:
`inputFile` - the input file
Returns:
the output pathname. It will return empty string, if there is any error.
copy
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> copy([Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> fileMap)
copy
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) copy([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) inputFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName)
Copy an input file to output file in binary format.
 

 For example: `<img src="$file.copy('icon.gif','icon.gif')">`
Parameters:
`inputFileName` - the input filename
`outputFileName` - the output filename
Returns:
the output pathname. It will return empty string, if there is any error.
copy
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) copy([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) inputFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName)
Copy an input file to output file in binary format.
 

 For example: `<img src="$file.copy($iconFile,'icon.gif')">`
Parameters:
`inputFile` - the input file
`outputFileName` - the output filename
Returns:
the output pathname. It will return empty string, if there is any error.
copy
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) copy([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) inputFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile)
Copy an input file to output file in binary format.
 

 For example: `<img src="$file.copy($iIcon, $oIcon)">`
Parameters:
`inputFile` - the input file
`outputFile` - the output file
Returns:
the output pathname. It will return empty string, if there is any error.
exists
public boolean exists([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pathname)
Tests whether the file denoted by `pathname` exists. By default, current directory will be
 referred to template location.
 

 For example: `$file.exists("$template.resourcesLocation/myimage.png")
 $file.exists("C:/myfolder/myimage.png")
 $file.exists("mytemplate.txt")`
Parameters:
`pathname` - A pathname string
Returns:
`true` if and only if the file or directory denoted by this name exists;
 `false` otherwise
computeName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) computeName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) directory,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Create pathname string from given directory, name.
Parameters:
`directory` - a parent directory of file
`name` - a name of file (exclude extension)
Returns:
pathname from given directory, name.
computeName
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) computeName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) directory,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileType)
Create pathname string from given directory, name, and file type.
Parameters:
`directory` - a parent directory of file
`name` - a name of file (exclude extension)
`fileType` - type of file. e.g. rtf, txt, html
Returns:
pathname string to filename
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.
Parameters:
`templateFileName` - an input template file name.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.
Parameters:
`templateFile` - an input template file.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.
Parameters:
`templateFileName` - an input template file name.
`contextValue` - additional object adding to new template context with default $importer name.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.
Parameters:
`templateFile` - an input template file name.
`contextValue` - additional object adding to new template context with default $importer name.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file.
 "importer" will be used as a name of context value.
Parameters:
`templateFileName` - an input template file name.
`outputFileName` - an output report file name.
`contextValue` - additional object adding to new template context with default $importer name.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file.
 "importer" will be used as a name of context value.
Parameters:
`templateFile` - an input template file.
`outputFileName` - an output report file name.
`contextValue` - additional object adding to new template context with default $importer name.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) contextName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file.
Parameters:
`templateFileName` - an input template file name.
`outputFileName` - an output report file name.
`contextName` - adding object context's name.
`contextValue` - additional object adding to new template context.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) contextName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) contextValue)
Invoke a new template engine to generate a report and return the path to output file.
Parameters:
`templateFile` - an input template file.
`outputFileName` - an output report file name.
`contextName` - adding object context's name.
`contextValue` - additional object adding to new template context.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.
Parameters:
`templateFileName` - an input template file name.
`context` - additional context adding to new template.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)
Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.
Parameters:
`templateFile` - an input template file.
`context` - additional context adding to new template.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)
Invoke a new template engine to generate a report and return the path to output file.
Parameters:
`templateFileName` - an input template file name.
`outputFileName` - an output report file name.
`context` - additional context adding to new template.
Returns:
an absolute path to output file.
createAndWait
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)
Invoke a new template engine to generate a report and return the path to output file.
Parameters:
`templateFile` - an input template file.
`outputFileName` - an output report file name.
`context` - additional context adding to new template.
Returns:
an absolute path to output file.
createAndWait
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) createAndWait([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputFile,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> context)
Invoke a new template engine to generate a report and return the path to output file.
Parameters:
`templateFile` - an input template file.
`outputFile` - an output report file.
`context` - additional context adding to new template.
Returns:
an absolute path to output file.
isEmpty
protected boolean isEmpty([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Check null object or empty string.
Parameters:
`obj` - object to check
Returns:
true if specific object is null or empty string.
getResultPath
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getResultPath([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resultFromProcess,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) originalPath)
Get result path.
 If result is empty, return original path
Parameters:
`resultFromProcess` - path from process
`originalPath` - specific output file name
Returns:
result path
createDir
protected void createDir([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) outputDirectory)
Create directory
Parameters:
`outputDirectory` - directory path
resolveOutputFileName
protected [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) resolveOutputFileName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) outputFileName,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) templateFile)
Sometime the name of real template file is not match to original template file name. 

 In case user does not specify output file name, we cannot assign the templateFileName to be outputFileName without checking. 

 e.g., templateFileName = "mdp://attachedFile#_1234" 

 templateFile = C://tmp//test.docx 

 So, outputFileName should be 'test.docx' not 'mdp://attachedFile#_1234'
Parameters:
`templateFileName` - original template file name
`outputFileName` - original output file name
`templateFile` - real template file
Returns:
outputFileName

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Class FileTool">Class FileTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance"><a href="../ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.ConcurrentTool</a>
<div class="inheritance">com.nomagic.magicreport.engine.tools.FileTool</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="../../../magicdraw/magicreport/tools/ReportFileTool.html" title="class in com.nomagic.magicdraw.magicreport.tools">ReportFileTool</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FileTool</span>
<span class="extends-implements">extends <a href="../ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></span></div>
<div class="block">This class enables to generate output report file in the template file.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jul 2, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.FileTool">Serialized Form</a></li>
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
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ConcurrentTool">Nested classes/interfaces inherited from class com.nomagic.magicreport.engine.<a href="../ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></h2>
<code><a href="../ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a></code></div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONTEXT_NAME">CONTEXT_NAME</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains a context name.</div>
</div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../Tool.html#context">context</a>, <a href="../Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine)">FileTool</a><wbr/>(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a file tool with default global engine.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#computeName(java.lang.String,java.lang.String)">computeName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create pathname string from given directory, name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#computeName(java.lang.String,java.lang.String,java.lang.String)">computeName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create pathname string from given directory, name, and file type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">consume</a><wbr/>(<a href="../ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Consumes this object so that it will be processed in the default manner.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.File)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> inputFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy an input file to output file with the same name in binary format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.File,java.io.File)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> inputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy an input file to output file in binary format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.File,java.lang.String)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> inputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy an input file to output file in binary format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.lang.String)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inputFileName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy an input file to output file with the same name in binary format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.lang.String,java.lang.String)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Copy an input file to output file in binary format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.util.Map)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fileMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.io.File)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is same as a name of template file and no import context object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.io.File,java.io.File,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importedObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output by using the template file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.io.File,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is same as a name of template file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.io.File,java.lang.String,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output from given template file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.io.File,java.lang.String,java.lang.String,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importedObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output by using the template file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is template name and no import context object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is template name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.String,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output from given template name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputname,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">see <a href="#create(java.lang.String,java.lang.String,java.lang.Object)"><code>create(String, String, Object)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importedObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output by using the template file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.io.File)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.io.File,java.io.File,java.util.Map)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.io.File,java.lang.Object)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.io.File,java.lang.String,java.lang.Object)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.io.File,java.lang.String,java.lang.String,java.lang.Object)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contextName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.io.File,java.lang.String,java.util.Map)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.io.File,java.util.Map)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.lang.String)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.lang.String,java.lang.Object)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.lang.String,java.lang.String,java.lang.Object)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contextName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.lang.String,java.lang.String,java.util.Map)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createAndWait(java.lang.String,java.util.Map)">createAndWait</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createDir(java.io.File)">createDir</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputDirectory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Create directory</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#exists(java.lang.String)">exists</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathname)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests whether the file denoted by <code>pathname</code> exists.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getResultPath(java.lang.String,java.lang.String)">getResultPath</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resultFromProcess,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> originalPath)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get result path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEmpty(java.lang.Object)">isEmpty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check null object or empty string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#resolveOutputFileName(java.lang.String,java.lang.String,java.io.File)">resolveOutputFileName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sometime the name of real template file is not match to original template file name.<br/>
 In case user does not specify output file name, we cannot assign the templateFileName to be outputFileName without checking.<br/>
 e.g., templateFileName = "mdp://attachedFile#_1234" <br/>
 templateFile = C://tmp//test.docx <br/>
 So, outputFileName should be 'test.docx' not 'mdp://attachedFile#_1234'<br/></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(java.io.File)">silentCreate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is same as a name of input template file and no import context object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(java.io.File,java.lang.Object)">silentCreate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is same as a name of input template file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(java.io.File,java.lang.String,java.lang.Object)">silentCreate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output from given template file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(java.lang.String)">silentCreate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is template name and no import context object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(java.lang.String,java.lang.Object)">silentCreate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A shortcut to create file which output filename is template name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#silentCreate(java.lang.String,java.lang.String,java.lang.Object)">silentCreate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generate the report output from given template name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#silentCreate(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">silentCreate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputname,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Sees <a href="#silentCreate(java.lang.String,java.lang.String,java.lang.Object)"><code>silentCreate(String, String, Object)</code></a></div>
</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ConcurrentTool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></h3>
<code><a href="../ConcurrentTool.html#destroy()">destroy</a>, <a href="../ConcurrentTool.html#getCustomPoolSize()">getCustomPoolSize</a>, <a href="../ConcurrentTool.html#isNoSpaceException(java.lang.Exception)">isNoSpaceException</a>, <a href="../ConcurrentTool.html#isRunning()">isRunning</a>, <a href="../ConcurrentTool.html#offer(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">offer</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../Tool.html#clone()">clone</a>, <a href="../Tool.html#getContext()">getContext</a>, <a href="../Tool.html#getProperties()">getProperties</a>, <a href="../Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../ITool.html#clearTool()">clearTool</a></code></div>
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
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONTEXT_NAME</span></div>
<div class="block">Contains a context name.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.FileTool.CONTEXT_NAME">Constant Field Values</a></li>
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
<h3>FileTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FileTool</span><wbr/><span class="parameters">(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> engine)</span></div>
<div class="block">Create a file tool with default global engine.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - default global engine</dd>
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
<section class="detail" id="silentCreate(java.lang.String)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is template name and no import context object.
 <p>
 For example: <pre><code>
    $file.silentCreate('overview.html')
 </code></pre></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - the input template name</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(java.io.File)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is same as a name of input template file and no import context object.
 <br/>
 For example: <pre><code>
    $file.silentCreate($iFile)
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the input template file</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(java.lang.String,java.lang.Object)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is template name.
 <br/>
 For example: <pre><code>
    $file.silentCreate('overview.html','')
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - the input template name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(java.io.File,java.lang.Object)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is same as a name of input template file.
 <br/>
 For example: <pre><code>
    $file.silentCreate($iFile,'')
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the input template file</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(java.lang.String,java.lang.String,java.lang.Object)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Generate the report output from given template name.
 <br/>
 For example: <pre><code>
    $file.silentCreate('overview.html','overview.html','')
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - the input template name</dd>
<dd><code>outputFileName</code> - the output file name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(java.io.File,java.lang.String,java.lang.Object)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Generate the report output from given template file.
 <br/>
 For example: <pre><code>
    $file.silentCreate($iFile,'overview.html','')
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the input template file</dd>
<dd><code>outputFileName</code> - the output file name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="silentCreate(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">
<h3>silentCreate</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></span> <span class="element-name">silentCreate</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputname,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
                        throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Sees <a href="#silentCreate(java.lang.String,java.lang.String,java.lang.Object)"><code>silentCreate(String, String, Object)</code></a></div>
</div>
<div class="block">Generate the report output from given template name.
 <br/>
 For example: <pre><code>
    $file.silentCreate('html','overview','overview','')
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateType</code> - the template type such rtf, html, htm.</dd>
<dd><code>template</code> - the input pathname string without extension</dd>
<dd><code>outputname</code> - the output file name, not include any extension.</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>void</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template)</span>
              throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is template name and no import context object.
 <br/>
 For example: <pre><code>
    &lt;a href="$file.create('overview.html')"&gt;overview.html&lt;/a&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - the input template name</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.io.File)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</span>
              throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is same as a name of template file and no import context object.
 <br/>
 For example: <pre><code>
    &lt;a href="$file.create($aFile)"&gt;overview.html&lt;/a&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the input template file</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
              throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is template name.
 <br/>
 For example: <pre><code>
    &lt;a href="$file.create('overview.html','')"&gt;overview.html&lt;/a&gt;
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - the input template name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.io.File,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
              throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">A shortcut to create file which output filename is same as a name of template file.
 <br/>
 For example: <pre><code>
    &lt;a href="$file.create($iFile,'')"&gt;overview.html&lt;/a&gt;
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the input template file</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
              throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Generate the report output from given template name.
 <br/>
 For example: <pre><code>
    &lt;a href="$file.create('overview.html','overview.html','')"&gt;overview.html&lt;/a&gt;
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - the input template file name</dd>
<dd><code>outputFileName</code> - the output file name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.io.File,java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
              throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Generate the report output from given template file.
 <br/>
 For example: <pre><code>
    &lt;a href="$file.create($iFile,'overview.html','')"&gt;overview.html&lt;/a&gt;
 </code></pre>
<br/>
 If <code>importObject</code> is an instance of <code>java.util.Map</code>, key-value of Map will be used as
 name-value of context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the input template file</dd>
<dd><code>outputFileName</code> - the output file name</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> template,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputname,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importObject)</span>
              throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">see <a href="#create(java.lang.String,java.lang.String,java.lang.Object)"><code>create(String, String, Object)</code></a></div>
</div>
<div class="block">Generate the report output from given template name.
 <br/>
 For example: <pre><code>
    &lt;a href="$file.create('html','overview','overview','')"&gt;overview.html&lt;/a&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateType</code> - the template type such rtf, html, htm.</dd>
<dd><code>template</code> - the input pathname string without extension</dd>
<dd><code>outputname</code> - the output file name, not include any extension.</dd>
<dd><code>importObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importedObject)</span>
                 throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Generate the report output by using the template file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateDir</code> - the directory of the template.</dd>
<dd><code>templateFileName</code> - the template file name.</dd>
<dd><code>outputDir</code> - the directory of the output report.</dd>
<dd><code>outputFileName</code> - the output file name, not include any extension.</dd>
<dd><code>importedObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.io.File,java.lang.String,java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importedObject)</span>
                 throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Generate the report output by using the template file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the template file.</dd>
<dd><code>outputDir</code> - the directory of the output report.</dd>
<dd><code>outputFileName</code> - the output file name, not include any extension.</dd>
<dd><code>importedObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.io.File,java.io.File,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> importedObject)</span>
                 throws <span class="exceptions"><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></span></div>
<div class="block">Generate the report output by using the template file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - the template file.</dd>
<dd><code>outputFile</code> - the output file.</dd>
<dd><code>importedObject</code> - the object reference, which will be DefaultElement in the template file. You can use
           DefaultElement variable in the template file for getting the data.</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - when template has a syntax or other error which prevents it from being parsed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">
<h3>consume</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">consume</span><wbr/><span class="parameters">(<a href="../ConcurrentTool.ConsumeObject.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool.ConsumeObject</a> consumeObject)</span></div>
<div class="block">Consumes this object so that it will be processed in the default manner.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)">consume</a></code> in class <code><a href="../ConcurrentTool.html" title="class in com.nomagic.magicreport.engine">ConcurrentTool</a></code></dd>
<dt>Parameters:</dt>
<dd><code>consumeObject</code> - consume object</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="../ConcurrentTool.html#consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)"><code>ConcurrentTool.consume(com.nomagic.magicreport.engine.ConcurrentTool.ConsumeObject)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.lang.String)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inputFileName)</span></div>
<div class="block">Copy an input file to output file with the same name in binary format.
 <br/>
 For example: <pre><code>
    &lt;img src="$file.copy('icon.gif')"&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputFileName</code> - the input filename</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.File)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> inputFile)</span></div>
<div class="block">Copy an input file to output file with the same name in binary format.
 <br/>
 For example: <pre><code>
    &lt;img src="$file.copy($iFile)"&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputFile</code> - the input file</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.util.Map)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; fileMap)</span></div>
</section>
</li>
<li>
<section class="detail" id="copy(java.lang.String,java.lang.String)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName)</span></div>
<div class="block">Copy an input file to output file in binary format.
 <br/>
 For example: <pre><code>
   &lt;img src="$file.copy('icon.gif','icon.gif')"&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputFileName</code> - the input filename</dd>
<dd><code>outputFileName</code> - the output filename</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.File,java.lang.String)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> inputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName)</span></div>
<div class="block">Copy an input file to output file in binary format.
 <br/>
 For example: <pre><code>
   &lt;img src="$file.copy($iconFile,'icon.gif')"&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputFile</code> - the input file</dd>
<dd><code>outputFileName</code> - the output filename</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.File,java.io.File)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> inputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile)</span></div>
<div class="block">Copy an input file to output file in binary format.
 <br/>
 For example: <pre><code>
   &lt;img src="$file.copy($iIcon, $oIcon)"&gt;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputFile</code> - the input file</dd>
<dd><code>outputFile</code> - the output file</dd>
<dt>Returns:</dt>
<dd>the output pathname. It will return empty string, if there is any error.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="exists(java.lang.String)">
<h3>exists</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">exists</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pathname)</span></div>
<div class="block">Tests whether the file denoted by <code>pathname</code> exists. By default, current directory will be
 referred to template location.
 <br/>
 For example: <pre><code>
        $file.exists("$template.resourcesLocation/myimage.png")
        $file.exists("C:/myfolder/myimage.png")
        $file.exists("mytemplate.txt")
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pathname</code> - A pathname string</dd>
<dt>Returns:</dt>
<dd><code>true</code> if and only if the file or directory denoted by this name exists;
         <code>false</code> otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="computeName(java.lang.String,java.lang.String)">
<h3>computeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">computeName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Create pathname string from given directory, name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>directory</code> - a parent directory of file</dd>
<dd><code>name</code> - a name of file (exclude extension)</dd>
<dt>Returns:</dt>
<dd>pathname from given directory, name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="computeName(java.lang.String,java.lang.String,java.lang.String)">
<h3>computeName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">computeName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> directory,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileType)</span></div>
<div class="block">Create pathname string from given directory, name, and file type.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>directory</code> - a parent directory of file</dd>
<dd><code>name</code> - a name of file (exclude extension)</dd>
<dd><code>fileType</code> - type of file. e.g. rtf, txt, html</dd>
<dt>Returns:</dt>
<dd>pathname string to filename</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.lang.String)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - an input template file name.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.io.File)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - an input template file.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.lang.String,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - an input template file name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context with default $importer name.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.io.File,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - an input template file name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context with default $importer name.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.lang.String,java.lang.String,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.
 <p>
 "importer" will be used as a name of context value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - an input template file name.</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context with default $importer name.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.io.File,java.lang.String,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.
 <p>
 "importer" will be used as a name of context value.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - an input template file.</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context with default $importer name.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contextName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - an input template file name.</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>contextName</code> - adding object context's name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.io.File,java.lang.String,java.lang.String,java.lang.Object)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> contextName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> contextValue)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - an input template file.</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>contextName</code> - adding object context's name.</dd>
<dd><code>contextValue</code> - additional object adding to new template context.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.lang.String,java.util.Map)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file. The output report will
 be named by template file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - an input template file name.</dd>
<dd><code>context</code> - additional context adding to new template.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.io.File,java.util.Map)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</span></div>
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
<section class="detail" id="createAndWait(java.lang.String,java.lang.String,java.util.Map)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - an input template file name.</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>context</code> - additional context adding to new template.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.io.File,java.lang.String,java.util.Map)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - an input template file.</dd>
<dd><code>outputFileName</code> - an output report file name.</dd>
<dd><code>context</code> - additional context adding to new template.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAndWait(java.io.File,java.io.File,java.util.Map)">
<h3>createAndWait</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createAndWait</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; context)</span></div>
<div class="block">Invoke a new template engine to generate a report and return the path to output file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFile</code> - an input template file.</dd>
<dd><code>outputFile</code> - an output report file.</dd>
<dd><code>context</code> - additional context adding to new template.</dd>
<dt>Returns:</dt>
<dd>an absolute path to output file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEmpty(java.lang.Object)">
<h3>isEmpty</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isEmpty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Check null object or empty string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj</code> - object to check</dd>
<dt>Returns:</dt>
<dd>true if specific object is null or empty string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getResultPath(java.lang.String,java.lang.String)">
<h3>getResultPath</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getResultPath</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> resultFromProcess,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> originalPath)</span></div>
<div class="block">Get result path.
 If result is empty, return original path</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resultFromProcess</code> - path from process</dd>
<dd><code>originalPath</code> - specific output file name</dd>
<dt>Returns:</dt>
<dd>result path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDir(java.io.File)">
<h3>createDir</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">createDir</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> outputDirectory)</span></div>
<div class="block">Create directory</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>outputDirectory</code> - directory path</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resolveOutputFileName(java.lang.String,java.lang.String,java.io.File)">
<h3>resolveOutputFileName</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">resolveOutputFileName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> outputFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> templateFile)</span></div>
<div class="block">Sometime the name of real template file is not match to original template file name.<br/>
 In case user does not specify output file name, we cannot assign the templateFileName to be outputFileName without checking.<br/>
 e.g., templateFileName = "mdp://attachedFile#_1234" <br/>
 templateFile = C://tmp//test.docx <br/>
 So, outputFileName should be 'test.docx' not 'mdp://attachedFile#_1234'<br/></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - original template file name</dd>
<dd><code>outputFileName</code> - original output file name</dd>
<dd><code>templateFile</code> - real template file</dd>
<dt>Returns:</dt>
<dd>outputFileName</dd>
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
