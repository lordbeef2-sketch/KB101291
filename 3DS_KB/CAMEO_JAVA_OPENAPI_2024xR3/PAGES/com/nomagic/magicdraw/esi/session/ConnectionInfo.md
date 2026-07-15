# JAVA OPENAPI: ConnectionInfo (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/esi/session/ConnectionInfo.html
- source_path: `com/nomagic/magicdraw/esi/session/ConnectionInfo.html`
- source_sha256: `db1df13e2add99f9363b83c66f793ef746f6a255b0183df4ef3c7d4f63d7935f`
- captured_utc: `2026-07-14T16:55:20.832069+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.esi.session](package-summary.html)

## Class ConnectionInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.esi.session.ConnectionInfo

@OpenApipublic classConnectionInfo
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Information where to connect when going online.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ConnectionInfo](#%3Cinit%3E(java.lang.String,java.lang.String,boolean,java.util.UUID))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hostPort,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName,
 boolean useSSL,
 [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) clusterID)`
Creates and initializes a new `ConnectionInfo` from the specified parameters.
`[ConnectionInfo](#%3Cinit%3E(java.lang.String,java.lang.String,java.security.KeyStore,java.util.UUID))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hostPort,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName,
 [KeyStore](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html) keyStore,
 [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) clusterID)`
Creates and initializes a new `ConnectionInfo` from the specified parameters.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`boolean`
`[equals](#equals(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)`

`[UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html)`
`[getClusterID](#getClusterID())()`
Returns clusterID of the connection info.
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getConnectionRepresentation](#getConnectionRepresentation())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getHostPort](#getHostPort())()`

`[KeyStore](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html)`
`[getKeystore](#getKeystore())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getLoginName](#getLoginName())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUserName](#getUserName())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getUserRepresentation](#getUserRepresentation())()`

`int`
`[hashCode](#hashCode())()`

`boolean`
`[isCompatible](#isCompatible(com.nomagic.magicdraw.esi.session.ConnectionInfo))([ConnectionInfo](ConnectionInfo.html) other)`
Checks whether the specified connection info is compatible with the current connection info.
`boolean`
`[isUseSecureConnection](#isUseSecureConnection())()`

`void`
`[setClusterID](#setClusterID(java.util.UUID))([UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) clusterID)`
Sets a new clusterID.
`void`
`[setUserName](#setUserName(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName)`
Setter for user name
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ConnectionInfo
public ConnectionInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hostPort,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName,
 @CheckForNull
 [KeyStore](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html) keyStore,
 @CheckForNull
 [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) clusterID)
Creates and initializes a new `ConnectionInfo` from the specified parameters.
Parameters:
`hostPort` - host and port.
`userName` - user name.
`keyStore` - SSL configuration.
`clusterID` - cluster ID.
ConnectionInfo
public ConnectionInfo([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) hostPort,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName,
 boolean useSSL,
 @CheckForNull
 [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) clusterID)
Creates and initializes a new `ConnectionInfo` from the specified parameters.
Parameters:
`hostPort` - host and port.
`userName` - user name.
`useSSL` - specifies if this connection info uses SSL.
`clusterID` - cluster ID.
 ============ METHOD DETAIL ========== 
Method Details
isUseSecureConnection
public boolean isUseSecureConnection()
Returns:
`true` when secure connection must be used
getHostPort
@OpenApipublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getHostPort()
Returns:
host and port
getConnectionRepresentation
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getConnectionRepresentation()
Returns:
connection representation
getUserName
@OpenApi
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUserName()
Returns:
user name
getLoginName
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getLoginName()
Returns:
user login name
setUserName
public void setUserName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) userName)
Setter for user name
Parameters:
`userName` - user name
getUserRepresentation
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getUserRepresentation()
Returns:
user representation
getClusterID
@OpenApi
@CheckForNullpublic [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) getClusterID()
Returns clusterID of the connection info.
Returns:
clusterID.
setClusterID
public void setClusterID(@CheckForNull
 [UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html) clusterID)
Sets a new clusterID.
Parameters:
`clusterID` - new cluster ID.
getKeystore
@CheckForNullpublic [KeyStore](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html) getKeystore()
Returns:
key store when secure connection is used, otherwise - `null`
isCompatible
public boolean isCompatible([ConnectionInfo](ConnectionInfo.html) other)
Checks whether the specified connection info is compatible with the current connection info.
 Compatible means that the connection info is from the same cluster and with the same user.
Parameters:
`other` - another connection info.
Returns:
true if compatible.
equals
public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) o)
Overrides:
`[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
hashCode
public int hashCode()
Overrides:
`[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode())` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.esi.session</a></div>
<h1 class="title" title="Class ConnectionInfo">Class ConnectionInfo</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.esi.session.ConnectionInfo</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ConnectionInfo</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Information where to connect when going online.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,boolean,java.util.UUID)">ConnectionInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> hostPort,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName,
 boolean useSSL,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> clusterID)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates and initializes a new <code>ConnectionInfo</code> from the specified parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,java.lang.String,java.security.KeyStore,java.util.UUID)">ConnectionInfo</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> hostPort,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html" title="class or interface in java.security">KeyStore</a> keyStore,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> clusterID)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates and initializes a new <code>ConnectionInfo</code> from the specified parameters.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getClusterID()">getClusterID</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns clusterID of the connection info.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConnectionRepresentation()">getConnectionRepresentation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getHostPort()">getHostPort</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html" title="class or interface in java.security">KeyStore</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getKeystore()">getKeystore</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLoginName()">getLoginName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserName()">getUserName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getUserRepresentation()">getUserRepresentation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isCompatible(com.nomagic.magicdraw.esi.session.ConnectionInfo)">isCompatible</a><wbr/>(<a href="ConnectionInfo.html" title="class in com.nomagic.magicdraw.esi.session">ConnectionInfo</a> other)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks whether the specified connection info is compatible with the current connection info.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseSecureConnection()">isUseSecureConnection</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setClusterID(java.util.UUID)">setClusterID</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> clusterID)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a new clusterID.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setUserName(java.lang.String)">setUserName</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Setter for user name</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,java.security.KeyStore,java.util.UUID)">
<h3>ConnectionInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConnectionInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> hostPort,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html" title="class or interface in java.security">KeyStore</a> keyStore,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> clusterID)</span></div>
<div class="block">Creates and initializes a new <code>ConnectionInfo</code> from the specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hostPort</code> - host and port.</dd>
<dd><code>userName</code> - user name.</dd>
<dd><code>keyStore</code> - SSL configuration.</dd>
<dd><code>clusterID</code> - cluster ID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.lang.String,boolean,java.util.UUID)">
<h3>ConnectionInfo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ConnectionInfo</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> hostPort,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName,
 boolean useSSL,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> clusterID)</span></div>
<div class="block">Creates and initializes a new <code>ConnectionInfo</code> from the specified parameters.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hostPort</code> - host and port.</dd>
<dd><code>userName</code> - user name.</dd>
<dd><code>useSSL</code> - specifies if this connection info uses SSL.</dd>
<dd><code>clusterID</code> - cluster ID.</dd>
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
<section class="detail" id="isUseSecureConnection()">
<h3>isUseSecureConnection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUseSecureConnection</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>true</code> when secure connection must be used</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHostPort()">
<h3>getHostPort</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHostPort</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>host and port</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConnectionRepresentation()">
<h3>getConnectionRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getConnectionRepresentation</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>connection representation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserName()">
<h3>getUserName</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUserName</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLoginName()">
<h3>getLoginName</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLoginName</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user login name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setUserName(java.lang.String)">
<h3>setUserName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setUserName</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> userName)</span></div>
<div class="block">Setter for user name</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>userName</code> - user name</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getUserRepresentation()">
<h3>getUserRepresentation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getUserRepresentation</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>user representation</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getClusterID()">
<h3>getClusterID</h3>
<div class="member-signature"><span class="annotations">@OpenApi
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a></span> <span class="element-name">getClusterID</span>()</div>
<div class="block">Returns clusterID of the connection info.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>clusterID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setClusterID(java.util.UUID)">
<h3>setClusterID</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setClusterID</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html" title="class or interface in java.util">UUID</a> clusterID)</span></div>
<div class="block">Sets a new clusterID.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clusterID</code> - new cluster ID.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getKeystore()">
<h3>getKeystore</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyStore.html" title="class or interface in java.security">KeyStore</a></span> <span class="element-name">getKeystore</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>key store when secure connection is used, otherwise - <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCompatible(com.nomagic.magicdraw.esi.session.ConnectionInfo)">
<h3>isCompatible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCompatible</span><wbr/><span class="parameters">(<a href="ConnectionInfo.html" title="class in com.nomagic.magicdraw.esi.session">ConnectionInfo</a> other)</span></div>
<div class="block">Checks whether the specified connection info is compatible with the current connection info.
 Compatible means that the connection info is from the same cluster and with the same user.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>other</code> - another connection info.</dd>
<dt>Returns:</dt>
<dd>true if compatible.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
