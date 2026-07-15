# JAVA OPENAPI: ChangeOwnerInfo (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/diff/ChangeOwnerInfo.html
- source_path: `com/nomagic/magicdraw/diff/ChangeOwnerInfo.html`
- source_sha256: `522796fe65b64ca1ab96601025bf0a5281fbd21d9701dea41954cce548f54638`
- captured_utc: `2026-07-14T16:45:32.556436+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface ChangeOwnerInfo

All Superinterfaces:
`[ModificationInfo](ModificationInfo.html)`, `[ReferenceModificationInfo](ReferenceModificationInfo.html)`, `[ValueModificationInfo](ValueModificationInfo.html)`

@OpenApiAllpublic interfaceChangeOwnerInfoextends [ReferenceModificationInfo](ReferenceModificationInfo.html)

Special kind of reference modification is owner change. Such change is detected when composite
 association is changed (element is moved).

========== METHOD SUMMARY =========== 
Method Summary
Methods inherited from interface com.nomagic.magicdraw.diff.[ReferenceModificationInfo](ReferenceModificationInfo.html)
`[getValue](ReferenceModificationInfo.html#getValue()), [getValueSpecificationID](ReferenceModificationInfo.html#getValueSpecificationID()), [wasChangeFromDefaultValue](ReferenceModificationInfo.html#wasChangeFromDefaultValue())`
Methods inherited from interface com.nomagic.magicdraw.diff.[ValueModificationInfo](ValueModificationInfo.html)
`[getModificationKind](ValueModificationInfo.html#getModificationKind())`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface ChangeOwnerInfo">Interface ChangeOwnerInfo</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ModificationInfo</a></code>, <code><a href="ReferenceModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ReferenceModificationInfo</a></code>, <code><a href="ValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ValueModificationInfo</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ChangeOwnerInfo</span><span class="extends-implements">
extends <a href="ReferenceModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ReferenceModificationInfo</a></span></div>
<div class="block">Special kind of reference modification is owner change. Such change is detected when composite
 association is changed (element is moved).</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.ReferenceModificationInfo">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="ReferenceModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ReferenceModificationInfo</a></h3>
<code><a href="ReferenceModificationInfo.html#getValue()">getValue</a>, <a href="ReferenceModificationInfo.html#getValueSpecificationID()">getValueSpecificationID</a>, <a href="ReferenceModificationInfo.html#wasChangeFromDefaultValue()">wasChangeFromDefaultValue</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.diff.ValueModificationInfo">Methods inherited from interface com.nomagic.magicdraw.diff.<a href="ValueModificationInfo.html" title="interface in com.nomagic.magicdraw.diff">ValueModificationInfo</a></h3>
<code><a href="ValueModificationInfo.html#getModificationKind()">getModificationKind</a></code></div>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
