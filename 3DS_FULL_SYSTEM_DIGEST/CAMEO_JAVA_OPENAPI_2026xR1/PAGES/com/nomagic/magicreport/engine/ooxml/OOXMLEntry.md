# JAVA OPENAPI: OOXMLEntry (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/ooxml/OOXMLEntry.html
- source_path: `com/nomagic/magicreport/engine/ooxml/OOXMLEntry.html`
- source_sha256: `4b4cc43146709287da3e2b9c039bfa2b0943d1f10d156d226c07bb878771a005`
- captured_utc: `2026-07-14T16:46:12.239963+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.ooxml](package-summary.html)

## Class OOXMLEntry

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.zip.ZipEntry](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html)
com.nomagic.magicreport.engine.ooxml.OOXMLEntry

All Implemented Interfaces:
`[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classOOXMLEntry
extends [ZipEntry](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html)

This class is used to represent a OOXML file entry.

Since:
May 28, 2008

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[CENATT](#CENATT)`

`static final int`
`[CENATX](#CENATX)`

`static final int`
`[CENCOM](#CENCOM)`

`static final int`
`[CENCRC](#CENCRC)`

`static final int`
`[CENDSK](#CENDSK)`

`static final int`
`[CENEXT](#CENEXT)`

`static final int`
`[CENFLG](#CENFLG)`

`static final int`
`[CENHDR](#CENHDR)`

`static final int`
`[CENHOW](#CENHOW)`

`static final int`
`[CENLEN](#CENLEN)`

`static final int`
`[CENNAM](#CENNAM)`

`static final int`
`[CENOFF](#CENOFF)`

`static final long`
`[CENSIG](#CENSIG)`

`static final int`
`[CENSIZ](#CENSIZ)`

`static final int`
`[CENTIM](#CENTIM)`

`static final int`
`[CENVEM](#CENVEM)`

`static final int`
`[CENVER](#CENVER)`

`static final int`
`[ENDCOM](#ENDCOM)`

`static final int`
`[ENDHDR](#ENDHDR)`

`static final int`
`[ENDOFF](#ENDOFF)`

`static final long`
`[ENDSIG](#ENDSIG)`

`static final int`
`[ENDSIZ](#ENDSIZ)`

`static final int`
`[ENDSUB](#ENDSUB)`

`static final int`
`[ENDTOT](#ENDTOT)`

`static final int`
`[EXTCRC](#EXTCRC)`

`static final int`
`[EXTHDR](#EXTHDR)`

`static final int`
`[EXTLEN](#EXTLEN)`

`static final long`
`[EXTSIG](#EXTSIG)`

`static final int`
`[EXTSIZ](#EXTSIZ)`

`static final int`
`[LOCCRC](#LOCCRC)`

`static final int`
`[LOCEXT](#LOCEXT)`

`static final int`
`[LOCFLG](#LOCFLG)`

`static final int`
`[LOCHDR](#LOCHDR)`

`static final int`
`[LOCHOW](#LOCHOW)`

`static final int`
`[LOCLEN](#LOCLEN)`

`static final int`
`[LOCNAM](#LOCNAM)`

`static final long`
`[LOCSIG](#LOCSIG)`

`static final int`
`[LOCSIZ](#LOCSIZ)`

`static final int`
`[LOCTIM](#LOCTIM)`

`static final int`
`[LOCVER](#LOCVER)`
Fields inherited from class java.util.zip.[ZipEntry](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html)
`[DEFLATED](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#DEFLATED), [STORED](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#STORED)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[OOXMLEntry](#%3Cinit%3E(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)`
Creates a new `OOXMLEntry` for the specified OOXML file entry name.
`[OOXMLEntry](#%3Cinit%3E(java.util.zip.ZipEntry))([ZipEntry](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html) ze)`
Creates a new `OOXMLEntry` with fields taken from the specified `ZipEntry` object.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)`
Determines whether another object is equal to this OOXMLEntry.
`int`
`[hashCode](#hashCode())()`
Returns the hash code value for this entry.
Methods inherited from class java.util.zip.[ZipEntry](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#clone()), [getComment](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getComment()), [getCompressedSize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getCompressedSize()), [getCrc](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getCrc()), [getCreationTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getCreationTime()), [getExtra](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getExtra()), [getLastAccessTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getLastAccessTime()), [getLastModifiedTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getLastModifiedTime()), [getMethod](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getMethod()), [getName](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getName()), [getSize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getSize()), [getTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getTime()), [getTimeLocal](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getTimeLocal()), [isDirectory](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#isDirectory()), [setComment](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setComment(java.lang.String)), [setCompressedSize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setCompressedSize(long)), [setCrc](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setCrc(long)), [setCreationTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setCreationTime(java.nio.file.attribute.FileTime)), [setExtra](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setExtra(byte%5B%5D)), [setLastAccessTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setLastAccessTime(java.nio.file.attribute.FileTime)), [setLastModifiedTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setLastModifiedTime(java.nio.file.attribute.FileTime)), [setMethod](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setMethod(int)), [setSize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setSize(long)), [setTime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setTime(long)), [setTimeLocal](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setTimeLocal(java.time.LocalDateTime)), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#toString())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
LOCSIG
static final long LOCSIG
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCSIG)
EXTSIG
static final long EXTSIG
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTSIG)
CENSIG
static final long CENSIG
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENSIG)
ENDSIG
static final long ENDSIG
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDSIG)
LOCHDR
static final int LOCHDR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCHDR)
EXTHDR
static final int EXTHDR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTHDR)
CENHDR
static final int CENHDR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENHDR)
ENDHDR
static final int ENDHDR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDHDR)
LOCVER
static final int LOCVER
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCVER)
LOCFLG
static final int LOCFLG
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCFLG)
LOCHOW
static final int LOCHOW
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCHOW)
LOCTIM
static final int LOCTIM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCTIM)
LOCCRC
static final int LOCCRC
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCCRC)
LOCSIZ
static final int LOCSIZ
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCSIZ)
LOCLEN
static final int LOCLEN
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCLEN)
LOCNAM
static final int LOCNAM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCNAM)
LOCEXT
static final int LOCEXT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCEXT)
EXTCRC
static final int EXTCRC
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTCRC)
EXTSIZ
static final int EXTSIZ
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTSIZ)
EXTLEN
static final int EXTLEN
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTLEN)
CENVEM
static final int CENVEM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENVEM)
CENVER
static final int CENVER
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENVER)
CENFLG
static final int CENFLG
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENFLG)
CENHOW
static final int CENHOW
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENHOW)
CENTIM
static final int CENTIM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENTIM)
CENCRC
static final int CENCRC
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENCRC)
CENSIZ
static final int CENSIZ
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENSIZ)
CENLEN
static final int CENLEN
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENLEN)
CENNAM
static final int CENNAM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENNAM)
CENEXT
static final int CENEXT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENEXT)
CENCOM
static final int CENCOM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENCOM)
CENDSK
static final int CENDSK
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENDSK)
CENATT
static final int CENATT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENATT)
CENATX
static final int CENATX
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENATX)
CENOFF
static final int CENOFF
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENOFF)
ENDSUB
static final int ENDSUB
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDSUB)
ENDTOT
static final int ENDTOT
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDTOT)
ENDSIZ
static final int ENDSIZ
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDSIZ)
ENDOFF
static final int ENDOFF
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDOFF)
ENDCOM
static final int ENDCOM
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDCOM)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
OOXMLEntry
public OOXMLEntry([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name)
Creates a new `OOXMLEntry` for the specified OOXML file entry name.
Parameters:
`name` - the JAR file entry name
Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if the entry name is `null`
`[IllegalArgumentException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html)` - if the entry name is longer than 0xFFFF bytes.
OOXMLEntry
public OOXMLEntry([ZipEntry](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html) ze)
Creates a new `OOXMLEntry` with fields taken from the specified `ZipEntry` object.
Parameters:
`ze` - the `ZipEntry` object to create the `OOXMLEntry` from
 ============ METHOD DETAIL ========== 
Method Details
hashCode
public int hashCode()
Returns the hash code value for this entry.
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#hashCode())` in class `[ZipEntry](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html)`
Returns:
a hash code value for this object.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) obj)
Determines whether another object is equal to this OOXMLEntry. The result is true if and only if the
 argument is not null and is a OOXMLEntry object that has the same name value as this object.
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
Parameters:
`obj` - the object to test for equality with this OOXMLEntry
Returns:
if the objects are the same; false otherwise.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.ooxml</a></div>
<h1 class="title" title="Class OOXMLEntry">Class OOXMLEntry</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html" title="class or interface in java.util.zip">java.util.zip.ZipEntry</a>
<div class="inheritance">com.nomagic.magicreport.engine.ooxml.OOXMLEntry</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">OOXMLEntry</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html" title="class or interface in java.util.zip">ZipEntry</a></span></div>
<div class="block">This class is used to represent a OOXML file entry.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>May 28, 2008</dd>
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
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENATT">CENATT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENATX">CENATX</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENCOM">CENCOM</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENCRC">CENCRC</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENDSK">CENDSK</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENEXT">CENEXT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENFLG">CENFLG</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENHDR">CENHDR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENHOW">CENHOW</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENLEN">CENLEN</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENNAM">CENNAM</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENOFF">CENOFF</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENSIG">CENSIG</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENSIZ">CENSIZ</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENTIM">CENTIM</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CENVEM">CENVEM</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CENVER">CENVER</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENDCOM">ENDCOM</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENDHDR">ENDHDR</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENDOFF">ENDOFF</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENDSIG">ENDSIG</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENDSIZ">ENDSIZ</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENDSUB">ENDSUB</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENDTOT">ENDTOT</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXTCRC">EXTCRC</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXTHDR">EXTHDR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXTLEN">EXTLEN</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#EXTSIG">EXTSIG</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXTSIZ">EXTSIZ</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCCRC">LOCCRC</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCEXT">LOCEXT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCFLG">LOCFLG</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCHDR">LOCHDR</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCHOW">LOCHOW</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCLEN">LOCLEN</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCNAM">LOCNAM</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCSIG">LOCSIG</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCSIZ">LOCSIZ</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#LOCTIM">LOCTIM</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOCVER">LOCVER</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-java.util.zip.ZipEntry">Fields inherited from class java.util.zip.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html" title="class or interface in java.util.zip">ZipEntry</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#DEFLATED" title="class or interface in java.util.zip">DEFLATED</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#STORED" title="class or interface in java.util.zip">STORED</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String)">OOXMLEntry</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new <code>OOXMLEntry</code> for the specified OOXML file entry name.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.zip.ZipEntry)">OOXMLEntry</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html" title="class or interface in java.util.zip">ZipEntry</a> ze)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new <code>OOXMLEntry</code> with fields taken from the specified <code>ZipEntry</code> object.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether another object is equal to this OOXMLEntry.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the hash code value for this entry.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.zip.ZipEntry">Methods inherited from class java.util.zip.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html" title="class or interface in java.util.zip">ZipEntry</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#clone()" title="class or interface in java.util.zip">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getComment()" title="class or interface in java.util.zip">getComment</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getCompressedSize()" title="class or interface in java.util.zip">getCompressedSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getCrc()" title="class or interface in java.util.zip">getCrc</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getCreationTime()" title="class or interface in java.util.zip">getCreationTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getExtra()" title="class or interface in java.util.zip">getExtra</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getLastAccessTime()" title="class or interface in java.util.zip">getLastAccessTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getLastModifiedTime()" title="class or interface in java.util.zip">getLastModifiedTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getMethod()" title="class or interface in java.util.zip">getMethod</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getName()" title="class or interface in java.util.zip">getName</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getSize()" title="class or interface in java.util.zip">getSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getTime()" title="class or interface in java.util.zip">getTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#getTimeLocal()" title="class or interface in java.util.zip">getTimeLocal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#isDirectory()" title="class or interface in java.util.zip">isDirectory</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setComment(java.lang.String)" title="class or interface in java.util.zip">setComment</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setCompressedSize(long)" title="class or interface in java.util.zip">setCompressedSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setCrc(long)" title="class or interface in java.util.zip">setCrc</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setCreationTime(java.nio.file.attribute.FileTime)" title="class or interface in java.util.zip">setCreationTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setExtra(byte%5B%5D)" title="class or interface in java.util.zip">setExtra</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setLastAccessTime(java.nio.file.attribute.FileTime)" title="class or interface in java.util.zip">setLastAccessTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setLastModifiedTime(java.nio.file.attribute.FileTime)" title="class or interface in java.util.zip">setLastModifiedTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setMethod(int)" title="class or interface in java.util.zip">setMethod</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setSize(long)" title="class or interface in java.util.zip">setSize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setTime(long)" title="class or interface in java.util.zip">setTime</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#setTimeLocal(java.time.LocalDateTime)" title="class or interface in java.util.zip">setTimeLocal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#toString()" title="class or interface in java.util.zip">toString</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="LOCSIG">
<h3>LOCSIG</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">long</span> <span class="element-name">LOCSIG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCSIG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTSIG">
<h3>EXTSIG</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">long</span> <span class="element-name">EXTSIG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTSIG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENSIG">
<h3>CENSIG</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">long</span> <span class="element-name">CENSIG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENSIG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDSIG">
<h3>ENDSIG</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">long</span> <span class="element-name">ENDSIG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDSIG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCHDR">
<h3>LOCHDR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCHDR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCHDR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTHDR">
<h3>EXTHDR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EXTHDR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTHDR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENHDR">
<h3>CENHDR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENHDR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENHDR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDHDR">
<h3>ENDHDR</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENDHDR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDHDR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCVER">
<h3>LOCVER</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCVER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCVER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCFLG">
<h3>LOCFLG</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCFLG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCFLG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCHOW">
<h3>LOCHOW</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCHOW</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCHOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCTIM">
<h3>LOCTIM</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCTIM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCTIM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCCRC">
<h3>LOCCRC</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCCRC</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCCRC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCSIZ">
<h3>LOCSIZ</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCSIZ</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCSIZ">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCLEN">
<h3>LOCLEN</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCLEN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCLEN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCNAM">
<h3>LOCNAM</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCNAM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCNAM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOCEXT">
<h3>LOCEXT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">LOCEXT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.LOCEXT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTCRC">
<h3>EXTCRC</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EXTCRC</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTCRC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTSIZ">
<h3>EXTSIZ</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EXTSIZ</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTSIZ">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTLEN">
<h3>EXTLEN</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">EXTLEN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.EXTLEN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENVEM">
<h3>CENVEM</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENVEM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENVEM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENVER">
<h3>CENVER</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENVER</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENVER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENFLG">
<h3>CENFLG</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENFLG</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENFLG">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENHOW">
<h3>CENHOW</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENHOW</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENHOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENTIM">
<h3>CENTIM</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENTIM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENTIM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENCRC">
<h3>CENCRC</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENCRC</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENCRC">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENSIZ">
<h3>CENSIZ</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENSIZ</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENSIZ">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENLEN">
<h3>CENLEN</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENLEN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENLEN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENNAM">
<h3>CENNAM</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENNAM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENNAM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENEXT">
<h3>CENEXT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENEXT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENEXT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENCOM">
<h3>CENCOM</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENCOM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENCOM">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENDSK">
<h3>CENDSK</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENDSK</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENDSK">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENATT">
<h3>CENATT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENATT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENATT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENATX">
<h3>CENATX</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENATX</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENATX">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CENOFF">
<h3>CENOFF</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">CENOFF</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.CENOFF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDSUB">
<h3>ENDSUB</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENDSUB</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDSUB">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDTOT">
<h3>ENDTOT</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENDTOT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDTOT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDSIZ">
<h3>ENDSIZ</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENDSIZ</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDSIZ">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDOFF">
<h3>ENDOFF</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENDOFF</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDOFF">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENDCOM">
<h3>ENDCOM</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">ENDCOM</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicreport.engine.ooxml.OOXMLEntry.ENDCOM">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>OOXMLEntry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLEntry</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Creates a new <code>OOXMLEntry</code> for the specified OOXML file entry name.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the JAR file entry name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the entry name is <code>null</code></dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the entry name is longer than 0xFFFF bytes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.zip.ZipEntry)">
<h3>OOXMLEntry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OOXMLEntry</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html" title="class or interface in java.util.zip">ZipEntry</a> ze)</span></div>
<div class="block">Creates a new <code>OOXMLEntry</code> with fields taken from the specified <code>ZipEntry</code> object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ze</code> - the <code>ZipEntry</code> object to create the <code>OOXMLEntry</code> from</dd>
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
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="block">Returns the hash code value for this entry.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html#hashCode()" title="class or interface in java.util.zip">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/ZipEntry.html" title="class or interface in java.util.zip">ZipEntry</a></code></dd>
<dt>Returns:</dt>
<dd>a hash code value for this object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="block">Determines whether another object is equal to this OOXMLEntry. The result is true if and only if the
 argument is not null and is a OOXMLEntry object that has the same name value as this object.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
<dt>Parameters:</dt>
<dd><code>obj</code> - the object to test for equality with this OOXMLEntry</dd>
<dt>Returns:</dt>
<dd>if the objects are the same; false otherwise.</dd>
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
