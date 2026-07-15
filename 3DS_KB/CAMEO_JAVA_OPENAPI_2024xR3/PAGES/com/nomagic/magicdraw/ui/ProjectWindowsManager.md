# JAVA OPENAPI: ProjectWindowsManager (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/ui/ProjectWindowsManager.html
- source_path: `com/nomagic/magicdraw/ui/ProjectWindowsManager.html`
- source_sha256: `be6ada6320e91459f9c178152fe19872716ccc955aeb84a580bdcd5032077f1c`
- captured_utc: `2026-07-14T16:55:50.781407+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Interface ProjectWindowsManager

All Superinterfaces:
`[WindowsManager](WindowsManager.html)`

@OpenApiAllpublic interfaceProjectWindowsManagerextends [WindowsManager](WindowsManager.html)

Project windows manager allows adding (and manage) the custom windows to the project.

See Also:
[`ProjectWindow`](ProjectWindow.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Interface
Description
`static class`
`[ProjectWindowsManager.ConfiguratorRegistry](ProjectWindowsManager.ConfiguratorRegistry.html)`
Project window configurator registry.
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from interface com.nomagic.magicdraw.ui.[WindowsManager](WindowsManager.html)
`[SIDE_EAST](WindowsManager.html#SIDE_EAST), [SIDE_NORTH](WindowsManager.html#SIDE_NORTH), [SIDE_SOUTH](WindowsManager.html#SIDE_SOUTH), [SIDE_WEST](WindowsManager.html#SIDE_WEST), [STATE_AUTOHIDE](WindowsManager.html#STATE_AUTOHIDE), [STATE_DOCKED](WindowsManager.html#STATE_DOCKED), [STATE_FLOATING](WindowsManager.html#STATE_FLOATING), [STATE_HIDDEN](WindowsManager.html#STATE_HIDDEN)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[activateWindow](#activateWindow(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Activates the project window.
`default void`
`[activateWindow](#activateWindow(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Deprecated.
use [`activateWindow(Project, String)`](#activateWindow(com.nomagic.magicdraw.core.Project,java.lang.String))
`void`
`[addWindow](#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))([Project](../core/Project.html) project,
 [ProjectWindow](ProjectWindow.html) projectWindow)`
Adds project window to the active project.
`default void`
`[addWindow](#addWindow(com.nomagic.magicdraw.ui.ProjectWindow))([ProjectWindow](ProjectWindow.html) projectWindow)`
Deprecated.
use [`addWindow(Project, ProjectWindow)`](#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))
`void`
`[addWindowWithoutOpen](#addWindowWithoutOpen(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))([Project](../core/Project.html) project,
 [ProjectWindow](ProjectWindow.html) window)`
Adds project window to the active project.
`default void`
`[addWindowWithoutOpen](#addWindowWithoutOpen(com.nomagic.magicdraw.ui.ProjectWindow))([ProjectWindow](ProjectWindow.html) projectWindow)`
Deprecated.
use [`addWindowWithoutOpen(Project, ProjectWindow)`](#addWindowWithoutOpen(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))
`[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html)`
`[getBounds](#getBounds(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Returns bounds of window with given id.
`void`
`[hideWindow](#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Hides the project window.
`default void`
`[hideWindow](#hideWindow(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Deprecated.
use [`hideWindow(Project, String)`](#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String))
`void`
`[removeWindow](#removeWindow(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Removes the project window.
`default void`
`[removeWindow](#removeWindow(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)`
Deprecated.
use [`hideWindow(Project, String)`](#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String))
`void`
`[setBounds](#setBounds(com.nomagic.magicdraw.core.Project,java.lang.String,java.awt.Rectangle))([Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)`
Set bounds of window.
`void`
`[updateWindow](#updateWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))([Project](../core/Project.html) project,
 [ProjectWindow](ProjectWindow.html) projectWindow)`
Updates the given project window.
`default void`
`[updateWindow](#updateWindow(com.nomagic.magicdraw.ui.ProjectWindow))([ProjectWindow](ProjectWindow.html) projectWindow)`
Deprecated.
use [`updateWindow(Project, ProjectWindow)`](#updateWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))

============ METHOD DETAIL ========== 
Method Details
addWindow
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void addWindow([ProjectWindow](ProjectWindow.html) projectWindow)
Deprecated.
use [`addWindow(Project, ProjectWindow)`](#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))
addWindow
void addWindow(@CheckForNull
 [Project](../core/Project.html) project,
 [ProjectWindow](ProjectWindow.html) projectWindow)
Adds project window to the active project. Window is opened.
Parameters:
`project` - project
`projectWindow` - project window to add
addWindowWithoutOpen
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void addWindowWithoutOpen([ProjectWindow](ProjectWindow.html) projectWindow)
Deprecated.
use [`addWindowWithoutOpen(Project, ProjectWindow)`](#addWindowWithoutOpen(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))
addWindowWithoutOpen
void addWindowWithoutOpen(@CheckForNull
 [Project](../core/Project.html) project,
 [ProjectWindow](ProjectWindow.html) window)
Adds project window to the active project. Does not try to open window.
Parameters:
`project` - project
`window` - project window to add
updateWindow
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void updateWindow([ProjectWindow](ProjectWindow.html) projectWindow)
Deprecated.
use [`updateWindow(Project, ProjectWindow)`](#updateWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))
updateWindow
void updateWindow(@CheckForNull
 [Project](../core/Project.html) project,
 [ProjectWindow](ProjectWindow.html) projectWindow)
Updates the given project window.
Parameters:
`project` - project
`projectWindow` - project window to update
hideWindow
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void hideWindow([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Deprecated.
use [`hideWindow(Project, String)`](#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String))
hideWindow
void hideWindow(@CheckForNull
 [Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Hides the project window. The window is just hidden, but not removed.
Parameters:
`project` - project
`id` - the id of project window to be hidden
removeWindow
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void removeWindow([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Deprecated.
use [`hideWindow(Project, String)`](#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String))
removeWindow
void removeWindow(@CheckForNull
 [Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Removes the project window.
Parameters:
`project` - project
`id` - the id of project window to be removed
activateWindow
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)default void activateWindow([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Deprecated.
use [`activateWindow(Project, String)`](#activateWindow(com.nomagic.magicdraw.core.Project,java.lang.String))
activateWindow
void activateWindow(@CheckForNull
 [Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Activates the project window.
Parameters:
`project` - project
`id` - the id of project window to be activated.
getBounds
@CheckForNull[Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) getBounds(@CheckForNull
 [Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)
Returns bounds of window with given id.
Parameters:
`project` - project
`id` - window id
Returns:
bounds of window
setBounds
void setBounds(@CheckForNull
 [Project](../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id,
 [Rectangle](https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html) bounds)
Set bounds of window. Bounds are changed only if window is "floating". If window is docked inside other container, size is not changed.
Parameters:
`project` - project
`id` - window id
`bounds` - bounds

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Interface ProjectWindowsManager">Interface ProjectWindowsManager</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="WindowsManager.html" title="interface in com.nomagic.magicdraw.ui">WindowsManager</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectWindowsManager</span><span class="extends-implements">
extends <a href="WindowsManager.html" title="interface in com.nomagic.magicdraw.ui">WindowsManager</a></span></div>
<div class="block">Project windows manager allows adding (and manage) the custom windows to the project.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui"><code>ProjectWindow</code></a></li>
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
<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Interface</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ProjectWindowsManager.ConfiguratorRegistry.html" title="class in com.nomagic.magicdraw.ui">ProjectWindowsManager.ConfiguratorRegistry</a></code></div>
<div class="col-last even-row-color">
<div class="block">Project window configurator registry.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicdraw.ui.WindowsManager">Fields inherited from interface com.nomagic.magicdraw.ui.<a href="WindowsManager.html" title="interface in com.nomagic.magicdraw.ui">WindowsManager</a></h3>
<code><a href="WindowsManager.html#SIDE_EAST">SIDE_EAST</a>, <a href="WindowsManager.html#SIDE_NORTH">SIDE_NORTH</a>, <a href="WindowsManager.html#SIDE_SOUTH">SIDE_SOUTH</a>, <a href="WindowsManager.html#SIDE_WEST">SIDE_WEST</a>, <a href="WindowsManager.html#STATE_AUTOHIDE">STATE_AUTOHIDE</a>, <a href="WindowsManager.html#STATE_DOCKED">STATE_DOCKED</a>, <a href="WindowsManager.html#STATE_FLOATING">STATE_FLOATING</a>, <a href="WindowsManager.html#STATE_HIDDEN">STATE_HIDDEN</a></code></div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab5" onclick="show('method-summary-table', 'method-summary-table-tab5', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Default Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#activateWindow(com.nomagic.magicdraw.core.Project,java.lang.String)">activateWindow</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Activates the project window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#activateWindow(java.lang.String)">activateWindow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#activateWindow(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>activateWindow(Project, String)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)">addWindow</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds project window to the active project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#addWindow(com.nomagic.magicdraw.ui.ProjectWindow)">addWindow</a><wbr/>(<a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)"><code>addWindow(Project, ProjectWindow)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#addWindowWithoutOpen(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)">addWindowWithoutOpen</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> window)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Adds project window to the active project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#addWindowWithoutOpen(com.nomagic.magicdraw.ui.ProjectWindow)">addWindowWithoutOpen</a><wbr/>(<a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#addWindowWithoutOpen(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)"><code>addWindowWithoutOpen(Project, ProjectWindow)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBounds(com.nomagic.magicdraw.core.Project,java.lang.String)">getBounds</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns bounds of window with given id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String)">hideWindow</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Hides the project window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#hideWindow(java.lang.String)">hideWindow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>hideWindow(Project, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#removeWindow(com.nomagic.magicdraw.core.Project,java.lang.String)">removeWindow</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Removes the project window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#removeWindow(java.lang.String)">removeWindow</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>hideWindow(Project, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBounds(com.nomagic.magicdraw.core.Project,java.lang.String,java.awt.Rectangle)">setBounds</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set bounds of window.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#updateWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)">updateWindow</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Updates the given project window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code>default void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6"><code><a class="member-name-link" href="#updateWindow(com.nomagic.magicdraw.ui.ProjectWindow)">updateWindow</a><wbr/>(<a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab5 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#updateWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)"><code>updateWindow(Project, ProjectWindow)</code></a></div>
</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="addWindow(com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>addWindow</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">addWindow</span><wbr/><span class="parameters">(<a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)"><code>addWindow(Project, ProjectWindow)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>addWindow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addWindow</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</span></div>
<div class="block">Adds project window to the active project. Window is opened.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>projectWindow</code> - project window to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addWindowWithoutOpen(com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>addWindowWithoutOpen</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">addWindowWithoutOpen</span><wbr/><span class="parameters">(<a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#addWindowWithoutOpen(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)"><code>addWindowWithoutOpen(Project, ProjectWindow)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="addWindowWithoutOpen(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>addWindowWithoutOpen</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">addWindowWithoutOpen</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> window)</span></div>
<div class="block">Adds project window to the active project. Does not try to open window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>window</code> - project window to add</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateWindow(com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>updateWindow</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">updateWindow</span><wbr/><span class="parameters">(<a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#updateWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)"><code>updateWindow(Project, ProjectWindow)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="updateWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)">
<h3>updateWindow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">updateWindow</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindow.html" title="class in com.nomagic.magicdraw.ui">ProjectWindow</a> projectWindow)</span></div>
<div class="block">Updates the given project window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>projectWindow</code> - project window to update</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideWindow(java.lang.String)">
<h3>hideWindow</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">hideWindow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>hideWindow(Project, String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>hideWindow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">hideWindow</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Hides the project window. The window is just hidden, but not removed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>id</code> - the id of project window to be hidden</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeWindow(java.lang.String)">
<h3>removeWindow</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">removeWindow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#hideWindow(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>hideWindow(Project, String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="removeWindow(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>removeWindow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">removeWindow</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Removes the project window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>id</code> - the id of project window to be removed</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="activateWindow(java.lang.String)">
<h3>activateWindow</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">default</span> <span class="return-type">void</span> <span class="element-name">activateWindow</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#activateWindow(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>activateWindow(Project, String)</code></a></div>
</div>
</section>
</li>
<li>
<section class="detail" id="activateWindow(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>activateWindow</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">activateWindow</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Activates the project window.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>id</code> - the id of project window to be activated.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBounds(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>getBounds</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a></span> <span class="element-name">getBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id)</span></div>
<div class="block">Returns bounds of window with given id.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>id</code> - window id</dd>
<dt>Returns:</dt>
<dd>bounds of window</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBounds(com.nomagic.magicdraw.core.Project,java.lang.String,java.awt.Rectangle)">
<h3>setBounds</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBounds</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> id,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.desktop/java/awt/Rectangle.html" title="class or interface in java.awt">Rectangle</a> bounds)</span></div>
<div class="block">Set bounds of window. Bounds are changed only if window is "floating". If window is docked inside other container, size is not changed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>id</code> - window id</dd>
<dd><code>bounds</code> - bounds</dd>
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
