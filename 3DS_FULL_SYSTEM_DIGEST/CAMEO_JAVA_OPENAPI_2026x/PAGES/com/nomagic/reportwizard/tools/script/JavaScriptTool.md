# JAVA OPENAPI: JavaScriptTool (2026x API)

- source_url: https://jdocs.nomagic.com/2026x/com/nomagic/reportwizard/tools/script/JavaScriptTool.html
- source_path: `com/nomagic/reportwizard/tools/script/JavaScriptTool.html`
- source_sha256: `99da37fa66daa0251c2373a23a019a582048ea7c16e9d1e2ccf32ab50c1aeb20`
- captured_utc: `2026-07-14T16:58:40.718322+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.reportwizard.tools.script](package-summary.html)

## Class JavaScriptTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)
[java.util.Observable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html)
[com.nomagic.magicreport.engine.Tool](../../../magicreport/engine/Tool.html)
com.nomagic.reportwizard.tools.script.JavaScriptTool

All Implemented Interfaces:
`[ITool](../../../magicreport/engine/ITool.html)`, `[IVariable](../../../magicreport/IVariable.html)`, `[Serializable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/Serializable.html)`, `[Cloneable](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Cloneable.html)`

@OpenApiAllpublic classJavaScriptTool
extends [Tool](../../../magicreport/engine/Tool.html)

Provide functions to execute JavaScript. The JavaScript can be executed during runtime inside Velocity
 template.
 Example: 

`#foreach ($class in $Class)
 $js.eval("'Class name is ' + c.getName();", "c", $class)
 #end` The output will be: 

`Class name is A
 Class name is B
 Class name is C`
Example: 

 JS file `// declare function foo()
 function foo()
 {
 return "Foo";
 }
 // call foo method then return
 foo();`Template file`$js.execute("jsfile.js")` The output will be: `Foo`
All implicit variables such as $Class or $sorter will be automatically imported into JS Script with the same
 variable name Example: `function getSupplier()
 {
 var supplierList = new ArrayList();
 for (var i=0; i<$Dependency.size(); i++)
 {
 var dependency = $Dependency.get(i);
 supplierList.add(dependency.getSupplier());
 }
 return supplierList;
 }`
**Limitation :**
Curly braces character '{' and '}' cannot be used as JS script in RTF file. The curly braces are special
 characters use by RTF syntax. When you want to evaluate the JavaScript function, you should put the function on
 separate JS file. 

 This statement will not be executed in RTF template. The curly braces are prohibited.`$js.eval("function foo() { return "Foo"; }")`
JS script can access only implicit variables, runtime variable is not accessible. For example: `#set ($runtime = "hello world")` The `$runtime` is runtime variable. This variable
 maintain inside Velocity and it is not accessible from other class thus report engine will not able to pass
 this variable to JS. You can pass your variable into JS file by passing them on binding arguments of JSTool.
 For example: `$js.execute('jsfile.js', 'myvarname', varObj)`
 The Java Scripting reference guide:
 [http://developer.mozilla.org/en/
 Rhino_documentation](http://developer.mozilla.org/en/Rhino_documentation)
[http://java
 .sun.com/javase/6/docs/technotes/guides/scripting/programmer_guide/index.html](http://java.sun.com/javase/6/docs/technotes/guides/scripting/programmer_guide/index.html)

Since:
Sep 9, 2008
See Also:
[Serialized Form](../../../../../serialized-form.html#com.nomagic.reportwizard.tools.script.JavaScriptTool)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested classes/interfaces inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[ITool.HTMLString](../../../magicreport/engine/ITool.HTMLString.html), [ITool.RetainedString](../../../magicreport/engine/ITool.RetainedString.html), [ITool.Void](../../../magicreport/engine/ITool.Void.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final int`
`[ENGINE_SCOPE](#ENGINE_SCOPE)`
EngineScope attributes are visible during the lifetime of a single call and a set of attributes is
 maintained for each method call.
`static final int`
`[GLOBAL_SCOPE](#GLOBAL_SCOPE)`
GlobalScope attributes are visible to all method call.
Fields inherited from class com.nomagic.magicreport.engine.[Tool](../../../magicreport/engine/Tool.html)
`[context](../../../magicreport/engine/Tool.html#context), [properties](../../../magicreport/engine/Tool.html#properties)`
Fields inherited from interface com.nomagic.magicreport.engine.[ITool](../../../magicreport/engine/ITool.html)
`[VOID](../../../magicreport/engine/ITool.html#VOID)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[JavaScriptTool](#%3Cinit%3E())()`
Create a JavaScriptTool.
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[call](#call(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function)`
Call a JavaScript function.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[call](#call(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)`
Call a JavaScript function.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[call](#call(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)`
Call a JavaScript function.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[call](#call(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> bindingMap)`
Call a JavaScript function.
`void`
`[destroy](#destroy())()`
Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[eval](#eval(java.lang.String))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script)`
Evaluate the specified script.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[eval](#eval(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)`
Evaluate the script using the bindings argument.
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
Execute a file as JavaScript source.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[execute](#execute(java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)`
Execute a file as JavaScript source using the bindings argument.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[execute](#execute(java.lang.String,java.lang.String,java.lang.Object))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)`
Execute a file as JavaScript source using the bindings argument.
`[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)`
`[execute](#execute(java.lang.String,java.util.Map))([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> bindingMap)`
Execute a file as JavaScript source.
`void`
`[init](#init(int))(int scope)`
Initialize JavaScript engine.
`void`
`[init](#init(int,boolean))(int scope,
 boolean implicitImportFunction)`
Initialize JavaScript engine.
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

============ FIELD DETAIL =========== 
Field Details
GLOBAL_SCOPE
public static final int GLOBAL_SCOPE
GlobalScope attributes are visible to all method call.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.script.JavaScriptTool.GLOBAL_SCOPE)
ENGINE_SCOPE
public static final int ENGINE_SCOPE
EngineScope attributes are visible during the lifetime of a single call and a set of attributes is
 maintained for each method call.
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.reportwizard.tools.script.JavaScriptTool.ENGINE_SCOPE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
JavaScriptTool
public JavaScriptTool()
Create a JavaScriptTool. The constructor will initialize all necessary variable using in this tool. This
 constructor will be called by template engine.
 ============ METHOD DETAIL ========== 
Method Details
setShowError
public void setShowError(boolean showError)
init
public void init(int scope)
Initialize JavaScript engine. (Default mode is [`GLOBAL_SCOPE`](#GLOBAL_SCOPE))
Parameters:
`scope` - define scope of attributes.
init
public void init(int scope,
 boolean implicitImportFunction)
Initialize JavaScript engine. The `scope` defines the scope of JS code. The
 `implicitImportFunction` allow you to use `importPackage()` and
 `importClass()` inside the JS file. The `importPackage` and `importClass`
 functions "pollute" the global variable scope of JavaScript. To avoid that, you may turn this option and use
 `JavaImporter`.
Parameters:
`scope` - define scope of attributes.
`implicitImportFunction` - true if you want to uses built-in functions importPackage and importClass
 (Default is `true`).
eval
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eval([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script)
Evaluate the specified script.
 For example: `$js.eval("context.put('var', 'hello world')")
 And the var value is $var` The output will be: `hello world
 And the var value is hello world`
Parameters:
`script` - the script language source to be executed.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
eval
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eval([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Evaluate the script using the bindings argument. The "importer" name will be used as an binding name for
 this argument.
Parameters:
`script` - the script language source to be executed.
`bindingObject` - the bindings of attribute object to be used for script execution.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
eval
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) eval([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) script,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Evaluate the script using the bindings argument.
 For example: `#foreach ($class in $Class)
 $js.eval("'Class name is ' + c.getName();", "c", $class)
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
 $js.eval("'Name is ' + name1 + ' ' + name2;", $map)` The output will be: `Name is foo bar`
Parameters:
`script` - the script language source to be executed.
`bindingMap` - the key-value pairs for binding name and binding object.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
execute
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName)
Execute a file as JavaScript source. All characters of the reader are consumed.
 For example: `$js.execute("script.js")`Or `$js.execute("c:/myfolder/script.js")`
Parameters:
`fileName` - the source of the script.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
execute
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Execute a file as JavaScript source using the bindings argument. The "importer" name will be used as an
 binding name for this argument. All characters from the file are consumed.
Parameters:
`fileName` - the source of the script.
`bindingObject` - the bindings of attribute object to be used for script execution.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
execute
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) execute([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) fileName,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Execute a file as JavaScript source using the bindings argument. All characters from the file are consumed.
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
Execute a file as JavaScript source. The binding map consists of key-value pairs for binding name and
 binding object. All characters from the file are consumed.
Parameters:
`fileName` - the source of the script.
`bindingMap` - the key-value pairs for binding name and binding object.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
call
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) call([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function)
Call a JavaScript function.
 For example: `$js.eval("function calc(var1, var2) { return var1 + var2; }")
 $js.call("calc(1, 3)")`
Parameters:
`function` - the JavaScript function
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
call
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) call([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Call a JavaScript function. The "importer" name will be used as an binding name for this argument.
Parameters:
`function` - the JavaScript function
`bindingObject` - the bindings of attribute object to be used for script execution.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
call
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) call([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function,
 [String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) bindingName,
 [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) bindingObject)
Call a JavaScript function. The function must be defined before calling this method. Function can be defined
 either by method `eval` or `execute`. The binding object will be pass as context
 variable under binding name.
 For example: `$js.eval("function calc(var1, var2) { var f = factor ? factor : 0; return f + var1 + var2; }")
 $js.call("calc(1, 3)", "factor", 10)` **Note :** The curly braces character '{' and '}' is not allowed to uses in RTF template.
 This curly braces is special characters uses by RTF syntax.
Parameters:
`function` - the JavaScript function
`bindingName` - the name being used with binding object.
`bindingObject` - the bindings of attribute object to be used for script execution.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
call
public [Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html) call([String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) function,
 [Map](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html)<[String](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html),[Object](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html)> bindingMap)
Call a JavaScript function. The function must be defined before calling this method. Function can be defined
 either by method `eval` or `execute`. The binding map consists of key-value pairs for
 binding name and binding object.
Parameters:
`function` - the JavaScript function
`bindingMap` - the key-value pairs for binding name and binding object.
Returns:
the value returned from the execution of the script or `ITool.VOID` if return value is
 `null`
destroy
public void destroy()
Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.reportwizard.tools.script</a></div>
<h1 class="title" title="Class JavaScriptTool">Class JavaScriptTool</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Observable.html" title="class or interface in java.util">java.util.Observable</a>
<div class="inheritance"><a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">com.nomagic.magicreport.engine.Tool</a>
<div class="inheritance">com.nomagic.reportwizard.tools.script.JavaScriptTool</div>
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
</span><span class="modifiers">public class </span><span class="element-name type-name-label">JavaScriptTool</span>
<span class="extends-implements">extends <a href="../../../magicreport/engine/Tool.html" title="class in com.nomagic.magicreport.engine">Tool</a></span></div>
<div class="block">Provide functions to execute JavaScript. The JavaScript can be executed during runtime inside Velocity
 template.
 <p>
 Example: <br/>
<code><pre>
    #foreach ($class in $Class)
    $js.eval("'Class name is ' + c.getName();", "c", $class)
    #end</pre></code> The output will be: <br/>
<code><pre>
    Class name is A
    Class name is B
    Class name is C</pre></code>
<p>
 Example: <br/>
 JS file <code><pre>
    // declare function foo()
    function foo()
    {
       return "Foo";
    }
    // call foo method then return
    foo();
 </pre></code>Template file<code><pre>
    $js.execute("jsfile.js")</pre></code> The output will be: <code><pre>
    Foo</pre></code>
<p>
 All implicit variables such as $Class or $sorter will be automatically imported into JS Script with the same
 variable name Example: <code><pre>
    function getSupplier()
    {
       var supplierList = new ArrayList();
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
<li>Curly braces character '{' and '}' cannot be used as JS script in RTF file. The curly braces are special
 characters use by RTF syntax. When you want to evaluate the JavaScript function, you should put the function on
 separate JS file. <br/>
 This statement will not be executed in RTF template. The curly braces are prohibited.<code><pre>
 $js.eval("function foo() { return "Foo"; }")</pre></code></li>
<li>JS script can access only implicit variables, runtime variable is not accessible. For example: <code><pre>
 #set ($runtime = "hello world")</pre></code> The <code>$runtime</code> is runtime variable. This variable
 maintain inside Velocity and it is not accessible from other class thus report engine will not able to pass
 this variable to JS. You can pass your variable into JS file by passing them on binding arguments of JSTool.
 For example: <code><pre>
 $js.execute('jsfile.js', 'myvarname', varObj)
 </pre></code></li>
</ol>
 The Java Scripting reference guide:
 <ul>
<li><a href="http://developer.mozilla.org/en/Rhino_documentation">http://developer.mozilla.org/en/
 Rhino_documentation</a></li>
<li><a href="http://java.sun.com/javase/6/docs/technotes/guides/scripting/programmer_guide/index.html">http://java
 .sun.com/javase/6/docs/technotes/guides/scripting/programmer_guide/index.html</a></li>
</ul></p></p></p></p></div>
<dl class="notes">
<dt>Since:</dt>
<dd>Sep 9, 2008</dd>
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../serialized-form.html#com.nomagic.reportwizard.tools.script.JavaScriptTool">Serialized Form</a></li>
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
<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ENGINE_SCOPE">ENGINE_SCOPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">EngineScope attributes are visible during the lifetime of a single call and a set of attributes is
 maintained for each method call.</div>
</div>
<div class="col-first odd-row-color"><code>static final int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#GLOBAL_SCOPE">GLOBAL_SCOPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">GlobalScope attributes are visible to all method call.</div>
</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">JavaScriptTool</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Create a JavaScriptTool.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#call(java.lang.String)">call</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call a JavaScript function.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#call(java.lang.String,java.lang.Object)">call</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call a JavaScript function.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#call(java.lang.String,java.lang.String,java.lang.Object)">call</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bindingName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call a JavaScript function.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#call(java.lang.String,java.util.Map)">call</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; bindingMap)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Call a JavaScript function.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#destroy()">destroy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eval(java.lang.String)">eval</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Evaluate the specified script.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#eval(java.lang.String,java.lang.Object)">eval</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Evaluate the script using the bindings argument.</div>
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
<div class="block">Execute a file as JavaScript source.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.Object)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute a file as JavaScript source using the bindings argument.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.lang.String,java.lang.Object)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bindingName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute a file as JavaScript source using the bindings argument.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#execute(java.lang.String,java.util.Map)">execute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; bindingMap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Execute a file as JavaScript source.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(int)">init</a><wbr/>(int scope)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize JavaScript engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#init(int,boolean)">init</a><wbr/>(int scope,
 boolean implicitImportFunction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Initialize JavaScript engine.</div>
</div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="GLOBAL_SCOPE">
<h3>GLOBAL_SCOPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">GLOBAL_SCOPE</span></div>
<div class="block">GlobalScope attributes are visible to all method call.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.script.JavaScriptTool.GLOBAL_SCOPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENGINE_SCOPE">
<h3>ENGINE_SCOPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type">int</span> <span class="element-name">ENGINE_SCOPE</span></div>
<div class="block">EngineScope attributes are visible during the lifetime of a single call and a set of attributes is
 maintained for each method call.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="tag-list">
<li><a href="../../../../../constant-values.html#com.nomagic.reportwizard.tools.script.JavaScriptTool.ENGINE_SCOPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<h3>JavaScriptTool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">JavaScriptTool</span>()</div>
<div class="block">Create a JavaScriptTool. The constructor will initialize all necessary variable using in this tool. This
 constructor will be called by template engine.</div>
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
<section class="detail" id="init(int)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(int scope)</span></div>
<div class="block">Initialize JavaScript engine. (Default mode is <a href="#GLOBAL_SCOPE"><code>GLOBAL_SCOPE</code></a>)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scope</code> - define scope of attributes.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="init(int,boolean)">
<h3>init</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">init</span><wbr/><span class="parameters">(int scope,
 boolean implicitImportFunction)</span></div>
<div class="block">Initialize JavaScript engine. The <code>scope</code> defines the scope of JS code. The
 <code>implicitImportFunction</code> allow you to use <code>importPackage()</code> and
 <code>importClass()</code> inside the JS file. The <code>importPackage</code> and <code>importClass</code>
 functions "pollute" the global variable scope of JavaScript. To avoid that, you may turn this option and use
 <code>JavaImporter</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scope</code> - define scope of attributes.</dd>
<dd><code>implicitImportFunction</code> - true if you want to uses built-in functions importPackage and importClass
           (Default is <code>true</code>).</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="eval(java.lang.String)">
<h3>eval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">eval</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script)</span></div>
<div class="block">Evaluate the specified script.
 <p>
 For example: <code><pre>
    $js.eval("context.put('var', 'hello world')")
    And the var value is $var
 </pre></code> The output will be: <code><pre>
    hello world
    And the var value is hello world
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
<section class="detail" id="eval(java.lang.String,java.lang.Object)">
<h3>eval</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">eval</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> script,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</span></div>
<div class="block">Evaluate the script using the bindings argument. The "importer" name will be used as an binding name for
 this argument.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>script</code> - the script language source to be executed.</dd>
<dd><code>bindingObject</code> - the bindings of attribute object to be used for script execution.</dd>
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
    $js.eval("'Class name is ' + c.getName();", "c", $class)
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
    $js.eval("'Name is ' + name1 + ' ' + name2;", $map)
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
<div class="block">Execute a file as JavaScript source. All characters of the reader are consumed.
 <p>
 For example: <code><pre>
    $js.execute("script.js")
 </pre></code>Or <code><pre>
    $js.execute("c:/myfolder/script.js")
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
<section class="detail" id="execute(java.lang.String,java.lang.Object)">
<h3>execute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">execute</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> fileName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</span></div>
<div class="block">Execute a file as JavaScript source using the bindings argument. The "importer" name will be used as an
 binding name for this argument. All characters from the file are consumed.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileName</code> - the source of the script.</dd>
<dd><code>bindingObject</code> - the bindings of attribute object to be used for script execution.</dd>
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
<div class="block">Execute a file as JavaScript source using the bindings argument. All characters from the file are consumed.</div>
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
<div class="block">Execute a file as JavaScript source. The binding map consists of key-value pairs for binding name and
 binding object. All characters from the file are consumed.</div>
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
<li>
<section class="detail" id="call(java.lang.String)">
<h3>call</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">call</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function)</span></div>
<div class="block">Call a JavaScript function.
 <p>
 For example: <code><pre>
    $js.eval("function calc(var1, var2) { return var1 + var2; }")
    $js.call("calc(1, 3)")
 </pre></code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>function</code> - the JavaScript function</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="call(java.lang.String,java.lang.Object)">
<h3>call</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">call</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</span></div>
<div class="block">Call a JavaScript function. The "importer" name will be used as an binding name for this argument.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>function</code> - the JavaScript function</dd>
<dd><code>bindingObject</code> - the bindings of attribute object to be used for script execution.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="call(java.lang.String,java.lang.String,java.lang.Object)">
<h3>call</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">call</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> bindingName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> bindingObject)</span></div>
<div class="block">Call a JavaScript function. The function must be defined before calling this method. Function can be defined
 either by method <code>eval</code> or <code>execute</code>. The binding object will be pass as context
 variable under binding name.
 <p>
 For example: <code><pre>
    $js.eval("function calc(var1, var2) { var f = factor ? factor : 0; return f + var1 + var2; }")
    $js.call("calc(1, 3)", "factor", 10)
 </pre></code> <b>Note : </b> The curly braces character '{' and '}' is not allowed to uses in RTF template.
 This curly braces is special characters uses by RTF syntax.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>function</code> - the JavaScript function</dd>
<dd><code>bindingName</code> - the name being used with binding object.</dd>
<dd><code>bindingObject</code> - the bindings of attribute object to be used for script execution.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="call(java.lang.String,java.util.Map)">
<h3>call</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">call</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> function,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>&gt; bindingMap)</span></div>
<div class="block">Call a JavaScript function. The function must be defined before calling this method. Function can be defined
 either by method <code>eval</code> or <code>execute</code>. The binding map consists of key-value pairs for
 binding name and binding object.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>function</code> - the JavaScript function</dd>
<dd><code>bindingMap</code> - the key-value pairs for binding name and binding object.</dd>
<dt>Returns:</dt>
<dd>the value returned from the execution of the script or <code>ITool.VOID</code> if return value is
         <code>null</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="destroy()">
<h3>destroy</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()</div>
<div class="block">Called by the engine to inform this tool is no longer use and that it should destroy any resources that it
 has allocated.</div>
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
