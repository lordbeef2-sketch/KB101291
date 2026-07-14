# JAVA OPENAPI: BookmarkTool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicreport/engine/tools/BookmarkTool.html
- source_path: `com/nomagic/magicreport/engine/tools/BookmarkTool.html`
- source_sha256: `f77b7ed9a7efa3cfc6cf9fac9820e7e8a96f598a6edfca2a5803d9567a11a669`
- captured_utc: `2026-07-14T16:58:37.176284+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.tools](package-summary.html)

## Class BookmarkTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../Tool.html)
com.nomagic.magicreport.engine.tools.BookmarkTool

All Implemented Interfaces:
`[ITool](../ITool.html)`, `[IVariable](../../IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classBookmarkTool
extends [Tool](../Tool.html)

Contains utilities functions for bookmark. Context name of this class is "bookmark". Public functions of this
 class are able to access via template by using `$bookmark`

Since:
Jun 19, 2007
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.BookmarkTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
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
`[BookmarkTool](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Bookmark](../../Bookmark.html)`
`[create](#create(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bookmarkObject)`
Function to create bookmark.
`[Bookmark](../../Bookmark.html)`
`[create](#create(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bookmarkId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bookmarkObject)`
Function to create bookmark.
`[Bookmark](../../Bookmark.html)`
`[create](#create(java.lang.String,java.lang.Object,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bookmarkId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bookmarkObject,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementType)`
Function to create bookmark with the specified element type.
`[TextReference](../../TextReference.html)`
`[createRef](#createRef(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId)`
Return a bookmark for REF from given string.
`[TextReference](../../TextReference.html)`
`[createRef](#createRef(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)`
Return a bookmark for REF from given string.
`[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html)`
`[getBookmarkId](#getBookmarkId(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)`
Return a bookmark id from given string.
`[Link](../../Link.html)`
`[open](#open(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)`
Function to create hyperlink for bookmark.
`[Link](../../Link.html)`
`[open](#open(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bookmarkId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)`
Function to create hyperlink for bookmark.
`[TextReference](../../TextReference.html)`
`[openRef](#openRef(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId)`
Return a reference to REF.
`[TextReference](../../TextReference.html)`
`[openRef](#openRef(java.lang.String,java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refText)`
eturn a reference to REF.
`[Link](../../Link.html)`
`[openURL](#openURL(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)`
Function to create hyperlink for open an URL.
`[Link](../../Link.html)`
`[openURL](#openURL(java.net.URI,java.lang.Object))([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)`
Function to create hyperlink for open an URL.
`[Link](../../Link.html)`
`[openURL](#openURL(java.net.URL,java.lang.Object))([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)`
Function to create hyperlink for open an URL.
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
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.BookmarkTool.CONTEXT_NAME)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
BookmarkTool
public BookmarkTool()
 ============ METHOD DETAIL ========== 
Method Details
openURL
public [Link](../../Link.html) openURL([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) url,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)
Function to create hyperlink for open an URL.
 
 <code>
 $bookmark.openURL("http://www.nomagicasia.com", "NoMagic Asia")
 </code>
Parameters:
`url` - the url text. If null, empty string will be used.
`content` - the text content. If null, empty string will be used.
Returns:
content with hyperlink in document format.
See Also:
[`open(String, Object)`](#open(java.lang.String,java.lang.Object))
[`create(Object)`](#create(java.lang.Object))
openURL
public [Link](../../Link.html) openURL([URL](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html) url,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)
Function to create hyperlink for open an URL.
 
 <code>
 $bookmark.openURL($url, "NoMagic Asia")
 </code>
Parameters:
`url` - the URL instance. If null, empty string will be used.
`content` - text content. If null, empty string will be used.
Returns:
content with hyperlink in RTF format.
See Also:
[`open(String, Object)`](#open(java.lang.String,java.lang.Object))
[`create(Object)`](#create(java.lang.Object))
openURL
public [Link](../../Link.html) openURL([URI](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html) uri,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)
Function to create hyperlink for open an URL.
 
 <code>
 $bookmark.openURL($uri, "NoMagic Asia")
 </code>
Parameters:
`uri` - the URI instance. If null, empty string will be used.
`content` - text content. If null, empty string will be used.
Returns:
content with hyperlink in RTF format.
See Also:
[`open(String, Object)`](#open(java.lang.String,java.lang.Object))
[`create(Object)`](#create(java.lang.Object))
open
public [Link](../../Link.html) open([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)
Function to create hyperlink for bookmark. The bookmark ID will be automatically generated from content.
 
 <code>
 #foreach ($uc in $UseCase)
 $bookmark.open($uc.name)
 #end
 #foreach ($uc in $UseCase)
 $bookmark.create($uc.name)
 #end
 </code>
Parameters:
`content` - text content. If null, ID will be a digest of "0" and name will be a hash code of object.
Returns:
content with hyperlink in RTF format.
See Also:
[`open(String, Object)`](#open(java.lang.String,java.lang.Object))
[`create(Object)`](#create(java.lang.Object))
open
public [Link](../../Link.html) open([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bookmarkId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) content)
Function to create hyperlink for bookmark. `bookmarkID` value must match with parameter
 `bookmarkID` that pass into [`create(String, Object)`](#create(java.lang.String,java.lang.Object)) function.
 
 <code>
 #foreach ($uc in $UseCase)
 $bookmark.open($uc.name)
 #end
 #foreach ($uc in $UseCase)
 $bookmark.create($uc.name)
 #end
 </code>
Parameters:
`bookmarkId` - the bookmark id. If null, digest of empty string will be used.
`content` - text content. If null, empty string will be used.
Returns:
content with hyperlink in RTF format.
See Also:
[`open(Object)`](#open(java.lang.Object))
[`create(String, Object)`](#create(java.lang.String,java.lang.Object))
create
public [Bookmark](../../Bookmark.html) create([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bookmarkObject)
Function to create bookmark. The bookmark ID will be automatically generated from bookmark object.
 
 <code>
 #foreach ($uc in $UseCase)
 $bookmark.open($uc.name)
 #end
 #foreach ($uc in $UseCase)
 $bookmark.create($uc.name)
 #end
 </code>
Parameters:
`bookmarkObject` - the bookmark object or content. If null, ID will be a digest of "0" and name will be a
 hash code of object.
Returns:
content with bookmark in RTF format.
create
public [Bookmark](../../Bookmark.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bookmarkId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bookmarkObject)
Function to create bookmark. The default element type for this function is "label".
 
 <code>
 #foreach ($uc in $UseCase)
 $bookmark.open($uc.ID, $uc.name)
 #end
 #foreach ($uc in $UseCase)
 $bookmark.create($uc.ID, $uc.name)
 #end
 </code>
Parameters:
`bookmarkId` - the bookmark. If null, digest of empty string will be used.
`bookmarkObject` - the bookmark object or content. If null, empty string will be used.
Returns:
content with bookmark in RTF format.
create
public [Bookmark](../../Bookmark.html) create([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bookmarkId,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bookmarkObject,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) elementType)
Function to create bookmark with the specified element type.
 
 <code>
 #foreach ($uc in $UseCase)
 $bookmark.open($uc.ID, $uc.name)
 #end
 #foreach ($uc in $UseCase)
 $bookmark.create($uc.ID, $uc.name, "label")
 #end
 </code>
Parameters:
`bookmarkId` - the bookmark id. If null, digest of empty string will be used.
`bookmarkObject` - the bookmark object or content. If null, empty string will be used.
`elementType` - name of element type e.g. html tag.
Returns:
content with bookmark in format.
getBookmarkId
public [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) getBookmarkId([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) id)
Return a bookmark id from given string.
Parameters:
`id` - original string value
Returns:
a bookmark id
See Also:
[`UUIDGenerator.createId(String)`](../../helper/UUIDGenerator.html#createId(java.lang.String))
createRef
public [TextReference](../../TextReference.html) createRef([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId)
Return a bookmark for REF from given string.
Parameters:
`refId` - the bookmark id. If null, digest of empty string will be used.
Returns:
a bookmark for REF
See Also:
[`UUIDGenerator.createId(String)`](../../helper/UUIDGenerator.html#createId(java.lang.String))
createRef
public [TextReference](../../TextReference.html) createRef([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) content)
Return a bookmark for REF from given string.
Parameters:
`refId` - the bookmark id. If null, digest of empty string will be used.
`content` - text content
Returns:
a bookmark for REF
See Also:
[`UUIDGenerator.createId(String)`](../../helper/UUIDGenerator.html#createId(java.lang.String))
openRef
public [TextReference](../../TextReference.html) openRef([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId)
Return a reference to REF.
Parameters:
`refId` - the bookmark id. If null, digest of empty string will be used.
Returns:
a reference to REF
openRef
public [TextReference](../../TextReference.html) openRef([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refId,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) refText)
eturn a reference to REF.
Parameters:
`refId` - the bookmark id. If null, digest of empty string will be used.
`content` - text content
Returns:
a reference to REF

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.tools</a></div>
<h1 class="title" title="Class BookmarkTool">Class BookmarkTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.magicreport.engine.tools.BookmarkTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">BookmarkTool</span>
<span class="extends-implements">extends <a href="../Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">Contains utilities functions for bookmark. Context name of this class is "bookmark". Public functions of this
 class are able to access via template by using <code>$bookmark</code></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 19, 2007</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.magicreport.engine.tools.BookmarkTool">Serialized Form</a></li>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">BookmarkTool</a>()</code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Bookmark.html" title="class in com.nomagic.magicreport">Bookmark</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bookmarkObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create bookmark.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Bookmark.html" title="class in com.nomagic.magicreport">Bookmark</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.Object)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bookmarkId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bookmarkObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create bookmark.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Bookmark.html" title="class in com.nomagic.magicreport">Bookmark</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#create(java.lang.String,java.lang.Object,java.lang.String)">create</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bookmarkId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bookmarkObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create bookmark with the specified element type.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRef(java.lang.String)">createRef</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a bookmark for REF from given string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createRef(java.lang.String,java.lang.String)">createRef</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a bookmark for REF from given string.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBookmarkId(java.lang.String)">getBookmarkId</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a bookmark id from given string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open(java.lang.Object)">open</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create hyperlink for bookmark.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#open(java.lang.String,java.lang.Object)">open</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bookmarkId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create hyperlink for bookmark.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openRef(java.lang.String)">openRef</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a reference to REF.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openRef(java.lang.String,java.lang.String)">openRef</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refText)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">eturn a reference to REF.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openURL(java.lang.String,java.lang.Object)">openURL</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create hyperlink for open an URL.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openURL(java.net.URI,java.lang.Object)">openURL</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create hyperlink for open an URL.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#openURL(java.net.URL,java.lang.Object)">openURL</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Function to create hyperlink for open an URL.</div>
</div>
</div>
</div>
</div>
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
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.tools.BookmarkTool.CONTEXT_NAME">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;()">
<h3>BookmarkTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BookmarkTool</span>()</div>
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
<section class="detail" id="openURL(java.lang.String,java.lang.Object)">
<h3>openURL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></span> <span class="element-name">openURL</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</span></div>
<div class="block">Function to create hyperlink for open an URL.
 
 <pre>
 &lt;code&gt;
 $bookmark.openURL("http://www.nomagicasia.com", "NoMagic Asia")
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - the url text. If null, empty string will be used.</dd>
<dd><code>content</code> - the text content. If null, empty string will be used.</dd>
<dt>Returns:</dt>
<dd>content with hyperlink in document format.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#open(java.lang.String,java.lang.Object)"><code>open(String, Object)</code></a></li>
<li><a href="#create(java.lang.Object)"><code>create(Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openURL(java.net.URL,java.lang.Object)">
<h3>openURL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></span> <span class="element-name">openURL</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URL.html" title="class or interface in java.net">URL</a> url,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</span></div>
<div class="block">Function to create hyperlink for open an URL.
 
 <pre>
 &lt;code&gt;
 $bookmark.openURL($url, "NoMagic Asia")
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - the URL instance. If null, empty string will be used.</dd>
<dd><code>content</code> - text content. If null, empty string will be used.</dd>
<dt>Returns:</dt>
<dd>content with hyperlink in RTF format.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#open(java.lang.String,java.lang.Object)"><code>open(String, Object)</code></a></li>
<li><a href="#create(java.lang.Object)"><code>create(Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openURL(java.net.URI,java.lang.Object)">
<h3>openURL</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></span> <span class="element-name">openURL</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/net/URI.html" title="class or interface in java.net">URI</a> uri,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</span></div>
<div class="block">Function to create hyperlink for open an URL.
 
 <pre>
 &lt;code&gt;
 $bookmark.openURL($uri, "NoMagic Asia")
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>uri</code> - the URI instance. If null, empty string will be used.</dd>
<dd><code>content</code> - text content. If null, empty string will be used.</dd>
<dt>Returns:</dt>
<dd>content with hyperlink in RTF format.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#open(java.lang.String,java.lang.Object)"><code>open(String, Object)</code></a></li>
<li><a href="#create(java.lang.Object)"><code>create(Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="open(java.lang.Object)">
<h3>open</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></span> <span class="element-name">open</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</span></div>
<div class="block">Function to create hyperlink for bookmark. The bookmark ID will be automatically generated from content.
 
 <pre>
 &lt;code&gt;
    #foreach ($uc in $UseCase)
       $bookmark.open($uc.name)
    #end
    #foreach ($uc in $UseCase)
       $bookmark.create($uc.name)
    #end
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>content</code> - text content. If null, ID will be a digest of "0" and name will be a hash code of object.</dd>
<dt>Returns:</dt>
<dd>content with hyperlink in RTF format.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#open(java.lang.String,java.lang.Object)"><code>open(String, Object)</code></a></li>
<li><a href="#create(java.lang.Object)"><code>create(Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="open(java.lang.String,java.lang.Object)">
<h3>open</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Link.html" title="class in com.nomagic.magicreport">Link</a></span> <span class="element-name">open</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bookmarkId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> content)</span></div>
<div class="block">Function to create hyperlink for bookmark. <code>bookmarkID</code> value must match with parameter
 <code>bookmarkID</code> that pass into <a href="#create(java.lang.String,java.lang.Object)"><code>create(String, Object)</code></a> function.
 
 <pre>
 &lt;code&gt;
    #foreach ($uc in $UseCase)
       $bookmark.open($uc.name)
    #end
    #foreach ($uc in $UseCase)
       $bookmark.create($uc.name)
    #end
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bookmarkId</code> - the bookmark id. If null, digest of empty string will be used.</dd>
<dd><code>content</code> - text content. If null, empty string will be used.</dd>
<dt>Returns:</dt>
<dd>content with hyperlink in RTF format.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#open(java.lang.Object)"><code>open(Object)</code></a></li>
<li><a href="#create(java.lang.String,java.lang.Object)"><code>create(String, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Bookmark.html" title="class in com.nomagic.magicreport">Bookmark</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bookmarkObject)</span></div>
<div class="block">Function to create bookmark. The bookmark ID will be automatically generated from bookmark object.
 
 <pre>
 &lt;code&gt;
    #foreach ($uc in $UseCase)
       $bookmark.open($uc.name)
    #end
    #foreach ($uc in $UseCase)
       $bookmark.create($uc.name)
    #end
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bookmarkObject</code> - the bookmark object or content. If null, ID will be a digest of "0" and name will be a
           hash code of object.</dd>
<dt>Returns:</dt>
<dd>content with bookmark in RTF format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.Object)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Bookmark.html" title="class in com.nomagic.magicreport">Bookmark</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bookmarkId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bookmarkObject)</span></div>
<div class="block">Function to create bookmark. The default element type for this function is "label".
 
 <pre>
 &lt;code&gt;
    #foreach ($uc in $UseCase)
       $bookmark.open($uc.ID, $uc.name)
    #end
    #foreach ($uc in $UseCase)
       $bookmark.create($uc.ID, $uc.name)
    #end
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bookmarkId</code> - the bookmark. If null, digest of empty string will be used.</dd>
<dd><code>bookmarkObject</code> - the bookmark object or content. If null, empty string will be used.</dd>
<dt>Returns:</dt>
<dd>content with bookmark in RTF format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="create(java.lang.String,java.lang.Object,java.lang.String)">
<h3>create</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../Bookmark.html" title="class in com.nomagic.magicreport">Bookmark</a></span> <span class="element-name">create</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bookmarkId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bookmarkObject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> elementType)</span></div>
<div class="block">Function to create bookmark with the specified element type.
 
 <pre>
 &lt;code&gt;
    #foreach ($uc in $UseCase)
       $bookmark.open($uc.ID, $uc.name)
    #end
    #foreach ($uc in $UseCase)
       $bookmark.create($uc.ID, $uc.name, "label")
    #end
 &lt;/code&gt;
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bookmarkId</code> - the bookmark id. If null, digest of empty string will be used.</dd>
<dd><code>bookmarkObject</code> - the bookmark object or content. If null, empty string will be used.</dd>
<dd><code>elementType</code> - name of element type e.g. html tag.</dd>
<dt>Returns:</dt>
<dd>content with bookmark in format.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBookmarkId(java.lang.String)">
<h3>getBookmarkId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getBookmarkId</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Return a bookmark id from given string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>id</code> - original string value</dd>
<dt>Returns:</dt>
<dd>a bookmark id</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../helper/UUIDGenerator.html#createId(java.lang.String)"><code>UUIDGenerator.createId(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRef(java.lang.String)">
<h3>createRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></span> <span class="element-name">createRef</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId)</span></div>
<div class="block">Return a bookmark for REF from given string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>refId</code> - the bookmark id. If null, digest of empty string will be used.</dd>
<dt>Returns:</dt>
<dd>a bookmark for REF</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../helper/UUIDGenerator.html#createId(java.lang.String)"><code>UUIDGenerator.createId(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createRef(java.lang.String,java.lang.String)">
<h3>createRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></span> <span class="element-name">createRef</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content)</span></div>
<div class="block">Return a bookmark for REF from given string.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>refId</code> - the bookmark id. If null, digest of empty string will be used.</dd>
<dd><code>content</code> - text content</dd>
<dt>Returns:</dt>
<dd>a bookmark for REF</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../helper/UUIDGenerator.html#createId(java.lang.String)"><code>UUIDGenerator.createId(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openRef(java.lang.String)">
<h3>openRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></span> <span class="element-name">openRef</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId)</span></div>
<div class="block">Return a reference to REF.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>refId</code> - the bookmark id. If null, digest of empty string will be used.</dd>
<dt>Returns:</dt>
<dd>a reference to REF</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="openRef(java.lang.String,java.lang.String)">
<h3>openRef</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../TextReference.html" title="class in com.nomagic.magicreport">TextReference</a></span> <span class="element-name">openRef</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refId,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> refText)</span></div>
<div class="block">eturn a reference to REF.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>refId</code> - the bookmark id. If null, digest of empty string will be used.</dd>
<dd><code>content</code> - text content</dd>
<dt>Returns:</dt>
<dd>a reference to REF</dd>
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
