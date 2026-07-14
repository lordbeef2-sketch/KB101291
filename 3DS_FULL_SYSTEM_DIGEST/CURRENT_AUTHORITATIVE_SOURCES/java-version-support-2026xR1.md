# CURRENT AUTHORITATIVE SOURCE: Java version support for 2026x Refresh1

- source_url: https://docs.nomagic.com/IL/latest/java-version-support-for-2026x-refresh1-304005583.html
- source_bytes: 84659
- source_sha256: `1571bea36e3a26f04c30b210214732b096d45ece2b085a5bb1e67663ef406af7`
- captured_utc: `2026-07-14T16:49:08.115303+00:00`

## NORMALIZED CONTENT

Java version support for 2026x Refresh1
Changing JVM version
For information on how to change the JVM version, please see
How to change JVM version
In the following table, please find the recommendations for the appropriate Java version for 2026x Refresh1.
Product
Version
Recommended and included in installation files**
MagicDraw
Cameo Systems Modeler
Cameo Enterprise Architecture
Magic Software Architect
Magic Cyber Systems Engineer
Magic Systems of Systems Architect
2026x Refresh1
AdoptOpenJDK 21.0.10+7
(Eclipse Temurin) with HotSpot JVM for all OSs.
Teamwork Cloud
Magic Collaboration Studio
2026x Refresh1
AdoptOpenJDK 21.0.10+7
(Eclipse Temurin) with HotSpot JVM.
Cassandra 5.0.x requires
JDK 17.0
(either Oracle or Open JDK).
Cameo Collaborator for Teamwork Cloud
Web Application Platform
Resources
TWCloud Admin Console NG
2026x Refresh1
AdoptOpenJDK 21.0.10+7
(Eclipse Temurin) with HotSpot JVM.
*
OpenJDK
. Based on the testing results, we recommend using Eclipse Temurin™ by ADOPTIUM.
OpenJ9 should not be used; instead, the HotSpot distribution should be utilized. For more information, see "Help Me Choose" tips at
https://adoptopenjdk.net/
.
**Java is included only in installation files for Windows and macOS. Linux installation files do not have built-in Java.
*** You should choose Java native to the macOS architecture (ARM or x86) in use.
See the
(2026x Refresh1) JVM recommendations for versions up to 19.0 SP1
.
See
Zip exceptions thrown after Java version upgrade to 11.0.20+ or 17.0.8+
.
×

## EXACT MAIN HTML

````html
<main>
<span id="admin-menu-link" style="display: none; position: absolute; top:-5000px;"></span>
<div class="grid-container article full">
<div class="grid-x article__content" data-sticky-container="">
<div class="cell large-2 article__navigation show-for-large">
<div data-options="marginTop:8;" data-sticky="">
<div class="page-tree-collapser"></div>
</div>
<div data-btm-anchor="article-content:bottom" data-options="marginTop:8;" data-sticky="" data-top-anchor="article-content" id="js-desktop-pageTree">
<ul aria-hidden="false" class="vertical menu js-loading accordion-menu renderPageTree scroll-y" data-accordion-menu="" data-current="/IL/latest/java-version-support-for-2026x-refresh1-304005583.html" data-root="/IL/latest/installation-licensing-and-system-requirements-documentation-304005228.html" data-submenu-toggle="true" data-viewport-id="AC1032020199382236A955E14861A48E">
<li class="js-loading js-loading__stacked js-loading__stacked--listItem"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem js-loading__stacked--listItem--short"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem js-loading__stacked--listItem--short"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem"></li>
</ul>
</div>
</div>
<div class="cell medium-auto grid-container full js-loading" id="article-content">
<article class="grid-x" role="article">
<header class="cell grid-x">
<nav aria-label="You are here:" class="cell medium-11" role="navigation">
<ul class="breadcrumbs js-loading js-loading__stacked js-loading__stacked--breadcrumb">
<li class="js-hide-until-loaded"><a href="/IL/latest/installation-licensing-and-system-requirements-documentation-304005228.html" rel="prev" target="_self">Installation and Licensing</a></li>
<li class="js-hide-until-loaded"><a class="js-breadcrumbs-truncate" href="/IL/latest/java-version-support-304005280.html" rel="prev" target="_self">Java version support</a></li>
<li class="breadcrumbs--active js-hide-until-loaded"><span class="show-for-sr">Current: </span>Java version support for 2026x Refresh1</li>
</ul>
</nav>
<h1 class="cell article__heading js-loading js-loading__stacked js-loading__stacked--heading" role="heading"><span class="js-hide-until-loaded">Java version support for 2026x Refresh1</span></h1>
</header>
<section class="cell page" id="content" role="main">
<div class="cell wiki-content js-tocBot-content js-hide-until-loaded hc-content-width--wide" id="main-content">
<div class="sp-grid-section conf-macro output-block" data-hasbody="true" data-macro-name="sp-pagelayout">
<div class="sp-grid-cell sp-grid-100">
<div class="panel-macro panel-macros--info conf-macro output-block" data-hasbody="true" data-macro-name="sp-macrooverride-richtextbody-block">
<div class="grid-x">
<div class="cell shrink panel-macros--info__icon">
<img src="/IL/_/AC103202019874DAB34395A7381E7D30/1779799496942/images/common/info-macro-icon.svg"/>
</div>
<div class="cell auto align-self-middle panel-macros--info__content">
<p class="panel-macros--info__content--heading">Changing JVM version</p>
<p>For information on how to change the JVM version, please see <a class="conf-macro output-inline" data-hasbody="true" data-macro-name="sp-plaintextbody-link" href="/IL/latest/how-to-change-jvm-version-304005462.html">How to change JVM version</a></p>
</div>
</div>
</div><p>In the following table, please find the recommendations for the appropriate Java version for 2026x Refresh1.</p><div class="table-wrap"><table class="fixed-table wrapped confluenceTable"><colgroup><col style="width: 234.0px;"/><col style="width: 142.0px;"/><col style="width: 279.0px;"/></colgroup><tbody><tr><th class="confluenceTh">Product</th><th class="confluenceTh">Version</th><th class="confluenceTh">Recommended and included in installation files**</th></tr><tr><td class="confluenceTd"><ul><li>MagicDraw</li><li>Cameo Systems Modeler</li><li>Cameo Enterprise Architecture</li><li>Magic Software Architect</li><li>Magic Cyber Systems Engineer</li><li>Magic Systems of Systems Architect</li></ul></td><td class="confluenceTd">2026x Refresh1</td><td class="confluenceTd"><p><span style="color:var(--ds-text,#172b4d);"><strong>AdoptOpenJDK 21.0.10+7</strong> (Eclipse Temurin) with HotSpot JVM for all OSs.</span></p></td></tr><tr><td class="confluenceTd"><ul><li>Teamwork Cloud</li><li>Magic Collaboration Studio</li></ul></td><td class="confluenceTd">2026x Refresh1</td><td class="confluenceTd"><p><span style="color:var(--ds-text,#172b4d);"><strong>AdoptOpenJDK 21.0.10+7 </strong>(Eclipse Temurin) with HotSpot JVM.</span></p><p>Cassandra 5.0.x requires <strong>JDK 17.0</strong> (either Oracle or Open JDK).</p></td></tr><tr><td class="confluenceTd"><ul><li>Cameo Collaborator for Teamwork Cloud</li><li>Web Application Platform</li><li>Resources</li><li>TWCloud Admin Console NG</li></ul></td><td class="confluenceTd">2026x Refresh1</td><td class="confluenceTd"><p><span style="color:var(--ds-text,#172b4d);"><strong>AdoptOpenJDK 21.0.10+7 </strong>(Eclipse Temurin) with HotSpot JVM.</span></p></td></tr></tbody></table></div><p>*<strong>OpenJDK</strong>. Based on the testing results, we recommend using Eclipse Temurin™ by ADOPTIUM.</p><div class="panel-macro panel-macros--note conf-macro output-block" data-hasbody="true" data-macro-name="sp-macrooverride-richtextbody-block">
<div class="grid-x">
<div class="cell shrink panel-macros--note__icon">
<img src="/IL/_/AC103202019874DAB34395A7381E7D30/1779799496942/images/common/note-macro-icon.svg"/>
</div>
<div class="cell auto align-self-middle panel-macros--note__content">
<p>OpenJ9 should not be used; instead, the HotSpot distribution should be utilized. For more information, see "Help Me Choose" tips at <a class="external-link" href="https://adoptopenjdk.net/" rel="nofollow">https://adoptopenjdk.net/</a>.</p>
</div>
</div>
</div><p>**Java is included only in installation files for Windows and macOS. Linux installation files do not have built-in Java.</p><p>*** You should choose Java native to the macOS architecture (ARM or x86) in use.</p><hr/><p>See the <a class="conf-macro output-inline" data-hasbody="false" data-macro-name="sp-nobody-link" href="/IL/latest/jvm-recommendations-for-versions-up-to-19-0-sp1-304005446.html">(2026x Refresh1) JVM recommendations for versions up to 19.0 SP1</a>.</p><p>See <a class="conf-macro output-inline" data-hasbody="false" data-macro-name="sp-nobody-link" href="/FAQ/zip-exceptions-thrown-after-java-version-upgrade-to-11-0-20+-or-17-0-8+-136708432.html">Zip exceptions thrown after Java version upgrade to 11.0.20+ or 17.0.8+</a>.</p>
</div>
</div>
<div class="table-overlay full reveal" data-reveal="" id="tableOverlay">
<button aria-label="Close modal" class="close-button table-overlay__close" data-close="" type="button">
<span aria-hidden="true">×</span>
</button>
<div class="article__content table-overlay__content"></div>
</div>
</div>
</section>
</article>
</div>
<div class="cell xlarge-2 article__toc show-for-xlarge">
<div class="scroll-y padding-bottom-3" data-btm-anchor="article-content:bottom" data-options="marginTop:8;" data-sticky="" data-top-anchor="article-content">
<div class="js-tocBot">
</div>
</div>
</div>
</div>
</div>
</main>
````
