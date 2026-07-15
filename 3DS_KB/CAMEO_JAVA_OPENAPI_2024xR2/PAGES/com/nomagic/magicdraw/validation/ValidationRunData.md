# JAVA OPENAPI: ValidationRunData (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh2/com/nomagic/magicdraw/validation/ValidationRunData.html
- source_path: `com/nomagic/magicdraw/validation/ValidationRunData.html`
- source_sha256: `feeae4bf2e98adac944aad8331a68298edd277b85262577e6f215104548c4bba`
- captured_utc: `2026-07-14T16:56:01.906531+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.validation](package-summary.html)

## Class ValidationRunData

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.validation.ValidationRunData

@OpenApiAllpublic classValidationRunData
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Parameters information for validation operation.

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ValidationRunData](#%3Cinit%3E(boolean,java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))(boolean wholeProject,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true.
`[ValidationRunData](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 boolean wholeProject,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true.
`[ValidationRunData](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 boolean wholeProject,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)`
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true.
`[ValidationRunData](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Validation data for specific constraints on the whole project scope
`[ValidationRunData](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)`
Validation data for specific constraints on the whole project scope
`[ValidationRunData](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`

`[ValidationRunData](#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean))([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)`

`[ValidationRunData](#%3Cinit%3E(java.util.Collection,java.lang.String,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean wholeProject,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true.
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,java.lang.String,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean wholeProject,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)`
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true.
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Validation data for specific constraints on the whole project scope
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)`
Validation data for specific constraints on the whole project scope
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Validation data for specific constraints.
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)`
Validation data for specific constraints.
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,com.nomagic.magicdraw.validation.Scope,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 [Scope](Scope.html) scope,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Constructs validation run data.
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
Validation data for specific constraints on the whole project scope
`[ValidationRunData](#%3Cinit%3E(java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete MethodsDeprecated Methods
Modifier and Type
Method
Description
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)>`
`[getConstraints](#getConstraints())()`
Validation constraints
`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getCustomSuccessMessage](#getCustomSuccessMessage())()`

`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)>`
`[getElements](#getElements())()`
The selected elements to run validation on.
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)>`
`[getIgnoredConstraints](#getIgnoredConstraints())()`

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[getName](#getName())()`
Gets name of the suite.
`[Project](../core/Project.html)`
`[getProject](#getProject())()`
Get project where the validation data is located.
`[Scope](Scope.html)`
`[getScope](#getScope())()`
Gets validation scope.
`[EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html)`
`[getSeverity](#getSeverity())()`
Minimum validation severity level.
`[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)`
`[getSuite](#getSuite())()`
Deprecated.
use [`getSuites()`](#getSuites())
`[Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)>`
`[getSuites](#getSuites())()`
Gets suits to be used in validation.
`boolean`
`[isAddElementsRecursively](#isAddElementsRecursively())()`
Should validation engine add scope elements recursively, or should it validate only provided scope.
`boolean`
`[isEnableSettingsDialog](#isEnableSettingsDialog())()`

`boolean`
`[isExcludeAdditionalContent](#isExcludeAdditionalContent())()`

`boolean`
`[isExcludeReadOnly](#isExcludeReadOnly())()`

`boolean`
`[isTrackActiveDiagrams](#isTrackActiveDiagrams())()`

`boolean`
`[isWholeProject](#isWholeProject())()`
Validation is run on whole project
`void`
`[setAddElementsRecursively](#setAddElementsRecursively(boolean))(boolean addElementsRecursively)`
Should validation engine add scope elements recursively, or should it validate only provided scope.
`void`
`[setCustomSuccessMessage](#setCustomSuccessMessage(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) customSuccessMessage)`
Set custom validation result message.
`void`
`[setEnableSettingsDialog](#setEnableSettingsDialog(boolean))(boolean enableSettingsDialog)`
Disable "Run validation with a new settings" button in the validation results window.
`void`
`[setExcludeAdditionalContent](#setExcludeAdditionalContent(boolean))(boolean excludeAdditionalContent)`

`void`
`[setExcludeReadOnly](#setExcludeReadOnly(boolean))(boolean excludeReadOnly)`

`void`
`[setIgnoredConstraints](#setIgnoredConstraints(java.util.Collection))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> ignoredConstraints)`
Collection of constraints to ignore
`void`
`[setTrackActiveDiagrams](#setTrackActiveDiagrams(boolean))(boolean trackActiveDiagrams)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ValidationRunData
public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Parameters:
`suites` - suites to execute.
`elements` - elements to validate. Their children recursively will also be validated unless [`setAddElementsRecursively(boolean)`](#setAddElementsRecursively(boolean))
 is called with false parameter
`severity` - minimum severity level
ValidationRunData
public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Validation data for specific constraints on the whole project scope
Parameters:
`suites` - suites to execute.
`severity` - minimum severity level
ValidationRunData
public ValidationRunData([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Validation data for specific constraints on the whole project scope
Parameters:
`suite` - suite to execute.
`severity` - minimum severity level
ValidationRunData
public ValidationRunData([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)
Validation data for specific constraints on the whole project scope
Parameters:
`suite` - suite to execute.
`severity` - minimum severity level
`excludeReadOnly` - exclude readonly elements from execution
ValidationRunData
public ValidationRunData([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Parameters:
`suite` - suite to execute.
`elements` - elements to validate. Their children recursively will also be validated unless [`setAddElementsRecursively(boolean)`](#setAddElementsRecursively(boolean))
 is called with false parameter
`severity` - minimum severity level
ValidationRunData
public ValidationRunData([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)
Parameters:
`suite` - suite to execute.
`elements` - elements to validate. Their children recursively will also be validated unless [`setAddElementsRecursively(boolean)`](#setAddElementsRecursively(boolean))
 is called with false parameter
`severity` - minimum severity level
`excludeReadOnly` - exclude readonly elements from execution
ValidationRunData
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public ValidationRunData([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 boolean wholeProject,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor
ValidationRunData
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public ValidationRunData([Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) suite,
 boolean wholeProject,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor
ValidationRunData
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public ValidationRunData(boolean wholeProject,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor
ValidationRunData
public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> suites,
 [Scope](Scope.html) scope,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Constructs validation run data.
Parameters:
`suites` - suites from which to take constraints.
`scope` - scope to validate.
`severity` - minimum severity level.
ValidationRunData
public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Validation data for specific constraints.
Parameters:
`constraints` - constraints to run
`name` - name for rule collection (like suite name)
`elements` - elements to validate. Their children recursively will also be validated unless [`setAddElementsRecursively(boolean)`](#setAddElementsRecursively(boolean))
 is called with false parameter
`severity` - minimum severity level
ValidationRunData
public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)
Validation data for specific constraints.
Parameters:
`constraints` - constraints to run
`name` - name for rule collection (like suite name)
`elements` - elements to validate
`severity` - minimum severity level
`excludeReadOnly` - exclude readonly elements from execution
ValidationRunData
public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Validation data for specific constraints on the whole project scope
Parameters:
`constraints` - constraints to run
`name` - name for rule collection (like suite name)
`severity` - minimum severity level
ValidationRunData
public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)
Validation data for specific constraints on the whole project scope
Parameters:
`constraints` - constraints to run
`name` - name for rule collection (like suite name)
`severity` - minimum severity level
`excludeReadOnly` - exclude readonly elements from execution
ValidationRunData
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean wholeProject,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity)
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor
ValidationRunData
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)public ValidationRunData([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> constraints,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name,
 boolean wholeProject,
 @CheckForNull
 [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> elements,
 @CheckForNull
 [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) severity,
 boolean excludeReadOnly)
Deprecated.
confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor
 ============ METHOD DETAIL ========== 
Method Details
setEnableSettingsDialog
public void setEnableSettingsDialog(boolean enableSettingsDialog)
Disable "Run validation with a new settings" button in the validation results window. Default value - true;
Parameters:
`enableSettingsDialog` - value
isEnableSettingsDialog
public boolean isEnableSettingsDialog()
setCustomSuccessMessage
public void setCustomSuccessMessage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) customSuccessMessage)
Set custom validation result message. If null - default is shown.
Parameters:
`customSuccessMessage` - Message text
getCustomSuccessMessage
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCustomSuccessMessage()
setExcludeReadOnly
public void setExcludeReadOnly(boolean excludeReadOnly)
isExcludeReadOnly
public boolean isExcludeReadOnly()
setExcludeAdditionalContent
public void setExcludeAdditionalContent(boolean excludeAdditionalContent)
isExcludeAdditionalContent
public boolean isExcludeAdditionalContent()
getName
public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()
Gets name of the suite. If suite was not assigned, then name value returned be defined by the constructor.
Returns:
name of the suite (constraint collection)
getSuite
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html)
@CheckForNullpublic [Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html) getSuite()
Deprecated.
use [`getSuites()`](#getSuites())
The suite of constraints to run on some target elements.
Returns:
suite
getSuites
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Package](../../uml2/ext/magicdraw/classes/mdkernel/Package.html)> getSuites()
Gets suits to be used in validation.
Returns:
suits to be used in validation.
getElements
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Element](../../uml2/ext/magicdraw/classes/mdkernel/Element.html)> getElements()
The selected elements to run validation on.
Returns:
scope
getSeverity
@CheckForNullpublic [EnumerationLiteral](../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html) getSeverity()
Minimum validation severity level.
Returns:
severity
getConstraints
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> getConstraints()
Validation constraints
Returns:
constraints. either from suite, either internal.
isWholeProject
public boolean isWholeProject()
Validation is run on whole project
Returns:
will run on whole project
getProject
public [Project](../core/Project.html) getProject()
Get project where the validation data is located. Returns `null` if no suite or constraints specified.
Returns:
validation suite/rule parent project
isAddElementsRecursively
public boolean isAddElementsRecursively()
Should validation engine add scope elements recursively, or should it validate only provided scope. Default is `true`
Returns:
true if elements should be added recursively
setAddElementsRecursively
public void setAddElementsRecursively(boolean addElementsRecursively)
Should validation engine add scope elements recursively, or should it validate only provided scope. Default is `true`
Parameters:
`addElementsRecursively` - true if elements should be added recursively
getScope
public [Scope](Scope.html) getScope()
Gets validation scope.
Returns:
validation scope.
setIgnoredConstraints
public void setIgnoredConstraints([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> ignoredConstraints)
Collection of constraints to ignore
Parameters:
`ignoredConstraints` - constraints to ignore
getIgnoredConstraints
public [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Constraint](../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html)> getIgnoredConstraints()
Returns:
ignored constraints
isTrackActiveDiagrams
public boolean isTrackActiveDiagrams()
setTrackActiveDiagrams
public void setTrackActiveDiagrams(boolean trackActiveDiagrams)

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.validation</a></div>
<h1 class="title" title="Class ValidationRunData">Class ValidationRunData</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.validation.ValidationRunData</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ValidationRunData</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Parameters information for validation operation.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(boolean,java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(boolean wholeProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true.</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 boolean wholeProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true.</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">ValidationRunData</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 boolean wholeProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true.</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block">Validation data for specific constraints on the whole project scope</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">ValidationRunData</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color">
<div class="block">Validation data for specific constraints on the whole project scope</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">ValidationRunData</a><wbr/>(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color"> </div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.lang.String,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean wholeProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true.</div>
</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.lang.String,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean wholeProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true.</div>
</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block">Validation data for specific constraints on the whole project scope</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color">
<div class="block">Validation data for specific constraints on the whole project scope</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block">Validation data for specific constraints.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color">
<div class="block">Validation data for specific constraints.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,com.nomagic.magicdraw.validation.Scope,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 <a href="Scope.html" title="class in com.nomagic.magicdraw.validation">Scope</a> scope,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs validation run data.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last even-row-color">
<div class="block">Validation data for specific constraints on the whole project scope</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">ValidationRunData</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</code></div>
<div class="col-last odd-row-color"> </div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConstraints()">getConstraints</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validation constraints</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCustomSuccessMessage()">getCustomSuccessMessage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getElements()">getElements</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The selected elements to run validation on.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIgnoredConstraints()">getIgnoredConstraints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getName()">getName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets name of the suite.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProject()">getProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get project where the validation data is located.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="Scope.html" title="class in com.nomagic.magicdraw.validation">Scope</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getScope()">getScope</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets validation scope.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeverity()">getSeverity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Minimum validation severity level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#getSuite()">getSuite</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getSuites()"><code>getSuites()</code></a></div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSuites()">getSuites</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets suits to be used in validation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isAddElementsRecursively()">isAddElementsRecursively</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Should validation engine add scope elements recursively, or should it validate only provided scope.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isEnableSettingsDialog()">isEnableSettingsDialog</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExcludeAdditionalContent()">isExcludeAdditionalContent</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isExcludeReadOnly()">isExcludeReadOnly</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTrackActiveDiagrams()">isTrackActiveDiagrams</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isWholeProject()">isWholeProject</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Validation is run on whole project</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAddElementsRecursively(boolean)">setAddElementsRecursively</a><wbr/>(boolean addElementsRecursively)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Should validation engine add scope elements recursively, or should it validate only provided scope.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCustomSuccessMessage(java.lang.String)">setCustomSuccessMessage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> customSuccessMessage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Set custom validation result message.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setEnableSettingsDialog(boolean)">setEnableSettingsDialog</a><wbr/>(boolean enableSettingsDialog)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disable "Run validation with a new settings" button in the validation results window.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExcludeAdditionalContent(boolean)">setExcludeAdditionalContent</a><wbr/>(boolean excludeAdditionalContent)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setExcludeReadOnly(boolean)">setExcludeReadOnly</a><wbr/>(boolean excludeReadOnly)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setIgnoredConstraints(java.util.Collection)">setIgnoredConstraints</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; ignoredConstraints)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Collection of constraints to ignore</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTrackActiveDiagrams(boolean)">setTrackActiveDiagrams</a><wbr/>(boolean trackActiveDiagrams)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suites</code> - suites to execute.</dd>
<dd><code>elements</code> - elements to validate. Their children recursively will also be validated unless <a href="#setAddElementsRecursively(boolean)"><code>setAddElementsRecursively(boolean)</code></a>
                 is called with false parameter</dd>
<dd><code>severity</code> - minimum severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="block">Validation data for specific constraints on the whole project scope</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suites</code> - suites to execute.</dd>
<dd><code>severity</code> - minimum severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="block">Validation data for specific constraints on the whole project scope</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suite</code> - suite to execute.</dd>
<dd><code>severity</code> - minimum severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</span></div>
<div class="block">Validation data for specific constraints on the whole project scope</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suite</code> - suite to execute.</dd>
<dd><code>severity</code> - minimum severity level</dd>
<dd><code>excludeReadOnly</code> - exclude readonly elements from execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suite</code> - suite to execute.</dd>
<dd><code>elements</code> - elements to validate. Their children recursively will also be validated unless <a href="#setAddElementsRecursively(boolean)"><code>setAddElementsRecursively(boolean)</code></a>
                 is called with false parameter</dd>
<dd><code>severity</code> - minimum severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</span></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suite</code> - suite to execute.</dd>
<dd><code>elements</code> - elements to validate. Their children recursively will also be validated unless <a href="#setAddElementsRecursively(boolean)"><code>setAddElementsRecursively(boolean)</code></a>
                        is called with false parameter</dd>
<dd><code>severity</code> - minimum severity level</dd>
<dd><code>excludeReadOnly</code> - exclude readonly elements from execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 boolean wholeProject,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Package,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a> suite,
 boolean wholeProject,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(boolean,java.util.Collection,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(boolean wholeProject,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,com.nomagic.magicdraw.validation.Scope,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt; suites,
 <a href="Scope.html" title="class in com.nomagic.magicdraw.validation">Scope</a> scope,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="block">Constructs validation run data.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>suites</code> - suites from which to take constraints.</dd>
<dd><code>scope</code> - scope to validate.</dd>
<dd><code>severity</code> - minimum severity level.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="block">Validation data for specific constraints.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraints</code> - constraints to run</dd>
<dd><code>name</code> - name for rule collection (like suite name)</dd>
<dd><code>elements</code> - elements to validate. Their children recursively will also be validated unless <a href="#setAddElementsRecursively(boolean)"><code>setAddElementsRecursively(boolean)</code></a>
                    is called with false parameter</dd>
<dd><code>severity</code> - minimum severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.lang.String,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</span></div>
<div class="block">Validation data for specific constraints.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraints</code> - constraints to run</dd>
<dd><code>name</code> - name for rule collection (like suite name)</dd>
<dd><code>elements</code> - elements to validate</dd>
<dd><code>severity</code> - minimum severity level</dd>
<dd><code>excludeReadOnly</code> - exclude readonly elements from execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="block">Validation data for specific constraints on the whole project scope</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraints</code> - constraints to run</dd>
<dd><code>name</code> - name for rule collection (like suite name)</dd>
<dd><code>severity</code> - minimum severity level</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</span></div>
<div class="block">Validation data for specific constraints on the whole project scope</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>constraints</code> - constraints to run</dd>
<dd><code>name</code> - name for rule collection (like suite name)</dd>
<dd><code>severity</code> - minimum severity level</dd>
<dd><code>excludeReadOnly</code> - exclude readonly elements from execution</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.lang.String,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean wholeProject,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor</div>
</div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.Collection,java.lang.String,boolean,java.util.Collection,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.EnumerationLiteral,boolean)">
<h3>ValidationRunData</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="element-name">ValidationRunData</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; constraints,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 boolean wholeProject,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt; elements,
 @CheckForNull
 <a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a> severity,
 boolean excludeReadOnly)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">confusing constructor that allows both providing scope elements and setting wholeProject to true. Use another constructor</div>
</div>
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
<section class="detail" id="setEnableSettingsDialog(boolean)">
<h3>setEnableSettingsDialog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setEnableSettingsDialog</span><wbr/><span class="parameters">(boolean enableSettingsDialog)</span></div>
<div class="block">Disable "Run validation with a new settings" button in the validation results window. Default value - true;</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enableSettingsDialog</code> - value</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnableSettingsDialog()">
<h3>isEnableSettingsDialog</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isEnableSettingsDialog</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setCustomSuccessMessage(java.lang.String)">
<h3>setCustomSuccessMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCustomSuccessMessage</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> customSuccessMessage)</span></div>
<div class="block">Set custom validation result message. If null - default is shown.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>customSuccessMessage</code> - Message text</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCustomSuccessMessage()">
<h3>getCustomSuccessMessage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCustomSuccessMessage</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExcludeReadOnly(boolean)">
<h3>setExcludeReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExcludeReadOnly</span><wbr/><span class="parameters">(boolean excludeReadOnly)</span></div>
</section>
</li>
<li>
<section class="detail" id="isExcludeReadOnly()">
<h3>isExcludeReadOnly</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExcludeReadOnly</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setExcludeAdditionalContent(boolean)">
<h3>setExcludeAdditionalContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setExcludeAdditionalContent</span><wbr/><span class="parameters">(boolean excludeAdditionalContent)</span></div>
</section>
</li>
<li>
<section class="detail" id="isExcludeAdditionalContent()">
<h3>isExcludeAdditionalContent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExcludeAdditionalContent</span>()</div>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block">Gets name of the suite. If suite was not assigned, then name value returned be defined by the constructor.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>name of the suite (constraint collection)</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuite()">
<h3>getSuite</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a></span> <span class="element-name">getSuite</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">use <a href="#getSuites()"><code>getSuites()</code></a></div>
</div>
<div class="block">The suite of constraints to run on some target elements.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>suite</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSuites()">
<h3>getSuites</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Package.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Package</a>&gt;</span> <span class="element-name">getSuites</span>()</div>
<div class="block">Gets suits to be used in validation.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>suits to be used in validation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getElements()">
<h3>getElements</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a>&gt;</span> <span class="element-name">getElements</span>()</div>
<div class="block">The selected elements to run validation on.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>scope</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSeverity()">
<h3>getSeverity</h3>
<div class="member-signature"><span class="annotations">@CheckForNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../../uml2/ext/magicdraw/classes/mdkernel/EnumerationLiteral.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">EnumerationLiteral</a></span> <span class="element-name">getSeverity</span>()</div>
<div class="block">Minimum validation severity level.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>severity</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConstraints()">
<h3>getConstraints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getConstraints</span>()</div>
<div class="block">Validation constraints</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>constraints. either from suite, either internal.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isWholeProject()">
<h3>isWholeProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isWholeProject</span>()</div>
<div class="block">Validation is run on whole project</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>will run on whole project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProject()">
<h3>getProject</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a></span> <span class="element-name">getProject</span>()</div>
<div class="block">Get project where the validation data is located. Returns <code>null</code> if no suite or constraints specified.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>validation suite/rule parent project</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isAddElementsRecursively()">
<h3>isAddElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAddElementsRecursively</span>()</div>
<div class="block">Should validation engine add scope elements recursively, or should it validate only provided scope. Default is <code>true</code></div>
<dl class="notes">
<dt>Returns:</dt>
<dd>true if elements should be added recursively</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAddElementsRecursively(boolean)">
<h3>setAddElementsRecursively</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAddElementsRecursively</span><wbr/><span class="parameters">(boolean addElementsRecursively)</span></div>
<div class="block">Should validation engine add scope elements recursively, or should it validate only provided scope. Default is <code>true</code></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>addElementsRecursively</code> - true if elements should be added recursively</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScope()">
<h3>getScope</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="Scope.html" title="class in com.nomagic.magicdraw.validation">Scope</a></span> <span class="element-name">getScope</span>()</div>
<div class="block">Gets validation scope.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>validation scope.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIgnoredConstraints(java.util.Collection)">
<h3>setIgnoredConstraints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIgnoredConstraints</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt; ignoredConstraints)</span></div>
<div class="block">Collection of constraints to ignore</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ignoredConstraints</code> - constraints to ignore</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIgnoredConstraints()">
<h3>getIgnoredConstraints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../uml2/ext/magicdraw/classes/mdkernel/Constraint.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Constraint</a>&gt;</span> <span class="element-name">getIgnoredConstraints</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>ignored constraints</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTrackActiveDiagrams()">
<h3>isTrackActiveDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTrackActiveDiagrams</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setTrackActiveDiagrams(boolean)">
<h3>setTrackActiveDiagrams</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrackActiveDiagrams</span><wbr/><span class="parameters">(boolean trackActiveDiagrams)</span></div>
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
