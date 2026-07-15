# JAVA OPENAPI: ValidationProfile (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/uml2/ValidationProfile.html
- source_path: `com/nomagic/uml2/ValidationProfile.html`
- source_sha256: `8a2038743adc71850d70f7666bfe3703c8851a39a23e57d5e6fc37ea1cbf119b`
- captured_utc: `2026-07-14T16:56:15.344682+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.uml2](package-summary.html)

## Class ValidationProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation](../profiles/ProfileImplementation.html)
com.nomagic.uml2.ValidationProfile

@OpenApiAllpublic classValidationProfile
extends [ProfileImplementation](../profiles/ProfileImplementation.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static class`
`[ValidationProfile.ActiveValidationSuiteStereotype](ValidationProfile.ActiveValidationSuiteStereotype.html)`

`static class`
`[ValidationProfile.DebugIconStereotype](ValidationProfile.DebugIconStereotype.html)`

`static class`
`[ValidationProfile.DefinitionStereotype](ValidationProfile.DefinitionStereotype.html)`

`static class`
`[ValidationProfile.ErrorIconStereotype](ValidationProfile.ErrorIconStereotype.html)`

`static class`
`[ValidationProfile.FatalIconStereotype](ValidationProfile.FatalIconStereotype.html)`

`static class`
`[ValidationProfile.ImagedStereotype](ValidationProfile.ImagedStereotype.html)`

`static class`
`[ValidationProfile.InfoIconStereotype](ValidationProfile.InfoIconStereotype.html)`

`static class`
`[ValidationProfile.InvariantStereotype](ValidationProfile.InvariantStereotype.html)`

`static enum`
`[ValidationProfile.SeverityKindEnum](ValidationProfile.SeverityKindEnum.html)`

`static class`
`[ValidationProfile.SystemValidationSuiteStereotype](ValidationProfile.SystemValidationSuiteStereotype.html)`

`static class`
`[ValidationProfile.ValidationRuleStereotype](ValidationProfile.ValidationRuleStereotype.html)`

`static class`
`[ValidationProfile.ValidationSuiteStereotype](ValidationProfile.ValidationSuiteStereotype.html)`

`static class`
`[ValidationProfile.WarningIconStereotype](ValidationProfile.WarningIconStereotype.html)`
Nested classes/interfaces inherited from class com.nomagic.profiles.[ProfileImplementation](../profiles/ProfileImplementation.html)
`[ProfileImplementation.StereotypeWrapper](../profiles/ProfileImplementation.StereotypeWrapper.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ACTIVEVALIDATIONSUITE_STEREOTYPE](#ACTIVEVALIDATIONSUITE_STEREOTYPE)`
Deprecated.
use ActiveValidationSuiteStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEBUGICON_STEREOTYPE](#DEBUGICON_STEREOTYPE)`
Deprecated.
use DebugIconStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[DEFINITION_STEREOTYPE](#DEFINITION_STEREOTYPE)`
Deprecated.
use DefinitionStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[ERRORICON_STEREOTYPE](#ERRORICON_STEREOTYPE)`
Deprecated.
use ErrorIconStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[FATALICON_STEREOTYPE](#FATALICON_STEREOTYPE)`
Deprecated.
use FatalIconStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[IMAGED_HIGHLIGHTCOLOR_PROPERTY](#IMAGED_HIGHLIGHTCOLOR_PROPERTY)`
Deprecated.
use ImagedStereotype.HIGHLIGHTCOLOR
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[IMAGED_STEREOTYPE](#IMAGED_STEREOTYPE)`
Deprecated.
use ImagedStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INFOICON_STEREOTYPE](#INFOICON_STEREOTYPE)`
Deprecated.
use InfoIconStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[INVARIANT_STEREOTYPE](#INVARIANT_STEREOTYPE)`
Deprecated.
use InvariantStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_NAME](#PROFILE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_URI](#PROFILE_URI)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SEVERITYKIND_DATATYPE](#SEVERITYKIND_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SEVERITYKIND_DEBUG_LITERAL](#SEVERITYKIND_DEBUG_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SEVERITYKIND_ERROR_LITERAL](#SEVERITYKIND_ERROR_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SEVERITYKIND_FATAL_LITERAL](#SEVERITYKIND_FATAL_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SEVERITYKIND_INFO_LITERAL](#SEVERITYKIND_INFO_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SEVERITYKIND_WARNING_LITERAL](#SEVERITYKIND_WARNING_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[SYSTEMVALIDATIONSUITE_STEREOTYPE](#SYSTEMVALIDATIONSUITE_STEREOTYPE)`
Deprecated.
use SystemValidationSuiteStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_ABBREVIATION_PROPERTY](#VALIDATIONRULE_ABBREVIATION_PROPERTY)`
Deprecated.
use ValidationRuleStereotype.ABBREVIATION
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY](#VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY)`
Deprecated.
use ValidationRuleStereotype.CONSTRAINEDELEMENTSFILTER
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_ERRORMESSAGE_PROPERTY](#VALIDATIONRULE_ERRORMESSAGE_PROPERTY)`
Deprecated.
use ValidationRuleStereotype.ERRORMESSAGE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_IMPLEMENTATION_PROPERTY](#VALIDATIONRULE_IMPLEMENTATION_PROPERTY)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_PARENTOBJECT_PROPERTY](#VALIDATIONRULE_PARENTOBJECT_PROPERTY)`
Deprecated.
use ValidationRuleStereotype.PARENTOBJECT
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_PARENTRULE_PROPERTY](#VALIDATIONRULE_PARENTRULE_PROPERTY)`
Deprecated.
use ValidationRuleStereotype.PARENTRULE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_SEVERITY_PROPERTY](#VALIDATIONRULE_SEVERITY_PROPERTY)`
Deprecated.
use ValidationRuleStereotype.SEVERITY
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONRULE_STEREOTYPE](#VALIDATIONRULE_STEREOTYPE)`
Deprecated.
use ValidationRuleStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALIDATIONSUITE_STEREOTYPE](#VALIDATIONSUITE_STEREOTYPE)`
Deprecated.
use ValidationSuiteStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[WARNINGICON_STEREOTYPE](#WARNINGICON_STEREOTYPE)`
Deprecated.
use WarningIconStereotype.STEREOTYPE_NAME
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ValidationProfile](#%3Cinit%3E(com.nomagic.profiles.ProfileCache))(com.nomagic.profiles.ProfileCache cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[ValidationProfile.ActiveValidationSuiteStereotype](ValidationProfile.ActiveValidationSuiteStereotype.html)`
`[activeValidationSuite](#activeValidationSuite())()`

`[ValidationProfile.DebugIconStereotype](ValidationProfile.DebugIconStereotype.html)`
`[debugIcon](#debugIcon())()`

`[ValidationProfile.DefinitionStereotype](ValidationProfile.DefinitionStereotype.html)`
`[definition](#definition())()`

`[ValidationProfile.ErrorIconStereotype](ValidationProfile.ErrorIconStereotype.html)`
`[errorIcon](#errorIcon())()`

`[ValidationProfile.FatalIconStereotype](ValidationProfile.FatalIconStereotype.html)`
`[fatalIcon](#fatalIcon())()`

`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`
Generated method for getting all stereotype wrappers contained within this profile.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`
Generated method for getting all stereotypes contained within this profile.
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getActiveValidationSuite](#getActiveValidationSuite())()`
Deprecated.
use getInstance(element).activeValidationSuite().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getDebugIcon](#getDebugIcon())()`
Deprecated.
use getInstance(element).debugIcon().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getDefinition](#getDefinition())()`
Deprecated.
use getInstance(element).definition().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getErrorIcon](#getErrorIcon())()`
Deprecated.
use getInstance(element).errorIcon().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getFatalIcon](#getFatalIcon())()`
Deprecated.
use getInstance(element).fatalIcon().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getImaged](#getImaged())()`
Deprecated.
use getInstance(element).imaged().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getInfoIcon](#getInfoIcon())()`
Deprecated.
use getInstance(element).infoIcon().getStereotype()
`static [ValidationProfile](ValidationProfile.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../magicdraw/uml/BaseElement.html) baseElement)`

`static [ValidationProfile](ValidationProfile.html)`
`[getInstanceByProject](#getInstanceByProject(com.nomagic.uml2.project.ElementProject))(com.nomagic.uml2.project.ElementProject project)`

`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getInvariant](#getInvariant())()`
Deprecated.
use getInstance(element).invariant().getStereotype()
`[Enumeration](ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getSeverityKind](#getSeverityKind())()`

`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getSystemValidationSuite](#getSystemValidationSuite())()`
Deprecated.
use getInstance(element).systemValidationSuite().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getValidationRule](#getValidationRule())()`
Deprecated.
use getInstance(element).validationRule().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getValidationSuite](#getValidationSuite())()`
Deprecated.
use getInstance(element).validationSuite().getStereotype()
`[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)`
`[getWarningIcon](#getWarningIcon())()`
Deprecated.
use getInstance(element).warningIcon().getStereotype()
`[ValidationProfile.ImagedStereotype](ValidationProfile.ImagedStereotype.html)`
`[imaged](#imaged())()`

`[ValidationProfile.InfoIconStereotype](ValidationProfile.InfoIconStereotype.html)`
`[infoIcon](#infoIcon())()`

`[ValidationProfile.InvariantStereotype](ValidationProfile.InvariantStereotype.html)`
`[invariant](#invariant())()`

`static boolean`
`[isActiveValidationSuite](#isActiveValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ActiveValidationSuiteStereotype.isInstance(element)
`static boolean`
`[isDebugIcon](#isDebugIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use DebugIconStereotype.isInstance(element)
`static boolean`
`[isDefinition](#isDefinition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use DefinitionStereotype.isInstance(element)
`static boolean`
`[isErrorIcon](#isErrorIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ErrorIconStereotype.isInstance(element)
`static boolean`
`[isFatalIcon](#isFatalIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use FatalIconStereotype.isInstance(element)
`static boolean`
`[isImaged](#isImaged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ImagedStereotype.isInstance(element)
`static boolean`
`[isInfoIcon](#isInfoIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use InfoIconStereotype.isInstance(element)
`static boolean`
`[isInvariant](#isInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use InvariantStereotype.isInstance(element)
`static boolean`
`[isSystemValidationSuite](#isSystemValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use SystemValidationSuiteStereotype.isInstance(element)
`static boolean`
`[isValidationRule](#isValidationRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ValidationRuleStereotype.isInstance(element)
`static boolean`
`[isValidationSuite](#isValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use ValidationSuiteStereotype.isInstance(element)
`static boolean`
`[isWarningIcon](#isWarningIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use WarningIconStereotype.isInstance(element)
`[ValidationProfile.SystemValidationSuiteStereotype](ValidationProfile.SystemValidationSuiteStereotype.html)`
`[systemValidationSuite](#systemValidationSuite())()`

`[ValidationProfile.ValidationRuleStereotype](ValidationProfile.ValidationRuleStereotype.html)`
`[validationRule](#validationRule())()`

`[ValidationProfile.ValidationSuiteStereotype](ValidationProfile.ValidationSuiteStereotype.html)`
`[validationSuite](#validationSuite())()`

`[ValidationProfile.WarningIconStereotype](ValidationProfile.WarningIconStereotype.html)`
`[warningIcon](#warningIcon())()`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation](../profiles/ProfileImplementation.html)
`[clearCache](../profiles/ProfileImplementation.html#clearCache()), [findByRelativeQualifiedName](../profiles/ProfileImplementation.html#findByRelativeQualifiedName(java.lang.String,java.lang.Class)), [getAllStereotypes](../profiles/ProfileImplementation.html#getAllStereotypes()), [getCache](../profiles/ProfileImplementation.html#getCache()), [getDataType](../profiles/ProfileImplementation.html#getDataType(java.lang.String)), [getProfile](../profiles/ProfileImplementation.html#getProfile()), [getStereotype](../profiles/ProfileImplementation.html#getStereotype(java.lang.String)), [isTypeOf](../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isTypeOf](../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [valueFromString](../profiles/ProfileImplementation.html#valueFromString(java.lang.Class,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
VALIDATIONRULE_IMPLEMENTATION_PROPERTY
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_IMPLEMENTATION_PROPERTY
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_IMPLEMENTATION_PROPERTY)
PROFILE_URI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_URI
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.PROFILE_URI)
PROFILE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.PROFILE_NAME)
SEVERITYKIND_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SEVERITYKIND_DATATYPE
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_DATATYPE)
SEVERITYKIND_DEBUG_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SEVERITYKIND_DEBUG_LITERAL
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_DEBUG_LITERAL)
SEVERITYKIND_ERROR_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SEVERITYKIND_ERROR_LITERAL
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_ERROR_LITERAL)
SEVERITYKIND_FATAL_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SEVERITYKIND_FATAL_LITERAL
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_FATAL_LITERAL)
SEVERITYKIND_INFO_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SEVERITYKIND_INFO_LITERAL
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_INFO_LITERAL)
SEVERITYKIND_WARNING_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SEVERITYKIND_WARNING_LITERAL
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_WARNING_LITERAL)
ACTIVEVALIDATIONSUITE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACTIVEVALIDATIONSUITE_STEREOTYPE
Deprecated.
use ActiveValidationSuiteStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ACTIVEVALIDATIONSUITE_STEREOTYPE)
DEBUGICON_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEBUGICON_STEREOTYPE
Deprecated.
use DebugIconStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.DEBUGICON_STEREOTYPE)
DEFINITION_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) DEFINITION_STEREOTYPE
Deprecated.
use DefinitionStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.DEFINITION_STEREOTYPE)
ERRORICON_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ERRORICON_STEREOTYPE
Deprecated.
use ErrorIconStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ERRORICON_STEREOTYPE)
FATALICON_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FATALICON_STEREOTYPE
Deprecated.
use FatalIconStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.FATALICON_STEREOTYPE)
IMAGED_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) IMAGED_STEREOTYPE
Deprecated.
use ImagedStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.IMAGED_STEREOTYPE)
IMAGED_HIGHLIGHTCOLOR_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) IMAGED_HIGHLIGHTCOLOR_PROPERTY
Deprecated.
use ImagedStereotype.HIGHLIGHTCOLOR
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.IMAGED_HIGHLIGHTCOLOR_PROPERTY)
INFOICON_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INFOICON_STEREOTYPE
Deprecated.
use InfoIconStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.INFOICON_STEREOTYPE)
INVARIANT_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) INVARIANT_STEREOTYPE
Deprecated.
use InvariantStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.INVARIANT_STEREOTYPE)
SYSTEMVALIDATIONSUITE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SYSTEMVALIDATIONSUITE_STEREOTYPE
Deprecated.
use SystemValidationSuiteStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SYSTEMVALIDATIONSUITE_STEREOTYPE)
VALIDATIONRULE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_STEREOTYPE
Deprecated.
use ValidationRuleStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_STEREOTYPE)
VALIDATIONRULE_ABBREVIATION_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_ABBREVIATION_PROPERTY
Deprecated.
use ValidationRuleStereotype.ABBREVIATION
Specify a short word, phrase, or acronym of the validation rule. It allows you to distinguish the validation rules among other rules when sorting or filtering.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_ABBREVIATION_PROPERTY)
VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY
Deprecated.
use ValidationRuleStereotype.CONSTRAINEDELEMENTSFILTER
Specify the condition that must be met in order to validate Constrained Elements.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY)
VALIDATIONRULE_ERRORMESSAGE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_ERRORMESSAGE_PROPERTY
Deprecated.
use ValidationRuleStereotype.ERRORMESSAGE
Describe the invalid situation when validation rule fails.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_ERRORMESSAGE_PROPERTY)
VALIDATIONRULE_PARENTOBJECT_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_PARENTOBJECT_PROPERTY
Deprecated.
use ValidationRuleStereotype.PARENTOBJECT
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_PARENTOBJECT_PROPERTY)
VALIDATIONRULE_PARENTRULE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_PARENTRULE_PROPERTY
Deprecated.
use ValidationRuleStereotype.PARENTRULE
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_PARENTRULE_PROPERTY)
VALIDATIONRULE_SEVERITY_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONRULE_SEVERITY_PROPERTY
Deprecated.
use ValidationRuleStereotype.SEVERITY
Select the severity kind of the validation rule: debug, info, warning, error, fatal.
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_SEVERITY_PROPERTY)
VALIDATIONSUITE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALIDATIONSUITE_STEREOTYPE
Deprecated.
use ValidationSuiteStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONSUITE_STEREOTYPE)
WARNINGICON_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) WARNINGICON_STEREOTYPE
Deprecated.
use WarningIconStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../constant-values.html#com.nomagic.uml2.ValidationProfile.WARNINGICON_STEREOTYPE)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ValidationProfile
public ValidationProfile(com.nomagic.profiles.ProfileCache cache)
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [ValidationProfile](ValidationProfile.html) getInstance([BaseElement](../magicdraw/uml/BaseElement.html) baseElement)
getInstanceByProject
public static [ValidationProfile](ValidationProfile.html) getInstanceByProject(com.nomagic.uml2.project.ElementProject project)
activeValidationSuite
public [ValidationProfile.ActiveValidationSuiteStereotype](ValidationProfile.ActiveValidationSuiteStereotype.html) activeValidationSuite()
debugIcon
public [ValidationProfile.DebugIconStereotype](ValidationProfile.DebugIconStereotype.html) debugIcon()
definition
public [ValidationProfile.DefinitionStereotype](ValidationProfile.DefinitionStereotype.html) definition()
errorIcon
public [ValidationProfile.ErrorIconStereotype](ValidationProfile.ErrorIconStereotype.html) errorIcon()
fatalIcon
public [ValidationProfile.FatalIconStereotype](ValidationProfile.FatalIconStereotype.html) fatalIcon()
imaged
public [ValidationProfile.ImagedStereotype](ValidationProfile.ImagedStereotype.html) imaged()
infoIcon
public [ValidationProfile.InfoIconStereotype](ValidationProfile.InfoIconStereotype.html) infoIcon()
invariant
public [ValidationProfile.InvariantStereotype](ValidationProfile.InvariantStereotype.html) invariant()
systemValidationSuite
public [ValidationProfile.SystemValidationSuiteStereotype](ValidationProfile.SystemValidationSuiteStereotype.html) systemValidationSuite()
validationRule
public [ValidationProfile.ValidationRuleStereotype](ValidationProfile.ValidationRuleStereotype.html) validationRule()
validationSuite
public [ValidationProfile.ValidationSuiteStereotype](ValidationProfile.ValidationSuiteStereotype.html) validationSuite()
warningIcon
public [ValidationProfile.WarningIconStereotype](ValidationProfile.WarningIconStereotype.html) warningIcon()
getSeverityKind
public [Enumeration](ext/magicdraw/classes/mdkernel/Enumeration.html) getSeverityKind()
getActiveValidationSuite
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getActiveValidationSuite()
Deprecated.
use getInstance(element).activeValidationSuite().getStereotype()
isActiveValidationSuite
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isActiveValidationSuite(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ActiveValidationSuiteStereotype.isInstance(element)
getDebugIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getDebugIcon()
Deprecated.
use getInstance(element).debugIcon().getStereotype()
isDebugIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isDebugIcon(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use DebugIconStereotype.isInstance(element)
getDefinition
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getDefinition()
Deprecated.
use getInstance(element).definition().getStereotype()
isDefinition
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isDefinition(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use DefinitionStereotype.isInstance(element)
getErrorIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getErrorIcon()
Deprecated.
use getInstance(element).errorIcon().getStereotype()
isErrorIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isErrorIcon(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ErrorIconStereotype.isInstance(element)
getFatalIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getFatalIcon()
Deprecated.
use getInstance(element).fatalIcon().getStereotype()
isFatalIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isFatalIcon(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use FatalIconStereotype.isInstance(element)
getImaged
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getImaged()
Deprecated.
use getInstance(element).imaged().getStereotype()
isImaged
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isImaged(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ImagedStereotype.isInstance(element)
getInfoIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getInfoIcon()
Deprecated.
use getInstance(element).infoIcon().getStereotype()
isInfoIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isInfoIcon(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use InfoIconStereotype.isInstance(element)
getInvariant
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getInvariant()
Deprecated.
use getInstance(element).invariant().getStereotype()
isInvariant
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isInvariant(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use InvariantStereotype.isInstance(element)
getSystemValidationSuite
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getSystemValidationSuite()
Deprecated.
use getInstance(element).systemValidationSuite().getStereotype()
isSystemValidationSuite
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isSystemValidationSuite(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use SystemValidationSuiteStereotype.isInstance(element)
getValidationRule
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getValidationRule()
Deprecated.
use getInstance(element).validationRule().getStereotype()
isValidationRule
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isValidationRule(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ValidationRuleStereotype.isInstance(element)
getValidationSuite
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getValidationSuite()
Deprecated.
use getInstance(element).validationSuite().getStereotype()
isValidationSuite
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isValidationSuite(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use ValidationSuiteStereotype.isInstance(element)
getWarningIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](ext/magicdraw/mdprofiles/Stereotype.html) getWarningIcon()
Deprecated.
use getInstance(element).warningIcon().getStereotype()
isWarningIcon
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isWarningIcon(@CheckForNull
 [Element](ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use WarningIconStereotype.isInstance(element)
generatedGetAllElementWrappers
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper> generatedGetAllElementWrappers()
Description copied from class: `[ProfileImplementation](../profiles/ProfileImplementation.html#generatedGetAllElementWrappers())`
Generated method for getting all stereotype wrappers contained within this profile.
Specified by:
`[generatedGetAllElementWrappers](../profiles/ProfileImplementation.html#generatedGetAllElementWrappers())` in class `[ProfileImplementation](../profiles/ProfileImplementation.html)`
Returns:
gets all stereotype wrappers contained within this profile.
generatedGetAllStereotypes
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](ext/magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()
Description copied from class: `[ProfileImplementation](../profiles/ProfileImplementation.html#generatedGetAllStereotypes())`
Generated method for getting all stereotypes contained within this profile.
Specified by:
`[generatedGetAllStereotypes](../profiles/ProfileImplementation.html#generatedGetAllStereotypes())` in class `[ProfileImplementation](../profiles/ProfileImplementation.html)`
Returns:
gets all stereotypes contained within this profile.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.uml2</a></div>
<h1 class="title" title="Class ValidationProfile">Class ValidationProfile</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation</a>
<div class="inheritance">com.nomagic.uml2.ValidationProfile</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ValidationProfile</span>
<span class="extends-implements">extends <a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></span></div>
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
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ValidationProfile.ActiveValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ActiveValidationSuiteStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ValidationProfile.DebugIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.DebugIconStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ValidationProfile.DefinitionStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.DefinitionStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ValidationProfile.ErrorIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ErrorIconStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ValidationProfile.FatalIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.FatalIconStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ValidationProfile.ImagedStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ImagedStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ValidationProfile.InfoIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.InfoIconStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ValidationProfile.InvariantStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.InvariantStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ValidationProfile.SeverityKindEnum.html" title="enum class in com.nomagic.uml2">ValidationProfile.SeverityKindEnum</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ValidationProfile.SystemValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.SystemValidationSuiteStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ValidationProfile.ValidationRuleStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ValidationRuleStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="ValidationProfile.ValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ValidationSuiteStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="ValidationProfile.WarningIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.WarningIconStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Nested classes/interfaces inherited from class com.nomagic.profiles.<a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h2>
<code><a href="../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></div>
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
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ACTIVEVALIDATIONSUITE_STEREOTYPE">ACTIVEVALIDATIONSUITE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ActiveValidationSuiteStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#DEBUGICON_STEREOTYPE">DEBUGICON_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DebugIconStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#DEFINITION_STEREOTYPE">DEFINITION_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DefinitionStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ERRORICON_STEREOTYPE">ERRORICON_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ErrorIconStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#FATALICON_STEREOTYPE">FATALICON_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FatalIconStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#IMAGED_HIGHLIGHTCOLOR_PROPERTY">IMAGED_HIGHLIGHTCOLOR_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImagedStereotype.HIGHLIGHTCOLOR</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#IMAGED_STEREOTYPE">IMAGED_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImagedStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#INFOICON_STEREOTYPE">INFOICON_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InfoIconStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#INVARIANT_STEREOTYPE">INVARIANT_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InvariantStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROFILE_NAME">PROFILE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROFILE_URI">PROFILE_URI</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SEVERITYKIND_DATATYPE">SEVERITYKIND_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SEVERITYKIND_DEBUG_LITERAL">SEVERITYKIND_DEBUG_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SEVERITYKIND_ERROR_LITERAL">SEVERITYKIND_ERROR_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SEVERITYKIND_FATAL_LITERAL">SEVERITYKIND_FATAL_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SEVERITYKIND_INFO_LITERAL">SEVERITYKIND_INFO_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#SEVERITYKIND_WARNING_LITERAL">SEVERITYKIND_WARNING_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SYSTEMVALIDATIONSUITE_STEREOTYPE">SYSTEMVALIDATIONSUITE_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemValidationSuiteStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_ABBREVIATION_PROPERTY">VALIDATIONRULE_ABBREVIATION_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.ABBREVIATION</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY">VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.CONSTRAINEDELEMENTSFILTER</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_ERRORMESSAGE_PROPERTY">VALIDATIONRULE_ERRORMESSAGE_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.ERRORMESSAGE</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_IMPLEMENTATION_PROPERTY">VALIDATIONRULE_IMPLEMENTATION_PROPERTY</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_PARENTOBJECT_PROPERTY">VALIDATIONRULE_PARENTOBJECT_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.PARENTOBJECT</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_PARENTRULE_PROPERTY">VALIDATIONRULE_PARENTRULE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.PARENTRULE</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_SEVERITY_PROPERTY">VALIDATIONRULE_SEVERITY_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.SEVERITY</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VALIDATIONRULE_STEREOTYPE">VALIDATIONRULE_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALIDATIONSUITE_STEREOTYPE">VALIDATIONSUITE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationSuiteStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#WARNINGICON_STEREOTYPE">WARNINGICON_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use WarningIconStereotype.STEREOTYPE_NAME</div>
</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.profiles.ProfileCache)">ValidationProfile</a><wbr/>(com.nomagic.profiles.ProfileCache cache)</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.ActiveValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ActiveValidationSuiteStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#activeValidationSuite()">activeValidationSuite</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.DebugIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.DebugIconStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#debugIcon()">debugIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.DefinitionStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.DefinitionStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#definition()">definition</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.ErrorIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ErrorIconStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#errorIcon()">errorIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.FatalIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.FatalIconStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#fatalIcon()">fatalIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getActiveValidationSuite()">getActiveValidationSuite</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).activeValidationSuite().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDebugIcon()">getDebugIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).debugIcon().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getDefinition()">getDefinition</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).definition().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getErrorIcon()">getErrorIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).errorIcon().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getFatalIcon()">getFatalIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).fatalIcon().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getImaged()">getImaged</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).imaged().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInfoIcon()">getInfoIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).infoIcon().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.nomagic.uml2.project.ElementProject)">getInstanceByProject</a><wbr/>(com.nomagic.uml2.project.ElementProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getInvariant()">getInvariant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).invariant().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverityKind()">getSeverityKind</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSystemValidationSuite()">getSystemValidationSuite</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).systemValidationSuite().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getValidationRule()">getValidationRule</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).validationRule().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getValidationSuite()">getValidationSuite</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).validationSuite().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getWarningIcon()">getWarningIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).warningIcon().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.ImagedStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ImagedStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#imaged()">imaged</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.InfoIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.InfoIconStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#infoIcon()">infoIcon</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.InvariantStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.InvariantStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#invariant()">invariant</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isActiveValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isActiveValidationSuite</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ActiveValidationSuiteStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isDebugIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isDebugIcon</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DebugIconStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isDefinition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isDefinition</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DefinitionStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isErrorIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isErrorIcon</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ErrorIconStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isFatalIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isFatalIcon</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FatalIconStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isImaged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isImaged</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImagedStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isInfoIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInfoIcon</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InfoIconStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isInvariant</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InvariantStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isSystemValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isSystemValidationSuite</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemValidationSuiteStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isValidationRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isValidationRule</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isValidationSuite</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationSuiteStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isWarningIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isWarningIcon</a><wbr/>(<a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use WarningIconStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.SystemValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.SystemValidationSuiteStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#systemValidationSuite()">systemValidationSuite</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.ValidationRuleStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ValidationRuleStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#validationRule()">validationRule</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.ValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ValidationSuiteStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#validationSuite()">validationSuite</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="ValidationProfile.WarningIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.WarningIconStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#warningIcon()">warningIcon</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Methods inherited from class com.nomagic.profiles.<a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h3>
<code><a href="../profiles/ProfileImplementation.html#clearCache()">clearCache</a>, <a href="../profiles/ProfileImplementation.html#findByRelativeQualifiedName(java.lang.String,java.lang.Class)">findByRelativeQualifiedName</a>, <a href="../profiles/ProfileImplementation.html#getAllStereotypes()">getAllStereotypes</a>, <a href="../profiles/ProfileImplementation.html#getCache()">getCache</a>, <a href="../profiles/ProfileImplementation.html#getDataType(java.lang.String)">getDataType</a>, <a href="../profiles/ProfileImplementation.html#getProfile()">getProfile</a>, <a href="../profiles/ProfileImplementation.html#getStereotype(java.lang.String)">getStereotype</a>, <a href="../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isTypeOf</a>, <a href="../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isTypeOf</a>, <a href="../profiles/ProfileImplementation.html#valueFromString(java.lang.Class,java.lang.Object)">valueFromString</a></code></div>
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
<section class="detail" id="VALIDATIONRULE_IMPLEMENTATION_PROPERTY">
<h3>VALIDATIONRULE_IMPLEMENTATION_PROPERTY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_IMPLEMENTATION_PROPERTY</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_IMPLEMENTATION_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROFILE_URI">
<h3>PROFILE_URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_URI</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.PROFILE_URI">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="PROFILE_NAME">
<h3>PROFILE_NAME</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_NAME</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.PROFILE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEVERITYKIND_DATATYPE">
<h3>SEVERITYKIND_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEVERITYKIND_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEVERITYKIND_DEBUG_LITERAL">
<h3>SEVERITYKIND_DEBUG_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEVERITYKIND_DEBUG_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_DEBUG_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEVERITYKIND_ERROR_LITERAL">
<h3>SEVERITYKIND_ERROR_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEVERITYKIND_ERROR_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_ERROR_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEVERITYKIND_FATAL_LITERAL">
<h3>SEVERITYKIND_FATAL_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEVERITYKIND_FATAL_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_FATAL_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEVERITYKIND_INFO_LITERAL">
<h3>SEVERITYKIND_INFO_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEVERITYKIND_INFO_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_INFO_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SEVERITYKIND_WARNING_LITERAL">
<h3>SEVERITYKIND_WARNING_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SEVERITYKIND_WARNING_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SEVERITYKIND_WARNING_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ACTIVEVALIDATIONSUITE_STEREOTYPE">
<h3>ACTIVEVALIDATIONSUITE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ACTIVEVALIDATIONSUITE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ActiveValidationSuiteStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ACTIVEVALIDATIONSUITE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEBUGICON_STEREOTYPE">
<h3>DEBUGICON_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEBUGICON_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DebugIconStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.DEBUGICON_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="DEFINITION_STEREOTYPE">
<h3>DEFINITION_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFINITION_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DefinitionStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.DEFINITION_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ERRORICON_STEREOTYPE">
<h3>ERRORICON_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ERRORICON_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ErrorIconStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.ERRORICON_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="FATALICON_STEREOTYPE">
<h3>FATALICON_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">FATALICON_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FatalIconStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.FATALICON_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMAGED_STEREOTYPE">
<h3>IMAGED_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IMAGED_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImagedStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.IMAGED_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="IMAGED_HIGHLIGHTCOLOR_PROPERTY">
<h3>IMAGED_HIGHLIGHTCOLOR_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">IMAGED_HIGHLIGHTCOLOR_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImagedStereotype.HIGHLIGHTCOLOR</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.IMAGED_HIGHLIGHTCOLOR_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INFOICON_STEREOTYPE">
<h3>INFOICON_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INFOICON_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InfoIconStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.INFOICON_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="INVARIANT_STEREOTYPE">
<h3>INVARIANT_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">INVARIANT_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InvariantStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.INVARIANT_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SYSTEMVALIDATIONSUITE_STEREOTYPE">
<h3>SYSTEMVALIDATIONSUITE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SYSTEMVALIDATIONSUITE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemValidationSuiteStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.SYSTEMVALIDATIONSUITE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONRULE_STEREOTYPE">
<h3>VALIDATIONRULE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONRULE_ABBREVIATION_PROPERTY">
<h3>VALIDATIONRULE_ABBREVIATION_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_ABBREVIATION_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.ABBREVIATION</div>
</div>
<div class="block">Specify a short word, phrase, or acronym of the validation rule. It allows you to distinguish the validation rules among other rules when sorting or filtering.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_ABBREVIATION_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY">
<h3>VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.CONSTRAINEDELEMENTSFILTER</div>
</div>
<div class="block">Specify the condition that must be met in order to validate Constrained Elements.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_CONSTRAINEDELEMENTSFILTER_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONRULE_ERRORMESSAGE_PROPERTY">
<h3>VALIDATIONRULE_ERRORMESSAGE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_ERRORMESSAGE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.ERRORMESSAGE</div>
</div>
<div class="block">Describe the invalid situation when validation rule fails.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_ERRORMESSAGE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONRULE_PARENTOBJECT_PROPERTY">
<h3>VALIDATIONRULE_PARENTOBJECT_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_PARENTOBJECT_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.PARENTOBJECT</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_PARENTOBJECT_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONRULE_PARENTRULE_PROPERTY">
<h3>VALIDATIONRULE_PARENTRULE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_PARENTRULE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.PARENTRULE</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_PARENTRULE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONRULE_SEVERITY_PROPERTY">
<h3>VALIDATIONRULE_SEVERITY_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONRULE_SEVERITY_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.SEVERITY</div>
</div>
<div class="block">Select the severity kind of the validation rule: debug, info, warning, error, fatal.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONRULE_SEVERITY_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALIDATIONSUITE_STEREOTYPE">
<h3>VALIDATIONSUITE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALIDATIONSUITE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationSuiteStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.VALIDATIONSUITE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="WARNINGICON_STEREOTYPE">
<h3>WARNINGICON_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">WARNINGICON_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use WarningIconStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../constant-values.html#com.nomagic.uml2.ValidationProfile.WARNINGICON_STEREOTYPE">Constant Field Values</a></li>
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
<section class="detail" id="&lt;init&gt;(com.nomagic.profiles.ProfileCache)">
<h3>ValidationProfile</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationProfile</span><wbr/><span class="parameters">(com.nomagic.profiles.ProfileCache cache)</span></div>
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
<section class="detail" id="getInstance(com.nomagic.magicdraw.uml.BaseElement)">
<h3>getInstance</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstanceByProject(com.nomagic.uml2.project.ElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="ValidationProfile.html" title="class in com.nomagic.uml2">ValidationProfile</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(com.nomagic.uml2.project.ElementProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="activeValidationSuite()">
<h3>activeValidationSuite</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.ActiveValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ActiveValidationSuiteStereotype</a></span> <span class="element-name">activeValidationSuite</span>()</div>
</section>
</li>
<li>
<section class="detail" id="debugIcon()">
<h3>debugIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.DebugIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.DebugIconStereotype</a></span> <span class="element-name">debugIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="definition()">
<h3>definition</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.DefinitionStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.DefinitionStereotype</a></span> <span class="element-name">definition</span>()</div>
</section>
</li>
<li>
<section class="detail" id="errorIcon()">
<h3>errorIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.ErrorIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ErrorIconStereotype</a></span> <span class="element-name">errorIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="fatalIcon()">
<h3>fatalIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.FatalIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.FatalIconStereotype</a></span> <span class="element-name">fatalIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="imaged()">
<h3>imaged</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.ImagedStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ImagedStereotype</a></span> <span class="element-name">imaged</span>()</div>
</section>
</li>
<li>
<section class="detail" id="infoIcon()">
<h3>infoIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.InfoIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.InfoIconStereotype</a></span> <span class="element-name">infoIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="invariant()">
<h3>invariant</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.InvariantStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.InvariantStereotype</a></span> <span class="element-name">invariant</span>()</div>
</section>
</li>
<li>
<section class="detail" id="systemValidationSuite()">
<h3>systemValidationSuite</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.SystemValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.SystemValidationSuiteStereotype</a></span> <span class="element-name">systemValidationSuite</span>()</div>
</section>
</li>
<li>
<section class="detail" id="validationRule()">
<h3>validationRule</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.ValidationRuleStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ValidationRuleStereotype</a></span> <span class="element-name">validationRule</span>()</div>
</section>
</li>
<li>
<section class="detail" id="validationSuite()">
<h3>validationSuite</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.ValidationSuiteStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.ValidationSuiteStereotype</a></span> <span class="element-name">validationSuite</span>()</div>
</section>
</li>
<li>
<section class="detail" id="warningIcon()">
<h3>warningIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ValidationProfile.WarningIconStereotype.html" title="class in com.nomagic.uml2">ValidationProfile.WarningIconStereotype</a></span> <span class="element-name">warningIcon</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getSeverityKind()">
<h3>getSeverityKind</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getSeverityKind</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getActiveValidationSuite()">
<h3>getActiveValidationSuite</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getActiveValidationSuite</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).activeValidationSuite().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isActiveValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isActiveValidationSuite</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isActiveValidationSuite</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ActiveValidationSuiteStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getDebugIcon()">
<h3>getDebugIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getDebugIcon</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).debugIcon().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isDebugIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isDebugIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDebugIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DebugIconStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getDefinition()">
<h3>getDefinition</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getDefinition</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).definition().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isDefinition(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isDefinition</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isDefinition</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use DefinitionStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getErrorIcon()">
<h3>getErrorIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getErrorIcon</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).errorIcon().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isErrorIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isErrorIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isErrorIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ErrorIconStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getFatalIcon()">
<h3>getFatalIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getFatalIcon</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).fatalIcon().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isFatalIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isFatalIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isFatalIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use FatalIconStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getImaged()">
<h3>getImaged</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getImaged</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).imaged().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isImaged(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isImaged</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isImaged</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ImagedStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getInfoIcon()">
<h3>getInfoIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getInfoIcon</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).infoIcon().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isInfoIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInfoIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInfoIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InfoIconStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getInvariant()">
<h3>getInvariant</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getInvariant</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).invariant().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isInvariant(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isInvariant</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isInvariant</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use InvariantStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getSystemValidationSuite()">
<h3>getSystemValidationSuite</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getSystemValidationSuite</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).systemValidationSuite().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isSystemValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isSystemValidationSuite</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isSystemValidationSuite</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use SystemValidationSuiteStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getValidationRule()">
<h3>getValidationRule</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getValidationRule</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).validationRule().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isValidationRule(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isValidationRule</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isValidationRule</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationRuleStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getValidationSuite()">
<h3>getValidationSuite</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getValidationSuite</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).validationSuite().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isValidationSuite(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isValidationSuite</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isValidationSuite</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use ValidationSuiteStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getWarningIcon()">
<h3>getWarningIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getWarningIcon</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).warningIcon().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isWarningIcon(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isWarningIcon</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isWarningIcon</span><wbr/><span class="parameters">(@CheckForNull
 <a href="ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use WarningIconStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../profiles/ProfileImplementation.html#generatedGetAllElementWrappers()">ProfileImplementation</a></code></span></div>
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../profiles/ProfileImplementation.html#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a></code> in class <code><a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></code></dd>
<dt>Returns:</dt>
<dd>gets all stereotype wrappers contained within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../profiles/ProfileImplementation.html#generatedGetAllStereotypes()">ProfileImplementation</a></code></span></div>
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../profiles/ProfileImplementation.html#generatedGetAllStereotypes()">generatedGetAllStereotypes</a></code> in class <code><a href="../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></code></dd>
<dt>Returns:</dt>
<dd>gets all stereotypes contained within this profile.</dd>
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
