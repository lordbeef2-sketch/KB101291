# JAVA OPENAPI: DiagramListenerAdapter (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/magicdraw/uml/symbols/DiagramListenerAdapter.html
- source_path: `com/nomagic/magicdraw/uml/symbols/DiagramListenerAdapter.html`
- source_sha256: `e86c64321332189fe801bf22eb429318854b7f2396b9c3568327e25801491461`
- captured_utc: `2026-07-14T16:58:29.750199+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.symbols](package-summary.html)

## Class DiagramListenerAdapter

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.symbols.DiagramListenerAdapter

@OpenApipublic classDiagramListenerAdapter
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
Forwards diagram events to the given [`PropertyChangeListener`](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) delegate.
 Diagram content event listeners in [`DiagramPresentationElement`](DiagramPresentationElement.html)
 are notified about all changes in the opened diagram.
 This class adds itself to those listeners and forwards all events to the delegate.
 It listens for diagram content change events from opened diagrams only.
 It takes care of (de)attaching itself as listener to the diagram when diagram is closed or opened.
 Diagram open/close events are forwarded to the delegate as well.
 
A DiagramListenerAdapter object has the ability to delegate all events to your own listener. This adapter is
 everything you need, when listening to the opened diagram change events. Adapter works in a project scope.
To listen to the diagram change events, you must create a DiagramListenerAdapter and install it for the project.
 To create the DiagramListenerAdapter, call:
 new DiagramListenerAdapter(propertyChangeListener)
To create the adapter, you need to pass the property change listener as a delegate,
 which will receive all events. To start using the adapter, install it.
 Uninstall it when it is no longer necessary.
IMPORTANT! The uninstalled adapter cannot be reused anymore.
 To start receiving events, you must create a new instance of the DiagramListenerAdapter.
Example of listening to symbol creation/deletion
DiagramListenerAdapter adapter = new DiagramListenerAdapter(new PropertyChangeListener()
 {
 public void propertyChange(PropertyChangeEvent evt)
 {
 String propertyName = evt.getPropertyName();
 if (ExtendedPropertyNames.VIEW_ADDED.equals(propertyName) ||
 ExtendedPropertyNames.VIEW_REMOVED.equals(propertyName))
 {
 // added/removed symbol
 PresentationElement presentationElement = (PresentationElement) evt.getNewValue();
 }
 }
 });

 adapter.install(project);

 // When it is no longer needed, uninstall it.
 adapter.uninstall(project);

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[DiagramListenerAdapter](#%3Cinit%3E(com.nomagic.magicdraw.core.Project,java.beans.PropertyChangeListener))([Project](../../core/Project.html) project,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) delegate)`
Deprecated.
Use [`DiagramListenerAdapter(java.beans.PropertyChangeListener)`](#%3Cinit%3E(java.beans.PropertyChangeListener))
`[DiagramListenerAdapter](#%3Cinit%3E(java.beans.PropertyChangeListener))([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) delegate)`
Constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`void`
`[dispose](#dispose(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Deprecated.
Use [`uninstall(Project)`](#uninstall(com.nomagic.magicdraw.core.Project))
`void`
`[install](#install(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Install DiagramListenerAdapter to a project.
`void`
`[uninstall](#uninstall(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Removes itself from the project.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
DiagramListenerAdapter
@OpenApi
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public DiagramListenerAdapter([Project](../../core/Project.html) project,
 [PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) delegate)
Deprecated.
Use [`DiagramListenerAdapter(java.beans.PropertyChangeListener)`](#%3Cinit%3E(java.beans.PropertyChangeListener))
Install DiagramListenerAdapter to a project.
 Use [`uninstall(Project)`](#uninstall(com.nomagic.magicdraw.core.Project)) to stop receiving property change event in delegate.
Parameters:
`project` - project to install adapter to.
`delegate` - delegate listener.
DiagramListenerAdapter
@OpenApipublic DiagramListenerAdapter([PropertyChangeListener](https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html) delegate)
Constructor.
Parameters:
`delegate` - delegate listener.
 ============ METHOD DETAIL ========== 
Method Details
dispose
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)
@OpenApipublic void dispose([Project](../../core/Project.html) project)
Deprecated.
Use [`uninstall(Project)`](#uninstall(com.nomagic.magicdraw.core.Project))
Removes itself from the project.
Parameters:
`project` - uninstall from a project.
install
@OpenApipublic void install([Project](../../core/Project.html) project)
Install DiagramListenerAdapter to a project.
Parameters:
`project` - project to install adapter to.
See Also:
[`uninstall(Project)`](#uninstall(com.nomagic.magicdraw.core.Project))
uninstall
@OpenApipublic void uninstall([Project](../../core/Project.html) project)
Removes itself from the project.
Parameters:
`project` - uninstall from a project.
See Also:
[`install(com.nomagic.magicdraw.core.Project)`](#install(com.nomagic.magicdraw.core.Project))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.symbols</a></div>
<h1 class="title" title="Class DiagramListenerAdapter">Class DiagramListenerAdapter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.symbols.DiagramListenerAdapter</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public class </span><span class="element-name type-name-label">DiagramListenerAdapter</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>
 Forwards diagram events to the given <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans"><code>PropertyChangeListener</code></a> delegate.
 Diagram content event listeners in <a href="DiagramPresentationElement.html" title="class in com.nomagic.magicdraw.uml.symbols"><code>DiagramPresentationElement</code></a>
 are notified about all changes in the opened diagram.
 This class adds itself to those listeners and forwards all events to the delegate.
 It listens for diagram content change events from opened diagrams only.
 It takes care of (de)attaching itself as listener to the diagram when diagram is closed or opened.
 Diagram open/close events are forwarded to the delegate as well.
 <p></p>
<p>
 A DiagramListenerAdapter object has the ability to delegate all events to your own listener. This adapter is
 everything you need, when listening to the opened diagram change events. Adapter works in a project scope.
 </p>
<p>
 To listen to the diagram change events, you must create a DiagramListenerAdapter and install it for the project.
 To create the DiagramListenerAdapter, call:
 <pre>
 new DiagramListenerAdapter(propertyChangeListener)
 </pre>
<p>
 To create the adapter, you need to pass the property change listener as a delegate,
 which will receive all events. To start using the adapter, install it.
 Uninstall it when it is no longer necessary.
 </p>
<p>
 IMPORTANT! The uninstalled adapter cannot be reused anymore.
 To start receiving events, you must create a new instance of the DiagramListenerAdapter.
 </p>
<h4 id="example-of-listening-to-symbol-creation-deletion-heading">Example of listening to symbol creation/deletion</h4>
<pre>
 DiagramListenerAdapter adapter = new DiagramListenerAdapter(new PropertyChangeListener()
 {
        public void propertyChange(PropertyChangeEvent evt)
     {
                String propertyName = evt.getPropertyName();
                if (ExtendedPropertyNames.VIEW_ADDED.equals(propertyName) ||
                        ExtendedPropertyNames.VIEW_REMOVED.equals(propertyName))
         {
                        // added/removed symbol
                        PresentationElement presentationElement = (PresentationElement) evt.getNewValue();
         }
     }
 });

 adapter.install(project);

 // When it is no longer needed, uninstall it.
 adapter.uninstall(project);
 </pre></p></p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicdraw.core.Project,java.beans.PropertyChangeListener)">DiagramListenerAdapter</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> delegate)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#%3Cinit%3E(java.beans.PropertyChangeListener)"><code>DiagramListenerAdapter(java.beans.PropertyChangeListener)</code></a></div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.beans.PropertyChangeListener)">DiagramListenerAdapter</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> delegate)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#dispose(com.nomagic.magicdraw.core.Project)">dispose</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#uninstall(com.nomagic.magicdraw.core.Project)"><code>uninstall(Project)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#install(com.nomagic.magicdraw.core.Project)">install</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Install DiagramListenerAdapter to a project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#uninstall(com.nomagic.magicdraw.core.Project)">uninstall</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes itself from the project.</div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicdraw.core.Project,java.beans.PropertyChangeListener)">
<h3>DiagramListenerAdapter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">DiagramListenerAdapter</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> delegate)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#%3Cinit%3E(java.beans.PropertyChangeListener)"><code>DiagramListenerAdapter(java.beans.PropertyChangeListener)</code></a></div>
</div>
<div class="block">Install DiagramListenerAdapter to a project.
 Use <a href="#uninstall(com.nomagic.magicdraw.core.Project)"><code>uninstall(Project)</code></a> to stop receiving property change event in delegate.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to install adapter to.</dd>
<dd><code>delegate</code> - delegate listener.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.beans.PropertyChangeListener)">
<h3>DiagramListenerAdapter</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="element-name">DiagramListenerAdapter</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.desktop/java/beans/PropertyChangeListener.html" title="class or interface in java.beans">PropertyChangeListener</a> delegate)</span></div>
<div class="block">Constructor.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>delegate</code> - delegate listener.</dd>
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
<section class="detail" id="dispose(com.nomagic.magicdraw.core.Project)">
<h3>dispose</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Use <a href="#uninstall(com.nomagic.magicdraw.core.Project)"><code>uninstall(Project)</code></a></div>
</div>
<div class="block">Removes itself from the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - uninstall from a project.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="install(com.nomagic.magicdraw.core.Project)">
<h3>install</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">install</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Install DiagramListenerAdapter to a project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project to install adapter to.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#uninstall(com.nomagic.magicdraw.core.Project)"><code>uninstall(Project)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="uninstall(com.nomagic.magicdraw.core.Project)">
<h3>uninstall</h3>
<div class="member-signature"><span class="annotations">@OpenApi
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">uninstall</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Removes itself from the project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - uninstall from a project.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#install(com.nomagic.magicdraw.core.Project)"><code>install(com.nomagic.magicdraw.core.Project)</code></a></li>
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
