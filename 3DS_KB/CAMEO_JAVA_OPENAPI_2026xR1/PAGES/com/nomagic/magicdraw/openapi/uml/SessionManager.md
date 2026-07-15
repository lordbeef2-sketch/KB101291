# JAVA OPENAPI: SessionManager (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/openapi/uml/SessionManager.html
- source_path: `com/nomagic/magicdraw/openapi/uml/SessionManager.html`
- source_sha256: `9e4df10c5df4abe9cd1281e05430b0f8e41117fd3260fe5ff737b73d03d33bb6`
- captured_utc: `2026-07-14T16:45:38.887518+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.openapi.uml](package-summary.html)

## Class SessionManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.openapi.uml.SessionManager

@OpenApiAllpublic classSessionManager
extends [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
The singleton manager for Elements editing in the model.
 In order to edit some Element session with this manager must be created.
 After Element editing session must be closed.
 After that all changes will be applied to model and registered in command history(for undo/redo).
 Only one session can be active at the time.
 The sample of code is :`Class classA = ...; 
 

 SessionManager.getInstance().createSession("Edit class A"); 

 classA.setName("nameB"); 

 Operation operation = Project.getProject(classA).getElementsFactory().createOperationInstance(); 

 ModelElementsManager.getInstance().addElement(operation, classA); 

 SessionManager.getInstance().closeSession();`
Not editable(read only) Elements cannot be edited.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`<V> V`
`[callInsideSession](#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable))([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)`
Calls given callable inside session.
`<V> V`
`[callInsideSession](#callInsideSession(java.lang.String,java.util.concurrent.Callable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)`
Deprecated.
use [`callInsideSession(Project, String, Callable)`](#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable))
`void`
`[cancelSession](#cancelSession())()`
Deprecated.
use [`cancelSession(Project)`](#cancelSession(com.nomagic.magicdraw.core.Project))
`void`
`[cancelSession](#cancelSession(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Closes active session in a given project.
`void`
`[checkReadOnly](#checkReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target)`
Tests if the given element is read only.
`void`
`[checkSessionExistance](#checkSessionExistance())()`
Deprecated.
use [`checkSessionExistence(Project)`](#checkSessionExistence(com.nomagic.magicdraw.core.Project))
`void`
`[checkSessionExistance](#checkSessionExistance(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Deprecated.
typo.
`void`
`[checkSessionExistence](#checkSessionExistence())()`
Deprecated.
type.
`void`
`[checkSessionExistence](#checkSessionExistence(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Checks if the session is created in a given project.
`void`
`[closeSession](#closeSession())()`
Deprecated.
use [`closeSession(Project)`](#closeSession(com.nomagic.magicdraw.core.Project))
`void`
`[closeSession](#closeSession(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Closes active session in a given project.
`void`
`[createSession](#createSession(com.nomagic.magicdraw.core.Project,java.lang.String))([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName)`
Creates new session in a given project.
`void`
`[createSession](#createSession(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName)`
Deprecated.
use [`createSession(Project, String)`](#createSession(com.nomagic.magicdraw.core.Project,java.lang.String))
`void`
`[executeInsideSession](#executeInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Runnable))([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)`
Executes given runnable inside session.
`void`
`[executeInsideSession](#executeInsideSession(java.lang.String,java.lang.Runnable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)`
Deprecated.
use [`executeInsideSession(Project, String, Runnable)`](#executeInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Runnable))
`static [SessionManager](SessionManager.html)`
`[getInstance](#getInstance())()`
Returns an instance of this manager.
`boolean`
`[isSessionCreated](#isSessionCreated())()`
Deprecated.
use [`isSessionCreated(Project)`](#isSessionCreated(com.nomagic.magicdraw.core.Project))
`boolean`
`[isSessionCreated](#isSessionCreated(com.nomagic.magicdraw.core.Project))([Project](../../core/Project.html) project)`
Returns true if some session is created in a given project.
`void`
`[runInSession](#runInSession(java.lang.String,java.lang.Runnable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)`
Deprecated.
use [`executeInsideSession(String, Runnable)`](#executeInsideSession(java.lang.String,java.lang.Runnable))
`<V> V`
`[runInSession](#runInSession(java.lang.String,java.util.concurrent.Callable))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)`
Deprecated.
use [`callInsideSession(Project, String, Callable)`](#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)) or [`supplyInsideSession(Project, String, Supplier)`](#supplyInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.function.Supplier))
`<V> V`
`[supplyInsideSession](#supplyInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.function.Supplier))([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<V> supplier)`
Applies given supplier inside session.
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ METHOD DETAIL ========== 
Method Details
getInstance
public static [SessionManager](SessionManager.html) getInstance()
Returns an instance of this manager.
Returns:
instance of this manager.
closeSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void closeSession()
Deprecated.
use [`closeSession(Project)`](#closeSession(com.nomagic.magicdraw.core.Project))
Closes active session in an active project. All changed made to registered ModelElements will be recorder in the command
 history.
 Session cannot be closed if it was not created with method `createSession` before that.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session was not created.
See Also:
[`createSession(java.lang.String)`](#createSession(java.lang.String))
closeSession
public void closeSession([Project](../../core/Project.html) project)
Closes active session in a given project. All changed made to registered ModelElements will be recorder in the command
 history.
 Session cannot be closed if it was not created with method `createSession` before that.
Parameters:
`project` - project
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session was not created.
See Also:
[`createSession(java.lang.String)`](#createSession(java.lang.String))
cancelSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void cancelSession()
Deprecated.
use [`cancelSession(Project)`](#cancelSession(com.nomagic.magicdraw.core.Project))
Closes active session. All changed made to registered ModelElements will be rolled back and command will be
 removed from the command history list.
 Session cannot be canceled if it was not created with method `createSession` before that.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session was not created.
See Also:
[`createSession(java.lang.String)`](#createSession(java.lang.String))
cancelSession
public void cancelSession(@CheckForNull
 [Project](../../core/Project.html) project)
Closes active session in a given project. All changed made to registered ModelElements will be rolled back and command will be
 removed from the command history list.
 Session cannot be canceled if it was not created with method `createSession` before that.
Parameters:
`project` - project
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session was not created.
See Also:
[`createSession(java.lang.String)`](#createSession(java.lang.String))
checkSessionExistance
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void checkSessionExistance()
Deprecated.
use [`checkSessionExistence(Project)`](#checkSessionExistence(com.nomagic.magicdraw.core.Project))
Checks if the session is created.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created at the current moment.
See Also:
[`isSessionCreated()`](#isSessionCreated())
checkSessionExistence
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void checkSessionExistence()
Deprecated.
type. Use [`checkSessionExistence(Project)`](#checkSessionExistence(com.nomagic.magicdraw.core.Project))
Checks if the session is created.
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created at the current moment.
See Also:
[`isSessionCreated()`](#isSessionCreated())
checkSessionExistance
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void checkSessionExistance(@CheckForNull
 [Project](../../core/Project.html) project)
Deprecated.
typo. Use [`checkSessionExistence(Project)`](#checkSessionExistence(com.nomagic.magicdraw.core.Project))
Checks if the session is created in a given project.
Parameters:
`project` - project
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created at the current moment.
See Also:
[`isSessionCreated()`](#isSessionCreated())
checkSessionExistence
public void checkSessionExistence(@CheckForNull
 [Project](../../core/Project.html) project)
Checks if the session is created in a given project.
Parameters:
`project` - project
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if session is not created at the current moment.
See Also:
[`isSessionCreated()`](#isSessionCreated())
createSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void createSession([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName)
Deprecated.
use [`createSession(Project, String)`](#createSession(com.nomagic.magicdraw.core.Project,java.lang.String))
Creates new session in an active project. Session cannot be created if other session was not closed with `closeSession`
 method.
Parameters:
`sessionName` - name of session which will be the name of command the command history(undo/redo).
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if other session is already created and not closed.
See Also:
[`closeSession()`](#closeSession())
createSession
public void createSession([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName)
Creates new session in a given project. Session cannot be created if other session was not closed with `closeSession`
 method.
Parameters:
`project` - project
`sessionName` - name of session which will be the name of command the command history(undo/redo).
Throws:
`[IllegalStateException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html)` - if other session is already created and not closed.
See Also:
[`closeSession()`](#closeSession())
isSessionCreated
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public boolean isSessionCreated()
Deprecated.
use [`isSessionCreated(Project)`](#isSessionCreated(com.nomagic.magicdraw.core.Project))
Returns true if some session is created in an active project.
Returns:
true, if session is created(active).
See Also:
[`createSession(java.lang.String)`](#createSession(java.lang.String))
isSessionCreated
public boolean isSessionCreated(@CheckForNull
 [Project](../../core/Project.html) project)
Returns true if some session is created in a given project.
Parameters:
`project` - project
Returns:
true, if session is created(active).
See Also:
[`createSession(java.lang.String)`](#createSession(java.lang.String))
checkReadOnly
public void checkReadOnly([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) target)
 throws [ReadOnlyElementException](ReadOnlyElementException.html)
Tests if the given element is read only.
Parameters:
`target` - element to check
Throws:
`[ReadOnlyElementException](ReadOnlyElementException.html)` - exception if given element is read only.
runInSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void runInSession([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)
Deprecated.
use [`executeInsideSession(String, Runnable)`](#executeInsideSession(java.lang.String,java.lang.Runnable))
Execute the given runnable in MD session. runInSession() will check whether a session has been
 already created. If not, it creates a new session. After executed, it closes its created session.
 The method never cancels the session even exception occurs. A runnable needs to cancel the session
 explicitly in case of exception.
Parameters:
`sessionName` - session name if it needs to be created
`runnable` - runnable to run
executeInsideSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public void executeInsideSession([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)
Deprecated.
use [`executeInsideSession(Project, String, Runnable)`](#executeInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Runnable))
Executes given runnable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on execution).
Parameters:
`sessionName` - new session name.
`runnable` - runnable to execute.
runInSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public <V> V runInSession([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)
Deprecated.
use [`callInsideSession(Project, String, Callable)`](#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)) or [`supplyInsideSession(Project, String, Supplier)`](#supplyInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.function.Supplier))
Execute the given callable in MD session. runInSession() will check whether a session has been
 already created. If not, it creates a new session. After executed, it closes its created session.
 The method never cancels the session even exception occurs. A callable needs to cancel the session
 explicitly in case of exception.
Type Parameters:
`V` - the return type
Parameters:
`sessionName` - the session name
`callable` - the callable object
Returns:
the return value from callable.
callInsideSession
[@Deprecated](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html)public <V> V callInsideSession([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Deprecated.
use [`callInsideSession(Project, String, Callable)`](#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable))
Calls given callable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on calling).
Type Parameters:
`V` - return type.
Parameters:
`sessionName` - new session name.
`callable` - callable to call.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
callInsideSession
public <V> V callInsideSession([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Callable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html)<V> callable)
 throws [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)
Calls given callable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on calling).
Type Parameters:
`V` - return type.
Parameters:
`project` - project
`sessionName` - new session name.
`callable` - callable to call.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
supplyInsideSession
public <V> V supplyInsideSession([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Supplier](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html)<V> supplier)
Applies given supplier inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on calling).
Type Parameters:
`V` - return type
Parameters:
`project` - project
`sessionName` - new session name
`supplier` - supplier to apply
executeInsideSession
public void executeInsideSession([Project](../../core/Project.html) project,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) sessionName,
 [Runnable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html) runnable)
Executes given runnable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on execution).
Parameters:
`project` - project
`sessionName` - new session name.
`runnable` - runnable to execute.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.openapi.uml</a></div>
<h1 class="title" title="Class SessionManager">Class SessionManager</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.openapi.uml.SessionManager</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">SessionManager</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">The singleton manager for Elements editing in the model.
 <p>
 In order to edit some Element session with this manager must be created.
 After Element editing session must be closed.
 After that all changes will be applied to model and registered in command history(for undo/redo).
 <p>
 Only one session can be active at the time.
 The sample of code is :<code><br/><br/>
 Class classA = ...;<br/><br/>
 SessionManager.getInstance().createSession("Edit class A");<br/>
 classA.setName("nameB");<br/>
 Operation operation = Project.getProject(classA).getElementsFactory().createOperationInstance();<br/>
 ModelElementsManager.getInstance().addElement(operation, classA);<br/>
 SessionManager.getInstance().closeSession();<br/>
</code>
<p>
 Not editable(read only) Elements cannot be edited.</p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;V&gt; V</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)">callInsideSession</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Calls given callable inside session.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>&lt;V&gt; V</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#callInsideSession(java.lang.String,java.util.concurrent.Callable)">callInsideSession</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)"><code>callInsideSession(Project, String, Callable)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#cancelSession()">cancelSession</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#cancelSession(com.nomagic.magicdraw.core.Project)"><code>cancelSession(Project)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#cancelSession(com.nomagic.magicdraw.core.Project)">cancelSession</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes active session in a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">checkReadOnly</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests if the given element is read only.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#checkSessionExistance()">checkSessionExistance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#checkSessionExistence(com.nomagic.magicdraw.core.Project)"><code>checkSessionExistence(Project)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#checkSessionExistance(com.nomagic.magicdraw.core.Project)">checkSessionExistance</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">typo.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#checkSessionExistence()">checkSessionExistence</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">type.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#checkSessionExistence(com.nomagic.magicdraw.core.Project)">checkSessionExistence</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if the session is created in a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#closeSession()">closeSession</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#closeSession(com.nomagic.magicdraw.core.Project)"><code>closeSession(Project)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#closeSession(com.nomagic.magicdraw.core.Project)">closeSession</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Closes active session in a given project.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#createSession(com.nomagic.magicdraw.core.Project,java.lang.String)">createSession</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates new session in a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#createSession(java.lang.String)">createSession</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createSession(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>createSession(Project, String)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#executeInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Runnable)">executeInsideSession</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Executes given runnable inside session.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#executeInsideSession(java.lang.String,java.lang.Runnable)">executeInsideSession</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#executeInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Runnable)"><code>executeInsideSession(Project, String, Runnable)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml">SessionManager</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance()">getInstance</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an instance of this manager.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSessionCreated()">isSessionCreated</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#isSessionCreated(com.nomagic.magicdraw.core.Project)"><code>isSessionCreated(Project)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isSessionCreated(com.nomagic.magicdraw.core.Project)">isSessionCreated</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns true if some session is created in a given project.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#runInSession(java.lang.String,java.lang.Runnable)">runInSession</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#executeInsideSession(java.lang.String,java.lang.Runnable)"><code>executeInsideSession(String, Runnable)</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>&lt;V&gt; V</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#runInSession(java.lang.String,java.util.concurrent.Callable)">runInSession</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)"><code>callInsideSession(Project, String, Callable)</code></a> or <a href="#supplyInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.function.Supplier)"><code>supplyInsideSession(Project, String, Supplier)</code></a></div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>&lt;V&gt; V</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#supplyInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.function.Supplier)">supplyInsideSession</a><wbr/>(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;V&gt; supplier)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Applies given supplier inside session.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="getInstance()">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="SessionManager.html" title="class in com.nomagic.magicdraw.openapi.uml">SessionManager</a></span> <span class="element-name">getInstance</span>()</div>
<div class="block">Returns an instance of this manager.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>instance of this manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeSession()">
<h3>closeSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeSession</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#closeSession(com.nomagic.magicdraw.core.Project)"><code>closeSession(Project)</code></a></div>
</div>
<div class="block">Closes active session in an active project. All changed made to registered ModelElements will be recorder in the command
 history.
 Session cannot be closed if it was not created with method <code>createSession</code> before that.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session was not created.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createSession(java.lang.String)"><code>createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closeSession(com.nomagic.magicdraw.core.Project)">
<h3>closeSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">closeSession</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Closes active session in a given project. All changed made to registered ModelElements will be recorder in the command
 history.
 Session cannot be closed if it was not created with method <code>createSession</code> before that.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session was not created.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createSession(java.lang.String)"><code>createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cancelSession()">
<h3>cancelSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelSession</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#cancelSession(com.nomagic.magicdraw.core.Project)"><code>cancelSession(Project)</code></a></div>
</div>
<div class="block">Closes active session. All changed made to registered ModelElements will be rolled back and command will be
 removed from the command history list.
 Session cannot be canceled if it was not created with method <code>createSession</code> before that.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session was not created.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createSession(java.lang.String)"><code>createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cancelSession(com.nomagic.magicdraw.core.Project)">
<h3>cancelSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelSession</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Closes active session in a given project. All changed made to registered ModelElements will be rolled back and command will be
 removed from the command history list.
 Session cannot be canceled if it was not created with method <code>createSession</code> before that.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session was not created.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createSession(java.lang.String)"><code>createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkSessionExistance()">
<h3>checkSessionExistance</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">checkSessionExistance</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#checkSessionExistence(com.nomagic.magicdraw.core.Project)"><code>checkSessionExistence(Project)</code></a></div>
</div>
<div class="block">Checks if the session is created.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created at the current moment.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isSessionCreated()"><code>isSessionCreated()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkSessionExistence()">
<h3>checkSessionExistence</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">checkSessionExistence</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">type. Use <a href="#checkSessionExistence(com.nomagic.magicdraw.core.Project)"><code>checkSessionExistence(Project)</code></a></div>
</div>
<div class="block">Checks if the session is created.</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created at the current moment.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isSessionCreated()"><code>isSessionCreated()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkSessionExistance(com.nomagic.magicdraw.core.Project)">
<h3>checkSessionExistance</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">checkSessionExistance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">typo. Use <a href="#checkSessionExistence(com.nomagic.magicdraw.core.Project)"><code>checkSessionExistence(Project)</code></a></div>
</div>
<div class="block">Checks if the session is created in a given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created at the current moment.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isSessionCreated()"><code>isSessionCreated()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkSessionExistence(com.nomagic.magicdraw.core.Project)">
<h3>checkSessionExistence</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">checkSessionExistence</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Checks if the session is created in a given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if session is not created at the current moment.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#isSessionCreated()"><code>isSessionCreated()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSession(java.lang.String)">
<h3>createSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createSession</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#createSession(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>createSession(Project, String)</code></a></div>
</div>
<div class="block">Creates new session in an active project. Session cannot be created if other session was not closed with <code>closeSession</code>
 method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sessionName</code> - name of session which will be the name of command the command history(undo/redo).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if other session is already created and not closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#closeSession()"><code>closeSession()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createSession(com.nomagic.magicdraw.core.Project,java.lang.String)">
<h3>createSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createSession</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName)</span></div>
<div class="block">Creates new session in a given project. Session cannot be created if other session was not closed with <code>closeSession</code>
 method.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>sessionName</code> - name of session which will be the name of command the command history(undo/redo).</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/IllegalStateException.html" title="class or interface in java.lang">IllegalStateException</a></code> - if other session is already created and not closed.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="#closeSession()"><code>closeSession()</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSessionCreated()">
<h3>isSessionCreated</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSessionCreated</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#isSessionCreated(com.nomagic.magicdraw.core.Project)"><code>isSessionCreated(Project)</code></a></div>
</div>
<div class="block">Returns true if some session is created in an active project.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true, if session is created(active).</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createSession(java.lang.String)"><code>createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isSessionCreated(com.nomagic.magicdraw.core.Project)">
<h3>isSessionCreated</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSessionCreated</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project)</span></div>
<div class="block">Returns true if some session is created in a given project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dt>Returns:</dt>
<dd>true, if session is created(active).</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="#createSession(java.lang.String)"><code>createSession(java.lang.String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="checkReadOnly(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>checkReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">checkReadOnly</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> target)</span>
                   throws <span class="exceptions"><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></span></div>
<div class="block">Tests if the given element is read only.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - element to check</dd>
<dt>Throws:</dt>
<dd><code><a href="ReadOnlyElementException.html" title="class in com.nomagic.magicdraw.openapi.uml">ReadOnlyElementException</a></code> - exception if given element is read only.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runInSession(java.lang.String,java.lang.Runnable)">
<h3>runInSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">runInSession</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#executeInsideSession(java.lang.String,java.lang.Runnable)"><code>executeInsideSession(String, Runnable)</code></a></div>
</div>
<div class="block">Execute the given runnable in MD session. runInSession() will check whether a session has been
 already created. If not, it creates a new session. After executed, it closes its created session.
 The method never cancels the session even exception occurs. A runnable needs to cancel the session
 explicitly in case of exception.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sessionName</code> - session name if it needs to be created</dd>
<dd><code>runnable</code> - runnable to run</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executeInsideSession(java.lang.String,java.lang.Runnable)">
<h3>executeInsideSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">executeInsideSession</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#executeInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Runnable)"><code>executeInsideSession(Project, String, Runnable)</code></a></div>
</div>
<div class="block">Executes given runnable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on execution).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sessionName</code> - new session name.</dd>
<dd><code>runnable</code> - runnable to execute.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="runInSession(java.lang.String,java.util.concurrent.Callable)">
<h3>runInSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;V&gt;</span> <span class="return-type">V</span> <span class="element-name">runInSession</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)"><code>callInsideSession(Project, String, Callable)</code></a> or <a href="#supplyInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.function.Supplier)"><code>supplyInsideSession(Project, String, Supplier)</code></a></div>
</div>
<div class="block">Execute the given callable in MD session. runInSession() will check whether a session has been
 already created. If not, it creates a new session. After executed, it closes its created session.
 The method never cancels the session even exception occurs. A callable needs to cancel the session
 explicitly in case of exception.</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>V</code> - the return type</dd>
<dt>Parameters:</dt>
<dd><code>sessionName</code> - the session name</dd>
<dd><code>callable</code> - the callable object</dd>
<dt>Returns:</dt>
<dd>the return value from callable.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callInsideSession(java.lang.String,java.util.concurrent.Callable)">
<h3>callInsideSession</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="type-parameters">&lt;V&gt;</span> <span class="return-type">V</span> <span class="element-name">callInsideSession</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)"><code>callInsideSession(Project, String, Callable)</code></a></div>
</div>
<div class="block">Calls given callable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on calling).</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>V</code> - return type.</dd>
<dt>Parameters:</dt>
<dd><code>sessionName</code> - new session name.</dd>
<dd><code>callable</code> - callable to call.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="callInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.concurrent.Callable)">
<h3>callInsideSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;V&gt;</span> <span class="return-type">V</span> <span class="element-name">callInsideSession</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/Callable.html" title="class or interface in java.util.concurrent">Callable</a>&lt;V&gt; callable)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span></div>
<div class="block">Calls given callable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on calling).</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>V</code> - return type.</dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>sessionName</code> - new session name.</dd>
<dd><code>callable</code> - callable to call.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="supplyInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.util.function.Supplier)">
<h3>supplyInsideSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="type-parameters">&lt;V&gt;</span> <span class="return-type">V</span> <span class="element-name">supplyInsideSession</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;V&gt; supplier)</span></div>
<div class="block">Applies given supplier inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on calling).</div>
<dl class="notes">
<dt>Type Parameters:</dt>
<dd><code>V</code> - return type</dd>
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>sessionName</code> - new session name</dd>
<dd><code>supplier</code> - supplier to apply</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="executeInsideSession(com.nomagic.magicdraw.core.Project,java.lang.String,java.lang.Runnable)">
<h3>executeInsideSession</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">executeInsideSession</span><wbr/><span class="parameters">(<a href="../../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> sessionName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runnable.html" title="class or interface in java.lang">Runnable</a> runnable)</span></div>
<div class="block">Executes given runnable inside session.
 Creates new session if session is not created yet, after execution new session is closed (canceled if exception occurs on execution).</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>sessionName</code> - new session name.</dd>
<dd><code>runnable</code> - runnable to execute.</dd>
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
