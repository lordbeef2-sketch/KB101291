# JAVA OPENAPI: Utilities (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/utils/Utilities.html
- source_path: `com/nomagic/utils/Utilities.html`
- source_sha256: `6c0bac9db3fd0bad2304cd2b88cc29a672b0645fc3e9efd1aec8e09d9ba5b4f3`
- captured_utc: `2026-07-14T16:56:41.517972+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.utils](package-summary.html)

## Class Utilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.utils.CameoUtilities](CameoUtilities.html)
com.nomagic.utils.Utilities

@OpenApiAllpublic classUtilities
extends [CameoUtilities](CameoUtilities.html)
General purpose utilities.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Utilities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[addHttpParameter](#addHttpParameter(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameter,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Adds http parameter to given parameters string
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Collection,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> source,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T> v,
 boolean allowDublication)`
Deprecated.
Use [`CollectionUtils.append(java.util.Collection, java.util.Collection, boolean)`](CollectionUtils.html#append(java.util.Collection,java.util.Collection,boolean))
`static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T>`
`[append](#append(java.util.Collection,java.util.Iterator,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> source,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<? extends T> it,
 boolean allowDublication)`
Deprecated.
Use [`CollectionUtils.append(java.util.Collection, java.util.Iterator, boolean)`](CollectionUtils.html#append(java.util.Collection,java.util.Iterator,boolean))
`static boolean`
`[areChildrenDisabled](#areChildrenDisabled(javax.swing.JMenu))([JMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenu.html) menu)`
Are all children disabled?
`static int`
`[arrayHash](#arrayHash(byte%5B%5D))(byte[] array)`
Calculate hash code for array of bytes
`static int`
`[calculateTextWidth](#calculateTextWidth(java.lang.String,java.awt.FontMetrics,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [FontMetrics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/FontMetrics.html) metrics,
 int numberOfLines)`
Calculates possible text longest text width of the given text splitted into lines.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[checkIsInstallRootWritable](#checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment))(com.nomagic.runtime.RuntimeEnvironment runtime)`
Get message for install root read only error.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[checkIsInstallRootWritable](#checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment,boolean))(com.nomagic.runtime.RuntimeEnvironment runtime,
 boolean skipWinUAC)`
Get message for install root read only error.
`static boolean`
`[checkProperty](#checkProperty(java.util.Properties,java.lang.String,boolean))([Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html) properties,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 boolean defaultValue)`

`static boolean`
`[checkResolvableException](#checkResolvableException(boolean))(boolean rule)`
if rule is false and it's DEVELOPER mode throws [`IllegalStateException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
`static boolean`
`[checkSystemProperty](#checkSystemProperty(java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 boolean defaultValue)`
Checks given system (boolean) property value
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[clearAllLine](#clearAllLine(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trash)`
Removes all trash from string
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[clearFromEveryLine](#clearFromEveryLine(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mask)`
Divides given string into lines and from every line beginning
 and end removes all chars from given string mask.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[clearLine](#clearLine(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) line,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trash)`
removes from line ends wanted characters
`static int`
`[collectInteger](#collectInteger(byte%5B%5D))(byte[] bytes)`
Makes int value from array of bytes
`static boolean`
`[compareFiles](#compareFiles(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f1,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f2)`
Compares two files
`static boolean`
`[compareStreams](#compareStreams(java.io.InputStream,java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) oldStr,
 [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) newStr)`
Compares two input streams.
`static byte[]`
`[compressData](#compressData(byte%5B%5D))(byte[] data)`
Compresses specified data using gzip output stream and returns the result as bytes array.
`static byte[]`
`[compressData](#compressData(byte%5B%5D,java.lang.String))(byte[] data,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) zipEntryName)`
Compresses specified data using zip output stream and returns the result as bytes array.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[concatHttpParameter](#concatHttpParameter(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters1,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters2)`
Concatenate given http parameters
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[constructHttpParameter](#constructHttpParameter(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameter,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`
Constructs http parameter
`static boolean`
`[contains](#contains(java.util.Iterator,java.lang.Object))([Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html) it,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`
Deprecated.
Use [`CollectionUtils.contains(java.util.Iterator, Object)`](CollectionUtils.html#contains(java.util.Iterator,java.lang.Object))
`static boolean`
`[containSameElements](#containSameElements(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection2)`

`static boolean`
`[containsAny](#containsAny(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) location,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) what)`
Deprecated.
Use [`CollectionUtils.containsAny(java.util.Collection, java.util.Collection)`](CollectionUtils.html#containsAny(java.util.Collection,java.util.Collection))
`static boolean`
`[containsNonDirectory](#containsNonDirectory(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> fileList)`

`static boolean`
`[containsOnlyFiles](#containsOnlyFiles(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) list)`
Indicates if given list contains only file objects.
`static boolean`
`[contentEquals](#contentEquals(java.io.InputStream,java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input1,
 [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input2)`
Compare content of two streams.
`static void`
`[copy](#copy(java.io.InputStream,java.io.OutputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output)`
Copies all bytes from InputStream into OutputStream.
`static void`
`[copy](#copy(java.io.InputStream,java.io.OutputStream,long,boolean))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output,
 long crc,
 boolean closeInput)`
Copies all bytes from InputStream into OutputStream.
`static void`
`[copy](#copy(java.io.InputStream,java.io.OutputStream,java.util.zip.Checksum))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output,
 [Checksum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/Checksum.html) checksum)`
Copies all bytes from InputStream into OutputStream
`static boolean`
`[copyDirectory](#copyDirectory(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)`
Copy all directory recursively
`static boolean`
`[copyFile](#copyFile(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)`
Copy source file to destination file.
`static boolean`
`[copyFile](#copyFile(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sourceName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dstName)`
Copy source file to destination file.
`static int`
`[countOccurrences](#countOccurrences(java.lang.String,char))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string,
 char c)`
Returns the number of times the character c appears in a string.
`static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[coverRectangle](#coverRectangle(java.awt.Rectangle,java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) inner,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) outer)`
Moves outer rectangle in such way that it must cover inner one (if outer is smaller than inner resizes outer).
`static <E extends [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)> 
E`
`[createCollection](#createCollection(java.lang.Class,java.util.Iterator))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<E> collection,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html) it)`
Deprecated.
Use [`CollectionUtils.createCollection(Class, java.util.Iterator)`](CollectionUtils.html#createCollection(java.lang.Class,java.util.Iterator))
`static [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[createCursor](#createCursor(java.awt.Image,java.awt.Point,java.lang.String))([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cursorName)`
Creates the cursor for given image.
`static [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[createCursor](#createCursor(javax.swing.Icon,java.awt.Point,java.lang.String))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cursorName)`
Creates the cursor for given icon.
`static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[createRectFromList](#createRectFromList(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> v)`
Creates rectangle from vector of points.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStringRepresentation](#createStringRepresentation(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) value)`

`static byte[]`
`[decodeBase64](#decodeBase64(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Decode string using Base64 encoding.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>`
`[deepPointsClone](#deepPointsClone(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> v)`
Makes a deep clone of vector that contains points.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)>`
`[deepPointsClone](#deepPointsClone(java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> v,
 boolean cloneList)`
Makes a deep clone of vector that contains points.
`static void`
`[deleteDirContent](#deleteDirContent(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f)`
Removes given directory contents.
`static void`
`[deleteTree](#deleteTree(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f)`
Removes given directory and all its contents.
`static void`
`[deleteTreeOnExit](#deleteTreeOnExit(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f)`
Removes given file (directory and all its contents) on exit.
`static byte[]`
`[distributeInteger](#distributeInteger(int,int))(int intValue,
 int size)`
Distributes integer intValue into array of bytes.
`static void`
`[dumpThreads](#dumpThreads())()`
Dumps all threads to system out.
`static void`
`[dumpThreads](#dumpThreads(java.io.PrintStream))([PrintStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/PrintStream.html) out)`
Dumps all threads to given stream.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[encodeBase64](#encodeBase64(byte%5B%5D))(byte[] abyte0)`
Encodes data using base64 encoding.
`static <T> void`
`[ensureObjectIsInCollection](#ensureObjectIsInCollection(java.util.Collection,T))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 T object)`
Ensures an object is in given collection.
`static <T> [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<T>`
`[excludeCommonElements](#excludeCommonElements(java.util.Collection,java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> first,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> second)`
Creates result collection which contains not common elements from two arguments
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)>`
`[extractZip](#extractZip(java.io.InputStream,java.lang.String,java.util.Collection,java.util.Collection))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) is,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dstDir,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> onlyTheseEntries,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> skipTheseEntries)`
Extracts files from Zip archive
`static void`
`[extractZip](#extractZip(java.util.zip.ZipFile,java.lang.String))([ZipFile](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipFile.html) zipFile,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dstDir)`
Extracts files from Zip archive
`static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[fitInRectangle](#fitInRectangle(java.awt.Rectangle,java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) small,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) big)`
recalculate bounds to fit in rectangle
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAsString](#getAsString(javax.swing.KeyStroke))([KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) e)`
Constructs the string representation of the given key stroke.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAsStringKeyStrokes](#getAsStringKeyStrokes(java.util.List,java.lang.String,java.lang.String))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html)> shortcuts,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bracketFirst,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bracketSecond)`
Constructs the string representation of the given key strokes.
`static byte[]`
`[getBytes](#getBytes(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str)`
Returns bytes of string.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getClassName](#getClassName(java.lang.Class))([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz)`
Get class name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCurrentDateFormatted](#getCurrentDateFormatted())()`

`static <E> int`
`[getDistance](#getDistance(E,E,java.util.function.Function))(E from,
 E to,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<E,[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>> connectedNodes)`
Calculate minimal distance in graph.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileExtension](#getFileExtension(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Get The given file extension.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileExtension](#getFileExtension(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)`
Get the given file extension.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileName](#getFileName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileWithoutExtension](#getFileWithoutExtension(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filename)`
Returns file name without extension (removes chars from last "." to end of string)
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileWitoutExtention](#getFileWitoutExtention(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filename)`
Deprecated.
type error in name
`static [ResizableIcon](../ui/ResizableIcon.html)`
`[getGrayIcon](#getGrayIcon(javax.swing.Icon))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)`
Deprecated.
Use [`IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)`](../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component))
`static [ResizableIcon](../ui/ResizableIcon.html)`
`[getGrayIcon](#getGrayIcon(javax.swing.Icon,java.awt.Component))([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)`
Deprecated.
Use [`IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)`](../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHtmlPage](#getHtmlPage(java.lang.String,java.lang.String,com.nomagic.license.utils.ProxyServerData))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pageHttpAddress,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters,
 [ProxyServerData](../license/utils/ProxyServerData.html) proxy)`
Returns HTML page
`static [JMenuItem](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html)`
`[getItemWithText](#getItemWithText(javax.swing.JPopupMenu,java.lang.String))([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) menu,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Returns inner component (not recursively) with given text.
`static [DateFormat](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html)`
`[getSystemDateFormat](#getSystemDateFormat(int))(int style)`
Returns system date format.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTempDir](#getTempDir())()`
Returns System temp directory.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getThreadsInfo](#getThreadsInfo())()`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getVersionFromInternal](#getVersionFromInternal(int))(int internal)`
Convert internal MagicDraw style version to human version in 17.0.2 format.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getVersionFromInternal](#getVersionFromInternal(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) internal)`
Convert internal MagicDraw style version to human version in 17.0.2 format.
`static boolean`
`[hasModalDialogs](#hasModalDialogs(java.awt.Window))([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) window)`
Checks recursively if given window has modal dialog as child (or window itself is a modal dialog)
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[implode](#implode(java.lang.String%5B%5D,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] values,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)`
Deprecated.
Use [`String.join(CharSequence, CharSequence...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.CharSequence...))
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[implode](#implode(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)`
Returns a new String composed of copies of the collection elements joined together with a copy of the specified delimiter.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[insertPeriodically](#insertPeriodically(java.lang.String,java.lang.String,int))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) insert,
 int period)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[insertSeparators](#insertSeparators(char%5B%5D,java.lang.String,int))(char[] chars,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 int groupSize)`
Constructs string from arrays of chars.
`static void`
`[invokeAndWaitOnDispatcher](#invokeAndWaitOnDispatcher(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)`
Executes given runnable on event dispatcher.
`static void`
`[invokeAndWaitOnDispatcherEvenInterrupted](#invokeAndWaitOnDispatcherEvenInterrupted(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)`
Executes given runnable on event dispatcher.
`static void`
`[invokeLaterAfterCondition](#invokeLaterAfterCondition(java.lang.Runnable,java.util.function.Supplier))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> condition)`
Invokes runnable latter after condition is satisfied.
`static void`
`[invokeLaterAfterCondition](#invokeLaterAfterCondition(java.lang.Runnable,java.util.function.Supplier,int))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> condition,
 int conditionCheckAttemptCount)`
Invokes runnable latter after condition is satisfied.
`static void`
`[invokeOnDispatcherOrLater](#invokeOnDispatcherOrLater(java.lang.Runnable))([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)`
If this thread is event dispatcher, than direct calls "run", else invoke on invoke later
`static boolean`
`[isAlphaNumeric](#isAlphaNumeric(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str)`

`static boolean`
`[isFileNameValid](#isFileNameValid(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)`
Returns if given file name is valid to be created.
`static boolean`
`[isHTMLText](#isHTMLText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)`
Check the given string to see if it should trigger the
 html rendering logic.
`static boolean`
`[isNameValid](#isNameValid(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)`

`static boolean`
`[isPrintableChar](#isPrintableChar(char))(char c)`
Checks if char is printable or not.
`static boolean`
`[isStreamEmpty](#isStreamEmpty(java.net.URL))([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) url)`
Check if it is possible to open a stream from a given URL and that stream is not empty
`static boolean`
`[isUseProxy](#isUseProxy(com.nomagic.license.utils.ProxyServerData))([ProxyServerData](../license/utils/ProxyServerData.html) proxy)`
Checks if use proxy server according given proxy server data
`static boolean`
`[isValidKeyCode](#isValidKeyCode(int))(int keyCode)`
Checks if given code is correct one or not.
`static void`
`[main](#main(java.lang.String%5B%5D))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)`

`static void`
`[makeEqual](#makeEqual(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) destination,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) source)`
Make destination the same as source with minimum changes to destination
`static boolean`
`[match](#match(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)`
Checks if given string matches given pattern with wild cards.
`static boolean`
`[matchIncludingEmpty](#matchIncludingEmpty(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)`
Checks if given string matches given pattern with wild cards.
`static <T> void`
`[merge](#merge(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> source,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> v)`
Merges two vector.
`static <T> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T>`
`[mergeLists](#mergeLists(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> l1,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> l2)`
Merges two lists into newly created one.
`static void`
`[normalize](#normalize(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
normalizes rectangle mRectToDraw;
`static void`
`[normalize](#normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rectangle,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) firstCorner,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) secondCorner)`
Normalizes rectangle; Calculates rectangle size and location using firstCorner and secondCorner.
`static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)`
`[notDublicatedList](#notDublicatedList(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) col)`
Deprecated.
Use [`CollectionUtils.notDuplicatedList(java.util.Collection)`](CollectionUtils.html#notDuplicatedList(java.util.Collection))
`static [HttpURLConnection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html)`
`[openHttpURLConnection](#openHttpURLConnection(java.lang.String,com.nomagic.license.utils.ProxyServerData))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pageHttpAddress,
 [ProxyServerData](../license/utils/ProxyServerData.html) proxyServerData)`
Opens HttpURLConnection according given page address and proxy server data.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[parseExceptQuotes](#parseExceptQuotes(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd)`
parses string by standard tokens, except parts wrapped in quotes
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[readFileSkipFirstLines](#readFileSkipFirstLines(java.io.File,int))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file,
 int n)`
Reads a file to string and skips a specified number of lines from the beginning.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[removeComments](#removeComments(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) body)`
Removes / * * / comments from body.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[removeNewLines](#removeNewLines(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)`
Removes new lines from the string.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[removeNonUtf8CompliantCharacters](#removeNonUtf8CompliantCharacters(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) inString)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[removeSeparators](#removeSeparators(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)`
Removes separators from specified str
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[replace](#replace(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) replaceWith)`
Replaces string fragment with another string
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[replaceEpsString](#replaceEpsString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) aStr)`
Replace special char for Eps format string
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[reverseString](#reverseString(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) source)`
Given a string, returns a string with reversed characters.
`static void`
`[sendHttpParameters](#sendHttpParameters(java.net.HttpURLConnection,java.lang.String))([HttpURLConnection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html) connection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters)`
Deprecated.
use `HttpUtilities.sendHttpParameters(HttpURLConnection, String)`
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[sha1Hex](#sha1Hex(byte%5B%5D))(byte[] data)`
Returns SHA-1 hash key that should be constructed from the specified data.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[sha1Hex](#sha1Hex(java.lang.String...))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)... strings)`
Returns SHA-1 hash key that should be constructed from the specified strings.
`static void`
`[sortStrings](#sortStrings(java.util.Vector))([Vector](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Vector.html) elem)`
Sorts elements in strings' vector
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[splitString](#splitString(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 boolean returnDelimiter)`
Splits string
`static void`
`[swapVector](#swapVector(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) v)`
Deprecated.
use [`Collections.reverse(java.util.List<?>)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collections.html#reverse(java.util.List))
`static void`
`[synchronizeDirectories](#synchronizeDirectories(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)`
Synchronize two directories.
`static byte[]`
`[toByteArray](#toByteArray(java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) stream)`
Copies the given file into the array of bytes.
`static byte[]`
`[toByteArray](#toByteArray(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bytes)`
Returns byte array from string formatted in toString(byte[]) method.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(byte%5B%5D))(byte[] data)`
Returns string representation of the given byte array.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) inputStream)`
Get String representation of inputStream
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> strings)`
Get String representation of given strings collection
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[trim](#trim(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trashBegin,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trashEnd)`
Removes from begin and end given Strings.
`static byte[]`
`[uncompressData](#uncompressData(byte%5B%5D))(byte[] data)`
Uncompresses specified data using gzip input stream and returns the result as bytes array.
`static void`
`[zipDir](#zipDir(java.lang.String,java.util.zip.ZipOutputStream))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dir2zip,
 [ZipOutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipOutputStream.html) zos)`
Compress specified directory recursively to the specified stream.
Methods inherited from class com.nomagic.utils.[CameoUtilities](CameoUtilities.html)
`[copy](CameoUtilities.html#copy(java.io.Reader,java.io.Writer)), [hasExtension](CameoUtilities.html#hasExtension(java.lang.String,java.lang.String)), [hasExtension](CameoUtilities.html#hasExtension(java.lang.String,java.util.List)), [isEqual](CameoUtilities.html#isEqual(java.lang.Object%5B%5D,java.lang.Object%5B%5D)), [isEqual](CameoUtilities.html#isEqual(java.lang.Object,java.lang.Object)), [removeExtension](CameoUtilities.html#removeExtension(java.lang.String,java.util.Collection)), [removeFromLine](CameoUtilities.html#removeFromLine(java.lang.String,java.lang.String)), [replaceNewLine](CameoUtilities.html#replaceNewLine(java.lang.String,java.lang.String)), [toString](CameoUtilities.html#toString(java.io.InputStream,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Utilities
public Utilities()
 ============ METHOD DETAIL ========== 
Method Details
createStringRepresentation
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStringRepresentation([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) value)
deepPointsClone
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> deepPointsClone([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> v)
Makes a deep clone of vector that contains points.
Parameters:
`v` - List of point.
Returns:
vector
deepPointsClone
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> deepPointsClone([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> v,
 boolean cloneList)
Makes a deep clone of vector that contains points.
Parameters:
`v` - List of point.
`cloneList` - True if clone to new list.
Returns:
vector
replace
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) replace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) replaceWith)
Replaces string fragment with another string
Parameters:
`src` - Source string.
`pattern` - String pattern.
`replaceWith` - The another string.
Returns:
string.
match
public static boolean match([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)
Checks if given string matches given pattern with wild cards.
 Empty string does not match any pattern.
Parameters:
`pattern` - pattern with wildcards
`string` - string
Returns:
boolean true if string matches pattern
matchIncludingEmpty
public static boolean matchIncludingEmpty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)
Checks if given string matches given pattern with wild cards.
 Empty string matches pattern "*".
Parameters:
`pattern` - pattern with wildcards
`string` - string
Returns:
boolean true if string matches pattern
sortStrings
public static void sortStrings([Vector](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Vector.html) elem)
Sorts elements in strings' vector
Parameters:
`elem` - The given vector.
clearLine
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clearLine([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) line,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trash)
removes from line ends wanted characters
Parameters:
`line` - The given line.
`trash` - characters as string.
Returns:
String.
clearAllLine
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clearAllLine([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trash)
Removes all trash from string
Parameters:
`src` - String that be removed trash
`trash` - Trash string.
Returns:
String.
merge
public static <T> void merge([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> source,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> v)
Merges two vector. Removes non existing in vector v elements from vector source.
 Adds existing in v into source.
 Result vector is source
Parameters:
`source` - source list.
`v` - The given vector.
append
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> source,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends T> v,
 boolean allowDublication)
Deprecated.
Use [`CollectionUtils.append(java.util.Collection, java.util.Collection, boolean)`](CollectionUtils.html#append(java.util.Collection,java.util.Collection,boolean))
append
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static <T> [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> append([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> source,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html)<? extends T> it,
 boolean allowDublication)
Deprecated.
Use [`CollectionUtils.append(java.util.Collection, java.util.Iterator, boolean)`](CollectionUtils.html#append(java.util.Collection,java.util.Iterator,boolean))
contains
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean contains([Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html) it,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Deprecated.
Use [`CollectionUtils.contains(java.util.Iterator, Object)`](CollectionUtils.html#contains(java.util.Iterator,java.lang.Object))
containsAny
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean containsAny([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) location,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) what)
Deprecated.
Use [`CollectionUtils.containsAny(java.util.Collection, java.util.Collection)`](CollectionUtils.html#containsAny(java.util.Collection,java.util.Collection))
clearFromEveryLine
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) clearFromEveryLine([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) mask)
Divides given string into lines and from every line beginning
 and end removes all chars from given string mask.
Parameters:
`text` - The given string.
`mask` - The given string mark.
Returns:
String.
countOccurrences
public static int countOccurrences([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string,
 char c)
Returns the number of times the character c appears in a string.
Parameters:
`string` - The given string
`c` - character
Returns:
number of time
removeNonUtf8CompliantCharacters
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeNonUtf8CompliantCharacters([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) inString)
fitInRectangle
public static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) fitInRectangle([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) small,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) big)
recalculate bounds to fit in rectangle
Parameters:
`small` - Small rectangle
`big` - Big rectangle
Returns:
New rectangle
containsOnlyFiles
public static boolean containsOnlyFiles([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) list)
Indicates if given list contains only file objects.
Parameters:
`list` - list to check.
Returns:
true if given list contains only file objects, false otherwise.
containsNonDirectory
public static boolean containsNonDirectory([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html)> fileList)
Parameters:
`fileList` - list of File objects
Returns:
true if there is at least one file that is not a directory
coverRectangle
public static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) coverRectangle([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) inner,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) outer)
Moves outer rectangle in such way that it must cover inner one (if outer is smaller than inner resizes outer).
 Modifies outer and returns it.
Parameters:
`inner` - Inner rectangle.
`outer` - Outer rectangle.
Returns:
Moved rectangle.
createRectFromList
@CheckForNullpublic static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) createRectFromList([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html)> v)
Creates rectangle from vector of points.
Parameters:
`v` - List of point
Returns:
null if vector was empty
swapVector
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void swapVector([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) v)
Deprecated.
use [`Collections.reverse(java.util.List<?>)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collections.html#reverse(java.util.List))
Swaps vector ( first element will be last, same with others elements)
Parameters:
`v` - List that be swapped.
getFileWithoutExtension
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileWithoutExtension([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filename)
Returns file name without extension (removes chars from last "." to end of string)
Parameters:
`filename` - The given file name
getFileWitoutExtention
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileWitoutExtention([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filename)
Deprecated.
type error in name
Returns file name without extension (removes chars from last "." to end of string)
Parameters:
`filename` - The given file name
See Also:
[`getFileWithoutExtension(String)`](#getFileWithoutExtension(java.lang.String))
getFileExtension
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileExtension([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Get The given file extension.
Parameters:
`file` - The given file
Returns:
File extension
getFileExtension
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileExtension([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)
Get the given file extension.
Parameters:
`fileName` - file name
Returns:
File extension
getFileName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
getCurrentDateFormatted
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCurrentDateFormatted()
removeComments
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeComments([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) body)
Removes / * * / comments from body.
Parameters:
`body` - String body.
Returns:
body without comment.
createCollection
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static <E extends [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)> E createCollection([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html)<E> collection,
 [Iterator](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html) it)
Deprecated.
Use [`CollectionUtils.createCollection(Class, java.util.Iterator)`](CollectionUtils.html#createCollection(java.lang.Class,java.util.Iterator))
notDublicatedList
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) notDublicatedList([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) col)
Deprecated.
Use [`CollectionUtils.notDuplicatedList(java.util.Collection)`](CollectionUtils.html#notDuplicatedList(java.util.Collection))
trim
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trim([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trashBegin,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trashEnd)
Removes from begin and end given Strings.
Parameters:
`src` - The given string.
`trashBegin` - Trash string that is a beginning.
`trashEnd` - Trash string that is a ending.
Returns:
String
replaceEpsString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) replaceEpsString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) aStr)
Replace special char for Eps format string
Parameters:
`aStr` - The given string.
Returns:
String
copy
public static void copy([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output,
 long crc,
 boolean closeInput)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Copies all bytes from InputStream into OutputStream. Closes the streams.
Parameters:
`input` - the input stream.
`output` - the output stream.
`crc` - crc to check. -1 if do not check crc.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
copy
public static void copy([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output,
 @CheckForNull
 [Checksum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/Checksum.html) checksum)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Copies all bytes from InputStream into OutputStream
Parameters:
`input` - the input stream.
`output` - the output stream.
`checksum` - checksum.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)` - exception
copy
public static void copy([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Copies all bytes from InputStream into OutputStream. Closes the streams.
Parameters:
`input` - the input stream.
`output` - the output stream.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
copyFile
public static boolean copyFile([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sourceName,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dstName)
Copy source file to destination file.
Parameters:
`sourceName` - Source file name.
`dstName` - destination file name.
Returns:
True if work successful.
copyFile
public static boolean copyFile([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)
Copy source file to destination file.
Parameters:
`source` - Source file.
`destination` - destination file.
Returns:
true if successful.
copyDirectory
public static boolean copyDirectory([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)
Copy all directory recursively
extractZip
public static void extractZip([ZipFile](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipFile.html) zipFile,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dstDir)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Extracts files from Zip archive
Parameters:
`zipFile` - Zip archive file
`dstDir` - name of the destination directory
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
extractZip
public static [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> extractZip([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) is,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dstDir,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> onlyTheseEntries,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> skipTheseEntries)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Extracts files from Zip archive
Parameters:
`is` - Input Stream - must be valid zip file
`dstDir` - destination directory
`onlyTheseEntries` - if not null specifies which entries must be extracted.
`skipTheseEntries` - if not null specifies which entries should be skiped.
Returns:
extracted entry names.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
toByteArray
public static byte[] toByteArray([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) stream)
Copies the given file into the array of bytes.
Parameters:
`stream` - the given file.
Returns:
the byte array with the context of the file;null if some errors occurs
getItemWithText
public static [JMenuItem](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html) getItemWithText([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) menu,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
Returns inner component (not recursively) with given text.
Parameters:
`menu` - The given JPopupMenu.
`text` - The given text.
Returns:
JMenuItem.
createCursor
public static [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) createCursor([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cursorName)
Creates the cursor for given image.
Parameters:
`image` - the given image.
`pt` - the hot point.
`cursorName` - the cursor name.
Returns:
Cursor.
createCursor
public static [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html) createCursor([Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cursorName)
Creates the cursor for given icon.
Parameters:
`icon` - the given icon.
`pt` - the hot point.
`cursorName` - the cursor name.
Returns:
Cursor.
getAsStringKeyStrokes
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAsStringKeyStrokes([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<[KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html)> shortcuts,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bracketFirst,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bracketSecond)
Constructs the string representation of the given key strokes.
Parameters:
`shortcuts` - The given key strokes.
`bracketFirst` - Open bracket.
`bracketSecond` - Close bracket.
Returns:
String.
getAsString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAsString(@CheckForNull
 [KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) e)
Constructs the string representation of the given key stroke.
Parameters:
`e` - the given key stroke.
Returns:
String representation.
isValidKeyCode
public static boolean isValidKeyCode(int keyCode)
Checks if given code is correct one or not.
Parameters:
`keyCode` - The given key code.
Returns:
true if given code is not CTRL, SHIFT, META or ALT.
isPrintableChar
public static boolean isPrintableChar(char c)
Checks if char is printable or not.
Parameters:
`c` - char which ic checked.
Returns:
true if char is printable.
toString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString(byte[] data)
Returns string representation of the given byte array.
Parameters:
`data` - the given bytes array.
Returns:
the string representation (every byte is represented as hex string separated by space)
toByteArray
public static byte[] toByteArray([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bytes)
Returns byte array from string formatted in toString(byte[]) method.
Parameters:
`bytes` - the given string.
Returns:
the byte array.
areChildrenDisabled
public static boolean areChildrenDisabled([JMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenu.html) menu)
Are all children disabled?
Parameters:
`menu` - the menu
Returns:
true, if all menu children are disabled
normalize
public static void normalize([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rectangle,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) firstCorner,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) secondCorner)
Normalizes rectangle; Calculates rectangle size and location using firstCorner and secondCorner.
Parameters:
`rectangle` - rectangle to normalize
`firstCorner` - first corner
`secondCorner` - second corner
normalize
public static void normalize([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
normalizes rectangle mRectToDraw;
Parameters:
`rect` - rectangle to normalize
getTempDir
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTempDir()
Returns System temp directory.
Returns:
string.
openHttpURLConnection
public static [HttpURLConnection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html) openHttpURLConnection([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pageHttpAddress,
 [ProxyServerData](../license/utils/ProxyServerData.html) proxyServerData)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Opens HttpURLConnection according given page address and proxy server data.
Parameters:
`pageHttpAddress` - page address with protocol e.g `"http://www.nomagic.com"`
`proxyServerData` - proxy server data
Returns:
HttpURLConnection.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
isUseProxy
public static boolean isUseProxy([ProxyServerData](../license/utils/ProxyServerData.html) proxy)
Checks if use proxy server according given proxy server data
Parameters:
`proxy` - proxy data.
Returns:
true if use; otherwise - false
getHtmlPage
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHtmlPage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pageHttpAddress,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters,
 [ProxyServerData](../license/utils/ProxyServerData.html) proxy)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Returns HTML page
Parameters:
`pageHttpAddress` - page address with protocol e.g `"http://www.nomagic.com"`
`parameters` - parameters for POST method (null if no data to POST)
`proxy` - proxy server data
Returns:
HTML page
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
toString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) inputStream)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Get String representation of inputStream
Parameters:
`inputStream` - The given inputStream
Returns:
String representation.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
toString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> strings)
Get String representation of given strings collection
Parameters:
`strings` - many strings
Returns:
String representation.
sendHttpParameters
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static void sendHttpParameters([HttpURLConnection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html) connection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Deprecated.
use `HttpUtilities.sendHttpParameters(HttpURLConnection, String)`
Send Http Parameters.
Parameters:
`connection` - HttpURLConnection
`parameters` - Http Parameters.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
constructHttpParameter
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) constructHttpParameter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameter,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Constructs http parameter
Parameters:
`parameter` - parameter name
`value` - parameter value
Returns:
constructed parameter
addHttpParameter
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) addHttpParameter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameter,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
Adds http parameter to given parameters string
Parameters:
`parameters` - parameters
`parameter` - parameter name to add
`value` - parameter value to add
Returns:
constructed parameters string
concatHttpParameter
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) concatHttpParameter([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters1,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) parameters2)
Concatenate given http parameters
Parameters:
`parameters1` -
`parameters2` -
Returns:
concatenated parameters
insertSeparators
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) insertSeparators(char[] chars,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 int groupSize)
Constructs string from arrays of chars.
 String characters are grouped into groups. Groups are separated by separator.
Parameters:
`chars` - array of characters to divide
`separator` - group separator
`groupSize` - size if the group
Returns:
result string
removeSeparators
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeSeparators([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator)
Removes separators from specified str
Parameters:
`str` - string to unite
`separator` -
Returns:
str without separators
getBytes
public static byte[] getBytes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str)
Returns bytes of string. 2 bytes for every char.
distributeInteger
public static byte[] distributeInteger(int intValue,
 int size)
Distributes integer intValue into array of bytes.
 int is 4 bytes, so max array size is 4
Parameters:
`intValue` - int intValue to distribute
`size` - size of result array
Returns:
array of bytes
collectInteger
public static int collectInteger(byte[] bytes)
Makes int value from array of bytes
Parameters:
`bytes` - array of bytes
Returns:
int value
invokeAndWaitOnDispatcher
public static void invokeAndWaitOnDispatcher([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)
 throws [RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html)
Executes given runnable on event dispatcher. Note if current thread is interrupted
 after runnable is submitted to the queue this method throws exception but runnable will be run on EDT.
Parameters:
`r` - the given runnable
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html)`
invokeAndWaitOnDispatcherEvenInterrupted
public static void invokeAndWaitOnDispatcherEvenInterrupted([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)
 throws [RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html)
Executes given runnable on event dispatcher. Waits until r is finished even current thread is interrupted.
Parameters:
`r` - the given runnable
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html)`
invokeOnDispatcherOrLater
public static void invokeOnDispatcherOrLater([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) r)
If this thread is event dispatcher, than direct calls "run", else invoke on invoke later
Parameters:
`r` -
invokeLaterAfterCondition
public static void invokeLaterAfterCondition([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> condition)
Invokes runnable latter after condition is satisfied.
Parameters:
`runnable` - runnable which will be executed.
`condition` - condition condition after which satisfaction runnable will be executed.
invokeLaterAfterCondition
public static void invokeLaterAfterCondition([Runnable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html) runnable,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)> condition,
 int conditionCheckAttemptCount)
Invokes runnable latter after condition is satisfied.
Parameters:
`runnable` - runnable which will be executed.
`condition` - condition condition after which satisfaction runnable will be executed.
`conditionCheckAttemptCount` - attempts count of the condition check; if count is reached before the condition is satisfied, runnable will not be executed.
compareStreams
public static boolean compareStreams([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) oldStr,
 [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) newStr)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Compares two input streams.
Parameters:
`oldStr` - First input stream.
`newStr` - Second input stream.
Returns:
true if streams contains identical data.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
compareFiles
public static boolean compareFiles([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f1,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f2)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Compares two files
Parameters:
`f1` - First file.
`f2` - Second file.
Returns:
true if files contains identical data.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
deleteTree
public static void deleteTree(@Nonnull
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f)
Removes given directory and all its contents.
 File.delete fails if directory is not empty
Parameters:
`f` - file to delete
deleteTreeOnExit
public static void deleteTreeOnExit([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f)
Removes given file (directory and all its contents) on exit.
 File.delete fails if directory is not empty
Parameters:
`f` - file to delete
deleteDirContent
public static void deleteDirContent([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f)
Removes given directory contents.
 File.delete fails if directory is not empty
Parameters:
`f` - file to delete
getGrayIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [ResizableIcon](../ui/ResizableIcon.html) getGrayIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon)
Deprecated.
Use [`IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)`](../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component))
Returns grey(disabled) icon from given one.
Parameters:
`icon` - the given icon.
Returns:
disabled icon
getGrayIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic static [ResizableIcon](../ui/ResizableIcon.html) getGrayIcon(@CheckForNull
 [Icon](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html) icon,
 [Component](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html) component)
Deprecated.
Use [`IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)`](../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component))
Returns grey(disabled) icon from given one.
Parameters:
`icon` - the given icon.
`component` - component.
Returns:
disabled icon
makeEqual
public static void makeEqual([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) destination,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) source)
Make destination the same as source with minimum changes to destination
Parameters:
`destination` - List
`source` - List
getClassName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getClassName([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html) clazz)
Get class name.
Parameters:
`clazz` - The given class.
Returns:
Class name.
isAlphaNumeric
public static boolean isAlphaNumeric([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str)
mergeLists
public static <T> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> mergeLists([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> l1,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> l2)
Merges two lists into newly created one.
Parameters:
`l1` - first list.
`l2` - second list.
Returns:
newly created list with added elements from l1 and l2.
synchronizeDirectories
public static void synchronizeDirectories([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Synchronize two directories. If new file appears in source, it should appear in destination.
 If file is removed from destination it should not appear in destination again. Typical use for this method
 is when one directory has default settings, and another have working copy.
Parameters:
`source` - source directory.
`destination` - destination directory.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
splitString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] splitString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 boolean returnDelimiter)
Splits string
Parameters:
`str` - a string to be parsed.
`delimiter` - the delimiter.
`returnDelimiter` - flag indicating whether to include the delimiter in result.
Returns:
array of strings
implode
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) implode([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)
Returns a new String composed of copies of the collection elements joined together with a copy of the specified delimiter.
 Consider using [`String.join(CharSequence, Iterable)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.Iterable)).
Parameters:
`collection` - collection of elements.
`delimiter` - delimiter.
Returns:
joined string.
See Also:
[`String.join(CharSequence, Iterable)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.Iterable))
implode
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) implode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] values,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)
Deprecated.
Use [`String.join(CharSequence, CharSequence...)`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.CharSequence...))
parseExceptQuotes
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] parseExceptQuotes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd)
parses string by standard tokens, except parts wrapped in quotes
readFileSkipFirstLines
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) readFileSkipFirstLines([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file,
 int n)
Reads a file to string and skips a specified number of lines from the beginning.
Parameters:
`file` - - file to read.
`n` - - number of lines to skip from the beginning.
Returns:
file contents as string with skipped lines.
zipDir
public static void zipDir([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dir2zip,
 [ZipOutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipOutputStream.html) zos)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Compress specified directory recursively to the specified stream.
Parameters:
`dir2zip` - directory to zip.
`zos` - `ZipOutputStream` object.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)` - if any occurs during
compressData
public static byte[] compressData(byte[] data,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) zipEntryName)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Compresses specified data using zip output stream and returns the result as bytes array.
Parameters:
`data` - a data.
`zipEntryName` - name of how the data will be named in the archive.
Returns:
compressed data.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)` - if any occurs during compressing the data.
compressData
public static byte[] compressData(byte[] data)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Compresses specified data using gzip output stream and returns the result as bytes array.
Parameters:
`data` - a data.
Returns:
compressed data.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)` - if any occurs during compressing the data.
uncompressData
public static byte[] uncompressData(byte[] data)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Uncompresses specified data using gzip input stream and returns the result as bytes array.
Parameters:
`data` - a data.
Returns:
compressed data.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)` - if any occurs during compressing the data.
checkSystemProperty
public static boolean checkSystemProperty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 boolean defaultValue)
Checks given system (boolean) property value
Parameters:
`property` -
`defaultValue` -
Returns:
value of the system property, or defaultValue if system property is not set
checkProperty
public static boolean checkProperty([Properties](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html) properties,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) property,
 boolean defaultValue)
checkResolvableException
public static boolean checkResolvableException(boolean rule)
if rule is false and it's DEVELOPER mode throws [`IllegalStateException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html)
Returns:
rule
dumpThreads
public static void dumpThreads()
Dumps all threads to system out.
dumpThreads
public static void dumpThreads([PrintStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/PrintStream.html) out)
Dumps all threads to given stream.
reverseString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) reverseString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) source)
Given a string, returns a string with reversed characters.
Parameters:
`source` - string which has to be reversed.
Returns:
a string with reversed characters.
calculateTextWidth
public static int calculateTextWidth([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [FontMetrics](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/FontMetrics.html) metrics,
 int numberOfLines)
Calculates possible text longest text width of the given text splitted into lines.
Parameters:
`text` - text for which to calculate width.
`metrics` - font metrics according which to calculate.
`numberOfLines` - number of lines into which to split the text.
Returns:
calculated possible text width.
isHTMLText
public static boolean isHTMLText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Check the given string to see if it should trigger the
 html rendering logic.
Parameters:
`s` - the given string.
Returns:
true if given text is html, false otherwise.
ensureObjectIsInCollection
public static <T> void ensureObjectIsInCollection([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> collection,
 T object)
Ensures an object is in given collection.
 If it isn't, the object is added to it.
Parameters:
`collection` - collection in which to check object existence.
`object` - object to check.
encodeBase64
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) encodeBase64(byte[] abyte0)
Encodes data using base64 encoding.
Parameters:
`abyte0` - data for encoding
Returns:
encoded string
decodeBase64
public static byte[] decodeBase64([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) s)
Decode string using Base64 encoding.
Parameters:
`s` - string for decoding
Returns:
decoded data
hasModalDialogs
public static boolean hasModalDialogs([Window](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html) window)
Checks recursively if given window has modal dialog as child (or window itself is a modal dialog)
Parameters:
`window` - window
Returns:
true if modal dialog is found
removeNewLines
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeNewLines([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)
Removes new lines from the string.
Parameters:
`string` - string for which to remove new lines.
Returns:
string with removed new lines.
checkIsInstallRootWritable
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment runtime)
Get message for install root read only error. Returns null if install root is writable. Method is suitable
 for read only checking.
Parameters:
`runtime` - Application runtime.
Returns:
Message for install root read only error or null if install root is writable
checkIsInstallRootWritable
@CheckForNullpublic static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment runtime,
 boolean skipWinUAC)
Get message for install root read only error. Returns null if install root is writable. Method is suitable
 for read only checking.
Parameters:
`runtime` - runtime environment.
`skipWinUAC` - skip checking writable installation root if Windows is supporting UAC.
Returns:
Message for install root read only error or null if install root is writable
main
public static void main([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] args)
getVersionFromInternal
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getVersionFromInternal([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) internal)
 throws [NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html),
[IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)
Convert internal MagicDraw style version to human version in 17.0.2 format.
Parameters:
`internal` - Internal version.
Returns:
Human version
Throws:
`[NumberFormatException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html)` - parse exception.
`[IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)` - if internal version is negative.
getVersionFromInternal
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getVersionFromInternal(int internal)
 throws [IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)
Convert internal MagicDraw style version to human version in 17.0.2 format.
Parameters:
`internal` - Internal version.
Returns:
human version
Throws:
`[IndexOutOfBoundsException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html)` - if internal version is negative.
containSameElements
public static boolean containSameElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection1,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<?> collection2)
arrayHash
public static int arrayHash(byte[] array)
Calculate hash code for array of bytes
Parameters:
`array` - bytes
Returns:
hash code
isStreamEmpty
public static boolean isStreamEmpty([URL](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html) url)
Check if it is possible to open a stream from a given URL and that stream is not empty
Parameters:
`url` - url to check
Returns:
true if not empty stream is opened from a given url
insertPeriodically
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) insertPeriodically([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) insert,
 int period)
sha1Hex
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sha1Hex([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)... strings)
 throws [NoSuchAlgorithmException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html)
Returns SHA-1 hash key that should be constructed from the specified strings.
Parameters:
`strings` - array of strings.
Returns:
SHA-1 hash key.
Throws:
`[NoSuchAlgorithmException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html)`
sha1Hex
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) sha1Hex(byte[] data)
 throws [NoSuchAlgorithmException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html)
Returns SHA-1 hash key that should be constructed from the specified data.
Parameters:
`data` - array of bytes
Returns:
SHA-1 hash key.
Throws:
`[NoSuchAlgorithmException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html)`
getDistance
public static <E> int getDistance(E from,
 E to,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<E,[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<E>> connectedNodes)
Calculate minimal distance in graph.
Type Parameters:
`E` - type of node.
Parameters:
`from` - starting point in graph.
`to` - destination point in graph.
`connectedNodes` - function to get connected edges.
Returns:
minimal number of steps required to get from node from to node to. Return -1 if nodes are not connected.
contentEquals
public static boolean contentEquals([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input1,
 [InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input2)
Compare content of two streams.
Parameters:
`input1` - first stream.
`input2` - another stream.
Returns:
true if stream provides exactly same content.
getSystemDateFormat
public static [DateFormat](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html) getSystemDateFormat(int style)
Returns system date format. Ordinary Java date format getting methods returns format taken from locale, which can be different from real system date format,
 set in calendar settings.
Parameters:
`style` - Format style (e.g. [`DateFormat.SHORT`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html#SHORT), [`DateFormat.LONG`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html#LONG)).
Returns:
System date format. If can't get it, returns SimpleDateFormat.
isFileNameValid
public static boolean isFileNameValid([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) fileName)
Returns if given file name is valid to be created.
Parameters:
`fileName` - file name
Returns:
true if file name can be created or already exists, else false
excludeCommonElements
public static <T> [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)<T> excludeCommonElements([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> first,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<T> second)
Creates result collection which contains not common elements from two arguments
Type Parameters:
`T` - type of collection
Parameters:
`first` - first collection
`second` - second collection
Returns:
not common elements of two arguments
isNameValid
public static boolean isNameValid(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)
getThreadsInfo
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getThreadsInfo()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.utils</a></div>
<h1 class="title" title="Class Utilities">Class Utilities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="CameoUtilities.html" title="class in com.nomagic.utils">com.nomagic.utils.CameoUtilities</a>
<div class="inheritance">com.nomagic.utils.Utilities</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Utilities</span>
<span class="extends-implements">extends <a href="CameoUtilities.html" title="class in com.nomagic.utils">CameoUtilities</a></span></div>
<div class="block">General purpose utilities.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">Utilities</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#addHttpParameter(java.lang.String,java.lang.String,java.lang.String)">addHttpParameter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Adds http parameter to given parameters string</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Collection,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt; v,
 boolean allowDublication)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#append(java.util.Collection,java.util.Collection,boolean)"><code>CollectionUtils.append(java.util.Collection, java.util.Collection, boolean)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#append(java.util.Collection,java.util.Iterator,boolean)">append</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; it,
 boolean allowDublication)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#append(java.util.Collection,java.util.Iterator,boolean)"><code>CollectionUtils.append(java.util.Collection, java.util.Iterator, boolean)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#areChildrenDisabled(javax.swing.JMenu)">areChildrenDisabled</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenu.html" title="class or interface in javax.swing">JMenu</a> menu)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Are all children disabled?</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#arrayHash(byte%5B%5D)">arrayHash</a><wbr/>(byte[] array)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculate hash code for array of bytes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#calculateTextWidth(java.lang.String,java.awt.FontMetrics,int)">calculateTextWidth</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/FontMetrics.html" title="class or interface in java.awt">FontMetrics</a> metrics,
 int numberOfLines)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculates possible text longest text width of the given text splitted into lines.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment)">checkIsInstallRootWritable</a><wbr/>(com.nomagic.runtime.RuntimeEnvironment runtime)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get message for install root read only error.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment,boolean)">checkIsInstallRootWritable</a><wbr/>(com.nomagic.runtime.RuntimeEnvironment runtime,
 boolean skipWinUAC)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get message for install root read only error.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkProperty(java.util.Properties,java.lang.String,boolean)">checkProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 boolean defaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkResolvableException(boolean)">checkResolvableException</a><wbr/>(boolean rule)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">if rule is false and it's DEVELOPER mode throws <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang"><code>IllegalStateException</code></a></div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkSystemProperty(java.lang.String,boolean)">checkSystemProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 boolean defaultValue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks given system (boolean) property value</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAllLine(java.lang.String,java.lang.String)">clearAllLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all trash from string</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearFromEveryLine(java.lang.String,java.lang.String)">clearFromEveryLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mask)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Divides given string into lines and from every line beginning
 and end removes all chars from given string mask.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearLine(java.lang.String,java.lang.String)">clearLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">removes from line ends wanted characters</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#collectInteger(byte%5B%5D)">collectInteger</a><wbr/>(byte[] bytes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes int value from array of bytes</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compareFiles(java.io.File,java.io.File)">compareFiles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compares two files</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compareStreams(java.io.InputStream,java.io.InputStream)">compareStreams</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> oldStr,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> newStr)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compares two input streams.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compressData(byte%5B%5D)">compressData</a><wbr/>(byte[] data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compresses specified data using gzip output stream and returns the result as bytes array.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compressData(byte%5B%5D,java.lang.String)">compressData</a><wbr/>(byte[] data,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> zipEntryName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compresses specified data using zip output stream and returns the result as bytes array.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#concatHttpParameter(java.lang.String,java.lang.String)">concatHttpParameter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Concatenate given http parameters</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#constructHttpParameter(java.lang.String,java.lang.String)">constructHttpParameter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs http parameter</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#contains(java.util.Iterator,java.lang.Object)">contains</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#contains(java.util.Iterator,java.lang.Object)"><code>CollectionUtils.contains(java.util.Iterator, Object)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#containSameElements(java.util.Collection,java.util.Collection)">containSameElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#containsAny(java.util.Collection,java.util.Collection)">containsAny</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> location,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> what)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#containsAny(java.util.Collection,java.util.Collection)"><code>CollectionUtils.containsAny(java.util.Collection, java.util.Collection)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#containsNonDirectory(java.util.List)">containsNonDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; fileList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#containsOnlyFiles(java.util.List)">containsOnlyFiles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> list)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if given list contains only file objects.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#contentEquals(java.io.InputStream,java.io.InputStream)">contentEquals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compare content of two streams.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.InputStream,java.io.OutputStream)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies all bytes from InputStream into OutputStream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.InputStream,java.io.OutputStream,long,boolean)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output,
 long crc,
 boolean closeInput)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies all bytes from InputStream into OutputStream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.InputStream,java.io.OutputStream,java.util.zip.Checksum)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/Checksum.html" title="class or interface in java.util.zip">Checksum</a> checksum)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies all bytes from InputStream into OutputStream</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyDirectory(java.io.File,java.io.File)">copyDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copy all directory recursively</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyFile(java.io.File,java.io.File)">copyFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copy source file to destination file.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyFile(java.lang.String,java.lang.String)">copyFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sourceName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copy source file to destination file.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#countOccurrences(java.lang.String,char)">countOccurrences</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 char c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the number of times the character c appears in a string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#coverRectangle(java.awt.Rectangle,java.awt.Rectangle)">coverRectangle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> inner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> outer)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Moves outer rectangle in such way that it must cover inner one (if outer is smaller than inner resizes outer).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static &lt;E extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&gt;<br/>E</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createCollection(java.lang.Class,java.util.Iterator)">createCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;E&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#createCollection(java.lang.Class,java.util.Iterator)"><code>CollectionUtils.createCollection(Class, java.util.Iterator)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCursor(java.awt.Image,java.awt.Point,java.lang.String)">createCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cursorName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates the cursor for given image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCursor(javax.swing.Icon,java.awt.Point,java.lang.String)">createCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cursorName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates the cursor for given icon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRectFromList(java.util.List)">createRectFromList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates rectangle from vector of points.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringRepresentation(java.util.Collection)">createStringRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#decodeBase64(java.lang.String)">decodeBase64</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Decode string using Base64 encoding.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deepPointsClone(java.util.List)">deepPointsClone</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a deep clone of vector that contains points.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deepPointsClone(java.util.List,boolean)">deepPointsClone</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v,
 boolean cloneList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a deep clone of vector that contains points.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deleteDirContent(java.io.File)">deleteDirContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes given directory contents.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deleteTree(java.io.File)">deleteTree</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes given directory and all its contents.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deleteTreeOnExit(java.io.File)">deleteTreeOnExit</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes given file (directory and all its contents) on exit.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#distributeInteger(int,int)">distributeInteger</a><wbr/>(int intValue,
 int size)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Distributes integer intValue into array of bytes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#dumpThreads()">dumpThreads</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dumps all threads to system out.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#dumpThreads(java.io.PrintStream)">dumpThreads</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/PrintStream.html" title="class or interface in java.io">PrintStream</a> out)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dumps all threads to given stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#encodeBase64(byte%5B%5D)">encodeBase64</a><wbr/>(byte[] abyte0)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Encodes data using base64 encoding.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ensureObjectIsInCollection(java.util.Collection,T)">ensureObjectIsInCollection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 T object)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Ensures an object is in given collection.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;T&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#excludeCommonElements(java.util.Collection,java.util.Collection)">excludeCommonElements</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; first,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; second)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates result collection which contains not common elements from two arguments</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#extractZip(java.io.InputStream,java.lang.String,java.util.Collection,java.util.Collection)">extractZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> is,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; onlyTheseEntries,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; skipTheseEntries)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extracts files from Zip archive</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#extractZip(java.util.zip.ZipFile,java.lang.String)">extractZip</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipFile.html" title="class or interface in java.util.zip">ZipFile</a> zipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstDir)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Extracts files from Zip archive</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fitInRectangle(java.awt.Rectangle,java.awt.Rectangle)">fitInRectangle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> small,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> big)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">recalculate bounds to fit in rectangle</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAsString(javax.swing.KeyStroke)">getAsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs the string representation of the given key stroke.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAsStringKeyStrokes(java.util.List,java.lang.String,java.lang.String)">getAsStringKeyStrokes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a>&gt; shortcuts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bracketFirst,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bracketSecond)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs the string representation of the given key strokes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getBytes(java.lang.String)">getBytes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns bytes of string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getClassName(java.lang.Class)">getClassName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get class name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentDateFormatted()">getCurrentDateFormatted</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;E&gt; int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getDistance(E,E,java.util.function.Function)">getDistance</a><wbr/>(E from,
 E to,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;E,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;&gt; connectedNodes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Calculate minimal distance in graph.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileExtension(java.io.File)">getFileExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get The given file extension.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileExtension(java.lang.String)">getFileExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get the given file extension.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileName(java.lang.String)">getFileName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileWithoutExtension(java.lang.String)">getFileWithoutExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns file name without extension (removes chars from last "." to end of string)</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFileWitoutExtention(java.lang.String)">getFileWitoutExtention</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">type error in name</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getGrayIcon(javax.swing.Icon)">getGrayIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component)"><code>IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a href="../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getGrayIcon(javax.swing.Icon,java.awt.Component)">getGrayIcon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component)"><code>IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getHtmlPage(java.lang.String,java.lang.String,com.nomagic.license.utils.ProxyServerData)">getHtmlPage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pageHttpAddress,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters,
 <a href="../license/utils/ProxyServerData.html" title="class in com.nomagic.license.utils">ProxyServerData</a> proxy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns HTML page</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html" title="class or interface in javax.swing">JMenuItem</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getItemWithText(javax.swing.JPopupMenu,java.lang.String)">getItemWithText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> menu,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns inner component (not recursively) with given text.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html" title="class or interface in java.text">DateFormat</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getSystemDateFormat(int)">getSystemDateFormat</a><wbr/>(int style)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns system date format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTempDir()">getTempDir</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns System temp directory.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getThreadsInfo()">getThreadsInfo</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionFromInternal(int)">getVersionFromInternal</a><wbr/>(int internal)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert internal MagicDraw style version to human version in 17.0.2 format.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getVersionFromInternal(java.lang.String)">getVersionFromInternal</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> internal)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Convert internal MagicDraw style version to human version in 17.0.2 format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasModalDialogs(java.awt.Window)">hasModalDialogs</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> window)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks recursively if given window has modal dialog as child (or window itself is a modal dialog)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#implode(java.lang.String%5B%5D,java.lang.String)">implode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] values,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.CharSequence...)" title="class or interface in java.lang"><code>String.join(CharSequence, CharSequence...)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#implode(java.util.Collection,java.lang.String)">implode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns a new String composed of copies of the collection elements joined together with a copy of the specified delimiter.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#insertPeriodically(java.lang.String,java.lang.String,int)">insertPeriodically</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> insert,
 int period)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#insertSeparators(char%5B%5D,java.lang.String,int)">insertSeparators</a><wbr/>(char[] chars,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 int groupSize)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs string from arrays of chars.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeAndWaitOnDispatcher(java.lang.Runnable)">invokeAndWaitOnDispatcher</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes given runnable on event dispatcher.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeAndWaitOnDispatcherEvenInterrupted(java.lang.Runnable)">invokeAndWaitOnDispatcherEvenInterrupted</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Executes given runnable on event dispatcher.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeLaterAfterCondition(java.lang.Runnable,java.util.function.Supplier)">invokeLaterAfterCondition</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; condition)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Invokes runnable latter after condition is satisfied.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeLaterAfterCondition(java.lang.Runnable,java.util.function.Supplier,int)">invokeLaterAfterCondition</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; condition,
 int conditionCheckAttemptCount)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Invokes runnable latter after condition is satisfied.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#invokeOnDispatcherOrLater(java.lang.Runnable)">invokeOnDispatcherOrLater</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">If this thread is event dispatcher, than direct calls "run", else invoke on invoke later</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAlphaNumeric(java.lang.String)">isAlphaNumeric</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isFileNameValid(java.lang.String)">isFileNameValid</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns if given file name is valid to be created.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isHTMLText(java.lang.String)">isHTMLText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check the given string to see if it should trigger the
 html rendering logic.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isNameValid(java.lang.String)">isNameValid</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isPrintableChar(char)">isPrintableChar</a><wbr/>(char c)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if char is printable or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isStreamEmpty(java.net.URL)">isStreamEmpty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Check if it is possible to open a stream from a given URL and that stream is not empty</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseProxy(com.nomagic.license.utils.ProxyServerData)">isUseProxy</a><wbr/>(<a href="../license/utils/ProxyServerData.html" title="class in com.nomagic.license.utils">ProxyServerData</a> proxy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if use proxy server according given proxy server data</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isValidKeyCode(int)">isValidKeyCode</a><wbr/>(int keyCode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given code is correct one or not.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#main(java.lang.String%5B%5D)">main</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#makeEqual(java.util.List,java.util.List)">makeEqual</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> destination,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Make destination the same as source with minimum changes to destination</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#match(java.lang.String,java.lang.String)">match</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given string matches given pattern with wild cards.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#matchIncludingEmpty(java.lang.String,java.lang.String)">matchIncludingEmpty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given string matches given pattern with wild cards.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#merge(java.util.List,java.util.List)">merge</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; v)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Merges two vector.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T&gt; <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#mergeLists(java.util.List,java.util.List)">mergeLists</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; l1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; l2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Merges two lists into newly created one.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalize(java.awt.Rectangle)">normalize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">normalizes rectangle mRectToDraw;</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point)">normalize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rectangle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> firstCorner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> secondCorner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Normalizes rectangle; Calculates rectangle size and location using firstCorner and secondCorner.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#notDublicatedList(java.util.Collection)">notDublicatedList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> col)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#notDuplicatedList(java.util.Collection)"><code>CollectionUtils.notDuplicatedList(java.util.Collection)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html" title="class or interface in java.net">HttpURLConnection</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#openHttpURLConnection(java.lang.String,com.nomagic.license.utils.ProxyServerData)">openHttpURLConnection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pageHttpAddress,
 <a href="../license/utils/ProxyServerData.html" title="class in com.nomagic.license.utils">ProxyServerData</a> proxyServerData)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Opens HttpURLConnection according given page address and proxy server data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#parseExceptQuotes(java.lang.String)">parseExceptQuotes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">parses string by standard tokens, except parts wrapped in quotes</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#readFileSkipFirstLines(java.io.File,int)">readFileSkipFirstLines</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 int n)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Reads a file to string and skips a specified number of lines from the beginning.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeComments(java.lang.String)">removeComments</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> body)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes / *       * /  comments from body.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeNewLines(java.lang.String)">removeNewLines</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes new lines from the string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeNonUtf8CompliantCharacters(java.lang.String)">removeNonUtf8CompliantCharacters</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inString)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSeparators(java.lang.String,java.lang.String)">removeSeparators</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes separators from specified str</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replace(java.lang.String,java.lang.String,java.lang.String)">replace</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replaceWith)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces string fragment with another string</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceEpsString(java.lang.String)">replaceEpsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> aStr)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replace special char for Eps format string</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#reverseString(java.lang.String)">reverseString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a string, returns a string with reversed characters.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#sendHttpParameters(java.net.HttpURLConnection,java.lang.String)">sendHttpParameters</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html" title="class or interface in java.net">HttpURLConnection</a> connection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HttpUtilities.sendHttpParameters(HttpURLConnection, String)</code></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sha1Hex(byte%5B%5D)">sha1Hex</a><wbr/>(byte[] data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns SHA-1 hash key that should be constructed from the specified data.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sha1Hex(java.lang.String...)">sha1Hex</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... strings)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns SHA-1 hash key that should be constructed from the specified strings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sortStrings(java.util.Vector)">sortStrings</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Vector.html" title="class or interface in java.util">Vector</a> elem)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sorts elements in strings' vector</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#splitString(java.lang.String,java.lang.String,boolean)">splitString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 boolean returnDelimiter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Splits string</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#swapVector(java.util.List)">swapVector</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> v)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collections.html#reverse(java.util.List)" title="class or interface in java.util"><code>Collections.reverse(java.util.List&lt;?&gt;)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#synchronizeDirectories(java.io.File,java.io.File)">synchronizeDirectories</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Synchronize two directories.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toByteArray(java.io.InputStream)">toByteArray</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies the given file into the array of bytes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toByteArray(java.lang.String)">toByteArray</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bytes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns byte array from string formatted in toString(byte[]) method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(byte%5B%5D)">toString</a><wbr/>(byte[] data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns string representation of the given byte array.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(java.io.InputStream)">toString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> inputStream)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get String representation of inputStream</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(java.util.Collection)">toString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; strings)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get String representation of given strings collection</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#trim(java.lang.String,java.lang.String,java.lang.String)">trim</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trashBegin,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trashEnd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes from begin and end given Strings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#uncompressData(byte%5B%5D)">uncompressData</a><wbr/>(byte[] data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Uncompresses specified data using gzip input stream and returns the result as bytes array.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#zipDir(java.lang.String,java.util.zip.ZipOutputStream)">zipDir</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dir2zip,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipOutputStream.html" title="class or interface in java.util.zip">ZipOutputStream</a> zos)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Compress specified directory recursively to the specified stream.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.utils.CameoUtilities">Methods inherited from class com.nomagic.utils.<a href="CameoUtilities.html" title="class in com.nomagic.utils">CameoUtilities</a></h3>
<code><a href="CameoUtilities.html#copy(java.io.Reader,java.io.Writer)">copy</a>, <a href="CameoUtilities.html#hasExtension(java.lang.String,java.lang.String)">hasExtension</a>, <a href="CameoUtilities.html#hasExtension(java.lang.String,java.util.List)">hasExtension</a>, <a href="CameoUtilities.html#isEqual(java.lang.Object%5B%5D,java.lang.Object%5B%5D)">isEqual</a>, <a href="CameoUtilities.html#isEqual(java.lang.Object,java.lang.Object)">isEqual</a>, <a href="CameoUtilities.html#removeExtension(java.lang.String,java.util.Collection)">removeExtension</a>, <a href="CameoUtilities.html#removeFromLine(java.lang.String,java.lang.String)">removeFromLine</a>, <a href="CameoUtilities.html#replaceNewLine(java.lang.String,java.lang.String)">replaceNewLine</a>, <a href="CameoUtilities.html#toString(java.io.InputStream,java.lang.String)">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<h3>Utilities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Utilities</span>()</div>
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
<section class="detail" id="createStringRepresentation(java.util.Collection)">
<h3>createStringRepresentation</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStringRepresentation</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="deepPointsClone(java.util.List)">
<h3>deepPointsClone</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">deepPointsClone</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</span></div>
<div class="block">Makes a deep clone of vector that contains points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - List of point.</dd>
<dt>Returns:</dt>
<dd>vector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deepPointsClone(java.util.List,boolean)">
<h3>deepPointsClone</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">deepPointsClone</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v,
 boolean cloneList)</span></div>
<div class="block">Makes a deep clone of vector that contains points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - List of point.</dd>
<dd><code>cloneList</code> - True if clone to new list.</dd>
<dt>Returns:</dt>
<dd>vector</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replace(java.lang.String,java.lang.String,java.lang.String)">
<h3>replace</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">replace</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replaceWith)</span></div>
<div class="block">Replaces string fragment with another string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>src</code> - Source string.</dd>
<dd><code>pattern</code> - String pattern.</dd>
<dd><code>replaceWith</code> - The another string.</dd>
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="match(java.lang.String,java.lang.String)">
<h3>match</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">match</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="block">Checks if given string matches given pattern with wild cards.
 Empty string does not match any pattern.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pattern</code> - pattern with wildcards</dd>
<dd><code>string</code> - string</dd>
<dt>Returns:</dt>
<dd>boolean true if string matches pattern</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="matchIncludingEmpty(java.lang.String,java.lang.String)">
<h3>matchIncludingEmpty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">matchIncludingEmpty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="block">Checks if given string matches given pattern with wild cards.
 Empty string matches pattern "*".</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pattern</code> - pattern with wildcards</dd>
<dd><code>string</code> - string</dd>
<dt>Returns:</dt>
<dd>boolean true if string matches pattern</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sortStrings(java.util.Vector)">
<h3>sortStrings</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sortStrings</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Vector.html" title="class or interface in java.util">Vector</a> elem)</span></div>
<div class="block">Sorts elements in strings' vector</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elem</code> - The given vector.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearLine(java.lang.String,java.lang.String)">
<h3>clearLine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">clearLine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</span></div>
<div class="block">removes from line ends wanted characters</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>line</code> - The given line.</dd>
<dd><code>trash</code> - characters as string.</dd>
<dt>Returns:</dt>
<dd>String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="clearAllLine(java.lang.String,java.lang.String)">
<h3>clearAllLine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">clearAllLine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</span></div>
<div class="block">Removes all trash from string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>src</code> - String that be removed trash</dd>
<dd><code>trash</code> - Trash string.</dd>
<dt>Returns:</dt>
<dd>String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="merge(java.util.List,java.util.List)">
<h3>merge</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">merge</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; v)</span></div>
<div class="block">Merges two vector. Removes non existing in vector v elements from vector source.
 Adds existing in v into source.
 Result vector is source</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source list.</dd>
<dd><code>v</code> - The given vector.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,java.util.Collection,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends T&gt; v,
 boolean allowDublication)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#append(java.util.Collection,java.util.Collection,boolean)"><code>CollectionUtils.append(java.util.Collection, java.util.Collection, boolean)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="append(java.util.Collection,java.util.Iterator,boolean)">
<h3>append</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt;</span> <span class="element-name">append</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;? extends T&gt; it,
 boolean allowDublication)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#append(java.util.Collection,java.util.Iterator,boolean)"><code>CollectionUtils.append(java.util.Collection, java.util.Iterator, boolean)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="contains(java.util.Iterator,java.lang.Object)">
<h3>contains</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#contains(java.util.Iterator,java.lang.Object)"><code>CollectionUtils.contains(java.util.Iterator, Object)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="containsAny(java.util.Collection,java.util.Collection)">
<h3>containsAny</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">containsAny</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> location,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> what)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#containsAny(java.util.Collection,java.util.Collection)"><code>CollectionUtils.containsAny(java.util.Collection, java.util.Collection)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="clearFromEveryLine(java.lang.String,java.lang.String)">
<h3>clearFromEveryLine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">clearFromEveryLine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> mask)</span></div>
<div class="block">Divides given string into lines and from every line beginning
 and end removes all chars from given string mask.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - The given string.</dd>
<dd><code>mask</code> - The given string mark.</dd>
<dt>Returns:</dt>
<dd>String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="countOccurrences(java.lang.String,char)">
<h3>countOccurrences</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">countOccurrences</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 char c)</span></div>
<div class="block">Returns the number of times the character c appears in a string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - The given string</dd>
<dd><code>c</code> - character</dd>
<dt>Returns:</dt>
<dd>number of time</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeNonUtf8CompliantCharacters(java.lang.String)">
<h3>removeNonUtf8CompliantCharacters</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeNonUtf8CompliantCharacters</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inString)</span></div>
</section>
</li>
<li>
<section class="detail" id="fitInRectangle(java.awt.Rectangle,java.awt.Rectangle)">
<h3>fitInRectangle</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">fitInRectangle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> small,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> big)</span></div>
<div class="block">recalculate bounds to fit in rectangle</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>small</code> - Small rectangle</dd>
<dd><code>big</code> - Big rectangle</dd>
<dt>Returns:</dt>
<dd>New rectangle</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsOnlyFiles(java.util.List)">
<h3>containsOnlyFiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">containsOnlyFiles</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> list)</span></div>
<div class="block">Indicates if given list contains only file objects.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>list</code> - list to check.</dd>
<dt>Returns:</dt>
<dd>true if given list contains only file objects, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containsNonDirectory(java.util.List)">
<h3>containsNonDirectory</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">containsNonDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a>&gt; fileList)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileList</code> - list of File objects</dd>
<dt>Returns:</dt>
<dd>true if there is at least one file that is not a directory</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coverRectangle(java.awt.Rectangle,java.awt.Rectangle)">
<h3>coverRectangle</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">coverRectangle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> inner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> outer)</span></div>
<div class="block">Moves outer rectangle in such way that it must cover inner one (if outer is smaller than inner resizes outer).
 Modifies outer and returns it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inner</code> - Inner rectangle.</dd>
<dd><code>outer</code> - Outer rectangle.</dd>
<dt>Returns:</dt>
<dd>Moved rectangle.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRectFromList(java.util.List)">
<h3>createRectFromList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">createRectFromList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</span></div>
<div class="block">Creates rectangle from vector of points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - List of point</dd>
<dt>Returns:</dt>
<dd>null if vector was empty</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="swapVector(java.util.List)">
<h3>swapVector</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">swapVector</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> v)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collections.html#reverse(java.util.List)" title="class or interface in java.util"><code>Collections.reverse(java.util.List&lt;?&gt;)</code></a></div>
</div>
<div class="block">Swaps vector ( first element will be last, same with others elements)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - List that be swapped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileWithoutExtension(java.lang.String)">
<h3>getFileWithoutExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileWithoutExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</span></div>
<div class="block">Returns file name without extension (removes chars from last "." to end of string)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filename</code> - The given file name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileWitoutExtention(java.lang.String)">
<h3>getFileWitoutExtention</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileWitoutExtention</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">type error in name</div>
</div>
<div class="block">Returns file name without extension (removes chars from last "." to end of string)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filename</code> - The given file name</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="#getFileWithoutExtension(java.lang.String)"><code>getFileWithoutExtension(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileExtension(java.io.File)">
<h3>getFileExtension</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Get The given file extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - The given file</dd>
<dt>Returns:</dt>
<dd>File extension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileExtension(java.lang.String)">
<h3>getFileExtension</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</span></div>
<div class="block">Get the given file extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - file name</dd>
<dt>Returns:</dt>
<dd>File extension</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileName(java.lang.String)">
<h3>getFileName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
</section>
</li>
<li>
<section class="detail" id="getCurrentDateFormatted()">
<h3>getCurrentDateFormatted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCurrentDateFormatted</span>()</div>
</section>
</li>
<li>
<section class="detail" id="removeComments(java.lang.String)">
<h3>removeComments</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeComments</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> body)</span></div>
<div class="block">Removes / *       * /  comments from body.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>body</code> - String body.</dd>
<dt>Returns:</dt>
<dd>body without comment.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCollection(java.lang.Class,java.util.Iterator)">
<h3>createCollection</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="type-parameters">&lt;E extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&gt;</span> <span class="return-type">E</span> <span class="element-name">createCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;E&gt; collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a> it)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#createCollection(java.lang.Class,java.util.Iterator)"><code>CollectionUtils.createCollection(Class, java.util.Iterator)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="notDublicatedList(java.util.Collection)">
<h3>notDublicatedList</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a></span> <span class="element-name">notDublicatedList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> col)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="CollectionUtils.html#notDuplicatedList(java.util.Collection)"><code>CollectionUtils.notDuplicatedList(java.util.Collection)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="trim(java.lang.String,java.lang.String,java.lang.String)">
<h3>trim</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">trim</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trashBegin,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trashEnd)</span></div>
<div class="block">Removes from begin and end given Strings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>src</code> - The given string.</dd>
<dd><code>trashBegin</code> - Trash string that is a beginning.</dd>
<dd><code>trashEnd</code> - Trash string that is a ending.</dd>
<dt>Returns:</dt>
<dd>String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceEpsString(java.lang.String)">
<h3>replaceEpsString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">replaceEpsString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> aStr)</span></div>
<div class="block">Replace special char for Eps format string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>aStr</code> - The given string.</dd>
<dt>Returns:</dt>
<dd>String</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.InputStream,java.io.OutputStream,long,boolean)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output,
 long crc,
 boolean closeInput)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Copies all bytes from InputStream into OutputStream. Closes the streams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - the input stream.</dd>
<dd><code>output</code> - the output stream.</dd>
<dd><code>crc</code> - crc to check. -1 if do not check crc.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.InputStream,java.io.OutputStream,java.util.zip.Checksum)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/Checksum.html" title="class or interface in java.util.zip">Checksum</a> checksum)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Copies all bytes from InputStream into OutputStream</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - the input stream.</dd>
<dd><code>output</code> - the output stream.</dd>
<dd><code>checksum</code> - checksum.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.InputStream,java.io.OutputStream)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Copies all bytes from InputStream into OutputStream. Closes the streams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - the input stream.</dd>
<dd><code>output</code> - the output stream.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyFile(java.lang.String,java.lang.String)">
<h3>copyFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">copyFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sourceName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstName)</span></div>
<div class="block">Copy source file to destination file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sourceName</code> - Source file name.</dd>
<dd><code>dstName</code> - destination file name.</dd>
<dt>Returns:</dt>
<dd>True if work successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyFile(java.io.File,java.io.File)">
<h3>copyFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">copyFile</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</span></div>
<div class="block">Copy source file to destination file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - Source file.</dd>
<dd><code>destination</code> - destination file.</dd>
<dt>Returns:</dt>
<dd>true if successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyDirectory(java.io.File,java.io.File)">
<h3>copyDirectory</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">copyDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</span></div>
<div class="block">Copy all directory recursively</div>
</section>
</li>
<li>
<section class="detail" id="extractZip(java.util.zip.ZipFile,java.lang.String)">
<h3>extractZip</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">extractZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipFile.html" title="class or interface in java.util.zip">ZipFile</a> zipFile,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstDir)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Extracts files from Zip archive</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zipFile</code> - Zip archive file</dd>
<dd><code>dstDir</code> - name of the destination directory</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="extractZip(java.io.InputStream,java.lang.String,java.util.Collection,java.util.Collection)">
<h3>extractZip</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt;</span> <span class="element-name">extractZip</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> is,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstDir,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; onlyTheseEntries,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; skipTheseEntries)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Extracts files from Zip archive</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>is</code> - Input Stream - must be valid zip file</dd>
<dd><code>dstDir</code> - destination directory</dd>
<dd><code>onlyTheseEntries</code> - if not null specifies which entries must be extracted.</dd>
<dd><code>skipTheseEntries</code> - if not null specifies which entries should be skiped.</dd>
<dt>Returns:</dt>
<dd>extracted entry names.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toByteArray(java.io.InputStream)">
<h3>toByteArray</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">toByteArray</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream)</span></div>
<div class="block">Copies the given file into the array of bytes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stream</code> - the given file.</dd>
<dt>Returns:</dt>
<dd>the byte array with the context of the file;null if some errors occurs</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getItemWithText(javax.swing.JPopupMenu,java.lang.String)">
<h3>getItemWithText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html" title="class or interface in javax.swing">JMenuItem</a></span> <span class="element-name">getItemWithText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> menu,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block">Returns inner component (not recursively) with given text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>menu</code> - The given JPopupMenu.</dd>
<dd><code>text</code> - The given text.</dd>
<dt>Returns:</dt>
<dd>JMenuItem.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCursor(java.awt.Image,java.awt.Point,java.lang.String)">
<h3>createCursor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">createCursor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cursorName)</span></div>
<div class="block">Creates the cursor for given image.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>image</code> - the given image.</dd>
<dd><code>pt</code> - the hot point.</dd>
<dd><code>cursorName</code> - the cursor name.</dd>
<dt>Returns:</dt>
<dd>Cursor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createCursor(javax.swing.Icon,java.awt.Point,java.lang.String)">
<h3>createCursor</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></span> <span class="element-name">createCursor</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cursorName)</span></div>
<div class="block">Creates the cursor for given icon.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the given icon.</dd>
<dd><code>pt</code> - the hot point.</dd>
<dd><code>cursorName</code> - the cursor name.</dd>
<dt>Returns:</dt>
<dd>Cursor.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAsStringKeyStrokes(java.util.List,java.lang.String,java.lang.String)">
<h3>getAsStringKeyStrokes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsStringKeyStrokes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a>&gt; shortcuts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bracketFirst,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bracketSecond)</span></div>
<div class="block">Constructs the string representation of the given key strokes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>shortcuts</code> - The given key strokes.</dd>
<dd><code>bracketFirst</code> - Open bracket.</dd>
<dd><code>bracketSecond</code> - Close bracket.</dd>
<dt>Returns:</dt>
<dd>String.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAsString(javax.swing.KeyStroke)">
<h3>getAsString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsString</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> e)</span></div>
<div class="block">Constructs the string representation of the given key stroke.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>e</code> - the given key stroke.</dd>
<dt>Returns:</dt>
<dd>String representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isValidKeyCode(int)">
<h3>isValidKeyCode</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isValidKeyCode</span><wbr/><span class="parameters">(int keyCode)</span></div>
<div class="block">Checks if given code is correct one or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>keyCode</code> - The given key code.</dd>
<dt>Returns:</dt>
<dd>true if given code is not CTRL, SHIFT, META or ALT.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPrintableChar(char)">
<h3>isPrintableChar</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isPrintableChar</span><wbr/><span class="parameters">(char c)</span></div>
<div class="block">Checks if char is printable or not.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>c</code> - char which ic checked.</dd>
<dt>Returns:</dt>
<dd>true if char is printable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString(byte[])">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span><wbr/><span class="parameters">(byte[] data)</span></div>
<div class="block">Returns string representation of the given byte array.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - the given bytes array.</dd>
<dt>Returns:</dt>
<dd>the string representation (every byte is represented as hex string separated by space)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toByteArray(java.lang.String)">
<h3>toByteArray</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">toByteArray</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bytes)</span></div>
<div class="block">Returns byte array from string formatted in toString(byte[]) method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bytes</code> - the given string.</dd>
<dt>Returns:</dt>
<dd>the byte array.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="areChildrenDisabled(javax.swing.JMenu)">
<h3>areChildrenDisabled</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">areChildrenDisabled</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenu.html" title="class or interface in javax.swing">JMenu</a> menu)</span></div>
<div class="block">Are all children disabled?</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>menu</code> - the menu</dd>
<dt>Returns:</dt>
<dd>true, if all menu children are disabled</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point)">
<h3>normalize</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">normalize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rectangle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> firstCorner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> secondCorner)</span></div>
<div class="block">Normalizes rectangle; Calculates rectangle size and location using firstCorner and secondCorner.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rectangle</code> - rectangle to normalize</dd>
<dd><code>firstCorner</code> - first corner</dd>
<dd><code>secondCorner</code> - second corner</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="normalize(java.awt.Rectangle)">
<h3>normalize</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">normalize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span></div>
<div class="block">normalizes rectangle mRectToDraw;</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rect</code> - rectangle to normalize</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTempDir()">
<h3>getTempDir</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTempDir</span>()</div>
<div class="block">Returns System temp directory.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openHttpURLConnection(java.lang.String,com.nomagic.license.utils.ProxyServerData)">
<h3>openHttpURLConnection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html" title="class or interface in java.net">HttpURLConnection</a></span> <span class="element-name">openHttpURLConnection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pageHttpAddress,
 <a href="../license/utils/ProxyServerData.html" title="class in com.nomagic.license.utils">ProxyServerData</a> proxyServerData)</span>
                                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Opens HttpURLConnection according given page address and proxy server data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pageHttpAddress</code> - page address with protocol e.g <code>"http://www.nomagic.com"</code></dd>
<dd><code>proxyServerData</code> - proxy server data</dd>
<dt>Returns:</dt>
<dd>HttpURLConnection.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUseProxy(com.nomagic.license.utils.ProxyServerData)">
<h3>isUseProxy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUseProxy</span><wbr/><span class="parameters">(<a href="../license/utils/ProxyServerData.html" title="class in com.nomagic.license.utils">ProxyServerData</a> proxy)</span></div>
<div class="block">Checks if use proxy server according given proxy server data</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>proxy</code> - proxy data.</dd>
<dt>Returns:</dt>
<dd>true if use; otherwise - false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHtmlPage(java.lang.String,java.lang.String,com.nomagic.license.utils.ProxyServerData)">
<h3>getHtmlPage</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHtmlPage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pageHttpAddress,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters,
 <a href="../license/utils/ProxyServerData.html" title="class in com.nomagic.license.utils">ProxyServerData</a> proxy)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Returns HTML page</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pageHttpAddress</code> - page address with protocol e.g <code>"http://www.nomagic.com"</code></dd>
<dd><code>parameters</code> - parameters for POST method (null if no data to POST)</dd>
<dd><code>proxy</code> - proxy server data</dd>
<dt>Returns:</dt>
<dd>HTML page</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString(java.io.InputStream)">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> inputStream)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Get String representation of inputStream</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputStream</code> - The given inputStream</dd>
<dt>Returns:</dt>
<dd>String representation.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString(java.util.Collection)">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; strings)</span></div>
<div class="block">Get String representation of given strings collection</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>strings</code> - many strings</dd>
<dt>Returns:</dt>
<dd>String representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sendHttpParameters(java.net.HttpURLConnection,java.lang.String)">
<h3>sendHttpParameters</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">sendHttpParameters</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/HttpURLConnection.html" title="class or interface in java.net">HttpURLConnection</a> connection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <code>HttpUtilities.sendHttpParameters(HttpURLConnection, String)</code></div>
</div>
<div class="block">Send Http Parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connection</code> - HttpURLConnection</dd>
<dd><code>parameters</code> - Http Parameters.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="constructHttpParameter(java.lang.String,java.lang.String)">
<h3>constructHttpParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">constructHttpParameter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Constructs http parameter</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameter</code> - parameter name</dd>
<dd><code>value</code> - parameter value</dd>
<dt>Returns:</dt>
<dd>constructed parameter</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addHttpParameter(java.lang.String,java.lang.String,java.lang.String)">
<h3>addHttpParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">addHttpParameter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block">Adds http parameter to given parameters string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameters</code> - parameters</dd>
<dd><code>parameter</code> - parameter name to add</dd>
<dd><code>value</code> - parameter value to add</dd>
<dt>Returns:</dt>
<dd>constructed parameters string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="concatHttpParameter(java.lang.String,java.lang.String)">
<h3>concatHttpParameter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">concatHttpParameter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> parameters2)</span></div>
<div class="block">Concatenate given http parameters</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>parameters1</code> - </dd>
<dd><code>parameters2</code> - </dd>
<dt>Returns:</dt>
<dd>concatenated parameters</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertSeparators(char[],java.lang.String,int)">
<h3>insertSeparators</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">insertSeparators</span><wbr/><span class="parameters">(char[] chars,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 int groupSize)</span></div>
<div class="block">Constructs string from arrays of chars.
 String characters are grouped into groups. Groups are separated by separator.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>chars</code> - array of characters to divide</dd>
<dd><code>separator</code> - group separator</dd>
<dd><code>groupSize</code> - size if the group</dd>
<dt>Returns:</dt>
<dd>result string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeSeparators(java.lang.String,java.lang.String)">
<h3>removeSeparators</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeSeparators</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</span></div>
<div class="block">Removes separators from specified str</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - string to unite</dd>
<dd><code>separator</code> - </dd>
<dt>Returns:</dt>
<dd>str without separators</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBytes(java.lang.String)">
<h3>getBytes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">getBytes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</span></div>
<div class="block">Returns bytes of string. 2 bytes for every char.</div>
</section>
</li>
<li>
<section class="detail" id="distributeInteger(int,int)">
<h3>distributeInteger</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">distributeInteger</span><wbr/><span class="parameters">(int intValue,
 int size)</span></div>
<div class="block">Distributes integer intValue into array of bytes.
 int is 4 bytes, so max array size is 4</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>intValue</code> - int intValue to distribute</dd>
<dd><code>size</code> - size of result array</dd>
<dt>Returns:</dt>
<dd>array of bytes</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="collectInteger(byte[])">
<h3>collectInteger</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">collectInteger</span><wbr/><span class="parameters">(byte[] bytes)</span></div>
<div class="block">Makes int value from array of bytes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bytes</code> - array of bytes</dd>
<dt>Returns:</dt>
<dd>int value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invokeAndWaitOnDispatcher(java.lang.Runnable)">
<h3>invokeAndWaitOnDispatcher</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">invokeAndWaitOnDispatcher</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</span>
                                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></span></div>
<div class="block">Executes given runnable on event dispatcher. Note if current thread is interrupted
 after runnable is submitted to the queue this method throws exception but runnable will be run on EDT.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - the given runnable</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invokeAndWaitOnDispatcherEvenInterrupted(java.lang.Runnable)">
<h3>invokeAndWaitOnDispatcherEvenInterrupted</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">invokeAndWaitOnDispatcherEvenInterrupted</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</span>
                                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></span></div>
<div class="block">Executes given runnable on event dispatcher. Waits until r is finished even current thread is interrupted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - the given runnable</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invokeOnDispatcherOrLater(java.lang.Runnable)">
<h3>invokeOnDispatcherOrLater</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">invokeOnDispatcherOrLater</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> r)</span></div>
<div class="block">If this thread is event dispatcher, than direct calls "run", else invoke on invoke later</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>r</code> - </dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invokeLaterAfterCondition(java.lang.Runnable,java.util.function.Supplier)">
<h3>invokeLaterAfterCondition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">invokeLaterAfterCondition</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; condition)</span></div>
<div class="block">Invokes runnable latter after condition is satisfied.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - runnable which will be executed.</dd>
<dd><code>condition</code> - condition condition after which satisfaction runnable will be executed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invokeLaterAfterCondition(java.lang.Runnable,java.util.function.Supplier,int)">
<h3>invokeLaterAfterCondition</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">invokeLaterAfterCondition</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a>&gt; condition,
 int conditionCheckAttemptCount)</span></div>
<div class="block">Invokes runnable latter after condition is satisfied.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runnable</code> - runnable which will be executed.</dd>
<dd><code>condition</code> - condition condition after which satisfaction runnable will be executed.</dd>
<dd><code>conditionCheckAttemptCount</code> - attempts count of the condition check; if count is reached before the condition is satisfied, runnable will not be executed.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareStreams(java.io.InputStream,java.io.InputStream)">
<h3>compareStreams</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">compareStreams</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> oldStr,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> newStr)</span>
                              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Compares two input streams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>oldStr</code> - First input stream.</dd>
<dd><code>newStr</code> - Second input stream.</dd>
<dt>Returns:</dt>
<dd>true if streams contains identical data.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareFiles(java.io.File,java.io.File)">
<h3>compareFiles</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">compareFiles</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f2)</span>
                            throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Compares two files</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>f1</code> - First file.</dd>
<dd><code>f2</code> - Second file.</dd>
<dt>Returns:</dt>
<dd>true if files contains identical data.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deleteTree(java.io.File)">
<h3>deleteTree</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">deleteTree</span><wbr/><span class="parameters">(@Nonnull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</span></div>
<div class="block">Removes given directory and all its contents.
 File.delete fails if directory is not empty</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>f</code> - file to delete</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deleteTreeOnExit(java.io.File)">
<h3>deleteTreeOnExit</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">deleteTreeOnExit</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</span></div>
<div class="block">Removes given file (directory and all its contents) on exit.
 File.delete fails if directory is not empty</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>f</code> - file to delete</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deleteDirContent(java.io.File)">
<h3>deleteDirContent</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">deleteDirContent</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</span></div>
<div class="block">Removes given directory contents.
 File.delete fails if directory is not empty</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>f</code> - file to delete</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGrayIcon(javax.swing.Icon)">
<h3>getGrayIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getGrayIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component)"><code>IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)</code></a></div>
</div>
<div class="block">Returns grey(disabled) icon from given one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the given icon.</dd>
<dt>Returns:</dt>
<dd>disabled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGrayIcon(javax.swing.Icon,java.awt.Component)">
<h3>getGrayIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="../ui/ResizableIcon.html" title="interface in com.nomagic.ui">ResizableIcon</a></span> <span class="element-name">getGrayIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/Icon.html" title="class or interface in javax.swing">Icon</a> icon,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Component.html" title="class or interface in java.awt">Component</a> component)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="../ui/IconUtilities.html#getGrayIcon(javax.swing.Icon,java.awt.Component)"><code>IconUtilities.getGrayIcon(javax.swing.Icon, java.awt.Component)</code></a></div>
</div>
<div class="block">Returns grey(disabled) icon from given one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>icon</code> - the given icon.</dd>
<dd><code>component</code> - component.</dd>
<dt>Returns:</dt>
<dd>disabled icon</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="makeEqual(java.util.List,java.util.List)">
<h3>makeEqual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">makeEqual</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> destination,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> source)</span></div>
<div class="block">Make destination the same as source with minimum changes to destination</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>destination</code> - List</dd>
<dd><code>source</code> - List</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClassName(java.lang.Class)">
<h3>getClassName</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getClassName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz)</span></div>
<div class="block">Get class name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - The given class.</dd>
<dt>Returns:</dt>
<dd>Class name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAlphaNumeric(java.lang.String)">
<h3>isAlphaNumeric</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isAlphaNumeric</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</span></div>
</section>
</li>
<li>
<section class="detail" id="mergeLists(java.util.List,java.util.List)">
<h3>mergeLists</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt;</span> <span class="element-name">mergeLists</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; l1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;T&gt; l2)</span></div>
<div class="block">Merges two lists into newly created one.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>l1</code> - first list.</dd>
<dd><code>l2</code> - second list.</dd>
<dt>Returns:</dt>
<dd>newly created list with added elements from l1 and l2.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="synchronizeDirectories(java.io.File,java.io.File)">
<h3>synchronizeDirectories</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">synchronizeDirectories</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</span>
                                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Synchronize two directories. If new file appears in source, it should appear in destination.
 If file is removed from destination it should not appear in destination again.  Typical use for this method
 is when one directory has default settings, and another have working copy.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - source directory.</dd>
<dd><code>destination</code> - destination directory.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="splitString(java.lang.String,java.lang.String,boolean)">
<h3>splitString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">splitString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 boolean returnDelimiter)</span></div>
<div class="block">Splits string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - a string to be parsed.</dd>
<dd><code>delimiter</code> - the delimiter.</dd>
<dd><code>returnDelimiter</code> - flag indicating whether to include the delimiter in result.</dd>
<dt>Returns:</dt>
<dd>array of strings</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="implode(java.util.Collection,java.lang.String)">
<h3>implode</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">implode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter)</span></div>
<div class="block">Returns a new String composed of copies of the collection elements joined together with a copy of the specified delimiter.
 Consider using <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.Iterable)" title="class or interface in java.lang"><code>String.join(CharSequence, Iterable)</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection of elements.</dd>
<dd><code>delimiter</code> - delimiter.</dd>
<dt>Returns:</dt>
<dd>joined string.</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.Iterable)" title="class or interface in java.lang"><code>String.join(CharSequence, Iterable)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="implode(java.lang.String[],java.lang.String)">
<h3>implode</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">implode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] values,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html#join(java.lang.CharSequence,java.lang.CharSequence...)" title="class or interface in java.lang"><code>String.join(CharSequence, CharSequence...)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="parseExceptQuotes(java.lang.String)">
<h3>parseExceptQuotes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">parseExceptQuotes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd)</span></div>
<div class="block">parses string by standard tokens, except parts wrapped in quotes</div>
</section>
</li>
<li>
<section class="detail" id="readFileSkipFirstLines(java.io.File,int)">
<h3>readFileSkipFirstLines</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">readFileSkipFirstLines</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file,
 int n)</span></div>
<div class="block">Reads a file to string and skips a specified number of lines from the beginning.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - - file to read.</dd>
<dd><code>n</code> - - number of lines to skip from the beginning.</dd>
<dt>Returns:</dt>
<dd>file contents as string with skipped lines.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="zipDir(java.lang.String,java.util.zip.ZipOutputStream)">
<h3>zipDir</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">zipDir</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dir2zip,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/zip/ZipOutputStream.html" title="class or interface in java.util.zip">ZipOutputStream</a> zos)</span>
                   throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Compress specified directory recursively to the specified stream.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dir2zip</code> - directory to zip.</dd>
<dd><code>zos</code> - <code>ZipOutputStream</code> object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if any occurs during</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compressData(byte[],java.lang.String)">
<h3>compressData</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">compressData</span><wbr/><span class="parameters">(byte[] data,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> zipEntryName)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Compresses specified data using zip output stream and returns the result as bytes array.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - a data.</dd>
<dd><code>zipEntryName</code> - name of how the data will be named in the archive.</dd>
<dt>Returns:</dt>
<dd>compressed data.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if any occurs during compressing the data.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compressData(byte[])">
<h3>compressData</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">compressData</span><wbr/><span class="parameters">(byte[] data)</span>
                           throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Compresses specified data using gzip output stream and returns the result as bytes array.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - a data.</dd>
<dt>Returns:</dt>
<dd>compressed data.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if any occurs during compressing the data.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="uncompressData(byte[])">
<h3>uncompressData</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">uncompressData</span><wbr/><span class="parameters">(byte[] data)</span>
                             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Uncompresses specified data using gzip input stream and returns the result as bytes array.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - a data.</dd>
<dt>Returns:</dt>
<dd>compressed data.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - if any occurs during compressing the data.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkSystemProperty(java.lang.String,boolean)">
<h3>checkSystemProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">checkSystemProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 boolean defaultValue)</span></div>
<div class="block">Checks given system (boolean) property value</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>property</code> - </dd>
<dd><code>defaultValue</code> - </dd>
<dt>Returns:</dt>
<dd>value of the system property, or defaultValue if system property is not set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkProperty(java.util.Properties,java.lang.String,boolean)">
<h3>checkProperty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">checkProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 boolean defaultValue)</span></div>
</section>
</li>
<li>
<section class="detail" id="checkResolvableException(boolean)">
<h3>checkResolvableException</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">checkResolvableException</span><wbr/><span class="parameters">(boolean rule)</span></div>
<div class="block">if rule is false and it's DEVELOPER mode throws <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang"><code>IllegalStateException</code></a></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>rule</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dumpThreads()">
<h3>dumpThreads</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">dumpThreads</span>()</div>
<div class="block">Dumps all threads to system out.</div>
</section>
</li>
<li>
<section class="detail" id="dumpThreads(java.io.PrintStream)">
<h3>dumpThreads</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">dumpThreads</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/PrintStream.html" title="class or interface in java.io">PrintStream</a> out)</span></div>
<div class="block">Dumps all threads to given stream.</div>
</section>
</li>
<li>
<section class="detail" id="reverseString(java.lang.String)">
<h3>reverseString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">reverseString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</span></div>
<div class="block">Given a string, returns a string with reversed characters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - string which has to be reversed.</dd>
<dt>Returns:</dt>
<dd>a string with reversed characters.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateTextWidth(java.lang.String,java.awt.FontMetrics,int)">
<h3>calculateTextWidth</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">calculateTextWidth</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/FontMetrics.html" title="class or interface in java.awt">FontMetrics</a> metrics,
 int numberOfLines)</span></div>
<div class="block">Calculates possible text longest text width of the given text splitted into lines.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>text</code> - text for which to calculate width.</dd>
<dd><code>metrics</code> - font metrics according which to calculate.</dd>
<dd><code>numberOfLines</code> - number of lines into which to split the text.</dd>
<dt>Returns:</dt>
<dd>calculated possible text width.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isHTMLText(java.lang.String)">
<h3>isHTMLText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isHTMLText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Check the given string to see if it should trigger the
 html rendering logic.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - the given string.</dd>
<dt>Returns:</dt>
<dd>true if given text is html, false otherwise.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ensureObjectIsInCollection(java.util.Collection,T)">
<h3 id="ensureObjectIsInCollection(java.util.Collection,java.lang.Object)">ensureObjectIsInCollection</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type">void</span> <span class="element-name">ensureObjectIsInCollection</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; collection,
 T object)</span></div>
<div class="block">Ensures an object is in given collection.
 If it isn't, the object is added to it.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>collection</code> - collection in which to check object existence.</dd>
<dd><code>object</code> - object to check.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="encodeBase64(byte[])">
<h3>encodeBase64</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">encodeBase64</span><wbr/><span class="parameters">(byte[] abyte0)</span></div>
<div class="block">Encodes data using base64 encoding.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>abyte0</code> - data for encoding</dd>
<dt>Returns:</dt>
<dd>encoded string</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="decodeBase64(java.lang.String)">
<h3>decodeBase64</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">decodeBase64</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Decode string using Base64 encoding.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - string for decoding</dd>
<dt>Returns:</dt>
<dd>decoded data</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasModalDialogs(java.awt.Window)">
<h3>hasModalDialogs</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasModalDialogs</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Window.html" title="class or interface in java.awt">Window</a> window)</span></div>
<div class="block">Checks recursively if given window has modal dialog as child (or window itself is a modal dialog)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>window</code> - window</dd>
<dt>Returns:</dt>
<dd>true if modal dialog is found</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeNewLines(java.lang.String)">
<h3>removeNewLines</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeNewLines</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="block">Removes new lines from the string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - string for which to remove new lines.</dd>
<dt>Returns:</dt>
<dd>string with removed new lines.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment)">
<h3>checkIsInstallRootWritable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">checkIsInstallRootWritable</span><wbr/><span class="parameters">(com.nomagic.runtime.RuntimeEnvironment runtime)</span></div>
<div class="block">Get message for install root read only error. Returns null if install root is writable. Method is suitable
 for read only checking.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runtime</code> - Application runtime.</dd>
<dt>Returns:</dt>
<dd>Message for install root read only error or null if install root is writable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkIsInstallRootWritable(com.nomagic.runtime.RuntimeEnvironment,boolean)">
<h3>checkIsInstallRootWritable</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">checkIsInstallRootWritable</span><wbr/><span class="parameters">(com.nomagic.runtime.RuntimeEnvironment runtime,
 boolean skipWinUAC)</span></div>
<div class="block">Get message for install root read only error. Returns null if install root is writable. Method is suitable
 for read only checking.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>runtime</code> - runtime environment.</dd>
<dd><code>skipWinUAC</code> - skip checking writable installation root if Windows is supporting UAC.</dd>
<dt>Returns:</dt>
<dd>Message for install root read only error or null if install root is writable</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="main(java.lang.String[])">
<h3>main</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">main</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] args)</span></div>
</section>
</li>
<li>
<section class="detail" id="getVersionFromInternal(java.lang.String)">
<h3>getVersionFromInternal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVersionFromInternal</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> internal)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a>,
<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></span></div>
<div class="block">Convert internal MagicDraw style version to human version in 17.0.2 format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>internal</code> - Internal version.</dd>
<dt>Returns:</dt>
<dd>Human version</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NumberFormatException.html" title="class or interface in java.lang">NumberFormatException</a></code> - parse exception.</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></code> - if internal version is negative.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVersionFromInternal(int)">
<h3>getVersionFromInternal</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getVersionFromInternal</span><wbr/><span class="parameters">(int internal)</span>
                                     throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></span></div>
<div class="block">Convert internal MagicDraw style version to human version in 17.0.2 format.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>internal</code> - Internal version.</dd>
<dt>Returns:</dt>
<dd>human version</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IndexOutOfBoundsException.html" title="class or interface in java.lang">IndexOutOfBoundsException</a></code> - if internal version is negative.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containSameElements(java.util.Collection,java.util.Collection)">
<h3>containSameElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">containSameElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;?&gt; collection2)</span></div>
</section>
</li>
<li>
<section class="detail" id="arrayHash(byte[])">
<h3>arrayHash</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">int</span> <span class="element-name">arrayHash</span><wbr/><span class="parameters">(byte[] array)</span></div>
<div class="block">Calculate hash code for array of bytes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>array</code> - bytes</dd>
<dt>Returns:</dt>
<dd>hash code</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStreamEmpty(java.net.URL)">
<h3>isStreamEmpty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isStreamEmpty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url)</span></div>
<div class="block">Check if it is possible to open a stream from a given URL and that stream is not empty</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - url to check</dd>
<dt>Returns:</dt>
<dd>true if not empty stream is opened from a given url</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="insertPeriodically(java.lang.String,java.lang.String,int)">
<h3>insertPeriodically</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">insertPeriodically</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> insert,
 int period)</span></div>
</section>
</li>
<li>
<section class="detail" id="sha1Hex(java.lang.String...)">
<h3>sha1Hex</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">sha1Hex</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>... strings)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html" title="class or interface in java.security">NoSuchAlgorithmException</a></span></div>
<div class="block">Returns SHA-1 hash key that should be constructed from the specified strings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>strings</code> - array of strings.</dd>
<dt>Returns:</dt>
<dd>SHA-1 hash key.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html" title="class or interface in java.security">NoSuchAlgorithmException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="sha1Hex(byte[])">
<h3>sha1Hex</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">sha1Hex</span><wbr/><span class="parameters">(byte[] data)</span>
                      throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html" title="class or interface in java.security">NoSuchAlgorithmException</a></span></div>
<div class="block">Returns SHA-1 hash key that should be constructed from the specified data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>data</code> - array of bytes</dd>
<dt>Returns:</dt>
<dd>SHA-1 hash key.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/NoSuchAlgorithmException.html" title="class or interface in java.security">NoSuchAlgorithmException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDistance(E,E,java.util.function.Function)">
<h3 id="getDistance(java.lang.Object,java.lang.Object,java.util.function.Function)">getDistance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;E&gt;</span> <span class="return-type">int</span> <span class="element-name">getDistance</span><wbr/><span class="parameters">(E from,
 E to,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;E,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;E&gt;&gt; connectedNodes)</span></div>
<div class="block">Calculate minimal distance in graph.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>E</code> - type of node.</dd>
<dt>Parameters:</dt>
<dd><code>from</code> - starting point in graph.</dd>
<dd><code>to</code> - destination point in graph.</dd>
<dd><code>connectedNodes</code> - function to get connected edges.</dd>
<dt>Returns:</dt>
<dd>minimal number of steps required to get from node from to node to. Return -1 if nodes are not connected.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contentEquals(java.io.InputStream,java.io.InputStream)">
<h3>contentEquals</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">contentEquals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input2)</span></div>
<div class="block">Compare content of two streams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input1</code> - first stream.</dd>
<dd><code>input2</code> - another stream.</dd>
<dt>Returns:</dt>
<dd>true if stream provides exactly same content.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSystemDateFormat(int)">
<h3>getSystemDateFormat</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html" title="class or interface in java.text">DateFormat</a></span> <span class="element-name">getSystemDateFormat</span><wbr/><span class="parameters">(int style)</span></div>
<div class="block">Returns system date format. Ordinary Java date format getting methods returns format taken from locale, which can be different from real system date format,
 set in calendar settings.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>style</code> - Format style (e.g. <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html#SHORT" title="class or interface in java.text"><code>DateFormat.SHORT</code></a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/text/DateFormat.html#LONG" title="class or interface in java.text"><code>DateFormat.LONG</code></a>).</dd>
<dt>Returns:</dt>
<dd>System date format. If can't get it, returns SimpleDateFormat.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFileNameValid(java.lang.String)">
<h3>isFileNameValid</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFileNameValid</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</span></div>
<div class="block">Returns if given file name is valid to be created.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - file name</dd>
<dt>Returns:</dt>
<dd>true if file name can be created or already exists, else false</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="excludeCommonElements(java.util.Collection,java.util.Collection)">
<h3>excludeCommonElements</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html" title="class or interface in java.util">Set</a>&lt;T&gt;</span> <span class="element-name">excludeCommonElements</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; first,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;T&gt; second)</span></div>
<div class="block">Creates result collection which contains not common elements from two arguments</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>T</code> - type of collection</dd>
<dt>Parameters:</dt>
<dd><code>first</code> - first collection</dd>
<dd><code>second</code> - second collection</dd>
<dt>Returns:</dt>
<dd>not common elements of two arguments</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isNameValid(java.lang.String)">
<h3>isNameValid</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNameValid</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
</section>
</li>
<li>
<section class="detail" id="getThreadsInfo()">
<h3>getThreadsInfo</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getThreadsInfo</span>()</div>
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
