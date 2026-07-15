# JAVA OPENAPI: CoreTextCreator (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/uml/text/CoreTextCreator.html
- source_path: `com/nomagic/magicdraw/uml/text/CoreTextCreator.html`
- source_sha256: `00d8eac0b52b5e1ad329162d7d0da43c79a8c0add6e3aa4cd95ba143fff20a1e`
- captured_utc: `2026-07-14T16:52:19.458978+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.uml.text](package-summary.html)

## Class CoreTextCreator

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.nomagic.magicdraw.uml.text.CoreTextCreator

Direct Known Subclasses:
`[ModelTextCreator](ModelTextCreator.html)`

@OpenApiAllpublic classCoreTextCreator
extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

Contains methods to create representation text for model elements that are commonly used as property values of other elements

=========== FIELD SUMMARY =========== 
Field Summary
Fields
Modifier and Type
Field
Description
`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[NEW_LINE_SEPARATOR](#NEW_LINE_SEPARATOR)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[TYPE_SEPARATOR](#TYPE_SEPARATOR)`

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[VALUE_SEPARATOR](#VALUE_SEPARATOR)`
 ======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[CoreTextCreator](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsStatic MethodsConcrete Methods
Modifier and Type
Method
Description
`protected static boolean`
`[containsParentheses](#containsParentheses(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)`

`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createElementNumberText](#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Create the element's number (auto id) text
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityRangeText](#createMultiplicityRangeText(java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) range)`
Creates multiplicity range text.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createMultiplicityText](#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier))([TextBuilder](../../../text/builders/TextBuilder.html) lower,
 [TextBuilder](../../../text/builders/TextBuilder.html) upper,
 boolean ordered,
 boolean unique,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Returns text representation of given multiplicity.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createMultiplicityText](#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier))([TextBuilder](../../../text/builders/TextBuilder.html) lower,
 [TextBuilder](../../../text/builders/TextBuilder.html) upper,
 [ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) lowerValue,
 boolean unique,
 boolean ordered,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the provided multiplicity range.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createMultiplicityText](#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier))([MultiplicityElement](../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates text representation of given element [`MultiplicityElement`](../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html).
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityText](#createMultiplicityText(java.lang.Integer,java.lang.Integer))([Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lower,
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) upper)`
Creates multiplicity text.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityText](#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 boolean ordered,
 boolean unique,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams)`
Creates text representation of given multiplicity range.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createMultiplicityText](#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 [ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) lowerValue,
 boolean unique,
 boolean ordered,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams)`
Creates string representation of the provided multiplicity range.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createNamedElementListText](#createNamedElementListText(java.util.List,java.util.function.Supplier))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> elements,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates representation text for a list of named elements, which contains names separated by a comma.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createStereotypesText](#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 [StereotypeTextParams](StereotypeTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of stereotypes that are applied to the provided element
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createStereotypesText](#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 [StereotypeTextParams](StereotypeTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation for the collection of [`Stereotype`](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) elements.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createStereotypeText](#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier))([Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [StereotypeTextParams](StereotypeTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`Stereotype`](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html).
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createStereotypeText](#createStereotypeText(java.lang.String))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)`

`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createStringCollectionText](#createStringCollectionText(java.util.Collection,java.lang.String,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> strings,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Joins strings
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createStyledTypeText](#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier))([Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates colored string representation of the given `Type`.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createStyledTypeTextWithSeparator](#createStyledTypeTextWithSeparator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier))([Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates colored string representation of the given `Type`.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTypeText](#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier))([Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given `Type`.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createTypeText](#createTypeText(java.util.Collection,boolean,java.util.function.Supplier))([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html)> types,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given `Type` elements, separated by comma.
`static [TextBuilder](../../../text/builders/TextBuilder.html)`
`[createValueSpecificationText](#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier))([ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 boolean addBraces,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)`
Creates string representation of the given [`ValueSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html).
`static <T extends [TextBuilder](../../../text/builders/TextBuilder.html)> 
T`
`[createValueSpecificationText](#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier))([ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> builderFactory)`
Creates string representation of the given [`ValueSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) with no braces.
`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`
`[createVisibilityText](#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind))([VisibilityKind](../../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html) visibility)`
Returns visibility representation(+, # or -)
`static boolean`
`[isUseStandardStereotypeChar](#isUseStandardStereotypeChar())()`

`protected static <T> [TextBuilder](../../../text/builders/TextBuilder.html)`
`[join](#join(com.nomagic.text.builders.TextBuilder,java.lang.String,java.util.stream.Stream,java.util.function.Function))([TextBuilder](../../../text/builders/TextBuilder.html) textBuilder,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<T> elements,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<T,[TextBuilder](../../../text/builders/TextBuilder.html)> map)`

`static void`
`[setUseStandardStereotypeChar](#setUseStandardStereotypeChar(boolean))(boolean useStandardStereotypeChar)`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`

============ FIELD DETAIL =========== 
Field Details
TYPE_SEPARATOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TYPE_SEPARATOR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.CoreTextCreator.TYPE_SEPARATOR)
NEW_LINE_SEPARATOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NEW_LINE_SEPARATOR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.CoreTextCreator.NEW_LINE_SEPARATOR)
VALUE_SEPARATOR
public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) VALUE_SEPARATOR
See Also:
[Constant Field Values](../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.CoreTextCreator.VALUE_SEPARATOR)
 ========= CONSTRUCTOR DETAIL ======== 
Constructor Details
CoreTextCreator
public CoreTextCreator()
 ============ METHOD DETAIL ========== 
Method Details
isUseStandardStereotypeChar
public static boolean isUseStandardStereotypeChar()
setUseStandardStereotypeChar
public static void setUseStandardStereotypeChar(boolean useStandardStereotypeChar)
createTypeText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTypeText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<? extends [Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html)> types,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given `Type` elements, separated by comma.
Parameters:
`types` - collection of types
`showQualifiedName` - true to include type's qualified name
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the types' text appended
createTypeText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createTypeText([Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given `Type`.
Parameters:
`type` - element to create representation text for
`showQualifiedName` - true to include type's qualified name
`builderFactory` - provides[`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the type's text appended
createStyledTypeText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createStyledTypeText([Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates colored string representation of the given `Type`.
Parameters:
`type` - element to create representation text for
`showQualifiedName` - true to include type's qualified name
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the type's text appended
createStyledTypeTextWithSeparator
public static [TextBuilder](../../../text/builders/TextBuilder.html) createStyledTypeTextWithSeparator([Type](../../../uml2/ext/magicdraw/classes/mdkernel/Type.html) type,
 boolean showQualifiedName,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates colored string representation of the given `Type`.
 Pre-appends CoreTextCreator.TYPE_SEPARATOR
Parameters:
`type` - element to create representation text for
`showQualifiedName` - true to include type's qualified name
`builderFactory` - provides[`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the type's text appended
createStringCollectionText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createStringCollectionText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)> strings,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Joins strings
Parameters:
`strings` - strings to join
`separator` - symbol(s) to separate each string with
`builderFactory` - provides[`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the joined strings appended
createNamedElementListText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createNamedElementListText([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)<? extends [NamedElement](../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html)> elements,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates representation text for a list of named elements, which contains names separated by a comma.
 Only names of the first 5 elements are included, and "..." is added in there are more elements in the list.
Parameters:
`elements` - to create joined named representation for
Returns:
builder with the element names appended
createValueSpecificationText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createValueSpecificationText(@CheckForNull
 [ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 boolean addBraces,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`ValueSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html).
Parameters:
`valueSpecification` - element to create representation text for
`addBraces` - true to add braces around the value specification text
`builderFactory` - provides[`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the value specification's text appended
createValueSpecificationText
public static <T extends [TextBuilder](../../../text/builders/TextBuilder.html)> T createValueSpecificationText(@CheckForNull
 [ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) valueSpecification,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<T> builderFactory)
Creates string representation of the given [`ValueSpecification`](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) with no braces.
Parameters:
`valueSpecification` - element to create representation text for
`builderFactory` - provides[`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the value specification's text appended
createMultiplicityText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityText([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 @CheckForNull
 [ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) lowerValue,
 boolean unique,
 boolean ordered,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams)
Creates string representation of the provided multiplicity range.
Parameters:
`lower` - lower bounds of the multiplicity
`upper` - upper bounds of the multiplicity
`lowerValue` - value specification element that holds the value of the lower bounds
`ordered` - is ordered
`unique` - is unique
`textParams` - text parameters
Returns:
builder with the multiplicity's text appended
createMultiplicityText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createMultiplicityText([TextBuilder](../../../text/builders/TextBuilder.html) lower,
 [TextBuilder](../../../text/builders/TextBuilder.html) upper,
 @CheckForNull
 [ValueSpecification](../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html) lowerValue,
 boolean unique,
 boolean ordered,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the provided multiplicity range.
Parameters:
`lower` - lower bounds of the multiplicity
`upper` - upper bounds of the multiplicity
`lowerValue` - value specification element that holds the value of the lower bounds
`ordered` - is ordered
`unique` - is unique
`textParams` - text parameters
Returns:
builder with the multiplicity's text appended
createMultiplicityRangeText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityRangeText(@CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) range)
Creates multiplicity range text.
Parameters:
`range` - multiplicity range.
Returns:
multiplicity range string representation.
createMultiplicityText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityText(@CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lower,
 @CheckForNull
 [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) upper)
Creates multiplicity text.
Parameters:
`lower` - Lower range.
`upper` - Upper range.
Returns:
representation text of multiplicity value.
createMultiplicityText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createMultiplicityText([TextBuilder](../../../text/builders/TextBuilder.html) lower,
 [TextBuilder](../../../text/builders/TextBuilder.html) upper,
 boolean ordered,
 boolean unique,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Returns text representation of given multiplicity.
Parameters:
`lower` - Lower value
`upper` - Upper value
`ordered` - ordered
`unique` - unique
`textParams` - text parameters
Returns:
builder with multiplicity's representation or empty string if multiplicity is null.
createMultiplicityText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createMultiplicityText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lower,
 @CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) upper,
 boolean ordered,
 boolean unique,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams)
Creates text representation of given multiplicity range.
Parameters:
`lower` - Lower value
`upper` - Upper value
`ordered` - ordered
`unique` - unique
`textParams` - text parameters
Returns:
text representation or empty string if multiplicity is null
createMultiplicityText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createMultiplicityText(@CheckForNull
 [MultiplicityElement](../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html) element,
 [MultiplicityTextParams](MultiplicityTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates text representation of given element [`MultiplicityElement`](../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html).
Parameters:
`element` - the given multiplicity element
`textParams` - text parameters
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the multiplicity text appended
join
protected static <T> [TextBuilder](../../../text/builders/TextBuilder.html) join([TextBuilder](../../../text/builders/TextBuilder.html) textBuilder,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) delimiter,
 [Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)<T> elements,
 [Function](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html)<T,[TextBuilder](../../../text/builders/TextBuilder.html)> map)
createVisibilityText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createVisibilityText(@CheckForNull
 [VisibilityKind](../../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html) visibility)
Returns visibility representation(+, # or -)
Parameters:
`visibility` - the given visibility.
Returns:
the char representation of given visibility.
createStereotypesText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createStereotypesText([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 [StereotypeTextParams](StereotypeTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of stereotypes that are applied to the provided element
Parameters:
`element` - to create representation text for
`separator` - symbol(s) to separate each stereotype's text with
`textParams` - text parameters
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the stereotypes' text appended
createStereotypesText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createStereotypesText([Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)<[Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html)> stereotypes,
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) separator,
 [StereotypeTextParams](StereotypeTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation for the collection of [`Stereotype`](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) elements.
Parameters:
`stereotypes` - collection of stereotypes to create representation text for
`separator` - symbol(s) to separate each stereotype's text with
`textParams` - configuration that defines what to include in the text of each stereotype
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the stereotypes' text appended
createStereotypeText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createStereotypeText([Stereotype](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html) stereotype,
 [StereotypeTextParams](StereotypeTextParams.html) textParams,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Creates string representation of the given [`Stereotype`](../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html).
Parameters:
`stereotype` - element to create representation text for
`textParams` - configuration that defines what to include in the text of the stereotype
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the stereotype's text appended
createStereotypeText
public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) createStereotypeText(@CheckForNull
 [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) stereotypeName)
containsParentheses
protected static boolean containsParentheses([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) string)
createElementNumberText
public static [TextBuilder](../../../text/builders/TextBuilder.html) createElementNumberText([Element](../../../uml2/ext/magicdraw/classes/mdkernel/Element.html) element,
 [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html)<[TextBuilder](../../../text/builders/TextBuilder.html)> builderFactory)
Create the element's number (auto id) text
Parameters:
`element` - the element that can be numbered
`builderFactory` - provides [`TextBuilder`](../../../text/builders/TextBuilder.html) to append the created text to
Returns:
builder with the number + space at the end or empty string if the number is not available

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.uml.text</a></div>
<h1 class="title" title="Class CoreTextCreator">Class CoreTextCreator</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.nomagic.magicdraw.uml.text.CoreTextCreator</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Direct Known Subclasses:</dt>
<dd><code><a href="ModelTextCreator.html" title="class in com.nomagic.magicdraw.uml.text">ModelTextCreator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">CoreTextCreator</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Contains methods to create representation text for model elements that are commonly used as property values of other elements</div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#NEW_LINE_SEPARATOR">NEW_LINE_SEPARATOR</a></code></div>
<div class="col-last even-row-color"> </div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TYPE_SEPARATOR">TYPE_SEPARATOR</a></code></div>
<div class="col-last odd-row-color"> </div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#VALUE_SEPARATOR">VALUE_SEPARATOR</a></code></div>
<div class="col-last even-row-color"> </div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">CoreTextCreator</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#containsParentheses(java.lang.String)">containsParentheses</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier)">createElementNumberText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create the element's number (auto id) text</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityRangeText(java.lang.Integer)">createMultiplicityRangeText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> range)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates multiplicity range text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">createMultiplicityText</a><wbr/>(<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> lower,
 <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> upper,
 boolean ordered,
 boolean unique,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns text representation of given multiplicity.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">createMultiplicityText</a><wbr/>(<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> lower,
 <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> upper,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> lowerValue,
 boolean unique,
 boolean ordered,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the provided multiplicity range.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">createMultiplicityText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates text representation of given element <a href="../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>MultiplicityElement</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityText(java.lang.Integer,java.lang.Integer)">createMultiplicityText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> upper)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates multiplicity text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)">createMultiplicityText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 boolean ordered,
 boolean unique,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates text representation of given multiplicity range.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)">createMultiplicityText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> lowerValue,
 boolean unique,
 boolean ordered,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the provided multiplicity range.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createNamedElementListText(java.util.List,java.util.function.Supplier)">createNamedElementListText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates representation text for a list of named elements, which contains names separated by a comma.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">createStereotypesText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a href="StereotypeTextParams.html" title="class in com.nomagic.magicdraw.uml.text">StereotypeTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of stereotypes that are applied to the provided element</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">createStereotypesText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a href="StereotypeTextParams.html" title="class in com.nomagic.magicdraw.uml.text">StereotypeTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation for the collection of <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a> elements.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">createStereotypeText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="StereotypeTextParams.html" title="class in com.nomagic.magicdraw.uml.text">StereotypeTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStereotypeText(java.lang.String)">createStereotypeText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStringCollectionText(java.util.Collection,java.lang.String,java.util.function.Supplier)">createStringCollectionText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; strings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Joins strings</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">createStyledTypeText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates colored string representation of the given <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createStyledTypeTextWithSeparator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">createStyledTypeTextWithSeparator</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates colored string representation of the given <code>Type</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">createTypeText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <code>Type</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createTypeText(java.util.Collection,boolean,java.util.function.Supplier)">createTypeText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt; types,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <code>Type</code> elements, separated by comma.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier)">createValueSpecificationText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 boolean addBraces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static &lt;T extends <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt;<br/>T</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier)">createValueSpecificationText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; builderFactory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a> with no braces.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">createVisibilityText</a><wbr/>(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns visibility representation(+, # or -)</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#isUseStandardStereotypeChar()">isUseStandardStereotypeChar</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>protected static &lt;T&gt; <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#join(com.nomagic.text.builders.TextBuilder,java.lang.String,java.util.stream.Stream,java.util.function.Function)">join</a><wbr/>(<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> textBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;T,<wbr/><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; map)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setUseStandardStereotypeChar(boolean)">setUseStandardStereotypeChar</a><wbr/>(boolean useStandardStereotypeChar)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"> </div>
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
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">
<h2>Field Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="TYPE_SEPARATOR">
<h3>TYPE_SEPARATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TYPE_SEPARATOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.CoreTextCreator.TYPE_SEPARATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="NEW_LINE_SEPARATOR">
<h3>NEW_LINE_SEPARATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">NEW_LINE_SEPARATOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.CoreTextCreator.NEW_LINE_SEPARATOR">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="VALUE_SEPARATOR">
<h3>VALUE_SEPARATOR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">VALUE_SEPARATOR</span></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="../../../../../constant-values.html#com.nomagic.magicdraw.uml.text.CoreTextCreator.VALUE_SEPARATOR">Constant Field Values</a></li>
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
<h3>CoreTextCreator</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CoreTextCreator</span>()</div>
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
<section class="detail" id="isUseStandardStereotypeChar()">
<h3>isUseStandardStereotypeChar</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">boolean</span> <span class="element-name">isUseStandardStereotypeChar</span>()</div>
</section>
</li>
<li>
<section class="detail" id="setUseStandardStereotypeChar(boolean)">
<h3>setUseStandardStereotypeChar</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setUseStandardStereotypeChar</span><wbr/><span class="parameters">(boolean useStandardStereotypeChar)</span></div>
</section>
</li>
<li>
<section class="detail" id="createTypeText(java.util.Collection,boolean,java.util.function.Supplier)">
<h3>createTypeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTypeText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a>&gt; types,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <code>Type</code> elements, separated by comma.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>types</code> - collection of types</dd>
<dd><code>showQualifiedName</code> - true to include type's qualified name</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the types' text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">
<h3>createTypeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createTypeText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <code>Type</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element to create representation text for</dd>
<dd><code>showQualifiedName</code> - true to include type's qualified name</dd>
<dd><code>builderFactory</code> - provides<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the type's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStyledTypeText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">
<h3>createStyledTypeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createStyledTypeText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates colored string representation of the given <code>Type</code>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element to create representation text for</dd>
<dd><code>showQualifiedName</code> - true to include type's qualified name</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the type's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStyledTypeTextWithSeparator(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Type,boolean,java.util.function.Supplier)">
<h3>createStyledTypeTextWithSeparator</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createStyledTypeTextWithSeparator</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Type.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Type</a> type,
 boolean showQualifiedName,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates colored string representation of the given <code>Type</code>.
 Pre-appends CoreTextCreator.TYPE_SEPARATOR</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - element to create representation text for</dd>
<dd><code>showQualifiedName</code> - true to include type's qualified name</dd>
<dd><code>builderFactory</code> - provides<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the type's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStringCollectionText(java.util.Collection,java.lang.String,java.util.function.Supplier)">
<h3>createStringCollectionText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createStringCollectionText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; strings,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Joins strings</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>strings</code> - strings to join</dd>
<dd><code>separator</code> - symbol(s) to separate each string with</dd>
<dd><code>builderFactory</code> - provides<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the joined strings appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createNamedElementListText(java.util.List,java.util.function.Supplier)">
<h3>createNamedElementListText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createNamedElementListText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;? extends <a href="../../../uml2/ext/magicdraw/classes/mdkernel/NamedElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">NamedElement</a>&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates representation text for a list of named elements, which contains names separated by a comma.
 Only names of the first 5 elements are included, and "..." is added in there are more elements in the list.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>elements</code> - to create joined named representation for</dd>
<dt>Returns:</dt>
<dd>builder with the element names appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,java.util.function.Supplier)">
<h3>createValueSpecificationText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createValueSpecificationText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 boolean addBraces,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecification</code> - element to create representation text for</dd>
<dd><code>addBraces</code> - true to add braces around the value specification text</dd>
<dd><code>builderFactory</code> - provides<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the value specification's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createValueSpecificationText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,java.util.function.Supplier)">
<h3>createValueSpecificationText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="type-parameters">&lt;T extends <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt;</span> <span class="return-type">T</span> <span class="element-name">createValueSpecificationText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> valueSpecification,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;T&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>ValueSpecification</code></a> with no braces.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>valueSpecification</code> - element to create representation text for</dd>
<dd><code>builderFactory</code> - provides<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the value specification's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(java.lang.String,java.lang.String,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> lowerValue,
 boolean unique,
 boolean ordered,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams)</span></div>
<div class="block">Creates string representation of the provided multiplicity range.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lower</code> - lower bounds of the multiplicity</dd>
<dd><code>upper</code> - upper bounds of the multiplicity</dd>
<dd><code>lowerValue</code> - value specification element that holds the value of the lower bounds</dd>
<dd><code>ordered</code> - is ordered</dd>
<dd><code>unique</code> - is unique</dd>
<dd><code>textParams</code> - text parameters</dd>
<dt>Returns:</dt>
<dd>builder with the multiplicity's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,com.nomagic.uml2.ext.magicdraw.classes.mdkernel.ValueSpecification,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> lower,
 <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> upper,
 @CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/ValueSpecification.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">ValueSpecification</a> lowerValue,
 boolean unique,
 boolean ordered,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the provided multiplicity range.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lower</code> - lower bounds of the multiplicity</dd>
<dd><code>upper</code> - upper bounds of the multiplicity</dd>
<dd><code>lowerValue</code> - value specification element that holds the value of the lower bounds</dd>
<dd><code>ordered</code> - is ordered</dd>
<dd><code>unique</code> - is unique</dd>
<dd><code>textParams</code> - text parameters</dd>
<dt>Returns:</dt>
<dd>builder with the multiplicity's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityRangeText(java.lang.Integer)">
<h3>createMultiplicityRangeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityRangeText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> range)</span></div>
<div class="block">Creates multiplicity range text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>range</code> - multiplicity range.</dd>
<dt>Returns:</dt>
<dd>multiplicity range string representation.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(java.lang.Integer,java.lang.Integer)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lower,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> upper)</span></div>
<div class="block">Creates multiplicity text.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lower</code> - Lower range.</dd>
<dd><code>upper</code> - Upper range.</dd>
<dt>Returns:</dt>
<dd>representation text of multiplicity value.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(com.nomagic.text.builders.TextBuilder,com.nomagic.text.builders.TextBuilder,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> lower,
 <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> upper,
 boolean ordered,
 boolean unique,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Returns text representation of given multiplicity.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lower</code> - Lower value</dd>
<dd><code>upper</code> - Upper value</dd>
<dd><code>ordered</code> - ordered</dd>
<dd><code>unique</code> - unique</dd>
<dd><code>textParams</code> - text parameters</dd>
<dt>Returns:</dt>
<dd>builder with multiplicity's representation or empty string if multiplicity is null.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(java.lang.String,java.lang.String,boolean,boolean,com.nomagic.magicdraw.uml.text.MultiplicityTextParams)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> lower,
 @CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> upper,
 boolean ordered,
 boolean unique,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams)</span></div>
<div class="block">Creates text representation of given multiplicity range.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lower</code> - Lower value</dd>
<dd><code>upper</code> - Upper value</dd>
<dd><code>ordered</code> - ordered</dd>
<dd><code>unique</code> - unique</dd>
<dd><code>textParams</code> - text parameters</dd>
<dt>Returns:</dt>
<dd>text representation or empty string if multiplicity is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createMultiplicityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.MultiplicityElement,com.nomagic.magicdraw.uml.text.MultiplicityTextParams,java.util.function.Supplier)">
<h3>createMultiplicityText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createMultiplicityText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">MultiplicityElement</a> element,
 <a href="MultiplicityTextParams.html" title="class in com.nomagic.magicdraw.uml.text">MultiplicityTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates text representation of given element <a href="../../../uml2/ext/magicdraw/classes/mdkernel/MultiplicityElement.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel"><code>MultiplicityElement</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the given multiplicity element</dd>
<dd><code>textParams</code> - text parameters</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the multiplicity text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="join(com.nomagic.text.builders.TextBuilder,java.lang.String,java.util.stream.Stream,java.util.function.Function)">
<h3>join</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="type-parameters">&lt;T&gt;</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">join</span><wbr/><span class="parameters">(<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a> textBuilder,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> delimiter,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html" title="class or interface in java.util.stream">Stream</a>&lt;T&gt; elements,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Function.html" title="class or interface in java.util.function">Function</a>&lt;T,<wbr/><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; map)</span></div>
</section>
</li>
<li>
<section class="detail" id="createVisibilityText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.VisibilityKind)">
<h3>createVisibilityText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createVisibilityText</span><wbr/><span class="parameters">(@CheckForNull
 <a href="../../../uml2/ext/magicdraw/classes/mdkernel/VisibilityKind.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">VisibilityKind</a> visibility)</span></div>
<div class="block">Returns visibility representation(+, # or -)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>visibility</code> - the given visibility.</dd>
<dt>Returns:</dt>
<dd>the char representation of given visibility.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypesText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">
<h3>createStereotypesText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createStereotypesText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a href="StereotypeTextParams.html" title="class in com.nomagic.magicdraw.uml.text">StereotypeTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of stereotypes that are applied to the provided element</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - to create representation text for</dd>
<dd><code>separator</code> - symbol(s) to separate each stereotype's text with</dd>
<dd><code>textParams</code> - text parameters</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the stereotypes' text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypesText(java.util.Collection,java.lang.String,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">
<h3>createStereotypesText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createStereotypesText</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html" title="class or interface in java.util">Collection</a>&lt;<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a>&gt; stereotypes,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> separator,
 <a href="StereotypeTextParams.html" title="class in com.nomagic.magicdraw.uml.text">StereotypeTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation for the collection of <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a> elements.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotypes</code> - collection of stereotypes to create representation text for</dd>
<dd><code>separator</code> - symbol(s) to separate each stereotype's text with</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of each stereotype</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the stereotypes' text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypeText(com.nomagic.uml2.ext.magicdraw.mdprofiles.Stereotype,com.nomagic.magicdraw.uml.text.StereotypeTextParams,java.util.function.Supplier)">
<h3>createStereotypeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createStereotypeText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles">Stereotype</a> stereotype,
 <a href="StereotypeTextParams.html" title="class in com.nomagic.magicdraw.uml.text">StereotypeTextParams</a> textParams,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Creates string representation of the given <a href="../../../uml2/ext/magicdraw/mdprofiles/Stereotype.html" title="interface in com.nomagic.uml2.ext.magicdraw.mdprofiles"><code>Stereotype</code></a>.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>stereotype</code> - element to create representation text for</dd>
<dd><code>textParams</code> - configuration that defines what to include in the text of the stereotype</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the stereotype's text appended</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="createStereotypeText(java.lang.String)">
<h3>createStereotypeText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">createStereotypeText</span><wbr/><span class="parameters">(@CheckForNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> stereotypeName)</span></div>
</section>
</li>
<li>
<section class="detail" id="containsParentheses(java.lang.String)">
<h3>containsParentheses</h3>
<div class="member-signature"><span class="modifiers">protected static</span> <span class="return-type">boolean</span> <span class="element-name">containsParentheses</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> string)</span></div>
</section>
</li>
<li>
<section class="detail" id="createElementNumberText(com.nomagic.uml2.ext.magicdraw.classes.mdkernel.Element,java.util.function.Supplier)">
<h3>createElementNumberText</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a></span> <span class="element-name">createElementNumberText</span><wbr/><span class="parameters">(<a href="../../../uml2/ext/magicdraw/classes/mdkernel/Element.html" title="interface in com.nomagic.uml2.ext.magicdraw.classes.mdkernel">Element</a> element,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html" title="class or interface in java.util.function">Supplier</a>&lt;<a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders">TextBuilder</a>&gt; builderFactory)</span></div>
<div class="block">Create the element's number (auto id) text</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>element</code> - the element that can be numbered</dd>
<dd><code>builderFactory</code> - provides <a href="../../../text/builders/TextBuilder.html" title="interface in com.nomagic.text.builders"><code>TextBuilder</code></a> to append the created text to</dd>
<dt>Returns:</dt>
<dd>builder with the number + space at the end or empty string if the number is not available</dd>
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
