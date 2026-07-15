# JAVA OPENAPI: Utilities (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/rcpf/product/utils/Utilities.html
- source_path: `com/nomagic/rcpf/product/utils/Utilities.html`
- source_sha256: `bb0c92ea6bd8a9f8b9f4c27ea591d75c455fafdb9903f558b677f7eadeae8662`
- captured_utc: `2026-07-14T16:56:02.633537+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.rcpf.product.utils](package-summary.html)

## Class Utilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.license.utils.CameoUtilities](../../../license/utils/CameoUtilities.html)
com.nomagic.rcpf.product.utils.Utilities

@OpenApiAllpublic classUtilities
extends [CameoUtilities](../../../license/utils/CameoUtilities.html)
General purpose utilities.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[Utilities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static boolean`
`[areChildrenDisabled](#areChildrenDisabled(javax.swing.JMenu))([JMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenu.html) menu)`
Are all children disabled?
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
`static boolean`
`[containsOnlyFiles](#containsOnlyFiles(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) list)`
Indicates if given list contains only file objects.
`static void`
`[copy](#copy(java.io.InputStream,java.io.OutputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output)`
Copies all bytes from InputStream into OutputStream.
`static void`
`[copy](#copy(java.io.InputStream,java.io.OutputStream,long))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output,
 long crc)`
Copies all bytes from InputStream into OutputStream.
`static boolean`
`[copyDirectory](#copyDirectory(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)`
copy all directory recursivelly
`static boolean`
`[copyFile](#copyFile(java.io.File,java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dst)`
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
Moves outer rectengle in such way that it must cover inner one (if outer is smaller than inner resizes outer).
`static [Cursor](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html)`
`[createCursor](#createCursor(java.awt.Image,java.awt.Point,java.lang.String))([Image](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html) image,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) pt,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cursorName)`
Creates the cursor for given image.
`static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[createRectFromList](#createRectFromList(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) v)`
Creates rectangle from vector of points.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStringRepresentation](#createStringRepresentation(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) value)`

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
`[getAsStringKeyStrokes](#getAsStringKeyStrokes(java.util.List,java.lang.String,java.lang.String))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) shortcuts,
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
`[getFileExtension](#getFileExtension(java.io.File))([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)`
Get The given file extension.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileName](#getFileName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getFileWitoutExtention](#getFileWitoutExtention(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filename)`
Returns file name without extention (removes chars from last "." to end of string)
`static [JMenuItem](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html)`
`[getItemWithText](#getItemWithText(javax.swing.JPopupMenu,java.lang.String))([JPopupMenu](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html) menu,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)`
Returns inner component (not recursively) with given text.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getTempDir](#getTempDir())()`
Returns directory can be used for writing temporary files.
`static boolean`
`[hasExtension](#hasExtension(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension)`
Checks if given file name has given file extension.
`static boolean`
`[hasExtension](#hasExtension(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) extensions)`
Checks if given file name has one of given file extensions.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[implode](#implode(java.lang.String%5B%5D,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] values,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[implode](#implode(java.util.Collection,java.lang.String))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)`

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[insertSeparators](#insertSeparators(char%5B%5D,java.lang.String,int))(char[] chars,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 int groupSize)`
Constructs string from arrays of chars.
`static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`
`[internString](#internString(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) strings)`
Replace all strings in given collection with String.intern().
`static boolean`
`[isAlphaNumeric](#isAlphaNumeric(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str)`

`static boolean`
`[isValidKeyCode](#isValidKeyCode(int))(int keyCode)`
Checks if given code is correct one or not.
`static boolean`
`[match](#match(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)`
algorithm for searching with wildcards.
`static boolean`
`[matchEmpty](#matchEmpty(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) patter,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)`
Matches empty string also
`static <T> [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T>`
`[mergeLists](#mergeLists(java.util.List,java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> l1,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<T> l2)`
Merges two lists into newly created one.
`static void`
`[normalize](#normalize(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
normalizes rectangle mRectToDraw;
`static void`
`[normalize](#normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point))([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) mRectToDraw,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) mFirstCorner,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) mSecondCorner)`
normalizes rectangle mRectToDraw; Calculates rectangle size and
 location using mFirstCorner and mSecondCorner.
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
`[removeExtension](#removeExtension(java.lang.String,java.util.Collection))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> extensions)`
Removes file extension form given file name.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[removeFromLine](#removeFromLine(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) line,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trash)`
Removes from line trash line
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
`[sortStrings](#sortStrings(java.util.Vector))([Vector](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Vector.html) elem)`
Sorts elements in strings' vector
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[]`
`[splitString](#splitString(java.lang.String,java.lang.String,boolean))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delim,
 boolean returnDelims)`
Splits string
`static void`
`[swapVector](#swapVector(java.util.List))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) v)`
Swaps vector ( first element will be last, same with others elements)
`static byte[]`
`[toByteArray](#toByteArray(java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) stream)`
Copies the given file into the array of bytes.
`static byte[]`
`[toByteArray](#toByteArray(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bytes)`
Returns byte array from string formated in toString(byte[]) method.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(byte%5B%5D))(byte[] data)`
Returns string representation of the given byte array.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) inputStream)`
Get String representation of inputStream
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
Compress specified directory recursivelly to the specified stream.
Methods inherited from class com.nomagic.license.utils.[CameoUtilities](../../../license/utils/CameoUtilities.html)
`[copy](../../../license/utils/CameoUtilities.html#copy(java.io.Reader,java.io.Writer)), [isEqual](../../../license/utils/CameoUtilities.html#isEqual(java.lang.Object%5B%5D,java.lang.Object%5B%5D)), [isEqual](../../../license/utils/CameoUtilities.html#isEqual(java.lang.Object,java.lang.Object)), [replaceNewLine](../../../license/utils/CameoUtilities.html#replaceNewLine(java.lang.String,java.lang.String)), [toString](../../../license/utils/CameoUtilities.html#toString(java.io.InputStream,java.lang.String))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
Utilities
public Utilities()
 ============ METHOD DETAIL ========== 
Method Details
hasExtension
public static boolean hasExtension([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) extensions)
Checks if given file name has one of given file extensions.
Parameters:
`name` -
`extensions` -
Returns:
hasExtension
public static boolean hasExtension([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) extension)
Checks if given file name has given file extension.
Parameters:
`name` -
`extension` -
Returns:
removeExtension
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeExtension([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> extensions)
Removes file extension form given file name.
Parameters:
`name` -
`extensions` - extensions
Returns:
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
algorithm for searching with wildcards.
Parameters:
`pattern` - The given pattern.
`string` - String.
Returns:
boolean expression.
matchEmpty
public static boolean matchEmpty([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) patter,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)
Matches empty string also
Parameters:
`patter` - The given pattern.
`string` - The given string.
Returns:
boolean
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
removeFromLine
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeFromLine([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) line,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) trash)
Removes from line trash line
Parameters:
`line` - the given line.
`trash` - characters as string.
Returns:
The given string without From Line.
countOccurrences
public static int countOccurrences([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string,
 char c)
Returns the number of times the character c appears in a string.
Parameters:
`string` - The given string.
`c` - character.
Returns:
number of time.
removeNonUtf8CompliantCharacters
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeNonUtf8CompliantCharacters([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) inString)
fitInRectangle
public static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) fitInRectangle([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) small,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) big)
recalculate bounds to fit in rectangle
Parameters:
`small` - Small rectangle.
`big` - Big rectangle.
Returns:
New rectangle.
containsOnlyFiles
public static boolean containsOnlyFiles([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) list)
Indicates if given list contains only file objects.
Parameters:
`list` - list to check.
Returns:
true if given list contains only file objects, false otherwise.
coverRectangle
public static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) coverRectangle([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) inner,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) outer)
Moves outer rectengle in such way that it must cover inner one (if outer is smaller than inner resizes outer).
 Modifies outer and returns it.
Parameters:
`inner` - Inner rectangle.
`outer` - Outer rectangle.
Returns:
Moved rectangle.
createRectFromList
public static [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) createRectFromList([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) v)
Creates rectangle from vector of points.
Parameters:
`v` - List of point.
Returns:
null if vector was empty.
swapVector
public static void swapVector([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) v)
Swaps vector ( first element will be last, same with others elements)
Parameters:
`v` - List that be swaped.
getFileWitoutExtention
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileWitoutExtention([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) filename)
Returns file name without extention (removes chars from last "." to end of string)
Parameters:
`filename` - The given file name.
getFileExtension
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileExtension([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) file)
Get The given file extension.
Parameters:
`file` - The given file.
Returns:
File extension.
getFileName
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getFileName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) text)
removeComments
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) removeComments([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) body)
Removes / * * / comments from body.
Parameters:
`body` - String body.
Returns:
body without comment.
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
 long crc)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Copies all bytes from InputStream into OutputStream. Closes the streams.
Parameters:
`input` - the inputstream.
`output` - the output stream.
`crc` - crc to check. -1 if do not check crc.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)`
copy
public static void copy([InputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html)
Copies all bytes from InputStream into OutputStream. Closes the streams.
Parameters:
`input` - the inputstream.
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
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) dst)
Copy source file to destination file.
Parameters:
`source` - Source file.
`dst` - destination file.
Returns:
True if work successful.
copyDirectory
public static boolean copyDirectory([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) source,
 [File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) destination)
copy all directory recursivelly
Parameters:
`source` -
`destination` -
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
Curser.
getAsStringKeyStrokes
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAsStringKeyStrokes([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) shortcuts,
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
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAsString([KeyStroke](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html) e)
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
toString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString(byte[] data)
Returns string representation of the given byte array.
Parameters:
`data` - the given bytes array.
Returns:
the string representation (every byte is represented as hex string separated by space)
toByteArray
public static byte[] toByteArray([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) bytes)
Returns byte array from string formated in toString(byte[]) method.
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
public static void normalize([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) mRectToDraw,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) mFirstCorner,
 [Point](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html) mSecondCorner)
normalizes rectangle mRectToDraw; Calculates rectangle size and
 location using mFirstCorner and mSecondCorner.
 This method is useful when resizing a shape and only opposite corners are
 known.
Parameters:
`mRectToDraw` - rectangle to normalize
`mFirstCorner` - first corner
`mSecondCorner` - second corner
normalize
public static void normalize([Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) rect)
normalizes rectangle mRectToDraw;
Parameters:
`rect` - rectangle to normalize
getTempDir
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTempDir()
Returns directory can be used for writing temporary files.
Returns:
string.
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
Parameters:
`str` -
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
public static void deleteTree([File](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html) f)
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
splitString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] splitString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) str,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delim,
 boolean returnDelims)
Splits string
Parameters:
`str` - string to split
`delim` - delimiter
`returnDelims` - flag indicating whether to return the delimiters with string
Returns:
array of strings
implode
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) implode([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html) collection,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)
implode
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) implode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] values,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter)
parseExceptQuotes
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)[] parseExceptQuotes([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) cmd)
parses string by standard tokens, except parts wrapped in quotes
Parameters:
`cmd` -
Returns:
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
Compress specified directory recursivelly to the specified stream.
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
Parameters:
`rule` -
Returns:
rule
internString
public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) internString([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html) strings)
Replace all strings in given collection with String.intern().
Parameters:
`strings` - collection of object. Strings among these objects will be interned, other objects will remain.
Returns:
the same collection as given
dumpThreads
public static void dumpThreads()
Dumps all threads to system out.
reverseString
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) reverseString([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) source)
Given a string, returns a string with reversed characters.
Parameters:
`source` - string which has to be reversed.
Returns:
a string with reversed characters.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.rcpf.product.utils</a></div>
<h1 class="title" title="Class Utilities">Class Utilities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../../license/utils/CameoUtilities.html" title="class in com.nomagic.license.utils">com.nomagic.license.utils.CameoUtilities</a>
<div class="inheritance">com.nomagic.rcpf.product.utils.Utilities</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">Utilities</span>
<span class="extends-implements">extends <a href="../../../license/utils/CameoUtilities.html" title="class in com.nomagic.license.utils">CameoUtilities</a></span></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#areChildrenDisabled(javax.swing.JMenu)">areChildrenDisabled</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenu.html" title="class or interface in javax.swing">JMenu</a> menu)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Are all children disabled?</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkProperty(java.util.Properties,java.lang.String,boolean)">checkProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 boolean defaultValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkResolvableException(boolean)">checkResolvableException</a><wbr/>(boolean rule)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">if rule is false and it's DEVELOPER mode throws <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang"><code>IllegalStateException</code></a></div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#checkSystemProperty(java.lang.String,boolean)">checkSystemProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 boolean defaultValue)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks given system (boolean) property value</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAllLine(java.lang.String,java.lang.String)">clearAllLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all trash from string</div>
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
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#containsOnlyFiles(java.util.List)">containsOnlyFiles</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> list)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Indicates if given list contains only file objects.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.InputStream,java.io.OutputStream)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies all bytes from InputStream into OutputStream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.InputStream,java.io.OutputStream,long)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output,
 long crc)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies all bytes from InputStream into OutputStream.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyDirectory(java.io.File,java.io.File)">copyDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">copy all directory recursivelly</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copyFile(java.io.File,java.io.File)">copyFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dst)</code></div>
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
<div class="block">Moves outer rectengle in such way that it must cover inner one (if outer is smaller than inner resizes outer).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Cursor.html" title="class or interface in java.awt">Cursor</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createCursor(java.awt.Image,java.awt.Point,java.lang.String)">createCursor</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Image.html" title="class or interface in java.awt">Image</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> pt,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cursorName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates the cursor for given image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRectFromList(java.util.List)">createRectFromList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates rectangle from vector of points.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringRepresentation(java.util.Collection)">createStringRepresentation</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deepPointsClone(java.util.List)">deepPointsClone</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a deep clone of vector that contains points.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deepPointsClone(java.util.List,boolean)">deepPointsClone</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v,
 boolean cloneList)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a deep clone of vector that contains points.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deleteDirContent(java.io.File)">deleteDirContent</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes given directory contents.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deleteTree(java.io.File)">deleteTree</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes given directory and all its contents.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deleteTreeOnExit(java.io.File)">deleteTreeOnExit</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes given file (directory and all its contents) on exit.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#distributeInteger(int,int)">distributeInteger</a><wbr/>(int intValue,
 int size)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Distributes integer intValue into array of bytes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#dumpThreads()">dumpThreads</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Dumps all threads to system out.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getAsStringKeyStrokes(java.util.List,java.lang.String,java.lang.String)">getAsStringKeyStrokes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> shortcuts,
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
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileExtension(java.io.File)">getFileExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get The given file extension.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileName(java.lang.String)">getFileName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getFileWitoutExtention(java.lang.String)">getFileWitoutExtention</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns file name without extention (removes chars from last "." to end of string)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JMenuItem.html" title="class or interface in javax.swing">JMenuItem</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getItemWithText(javax.swing.JPopupMenu,java.lang.String)">getItemWithText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/JPopupMenu.html" title="class or interface in javax.swing">JPopupMenu</a> menu,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns inner component (not recursively) with given text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getTempDir()">getTempDir</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns directory can be used for writing temporary files.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasExtension(java.lang.String,java.lang.String)">hasExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given file name has given file extension.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasExtension(java.lang.String,java.util.List)">hasExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> extensions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given file name has one of given file extensions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#implode(java.lang.String%5B%5D,java.lang.String)">implode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] values,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#implode(java.util.Collection,java.lang.String)">implode</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a> collection,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#insertSeparators(char%5B%5D,java.lang.String,int)">insertSeparators</a><wbr/>(char[] chars,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 int groupSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs string from arrays of chars.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#internString(java.util.List)">internString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> strings)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replace all strings in given collection with String.intern().</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isAlphaNumeric(java.lang.String)">isAlphaNumeric</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isValidKeyCode(int)">isValidKeyCode</a><wbr/>(int keyCode)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given code is correct one or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#match(java.lang.String,java.lang.String)">match</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">algorithm for searching with wildcards.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#matchEmpty(java.lang.String,java.lang.String)">matchEmpty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> patter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Matches empty string also</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point)">normalize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> mRectToDraw,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> mFirstCorner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> mSecondCorner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">normalizes rectangle mRectToDraw; Calculates rectangle size and
 location using mFirstCorner and mSecondCorner.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExtension(java.lang.String,java.util.Collection)">removeExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; extensions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes file extension form given file name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeFromLine(java.lang.String,java.lang.String)">removeFromLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes from line trash line</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeNonUtf8CompliantCharacters(java.lang.String)">removeNonUtf8CompliantCharacters</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> inString)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeSeparators(java.lang.String,java.lang.String)">removeSeparators</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes separators from specified str</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replace(java.lang.String,java.lang.String,java.lang.String)">replace</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replaceWith)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces string fragment with another string</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceEpsString(java.lang.String)">replaceEpsString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> aStr)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replace special char for Eps format string</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#reverseString(java.lang.String)">reverseString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> source)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Given a string, returns a string with reversed characters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#sortStrings(java.util.Vector)">sortStrings</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Vector.html" title="class or interface in java.util">Vector</a> elem)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sorts elements in strings' vector</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#splitString(java.lang.String,java.lang.String,boolean)">splitString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delim,
 boolean returnDelims)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Splits string</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#swapVector(java.util.List)">swapVector</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> v)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Swaps vector ( first element will be last, same with others elements)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toByteArray(java.io.InputStream)">toByteArray</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies the given file into the array of bytes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toByteArray(java.lang.String)">toByteArray</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bytes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns byte array from string formated in toString(byte[]) method.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(byte%5B%5D)">toString</a><wbr/>(byte[] data)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns string representation of the given byte array.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(java.io.InputStream)">toString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> inputStream)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get String representation of inputStream</div>
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
<div class="block">Compress specified directory recursivelly to the specified stream.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.license.utils.CameoUtilities">Methods inherited from class com.nomagic.license.utils.<a href="../../../license/utils/CameoUtilities.html" title="class in com.nomagic.license.utils">CameoUtilities</a></h3>
<code><a href="../../../license/utils/CameoUtilities.html#copy(java.io.Reader,java.io.Writer)">copy</a>, <a href="../../../license/utils/CameoUtilities.html#isEqual(java.lang.Object%5B%5D,java.lang.Object%5B%5D)">isEqual</a>, <a href="../../../license/utils/CameoUtilities.html#isEqual(java.lang.Object,java.lang.Object)">isEqual</a>, <a href="../../../license/utils/CameoUtilities.html#replaceNewLine(java.lang.String,java.lang.String)">replaceNewLine</a>, <a href="../../../license/utils/CameoUtilities.html#toString(java.io.InputStream,java.lang.String)">toString</a></code></div>
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
<section class="detail" id="hasExtension(java.lang.String,java.util.List)">
<h3>hasExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> extensions)</span></div>
<div class="block">Checks if given file name has one of given file extensions.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - </dd>
<dd><code>extensions</code> - </dd>
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="hasExtension(java.lang.String,java.lang.String)">
<h3>hasExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
<div class="block">Checks if given file name has given file extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - </dd>
<dd><code>extension</code> - </dd>
<dt>Returns:</dt>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeExtension(java.lang.String,java.util.Collection)">
<h3>removeExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; extensions)</span></div>
<div class="block">Removes file extension form given file name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - </dd>
<dd><code>extensions</code> - extensions</dd>
<dt>Returns:</dt>
</dl>
</section>
</li>
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
<div class="block">algorithm for searching with wildcards.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pattern</code> - The given pattern.</dd>
<dd><code>string</code> - String.</dd>
<dt>Returns:</dt>
<dd>boolean expression.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="matchEmpty(java.lang.String,java.lang.String)">
<h3>matchEmpty</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">matchEmpty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> patter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
<div class="block">Matches empty string also</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>patter</code> - The given pattern.</dd>
<dd><code>string</code> - The given string.</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
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
<section class="detail" id="removeFromLine(java.lang.String,java.lang.String)">
<h3>removeFromLine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeFromLine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</span></div>
<div class="block">Removes from line trash line</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>line</code> - the given line.</dd>
<dd><code>trash</code> - characters as string.</dd>
<dt>Returns:</dt>
<dd>The given string without From Line.</dd>
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
<dd><code>string</code> - The given string.</dd>
<dd><code>c</code> - character.</dd>
<dt>Returns:</dt>
<dd>number of time.</dd>
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
<dd><code>small</code> - Small rectangle.</dd>
<dd><code>big</code> - Big rectangle.</dd>
<dt>Returns:</dt>
<dd>New rectangle.</dd>
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
<section class="detail" id="coverRectangle(java.awt.Rectangle,java.awt.Rectangle)">
<h3>coverRectangle</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">coverRectangle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> inner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> outer)</span></div>
<div class="block">Moves outer rectengle in such way that it must cover inner one (if outer is smaller than inner resizes outer).
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">createRectFromList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> v)</span></div>
<div class="block">Creates rectangle from vector of points.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - List of point.</dd>
<dt>Returns:</dt>
<dd>null if vector was empty.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="swapVector(java.util.List)">
<h3>swapVector</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">swapVector</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> v)</span></div>
<div class="block">Swaps vector ( first element will be last, same with others elements)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>v</code> - List that be swaped.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileWitoutExtention(java.lang.String)">
<h3>getFileWitoutExtention</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileWitoutExtention</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filename)</span></div>
<div class="block">Returns file name without extention (removes chars from last "." to end of string)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filename</code> - The given file name.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFileExtension(java.io.File)">
<h3>getFileExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getFileExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Get The given file extension.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>file</code> - The given file.</dd>
<dt>Returns:</dt>
<dd>File extension.</dd>
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
<section class="detail" id="copy(java.io.InputStream,java.io.OutputStream,long)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output,
 long crc)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Copies all bytes from InputStream into OutputStream. Closes the streams.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - the inputstream.</dd>
<dd><code>output</code> - the output stream.</dd>
<dd><code>crc</code> - crc to check. -1 if do not check crc.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
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
<dd><code>input</code> - the inputstream.</dd>
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
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> dst)</span></div>
<div class="block">Copy source file to destination file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - Source file.</dd>
<dd><code>dst</code> - destination file.</dd>
<dt>Returns:</dt>
<dd>True if work successful.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copyDirectory(java.io.File,java.io.File)">
<h3>copyDirectory</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">copyDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> source,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> destination)</span></div>
<div class="block">copy all directory recursivelly</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>source</code> - </dd>
<dd><code>destination</code> - </dd>
</dl>
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
<dd>Curser.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAsStringKeyStrokes(java.util.List,java.lang.String,java.lang.String)">
<h3>getAsStringKeyStrokes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsStringKeyStrokes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> shortcuts,
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAsString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/javax/swing/KeyStroke.html" title="class or interface in javax.swing">KeyStroke</a> e)</span></div>
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
<div class="block">Returns byte array from string formated in toString(byte[]) method.</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">normalize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> mRectToDraw,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> mFirstCorner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> mSecondCorner)</span></div>
<div class="block">normalizes rectangle mRectToDraw; Calculates rectangle size and
 location using mFirstCorner and mSecondCorner.
 This method is useful when resizing a shape and only opposite corners are
 known.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mRectToDraw</code> - rectangle to normalize</dd>
<dd><code>mFirstCorner</code> - first corner</dd>
<dd><code>mSecondCorner</code> - second corner</dd>
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
<div class="block">Returns directory can be used for writing temporary files.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>string.</dd>
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
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - </dd>
</dl>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">deleteTree</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> f)</span></div>
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
<section class="detail" id="splitString(java.lang.String,java.lang.String,boolean)">
<h3>splitString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">splitString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> str,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delim,
 boolean returnDelims)</span></div>
<div class="block">Splits string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>str</code> - string to split</dd>
<dd><code>delim</code> - delimiter</dd>
<dd><code>returnDelims</code> - flag indicating whether to return the delimiters with string</dd>
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
</section>
</li>
<li>
<section class="detail" id="implode(java.lang.String[],java.lang.String)">
<h3>implode</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">implode</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[] values,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter)</span></div>
</section>
</li>
<li>
<section class="detail" id="parseExceptQuotes(java.lang.String)">
<h3>parseExceptQuotes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>[]</span> <span class="element-name">parseExceptQuotes</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> cmd)</span></div>
<div class="block">parses string by standard tokens, except parts wrapped in quotes</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>cmd</code> - </dd>
<dt>Returns:</dt>
</dl>
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
<div class="block">Compress specified directory recursivelly to the specified stream.</div>
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
<dt>Parameters:</dt>
<dd><code>rule</code> - </dd>
<dt>Returns:</dt>
<dd>rule</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="internString(java.util.List)">
<h3>internString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a></span> <span class="element-name">internString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> strings)</span></div>
<div class="block">Replace all strings in given collection with String.intern().</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>strings</code> - collection of object. Strings among these objects will be interned, other objects will remain.</dd>
<dt>Returns:</dt>
<dd>the same collection as given</dd>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
