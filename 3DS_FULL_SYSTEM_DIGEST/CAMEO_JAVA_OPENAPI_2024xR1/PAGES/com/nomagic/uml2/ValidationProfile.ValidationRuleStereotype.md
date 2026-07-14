# JAVA OPENAPI: ValidationProfile.ValidationRuleStereotype (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/uml2/ValidationProfile.ValidationRuleStereotype.html
- source_path: `com/nomagic/uml2/ValidationProfile.ValidationRuleStereotype.html`
- source_sha256: `e6c698e9a2623d77d65fc60f3db5ef46343918aa633bed862ac48717e49a081b`
- captured_utc: `2026-07-14T16:52:38.594233+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2](package-summary.html)

## Class ValidationProfile.ValidationRuleStereotype

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)
com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype

Enclosing class:
[ValidationProfile](ValidationProfile.html)

public static classValidationProfile.ValidationRuleStereotype
extends [ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ABBREVIATION](#ABBREVIATION)`
Specify a short word, phrase, or acronym of the validation rule.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[CONSTRAINEDELEMENTSFILTER](#CONSTRAINEDELEMENTSFILTER)`
Specify the condition that must be met in order to validate Constrained Elements.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ERRORMESSAGE](#ERRORMESSAGE)`
Describe the invalid situation when validation rule fails.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[IMPLEMENTATION](#IMPLEMENTATION)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PARENTOBJECT](#PARENTOBJECT)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PARENTRULE](#PARENTRULE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SEVERITY](#SEVERITY)`
Select the severity kind of the validation rule: debug, info, warning, error, fatal.
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[STEREOTYPE_NAME](#STEREOTYPE_NAME)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Modifier
Constructor
Description
`protected`
`[ValidationRuleStereotype](#%3Cinit%3E(com.nomagic.uml2.ValidationProfile))([ValidationProfile](ValidationProfile.html) profile)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete Methods
Modifier and Type
Method
Description
`protected void`
`[clear](#clear())()`

`void`
`[clearAbbreviation](#clearAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearConstrainedElementsFilter](#clearConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearErrorMessage](#clearErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearImplementation](#clearImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearParentObject](#clearParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearParentRule](#clearParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[clearSeverity](#clearSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getAbbreviation](#getAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getAbbreviationProperty](#getAbbreviationProperty())()`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getConstrainedElementsFilter](#getConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getConstrainedElementsFilterProperty](#getConstrainedElementsFilterProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getErrorMessage](#getErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getErrorMessageProperty](#getErrorMessageProperty())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getImplementation](#getImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getImplementationProperty](#getImplementationProperty())()`

`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)`
`[getParentObject](#getParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getParentObjectProperty](#getParentObjectProperty())()`

`[Element](ext/magicdraw/classes/mdkernel/Element.html)`
`[getParentRule](#getParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getParentRuleProperty](#getParentRuleProperty())()`

`[ValidationProfile.SeverityKindEnum](ValidationProfile.SeverityKindEnum.html)`
`[getSeverity](#getSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`[Property](ext/magicdraw/classes/mdkernel/Property.html)`
`[getSeverityProperty](#getSeverityProperty())()`

`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getStereotype](#getStereotype())()`
Returns stereotype for this wrapper.
`boolean`
`[is](#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`static boolean`
`[isInstance](#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`

`void`
`[setAbbreviation](#setAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setConstrainedElementsFilter](#setConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[setErrorMessage](#setErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setImplementation](#setImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)`

`void`
`[setParentObject](#setParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)`

`void`
`[setParentRule](#setParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [Element](ext/magicdraw/classes/mdkernel/Element.html) value)`

`void`
`[setSeverity](#setSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ValidationProfile.SeverityKindEnum))([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 [ValidationProfile.SeverityKindEnum](ValidationProfile.SeverityKindEnum.html) value)`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)
`[apply](../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)), [isDerivedStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isSameOrDerivedStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [unApply](../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
STEREOTYPE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.STEREOTYPE_NAME)
ABBREVIATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ABBREVIATION
Specify a short word, phrase, or acronym of the validation rule. It allows you to distinguish the validation rules among other rules when sorting or filtering.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.ABBREVIATION)
CONSTRAINEDELEMENTSFILTER
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) CONSTRAINEDELEMENTSFILTER
Specify the condition that must be met in order to validate Constrained Elements.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.CONSTRAINEDELEMENTSFILTER)
ERRORMESSAGE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ERRORMESSAGE
Describe the invalid situation when validation rule fails.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.ERRORMESSAGE)
PARENTOBJECT
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PARENTOBJECT
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.PARENTOBJECT)
PARENTRULE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PARENTRULE
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.PARENTRULE)
SEVERITY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SEVERITY
Select the severity kind of the validation rule: debug, info, warning, error, fatal.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.SEVERITY)
IMPLEMENTATION
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) IMPLEMENTATION
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.IMPLEMENTATION)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ValidationRuleStereotype
protected ValidationRuleStereotype([ValidationProfile](ValidationProfile.html) profile)
 ============ METHOD DETAIL ========== 
Method Details
getStereotype
public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getStereotype()
Description copied from class: `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())`
Returns stereotype for this wrapper.
Specified by:
`[getStereotype](../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype())` in class `[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)`
Returns:
stereotype
getAbbreviationProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getAbbreviationProperty()
getConstrainedElementsFilterProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getConstrainedElementsFilterProperty()
getErrorMessageProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getErrorMessageProperty()
getParentObjectProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getParentObjectProperty()
getParentRuleProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getParentRuleProperty()
getSeverityProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getSeverityProperty()
getImplementationProperty
@CheckForNullpublic [Property](ext/magicdraw/classes/mdkernel/Property.html) getImplementationProperty()
setAbbreviation
public void setAbbreviation([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearAbbreviation
public void clearAbbreviation([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getAbbreviation
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getAbbreviation([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setConstrainedElementsFilter
public void setConstrainedElementsFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
clearConstrainedElementsFilter
public void clearConstrainedElementsFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getConstrainedElementsFilter
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getConstrainedElementsFilter([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setErrorMessage
public void setErrorMessage([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearErrorMessage
public void clearErrorMessage([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getErrorMessage
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getErrorMessage([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setParentObject
public void setParentObject([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) value)
clearParentObject
public void clearParentObject([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getParentObject
@CheckForNullpublic [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) getParentObject([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setParentRule
public void setParentRule([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) value)
clearParentRule
public void clearParentRule([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getParentRule
@CheckForNullpublic [Element](ext/magicdraw/classes/mdkernel/Element.html) getParentRule([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setSeverity
public void setSeverity([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [ValidationProfile.SeverityKindEnum](ValidationProfile.SeverityKindEnum.html) value)
clearSeverity
public void clearSeverity([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getSeverity
@CheckForNullpublic [ValidationProfile.SeverityKindEnum](ValidationProfile.SeverityKindEnum.html) getSeverity([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
setImplementation
public void setImplementation([Element](ext/magicdraw/classes/mdkernel/Element.html) element,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)
clearImplementation
public void clearImplementation([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
getImplementation
@CheckForNullpublic [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getImplementation([Element](ext/magicdraw/classes/mdkernel/Element.html) element)
clear
protected void clear()
is
public boolean is(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
isInstance
public static boolean isInstance(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2</a></div>
<h1 class="title" title="Class ValidationProfile.ValidationRuleStereotype">Class ValidationProfile.ValidationRuleStereotype</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation.StereotypeWrapper</a>
<div class="inheritance">com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static class </span><span class="element-name type-name-label">ValidationProfile.ValidationRuleStereotype</span>
<span class="extends-implements">extends <a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></span></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ABBREVIATION">ABBREVIATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specify a short word, phrase, or acronym of the validation rule.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#CONSTRAINEDELEMENTSFILTER">CONSTRAINEDELEMENTSFILTER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specify the condition that must be met in order to validate Constrained Elements.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ERRORMESSAGE">ERRORMESSAGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describe the invalid situation when validation rule fails.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IMPLEMENTATION">IMPLEMENTATION</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PARENTOBJECT">PARENTOBJECT</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PARENTRULE">PARENTRULE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SEVERITY">SEVERITY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Select the severity kind of the validation rule: debug, info, warning, error, fatal.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#STEREOTYPE_NAME">STEREOTYPE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier</div>
<div class="table-header col-second">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>protected </code></div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ValidationProfile)">ValidationRuleStereotype</a><wbr/>(<a href="ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a> profile)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clear()">clear</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearAbbreviation</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearConstrainedElementsFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearErrorMessage</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearImplementation</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearParentObject</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearParentRule</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#clearSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">clearSeverity</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getAbbreviation</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAbbreviationProperty()">getAbbreviationProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getConstrainedElementsFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstrainedElementsFilterProperty()">getConstrainedElementsFilterProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getErrorMessage</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getErrorMessageProperty()">getErrorMessageProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getImplementation</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImplementationProperty()">getImplementationProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getParentObject</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentObjectProperty()">getParentObjectProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getParentRule</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getParentRuleProperty()">getParentRuleProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.SeverityKindEnum.html" title="enum class in com.nomagic.uml2">ValidationProfile.SeverityKindEnum</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">getSeverity</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverityProperty()">getSeverityProperty</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStereotype()">getStereotype</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns stereotype for this wrapper.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">is</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInstance</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setAbbreviation</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">setConstrainedElementsFilter</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setErrorMessage</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">setImplementation</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">setParentObject</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">setParentRule</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ValidationProfile.SeverityKindEnum)">setSeverity</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a href="ValidationProfile.SeverityKindEnum.html" title="enum class in com.nomagic.uml2">ValidationProfile.SeverityKindEnum</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation.StereotypeWrapper">Methods inherited from class com.nomagic.profiles.<a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></h3>
<code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#apply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">apply</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#isDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isDerivedStereotype</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#isSameOrDerivedStereotype(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isSameOrDerivedStereotype</a>, <a href="../profiles/ProfileImplementation.StereotypeWrapper.html#unApply(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">unApply</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="STEREOTYPE_NAME">
<h3>STEREOTYPE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">STEREOTYPE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.STEREOTYPE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ABBREVIATION">
<h3>ABBREVIATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ABBREVIATION</span></div>
<div class="block">Specify a short word, phrase, or acronym of the validation rule. It allows you to distinguish the validation rules among other rules when sorting or filtering.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.ABBREVIATION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONSTRAINEDELEMENTSFILTER">
<h3>CONSTRAINEDELEMENTSFILTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONSTRAINEDELEMENTSFILTER</span></div>
<div class="block">Specify the condition that must be met in order to validate Constrained Elements.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.CONSTRAINEDELEMENTSFILTER">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ERRORMESSAGE">
<h3>ERRORMESSAGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ERRORMESSAGE</span></div>
<div class="block">Describe the invalid situation when validation rule fails.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.ERRORMESSAGE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PARENTOBJECT">
<h3>PARENTOBJECT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PARENTOBJECT</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.PARENTOBJECT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PARENTRULE">
<h3>PARENTRULE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PARENTRULE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.PARENTRULE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEVERITY">
<h3>SEVERITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEVERITY</span></div>
<div class="block">Select the severity kind of the validation rule: debug, info, warning, error, fatal.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.SEVERITY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMPLEMENTATION">
<h3>IMPLEMENTATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IMPLEMENTATION</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ValidationRuleStereotype.IMPLEMENTATION">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ValidationProfile)">
<h3>ValidationRuleStereotype</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="element-name">ValidationRuleStereotype</span><wbr/><span class="parameters">(<a href="ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a> profile)</span></div>
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
<section class="detail" id="getStereotype()">
<h3>getStereotype</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getStereotype</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">ProfileImplementation.StereotypeWrapper</a></code></span></div>
<div class="block">Returns stereotype for this wrapper.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html#getStereotype()">getStereotype</a></code> in class <code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></dd>
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAbbreviationProperty()">
<h3>getAbbreviationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getAbbreviationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getConstrainedElementsFilterProperty()">
<h3>getConstrainedElementsFilterProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getConstrainedElementsFilterProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getErrorMessageProperty()">
<h3>getErrorMessageProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getErrorMessageProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getParentObjectProperty()">
<h3>getParentObjectProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getParentObjectProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getParentRuleProperty()">
<h3>getParentRuleProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getParentRuleProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSeverityProperty()">
<h3>getSeverityProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getSeverityProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getImplementationProperty()">
<h3>getImplementationProperty</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Property.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Property</a></span> <span class="element-name">getImplementationProperty</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setAbbreviation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAbbreviation</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearAbbreviation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearAbbreviation</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getAbbreviation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getAbbreviation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getAbbreviation</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>setConstrainedElementsFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setConstrainedElementsFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearConstrainedElementsFilter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearConstrainedElementsFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getConstrainedElementsFilter(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getConstrainedElementsFilter</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getConstrainedElementsFilter</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setErrorMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setErrorMessage</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearErrorMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearErrorMessage</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getErrorMessage(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getErrorMessage</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getErrorMessage</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.Object)">
<h3>setParentObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentObject</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearParentObject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearParentObject</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getParentObject(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getParentObject</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span> <span class="element-name">getParentObject</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>setParentRule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setParentRule</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearParentRule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearParentRule</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getParentRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getParentRule</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a></span> <span class="element-name">getParentRule</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ValidationProfile.SeverityKindEnum)">
<h3>setSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setSeverity</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a href="ValidationProfile.SeverityKindEnum.html" title="enum class in com.nomagic.uml2">ValidationProfile.SeverityKindEnum</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearSeverity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearSeverity</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getSeverity(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getSeverity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.SeverityKindEnum.html" title="enum class in com.nomagic.uml2">ValidationProfile.SeverityKindEnum</a></span> <span class="element-name">getSeverity</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="setImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">
<h3>setImplementation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImplementation</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
</section>
</li>
<li>
<section class="detail" id="clearImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>clearImplementation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearImplementation</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="getImplementation(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>getImplementation</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getImplementation</span><wbr/><span class="parameters">(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="clear()">
<h3>clear</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type">void</span> <span class="element-name">clear</span>()</div>
</section>
</li>
<li>
<section class="detail" id="is(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>is</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">is</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
</section>
</li>
<li>
<section class="detail" id="isInstance(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInstance</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
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
