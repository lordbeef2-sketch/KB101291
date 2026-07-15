# JAVA OPENAPI: Difference (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/diff/Difference.html
- source_path: `com/nomagic/magicdraw/diff/Difference.html`
- source_sha256: `004aad73acff4ba3472624a3a447e0211e8d210d45292b67d14e585eadffcbf5`
- captured_utc: `2026-07-14T16:51:17.501155+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.diff](package-summary.html)

## Interface Difference

All Known Subinterfaces:
`[DiagramDifference](DiagramDifference.html)`, `[DomainSpecificCustomizationDifference](DomainSpecificCustomizationDifference.html)`, `[ElementAddition](ElementAddition.html)`, `[ElementDeletion](ElementDeletion.html)`, `[ElementDifference](ElementDifference.html)`, `[ElementModification](ElementModification.html)`, `[MacroDifference](macro/MacroDifference.html)`, `[MDExtensionDifference](mdextensions/MDExtensionDifference.html)`, `[MDExtensionExistenceDifference](mdextensions/MDExtensionExistenceDifference.html)`, `[MDExtensionModificationDifference](mdextensions/MDExtensionModificationDifference.html)`, `[Modification](Modification.html)`, `[ModuleUsageDifference](ModuleUsageDifference.html)`, `[MultiplePersistentPropertyDifference](symbols/MultiplePersistentPropertyDifference.html)<T>`, `[PersistentPropertyOrderDifference](symbols/PersistentPropertyOrderDifference.html)<T>`, `[ProjectOptionsDifference](ProjectOptionsDifference.html)`, `[ShareDifference](ShareDifference.html)`, `[StereotypeModification](StereotypeModification.html)`, `[SymbolAddition](symbols/SymbolAddition.html)`, `[SymbolDeletion](symbols/SymbolDeletion.html)`, `[SymbolDifference](symbols/SymbolDifference.html)`, `[SymbolPersistentPropertyDifference](symbols/SymbolPersistentPropertyDifference.html)<T>`, `[TagValueModification](TagValueModification.html)`

@OpenApipublic interfaceDifference

Difference between two entities which can be compared. Original entity is named ancestor, changed
 entity is contributor. Difference must hold information which is enough to restore change when
 applying to ancestor entity.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.diff</a></div>
<h1 class="title" title="Interface Difference">Interface Difference</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="DiagramDifference.html" title="interface in com.nomagic.magicdraw.diff">DiagramDifference</a></code>, <code><a href="DomainSpecificCustomizationDifference.html" title="interface in com.nomagic.magicdraw.diff">DomainSpecificCustomizationDifference</a></code>, <code><a href="ElementAddition.html" title="interface in com.nomagic.magicdraw.diff">ElementAddition</a></code>, <code><a href="ElementDeletion.html" title="interface in com.nomagic.magicdraw.diff">ElementDeletion</a></code>, <code><a href="ElementDifference.html" title="interface in com.nomagic.magicdraw.diff">ElementDifference</a></code>, <code><a href="ElementModification.html" title="interface in com.nomagic.magicdraw.diff">ElementModification</a></code>, <code><a href="macro/MacroDifference.html" title="interface in com.nomagic.magicdraw.diff.macro">MacroDifference</a></code>, <code><a href="mdextensions/MDExtensionDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionDifference</a></code>, <code><a href="mdextensions/MDExtensionExistenceDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionExistenceDifference</a></code>, <code><a href="mdextensions/MDExtensionModificationDifference.html" title="interface in com.nomagic.magicdraw.diff.mdextensions">MDExtensionModificationDifference</a></code>, <code><a href="Modification.html" title="interface in com.nomagic.magicdraw.diff">Modification</a></code>, <code><a href="ModuleUsageDifference.html" title="interface in com.nomagic.magicdraw.diff">ModuleUsageDifference</a></code>, <code><a href="symbols/MultiplePersistentPropertyDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">MultiplePersistentPropertyDifference</a>&lt;T&gt;</code>, <code><a href="symbols/PersistentPropertyOrderDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">PersistentPropertyOrderDifference</a>&lt;T&gt;</code>, <code><a href="ProjectOptionsDifference.html" title="interface in com.nomagic.magicdraw.diff">ProjectOptionsDifference</a></code>, <code><a href="ShareDifference.html" title="interface in com.nomagic.magicdraw.diff">ShareDifference</a></code>, <code><a href="StereotypeModification.html" title="interface in com.nomagic.magicdraw.diff">StereotypeModification</a></code>, <code><a href="symbols/SymbolAddition.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolAddition</a></code>, <code><a href="symbols/SymbolDeletion.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDeletion</a></code>, <code><a href="symbols/SymbolDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolDifference</a></code>, <code><a href="symbols/SymbolPersistentPropertyDifference.html" title="interface in com.nomagic.magicdraw.diff.symbols">SymbolPersistentPropertyDifference</a>&lt;T&gt;</code>, <code><a href="TagValueModification.html" title="interface in com.nomagic.magicdraw.diff">TagValueModification</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">Difference</span></div>
<div class="block">Difference between two entities which can be compared. Original entity is named ancestor, changed
 entity is contributor. Difference must hold information which is enough to restore change when
 applying to ancestor entity.</div>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
