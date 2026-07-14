# JAVA OPENAPI: CameoUtilities (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/utils/CameoUtilities.html
- source_path: `com/nomagic/utils/CameoUtilities.html`
- source_sha256: `4769b9dabd5351af511175abdbfb51f2f28e4ad7a2806235b38d2b5c47cacde9`
- captured_utc: `2026-07-14T16:46:49.332455+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.utils](package-summary.html)

## Class CameoUtilities

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.utils.CameoUtilities

Direct Known Subclasses:
`[Utilities](Utilities.html)`

@OpenApiAllpublic classCameoUtilities
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)

General purpose utilities.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CameoUtilities](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[clearAllLine](#clearAllLine(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) trash)`
Removes all trash from string
`static void`
`[copy](#copy(java.io.InputStream,java.io.OutputStream))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) output)`

`static void`
`[copy](#copy(java.io.Reader,java.io.Writer))([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) input,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) output)`
Copies all bytes from Reader into Writer.
`static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html)`
`[createRectFromList](#createRectFromList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> v)`
Creates rectangle from vector of points.
`static byte[]`
`[decodeBase64](#decodeBase64(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)`
Decode string using Base64 encoding.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)>`
`[deepPointsClone](#deepPointsClone(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> v)`
Makes a deep clone of vector that contains points.
`static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)>`
`[deepPointsClone](#deepPointsClone(java.util.List,boolean))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> v,
 boolean cloneList)`
Makes a deep clone of vector that contains points.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[encodeBase64](#encodeBase64(byte%5B%5D))(byte[] abyte0)`
Encodes data using base64 encoding.
`static boolean`
`[hasExtension](#hasExtension(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)`
Checks if given file name has given file extension.
`static boolean`
`[hasExtension](#hasExtension(java.lang.String,java.util.List))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> extensions)`
Checks if given file name has one of given file extensions.
`static boolean`
`[isEqual](#isEqual(java.lang.Object%5B%5D,java.lang.Object%5B%5D))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[] obj1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[] obj2)`
Returns true of both objects are nulls or equal
`static boolean`
`[isEqual](#isEqual(java.lang.Object,java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj2)`
Returns true of both objects are nulls or equal
`static void`
`[normalize](#normalize(java.awt.Rectangle))([Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) rect)`
normalizes rectangle mRectToDraw;
`static void`
`[normalize](#normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point))([Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) rectangle,
 [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) firstCorner,
 [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) secondCorner)`
Normalizes rectangle; Calculates rectangle size and location using firstCorner and secondCorner.
`static void`
`[removeClosestToTheMiddle](#removeClosestToTheMiddle(java.util.List,java.lang.Object,java.lang.Object))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) objects,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o2)`
Removes an object from the list which is closest to the middle.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[removeExtension](#removeExtension(java.lang.String,java.util.Collection))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> extensions)`
Removes file extension form given file name.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[removeFromLine](#removeFromLine(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) line,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) trash)`
Removes from line trash line
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[replace](#replace(java.lang.String,java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replaceWith)`
Replaces string fragment with another string
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[replaceNewLine](#replaceNewLine(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) lineSeparator)`
Separate lines with the provided separator string.
`static byte[]`
`[toByteArray](#toByteArray(java.io.InputStream))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) stream)`
Copies the given file into the array of bytes.
`static byte[]`
`[toByteArray](#toByteArray(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bytes)`
Returns byte array from string formatted in toString(byte[]) method.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(byte%5B%5D))(byte[] data)`
Returns string representation of the given byte array.
`static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[toString](#toString(java.io.InputStream,java.lang.String))([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) inputStream,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding)`
Get String representation of inputStream
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CameoUtilities
public CameoUtilities()
 ============ METHOD DETAIL ========== 
Method Details
clearAllLine
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) clearAllLine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) trash)
Removes all trash from string
Parameters:
`src` - String from witch thrash should be removed
`trash` - Trash string.
Returns:
cleared string or same if nothing was cleared
isEqual
public static boolean isEqual(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj1,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj2)
Returns true of both objects are nulls or equal
Parameters:
`obj1` - First object.
`obj2` - Second object.
Returns:
boolean
isEqual
public static boolean isEqual(@CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[] obj1,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)[] obj2)
Returns true of both objects are nulls or equal
Parameters:
`obj1` - object list.
`obj2` - object list.
Returns:
boolean
toString
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) inputStream,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encoding)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Get String representation of inputStream
Parameters:
`inputStream` - The given inputStream
Returns:
String representation
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
replaceNewLine
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replaceNewLine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) string,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) lineSeparator)
Separate lines with the provided separator string.
Parameters:
`string` - input string.
`lineSeparator` - line separator.
Returns:
result string.
copy
public static void copy([Reader](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html) input,
 [Writer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Copies all bytes from Reader into Writer. Closes the reader and writer.
Parameters:
`input` - the reader.
`output` - the writer.
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
copy
public static void copy([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) input,
 [OutputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html) output)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)`
toByteArray
public static byte[] toByteArray([InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) stream)
Copies the given file into the array of bytes.
Parameters:
`stream` - the given file.
Returns:
the byte array with the context of the file;null if some errors occurs
toByteArray
public static byte[] toByteArray([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bytes)
Returns byte array from string formatted in toString(byte[]) method.
Parameters:
`bytes` - the given string.
Returns:
the byte array.
toString
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) toString(byte[] data)
Returns string representation of the given byte array.
Parameters:
`data` - the given bytes array.
Returns:
the string representation (every byte is represented as hex string separated by space)
removeFromLine
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) removeFromLine([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) line,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) trash)
Removes from line trash line
Parameters:
`line` - the given line.
`trash` - characters as string.
Returns:
The given string without From Line.
hasExtension
public static boolean hasExtension([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> extensions)
Checks if given file name has one of given file extensions.
hasExtension
public static boolean hasExtension([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) extension)
Checks if given file name has given file extension.
removeExtension
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) removeExtension([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)> extensions)
Removes file extension form given file name.
deepPointsClone
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> deepPointsClone([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> v)
Makes a deep clone of vector that contains points.
Parameters:
`v` - List of point.
Returns:
vector
deepPointsClone
public static [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> deepPointsClone([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> v,
 boolean cloneList)
Makes a deep clone of vector that contains points.
Parameters:
`v` - List of point.
`cloneList` - True if clone to new list.
Returns:
vector
normalize
public static void normalize([Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) rectangle,
 [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) firstCorner,
 [Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html) secondCorner)
Normalizes rectangle; Calculates rectangle size and location using firstCorner and secondCorner.
Parameters:
`rectangle` - rectangle to normalize
`firstCorner` - first corner
`secondCorner` - second corner
normalize
public static void normalize([Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) rect)
normalizes rectangle mRectToDraw;
Parameters:
`rect` - rectangle to normalize
createRectFromList
@CheckForNullpublic static [Rectangle](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html) createRectFromList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[Point](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html)> v)
Creates rectangle from vector of points.
Parameters:
`v` - List of point
Returns:
null if vector was empty
replace
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replace([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) src,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) pattern,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) replaceWith)
Replaces string fragment with another string
Parameters:
`src` - Source string.
`pattern` - String pattern.
`replaceWith` - The another string.
Returns:
string.
removeClosestToTheMiddle
public static void removeClosestToTheMiddle([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html) objects,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o1,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) o2)
Removes an object from the list which is closest to the middle.
Parameters:
`objects` - - a list of objects.
`o1` - - first object.
`o2` - - second object.
encodeBase64
public static [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) encodeBase64(byte[] abyte0)
Encodes data using base64 encoding.
Parameters:
`abyte0` - data for encoding
Returns:
encoded string
decodeBase64
public static byte[] decodeBase64([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) s)
Decode string using Base64 encoding.
Parameters:
`s` - string for decoding
Returns:
decoded data

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.utils</a></div>
<h1 class="title" title="Class CameoUtilities">Class CameoUtilities</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.utils.CameoUtilities</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="Utilities.html" title="class in com.nomagic.utils">Utilities</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CameoUtilities</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CameoUtilities</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAllLine(java.lang.String,java.lang.String)">clearAllLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all trash from string</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.InputStream,java.io.OutputStream)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#copy(java.io.Reader,java.io.Writer)">copy</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> output)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies all bytes from Reader into Writer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createRectFromList(java.util.List)">createRectFromList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates rectangle from vector of points.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#decodeBase64(java.lang.String)">decodeBase64</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Decode string using Base64 encoding.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deepPointsClone(java.util.List)">deepPointsClone</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a deep clone of vector that contains points.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#deepPointsClone(java.util.List,boolean)">deepPointsClone</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v,
 boolean cloneList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Makes a deep clone of vector that contains points.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#encodeBase64(byte%5B%5D)">encodeBase64</a><wbr/>(byte[] abyte0)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Encodes data using base64 encoding.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasExtension(java.lang.String,java.lang.String)">hasExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given file name has given file extension.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#hasExtension(java.lang.String,java.util.List)">hasExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; extensions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Checks if given file name has one of given file extensions.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEqual(java.lang.Object%5B%5D,java.lang.Object%5B%5D)">isEqual</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] obj1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] obj2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true of both objects are nulls or equal</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isEqual(java.lang.Object,java.lang.Object)">isEqual</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj2)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns true of both objects are nulls or equal</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalize(java.awt.Rectangle)">normalize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">normalizes rectangle mRectToDraw;</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point)">normalize</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rectangle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> firstCorner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> secondCorner)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Normalizes rectangle; Calculates rectangle size and location using firstCorner and secondCorner.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeClosestToTheMiddle(java.util.List,java.lang.Object,java.lang.Object)">removeClosestToTheMiddle</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> objects,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o2)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes an object from the list which is closest to the middle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeExtension(java.lang.String,java.util.Collection)">removeExtension</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; extensions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes file extension form given file name.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeFromLine(java.lang.String,java.lang.String)">removeFromLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes from line trash line</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replace(java.lang.String,java.lang.String,java.lang.String)">replace</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replaceWith)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Replaces string fragment with another string</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#replaceNewLine(java.lang.String,java.lang.String)">replaceNewLine</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lineSeparator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Separate lines with the provided separator string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toByteArray(java.io.InputStream)">toByteArray</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Copies the given file into the array of bytes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toByteArray(java.lang.String)">toByteArray</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bytes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns byte array from string formatted in toString(byte[]) method.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(byte%5B%5D)">toString</a><wbr/>(byte[] data)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns string representation of the given byte array.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#toString(java.io.InputStream,java.lang.String)">toString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> inputStream,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Get String representation of inputStream</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>CameoUtilities</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CameoUtilities</span>()</div>
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
<section class="detail" id="clearAllLine(java.lang.String,java.lang.String)">
<h3>clearAllLine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">clearAllLine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</span></div>
<div class="block">Removes all trash from string</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>src</code> - String from witch thrash should be removed</dd>
<dd><code>trash</code> - Trash string.</dd>
<dt>Returns:</dt>
<dd>cleared string or same if nothing was cleared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEqual(java.lang.Object,java.lang.Object)">
<h3>isEqual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEqual</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj1,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj2)</span></div>
<div class="block">Returns true of both objects are nulls or equal</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj1</code> - First object.</dd>
<dd><code>obj2</code> - Second object.</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEqual(java.lang.Object[],java.lang.Object[])">
<h3>isEqual</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isEqual</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] obj1,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>[] obj2)</span></div>
<div class="block">Returns true of both objects are nulls or equal</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>obj1</code> - object list.</dd>
<dd><code>obj2</code> - object list.</dd>
<dt>Returns:</dt>
<dd>boolean</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toString(java.io.InputStream,java.lang.String)">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> inputStream,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> encoding)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Get String representation of inputStream</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>inputStream</code> - The given inputStream</dd>
<dt>Returns:</dt>
<dd>String representation</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="replaceNewLine(java.lang.String,java.lang.String)">
<h3>replaceNewLine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">replaceNewLine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lineSeparator)</span></div>
<div class="block">Separate lines with the provided separator string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>string</code> - input string.</dd>
<dd><code>lineSeparator</code> - line separator.</dd>
<dt>Returns:</dt>
<dd>result string.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.Reader,java.io.Writer)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Reader.html" title="class or interface in java.io">Reader</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Writer.html" title="class or interface in java.io">Writer</a> output)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Copies all bytes from Reader into Writer. Closes the reader and writer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - the reader.</dd>
<dd><code>output</code> - the writer.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="copy(java.io.InputStream,java.io.OutputStream)">
<h3>copy</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">copy</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> input,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/OutputStream.html" title="class or interface in java.io">OutputStream</a> output)</span>
                 throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toByteArray(java.io.InputStream)">
<h3>toByteArray</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">toByteArray</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a> stream)</span></div>
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
<section class="detail" id="toByteArray(java.lang.String)">
<h3>toByteArray</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">toByteArray</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bytes)</span></div>
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
<section class="detail" id="toString(byte[])">
<h3>toString</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">toString</span><wbr/><span class="parameters">(byte[] data)</span></div>
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
<section class="detail" id="removeFromLine(java.lang.String,java.lang.String)">
<h3>removeFromLine</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeFromLine</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> line,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> trash)</span></div>
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
<section class="detail" id="hasExtension(java.lang.String,java.util.List)">
<h3>hasExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; extensions)</span></div>
<div class="block">Checks if given file name has one of given file extensions.</div>
</section>
</li>
<li>
<section class="detail" id="hasExtension(java.lang.String,java.lang.String)">
<h3>hasExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">hasExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> extension)</span></div>
<div class="block">Checks if given file name has given file extension.</div>
</section>
</li>
<li>
<section class="detail" id="removeExtension(java.lang.String,java.util.Collection)">
<h3>removeExtension</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">removeExtension</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; extensions)</span></div>
<div class="block">Removes file extension form given file name.</div>
</section>
</li>
<li>
<section class="detail" id="deepPointsClone(java.util.List)">
<h3>deepPointsClone</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">deepPointsClone</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt;</span> <span class="element-name">deepPointsClone</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v,
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
<section class="detail" id="normalize(java.awt.Rectangle,java.awt.Point,java.awt.Point)">
<h3>normalize</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">normalize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rectangle,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> firstCorner,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a> secondCorner)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">normalize</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> rect)</span></div>
<div class="block">normalizes rectangle mRectToDraw;</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>rect</code> - rectangle to normalize</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRectFromList(java.util.List)">
<h3>createRectFromList</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">createRectFromList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/awt/Point.html" title="class or interface in java.awt">Point</a>&gt; v)</span></div>
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
<section class="detail" id="replace(java.lang.String,java.lang.String,java.lang.String)">
<h3>replace</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">replace</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> src,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pattern,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> replaceWith)</span></div>
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
<section class="detail" id="removeClosestToTheMiddle(java.util.List,java.lang.Object,java.lang.Object)">
<h3>removeClosestToTheMiddle</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeClosestToTheMiddle</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a> objects,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o1,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o2)</span></div>
<div class="block">Removes an object from the list which is closest to the middle.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>objects</code> - - a list of objects.</dd>
<dd><code>o1</code> - - first object.</dd>
<dd><code>o2</code> - - second object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="encodeBase64(byte[])">
<h3>encodeBase64</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">encodeBase64</span><wbr/><span class="parameters">(byte[] abyte0)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">decodeBase64</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> s)</span></div>
<div class="block">Decode string using Base64 encoding.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>s</code> - string for decoding</dd>
<dt>Returns:</dt>
<dd>decoded data</dd>
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
