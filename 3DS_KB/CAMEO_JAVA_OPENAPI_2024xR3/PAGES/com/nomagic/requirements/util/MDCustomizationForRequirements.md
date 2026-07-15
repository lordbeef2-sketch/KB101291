# JAVA OPENAPI: MDCustomizationForRequirements (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/requirements/util/MDCustomizationForRequirements.html
- source_path: `com/nomagic/requirements/util/MDCustomizationForRequirements.html`
- source_sha256: `f93feae9a3037d18791a97ce361b2d9501faba22a84ebcbb1a70d25b7068b6d0`
- captured_utc: `2026-07-14T16:56:09.736618+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.requirements.util](package-summary.html)

## Class MDCustomizationForRequirements

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.profiles.ProfileImplementation](../../profiles/ProfileImplementation.html)
com.nomagic.requirements.util.MDCustomizationForRequirements

@OpenApiAllpublic classMDCustomizationForRequirements
extends [ProfileImplementation](../../profiles/ProfileImplementation.html)

======== NESTED CLASS SUMMARY ======== 
Nested Class Summary
Nested Classes
Modifier and Type
Class
Description
`static enum`
`[MDCustomizationForRequirements.NumberingStyleEnum](MDCustomizationForRequirements.NumberingStyleEnum.html)`

`static class`
`[MDCustomizationForRequirements.NumberOwnerStereotype](MDCustomizationForRequirements.NumberOwnerStereotype.html)`

`static class`
`[MDCustomizationForRequirements.RequirementTableStereotype](MDCustomizationForRequirements.RequirementTableStereotype.html)`

`static class`
`[MDCustomizationForRequirements.RequirementTermsStereotype](MDCustomizationForRequirements.RequirementTermsStereotype.html)`

`static class`
`[MDCustomizationForRequirements.VerificationStatusStereotype](MDCustomizationForRequirements.VerificationStatusStereotype.html)`
Nested classes/interfaces inherited from class com.nomagic.profiles.[ProfileImplementation](../../profiles/ProfileImplementation.html)
`[ProfileImplementation.StereotypeWrapper](../../profiles/ProfileImplementation.StereotypeWrapper.html)`
 =========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBERINGSTYLE_DATATYPE](#NUMBERINGSTYLE_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBERINGSTYLE_NESTED_LITERAL](#NUMBERINGSTYLE_NESTED_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBERINGSTYLE_NORMAL_LITERAL](#NUMBERINGSTYLE_NORMAL_LITERAL)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROWNER_NUMBERINGSTYLE_PROPERTY](#NUMBEROWNER_NUMBERINGSTYLE_PROPERTY)`
Deprecated.
use NumberOwnerStereotype.NUMBERINGSTYLE
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROWNER_PREFIX_PROPERTY](#NUMBEROWNER_PREFIX_PROPERTY)`
Deprecated.
use NumberOwnerStereotype.PREFIX
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROWNER_SEPARATOR_PROPERTY](#NUMBEROWNER_SEPARATOR_PROPERTY)`
Deprecated.
use NumberOwnerStereotype.SEPARATOR
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NUMBEROWNER_STEREOTYPE](#NUMBEROWNER_STEREOTYPE)`
Deprecated.
use NumberOwnerStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_NAME](#PROFILE_NAME)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[PROFILE_URI](#PROFILE_URI)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQNUMBER_DATATYPE](#REQNUMBER_DATATYPE)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY](#REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY)`
Deprecated.
use RequirementTableStereotype.COLUMNSWIDTH
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTABLE_CONTEXT_PROPERTY](#REQUIREMENTTABLE_CONTEXT_PROPERTY)`
Deprecated.
use RequirementTableStereotype.CONTEXT
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY](#REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY)`
Deprecated.
use RequirementTableStereotype.CUSTOMCOLUMNELEMENTS
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY](#REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY)`
Deprecated.
use RequirementTableStereotype.SHOWCOLUMNS
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY](#REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY)`
Deprecated.
use RequirementTableStereotype.SHOWCONTEXT
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY](#REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY)`
Deprecated.
use RequirementTableStereotype.SHOWCUSTOMCOLUMNS
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTABLE_STEREOTYPE](#REQUIREMENTTABLE_STEREOTYPE)`
Deprecated.
use RequirementTableStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[REQUIREMENTTERMS_STEREOTYPE](#REQUIREMENTTERMS_STEREOTYPE)`
Deprecated.
use RequirementTermsStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VERIFICATIONSTATUS_CONSTRAINT_PROPERTY](#VERIFICATIONSTATUS_CONSTRAINT_PROPERTY)`
Deprecated.
use VerificationStatusStereotype.CONSTRAINT
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VERIFICATIONSTATUS_MARGIN_PROPERTY](#VERIFICATIONSTATUS_MARGIN_PROPERTY)`
Deprecated.
use VerificationStatusStereotype.MARGIN
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VERIFICATIONSTATUS_REQUIREMENT_PROPERTY](#VERIFICATIONSTATUS_REQUIREMENT_PROPERTY)`
Deprecated.
use VerificationStatusStereotype.REQUIREMENT
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VERIFICATIONSTATUS_STATUS_PROPERTY](#VERIFICATIONSTATUS_STATUS_PROPERTY)`
Deprecated.
use VerificationStatusStereotype.STATUS
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VERIFICATIONSTATUS_STEREOTYPE](#VERIFICATIONSTATUS_STEREOTYPE)`
Deprecated.
use VerificationStatusStereotype.STEREOTYPE_NAME
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VERIFICATIONSTATUS_TIMESTAMP_PROPERTY](#VERIFICATIONSTATUS_TIMESTAMP_PROPERTY)`
Deprecated.
use VerificationStatusStereotype.TIMESTAMP
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[MDCustomizationForRequirements](#%3Cinit%3E(com.nomagic.profiles.ProfileCache))(com.nomagic.profiles.ProfileCache cache)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper>`
`[generatedGetAllElementWrappers](#generatedGetAllElementWrappers())()`
Generated method for getting all stereotype wrappers contained within this profile.
`protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)>`
`[generatedGetAllStereotypes](#generatedGetAllStereotypes())()`
Generated method for getting all stereotypes contained within this profile.
`static [MDCustomizationForRequirements](MDCustomizationForRequirements.html)`
`[getInstance](#getInstance(com.nomagic.magicdraw.uml.BaseElement))([BaseElement](../../magicdraw/uml/BaseElement.html) baseElement)`

`static [MDCustomizationForRequirements](MDCustomizationForRequirements.html)`
`[getInstanceByProject](#getInstanceByProject(com.nomagic.uml2.project.ElementProject))(com.nomagic.uml2.project.ElementProject project)`

`[Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html)`
`[getNumberingStyle](#getNumberingStyle())()`

`[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getNumberOwner](#getNumberOwner())()`
Deprecated.
use getInstance(element).numberOwner().getStereotype()
`[DataType](../../uml2/ext/magicdraw/classes/mdkernel/DataType.html)`
`[getReqNumber](#getReqNumber())()`

`[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getRequirementTable](#getRequirementTable())()`
Deprecated.
use getInstance(element).requirementTable().getStereotype()
`[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getRequirementTerms](#getRequirementTerms())()`
Deprecated.
use getInstance(element).requirementTerms().getStereotype()
`[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)`
`[getVerificationStatus](#getVerificationStatus())()`
Deprecated.
use getInstance(element).verificationStatus().getStereotype()
`static boolean`
`[isNumberOwner](#isNumberOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use NumberOwnerStereotype.isInstance(element)
`static boolean`
`[isRequirementTable](#isRequirementTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use RequirementTableStereotype.isInstance(element)
`static boolean`
`[isRequirementTerms](#isRequirementTerms(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use RequirementTermsStereotype.isInstance(element)
`static boolean`
`[isVerificationStatus](#isVerificationStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element))([Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)`
Deprecated.
use VerificationStatusStereotype.isInstance(element)
`[MDCustomizationForRequirements.NumberOwnerStereotype](MDCustomizationForRequirements.NumberOwnerStereotype.html)`
`[numberOwner](#numberOwner())()`

`[MDCustomizationForRequirements.RequirementTableStereotype](MDCustomizationForRequirements.RequirementTableStereotype.html)`
`[requirementTable](#requirementTable())()`

`[MDCustomizationForRequirements.RequirementTermsStereotype](MDCustomizationForRequirements.RequirementTermsStereotype.html)`
`[requirementTerms](#requirementTerms())()`

`[MDCustomizationForRequirements.VerificationStatusStereotype](MDCustomizationForRequirements.VerificationStatusStereotype.html)`
`[verificationStatus](#verificationStatus())()`
Methods inherited from class com.nomagic.profiles.[ProfileImplementation](../../profiles/ProfileImplementation.html)
`[clearCache](../../profiles/ProfileImplementation.html#clearCache()), [findByRelativeQualifiedName](../../profiles/ProfileImplementation.html#findByRelativeQualifiedName(java.lang.String,java.lang.Class)), [getAllStereotypes](../../profiles/ProfileImplementation.html#getAllStereotypes()), [getCache](../../profiles/ProfileImplementation.html#getCache()), [getDataType](../../profiles/ProfileImplementation.html#getDataType(java.lang.String)), [getProfile](../../profiles/ProfileImplementation.html#getProfile()), [getStereotype](../../profiles/ProfileImplementation.html#getStereotype(java.lang.String)), [isTypeOf](../../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)), [isTypeOf](../../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)), [valueFromString](../../profiles/ProfileImplementation.html#valueFromString(java.lang.Class,java.lang.Object))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
PROFILE_URI
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_URI
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.PROFILE_URI)
PROFILE_NAME
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) PROFILE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.PROFILE_NAME)
REQNUMBER_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQNUMBER_DATATYPE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQNUMBER_DATATYPE)
NUMBERINGSTYLE_DATATYPE
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBERINGSTYLE_DATATYPE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBERINGSTYLE_DATATYPE)
NUMBERINGSTYLE_NESTED_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBERINGSTYLE_NESTED_LITERAL
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBERINGSTYLE_NESTED_LITERAL)
NUMBERINGSTYLE_NORMAL_LITERAL
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBERINGSTYLE_NORMAL_LITERAL
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBERINGSTYLE_NORMAL_LITERAL)
REQUIREMENTTABLE_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTABLE_STEREOTYPE
Deprecated.
use RequirementTableStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_STEREOTYPE)
REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY
Deprecated.
use RequirementTableStereotype.COLUMNSWIDTH
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY)
REQUIREMENTTABLE_CONTEXT_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTABLE_CONTEXT_PROPERTY
Deprecated.
use RequirementTableStereotype.CONTEXT
Specify a Block or an Instance for the context-specific analysis of the Requirements verification using the Bounds, Property, Margin, and Value columns.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_CONTEXT_PROPERTY)
REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY
Deprecated.
use RequirementTableStereotype.CUSTOMCOLUMNELEMENTS
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY)
REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY
Deprecated.
use RequirementTableStereotype.SHOWCOLUMNS
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY)
REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY
Deprecated.
use RequirementTableStereotype.SHOWCONTEXT
Set to true to show the Context box in the Criteria area of the table.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY)
REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY
Deprecated.
use RequirementTableStereotype.SHOWCUSTOMCOLUMNS
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY)
REQUIREMENTTERMS_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) REQUIREMENTTERMS_STEREOTYPE
Deprecated.
use RequirementTermsStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTERMS_STEREOTYPE)
VERIFICATIONSTATUS_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VERIFICATIONSTATUS_STEREOTYPE
Deprecated.
use VerificationStatusStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_STEREOTYPE)
VERIFICATIONSTATUS_CONSTRAINT_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VERIFICATIONSTATUS_CONSTRAINT_PROPERTY
Deprecated.
use VerificationStatusStereotype.CONSTRAINT
The related constraints of value specification.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_CONSTRAINT_PROPERTY)
VERIFICATIONSTATUS_MARGIN_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VERIFICATIONSTATUS_MARGIN_PROPERTY
Deprecated.
use VerificationStatusStereotype.MARGIN
Requirement margin
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_MARGIN_PROPERTY)
VERIFICATIONSTATUS_REQUIREMENT_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VERIFICATIONSTATUS_REQUIREMENT_PROPERTY
Deprecated.
use VerificationStatusStereotype.REQUIREMENT
The related requirement of value specification.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_REQUIREMENT_PROPERTY)
VERIFICATIONSTATUS_STATUS_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VERIFICATIONSTATUS_STATUS_PROPERTY
Deprecated.
use VerificationStatusStereotype.STATUS
The status of value specification.
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_STATUS_PROPERTY)
VERIFICATIONSTATUS_TIMESTAMP_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VERIFICATIONSTATUS_TIMESTAMP_PROPERTY
Deprecated.
use VerificationStatusStereotype.TIMESTAMP
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_TIMESTAMP_PROPERTY)
NUMBEROWNER_STEREOTYPE
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROWNER_STEREOTYPE
Deprecated.
use NumberOwnerStereotype.STEREOTYPE_NAME
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_STEREOTYPE)
NUMBEROWNER_NUMBERINGSTYLE_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROWNER_NUMBERINGSTYLE_PROPERTY
Deprecated.
use NumberOwnerStereotype.NUMBERINGSTYLE
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_NUMBERINGSTYLE_PROPERTY)
NUMBEROWNER_PREFIX_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROWNER_PREFIX_PROPERTY
Deprecated.
use NumberOwnerStereotype.PREFIX
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_PREFIX_PROPERTY)
NUMBEROWNER_SEPARATOR_PROPERTY
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NUMBEROWNER_SEPARATOR_PROPERTY
Deprecated.
use NumberOwnerStereotype.SEPARATOR
See Also:
[Constant Field Values](../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_SEPARATOR_PROPERTY)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
MDCustomizationForRequirements
public MDCustomizationForRequirements(com.nomagic.profiles.ProfileCache cache)
 ============ METHOD DETAIL ========== 
Method Details
getInstance
public static [MDCustomizationForRequirements](MDCustomizationForRequirements.html) getInstance([BaseElement](../../magicdraw/uml/BaseElement.html) baseElement)
getInstanceByProject
public static [MDCustomizationForRequirements](MDCustomizationForRequirements.html) getInstanceByProject(com.nomagic.uml2.project.ElementProject project)
requirementTable
public [MDCustomizationForRequirements.RequirementTableStereotype](MDCustomizationForRequirements.RequirementTableStereotype.html) requirementTable()
requirementTerms
public [MDCustomizationForRequirements.RequirementTermsStereotype](MDCustomizationForRequirements.RequirementTermsStereotype.html) requirementTerms()
verificationStatus
public [MDCustomizationForRequirements.VerificationStatusStereotype](MDCustomizationForRequirements.VerificationStatusStereotype.html) verificationStatus()
numberOwner
public [MDCustomizationForRequirements.NumberOwnerStereotype](MDCustomizationForRequirements.NumberOwnerStereotype.html) numberOwner()
getReqNumber
public [DataType](../../uml2/ext/magicdraw/classes/mdkernel/DataType.html) getReqNumber()
getNumberingStyle
public [Enumeration](../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html) getNumberingStyle()
getRequirementTable
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getRequirementTable()
Deprecated.
use getInstance(element).requirementTable().getStereotype()
p {padding:0px; margin:0px;}
**A Requirements Table** allows you to organize your requirements in a tabular form. As requirements are text-based, this table provides a convenient way for filling-in requirements' information using a spreadsheet-like tabular format, instead of limited-size boxes in a diagram. Each row in the table represents a requirement. The table columns represents the properties of each requirement in the table. With this table, you can:
 Create new requirements directly in the table, or import the existing ones from your model to the table.
Directly edit the properties of the requirements in the table.
Directly generate requirement reports, renumber requirements' IDs, or export the table into CSV or HTML format.

There are 3 methods to add requirement(s) to the table:
1. Create a new requirement and add to the table.
Click the **"Add New"** button on the table toolbar, and then select a requirement types you would like to create from the drop-down menu. The owner of the newly-created requirement will be similar to the owner of the table.
To select a different owner, hold Shift and then select a requirement type from the drop-down menu.
Shortcut: **Insert** (**Cmd+I** on MAC)

2. Create a new nested requirement and add to the table.
Click the **"Add Nested"** button on the table toolbar while an existing requirement is highlighted in the table, and then select a requirement types you would like to create from the drop-down menu. The owner of the newly-created requirement will be the highlighted requirement.
Alternatively, just right-click the requirement row in the table, and then select **Add Nested** option in the displayed shortcut menu.
Shortcut: **Alt+Insert**(**Alt+I** on MAC).

3. Add existing requirement(s) to the table.
Click **"Add Existing"** button. In the dialog, select requirement(s) already existed in your model to display it(them) in the table.
Or, directly drag existing requirement(s) from a browser to the table.
Shortcut: **Ctrl+Insert** (**Cmd+E** on MAC) Additional commands are available when right-click on a cell in the table.
Returns:
stereotype
isRequirementTable
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isRequirementTable(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use RequirementTableStereotype.isInstance(element)
getRequirementTerms
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getRequirementTerms()
Deprecated.
use getInstance(element).requirementTerms().getStereotype()
isRequirementTerms
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isRequirementTerms(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use RequirementTermsStereotype.isInstance(element)
getVerificationStatus
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getVerificationStatus()
Deprecated.
use getInstance(element).verificationStatus().getStereotype()
This stereotype is created by Cameo Simulation Toolkit plugin for tracing the last result of constraint verification.
Returns:
stereotype
isVerificationStatus
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isVerificationStatus(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use VerificationStatusStereotype.isInstance(element)
getNumberOwner
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public [Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) getNumberOwner()
Deprecated.
use getInstance(element).numberOwner().getStereotype()
isNumberOwner
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public static boolean isNumberOwner(@CheckForNull
 [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element)
Deprecated.
use NumberOwnerStereotype.isInstance(element)
generatedGetAllElementWrappers
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper> generatedGetAllElementWrappers()
Description copied from class: `[ProfileImplementation](../../profiles/ProfileImplementation.html#generatedGetAllElementWrappers())`
Generated method for getting all stereotype wrappers contained within this profile.
Specified by:
`[generatedGetAllElementWrappers](../../profiles/ProfileImplementation.html#generatedGetAllElementWrappers())` in class `[ProfileImplementation](../../profiles/ProfileImplementation.html)`
Returns:
gets all stereotype wrappers contained within this profile.
generatedGetAllStereotypes
protected [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> generatedGetAllStereotypes()
Description copied from class: `[ProfileImplementation](../../profiles/ProfileImplementation.html#generatedGetAllStereotypes())`
Generated method for getting all stereotypes contained within this profile.
Specified by:
`[generatedGetAllStereotypes](../../profiles/ProfileImplementation.html#generatedGetAllStereotypes())` in class `[ProfileImplementation](../../profiles/ProfileImplementation.html)`
Returns:
gets all stereotypes contained within this profile.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.requirements.util</a></div>
<h1 class="title" title="Class MDCustomizationForRequirements">Class MDCustomizationForRequirements</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">com.nomagic.profiles.ProfileImplementation</a>
<div class="inheritance">com.nomagic.requirements.util.MDCustomizationForRequirements</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">MDCustomizationForRequirements</span>
<span class="extends-implements">extends <a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></span></div>
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
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MDCustomizationForRequirements.NumberingStyleEnum.html" title="enum class in com.nomagic.requirements.util">MDCustomizationForRequirements.NumberingStyleEnum</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="MDCustomizationForRequirements.NumberOwnerStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.NumberOwnerStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MDCustomizationForRequirements.RequirementTableStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.RequirementTableStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="MDCustomizationForRequirements.RequirementTermsStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.RequirementTermsStereotype</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="MDCustomizationForRequirements.VerificationStatusStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.VerificationStatusStereotype</a></code></div>
<div class="col-last even-row-color"> </div>
</div>
<div class="inherited-list">
<h2 id="nested-classes-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Nested classes/interfaces inherited from class com.nomagic.profiles.<a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h2>
<code><a href="../../profiles/ProfileImplementation.StereotypeWrapper.html" title="class in com.nomagic.profiles">ProfileImplementation.StereotypeWrapper</a></code></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBERINGSTYLE_DATATYPE">NUMBERINGSTYLE_DATATYPE</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBERINGSTYLE_NESTED_LITERAL">NUMBERINGSTYLE_NESTED_LITERAL</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBERINGSTYLE_NORMAL_LITERAL">NUMBERINGSTYLE_NORMAL_LITERAL</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBEROWNER_NUMBERINGSTYLE_PROPERTY">NUMBEROWNER_NUMBERINGSTYLE_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.NUMBERINGSTYLE</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBEROWNER_PREFIX_PROPERTY">NUMBEROWNER_PREFIX_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.PREFIX</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#NUMBEROWNER_SEPARATOR_PROPERTY">NUMBEROWNER_SEPARATOR_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.SEPARATOR</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NUMBEROWNER_STEREOTYPE">NUMBEROWNER_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#PROFILE_NAME">PROFILE_NAME</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#PROFILE_URI">PROFILE_URI</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQNUMBER_DATATYPE">REQNUMBER_DATATYPE</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY">REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.COLUMNSWIDTH</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQUIREMENTTABLE_CONTEXT_PROPERTY">REQUIREMENTTABLE_CONTEXT_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.CONTEXT</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY">REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.CUSTOMCOLUMNELEMENTS</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY">REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.SHOWCOLUMNS</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY">REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.SHOWCONTEXT</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY">REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.SHOWCUSTOMCOLUMNS</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#REQUIREMENTTABLE_STEREOTYPE">REQUIREMENTTABLE_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#REQUIREMENTTERMS_STEREOTYPE">REQUIREMENTTERMS_STEREOTYPE</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTermsStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VERIFICATIONSTATUS_CONSTRAINT_PROPERTY">VERIFICATIONSTATUS_CONSTRAINT_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.CONSTRAINT</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VERIFICATIONSTATUS_MARGIN_PROPERTY">VERIFICATIONSTATUS_MARGIN_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.MARGIN</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VERIFICATIONSTATUS_REQUIREMENT_PROPERTY">VERIFICATIONSTATUS_REQUIREMENT_PROPERTY</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.REQUIREMENT</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VERIFICATIONSTATUS_STATUS_PROPERTY">VERIFICATIONSTATUS_STATUS_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.STATUS</div>
</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VERIFICATIONSTATUS_STEREOTYPE">VERIFICATIONSTATUS_STEREOTYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.STEREOTYPE_NAME</div>
</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#VERIFICATIONSTATUS_TIMESTAMP_PROPERTY">VERIFICATIONSTATUS_TIMESTAMP_PROPERTY</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.TIMESTAMP</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.profiles.ProfileCache)">MDCustomizationForRequirements</a><wbr/>(com.nomagic.profiles.ProfileCache cache)</code></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>protected <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#generatedGetAllStereotypes()">generatedGetAllStereotypes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MDCustomizationForRequirements.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstance(com.nomagic.magicdraw.uml.BaseElement)">getInstance</a><wbr/>(<a href="../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="MDCustomizationForRequirements.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#getInstanceByProject(com.nomagic.uml2.project.ElementProject)">getInstanceByProject</a><wbr/>(com.nomagic.uml2.project.ElementProject project)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNumberingStyle()">getNumberingStyle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getNumberOwner()">getNumberOwner</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).numberOwner().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getReqNumber()">getReqNumber</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRequirementTable()">getRequirementTable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).requirementTable().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getRequirementTerms()">getRequirementTerms</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).requirementTerms().getStereotype()</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getVerificationStatus()">getVerificationStatus</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).verificationStatus().getStereotype()</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isNumberOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isNumberOwner</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isRequirementTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRequirementTable</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isRequirementTerms(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isRequirementTerms</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTermsStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#isVerificationStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">isVerificationStatus</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.isInstance(element)</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDCustomizationForRequirements.NumberOwnerStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.NumberOwnerStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#numberOwner()">numberOwner</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDCustomizationForRequirements.RequirementTableStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.RequirementTableStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#requirementTable()">requirementTable</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDCustomizationForRequirements.RequirementTermsStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.RequirementTermsStereotype</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#requirementTerms()">requirementTerms</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="MDCustomizationForRequirements.VerificationStatusStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.VerificationStatusStereotype</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#verificationStatus()">verificationStatus</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.profiles.ProfileImplementation">Methods inherited from class com.nomagic.profiles.<a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></h3>
<code><a href="../../profiles/ProfileImplementation.html#clearCache()">clearCache</a>, <a href="../../profiles/ProfileImplementation.html#findByRelativeQualifiedName(java.lang.String,java.lang.Class)">findByRelativeQualifiedName</a>, <a href="../../profiles/ProfileImplementation.html#getAllStereotypes()">getAllStereotypes</a>, <a href="../../profiles/ProfileImplementation.html#getCache()">getCache</a>, <a href="../../profiles/ProfileImplementation.html#getDataType(java.lang.String)">getDataType</a>, <a href="../../profiles/ProfileImplementation.html#getProfile()">getProfile</a>, <a href="../../profiles/ProfileImplementation.html#getStereotype(java.lang.String)">getStereotype</a>, <a href="../../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype)">isTypeOf</a>, <a href="../../profiles/ProfileImplementation.html#isTypeOf(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String)">isTypeOf</a>, <a href="../../profiles/ProfileImplementation.html#valueFromString(java.lang.Class,java.lang.Object)">valueFromString</a></code></div>
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
<section class="detail" id="PROFILE_URI">
<h3>PROFILE_URI</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">PROFILE_URI</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.PROFILE_URI">Constant Field Values</a></li>
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
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.PROFILE_NAME">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQNUMBER_DATATYPE">
<h3>REQNUMBER_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQNUMBER_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQNUMBER_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBERINGSTYLE_DATATYPE">
<h3>NUMBERINGSTYLE_DATATYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBERINGSTYLE_DATATYPE</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBERINGSTYLE_DATATYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBERINGSTYLE_NESTED_LITERAL">
<h3>NUMBERINGSTYLE_NESTED_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBERINGSTYLE_NESTED_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBERINGSTYLE_NESTED_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBERINGSTYLE_NORMAL_LITERAL">
<h3>NUMBERINGSTYLE_NORMAL_LITERAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBERINGSTYLE_NORMAL_LITERAL</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBERINGSTYLE_NORMAL_LITERAL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTABLE_STEREOTYPE">
<h3>REQUIREMENTTABLE_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTABLE_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY">
<h3>REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.COLUMNSWIDTH</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_COLUMNSWIDTH_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTABLE_CONTEXT_PROPERTY">
<h3>REQUIREMENTTABLE_CONTEXT_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTABLE_CONTEXT_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.CONTEXT</div>
</div>
<div class="block">Specify a Block or an Instance for the context-specific analysis of the Requirements verification using the Bounds, Property, Margin, and Value columns.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_CONTEXT_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY">
<h3>REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.CUSTOMCOLUMNELEMENTS</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_CUSTOMCOLUMNELEMENTS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY">
<h3>REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.SHOWCOLUMNS</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_SHOWCOLUMNS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY">
<h3>REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.SHOWCONTEXT</div>
</div>
<div class="block">Set to true to show the Context box in the Criteria area of the table.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_SHOWCONTEXT_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY">
<h3>REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.SHOWCUSTOMCOLUMNS</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTABLE_SHOWCUSTOMCOLUMNS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="REQUIREMENTTERMS_STEREOTYPE">
<h3>REQUIREMENTTERMS_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">REQUIREMENTTERMS_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTermsStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.REQUIREMENTTERMS_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATIONSTATUS_STEREOTYPE">
<h3>VERIFICATIONSTATUS_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VERIFICATIONSTATUS_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATIONSTATUS_CONSTRAINT_PROPERTY">
<h3>VERIFICATIONSTATUS_CONSTRAINT_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VERIFICATIONSTATUS_CONSTRAINT_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.CONSTRAINT</div>
</div>
<div class="block">The related constraints of value specification.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_CONSTRAINT_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATIONSTATUS_MARGIN_PROPERTY">
<h3>VERIFICATIONSTATUS_MARGIN_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VERIFICATIONSTATUS_MARGIN_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.MARGIN</div>
</div>
<div class="block">Requirement margin</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_MARGIN_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATIONSTATUS_REQUIREMENT_PROPERTY">
<h3>VERIFICATIONSTATUS_REQUIREMENT_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VERIFICATIONSTATUS_REQUIREMENT_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.REQUIREMENT</div>
</div>
<div class="block">The related requirement of value specification.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_REQUIREMENT_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATIONSTATUS_STATUS_PROPERTY">
<h3>VERIFICATIONSTATUS_STATUS_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VERIFICATIONSTATUS_STATUS_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.STATUS</div>
</div>
<div class="block">The status of value specification.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_STATUS_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VERIFICATIONSTATUS_TIMESTAMP_PROPERTY">
<h3>VERIFICATIONSTATUS_TIMESTAMP_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VERIFICATIONSTATUS_TIMESTAMP_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.TIMESTAMP</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.VERIFICATIONSTATUS_TIMESTAMP_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROWNER_STEREOTYPE">
<h3>NUMBEROWNER_STEREOTYPE</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROWNER_STEREOTYPE</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.STEREOTYPE_NAME</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_STEREOTYPE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROWNER_NUMBERINGSTYLE_PROPERTY">
<h3>NUMBEROWNER_NUMBERINGSTYLE_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROWNER_NUMBERINGSTYLE_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.NUMBERINGSTYLE</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_NUMBERINGSTYLE_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROWNER_PREFIX_PROPERTY">
<h3>NUMBEROWNER_PREFIX_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROWNER_PREFIX_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.PREFIX</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_PREFIX_PROPERTY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NUMBEROWNER_SEPARATOR_PROPERTY">
<h3>NUMBEROWNER_SEPARATOR_PROPERTY</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NUMBEROWNER_SEPARATOR_PROPERTY</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.SEPARATOR</div>
</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../constant-values.html#com.nomagic.requirements.util.MDCustomizationForRequirements.NUMBEROWNER_SEPARATOR_PROPERTY">Constant Field Values</a></li>
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
<h3>MDCustomizationForRequirements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MDCustomizationForRequirements</span><wbr/><span class="parameters">(com.nomagic.profiles.ProfileCache cache)</span></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MDCustomizationForRequirements.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements</a></span> <span class="element-name">getInstance</span><wbr/><span class="parameters">(<a href="../../magicdraw/uml/BaseElement.html" title="interface in com.nomagic.magicdraw.uml">BaseElement</a> baseElement)</span></div>
</section>
</li>
<li>
<section class="detail" id="getInstanceByProject(com.nomagic.uml2.project.ElementProject)">
<h3>getInstanceByProject</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="MDCustomizationForRequirements.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements</a></span> <span class="element-name">getInstanceByProject</span><wbr/><span class="parameters">(com.nomagic.uml2.project.ElementProject project)</span></div>
</section>
</li>
<li>
<section class="detail" id="requirementTable()">
<h3>requirementTable</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MDCustomizationForRequirements.RequirementTableStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.RequirementTableStereotype</a></span> <span class="element-name">requirementTable</span>()</div>
</section>
</li>
<li>
<section class="detail" id="requirementTerms()">
<h3>requirementTerms</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MDCustomizationForRequirements.RequirementTermsStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.RequirementTermsStereotype</a></span> <span class="element-name">requirementTerms</span>()</div>
</section>
</li>
<li>
<section class="detail" id="verificationStatus()">
<h3>verificationStatus</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MDCustomizationForRequirements.VerificationStatusStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.VerificationStatusStereotype</a></span> <span class="element-name">verificationStatus</span>()</div>
</section>
</li>
<li>
<section class="detail" id="numberOwner()">
<h3>numberOwner</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="MDCustomizationForRequirements.NumberOwnerStereotype.html" title="class in com.nomagic.requirements.util">MDCustomizationForRequirements.NumberOwnerStereotype</a></span> <span class="element-name">numberOwner</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getReqNumber()">
<h3>getReqNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/DataType.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">DataType</a></span> <span class="element-name">getReqNumber</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getNumberingStyle()">
<h3>getNumberingStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Enumeration.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Enumeration</a></span> <span class="element-name">getNumberingStyle</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getRequirementTable()">
<h3>getRequirementTable</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getRequirementTable</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).requirementTable().getStereotype()</div>
</div>
<div class="block"><html>
<head>
<style>
 p {padding:0px; margin:0px;}
 </style>
</head>
<body>
<b>A Requirements Table</b> allows you to organize your requirements in a tabular form. As requirements are text-based, this table provides a convenient way for filling-in requirements' information using a spreadsheet-like tabular format, instead of limited-size boxes in a diagram. Each row in the table represents a requirement. The table columns represents the properties of each requirement in the table. With this table, you can:
 <ul>
<li>
 Create new requirements directly in the table, or import the existing ones from your model to the table.

 </li>
<li>
 Directly edit the properties of the requirements in the table.

 </li>
<li>
 Directly generate requirement reports, renumber requirements' IDs, or export the table into CSV or HTML format.

 </li>
</ul>
<p>
  

 </p>
<p>
 There are 3 methods to add requirement(s) to the table:

 </p>
<p>
 1. Create a new requirement and add to the table.

 </p>
<ul>
<li>
 Click the <b>"Add New"</b> button on the table toolbar, and then select a requirement types you would like to create from the drop-down menu. The owner of the newly-created requirement will be similar to the owner of the table.

 </li>
<li>
 To select a different owner, hold Shift and then select a requirement type from the drop-down menu.

 </li>
<li>
 Shortcut: <b>Insert</b> (<b>Cmd+I</b> on MAC)

 </li>
</ul>
<p>
  

 </p>
<p>
 2. Create a new nested requirement and add to the table.

 </p>
<ul>
<li>
 Click the <b>"Add Nested"</b> button on the table toolbar while an existing requirement is highlighted in the table, and then select a requirement types you would like to create from the drop-down menu. The owner of the newly-created requirement will be the highlighted requirement.

 </li>
<li>
 Alternatively, just right-click the requirement row in the table, and then select <b>Add Nested</b> option in the displayed shortcut menu.

 </li>
<li>
 Shortcut: <b>Alt+Insert </b>(<b>Alt+I</b> on MAC).

 </li>
</ul>
<p>
  

 </p>
<p>
 3. Add existing requirement(s) to the table.

 </p>
<ul>
<li>
 Click <b>"Add Existing"</b> button. In the dialog, select requirement(s) already existed in your model to display it(them) in the table.

 </li>
<li>
 Or, directly drag existing requirement(s) from a browser to the table.

 </li>
<li>
 Shortcut: <b>Ctrl+Insert</b> (<b>Cmd+E</b> on MAC) Additional commands are available when right-click on a cell in the table.

 </li>
</ul>
</body>
</html></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isRequirementTable(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRequirementTable</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequirementTable</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTableStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getRequirementTerms()">
<h3>getRequirementTerms</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getRequirementTerms</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).requirementTerms().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isRequirementTerms(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isRequirementTerms</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isRequirementTerms</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use RequirementTermsStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getVerificationStatus()">
<h3>getVerificationStatus</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getVerificationStatus</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).verificationStatus().getStereotype()</div>
</div>
<div class="block">This stereotype is created by Cameo Simulation Toolkit plugin for tracing the last result of constraint verification.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>stereotype</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isVerificationStatus(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isVerificationStatus</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isVerificationStatus</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use VerificationStatusStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="getNumberOwner()">
<h3>getNumberOwner</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a></span> <span class="element-name">getNumberOwner</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use getInstance(element).numberOwner().getStereotype()</div>
</div>
</section>
</li>
<li>
<section class="detail" id="isNumberOwner(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element)">
<h3>isNumberOwner</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isNumberOwner</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use NumberOwnerStereotype.isInstance(element)</div>
</div>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllElementWrappers()">
<h3>generatedGetAllElementWrappers</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;com.nomagic.profiles.ProfileImplementation.ProfileElementWrapper&gt;</span> <span class="element-name">generatedGetAllElementWrappers</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../profiles/ProfileImplementation.html#generatedGetAllElementWrappers()">ProfileImplementation</a></code></span></div>
<div class="block">Generated method for getting all stereotype wrappers contained within this profile.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../profiles/ProfileImplementation.html#generatedGetAllElementWrappers()">generatedGetAllElementWrappers</a></code> in class <code><a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></code></dd>
<dt>Returns:</dt>
<dd>gets all stereotype wrappers contained within this profile.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="generatedGetAllStereotypes()">
<h3>generatedGetAllStereotypes</h3>
<div class="member-signature"><span class="modifiers">protected</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt;</span> <span class="element-name">generatedGetAllStereotypes</span>()</div>
<div class="block"><span class="descfrm-type-label">Description copied from class: <code><a href="../../profiles/ProfileImplementation.html#generatedGetAllStereotypes()">ProfileImplementation</a></code></span></div>
<div class="block">Generated method for getting all stereotypes contained within this profile.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="../../profiles/ProfileImplementation.html#generatedGetAllStereotypes()">generatedGetAllStereotypes</a></code> in class <code><a href="../../profiles/ProfileImplementation.html" title="class in com.nomagic.profiles">ProfileImplementation</a></code></dd>
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
