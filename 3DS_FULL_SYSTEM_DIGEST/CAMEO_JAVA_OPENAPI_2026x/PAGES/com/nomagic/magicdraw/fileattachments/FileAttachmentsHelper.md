# JAVA OPENAPI: FileAttachmentsHelper (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/fileattachments/FileAttachmentsHelper.html
- source_path: `com/nomagic/magicdraw/fileattachments/FileAttachmentsHelper.html`
- source_sha256: `ccbed136a26d5cbbb659c7e36af89ed0b757338037c86cf53cc861bacea1209d`
- captured_utc: `2026-07-14T16:57:57.884534+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.fileattachments](package-summary.html)

## Class FileAttachmentsHelper

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.fileattachments.FileAttachmentsHelper

@OpenApiAllpublic classFileAttachmentsHelper
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Methods to work with files attached to the model: create attached file, read it or remove the attachment.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[FileAttachmentsHelper](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html)`
`[createAttachedFileElement](#createAttachedFileElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owner)`
Creates a comment stereotyped with AttachedFile stereotype.
`static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[extractToDirectory](#extractToDirectory(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) directory,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static [InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html)`
`[getStoredFileInputStream](#getStoredFileInputStream(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`

`static void`
`[removeStoredFile](#removeStoredFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Removes any file that has been previously stored using [`storeFile(Element, File)`](#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)) or [`storeFileToAttachedFile(Comment, File)`](#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)) methods.
`static boolean`
`[storeFile](#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Stores a file inside the element.
`static boolean`
`[storeFileToAttachedFile](#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File))([Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) attachedFileElement,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)`
Attaches provided file to the AttachedFile element and updates informative element properties that are visible to the user:
 name, size, dateAdded, dateModified, author.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
FileAttachmentsHelper
public FileAttachmentsHelper()
 ============ METHOD DETAIL ========== 
Method Details
storeFile
public static boolean storeFile([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Stores a file inside the element. This attachment will not be visible in MagicDraw GUI.
 If some file was already attached, then it will be replaced.
Parameters:
`element` - any element
`file` - existing file to store
Returns:
true if file was successfully attached
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - exception
storeFileToAttachedFile
public static boolean storeFileToAttachedFile([Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) attachedFileElement,
 @CheckForNull
 [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) file)
Attaches provided file to the AttachedFile element and updates informative element properties that are visible to the user:
 name, size, dateAdded, dateModified, author.
 This method can also be used to replace previously stored file.
Parameters:
`attachedFileElement` - stereotyped comment created with the [`createAttachedFileElement(Element)`](#createAttachedFileElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)) method.
`file` - existing file to store.
removeStoredFile
public static void removeStoredFile([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Removes any file that has been previously stored using [`storeFile(Element, File)`](#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)) or [`storeFileToAttachedFile(Comment, File)`](#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)) methods.
Parameters:
`element` - element to remove attachment from
getStoredFileInputStream
@CheckForNullpublic static [InputStream](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html) getStoredFileInputStream([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Parameters:
`element` - element that has a file stored with [`storeFile(Element, File)`](#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)) or [`storeFileToAttachedFile(Comment, File)`](#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)) method.
Returns:
InputStream to read the contents of the attached file from.
extractToDirectory
@CheckForNullpublic static [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) extractToDirectory([File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) directory,
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
 throws [IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)
Parameters:
`directory` - directory to save the attachment to. It will be created if not yet exists
`element` - element that has a file stored with [`storeFile(Element, File)`](#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)) or [`storeFileToAttachedFile(Comment, File)`](#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)) method.
Returns:
File with the attachment stored in it. Null if there was no attached file on the element
Throws:
`[IOException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html)` - when saving of the file fails
createAttachedFileElement
public static [Comment](../../uml2/ext/magicdraw/classes/mdkernel/Comment.html) createAttachedFileElement([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) owner)
Creates a comment stereotyped with AttachedFile stereotype. Such element appears as AttachedFile element in MagicDraw UI.
Parameters:
`owner` - parent for the new element
Returns:
AttachedFile element

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.fileattachments</a></div>
<h1 class="title" title="Class FileAttachmentsHelper">Class FileAttachmentsHelper</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.fileattachments.FileAttachmentsHelper</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">FileAttachmentsHelper</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Methods to work with files attached to the model: create attached file, read it or remove the attachment.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">FileAttachmentsHelper</a>()</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createAttachedFileElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">createAttachedFileElement</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a comment stereotyped with AttachedFile stereotype.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#extractToDirectory(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">extractToDirectory</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> directory,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getStoredFileInputStream(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getStoredFileInputStream</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#removeStoredFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">removeStoredFile</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes any file that has been previously stored using <a href="#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)"><code>storeFile(Element, File)</code></a> or <a href="#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)"><code>storeFileToAttachedFile(Comment, File)</code></a> methods.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)">storeFile</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Stores a file inside the element.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)">storeFileToAttachedFile</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> attachedFileElement,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Attaches provided file to the AttachedFile element and updates informative element properties that are visible to the user:
 name, size, dateAdded, dateModified, author.</div>
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
<h3>FileAttachmentsHelper</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">FileAttachmentsHelper</span>()</div>
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
<section class="detail" id="storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)">
<h3>storeFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">storeFile</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span>
                         throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<div class="block">Stores a file inside the element. This attachment will not be visible in MagicDraw GUI.
 If some file was already attached, then it will be replaced.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - any element</dd>
<dd><code>file</code> - existing file to store</dd>
<dt>Returns:</dt>
<dd>true if file was successfully attached</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - exception</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)">
<h3>storeFileToAttachedFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">storeFileToAttachedFile</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a> attachedFileElement,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> file)</span></div>
<div class="block">Attaches provided file to the AttachedFile element and updates informative element properties that are visible to the user:
 name, size, dateAdded, dateModified, author.
 This method can also be used to replace previously stored file.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attachedFileElement</code> - stereotyped comment created with the <a href="#createAttachedFileElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)"><code>createAttachedFileElement(Element)</code></a> method.</dd>
<dd><code>file</code> - existing file to store.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeStoredFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>removeStoredFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">removeStoredFile</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="block">Removes any file that has been previously stored using <a href="#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)"><code>storeFile(Element, File)</code></a> or <a href="#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)"><code>storeFileToAttachedFile(Comment, File)</code></a> methods.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element to remove attachment from</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStoredFileInputStream(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getStoredFileInputStream</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/InputStream.html" title="class or interface in java.io">InputStream</a></span> <span class="element-name">getStoredFileInputStream</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - element that has a file stored with <a href="#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)"><code>storeFile(Element, File)</code></a> or <a href="#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)"><code>storeFileToAttachedFile(Comment, File)</code></a> method.</dd>
<dt>Returns:</dt>
<dd>InputStream to read the contents of the attached file from.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="extractToDirectory(java.io.File,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>extractToDirectory</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">extractToDirectory</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a> directory,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span>
                               throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>directory</code> - directory to save the attachment to. It will be created if not yet exists</dd>
<dd><code>element</code> - element that has a file stored with <a href="#storeFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.io.File)"><code>storeFile(Element, File)</code></a> or <a href="#storeFileToAttachedFile(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Comment,java.io.File)"><code>storeFileToAttachedFile(Comment, File)</code></a> method.</dd>
<dt>Returns:</dt>
<dd>File with the attachment stored in it. Null if there was no attached file on the element</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/IOException.html" title="class or interface in java.io">IOException</a></code> - when saving of the file fails</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createAttachedFileElement(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>createAttachedFileElement</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Comment.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Comment</a></span> <span class="element-name">createAttachedFileElement</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> owner)</span></div>
<div class="block">Creates a comment stereotyped with AttachedFile stereotype. Such element appears as AttachedFile element in MagicDraw UI.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>owner</code> - parent for the new element</dd>
<dt>Returns:</dt>
<dd>AttachedFile element</dd>
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
