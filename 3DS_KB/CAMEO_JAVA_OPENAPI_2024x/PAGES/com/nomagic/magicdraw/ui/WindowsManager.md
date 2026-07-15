# JAVA OPENAPI: WindowsManager (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/WindowsManager.html
- source_path: `com/nomagic/magicdraw/ui/WindowsManager.html`
- source_sha256: `92406ebc39fefbfe6783c4bc908b8c1b621b6f247f2a188e45cffae2528d16b0`
- captured_utc: `2026-07-14T16:52:03.186760+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Interface WindowsManager

All Known Subinterfaces:
`[ProjectWindowsManager](ProjectWindowsManager.html)`

@OpenApiAllpublic interfaceWindowsManager

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[SIDE_EAST](#SIDE_EAST)`

`static final int`
`[SIDE_NORTH](#SIDE_NORTH)`

`static final int`
`[SIDE_SOUTH](#SIDE_SOUTH)`

`static final int`
`[SIDE_WEST](#SIDE_WEST)`

`static final int`
`[STATE_AUTOHIDE](#STATE_AUTOHIDE)`

`static final int`
`[STATE_DOCKED](#STATE_DOCKED)`

`static final int`
`[STATE_FLOATING](#STATE_FLOATING)`

`static final int`
`[STATE_HIDDEN](#STATE_HIDDEN)`

============ FIELD DETAIL =========== 
Field Details
SIDE_EAST
static final int SIDE_EAST
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_EAST)
SIDE_NORTH
static final int SIDE_NORTH
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_NORTH)
SIDE_SOUTH
static final int SIDE_SOUTH
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_SOUTH)
SIDE_WEST
static final int SIDE_WEST
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_WEST)
STATE_DOCKED
static final int STATE_DOCKED
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_DOCKED)
STATE_FLOATING
static final int STATE_FLOATING
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_FLOATING)
STATE_AUTOHIDE
static final int STATE_AUTOHIDE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_AUTOHIDE)
STATE_HIDDEN
static final int STATE_HIDDEN
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_HIDDEN)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Interface WindowsManager">Interface WindowsManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ProjectWindowsManager.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowsManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">WindowsManager</span></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SIDE_EAST">SIDE_EAST</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SIDE_NORTH">SIDE_NORTH</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SIDE_SOUTH">SIDE_SOUTH</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SIDE_WEST">SIDE_WEST</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STATE_AUTOHIDE">STATE_AUTOHIDE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STATE_DOCKED">STATE_DOCKED</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#STATE_FLOATING">STATE_FLOATING</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STATE_HIDDEN">STATE_HIDDEN</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
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
<section class="detail" id="SIDE_EAST">
<h3>SIDE_EAST</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SIDE_EAST</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_EAST">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SIDE_NORTH">
<h3>SIDE_NORTH</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SIDE_NORTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_NORTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SIDE_SOUTH">
<h3>SIDE_SOUTH</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SIDE_SOUTH</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_SOUTH">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SIDE_WEST">
<h3>SIDE_WEST</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">SIDE_WEST</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.SIDE_WEST">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_DOCKED">
<h3>STATE_DOCKED</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STATE_DOCKED</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_DOCKED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_FLOATING">
<h3>STATE_FLOATING</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STATE_FLOATING</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_FLOATING">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_AUTOHIDE">
<h3>STATE_AUTOHIDE</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STATE_AUTOHIDE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_AUTOHIDE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="STATE_HIDDEN">
<h3>STATE_HIDDEN</h3>
<div class="member-signature"><span class="modifiers">static final</span> <span class="return-type">int</span> <span class="element-name">STATE_HIDDEN</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.magicdraw.ui.WindowsManager.STATE_HIDDEN">Constant Field Values</a></li>
</ul>
</dd>
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
