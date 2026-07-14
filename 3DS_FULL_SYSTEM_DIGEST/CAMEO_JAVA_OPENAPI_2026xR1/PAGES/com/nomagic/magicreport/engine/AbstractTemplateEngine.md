# JAVA OPENAPI: AbstractTemplateEngine (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/AbstractTemplateEngine.html
- source_path: `com/nomagic/magicreport/engine/AbstractTemplateEngine.html`
- source_sha256: `03051228962eced64f96aecc9d3ae8a5cc76a5ee00a591cbcb788ecffb1df32d`
- captured_utc: `2026-07-14T16:46:11.801958+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine](package-summary.html)

## Class AbstractTemplateEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
com.nomagic.magicreport.engine.AbstractTemplateEngine

All Implemented Interfaces:
`com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`, `[ITemplateEngine](ITemplateEngine.html)`

Direct Known Subclasses:
`[DefaultTemplateEngine](velocity/DefaultTemplateEngine.html)`

@OpenApiAllpublic abstract classAbstractTemplateEngine
extends [Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
implements [ITemplateEngine](ITemplateEngine.html), com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine

This class provides default implementations for the [`ITemplateEngine`](ITemplateEngine.html) Action interface. Standard
 behaviors like the context and evaluate methods are defined here. The developer need only subclass this
 abstract class and define the [`preProcess(Template)`](#preProcess(com.nomagic.magicreport.Template)), [`process(Template)`](#process(com.nomagic.magicreport.Template)), and
 [`postProcess(Template)`](#postProcess(com.nomagic.magicreport.Template)) method.

Since:
Jun 11, 2007 10:45:01 PM
Version:
1.0 Jun 11, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`protected [IContext](IContext.html)`
`[context](#context)`
Current context of this engine.
`protected boolean`
`[isAborted](#isAborted)`
True if this engine is canceled.
`protected [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[preProcessFile](#preProcessFile)`
Link to the output of pre-processing file.
`protected [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)`
`[processFile](#processFile)`
Link to the output of processing file.
`protected [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[properties](#properties)`
Contains properties from this engine.
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[AbstractTemplateEngine](#%3Cinit%3E())()`
Default constructor.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract MethodsConcrete Methods
Modifier and Type
Method
Description
`void`
`[abort](#abort())()`
Called by the application to abort current evaluation context.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[addContext](#addContext(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Add a name/value pair into the context.
`void`
`[addInvalidReferenceHandler](#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler))([IInvalidReferenceHandler](IInvalidReferenceHandler.html) handler)`
Add an invalid reference event handler to the engine.
`void`
`[addObserver](#addObserver(java.util.Observer))([Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html) o)`
Adds an observer to the set of observers for this object, provided that it is not the same as some observer
 already in the set.
`void`
`[addReferenceInsertionHandler](#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler))([IReferenceInsertionHandler](IReferenceInsertionHandler.html) handler)`
Add a reference insertion event handler to the engine.
`void`
`[destroy](#destroy())()`
Called by the application or [`TemplateEngineFactory`](../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
`void`
`[evaluate](#evaluate(com.nomagic.magicreport.Template))([Template](../Template.html) template)`
Merge a template with current context and rendered stream into the writer.
`void`
`[evaluate](#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine))([Template](../Template.html) template,
 [ITemplateEngine](ITemplateEngine.html) parentEngine)`
Merge a template with current context and rendered stream into the writer.
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)`
`[getConcurrentToolException](#getConcurrentToolException())()`

`[IContext](IContext.html)`
`[getContext](#getContext())()`
Return context of this engine.
`org.apache.velocity.runtime.RuntimeInstance`
`[getCurrentRuntimeInstance](#getCurrentRuntimeInstance())()`
Get (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IInvalidReferenceHandler](IInvalidReferenceHandler.html)>`
`[getInvalidReferenceHandler](#getInvalidReferenceHandler())()`
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
`protected int`
`[getProcessSize](#getProcessSize())()`
Return a process buffered size from configuration value.
`[Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html)`
`[getProperties](#getProperties())()`
Returns the current properties of engine.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[getProperty](#getProperty(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)`
Return an engine Runtime property.
`[List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IReferenceInsertionHandler](IReferenceInsertionHandler.html)>`
`[getReferenceInsertionHandler](#getReferenceInsertionHandler())()`
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
`protected boolean`
`[isMemoryMode](#isMemoryMode(com.nomagic.magicreport.Template))([Template](../Template.html) template)`
Tests if this template should process in memory mode. 

 This method is similar to code:
`void`
`[notifyObservers](#notifyObservers(java.lang.Object))([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) event)`
Override `notifyObservers` by provide sequence of calling these methods.
`[Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html)>`
`[observers](#observers())()`
Return current observer object in this engine.
`protected abstract void`
`[postProcess](#postProcess(com.nomagic.magicreport.Template))([Template](../Template.html) template)`
Perform a post-processing after the template has been evaluated.
`protected abstract void`
`[preProcess](#preProcess(com.nomagic.magicreport.Template))([Template](../Template.html) template)`
Perform a pre-processing before evaluate the template.
`protected abstract void`
`[process](#process(com.nomagic.magicreport.Template))([Template](../Template.html) template)`
Process a template evaluation.
`protected abstract void`
`[process](#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine))([Template](../Template.html) template,
 [ITemplateEngine](ITemplateEngine.html) parentEngine)`
Process a template evaluation.
`void`
`[setConcurrentToolException](#setConcurrentToolException(java.lang.Exception))([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)`

`protected void`
`[setContext](#setContext(com.nomagic.magicreport.engine.IContext))([IContext](IContext.html) context)`
Replace current context with another context.
`void`
`[setCurrentRuntimeInstance](#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance))(org.apache.velocity.runtime.RuntimeInstance currentRuntimeInstance)`
Set current RuntimeInstance (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).
`void`
`[setProperty](#setProperty(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
Set an engine Runtime property.
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITemplateEngine](ITemplateEngine.html)
`[createTemplate](ITemplateEngine.html#createTemplate()), [createTemplate](ITemplateEngine.html#createTemplate(java.io.File,java.io.File)), [getFormatter](ITemplateEngine.html#getFormatter())`

============ FIELD DETAIL =========== 
Field Details
context
protected [IContext](IContext.html) context
Current context of this engine.
properties
protected [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties
Contains properties from this engine.
preProcessFile
protected [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) preProcessFile
Link to the output of pre-processing file. Null if engine running on [Memory] mode.
processFile
protected [File](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html) processFile
Link to the output of processing file. Null if engine running on [Memory] mode.
isAborted
protected boolean isAborted
True if this engine is canceled.
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
AbstractTemplateEngine
public AbstractTemplateEngine()
Default constructor.
 ============ METHOD DETAIL ========== 
Method Details
setContext
protected void setContext([IContext](IContext.html) context)
Replace current context with another context.
Parameters:
`context` - new context.
addContext
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) addContext([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) name,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Add a name/value pair into the context. Before calling this method, programmer must make sure that context
 has been constructed or assigned by [`setContext(IContext)`](#setContext(com.nomagic.magicreport.engine.IContext)) method.
Specified by:
`[addContext](ITemplateEngine.html#addContext(java.lang.String,java.lang.Object))` in interface `[ITemplateEngine](ITemplateEngine.html)`
Parameters:
`name` - The name to key the provided value with.
`value` - The corresponding value.
Returns:
The old value or null if there was no old value.
Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if context has not be constructed or assigned.
getContext
public [IContext](IContext.html) getContext()
Return context of this engine.
Specified by:
`[getContext](ITemplateEngine.html#getContext())` in interface `[ITemplateEngine](ITemplateEngine.html)`
Returns:
context of engine
getProperty
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) getProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key)
Return an engine Runtime property.
Specified by:
`[getProperty](ITemplateEngine.html#getProperty(java.lang.String))` in interface `[ITemplateEngine](ITemplateEngine.html)`
Parameters:
`key` - the property key
Returns:
the value in this property list with the specified key value.
See Also:
[`ITemplateEngine.setProperty(String, Object)`](ITemplateEngine.html#setProperty(java.lang.String,java.lang.Object))
setProperty
public void setProperty([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) key,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Set an engine Runtime property.
Specified by:
`[setProperty](ITemplateEngine.html#setProperty(java.lang.String,java.lang.Object))` in interface `[ITemplateEngine](ITemplateEngine.html)`
Parameters:
`key` - the key to be placed into this property list.
`value` - the value corresponding to key.
See Also:
[`ITemplateEngine.getProperty(String)`](ITemplateEngine.html#getProperty(java.lang.String))
getProperties
public [Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) getProperties()
Returns the current properties of engine.
Specified by:
`[getProperties](ITemplateEngine.html#getProperties())` in interface `[ITemplateEngine](ITemplateEngine.html)`
Returns:
the engine properties
addReferenceInsertionHandler
public void addReferenceInsertionHandler([IReferenceInsertionHandler](IReferenceInsertionHandler.html) handler)
Add a reference insertion event handler to the engine.
Specified by:
`[addReferenceInsertionHandler](ITemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler))` in interface `[ITemplateEngine](ITemplateEngine.html)`
Parameters:
`handler` - ReferenceInsertionEventHandler
addInvalidReferenceHandler
public void addInvalidReferenceHandler([IInvalidReferenceHandler](IInvalidReferenceHandler.html) handler)
Add an invalid reference event handler to the engine.
Specified by:
`[addInvalidReferenceHandler](ITemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler))` in interface `[ITemplateEngine](ITemplateEngine.html)`
Parameters:
`handler` - IInvalidReferenceHandler
getInvalidReferenceHandler
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IInvalidReferenceHandler](IInvalidReferenceHandler.html)> getInvalidReferenceHandler()
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
Specified by:
`[getInvalidReferenceHandler](ITemplateEngine.html#getInvalidReferenceHandler())` in interface `[ITemplateEngine](ITemplateEngine.html)`
Returns:
invalid reference handler for this engine.
getReferenceInsertionHandler
public [List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IReferenceInsertionHandler](IReferenceInsertionHandler.html)> getReferenceInsertionHandler()
Return a [`IInvalidReferenceHandler`](IInvalidReferenceHandler.html) of this engine.
Specified by:
`[getReferenceInsertionHandler](ITemplateEngine.html#getReferenceInsertionHandler())` in interface `[ITemplateEngine](ITemplateEngine.html)`
Returns:
reference insertion handler for this engine.
addObserver
public void addObserver([Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html) o)
Adds an observer to the set of observers for this object, provided that it is not the same as some observer
 already in the set. The order in which notifications will be delivered to multiple observers is not
 specified. See the class comment.
Overrides:
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer))` in class `[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)`
Parameters:
`o` - an observer to be added.
Throws:
`[NullPointerException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html)` - if the parameter o is null.
observers
public [Iterator](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html)<[Observer](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html)> observers()
Return current observer object in this engine.
Returns:
`Iterator` of current observer object.
notifyObservers
public void notifyObservers([Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) event)
Override `notifyObservers` by provide sequence of calling these methods. `setChanged();
 super.notifyObservers(event);`
Overrides:
`[notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers(java.lang.Object))` in class `[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)`
Parameters:
`event` - any object.
See Also:
[`Observable.clearChanged()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged())
[`Observable.hasChanged()`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged())
[`Observer.update(java.util.Observable, java.lang.Object)`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html#update(java.util.Observable,java.lang.Object))
isMemoryMode
protected boolean isMemoryMode([Template](../Template.html) template)
Tests if this template should process in memory mode. 

 This method is similar to code: `template.getSize() > properties.getProperty(TemplateConstants.TEMPLATE_PROCESS_SIZE, "0")`
Parameters:
`template` - a test Template
Returns:
true if template size is less than TEMPLATE_PROCESS_SIZE
getProcessSize
protected int getProcessSize()
Return a process buffered size from configuration value. Default is 3,145,728 bytes.
Returns:
a process buffered size
Since:
17.0.4
evaluate
public void evaluate([Template](../Template.html) template)
 throws [TemplateException](../TemplateException.html)
Merge a template with current context and rendered stream into the writer.
Specified by:
`[evaluate](ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template))` in interface `[ITemplateEngine](ITemplateEngine.html)`
Parameters:
`template` - Template being evaluated
Throws:
`[ParseErrorException](../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../TemplateException.html)` - other error while processing the template
See Also:
[`ITemplateEngine.evaluate(Template)`](ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template))
evaluate
public void evaluate([Template](../Template.html) template,
 [ITemplateEngine](ITemplateEngine.html) parentEngine)
 throws [TemplateException](../TemplateException.html)
Merge a template with current context and rendered stream into the writer.
Parameters:
`template` - Template being evaluated
`parentEngine` - an engine to shared a runtime instance for evaluate
Throws:
`[ParseErrorException](../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../TemplateException.html)` - other error while processing the template
See Also:
[`ITemplateEngine.evaluate(Template)`](ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template))
preProcess
protected abstract void preProcess([Template](../Template.html) template)
 throws [TemplateException](../TemplateException.html)
Perform a pre-processing before evaluate the template.
Parameters:
`template` - template before evaluated.
Throws:
`[ParseErrorException](../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../TemplateException.html)` - other error while processing the template
process
protected abstract void process([Template](../Template.html) template)
 throws [TemplateException](../TemplateException.html)
Process a template evaluation.
Parameters:
`template` - template being evaluated.
Throws:
`[ParseErrorException](../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../TemplateException.html)` - other error while processing the template
process
protected abstract void process([Template](../Template.html) template,
 [ITemplateEngine](ITemplateEngine.html) parentEngine)
 throws [TemplateException](../TemplateException.html)
Process a template evaluation.
Parameters:
`template` - template being evaluated.
`parentEngine` - an engine to shared a runtime instance for evaluate
Throws:
`[ParseErrorException](../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../TemplateException.html)` - other error while processing the template
postProcess
protected abstract void postProcess([Template](../Template.html) template)
 throws [TemplateException](../TemplateException.html)
Perform a post-processing after the template has been evaluated.
Parameters:
`template` - template after evaluated.
Throws:
`[ParseErrorException](../ParseErrorException.html)` - if a syntax or other error which prevents it from being
 parsed.
`[InitializationEngineException](../InitializationEngineException.html)` - error while initializing engine
`[TemplateException](../TemplateException.html)` - other error while processing the template
destroy
public void destroy()
Called by the application or [`TemplateEngineFactory`](../TemplateEngineFactory.html) to inform this engine
 that it should destroy any resources that it has allocated.
 A subclass of engine should override this method if it has any operation that it wants to perform before it
 is destroyed.
Specified by:
`[destroy](ITemplateEngine.html#destroy())` in interface `[ITemplateEngine](ITemplateEngine.html)`
abort
public void abort()
Called by the application to abort current evaluation context.
Specified by:
`[abort](ITemplateEngine.html#abort())` in interface `[ITemplateEngine](ITemplateEngine.html)`
getCurrentRuntimeInstance
public org.apache.velocity.runtime.RuntimeInstance getCurrentRuntimeInstance()
Description copied from interface: `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`
Get (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).
Specified by:
`getCurrentRuntimeInstance` in interface `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`
Returns:
current RuntimeInstance
setCurrentRuntimeInstance
public void setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance currentRuntimeInstance)
Description copied from interface: `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`
Set current RuntimeInstance (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).
Specified by:
`setCurrentRuntimeInstance` in interface `com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine`
Parameters:
`currentRuntimeInstance` - current RuntimeInstance
setConcurrentToolException
public void setConcurrentToolException([Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)
getConcurrentToolException
public [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) getConcurrentToolException()

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine</a></div>
<h1 class="title" title="Class AbstractTemplateEngine">Class AbstractTemplateEngine</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance">com.nomagic.magicreport.engine.AbstractTemplateEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code>, <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
</dl>
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="velocity/DefaultTemplateEngine.html" title="class in com.nomagic.magicreport.engine.velocity">DefaultTemplateEngine</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public abstract class </span><span class="element-name type-name-label">AbstractTemplateEngine</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a>
implements <a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a>, com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</span></div>
<div class="block">This class provides default implementations for the <a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine"><code>ITemplateEngine</code></a> Action interface. Standard
 behaviors like the context and evaluate methods are defined here. The developer need only subclass this
 abstract class and define the <a href="#preProcess(com.nomagic.magicreport.Template)"><code>preProcess(Template)</code></a>, <a href="#process(com.nomagic.magicreport.Template)"><code>process(Template)</code></a>, and
 <a href="#postProcess(com.nomagic.magicreport.Template)"><code>postProcess(Template)</code></a> method.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 11, 2007 10:45:01 PM</dd>
<dt>Version:</dt>
<dd>1.0 Jun 11, 2007</dd>
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
<div class="col-first even-row-color"><code>protected <a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#context">context</a></code></div>
<div class="col-last even-row-color">
<div class="block">Current context of this engine.</div>
</div>
<div class="col-first odd-row-color"><code>protected boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isAborted">isAborted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">True if this engine is canceled.</div>
</div>
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#preProcessFile">preProcessFile</a></code></div>
<div class="col-last even-row-color">
<div class="block">Link to the output of pre-processing file.</div>
</div>
<div class="col-first odd-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#processFile">processFile</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Link to the output of processing file.</div>
</div>
<div class="col-first even-row-color"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#properties">properties</a></code></div>
<div class="col-last even-row-color">
<div class="block">Contains properties from this engine.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">AbstractTemplateEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Default constructor.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#abort()">abort</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called by the application to abort current evaluation context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addContext(java.lang.String,java.lang.Object)">addContext</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add a name/value pair into the context.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">addInvalidReferenceHandler</a><wbr/>(<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add an invalid reference event handler to the engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addObserver(java.util.Observer)">addObserver</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds an observer to the set of observers for this object, provided that it is not the same as some observer
 already in the set.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">addReferenceInsertionHandler</a><wbr/>(<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a> handler)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add a reference insertion event handler to the engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called by the application or <a href="../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#evaluate(com.nomagic.magicreport.Template)">evaluate</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">evaluate</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConcurrentToolException()">getConcurrentToolException</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getContext()">getContext</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return context of this engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>org.apache.velocity.runtime.RuntimeInstance</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCurrentRuntimeInstance()">getCurrentRuntimeInstance</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getInvalidReferenceHandler()">getInvalidReferenceHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProcessSize()">getProcessSize</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a process buffered size from configuration value.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the current properties of engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperty(java.lang.String)">getProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return an engine Runtime property.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><wbr/>&lt;<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReferenceInsertionHandler()">getReferenceInsertionHandler</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isMemoryMode(com.nomagic.magicreport.Template)">isMemoryMode</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Tests if this template should process in memory mode.<br/>
 This method is similar to code:</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#notifyObservers(java.lang.Object)">notifyObservers</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> event)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Override <code>notifyObservers</code> by provide sequence of calling these methods.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a><wbr/>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#observers()">observers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Return current observer object in this engine.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#postProcess(com.nomagic.magicreport.Template)">postProcess</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Perform a post-processing after the template has been evaluated.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#preProcess(com.nomagic.magicreport.Template)">preProcess</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Perform a pre-processing before evaluate the template.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#process(com.nomagic.magicreport.Template)">process</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Process a template evaluation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>protected abstract void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">process</a><wbr/>(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Process a template evaluation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConcurrentToolException(java.lang.Exception)">setConcurrentToolException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a><wbr/>(<a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a> context)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replace current context with another context.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance)">setCurrentRuntimeInstance</a><wbr/>(org.apache.velocity.runtime.RuntimeInstance currentRuntimeInstance)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set current RuntimeInstance (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperty(java.lang.String,java.lang.Object)">setProperty</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set an engine Runtime property.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITemplateEngine">Methods inherited from interface com.nomagic.magicreport.engine.<a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></h3>
<code><a href="ITemplateEngine.html#createTemplate()">createTemplate</a>, <a href="ITemplateEngine.html#createTemplate(java.io.File,java.io.File)">createTemplate</a>, <a href="ITemplateEngine.html#getFormatter()">getFormatter</a></code></div>
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
<section class="detail" id="context">
<h3>context</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></span> <span class="element-name">context</span></div>
<div class="block">Current context of this engine.</div>
</section>
</li>
<li>
<section class="detail" id="properties">
<h3>properties</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">properties</span></div>
<div class="block">Contains properties from this engine.</div>
</section>
</li>
<li>
<section class="detail" id="preProcessFile">
<h3>preProcessFile</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">preProcessFile</span></div>
<div class="block">Link to the output of pre-processing file. Null if engine running on [Memory] mode.</div>
</section>
</li>
<li>
<section class="detail" id="processFile">
<h3>processFile</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html" title="class or interface in java.io">File</a></span> <span class="element-name">processFile</span></div>
<div class="block">Link to the output of processing file. Null if engine running on [Memory] mode.</div>
</section>
</li>
<li>
<section class="detail" id="isAborted">
<h3>isAborted</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isAborted</span></div>
<div class="block">True if this engine is canceled.</div>
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
<h3>AbstractTemplateEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AbstractTemplateEngine</span>()</div>
<div class="block">Default constructor.</div>
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
<section class="detail" id="setContext(com.nomagic.magicreport.engine.IContext)">
<h3>setContext</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">setContext</span><wbr/><span class="parameters">(<a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a> context)</span></div>
<div class="block">Replace current context with another context.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>context</code> - new context.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addContext(java.lang.String,java.lang.Object)">
<h3>addContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">addContext</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Add a name/value pair into the context. Before calling this method, programmer must make sure that context
 has been constructed or assigned by <a href="#setContext(com.nomagic.magicreport.engine.IContext)"><code>setContext(IContext)</code></a> method.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#addContext(java.lang.String,java.lang.Object)">addContext</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>name</code> - The name to key the provided value with.</dd>
<dd><code>value</code> - The corresponding value.</dd>
<dt>Returns:</dt>
<dd>The old value or null if there was no old value.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if context has not be constructed or assigned.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getContext()">
<h3>getContext</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="IContext.html" title="interface in com.nomagic.magicreport.engine">IContext</a></span> <span class="element-name">getContext</span>()</div>
<div class="block">Return context of this engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#getContext()">getContext</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>context of engine</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperty(java.lang.String)">
<h3>getProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key)</span></div>
<div class="block">Return an engine Runtime property.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#getProperty(java.lang.String)">getProperty</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - the property key</dd>
<dt>Returns:</dt>
<dd>the value in this property list with the specified key value.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ITemplateEngine.html#setProperty(java.lang.String,java.lang.Object)"><code>ITemplateEngine.setProperty(String, Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProperty(java.lang.String,java.lang.Object)">
<h3>setProperty</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperty</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">Set an engine Runtime property.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#setProperty(java.lang.String,java.lang.Object)">setProperty</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>key</code> - the key to be placed into this property list.</dd>
<dd><code>value</code> - the value corresponding to key.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ITemplateEngine.html#getProperty(java.lang.String)"><code>ITemplateEngine.getProperty(String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a></span> <span class="element-name">getProperties</span>()</div>
<div class="block">Returns the current properties of engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#getProperties()">getProperties</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>the engine properties</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">
<h3>addReferenceInsertionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addReferenceInsertionHandler</span><wbr/><span class="parameters">(<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a> handler)</span></div>
<div class="block">Add a reference insertion event handler to the engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#addReferenceInsertionHandler(com.nomagic.magicreport.engine.IReferenceInsertionHandler)">addReferenceInsertionHandler</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>handler</code> - ReferenceInsertionEventHandler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">
<h3>addInvalidReferenceHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addInvalidReferenceHandler</span><wbr/><span class="parameters">(<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a> handler)</span></div>
<div class="block">Add an invalid reference event handler to the engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#addInvalidReferenceHandler(com.nomagic.magicreport.engine.IInvalidReferenceHandler)">addInvalidReferenceHandler</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>handler</code> - IInvalidReferenceHandler</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getInvalidReferenceHandler()">
<h3>getInvalidReferenceHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a>&gt;</span> <span class="element-name">getInvalidReferenceHandler</span>()</div>
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#getInvalidReferenceHandler()">getInvalidReferenceHandler</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>invalid reference handler for this engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getReferenceInsertionHandler()">
<h3>getReferenceInsertionHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a>&gt;</span> <span class="element-name">getReferenceInsertionHandler</span>()</div>
<div class="block">Return a <a href="IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> of this engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#getReferenceInsertionHandler()">getReferenceInsertionHandler</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Returns:</dt>
<dd>reference insertion handler for this engine.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addObserver(java.util.Observer)">
<h3>addObserver</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addObserver</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a> o)</span></div>
<div class="block">Adds an observer to the set of observers for this object, provided that it is not the same as some observer
 already in the set. The order in which notifications will be delivered to multiple observers is not
 specified. See the class comment.</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></code></dd>
<dt>Parameters:</dt>
<dd><code>o</code> - an observer to be added.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the parameter o is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="observers()">
<h3>observers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Iterator.html" title="class or interface in java.util">Iterator</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html" title="class or interface in java.util">Observer</a>&gt;</span> <span class="element-name">observers</span>()</div>
<div class="block">Return current observer object in this engine.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><code>Iterator</code> of current observer object.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="notifyObservers(java.lang.Object)">
<h3>notifyObservers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">notifyObservers</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> event)</span></div>
<div class="block">Override <code>notifyObservers</code> by provide sequence of calling these methods. <pre><code>
 setChanged();
 super.notifyObservers(event);
 </code></pre></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers(java.lang.Object)" title="class or interface in java.util">notifyObservers</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></code></dd>
<dt>Parameters:</dt>
<dd><code>event</code> - any object.</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util"><code>Observable.clearChanged()</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util"><code>Observable.hasChanged()</code></a></li>
<li><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observer.html#update(java.util.Observable,java.lang.Object)" title="class or interface in java.util"><code>Observer.update(java.util.Observable, java.lang.Object)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMemoryMode(com.nomagic.magicreport.Template)">
<h3>isMemoryMode</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">boolean</span> <span class="element-name">isMemoryMode</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span></div>
<div class="block">Tests if this template should process in memory mode.<br/>
 This method is similar to code: <pre>
 <code>
 template.getSize() &gt; properties.getProperty(TemplateConstants.TEMPLATE_PROCESS_SIZE, "0")
 </code>
 </pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - a test Template</dd>
<dt>Returns:</dt>
<dd>true if template size is less than TEMPLATE_PROCESS_SIZE</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProcessSize()">
<h3>getProcessSize</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">int</span> <span class="element-name">getProcessSize</span>()</div>
<div class="block">Return a process buffered size from configuration value. Default is 3,145,728 bytes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>a process buffered size</dd>
<dt>Since:</dt>
<dd>17.0.4</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="evaluate(com.nomagic.magicreport.Template)">
<h3>evaluate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
              throws <span class="exceptions"><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template)">evaluate</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
<dt>Parameters:</dt>
<dd><code>template</code> - Template being evaluated</dd>
<dt>Throws:</dt>
<dd><code><a href="../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template)"><code>ITemplateEngine.evaluate(Template)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="evaluate(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>evaluate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">evaluate</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</span>
              throws <span class="exceptions"><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Merge a template with current context and rendered stream into the writer.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - Template being evaluated</dd>
<dd><code>parentEngine</code> - an engine to shared a runtime instance for evaluate</dd>
<dt>Throws:</dt>
<dd><code><a href="../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list-long">
<li><a href="ITemplateEngine.html#evaluate(com.nomagic.magicreport.Template)"><code>ITemplateEngine.evaluate(Template)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="preProcess(com.nomagic.magicreport.Template)">
<h3>preProcess</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">preProcess</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                            throws <span class="exceptions"><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Perform a pre-processing before evaluate the template.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - template before evaluated.</dd>
<dt>Throws:</dt>
<dd><code><a href="../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="process(com.nomagic.magicreport.Template)">
<h3>process</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">process</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                         throws <span class="exceptions"><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Process a template evaluation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - template being evaluated.</dd>
<dt>Throws:</dt>
<dd><code><a href="../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="process(com.nomagic.magicreport.Template,com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>process</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">process</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template,
 <a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> parentEngine)</span>
                         throws <span class="exceptions"><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Process a template evaluation.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - template being evaluated.</dd>
<dd><code>parentEngine</code> - an engine to shared a runtime instance for evaluate</dd>
<dt>Throws:</dt>
<dd><code><a href="../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="postProcess(com.nomagic.magicreport.Template)">
<h3>postProcess</h3>
<div class="member-signature"><span class="modifiers">protected abstract</span> <span class="return-type">void</span> <span class="element-name">postProcess</span><wbr/><span class="parameters">(<a href="../Template.html" title="class in com.nomagic.magicreport">Template</a> template)</span>
                             throws <span class="exceptions"><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></span></div>
<div class="block">Perform a post-processing after the template has been evaluated.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>template</code> - template after evaluated.</dd>
<dt>Throws:</dt>
<dd><code><a href="../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - if a syntax or other error which prevents it from being
            parsed.</dd>
<dd><code><a href="../InitializationEngineException.html" title="class in com.nomagic.magicreport">InitializationEngineException</a></code> - error while initializing engine</dd>
<dd><code><a href="../TemplateException.html" title="class in com.nomagic.magicreport">TemplateException</a></code> - other error while processing the template</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block">Called by the application or <a href="../TemplateEngineFactory.html" title="class in com.nomagic.magicreport"><code>TemplateEngineFactory</code></a> to inform this engine
 that it should destroy any resources that it has allocated.
 <p>
 A subclass of engine should override this method if it has any operation that it wants to perform before it
 is destroyed.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#destroy()">destroy</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="abort()">
<h3>abort</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">abort</span>()</div>
<div class="block">Called by the application to abort current evaluation context.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ITemplateEngine.html#abort()">abort</a></code> in interface <code><a href="ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentRuntimeInstance()">
<h3>getCurrentRuntimeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">org.apache.velocity.runtime.RuntimeInstance</span> <span class="element-name">getCurrentRuntimeInstance</span>()</div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code></span></div>
<div class="block">Get (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>getCurrentRuntimeInstance</code> in interface <code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code></dd>
<dt>Returns:</dt>
<dd>current RuntimeInstance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCurrentRuntimeInstance(org.apache.velocity.runtime.RuntimeInstance)">
<h3>setCurrentRuntimeInstance</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCurrentRuntimeInstance</span><wbr/><span class="parameters">(org.apache.velocity.runtime.RuntimeInstance currentRuntimeInstance)</span></div>
<div class="block"><span class="description-from-type-label">Description copied from interface: <code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code></span></div>
<div class="block">Set current RuntimeInstance (com.nomagic.magicreport.engine.velocity.ReportVelocityEngine.RuntimeInstance).</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>setCurrentRuntimeInstance</code> in interface <code>com.nomagic.magicreport.engine.IRuntimeInstanceVelocityEngine</code></dd>
<dt>Parameters:</dt>
<dd><code>currentRuntimeInstance</code> - current RuntimeInstance</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setConcurrentToolException(java.lang.Exception)">
<h3>setConcurrentToolException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConcurrentToolException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</span></div>
</section>
</li>
<li>
<section class="detail" id="getConcurrentToolException()">
<h3>getConcurrentToolException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></span> <span class="element-name">getConcurrentToolException</span>()</div>
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
