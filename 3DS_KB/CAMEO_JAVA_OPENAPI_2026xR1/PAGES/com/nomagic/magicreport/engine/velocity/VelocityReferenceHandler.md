# JAVA OPENAPI: VelocityReferenceHandler (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicreport/engine/velocity/VelocityReferenceHandler.html
- source_path: `com/nomagic/magicreport/engine/velocity/VelocityReferenceHandler.html`
- source_sha256: `9b94939957f39cb80c60f027675b376eda946dc031da4edb7a0871ad94e7bbb3`
- captured_utc: `2026-07-14T16:46:13.461981+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicreport.engine.velocity](package-summary.html)

## Class VelocityReferenceHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
org.apache.velocity.app.event.implement.ReportInvalidReferences
com.nomagic.magicreport.engine.velocity.VelocityReferenceHandler

All Implemented Interfaces:
`org.apache.velocity.app.event.EventHandler`, `org.apache.velocity.app.event.InvalidReferenceEventHandler`, `org.apache.velocity.app.event.MethodExceptionEventHandler`, `org.apache.velocity.app.event.ReferenceInsertionEventHandler`, `org.apache.velocity.util.RuntimeServicesAware`

@OpenApiAllpublic classVelocityReferenceHandler
extends org.apache.velocity.app.event.implement.ReportInvalidReferences
implements org.apache.velocity.app.event.ReferenceInsertionEventHandler, org.apache.velocity.app.event.MethodExceptionEventHandler

Event handler called when an invalid reference is encountered.

Since:
Jun 18, 2007

=========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class org.apache.velocity.app.event.implement.ReportInvalidReferences
`EVENTHANDLER_INVALIDREFERENCE_EXCEPTION, OLD_EVENTHANDLER_INVALIDREFERENCE_EXCEPTION`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[VelocityReferenceHandler](#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine))([ITemplateEngine](../ITemplateEngine.html) templateEngine)`
Create the references handler.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[invalidGetMethod](#invalidGetMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info))(org.apache.velocity.context.Context context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 org.apache.velocity.util.introspection.Info info)`
Collect the error and/or throw an exception, depending on configuration.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[invalidMethod](#invalidMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info))(org.apache.velocity.context.Context context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 org.apache.velocity.util.introspection.Info info)`
Collect the error and/or throw an exception, depending on configuration.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[methodException](#methodException(java.lang.Class,java.lang.String,java.lang.Exception))([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)`
Render the method exception, and optionally the exception message and stack trace.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[methodException](#methodException(org.apache.velocity.context.Context,java.lang.Class,java.lang.String,java.lang.Exception,org.apache.velocity.util.introspection.Info))(org.apache.velocity.context.Context context,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e,
 org.apache.velocity.util.introspection.Info info)`

`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[referenceInsert](#referenceInsert(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`
A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[referenceInsert](#referenceInsert(org.apache.velocity.context.Context,java.lang.String,java.lang.Object))(org.apache.velocity.context.Context context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[setInvalidReferenceHandlerList](#setInvalidReferenceHandlerList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IInvalidReferenceHandler](../IInvalidReferenceHandler.html)> invalidReferenceHandlerList)`
Set the list of [`IInvalidReferenceHandler`](../IInvalidReferenceHandler.html).
`void`
`[setProperties](#setProperties(java.util.Properties))([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)`
Set the properties of handler.
`void`
`[setReferenceInsertionHandlerList](#setReferenceInsertionHandlerList(java.util.List))([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IReferenceInsertionHandler](../IReferenceInsertionHandler.html)> referenceInsertionHandlerList)`
Set the list of [`IReferenceInsertionHandler`](../IReferenceInsertionHandler.html).
Methods inherited from class org.apache.velocity.app.event.implement.ReportInvalidReferences
`getInvalidReferences, invalidSetMethod, setRuntimeServices`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
VelocityReferenceHandler
public VelocityReferenceHandler([ITemplateEngine](../ITemplateEngine.html) templateEngine)
Create the references handler.
Parameters:
`templateEngine` - template engine
 ============ METHOD DETAIL ========== 
Method Details
setProperties
public void setProperties([Properties](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html) properties)
Set the properties of handler. This properties is refer to
 [`ITemplateEngine.getProperty(String)`](../ITemplateEngine.html#getProperty(java.lang.String))
Parameters:
`properties` - a properties to be set
setInvalidReferenceHandlerList
public void setInvalidReferenceHandlerList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IInvalidReferenceHandler](../IInvalidReferenceHandler.html)> invalidReferenceHandlerList)
Set the list of [`IInvalidReferenceHandler`](../IInvalidReferenceHandler.html).
Parameters:
`invalidReferenceHandlerList` - a list of [`IInvalidReferenceHandler`](../IInvalidReferenceHandler.html) to be set
setReferenceInsertionHandlerList
public void setReferenceInsertionHandlerList([List](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html)<[IReferenceInsertionHandler](../IReferenceInsertionHandler.html)> referenceInsertionHandlerList)
Set the list of [`IReferenceInsertionHandler`](../IReferenceInsertionHandler.html).
Parameters:
`referenceInsertionHandlerList` - a list of [`IReferenceInsertionHandler`](../IReferenceInsertionHandler.html) to be set
invalidMethod
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) invalidMethod(org.apache.velocity.context.Context context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 org.apache.velocity.util.introspection.Info info)
Collect the error and/or throw an exception, depending on configuration.
Specified by:
`invalidMethod` in interface `org.apache.velocity.app.event.InvalidReferenceEventHandler`
Overrides:
`invalidMethod` in class `org.apache.velocity.app.event.implement.ReportInvalidReferences`
Parameters:
`context` - the context when the reference was found invalid
`reference` - complete invalid reference
`object` - the object referred to, or null if not found
`method` - the property name from the reference
`info` - contains template, line, column details
Returns:
always returns null
Throws:
`[ParseErrorException](../../ParseErrorException.html)` - error when cannot parse method
invalidGetMethod
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) invalidGetMethod(org.apache.velocity.context.Context context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) object,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) property,
 org.apache.velocity.util.introspection.Info info)
Collect the error and/or throw an exception, depending on configuration. This method will pass the input
 object into [`IInvalidReferenceHandler`](../IInvalidReferenceHandler.html) sequencely. And stop process when
 [`IInvalidReferenceHandler.invalidReference(String, Object, String, Properties)`](../IInvalidReferenceHandler.html#invalidReference(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)) return Object.
 

`for (Iterator it = invalidReferenceHandlerList.iterator(); it.hasNext();)
 {
 if ((result = invalidReferenceHandler.invalidReference(reference, object, property, properties)) != null)
 break;
 }
 return result;`
Specified by:
`invalidGetMethod` in interface `org.apache.velocity.app.event.InvalidReferenceEventHandler`
Overrides:
`invalidGetMethod` in class `org.apache.velocity.app.event.implement.ReportInvalidReferences`
Parameters:
`context` - the context when the reference was found invalid
`reference` - string with complete invalid reference
`object` - the object referred to, or null if not found
`property` - the property name from the reference
`info` - contains template, line, column details
Returns:
always returns null
referenceInsert
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) referenceInsert([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream. All registered ReferenceInsertionEventHandlers are called in sequence. If no
 ReferenceInsertionEventHandlers are are registered then reference value is inserted into the output stream
 as is. This method will pass the result of each [`IReferenceInsertionHandler`](../IReferenceInsertionHandler.html) sequencely.
 

`for (Iterator it = referenceInsertionHandlerList.iterator(); it.hasNext();)
 {
 result = referenceInsertionHandler.referenceInsert(reference, result, properties));
 }
 return result;`
Parameters:
`reference` - Reference from template about to be inserted.
`value` - Value about to be inserted (after its `toString()` method is called).
Returns:
Object on which `toString()` should be called for output.
referenceInsert
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) referenceInsert(org.apache.velocity.context.Context context,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) reference,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) value)
Specified by:
`referenceInsert` in interface `org.apache.velocity.app.event.ReferenceInsertionEventHandler`
methodException
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) methodException([Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html) clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e)
 throws [RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)
Render the method exception, and optionally the exception message and stack trace. This method always return
 `null` to keep valid reference and property pass to
 [`invalidGetMethod(org.apache.velocity.context.Context, java.lang.String, java.lang.Object, java.lang.String, org.apache.velocity.util.introspection.Info)`](#invalidGetMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info))
Parameters:
`clazz` - the class of the object the method is being applied to
`method` - the method
`e` - the thrown exception
Returns:
an `null` object.
Throws:
`[Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html)` - an exception to be thrown instead inserting an object
`[RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)`
methodException
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) methodException(org.apache.velocity.context.Context context,
 [Class](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html)<?> clazz,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) method,
 [Exception](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html) e,
 org.apache.velocity.util.introspection.Info info)
 throws [RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)
Specified by:
`methodException` in interface `org.apache.velocity.app.event.MethodExceptionEventHandler`
Throws:
`[RuntimeException](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html)`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicreport.engine.velocity</a></div>
<h1 class="title" title="Class VelocityReferenceHandler">Class VelocityReferenceHandler</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">org.apache.velocity.app.event.implement.ReportInvalidReferences
<div class="inheritance">com.nomagic.magicreport.engine.velocity.VelocityReferenceHandler</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>org.apache.velocity.app.event.EventHandler</code>, <code>org.apache.velocity.app.event.InvalidReferenceEventHandler</code>, <code>org.apache.velocity.app.event.MethodExceptionEventHandler</code>, <code>org.apache.velocity.app.event.ReferenceInsertionEventHandler</code>, <code>org.apache.velocity.util.RuntimeServicesAware</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">VelocityReferenceHandler</span>
<span class="extends-implements">extends org.apache.velocity.app.event.implement.ReportInvalidReferences
implements org.apache.velocity.app.event.ReferenceInsertionEventHandler, org.apache.velocity.app.event.MethodExceptionEventHandler</span></div>
<div class="block">Event handler called when an invalid reference is encountered.</div>
<dl class="notes">
<dt>Since:</dt>
<dd>Jun 18, 2007</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-org.apache.velocity.app.event.implement.ReportInvalidReferences">Fields inherited from class org.apache.velocity.app.event.implement.ReportInvalidReferences</h3>
<code>EVENTHANDLER_INVALIDREFERENCE_EXCEPTION, OLD_EVENTHANDLER_INVALIDREFERENCE_EXCEPTION</code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.magicreport.engine.ITemplateEngine)">VelocityReferenceHandler</a><wbr/>(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> templateEngine)</code></div>
<div class="col-last even-row-color">
<div class="block">Create the references handler.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invalidGetMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info)">invalidGetMethod</a><wbr/>(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 org.apache.velocity.util.introspection.Info info)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect the error and/or throw an exception, depending on configuration.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invalidMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info)">invalidMethod</a><wbr/>(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 org.apache.velocity.util.introspection.Info info)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collect the error and/or throw an exception, depending on configuration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#methodException(java.lang.Class,java.lang.String,java.lang.Exception)">methodException</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Render the method exception, and optionally the exception message and stack trace.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#methodException(org.apache.velocity.context.Context,java.lang.Class,java.lang.String,java.lang.Exception,org.apache.velocity.util.introspection.Info)">methodException</a><wbr/>(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 org.apache.velocity.util.introspection.Info info)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#referenceInsert(java.lang.String,java.lang.Object)">referenceInsert</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#referenceInsert(org.apache.velocity.context.Context,java.lang.String,java.lang.Object)">referenceInsert</a><wbr/>(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setInvalidReferenceHandlerList(java.util.List)">setInvalidReferenceHandlerList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a>&gt; invalidReferenceHandlerList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the list of <a href="../IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setProperties(java.util.Properties)">setProperties</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the properties of handler.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setReferenceInsertionHandlerList(java.util.List)">setReferenceInsertionHandlerList</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a>&gt; referenceInsertionHandlerList)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set the list of <a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IReferenceInsertionHandler</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-org.apache.velocity.app.event.implement.ReportInvalidReferences">Methods inherited from class org.apache.velocity.app.event.implement.ReportInvalidReferences</h3>
<code>getInvalidReferences, invalidSetMethod, setRuntimeServices</code></div>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.magicreport.engine.ITemplateEngine)">
<h3>VelocityReferenceHandler</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">VelocityReferenceHandler</span><wbr/><span class="parameters">(<a href="../ITemplateEngine.html" title="interface in com.nomagic.magicreport.engine">ITemplateEngine</a> templateEngine)</span></div>
<div class="block">Create the references handler.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>templateEngine</code> - template engine</dd>
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
<section class="detail" id="setProperties(java.util.Properties)">
<h3>setProperties</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProperties</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html" title="class or interface in java.util">Properties</a> properties)</span></div>
<div class="block">Set the properties of handler. This properties is refer to
 <a href="../ITemplateEngine.html#getProperty(java.lang.String)"><code>ITemplateEngine.getProperty(String)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - a properties to be set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInvalidReferenceHandlerList(java.util.List)">
<h3>setInvalidReferenceHandlerList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInvalidReferenceHandlerList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine">IInvalidReferenceHandler</a>&gt; invalidReferenceHandlerList)</span></div>
<div class="block">Set the list of <a href="../IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>invalidReferenceHandlerList</code> - a list of <a href="../IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> to be set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setReferenceInsertionHandlerList(java.util.List)">
<h3>setReferenceInsertionHandlerList</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setReferenceInsertionHandlerList</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine">IReferenceInsertionHandler</a>&gt; referenceInsertionHandlerList)</span></div>
<div class="block">Set the list of <a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IReferenceInsertionHandler</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>referenceInsertionHandlerList</code> - a list of <a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IReferenceInsertionHandler</code></a> to be set</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invalidMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info)">
<h3>invalidMethod</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">invalidMethod</span><wbr/><span class="parameters">(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 org.apache.velocity.util.introspection.Info info)</span></div>
<div class="block">Collect the error and/or throw an exception, depending on configuration.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>invalidMethod</code> in interface <code>org.apache.velocity.app.event.InvalidReferenceEventHandler</code></dd>
<dt>Overrides:</dt>
<dd><code>invalidMethod</code> in class <code>org.apache.velocity.app.event.implement.ReportInvalidReferences</code></dd>
<dt>Parameters:</dt>
<dd><code>context</code> - the context when the reference was found invalid</dd>
<dd><code>reference</code> - complete invalid reference</dd>
<dd><code>object</code> - the object referred to, or null if not found</dd>
<dd><code>method</code> - the property name from the reference</dd>
<dd><code>info</code> - contains template, line, column details</dd>
<dt>Returns:</dt>
<dd>always returns null</dd>
<dt>Throws:</dt>
<dd><code><a href="../../ParseErrorException.html" title="class in com.nomagic.magicreport">ParseErrorException</a></code> - error when cannot parse method</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="invalidGetMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info)">
<h3>invalidGetMethod</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">invalidGetMethod</span><wbr/><span class="parameters">(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> object,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> property,
 org.apache.velocity.util.introspection.Info info)</span></div>
<div class="block">Collect the error and/or throw an exception, depending on configuration. This method will pass the input
 object into <a href="../IInvalidReferenceHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IInvalidReferenceHandler</code></a> sequencely. And stop process when
 <a href="../IInvalidReferenceHandler.html#invalidReference(java.lang.String,java.lang.Object,java.lang.String,java.util.Properties)"><code>IInvalidReferenceHandler.invalidReference(String, Object, String, Properties)</code></a> return Object.
 <br/>
<pre><code>
 for (Iterator it = invalidReferenceHandlerList.iterator(); it.hasNext();)
 {
    if ((result = invalidReferenceHandler.invalidReference(reference, object, property, properties)) != null)
       break;
 }
 return result;
 </code></pre></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>invalidGetMethod</code> in interface <code>org.apache.velocity.app.event.InvalidReferenceEventHandler</code></dd>
<dt>Overrides:</dt>
<dd><code>invalidGetMethod</code> in class <code>org.apache.velocity.app.event.implement.ReportInvalidReferences</code></dd>
<dt>Parameters:</dt>
<dd><code>context</code> - the context when the reference was found invalid</dd>
<dd><code>reference</code> - string with complete invalid reference</dd>
<dd><code>object</code> - the object referred to, or null if not found</dd>
<dd><code>property</code> - the property name from the reference</dd>
<dd><code>info</code> - contains template, line, column details</dd>
<dt>Returns:</dt>
<dd>always returns null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="referenceInsert(java.lang.String,java.lang.Object)">
<h3>referenceInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">referenceInsert</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<div class="block">A call-back which is executed during Velocity merge before a reference value is inserted into the output
 stream. All registered ReferenceInsertionEventHandlers are called in sequence. If no
 ReferenceInsertionEventHandlers are are registered then reference value is inserted into the output stream
 as is. This method will pass the result of each <a href="../IReferenceInsertionHandler.html" title="interface in com.nomagic.magicreport.engine"><code>IReferenceInsertionHandler</code></a> sequencely.
 <br/>
<pre><code>
 for (Iterator it = referenceInsertionHandlerList.iterator(); it.hasNext();)
 {
    result = referenceInsertionHandler.referenceInsert(reference, result, properties));
 }
 return result;
 </code></pre></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>reference</code> - Reference from template about to be inserted.</dd>
<dd><code>value</code> - Value about to be inserted (after its <code>toString()</code> method is called).</dd>
<dt>Returns:</dt>
<dd>Object on which <code>toString()</code> should be called for output.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="referenceInsert(org.apache.velocity.context.Context,java.lang.String,java.lang.Object)">
<h3>referenceInsert</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">referenceInsert</span><wbr/><span class="parameters">(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> reference,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>referenceInsert</code> in interface <code>org.apache.velocity.app.event.ReferenceInsertionEventHandler</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="methodException(java.lang.Class,java.lang.String,java.lang.Exception)">
<h3>methodException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">methodException</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a> clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></span></div>
<div class="block">Render the method exception, and optionally the exception message and stack trace. This method always return
 <code>null</code> to keep valid reference and property pass to
 <a href="#invalidGetMethod(org.apache.velocity.context.Context,java.lang.String,java.lang.Object,java.lang.String,org.apache.velocity.util.introspection.Info)"><code>invalidGetMethod(org.apache.velocity.context.Context, java.lang.String, java.lang.Object, java.lang.String, org.apache.velocity.util.introspection.Info)</code></a></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>clazz</code> - the class of the object the method is being applied to</dd>
<dd><code>method</code> - the method</dd>
<dd><code>e</code> - the thrown exception</dd>
<dt>Returns:</dt>
<dd>an <code>null</code> object.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a></code> - an exception to be thrown instead inserting an object</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="methodException(org.apache.velocity.context.Context,java.lang.Class,java.lang.String,java.lang.Exception,org.apache.velocity.util.introspection.Info)">
<h3>methodException</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">methodException</span><wbr/><span class="parameters">(org.apache.velocity.context.Context context,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Class.html" title="class or interface in java.lang">Class</a>&lt;?&gt; clazz,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> method,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Exception.html" title="class or interface in java.lang">Exception</a> e,
 org.apache.velocity.util.introspection.Info info)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code>methodException</code> in interface <code>org.apache.velocity.app.event.MethodExceptionEventHandler</code></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/RuntimeException.html" title="class or interface in java.lang">RuntimeException</a></code></dd>
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
