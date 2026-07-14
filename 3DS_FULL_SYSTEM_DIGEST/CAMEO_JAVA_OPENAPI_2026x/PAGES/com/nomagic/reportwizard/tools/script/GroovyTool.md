# JAVA OPENAPI: GroovyTool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/script/GroovyTool.html
- source_path: `com/nomagic/reportwizard/tools/script/GroovyTool.html`
- source_sha256: `a64e1f83faeeb50f3b5cef4130529388cd757a26b640a9d5cd53a124cc34c53a`
- captured_utc: `2026-07-14T16:58:40.677321+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.script](package-summary.html)

## Class GroovyTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../../magicreport/engine/Tool.html)
com.nomagic.reportwizard.tools.script.GroovyTool

All Implemented Interfaces:
`[ITool](../../../magicreport/engine/ITool.html)`, `[IVariable](../../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classGroovyTool
extends [Tool](../../../magicreport/engine/Tool.html)

Provide functions to execute Groovy script. The script will be executed during runtime with Velocity template.
 Example: 

`#import ('groovy', 'com.nomagic.reportwizard.tools.script.GroovyTool')
 #foreach ($class in $Class)
 $groovy.eval("'Class name is ' + c.getName();", "c", $class)
 #end` The output will be: 

`Class name is A
 Class name is B
 Class name is C`
Example: 

 Groovy file "Text.groovy"`def toCap(word) {
 println 'toCap $word'
 return word[0].toUpperCase() + word[1..-1] 
 }`Template file`$groovy.execute("Text.groovy")
 #foreach ($c in $Class)
 $groovy.eval('new Text().toCap('+$c.name+')');
 #end`If the $Class contains class name 'foo' and 'bar'. The output will be: `Foo
 Bar`
All implicit variables such as $Class or $sorter will be automatically imported into JS Script with the same
 variable name Example: `def getSupplier()
 {
 def supplierList = [];
 for (var i=0; i<$Dependency.size(); i++)
 {
 var dependency = $Dependency.get(i);
 supplierList.add(dependency.getSupplier());
 }
 return supplierList;
 }`
**Limitation :**
Curly braces character '{' and '}' cannot be used in eval() function in RTF file. The curly braces are
 special characters use by RTF syntax. When you want to evaluate the Groovy function, you should put the
 function on separate groovy file. 

 For example: this statement will not be executed in RTF template. The curly braces are prohibited.`$groovy.eval("def foo() { return "Foo"; }")`
**The Groovy reference guide:**
[http://groovy.codehaus.org/](http://groovy.codehaus.org/)

Since:
Mar 16, 2010
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.reportwizard.tools.script.GroovyTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[context](../../../magicreport/engine/Tool.html#context), [properties](../../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[VOID](../../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[GroovyTool](#%3Cinit%3E())()`
Create a GroovyTool.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[eval](#eval(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script)`
Evaluate the specified script.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[eval](#eval(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)`
Evaluate the script using the bindings argument.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[eval](#eval(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> bindingMap)`
Evaluate the script using the set of bindings argument.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[execute](#execute(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName)`
Execute a file as Groovy source.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[execute](#execute(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)`
Execute a file as Groovy source using the bindings argument.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[execute](#execute(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> bindingMap)`
Execute a file as Groovy source.
`void`
`[setLoaderMode](#setLoaderMode(int))(int loaderMode)`

`void`
`[setShowError](#setShowError(boolean))(boolean showError)`
Methods inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[clone](../../../magicreport/engine/Tool.html#clone()), [getContext](../../../magicreport/engine/Tool.html#getContext()), [getProperties](../../../magicreport/engine/Tool.html#getProperties()), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String)), [getProperty](../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)), [notifyObservers](../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)), [setContext](../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)), [setProperties](../../../magicreport/engine/Tool.html#setProperties(java.util.Properties))`
Methods inherited from class java.util.[Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
`[addObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)), [clearChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()), [countObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()), [deleteObserver](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)), [deleteObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()), [hasChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()), [notifyObservers](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()), [setChanged](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged())`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
`[equals](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[clearTool](../../../magicreport/engine/ITool.html#clearTool())`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
GroovyTool
public GroovyTool()
Create a GroovyTool.
 ============ METHOD DETAIL ========== 
Method Details
setShowError
public void setShowError(boolean showError)
setLoaderMode
public void setLoaderMode(int loaderMode)
eval
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eval([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script)
Evaluate the specified script.
 For example: `$groovy.eval("println 'Hello World!'; x = 123; return x * 10")` The output will be: 

 [on message view]`Hello World!`[on output report]`1230`
Parameters:
`script` - the script language source to be executed.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
eval
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eval([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Evaluate the script using the bindings argument.
 For example: `#foreach ($class in $Class)
 $groovy.eval("'Class name is ' + c.getName();", "c", $class)
 #end` The output will be: `Class name is A
 Class name is B
 Class name is C`
Parameters:
`script` - the script language source to be executed.
`bindingName` - the name being used with binding object.
`bindingObject` - the bindings of attribute object to be used for script execution.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
eval
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eval([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> bindingMap)
Evaluate the script using the set of bindings argument. The binding map consists of key-value pairs for
 binding name and binding object.
 For example: `#set ($map = $map.createHashMap())
 #set ($void = $map.put("name1", "foo"))
 #set ($void = $map.put("name2", "bar"))
 $groovy.eval("'Name is ' + name1 + ' ' + name2;", $map)` The output will be: `Name is foo bar` For example: `$groovy.eval("'Name is ' + name1 + ' ' + name2;", {"name1":"foo","name2":"bar"})` The output will be: `Name is foo bar`
Parameters:
`script` - the script language source to be executed.
`bindingMap` - the key-value pairs for binding name and binding object.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
execute
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName)
Execute a file as Groovy source. All characters of the reader are consumed.
 For example: `$groovy.execute("script.groovy")`Or `$groovy.execute("c:/myfolder/script.groovy")`
Parameters:
`fileName` - the source of the script.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
execute
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Execute a file as Groovy source using the bindings argument. All characters from the file are consumed.
Parameters:
`fileName` - the source of the script.
`bindingName` - the name being used with binding object.
`bindingObject` - the bindings of attribute object to be used for script execution.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
execute
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> bindingMap)
Execute a file as Groovy source. The binding map consists of key-value pairs for binding name and binding
 object. All characters from the file are consumed.
Parameters:
`fileName` - the source of the script.
`bindingMap` - the key-value pairs for binding name and binding object.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.script</a></div>
<h1 class="title" title="Class GroovyTool">Class GroovyTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.script.GroovyTool</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></code>, <code><a href="../../../magicreport/IVariable.html" title="interface in com.nomagic.magicreport">IVariable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html" title="class or interface in java.lang">Cloneable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">GroovyTool</span>
<span class="extends-implements">extends <a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">Provide functions to execute Groovy script. The script will be executed during runtime with Velocity template.
 <p>
 Example: <br/>
<code><pre>
    #import ('groovy', 'com.nomagic.reportwizard.tools.script.GroovyTool')
    #foreach ($class in $Class)
       $groovy.eval("'Class name is ' + c.getName();", "c", $class)
    #end</pre></code> The output will be: <br/>
<code><pre>
    Class name is A
    Class name is B
    Class name is C</pre></code>
<p>
 Example: <br/>
 Groovy file "Text.groovy"<code><pre>
    def toCap(word) {
       println 'toCap $word'
       return word[0].toUpperCase() + word[1..-1] 
    }
 </pre></code>Template file<code><pre>
    $groovy.execute("Text.groovy")
    #foreach ($c in $Class)
       $groovy.eval('new Text().toCap('+$c.name+')');
    #end
    </pre></code>If the $Class contains class name 'foo' and 'bar'. The output will be: <code><pre>
    Foo
    Bar</pre></code>
<p>
 All implicit variables such as $Class or $sorter will be automatically imported into JS Script with the same
 variable name Example: <code><pre>
    def getSupplier()
    {
       def supplierList = [];
       for (var i=0; i&lt;$Dependency.size(); i++)
       {
          var dependency = $Dependency.get(i);
          supplierList.add(dependency.getSupplier());
       }
       return supplierList;
    }</pre></code>
<p>
<b>Limitation : </b>
<ol>
<li>Curly braces character '{' and '}' cannot be used in eval() function in RTF file. The curly braces are
 special characters use by RTF syntax. When you want to evaluate the Groovy function, you should put the
 function on separate groovy file. <br/>
 For example: this statement will not be executed in RTF template. The curly braces are prohibited.<code><pre>
 $groovy.eval("def foo() { return "Foo"; }")</pre></code></li>
</ol>
<b>The Groovy reference guide:</b>
<ul>
<li><a href="http://groovy.codehaus.org/">http://groovy.codehaus.org/</a></li>
</ul></p></p></p></p></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Mar 16, 2010</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.reportwizard.tools.script.GroovyTool">Serialized Form</a></li>
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
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.magicreport.engine.ITool">Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h2>
<code><a href="../../../magicreport/engine/ITool.HTMLString.html" title="class in com.nomagic.magicreport.engine">ITool.HTMLString</a>, <a href="../../../magicreport/engine/ITool.RetainedString.html" title="class in com.nomagic.magicreport.engine">ITool.RetainedString</a>, <a href="../../../magicreport/engine/ITool.Void.html" title="class in com.nomagic.magicreport.engine">ITool.Void</a></code></div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">
<h2>Field Summary</h2>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.Tool">Fields inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#context">context</a>, <a href="../../../magicreport/engine/Tool.html#properties">properties</a></code></div>
<div class="inherited-list">
<h3 id="fields-inherited-from-class-com.nomagic.magicreport.engine.ITool">Fields inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#VOID">VOID</a></code></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">GroovyTool</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create a GroovyTool.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eval(java.lang.String)">eval</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Evaluate the specified script.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eval(java.lang.String,java.lang.String,java.lang.Object)">eval</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bindingName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Evaluate the script using the bindings argument.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eval(java.lang.String,java.util.Map)">eval</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; bindingMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Evaluate the script using the set of bindings argument.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute a file as Groovy source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.String,java.lang.Object)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bindingName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute a file as Groovy source using the bindings argument.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.util.Map)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; bindingMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute a file as Groovy source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLoaderMode(int)">setLoaderMode</a><wbr/>(int loaderMode)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setShowError(boolean)">setShowError</a><wbr/>(boolean showError)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.Tool">Methods inherited from class com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></h3>
<code><a href="../../../magicreport/engine/Tool.html#clone()">clone</a>, <a href="../../../magicreport/engine/Tool.html#getContext()">getContext</a>, <a href="../../../magicreport/engine/Tool.html#getProperties()">getProperties</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#getProperty(java.lang.String,java.lang.String)">getProperty</a>, <a href="../../../magicreport/engine/Tool.html#notifyObservers(java.lang.Object)">notifyObservers</a>, <a href="../../../magicreport/engine/Tool.html#setContext(com.nomagic.magicreport.engine.IContext)">setContext</a>, <a href="../../../magicreport/engine/Tool.html#setProperties(java.util.Properties)">setProperties</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.util.Observable">Methods inherited from class java.util.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">Observable</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#addObserver(java.util.Observer)" title="class or interface in java.util">addObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#clearChanged()" title="class or interface in java.util">clearChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#countObservers()" title="class or interface in java.util">countObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObserver(java.util.Observer)" title="class or interface in java.util">deleteObserver</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#deleteObservers()" title="class or interface in java.util">deleteObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#hasChanged()" title="class or interface in java.util">hasChanged</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#notifyObservers()" title="class or interface in java.util">notifyObservers</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html#setChanged()" title="class or interface in java.util">setChanged</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicreport.engine.ITool">Methods inherited from interface com.nomagic.magicreport.engine.<a href="../../../magicreport/engine/ITool.html" title="interface in com.nomagic.magicreport.engine">ITool</a></h3>
<code><a href="../../../magicreport/engine/ITool.html#clearTool()">clearTool</a></code></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>GroovyTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GroovyTool</span>()</div>
<div class="block">Create a GroovyTool.</div>
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
<section class="detail" id="setShowError(boolean)">
<h3>setShowError</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setShowError</span><wbr/><span class="parameters">(boolean showError)</span></div>
</section>
</li>
<li>
<section class="detail" id="setLoaderMode(int)">
<h3>setLoaderMode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setLoaderMode</span><wbr/><span class="parameters">(int loaderMode)</span></div>
</section>
</li>
<li>
<section class="detail" id="eval(java.lang.String)">
<h3>eval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">eval</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script)</span></div>
<div class="block">Evaluate the specified script.
 <p>
 For example: <code><pre>
    $groovy.eval("println 'Hello World!'; x = 123; return x * 10")
 </pre></code> The output will be: <br/>
 [on message view]<code><pre>
    Hello World!
 </pre></code>[on output report]<code><pre>
    1230
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>script</code> - the script language source to be executed.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eval(java.lang.String,java.lang.String,java.lang.Object)">
<h3>eval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">eval</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bindingName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</span></div>
<div class="block">Evaluate the script using the bindings argument.
 <p>
 For example: <code><pre>
    #foreach ($class in $Class)
       $groovy.eval("'Class name is ' + c.getName();", "c", $class)
    #end
 </pre></code> The output will be: <code><pre>
    Class name is A
    Class name is B
    Class name is C
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>script</code> - the script language source to be executed.</dd>
<dd><code>bindingName</code> - the name being used with binding object.</dd>
<dd><code>bindingObject</code> - the bindings of attribute object to be used for script execution.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eval(java.lang.String,java.util.Map)">
<h3>eval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">eval</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; bindingMap)</span></div>
<div class="block">Evaluate the script using the set of bindings argument. The binding map consists of key-value pairs for
 binding name and binding object.
 <p>
 For example: <code><pre>
    #set ($map = $map.createHashMap())
    #set ($void = $map.put("name1", "foo"))
    #set ($void = $map.put("name2", "bar"))
    $groovy.eval("'Name is ' + name1 + ' ' + name2;", $map)
 </pre></code> The output will be: <code><pre>
    Name is foo bar
 </pre></code> For example: <code><pre>
    $groovy.eval("'Name is ' + name1 + ' ' + name2;", {"name1":"foo","name2":"bar"})
 </pre></code> The output will be: <code><pre>
    Name is foo bar
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>script</code> - the script language source to be executed.</dd>
<dd><code>bindingMap</code> - the key-value pairs for binding name and binding object.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName)</span></div>
<div class="block">Execute a file as Groovy source. All characters of the reader are consumed.
 <p>
 For example: <code><pre>
    $groovy.execute("script.groovy")
 </pre></code>Or <code><pre>
    $groovy.execute("c:/myfolder/script.groovy")
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the source of the script.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String,java.lang.String,java.lang.Object)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bindingName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</span></div>
<div class="block">Execute a file as Groovy source using the bindings argument. All characters from the file are consumed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the source of the script.</dd>
<dd><code>bindingName</code> - the name being used with binding object.</dd>
<dd><code>bindingObject</code> - the bindings of attribute object to be used for script execution.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="execute(java.lang.String,java.util.Map)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; bindingMap)</span></div>
<div class="block">Execute a file as Groovy source. The binding map consists of key-value pairs for binding name and binding
 object. All characters from the file are consumed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the source of the script.</dd>
<dd><code>bindingMap</code> - the key-value pairs for binding name and binding object.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
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
