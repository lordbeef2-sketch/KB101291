# JAVA OPENAPI: FileUtils (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/helper/FileUtils.html
- source_path: `com/nomagic/magicreport/helper/FileUtils.html`
- source_sha256: `548bc0189de09a33be03e40214895f5727e8f104aa2de2210c18a1ebe2eaf545`
- captured_utc: `2026-07-14T16:46:14.432994+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.helper](package-summary.html)

## Class FileUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicreport.helper.FileUtils

@OpenApiAllpublic final classFileUtils
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

A collection of utility methods for File handler.

Since:
1.0 Nov 20, 2006
Version:
May 17, 2007

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static int`
`[copy](#copy(java.io.InputStream,java.io.OutputStream))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) output)`
Copy bytes from an `InputStream` to an `OutputStream`.
`static int`
`[copy](#copy(java.io.Reader,java.io.Writer))([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) input,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) output)`
Copy chars from a `Reader` to a `Writer`.
`static void`
`[createDirectory](#createDirectory(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Create a directory denoted by abstract pathname.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[createMrTempFile](#createMrTempFile(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suffix)`
Create temporary file in the [`getMrTempDir()`](#getMrTempDir()) directory.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[createNonOverwriteFile](#createNonOverwriteFile(java.io.File,java.lang.String))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) child)`
Create a non-overwrite file from given name and extension.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[createNonOverwriteFile](#createNonOverwriteFile(java.io.File,java.lang.String,java.lang.String))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suffix)`
Create a non-overwrite file from given name and extension.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[createTempFile](#createTempFile(java.lang.String,java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suffix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) parent,
 boolean useUnique)`
Creates a new empty file in the specified directory, using the given prefix and suffix strings to generate
 its name.
`static boolean`
`[delete](#delete(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Deletes the file or directory denoted by this abstract pathname.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getExtension](#getExtension(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Return extension of file.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getExtension](#getExtension(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filename)`
Return extension of file.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getMrTempDir](#getMrTempDir())()`
Get MagicReport temporary directory.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getName](#getName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filename)`
Return name of file without extension.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getTempDir](#getTempDir())()`
Return system temporary directory.The default temporary-file directory is specified by the system property
 `java.io.tmpdir`.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateLocation)`
Get Template file from template file name/path.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile(java.lang.String,java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateLocation,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)`
Get Template file from template file name/path.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[getTemplateFile](#getTemplateFile(java.lang.String,java.util.List,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> templateLocations,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)`
Get Template file from template file name/path.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[normalize](#normalize(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Convert the given file to normal form.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[normalize](#normalize(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Convert the given name string to normal form.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)[]`
`[recursiveFileList](#recursiveFileList(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) basedDir)`
Recursive to get all files in `basedDir`.
`static [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)[]`
`[recursiveFileURLList](#recursiveFileURLList(java.io.File))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) basedDir)`
Recursive to get all resources in `basedDir`.
`static void`
`[track](#track(java.io.File,java.lang.Object))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)`
Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.
`static void`
`[track](#track(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) path,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)`
Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
createNonOverwriteFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) createNonOverwriteFile([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suffix)
Create a non-overwrite file from given name and extension. The format of new file name is name + "." +
 extension. If file already exists, append (number) after name.
 

 

`Example: createNonOverwriteFile(parent, "filename", "txt");
 // result of this method is "filename.txt"
 // if "filename.txt" already exists, the new file name is "filename(1).txt"`
Parameters:
`parent` - The directory in which the file is to be created
`prefix` - The prefix string to be used in generating the file's name
`suffix` - The suffix string to be used in generating the file's name; may be extension of file.
Returns:
an instance of File
createNonOverwriteFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) createNonOverwriteFile([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) parent,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) child)
Create a non-overwrite file from given name and extension. The format of new file name is name + "." +
 extension. If file already exists, append (number) after name.
 

 

`Example: createNonOverwriteFile(parent, "filename", "txt");
 // result of this method is "filename.txt"
 // if "filename.txt" already exists, the new file name is "filename(1).txt"`
Parameters:
`parent` - The directory in which the file is to be created
`child` - The child pathname string
Returns:
an instance of File
getExtension
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getExtension([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
Return extension of file. Extension excluded "." character.
Parameters:
`file` - file to find an extension
Returns:
extension of file
getExtension
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getExtension([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filename)
Return extension of file. Extension excluded "." character.
Parameters:
`filename` - file name
Returns:
extension of file
getName
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getName([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) filename)
Return name of file without extension.
Parameters:
`filename` - file name
Returns:
name of file
recursiveFileURLList
public static [URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html)[] recursiveFileURLList([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) basedDir)
Recursive to get all resources in `basedDir`. Return array of file `URL`, or array
 length zero if no file found.
Parameters:
`basedDir` - root directory
Returns:
`array` of file `URL`
recursiveFileList
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)[] recursiveFileList([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) basedDir)
Recursive to get all files in `basedDir`. Return array of `File`, or array length zero
 if no file found.
Parameters:
`basedDir` - root directory
Returns:
`array` of `File`
createTempFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) createTempFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suffix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) parent,
 boolean useUnique)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Creates a new empty file in the specified directory, using the given prefix and suffix strings to generate
 its name. If this method returns successfully then it is guaranteed that:
 The file denoted by the returned abstract pathname did not exist before this method was invoked, and
 Neither this method nor any of its variants will return the same abstract pathname again in the current
 invocation of the virtual machine.
 This method provides only part of a temporary-file facility. To arrange for a file created by this method to
 be deleted automatically, use the `[track(File,Object)](#track(java.io.File,java.lang.Object))` or
 `java.io.File#deleteOnExit()` method.
 

 If the `parent` argument is `null` then the system-dependent default temporary-file
 directory will be used. The default temporary-file directory is specified by the system property
 `java.io.tmpdir`.
 

 The complete structure of empty file is: `prefix + unique_number + suffix`
Parameters:
`prefix` - The prefix string to be used in generating the file's name; must be at least three characters
 long
`suffix` - The suffix string to be used in generating the file's name; may be `null`, in which
 case the suffix `".tmp"` will be used
`parent` - The directory in which the file is to be created, or `null` if the default
 temporary-file directory is to be used
`useUnique` - if true always create unique file name.
Returns:
An abstract pathname denoting a newly-created empty file
Throws:
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - If the `prefix` argument contains fewer than three characters
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If a file could not be created
createMrTempFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) createMrTempFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) prefix,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) suffix)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create temporary file in the [`getMrTempDir()`](#getMrTempDir()) directory.
 This equals to [`createTempFile(prefix, suffix,
 getMrTempDir(), true)`](#createTempFile(java.lang.String,java.lang.String,java.lang.String,boolean)).
Parameters:
`prefix` - The prefix string to be used in generating the file's name; must be at least three characters
 long
`suffix` - The suffix string to be used in generating the file's name; may be `null`, in which
 case the suffix `".tmp"` will be used
Returns:
An abstract pathname denoting a newly-created empty file
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - If a file could not be created
getTempDir
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getTempDir()
Return system temporary directory.The default temporary-file directory is specified by the system property
 `java.io.tmpdir`. On UNIX systems the default value of this property is typically "
 `/tmp`" or "`/var/tmp`"; on Microsoft Windows systems it is typically "
 `C:\\WINNT\\TEMP`". A different value may be given to this system property when the Java virtual
 machine is invoked
Returns:
default temporary-file directory
getMrTempDir
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getMrTempDir()
Get MagicReport temporary directory.
 The MagicReport directory is `[getTempDir()](#getTempDir())+"mr/"`. The directory will be automatically
 created if it doesn't exist.
Returns:
MagicReport temporary directory.
See Also:
[`getTempDir()`](#getTempDir())
copy
public static int copy([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Copy bytes from an `InputStream` to an `OutputStream`.
 

 This method buffers the input internally, so there is no need to use a `BufferedInputStream`.
Parameters:
`input` - the `InputStream` to read from
`output` - the `OutputStream` to write to
Returns:
the number of bytes copied
Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if the input or output is null
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error occurs
copy
public static int copy([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) input,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Copy chars from a `Reader` to a `Writer`.
 

 This method buffers the input internally, so there is no need to use a `BufferedReader`.
Parameters:
`input` - the `Reader` to read from
`output` - the `Writer` to write to
Returns:
the number of characters copied
Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if the input or output is null
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if an I/O error occurs
delete
public static boolean delete([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
Deletes the file or directory denoted by this abstract pathname. If this pathname denotes a directory, then
 the file and directory inside this file will be deleted recursively.
Parameters:
`file` - the file or directory to be deleted
Returns:
`true` if and only if the file or directory is successfully deleted; `false`
 otherwise
Throws:
`[SecurityException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/SecurityException.html)` - If a security manager exists and its `[SecurityManager.checkDelete(java.lang.String)](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/SecurityManager.html#checkDelete(java.lang.String))` method denies delete access to the file
createDirectory
public static void createDirectory([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Create a directory denoted by abstract pathname. This method automatically remove special characters in name
 before create a directory. Special characters are one of the following: `\/?*:"<>|`
Parameters:
`file` - directory to be created.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - if false to create directory.
normalize
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) normalize([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
Convert the given file to normal form. If the string is already in normal form then it is simply returned.
Parameters:
`file` - file
Returns:
normalized name
normalize
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) normalize([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Convert the given name string to normal form. If the string is already in normal form then it is simply
 returned.
Parameters:
`name` - name of file
Returns:
normalized name
track
public static void track([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)
Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.
Parameters:
`file` - The file to be tracked.
`marker` - The marker object used to track the file.
track
public static void track([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) path,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)
Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.
Parameters:
`path` - The full path to the file to be tracked.
`marker` - The marker object used to track the file.
getTemplateFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getTemplateFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateLocation)
Get Template file from template file name/path.
Parameters:
`templateFileName` - template file name or path
`templateLocation` - template location
Returns:
template file
getTemplateFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getTemplateFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateLocation,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)
Get Template file from template file name/path.
Parameters:
`templateFileName` - template file name or path
`templateLocation` - template location
`extension` - extension for template file. in case it has no extension
`marker` - The marker object used to track the file.
Returns:
template file
getTemplateFile
public static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) getTemplateFile([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) templateFileName,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> templateLocations,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) marker)
Get Template file from template file name/path.
Parameters:
`templateFileName` - template file name or path
`templateLocations` - list of possible locations
`extension` - extension for template file. in case it has no extension
`marker` - The marker object used to track the file.
Returns:
template file

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.helper</a></div>
<h1 class="title" title="Class FileUtils">Class FileUtils</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicreport.helper.FileUtils</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">FileUtils</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">A collection of utility methods for File handler.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>1.0 Nov 20, 2006</dd>
<dt>Version:</dt>
<dd>May 17, 2007</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.InputStream,java.io.OutputStream)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copy bytes from an <code>InputStream</code> to an <code>OutputStream</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.Reader,java.io.Writer)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> output)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copy chars from a <code>Reader</code> to a <code>Writer</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createDirectory(java.io.File)">createDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a directory denoted by abstract pathname.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMrTempFile(java.lang.String,java.lang.String)">createMrTempFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create temporary file in the <a href="#getMrTempDir()"><code>getMrTempDir()</code></a> directory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createNonOverwriteFile(java.io.File,java.lang.String)">createNonOverwriteFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> child)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a non-overwrite file from given name and extension.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createNonOverwriteFile(java.io.File,java.lang.String,java.lang.String)">createNonOverwriteFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a non-overwrite file from given name and extension.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTempFile(java.lang.String,java.lang.String,java.lang.String,boolean)">createTempFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parent,
 boolean useUnique)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block"><br/>
 Creates a new empty file in the specified directory, using the given prefix and suffix strings to generate
 its name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#delete(java.io.File)">delete</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Deletes the file or directory denoted by this abstract pathname.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtension(java.io.File)">getExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return extension of file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getExtension(java.lang.String)">getExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return extension of file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getMrTempDir()">getMrTempDir</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get MagicReport temporary directory.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getName(java.lang.String)">getName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return name of file without extension.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTempDir()">getTempDir</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Return system temporary directory.The default temporary-file directory is specified by the system property
 <code>java.io.tmpdir</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile(java.lang.String,java.lang.String)">getTemplateFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateLocation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Template file from template file name/path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">getTemplateFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateLocation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Template file from template file name/path.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTemplateFile(java.lang.String,java.util.List,java.lang.String,java.lang.Object)">getTemplateFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; templateLocations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get Template file from template file name/path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalize(java.io.File)">normalize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert the given file to normal form.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalize(java.lang.String)">normalize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert the given name string to normal form.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#recursiveFileList(java.io.File)">recursiveFileList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> basedDir)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Recursive to get all files in <code>basedDir</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#recursiveFileURLList(java.io.File)">recursiveFileURLList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> basedDir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Recursive to get all resources in <code>basedDir</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#track(java.io.File,java.lang.Object)">track</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#track(java.lang.String,java.lang.Object)">track</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="createNonOverwriteFile(java.io.File,java.lang.String,java.lang.String)">
<h3>createNonOverwriteFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createNonOverwriteFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix)</span></div>
<div class="block">Create a non-overwrite file from given name and extension. The format of new file name is name + "." +
 extension. If file already exists, append (number) after name.
 <br/>
<br/>
<pre><code>
 Example: createNonOverwriteFile(parent, "filename", "txt");
 // result of this method is "filename.txt"
 // if "filename.txt" already exists, the new file name is "filename(1).txt"
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - The directory in which the file is to be created</dd>
<dd><code>prefix</code> - The prefix string to be used in generating the file's name</dd>
<dd><code>suffix</code> - The suffix string to be used in generating the file's name; may be extension of file.</dd>
<dt>Returns:</dt>
<dd>an instance of File</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNonOverwriteFile(java.io.File,java.lang.String)">
<h3>createNonOverwriteFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createNonOverwriteFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> parent,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> child)</span></div>
<div class="block">Create a non-overwrite file from given name and extension. The format of new file name is name + "." +
 extension. If file already exists, append (number) after name.
 <br/>
<br/>
<pre><code>
 Example: createNonOverwriteFile(parent, "filename", "txt");
 // result of this method is "filename.txt"
 // if "filename.txt" already exists, the new file name is "filename(1).txt"
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parent</code> - The directory in which the file is to be created</dd>
<dd><code>child</code> - The child pathname string</dd>
<dt>Returns:</dt>
<dd>an instance of File</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtension(java.io.File)">
<h3>getExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Return extension of file. Extension excluded "." character.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - file to find an extension</dd>
<dt>Returns:</dt>
<dd>extension of file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExtension(java.lang.String)">
<h3>getExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</span></div>
<div class="block">Return extension of file. Extension excluded "." character.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filename</code> - file name</dd>
<dt>Returns:</dt>
<dd>extension of file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName(java.lang.String)">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</span></div>
<div class="block">Return name of file without extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filename</code> - file name</dd>
<dt>Returns:</dt>
<dd>name of file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="recursiveFileURLList(java.io.File)">
<h3>recursiveFileURLList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a>[]</span> <span class="element-name">recursiveFileURLList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> basedDir)</span></div>
<div class="block">Recursive to get all resources in <code>basedDir</code>. Return array of file <code>URL</code>, or array
 length zero if no file found.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>basedDir</code> - root directory</dd>
<dt>Returns:</dt>
<dd><code>array</code> of file <code>URL</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="recursiveFileList(java.io.File)">
<h3>recursiveFileList</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>[]</span> <span class="element-name">recursiveFileList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> basedDir)</span></div>
<div class="block">Recursive to get all files in <code>basedDir</code>. Return array of <code>File</code>, or array length zero
 if no file found.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>basedDir</code> - root directory</dd>
<dt>Returns:</dt>
<dd><code>array</code> of <code>File</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTempFile(java.lang.String,java.lang.String,java.lang.String,boolean)">
<h3>createTempFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createTempFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parent,
 boolean useUnique)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block"><br/>
 Creates a new empty file in the specified directory, using the given prefix and suffix strings to generate
 its name. If this method returns successfully then it is guaranteed that:
 <ol>
<li>The file denoted by the returned abstract pathname did not exist before this method was invoked, and
 <li>Neither this method nor any of its variants will return the same abstract pathname again in the current
 invocation of the virtual machine.
 </li></li></ol>
 This method provides only part of a temporary-file facility. To arrange for a file created by this method to
 be deleted automatically, use the <code><a href="#track(java.io.File,java.lang.Object)"><code>track(File,Object)</code></a></code> or
 <code>java.io.File#deleteOnExit()</code> method.
 <br/>
 If the <code>parent</code> argument is <code>null</code> then the system-dependent default temporary-file
 directory will be used. The default temporary-file directory is specified by the system property
 <code>java.io.tmpdir</code>.
 <br/>
 The complete structure of empty file is: <code>prefix + unique_number + suffix</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prefix</code> - The prefix string to be used in generating the file's name; must be at least three characters
           long</dd>
<dd><code>suffix</code> - The suffix string to be used in generating the file's name; may be <code>null</code>, in which
           case the suffix <code>".tmp"</code> will be used</dd>
<dd><code>parent</code> - The directory in which the file is to be created, or <code>null</code> if the default
           temporary-file directory is to be used</dd>
<dd><code>useUnique</code> - if true always create unique file name.</dd>
<dt>Returns:</dt>
<dd>An abstract pathname denoting a newly-created empty file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - If the <code>prefix</code> argument contains fewer than three characters</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If a file could not be created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMrTempFile(java.lang.String,java.lang.String)">
<h3>createMrTempFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">createMrTempFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> prefix,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> suffix)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create temporary file in the <a href="#getMrTempDir()"><code>getMrTempDir()</code></a> directory.
 <p>
 This equals to <a href="#createTempFile(java.lang.String,java.lang.String,java.lang.String,boolean)"><code>createTempFile(prefix, suffix,
 getMrTempDir(), true)</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>prefix</code> - The prefix string to be used in generating the file's name; must be at least three characters
           long</dd>
<dd><code>suffix</code> - The suffix string to be used in generating the file's name; may be <code>null</code>, in which
           case the suffix <code>".tmp"</code> will be used</dd>
<dt>Returns:</dt>
<dd>An abstract pathname denoting a newly-created empty file</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - If a file could not be created</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTempDir()">
<h3>getTempDir</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTempDir</span>()</div>
<div class="block">Return system temporary directory.The default temporary-file directory is specified by the system property
 <code>java.io.tmpdir</code>. On UNIX systems the default value of this property is typically "
 <code>/tmp</code>" or "<code>/var/tmp</code>"; on Microsoft Windows systems it is typically "
 <code>C:\\WINNT\\TEMP</code>". A different value may be given to this system property when the Java virtual
 machine is invoked</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>default temporary-file directory</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMrTempDir()">
<h3>getMrTempDir</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getMrTempDir</span>()</div>
<div class="block">Get MagicReport temporary directory.
 <p>
 The MagicReport directory is <code><a href="#getTempDir()"><code>getTempDir()</code></a>+"mr/"</code>. The directory will be automatically
 created if it doesn't exist.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>MagicReport temporary directory.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#getTempDir()"><code>getTempDir()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.InputStream,java.io.OutputStream)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output)</span>
                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Copy bytes from an <code>InputStream</code> to an <code>OutputStream</code>.
 <br/>
 This method buffers the input internally, so there is no need to use a <code>BufferedInputStream</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - the <code>InputStream</code> to read from</dd>
<dd><code>output</code> - the <code>OutputStream</code> to write to</dd>
<dt>Returns:</dt>
<dd>the number of bytes copied</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the input or output is null</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.Reader,java.io.Writer)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> output)</span>
                throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Copy chars from a <code>Reader</code> to a <code>Writer</code>.
 <br/>
 This method buffers the input internally, so there is no need to use a <code>BufferedReader</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - the <code>Reader</code> to read from</dd>
<dd><code>output</code> - the <code>Writer</code> to write to</dd>
<dt>Returns:</dt>
<dd>the number of characters copied</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the input or output is null</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if an I/O error occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="delete(java.io.File)">
<h3>delete</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">delete</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Deletes the file or directory denoted by this abstract pathname. If this pathname denotes a directory, then
 the file and directory inside this file will be deleted recursively.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - the file or directory to be deleted</dd>
<dt>Returns:</dt>
<dd><code>true</code> if and only if the file or directory is successfully deleted; <code>false</code>
         otherwise</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/SecurityException.html" title="class or interface in java.lang">SecurityException</a></code> - If a security manager exists and its <code>
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/SecurityManager.html#checkDelete(java.lang.String)" title="class or interface in java.lang"><code>SecurityManager.checkDelete(java.lang.String)</code></a></code> method denies delete access to the file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createDirectory(java.io.File)">
<h3>createDirectory</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">createDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Create a directory denoted by abstract pathname. This method automatically remove special characters in name
 before create a directory. Special characters are one of the following: <code>\/?*:"&lt;&gt;|</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - directory to be created.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if false to create directory.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="normalize(java.io.File)">
<h3>normalize</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">normalize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Convert the given file to normal form. If the string is already in normal form then it is simply returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - file</dd>
<dt>Returns:</dt>
<dd>normalized name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="normalize(java.lang.String)">
<h3>normalize</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">normalize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Convert the given name string to normal form. If the string is already in normal form then it is simply
 returned.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - name of file</dd>
<dt>Returns:</dt>
<dd>normalized name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="track(java.io.File,java.lang.Object)">
<h3>track</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">track</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</span></div>
<div class="block">Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - The file to be tracked.</dd>
<dd><code>marker</code> - The marker object used to track the file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="track(java.lang.String,java.lang.Object)">
<h3>track</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">track</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</span></div>
<div class="block">Track the specified file, using the provided marker, deleting the file when the marker instance is garbage
 collected.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - The full path to the file to be tracked.</dd>
<dd><code>marker</code> - The marker object used to track the file.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateFile(java.lang.String,java.lang.String)">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateLocation)</span></div>
<div class="block">Get Template file from template file name/path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - template file name or path</dd>
<dd><code>templateLocation</code> - template location</dd>
<dt>Returns:</dt>
<dd>template file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateFile(java.lang.String,java.lang.String,java.lang.String,java.lang.Object)">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateLocation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</span></div>
<div class="block">Get Template file from template file name/path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - template file name or path</dd>
<dd><code>templateLocation</code> - template location</dd>
<dd><code>extension</code> - extension for template file. in case it has no extension</dd>
<dd><code>marker</code> - The marker object used to track the file.</dd>
<dt>Returns:</dt>
<dd>template file</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTemplateFile(java.lang.String,java.util.List,java.lang.String,java.lang.Object)">
<h3>getTemplateFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">getTemplateFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> templateFileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; templateLocations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> marker)</span></div>
<div class="block">Get Template file from template file name/path.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateFileName</code> - template file name or path</dd>
<dd><code>templateLocations</code> - list of possible locations</dd>
<dd><code>extension</code> - extension for template file. in case it has no extension</dd>
<dd><code>marker</code> - The marker object used to track the file.</dd>
<dt>Returns:</dt>
<dd>template file</dd>
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
