# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=3251 end=3500 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/findindex-function.html language=enus -->
## TOPIC 03251: FindIndex Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/findindex-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/findindex-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String FindIndex(Array array, PropertyObject object, Boolean caseSensitive = True) Return Value String If found, returns the index string of the value. If not found, returns an empty string. Purpose This function searches for the first index of the specified value in the given array. The func

### FindIndex Function

#### Syntax

String FindIndex(Array array, PropertyObject object, Boolean caseSensitive = True)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

If found, returns the index string of the value. If not found, returns an empty string.

#### Purpose

This function searches for the first index of the specified value in the given array. The function returns the array bounds as a string with the syntax "[i][j][k]", with an integer value in square brackets for each dimension of the source array. Note: To obtain a numeric index result, use the FindOffset function instead of FindIndex.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

An array to search.

object
 as
 [PropertyObject](../tsapiref/propertyobject.html)

The value to be found.

caseSensitive
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

For string arrays, pass True to use a case-sensitive comparison.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/findoffset-function.html language=enus -->
## TOPIC 03252: FindOffset Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/findoffset-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/findoffset-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number FindOffset(Array array, PropertyObject object, Boolean caseSensitive = True) Return Value Number If the specified value found, returns the offset of the value. If the specified value not found, returns -1. Parameters array as Array An array to search. object as PropertyObject Value to

### FindOffset Function

#### Syntax

Number FindOffset(Array array, PropertyObject object, Boolean caseSensitive = True)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

If the specified value found, returns the offset of the value. If the specified value not found, returns -1.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

An array to search.

object
 as
 [PropertyObject](../tsapiref/propertyobject.html)

Value to be searched.

caseSensitive
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

For string arrays, pass True to use a case-sensitive comparison.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/findpattern-function.html language=enus -->
## TOPIC 03253: FindPattern Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/findpattern-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/findpattern-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number FindPattern(String string, String stringPatternToSearchFor, [Number indexToSearchFrom = 0], [Boolean ignoreCase = False], [Out] [Number patternLength]) Return Value Number Number containing the start index of the first substring matching the pattern. Returns -1 if the pattern is not fo

### FindPattern Function

#### Syntax

Number FindPattern(String string, String stringPatternToSearchFor, [Number indexToSearchFrom = 0], [Boolean ignoreCase = False], [Out] [Number patternLength])

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

Number containing the start index of the first substring matching the pattern. Returns -1 if the pattern is not found.

#### Purpose

This function searches for a substring that matches the regular expression pattern.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to compare against a pattern.

stringPatternToSearchFor
 as
 [String](../tsapiref/data-types-for-teststand.html)

The regular expression pattern to search for.

Note

Microsoft documentation for regular expressions

indexToSearchFrom
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) A number that specifies the zero-based character index at which to begin searching. The default is 0.

ignoreCase
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) A Boolean that specifies whether to ignore character case when searching. The default is False.

patternLength
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) A number representing the length of the substring matching the pattern.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/findstep-function.html language=enus -->
## TOPIC 03254: FindStep Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/findstep-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/findstep-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Step FindStep(PropertyObject propertyObject, String uniqueStepId) Return Value Step A reference to the Step object, if it was found. Otherwise, returns nothing. Purpose This function searches the propertyObject, which must be either a Sequence or a SequenceFile, for the step identified by the

### FindStep Function

#### Syntax

Step FindStep(PropertyObject propertyObject, String uniqueStepId)

#### Return Value

[Step](../tsapiref/data-types-for-teststand.html)

A reference to the Step object, if it was found. Otherwise, returns nothing.

#### Purpose

This function searches the propertyObject, which must be either a Sequence or a SequenceFile, for the step identified by the specified unique step Id.

#### Parameters

propertyObject
 as
 [PropertyObject](../tsapiref/propertyobject.html)

A Sequence or SequenceFile property object.

uniqueStepId
 as
 [String](../tsapiref/data-types-for-teststand.html)

A unique step Id string.

Parent topic:

Property Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/float64-function.html language=enus -->
## TOPIC 03255: Float64 Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/float64-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/float64-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Float64(AnyType value) Return Value Number This function converts a type to a number with a representation of Double Precision 64-bit Floating Point. The function cannot convert a container or array data type to a number, and cannot convert an empty string to a number. The TestStand Se

### Float64 Function

#### Syntax

Number Float64(AnyType value)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function converts a type to a number with a representation of Double Precision 64-bit Floating 
 Point. The function cannot convert a container or array data type to a number, and cannot convert an empty string to a number.

Note

#NoValidation

Float64

Locals.MyNumber = #NoValidation(Float64(Locals.MyEmptyString))

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/getarraybounds-function.html language=enus -->
## TOPIC 03256: GetArrayBounds Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/getarraybounds-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/getarraybounds-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number GetArrayBounds(Array array, [Out] String lowerBounds, [Out] String upperBounds) Return Value Number The function always returns 0. Purpose Determines whether the array contains a specified object. The function outputs the array bounds as strings with the syntax "[i][j][k]", with an int

### GetArrayBounds Function

#### Syntax

Number GetArrayBounds(Array array, [Out] String lowerBounds, [Out] String upperBounds)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The function always returns 0.

#### Purpose

Determines whether the array contains a specified object. The function outputs the array bounds as strings with the syntax "[i][j][k]", with an integer value in square brackets for each dimension of the source array.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

The array to examine.

lowerBounds
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string in which the function returns the index/indices of the array's smallest value.

upperBounds
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string in which the function returns the index/indices of the array's largest value.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/getdescription.html language=enus -->
## TOPIC 03257: GetDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/getdescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/getdescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: void GetDescription(long index, char *description, long maxDescriptionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes) Purpose Returns the description of the file extension the translator supports. TestStand uses the description in the Open File dialog box. Parameter

### GetDescription

void GetDescription(long index, char *description, long maxDescriptionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes)

#### Purpose

Returns the description of the file extension the translator supports. TestStand uses the description in the
 [Open File](../tsref/open-file-dialog-box.html)
 dialog box.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the translator in the DLL that must process the callback. |
| description | string | The description of the file extension the translator supports. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxDescriptionLengthInBytes parameter to determine the size of the buffer. |
| maxDescriptionLengthInBytes | long | The maximum number of bytes you can copy to the description parameter. |
| errorCode | TSERROR | The error code when an error occurs in the callback. |
| errorMsg | string | The error message when an error occurs in the callback. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxErrorMsgLengthInBytes parameter to determine the size of the buffer. |
| maxErrorMsgLengthInBytes | long | The maximum number of bytes the DLL can copy to the errorMsg parameter. |

#### See Also

[Open File dialog box](../tsref/open-file-dialog-box.html)

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/getengine-function.html language=enus -->
## TOPIC 03258: GetEngine Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/getengine-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/getengine-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine GetEngine() Return Value Engine a reference to the TestStand Engine. Expressions are typically evaluated against a SequenceContext object which provides access to the Engine through its RunState.Engine property. However, expressions can be evaluated without a SequenceContext using meth

### GetEngine Function

#### Syntax

Engine GetEngine()

#### Return Value

[Engine](../tsapiref/data-types-for-teststand.html)

a reference to the TestStand Engine. Expressions are typically evaluated against a SequenceContext object which provides access to the Engine through its RunState.Engine property. However, expressions can be evaluated without a SequenceContext using methods in the TestStand API. This function provides the expression access to the TestStand engine even if the expression is not evaluated against a SequenceContext.Returns: A reference to the TestStand Engine.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/getextension.html language=enus -->
## TOPIC 03259: GetExtension

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/getextension.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/getextension.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: void GetExtension(long index, char *extension, long maxExtensionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes) Purpose Returns the file extension the translator supports. Implement the callback to copy the extension string to the extension parameter without the per

### GetExtension

void GetExtension(long index, char *extension, long maxExtensionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes)

#### Purpose

Returns the file extension the translator supports. Implement the callback to copy the extension string to the
 extension
 parameter without the period character, for example,
 "txt"
 not
 ".txt"
 .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the translator in the DLL that must process the callback. |
| extension | string | The file extension for the files the translator supports. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxExtensionLengthInBytes parameter to determine the size of the buffer. |
| maxExtensionLengthInBytes | long | The maximum number of bytes you can copy to the extension parameter. |
| errorCode | TSError | Returns the error code when an error occurs in the callback. |
| errorMsg | string | The error message when an error occurs in the callback. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxErrorMsgLengthInBytes parameter to determine the size of the buffer. |
| maxErrorMsgLengthInBytes | long | The maximum number of bytes the DLL can copy to the errorMsg parameter. |

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/getfileformatversion.html language=enus -->
## TOPIC 03260: GetFileFormatVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/getfileformatversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/getfileformatversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: void GetFileFormatVersion(long index, const char *path, IDispatch *inputStream, char *fileFormatVersion, long maxVersionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes) Purpose The file format version for the file the path and inputStream parameters specify. Implemen

### GetFileFormatVersion

void GetFileFormatVersion(long index, const char *path, IDispatch *inputStream, char *fileFormatVersion, long maxVersionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes)

#### Purpose

The file format version for the file the path and
 inputStream
 parameters specify. Implement the callback to assign the file format version to the
 fileFormatVersion
 parameter. When the translator does not support reading file format version information from the file, assign an empty string to the
 fileFormatVersion
 parameter. TestStand calls this callback to return a version string for the
 [FileInformation.GetFileFormatVersion](../tsapiref/fileinformation-getfileformatversion.html)
 method in the TestStand API.

Note

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the translator in the DLL that must process the callback. |
| path | long | The path to the file. |
| inputStream | InputStream | A reference to an InputStream object that contains the contents of the file TestStand attempts to open. |
| fileFormatVersion | string | The file format version of the file. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxVersionLengthInBytes parameter to determine the size of the buffer. When the translator does not support reading file format version information from the file, assign an empty string to the buffer. |
| maxVersionLengthInBytes | long | The maximum number of bytes you can copy to the fileFormatVersion parameter. |
| errorCode | TSERROR | The error code when an error occurs in the callback. |
| errorMsg | string | The error message when an error occurs in the callback. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxErrorMsgLengthInBytes parameter to determine the size of the buffer. |
| maxErrorMsgLengthInBytes | long | The maximum number of bytes the DLL can copy to the errorMsg parameter. |

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/getfileversion.html language=enus -->
## TOPIC 03261: GetFileVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/getfileversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/getfileversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: void GetFileVersion(long index, const char *path, IDispatch *inputStream, char *fileVersion, long maxVersionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes) Purpose Returns the file version string for the file the path and inputStream parameters specify. National Ins

### GetFileVersion

void GetFileVersion(long index, const char *path, IDispatch *inputStream, char *fileVersion, long maxVersionLengthInBytes, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes)

#### Purpose

Returns the file version string for the file the path and
 inputStream
 parameters specify. National Instruments recommends using a file version format of
 "major.minor.revision.build"
 . Implement the callback to assign the file version to the
 fileVersion
 parameter. When the translator does not support reading file version information from the file, assign an empty string to the
 fileVersion
 parameter. When a translator supports obtaining the file version from a file, the TranslateToSequenceFile callback in the translator must assign the file version to the
 [PropertyObjectFile.Version](../tsapiref/propertyobjectfile-version.html)
 property of the translated sequence file. Otherwise, the version property is
 "0.0.0.0"
 . TestStand calls this callback to return a version string for the
 [FileInformation.GetFileVersion](../tsapiref/fileinformation-getfileversion.html)
 method in the TestStand API.

Note

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the translator in the DLL that must process the callback. |
| path | long | The path to the file. |
| inputStream | InputStream | A reference to an InputStream object that contains the contents of the file TestStand attempts to open. |
| fileVersion | string | The file version of the file. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxVersionLengthInBytes parameter to determine the size of the buffer. When the translator does not support reading file version information from the file, assign an empty string to the buffer. |
| maxVersionLengthInBytes | long | The maximum number of bytes you can copy to the fileVersion parameter. |
| errorCode | TSERROR | The error code when an error occurs in the callback. |
| errorMsg | string | The error message when an error occurs in the callback. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxErrorMsgLengthInBytes parameter to determine the size of the buffer. |
| maxErrorMsgLengthInBytes | long | The maximum number of bytes the DLL can copy to the errorMsg parameter. |

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/getnumelements-function.html language=enus -->
## TOPIC 03262: GetNumElements Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/getnumelements-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/getnumelements-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number GetNumElements(Array array) Return Value Number The number of elements in the array. For multi-dimensional arrays, this function returns a single value representing the total number of elements. Purpose This function returns the number elements in an array. Parameters array as Array An

### GetNumElements Function

#### Syntax

Number GetNumElements(Array array)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The number of elements in the array. For multi-dimensional arrays, this function returns a single value representing the total number of elements.

#### Purpose

This function returns the number elements in an array.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

An array

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/gettranslatorcount.html language=enus -->
## TOPIC 03263: GetTranslatorCount

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/gettranslatorcount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/gettranslatorcount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: long GetTranslatorCount() Purpose Returns the number of translators the DLL implements. Each translator supports a single custom file format. When a DLL implements more than one translator, the DLL must maintain indexes of the translators to support the required callback functions. Return Value Retu

### GetTranslatorCount

long GetTranslatorCount()

#### Purpose

Returns the number of translators the DLL implements. Each translator supports a single custom file format. When a DLL implements more than one translator, the DLL must maintain indexes of the translators to support the required callback functions.

#### Return Value

Returns the number of translators the DLL implements.

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/indextooffset-function.html language=enus -->
## TOPIC 03264: IndexToOffset Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/indextooffset-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/indextooffset-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number IndexToOffset(Array array, String index) Return Value Number Returns the Number offset. Purpose This function returns the numeric offset that is equivalent to the specified array index string. Note: to convert from an offset to an index, use the OffsetToIndex function. Parameters array

### IndexToOffset Function

#### Syntax

Number IndexToOffset(Array array, String index)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

Returns the Number offset.

#### Purpose

This function returns the numeric offset that is equivalent to the specified array index string. Note: to convert from an offset to an index, use the OffsetToIndex function.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

An array.

index
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string index for which the respective offset needs to be found. The index has the syntax "[i][j][k]", with an integer value in square brackets for each dimension of the source array.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/insertelements-function.html language=enus -->
## TOPIC 03265: InsertElements Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/insertelements-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/insertelements-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax InsertElements(Array array, String index, Number numElements) Return Value This function always returns 0. Purpose This function inserts new elements into a one-dimensional array. Parameters array as Array A single dimensional array. index as String The index at which to insert the new elemen

### InsertElements Function

#### Syntax

InsertElements(Array array, String index, Number numElements)

#### Return Value

This function always returns 0.

#### Purpose

This function inserts new elements into a one-dimensional array.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

A single dimensional array.

index
 as
 [String](../tsapiref/data-types-for-teststand.html)

The index at which to insert the new elements. You specify the array index as a string with the syntax "[x]", where x is an integer constant.

numElements
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The number of elements to insert. The values of the new elements are as follows: False for Booleans, zero for numbers,empty strings for strings, NULL references for references, and empty containers for containers.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/int64-function.html language=enus -->
## TOPIC 03266: Int64 Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/int64-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/int64-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number {Signed 64-bit Integer} Int64(AnyType value) Return Value Number This function converts a type to number with a representation of Signed 64-bit Integer. The function cannot convert a container or array data type to a number, and cannot convert an empty string to a number. The TestStand

### Int64 Function

#### Syntax

Number {Signed 64-bit Integer} Int64(AnyType value)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function converts a type to number with a representation of Signed 64-bit Integer. The function cannot convert a container or array data type to a number, and cannot convert an empty string to a number.

Note

#NoValidation

Int64

Locals.MyNumber = #NoValidation(Int64(Locals.MyEmptyString))

Note

Description

Constants

Other

Operators/Function

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/iscurrentfileversion.html language=enus -->
## TOPIC 03267: IsCurrentFileVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/iscurrentfileversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/iscurrentfileversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: long IsCurrentFileVersion(long index, const char *path, IDispatch *inputStream, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes) Purpose Returns whether the version of the file the path and inputStream parameters specify matches the current version of the translator, an older versi

### IsCurrentFileVersion

long IsCurrentFileVersion(long index, const char *path, IDispatch *inputStream, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes)

#### Purpose

Returns whether the version of the file the path and
 inputStream
 parameters specify matches the current version of the translator, an older version of the translator, or a newer version of the translator. TestStand calls this callback to return a value for the
 [Engine.IsCurrentSequenceFileVersion](../tsapiref/engine-iscurrentsequencefileversion.html)
 method in the TestStand API.

Note

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the translator in the DLL that must process the callback. |
| path | long | The path to the file. |
| inputStream | InputStream | A reference to an InputStream object that contains the contents of the file TestStand attempts to open. |
| errorCode | TSERROR | The error code when an error occurs in the callback. |
| errorMsg | string | The error message when an error occurs in the callback. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxErrorMsgLengthInBytes parameter to determine the size of the buffer. |
| maxErrorMsgLengthInBytes | long | The maximum number of bytes the DLL can copy to the errorMsg parameter. |

#### Return Value

Returns one of the following values:

| Name | Type |
| --- | --- |
| -1 | The file is compatible with an older version of the translator. |
| 0 | The file is compatible with the current version of the translator. When the translator does not support reading file version information from the file, return 0 . |
| 1 | The file is compatible with a newer version of the translator. |

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/left-function.html language=enus -->
## TOPIC 03268: Left Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/left-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/left-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Left(String string, Number numberOfCharacters) Return Value String A string that contains the specified number of characters from the left side of the original string. Purpose This function retrieves a substring from the left side of a string of the specified number of characters. Para

### Left Function

#### Syntax

String Left(String string, Number numberOfCharacters)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string that contains the specified number of characters from the left side of the original string.

#### Purpose

This function retrieves a substring from the left side of a string of the specified number of characters.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string.

numberOfCharacters
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The number of characters to return from the left side of the string. If this number is greater than the number of characters available, the function returns the entire string.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/len-function.html language=enus -->
## TOPIC 03269: Len Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/len-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/len-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Len(String string) Return Value Number The number of characters in a string.

### Len Function

#### Syntax

Number Len(String string)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The number of characters in a string.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/localizeddecimalpoint-function.html language=enus -->
## TOPIC 03270: LocalizedDecimalPoint Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/localizeddecimalpoint-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/localizeddecimalpoint-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String LocalizedDecimalPoint(Number decimalPointOption = 1) Return Value String A string containing the localized decimal point character. Purpose This function returns the value of the localized decimal point. Parameters decimalPointOption as Number An optional number that specifies how the

### LocalizedDecimalPoint Function

#### Syntax

String LocalizedDecimalPoint(Number decimalPointOption = 1)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string containing the localized decimal point character.

#### Purpose

This function returns the value of the localized decimal point.

#### Parameters

decimalPointOption
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies how the function determines which character to use for the localized decimal point. The valid values are:     1 - (default) Use the Station Options localization preferences to determine whether to use the operating system setting.     2 - Use the operating system setting.     3 - Use the period character.     4 - Use the comma character.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/localizeexpression-function.html language=enus -->
## TOPIC 03271: LocalizeExpression Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/localizeexpression-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/localizeexpression-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String LocalizeExpression(String expressionString, Number decimalPointOption = 1) Return Value String A string containing the localized expression. Purpose This function converts an expression string to conform to the localization settings for the computer. Call this function to localize an e

### LocalizeExpression Function

#### Syntax

String LocalizeExpression(String expressionString, Number decimalPointOption = 1)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string containing the localized expression.

#### Purpose

This function converts an expression string to conform to the localization settings for the computer. Call this function to localize an expression before you display it. The function replaces the periods that represent decimal points in the expression with the localized decimal point character. If the localized decimal point character is the comma character, the function also replaces commas that represent argument or expression separators with semicolons. The function does not change periods used as property field separators or any characters inside string constants.

#### Parameters

expressionString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The unlocalized expression string to convert.

decimalPointOption
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies how the function determines which character is the localized decimal point it uses to localize the expression. The valid values are:     1 - (default) Use the Station Options localization preferences to determine whether to use the operating system setting.     2 - Use the operating system setting.     3 - Use the period character.     4 - Use the comma character.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/log-function.html language=enus -->
## TOPIC 03272: Log Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/log-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/log-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Log(Number number) Return Value Number The natural (base e) logarithm of the number. Number must be greater than 0.

### Log Function

#### Syntax

Number Log(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The natural (base e) logarithm of the number. Number must be greater than 0.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/log10-function.html language=enus -->
## TOPIC 03273: Log10 Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/log10-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/log10-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Log10(Number number) Return Value Number The base 10 logarithm of the number. Number must be greater than 0.

### Log10 Function

#### Syntax

Number Log10(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The base 10 logarithm of the number. Number must be greater than 0.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/matchpattern-function.html language=enus -->
## TOPIC 03274: MatchPattern Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/matchpattern-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/matchpattern-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Boolean MatchPattern(String string, String stringPatternToMatchFor, [Boolean ignoreCase = False], [Out] [Array of String subPatterns]) Return Value Boolean True if a string matches the pattern. False if otherwise. Purpose This function checks if the string matches the regular expression patte

### MatchPattern Function

#### Syntax

Boolean MatchPattern(String string, String stringPatternToMatchFor, [Boolean ignoreCase = False], [Out] [Array of String subPatterns])

#### Return Value

[Boolean](../tsapiref/data-types-for-teststand.html)

True if a string matches the pattern. False if otherwise.

#### Purpose

This function checks if the string matches the regular expression pattern.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to compare against a pattern.

stringPatternToMatchFor
 as
 [String](../tsapiref/data-types-for-teststand.html)

The regular expression pattern to match.

Note

Microsoft documentation for regular expressions

ignoreCase
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) A Boolean that specifies whether to ignore character case when searching. The default is False.

of String subPatterns
 as
 [Array](../tsapiref/data-types-for-teststand.html)

(Optional) An empty array of strings in which the function stores the sub-patterns.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/max-function.html language=enus -->
## TOPIC 03275: Max Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/max-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/max-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Max(Number number1, Number number2, etc.) Return Value Number This function returns the largest number in the set of numbers you pass it. Alternatively, you can use the prototype Max(Array array, [String/Number] [indexOrOffset]) to use this function to find the maximum element in an ar

### Max Function

#### Syntax

Number Max(Number number1, Number number2, etc.)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function returns the largest number in the set of numbers you pass it. Alternatively, you can use the prototype Max(Array array, [String/Number] [indexOrOffset]) to use this function to find the maximum element in an array. In this case, you can optionally pass a number or string for the second parameter to store the numeric array offset or array index string of the maximum element in the array, respectively.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/mid-function.html language=enus -->
## TOPIC 03276: Mid Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/mid-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/mid-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Mid(String string, Number startIndex, [Number numberOfCharacters]) Return Value String A new string that contains the specified characters from the original string. Purpose This function retrieves a substring from the string beginning at the specified index. Parameters string as String

### Mid Function

#### Syntax

String Mid(String string, Number startIndex, [Number numberOfCharacters])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A new string that contains the specified characters from the original string.

#### Purpose

This function retrieves a substring from the string beginning at the specified index.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string.

startIndex
 as
 [Number](../tsapiref/data-types-for-teststand.html)

A number specifying the zero-based starting index of the substring to retrieve.

numberOfCharacters
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number specifying the number of characters to retrieve. If you omit this parameter or pass a value greater than the number of characters in the string beyond the starting index, the function returns all the characters from the start index to the end of the string.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/min-function.html language=enus -->
## TOPIC 03277: Min Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/min-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/min-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Min(Number number1, Number number2, etc.) Return Value Number This function returns the smallest number in the set of numbers you pass it. Alternatively, you can use the prototype Min(Array array, [String/Number] [indexOrOffset]) to use this function to find the minimum element in an a

### Min Function

#### Syntax

Number Min(Number number1, Number number2, etc.)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function returns the smallest number in the set of numbers you pass it. Alternatively, you can use the prototype Min(Array array, [String/Number] [indexOrOffset]) to use this function to find the minimum element in an array. In this case, you can optionally pass a number or string for the second parameter to store the numeric array offset or array index string of the minimum element in the array, respectively.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/model-plug-in-data-and-data-types.html language=enus -->
## TOPIC 03278: Model Plug-in Data and Data Types

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/model-plug-in-data-and-data-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/model-plug-in-data-and-data-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Model plug-ins use the following data types and related subproperties: NI_ModelPluginComponentDescription NI_ModelPluginConfiguration NI_ModelPluginConfigurationRuntimeVariables NI_ModelPlugin NI_ModelPluginRuntimeVariables NI_ModelPluginPerSocketRuntimeVariables

### Model Plug-in Data and Data Types

Model plug-ins use the following data types and related subproperties:

- NI_ModelPluginComponentDescription
- NI_ModelPluginConfiguration
- NI_ModelPluginConfigurationRuntimeVariables
- NI_ModelPlugin
- NI_ModelPluginRuntimeVariables
- NI_ModelPluginPerSocketRuntimeVariables

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/nameof-function.html language=enus -->
## TOPIC 03279: NameOf Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/nameof-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/nameof-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String NameOf(PropertyObject propertyObject) Return Value String The name of the property object. Note: The name of a property object is typically the property name itself. However, this function is useful for retrieving the names of array elements, such as the steps in a step group, or the s

### NameOf Function

#### Syntax

String NameOf(PropertyObject propertyObject)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The name of the property object. Note: The name of a property object is typically the property name itself. However, this function is useful for retrieving the names of array elements, such as the steps in a step group, or the sequences in a sequence file.

#### Parameters

propertyObject
 as
 [PropertyObject](../tsapiref/propertyobject.html)

A property object (String, Number, Container, etc.).

Parent topic:

Property Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/ni-modelplugin.html language=enus -->
## TOPIC 03280: NI_ModelPlugin

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/ni-modelplugin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/ni-modelplugin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: When you insert an instance of a plug-in into a configuration, the process model creates the instance of the plug-in by copying the FileGlobals.ModelPluginComponentDescription.Default property of the NI_ModelPlugin data type in the plug-in sequence file. When you edit the options for an instance of

### NI_ModelPlugin

When you insert an instance of a plug-in into a configuration, the process model creates the instance of the plug-in by copying the
 FileGlobals.ModelPluginComponentDescription.Default
 property of the NI_ModelPlugin data type in the plug-in sequence file.

When you edit the options for an instance of a plug-in, you change the values of subproperties of the NI_ModelPlugin data type instance.

Each time you execute a sequence using a process model, the process model loads a copy of the plug-in configuration from its configuration file. For each NI_ModelPlugin data type instance in the configuration, the model passes the instance to the
 ModelPlugin
 parameter of the entry points in the corresponding plug-in. The plug-in accesses the
 ModelPlugin
 parameter subproperties to determine the options you configured.

#### NI_ModelPlugin Properties

The NI_ModelPlugin data type includes
 [PluginSpecific](pluginspecific-subproperties.html)
 ,
 [CategorySpecific](categoryspecific-subproperties.html)
 , and
 [Base](base-subproperties.html)
 top-level subproperties.

Parent topic:

Model Plug-in Data and Data Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/ni-modelplugincomponentdescription.html language=enus -->
## TOPIC 03281: NI_ModelPluginComponentDescription

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/ni-modelplugincomponentdescription.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/ni-modelplugincomponentdescription.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Every model plug-in sequence file must include a FileGlobals.ModelPluginComponentDescription variable of type NI_ModelPluginComponentDescription. This variable includes the following fields. The data type appears in parentheses. Default (NI_ModelPlugin)—The default structure and values for new insta

### NI_ModelPluginComponentDescription

Every model plug-in sequence file must include a
 FileGlobals.ModelPluginComponentDescription
 variable of type NI_ModelPluginComponentDescription. This variable includes the following fields. The data type appears in parentheses.

- Default 
 (NI_ModelPlugin)—The default structure and values for new instances of the plug-in. The process model copies this property to create a new instance of the plug-in in a configuration.
- InsertOrder 
 (Number)—A value that determines where the plug-in appears in the list of plug-ins you can insert. The list sorts in ascending order. For example, the built-in reporting plug-in uses a value of 1, and the built-in database plug-in uses a value of 2. Therefore, the built-in reporting plug-in appears before the built-in database plug-in in the list of plug-ins you can insert. You can specify fractional values.
- ConfigurationOrder 
 (Number)—A value that determines where the plug-in appears in the default configuration of plug-ins the process model creates if the plug-in configuration file does not yet exist. The plug-ins appear in ascending order. For example, the built-in reporting plug-in uses a value of 1, and the built-in database plug-in uses a value of 2. Therefore, the built-in reporting plug-in appears before the built-in database plug-in in the default configuration. You can specify fractional values.
- InitializationExpression 
 (Expression)—The process model evaluates this expression when it instantiates a new instance of the plug-in. Use this expression to initialize fields that cannot use a static default value, such as system-dependent paths. Use the
 ModelPlugin 
 prefix in the expression to refer to ModelPlugin fields. You can also access a top-level
 UserCreated 
 Boolean property to determine whether a user created the plug-in or TestStand created the plug-in when creating the initial configuration file. For example, the built-in offline results generator plug-in uses an expression similar to the following to specify the location of the default offline results directory in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components 
 directory and to disable the offline results generator plug-in if you did not explicitly insert it:
 ModelPlugin.PluginSpecific.Options.Directory = Runstate.Engine.GetTestStandPath(TestStandPath_PublicComponents) + "\\Models\\UnprocessedResults",
ModelPlugin.Base.Enabled = UserCreated
- DisplayNameExpression 
 (Expression)—The process model evaluates this expression to determine the display name of the plug-in to use in the list of plug-ins you can insert. Use the
 ResStr 
 expression function to return a localizable string or specify a quoted string literal.

Parent topic:

Model Plug-in Data and Data Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/ni-modelpluginconfiguration.html language=enus -->
## TOPIC 03282: NI_ModelPluginConfiguration

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/ni-modelpluginconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/ni-modelpluginconfiguration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Process models use a variable of type NI_ModelPluginConfiguration to hold information about which model plugins to invoke and in what order. Process model execution entry points call Initialize Execution Entry Point , which calls Load Configuration in ModelSupport.seq . Load Configuration loads a de

### NI_ModelPluginConfiguration

Process models use a variable of type
 NI_ModelPluginConfiguration
 to hold information about which model plugins to invoke and in what order.
Process model execution entry points call
 Initialize Execution Entry Point
 , which calls
 Load Configuration
 in
 ModelSupport.seq
 .
Load Configuration loads a description of which plugins to execute from each existing model plugin configuration file such as
 ResultProcessing.cfg
 and
 Addons.cfg
 .
It merges this data into a single instance of NI_ModelPluginConfiguration. You can modify this configuration in a
 ModelPluginConfiguration
 callback in client
 sequence file, in a
 Model Plugin - Initialize
 entry point of a model plugin, or in a process model immediately after a call to
 Model Plugins - Begin
 .

- Plugins (Array of NI_ModelPlugin) 
 —The plugins are configured to execute.
- RuntimeVariables (NI_ModelPluginConfigurationRuntimeVariables) 
 —Information that controls the execution of the model and model plugins, including the orders in which the plugin entry
 points are invoked and whether the process model displays dialog prompts to the user.
- OTF.PostResultsCallbackInterval 
 —The value to which the model sets Execution.PostResultsCallbackInterval.
- OTF.MaximumResultsPerPostResultsCallback 
 —The value to which the model sets Execution.MaximumResultsPerPostResultsCallback.
- GUID (String) 
 —A comma separated list of the GUIDs of each NI_ModelPluginConfiguration merged into this instance, with the exception of the GUID from
 Addons.cfg 
 .
- RunOrder (Number) 
 —For configurations stored in separate configuration files, this property determines the order in which they merge into a single configuration. This value is not used within a merged configuration.

Parent topic:

Model Plug-in Data and Data Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/ni-modelpluginconfigurationruntimevariables.html language=enus -->
## TOPIC 03283: NI_ModelPluginConfigurationRuntimeVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/ni-modelpluginconfigurationruntimevariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/ni-modelpluginconfigurationruntimevariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type specifies information that controls the execution of the model and model plugins, including the order in which the plugin entry points are invoked and whether the process model displays dialog prompts to the user. RunOrders —Contains an array of reference sub-properties for each type

### NI_ModelPluginConfigurationRuntimeVariables

This data type specifies information that controls the execution of the model and model plugins, including the order in which the plugin entry
points are invoked and whether the process model displays dialog prompts to the user.

- RunOrders 
 —Contains an array of reference sub-properties for each type of model plugin entry point invoked at runtime. The reference elements
 refer to instances of NI_ModelPlugin in the NI_ModelPluginConfiguration.Plugins arrray. The order of the references in each array defines the
 order in which the process model invokes the plugins that define the entry point. You can re-order the items in these arrays in a ModelPluginConfiguration callback in client
 sequence file, in a
 Model Plugin - Initialize 
 or a
 Model Plugin - Begin 
 entry points of a model plugin, or in a process model immediately after a call to
 Model Plugins - Begin 
 .

Other fields in this data type that are not described here are reserved for the process model implementation.

Parent topic:

Model Plug-in Data and Data Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/ni-modelpluginpersocketruntimevariables.html language=enus -->
## TOPIC 03284: NI_ModelPluginPerSocketRuntimeVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/ni-modelpluginpersocketruntimevariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/ni-modelpluginpersocketruntimevariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI_ ModelPluginPerSocketRuntimeVariables data type is the data type of the elements of the Base.RuntimeVariables.PerSocket array property of the NI_ModelPluginRuntimeVariables data type. The NI_ModelPluginPerSocketRuntimeVariables data type contains variables the process model updates to control

### NI_ModelPluginPerSocketRuntimeVariables

The NI_ ModelPluginPerSocketRuntimeVariables data type is the data type of the elements of the
 Base.RuntimeVariables.PerSocket
 array property of the
 [NI_ModelPluginRuntimeVariables](ni-modelpluginruntimevariables.html)
 data type. The NI_ModelPluginPerSocketRuntimeVariables data type contains variables the process model updates to control and indicate the test socket execution state of the instance of the plug-in.

The NI_ModelPluginPerSocketRuntimeVariables data type includes the following subproperty. The data type appears in parentheses.

- Thread 
 (Reference)—When the
 NewThread 
 and
 UseDefaultNewThreadImplementation 
 properties of the
 NI_ModelPlugin 
 data type are
 True 
 and the process model calls the
 Model Plugin – UUT Done 
 entry point in a new thread, the process model stores a reference to the new thread in this property.

Parent topic:

Model Plug-in Data and Data Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/ni-modelpluginruntimevariables.html language=enus -->
## TOPIC 03285: NI_ModelPluginRuntimeVariables

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/ni-modelpluginruntimevariables.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/ni-modelpluginruntimevariables.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI_ModelPluginRuntimeVariables data type is the data type of the Base.RuntimeVariables property of the NI_ModelPlugin data type. The NI_ModelPluginRuntimeVariables data type contains variables the process model updates to control and indicate the execution state of the instance of the plug-in. T

### NI_ModelPluginRuntimeVariables

The NI_ModelPluginRuntimeVariables data type is the data type of the
 [Base.RuntimeVariables](base-subproperties.html)
 property of the NI_ModelPlugin data type. The NI_ModelPluginRuntimeVariables data type contains variables the process model updates to control and indicate the execution state of the instance of the plug-in. Typically, only the process model changes these variables.

The NI_ModelPluginRuntimeVariables data type includes the following subproperties. The data type appears in parentheses.

- ProcessorIndex 
 (Number)—Indicates the zero-based offset of the instance of the plug-in within the
 Plugins 
 array property of the NI_ModelPluginConfiguration data type in which the instance resides.
- Thread 
 (Reference)—When the
 NewThread 
 and
 UseDefaultNewThreadImplementation 
 properties of the NI_ModelPlugin data type are
 True 
 and the process model calls the
 Model Plugin – Batch Done 
 entry point in a new thread, the process model stores a reference to the new thread in this property.
- PluginEntryPoints 
 (Number)—A bit mask that indicates the entry points the plug-in contains. The bit values correspond to the subproperties of the
 FileGlobals.PluginEntryPoints 
 variable in
 ModelSupport.seq 
 .
- InitializationState 
 (Number)—A bit mask the process model uses to indicate whether certain run-time operations have occurred. The values correspond to the subproperties of the
 FileGlobals.InitializationStates 
 variable in
 ModelSupport.seq 
 . If you insert plug-in elements into the
 <NI_ModelPluginConfiguration>.Plugins 
 array in the
 ModelPluginConfiguration 
 callback, ensure this property is set to zero for each plug-in you insert.
- AsyncControllerAndSocketSynchronizationManager 
 (Reference)—When the
 NewThread 
 ,
 UseDefaultNewThreadImplementation 
 , and
 RequiresBatchControllerAndSocketSynchronization 
 properties of the
 NI_ModelPlugin 
 data type are
 True 
 , the process model stores a reference to an instance of the
 ControllerAndSocketSynchronizationManager 
 class in this property. You can use this instance of the
 ControllerAndSocketSynchronizationManager 
 class to enforce controller and socket synchronization between the new threads the process models create for the Batch Done and
 Model Plugin – UUT Done 
 entry points of this plug-in instance.
- SourceConfigurationFile 
 (String)—The filename of the configuration file from which this plug-in instance was read at run time.
- PerSocket 
 (Array of NI_ModelPluginPerSocketRuntimeVariables)—At run time, the process model resizes the
 PerSocket 
 array to include one element for each test socket in the system so that each socket has a separate instance of the NI_ModelPluginPerSocketRuntimeVariables data type.

Parent topic:

Model Plug-in Data and Data Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/novalidation-function.html language=enus -->
## TOPIC 03286: #NoValidation Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/novalidation-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/novalidation-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax #NoValidation(Expression expr) Purpose Disables evaluation error checking for part or all of the expression. Use this directive to suppress errors reported at edit time that will not occur at run time, such as using a variable the sequence creates at run time by using the TestStand API. Use t

### #NoValidation Function

#### Syntax

#NoValidation(Expression expr)

#### Purpose

Disables evaluation error checking for part or all of the expression. Use this directive to suppress errors reported at edit time that will not occur at run time, such as using a variable the sequence creates at run time by using the TestStand API. Use this directive without a parameter list to suppress error checking for the remainder of the expression, or pass a separate expression as the parameter to this directive to suppress error checking for only the parameter expression.

#### Parameters

expr
 as
 [Expression](../tsapiref/data-types-for-teststand.html)

Pass an expression for which you want to disable evaluation error checking at edit time.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/numeric-expression-functions.html language=enus -->
## TOPIC 03287: Numeric Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/numeric-expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/numeric-expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following numeric functions in TestStand expressions: Abs ACos Asc ASin ATan Cos Exp Float64 Int64 Log Log10 Max Min Pow Random Round Sin Sqrt Tan UInt64 Val

### Numeric Expression Functions

You can use the following numeric functions in TestStand expressions:

- Abs
- ACos
- Asc
- ASin
- ATan
- Cos
- Exp
- Float64
- Int64
- Log
- Log10
- Max
- Min
- Pow
- Random
- Round
- Sin
- Sqrt
- Tan
- UInt64
- Val

Parent topic:

Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/offsettoindex-function.html language=enus -->
## TOPIC 03288: OffsetToIndex Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/offsettoindex-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/offsettoindex-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String OffsetToIndex(Array array, Number offset) Return Value String Returns the String array index. Purpose This function returns the array index string that is equivalent to the specified numeric offset. The index has the syntax "[i][j][k]", with an integer value in square brackets for each

### OffsetToIndex Function

#### Syntax

String OffsetToIndex(Array array, Number offset)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

Returns the String array index.

#### Purpose

This function returns the array index string that is equivalent to the specified numeric offset. The index has the syntax "[i][j][k]", with an integer value in square brackets for each dimension of the source array. Note: to convert from an index to an offset, use the IndexToOffset function.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

An array.

offset
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The offset for which the respective string index needs to be found.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/other-expression-functions.html language=enus -->
## TOPIC 03289: Other Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/other-expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/other-expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following functions in TestStand expressions: AllOf AnyOf CheckLimits ConvertColor CurrentUserHasPrivilege Enum Evaluate FindFile GetEngine NoValidation OutputMessage RGB TargetName

### Other Expression Functions

You can use the following functions in TestStand expressions:

- AllOf
- AnyOf
- CheckLimits
- ConvertColor
- CurrentUserHasPrivilege
- Enum
- Evaluate
- FindFile
- GetEngine
- NoValidation
- OutputMessage
- RGB
- TargetName

Parent topic:

Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/outputmessage-function.html language=enus -->
## TOPIC 03290: OutputMessage Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/outputmessage-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/outputmessage-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax OutputMessage(String message, String category = "", Number severity = 0, [Number textColor], [String icon]) Return Value This function always returns 0. Parameters message as String A string containing the message to be displayed in the output window. category as String (Optional) Specifies t

### OutputMessage Function

#### Syntax

OutputMessage(String message, String category = "", Number severity = 0, [Number textColor], [String icon])

#### Return Value

This function always returns 0.

#### Parameters

message
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string containing the message to be displayed in the output window.

category
 as
 [String](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the category of the message. If you do not specify a category, the output message will be considered uncategorized. You can define your own categories. The default value is an empty string.

severity
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the severity of the message. The valid values are:      0 - (Default) OutputMessageSeverity_Information.      1 - OutputMessageSeverity_Warning.      2 - OutputMessageSeverity_Error.

textColor
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the text color used to display the message. Use a color constant such as tsBlack, or use the RGB function to specify a color using component color values.

icon
 as
 [String](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the name of the icon file related to the output message. The TestStand Engine obtains the icons from the <TestStand>\ComponentsIcons and <TestStand Public>\ComponentsIcons directories. This parameter is optional and the default icon is selected based on the severity of the message.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/pluginspecific-subproperties.html language=enus -->
## TOPIC 03291: PlugInSpecific Subproperties

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/pluginspecific-subproperties.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/pluginspecific-subproperties.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The PlugInSpecific property contains subproperties that vary depending on the plug-in. The PlugInSpecific property is an unstructured container, meaning the subproperties and subproperty data types can vary regardless of the NI_ModelPlugin type definition. When you create a plug-in, the PluginSpecif

### PlugInSpecific Subproperties

The
 PlugInSpecific
 property contains subproperties that vary depending on the plug-in. The
 PlugInSpecific
 property is an unstructured container, meaning the subproperties and subproperty data types can vary regardless of the NI_ModelPlugin type definition.

When you create a plug-in, the
 PluginSpecific
 property includes the following subproperties, each with a data type unique to the plug-in, as shown in parentheses. Edit the corresponding data type to add subproperties to each property.

- Options 
 (
 <plug-in name> 
 Options)—Create subproperties to store any options or settings the plug-in provides. Typically, you implement the
 Model Plugin – Configure Standard Options 
 entry point to provide a way for end users to edit the options you add.
- AdditionalOptions 
 (
 <plug-in name> 
 AdditionalOptions)—Create subproperties only if you define a
 Model Plugin – Configure Additional Options 
 entry point.
- RuntimeVariables 
 (
 <plug-in name> 
 RuntimeVariables)—Use the
 RuntimeVariables 
 subproperty to define variables the plug-in uses at run time. Create subproperties to share data within the same process model execution among the different entry points in the plug-in. The
 <plug-in name> 
 RuntimeVariables data type must always include the following subproperty:
  - PerSocket 
 (Array of
 <plug-in name> 
 PerSocketRuntimeVariables)—At run time, the process model resizes the PerSocket array to include one element for each test socket in the system. By adding properties to the
 <plug-in name> 
 PerSocketRuntimeVariables data type, you create per-socket variables you can use to share data within the same process model execution among the different entry points in the plug-in.

#### See Also

[Thread-Safety of the PropertyObject API and TestStand Variables](/csh?context=ts_tsapiref_threadsafetyapi)

Parent topic:

NI_ModelPlugin

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/pow-function.html language=enus -->
## TOPIC 03292: Pow Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/pow-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/pow-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Pow(Number base, Number exponent) Return Value Number The number x raised to the power of y. Purpose This function returns a base value raised to a specified power. Parameters base as Number A number specifying the base value. exponent as Number A number specifying the exponent value.

### Pow Function

#### Syntax

Number Pow(Number base, Number exponent)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The number x raised to the power of y.

#### Purpose

This function returns a base value raised to a specified power.

#### Parameters

base
 as
 [Number](../tsapiref/data-types-for-teststand.html)

A number specifying the base value.

exponent
 as
 [Number](../tsapiref/data-types-for-teststand.html)

A number specifying the exponent value.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/property-expression-functions.html language=enus -->
## TOPIC 03293: Property Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/property-expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/property-expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following property functions in TestStand expressions: CommentOf FindStep NameOf PropertyExists TypeOf

### Property Expression Functions

You can use the following property functions in TestStand expressions:

- CommentOf
- FindStep
- NameOf
- PropertyExists
- TypeOf

Parent topic:

Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/propertyexists-function.html language=enus -->
## TOPIC 03294: PropertyExists Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/propertyexists-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/propertyexists-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Boolean PropertyExists(String propertyName) Return Value Boolean True if the property exists, False otherwise. Parameters propertyName as String The lookup string for the property to check.

### PropertyExists Function

#### Syntax

Boolean PropertyExists(String propertyName)

#### Return Value

[Boolean](../tsapiref/data-types-for-teststand.html)

True if the property exists, False otherwise.

#### Parameters

propertyName
 as
 [String](../tsapiref/data-types-for-teststand.html)

The lookup string for the property to check.

Parent topic:

Property Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/random-function.html language=enus -->
## TOPIC 03295: Random Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/random-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/random-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Random(Number low, Number high, [Number seed]) Return Value Number The random number. Purpose This function returns a random number between the specified low and high values. Parameters low as Number The lower limit for the random number. high as Number The upper limit for the random n

### Random Function

#### Syntax

Number Random(Number low, Number high, [Number seed])

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The random number.

#### Purpose

This function returns a random number between the specified low and high values.

#### Parameters

low
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The lower limit for the random number.

high
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The upper limit for the random number.

seed
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number the function uses to determine where in the virtual sequence of random numbers the function obtains its random numbers. When you seed the Random function with the same value, subsequent calls to Random return the same sequence of numbers. If you pass a seed value of 0.0, the function generates a seed value based on the current time. If you do not pass a seed value, the function returns the next number in the current sequence of random numbers.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/removeelements-function.html language=enus -->
## TOPIC 03296: RemoveElements Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/removeelements-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/removeelements-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RemoveElements(Array array, String index, Number numElements) Return Value The function always returns 0. Purpose This function removes elements from a one-dimensional array. Parameters array as Array A one-dimensional array. index as String The index from which to remove the elements. Specif

### RemoveElements Function

#### Syntax

RemoveElements(Array array, String index, Number numElements)

#### Return Value

The function always returns 0.

#### Purpose

This function removes elements from a one-dimensional array.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

A one-dimensional array.

index
 as
 [String](../tsapiref/data-types-for-teststand.html)

The index from which to remove the elements. Specify the array index as a string with the syntax "[x]", where x is an integer constant.

numElements
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The number of elements to remove, including the index element.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/replace-function.html language=enus -->
## TOPIC 03297: Replace Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/replace-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/replace-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Replace(String string, Number startIndex, Number numCharsToReplace, String replacementString) Return Value Number This function always returns 0. Purpose This function replaces the given number of characters at the specified index with the replacement string. If you pass a property for

### Replace Function

#### Syntax

Number Replace(String string, Number startIndex, Number numCharsToReplace, String replacementString)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function always returns 0.

#### Purpose

This function replaces the given number of characters at the specified index with the replacement string. If you pass a property for the string parameter, the function updates the contents of the property.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string in which to replace the specified characters.

startIndex
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The zero-based index of the first character to replace.

numCharsToReplace
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The number of characters to replace.

replacementString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to insert in place of the specified characters.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/resstr-function.html language=enus -->
## TOPIC 03298: ResStr Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/resstr-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/resstr-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String ResStr(String category, String tag, [String defaultString], [Out] [Boolean found]) Return Value String The string you requested from the language resource files. Purpose This function retrieves a string from the language resource files. An alternative name for this function is GetResou

### ResStr Function

#### Syntax

String ResStr(String category, String tag, [String defaultString], [Out] [Boolean found])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The string you requested from the language resource files.

#### Purpose

This function retrieves a string from the language resource files. An alternative name for this function is GetResourceString().

#### Parameters

category
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string specifying the name of the category for the string you want to retrieve.

tag
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string specifying the name of the tag for the string you want to retrieve.

defaultString
 as
 [String](../tsapiref/data-types-for-teststand.html)

An optional string specifying the return value if the string you request is not found.

found
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional output value indicating whether the string was found.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/rgb-function.html language=enus -->
## TOPIC 03299: RGB Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/rgb-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/rgb-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number RGB(Number redComponent, Number greenComponent, Number blueComponent) Return Value Number a number that represents a color with the components you specify. Color values are in little-endian format. Use the ConvertColor function to change to big-endian format. Note: You can specify comm

### RGB Function

#### Syntax

Number RGB(Number redComponent, Number greenComponent, Number blueComponent)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

a number that represents a color with the components you specify. Color values are in little-endian format. Use the ConvertColor function to change to big-endian format. Note: You can specify common color values with color constants, such as tsRed and tsWhite.

#### Parameters

redComponent
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The amount of red in the color. The range is from 0 (none) to 255 (maximum).

greenComponent
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The amount of green in the color. The range is from 0 (none) to 255 (maximum).

blueComponent
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The amount of blue in the color. The range is from 0 (none) to 255 (maximum).

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/right-function.html language=enus -->
## TOPIC 03300: Right Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/right-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/right-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Right(String string, Number numberOfCharacters) Return Value String A string that contains the specified number of characters from the right side of the original string. Purpose This function retrieves a substring from the right side of a string of the specified number of characters. P

### Right Function

#### Syntax

String Right(String string, Number numberOfCharacters)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string that contains the specified number of characters from the right side of the original string.

#### Purpose

This function retrieves a substring from the right side of a string of the specified number of characters.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string.

numberOfCharacters
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The number of characters to return from the right side of the string. If this number is greater than the number of characters available, the function returns the entire string.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/round-function.html language=enus -->
## TOPIC 03301: Round Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/round-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/round-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Round(Number number, Number option = 0) Return Value Number The rounded number. Purpose This function rounds a number to an integer using the specified rounding method. Parameters number as Number The number to round. option as Number An optional parameter: how to round. Use the follow

### Round Function

#### Syntax

Number Round(Number number, Number option = 0)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The rounded number.

#### Purpose

This function rounds a number to an integer using the specified rounding method.

#### Parameters

number
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The number to round.

option
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional parameter: how to round. Use the following values:     0 - (default) round towards zero     1 - round away from zero.     2 - round towards positive infinity.     3 - round towards negative infinity.     4 - round to the nearest integer. If the number is exactly between two integers, rounds to the nearest even integer.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/searchandreplace-function.html language=enus -->
## TOPIC 03302: SearchAndReplace Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/searchandreplace-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/searchandreplace-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String SearchAndReplace(String string, String searchString, String replacementString, Number startIndex = 0, Boolean ignoreCase = False, Number maxReplacements = -1, Boolean searchInReverse = False, [Out] [Number numReplacements]) Return Value String The modified string. Purpose This function

### SearchAndReplace Function

#### Syntax

String SearchAndReplace(String string, String searchString, String replacementString, Number startIndex = 0, Boolean ignoreCase = False, Number maxReplacements = -1, Boolean searchInReverse = False, [Out] [Number numReplacements])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The modified string.

#### Purpose

This function searches for and replaces one or more substrings with the replacementString. If you pass a property for the string parameter, the function updates the contents of the property.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string in which to perform substring replacements.

searchString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The substring to find and then replace with the replacement string.

replacementString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The replacement string.

startIndex
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies the zero-based character index at which to begin searching. The default is 0.

ignoreCase
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that specifies whether to ignore character case when searching. The default is False.

maxReplacements
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies the maximum number of occurrences of substring to replace. A value of -1 signals the function to replace all occurrences of the substring. The default is -1.

searchInReverse
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that specifies whether to search the string in reverse. The default is False. If you pass True, the start index passed to parameter 3 specifies the zero-based index from the end of the string of the character at which to begin searching in reverse.

numReplacements
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number in which the function stores the number of substrings that it replaced.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/searchpatternandreplace-function.html language=enus -->
## TOPIC 03303: SearchPatternAndReplace Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/searchpatternandreplace-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/searchpatternandreplace-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String SearchPatternAndReplace(String string, String searchPattern, String replacementString, [Number startIndex = 0], [Boolean ignoreCase = False], [Number maxReplacements = -1], [Out] [Number numReplacements]) Return Value String The modified string. Purpose This function searches and repla

### SearchPatternAndReplace Function

#### Syntax

String SearchPatternAndReplace(String string, String searchPattern, String replacementString, [Number startIndex = 0], [Boolean ignoreCase = False], [Number maxReplacements = -1], [Out] [Number numReplacements])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The modified string.

#### Purpose

This function searches and replaces one or more substrings that match a regular expression pattern.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string in which to perform substring replacements.

searchPattern
 as
 [String](../tsapiref/data-types-for-teststand.html)

The regular expression pattern to find and then replace with the replacement string.

Note

Microsoft documentation for regular expressions

replacementString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The replacement string.

startIndex
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) A number that specifies the zero-based character index at which to begin searching. The default is 0.

ignoreCase
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) A Boolean that specifies whether to ignore character case when searching. The default is False.

maxReplacements
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) A number that specifies the maximum number of occurrences of the substring to replace. A value of -1 signals the function to replace all occurrences of the substring. The default is -1.

numReplacements
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) The number of replacements.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/seconds-function.html language=enus -->
## TOPIC 03304: Seconds Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/seconds-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/seconds-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Seconds(Boolean returnSecondsSinceStartup = True) Purpose Note: In certain situations, the TestStand Seconds(True) function returns incorrect elapsed time values when the operating system timer is running slower than actual time. Visit ni.com/info and enter the Info Code tstime for mor

### Seconds Function

#### Syntax

Number Seconds(Boolean returnSecondsSinceStartup = True)

#### Purpose

Note: In certain situations, the TestStand Seconds(True) function returns incorrect elapsed time values when the operating system timer is running slower than actual time. Visit ni.com/info and enter the Info Code tstime for more information about this issue.This function returns the number of seconds that have elapsed since an initial base time.

#### Parameters

returnSecondsSinceStartup
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the base time from which the function determines the current time in seconds. If you pass the default parameter of True or if you do not pass a parameter, the function returns the number of seconds since the application initialized the TestStand Engine. This option provides the greatest resolution in the numeric representation of the time. The time resolution is typically one millisecond or smaller, and can be as small as the cpu clock interval. If you pass False, the function returns the number of seconds elapsed since midnight, January 1, 1970, universal coordinated time (UTC). UTC is also known as Greenwich mean time (GMT). This option provides an absolute time that you can compare to times you record in other application sessions or on other computers. The time resolution is no smaller than one millisecond.

Parent topic:

Time Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/sequence-file-translator-functions.html language=enus -->
## TOPIC 03305: Sequence File Translator Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/sequence-file-translator-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/sequence-file-translator-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A TestStand sequence file translator DLL must export and implement the following C callback functions. When a translator DLL does not export all the callback functions, TestStand does not load the DLL. CanTranslate GetDescription GetExtension GetFileFormatVersion GetFileVersion GetTranslatorCount Is

### Sequence File Translator Functions

A TestStand sequence file translator DLL must export and implement the following C callback functions. When a translator DLL does not export all the callback functions, TestStand does not load the DLL.

- CanTranslate
- GetDescription
- GetExtension
- GetFileFormatVersion
- GetFileVersion
- GetTranslatorCount
- IsCurrentFileVersion
- TranslateToSequenceFile

#### Error Handling

Each callback function contains three parameters for error handling—an error code, an error string, and the maximum length for the error string. When an error occurs within a callback function, set the error code to a non-zero value. When the value you assign is a TestStand error code, TestStand uses the standard error code description. The callback function can copy additional error details to the standard error message string. However, the callback must not exceed the specified number of bytes for the maximum length for the error message. TestStand uses the error message string the callback function specifies.

Note

<TestStand Public>

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/setarraybounds-function.html language=enus -->
## TOPIC 03306: SetArrayBounds Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/setarraybounds-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/setarraybounds-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number SetArrayBounds(Array array, String lowerBounds, String upperBounds) Return Value Number This function always returns 0. Purpose This function changes the bounds of an array. You can use this function to change the size and/or the number of dimensions of an array. This function adds ele

### SetArrayBounds Function

#### Syntax

Number SetArrayBounds(Array array, String lowerBounds, String upperBounds)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function always returns 0.

#### Purpose

This function changes the bounds of an array. You can use this function to change the size and/or the number of dimensions of an array. This function adds elements to or removes elements from the array as needed by the specified bounds. New elements added in this way will have the default value for the element type, and are added to the end of the array.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

The array to redimension.

lowerBounds
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string specifying the index/indices of the new lower bound. Specify the array bounds as strings with the syntax "[i][j][k]", with an integer value in square brackets for each dimension of the source array.

upperBounds
 as
 [String](../tsapiref/data-types-for-teststand.html)

A string specifying the index/indices of the new upper bound. Specify the array bounds as strings with the syntax "[i][j][k]", with an integer value in square brackets for each dimension of the source array.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/setelements-function.html language=enus -->
## TOPIC 03307: SetElements Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/setelements-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/setelements-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SetElements(Array array, PropertyObject value, [String range]) Return Value This function always returns 0. Purpose This function assigns the passed value to all indices of the passed array. If an index range is specified, only elements in the range are assigned the passed value. Parameters a

### SetElements Function

#### Syntax

SetElements(Array array, PropertyObject value, [String range])

#### Return Value

This function always returns 0.

#### Purpose

This function assigns the passed value to all indices of the passed array. If an index range is specified, only elements in the range are assigned the passed value.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

An array to which the value should be assigned.

value
 as
 [PropertyObject](../tsapiref/propertyobject.html)

The value which is to be assigned to the specified parts of the array.

range
 as
 [String](../tsapiref/data-types-for-teststand.html)

An optional parameter specifying the range string specifying the indices of the array to which the value should be assigned. For example, the range "[0..2]" specifies elements [0], [1], and [2]. If unspecified, the range is assumed to be the whole array. Refer to the "Brackets" section in the Expression Operators help topic for more information on specifying an index range.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/setnumelements-function.html language=enus -->
## TOPIC 03308: SetNumElements Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/setnumelements-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/setnumelements-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number SetNumElements(Array array, Number numElements) Return Value Number This function always returns 0. Purpose This function sets the number of elements in a one-dimensional array. It preserves the lower bound and the values of all elements that can fit within the new array. Any new eleme

### SetNumElements Function

#### Syntax

Number SetNumElements(Array array, Number numElements)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function always returns 0.

#### Purpose

This function sets the number of elements in a one-dimensional array. It preserves the lower bound and the values of all elements that can fit within the new array. Any new elements added to the array have the default value for the element type and are added to the end of the array.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

A one-dimensional array to resize.

numElements
 as
 [Number](../tsapiref/data-types-for-teststand.html)

The desired number of elements.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/sin-function.html language=enus -->
## TOPIC 03309: Sin Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/sin-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/sin-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Sin(Number number) Return Value Number The sine of the number (where the number is measured in radians). To convert from degrees to radians, multiply degrees by (PI/180).

### Sin Function

#### Syntax

Number Sin(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The sine of the number (where the number is measured in radians). To convert from degrees to radians, multiply degrees by (PI/180).

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/sort-function.html language=enus -->
## TOPIC 03310: Sort Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/sort-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/sort-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Array Sort(Array array, Boolean inPlace, Boolean stable = False, Boolean caseSensitive = True) Return Value Array Returns the sorted array. If sorting in place, returns the array you pass. Otherwise, returns a sorted copy of the array. Purpose This function sorts the elements of the specified

### Sort Function

#### Syntax

Array Sort(Array array, Boolean inPlace, Boolean stable = False, Boolean caseSensitive = True)

#### Return Value

[Array](../tsapiref/data-types-for-teststand.html)

Returns the sorted array. If sorting in place, returns the array you pass. Otherwise, returns a sorted copy of the array.

#### Purpose

This function sorts the elements of the specified array.

#### Parameters

array
 as
 [Array](../tsapiref/data-types-for-teststand.html)

The input array to sort.

inPlace
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

Pass True to directly modify the input array (in place operation). Pass False to modify only the return value without modifying the input array.

stable
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

Pass True to run a stable sort, where elements with the same sort precedence are guaranteed to remain in the same order after sorting. This option can affect string values that match case insensitively in a case insensitive sort.

caseSensitive
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

Pass True to use a case-sensitive sort. If True, capital letters take precedence over lowercase letters in the sort order.

Parent topic:

Array Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/split-function.html language=enus -->
## TOPIC 03311: Split Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/split-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/split-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Array Split(String string, String/Array delimiters) Return Value Array An array of strings containing the tokens. Purpose This function generates an array of strings from the specified string using the specified delimiter. Parameters string as String The string to split. delimiters as String/

### Split Function

#### Syntax

Array Split(String string, String/Array delimiters)

#### Return Value

[Array](../tsapiref/data-types-for-teststand.html)

An array of strings containing the tokens.

#### Purpose

This function generates an array of strings from the specified string using the specified delimiter.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to split.

delimiters
 as
 [String/Array](../tsapiref/data-types-for-teststand.html)

The list of delimiters. Specify delimiters by passing a string in which each character of the string is a delimiter, or by passing an array of strings in which each string in the array is a delimiter.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/sqrt-function.html language=enus -->
## TOPIC 03312: Sqrt Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/sqrt-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/sqrt-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Sqrt(Number number) Return Value Number The square root of the number. The number must be >= 0.

### Sqrt Function

#### Syntax

Number Sqrt(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The square root of the number. The number must be >= 0.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/str-function.html language=enus -->
## TOPIC 03313: Str Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/str-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/str-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Str(AnyType value, [String formatString], Number decimalPointOption = 1, Boolean useValueFormatIfDefined = False, [String separator]) Return Value String A string representation of the property value.Note: Place a $ character after the % character in the format string to remove trailin

### Str Function

#### Syntax

String Str(AnyType value, [String formatString], Number decimalPointOption = 1, Boolean useValueFormatIfDefined = False, [String separator])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string representation of the property value.Note: Place a $ character after the % character in the format string to remove trailing zeros after the decimal point.Note: If you pass a "%s" style format specifier for parameter 2, the first parameter must be a string instead of a number. This allows you to format strings as well as numbers. For example: Str("Right justified", "%40s") evaluates to:    " Right justified"Note: If you pass an array value to parameter one, the function returns a string composed of the concatenated values of the array elements.Note: Use a format code of %b to format a number in binary.Note: Use a format code of %expr to format an expression for display. The expression must be a localized expression. Specify combinations of the following values for parameter 3 to control how the expression is formatted:   0x1 - Format precondition-style expressions into a simpler format.   0x2 - Insert step name comments for expressions that use unique step Ids.   0x4 - Use shorthand for RunState.Sequence.<StepGroup>["step"] in expression.   0x8 - Replace unique step Ids with step names.

#### Purpose

This function formats a property value to a string.

#### Parameters

value
 as
 [AnyType](../tsapiref/data-types-for-teststand.html)

A property to format.

formatString
 as
 [String](../tsapiref/data-types-for-teststand.html)

An optional string that specifies a C (printf) style format string to control the conversion. The default is "%$.13g" for numeric values.

decimalPointOption
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies how the function determines which character to use as the localized decimal point. The valid values are:     1 - (default) Use the Station Options localization preferences to determine whether to use the operating system setting.     2 - Use the operating system setting.     3 - Use the period character.     4 - Use the comma character.

useValueFormatIfDefined
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that specifies whether the function uses the inherent format of the first argument if the argument value has a non-default numeric display format. The default is false. If you pass true and the value argument has a non-default format, the function uses the value format instead of the format you pass to parameter 2.

separator
 as
 [String](../tsapiref/data-types-for-teststand.html)

An optional string that separates each element in the concatenated string of array elements that the function returns when the first argument is an array.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/strcomp-function.html language=enus -->
## TOPIC 03314: StrComp Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/strcomp-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/strcomp-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number StrComp(String stringA, String stringB, Number compareOption = 0, Number maxChars = -1) Return Value Number A number less than 0 if the first string is less than the second. A number greater than 0 if the first string is greater than the second. 0 if the strings are equal. Purpose This

### StrComp Function

#### Syntax

Number StrComp(String stringA, String stringB, Number compareOption = 0, Number maxChars = -1)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

A number less than 0 if the first string is less than the second. A number greater than 0 if the first string is greater than the second. 0 if the strings are equal.

#### Purpose

This function compares two strings.

#### Parameters

stringA
 as
 [String](../tsapiref/data-types-for-teststand.html)

The first string to compare.

stringB
 as
 [String](../tsapiref/data-types-for-teststand.html)

The second string to compare.

compareOption
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies how to compare the strings. Pass 0 for a case-sensitive comparison (this is the default). Pass 1 for a case-insensitive comparison.

maxChars
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies the maximum number of characters to compare. Pass -1 to compare all characters (this is the default).

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/string-expression-functions.html language=enus -->
## TOPIC 03315: String Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/string-expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/string-expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following string functions in TestStand expressions: CheckStrLimit Chr DelocalizeExpression Find FindPattern Left Len LocalizedDecimalPoint LocalizeExpression MatchPattern Mid Replace ResStr Right SearchAndReplace SearchPatternAndReplace Split Str StrComp ToLower ToUpper Trim TrimEnd

### String Expression Functions

You can use the following string functions in TestStand expressions:

- CheckStrLimit
- Chr
- DelocalizeExpression
- Find
- FindPattern
- Left
- Len
- LocalizedDecimalPoint
- LocalizeExpression
- MatchPattern
- Mid
- Replace
- ResStr
- Right
- SearchAndReplace
- SearchPatternAndReplace
- Split
- Str
- StrComp
- ToLower
- ToUpper
- Trim
- TrimEnd
- TrimStart

Parent topic:

Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/switchconnect-function.html language=enus -->
## TOPIC 03316: SwitchConnect Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/switchconnect-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/switchconnect-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SwitchConnect(String device, String connectRoutes, Number multiConnectMode = 1, Number lifetime = 4, Boolean waitForDebounce = True) Return Value This function always returns 0. Purpose This function connects paths for the specified routes in the device defined in the National Instruments Swi

### SwitchConnect Function

#### Syntax

SwitchConnect(String device, String connectRoutes, Number multiConnectMode = 1, Number lifetime = 4, Boolean waitForDebounce = True)

#### Return Value

This function always returns 0.

#### Purpose

This function connects paths for the specified routes in the device defined in the National Instruments Switch Executive.

#### Parameters

device
 as
 [String](../tsapiref/data-types-for-teststand.html)

The virtual device on which to performs the switching action.

connectRoutes
 as
 [String](../tsapiref/data-types-for-teststand.html)

The routes you are connecting. The expression must be a valid route specification string as defined by the National Instruments Switch Executive configuration for the virtual device name you are using. The string can be a combination of route group alias names, route names, and physical route paths. Example: 'MyRouteGroup & MyRoute & [Dev1/CH3->CH4,CH4->R0]'

multiConnectMode
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) value that defines the behavior when more than one connection operation occurs on a specific route. The valid values are: 0 - No Multiconnect: A route can only be connected once. Any attempt to reconnect a route that is already connected results in an error. 1 - Multiconnect Routes (default): A route can be connected multiple times. The route must contain the same endpoints and path. National Instruments Switch Executive automatically reference counts the routes. If you issue multiple connect operations for a specific route, the route is not physically disconnected until an equal number of disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The DisconnectAll function disconnects a route even if the route reference count is greater than one. -1 - Use Default Setting for Routes: Use the setting defined for the route in Switch Executive. (Only supported by Switch Executive version 2.0 or later.)

lifetime
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) value that specifies the lifetime that TestStand applies to the routes specified for connect operation. You can specify whether you want the routes to exist until manually disconnected later, or until the sequence, thread, or execution completes. If you use the Multiconnect Mode, a route can exist longer if another step specifies its own lifetime for the same route. Selecting a lifetime other than manual guarantees that the route stays connected as long as the step, sequence, thread, or execution in which you connect is still executing. If you manually disconnect a route that was previously connected using a non-manual lifetime setting, TestStand releases the reference to the route for the last step that performed a Connect operation for that route. The valid values are: 0 - Manual 1 - Execution 2 - Thread 3 - Sequence 4 - Step (default)

waitForDebounce
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether the operation waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after the connect operation completes. The default value is True.

Parent topic:

Switching Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/switchconnectdisconnect-function.html language=enus -->
## TOPIC 03317: SwitchConnectDisconnect Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/switchconnectdisconnect-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/switchconnectdisconnect-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SwitchConnectDisconnect(String device, String connectRoutes, String disconnectRoutes, Number multiConnectMode = 1, Number operationOrder = 1, Number lifetime = 4, Boolean waitForDebounce = True) Return Value This function always returns 0. Purpose This function connects and disconnects paths

### SwitchConnectDisconnect Function

#### Syntax

SwitchConnectDisconnect(String device, String connectRoutes, String disconnectRoutes, Number multiConnectMode = 1, Number operationOrder = 1, Number lifetime = 4, Boolean waitForDebounce = True)

#### Return Value

This function always returns 0.

#### Purpose

This function connects and disconnects paths for the specified routes in the device defined in the National Instruments Switch Executive.

#### Parameters

device
 as
 [String](../tsapiref/data-types-for-teststand.html)

The virtual device on which to performs the switching action.

connectRoutes
 as
 [String](../tsapiref/data-types-for-teststand.html)

The routes you are connecting. The expression must be a valid route specification string as defined by the National Instruments Switch Executive configuration for the virtual device name you are using. The string can be a combination of route group alias names, route names, and physical route paths. Example: 'MyRouteGroup & MyRoute & [Dev1/CH3->CH4,CH4->R0]'

disconnectRoutes
 as
 [String](../tsapiref/data-types-for-teststand.html)

The routes you are disconnecting. The expression must be a valid route specification string as defined by the National Instruments Switch Executive configuration for the virtual device name you are using.

multiConnectMode
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) value that defines the behavior when more than one connection operation occurs on a specific route. The valid values are: 0 - No Multiconnect: A route can only be connected once. Any attempt to reconnect a route that is already connected results in an error. 1 - Multiconnect Routes (default): A route can be connected multiple times. The route must contain the same endpoints and path. National Instruments Switch Executive automatically reference counts the routes. If you issue multiple connect operations for a specific route, the route is not physically disconnected until an equal number of disconnect operations occur. You can either issue the Disconnect operation manually or use a lifetime setting for the route. The DisconnectAll function disconnects a route even if the route reference count is greater than one. -1 - Use Default Setting for Routes: Use the setting defined for the route in Switch Executive. (Only supported by Switch Executive version 2.0 or later.)

operationOrder
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether the Disconnect operation occurs before or after the Connect operation. The valid values are: 1 - Disconnect Before Connect (default): Disconnect the specified routes before connecting any routes. This is the typical mode of operation. 2 - Connect Before Disconnect: Connect the specified routes before disconnecting any routes. Use this mode of operation when you are switching electric current and want to ensure that a load is always connected to your source.

lifetime
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) value that specifies the lifetime that TestStand applies to the routes specified for connect operation. You can specify whether you want the routes to exist until manually disconnected later, or until the sequence, thread, or execution completes. If you use the Multiconnect Mode, a route can exist longer if another step specifies its own lifetime for the same route. Selecting a lifetime other than manual guarantees that the route stays connected as long as the step, sequence, thread, or execution in which you connect is still executing. If you manually disconnect a route that was previously connected using a non-manual lifetime setting, TestStand releases the reference to the route for the last step that performed a Connect operation for that route. The valid values are: 0 - Manual 1 - Execution 2 - Thread 3 - Sequence 4 - Step (default)

waitForDebounce
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether the operation waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after both connect and disconnect operations are complete. The default value is True.

Parent topic:

Switching Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/switchdisconnect-function.html language=enus -->
## TOPIC 03318: SwitchDisconnect Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/switchdisconnect-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/switchdisconnect-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SwitchDisconnect(String device, String disconnectRoutes, Boolean waitForDebounce = True) Return Value This function always returns 0. Purpose This function disconnects paths for the specified routes in the device defined in the National Instruments Switch Executive. Parameters device as Strin

### SwitchDisconnect Function

#### Syntax

SwitchDisconnect(String device, String disconnectRoutes, Boolean waitForDebounce = True)

#### Return Value

This function always returns 0.

#### Purpose

This function disconnects paths for the specified routes in the device defined in the National Instruments Switch Executive.

#### Parameters

device
 as
 [String](../tsapiref/data-types-for-teststand.html)

The virtual device on which to performs the switching action.

disconnectRoutes
 as
 [String](../tsapiref/data-types-for-teststand.html)

The routes you are disconnecting. The expression must be a valid route specification string as defined by the National Instruments Switch Executive configuration for the virtual device name you are using. The string can be a combination of route group alias names, route names, and physical route paths. Example: 'MyRouteGroup & MyRoute & [Dev1/CH3->CH4,CH4->R0]'

waitForDebounce
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether the operation waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after the disconnect operation completes. The default value is True.

Parent topic:

Switching Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/switchdisconnectall-function.html language=enus -->
## TOPIC 03319: SwitchDisconnectAll Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/switchdisconnectall-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/switchdisconnectall-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SwitchDisconnectAll(String device, Boolean waitForDebounce = True) Return Value This function always returns 0. Purpose This function disconnects all paths in the device defined in the National Instruments Switch Executive. Parameters device as String The virtual device on which to performs t

### SwitchDisconnectAll Function

#### Syntax

SwitchDisconnectAll(String device, Boolean waitForDebounce = True)

#### Return Value

This function always returns 0.

#### Purpose

This function disconnects all paths in the device defined in the National Instruments Switch Executive.

#### Parameters

device
 as
 [String](../tsapiref/data-types-for-teststand.html)

The virtual device on which to performs the switching action.

waitForDebounce
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that specifies whether the operation waits for all switches to debounce before returning to TestStand. The wait for debounce occurs after the disconnect operation completes. The default value is True.

Parent topic:

Switching Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/switchfindroute-function.html language=enus -->
## TOPIC 03320: SwitchFindRoute Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/switchfindroute-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/switchfindroute-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String SwitchFindRoute(String device, String channel1, String channel2, Boolean raiseError = True, [Out] [Number capability]) Return Value String This function returns the route string that is available or already exists. Purpose This function finds an existing or potential route between two

### SwitchFindRoute Function

#### Syntax

String SwitchFindRoute(String device, String channel1, String channel2, Boolean raiseError = True, [Out] [Number capability])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

This function returns the route string that is available or already exists.

#### Purpose

This function finds an existing or potential route between two channels in the device defined in the National Instruments Switch Executive.

#### Parameters

device
 as
 [String](../tsapiref/data-types-for-teststand.html)

The virtual device on which to performs the switching action.

channel1
 as
 [String](../tsapiref/data-types-for-teststand.html)

The channel name of one of the endpoints of the route to find. The channel name must either be a channel alias name or a name in the Device/IviChannel syntax defined by the Switch Executive. Example: 'Dev1/CH2'

channel2
 as
 [String](../tsapiref/data-types-for-teststand.html)

The channel name of one of the endpoints of the route to find. The channel name must either be a channel alias name or a name in the Device/IviChannel syntax defined by the Switch Executive. Example: 'Dev1/CH3'

raiseError
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that specifies whether the function errors if the route is not available or does not already exist. The default value is True.

capability
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional output Number that indicate the capability of finding a valid route between the two channels.The valid return values are: 1 - Path available 2 - Path already exists, no route possible 3 - Path unsupported, no route possible 4 - Path possible but required resource in use, no route possible 5 - Both channels are sources, no route possible 6 - Channel cannot be an endpoint, no route possible

Parent topic:

Switching Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/switching-expression-functions.html language=enus -->
## TOPIC 03321: Switching Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/switching-expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/switching-expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following switching functions in TestStand expressions: SwitchConnect SwitchConnectDisconnect SwitchDisconnect SwitchDisconnectAll SwitchFindRoute

### Switching Expression Functions

You can use the following switching functions in TestStand expressions:

- SwitchConnect
- SwitchConnectDisconnect
- SwitchDisconnect
- SwitchDisconnectAll
- SwitchFindRoute

Parent topic:

Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/tan-function.html language=enus -->
## TOPIC 03322: Tan Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/tan-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/tan-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Tan(Number number) Return Value Number the tangent of the number (where the number is measured in radians). To convert from degrees to radians, multiply degrees by (PI/180).

### Tan Function

#### Syntax

Number Tan(Number number)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

the tangent of the number (where the number is measured in radians). To convert from degrees to radians, multiply degrees by (PI/180).

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/targetname-function.html language=enus -->
## TOPIC 03323: TargetName Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/targetname-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/targetname-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String TargetName(PropertyObject propertyObject, String stepIdOrName, Boolean isExpression = False, Boolean includeStepGroup = False, Number/String stepGroup = -1, Number/String stepGroupToOmit = -1) Return Value String The target name string. Parameters propertyObject as PropertyObject A Seq

### TargetName Function

#### Syntax

String TargetName(PropertyObject propertyObject, String stepIdOrName, Boolean isExpression = False, Boolean includeStepGroup = False, Number/String stepGroup = -1, Number/String stepGroupToOmit = -1)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The target name string.

#### Parameters

propertyObject
 as
 [PropertyObject](../tsapiref/propertyobject.html)

A Sequence or SequenceFile property object.

stepIdOrName
 as
 [String](../tsapiref/data-types-for-teststand.html)

A unique step ID or a step name string.

isExpression
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether the stepIdOrName is a string expression. Default value is False.

includeStepGroup
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies whether the step group of the target should be included in the target name. Default value is False.

stepGroup
 as
 [Number/String](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies the step group of the target. This parameter is ignored when you specify a unique step Id. Default value is -1.

stepGroupToOmit
 as
 [Number/String](../tsapiref/data-types-for-teststand.html)

(Optional) Specifies a step group that should not be displayed. If this [includeStepGroup] is True and the target is in the step group specified by this parameter, then the step group is not added to the target name. Default value is -1.

Parent topic:

Other Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/time-expression-functions.html language=enus -->
## TOPIC 03324: Time Expression Functions

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/time-expression-functions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/time-expression-functions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You can use the following time functions in TestStand expressions: Date Seconds Time

### Time Expression Functions

You can use the following time functions in TestStand expressions:

- Date
- Seconds
- Time

Parent topic:

Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/time-function.html language=enus -->
## TOPIC 03325: Time Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/time-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/time-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Time(Boolean force24HourFormat = False, [Out] [Number hours], [Out] [Number minutes], [Out] [Number seconds], [Out] [Number milliseconds], [Number timeStampInSeconds], [Boolean baseTimeIsInitTime]) Return Value String A string containing the current time in localized format. Purpose Th

### Time Function

#### Syntax

String Time(Boolean force24HourFormat = False, [Out] [Number hours], [Out] [Number minutes], [Out] [Number seconds], [Out] [Number milliseconds], [Number timeStampInSeconds], [Boolean baseTimeIsInitTime])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string containing the current time in localized format.

#### Purpose

This function returns the current time.

#### Parameters

force24HourFormat
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that specifies whether the function returns the time string in 24 hour format (the default is false).

hours
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that returns the number of hours since midnight (from 0 to 23).

minutes
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that returns the number of minutes after the hour (from 0 to 59).

seconds
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that returns the number of seconds after the minute (from 0 to 59).

milliseconds
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that returns the number of milliseconds after the second (from 0 to 999).

timeStampInSeconds
 as
 [Number](../tsapiref/data-types-for-teststand.html)

An optional number that specifies a timestamp the function uses in place of the current time. Pass a time value you obtain from the expression function Seconds().

baseTimeIsInitTime
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that specifies the base time for the timestamp you pass to parameter 6. Pass True if the base time is the time at which the application initialized the TestStand Engine. Pass False if the base time is midnight, January 1, 1970, universal coordinated time (UTC). UTC is also known as Greenwich mean time (GMT).

Parent topic:

Time Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/tolower-function.html language=enus -->
## TOPIC 03326: ToLower Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/tolower-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/tolower-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String ToLower(String string, Number startIndex = 0, Number numCharacters = -1, Boolean reverse = False) Return Value String The modified string. Purpose This function converts the alphabetic characters in a string to lowercase characters. Parameters string as String String to convert. startI

### ToLower Function

#### Syntax

String ToLower(String string, Number startIndex = 0, Number numCharacters = -1, Boolean reverse = False)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The modified string.

#### Purpose

This function converts the alphabetic characters in a string to lowercase characters.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

String to convert.

startIndex
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) the zero-based character index at which to begin converting. The default is 0.

numCharacters
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) the number of characters to convert. A value of -1 signals the function to convert all characters. The default is -1.

reverse
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Pass True to convert the string in reverse. In this case, the start index passed to parameter 2 specifies the zero-based index from the end of the string as the character at which to begin converting in reverse. The default is False.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/toupper-function.html language=enus -->
## TOPIC 03327: ToUpper Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/toupper-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/toupper-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String ToUpper(String string, Number startIndex = 0, Number numCharacters = -1, Boolean reverse = False) Return Value String The modified string. Purpose This function converts the alphabetic characters in a string to uppercase characters. Parameters string as String String to convert. startI

### ToUpper Function

#### Syntax

String ToUpper(String string, Number startIndex = 0, Number numCharacters = -1, Boolean reverse = False)

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The modified string.

#### Purpose

This function converts the alphabetic characters in a string to uppercase characters.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

String to convert.

startIndex
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) the zero-based character index at which to begin converting. The default is 0.

numCharacters
 as
 [Number](../tsapiref/data-types-for-teststand.html)

(Optional) the number of characters to convert. A value of -1 signals the function to convert all characters. The default is -1.

reverse
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

(Optional) Pass True to convert the string in reverse. In this case, the start index passed to parameter 2 specifies the zero-based index from the end of the string as the character at which to begin converting in reverse. The default is False.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/translatetosequencefile.html language=enus -->
## TOPIC 03328: TranslateToSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/translatetosequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/translatetosequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: void TranslateToSequenceFile(long index, IDispatch *engine, IDispatch *inputStream, IDispatch *sequenceFile, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes) Purpose Translates the file the inputStream parameter represents and returns a SequenceFile object to TestStand. Implement t

### TranslateToSequenceFile

void TranslateToSequenceFile(long index, IDispatch *engine, IDispatch *inputStream, IDispatch *sequenceFile, TSERROR *errorCode, char *errorMsg, long maxErrorMsgLengthInBytes)

#### Purpose

Translates the file the
 inputStream
 parameter represents and returns a
 [SequenceFile](../tsapiref/sequencefile.html)
 object to TestStand. Implement the callback to create the SequenceFile object using the
 engine
 parameter, to add sequences and steps that correspond to the contents of the
 inputStream
 parameter, and to assign the reference to the
 sequenceFile
 parameter. Set the
 sequenceFile
 parameter to
 NULL
 and set the
 error
 parameter to a non-zero value when the translator cannot translate the file stream.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| index | long | The zero-based index of the translator the DLL implements. |
| engine | Engine | A reference to the TestStand Engine. Use the Engine object to create a new SequenceFile object. |
| inputStream | InputStream | A reference to an InputStream object that contains the contents of the file TestStand attempts to open. |
| sequenceFile | SequenceFile | Returns a reference to a new SequenceFile object that represents the translated file. |
| errorCode | TSERROR | Returns the error code when an error occurs in the callback. |
| errorMsg | string | Returns the error message when an error occurs in the callback. The callback must copy a string value to the existing buffer, including the NUL terminating character. Use the maxErrorMsgLengthInBytes parameter to determine the size of the buffer. |
| maxErrorMsgLengthInBytes | long | The maximum number of bytes the DLL can copy to the errorMsg parameter. |

Parent topic:

Sequence File Translator Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/trim-function.html language=enus -->
## TOPIC 03329: Trim Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/trim-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/trim-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String Trim(String untrimmedString, [String charsToTrim]) Return Value String The trimmed string. Purpose This function removes all leading and trailing whitespace or specified characters from a string. Parameters untrimmedString as String The string to trim. charsToTrim as String (Optional)

### Trim Function

#### Syntax

String Trim(String untrimmedString, [String charsToTrim])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The trimmed string.

#### Purpose

This function removes all leading and trailing whitespace or specified characters from a string.

#### Parameters

untrimmedString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to trim.

charsToTrim
 as
 [String](../tsapiref/data-types-for-teststand.html)

(Optional) Pass a string containing specific characters to remove instead of white space.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/trimend-function.html language=enus -->
## TOPIC 03330: TrimEnd Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/trimend-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/trimend-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String TrimEnd(String untrimmedString, [String charsToTrim]) Return Value String The trimmed string. Purpose This function removes all trailing whitespace or specified characters from a string. Parameters untrimmedString as String The string to trim. charsToTrim as String (Optional) Pass a st

### TrimEnd Function

#### Syntax

String TrimEnd(String untrimmedString, [String charsToTrim])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The trimmed string.

#### Purpose

This function removes all trailing whitespace or specified characters from a string.

#### Parameters

untrimmedString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to trim.

charsToTrim
 as
 [String](../tsapiref/data-types-for-teststand.html)

(Optional) Pass a string containing specific characters to remove instead of white space.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/trimstart-function.html language=enus -->
## TOPIC 03331: TrimStart Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/trimstart-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/trimstart-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String TrimStart(String untrimmedString, [String charsToTrim]) Return Value String The trimmed string. Purpose This function removes all leading whitespace or specified characters from a string. Parameters untrimmedString as String The string to trim. charsToTrim as String (Optional) Pass a s

### TrimStart Function

#### Syntax

String TrimStart(String untrimmedString, [String charsToTrim])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

The trimmed string.

#### Purpose

This function removes all leading whitespace or specified characters from a string.

#### Parameters

untrimmedString
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to trim.

charsToTrim
 as
 [String](../tsapiref/data-types-for-teststand.html)

(Optional) Pass a string containing specific characters to remove instead of white space.

Parent topic:

String Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/typeof-function.html language=enus -->
## TOPIC 03332: TypeOf Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/typeof-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/typeof-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax String TypeOf(PropertyObject propertyObject, [Out] [String typeDisplayName], [Out] [PropertyValueTypes propertyValueType], [Out] [Boolean isArray], [Out] [String namedType]) Return Value String A string containing the type name of the property object you pass. Parameters propertyObject as Pro

### TypeOf Function

#### Syntax

String TypeOf(PropertyObject propertyObject, [Out] [String typeDisplayName], [Out] [PropertyValueTypes propertyValueType], [Out] [Boolean isArray], [Out] [String namedType])

#### Return Value

[String](../tsapiref/data-types-for-teststand.html)

A string containing the type name of the property object you pass.

#### Parameters

propertyObject
 as
 [PropertyObject](../tsapiref/propertyobject.html)

A property object (String, Number, Container, etc.).

typeDisplayName
 as
 [String](../tsapiref/data-types-for-teststand.html)

An optional string that returns more detailed type information.

propertyValueType
 as
 [PropertyValueTypes](../tsapiref/data-types-for-teststand.html)

An optional number that returns a PropertyValueTypes enumeration value. See the TestStand Help for more information. This parameter never returns PropValType_NamedType.

isArray
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean that returns whether the property object is an array.

namedType
 as
 [String](../tsapiref/data-types-for-teststand.html)

An optional string that returns the named type. This parameter returns an empty string if the property object is not an instance of a named type.

Parent topic:

Property Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/uint64-function.html language=enus -->
## TOPIC 03333: UInt64 Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/uint64-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/uint64-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number {Unsigned 64-bit Integer} UInt64(Any Type value) Return Value Number This function converts a type to a number with a representation of Unsigned 64-bit Integer. The function cannot convert a container or array data type to a number, and cannot convert an empty string to a number. The T

### UInt64 Function

#### Syntax

Number {Unsigned 64-bit Integer} UInt64(Any Type value)

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

This function converts a type to a number with a representation of Unsigned 64-bit Integer. The function cannot convert a container or array data type to a number, and cannot convert an empty string to a number.

Note

#NoValidation

UInt64

Locals.MyNumber = #NoValidation(UInt64(Locals.MyEmptyString))

Note

Description

Constants

Other

Operators/Function

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tsfundamentals/val-function.html language=enus -->
## TOPIC 03334: Val Function

- bundle_id: `teststand-api-reference`
- source_path: `tsfundamentals/val-function.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsfundamentals/val-function.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Number Val(String string, [Out] [Boolean isValid]) Return Value Number The number represented by the string. If the string did not represent a valid number, returns 0. Parameters string as String The string to convert. isValid as Boolean An optional Boolean parameter that the function sets to

### Val Function

#### Syntax

Number Val(String string, [Out] [Boolean isValid])

#### Return Value

[Number](../tsapiref/data-types-for-teststand.html)

The number represented by the string. If the string did not represent a valid number, returns 0.

#### Parameters

string
 as
 [String](../tsapiref/data-types-for-teststand.html)

The string to convert.

isValid
 as
 [Boolean](../tsapiref/data-types-for-teststand.html)

An optional Boolean parameter that the function sets to indicate if the first parameter contains a valid number.

Parent topic:

Numeric Expression Functions

<!--NI_TOPIC bundle=teststand-api-reference path=tshelp/teststand-api-reference.html language=enus -->
## TOPIC 03335: TestStand API Reference

- bundle_id: `teststand-api-reference`
- source_path: `tshelp/teststand-api-reference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tshelp/teststand-api-reference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The NI TestStand User Interface (UI) Controls are a set of ActiveX controls that implement the common functionality for applications to display, execute, edit, save, and debug test sequences. These ActiveX controls greatly reduce the amount of source code a user interface application requires. TestS

### TestStand API Reference

The
 
 [NI TestStand User Interface (UI) Controls](../tsuiref/teststand-ui-controls-api-reference-help.html)
 are a set of ActiveX controls that implement the common functionality for applications to display, execute, edit, save, and debug test sequences. These ActiveX controls greatly reduce the amount of source code a user interface application requires.

TestStand provides a comprehensive ActiveX Automation server
 
 [application programming interface (API)](../tsapiref/teststand-api-reference-help.html)
 for building sophisticated test management systems and other sequencing applications. Use the TestStand API to read and write data from TestStand properties, including TestStand sequences and steps, or to create, edit, run, and debug sequences. You can access the TestStand API from any programming environment that supports access to ActiveX servers.

<!--NI_TOPIC bundle=teststand-api-reference path=tshelp/teststand-intro.html language=enus -->
## TOPIC 03336: TestStand Programming Reference Manual

- bundle_id: `teststand-api-reference`
- source_path: `tshelp/teststand-intro.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tshelp/teststand-intro.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The TestStand Programming Reference Manual includes detailed descriptions of functions, methods, and properties as well as error code descriptions and dialog box references.

### TestStand Programming Reference Manual

The TestStand Programming Reference Manual includes detailed descriptions of functions, methods, and properties as well as error code descriptions and dialog box references.

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/17600-failed-to-load-vi.html language=enus -->
## TOPIC 03337: -17600: Failed to Load VI

- bundle_id: `teststand-api-reference`
- source_path: `tsref/17600-failed-to-load-vi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/17600-failed-to-load-vi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Message LabVIEW: The VI is not executable. This error may occur becuase the VI needs to be compiled, it is broken, or it contains a subVI that LabVIEW cannot locate. Select File»Open to open the VI and verify that you can run it. Why does this error occur? The error occurred for one of the following

### -17600: Failed to Load VI

#### Message

LabVIEW: The VI is not executable. This error may occur becuase the VI needs to be compiled, it is broken, or it contains a subVI that LabVIEW cannot locate. Select
 File»Open
 to open the VI and verify that you can run it.

#### Why does this error occur?

The error occurred for one of the following reasons:

- A VI, subVI, or its dependencies are not compiled.
- Dependencies are missing for a VI or subVI.
- A VI or subVI is broken.

#### How do I resolve this error?

Use the following suggestions to resolve the issue.

| Suggestions | Resources |
| --- | --- |
| Mass compile your LabVIEW code or project to ensure they are all in one version of LabVIEW, and ensure you have auto-detect enabled. | How to Mass Compile in LabVIEW How to Change the LabVIEW Version TestStand Uses |
| Build a Packed Project Library. | Caveats and Recommendations for Packed Project Libraries |
| Ensure that all VIs that are set to separate compiled code from source code have been compiled on the machine. | Separating Compiled Code from VIs and Other File Types |
| Make sure you have followed the instructions from the Deploying LabVIEW Code Modules with NI TestStand tutorial. | Deploying LabVIEW Code Modules with NI TestStand |

If the issue persists, contact NI for support.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/abort-operation-edit-ivi-dmm-step-dialog-box.html language=enus -->
## TOPIC 03338: Abort Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/abort-operation-edit-ivi-dmm-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/abort-operation-edit-ivi-dmm-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Abort Operation The Abort operation aborts a previously initiated measurement and returns the instrument to the idle state. This operation does not check the instrument status. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the Initiate

### Abort Operation - Edit IVI Dmm Step Dialog Box

#### Abort Operation

The Abort operation aborts a previously initiated measurement and returns the instrument to the idle state. This operation does not check the instrument status. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the
 [Initiate](initiate-operation-edit-ivi-dmm-step-dialog-b.html)
 operation.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/abort-operation-edit-ivi-fgen-step-dialog-box.html language=enus -->
## TOPIC 03339: Abort Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/abort-operation-edit-ivi-fgen-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/abort-operation-edit-ivi-fgen-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Abort Operation Aborts a previously configured output and returns the function generator to the idle state. When the function generator is in the output generation state, this operation moves the function generator to the idle state. When the function generator is already in the idle state, this ope

### Abort Operation - Edit IVI Fgen Step Dialog Box

#### Abort Operation

Aborts a previously configured output and returns the function generator to the idle state. When the function generator is in the output generation state, this operation moves the function generator to the idle state. When the function generator is already in the idle state, this operation performs no action.

You can configure the output of the function generator regardless of whether the function generator is in the idle state or the generation state. You are not required to call the Abort operation before configuring the output of the function generator.

Many function generators constantly generate an output signal and do not require you to abort signal generation before configuring the instrument. If the output of a function generator cannot be aborted, this operation performs no action.

Some function generators require that you abort signal generation before configuring the instrument. The specific drivers for these types of instruments must compensate for this restriction and allow you to configure the instrument without requiring you to call the Abort operation. These types of instruments often display a significant performance increase if you configure the output while the instrument is not generating a signal.

You are not required to call the Initiate and Abort operations. These operations have no impact on interchangeability. Use these operations to optimize the application for instruments that exhibit increased performance when output configuration is performed while the instrument is not generating a signal.

Parent topic:

Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/abort-operation-edit-ivi-power-supply-step-di.html language=enus -->
## TOPIC 03340: Abort Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/abort-operation-edit-ivi-power-supply-step-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/abort-operation-edit-ivi-power-supply-step-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Abort Operation Cancels the wait for a trigger. When the power supply is waiting for a trigger to change the output signal, this operation returns the power supply to the ignore triggers state. When the power supply is not waiting for a trigger, this operation performs no action.

### Abort Operation - Edit IVI Power Supply Step Dialog Box

#### Abort Operation

Cancels the wait for a trigger. When the power supply is waiting for a trigger to change the output signal, this operation returns the power supply to the ignore triggers state. When the power supply is not waiting for a trigger, this operation performs no action.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/abort-operation-edit-ivi-scope-step-dialog-bo.html language=enus -->
## TOPIC 03341: Abort Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/abort-operation-edit-ivi-scope-step-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/abort-operation-edit-ivi-scope-step-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Abort Operation The Abort operation aborts a previously initiated measurement and returns the instrument to the idle state. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the Initiate operation . This operation does not check the instrum

### Abort Operation - Edit IVI Scope Step Dialog Box

#### Abort Operation

The Abort operation aborts a previously initiated measurement and returns the instrument to the idle state. Typically, this operation is only called in a sequence of calls to other low-level driver operations, such as the
 [Initiate operation](initiate-operation-edit-ivi-scope-step-dialog.html)
 .

Note

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/abort-scan-operation-ivi-switching-mode-edit.html language=enus -->
## TOPIC 03342: Abort Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/abort-scan-operation-ivi-switching-mode-edit.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/abort-scan-operation-ivi-switching-mode-edit.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Abort Scan Operation (IVI Switching Mode) The Abort Scan operation stops a previously initiated scan from a Start Scan operation and returns the switch to an idle state. The Abort Scan operation does not reset the switch module or in any way initialize the state of the switch module. The operation d

### Abort Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Abort Scan Operation (IVI Switching Mode)

The Abort Scan operation stops a previously initiated scan from a Start Scan operation and returns the switch to an idle state. The Abort Scan operation does not reset the switch module or in any way initialize the state of the switch module. The operation desensitizes the switch module from triggers and moves it to an idle state. If the switch module is not currently scanning through the scan list, this method generates an error.

Parent topic:

IVI Switching Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/acquire-decrement-operation-semaphore-setting.html language=enus -->
## TOPIC 03343: Acquire (decrement) Operation - Semaphore Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/acquire-decrement-operation-semaphore-setting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/acquire-decrement-operation-semaphore-setting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquire (decrement) Operation Before you access a resource a semaphore protects, you must perform an Acquire (decrement) operation on the semaphore. Enable the Acquire option on the left of the Semaphore Settings panel. The Acquire (decrement) operation contains the following options: Semaphore Name

### Acquire (decrement) Operation - Semaphore Settings Edit Tab

#### Acquire (decrement) Operation

Before you access a resource a semaphore protects, you must perform an Acquire (decrement) operation on the semaphore. Enable the
 Acquire
 option on the left of the Semaphore Settings panel.

The Acquire (decrement) operation contains the following options:

- Semaphore Name or Reference Expression 
 —The semaphore on which to perform the operation. You can specify the semaphore by name or by the object reference you receive when you create the semaphore using the Use Object Reference for the Semaphore Reference Lifetime option.
- Auto Release 
 —When you enable this option, TestStand releases (increment) the semaphore automatically when the lifetime you specify expires.
- Acquire Lifetime 
 —Specifies how long the thread holds the semaphore after it acquires the semaphore. The thread releases the semaphore automatically when the
 lifetime 
 of the acquire ends.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you wish to refer to the object using an object reference variable.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —Use these controls to specify the timeout behavior when waiting to acquire the semaphore. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Semaphore Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/acquire-decrement-operation-semaphore-step-co.html language=enus -->
## TOPIC 03344: Acquire (decrement) Operation - Semaphore Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/acquire-decrement-operation-semaphore-step-co.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/acquire-decrement-operation-semaphore-step-co.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Acquire (decrement) Operation Before you access a resource a semaphore protects, you must perform an Acquire (decrement) operation on the semaphore. The Acquire (decrement) operation contains the following options: Semaphore Name or Reference Expression —The semaphore on which to perform the operati

### Acquire (decrement) Operation - Semaphore Step Configuration Dialog Box

#### Acquire (decrement) Operation

Before you access a resource a semaphore protects, you must perform an Acquire (decrement) operation on the semaphore.

The Acquire (decrement) operation contains the following options:

- Semaphore Name or Reference Expression 
 —The semaphore on which to perform the operation. You can specify the semaphore by name or by the object reference you receive when you create the semaphore using the Use Object Reference for the Semaphore Reference Lifetime option.
- Auto Release 
 —When you enable this option, TestStand automatically releases (increments) the semaphore when the lifetime you specify expires.
- Acquire Lifetime 
 —The amount of time the thread holds the semaphore after it acquires the semaphore. The thread releases the semaphore automatically when the
 lifetime 
 of the acquire ends.
  - Same as Sequence 
 —Releases the object reference after the sequence executes.
  - Same as Thread 
 —Releases the object reference after the thread completes.
  - Use Object Reference 
 —Use this option when you want to explicitly control the lifetime of the object reference or when you want to refer to the object using an object reference variable.
- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —Use these controls to specify the timeout behavior when waiting to acquire the semaphore. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .

Parent topic:

Semaphore Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/action-step.html language=enus -->
## TOPIC 03345: Action Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/action-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/action-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Action step calls code modules that do not perform tests but instead perform actions necessary for testing, such as initializing an instrument. By default, Action steps do not pass or fail. The step type does not modify the step status . Therefore, the status for an Action step is Done or Error

### Action Step

The Action step calls
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 that do not perform tests but instead perform actions necessary for testing, such as initializing an instrument.

By default, Action steps do not pass or fail. The step type does not modify the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 . Therefore, the status for an Action step is
 Done
 or
 Error
 unless the code module specifically sets another status for the step or the step calls a subsequence that fails. When an action uses the
 [Sequence Adapter](/csh?context=ts_tsref_sequence)
 to call a subsequence, and the subsequence fails, the Sequence Adapter sets the status of the step to
 Failed
 .

#### Configuring the Step

Use the adapter-specific edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Action step.

#### Step Properties

The Action step type does not define any additional step properties other than the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 all steps contain.

#### See Also

[Specify Module Tabs and Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Step Types You Can Use with Any Module Adapter](/csh?context=ts_tsfundamentals_universal_step_types)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/activex-com-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 03346: ActiveX/COM Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/activex-com-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/activex-com-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters , select the ActiveX/COM Adapter in the list control, and click Configure to launch the ActiveX/COM Adapter Configuration dialog box. The ActiveX/COM Adapter Configuration dialog box contains the following options: Use Late Binding —Specifies whether the ActiveX/COM Adapter

### ActiveX/COM Adapter Configuration Dialog Box

Select
 Configure»Adapters
 , select the ActiveX/COM Adapter in the list control, and click
 Configure
 to launch the ActiveX/COM Adapter Configuration dialog box.

The ActiveX/COM Adapter Configuration dialog box contains the following options:

- Use Late Binding 
 —Specifies whether the ActiveX/COM Adapter uses late binding or early binding. When you specify the
 code module 
 for an ActiveX/COM step, TestStand stores the IDs and names of the object and member the step calls. During execution, the ActiveX/COM Adapter must invoke the ActiveX Automation server and specify which object to create and which member to call.
 The ActiveX/COM Adapter always stores both IDs and names for the modules you specify. Early binding is more efficient, but requires that the IDs of the automation server do not change. When you are developing the automation server in an environment that does not provide direct control over IDs, use late binding so inadvertent changes to IDs do not invalidate the code module information for the steps. When you are finished developing the development automation server, disable this option and update the IDs in the client sequence files. 
 You can update the IDs by editing the code module information for each step or by selecting
 Tools»Update Automation Identifiers
 and running the Update Automation Identifiers tool on each sequence file that contains ActiveX/COM steps that reference the server.
- Unload Unused ActiveX Servers After Execution 
 —The ActiveX/COM Adapter requests the operating system to unload in-process (DLL) servers after every execution. The operating system only unloads those servers you are no longer using. Disable this option to improve execution speed.
- Show Method Arguments in Step Description 
 —The description for steps that use the ActiveX/COM Adapter includes the arguments steps pass to the methods they call.
- Show ActiveX Controls When Specifying a Module 
 —The
 ActiveX/COM Module 
 tab and the
 Edit ActiveX/COM Call 
 dialog box include ActiveX controls in the list of available servers.

#### See Also

[ActiveX/COM Module Tab](activex-com-module-tab.html)

[Edit ActiveX/COM Call dialog box](edit-activex-com-call-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/activex-com-module-tab.html language=enus -->
## TOPIC 03347: ActiveX/COM Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/activex-com-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/activex-com-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the ActiveX/COM Adapter and select Specify Module or Step Settings from the context menu to display the ActiveX/COM Module tab in the TestStand Sequence Editor . The ActiveX/COM Module tab contains the following options: Automation Server —The name of the server the s

### ActiveX/COM Module Tab

Insert a step configured to use the ActiveX/COM Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu to display the ActiveX/COM Module tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

The ActiveX/COM Module tab contains the following options:

- Automation Server 
 —The name of the server the step uses. The ActiveX/COM Adapter populates the ring control with the list of ActiveX Automation servers registered with Microsoft Windows. To select a server from the list, click the ring control or the
 Browse for Type Library 
 button to load a type library file from disk for a specific server. If you want the ActiveX/COM Adapter to refresh the list of registered servers and type library information, click
 Refresh Server List 
 . You can also refresh the server type library information when you select
 File»Unload All Modules 
 . If the server has a help file associated with it, you can open it by clicking the
 ? 
 button.
 Note 
 TestStand registers the type library with Windows when you click the
 ?
 button.
- Object Reference 
 —An Object Reference variable or property. When a step creates an object, the ActiveX/COM Adapter assigns the object reference to the variable or property, if specified. Otherwise, the ActiveX/COM Adapter automatically releases the object reference after executing the step. If the step does not create an object, but instead calls a method or accesses a property, the Object Reference control must contain the value of a valid ActiveX reference that refers to the object on which to call the method or access the property. Click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box.
- Object Class 
 —The name of the server class the step uses when it creates or invokes an object of the class. When you select a server, the ActiveX/COM Adapter populates this control with a list of objects defined for the server. The ring control separates the list of objects into two groups which are separated with a line. The upper group includes all top-level objects the ActiveX/COM Adapter can create. The lower group includes all other objects the server creates as a result of an invocation of a method or get property call. If a server type library contains help strings or links to a help file for a class, click the
 ? 
 button to access the help.
- Create Object 
 —When you enable this option, the step creates a new instance of the object class when the ActiveX/COM Adapter executes the step. When the step creates an object and you specify a property name in the Object Reference control, the ActiveX/COM Adapter assigns the value of the object handle to the property. Otherwise, the ActiveX/COM Adapter automatically releases the object reference after it executes the step. When you enable Create Object, you can launch the
 Create Options 
 window by clicking the
 Create Options 
 button.
 Note 
 Do not select Create Object when specifying an existing ActiveX object such as
 RunState.Engine
 or
 RunState.Sequence
 in the Object Reference control.
- Call Method or Access Property 
 —Specifies whether the step invokes a class method or accesses a class property when the ActiveX/COM Adapter executes the step. This control lists the types of access the server defines for the selected object class. The options are: Do Not Call, Call Method, Get Property, Set Property, and Set Property by Reference. When an object class does not have any methods, the control does not list the Call Method option.
 After you select the type of access, the ActiveX/COM Adapter populates the Method control with the method or property names the class defines for the access type. When a server type library contains help strings or links to a help file for a method or property, click the
 ?
 button to access the help.
- Parameters Table 
 —Contains the input and output parameters for the selected method or property. When the selected access type is Get Property, the control usually contains a single output parameter. When the access type is Set Property or Set Property by Reference, the control usually contains a single input parameter. When you call a method, the control can contain any number of input and output parameters. The ActiveX/COM Adapter automatically populates the Value field for parameters that have default values.
  - Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameters Table to access the
 [Parameters Table](for-module-tabs-parameters-table-context-menu.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box.
  - Type 
 —ActiveX data type for the parameter.
  - Direction 
 —Specifies whether the parameter is an input or an output.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name on the
 Additional Results panel 
 of the
 Properties 
 tab of the
 Step Settings 
 pane. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter on the Additional Results panel. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results panel specifies to log the [In] parameter value or the [Out] parameter value.
  - Default 
 —When you enable this option, TestStand uses the default value for the parameter the type library specifies.
  - Value 
 —A TestStand expression. For input parameters, TestStand passes the value of this expression. For output parameters, TestStand stores the data the method returns in the location this expression specifies. To help you enter an expression in the Value column, click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box. For enumerated types, a combo box displays all valid values for the type. You can use an expression with an enumerated type. Refer to the
 ActiveX/COM Call Parameters 
 topic for more information about using enumeration parameters.

Note

Refer to the Microsoft support article
 [Q186273](http://support.microsoft.com/kb/186273)
 at
 support.microsoft.com/kb/186273
 for more information about this issue.

Out-of-process (EXE) servers do not have this problem.

#### See Also

[ActiveX/COM Code Module Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64activexcomcodemodules)

[Attributes dialog box](attributes-dialog-box.html)

[Create Options Window](create-options-window.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[In-Process COM Servers Support in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64inprocesscomservers)

[Out-of-Process COM Servers in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64outprocesscomservers)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Step Settings Pane](step-settings-pane.html)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/adapter-configuration-dialog-box.html language=enus -->
## TOPIC 03348: Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters to launch the Adapter Configuration dialog box, in which you can change settings that apply to each adapter, specify the selected adapter new steps you create use, and specify which adapters you can select in the Insertion Palette and adapter list controls. Select an adapte

### Adapter Configuration Dialog Box

Select
 Configure»Adapters
 to launch the Adapter Configuration dialog box, in which you can change settings that apply to each adapter, specify the selected adapter new steps you create use, and specify which adapters you can select in the Insertion Palette and adapter list controls.

Select an adapter by enabling the option in the Selected column of the Adapter list control. You can also use the
 [Insertion Palette](insertion-palette-pane.html)
 to specify a module adapter. The selected adapter applies only to step types that can use any module adapter, such as the Action, Numeric Limit Test, Multiple Numeric Limit Test, String Value Test, and Pass/Fail Test step types. Refer to the Insert Step option in the
 [Steps](steps-pane-context-menu-sequence-file-window.html)
 pane context menu for more information about how TestStand uses the selected adapter when you insert a step.

Select an adapter in the Adapter list control and click the
 Configure
 button to launch an adapter-specific dialog box in which you configure the adapter. The following adapter-specific dialog boxes are available:

- LabVIEW Adapter Configuration 
 —Specifies which LabVIEW server TestStand uses, specifies whether to reserve loaded VIs for execution, and selects the source code template policy.
- LabVIEW NXG Adapter Configuration 
 —Specifies which LabVIEW NXG server TestStand uses, specifies whether to reserve loaded VIs for execution, and selects the source code template policy.
- LabWindows/CVI Adapter Configuration 
 —Specifies whether to show function arguments in step descriptions, whether to execute steps in process or in an external instance of LabWindows/CVI, the default structure passing size, and the source code template policy.
- C/C++ DLL Adapter Configuration 
 —Specifies whether to show function arguments in step descriptions and the default structure passing size.
- .NET Adapter Configuration 
 —Specifies whether to show function arguments in step descriptions.
- ActiveX/COM Adapter Configuration 
 —Specifies whether to use late binding, show method arguments in step descriptions, and unload used servers after execution.
- HTBasic Adapter Configuration 
 —Indicates the HTBasic server to use and the working directory. (64-bit TestStand) The HTBasic Adapter is not supported.
- Sequence Adapter Configuration 
 —Specifies whether to show function arguments in step descriptions.
 Note 
 By default, the Sequence Adapter contains a checkmark in the option for the
 Hidden
 column and does not appear in the Adapter ring control. You must remove the checkmark from the option in the
 Hidden
 column to enable the Sequence Adapter. National Instruments recommends using a
 [Sequence Call step](sequence-call-step.html)
 instead.
- Python Adapter Configuration 
 —Specifies which Python interpreter session to use, which Python version and Python virtual environment path to use, and which viewer to use to launch Python modules.

You can also remove an adapter from controls that list adapters by enabling the option in the Hidden column.

#### See Also

[Insertion Palette](insertion-palette-pane.html)

[Sequence Call Step](sequence-call-step.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-column-dialog-box.html language=enus -->
## TOPIC 03349: Add Column Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-column-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-column-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Add Column option in the Table or Column context menu in the Database Object View to launch the Add Column dialog box, in which you can add a new column to the selected table or to generate a query to add a column to the selected table. The Add Column dialog box contains the following options

### Add Column Dialog Box

Select
 Add Column
 option in the Table or Column context menu in the
 [Database Object View](database-explorer.html)
 to launch the Add Column dialog box, in which you can add a new column to the selected table or to generate a query to add a column to the selected table.

The Add Column dialog box contains the following options:

- Table Name 
 —Displays the name of the table in which to add the new column.
- Column Name 
 —Enter the name of the column to add.
- Data Type 
 —Select the data type of the column to add.
- Size 
 —Select the size of the column to be added. This control is enabled only if the data type you select supports variable-sized data.
- Precision 
 —Select the precision of the column to add. This control is enabled only if the data type you select supports precision.
- Scale 
 —Select the scale of the column to add. This control is enabled only if the data type you select supports scale.
- Is Nullable 
 —Specifies a nullable column. This control is enabled only if the data type you select allows nullable columns.
- Create Column 
 —Creates a new column in the database table and adds that new column to the Tree View under the selected table.
- Generate Query 
 —Generates a query to add a new column to the database table and launches a new Execute SQL tab that contains the query content.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-file-to-workspace-dialog-box.html language=enus -->
## TOPIC 03350: Add File To Workspace Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-file-to-workspace-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-file-to-workspace-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the Add File to Workspace dialog box, select File»Add File to Workspace when you have a workspace file open and the active window is a sequence file in the TestStand Sequence Editor . You cannot insert a file if it already exists in the workspace file. The Add File To Workspace dialog box

### Add File To Workspace Dialog Box

To launch the Add File to Workspace dialog box, select
 File»Add File to Workspace
 when you have a workspace file open and the active window is a sequence file in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 . You cannot insert a file if it already exists in the workspace file.

The Add File To Workspace dialog box contains the following option:

- Select Location to Insert File 
 —The project file, folder, or sequence file where TestStand inserts the new file.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-or-remove-items-from-labview-project-dial.html language=enus -->
## TOPIC 03351: Add or Remove Items From LabVIEW Project Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-or-remove-items-from-labview-project-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-or-remove-items-from-labview-project-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Add or Remove VIs from LabVIEW Project button on the LabVIEW Module tab of the Step Settings pane or in the Edit LabVIEW VI Call dialog box to launch the Add or Remove Items From LabVIEW Project dialog box. Right-click the LabVIEW project item you want to add or remove to display a context

### Add or Remove Items From LabVIEW Project Dialog Box

Click the
 Add or Remove VIs from LabVIEW Project
 button on the
 [LabVIEW Module](labview-module-tab.html)
 tab of the Step Settings pane or in the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 dialog box to launch the Add or Remove Items From LabVIEW Project dialog box.

Right-click the
 [LabVIEW project](/csh?context=ts_tslabview_project)
 item you want to add or remove to display a context menu.

- My Computer 
 —Creates a new VI, a new LabVIEW virtual folder, or adds an existing VI to the project. If you create a new VI, the LabVIEW Adapter creates a code shell for the VI. If the project item you select does not already exist, the LabVIEW Adapter creates it. If the file exists, the LabVIEW Adapter prompts you to overwrite the existing file. If a VI code template exists for the step type defined for the step, the LabVIEW Adapter uses that code template to create the new VI.
- Virtual Folder 
 —Creates a new VI, a new LabVIEW virtual folder, adds an existing VI to the project, or removes the item from the project.
- VIs 
 —Edits the VI or removes it from the project.

Note

When you click the
 Select
 button, the Add or Remove Items From LabVIEW Project dialog box selects the active VI. However, clicking the
 Done
 button does not revert changes to the project.

The LabVIEW Adapter uses the last selected VI to configure the step.

#### See Also

[LabVIEW Module Tab](labview-module-tab.html)

[Edit LabVIEW VI Call dialog box](edit-labview-vi-call-dialog-box.html)

[Organizing Test Program Files with LabVIEW Projects](/csh?context=ts_tslabview_project)

Parent topic:

LabVIEW Module Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-parameters-from-csv-file-dialog-box.html language=enus -->
## TOPIC 03352: Add Parameters from CSV File Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-parameters-from-csv-file-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-parameters-from-csv-file-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the Add Parameters from CSV File dialog box, navigate to the Sweep Parameters tab on the Sweep Loop step and click the dropdown arrow beside the Add Parameter icon. Use the Add Parameters from CSV File dialog at edit time to import sweep parameter definitions from a CSV file that contains

### Add Parameters from CSV File Dialog Box

To launch the Add Parameters from CSV File dialog box, navigate to the Sweep Parameters tab on the
 [Sweep Loop](sweep-loop-step.html)
 step and click the dropdown arrow beside the Add Parameter icon. Use the Add Parameters from CSV File dialog at edit time to import sweep parameter definitions from a CSV file that contains a record prototype.

This dialog contains the following options:

- CSV File Path 
 —Specifies the path of the CSV file.
- Data Tag 
 —(Optional) Specifies the data tag for the CSV file. TestStand searches for the file for this tag and begins reading the prototype on the following line.
- Separator Character 
 —Choose a separator character from the drop down menu.
- Import data values into/via the the Array Strategy associated with each parameter 
 —Check this checkbox to import data values, as Array strategy, while adding parameters from a CSV file.
- Add Parameters Button 
 —Launches the Import Prototype from CSV File dialog box to read the prototype from the specified CSV file. The dialog shows a view of the specified CSV file. Select the first line of the
 record prototype 
 in the file and click
 OK 
 to import the prototype and close the dialog box. If an imported parameter name matches an existing parameter name in the step, the imported parameter name will be differentiated with a numeric suffix. The new parameter has the Stream strategy and Field/Column ID automatically populated with the name from the prototype. After successfully importing sweep parameter definitions, the dialog closes, returning you to the Sweep Parameters tab of the Sweep Loop step.

Parent topic:

Sweep Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-table-dialog-box.html language=enus -->
## TOPIC 03353: Add Table Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-table-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-table-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Add Table in the Database, Tables, or Table context menus in the Database Object View to launch the Add Table dialog box, in which you can add a new table to the selected database or generate a query to add a table. The Add Table dialog box contains the following options: Table Name —Enter th

### Add Table Dialog Box

Select
 Add Table
 in the Database, Tables, or Table context menus in the
 [Database Object View](database-explorer.html)
 to launch the Add Table dialog box, in which you can add a new table to the selected database or generate a query to add a table.

The Add Table dialog box contains the following options:

- Table Name 
 —Enter the name of the table to add.
- Column Name 
 —Enter the name of the column to add.
- Data Type 
 —Select the data type of the column to add.
- Size 
 —Select the size of the column to add. This control is enabled only if the data type you select supports variable-sized data.
- Precision 
 —Select the precision of the column to add. This control is enabled only if the data type you select supports precision.
- Scale 
 —Select the scale of the column to add. This control is enabled only if the data type you select supports scale.
- Primary Key 
 —Adds the column as a primary key.
 Note 
 One of the added columns must be selected as a primary key.
- Is Nullable 
 —Specifies a nullable column. This control is enabled only if the data type you select allows nullable columns.
 Note 
 If a column is a primary key, you cannot make the column nullable.
- Grid 
 —Displays the list of columns added.
- Add Column 
 —Adds a column to the grid. You can edit the added column in the grid.
- Remove Column 
 —Removes the selected column from the grid.
- Up and Down 
 —Controls the order of columns in the grid.
- Create Table 
 —Creates a new table and adds the table to the Tree View with the specified table name and list of columns.
- Generate Query 
 —Generates a query to create a new table with the specified table name and list of columns and launches a new Execute SQL tab that contains the query content.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-thread-operation-batch-settings-edit-tab.html language=enus -->
## TOPIC 03354: Add Thread Operation - Batch Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-thread-operation-batch-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-thread-operation-batch-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add Thread Operation Use the Add Thread operation to add a TestStand thread to the group of batch threads. Select the Add Thread option on the left of the Batch Settings panel. The Add Thread operation contains the following options: Batch Name or Reference Expression —The batch on which to perform

### Add Thread Operation - Batch Settings Edit Tab

#### Add Thread Operation

Use the Add Thread operation to add a TestStand thread to the group of batch threads. Select the
 Add Thread
 option on the left of the Batch Settings panel.

The Add Thread operation contains the following options:

- Batch Name or Reference Expression 
 —The batch on which to perform the operation. You can specify the batch by name or by the object reference you receive when you create the batch using the Use Object Reference for the Batch Reference Lifetime option.
- Object Reference to Thread 
 —A
 Thread 
 object to add to the batch. A thread can belong to only one batch at a time. Adding a thread to a batch removes the thread from a previous batch, if any. A terminating thread removes itself from the batch.
- Order Number 
 —The order in which threads enter synchronized sections. Threads with a lower order number enter a synchronized section before threads with a higher order number.

#### See Also

[Thread](../tsapiref/thread.html)

Parent topic:

Batch Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-thread-operation-batch-specification-step.html language=enus -->
## TOPIC 03355: Add Thread Operation - Batch Specification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-thread-operation-batch-specification-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-thread-operation-batch-specification-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Add Thread Operation Use the Add Thread operation to add a TestStand thread to the group of batch threads. The Add Thread operation contains the following options: Batch Name or Reference Expression —The batch on which to perform the operation. You can specify the batch by name or by the object refe

### Add Thread Operation - Batch Specification Step Configuration Dialog Box

#### Add Thread Operation

Use the Add Thread operation to add a TestStand thread to the group of batch threads.

The Add Thread operation contains the following options:

- Batch Name or Reference Expression 
 —The batch on which to perform the operation. You can specify the batch by name or by the object reference you receive when you create the batch using the Use Object Reference for the Batch Reference Lifetime option.
- Object Reference to Thread 
 —A
 Thread 
 object to add to the batch. A thread can belong to only one batch at a time. Adding a thread to a batch removes the thread from a previous batch, if any. Additionally, when a thread terminates, the thread removes itself from the batch.
- Order Number 
 —The order in which threads enter synchronized sections. Threads with a lower order number enter a synchronized section before threads with a higher order number.

#### See Also

[Thread](../tsapiref/thread.html)

Parent topic:

Batch Specification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/add-tools-menu-item-dialog-box.html language=enus -->
## TOPIC 03356: Add Tools Menu Item Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/add-tools-menu-item-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/add-tools-menu-item-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the Customize Tools Menu dialog box and click Add to launch the Add Tools Menu Item dialog box. The Add Tools Menu Item dialog box contains the following options: Item Type —The type of menu item to insert. The following options are available in the ring control: Command —Select this option t

### Add Tools Menu Item Dialog Box

Launch the
 [Customize Tools Menu](customize-tools-menu-dialog-box.html)
 dialog box and click
 Add
 to launch the Add Tools Menu Item dialog box.

The Add Tools Menu Item dialog box contains the following options:

- Item Type 
 —The type of menu item to insert. The following options are available in the ring control:
  - Command 
 —Select this option to make the Command text box visible.
  - Sequence 
 —Select this option to make the Sequence File and Sequence text boxes visible.
  - Submenu 
 —Selecting this option displays no additional controls.
  - Sequence File 
 —Select this option to make the Sequence File text box visible.
- Command 
 —The Microsoft Windows executable the new tools menu item invokes.
- Sequence File 
 —The sequence file the new tools menu item uses. This option is available only when you select
 Sequence File 
 in
 Item Type 
 .
- Sequence 
 —The sequence the new tools menu item launches. This option is available only when you select
 Sequence 
 in
 Item Type 
 .

#### See Also

[Customize Tools Menu dialog box](customize-tools-menu-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/additional-columns-tab-legacy-import-export-p.html language=enus -->
## TOPIC 03357: Additional Columns Tab - Legacy Import/Export Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/additional-columns-tab-legacy-import-export-p.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/additional-columns-tab-legacy-import-export-p.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Additional Columns Tab When you export to a database, the Additional Columns tab defines the set of column values TestStand writes to the database for each record. When you import from a database, the tab defines the column values that a record must match before TestStand loads values from the recor

### Additional Columns Tab - Legacy Import/Export Properties Dialog Box

#### Additional Columns Tab

When you export to a database, the Additional Columns tab defines the set of column values TestStand writes to the database for each record. When you import from a database, the tab defines the column values that a record must match before TestStand loads values from the record.

The option at the top of the tab enables the controls on the Additional Columns tab. The Additional Columns tab for database locations contains the following options:

- Values 
 —The mappings of column names to variables or properties. The list control displays the mappings. Use the
 New 
 ,
 Cut 
 ,
 Copy 
 , and
 Paste 
 buttons to create a new item in the list, remove items from the list, and rearrange the items in the list.
  - Name/Number 
 —A literal value or an expression TestStand evaluates during import and export. Use this control to specify the column for the currently selected mapping.
 For export, the column that corresponds to a property that contains a signed 64-bit integer must be
 BIGINT 
 ,
 NUMERIC 
 , or
 DECIMAL 
 with a precision of 19 and a scale of 0, and the column that corresponds to a property that contains an unsigned 64-bit integer must be
 BIGINT 
 ,
 NUMERIC 
 , or
 DECIMAL 
 with a precision of 20 and a scale of 0.
  - Value 
 —A literal value or an expression TestStand evaluates during import and export. When importing values, this control must contain the name of a variable or property.
 Include the
 <FILE>
 or
 <SEQUENCE>
 tag within a value to instruct TestStand to automatically substitute the name of the sequence or file on which the step operates. Select
 <FILE>
 or
 <SEQUENCE>
 from the drop-down list to insert the tag.
  - Export NULL 
 —When you enable this option, TestStand assigns
 NULL 
 as the column value. When you enable this option, the Value expression is ignored and
 NULL 
 is assigned to the corresponding column. This option only affects the exporting process.
  - Format String 
 —Specifies how to
 convert a string value 
 when comparing a column value to a string expression. Typically, you use this control when comparing data from a column that is of the date/time or currency type.
- Create Columns 
 —Launches the
 Create Columns 
 dialog box. TestStand automatically populates the dialog box with the list of any column names that you specify and the SQL statement does not return. You typically use the Create Columns dialog box to add new columns to a database table.

Click the
 Expression Browse
 button to launch the
 [Expression Browser](expression-browser-dialog-box.html)
 dialog box for controls that contain a TestStand expression.

#### See Also

[Create Columns dialog box](create-columns-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Format Strings for Database Date Values](/csh?context=ts_tsfundamentals_strings_format)

Parent topic:

Database Data Location - Legacy Import/Export Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/additional-results-dialog-box.html language=enus -->
## TOPIC 03358: Additional Results Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/additional-results-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/additional-results-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Additional Results in the context menu for the step or click Additional Results on the General tab of the Step Properties dialog box to launch the Additional Results dialog box from a TestStand User Interface . Use this dialog box to add and configure additional results. An addition

### Additional Results Dialog Box

Select
 Configure Additional Results
 in the context menu for the step or click
 Additional Results
 on the General tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Additional Results dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to add and configure additional results. An additional result is a value TestStand adds to the result list of a step when the step executes and when you skip a step or force the step to pass or fail. An additional result can be a module parameter or a custom additional result in which you specify the name and value of the result. You can configure TestStand to automatically include additional results in reports and when logging results to a database. The default TestStand report generation sequences and XML style sheets do not display additional results for skipped steps.

The Additional Results dialog box contains the following options:

- Additional Results 
 —Lists the additional results TestStand logs when you execute the step. The list contains any additional results you have added. If the step calls a
 code module 
 , the list also contains all parameters passed to the module. Use the following controls to modify an additional result:
  - Name 
 —An expression that specifies the name of the additional result. TestStand logs only the additional results you select using the checkbox next to the additional result name. For custom additional results, you normally use a literal string or the
 ResStr 
 expression function to specify a localized name. If the expression you specify as the Value to Log evaluates to a property object with a name, you can leave the Name field empty to use the name of the property object the Value to Log expression evaluates to as the name of the additional result. For parameter additional results, TestStand uses the name of the parameter, and you cannot change this value.
    - Check or uncheck parameters using a filter 
 —Launches a menu that contains the following items. This option appears only for steps that have parameters.
      - Check Non-Filtered Parameters 
 —Places a checkmark in all parameters not included in the parameter filter.
      - Uncheck Filtered Parameters 
 —Removes the checkmark from all parameters included in the parameter filter.
      - Configure Parameter Filter 
 —Launches the
 Configure Parameter Filter 
 dialog box, in which you can define the parameter filter.
    - Select Result From List 
 —For a custom additional result, select an item from the list to set all columns to a value the item defines. The list contains items that apply to any step and might also contain items specific to the step type.
  - Value to Log 
 —An expression that specifies the value of the additional result. For a parameter additional result, TestStand uses the value passed to or from the code module. You can log the additional result for an output parameter not stored in a variable.
  - Type 
 —The type of the additional result.
 For parameter additional results, the Type column shows the type of the parameter and you cannot change the value. For custom additional results, you can click the
 Change Result Type
 button to change the expected type of the additional result. When you click the
 Change Result Type
 button and select
 <Any Type>
 , the Value to Log expression can evaluate to any type and the Type column displays the type of the Value to Log expression. 
 When you click the
 Change Result Type
 button and select a type, you can expand the Name column of the Additional Results list to view the subproperties of the selected type and specify settings for each subproperty. For example, you can specify a Value to Log expression for each individual subproperty and leave the Value to Log expression for the top-level object empty, or remove the checkmark next to the Name column for an additional result to not log that subproperty. 
 When you click the
 Change Result Type
 button and select an array type, you can expand the Name column of the Additional Results list to view the subproperties of the array elements of the selected type and specify settings for each individual subproperty of the array elements. The settings you specify apply to every element of the array. For example, you can remove the checkmark next to the additional result name to not log that subproperty for every array element. You cannot specify a Value to Log expression for each individual array element subproperty. You must specify a Value to Log expression for the array itself.
  - Condition 
 —If you specify a condition that evaluates to
 False 
 , TestStand does not log the additional result.
  - Include in Report 
 —Sets the
 PropFlags_IncludeInReport 
 flag on the additional result, which indicates that the report displays the additional result.
  - Is Measurement 
 —Sets the
 PropFlags_IsMeasurementValue 
 flag on the additional result, which indicates that the additional result is a measurement.
  - Is Limit 
 —Sets the
 PropFlags_IsLimit 
 flag on the additional result, which indicates that the additional result is a test limit.
- Add Result From List 
 —Behaves the same as the
 Select Result From List 
 button, except the Add Result From List button inserts a new custom result before setting the column values.
- Add Custom Result 
 —Adds a new custom additional result.
- Remove Selected Result 
 —Removes the currently selected custom additional result.
- Move Selected Result Up 
 —Moves the currently selected custom additional result up in the Additional Results list.
- Move Selected Result Down 
 —Moves the currently selected custom additional result down in the Additional Results list.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Configure Parameter Filter dialog box](configure-parameter-filter-dialog-box.html)

[PropertyFlags](../tsapiref/propertyflags.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Additional Results Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/additional-results-edit-tab.html language=enus -->
## TOPIC 03359: Additional Results Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/additional-results-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/additional-results-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Additional Results edit tab in the TestStand Sequence Editor to add and configure additional results. An additional result is a value TestStand adds to the result list of a step when the step executes and when you skip a step or force the step to pass or fail. An additional result can be a m

### Additional Results Edit Tab

Use the Additional Results edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to add and configure additional results. An additional result is a value TestStand adds to the result list of a step when the step executes and when you skip a step or force the step to pass or fail. An additional result can be a module parameter or a custom additional result in which you specify the name and value of the result. You can configure TestStand to automatically include additional results in reports and when logging results to a database. The default TestStand report generation sequences and XML style sheets do not display additional results for skipped steps.

The Additional Results edit tab contains the following options:

- Additional Results 
 —Lists the additional results TestStand logs when you execute the step. The list contains any additional results you have added. If the step calls a
 code module 
 , the list also contains all parameters passed to the module. Use the following controls to modify an additional result:
  - Name 
 —An expression that specifies the name of the additional result. TestStand logs only the additional results you select by using the checkbox next to the additional result name. For custom additional results, you normally use a literal string or the
 ResStr 
 expression function to specify a localized name. If the expression you specify as the Value to Log evaluates to a property object with a name, you can leave the Name field empty to use the name of the property object the Value to Log expression evaluates to as the name of the additional result. For parameter additional results, TestStand uses the name of the parameter, and you cannot change this value.
    - Select Result From List 
 —For a custom additional result, select an item from the list to set all columns to a value the item defines. The list contains items that apply to any step and might also contain items specific to the step type.
  - Value to Log 
 —An expression that specifies the value of the additional result. For a parameter additional result, TestStand uses the value passed to or from the code module. You can log the additional result for an output parameter not stored in a variable.
  - Type 
 —The type of the additional result.
 For parameter additional results, the Type column shows the type of the parameter and you cannot change the value. For custom additional results, you can click the
 Change Result Type
 button to change the expected type of the additional result. When you click the
 Change Result Type
 button and select
 <Any Type>
 , the Value to Log expression can evaluate to any type and the Type column displays the type of the Value to Log expression. 
 When you click the
 Change Result Type
 button and select a type, you can expand the Name column of the Additional Results list to view the subproperties of the selected type and specify settings for each subproperty. For example, you can specify a Value to Log expression for each individual subproperty and leave the Value to Log expression for the top-level object empty, or remove the checkmark next to the Name column for an additional result to not log that subproperty. 
 When you click the
 Change Result Type
 button and select an array type, you can expand the Name column of the Additional Results list to view the subproperties of the array elements of the selected type and specify settings for each individual subproperty of the array elements. The settings you specify apply to every element of the array. For example, you can remove the checkmark next to the additional result name to not log that subproperty for every array element. You cannot specify a Value to Log expression for each individual array element subproperty. You must specify a Value to Log expression for the array itself.
  - Condition 
 —If you specify a condition that evaluates to
 False 
 , TestStand does not log the additional result.
  - Include in Report 
 —Enable this option to set the
 PropFlags_IncludeInReport 
 flag on the additional result, which indicates that the report displays the additional result.
  - Is Measurement 
 —Enable this option to set the
 PropFlags_IsMeasurementValue 
 flag on the additional result, which indicates that the additional result is a measurement.
  - Is Limit 
 —Enable this option to set the
 PropFlags_IsLimit 
 flag on the additional result, which indicates that the additional result is a test limit.
- Add Result From List 
 —Behaves the same as the
 Select Result From List 
 button, except the
 Add Result From List 
 button inserts a new custom result before setting the column values.
- Add Custom Result 
 —Adds a new custom additional result.
- Remove Selected Result 
 —Removes the currently selected custom additional result.
- Move Selected Result Up 
 —Moves the currently selected custom additional result up in the Additional Results list.
- Move Selected Result Down 
 —Moves the currently selected custom additional result down in the Additional Results list.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[PropertyFlags](../tsapiref/propertyflags.html)

Parent topic:

Additional Results Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/additional-results-panel-step-settings-pane.html language=enus -->
## TOPIC 03360: Additional Results Panel - Step Settings Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/additional-results-panel-step-settings-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/additional-results-panel-step-settings-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Additional Results Panel Use the Additional Results panel to add and configure additional results, which are values TestStand adds to the result list of a step when the step executes and when you skip a step or force the step to pass or fail. An additional result can be a module parameter or a custo

### Additional Results Panel - Step Settings Pane

#### Additional Results Panel

Use the Additional Results panel to add and configure additional results, which are values TestStand adds to the result list of a step when the step executes and when you skip a step or force the step to pass or fail. An additional result can be a module parameter or a custom additional result in which you specify the name and value of the result. You can configure TestStand to automatically include additional results when generating a report or when logging results to a database. The default TestStand report generator style sheets do not display additional results for skipped steps.

The Additional Results panel contains the following options:

- Additional Results 
 —Lists the additional results TestStand logs when you execute the step. The list contains any additional results you have added. If the step calls a
 code module 
 , the list also contains all parameters passed to the module. Use the following controls to modify an additional result:
  - Name 
 —An expression that specifies the name of the additional result. TestStand logs only the additional results you select by using the checkbox next to the additional result name. For custom additional results, you normally use a literal string or the
 ResStr 
 expression function to specify a localized name. If the expression you specify as the Value to Log evaluates to a property object with a name, you can leave the Name field empty to use the name of the property object the Value to Log expression evaluates to as the name of the additional result. For parameter additional results, TestStand uses the name of the parameter, and you cannot change this value.
    - Check or uncheck parameters using a filter 
 —Launches a menu that contains the following items. This button appears only for steps that have parameters.
      - Check Non-Filtered Parameters 
 —Places a checkmark in all parameters not included in the parameter filter.
      - Uncheck Filtered Parameters 
 —Removes the checkmark from all parameters included in the parameter filter.
      - Configure Parameter Filter 
 —Launches the
 Configure Parameter Filter 
 dialog box, in which you can define the parameter filter.
    - Select Result From List 
 —For a custom additional result, select an item from the list to set all columns to a value the item defines. The list contains items that apply to any step and might also contain items specific to the step type.
  - Value to Log 
 —An expression that specifies the value of the additional result. For a parameter additional result, TestStand uses the value passed to or from the code module. You can log the additional result for an output parameter not stored in a variable.
  - Type 
 —The type of the additional result.
 For parameter additional results, the Type column shows the type of the parameter and you cannot change the value. For custom additional results, you can click the
 Change Result Type
 button to change the expected type of the additional result. When you click the
 Change Result Type
 button and select
 <Any Type>
 , the Value to Log expression can evaluate to any type and the Type column displays the type of the Value to Log expression. 
 When you click the
 Change Result Type
 button and select a type, you can expand the Name column of the Additional Results list to view the subproperties of the selected type and specify settings for each subproperty. For example, you can specify a Value to Log expression for each individual subproperty and leave the Value to Log expression for the top-level object empty, or remove the checkmark next to the Name column for an additional result to not log that subproperty. 
 When you click the
 Change Result Type
 button and select an array type, you can expand the Name column of the Additional Results list to view the subproperties of the array elements of the selected type and specify settings for each individual subproperty of the array elements. The settings you specify apply to every element of the array. For example, you can remove the checkmark next to the additional result name to not log that subproperty for every array element. You cannot specify a Value to Log expression for each individual array element subproperty. You must specify a Value to Log expression for the array itself.
  - Condition 
 —If you specify a condition that evaluates to
 False 
 , TestStand does not log the additional result.
  - Include in Report 
 —Enable this option to set the
 PropFlags_IncludeInReport 
 flag on the additional result, which indicates that the report displays the additional result.
  - Is Measurement 
 —Enable this option to set the
 PropFlags_IsMeasurementValue 
 flag on the additional result, which indicates that the additional result is a measurement.
  - Is Limit 
 —Enable this option to set the
 PropFlags_IsLimit 
 flag on the additional result, which indicates that the additional result is a test limit.
- Add Result From List 
 —Behaves the same as the Select Result From List button, except the Add Result From List button inserts a new custom result before setting the column values.
- Add Custom Result 
 —Adds a new custom additional result.
- Remove Selected Result 
 —Removes the currently selected custom additional result.
- Move Selected Result Up 
 —Moves the currently selected custom additional result up in the Additional Results list.
- Move Selected Result Down 
 —Moves the currently selected custom additional result down in the Additional Results list.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Configure Parameter Filter dialog box](configure-parameter-filter-dialog-box.html)

[PropertyFlags](../tsapiref/propertyflags.html)

Parent topic:

Properties Tab - Step Settings Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/additional-results-step.html language=enus -->
## TOPIC 03361: Additional Results Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/additional-results-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/additional-results-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Additional Results step type when you want to log data outside the context of one particular step in the sequence. The Additional Results step specifies values to add to the result list of a step. An additional result is a value TestStand adds to the result list of a step when the step execu

### Additional Results Step

Use the Additional Results step type when you want to log data outside the
context of one particular step in the sequence. The Additional Results step specifies values to add to the result list of a step.

An additional result is a value TestStand adds to the
 [result list](/csh?context=ts_tsfundamentals_result_collection)
 of a step when the step executes and when you skip a step or force the step to pass or fail. An additional result can be a module parameter or a custom additional result in which you specify the name and value of the result. You can configure TestStand to automatically include additional results in reports and when logging results to a database.

#### Configuring the Step

Use the
 [Additional Results](additional-results-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Additional Results](additional-results-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to add and configure additional results.

#### Step Properties

The Additional Results step type does not define any additional step properties other than the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 all steps contain.

#### See Also

[Built-In Step Types](built-in-step-types.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-installer-options-dialog-box.html language=enus -->
## TOPIC 03362: Advanced Installer Options Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-installer-options-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-installer-options-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the TestStand Deployment Utility and click Advanced Options on the Installer Options tab to launch the Advanced Installer Options dialog box. Refer to <National Instruments>\_Legal Information.txt for information about including legal information in installers built with NI products. The opti

### Advanced Installer Options Dialog Box

TestStand Deployment Utility

Advanced Options

Installer Options

Note

- Refer to
 <National Instruments>\_Legal Information.txt 
 for information about including legal information in installers built with NI products.
- The options in this dialog box apply only to the
 type of deployment 
 you create. Changing the type of deployment might change the options available in this dialog box.

The Advanced Installer Options dialog box contains the following options:

#### Version

- Version Number 
 —Current
 software version number 
 the installer uses to determine the action to perform when an installer file already exists on a computer on which you want to deploy a test system. Increment the installer version number when you change the contents of the installer to ensure that the installer overwrites previous installers that exist on the test station computer. The version corresponds to the
 [ProductVersion] 
 Microsoft Installer (MSI) property.
 Note 
 This control is disabled when the Auto Increment option is enabled.
- Auto Increment 
 —Indicates whether the deployment utility automatically increases the version number when you build an installer to ensure the installer upgrades previous installers on the test station computer. This control is enabled by default, and when enabled, the Version control is disabled.
 Note 
 You must save the deployment before closing the deployment utility to retain the new version number.
- Lock to Deployment Version 
 —Forces the installer to use the same version number as the software version number the deployment utility uses to identify the deployment. If you enable this option, the Version option on the
 Mode 
 tab determines the installer version number, and the deployment utility automatically increments the installer version number each time you build the installer.
 Note 
 If you enable this option when you are creating a
 [patch](/csh?context=ts_tsdeploysystem_createpatch)
 deployment installer and the dependent installer version is later than the current deployment software version number, you must increment the deployment software version number so the current patch deployment installer can update the dependent installer.

#### General Settings

- Installer Executable Name 
 —Specifies the filename of the executable.
- Manufacturer 
 —Name of the company that manufactured the software. This name appears in the standard Windows Control Panel facility for adding and removing programs. This option corresponds to the [Manufacturer] MSI property.
- Upgrade Code 
 —GUID
 
 that uniquely identifies a related set of installers in Windows. You can install only one installer, as identified by its
 unique upgrade code 
 , on a computer at a given time. An installer that specifies the same upgrade code and a later version updates an older installation.
When you copy a TestStand deployment specification file (
 .tsd 
 ), the file uses the same upgrade code as the original file. Complete the following steps to use a different upgrade code in the file you copied.
 
 The upgrade code corresponds to the
 [UpgradeCode] 
 MSI property.
 Note 
 The Upgrade Code is not available when you create a patch deployment. The deployment utility generates a new upgrade code when the patch deployment depends on a full deployment to ensure the patch installer includes the correct components. Future patch installers that depend on the patch deployment use the same upgrade code to update the new patch installer to ensure the new patch installer does not uninstall required components.
  1. Load the
 .tsd 
 file you copied in the deployment utility.
  2. Click the
 Installer Options 
 tab and click the
 Advanced Options 
 button.
  3. Click the
 Generate 
 button to generate a new upgrade code.
  4. Click
 OK 
 to accept the changed upgrade code.
  5. Save the
 .tsd 
 file.
- Generate 
 —Generates a new upgrade code so you can install a newer version of the deployment instead of upgrading an older version of the deployment.
- ReadMe File 
 —Path to a Rich Text Format (
 .rtf 
 ) file the installer displays as the Readme for the installer.
- License Agreement 
 —Path to an
 .rtf 
 file the installer displays as the license agreement for the installer.
- Media Spanning (size in MB) 
 —Maximum size to use for multiple pieces of distribution media when you want to divide an installer that is too large for a single distribution media, such as a CD. Select
 None 
 to create only a single volume.
- Include Network License Server Settings 
 —Indicates whether the target computer is configured to check out licenses from a network server. Your company must have a Volume License Agreement with National Instruments to use this option. This option also copies the server settings found in the Preferences dialog box of the NI License Manager on the build computer.

#### TestStand Specific Settings (Requires Inclusion of TestStand Runtime)

- Specify Configuration Directory 
 —Available only when you install the TestStand Engine to configure the deployed TestStand Engine to read configuration files from the locations the Destination and Destination Subdirectory options specify. If a TestStand Engine is already installed on the test station computer, the installer you build with the deployment utility does not change the location TestStand uses to read the configuration files. Use the
 Preferences 
 tab of the
 Station Options 
 dialog box to change the configuration directory. You can use multiple configuration directories to support
 multiple test systems on one computer 
 .
  - Destination 
 —The base directory for configuration files.
  - Destination Subdirectory 
 —The subdirectory, in the directory the Destination option specifies, for configuration files.
- Alternate Association for .seq Files 
 —Available only when you install the TestStand Engine to specify an executable included in the deployment, typically a user interface, to run when a user double-clicks a
 .seq 
 file in Microsoft Windows Explorer on the test station computer.
 Note 
 The Alternate Association for .seq Files option is available only when you enable the
 Install TestStand Runtime
 option on the
 [Installer Options](installer-options-tab-teststand-deployment-ut.html)
 tab of the deployment utility.
- Process Model Used by TestStand Runtime Installer 
 —Use this option to control which process models to use on the computer to which you deploy the TestStand Runtime using an installer you build with the deployment utility. This setting does not change the settings on the development computer.
 
 Note 
 The Process Model Used by TestStand Runtime Installer option is available only when you enable the
 Install TestStand Runtime
 option on the
 [Installer Options](installer-options-tab-teststand-deployment-ut.html)
 tab of the deployment utility. 
 Note 
 This option is only available in the 32-bit version of the TestStand deployment utility.
  - No Change 
 —Uses the default TestStand 2012 or later process models. This setting does not alter the system settings.
  - Force Default Models 
 —Uses the default process models.
  - Force Legacy Models 
 —Uses the equivalent legacy TestStand 2010 process models.
- Allow Installer to Upgrade an Installed TestStand Runtime 
 —specifies whether the installer you create for a deployment can upgrade an existing installation of the TestStand Runtime. For example, when you enable this option, an installer that contains the TestStand 2014 Runtime can upgrade an existing installation of the TestStand 2014 Runtime.
 When you do not enable this option, the installer cannot install a new version of the TestStand Runtime over an existing service pack version of the TestStand Runtime. For example, when you do not enable this option, an installer that contains the TestStand 2014 SP1 Runtime cannot upgrade an existing installation of the TestStand 2014 Runtime.
 When you do not enable this option, the installer installs drivers and other support files, so you must ensure that those files are compatible with any installed service pack versions of the TestStand Runtime. For example, if you build an installer against TestStand 2014 SP2 and you do not enable this option, you must verify that
 code modules 
 , sequences, and drivers work correctly with TestStand 2014, TestStand 2014 SP1, and TestStand 2014 SP2.
 This option is disabled for installers that do not include the TestStand Runtime and for installers that install a non-service pack version of the TestStand Runtime.

Refer to the
 [Microsoft website](http://www.microsoft.com/en/us/default.aspx)
 for more information about MSI properties.

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

[Patching Deployments](/csh?context=ts_tsdeploysystem_createpatch)

[TestStand Deployment Utility](teststand-deployment-utility.html)

Parent topic:

Installer Options Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-result-processing-settings-dialog-bo.html language=enus -->
## TOPIC 03363: Advanced Result Processing Settings Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-result-processing-settings-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-result-processing-settings-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Advanced button in the Result Processing dialog box to launch the Advanced Result Processing Settings dialog box, in which you configure on-the-fly result processing options that apply to all plug-in instances in all configurations, such as specifying and managing the processing interval a

### Advanced Result Processing Settings Dialog Box

Advanced

Result Processing

create new process model plug-ins

Note

The options in this dialog box apply only to the on-the-fly results processing action TestStand takes when it generates a result. TestStand does not process results for a thread while a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 in the same thread executes, regardless of how long the code module takes to execute. Additionally, these options set only maximum thresholds to trigger result processing. Depending on the internal requirements of the result processing plug-ins you use, on-the-fly result processing might occur more frequently than the maximum values you set in this dialog box.

The Advanced Result Processing Settings dialog box includes the following options:

- Processing Interval 
 —Specifies the duration in seconds to wait after processing on-the-fly results before processing the next set of accumulated on-the-fly results. When a new result is available and time interval exceeds the value you set for this option, TestStand begins processing the results.
 Note 
 A result processing plug-in may impose its own limit on this setting. For example, the default TestStand Report Generator plug-in and the Database Logging plug-in require the processing of collected results before and after making any call to a subsequence.
- Automatically Tune Interval 
 —Enable this option to begin processing the accumulated on-the-fly results when a new result is available and the number of accumulated results equals or exceeds the number of results TestStand estimates it can process within the duration you set in the
 Processing Interval 
 control. Enabling this option helps to ensure that large amounts of rapidly generated results do not cause long pauses in test execution during on-the-fly result processing.
- Maximum Number of Results 
 —Specifies the number of accumulated on-the-fly results at which to begin processing the results. When a new result is available and the number of accumulated on-the-fly results equals or exceeds the value you set for this option, TestStand begins processing the results. Set this value to
 1 
 for TestStand to process each result immediately.
 Note 
 A result processing plug-in may impose its own limit on this setting by setting. For example, a plug-in may override this option by setting
 RunState.Execution.MaximumResultsPerPostResultsCallback
 .
- Create New Result Processor Plug-in 
 —Creates and opens a plug-in sequence file shell in which you complete the entry points you need and delete the entry points you do not require. You must also update
 FileGlobals.ResultProcessorComponentDescription 
 in the plug-in you create to meet the requirements of the plug-in. Refer to the
 examples 
 in the
 <TestStand Public> 
 \Examples\Customizing Result Processing\Model Plugin - Simple Text Report 
 directory for more information about how to implement a custom result processing plug-in
 
 .

#### See Also

[Process Model Plug-In Architecture](/csh?context=ts_tsfundamentals_process_model_plugin_arch)

[Process Model Plug-ins Example](/csh?context=ts_8186)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-settings-dialog-for-python.html language=enus -->
## TOPIC 03364: Advanced Settings Dialog for Python

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-settings-dialog-for-python.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-settings-dialog-for-python.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Advanced Settings Dialog for Python lets you configure the Python interpreter session settings for the step. The Advanced Settings Dialog for Python contains the following options: Use Adapter Settings for Python Interpreter —Settings configured in Python adapter to determine the Python interpre

### Advanced Settings Dialog for Python

The Advanced Settings Dialog for Python lets you configure the Python interpreter session settings for the step. The Advanced Settings Dialog for Python contains the following options:

- Use Adapter Settings for Python Interpreter 
 —Settings configured in Python adapter to determine the Python interpreter session for executing the module.
- Python Interpreter to use 
 —Interpreter to use for the execution. It has the following options:
  - Object Reference 
 —Use the interpreter session present in interpreter reference.
  - Per Thread 
 —Each thread uses a separate instance of the Python interpreter to execute modules.
  - Per Execution 
 —Each execution uses a separate instance of the Python interpreter to execute modules.
  - Global 
 —All Python modules execute in a single instance of the Python interpreter.
- Python Version 
 —Python version to use for executing the Python code module.
- Python Virtual Environment 
 —Path of virtual environment directory to use for executing the Python code module. Leave the field empty to use default environment.
 Note 
 TestStand supports virtual environment created using the virtualenv or venv tool.
- Interpreter Reference 
 —Location of the object reference variable containing the interpreter session to use for executing the Python code module.
- Create Interpreter if it does not exist 
 —When enabled, if the variable specified by
 Interpreter Reference 
 does not contain an interpreter session, executing the step will create an instance of the interpreter session and store in that variable.
- Pass Array of Numbers as 
 —Sets the default behavior for passing an array of numbers from TestStand to the Python code module. It contains the following options:
 
 Note 
 You can override the default behavior in the following ways:
 In the Python Parameter Passing tab of the custom data type properties, configure the
 Pass Property as
 setting for subproperties of the named container.
 In the Python Module tab, configure the Parameter Type to List or NumPy Array.
  - List 
 —Passes an array of numbers from TestStand to the Python code module as a list of numbers.
  - NumPy Array 
 —Passes an array of numbers from TestStand to the Python code module as a NumPy array of numbers.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-settings-tab-edit-labview-vi-call-di.html language=enus -->
## TOPIC 03365: Advanced Settings Tab - Edit LabVIEW VI Call Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-settings-tab-edit-labview-vi-call-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-settings-tab-edit-labview-vi-call-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Advanced Settings Tab The LabVIEW Advanced Settings tab contains the following options: Run VI on a Remote Computer —Specifies a VI for remote call. This section contains the following options: Remote Host —The remote computer to use to run the VI. Specify Expression For Host —Specifies whether the

### Advanced Settings Tab - Edit LabVIEW VI Call Dialog Box

#### Advanced Settings Tab

The LabVIEW Advanced Settings tab contains the following options:

- Run VI on a Remote Computer 
 —Specifies a VI for remote call. This section contains the following options:
  - Remote Host 
 —The remote computer to use to run the VI.
  - Specify Expression For Host 
 —Specifies whether the Remote Host control contains an expression the LabVIEW Adapter evaluates at run time to determine the name of the remote host.
  - Remote Project Path 
 —The path and name of the LabVIEW project the step calls on the remote computer. When you specify an absolute or relative path, the remote computer loads the LabVIEW project into memory, if it is not already open. When the path is relative, the remote computer interprets the path as relative to the application directory, if applicable. Specifying a remote LabVIEW project path is optional.
  - Remote VI Path 
 —The path and name of the VI the step calls on the remote system. When you specify an absolute or relative path, the remote computer loads the VI into memory, if it is not already open. When the path is relative, the remote computer interprets the path as relative to the application directory, if applicable. If a VI of the same name is already in memory, the VI is used regardless of whether the path of the VI is the same as the path specified.
 Note 
 If a path is not specified in the Remote VI Path control, the remote system will download the VI specified in the VI Pathname control on the
 [Module](module-tab-edit-labview-vi-call-dialog-box.html)
 tab, if it is not already in memory and if the remote system is running LabVIEW Real-Time Module to which TestStand can download.
 If the step calls an Express VI, the Remote VI Path control is disabled. Express VIs are downloaded to a real-time system that uses LabVIEW if supported by TestStand.
 If the step uses a Remote Project Path, the Remote VI Path control specifies the URL of the VI within the defined LabVIEW project.
  - Port Number 
 —The TCP/IP port number to use to connect to the remote system.
  - Timeout (ms) 
 —The time, in milliseconds, to wait for a connection before timing out.
- Always Run VI in LabVIEW Run-Time Engine 
 —When you enable this option, you can always use a LabVIEW Run-Time Engine (RTE) to run the VI, regardless of the global
 LabVIEW Adapter 
 setting. TestStand selects the appropriate version of the LabVIEW RTE according to the version of LabVIEW in which you last compiled the VI. This guarantees that the VI will always be loaded with a specific version of the LabVIEW RTE, even if another version exists. Use this option when you do not want the global settings for the adapter to affect the tools and step types you create.
 Note 
 TestStand can use newer versions of the LabVIEW RTE when you install LabVIEW on your development system. You can include newer versions of the LabVIEW RTE in deployments using the
 [Drivers and Components](drivers-and-components-dialog-box.html)
 dialog box of the
 [TestStand Deployment Utility](teststand-deployment-utility.html)
 .
- Array Parameters Match LabVIEW Array Dimensions 
 —Constrain array parameters to match the size of the corresponding LabVIEW array control or indicator in every dimension. When enabled, the data at each index of a multi-dimensional array in TestStand and the corresponding control or indicator in LabVIEW will be the same when passing arrays during execution.
 Note 
 After you change this option, you must reload the module before you can execute it. An error indicator on the Module tab of the
 [Step Settings](step-settings-pane.html)
 pane will prompt you to reload the module.

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

Parent topic:

Edit LabVIEW VI Call Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-settings-window.html language=enus -->
## TOPIC 03366: Advanced Settings Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-settings-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-settings-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Advanced Settings button on the .NET Module tab of the Step Settings pane in the TestStand Sequence Editor or on the Module tab of the Edit .NET Call dialog box in a TestStand User Interface to launch the Advanced Settings window, which contains the following option: Use Step Load/Unload O

### Advanced Settings Window

Click the
 Advanced Settings
 button on the
 [.NET Module](net-module-tab.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or on the
 [Module](module-tab-edit-net-call-dialog-box.html)
 tab of the
 [Edit .NET Call](edit-net-call-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to launch the Advanced Settings window, which contains the following option:

- Use Step Load/Unload Options to Specify Object Creation and Lifetime 
 —Controls the lifetime of the root object the step creates. When you do not set this option, the step creates the object when the step begins and the step releases the internal reference of the step to the object when the step completes. When you enable this option, the step creates the object when the step loads according to the Load option of the step and holds an internal reference to the object until the step unloads according to the Unload option of the step.
- Allow unload of the assemblies specified in the step 
 — The .Net adapter loads the assemblies specified in the step into a collectible AssemblyLoadContext so they can be unloaded if required. .NET Core doesn't support loading C++/CLI (mixed-mode) assemblies into collectible AssemblyLoadContexts. To allow loading C++/CLI assemblies in a .NET step, uncheck this option.

Note

#### See Also

[Edit .NET Call dialog box](edit-net-call-dialog-box.html)

[.NET Module Tab](net-module-tab.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-tab-data-link-properties-dialog-box.html language=enus -->
## TOPIC 03367: Advanced Tab - Data Link Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-tab-data-link-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-tab-data-link-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Advanced Tab Refer to the documentation you received with the OLE DB provider for more information about advanced initialization properties. Click Help to display the Microsoft online help for this tab.

### Advanced Tab - Data Link Properties Dialog Box

#### Advanced Tab

Refer to the documentation you received with the OLE DB provider for more information about advanced initialization properties.

Click
 Help
 to display the Microsoft online help for this tab.

Parent topic:

Data Link Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-tab-edit-open-sql-statement-dialog-b.html language=enus -->
## TOPIC 03368: Advanced Tab - Edit Open SQL Statement Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-tab-edit-open-sql-statement-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-tab-edit-open-sql-statement-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Advanced Tab The Advanced tab of the Edit Open SQL Statement dialog box specifies optional attributes TestStand can set when opening an SQL statement. In most cases, the database defines default values for each attribute. When you select the Use Default option, the step does not set the attribute. S

### Advanced Tab - Edit Open SQL Statement Dialog Box

#### Advanced Tab

The Advanced tab of the Edit Open SQL Statement dialog box specifies optional attributes TestStand can set when opening an SQL statement. In most cases, the database defines default values for each attribute. When you select the Use Default option, the step does not set the attribute. Some databases do not support all the attributes in the Edit Open SQL Statement dialog box.

The Advanced tab contains the following options:

- Page Size in Records 
 —The number of records in a page.
- Max Records to Select 
 —The maximum number of records the connection returns from the data source.
- Command Timeout 
 —The number of seconds TestStand waits for a command to execute.
- Cache Size 
 —The number of records the connection maintains in a memory buffer and how many records the connection retrieves at one time.
- Cursor Type 
 —The type of cursor for the SQL statement. Select one of the following options from the ring control:
  - Dynamic 
 —Additions, changes, and deletions by other users are visible, and all types of movement through the set of records are allowed.
  - Static 
 —Additions, changes, or deletions by other users are not visible.
  - Forward Only 
 —Identical to a static cursor, except you can only scroll forward through records. This improves performance when you want to make a single pass through a set of records.
  - Keyset 
 —Similar to a dynamic cursor, except you cannot see records other users add. Records other users delete are inaccessible from your set of records. Data changes by other users within records are visible.
- Cursor Location 
 —Specifies where the data source maintains cursors for a connection. Select one of the following options from the ring control:
  - Server 
 —Uses cursors the data provider supplies. These cursors are sometimes very flexible and allow for additional sensitivity to reflect changes other users make to the actual data.
  - Client 
 —Uses client-side cursors a local cursor library supplies. Local cursor engines often allow many features driver-supplied cursors might not.
- Marshal Options 
 —Specifies how modified data is written back to the server. Select one of the following options from the ring control:
  - Write All Records 
 —All records are written back to the server.
  - Write Modified Records Only 
 —Only modified data is written back to the server.
- Lock Type 
 —Specifies when the data source locks a record. Select one of the following options from the ring control:
  - Read Only 
 —You cannot alter the data in a record.
  - Pessimistic 
 —The provider does what is necessary to ensure successful editing of the records, usually by locking records at the data source immediately upon editing.
  - Optimistic 
 —The provider only locks records when you put the data back to the database.
  - Batch Optimistic 
 —This type is required for batch updates.
- Command Type 
 —Specifies how Microsoft ActiveX Data Objects (ADO) interprets the SQL statement. Select one of the following options from the ring control:
  - Unknown 
 —Microsoft ADO attempts to determine the command type.
  - Text 
 —SQL statement or, for some providers, a command string in the command language the provider uses.
  - Table 
 —Used for a table name.
  - Stored Procedure 
 —A call to a stored procedure.

Parent topic:

Edit Open SQL Statement Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-tab-edit-rule-dialog-box.html language=enus -->
## TOPIC 03369: Advanced Tab - Edit Rule Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-tab-edit-rule-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-tab-edit-rule-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Advanced Tab The Advanced tab contains the following options: Resource String Category —Category in the resource ( .ini ) file you create in the <TestStand Public> \Components\Language directory. The tags in the category section of the .ini file indicate to localize the strings associated with the c

### Advanced Tab - Edit Rule Dialog Box

#### Advanced Tab

The Advanced tab contains the following options:

- Resource String Category 
 —Category in the resource (
 .ini 
 ) file you create in the
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \Components\Language 
 directory. The tags in the category section of the
 .ini 
 file indicate to
 localize the strings 
 associated with the custom rule name, description, settings, and enumeration item names. Leave this control empty if you do not want to localize any strings.
- Configuration Option 
 —
 Configuration option 
 for the rule. You can choose from the following options:
 
 When you select the Use Configuration Module or Use Rule Settings options, the TestStand Sequence Analyzer includes a
 Settings 
 button next to the rule name in the Rule column on the
 Rules 
 pane of the
 Current Sequence Analyzer Project 
 window in the
 TestStand Sequence Editor 
 or on the
 Rules 
 tab of the stand-alone
 TestStand Sequence Analyzer application 
 .
  - None 
 —The custom rule is not configurable.
  - Use Configuration Module 
 —The TestStand Sequence Analyzer configures the custom rule by invoking a
 rule configuration module 
 that launches a custom dialog box. Entering a VI path hides the Function control and displays the Run VI in LabVIEW Run-Time Engine control. Entering a DLL path displays the Function control. Entering a .NET assembly path displays the Class and Method controls. Entering a LabVIEW NXG project displays a Module Name control that allows you to choose a VI from the selected project.
 Select this option when you want to accomplish any of the following: 
 
 When you select this option, you must enter the path of the VI, .NET assembly, DLL module, or LabVIEW NXG project the sequence analyzer calls to configure the rule. For .NET assemblies, you must also specify the class and method to call. For DLLs, you must also specify the function in the DLL to call. For LabVIEW NXG, you must specify the name of a VI within the selected project.
    - Create a custom dialog box in LabVIEW, LabWindows/CVI, .NET, Microsoft Visual C++, or LabVIEW NXG to configure the custom rule
    - Store data more complex than Boolean, number, string, or enumeration values, such as a list of string values
    - Use custom controls, tree controls, or list controls in a dialog box
    - Run VI in LabVIEW Run-Time Engine 
 —When you enable this option, you can always use a LabVIEW Run-Time Engine (RTE) to run the VI, regardless of the global
 LabVIEW Adapter 
 setting. This option specifies that the LabVIEW Adapter settings must be ignored and the VI must be loaded with the same version of the LabVIEW RTE in which the VI was last compiled. This guarantees that the VI will always be loaded with a specific version of the LabVIEW RTE, even if another version exists.
 
 When you disable this option, the sequence analyzer uses the LabVIEW Adapter settings to determine whether to run the VI in the LabVIEW RTE or in the LabVIEW development system.
    - Function 
 —Name of the function in the DLL that the sequence analyzer calls. This control is visible only when you enter a path to a DLL.
    - Class 
 —Name of the class in the .NET assembly that has the method the sequence analyzer calls. This control is visible only when you enter a path to a .NET assembly.
    - Method 
 —Name of the method on the class in the .NET assembly that the sequence analyzer calls. This control is visible only when you enter a path to a .NET assembly.
    - Allow Unload of .NET Assemblies 
 —Uncheck this option to load C++/CLI (mixed-mode) .NET assemblies as the configuration module. C++/CLI assemblies can't be unloaded. This control is visible only when you enter a path to a .NET assembly.
    - Module Name 
 —The VI from the LabVIEW NXG project that the sequence analyzer calls. This control is visible only when you enter a LabVIEW NXG project in the Path control.
  - Use Rule Settings 
 —The sequence analyzer configures the custom rule by launching the
 Rule Settings 
 dialog box, which shows individual
 rule settings 
 . When you select this option, you can add, remove, and edit rule settings, including settings for the custom setting name, type, and default value. The sequence analyzer uses the Resource String Category option on this tab to localize rule setting names. Select this option when you do not need to create a custom dialog box to configure the rule.
 Rule settings can have number, string, Boolean, or enumeration types. The sequence analyzer saves the values for the rule settings in the analyzer project. During analysis, the corresponding rule module accesses the setting values from the
 RuleConfiguration.RuleSettingValues 
 property for the rule. The following table describes the kind of controls the Rule Settings dialog box specifies for each setting type and the type of data stored in the
 RuleSettingValue 
 object.
 Rule Setting Type
 Control in Rule Settings Dialog Box
 Type of RuleSettingValue.Value
 CommentsNumber
 Text control
 Double
 You must enter a valid floating-point number.
 String
 Text control
 String
 You can enter any string.
 Boolean
 Checkbox control
 Boolean
 —
 Rule Settings Enumeration
 Ring control
 Double
 Each item in the ring control corresponds to an item in the enumeration. 
 Use a rule settings enumeration type when you want to select a named value from a list you define. Click the
 Enums 
 button located to the right of the rule settings table to launch the
 Edit Rule Settings Enumerations 
 dialog box, in which you create new rule settings enumeration types to use for rule settings. You can customize the rule description to include information about the setting values by adding the text
 %(
 SettingName
 ) 
 to the Description control on the
 General 
 tab of the Edit Rule dialog box. The sequence analyzer replaces each instance of the string
 %(
 SettingName
 ) 
 in the rule description with the value for the setting named SettingName.

#### See Also

[Accessing Rule Configuration Data in Rule Configuration Modules and Analysis Modules](/csh?context=ts_tsref_sa_accessing_rule_config_data)

[Accessing Rule Settings in Analysis Modules](/csh?context=ts_tsref_sa_accessing_rule_settings)

[Creating Rule Configuration Modules](/csh?context=ts_tsref_sa_creating_rule_config_modules)

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[Edit Rule Settings Enumerations dialog box](edit-rule-settings-enumerations-dialog-box.html)

[Effectively Using LabVIEW with TestStand](/csh?context=ts_10208)

Effectively Using LabVIEW NXG with TestStand

[LabVIEW Adapter](/csh?context=ts_tsref_labview)

[Localizing Custom Rules](/csh?context=ts_tsref_sa_localizing_custom_rules)

[Making a Custom Rule Configurable](/csh?context=ts_tsref_sa_making_custom_rule_config)

[Rule Settings dialog box](rule-settings-dialog-box.html)

[RuleConfiguration.RuleSettingValues](../tsanalyzer/ruleconfiguration-rulesettingvalues.html)

[TestStand Sequence Analyzer Application](teststand-sequence-analyzer-application.html)

Parent topic:

Edit Rule Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/advanced-tab-sequence-file-properties-dialog.html language=enus -->
## TOPIC 03370: Advanced Tab - Sequence File Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/advanced-tab-sequence-file-properties-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/advanced-tab-sequence-file-properties-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Advanced Tab The Advanced tab contains the following options: Type —Specifies one of the following type settings for the sequence file: Normal —Sequence file that is not a Model callback sequence, callback file, or reserved. Model —A sequence that defines the default behavior of the process model. T

### Advanced Tab - Sequence File Properties Dialog Box

#### Advanced Tab

The Advanced tab contains the following options:

- Type 
 —Specifies one of the following type settings for the sequence file:
 
 When you use the sequence file as a process model, set the type to
 Model 
 . When you do not use the file as a process model, leave the type set to
 Normal 
 .
  - Normal 
 —Sequence file that is not a Model callback sequence, callback file, or reserved.
  - Model 
 —A sequence that defines the default behavior of the process model. The client sequence file can customize the default behavior of its sequence if the client sequence file contains a sequence by the same name.
  - Front-End Callbacks 
 —Common sequence the
 TestStand Sequence Editor 
 and User Interfaces call. Front-End callbacks allow multiple applications to share the same implementation for a specific operation. TestStand installs the
 FrontEndCallback.seq 
 sequence file, which contains the LoginLogout Front-End callback sequence.
  - Station Callbacks 
 —Sequence file that contains a sequence that runs before and after the engine executes each step in any normal or interactive execution.
  - Reserved 
 —Contains sequences that designate templates for newly inserted callbacks.

The following options are available when you select
 Normal
 from the Type ring control:

- Model Option 
 —Select one of the following settings for the process model file to use for the sequence file.
  - Use Station Model 
 —Causes TestStand to use the process model file the Station Model option specifies in the
 Station Options 
 dialog box. This is the default setting for this option.
  - No Model 
 —Specifies that the sequence file does not use a process model.
  - Require Specific Model 
 —A particular process model file. When you select this value, the tab displays a Model File control you can use to specify the location of a process model file.
 Note 
 The Require Specific Model setting is valid only when you enable the
 Allow Other Models
 option on the
 [Model](model-tab-station-options-dialog-box.html)
 tab of the
 [Station Options](station-options-dialog-box.html)
 dialog box.
- Password Protection 
 —When you enable this option, the sequence file is protected and you can change the lock state of the file. The sequence editor and user interfaces prevent viewing and editing of locked sequence files. Use the
 Lock/Unlock 
 button with the password controls to lock, unlock, and password protect the file.
 The sequence editor and user interfaces, which use the TestStand User Interface (UI) Controls, display a lock icon to indicate non-viewable items within a locked file. The sequence editor prompts you to unlock the file when you attempt to edit or save the file, or when you double-click the lock icon in a non-viewable list view of the Sequence File window or the
 [Variables](variables-pane-execution-window.html)
 pane in the Execution window. 
 Note 
 TestStand supports password protecting sequence files to deter editing and viewing within the sequence editor and user interfaces that use the TestStand UI Controls. The TestStand API limits access to a file protected from viewing but cannot prevent access to the file content during execution. National Instruments does not recommend using passwords as the only way of protecting intellectual property.
- Attributes 
 —Launches the
 Attributes 
 dialog box, in which you can create and edit attributes for the sequence file.

#### See Also

[Edit Attributes dialog box](attributes-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

[Variables Pane](variables-pane-execution-window.html)

Parent topic:

Sequence File Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/analysis-modules-tab-configure-sequence-analy.html language=enus -->
## TOPIC 03371: Analysis Modules Tab - Configure Sequence Analyzer Available Rules Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/analysis-modules-tab-configure-sequence-analy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/analysis-modules-tab-configure-sequence-analy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Analysis Modules Tab Use the Analysis Modules tab to add, remove, and edit custom analysis module specifications on the computer. The Analysis Modules tab contains the following sections: BuiltinRules.tsarules —Shows the settings of the built-in analysis modules National Instruments provides. TestSt

### Analysis Modules Tab - Configure Sequence Analyzer Available Rules Dialog Box

#### Analysis Modules Tab

Use the Analysis Modules tab to add, remove, and edit custom
 [analysis module specifications](/csh?context=ts_tsref_sa_creating_custom_rules)
 on the computer.

The Analysis Modules tab contains the following sections:

- BuiltinRules.tsarules 
 —Shows the settings of the built-in analysis modules National Instruments provides. TestStand stores the analysis module settings in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Analyzer\BuiltinRules.tsarules 
 file.
 Note 
 You cannot modify the built-in modules.
- CustomRules.tsarules 
 —Shows the settings of the custom analysis modules on the computer. TestStand stores the analysis module settings in the
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\CustomRules.tsarules 
 file.

Right-click an analysis module and select
 Insert Analysis Module
 from the context menu to create a custom analysis module specification. You can also click the
 New Analysis Module
 button located to the right of the
 <Insert New Analysis Module>
 item in the Rule ID column to launch the Edit Analysis Module dialog box.

Double-click an analysis module specification, right-click an analysis module specification and select
 Edit Analysis Module
 from the context menu, or click the
 Edit Analysis Module
 button located to the right of the Module column to launch the
 [Edit Analysis Module](edit-analysis-module-dialog-box.html)
 dialog box, in which you can view the settings for built-in analysis modules and edit the settings for custom analysis modules.

You can drag and drop custom analysis modules to change the order of the list, which the TestStand Sequence Analyzer uses to determine the order in which to call the analysis modules. The sequence analyzer runs the built-in analysis modules before any custom analysis modules. You can cut, copy, paste, and delete custom analysis modules.

Before you edit an analysis module DLL or VI, you must unload the analysis module from memory. You can unload all analysis modules by right-clicking anywhere on the Analysis Modules tab and selecting Unload All Modules from the context menu. In the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , you can also select
 File»Unload All Modules
 to unload all modules, including analysis modules, from memory.

#### See Also

[Creating Analysis Modules for Custom Rules](/csh?context=ts_tsref_sa_creating_analysis_modules)

[Creating Custom Rules](/csh?context=ts_tsref_sa_creating_custom_rules)

[Edit Analysis Module dialog box](edit-analysis-module-dialog-box.html)

Parent topic:

Configure Sequence Analyzer Available Rules Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/analysis-results-pane.html language=enus -->
## TOPIC 03372: Analysis Results Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/analysis-results-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/analysis-results-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Analysis Results pane includes an Analyzer Messages tab for the current analyzer project and for each sequence file and workspace file you analyze. When you open a sequence file or analyze a workspace file for the first time, the TestStand Sequence Editor creates a tab on the Analysis Results pa

### Analysis Results Pane

The Analysis Results pane includes an
 [Analyzer Messages](analyzer-messages-tab-analysis-results-pane.html)
 tab for the current analyzer project and for each sequence file and workspace file you analyze. When you open a sequence file or analyze a workspace file for the first time, the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 creates a tab on the Analysis Results pane with the same name as the
 [Sequence File](sequence-file-window.html)
 window or
 [Workspace](workspace-pane.html)
 pane caption. These tabs display the analyzer messages for the analysis of the sequence files or workspace files. The TestStand Sequence Analyzer reuses these tabs each time you analyze a sequence file or workspace file.

When you create or open an analyzer project, the sequence editor creates a tab on the Analysis Results pane with the same name as the
 [Current Sequence Analyzer Project](current-sequence-analyzer-project-window.html)
 window caption. This tab contains the analyzer messages in the current analyzer project.

The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 removes the corresponding Analyzer Messages tab when you close a sequence file, workspace file, or the Current Sequence Analyzer Project window.

You can float and resize the Analysis Results pane for easier processing of analyzer messages. When you float the Analysis Results pane, you can resize the pane to show more messages, and you can move the pane outside the main sequence editor window so you do not obscure the pane when you view the object in the TestStand file that caused the analysis message.

#### See Also

[Current Sequence Analyzer Project window](current-sequence-analyzer-project-window.html)

[Sequence Analyzer Messages Tab Context Menu](messages-tab-context-menu-teststand-sequence.html)

[Sequence File Window](sequence-file-window.html)

[Workspace Pane](workspace-pane.html)

Parent topic:

Panes

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/analysis-summary-tab-teststand-sequence-analy.html language=enus -->
## TOPIC 03373: Analysis Summary Tab - TestStand Sequence Analyzer Application

- bundle_id: `teststand-api-reference`
- source_path: `tsref/analysis-summary-tab-teststand-sequence-analy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/analysis-summary-tab-teststand-sequence-analy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Analysis Summary Tab Use the Analysis Summary tab to view the status of the most recent analysis of the project. This tab shows the status, start time, elapsed time, user name, and computer name of the most recent analysis. A status of Stopped indicates that analysis stopped before it completed. Thi

### Analysis Summary Tab - TestStand Sequence Analyzer Application

#### Analysis Summary Tab

Use the Analysis Summary tab to view the status of the most recent analysis of the project.

This tab shows the status, start time, elapsed time, user name, and computer name of the most recent analysis. A status of Stopped indicates that analysis stopped before it completed. This tab also shows the number of messages from the most recent analysis.

The Analyzed Files control lists the analyzed files and the number of messages associated with each file.

#### See Also

[Sequence Call Step](sequence-call-step.html)

[Types Window](types-window.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/analyzer-messages-tab-analysis-results-pane.html language=enus -->
## TOPIC 03374: Analyzer Messages Tab - Analysis Results Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/analyzer-messages-tab-analysis-results-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/analyzer-messages-tab-analysis-results-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Analyzer Messages Tab Use the Analyzer Messages tab to view and resolve the messages for the most recent analysis of the current TestStand Sequence Analyzer project, sequence file, or workspace file in the order in which the analyzer generated them. In the TestStand Sequence Editor , the sequence an

### Analyzer Messages Tab - Analysis Results Pane

#### Analyzer Messages Tab

Use the Analyzer Messages tab to view and resolve the messages for the most recent analysis of the current TestStand Sequence Analyzer project, sequence file, or workspace file in the order in which the analyzer generated them. In the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , the sequence analyzer creates messages tabs for each sequence file you open and each analyzer project or workspace file you analyze. Each time you start an analysis session of an analyzer project or workspace file, the sequence analyzer overwrites the content of the Analyzer Messages tab. When you analyze a sequence file, the sequence analyzer overwrites the content of the tab except for the messages shown in the
 Messages the Sequence File Ignores
 view.

The Analyzer Messages tab contains the following buttons:

| Command Name | Icon | Description |
| --- | --- | --- |
| Restart Analysis |  | Restarts the analysis of the current analyzer project, sequence file, or workspace file. |
| Stop Analysis |  | Stops the analysis of the current analyzer project, sequence file, or workspace file. |
| Current Sequence Analyzer Project |  | Shows the Current Sequence Analyzer Project window. |
| Generate Analysis Report |  | Saves the messages for the most recent analysis in an XML report file to use in an external viewer. The XML file uses the AnalyzerReportViewer.xsl style sheet, located in the <TestStand> \\Components\\Stylesheets\\Analyzer directory. Use the XML Packaging Utility to package the files necessary to view the XML report on a computer that does not have TestStand installed. When you generate a report file, the sequence analyzer provides a snapshot of the most recent analysis, including a list of the analyzed files, a list of the rules and settings used during the analysis, and a list of all the generated messages. The report file does not include the list of messages the sequence files ignored during analysis. |
| Sequence Analyzer Options |  | Launches the Sequence Analyzer Options dialog box, in which you edit settings the sequence analyzer uses to analyze the active sequence file. Note The sequence editor requires an enabled ConfigApp user privilege to launch the Sequence Analyzer Options dialog box. The built-in TestStand Developer and Administrator user groups grant this privilege by default. |

The Analyzer Messages tab contains the following controls:

- Show 
 —Filters the messages to show in the Messages list. You can also show the list of analyzed files. The Show ring control contains the following options:
  - Active Messages 
 —Shows the messages in the current analyzer project, sequence file, or workspace file that represent the issues you must address by marking the message as ignored or fixed.
  - Messages the Analyzer Project Ignores 
 —Shows the messages in the current analyzer project or workspace file that you marked to ignore in future analysis. The sequence analyzer maintains this list and does not report these messages again in subsequent analysis sessions. When analyzing the analyzer project, the sequence analyzer stores this list in the analyzer project file.
 Right-click a message and select
 Mark Message as Active 
 from the context menu to return the message to the Active Messages view.
 Dimmed messages in this view indicate that the most recent analysis of the current project or workspace file did not generate the message. You cannot make dimmed messages active, but you can right-click the dimmed message and select
 Delete Message 
 from the context menu to remove the message from the current project.
  - Messages the Sequence File Ignores 
 —Shows the messages in the current sequence file that you marked to ignore in future analysis. The sequence analyzer stores this list with the sequence file and does not report these messages again in subsequent analysis sessions.
  - Messages Marked as Fixed 
 —Shows the messages in the current analyzer project, sequence file, or workspace file that you marked as fixed. The sequence analyzer reports these messages again in future analysis sessions if you do not fix the issue itself.
 Right-click a message and select
 Mark Message as Active 
 from the context menu to return the message to the Active Messages view.
  - Analyzed Files 
 —Shows the list of files the sequence analyzer analyzed for the most recent analysis session and the number of messages associated with each file.
- Group By 
 —Specifies how to group the messages in the Messages list. Click the column headers to resort the list. The Group By ring control is disabled when you set the Show ring control to Analyzed Files. The Group By ring control contains the following options:
  - <None> 
 —Shows the messages in the order in which the sequence analyzer generated them.
  - Severity 
 —Groups the messages in alphabetical order by message severity level.
  - Rule 
 —Groups the messages in alphabetical order by the rule associated with each message.
  - Category 
 —Groups the messages in alphabetical order by the category of the rule associated with each message.
  - Text 
 —Groups the messages in alphabetical order by the message text.
  - File 
 —Groups the messages in alphabetical order by the file that generated the message.
  - Location 
 —Groups the messages in alphabetical order by the property path of the object that generated the message.
  - Justification to Ignore 
 —Groups the messages in alphabetical order by the justification to ignore text associated with a message marked as ignored.
- Messages List 
 —List of messages for the current analyzer project, sequence file, or workspace file in the order in which the sequence analyzer generated them. The sequence analyzer adds new messages to the bottom of the list.
 Right-click the list to display the
 context menu 
 , which you use to resolve each message and specify which columns to show or hide. You can also right-click the column header to show or hide columns. Click the column header to resort the messages in the list. Drag the column header to reorder the columns.
- Message Details 
 —Details for the analysis message you select, including suggestions for how to fix the related issue. This control is empty when you select more than one message.

#### See Also

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

[Sequence Analyzer Messages Tab Context Menu](messages-tab-context-menu-teststand-sequence.html)

[XML Packaging Utility](xml-packaging-utility.html)

Parent topic:

Analysis Results Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/analyzer-messages-tab-context-menu-analysis-r.html language=enus -->
## TOPIC 03375: Analyzer Messages Tab Context Menu - Analysis Results Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/analyzer-messages-tab-context-menu-analysis-r.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/analyzer-messages-tab-context-menu-analysis-r.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Analyzer Messages Tab Analyzer Messages Tab Context Menu Right-click an item in the Messages list on the Analyzer Messages tab to launch the context menu, which can contain the following options depending on the item you select: Goto Location —Opens the TestStand file and locates the object that cau

### Analyzer Messages Tab Context Menu - Analysis Results Pane

#### Analyzer Messages Tab

#### Analyzer Messages Tab Context Menu

Right-click an item in the Messages list on the Analyzer Messages tab to launch the context menu, which can contain the following options depending on the item you select:

- Goto Location 
 —Opens the TestStand file and locates the object that caused the message. You can also double-click a message in the Messages list to go to the location of the object in the TestStand file that caused the message.
- Mark Message as Ignored in Sequence File 
 —Ignores the messages you select in subsequent analysis sessions by moving the messages from the Active Messages view to the sequence file. You can view the messages marked as ignored in a sequence file by selecting the
 Messages the Sequence File Ignores 
 from the Show dropdown. When you mark a message as ignored, the sequence analyzer prompts you for text that provides the justification to ignore the message. The Justification to Ignore column displays the text you enter for the messages.
- Mark Message as Ignored in Analyzer Project 
 —Ignores the messages you select in subsequent analysis sessions and moves the messages from the Active Messages view of each Analyzer Messages tab that includes the messages to the ignored messages view of each tab. When you mark a message as ignored, the sequence analyzer prompts you for text that provides the justification to ignore the message. The Justification to Ignore column displays the text you enter for the messages
 Select this option only when you are sure the issue will not cause a run-time error. For example, if the subsequent analyzer session reports an undefined local variable in a step expression and you know a step in the sequence creates that local variable, you can safely ignore the error message. As another example, if the TestStand Sequence Analyzer warns about a potentially unused variable and you know a
 code module 
 uses the variable, you can safely ignore the message.
 If the sequence analyzer generates a message when analyzing a file that contains a TestStand type, the analyzer also generates a nearly identical message when analyzing other files that contain the same type. The messages for each file differ only with respect to the specified filename. When you mark any of these messages as ignored, the analyzer ignores the messages for all files that contain the type.
 Disable a rule on the
 Rules 
 pane of the
 Current Sequence Analyzer Project 
 window to ignore all messages for that rule in subsequent analysis.
- Mark Message as Fixed 
 —Marks the messages you select as fixed and moves the messages from the Active Messages view of each Analyzer Messages tab that includes the messages to the Fixed view of each tab. When you mark an issue as fixed, the sequence analyzer reports the message again in subsequent analysis sessions if you do not fix the issue itself.
- Mark Message as Active 
 —Marks the messages you select as active and moves the messages from the ignored messages view or the Messages Fixed view of each Analyzer Messages tab that includes the messages to the Active Messages view of each tab.
- Delete Message 
 —Removes the messages you select from the current project. When analyzing sequence files, this option is available only for messages in the Messages the Sequence File Ignores view. When analyzing an analyzer project or workspace file, this option is available only for dimmed messages in the Messages the Analyzer Project Ignores view, which indicates that the most recent analysis of the current analyzer project or workspace file did not generate the message.
- Goto Rule 
 —Locates the rule on the Rules pane of the Current Sequence Analyzer Project window so you can disable or configure the rule.
- Columns 
 —Launches the Columns context menu, which you use to show and hide columns.

#### See Also

[Current Sequence Analyzer Project Window](current-sequence-analyzer-project-window.html)

Parent topic:

Analyzer Messages Tab - Analysis Results Pane

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/appearance-tab-configuration-properties-dialo.html language=enus -->
## TOPIC 03376: Appearance Tab - Configuration Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/appearance-tab-configuration-properties-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/appearance-tab-configuration-properties-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Appearance Tab The Appearance tab contains the following options: Comments —Specifies how step comments are displayed. Display Step Comments —Displays step comments above the step. Draw Comment Bar —Draws a vertical bar to the left of step comments. Lines to Display —The maximum number of comment li

### Appearance Tab - Configuration Properties Dialog Box

#### Appearance Tab

The Appearance tab contains the following options:

- Comments 
 —Specifies how step comments are displayed.
  - Display Step Comments 
 —Displays step comments above the step.
  - Draw Comment Bar 
 —Draws a vertical bar to the left of step comments.
  - Lines to Display 
 —The maximum number of comment lines to display for a step.
- Grid Lines 
 —Enables horizontal and vertical grid lines.
  - Horizontal 
 —Draws horizontal lines between steps.
  - Vertical 
 —Draws vertical lines between columns.
- Block Display Options 
 —Controls the appearance of steps, such as Flow Control steps, that define a block structure in a sequence.
  - Indent Blocks 
 —Indents the steps within a block.
  - Show Block Lines 
 —Draws a vertical bar to the left of the steps in a block.
  - Show Step Group Lines 
 —Draws a vertical line to the left of the steps to outline each step group. This option is available only when you enable the
 Show Block Lines 
 option.
  - Dotted Block Lines 
 —Draws the vertical bar to the left of the block with a dotted line. This option is available only when you enable the
 Show Block Lines 
 option.
  - Show Block Step Icons 
 —Displays icons for steps that define or operate according to the block structure of the sequence.
  - Bold Block Step Font 
 —Displays the step name in bold for steps that define or operate according to the block structure of the sequence.
  - Highlight Block Mismatch Errors 
 —Draws the step name in red for steps that start blocks that do not have an ending step and for block ending steps that do not match with a block starting step. Also draws the vertical block bar red for blocks that do not have an ending step.
- Appearance 
 —Defines the look and feel of the control.
  - Make Columns Always Fit 
 —When you enable this option, every column for which you enable the Autosize option on the
 Columns 
 tab of the
 Configuration Properties 
 dialog box automatically expands or contracts when the control size changes so all of the columns fit within the available space.
  - Shade Alternate Columns 
 —When you enable this option, TestStand uses slightly darker color to paint the background for the alternate columns.
  - Round Cells 
 —When you enable this option, TestStand uses rounded corners to draw the background for the individual cells. By default all cells have the same background color as the control. However, you can alter an individual cell background using the
 SeqViewColumn.BackColorExpression 
 property.
  - Show Step Icons 
 —When you enable this option, TestStand draws the step icons.
  - Icon Size 
 —The size of icons that display in the control. Icons are always square. For example, when you select 32 in the Icon Size control, the icon dimensions are 32 x 32 pixels.

#### See Also

[Configuration Properties dialog box](configuration-properties-dialog-box.html)

[SeqViewColumn.BackColorExpression](../tsuiref/seqviewcolumn-backcolorexpression.html)

Parent topic:

Configuration Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/apply-configuration-edit-tab.html language=enus -->
## TOPIC 03377: Apply Configuration Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/apply-configuration-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/apply-configuration-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Apply Configuration edit tab in the TestStand Sequence Editor to specify which configuration to apply to existing IO sessions. The Apply Configuration edit tab contains the following options: IO Configuration —The name of the IO Configuration that is applied to IO sessions. Use the dropdown

### Apply Configuration Edit Tab

Use the Apply Configuration edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify which configuration to apply to existing IO sessions.

The Apply Configuration edit tab contains the following options:

- IO Configuration 
 —The name of the IO Configuration that is applied to IO sessions. 
 Use the dropdown menu to select from one of the exported configurations. Click
 Edit IO Configuration 
 to edit the selected IO configuration. Expand the selected IO configuration to view all the IO sessions contained within the configuration. The right pane displays additional information about the selected IO configuration and IO session, including a read-only list of instrument attributes. 
 You can modify settings for each IO session using the following controls:
  - Logical Names 
 —The logical name of the IO session.
 Note 
 The logical names of IO sessions are not editable.
  - Session Description 
 —The description about the session.
 Note 
 The session description is not editable.
  - Session Variable 
 —The TestStand variable used to store the IO session.

Parent topic:

Apply Configuration Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/apply-configuration-step.html language=enus -->
## TOPIC 03378: Apply Configuration Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/apply-configuration-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/apply-configuration-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an Apply Configuration step to apply an IO configuration on an existing IO session. Configuring the Step Use the Apply Configuration edit tab in the TestStand Sequence Editor and the Configure Apply Configuration dialog box in a TestStand User Interface to specify which configuration to apply to

### Apply Configuration Step

Use an Apply Configuration step to apply an IO configuration on an existing IO session.

#### Configuring the Step

Use the
 [Apply Configuration](apply-configuration-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Apply Configuration](configure-apply-configuration-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify which configuration to apply to existing IO sessions.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Apply Configuration step type defines the following step properties:

- Step.IOConfigurations 
 —Specifies the IO sessions to which a configuration is applied.
- Step.StepDescription 
 —Specifies a brief description of the step.

Parent topic:

IO Configuration Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/array-bounds-dialog-box.html language=enus -->
## TOPIC 03379: Array Bounds Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/array-bounds-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/array-bounds-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Bounds tab of the Type Properties dialog box to launch the Array Bounds dialog box, in which you can modify the array bounds. You can also launch the Array Bounds dialog box by selecting Insert Local on the Locals tab to insert a local array variable. The Array Bounds dialog box contains t

### Array Bounds Dialog Box

Click the
 [Bounds](bounds-tab-type-properties-dialog-box.html)
 tab of the
 [Type Properties](type-properties-dialog-box.html)
 dialog box to launch the Array Bounds dialog box, in which you can modify the array bounds. You can also launch the Array Bounds dialog box by selecting
 Insert Local
 on the Locals tab to insert a local array variable.

The Array Bounds dialog box contains the following options:

- Dimensions String 
 —Shows a string that describes the array dimensions.
- Number of Dimensions 
 —Sets the number of dimensions in the array. The maximum number of dimensions is 16.
- Empty 
 —Indicates that the array has no elements when you start execution. When you enable this option, the Upper Bounds control for each dimension dims. Enabling this option is useful when you do not know the maximum array size the sequence requires during execution or when you want to save memory during the periods of execution when the sequence does not use the array.
- Lower Bounds 
 and
 Upper Bounds 
 —Sets the minimum and maximum index for each dimension. For example, you can define one as dimension zero-based and another dimension as one-based. The Upper Bounds setting must be greater than or equal to the Lower Bounds setting for the same dimension. You can calculate the number of elements in each dimension according to the following formula:
 Upper Bounds - Lower Bounds + 1

Note

#### See Also

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/array-parameters-c-c-dll-call-parameters.html language=enus -->
## TOPIC 03380: Array Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/array-parameters-c-c-dll-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/array-parameters-c-c-dll-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array Parameters When you select the Array of Numbers, Array of Strings, Array of Enumerations, Array of Objects, Array of Booleans, or Array of C Structs categories for a parameter, the adapter displays controls similar to what it shows for the Numeric, String, Enumeration, Object, Boolean, or C St

### Array Parameters - C/C++ DLL Call Parameters

#### Array Parameters

When you select the Array of Numbers, Array of Strings, Array of Enumerations, Array of Objects, Array of Booleans, or Array of C Structs categories for a parameter, the adapter displays controls similar to what it shows for the Numeric, String, Enumeration, Object, Boolean, or C Struct categories. You can specify an array that contains elements of the specified type. TestStand reformats and copies the contents of the array arguments into a temporary array containing elements that have the data type you select.

Use the
 Dimensions
 and
 Dim
 N
 Size
 controls to specify the number of dimensions and the number of elements in each dimension of the temporary array.

#### One-Dimensional Arrays

For one-dimensional arrays in which the array argument has fewer elements than the temporary array, the C/C++ DLL Adapter fills the remaining elements in the temporary array with zeros. When the array argument has more elements than the temporary array, TestStand fills the temporary array with the maximum number of elements that can fit.

For one-dimensional arrays in which you want the number of elements in the temporary array to always match the number of elements in the array argument, specify a negative value in the Dim
 N
 Size control. This specification is equivalent to the following expression:

GetNumElements (arrayArgument)

If you specify a zero value in the Dim
 N
 Size control, TestStand passes the address of the temporary array with no elements to the DLL function. When the DLL function returns, TestStand cannot fill the contents of the array argument with the contents of the temporary array because the array size is zero.

For one-dimensional arrays, when the array argument has fewer elements than the temporary array, TestStand stores only the number of elements from the temporary array that fit into the array argument. When the array argument has more elements than the temporary array, TestStand stores all the elements of the temporary array in the array argument and makes no changes to the remaining elements of the array argument.

#### Multi-Dimensional Arrays

For multi-dimensional arrays, the dimension sizes of the array argument must match the specified number of elements in the Dim
 N
 Size control.

If you select the Array of C Structs category, the C/C++ DLL Adapter displays the Element Pass control. When you select
 Embedded Element
 , TestStand creates an array of C structures and passes the array to the DLL function. When you select
 Pointer to Element
 , TestStand creates an array of C structures and passes the array of pointers to the DLL function.

Note

NULL

Nothing

0

#### See Also

[Accessing Arrays Using API from LabWindows/CVI Code Modules (Example)](/csh?context=ts_8152)

[Accessing Arrays Using API from MFC Code Modules (Example)](/csh?context=ts_8154)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/array-parameters-labview-nxg-vi-call-paramete.html language=enus -->
## TOPIC 03381: Array Parameters - LabVIEW NXG VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/array-parameters-labview-nxg-vi-call-paramete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/array-parameters-labview-nxg-vi-call-paramete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array Parameters You can specify an array that contains elements of any type. For numeric arrays, TestStand reformats the contents of the numeric array argument into a temporary array that contains elements that have the specific numeric type the VI expects. For an array of clusters, you must specif

### Array Parameters - LabVIEW NXG VI Call Parameters

#### Array Parameters

You can specify an array that contains elements of any type. For numeric arrays, TestStand reformats the contents of the numeric array argument into a temporary array that contains elements that have the specific numeric type the VI expects. For an array of clusters, you must specify an array of containers. The data type for the array of containers must have cluster passing enabled, and it must match the cluster structure the array of clusters expects.

For inputs, the number of dimensions in the TestStand array must match the number of dimensions in the LabVIEW NXG array. For outputs, the TestStand array is resized to match the LabVIEW NXG array.

For small, one-dimensional arrays, you can specify an argument for each element of the array. To add elements at the bottom of the array, click the
 <+>
 button at the root of the array. To insert a new element after an existing element, click the
 <+>
 button next to the existing element. Click the
 <–>
 button to delete the selected array element.

#### See Also

Accessing Arrays Using API from LabVIEW NXG Code Modules (Example)

[LabVIEW NXG Data Types in TestStand](labview-nxg-data-types-in-teststand.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

LabVIEW NXG Data Types in TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/array-parameters-labview-vi-call-parameters.html language=enus -->
## TOPIC 03382: Array Parameters - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/array-parameters-labview-vi-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/array-parameters-labview-vi-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array Parameters You can specify an array that contains elements of any type. For numeric arrays, TestStand reformats the contents of the numeric array argument into a temporary array that contains elements that have the specific numeric type the VI expects. For an array of clusters, you must specif

### Array Parameters - LabVIEW VI Call Parameters

#### Array Parameters

You can specify an array that contains elements of any type. For numeric arrays, TestStand reformats the contents of the numeric array argument into a temporary array that contains elements that have the specific numeric type the VI expects. For an array of clusters, you must specify an array of containers. The data type for the array of containers must have cluster passing enabled, and it must match the cluster structure the array of clusters expects.

For inputs, the number of dimensions in the TestStand array must match the number of dimensions in the LabVIEW array. For outputs, the TestStand array is resized to match the LabVIEW array.

For small, one-dimensional arrays, you can specify an argument for each element of the array. To add elements at the bottom of the array, click the
 <+>
 button at the root of the array. To insert a new element after an existing element, click the
 <+>
 button next to the existing element. Click the
 <–>
 button to delete the selected array element.

#### See Also

[Accessing Arrays Using API from LabVIEW Code Modules (Example)](/csh?context=ts_8153)

[LabVIEW Data Types in TestStand](/csh?context=ts_tsref_labview_data_types)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/array-parameters-labwindows-cvi-call-paramete.html language=enus -->
## TOPIC 03383: Array Parameters - LabWindows/CVI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/array-parameters-labwindows-cvi-call-paramete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/array-parameters-labwindows-cvi-call-paramete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array Parameters When you select the Array of Numbers, Array of Strings, Array of Enumerations, Array of Objects, or Array of C Structs categories for a parameter, the LabWindows/CVI Adapter displays controls similar to the controls for the Numeric, String, Enumeration, Object, or C Struct categorie

### Array Parameters - LabWindows/CVI Call Parameters

#### Array Parameters

When you select the Array of Numbers, Array of Strings, Array of Enumerations, Array of Objects, or Array of C Structs categories for a parameter, the LabWindows/CVI Adapter displays controls similar to the controls for the Numeric, String, Enumeration, Object, or C Struct categories. You can specify an array that contains elements of the specified type, and TestStand reformats the contents of the array argument into a temporary array that contains elements that have the data type you select.

Use the
 Dimensions
 and
 Dim
 N
 Size
 controls to specify the number of dimensions and the number of elements in each dimension of the temporary array.

#### One-Dimensional Arrays

If the array argument has fewer elements than the temporary array, the LabWindows/CVI Adapter fills the remaining elements in the temporary array with zeros. If the array argument has more elements than the temporary array, TestStand fills the temporary array with the maximum number of elements that can fit.

For one-dimensional arrays in which you want the number of elements in the temporary array to always match the number of elements in the array argument, specify a negative value in the Dim
 N
 Size control. This specification is equivalent to the following expression:

GetNumElements (arrayArgument)

If you specify a zero value in the Dim
 N
 Size control, TestStand passes the address of the temporary array with no elements to the DLL function. When the DLL function returns, TestStand cannot fill the contents of the array argument with the contents of the temporary array because the array size is zero.

If the array argument has fewer elements than the temporary array, TestStand only stores the number of elements from the temporary array that fit into the array argument. If the array argument has more elements than the temporary array, TestStand stores all the elements of the temporary array in the array argument and makes no changes to the remaining elements of the array argument.

#### Multi-Dimensional Arrays

For multi-dimensional arrays, the dimension sizes of the array argument must match the specified number of elements in the Dim
 N
 Size control.

If you select the Array of C Structs category, the LabWindows/CVI Adapter displays the Element Pass control. If you select
 Embedded Element
 , TestStand creates an array of C structures and passes the array to the DLL function. If you select
 Pointer to Element
 , TestStand creates an array of C structures and passes the array of pointers to the DLL function.

Note

NULL

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Accessing Arrays Using API from LabWindows/CVI Code Modules (Example)](/csh?context=ts_8152)

[Accessing Arrays Using API from MFC Code Modules (Example)](/csh?context=ts_8154)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/array-parameters-net-call-parameters.html language=enus -->
## TOPIC 03384: Array Parameters - .NET Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/array-parameters-net-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/array-parameters-net-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Array Parameters You can specify an array that contains elements of any type. For arrays, TestStand reformats the contents of the array into a temporary .NET array that contains elements that have the data type the assembly expects. For an array of structs, you can specify an array of object referen

### Array Parameters - .NET Call Parameters

#### Array Parameters

You can specify an array that contains elements of any type. For arrays, TestStand reformats the contents of the array into a temporary .NET array that contains elements that have the data type the assembly expects. For an array of structs, you can specify an array of object references, where each element is a reference to a .NET struct, or you can specify an array of TestStand data types where each element is an instance of a TestStand data type that corresponds to the .NET struct. In the latter case, the TestStand custom data type of the array must have struct passing enabled, and it must match the structure of the struct.

For inputs, the number of dimensions in the TestStand array must match the number of dimensions in the .NET array. For outputs, the TestStand array is resized, and new dimensions are specified to match the .NET array.

For one-dimensional arrays other than arrays of structs, you can specify an argument for each element of the array. To add elements to the bottom of the array, click the
 <+>
 sign at the root of the array. Click
 <+>
 on an array element to add a new element below the selected array element. Click
 <->
 to delete the selected array element.

For one-dimensional arrays, TestStand always converts the arrays to zero-based indexes no matter what the lower-bound value is in TestStand because the .NET Framework supports only zero-based indexes for one-dimensional arrays. Ensure that any one-dimensional array you use with the .NET Adapter is zero-based or will be zero-based after the call.

For multi-dimensional arrays, the .NET Adapter preserves the lower-bound values because multi-dimensional arrays can have lower-bound values other than zero in .NET.

#### Jagged Array Parameters

The .NET Adapter supports storing and passing jagged arrays, also known as arrays of arrays, as parameters using TestStand object reference variables. The .NET Adapter does not support converting jagged arrays to or from a TestStand equivalent array.

#### See Also

[Accessing Arrays Using API from .NET Code Modules (Example)](/csh?context=ts_8200)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/array-sweep-parameter-strategy.html language=enus -->
## TOPIC 03385: Array Sweep Parameter Strategy

- bundle_id: `teststand-api-reference`
- source_path: `tsref/array-sweep-parameter-strategy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/array-sweep-parameter-strategy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Array strategy with the Sweep Loop step to specify a parameter that sweeps over the values in an array. At the beginning of each iteration, the sweep parameter takes on the next value in the specified array. When the Array strategy is selected for a sweep parameter, the following additional

### Array Sweep Parameter Strategy

Use the Array strategy with the
 [Sweep Loop](sweep-loop-step.html)
 step to specify a parameter that sweeps over the values in an array. At the beginning of each iteration, the sweep parameter takes on the next value in the specified array.

When the Array strategy is selected for a sweep parameter, the following additional options are available:

- Array 
 —Contains the sweep parameter values. The elements of the array may be numbers of any representation, strings, Booleans, or enumerations. The elements of the array must be the same type as configured in the Type column.
- Count 
 —Tracks the number of elements specified in the array. In Dynamic Mode, this value is read-only. In Static mode, specify a value here to update the number of elements in the array.
- Values 
 —Allows you to specify the values of the array to be used in the loop in Static mode. In Dynamic mode, the elements of the array specified in the Array option are listed here, but the values are read-only.

Parent topic:

Sweep Parameter Strategies

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/attributes-dialog-box.html language=enus -->
## TOPIC 03386: Attributes Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/attributes-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/attributes-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Attributes dialog box to modify the attributes of any PropertyObject in the TestStand Sequence Editor or a TestStand User Interface . Attributes store data associated with a PropertyObject. Every PropertyObject has an Attributes container object under which you can create attribute variables

### Attributes Dialog Box

Use the Attributes dialog box to modify the attributes of any PropertyObject in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Attributes store data associated with a PropertyObject. Every PropertyObject has an Attributes container object under which you can create attribute variables. Use container subproperties as attribute namespaces. For some PropertyObjects, the sequence editor might display an
 Edit Attributes
 button next to the name of the PropertyObject to indicate the PropertyObject has attributes.

You can launch the Attributes dialog box in different ways depending on the kind of PropertyObject you are modifying. Typically, you access the Attributes dialog box by clicking an
 Edit Attributes
 button or selecting an
 Edit Attributes
 context menu item, which is often located in an Advanced submenu or in a context menu you launch by clicking an
 Advanced
 button.

Create attributes using the context menu in the attributes variables control. The attributes variables control contains the following columns:

- Name 
 —The name of the attribute.
- Value 
 —The value of the attribute.
- Type 
 —The type of the attribute. Use container subproperties to serve as attributes namespaces. To avoid name conflicts, National Instruments recommends that you create a uniquely named container or hierarchy of containers under which you store attribute variables, such as
 CompanyName.AttributeCategory.Attribute 
 .
- Comment 
 —A comment for the attribute.

When editing the attributes of a type definition, you can edit both Attributes and TypeAttributes. For a type definition, Attributes determine the default values of the Attributes of type instances. TypeAttributes are attributes for the type definition.

You can sort the contents of the Attributes dialog box. Click any column header to sort the view by the values of that column in increasing order. Click the column header again to sort the values in decreasing order. Click the column header a third time to restore the values to the unsorted order.

#### See Also

[Advanced Tab - Sequence File Properties dialog box](advanced-tab-sequence-file-properties-dialog.html)

[General Panel - Step Settings Pane](general-panel-step-settings-pane.html)

[General Tab - Sequence Properties dialog box](general-tab-sequence-properties-dialog-box.html)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Parameters Table Context Menu for Specify Module Dialog Boxes](for-specify-module-dialog-boxes-parameters-ta.html)

[Sequence File Window - Variables Pane](variables-pane-sequence-file-window4.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/auto-refresh-dialog-box.html language=enus -->
## TOPIC 03387: Auto-Refresh Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/auto-refresh-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/auto-refresh-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: When Auto-Refresh is disabled, clicking the Auto-Refresh button launches the Auto-Refresh dialog box, in which you can set the Auto-Refresh options. If Auto-Refresh is enabled when you close the dialog box, the Auto-Refresh settings take effect. The Auto-Refresh dialog box contains the following opt

### Auto-Refresh Dialog Box

When Auto-Refresh is disabled, clicking the
 Auto-Refresh
 button launches the Auto-Refresh dialog box, in which you can set the Auto-Refresh options. If Auto-Refresh is enabled when you close the dialog box, the Auto-Refresh settings take effect.

The Auto-Refresh dialog box contains the following options:

- Enable Auto-Refresh 
 —Enables the Auto-Refresh setting.
- Time Interval 
 —Specifies the Auto-Refresh time interval in seconds. When Auto-Refresh is enabled, the configured SQL query executes each time this interval elapses.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/auto-schedule-settings-edit-tab.html language=enus -->
## TOPIC 03388: Auto Schedule Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/auto-schedule-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/auto-schedule-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert an Auto Schedule step and select Edit Auto Schedule Settings or Step Settings from the context menu to display the Auto Schedule Settings edit tab in the TestStand Sequence Editor . The following operations are available when you use the Auto Schedule step type: Timeout Enabled, Timeout Expre

### Auto Schedule Settings Edit Tab

Insert an Auto Schedule step and select
 Edit Auto Schedule Settings
 or
 Step Settings
 from the context menu to display the Auto Schedule Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

The following operations are available when you use the Auto Schedule step type:

- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —The timeout behavior TestStand uses when Use Auto Scheduled Resource blocks within the Auto Schedule block can acquire the required resource locks. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .
- Display Execution Scheduling Information in Step Description 
 —When you enable this option, the step description in the Execution window of the sequence editor or a
 TestStand User Interface 
 contains information about the scheduling of the execution of the various Use Auto Scheduled Resource blocks within the Auto Schedule block.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Auto Schedule Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/auto-schedule-step.html language=enus -->
## TOPIC 03389: Auto Schedule Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/auto-schedule-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/auto-schedule-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use an Auto Schedule step to define a block that contains any number of Use Auto Scheduled Resource step sub-blocks. You typically use Auto Schedule steps in a sequence you execute using the Parallel or Batch process models. The Auto Schedule step executes each sub-block once. The order in which the

### Auto Schedule Step

Use an Auto Schedule step to define a block that contains any number of
 [Use Auto Scheduled Resource](use-auto-scheduled-resource-step.html)
 step sub-blocks. You typically use Auto Schedule steps in a sequence you execute using the Parallel or Batch process models.

The Auto Schedule step executes each sub-block once. The order in which the Auto Schedule step executes the sub-blocks can vary according to the availability of the resources the sub-blocks require. The Auto Schedule step can increase CPU and resource use by directing a thread that otherwise waits for a resource another thread locks to perform other actions using available resources instead.

#### Configuring the Step

Use the
 [Auto Schedule Settings](auto-schedule-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Auto Schedule Step](configure-auto-schedule-step-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Auto Schedule step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Auto Schedule step type defines the following step properties:

- Step.Result.TimeoutOccurred 
 —Exists only when you configure the step for the Acquire operation. TestStand sets the value to
 True 
 when any Auto Scheduled Resource blocks within the Auto Schedule block time out.
 Note 
 If you configure the step to use the Acquire operation programmatically, you must also create the
 Step.Result.TimeoutOccurred
 property using the
 newProperty(
 ) method for the step to execute successfully.
- Step.TimeoutEnabled 
 —The
 Timeout 
 Enabled setting for the Auto Schedule operation.
- Step.TimeoutExpression 
 —The Timeout expression, in seconds, for the Auto Schedule operation.
- Step.TimeoutIsRuntimeError 
 —Setting value to
 True 
 causes a step run-time error when a timeout occurs.
- Step.DisplayRuntimeDescription 
 —Setting to
 True 
 displays execution scheduling information in the step description.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/auto-scheduled-resource-settings-edit-tab.html language=enus -->
## TOPIC 03390: Auto Scheduled Resource Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/auto-scheduled-resource-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/auto-scheduled-resource-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Use Auto Scheduled Resource step and select Edit Auto Scheduled Resource Settings or Step Settings from the context menu to display the Auto Scheduled Resource Settings edit tab in the TestStand Sequence Editor . The following operations are available when you use the Use Auto Scheduled Res

### Auto Scheduled Resource Settings Edit Tab

Insert a Use Auto Scheduled Resource step and select
 Edit Auto Scheduled Resource Settings
 or
 Step Settings
 from the context menu to display the Auto Scheduled Resource Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

The following operations are available when you use the Use Auto Scheduled Resource step type:

- Resource Lock Alternatives 
 —A list of lock names or reference
 expressions 
 . The list must consist of at least one lock name or reference expression. The step attempts to acquire the first lock in the list. If the lock is not available, the step attempts to acquire the next lock, and so forth, until it successfully acquires a lock. If the step cannot acquire a lock, the step proceeds to the next Use Auto Scheduled Resource step in the same Auto Schedule block.
 Specify alternative locks if the steps in the Use Auto Scheduled Resource sub-block can execute with more than one set of resources. For example, you can specify alternative locks "
 DAQCard1
 " and "
 DAQCard2
 " if the steps can execute with either card, depending on which card is available. Specify an array of lock names for a single item to lock multiple resources. For example, you can use the expression
 {"DAQCard1", "DAQCard2"}
 if the steps require both devices to execute. This operation is atomic, and neither resource is acquired unless both resources are available.
  - Add 
 —Adds a new empty lock name or reference expression to the end of the list.
  - Delete 
 —Deletes the currently selected item.
  - Move Up 
 —Moves the currently selected item up one place in the list.
  - Move Down 
 —Moves the currently selected item down one place in the list.
- Acquired Lock (optional output string) 
 —An expression that specifies a string variable or property into which to store the lock alternative the step acquires during execution. To identify the alternative lock it selects, the step stores the unevaluated alternative lock expression, exactly as the expression appears in the list.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Use Auto Scheduled Resource Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/auto-setup-operation-edit-ivi-scope-step-dial.html language=enus -->
## TOPIC 03391: Auto Setup Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/auto-setup-operation-edit-ivi-scope-step-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/auto-setup-operation-edit-ivi-scope-step-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Auto Setup Operation The Auto Setup operation performs an automatic setup on the instrument, which causes the instrument to put itself into a known state. Since the Auto Setup operation is different for each instrument, using it will break interchangeability. Auto Setup is only recommended for cases

### Auto Setup Operation - Edit IVI Scope Step Dialog Box

#### Auto Setup Operation

The Auto Setup operation performs an automatic setup on the instrument, which causes the instrument to put itself into a known state. Since the Auto Setup operation is different for each instrument, using it will break interchangeability. Auto Setup is only recommended for cases in which further calls to the instrument are not planned.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/backup-prompt-dialog-box.html language=enus -->
## TOPIC 03392: Backup Prompt Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/backup-prompt-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/backup-prompt-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: You must attempt to save a sequence file over an existing sequence file that a different version of TestStand saved to launch the Backup Prompt dialog box. You must also set the TestStand Sequence Editor option, Backup Sequence Files when Resaving in Older or Newer Format, in the Sequence Editor Opt

### Backup Prompt Dialog Box

You must attempt to save a sequence file over an existing sequence file that a different version of TestStand saved to launch the Backup Prompt dialog box. You must also set the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 option, Backup Sequence Files when Resaving in Older or Newer Format, in the
 [Sequence Editor Options](sequence-editor-options-dialog-box.html)
 dialog box to Prompt.

The Backup Prompt dialog box contains the following options:

- File Name 
 —The sequence file path.
- Backup sequence files when saving in older or newer format 
 —Specifies whether the sequence editor launches this dialog box in the future or uses a specific setting by default. The following options are available in the ring control:
  - Yes 
 —Always backup sequence files.
  - No 
 —Do not backup sequence files.
  - Prompt 
 —Prompt to backup sequence files.
- Yes 
 —Renames the existing sequence file on disk by appending
 "_old" 
 to the filename and saves the currently loaded file.
- No 
 —Saves the currently loaded file over the existing sequence file.
- Cancel 
 —Does not save the currently loaded sequence file.

#### See Also

[Sequence Editor Options dialog box](sequence-editor-options-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/basic-step-time-report-configuration-dialog-b.html language=enus -->
## TOPIC 03393: Basic Step Time Report Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/basic-step-time-report-configuration-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/basic-step-time-report-configuration-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Result Processing dialog box, click the icon in the Options column of the Basic Step Time Report plug-in to launch the Basic Step Time Report Configuration dialog box, in which you specify the directory in which to store the report and specify whether to launch the report in Excel. The Basic

### Basic Step Time Report Configuration Dialog Box

In the
 [Result Processing](result-processing-dialog-box.html)
 dialog box, click the icon in the Options column of the Basic Step Time Report plug-in to launch the Basic Step Time Report Configuration dialog box, in which you specify the directory in which to store the report and specify whether to launch the report in Excel.

The Basic Step Time Report Configuration dialog box includes the following options:

- Report Directory 
 —Specify the path where you want to create the report.
- Report Filename 
 —Displays the format of the report filename, which you cannot change.
- Launch Basic Step Time Report in Microsoft Excel 
 —Enable this option to display the report in Microsoft Office Excel 2007 SP2 or later.

#### See Also

[Basic Step Time Report Example](/csh?context=ts_8194)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/batch-results-dialog-box.html language=enus -->
## TOPIC 03394: Batch Results Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/batch-results-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/batch-results-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The default Batch model launches the Batch Results dialog box, in which you can view the status and reports for each test socket and UUT when a batch test completes. The Batch Results dialog box contains the following options: Batch Serial Number —The serial number that identifies the batch of UUTs.

### Batch Results Dialog Box

The default Batch model launches the Batch Results dialog box, in which you can view the status and reports for each test socket and UUT when a batch test completes.

The Batch Results dialog box contains the following options:

- Batch Serial Number 
 —The serial number that identifies the batch of UUTs.
- View Batch Report 
 —Displays the report for the batch. You can select whether to view the report for the current batch only or to view the entire file to which you configure batch reports to append.
- Test Socket 
 —The test socket index.
- UUT Serial Number 
 —A serial number that identifies the UUT in the test socket.
- View Report 
 —Displays the report for the UUT in the test socket. You can select whether to view the report for the current UUT only or to view the entire file to which you configure UUT reports for the test socket to append.
- Status Message 
 —The final status of the UUT.
- Next Batch 
 —Returns to the
 UUT Information 
 dialog box for the Batch model.

#### See Also

[UUT Information Dialog Box (Batch Model)](uut-information-dialog-box-batch-model.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/batch-settings-edit-tab.html language=enus -->
## TOPIC 03395: Batch Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/batch-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/batch-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Batch Specification step and select Edit Batch Settings or Step Settings from the context menu to display the Batch Settings edit tab in the TestStand Sequence Editor . The following operations are available when you use the Batch Specification step type: Create —Creates a reference to a ne

### Batch Settings Edit Tab

Insert a Batch Specification step and select
 Edit Batch Settings
 or
 Step Settings
 from the context menu to display the Batch Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

The following operations are available when you use the Batch Specification step type:

- Create 
 —Creates a reference to a new or existing Batch object.
- Add Thread 
 —Adds a TestStand thread to the group of batch threads.
- Remove Thread 
 —Removes a TestStand thread from a group of batch threads.
- Get Status 
 —Obtains information about the current state of the batch.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Batch Specification Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/batch-specification-step-configuration-dialog.html language=enus -->
## TOPIC 03396: Batch Specification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/batch-specification-step-configuration-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/batch-specification-step-configuration-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Batch Specification in the context menu for the step to launch the Batch Specification Step Configuration dialog box from a TestStand User Interface . You can also click Configure Batch Specification on the General tab of the Step Properties dialog box. In the Batch Specification St

### Batch Specification Step Configuration Dialog Box

Select
 Configure Batch Specification
 in the context menu for the step to launch the Batch Specification Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Batch Specification
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Batch Specification Step Configuration dialog box, select an operation for the step to perform.

The following operations are available when you use the Batch Specification step type:

- Create 
 —Creates a reference to a new or existing Batch object.
- Add Thread 
 —Adds a TestStand thread to the group of batch threads.
- Remove Thread 
 —Removes a TestStand thread from a group of batch threads.
- Get Status 
 —Obtains information about the current state of the batch.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Batch Specification Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/batch-specification-step.html language=enus -->
## TOPIC 03397: Batch Specification Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/batch-specification-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/batch-specification-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Batch Specification step to define a group of threads in which each thread in the group runs an instance of the client sequence file. When you define a group, you can perform Batch Synchronization operations on the threads in the group. The Batch process model uses Batch Specification steps to

### Batch Specification Step

Use a Batch Specification step to define a group of threads in which each thread in the group runs an instance of the client sequence file. When you define a group, you can perform
 [Batch Synchronization](batch-synchronization-step.html)
 operations on the threads in the group. The
 [Batch process model](/csh?context=ts_tsfundamentals_batch)
 uses Batch Specification steps to create a batch that contains a thread for each test socket.

When you test each UUT in a separate thread, use the Batch Specification step to include the UUT threads in one batch. Use the Batch Synchronization step to control the interaction of the UUT threads as the threads execute the test steps.

#### Configuring the Step

Use the
 [Batch Settings](batch-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Batch Specification Step Configuration](batch-specification-step-configuration-dialog.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Batch Specification step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Batch Specification step type defines the following step properties:

- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Create,
 1 
 = Add Thread,
 2 
 = Remove Thread, and
 3 
 = Get Status.
- Step.NameOrRefExpr 
 —Contains the
 Name 
 expression for the
 Create 
 operation and the Name or Reference expression for all other Batch operations.
- Step.Lifetime 
 —A value that specifies the
 lifetime 
 setting to use for the Create operation. The valid values are
 0 
 = Same as Sequence,
 1 
 = Same as Thread,
 2 
 = Use Object Reference, and
 3 
 = Same as Execution.
- Step.LifetimeRefExpr 
 —The object reference expression for the Batch Reference Lifetime when you set the lifetime to Use Object Reference.
- Step.AlreadyExistsExpr 
 —Contains the Already Exists expression for the Create operation or the Batch Exists expression for the
 Get Status 
 operation.
- Step.ThreadRefExpr 
 —The Object Reference to Thread expression for the Add Thread and Remove Thread operations.
- Step.OrderNumExpr 
 —The Order Number expression for the Add Thread operation.
- Step.NumThreadsWaitingExpr 
 —The Number of Threads Waiting at Synchronized Sections expression for the Get Status operation.
- Step.NumThreadsInBatchExpr 
 —The Number of Threads in Batch expression for the Get Status operation.
- Step.DefaultBatchSyncExpr 
 —The Default Batch Synchronization expression for the Create operation.
- Step.DefaultBatchSyncOutExpr 
 —The Default Batch Synchronization expression for the Get Status operation.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/batch-synchronization-settings-edit-tab.html language=enus -->
## TOPIC 03398: Batch Synchronization Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/batch-synchronization-settings-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/batch-synchronization-settings-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the Batch Synchronization Settings edit tab in the TestStand Sequence Editor , insert a Batch Synchronization step and select Edit Batch Synchronization Settings or Step Settings from the context menu. The following operations are available when you use the Batch Synchronization step type

### Batch Synchronization Settings Edit Tab

To display the Batch Synchronization Settings edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a Batch Synchronization step and select
 Edit Batch Synchronization Settings
 or
 Step Settings
 from the context menu. The following operations are available when you use the Batch Synchronization step type:

- Enter Synchronized Section 
 —Marks the beginning of a synchronized section and defines the type of synchronization for that section.
- Exit Synchronized Section 
 —Marks the end of a synchronized section.

#### Requirements for Using Enter and Exit Synchronized Section Operations

TestStand generates a run-time error if the Enter Synchronized Section and Exit Synchronized Section operations do not adhere to the following requirements:

- Each Exit Synchronized Section operation must match the most nested Enter Synchronized Section operation.
- A thread cannot reenter a section it is already in.
- You must exit a section in the same sequence you enter it.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Batch Synchronization Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/batch-synchronization-step-configuration-dial.html language=enus -->
## TOPIC 03399: Batch Synchronization Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/batch-synchronization-step-configuration-dial.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/batch-synchronization-step-configuration-dial.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Batch Synchronization in the context menu for the step to launch the Batch Synchronization Step Configuration dialog box from a TestStand User Interface . You can also click Configure Batch Synchronization on the General tab of the Step Properties dialog box. In the Batch Synchroniz

### Batch Synchronization Step Configuration Dialog Box

Select
 Configure Batch Synchronization
 in the context menu for the step to launch the Batch Synchronization Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Batch Synchronization
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box. In the Batch Synchronization Step Configuration dialog box, select an operation for the step to perform.

The following operations are available when you use the Batch Synchronization step type:

- Enter Synchronized Section 
 —Marks the beginning of a synchronized section and defines the type of synchronization for the section.
- Exit Synchronized Section 
 —Marks the end of a synchronized section.

#### Requirements for Using Enter and Exit Synchronized Section Operations

TestStand generates a run-time error if the Enter Synchronized Section and Exit Synchronized Section operations do not adhere to the following requirements:

- Each Exit Synchronized Section operation must match the most nested Enter Synchronized Section operation.
- A thread cannot reenter a section it is already in.
- You must exit a section in the same sequence you enter it.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Batch Synchronization Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/batch-synchronization-step.html language=enus -->
## TOPIC 03400: Batch Synchronization Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/batch-synchronization-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/batch-synchronization-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Batch Synchronization step to define a section of a sequence in which to synchronize multiple threads that belong to one batch. Place Batch Synchronization steps around test steps to create a synchronized section. Use the Synchronization panel on the Properties tab of the Step Settings pane to

### Batch Synchronization Step

Use a Batch Synchronization step to define a
 [section of a sequence](/csh?context=ts_tsref_sync_sections)
 in which to synchronize multiple threads that belong to one batch.

Place Batch Synchronization steps around test steps to create a synchronized section. Use the
 [Synchronization](synchronization-panel-step-settings-pane.html)
 panel on the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane to synchronize a single step for the multiple threads that belong to a batch. Typically, you use Batch Synchronization steps in a sequence you execute using the Batch process model.

#### Configuring the Step

Use the
 [Batch Synchronization Settings](batch-synchronization-settings-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Batch Synchronization Step Configuration](batch-synchronization-step-configuration-dial.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Batch Synchronization step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Batch Synchronization step type defines the following step properties:

- Step.Result.TimeoutOccurred 
 —Exists only when you configure the step for the
 Enter 
 or
 Exit 
 operation. TestStand sets the value to
 True 
 when the Enter or Exit operation times out.
 Note 
 If you configure the step to use the Enter or Exit operation programmatically using the
 Step.Operation
 property, you must also create the
 Step.Result.TimeoutOccurred
 property using the
 newProperty(
 ) method for the step to execute successfully.
- Step.TimeoutEnabled 
 —The
 Timeout 
 Enabled setting for the Enter or Exit operation.
- Step.TimeoutExpr 
 —The Timeout expression, in seconds, for the Enter or Exit operation.
- Step.ErrorOnTimeout 
 —The Timeout Causes Run-Time Error setting for the Enter or Exit operation.
- Step.Operation 
 —A value that specifies the operation for the step to perform. The valid values are
 0 
 = Enter Synchronized Section and
 1 
 = Exit Synchronized Section.
- Step.SectionNameExpr 
 —The expression that specifies the section name for the Enter or Exit operation.
- Step.SectionType 
 —A value that specifies the type of section the Enter operation defines. The valid values are
 1 
 = Serial,
 2 
 = Parallel, and
 3 
 = One Thread Only.

#### See Also

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Synchronization Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/binary-data-viewer.html language=enus -->
## TOPIC 03401: Binary Data Viewer

- bundle_id: `teststand-api-reference`
- source_path: `tsref/binary-data-viewer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/binary-data-viewer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the Database Viewer, click a table in Database Object View that contains binary data and select View Data from the context menu. The Database Viewer uses the words Binary Data to indicate that a cell contains binary data. Double click the cell to launch the Binary Data Viewer. By default, the Bin

### Binary Data Viewer

Database Object View

Binary Data

Note

- By default, the Binary Data Viewer retains previously-set options. The options reset when you view binary data that contains a different number of bytes compared to the data from the previous view or when you close the Database Viewer application.
- The Binary Data Viewer uses the data type you specify to parse the binary data.

The Binary Data Viewer dialog box contains the following tabs:

- Data Tab 
 —Displays the parsed elements in list form. This tab modifies the display based on the display options you set.
- Graph Tab 
 —Plots the parsed elements on a graph. This tab modifies the graph based on the display options you set.
- Memory Tab 
 —Displays the parsed elements in hexadecimal and character data form. This tab modifies the display based on the data type you set.

Use the following display options in the Binary Data Viewer tabs:

- Data Type 
 —Specifies one of the following data types with which to parse the bytes data.
 
 Note 
 If an element corresponds to a valid character, the Binary Data Viewer displays the character with the element for 8-bit and 16-bit integers.
  - 8-bit integer
  - 16-bit integer
  - 32-bit integer
  - 64-bit integer
  - Floating-point integer
  - Double-precision, floating-point integer
- Array Dimensions 
 —Specifies the following array dimension options to modify the display of the parsed elements.
  - 1 
 —Displays one column for indexes and another column for parsed elements. The graph tab uses the indexes as x values and the corresponding parsed elements as y values to plot the data.
  - 2 
 —You can specify the number of rows/columns to create and which row/column index contains the X axis values for the graph. The graph tab uses the values in the row/column index as x values and the corresponding values in other columns as y values to plot the data.
    - Data Arranged 
 —Includes the following options to change the arrangement of the parsed elements.
      - Row-wise 
 —Reads and displays the parsed elements according to row.
      - Number of Rows 
 —Specifies the number of rows to create.
      - Column-wise 
 —Reads and displays the parsed elements according to column.
      - Number of Columns 
 —Specifies the number of columns to create.
    - Data Contains 
 —Specifies whether the data contains only y-values or x- and y-values.
    - X-Values in Row 
 —Specifies the row that contains x-values if the data contains x- and y-values when you select
 Row-wise 
 in the Data Arranged option.
    - X-Values in Column 
 —Specifies the column that contains x-values if the data contains x- and y-values when you select
 Column-wise 
 in the Data Arranged option.
 Note 
 The Data tab highlights x values in the row or column you specify.
  - 3 or more 
 —Displays the Specify Array Dimension field in which you can specify a multi-dimensional string.
    - Specify Array Dimension 
 —Specifies the dimension string for the array when you select
 3 or more 
 in the Array Dimensions option. Use the
 [lower,higher][lower,higher][lower,higher] 
 syntax for the string. For example, specify a four-dimensional array as:
 [1,4][1,5][0,9][1,10] 
 . Click the
 View Data 
 button or press the <Enter> key after you enter the dimension string to view the data on the Data tab or to view the graph on the Graph tab.
 Note 
 The graph tab displays the data as a one-dimensional array.
    - View Data 
 —Displays the multi-dimensional array using the dimension string you specified in the Specify Array Dimension option.
- View 
 —Uses one of the following options to specify the values to view, where N is a number you specify:
  - All Values
  - First N Values
  - Every Nth Value

#### Binary Data Viewer Menu

The Binary Data Viewer menu includes an options menu and a print menu.

The Options menu contains the following options:

- Print Option: Page Header 
 —Specifies the document header to display on each printed page.
- Graph Option: Label Datapoints in Graph 
 —Includes labels for data points on the graph. This option is disabled by default.

The print menu contains the following options:

- Print 
 —Launches the standard Print dialog box.
- Quick Print 
 —Prints the data or graph the selected tab displays using the default printer.
- Print Preview 
 —Launches Print Preview dialog box.

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/block-structure-dialog-box.html language=enus -->
## TOPIC 03402: Block Structure Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/block-structure-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/block-structure-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To launch the Block Structure dialog box, launch the Step Type Properties dialog box, click the Advanced button on the General tab, and then select Block Structure . The Block Structure dialog box contains the following options: Step Affects Sequence Block Structure —Set this property to indicate th

### Block Structure Dialog Box

To launch the Block Structure dialog box, launch the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box, click the
 Advanced
 button on the
 [General](general-tab-step-type-properties-dialog-box.html)
 tab, and then select
 Block Structure
 .

The Block Structure dialog box contains the following options:

- Step Affects Sequence Block Structure 
 —Set this property to indicate that the instances of this step type affect the block structure in a sequence. Typically, applications visually indicate the steps that apply to a block structure, such as displaying the step name in bold font.
- Block Start Step Types 
 —A comma-delimited list of step type names. A non-empty list indicates a step of this type must end a block. A step of this type can end a block a step of any type in the list starts. For example, the Block Start step types for the NI_Flow_Else step type are NI_Flow_If, and NI_Flow_ElseIf.
- Block End Step Types 
 —A comma-delimited list of step type names. A non-empty list indicates a step of this type starts a block. A step of a type in the list must end the block. For example, the Block End step types for an NI_Flow_If step type are NI_Flow_Else, NI_Flow_ElseIf, and NI_Flow_End.
- Can Surround a Selection of Steps 
 —Specifies that the step type appears in the Surround Selection With context menu so that you can surround a block of contiguous steps with a set of corresponding begin and end steps of this type. Use an
 OnNewStep substep 
 for the custom step to check the Boolean value of the
 SequenceContext.RunState.ShouldEncapsulate 
 property to determine where to insert a corresponding end step for the custom step.

#### See Also

[Adding Step Types to Surround Selection With Context Menu](/csh?context=ts_tsfundamentals_addtoencapsulatewithcm)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/boolean-parameters-c-c-dll-call-parameters.html language=enus -->
## TOPIC 03403: Boolean Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/boolean-parameters-c-c-dll-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/boolean-parameters-c-c-dll-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Boolean Parameters The Boolean category is similar to the Numeric category, except the C/C++ DLL Adapter does not allow you to choose a Numeric data type. Instead, the adapter automatically chooses the C++ bool data type for you. When you pass a numeric value to a Boolean parameter, TestStand passes

### Boolean Parameters - C/C++ DLL Call Parameters

#### Boolean Parameters

The Boolean category is similar to the Numeric category, except the C/C++ DLL Adapter does not allow you to choose a Numeric data type. Instead, the adapter automatically chooses the C++ bool data type for you. When you pass a numeric value to a Boolean parameter, TestStand passes
 False
 when the number is zero and passes
 True
 otherwise.

Note

NULL

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/bounds-tab-properties-dialog-box.html language=enus -->
## TOPIC 03404: Bounds Tab - Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/bounds-tab-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/bounds-tab-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Bounds Tab The Bounds tab is visible only for array properties, and contains the following options: Dimensions String —A string that describes the array dimensions. Number of Dimensions —The number of dimensions in the array. The maximum number of dimensions is 16. Empty —Specifies that the array ha

### Bounds Tab - Properties Dialog Box

#### Bounds Tab

The Bounds tab is visible only for array properties, and contains the following options:

- Dimensions String 
 —A string that describes the array dimensions.
- Number of Dimensions 
 —The number of dimensions in the array. The maximum number of dimensions is 16.
- Empty 
 —Specifies that the array has no elements when you start execution. When you enable this option, the Upper Bounds control for each dimension dims. Enable this option when you do not know the maximum array size the sequence requires during execution or when you want to save memory during the periods of execution when the sequence does not use the array.
- Lower Bounds 
 and
 Upper Bounds 
 —Sets the minimum and maximum index for each dimension. For example, you can define one dimension as zero-based and another dimension as one-based. The Upper Bounds setting must be equal to or greater than the Lower Bounds setting for the same dimension. You can calculate the number of elements in each dimension according to the following formula:
 Upper Bounds - Lower Bounds + 1 
 Note 
 The number of controls that appear next to the Lower Bounds and Upper Bounds options varies according to the setting of the Number of Dimensions control.

Parent topic:

Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/bounds-tab-type-properties-dialog-box.html language=enus -->
## TOPIC 03405: Bounds Tab - Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/bounds-tab-type-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/bounds-tab-type-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Bounds Tab The Bounds tab is visible for array data types only. If you have already created variables, parameters, or properties with the data type, enable the Apply Bounds to All Loaded Instances of the Type option to change the array bounds in all instances of the array data type for files current

### Bounds Tab - Type Properties Dialog Box

#### Bounds Tab

The Bounds tab is visible for array data types only. If you have already created variables, parameters, or properties with the data type, enable the
 Apply Bounds to All Loaded Instances of the Type
 option to change the array bounds in all instances of the array data type for files currently in memory. Instances of the type in files not currently loaded are not updated.

#### See Also

[Array Bounds dialog box](array-bounds-dialog-box.html)

Parent topic:

Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/break-step.html language=enus -->
## TOPIC 03406: Break Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/break-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/break-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Break step to cause a For , For Each , While , or Do While loop block or a Case block to exit before completing. Configuring the Step Use the Properties tab of the Step Settings pane in the TestStand Sequence Editor or the Step Properties dialog box in a TestStand User Interface to configure t

### Break Step

Use a Break step to cause a
 [For](for-step.html)
 ,
 [For Each](for-each-step.html)
 ,
 [While](while-step.html)
 , or
 [Do While](do-while-step.html)
 loop block or a
 [Case](case-step.html)
 block to exit before completing.

#### Configuring the Step

Use the
 [Properties](properties-tab-step-settings-pane.html)
 tab of the
 [Step Settings](step-settings-pane.html)
 pane in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or the
 [Step Properties](step-properties-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Break step.

#### Step Properties

The Break step type does not define any additional step properties other than the
 [custom properties common to all steps](/csh?context=ts_tsfundamentals_custom_result_props)
 .

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/breakpoint-settings-dialog-box.html language=enus -->
## TOPIC 03407: Breakpoint Settings Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/breakpoint-settings-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/breakpoint-settings-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Breakpoint»Breakpoint Settings from the context menu for a step in the list view of a Sequence File or Execution window to launch the Breakpoint Settings dialog box. The Breakpoint Settings dialog box contains the following options: Breakpoint Set —Enable this option if the breakpoint is set.

### Breakpoint Settings Dialog Box

Select
 Breakpoint»Breakpoint Settings
 from the context menu for a step in the list view of a Sequence File or Execution window to launch the Breakpoint Settings dialog box.

The Breakpoint Settings dialog box contains the following options:

- Breakpoint Set 
 —Enable this option if the breakpoint is set. Disable this option to delete the breakpoint.
- Breakpoint Enabled 
 —Enable this option when the breakpoint is enabled. TestStand ignores disabled breakpoints during execution.
- Pass Count 
 —Specify the number of iterations,
 n 
 , in which the execution skips the breakpoint before suspending execution. Execution suspends at the
 n+1 
 iteration, resumes, runs another
 n 
 times before suspending again, and repeats this pattern until the execution ends.
 Note 
 Pass, in this context, does not refer to the success or failure of a step, but rather the behavior of skipping, or passing, over a breakpoint.
- Condition 
 —Specify the expression that must evaluate to
 True 
 before suspending the execution. An empty value defaults to
 True 
 . If you specify a non-zero pass count value and a conditional expression, the pass count decrements only when the expression evaluates to
 True 
 .

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/breakpoints-tab-edit-breakpoints-watch-expres.html language=enus -->
## TOPIC 03408: Breakpoints Tab - Edit Breakpoints/Watch Expressions Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/breakpoints-tab-edit-breakpoints-watch-expres.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/breakpoints-tab-edit-breakpoints-watch-expres.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breakpoints Tab The list control contains the breakpoints in previously opened sequence files TestStand saved while the current workspace was loaded and breakpoints that apply only to currently running executions. The Breakpoint column displays the sequence files that contain breakpoints. You can ex

### Breakpoints Tab - Edit Breakpoints/Watch Expressions Dialog Box

#### Breakpoints Tab

The list control contains the breakpoints in previously opened sequence files TestStand saved while the current workspace was loaded and breakpoints that apply only to currently running executions. The Breakpoint column displays the sequence files that contain breakpoints. You can expand the sequence file entry to view sequences in the file. You can also expand the sequence entry to view the steps that specify breakpoints. Use the Enabled column to specify to enable or disable a breakpoint.

The Breakpoints tab contains the following options:

- Goto 
 —Opens the sequence file and displays the selected file, sequence, or step.
- Edit 
 —Launches the
 Breakpoint Settings 
 dialog box, in which you can specify the pass count and conditional expression for the selected step.
- Expand 
 —Expands the Breakpoints list control for the currently selected file to show all breakpoints associated with the file.
- Expand All 
 —Expands the Breakpoints list control for all files to show all breakpoints.
- Collapse All 
 —Collapses the Breakpoints list control for all files, so the list shows the files that contain breakpoints.
- Delete 
 —Deletes the breakpoint for the selected step, or the breakpoints in the selected sequence or sequence file.
- Delete All 
 —Deletes all breakpoints in the list.

#### See Also

[Breakpoint Settings dialog box](breakpoint-settings-dialog-box.html)

Parent topic:

Edit Breakpoints/Watch Expressions Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/browse-sequence-context-and-variables-dialog.html language=enus -->
## TOPIC 03409: Browse Sequence Context and Variables Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/browse-sequence-context-and-variables-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/browse-sequence-context-and-variables-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Browse Sequence Context and Variables dialog box to view the structure of a property object. Call the Engine.DisplayBrowsePropertyObjectDialog method to launch the Browse Sequence Context and Variables dialog box. The arguments you pass to the method typically represent an active window and

### Browse Sequence Context and Variables Dialog Box

Use the Browse Sequence Context and Variables dialog box to view the structure of a property object. Call the
 [Engine.DisplayBrowsePropertyObjectDialog](../tsapiref/engine-displaybrowsepropertyobjectdialog.html)
 method to launch the Browse Sequence Context and Variables dialog box. The arguments you pass to the method typically represent an active window and the item currently selected in the window.

The dialog box shows variables and properties you can access and the names that appear depending on the object the dialog is browsing.

The variables and properties you can access at run time differ depending on the state of execution.

Select
 Copy Property Path
 to copy the literal string for the selected variable to the system clipboard. You can then paste the string into an expression or into the code for a step module.

#### See Also

[Engine.DisplayBrowsePropertyObjectDialog Method](../tsapiref/engine-displaybrowsepropertyobjectdialog.html)

[PropertyObject](../tsapiref/propertyobject.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/build-sql-select-statement-dialog-box.html language=enus -->
## TOPIC 03410: Build SQL Select Statement Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/build-sql-select-statement-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/build-sql-select-statement-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Build on the SQL Statement tab of the Edit Open SQL Statement dialog box to launch the Build SQL Select Statement dialog box. The Build SQL Select Statement dialog box contains the following options: Data Link Name —Indicates the name of the data link to use to populate the Table and Column ri

### Build SQL Select Statement Dialog Box

Click
 Build
 on the
 [SQL Statement](sql-statement-tab-edit-open-sql-statement-dia.html)
 tab of the
 [Edit Open SQL Statement](edit-open-sql-statement-dialog-box.html)
 dialog box to launch the Build SQL Select Statement dialog box.

The Build SQL Select Statement dialog box contains the following options:

- Data Link Name 
 —Indicates the name of the data link to use to populate the Table and Column ring controls. Click
 Select Data Link 
 to select a
 predefined data link 
 in the
 Select Data Link 
 dialog box. When you select a data link, TestStand automatically updates the Table and Column ring controls in the Add/Remove Columns section.
- Add/Remove Columns 
 —Select the tables and columns to include in the SQL SELECT statement. TestStand populates the Table ring control with the tables the selected data link defines. When you select a table in the Table ring control, TestStand populates the Column ring control with a list of all columns in the table. When you want to select all columns in the SQL statement, choose the
 * 
 item in the Column control.

Use the
 Add
 button to insert the selected table and column into the Table and Column list control. You can remove an item from the list control by selecting the item you want to delete and clicking
 Remove
 . You can reorder the items in the list control by selecting an item and clicking the up or down arrow buttons.

- Where Clause 
 —An SQL WHERE clause to include in the SQL SELECT statement. You can specify a literal string or an expression TestStand evaluates at run time. Refer to
 Structured Query Language (SQL) 
 for an overview of SQL commands. Click the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box.

#### See Also

[Data Link Properties dialog box](data-link-properties-dialog-box.html)

[Edit Open SQL Statement dialog box](edit-open-sql-statement-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Select Data Link dialog box](select-data-link-dialog-box.html)

[Structured Query Language (SQL)](/csh?context=ts_tsfundamentals_sql)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/build-status-tab-teststand-deployment-utility.html language=enus -->
## TOPIC 03411: Build Status Tab - TestStand Deployment Utility

- bundle_id: `teststand-api-reference`
- source_path: `tsref/build-status-tab-teststand-deployment-utility.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/build-status-tab-teststand-deployment-utility.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Build Status Tab Use the Build Status tab to monitor progress and log information when analyzing files to include in a full or patch deployment and when building a full or patch deployment image and installer . The utility does not save the status log file until you click the Save Log button. Nation

### Build Status Tab - TestStand Deployment Utility

#### Build Status Tab

Use the Build Status tab to monitor progress and log information when analyzing files to include in a full or
 [patch](/csh?context=ts_tsdeploysystem_createpatch)
 deployment and when
 [building a full or patch deployment image](/csh?context=ts_tsdeploysystem_deployableimage)
 and
 [installer](/csh?context=ts_tsdeploysystem_buildinstaller)
 . The utility does not save the status log file until you click the
 Save Log
 button. National Instruments recommends that you save build status log files, especially for deployments that you might patch, so you can compare changes between different versions of the deployment.

The Build Status tab contains the following options:

- Abort 
 —Stops the deployment build process. This button is dimmed when the deployment utility is not performing a build.
- Build State 
 —Displays the current state of the deployment build or displays information about the previous deployment build.
- Save Log 
 —Exports an XML file that contains all the information you need to rebuild the log or a text file that contains most of the information the Status Log displays. Select
 Technical Support Report 
 from the
 Save Log 
 button pull-down menu to create a file that you can send to National Instruments to help diagnose issues related to the deployment and installer creation process.
- Clear Log 
 —Removes the data from the Status Log control.
- Status Log 
 —Contains real-time information about the deployment process, such as when analysis starts and completes, when the utility processes files, and when the deployment build starts and completes. When the deployment build completes, review the status log for the following types of warning or error messages the utility returns:
 
 Click the
 + 
 icon to expand a message for additional information, such as system information, source path to destination path transformations, build summary, and installer details.
 Click the Status Log and press
 <Ctrl+F> 
 to launch the Find option, in which you can enter text you want to search for.
 You can use the arrow pull-down menus in the Severity, Code, Message, and Additional Details column headings of the Status Log or the Status Log context menu to display only messages that match a certain filter criteria. Click the arrow pull-down menu in the column headings to filter the Status Log to display only the items you select from the pull-down menu. Select
 (Custom) 
 to launch the Custom AutoFilter dialog box, in which you can customize the information to display.
 You can also use the Severity, Code, Message, and Additional Details column headings of the Status Log to change the display order of the data. Click the column heading to order the data in that column in descending order. Click the column heading a second time to order the data in ascending order. Click the column heading a third time to restore the original order by time.
 The Additional Details column includes an icon for messages that display more information in the Additional Details tab in the lower right corner of the Build Status tab. 
 Use the Status Log context menu to group and display messages by category in expandable rows. For messages that reference a file, you can also use the context menu to navigate to the file in Windows Explorer or on the Distributed Files tab or to open the file in the application associated with the file extension. Right-click the Status Log to launch the context menu, which contains the following options:
  - Information 
 —Issues that might be a warning or error that you cannot resolve before creating the deployment and must verify in the final deployment, such as steps that contain expressions the utility was unable to resolve.
  - Warning 
 —Issues that do not break the deployment creation process but might cause incorrect behavior in the final deployment, such as configuring a step with an absolute path.
  - Error 
 —Issues that you must resolve before the deployment creation process can complete successfully.
  - Group by 
 —Contains the following options:
    - Severity 
 —Groups messages by severity level, such as process, warning, and error. Grouping messages by severity level might display the same message multiple times because the issue occurs in different phases during deployment or the Status Log includes information for multiple deployments.
    - Code 
 —Groups messages by numeric code value.
    - Message 
 —Groups messages by the text the message contains. Grouping messages this way might display the same message multiple times because the issue occurs in different phases during deployment or the Status Log includes information for multiple deployments.
    - Phase 
 —Groups messages by the deployment creation phase, such as setup, analysis, and cleanup.
    - Deployment Version 
 —Groups messages by the value of the Deployment Version option on the Mode tab of the utility.
    - Remove Grouping 
 —Displays all messages in default order.
  - Go To Location 
 —Contains the following options for messages that include a path or file:
    - Open in <application> 
 —Opens the file using the application associated with the file extension.
    - Open in Explorer 
 —Locates the file in Windows Explorer.
    - Select in the Files View 
 —Selects the file on the Distributed Files tab of the utility.
  - Copy as XML 
 —Copies the full content of the message in XML format.
  - Copy 
 —Copies most of the content of the message in text format.
  - Expand all 
 —Expands all messages that include additional information.
  - Collapse all 
 —Collapses all messages that include additional information.
- Help Tab 
 —Provides information about the most common errors and warnings, such as why the error or message occurred and guidance to help you resolve the issue.
- Additional Details 
 —When the Additional Details column of the Status Log includes an icon, this tab displays the calling hierarchy of VIs for relevant messages.

#### See Also

[Deploying TestStand Systems](/csh?context=ts_10203)

[TestStand Deployment Utility Error Codes](../tserrors/teststand-deployment-utility-messages.html)

Parent topic:

TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/built-in-step-types.html language=enus -->
## TOPIC 03412: Built-In Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/built-in-step-types.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/built-in-step-types.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand includes the following built-in step types: Action Sequence Call Statement Label Message Popup Call Executable Property Loader Legacy Property Loader FTP Files Additional Results To edit a built-in step type in the TestStand Sequence Editor , use the tabs on the Step Settings pane. The tab

### Built-In Step Types

TestStand includes the following built-in step types:

- Action
- Sequence Call
- Statement
- Label
- Message Popup
- Call Executable
- Property Loader
- Legacy Property Loader
- FTP Files
- Additional Results

To edit a built-in step type in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , use the tabs on the
 [Step Settings](step-settings-pane.html)
 pane. The tabs available update based on the type of step you select.

To edit a built-in step type in a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select
 Edit
 from the context menu for the step or click
 Edit
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/c-c-dll-adapter-configuration-dialog-box.html language=enus -->
## TOPIC 03413: C/C++ DLL Adapter Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/c-c-dll-adapter-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/c-c-dll-adapter-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»Adapters , select the C/C++ DLL Adapter in the list control, and click Configure to launch the C/C++ DLL Adapter Configuration dialog box. The C/C++ DLL Adapter Configuration dialog box contains the following options: Show Function Arguments in Step Description —When you enable this

### C/C++ DLL Adapter Configuration Dialog Box

Select
 Configure»Adapters
 , select the C/C++ DLL Adapter in the list control, and click
 Configure
 to launch the C/C++ DLL Adapter Configuration dialog box.

The C/C++ DLL Adapter Configuration dialog box contains the following options:

- Show Function Arguments in Step Description 
 —When you enable this option, the description for a step displays the function and the parameters of the function. When you disable this option, the description displays the function and DLL name.
- Default Struct Packing 
 —Specifies how the C/C++ DLL Adapter packs
 structure parameters it passes 
 . Set the packing options to match the default for structure packing in the DLL development environment. The following packing options are available: 1-, 2-, 4-, 8-, and 16-byte boundaries.
 Note 
 The development environment you use to create DLLs determines the choice for the structure value packing value, as follows:
 Visual C++ and Symantec C++ have a default of 8-byte packing.
 LabVIEW, Borland C++, and Watcom C++ have a default of 1-byte packing.
 For LabWindows/CVI, the default packing can be either 1- or 8-byte, depending on the compatibility mode. For example, in Visual C++ compatibility mode, LabWindows/CVI has a default of 8-byte packing.
- Version of Visual Studio to Use for Create and Edit Code 
 —The version of Microsoft Visual Studio that the C/C++ DLL Adapter uses to perform Create Code and Edit Code operations.
- Version of Visual Studio to Use for Debugging 
 —The version of Visual Studio that the C/C++ DLL Adapter uses to
 debug code modules 
 .

#### See Also

[Type Properties dialog box](type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/c-c-dll-module-tab.html language=enus -->
## TOPIC 03414: C/C++ DLL Module Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/c-c-dll-module-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/c-c-dll-module-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a step configured to use the C/C++ DLL Adapter and select Specify Module or Step Settings from the context menu to display the C/C++ DLL Module tab in the TestStand Sequence Editor . The C/C++ DLL Module tab contains the following options: Module —The pathname of the DLL file that contains th

### C/C++ DLL Module Tab

Insert a step configured to use the C/C++ DLL Adapter and select
 Specify Module
 or
 Step Settings
 from the context menu to display the C/C++ DLL Module tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 . The C/C++ DLL Module tab contains the following options:

- Module 
 —The pathname of the DLL file that contains the function the step calls. You can specify an absolute or relative pathname for the DLL file. Relative pathnames are relative to the TestStand
 search directory paths 
 .
 You can customize the search directory paths using the
 [Edit Search Directories](edit-search-directories-dialog-box.html)
 dialog box.
- Function 
 —Selects the function in the
 code module 
 the step calls. If a DLL file contains a type library or if a type library exists with the same name as the DLL file, the C/C++ DLL Adapter automatically populates the Function ring control with all of the function names in the type library. Otherwise, the C/C++ DLL Adapter reads the DLL file and finds the names of all functions the DLL exports. The C/C++ DLL Adapter also includes the names of
 exported, static C++ class methods that use data types TestStand supports 
 . If a DLL type library contains links to a help file for a function, you can click the
 ? 
 button to access the help.
- Reload Prototype 
 —Allows the user to refresh the parameter information for the function call. If you
 create a DLL 
 using LabWindows/CVI 7.1 or later, TestStand can read the prototype information for the currently selected function without the use of a type library.
- Code Template 
 —The code template to which the module call adheres. TestStand lists the code templates the step type defines. The Code Template control contains the following default options:
  - None 
 —Specifies if the module call does not adhere to a prototype of any code template. When you select this option, the
 New 
 and
 Delete 
 buttons in the Parameters Table are enabled.
  - Default template for Visual C++ 6.0 SP3 or greater 
 —Specifies whether the module adheres to the default template for the C/C++ adapter when used with Microsoft Visual C++.
- Parameters Table 
 —Shows all of the available parameters for the function call and an entry for the return value. The Parameters Table control contains the following columns:
 
 If a DLL file contains export information or a type library or if a type library exists with the same base name as the DLL file that resides in the same directory as the DLL file, the C/C++ DLL Adapter queries the type library for the parameter list information. In addition, if a DLL file contains C++ type information Visual Studio creates, the C/C++ DLL Adapter obtains the parameter list information from the DLL file. When the adapter finds parameter list information for the function it displays, it automatically updates the Parameters Table control when you select a new function in the Function ring control. You can request the C/C++ DLL Adapter to query the type information for the currently selected function at any time by clicking the
 Reload Prototype 
 button. If the module file does not have type information, you must enter parameter information manually.
 When you select a parameter in the view, the Parameter Details Table control displays specific details about the parameter. To insert or remove parameters, click
 New
 or
 Delete
 . To rearrange the parameter order, select the parameter you want to move and click
 Move Up
 or
 Move Down
 . You must select the
 None
 code template before attempting to insert, remove, or rearrange parameters.
  - Parameter Name 
 —A symbolic name for the parameter.
 Note 
 Parameters with attributes include an
 Edit Attributes
 button in the Name column of the Parameters Table. TestStand associates parameter attributes with the module parameter, which TestStand stores with the step configuration information, not with the parameter value that TestStand passes to the module. Right-click an item in the Parameter Table to access the
 [Parameters Table](for-module-tabs-parameters-table-context-menu.html)
 context menu, from which you can launch the
 [Attributes](attributes-dialog-box.html)
 dialog box. You cannot edit attributes for the real and imaginary parts of complex parameters and complex vector parameters in the C/C++ DLL Adapter.
  - Description 
 —The short description of the parameter type using C++ syntax.
  - Log 
 —When you enable this option, the step logs the parameter as an additional result. Enabling this option is equivalent to using the checkbox next to the additional result name on the
 Additional Results panel 
 of the
 Properties 
 tab of the
 Step Settings 
 pane. For in/out parameters, enabling this option enables the [In] parameter and the [Out] parameter on the Additional Results panel. This option is indeterminate for in/out parameters if you specify to log only the [In] parameter value or only the [Out] parameter value. If this option is indeterminate, a tooltip specifies whether the Additional Results panel specifies to log the [In] parameter value or the [Out] parameter value.
  - Value Expression 
 —The argument expression to pass.
- Parameter Details Table 
 —The data type of each parameter and additional information according to each parameter type.
 
 Note 
 The C/C++ DLL Adapter supports numeric return values, which includes Boolean, void*, and void.
  - Category 
 —A group of data types to list in the Data Type control. The following categories are available in the Category ring control:
 Numeric 
 ,
 Boolean 
 ,
 String 
 ,
 Enumeration 
 ,
 Object 
 ,
 TS Object 
 ,
 C Struct 
 ,
 Arrays 
 , selected
 C++ class 
 , and
 Pointer/Handle 
 types.
- Create Code 
 —Creates the source code shell for the function. You must specify an existing source file when creating code in Visual Studio. If the source file you specify does not already exist when creating code in a text file, the adapter creates it. If the file already exists, the C/C++ DLL Adapter appends the function to the end of the file. If a code template file exists for the step type you use for the step, the C/C++ DLL Adapter uses the template to create the shell of the new function. When the project file you specify is not in the solution, the C/C++ DLL Adapter prompts you to add it. When the source file you specify is not in the project, the C/C++ DLL Adapter prompts you to add it. When the C/C++ DLL Adapter creates the code, the adapter launches the application currently registered on the system for the type of the file, such as Visual Studio for
 .cpp 
 files, and displays the file in the application.
- Edit Code 
 —Edits the source code for the function if the source code already exists.
- Verify Prototype 
 —Checks for any conflicts between the source code and the parameter information on the Module tab. Refer to
 Parsing Parameters from Source Code 
 for more information about how the adapter interprets parameter declarations when parsing source code.
- Source Code Files 
 —Launches the
 DLL Source Code Files 
 window, in which you can specify the pathname for the source file, project file, and solution file that implements the function the module calls.
- Function Call 
 —Directly edits the function name and all function arguments at once.

#### Editing the Function Call

You can use the various controls on the C/C++ DLL Module tab to edit the function name and the argument values of the function. You can also use the Function Call control to directly edit the function name and all of the function arguments at once. In the Function Call control, edit the call just as you would in a source code editor. If you enter a number of arguments different than the function prototype specifies, TestStand prompts you to alter the prototype to match the number and type of arguments you specify.

When you make a change in the Function Call control, the following buttons appear while all other controls dim:

- Accept 
 —Applies the changes you make in the Function Call control.
- Revert 
 —Discards the changes you make in the Function Call control.

Note

#### See Also

[Attributes dialog box](attributes-dialog-box.html)

[DLL Source Code Files Window](dll-source-code-files-window.html)

[Exporting Class Methods and Functions in Microsoft Visual Studio](/csh?context=ts_tsref_exporting_in_net)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Locating the Correct DLL in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64locatingdlls)

[Parsing Parameters from Source Code](/csh?context=ts_tsref_parsing_parameters_from_source_code)

[Parameters Table Context Menu for Module Tabs](for-module-tabs-parameters-table-context-menu.html)

[Step Settings Pane](step-settings-pane.html)

[Using Side-by-Side Versions of the LabWindows/CVI Run-Time Engine with TestStand](/csh?context=ts_tsfundamentals_sxscvirte)

[Using the $(Platform) Path Macro to Locate the Correct Code Module in 32-bit TestStand and 64-bit TestStand](/csh?context=ts_tsfundamentals_64platformmacro)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/c-class-parameters-c-c-dll-call-parameters.html language=enus -->
## TOPIC 03415: C++ Class Parameters - C/C++ DLL Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/c-class-parameters-c-c-dll-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/c-class-parameters-c-c-dll-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: C++ Class Parameters If you create a C++ DLL using National Instruments Measurement Studio in Microsoft Visual Studio, you can pass TestStand data to Measurement Studio class objects. The following table shows the supported C++ classes and the corresponding data types you can pass. (64-bit TestStand

### C++ Class Parameters - C/C++ DLL Call Parameters

#### C++ Class Parameters

If you create a C++ DLL using National Instruments Measurement Studio in Microsoft Visual Studio, you can pass TestStand data to Measurement Studio class objects. The following table shows the supported C++ classes and the corresponding data types you can pass.

(64-bit TestStand) Measurement Studio data types (
 CNiVector
 ,
 CNiMatrix
 ,
 CNiComplex
 ,
 CNiComplexVector
 ,
 CNiBoolVector
 ,
 CNiString
 ) are not supported.

| Category | Compatible TestStand Type |
| --- | --- |
| CNiVector | Array of Numbers (one-dimensional) |
| CNiMatrix | Array of Numbers (two-dimensional) |
| CNiComplex | Two Numbers |
| CNiComplexVector | Two Arrays of Numbers (one-dimensional) |
| CNiBoolVector | Array of Booleans (one-dimensional) |
| CNiString | String |
| CString | String |
| CStringArray | Array of Strings (one-dimensional) |
| _bstr_t | String |

If the Visual Studio project is not a Measurement Studio project, you can pass data to the
 CString
 ,
 CStringArray
 , and
 _bstr_t
 classes. To add support for these classes to the DLL, include the
 tsdllparams.cpp
 source file, located in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \API\VC
 directory, in a single source file in the project.

The
 CNiVector
 ,
 CNiMatrix
 ,
 CNiComplex
 , or
 CNiComplexVector
 categories contain the same data types as the Numeric category. Each of these categories correspond to Measurement Studio C++ template, for which the Type control specifies the template argument. The following table shows the Measurement Studio classes that correspond to each TestStand category and type.

| Category | Type Setting | Measurement Studio Class |
| --- | --- | --- |
| CNiVector | Signed 8-bit Integer | CNiInt8Vector |
| Unsigned 8-bit Integer | CNiUInt8Vector |  |
| Signed 16-bit Integer | CNiInt16Vector |  |
| Unsigned 16-bit Integer | CNiUInt16Vector |  |
| Signed 32-bit Integer | CNiInt32Vector |  |
| Unsigned 32-bit Integer | CNiUInt32Vector |  |
| 32-bit Real Number | CNiReal32Vector |  |
| 64-bit Real Number | CNiReal64Vector |  |
| CNiMatrix | Signed 8-bit Integer | CNiInt8Vector |
| Unsigned 8-bit Integer | CNiUInt8Matrix |  |
| Signed 16-bit Integer | CNiInt16Matrix |  |
| Unsigned 16-bit Integer | CNiUInt16Matrix |  |
| Signed 32-bit Integer | CNiInt32Matrix |  |
| Unsigned 32-bit Integer | CNiUInt32Matrix |  |
| 32-bit Real Number | CNiReal32Matrix |  |
| 64-bit Real Number | CNiReal64Matrix |  |
| CNiComplex | Signed 8-bit Integer | CNiComplexInt8 |
| Unsigned 8-bit Integer | CNiComplexUInt8 |  |
| Signed 16-bit Integer | CNiComplexInt16 |  |
| Unsigned 16-bit Integer | CNiComplexUInt16 |  |
| Signed 32-bit Integer | CNiComplexInt32 |  |
| Unsigned 32-bit Integer | CNiComplexUInt32 |  |
| 32-bit Real Number | CNiComplexReal32 |  |
| 64-bit Real Number | CNiComplexReal64 |  |
| CNiComplexVector | Signed 8-bit Integer | CNiComplexInt8Vector |
| Unsigned 8-bit Integer | CNiComplexUInt8Vector |  |
| Signed 16-bit Integer | CNiComplexInt16Vector |  |
| Unsigned 16-bit Integer | CNiComplexUInt16Vector |  |
| Signed 32-bit Integer | CNiComplexInt32Vector |  |
| Unsigned 32-bit Integer | CNiComplexUInt32Vector |  |
| 32-bit Real Number | CNiComplexReal32Vector |  |
| 64-bit Real Number | CNiComplexReal64Vector |  |

#### Pass by Value or by Reference

When you select one of the C++ classes as the category for a parameter, the C/C++ DLL Adapter displays the Pass control. This control specifies whether TestStand passes the value of the argument you specify in the Value Expression control or passes a pointer to the argument. If you select
 By Pointer (*)
 ,
 By Const Pointer (const*)
 ,
 By Reference (&)
 , or
 By Const Reference (const &)
 , the C/C++ DLL Adapter passes a pointer to the argument value.

Before calling the DLL function, TestStand constructs a temporary C++ class object of the selected type and initializes the object with the argument value. If you choose to pass by value, TestStand passes the temporary object to the DLL function on the call stack. When the DLL function returns, TestStand does not copy the data of the function back to the TestStand argument.

If you choose to pass a pointer, TestStand passes a pointer to the temporary object to the DLL function. If you specify By Pointer (*) or By Reference (&), TestStand copies the object data back to the TestStand argument when the DLL function returns. In this case, the argument you specify in the Value Expression control must be the name of a variable or property. TestStand destroys the temporary object after the DLL function returns.

Note

NULL

Nothing

0

#### See Also

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Microsoft Visual C++/#import](/csh?context=ts_tsapiref_visual_cpp_import)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/c-struct-passing-tab-type-properties-dialog-b.html language=enus -->
## TOPIC 03416: C Struct Passing Tab - Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/c-struct-passing-tab-type-properties-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/c-struct-passing-tab-type-properties-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: C Struct Passing Tab You can use the C/C++ DLL Adapter or LabWindows/CVI Adapter to pass a TestStand variable or property to a structure parameter in a code module function. The data type of the variable or property you pass must contain all fields the structure parameter expects. If a data type con

### C Struct Passing Tab - Type Properties Dialog Box

#### C Struct Passing Tab

You can use the C/C++ DLL Adapter or LabWindows/CVI Adapter to pass a TestStand variable or property to a structure parameter in a
 [code module](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 function. The data type of the variable or property you pass must contain all fields the structure parameter expects. If a data type contains a subproperty that is a named data type, you must also allow objects of the named data type to be passed as a structure.

There are several ways to format data type fields in the in-memory representation of a structure parameter. Use the C Struct Passing tab to specify how TestStand formats an instance of a data type you pass as a structure in memory.

The C Struct Passing tab can contain the following options:

- Allow Objects of this Type to be Passed as Structs 
 —Passes instances of the data type to structure parameters.
- Packing 
 —Select the Packing option according to the development environment and compiler settings you use to create the DLLs you call.
 Microsoft Visual C++ and Symantec C++ have a default of 8-byte packing. LabVIEW, Borland C++ and Watcom C++ have a default of 1-byte packing. For LabWindows/CVI, the default packing can be either 8- or 1-byte, depending upon the compatibility mode. For example, in Visual C++ compatibility mode, LabWindows/CVI has a default of 8-byte packing. Configure this option for all data types that specify Default Adapter Packing in the
 [C/C++ DLL Adapter Configuration](c-c-dll-adapter-configuration-dialog-box.html)
 or
 [LabWindows/CVI Adapter Configuration](labwindows-cvi-adapter-configuration-dialog-b.html)
 dialog boxes.
- Property 
 —Use this ring control to select a subproperty of the data type in order to specify the in-memory format of the subproperty. You can also configure the in-memory format for a data type subproperty in the Variable Properties dialog box for the subproperty.
 If a subproperty of the data type is a named type, the Property control does not include the subproperties of the type in the ring control. You must separately configure the named data type to allow the C/C++ DLL Adapter to pass objects of the named type as a structure, and specify the structure elements to map.
- Exclude when Passing Structure 
 —When you enable this option, TestStand does not include the selected subproperty in the in-memory representation of the data type.
- Type 
 —The data type of the selected subproperty.
- Numeric Type 
 —Specifies whether the numeric property is a real, signed, or unsigned integer. It also specifies whether the numeric property is 8-, 16-, 32-, or 64-bit.
- String Type 
 —Specifies whether a pointer to string references a C-string, unicode string, C-string buffer, or unicode string buffer.
- Store Array as 
 —Visible for array subproperties only. This control contains the following options:
  - Embedded Array 
 —The array resides within the in-memory representation of the data type.
  - Pointer To Array 
 —A pointer to the array resides within the in-memory representation of the data type. The C/C++ DLL and LabWindows/CVI Adapters cannot call functions that specify structure fields that contain pointers to memory which the function allocates or deallocates.
  - LabVIEW Array 
 —The struct member is a LabVIEW array.
- Store Struct as 
 —Visible for container subproperties only. This control contains the following options:
  - Embedded Struct 
 —The structure representation of the container property resides within the in-memory representation of the data type.
  - Pointer To Struct 
 —A pointer to the structure representation of the container property resides within the in-memory representation of the data type. The C/C++ DLL and LabWindows/CVI Adapters cannot call functions that specify structure fields that contain pointers to memory which the function allocates or deallocates.
- String Buffer Size 
 —Visible for string subproperties only. The maximum size of an inline or buffered string.
- Store String as 
 —Visible for string subproperties only. This control contains the following options:
  - Inline String 
 —The struct member is an array of characters.
  - Pointer to String 
 —The struct member is a pointer to an array of characters. The C/C++ DLL and LabWindows/CVI Adapters cannot call functions that specify structure fields that contain pointers to memory which the function allocates or deallocates.
  - LabVIEW String 
 —The struct member is a LabVIEW string.
- <
 Type Ring
 > 
 —Specifies how to format the subproperty in memory. The choices vary according to the subproperty type and are the same as the data passing options you specify for parameters on the Module tab of the Step Settings pane for the C/C++ DLL and LabWindows/CVI Adapters or in the
 Edit DLL Module Call 
 or
 Edit LabWindows/CVI Module Call 
 dialog boxes.

#### See Also

[C/C++ DLL Adapter Configuration dialog box](c-c-dll-adapter-configuration-dialog-box.html)

[Edit DLL Module Call dialog box](edit-c-c-dll-call-dialog-box.html)

[Edit LabWindows/CVI Module Call dialog box](edit-labwindows-cvi-module-call-dialog-box.html)

[LabWindows/CVI Adapter Configuration dialog box](labwindows-cvi-adapter-configuration-dialog-b.html)

Parent topic:

Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/call-executable-edit-tabs.html language=enus -->
## TOPIC 03417: Call Executable Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/call-executable-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/call-executable-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Insert a Call Executable step and select Configure Call Executable from the context menu to display the following Call Executable edit tabs in the TestStand Sequence Editor . Call Settings Tab —The executable path, arguments, and options for the Call Executable step, which launches an application or

### Call Executable Edit Tabs

Insert a Call Executable step and select
 Configure Call Executable
 from the context menu to display the following Call Executable edit tabs in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 .

- Call Settings Tab 
 —The executable path, arguments, and options for the Call Executable step, which launches an application or runs a system command.
- Wait Options Tab 
 —Specifies whether the step waits for the call to complete, as well as additional actions to perform based on the exit code from the call.
- Standard Input Tab 
 —The standard input the step passes to the call. You must configure the step to wait for the call to use this tab.
- Standard Output/Error Tab 
 —Specifies where the step stores the standard output and errors from the call. You must configure the step to wait for the call to use this tab.

You can also use the Call Executable edit tabs to configure a Sequence Call step for
 [calling scripting languages from TestStand](calling-scripting-languages-from-teststand.html)
 .

#### See Also

[Calling Scripting Languages from TestStand](calling-scripting-languages-from-teststand.html)

Parent topic:

Call Executable Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/call-executable-step.html language=enus -->
## TOPIC 03418: Call Executable Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/call-executable-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/call-executable-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Call Executable step launches an application or runs a system command. You can also use a Call Executable step to call scripting languages from TestStand . Configuring the Step Use the Call Executable edit tabs in the TestStand Sequence Editor and the Configure Call Executable dialog box in a Te

### Call Executable Step

The Call Executable step launches an application or runs a system command. You can also use a Call Executable step to
 [call scripting languages from TestStand](calling-scripting-languages-from-teststand.html)
 .

#### Configuring the Step

Use the
 [Call Executable edit tabs](call-executable-edit-tabs.html)
 in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Call Executable](configure-call-executable-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the executable path, arguments, and options for the Call Executable step.

When you specify the name of a non-executable file, the step launches the file using the default application associated with the extension of the file. For example, you can execute a Python or Perl script file or open a text file by specifying the non-executable file directly.

You can use
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 to specify the path to the executable and to configure the working directory. You can use an absolute path to the working directory, use the executable directory, use the sequence file directory, or use the current working directory of the TestStand application.

You can configure whether the step waits for the call to exit or waits for a specified amount of time. When a step waits for the call, you can configure the standard input passed to the call and where to store the standard output and error the call generates.

You can configure the step to stream a file as input or evaluate a string or an expression as input. You can store the output and error information in a file on the local computer or on the remote computer when you call the executable on a remote computer. TestStand overwrites the file if it already exists. Alternatively, you can use expressions to store the output and error information in TestStand variables or properties. When you store the information in a variable or property, you can use Additional Results to include the information in the report TestStand generates.

#### Final Status of a Call Executable Step

The final
 [status](/csh?context=ts_tsfundamentals_step_status_values_table)
 of a Call Executable step can depend on whether the step waits for the executable to exit, as described in the following table.

| Scenario | Step Status |
| --- | --- |
| The step does not wait for the executable to exit. | Done |
| The step waits for the executable to exit and a timeout does not occur. | Done , Passed , or Failed , depending on the status action you specify in the Exit Code Status Action ring control on the Call Executable edit tab for the step. When you set the Exit Code Status Action ring control to No Action , the step always sets the step status to Done . Otherwise, you can choose to set the step status to Failed based on the value of the exit code—less than zero, greater than zero, equal to zero, or not equal to zero. You can also choose to ignore or set the step status to Error or Failed when the executable you call returns standard error information. |
| The step waits for the executable to exit but a timeout occurs. | Error |

#### Step Properties

Note

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Call Executable step type defines the following step properties:

- Step.Result.ExitCode 
 —The exit code the executable returns.
- Step.Executable 
 —The pathname of the executable to launch.
- Step.ExecutableExpr 
 —The expression for the pathname of the executable to launch.
- Step.SpecifyExeByExpr 
 —Specifies whether the step uses the
 Step.Executable 
 property or the
 Step.ExecutableExpr 
 property to determine the executable to launch.
- Step.ExecutableCalled 
 —The executable the step called.
- Step.Arguments 
 —The expression for the argument string the step passes to the executable.
- Step.WaitCondition 
 —Specifies how the step waits for the executable to exit before completing.
- Step.TimeToWait 
 —The number of seconds to wait for the executable to exit.
- Step.InitialWindowState 
 —Specifies if the executable is initially active, not active, hidden, normal, minimized, or maximized.
- Step.TerminateOnAbort 
 —Specifies whether to terminate the executable process when the execution terminates or aborts while waiting for the executable.
- Step.StoreProcessHandle 
 —When this property is
 True 
 , the step stores the Microsoft Windows process handle in a variable or property.
- Step.ProcessHandleExpr 
 —The expression that determines the variable or property in which the step stores the Windows process handle for the executable.
- Step.ProcessHandle 
 —A number property in which to store the Windows process handle for the executable. Only 32-bit TestStand can use this property, which is available only to support backward compatibility. For new instances of this step type, use the
 Step.ProcessHandlePtr 
 property instead because it supports 32-bit TestStand and 64-bit TestStand.
- Step.ProcessHandlePtr 
 — Default value for the
 Step.ProcessHandleExpr 
 property to store the Windows process handle for the executable.
- Step.ExitCodeStatusAction 
 —The condition the step evaluates for the exit code the executable returns to set the step status to
 Failed 
 .
- Step.ExitCodeErrorAction 
 —Specifies the condition the step evaluates for the exit code the executable returns to set the step status to
 Error 
 .
- Step.RemoteSettings 
 —Contains the following settings for calling the executable on a remote computer:
  - Enabled 
 —TestStand calls the executable on a remote computer.
  - Host 
 —The computer name or IP address of the remote computer. The
 Step.RemoteSettings.HostByExpr 
 property specifies whether the step interprets this property value as an expression or as a string.
  - HostByExpr 
 —When this setting is
 True 
 , the step interprets the
 Step.RemoteSettings.Host 
 property value as an expression. When this setting is
 False 
 , the step interprets the value as a string.
  - Port 
 —The port number the remote host server application uses.
  - Password 
 —The password configured on the remote host server application. The
 Step.RemoteSettings.PasswordByExpr 
 property specifies whether the step interprets this property value as an expression or as a string.
  - PasswordByExpr 
 —When this setting is
 True 
 , the step interprets the
 Step.RemoteSettings.Password 
 property value as an expression. When this setting is
 False 
 , the step interprets the value as a string.
- Step.StdInput 
 —Contains the following standard input settings:
  - Type 
 —A value that specifies the method for passing standard input to the call. The valid values are
 0 
 = No Input,
 1 
 = String,
 2 
 = Expression,
 3 
 = File on Local Machine, and
 4 
 = File on Remote Machine.
  - Source 
 —The standard input string, expression, or file pathname. The
 Step.StdInput.IsExpr 
 property specifies whether the step interprets a file pathname value in this property as an expression or as a string.
  - IsExpr 
 —When this setting is
 True 
 , the step interprets a file pathname value in the
 SourceStep.StdInput.Source 
 property as an expression. When this setting is
 False 
 , the step interprets the value as a string.
- Step.StdOutput 
 —Contains the following standard output settings:
  - Dest 
 —A value that specifies the method for retrieving standard output from the call. The valid values are
 0 
 = Ignore,
 1 
 = Store in Variable/Property,
 2 
 = Save to Local File, and
 3 
 = Save to Remote File.
  - Expr 
 —The standard output variable/property or file pathname. The
 Step.StdOutput.IsExpr 
 property specifies whether the step interprets a file pathname value in this property as an expression or as a string.
  - IsExpr 
 —When this setting is
 True 
 , the step interprets a file pathname value in the
 SourceStep.StdOutput.Source 
 property as an expression. When this setting is
 False 
 , the step interprets the value as a string.
  - Text 
 —Default property for the value of the
 Step.StdOutput.Expr 
 property when the
 Step.StdOutput.Dest 
 property specifies to store the standard output to a variable or property.
- Step.WorkingDir 
 —Contains the following working directory settings:
  - Source 
 —A value that specifies the method to determine the working directory. The valid values are
 0 
 = Use Current Working Directory,
 1 
 = Use Executable Directory,
 2 
 = Use Sequence File Directory, and
 3 
 = Specific Directory.
  - Expr 
 —A specific working directory. The
 Step.WorkingDir.IsExpr 
 property specifies whether the step interprets this property value as an expression or as a string.
  - IsExpr 
 —When this setting is
 True 
 , the step interprets the working directory path in the
 SourceStep.WorkingDir.Expr 
 property as an expression. When this setting is
 False 
 , the step interprets the path as a string.
- Step.StdError 
 —Contains the following standard error settings:
  - Dest 
 —A value that specifies the method for retrieving standard error from the call. The valid values are
 0 
 = Ignore,
 1 
 = Store in Variable/Property,
 2 
 = Save to Local File, and
 3 
 = Save to Remote File.
  - Expr 
 —The standard error variable/property or file pathname. The
 Step.StdError.IsExpr 
 property specifies whether the step interprets a file pathname value in this property as an expression or as a string.
  - IsExpr 
 —When this setting is
 True 
 , the step interprets a file pathname value in the
 SourceStep.StdError.Expr 
 property as an expression. When this setting is
 False 
 , the step interprets the value as a string.
  - Text 
 —Default property for value of the
 Step.StdError.Expr 
 property when the
 Step.StdError.Dest 
 property specifies to store the standard error in a variable or property.
- Step.Action 
 —Specifies how TestStand responds when the standard error is not empty. The valid values are
 0 
 = No Action,
 1 
 = Set Step Status to Failed,
 2 
 = Set Step Status to Error.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Call Executable Step Type Support for 64-bit TestStand](/csh?context=ts_tsfundamentals_64callexecutablesteptype)

[Calling Scripting Languages from TestStand](calling-scripting-languages-from-teststand.html)

Parent topic:

Built-In Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/call-graph-pane-context-menu-sequence-hierarc.html language=enus -->
## TOPIC 03419: Call Graph Pane Context Menu - Sequence Hierarchy Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/call-graph-pane-context-menu-sequence-hierarc.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/call-graph-pane-context-menu-sequence-hierarc.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call Graph Pane Context Menu To access the context menu, right-click the Call Graph pane. The items in the context menu vary depending on whether you right-click a node or the background area of the pane. The Call Graph pane context menu contains the following items when you right-click a node: Disp

### Call Graph Pane Context Menu - Sequence Hierarchy Window

#### Call Graph Pane Context Menu

To access the context menu, right-click the Call Graph pane. The items in the context menu vary depending on whether you right-click a node or the background area of the pane.

The Call Graph pane context menu contains the following items when you right-click a node:

- Display Hierarchy From This Node 
 —Displays a new hierarchy graph that starts at the selected node. This option is disabled at the root node because the hierarchy of that node is already displayed. When you select this option, the new hierarchy graph replaces the previous graph in the Call Graph pane. Select the
 Go Back 
 menu item to return to the previous graph.
- Create New Hierarchy From This Node 
 —Displays a new hierarchy graph that starts at the selected node in a new window.
- Go To Sequence Call 
 —Opens the selected sequence in the
 Sequence File 
 window and highlights the Sequence Call step to which the node corresponds.
- Recreate Expression Node For 
 —Recreates the expression node if you replaced an expression node with a sequence in the
 Specify Sequence Call Expressions 
 dialog box. Select the Sequence Call step name from the submenu for the sequence for which you want to recreate the expression node. This option is available only if you used
 expressions 
 to specify the Sequence Call step and if TestStand evaluated the expression.

The Call Graph pane context menu contains the following items when you right-click the background area of the pane:

- Graph Layout 
 —The layout of the graph. This menu item displays the currently selected layout. Select this menu item to launch a submenu that contains the following layout options:
  - Layered Digraph 
 —A layered graph that groups edges into layers so no two edges in the same layer cross. This layout option reduces link crossings and produces clean graphs. This is the default option.
  - Tree Graph 
 —A layered graph that displays rapidly. Link overlapping can occur if cycles exist in the graph. Links can cross nodes if a node has more than one parent node.
- Graph Direction 
 —The horizontal or vertical orientation of the graph. This menu item displays the currently selected layout. Select this menu item to launch a submenu that contains the following graph direction options:
  - Horizontal 
 —Displays a horizontal graph.
  - Vertical 
 —Displays a vertical graph.
- Expand All Nodes 
 —Expands all the nodes in the graph.
- Collapse All Nodes 
 —Collapses all the nodes in the graph.
- Expand One Level 
 —Expands all nodes one level.
- Collapse One Level 
 —Collapses all nodes one level
- Allow Rearranging Nodes 
 —Enables or disables the rearranging of nodes on the Call Graph pane. Rearranging nodes is allowed by default. Select this menu item to disallow rearranging nodes. The icon next to the menu item changes to
 
 when rearranging is not allowed. Select this menu item again to restore the default setting.
- Go Back 
 —Returns to the previous graph after you select the Create New Hierarchy From This Node option in the node context menu.
- Go Forward 
 —Displays the next graph after you select the Create New Hierarchy From This Node option in the node context menu and you return to the previous graph.
- Page Setup 
 —Launches the Page Setup dialog box.
- Print Preview 
 —Launches the Print Preview dialog box.
- Print 
 —Launches the Print dialog box.
- View 
 —Restores hidden panes. You can restore the following hidden panes:
  - Call Graph 
 —Restores the Call Graph pane.
  - Legend 
 —Restores the Legend pane.
  - Overview 
 —Restores the Graph Overview pane.
- Update From Sequences 
 —Recreates the graph starting at the root sequence. The new graph reflects any changes you made to the call hierarchy in the sequence file. When you refresh the graph, the color palette might change.

#### See Also

[Sequence File Window](sequence-file-window.html)

[Specify Sequence Call Expressions dialog box](specify-sequence-call-expressions-dialog-box.html)

Parent topic:

Call Graph Pane - Sequence Hierarchy Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/call-graph-pane-sequence-hierarchy-window.html language=enus -->
## TOPIC 03420: Call Graph Pane - Sequence Hierarchy Window

- bundle_id: `teststand-api-reference`
- source_path: `tsref/call-graph-pane-sequence-hierarchy-window.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/call-graph-pane-sequence-hierarchy-window.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call Graph Pane The Call Graph pane displays a graph that represents all the sequence calls that start at the root sequence. Each sequence appears as a node in the graph, and each sequence call step appears as a link. You can expand or collapse the links for each node. The arrow on the link indicate

### Call Graph Pane - Sequence Hierarchy Window

#### Call Graph Pane

The Call Graph pane displays a graph that represents all the sequence calls that start at the root sequence. Each sequence appears as a node in the graph, and each sequence call step appears as a link. You can expand or collapse the links for each node. The arrow on the link indicates the direction of the call, and a number on the link indicates the number of steps that call the sequence. Each node and link has a tooltip that shows more detail about the item. Each node is color-coded. All nodes that represent a sequence in the same sequence file have the same color.

Use the options on the
 [Sequence Hierarchy toolbar](toolbar-buttons-and-shortcuts.html)
 to configure the layout and horizontal and vertical direction of the graph and to arrange the nodes and links. Adjust the default graph layout to your needs before printing or saving the graph to disk, if necessary.

Use the following keyboard shortcuts or the
 [context](call-graph-pane-context-menu-sequence-hierarc.html)
 menu to navigate through the nodes:

| Key | Action |
| --- | --- |
| Arrow left | Selects the node to the left of the currently selected node. The target node can be a sibling or a parent node. |
| Arrow right | Selects the node to the right of the currently selected node. The target node can be a sibling or a child node. |
| Arrow up | Selects the node directly above the currently selected node. The target node can be a sibling or a parent node. |
| Arrow down | Selects the node directly below the currently selected node. The target node can be a sibling or a child node. |
| <*> on the keypad | Expands all nodes. |
| <⁄> on the keypad | Collapses all nodes. |
| <+> on the keypad | Expands the currently selected node. |
| <-> on the keypad | Collapses the currently selected node. |
| <Home> | Selects the root node. |
| <End> | Selects the bottommost or rightmost node, depending on the horizontal or vertical orientation of the graph. |
| <Enter> | Same as double-clicking on the node. |
| Context Menu | Shows the context menu of the selected node. |
| <Shift-F10> | Shows the context menu of the selected node. |

Double-clicking a node opens the sequence in the
 [Sequence File](sequence-file-window.html)
 window. Double-clicking a link opens the sequence in the Sequence File window and highlights the Sequence Call step to which the link corresponds. When multiple Sequence Call steps call the same sequence, a number that equals the number of sequence calls displays on the link. Double-clicking a link that shows such a number launches a combo box, in which you can select the Sequence Call step you want.

If you use
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 to specify a sequence call, TestStand evaluates the expressions while building the graph. TestStand creates a sequence context using the call step. If TestStand cannot evaluate the expressions, an expression node appears on the graph. Right-click the expression node and select
 Specify Sequence Call Expressions
 from the context menu or double-click the expression node to launch the
 [Specify Sequence Call Expressions](specify-sequence-call-expressions-dialog-box.html)
 dialog box, in which you can replace an expression node with any sequence. You can also drag and drop a sequence on an expression node, which is useful when you work with unsaved sequence files.

Note

Callback Overridden

Entry Point Name

Steps

Sequences

Workspace

#### See Also

[Call Graph Pane Context Menu](call-graph-pane-context-menu-sequence-hierarc.html)

[Sequence File Window](sequence-file-window.html)

[Sequences Pane Context Menu](sequences-pane-context-menu-sequence-file-win.html)

[Specify Sequence Call Expression dialog box](specify-sequence-call-expressions-dialog-box.html)

[Steps Pane Context Menu](steps-pane-context-menu-sequence-file-window.html)

[Toolbar Buttons and Shortcuts](toolbar-buttons-and-shortcuts.html)

[Workspace Pane Context Menu](context-menu-workspace-pane.html)

Parent topic:

Sequence Hierarchy Window

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/call-settings-tab-call-executable-edit-tabs.html language=enus -->
## TOPIC 03421: Call Settings Tab - Call Executable Edit Tabs

- bundle_id: `teststand-api-reference`
- source_path: `tsref/call-settings-tab-call-executable-edit-tabs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/call-settings-tab-call-executable-edit-tabs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call Settings Tab Use the Call Settings tab in the TestStand Sequence Editor to specify the executable path, arguments, and options for the Call Executable step, which launches an application or runs a system command. The Call Settings tab contains the following options: File Pathname —Absolute or r

### Call Settings Tab - Call Executable Edit Tabs

#### Call Settings Tab

Use the Call Settings tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify the executable path, arguments, and options for the Call Executable step, which launches an application or runs a system command.

The Call Settings tab contains the following options:

- File Pathname 
 —Absolute or relative pathname for the executable or file the step calls. The step launches non-executable files using a system-associated executable, if defined.
- Specify File Path by Expression 
 —Enable this option to specify that the file pathname is an expression the step evaluates at run time.
- Working Directory 
 —A working directory for the executable that the step calls. The ring control contains the following options:
  - Use File Directory 
 —The directory of the file that the step calls.
  - Use Sequence File Directory 
 —The directory of the sequence file for the step. This option is not available when calling executables on remote computers.
  - Use Current Working Directory 
 —The current directory of the TestStand process at the time of the call.
  - Specific Directory 
 —The directory the Working Directory path specifies.
- Working Directory Path 
 —An absolute path to use as the working directory. This control is available only when you select
 Specific Directory 
 in the Working Directory control.
- Specify Working Directory by Expression 
 —Enable this option to specify that the working directory path is an expression the step evaluates at run time.
- Argument Expression 
 —An expression that the step evaluates at run time to determine the arguments to pass to the executable. The step appends arguments after a non-executable file pathname when performing a call using a system associated executable.
- Initial Window State 
 —Specifies whether the step launches the executable as a hidden, normal, minimized, or maximized application, and whether the application is active initially.
- Remote Settings 
 —Launches the
 Remote Settings 
 window, which specifies whether the step performs the call on a remote computer.

#### See Also

[Remote Settings Window](remote-settings-window2.html)

Parent topic:

Call Executable Edit Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/call-stack-pane-execution-tab.html language=enus -->
## TOPIC 03422: Call Stack Pane - Execution Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/call-stack-pane-execution-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/call-stack-pane-execution-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Call Stack Pane The Call Stack pane displays the call stack for the execution thread currently selected on the Threads pane. A yellow pointer icon appears to the right of the most nested sequence invocation while running. When a step invokes a subsequence, the sequence that contains the calling step

### Call Stack Pane - Execution Tab

#### Call Stack Pane

The Call Stack pane displays the call stack for the execution thread currently selected on the
 [Threads](threads-pane-execution-tab.html)
 pane. A yellow pointer icon appears to the right of the most nested sequence invocation while running.

When a step invokes a subsequence, the sequence that contains the calling step waits for the subsequence to return. The subsequence invocation is nested in the invocation of the calling sequence. The sequence currently executing is the most nested sequence. The chain of active sequences waiting for nested subsequences to complete is called the call stack. The first item in the call stack is the most nested sequence invocation. You can double-click a sequence invocation on the Call Stack pane to display the window for the sequence file.

When execution suspends, you can select a sequence invocation in the call stack by selecting a sequence. The
 [Steps](steps-pane-execution-tab.html)
 pane displays the steps for the sequence invocation you select.

When the
 [Steps](steps-pane-execution-tab.html)
 pane displays the steps for a call stack item that is not the most nested item, a green pointer icon appears next to the waiting Sequence Call step.

#### See Also

[Steps Pane](steps-pane-execution-tab.html)

[Threads Pane](threads-pane-execution-tab.html)

Parent topic:

Execution Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/call-stack-pane.html language=enus -->
## TOPIC 03423: Call Stack Pane

- bundle_id: `teststand-api-reference`
- source_path: `tsref/call-stack-pane.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/call-stack-pane.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Call Stack pane displays the call stack for the execution thread currently selected on the Threads pane. A yellow pointer icon appears to the right of the most nested sequence invocation while the sequence executes. When a step invokes a subsequence, the sequence that contains the calling step w

### Call Stack Pane

The Call Stack pane displays the call stack for the execution thread currently selected on the
 [Threads](threads-pane.html)
 pane. A yellow pointer icon appears to the right of the most nested sequence invocation while the sequence executes.

When a step invokes a subsequence, the sequence that contains the calling step waits for the subsequence to return. The subsequence invocation is nested in the invocation of the calling sequence. The sequence that is currently executing is the most nested sequence. The chain of active sequences that wait for nested subsequences to complete is called the call stack. The first item in the call stack is the most-nested sequence invocation. You can select
 Open <
 sequence file
 >
 from the context menu for or double-click a sequence invocation on the Call Stack pane to display the window for the sequence file.

When execution suspends, you can select a sequence invocation in the call stack by selecting a sequence. The
 [Steps](steps-pane-execution-window.html)
 pane displays the steps for the sequence invocation you select. In the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , the
 [Watch View](watch-view-pane.html)
 pane evaluates watch
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 using the sequence context for the selected sequence invocation.

When the
 [Steps](steps-pane-execution-window.html)
 pane displays the steps for a call stack item that is not the most nested item, a green pointer icon appears next to the waiting Sequence Call step.

#### See Also

[Steps Pane](steps-pane-execution-window.html)

[Threads Pane](threads-pane.html)

[Watch View Pane](watch-view-pane.html)

Parent topic:

Panes

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/calling-scripting-languages-from-teststand.html language=enus -->
## TOPIC 03424: Calling Scripting Languages from TestStand

- bundle_id: `teststand-api-reference`
- source_path: `tsref/calling-scripting-languages-from-teststand.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/calling-scripting-languages-from-teststand.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A scripting language is a programming language you can use to control one or more software applications. Typically, the core code of an application and the scripts are written in different languages, and the end user is often responsible for creating or modifying the scripts. Scripting languages inc

### Calling Scripting Languages from TestStand

A scripting language is a programming language you can use to control one or more software applications. Typically, the core code of an application and the scripts are written in different languages, and the end user is often responsible for creating or modifying the scripts. Scripting languages include the following distinctive features:

- You do not compile a scripting language into an executable. An interpreter converts a scripting language from source code to native computer code at run time.
- Scripting languages can use variables to hold any type of data without explicitly declaring a data type.
- Scripting languages can natively provide some complex data types, such as strings, arrays, lists, and hash functions.
- Scripting languages can automate garbage collection to reduce the chance of memory leaks occurring.

You can use the
 [Call Executable step type](call-executable-step.html)
 in TestStand to call a scripting language, such as Python or Perl, using any of the following methods:

- Specifying the script file as the file to execute
- Configuring the standard input text or file to pass to the executable call
- Configuring the file or variable to retrieve standard output and error
- Specifying the working directory

You can use the File Pathname control on the
 [Call Settings tab](call-settings-tab-call-executable-edit-tabs.html)
 of the
 [Call Executable edit tab](call-executable-edit-tabs.html)
 on the
 [Step Settings pane](step-settings-pane.html)
 to specify the name of a file to open using the default application associated with the extension of the file. For example, you can launch a
 .bat
 file or open a
 .txt
 file by specifying the non-executable file directly. You can also use
 [expressions](/csh?context=ts_tsfundamentals_bldgblocks_expressions)
 to specify the path to the file.

You must configure the step to wait for the specified executable call to exit or wait for a specified time to enable access to the options you use to specify standard input to pass to the call and to specify how to retrieve standard output and standard error from the call.

You can configure the step to stream a file as input or evaluate a string or an expression as input. You can store the output and error information in a file on the local computer or on the remote computer when you call the executable on a remote computer. TestStand overwrites the file if it already exists. Alternatively, you can use an expression to store the output and error information in a TestStand variable or property, and you can use the status expression of the step to evaluate the output value. You can configure the step to ignore or set the
 [step status](/csh?context=ts_tsfundamentals_step_status_values_table)
 to Error or Failed when the executable you call returns an error. You can include error information in the report TestStand generates.

You can specify the working directory for the executable by configuring TestStand to use the file directory, the sequence file directory, the current directory for the process, or an absolute path. You can also use expressions to determine the working directory at run time.

Refer to the following TestStand support documents on the National Instruments website for more information about calling scripting languages in TestStand:

- Introduction to Scripting in Perl, Python, and Tcl
- Calling Scripting Languages from NI TestStand
- Advanced Scripting in Perl, Python, and Tcl

#### See Also

[Call Executable Step](call-executable-step.html)

[Call Executable Edit Tab](call-executable-edit-tabs.html)

[Step Settings Pane](step-settings-pane.html)

Parent topic:

Call Executable Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/capture-value-sweep-parameter-strategy.html language=enus -->
## TOPIC 03425: Capture Value Sweep Parameter Strategy

- bundle_id: `teststand-api-reference`
- source_path: `tsref/capture-value-sweep-parameter-strategy.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/capture-value-sweep-parameter-strategy.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Capture Value strategy with the Sweep Loop step to specify a sweep parameter whose value is determined elsewhere. Although the Sweep Loop does not specify or set the value of a parameter with the Capture Value strategy, the parameter value can still be logged if the output is enabled on the

### Capture Value Sweep Parameter Strategy

Use the Capture Value strategy with the
 [Sweep Loop](sweep-loop-step.html)
 step to specify a sweep parameter whose value is determined elsewhere. Although the Sweep Loop does not specify or set the value of a parameter with the Capture Value strategy, the parameter value can still be logged if the output is enabled on the Output tab.

The parameter value will also be included in the
 [Test Vector Table](test-vector-and-value-summary-table-view.html)
 . The value updates at execution time and can be exported to a CSV file from this table.

A parameter configured with the Capture Value strategy may be a number (any representation), string, Boolean, or enumeration.

Parent topic:

Sweep Parameter Strategies

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/case-edit-tab.html language=enus -->
## TOPIC 03426: Case Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/case-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/case-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Case edit tab in the TestStand Sequence Editor to configure the Case step. The Case edit tab contains the following options: Value to Compare —The expression the step evaluates and compares to the value the Select step specifies to determine whether it is the case within the surrounding Sele

### Case Edit Tab

Use the Case edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to configure the Case step.

The Case edit tab contains the following options:

- Value to Compare 
 —The expression the step evaluates and compares to the value the Select step specifies to determine whether it is the case within the surrounding Select block that executes. For string
 expressions 
 , the comparison is case-sensitive if you enable the
 Case Sensitive 
 option for the corresponding Select step. If the case expression evaluates to an array, the step also compares each element in the array to the value you specify in the Select step. Thus, you can use array literal syntax, such as
 {"Short", "Open", "Unknown"} 
 , to specify multiple matchable items in a single Case step.
- Default Case 
 —Specifies whether this step defines the default case for the surrounding Select block. If none of the Case steps have a Value to Compare expression that equals the Select step Item to Compare Expression, the default case executes. Only one Case step can be the default case for a Select block.
- Case Sensitive (for string values) 
 —Specifies whether to use a case-sensitive string comparison when the value for the step contains strings. The default value is
 OFF 
 , or case-insensitive.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Case Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/case-step.html language=enus -->
## TOPIC 03427: Case Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/case-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/case-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Case step to define a block of steps within a Select block that execute if the expression the Select step specifies evaluates to a certain value. Configuring the Step Use the Case edit tab in the TestStand Sequence Editor and the Configure Case dialog box in a TestStand User Interface to confi

### Case Step

Use a Case step to define a block of steps within a
 [Select](select-step.html)
 block that execute if the expression the Select step specifies evaluates to a certain value.

#### Configuring the Step

Use the
 [Case](case-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Case](configure-case-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Case step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Case step type defines the following step properties:

- Step.ItemExpr 
 —The expression that determines which Case block within the Select block executes.
- Step.IsDefault 
 —Specifies which step defines the default case for the surrounding Select block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

Parent topic:

Flow Control Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/check-remote-system-status-edit-tab.html language=enus -->
## TOPIC 03428: Check Remote System Status Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/check-remote-system-status-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/check-remote-system-status-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: To display the Check Remote System Status edit tab in the TestStand Sequence Editor , insert a Check Remote System Status step and select Check Remote System Status or Step Settings from the context menu. Use the Check Remote System Status edit tab to specify the remote system and the location to st

### Check Remote System Status Edit Tab

To display the Check Remote System Status edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 , insert a Check Remote System Status step and select
 Check Remote System Status
 or
 Step Settings
 from the context menu. Use the Check Remote System Status edit tab to specify the remote system and the location to store the result of the system check.

The Check Remote System Status edit tab contains the following options:

- Hostname 
 —The remote computer. Leave this option empty to use the local computer.
- Specify Remote Host by Expression 
 —Enable this option to specify that the Hostname control contains an expression the step evaluates at run time to determine the name of the remote host.
- Port Number 
 —The TCP/IP port number to use to connect to the remote system.
- Timeout (ms) 
 —The time, in milliseconds, to wait for a connection before timing out. A value of
 –1 
 indicates to wait indefinitely.
- Server Ready 
 —The location to store a Boolean value that indicates whether the remote system check passed. The default value is
 Step.Result.PassFail 
 .

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

Parent topic:

Check Remote System Status Step - LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/check-remote-system-status-step-configuration.html language=enus -->
## TOPIC 03429: Check Remote System Status Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/check-remote-system-status-step-configuration.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/check-remote-system-status-step-configuration.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Check Remote System Status in the context menu for the step or click Configure Check Remote System Status on the General tab of the Step Properties dialog box to launch the Check Remote System Status Step Configuration dialog box from a TestStand User Interface . Use this dialog box

### Check Remote System Status Step Configuration Dialog Box

Select
 Configure Check Remote System Status
 in the context menu for the step or click
 Configure Check Remote System Status
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Check Remote System Status Step Configuration dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to specify the remote system and the location to store the result of the system check.

The Check Remote System Status Step Configuration dialog box contains the following options:

- Hostname 
 —The remote computer. Leave this option empty to use the local computer.
- Specify Remote Host by Expression 
 —Enable this option to specify that the Hostname control contains an expression the step evaluates at run time to determine the name of the remote host.
- Port Number 
 —The TCP/IP port number to use to connect to the remote system.
- Timeout (ms) 
 —The time, in milliseconds, to wait for a connection before timing out. A value of
 –1 
 indicates to wait indefinitely.
- Server Check 
 —The location to store a Boolean value that indicates whether the remote system check passed. The default value is
 Step.Result.PassFail 
 .

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Check Remote System Status Step - LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/check-remote-system-status-step-labview-utili.html language=enus -->
## TOPIC 03430: Check Remote System Status Step - LabVIEW Utility Step Types

- bundle_id: `teststand-api-reference`
- source_path: `tsref/check-remote-system-status-step-labview-utili.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/check-remote-system-status-step-labview-utili.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Check Remote System Status Step Use a Check Remote System Status step to determine whether LabVIEW is running on a remote computer and whether TestStand can connect to the remote computer. Configuring the Step Use the Check Remote System Status edit tab in the TestStand Sequence Editor and the Check

### Check Remote System Status Step - LabVIEW Utility Step Types

#### Check Remote System Status Step

Use a Check Remote System Status step to determine whether LabVIEW is running on a remote computer and whether TestStand can connect to the remote computer.

#### Configuring the Step

Use the
 [Check Remote System Status](check-remote-system-status-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Check Remote System Status Step Configuration](check-remote-system-status-step-configuration.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify the remote system and the location to store the result of the system check.

#### Step Properties

In addition to the common custom properties, the Check Remote System Status step type defines the following step properties:

- Step.RemoteHost 
 —The computer name or IP address of the remote computer. The
 Step.RemoteHostByExpr 
 property specifies whether the step interprets this property value as an expression or as a string.
- Step.RemoteHostByExpr 
 —When this property is
 True 
 , the step interprets the
 Step.RemoteHost 
 property value as an expression. When this property is
 False 
 , the step interprets the value as a string.
- Step.PortNumber 
 —The remote host port number.
- Step.Timeout 
 —The number of seconds to wait to connect to the remote computer.
- Step.ServerCheckExpr 
 —Specifies where to store a Boolean value that indicates whether the remote computer check passed.

#### See Also

[Calling VIs on Remote Computers](/csh?context=ts_tslabview_remote)

[LabVIEW Utility Step Types](labview-utility-step-types.html)

Parent topic:

LabVIEW Utility Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/choose-code-template-dialog-box.html language=enus -->
## TOPIC 03431: Choose Code Template Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/choose-code-template-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/choose-code-template-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Create Code on the Source Code tab of the Specify Module dialog box to launch the Choose Code Template dialog box. TestStand only launches this dialog box when more than one code template is configured for the step type. The Choose Code Template dialog box contains a list control with the foll

### Choose Code Template Dialog Box

Click
 Create Code
 on the Source Code tab of the
 [Specify Module](specify-module-tabs-and-dialog-boxes.html)
 dialog box to launch the Choose Code Template dialog box. TestStand only launches this dialog box when more than one code template is configured for the step type.

The Choose Code Template dialog box contains a list control with the following columns:

- Description 
 —The description for the code template.
- Name 
 —The name of the code template.
- Show Legacy Templates in List 
 —Enable this option to show legacy templates in the list control.

The following options are also available when you select a legacy template:

- Optional Parameters for Legacy Templates 
 —Specifies which of the following optional parameters you want to include as input parameters for the VI:
  - Input Buffer 
 —An optional parameter you can wire to the connector pane of the VI. This option dims if the
 Step.InBuf 
 property does not exist for the step you are editing. For example, the Input Buffer control dims for an Action step.
  - Sequence Context ActiveX Pointer 
 —An optional parameter you can wire to the connector pane of the VI.
  - Invocation Info 
 —An optional parameter you can wire to the connector pane of the VI.

#### See Also

[LabVIEW Adapter Configuration dialog box](labview-adapter-configuration-dialog-box.html)

[Specify Module dialog box](specify-module-tabs-and-dialog-boxes.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/clear-operation-notification-settings-edit-ta.html language=enus -->
## TOPIC 03432: Clear Operation - Notification Settings Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/clear-operation-notification-settings-edit-ta.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/clear-operation-notification-settings-edit-ta.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clear Operation Use the Clear operation to clear the state of a notification so subsequent Wait operations block until the next Set operation. Enable the Clear option on the left of the Notification Settings panel. The Clear operation contains the following option: Notification Name or Reference Exp

### Clear Operation - Notification Settings Edit Tab

#### Clear Operation

Use the Clear operation to clear the state of a notification so subsequent Wait operations block until the next Set operation. Enable the
 Clear
 option on the left of the Notification Settings panel.

The Clear operation contains the following option:

- Notification Name or Reference Expression 
 —The notification on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.

Parent topic:

Notification Settings Edit Tab

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/clear-operation-notification-step-configurati.html language=enus -->
## TOPIC 03433: Clear Operation - Notification Step Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/clear-operation-notification-step-configurati.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/clear-operation-notification-step-configurati.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clear Operation Use the Clear operation to clear the state of a notification so subsequent Wait operations block until the next Set operation. The Clear operation contains the following option: Notification Name or Reference Expression —The notification on which to perform the operation. You can spe

### Clear Operation - Notification Step Configuration Dialog Box

#### Clear Operation

Use the Clear operation to clear the state of a notification so subsequent Wait operations block until the next Set operation.

The Clear operation contains the following option:

- Notification Name or Reference Expression 
 —The notification on which to perform the operation. You can specify the notification by name or by the object reference you receive when you create the notification using the Use Object Reference for the Notification Reference Lifetime option.

Parent topic:

Notification Step Configuration Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/close-all-windows-modified-files-dialog-box.html language=enus -->
## TOPIC 03434: Close All Windows Modified Files Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/close-all-windows-modified-files-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/close-all-windows-modified-files-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Close All Windows Modified Files dialog box when you attempt to close all windows without saving one or more modified files. Use this dialog box to select the files to save before closing all windows. The list control displays all modified files. Files for which you have permi

### Close All Windows Modified Files Dialog Box

TestStand launches the Close All Windows Modified Files dialog box when you attempt to close all windows without saving one or more modified files. Use this dialog box to select the files to save before closing all windows. The list control displays all modified files. Files for which you have permission to save are selected by default, and read-only files are not selected by default. Files for which you do not have permission to save are dimmed.

The Close All Windows Modified Files dialog box contains the following options:

- Save Checked Files 
 —TestStand saves the selected files and continues with closing all windows.
- Close without Saving 
 —TestStand does not save any files and continues with closing all windows.
- Cancel 
 —TestStand does save any files and does not close any windows.

#### See Also

[Logout Modified Files dialog box](logout-modified-files-dialog-box.html)

[Save All Modified Files dialog box](save-all-modified-files-dialog-box.html)

[Shutdown Modified Files dialog box](shutdown-modified-files-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/close-database-step.html language=enus -->
## TOPIC 03435: Close Database Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/close-database-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/close-database-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Close Database step to close the database handle you obtain from an Open Database step. You must call a Close Database step for open handles because TestStand does not automatically close open database handles. When you abort an execution, you must exit the application process that loaded the

### Close Database Step

Use a Close Database step to close the database handle you obtain from an
 [Open Database](open-database-step.html)
 step. You must call a Close Database step for open handles because TestStand does not automatically close open database handles.

When you abort an execution, you must exit the application process that loaded the TestStand Engine to guarantee that TestStand frees all database handles. Selecting
 File»Unload All Modules
 does not close the handles. National Instruments recommends placing Close Database steps in the
 [Cleanup step group](/csh?context=ts_tsfundamentals_bldgblocks_stepgroups)
 .

#### Configuring the Step

Use the
 [Edit Close Database](edit-close-database-dialog-box.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Close Database step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Close Database step type defines the
 Step.DatabaseHandle
 step property, which specifies the name of the numeric variable or property that contains the open database handle to close.

#### See Also

[Database Step Types](database-step-types.html)

Parent topic:

Database Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/close-operation-edit-ivi-tools-step-dialog-bo.html language=enus -->
## TOPIC 03436: Close Operation - Edit IVI Tools Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/close-operation-edit-ivi-tools-step-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/close-operation-edit-ivi-tools-step-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Close Operation The Close operation closes the IVI session for the specified logical name. Normally, the instrument session for a logical name automatically closes when the last execution to run an IVI step closes.

### Close Operation - Edit IVI Tools Step Dialog Box

#### Close Operation

The Close operation closes the IVI session for the specified logical name. Normally, the instrument session for a logical name automatically closes when the last execution to run an IVI step closes.

Parent topic:

Edit IVI Tools Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/close-sessions-edit-tab.html language=enus -->
## TOPIC 03437: Close Sessions Edit Tab

- bundle_id: `teststand-api-reference`
- source_path: `tsref/close-sessions-edit-tab.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/close-sessions-edit-tab.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Close Sessions edit tab in the TestStand Sequence Editor to specify which IO sessions you want to close. The Close Session edit tab contains the following options: Close All open Sessions —Automatically closes all sessions that are currently open in the executing sequence, including Locals,

### Close Sessions Edit Tab

Use the Close Sessions edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 to specify which IO sessions you want to close.

The Close Session edit tab contains the following options:

- Close All open Sessions 
 —Automatically closes all sessions that are currently open in the executing sequence, including Locals, Parameters, File Globals and Station Globals. The sessions close in the order the IO session variables were created in Locals, Parameters, File Globals and Station Globals. Use the Close Selected Sessions option to close the IO sessions in a specific order.
- Close Selected Sessions 
 —Closes the sessions you select. The IO sessions close in the order they are listed in the selected session list. You can choose an existing Create Session and Apply Configuration step, or specific IO session variables defined as Locals, Parameters, FileGlobals, or StationGlobals. Click
 Add/Modify Sessions 
 to add or modify sessions in the list. Click
 Remove Session 
 to remove the selected session from the list. Click
 Move Session Up 
 to move the currently selected session up, and click
 Move Session Down 
 to move the currently selected session down. Settings available for each IO session are:
  - Ignore Error 
 —Ignores any errors that occur while closing the session.
  - Session Variable 
 —The TestStand variable used to store the session.
  - Session Description 
 —The description about a session.

Parent topic:

Close Sessions Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/close-sessions-step.html language=enus -->
## TOPIC 03438: Close Sessions Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/close-sessions-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/close-sessions-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Close Sessions step to close currently open IO sessions. You can close all open IO sessions or close selected IO sessions. If you do not close IO sessions for instruments that are open in TestStand, you will be unable to use the instruments in other applications. Configuring the Step Use the C

### Close Sessions Step

Note

#### Configuring the Step

Use the
 [Close Sessions](close-sessions-edit-tab.html)
 edit tab in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 and the
 [Configure Close Sessions](configure-close-sessions-dialog-box.html)
 dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to specify which IO sessions you want to close.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Close Session step type defines the following step properties:

- Step.SessionList 
 —The session location where each session is stored and whether to ignore any errors encountered while closing session(s).

#### See Also

[Select Session dialog box](select-session-dialog-box.html)

Parent topic:

IO Configuration Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/close-sql-statement-step.html language=enus -->
## TOPIC 03439: Close SQL Statement Step

- bundle_id: `teststand-api-reference`
- source_path: `tsref/close-sql-statement-step.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/close-sql-statement-step.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use a Close SQL Statement step to close an SQL statement handle you obtain from an Open SQL Statement step. National Instruments recommends placing Close SQL Statement steps in the Cleanup step group . Configuring the Step Use the Edit Close SQL Statement dialog box in the TestStand Sequence Editor

### Close SQL Statement Step

Use a Close SQL Statement step to close an SQL statement handle you obtain from an
 [Open SQL Statement](open-sql-statement-step.html)
 step. National Instruments recommends placing Close SQL Statement steps in the
 [Cleanup step group](/csh?context=ts_tsfundamentals_bldgblocks_stepgroups)
 .

#### Configuring the Step

Use the
 [Edit Close SQL Statement](edit-close-sql-statement-dialog-box.html)
 dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 or in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to configure the Close SQL Statement step.

#### Step Properties

In addition to the
 [common custom properties](/csh?context=ts_tsfundamentals_custom_result_props)
 , the Close SQL Statement step type defines the
 Step.StatementHandle
 step property, which specifies the name of the numeric variable or property that contains the SQL statement handle to close.

#### See Also

[Database Step Types](database-step-types.html)

Parent topic:

Database Step Types

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/cluster-parameters-labview-nxg-vi-call-parame.html language=enus -->
## TOPIC 03440: Cluster Parameters - LabVIEW NXG VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/cluster-parameters-labview-nxg-vi-call-parame.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/cluster-parameters-labview-nxg-vi-call-parame.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Cluster Parameters When you configure calls to VIs that use clusters as parameters, you can specify that each cluster element maps to a different TestStand expression or that the entire LabVIEW NXG cluster maps to a TestStand data type. You can create a custom data type that matches a LabVIEW NXG cl

### Cluster Parameters - LabVIEW NXG VI Call Parameters

#### Cluster Parameters

When you configure calls to VIs that use clusters as parameters, you can specify that each cluster element maps to a different TestStand expression or that the entire LabVIEW NXG cluster maps to a TestStand data type.

You can
 [create a custom data type that matches a LabVIEW NXG cluster](/csh?context=ts_tsref_labview_cluster_params_existing)
 . When you create or edit a data type, you specify whether the type can be a cluster argument and how the properties of the type map to the cluster. The mapping is done between the cluster element label and the name of a property of the data type.

For input parameters, you can pass the default value for the entire cluster or the default values for specific elements of the cluster control on the front panel of the VI. For output parameters, you can optionally specify where TestStand stores the cluster value or specific elements of the cluster value.

The cluster mapping eliminates the need to specify an argument for each element of the cluster. You can create the new data type and the mapping to the cluster directly from the
 [LabVIEW NXG Module](labview-nxg-module-tab.html)
 or Module tab of the
 [Edit LabVIEW NXG VI Call](edit-labview-nxg-vi-call-dialog-box.html)
 dialog box by clicking the
 Create/Update Custom Data Type
 button in the Type column of the VI Parameter Table to launch the
 [Create/Update Custom Data Type from Cluster](create-update-custom-data-type-from-cluster-d.html)
 dialog box.

You can use the
 [Create/Update Custom Data Type from Cluster](create-update-custom-data-type-from-cluster-d.html)
 dialog box or the
 [Cluster Passing](cluster-passing-tab-type-properties-dialog-bo.html)
 tab in the
 [Type Properties](type-properties-dialog-box.html)
 dialog box to edit the cluster passing settings for an existing custom data type.

#### Passing Complex Arrays of Clusters

When you use several VIs with a complex array of clusters that is not used in TestStand, complete the following steps to use the
 LabVIEWClusterArray
 data type, which adapts to the array of clusters as needed.

1. Use the
 LabVIEWClusterArray 
 data type as an output expression that TestStand uses to adapt the data type to fit the array of clusters.
2. Pass the data type to the remaining VIs as an input.

#### Specifying Each Cluster Element Individually

To configure each cluster element individually, specify a different TestStand expression for each element of the cluster. The following figure shows a VI Parameter Table in which the data source for the
 Number
 element of the
 Input Cluster
 parameter is a local variable. TestStand passes the default value for the
 String
 element of the
 Input Cluster
 parameter.

[IMAGE alt='image' src='../images/cluster_individ.png']

#### See Also

[Create/Update Custom Data Type from Cluster Dialog Box](create-update-custom-data-type-from-cluster-d.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

Partially Specifying LabVIEW NXG Clusters

Passing a LabVIEW NXG Cluster to a VI (Example)

[Passing Existing TestStand Container Variables to LabVIEW](/csh?context=ts_tsref_labview_cluster_params_existing)

[Type Properties Dialog Box](type-properties-dialog-box.html)

[Updating Cluster Element Mapping](/csh?context=ts_tsref_labview_cluster_params_update)

Parent topic:

LabVIEW NXG Data Types in TestStand

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/cluster-parameters-labview-vi-call-parameters.html language=enus -->
## TOPIC 03441: Cluster Parameters - LabVIEW VI Call Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsref/cluster-parameters-labview-vi-call-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/cluster-parameters-labview-vi-call-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Cluster Parameters When you configure calls to VIs that use clusters as parameters, you can specify that each cluster element maps to a different TestStand expression or that the entire LabVIEW cluster maps to a TestStand data type. You can create a custom data type that matches a LabVIEW cluster .

### Cluster Parameters - LabVIEW VI Call Parameters

#### Cluster Parameters

When you configure calls to VIs that use clusters as parameters, you can specify that each cluster element maps to a different TestStand expression or that the entire LabVIEW cluster maps to a TestStand data type.

You can
 [create a custom data type that matches a LabVIEW cluster](/csh?context=ts_tsref_labview_cluster_params_existing)
 . When you create or edit a data type, you specify whether the type can be a cluster argument and how the properties of the type map to the cluster. The mapping is done between the cluster element label and the name of a property of the data type.

For input parameters, you can pass the default value for the entire cluster or the default values for specific elements of the cluster control on the front panel of the VI. For output parameters, you can optionally specify where TestStand stores the cluster value or specific elements of the cluster value.

Note

The mapping eliminates the need to specify an argument for each element of the cluster. You can create the new data type and the mapping to the cluster directly from the
 [LabVIEW Module](labview-module-tab.html)
 or
 [Module](module-tab-edit-labview-vi-call-dialog-box.html)
 tab of the
 [Edit LabVIEW VI Call](edit-labview-vi-call-dialog-box.html)
 dialog box by clicking the
 Create/Update Custom Data Type
 button in the Type column of the VI Parameter Table to launch the
 [Create/Update Custom Data Type from Cluster](create-update-custom-data-type-from-cluster-d.html)
 dialog box.

You can use the
 [Create/Update Custom Data Type from Cluster](create-update-custom-data-type-from-cluster-d.html)
 dialog box or the
 [Cluster Passing](cluster-passing-tab-type-properties-dialog-bo.html)
 tab in the
 [Type Properties](type-properties-dialog-box.html)
 dialog box to edit the cluster passing settings for an existing custom data type.

#### Passing Complex Arrays of Clusters

When you use several VIs with a complex array of clusters that is not used in TestStand, complete the following steps to use the LabVIEWClusterArray data type, which adapts to the array of clusters as needed.

1. Use the LabVIEWClusterArray data type as an output expression that TestStand uses to adapt the data type to fit the array of clusters.
2. Pass the data type to the remaining VIs as an input.

#### Specifying Each Cluster Element Individually

To configure each cluster element individually, specify a different TestStand expression for each element of the cluster. The following figure shows a VI Parameter Table in which the data source for the
Number element of the
 Input Cluster
 parameter is a local variable. TestStand passes the default value for the String element of the
 Input Cluster
 parameter.

[IMAGE alt='image' src='../images/cluster_individ.png']

#### See Also

[Create/Update Custom Data Type from Cluster dialog box](create-update-custom-data-type-from-cluster-d.html)

[Mapping Parameters](/csh?context=ts_tsref_parameters)

[Partially Specifying LabVIEW Clusters](/csh?context=ts_tslabview_cluster)

[Passing a LabVIEW Cluster to a VI (Example)](/csh?context=ts_8210)

[Passing Existing TestStand Container Variables to LabVIEW](/csh?context=ts_tsref_labview_cluster_params_existing)

[Type Properties dialog box](type-properties-dialog-box.html)

[Updating Cluster Element Mapping](/csh?context=ts_tsref_labview_cluster_params_update)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/cluster-passing-tab-type-properties-dialog-bo.html language=enus -->
## TOPIC 03442: Cluster Passing Tab - Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/cluster-passing-tab-type-properties-dialog-bo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/cluster-passing-tab-type-properties-dialog-bo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Cluster Passing Tab You can use the LabVIEW NXG Adapter to pass a TestStand variable or property to a cluster terminal on a VI connector pane. The data type of the variable or property you pass must contain all the fields the cluster expects. If a data type contains a subproperty that is a named dat

### Cluster Passing Tab - Type Properties Dialog Box

#### Cluster Passing Tab

You can use the
 [LabVIEW NXG Adapter](/csh?context=ts_tsref_labview)
 to pass a TestStand variable or property to a
 [cluster](cluster-parameters-labview-vi-call-parameters.html)
 terminal on a VI connector pane. The data type of the variable or property you pass must contain all the fields the cluster expects. If a data type contains a subproperty that is a named data type, you must also allow the LabVIEW NXG Adapter to pass objects of the named data type as a cluster.

Use the Cluster Passing tab to specify how TestStand maps the subproperties of a data type to the elements of a cluster parameter. The Cluster Passing tab contains the following options:

- Allow Objects of this Type to be Passed as LabVIEW NXG Clusters 
 —Enables you to pass instances of the data type to cluster parameters.
- Property 
 —Use this ring control to select a subproperty of the data type in order to display the type and specify the name of the cluster element to which TestStand maps the property.
 If a subproperty of the data type is a named type, the control does not include the subproperties of the type in the ring control. You must separately configure the named data type to allow the LabVIEW NXG Adapter to pass objects of the named type as a cluster, and specify the cluster elements to map.
- Exclude when Passing Cluster 
 —When you enable this option, TestStand does not include the selected subproperty in the mapping between the data type and cluster.
- Is Binary String 
 —Indicates whether the cluster element contains binary data. When you select this option, the LabVIEW NXG Adapter automatically compresses the binary string for output parameters and uncompresses the binary string for input parameters.
- Type 
 —The data type of the selected subproperty.
- Cluster Item Label 
 —The name of the cluster element to which TestStand maps the property.

#### See Also

[Cluster Parameters](cluster-parameters-labview-vi-call-parameters.html)

[Passing Existing TestStand Container Variables to LabVIEW NXG](cluster-parameters-labview-nxg-vi-call-parame.html)

[Updating Cluster Element Mapping](/csh?context=ts_tsref_labview_cluster_params_update)

Parent topic:

Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/code-template-parse-error-dialog-box.html language=enus -->
## TOPIC 03443: Code Template Parse Error Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/code-template-parse-error-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/code-template-parse-error-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: TestStand launches the Code Template Parse Error dialog box when you click Create Code on the Source Code tab of the Specify Module dialog box and TestStand cannot read the prototype of the code template. The Code Template Parse Error dialog box contains the following options: Use the Prototype from

### Code Template Parse Error Dialog Box

TestStand launches the Code Template Parse Error dialog box when you click
 Create Code
 on the Source Code tab of the Specify Module dialog box and TestStand cannot read the prototype of the code template.

The Code Template Parse Error dialog box contains the following options:

- Use the Prototype from the Module Tab 
 —TestStand uses the prototype the Module tab specifies.
- Use the Prototype from the Code Template 
 —TestStand uses the prototype the code template specifies.

#### See Also

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/code-templates-tab-step-type-properties-dialo.html language=enus -->
## TOPIC 03444: Code Templates Tab - Step Type Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/code-templates-tab-step-type-properties-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/code-templates-tab-step-type-properties-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Code Templates Tab Use the Code Template tab to associate one or more code templates with the step type. A code template is a set of source files that contain skeleton code to serve as a starting point for developing code modules for steps that use the step type. TestStand uses the code template whe

### Code Templates Tab - Step Type Properties Dialog Box

#### Code Templates Tab

Use the Code Template tab to associate one or more code templates with the step type. A code template is a set of source files that contain skeleton code to serve as a starting point for developing
 [code modules](/csh?context=ts_tsfundamentals_bldgblocks_codemodules)
 for steps that use the step type. TestStand uses the code template when you click
 Create Code
 on the Module tab of the
 [Step Settings](step-settings-pane.html)
 pane or the Source Code tab of the
 [Specify Module](specify-module-tabs-and-dialog-boxes.html)
 dialog box for a step.

You can use the default TestStand code template for any step type, and you can customize code templates for individual steps.

The listbox shows the code templates currently associated with the step type. The Description indicator displays the description string for the currently selected code template. The following command buttons appear to the right of the listbox:

- Create 
 —Launches the
 Create Code Templates 
 dialog box, in which you can create a new code template.
- Add 
 —Associates an existing code template with the step type. Click
 Add 
 to launch the
 Select Code Templates to Add to Step Type 
 dialog box, in which you can select from a list of code templates. TestStand generates the list from the set of subdirectories in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \CodeTemplates 
 and
 [<TestStand Public>](/csh?context=ts_tsfundamentals_directories)
 \CodeTemplates 
 directories. If you specify a code template that is not in the list, the code template subdirectory must be in the TestStand
 search directory paths 
 . Use the
 Edit Search Directories 
 dialog box to customize the search directory paths.
- Remove 
 —Disassociates the currently selected code template from the step type.
- Edit 
 —Launches the
 Edit Code Template 
 dialog box, in which you can modify properties of the currently selected code template.
- Move Up 
 and
 Move Down 
 —Changes the order of the items in the code template list. The order of the code templates in the listbox is the same order TestStand uses to display the code templates in the
 Choose Code Template 
 dialog box.

#### See Also

[Choose Code Template dialog box](choose-code-template-dialog-box.html)

[Create Code Templates dialog box](create-code-templates-dialog-box.html)

[Creating and Customizing Code Template Files](/csh?context=ts_tsfundamentals_template_files_create_customize)

[Edit Code Template dialog box](edit-code-template-dialog-box.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Module Tabs and Specify Module Dialog Boxes](specify-module-tabs-and-dialog-boxes.html)

[Multiple Code Templates Per Step Type](/csh?context=ts_tsfundamentals_code_templates_multiple)

[Select Code Templates to Add to Step Type dialog box](select-code-templates-to-add-to-step-type-dia.html)

[Step Settings Pane](step-settings-pane.html)

[Template Files for Different Development Environments](/csh?context=ts_tsfundamentals_template_files_dev_env)

Parent topic:

Step Type Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/column-parameter-values-tab-edit-data-operati.html language=enus -->
## TOPIC 03445: Column/Parameter Values Tab - Edit Data Operation Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/column-parameter-values-tab-edit-data-operati.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/column-parameter-values-tab-edit-data-operati.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Column/Parameter Values Tab The Column/Parameter Values tab of the Edit Data Operations dialog box applies only to Get, Set, Set and Put, Execute, and Close operations you perform in a Data Operation step. You can use the Column/Parameter Values tab to specify the mapping between SQL columns and Tes

### Column/Parameter Values Tab - Edit Data Operation Dialog Box

#### Column/Parameter Values Tab

The Column/Parameter Values tab of the Edit Data Operations dialog box applies only to Get, Set, Set and Put, Execute, and Close operations you perform in a Data Operation step. You can use the Column/Parameter Values tab to specify the mapping between SQL columns and TestStand variables and properties.

- For a Get operation, a mapping between a column and variable or property instructs TestStand to assign the column value to the variable or property.
- For a Set operation, a mapping between a column and a variable or property instructs TestStand to assign the value of the variable or property to the column.
- For an Execute operation, a mapping between a parameter and a variable or property instructs TestStand to create the parameter and assign the value of the variable or property to the parameter.
- For a Close operation, a mapping between a parameter and a variable or property instructs TestStand to assign the parameter to the variable or property.

The Column List Source control on the
 [Record/Operation](record-operation-tab-edit-data-operation-dial.html)
 tab specifies a variable or property that stores this mapping.

The Column/Parameter Values tab contains the following options:

- Data Link Name 
 —The name of a data link to open and query. The Edit Data Operations dialog box uses the data link to populate the ring control that contains column names. Click
 Select Data Link 
 to select a
 predefined data link 
 in the
 Select Data Link 
 dialog box.
- SQL Statement 
 —The SQL Statement the Edit Data Operations dialog box uses to populate the ring control that contains column names. The SQL Statement ring control contains a list of the Open SQL Statement steps in the current sequence file. TestStand can populate the Name/Number ring control only when the selected SQL statement step uses a literal string or a valid expression.
- Values 
 —The mappings of column names to variables or properties. The list control displays the mappings. The Name/Number, Values, and Format String controls specify the settings for the currently selected mapping. Use the
 New 
 ,
 Cut 
 ,
 Copy 
 , and
 Paste 
 buttons to create a new item in the list, remove items from the list, and rearrange the items in the list. Use the
 Expression Browse 
 button to launch the
 Expression Browser 
 dialog box.
 The Values section contains the following options:
  - Name/Number 
 —A valid expression TestStand evaluates at run time. Enter a one-based number without surrounding quotes to refer to a column by the order of the column in the SQL statement.
  - Direction 
 —Defines the parameter information the Execute operation uses to create parameters. A parameter direction can be In, Out, In/Out, or a return value. This option is available only when you perform an Execute operation.
  - Type 
 —Defines the data type of the parameter in the database. The data type of a parameter can be String, Number, Boolean, or Date/Time. You must specify a Format String value when the data type is Date/Time. This option is available only when you perform an Execute operation.
  - Size 
 —The maximum size for a String parameter. This option is available only when you perform an Execute operation.
  - Value 
 —A valid expression TestStand evaluates at run time. When the Data Operation step performs a Get or Close operation, the Value control must contain the name of a variable or property. When the Data Operation step performs a Set or Execute operation, the Value Control can contain a literal value or an expression TestStand evaluates at run time.
    - Convert Null to Default Value 
 —Specifies to store an empty string value, zero numeric value, or
 False 
 Boolean value when the step performs a Get operation and the column value is
 NULL 
 . The option is available only when you perform a Get or Close operation.
    - Write Null 
 —TestStand stores
 NULL 
 for the column value when the step performs a Set operation. This option is available only when you perform a Set, Set and Put, or Execute operation.
  - Format String 
 —Specifies how to convert a string value when assigning a string expression to a column or when assigning the value of a column to a string variable or property. Use this control when getting or setting data from a column that is of the date-time or currency type.

Note

#### See Also

[Data Link Properties dialog box](data-link-properties-dialog-box.html)

[Expression Browser dialog box](expression-browser-dialog-box.html)

[Format Strings for Database Date Values](/csh?context=ts_tsfundamentals_strings_format)

[Select Data Link dialog box](select-data-link-dialog-box.html)

Parent topic:

Edit Data Operation Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/columns-tab-configuration-properties-dialog-b.html language=enus -->
## TOPIC 03446: Columns Tab - Configuration Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/columns-tab-configuration-properties-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/columns-tab-configuration-properties-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Columns Tab The Columns tab contains the following options, which you can use to configure the columns on the Steps pane: When you configure columns, you must provide a unique column name for each column on the Steps pane. Column List —List of columns on the Steps pane. Add —Adds a new column and as

### Columns Tab - Configuration Properties Dialog Box

#### Columns Tab

The Columns tab contains the following options, which you can use to configure the columns on the
 [Steps](steps-pane-sequence-file-window.html)
 pane:

Note

- Column List 
 —List of columns on the Steps pane.
  - Add 
 —Adds a new column and assigns it a unique default name.
  - Remove 
 —Deletes the currently selected column.
  - Up 
 —Moves the currently selected column up one position.
  - Down 
 —Moves the currently selected column down one position.
- Column Properties 
 —These options apply to the currently selected column in the column list.
  - Caption 
 —The caption of the currently selected column.
 If the caption is a resource string tag in the string section the application uses to
 [localize the control](/csh?context=ts_tsfundamentals_localization)
 , the localized string replaces the caption at run time. Refer to the
 [SequenceView.Localize](../tsuiref/sequenceview-localize.html)
 method and the
 [ApplicationMgr.LocalizeAllControls](../tsuiref/applicationmgr-localizeallcontrols.html)
 method for more information about localizing captions. 
 Note 
 The
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 localizes the captions on the Steps pane using the TSUI_STEPLIST_CONFIGURATIONS string section.
  - Type 
 —The type of the column. The available column types are Name, Index, Description, Execution Flow, Status, and Expression.
  - Width 
 —The horizontal size of the column in pixels.
  - Autosize 
 —When you enable this option, the width of the column adjusts to fill the control when the size of the control changes. This option is enabled only when you select the
 Make Columns Always Fit 
 option on the
 Appearance 
 tab of the
 Configuration Properties 
 dialog box.
  - Visible 
 —When you disable this option, the column becomes invisible.
  - Expression 
 —Defines an expression TestStand evaluates for each step at run time. TestStand places the result of the expression you define in the column.
 Note 
 This property has no effect unless the column type is set to Expression.
  - Text Color Expression 
 —An expression that returns a
 numeric color value 
 . The column evaluates the expression at run time to determine the column text color. If the expression returns
 -1 
 , the column uses the default color specified in the Step Names option on the
 Fonts and Colors 
 tab.
  - Background Color Expression 
 —An expression that returns a
 numeric color value 
 . The column evaluates the expression at run time to determine the column background color. If the expression returns
 -1 
 , the column uses the default color specified in the Background option on the
 Fonts and Colors 
 tab.

#### See Also

[ApplicationMgr.LocalizeAllControls](../tsuiref/applicationmgr-localizeallcontrols.html)

[Color](../tsapiref/color.html)

[Configuration Properties dialog box](configuration-properties-dialog-box.html)

[SequenceView.Localize](../tsuiref/sequenceview-localize.html)

Parent topic:

Configuration Properties Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/command-line-arguments.html language=enus -->
## TOPIC 03447: Command Line Arguments

- bundle_id: `teststand-api-reference`
- source_path: `tsref/command-line-arguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/command-line-arguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following syntax when writing command line arguments for the Database Viewer application: DatabaseView.exe [-env environmentfilepath][-connectionstring connectionstringvalue][-connectionfile connectionfilepath][-connectionname name][-sqlfile sqlfilepath][-useexisting] The Database Viewer app

### Command Line Arguments

Use the following syntax when writing command line arguments for the
 [Database Viewer](database-viewer-application.html)
 application:

DatabaseView.exe [-env environmentfilepath][-connectionstring connectionstringvalue][-connectionfile connectionfilepath][-connectionname name][-sqlfile sqlfilepath][-useexisting]

The Database Viewer application supports the following command line options:

- -env 
 —Specify the path to a
 .tsenv 
 file following this flag. Use the
 .tsenv 
 file that defines the environment in which you want to launch the Database Viewer application. Click
 here 
 for more information about
 .tsenv 
 files and
 here 
 for more information about choosing an evironment with the
 -env 
 command line switch.
- -connectionstring 
 —Specify a connection string value following this flag to launch the Database Viewer and open the connection.
- -connectionfile 
 —Specify the path to a
 .udl, .accdb, .mdb, or .dbf 
 file following this flag. The Database Viewer will open the connection specified by the file.
 Note 
 Use only one of the
 -connectionstring
 or
 -connectionfile
 flags at a time.
- -connectionname 
 —Specify a name for the connection following this flag. If you use the
 -connectionstring 
 or
 -connectionfile 
 flags and provide no connection name, the Database Viewer will generate a unique name for the connection.
- -sqlfilepath 
 —Specify the path of the .sql file you want to open following this flag. Always use this option in conjunction with the
 -connectionstring 
 or
 connectionfile 
 flags. The Database Viewer creates a new
 Execute SQL Tab 
 and pastes the SQL commands present in the .sql file into the SQL editor. You can execute the commands against the connection specified in the command line argument.
- -useexisting 
 —Use this flag to reuse an already-running instance of the Database Viewer, rather than launch a new instance.
 Note 
 If a connection that matches the connection specified by the
 -connectionstring
 or
 -connectionfile
 flags is already open in an existing instance of the Database Viewer, that instance of the connection is reused. The application switches to this connection in the Connection List. A balloon appears near the Connection List to indicate that an existing connection is being reused.

#### See Also

[Configuring Connection Strings](/csh?context=ts_tsref_dbviewer_connectionstrings)

Parent topic:

Database Viewer Application

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configuration-properties-dialog-box.html language=enus -->
## TOPIC 03448: Configuration Properties Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configuration-properties-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configuration-properties-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Double-click on a configuration name or click Edit in the Edit Step List Configurations dialog box to launch the Configuration Properties dialog box, in which you can edit the configuration you select in the Edit Step List Configurations dialog box. The Configuration Properties dialog box contains t

### Configuration Properties Dialog Box

Double-click on a configuration name or click
 Edit
 in the
 [Edit Step List Configurations](edit-step-list-configurations-dialog-box.html)
 dialog box to launch the Configuration Properties dialog box, in which you can edit the configuration you select in the Edit Step List Configurations dialog box.

The Configuration Properties dialog box contains the following tabs:

- Appearance 
 –Configures the appearance of the step list, including grid lines, indenting, shading and headers.
- Fonts and Colors 
 –Configures the font, color, comment columns, and the header text for the step.
- Columns 
 –Configures the columns in the step list.

#### See Also

[Edit Step List Configurations dialog box](edit-step-list-configurations-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configuration-vi-passwords-to-use-dialog-box.html language=enus -->
## TOPIC 03449: Configuration VI Passwords To Use Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configuration-vi-passwords-to-use-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configuration-vi-passwords-to-use-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click Passwords on the Files To Update tab of the Update VI Calls dialog box to launch the Configuration VI Passwords To Use dialog box. This dialog box gives TestStand the passwords for configuration VIs you protected so TestStand can unlock and use the VIs. These passwords are required to run the

### Configuration VI Passwords To Use Dialog Box

Click
 Passwords
 on the
 [Files To Update](files-to-update-tab-update-vi-calls-dialog-bo.html)
 tab of the
 [Update VI Calls](update-vi-lv-nxg-vi-calls-dialog-box.html)
 dialog box to launch the Configuration VI Passwords To Use dialog box. This dialog box gives TestStand the passwords for configuration VIs you protected so TestStand can unlock and use the VIs. These passwords are required to run the Update VI Calls tool.

The Configuration VI Passwords To Use dialog box contains the following options:

- Password 
 —A configuration VI password.
- Add 
 —Adds the password you specify in the Password field.
- Delete 
 —Deletes the password you select.

#### See Also

[Update VI Calls dialog box](update-vi-lv-nxg-vi-calls-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-apply-configuration-dialog-box.html language=enus -->
## TOPIC 03450: Configure Apply Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-apply-configuration-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-apply-configuration-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In a TestStand User Interface , select Configure Apply Configurations in the context menu for the step, or click Configure Apply Configurations on the General tab of the Step Properties dialog box to launch the Configure Apply Configurations dialog box. Use this dialog box to specify which configura

### Configure Apply Configuration Dialog Box

In a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select Configure Apply Configurations in the context menu for the step, or click Configure Apply Configurations on the General tab of the Step Properties dialog box to launch the Configure Apply Configurations dialog box. Use this dialog box to specify which configuration to apply to a particular IO session.

The Configure Apply Configuration dialog box contains the following options:

- IO Configuration 
 —The name of the IO Configuration that is applied to IO sessions. 
 Use the dropdown menu to select from one of the exported configurations. Click
 Edit IO Configuration 
 to edit the selected IO configuration. Expand the selected IO configuration to view all the IO sessions contained within the configuration. The right pane displays additional information about the selected IO configuration and IO session, including a read-only list of instrument attributes. 
 You can modify settings for each IO session using the following controls:
  - Logical Names 
 —The logical name of the IO session.
 Note 
 The logical names of IO sessions are not editable.
  - Session Description 
 —The description about the session.
 Note 
 The session description is not editable.
  - Session Variable 
 —The TestStand variable used to store the IO session.

Parent topic:

Apply Configuration Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-auto-schedule-step-dialog-box.html language=enus -->
## TOPIC 03451: Configure Auto Schedule Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-auto-schedule-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-auto-schedule-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Auto Schedule in the context menu for the step to launch the Configure Auto Schedule Step dialog box from a TestStand User Interface . You can also click Configure Auto Schedule on the General tab of the Step Properties dialog box. The Configure Auto Schedule Step dialog box contain

### Configure Auto Schedule Step Dialog Box

Select
 Configure Auto Schedule
 in the context menu for the step to launch the Configure Auto Schedule Step dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 . You can also click
 Configure Auto Schedule
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box.

The Configure Auto Schedule Step dialog box contains the following options:

- Timeout Enabled, Timeout Expression, Timeout Causes Run-Time Error 
 —The timeout behavior TestStand uses when no Use Auto Scheduled Resource blocks within the Auto Schedule block can acquire the required resource locks. If a timeout occurs, the
 Step.Result.TimeoutOccurred 
 property is set to
 True 
 .
- Display Execution Scheduling Information in Step Description 
 —When you enable this option, TestStand displays information in the Execution window of the
 TestStand Sequence Editor 
 or a
 TestStand User Interface 
 about the scheduling of the execution of the various Use Auto Scheduled Resource blocks within the Auto Schedule block.

#### See Also

[Step Properties dialog box](step-properties-dialog-box.html)

[Synchronization Step Types](synchronization-step-types.html)

Parent topic:

Auto Schedule Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-call-executable-dialog-box.html language=enus -->
## TOPIC 03452: Configure Call Executable Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-call-executable-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-call-executable-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Call Executable in the context menu for the step or click Configure Call Executable on the General tab of the Step Properties dialog box to launch the Configure Call Executable dialog box from a TestStand User Interface . You can also use the Configure Call Executable dialog box to

### Configure Call Executable Dialog Box

Select
 Configure Call Executable
 in the context menu for the step or click
 Configure Call Executable
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure Call Executable dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

You can also use the Configure Call Executable dialog box to configure a Sequence Call step for
 [calling scripting languages from TestStand](calling-scripting-languages-from-teststand.html)
 .

Use this dialog box to specify the following options for the Call Executable step.

- File Pathname 
 —Absolute or relative pathname for the executable or file the step calls. The step launches non-executable files using a system associated executable, if defined.
- Specify File Path by Expression 
 —Enable this option to specify that the file pathname is an expression the step evaluates at run time.
- Argument Expression 
 —An expression that the step evaluates at run time to determine the arguments to pass to the executable. The step appends arguments after a non-executable file pathname when performing a call using a system associated executable.
- Working Directory 
 —A working directory for the executable that the step calls. The ring control contains the following options:
  - Use File Directory 
 —The directory of the file that the step calls.
  - Use Sequence File Directory 
 —The directory of the sequence file for the step. This option is not available when calling executables on remote computers.
  - Use Current Working Directory 
 —The current directory of the TestStand process at the time of the call.
- Working Directory Path 
 —An absolute path to use as the working directory. This control is available only when you select
 Specific Directory 
 in the Working Directory control.
- Specific Directory 
 —The directory the Working Directory path specifies.
- Specify Working Directory by Expression 
 —Enable this option to specify that the working directory path is an expression the step evaluates at run time.
- Initial Window State 
 —Specifies whether the step launches the executable as a hidden, normal, minimized, or maximized application, and whether the application is active initially.
- Remote Settings 
 —Launches the
 Remote Settings 
 window, which specifies whether the step performs the call on a remote computer.

The Configure Call Executable dialog box contains the following tabs:

- Wait Options Tab 
 —Specifies whether the step waits for the call to complete, and specifies additional actions to perform based on the exit code from the call.
- Standard Input Tab 
 —The standard input the step passes to the call. You must configure the step to wait for the call to use this tab.
- Standard Output/Error Tab 
 —Specifies where the step stores the standard output and errors from the call. You must configure the step to wait for the call to use this tab.

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Calling Scripting Languages from TestStand](calling-scripting-languages-from-teststand.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Call Executable Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-case-dialog-box.html language=enus -->
## TOPIC 03453: Configure Case Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-case-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-case-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Case in the context menu for the step or click Configure Case on the General tab of the Step Properties dialog box to launch the Configure Case dialog box from a TestStand User Interface . The Configure Case dialog box contains the following options: Value to Compare —The expression

### Configure Case Dialog Box

Select
 Configure Case
 in the context menu for the step or click
 Configure Case
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure Case dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure Case dialog box contains the following options:

- Value to Compare 
 —The expression the step evaluates and compares to the value the Select step specifies to determine whether it is the case within the surrounding Select block that executes. For string
 expressions 
 the comparison is case insensitive.
- Default Case 
 —When you enable this option, this step defines the default case for the surrounding Select block. If none of the Case steps have a Value to Compare expression that equals the Select step Item to Compare Expression, the default case executes. Only one Case step can be the default case for a Select block.
- Case Sensitive (for string values) 
 —Specifies whether to use a case-sensitive string comparison when the value for the step contains strings. The default value is
 OFF 
 , or case-insensitive.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Case Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-close-sessions-dialog-box.html language=enus -->
## TOPIC 03454: Configure Close Sessions Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-close-sessions-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-close-sessions-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In a TestStand User Interface , select Configure Close Session in the context menu for the step, or click Configure Close Session on the General tab of the Step Properties dialog box to launch the Configure Close Session dialog box. Use this dialog box to specify which IO sessions you want to close.

### Configure Close Sessions Dialog Box

In a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select Configure Close Session in the context menu for the step, or click Configure Close Session on the General tab of the Step Properties dialog box to launch the Configure Close Session dialog box. Use this dialog box to specify which IO sessions you want to close.

The Configure Close Sessions dialog box contains the following options:

- Close All open Sessions 
 —Automatically closes all sessions that are currently open in the executing sequence, including Locals, Parameters, File Globals and Station Globals. The sessions close in the order the IO session variables were created in Locals, Parameters, File Globals and Station Globals. Use the Close Selected Sessions option to close the IO sessions in a specific order.
- Close Selected Sessions 
 —Closes the sessions you select. The IO sessions close in the order they are listed in the selected session list. You can choose an existing Create Session and Apply Configuration step, or specific IO session variables defined as Locals, Parameters, FileGlobals, or StationGlobals. Click
 Add/Modify Sessions 
 to add or modify sessions in the list. Click
 Remove Session 
 to remove the selected session from the list. Click
 Move Session Up 
 to move the currently selected session up, and click
 Move Session Down 
 to move the currently selected session down. Settings available for each IO session are:
  - Ignore Error 
 —Ignores any errors that occur while closing the session.
  - Session Variable 
 —The TestStand variable used to store the session.
  - Session Description 
 —The description about a session.

Parent topic:

Close Sessions Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-create-sessions-and-apply-configura.html language=enus -->
## TOPIC 03455: Configure Create Sessions and Apply Configuration Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-create-sessions-and-apply-configura.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-create-sessions-and-apply-configura.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In a TestStand User Interface , select Configure Create Sessions and Apply Configurations in the context menu for the step, or click Configure Create Sessions and Apply Configurations on the General tab of the Step Properties dialog box to launch the Create Sessions and Apply Configurations Step Con

### Configure Create Sessions and Apply Configuration Dialog Box

In a
 [TestStand User Interface](teststand-user-interfaces.html)
 , select Configure Create Sessions and Apply Configurations in the context menu for the step, or click Configure Create Sessions and Apply Configurations on the General tab of the Step Properties dialog box to launch the Create Sessions and Apply Configurations Step Configuration dialog box. 
Use this dialog box select the IO configuration, create IO sessions associated with the selected IO configuration, and then apply the selected configuration to those IO sessions.

The Configure Create Session and Apply Configuration dialog box contains the following options:

- Adapter 
 —Specifies the adapter to use to create the IO sessions.
- IO Configuration 
 —The name of the of IO Configuration that defines the names and number of IO sessions created, and that applies to the IO sessions. 
 Use the dropdown menu to select from one of the exported configurations. Selecting an IO configuration automatically creates the TestStand variables required to store the IO sessions for that configuration. This operation also deletes unused IO session variables used by the previous IO Configuration. Click
 Edit IO Configuration 
 to edit the selected IO configuration and view all the IO sessions contained within the configuration. The right pane displays additional information about the selected IO configuration and IO session, including a read-only list of instrument attributes. 
 You can modify settings for each IO session using the following controls:
  - Logical Names 
 —The logical name of the IO session.
 Note 
 The logical names of IO sessions are not editable.
  - Description 
 —The description about the session.
 Note 
 The session description is not editable.
  - Session Variable 
 —The TestStand variable used to store the IO session.

Parent topic:

Create sessions and Apply Configuration Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-data-collection-dialog-box.html language=enus -->
## TOPIC 03456: Configure Data Collection Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-data-collection-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-data-collection-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Data Collection Dialog Box Use the Configure Data Collection dialog to prevent the profiler from collecting information you do not need in order to increase execution speed and reduce memory consumption. The dialog contains the following controls: Locations —Specifies whether the profiler

### Configure Data Collection Dialog Box

#### Configure Data Collection Dialog Box

Use the Configure Data Collection dialog to prevent the profiler from collecting information you do not need in order to increase execution speed and reduce memory consumption. The dialog contains the following controls:

- Locations 
 —Specifies whether the profiler records locations that originate event so that you can navigate from events, operations, and items to the corresponding locations in sequence files and executions. Disabling this option can significantly improve speed and reduce memory usage. In particular, avoiding the overhead of storing location information can increase the accuracy of profiler times for operations that are very short.
- Process Models 
 —Specifies whether the profiler collects events that originate from process models. To significantly reduce memory usage and improve speed, do not enable this option unless you want to debug or inspect the operations of a process model.
- Synchronization 
 —Specifies whether the profiler records events from synchronization operations, such as Locks, Waits, Auto Scheduling, Queues, Rendezvous, Notifications, Batch Synchronization, and Semaphores.
- Steps 
 —Specifies whether the profiler records the duration of each step.
- Step Modules 
 —Specifies whether the profiler records the duration of each step module.
- Step Type Modules 
 —Specifies whether the profiler records the duration of each step type substep module.
- Module Loading 
 —Specifies whether the profiler records the duration of each module load.
- Module Unloading 
 —Specifies whether the profiler records the duration of each module unload.
- Module Paths and Environments 
 —Specifies whether the Operations Table populates the Module Path and Module Environment columns with the path to the code module and with information about the module execution environment that might affect performance.
- Module Inputs 
 —Specifies whether the Operations Table populates the Module Inputs and Outputs column with module input values.
- Module Outputs 
 —Specifies whether the Operations Table populates the Module Inputs and Outputs column with module output values.
- Limit Module Input/Output Text Length 
 —If enabled, the numeric control specifies the maximum text size per row of the Module Inputs and Outputs column.
- Module Adapters 
 —Displays a list containing a checkbox for each module adapter. Each checkbox specifies whether the profiler records load, unload, and execution durations for the modules that the adapter calls.
- Limit the Number of Retained Events 
 —If enabled, the profiler periodically discards the oldest events it has collected if the number of events collected exceeds the specified limit. You can use this option to ensure that profiling continues indefinitely without excessively slowing execution or running out of memory.
- Limit the Duration of the Profile in Seconds 
 —If enabled, the profiler periodically discards the events it has collected that are older than the specified duration. You can use this option to ensure that profiling continues indefinitely without excessively slowing execution or running out of memory.
- Specify a text file to log operations as they complete 
 —Specifies the path to a tab delimited text file in which the profiler logs operations as they complete.
  - Browse for File 
 —Launches the Select File dialog box in which you select a log file.
  - View File 
 —Opens the specified text file in the default viewer application.
  - Create File/Clear File Contents 
 —Creates or clears the log file and populates it with the appropriate headers.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-default-additional-results-dialog-b.html language=enus -->
## TOPIC 03457: Configure Default Additional Results Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-default-additional-results-dialog-b.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-default-additional-results-dialog-b.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Default Additional Results from the context menu for the Advanced button on the General tab of the Step Type Properties dialog box to launch the Configure Default Additional Results dialog box. Use this dialog box to configure the initial additional results for new steps you create from the s

### Configure Default Additional Results Dialog Box

Select
 Default Additional Results
 from the context menu for the
 Advanced
 button on the
 [General](general-tab-step-type-properties-dialog-box.html)
 tab of the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box to launch the Configure Default Additional Results dialog box.

Note

- TestStand uses the values in this dialog box as the initial values for new steps you create. Changes to these values do not automatically propagate to existing steps of this type. Enable the
 Apply Changes in this Dialog Box to all Loaded Steps of this Type 
 option in the Step Type Properties Dialog Box to apply the changes to all instances of the step type currently in memory. Enabling this option does not update instances of the step type in files not currently loaded.
- This dialog box and the
 Default Run Options 
 ,
 Default Post Actions 
 ,
 Default Loop Options 
 ,
 Default Expressions 
 ,
 Default Switching 
 , and
 Default Synchronization 
 tabs of the Step Type Properties dialog box display instance properties. This dialog box and these tabs have the same appearance and behavior as the
 Additional Results 
 dialog box and the Run Options, Loop Options, Expressions, and Synchronization tabs on the
 Properties 
 tab of the
 Step Settings 
 pane or in the
 Step Properties 
 dialog box for a step instance.

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

[Step Settings Pane](step-settings-pane.html)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-do-while-loop-dialog-box.html language=enus -->
## TOPIC 03458: Configure Do While Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-do-while-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-do-while-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Do While Loop in the context menu for the step or click Configure Do While Loop on the General tab of the Step Properties dialog box to launch the Configure Do While Loop dialog box from a TestStand User Interface . The Configure Do While Loop dialog box contains the following optio

### Configure Do While Loop Dialog Box

Select
 Configure Do While Loop
 in the context menu for the step or click
 Configure Do While Loop
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure Do While Loop dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure Do While Loop dialog box contains the following option:

- Loop Condition 
 —The expression the step evaluates before executing steps within the block after they have executed once. If the expression evaluates to
 True 
 , execution proceeds to the first step in the block. If the expression evaluates to
 False 
 , the loop ends and execution proceeds to the End step for the While block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Do While Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-else-if-condition-dialog-box.html language=enus -->
## TOPIC 03459: Configure Else If Condition Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-else-if-condition-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-else-if-condition-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Else If Condition in the context menu for the step or click Configure Else If Condition on the General tab of the Step Properties dialog box to launch the Configure Else If Condition dialog box from a TestStand User Interface . The Configure Else If Condition dialog box contains the

### Configure Else If Condition Dialog Box

Select
 Configure Else If Condition
 in the context menu for the step or click
 Configure Else If Condition
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure Else If Condition dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure Else If Condition dialog box contains the following options:

- Conditional Expression 
 —The expression that must evaluate to
 True 
 for the steps within the Else If block to execute. If the expression evaluates to
 False 
 , the execution proceeds to the next Else If, Else, or End step for the If block.
- Condition Builder 
 —Launches the
 Condition Builder 
 dialog box, in which you can build conditional
 expressions 
 that refer to the execution statuses of other steps.

#### See Also

[Condition Builder dialog box](preconditions-dialog-box.html)

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Else If Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-environment-dialog-box.html language=enus -->
## TOPIC 03460: Configure Environment Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-environment-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-environment-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: In the TestStand Sequence Editor, select Configure»Environment to launch the Configure Environment dialog box. The Configure Environment dialog box serves as an editor that you can use to create and edit TestStand environments . Environment Path —Specify the path to the environment configuration ( .

### Configure Environment Dialog Box

In the TestStand Sequence Editor, select
 Configure»Environment
 to launch the Configure Environment dialog box. The Configure Environment dialog box serves as an editor that you can use to create and edit
 [TestStand environments](/csh?context=ts_tsfundamentals_tsenv)
 .

- Environment Path 
 —Specify the path to the environment configuration (
 .tsenv 
 ) file that you wish to inspect, create, or modify. Specify
 <Global> 
 to specify the global environment. You can browse for an environment file by pressing the browse button next to the text entry field. You can also select the global environment or the path to the current environment (if not the global environment) from the drop down menu.
- Save 
 —Save the current settings to the specified file. The save button is disabled if you have made no changes or have specified the global environment. The global environment cannot be modified.
- Save As 
 —Copy the settings specified in the current environment configuration to a new environment configuration (
 .tsenv 
 ) file.
- Load 
 —Load the configuration of specified environment. The load button is disabled if you have not made any changes to the currently specified environment. (Note: Loading an environment file in the Configure Environment dialog only loads the file for viewing and editing. Loading does not change the environment in which the application is currently running. To run the application in a new environment, use the Set Engine Environment button.)
- Custom Directories 
 —Select the directories your environment overrides by checking the desired CommonAppData, Public, and/or LocalAppData check boxes. Specify the paths by entering them in the text fields or browse to them using the browse buttons.
- Help 
 —Get help for this dialog.
- Set Engine Environment 
 —Exit the current application and relaunch in the selected environment. This button is disabled if you have unsaved changes to the currently selected environment.
- Close 
 —Exit the Configure Environment dialog.

Note

.tsenv

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-external-viewers-dialog-box.html language=enus -->
## TOPIC 03461: Configure External Viewers Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-external-viewers-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-external-viewers-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure»External Viewers to launch the Configure External Viewers dialog box, in which you can specify both the external viewer, such as Microsoft Notepad or Microsoft Edge, and the report format, such as text ( .txt ), or HTML ( .html ) files. The Configure External Viewers dialog box cont

### Configure External Viewers Dialog Box

Select
 Configure»External Viewers
 to launch the Configure External Viewers dialog box, in which you can specify both the external viewer, such as Microsoft Notepad or Microsoft Edge, and the report format, such as text (
 .txt
 ), or HTML (
 .html
 ) files.

The Configure External Viewers dialog box contains the following options:

- Viewers 
 —A list of external viewer applications TestStand associates with specific report file extensions. When you select a viewer in the list control or click
 Add 
 , the following controls display the settings for the selected viewer:
 
 Click
 Add
 to add an entry to the viewer list. Click
 Delete
 to remove an entry.
  - Viewer 
 —The pathname of the external viewer application.
  - Format 
 —The file extension of the file, such as
 .txt 
 ,
 .html 
 , or
 .doc 
 .
  - Arguments 
 —The arguments to pass to the viewer. Use the keyword
 %filename 
 to designate the report file in the argument.
  - Automatically Launch Viewer 
 —Directs TestStand to open the report file in the specified external viewer application when an execution completes.
- Automatically Launch Default External Viewers 
 —Specifies that when an execution completes and you do not specify an external viewer for a file format, TestStand opens the file in the application Microsoft Windows associates with the file extension.

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-for-each-loop-dialog-box.html language=enus -->
## TOPIC 03462: Configure For Each Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-for-each-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-for-each-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure For Each Loop in the context menu for the step or click Configure For Each Loop on the General tab of the Step Properties dialog box to launch the Configure For Each Loop dialog box from a TestStand User Interface . The Configure For Each Loop dialog box contains the following optio

### Configure For Each Loop Dialog Box

Select
 Configure For Each Loop
 in the context menu for the step or click
 Configure For Each Loop
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure For Each Loop dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure For Each Loop dialog box contains the following options:

- Array/InputRecordStream to Interate Over 
 —The expression that determines the array or InputRecordStream over which the loop iterates. The steps within the block execute once for each element in the array or stream. Choose whether to iterate over an array or a stream by selecting the appropriate option from the
 Iterate Over Array / Iterate Over Stream 
 dropdown.
- Loop Variables (Optional) 
 —
 Expressions 
 that determine the location to store information about the current loop interation.
  - Current Element 
 —An expression that determines the variable or property in which to reference the current element in the array or to store the next record from the InputRecordStream during each iteration of the loop.
    - Interating Over Arrays 
 —The location the expression specifies must be of the same type as the element type for the
 Array to Iterate Over 
 option. Typically, you specify a local variable so the steps in the block can read or modify the current array element by referring to the local variable. The current element reference is valid only while the loop executes, and the reference resets after the loop completes. If the loop prematurely exits, the current element references the array element of the exiting iteration.
    - Interating Over Streams 
 — Current Element must refer to a container or array. Each iteration of the loop updates the value of the Current Element.
  - Current Offset 
 —An expression that determines the numeric variable or property into which to store current offset during each iteration of the loop. For zero-based one-dimensional arrays, the offset is equal to the index of the array. For multi-dimensional arrays, the offset is the linearized index of the array. For streams, the offset is a zero-based counter of the number of loop iterations.
  - Current Subscript 
 —An expression that determines the string variable or property into which to store the subscript of the current element in the
 Array to Iterate Over 
 option. Examples of the subscripts include [23] and [1][3]. Current Subscript is disabled when
 Iterate Over Stream 
 is selected.
- Interate Over Array/Interate Over Stream 
 —Specifies if this For Each loop iterates over an array or an InputRecordStream.
- Stream Options 
 —Settings that specify options specific to iterating over streams. These settings are hidden if
 Iterate Over Array 
 is selected.
  - Field Mapping (Optional) 
 —Specifies which container subproperties or array elements of the Current Element to store fields from the InputRecordStream to.
  - Auto Close at End of File 
 —Check this box to automatically clean up the InputRecordstream being read at the end of the loop. When this box is checked, upon terminating the loop, the For Each step closes the stream and sets the object reference in the
 InputRecordStream to Iterate Over 
 expression to Nothing.
 Note 
 Automatic cleanup only occurs if the loop terminates normally by encountering end of file (EOF). Cleanup does not occur if execution flow exits the loop for some other reason, for example via a Goto step.

#### Specifying the Current Element and Mapping When Iterating Over Streams

When iterating over an InputRecordStream, Current Element may be a container or array. If Current Element is a container, the container represents the record, and each subproperty is a field. If Current Element is an array, the array represents the record, and each array element is a field.

Field Mapping specifies the mapping to subproperties or array elements in Current Element from fields in the stream. The mapping is a comma-separated list of index ranges. For example, "0, 3-5, 8-7" specifies that fields from the incoming record be stored to elements 0, 3, 4, 5, 8, and 7 of the container or array. The final range in the list may be open-ended. For example, "2, 3-" specifies that fields from the incoming record be written to elements 2, 3, and all elements beyond 3 of the container or array.

If Current Element is a container, the range list may include individual subproperty names. For example, "Temperature, Pressure, 0-1" specifies that fields from the incoming record be written to the subproperties Temperature and Pressure and then elements 0 and 1.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

For Each Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-for-loop-dialog-box.html language=enus -->
## TOPIC 03463: Configure For Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-for-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-for-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure For Loop in the context menu for the step or click Configure For Loop on the General tab of the Step Properties dialog box to launch the Configure For Loop dialog box from a TestStand User Interface . The Configure For Loop dialog box contains the following options: Fixed Number of

### Configure For Loop Dialog Box

Select
 Configure For Loop
 in the context menu for the step or click
 Configure For Loop
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure For Loop dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure For Loop dialog box contains the following options:

- Fixed Number of Iterations 
 —Specifies if the steps within the For block execute repeatedly for a fixed number of loops.
  - Number of Loops 
 —The numeric expression that determines the number of iterations for the For block.
  - Loop Variable 
 —The numeric expression that determines the variable or property into which to store the current iteration number for the For block.
- Custom Loop 
 —The custom looping behavior for the steps within the For block.
  - Initialization 
 —The expression the step evaluates before executing the steps within the block for the first time.
  - Condition 
 —The expression the step evaluates each time before executing the steps within the block. If the expression evaluates to
 True 
 , execution proceeds to the first step in the block. If the expression evaluates to
 False 
 , execution proceeds to the End step for the For block.
  - Increment 
 —The expression the step evaluates after each execution of the steps within the block.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

For Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-if-condition-dialog-box.html language=enus -->
## TOPIC 03464: Configure If Condition Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-if-condition-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-if-condition-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure If Condition in the context menu for the step or click Configure If Condition on the General tab of the Step Properties dialog box to launch the Configure If Condition dialog box from a TestStand User Interface . The Configure If Condition dialog box contains the following options:

### Configure If Condition Dialog Box

Select
 Configure If Condition
 in the context menu for the step or click
 Configure If Condition
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure If Condition dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure If Condition dialog box contains the following options:

- Conditional Expression 
 —The expression that must evaluate to
 True 
 for the steps within the If block to execute. If the expression evaluates to
 False 
 , the execution proceeds to the next Else If, Else, or End step for the If block.
- Condition Builder 
 —Launches the
 Condition Builder 
 dialog box, in which you can build conditional
 expressions 
 that refer to the execution statuses of other steps.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Condition Builder dialog box](precondition-builder-dialog-box.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

If Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-menu.html language=enus -->
## TOPIC 03465: Configure Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-menu.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-menu.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Configure menu in the TestStand Sequence Editor contains the following items that control the operation of the TestStand station: Sequence Editor Options —Launches the Sequence Editor Options dialog box, in which you can set preferences for the sequence editor. Station Options —Launches the Stat

### Configure Menu

The Configure menu in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 contains the following items that control the operation of the TestStand station:

- Sequence Editor Options 
 —Launches the
 Sequence Editor Options 
 dialog box, in which you can set preferences for the sequence editor.
- Station Options 
 —Launches the
 Station Options 
 dialog box, in which you can set preferences for a TestStand station. These settings affect all sequence editor and user interface sessions you run on the computer.
- Search Directories 
 —Launches the
 Edit Search Directories 
 dialog box, in which you can customize the
 search paths 
 for finding files. The Edit Search Directories dialog box displays a list of paths. The paths that appear first in the list take precedence over the paths that appear later in the list. When you first run TestStand, the list contains a default set of directory paths.
- External Viewers 
 —Launches the
 Configure External Viewers 
 dialog box, in which you can specify the external viewer, such as Microsoft Notepad or Microsoft Edge, for each
 report format 
 .
- Adapters 
 —Launches the
 Adapter Configuration 
 dialog box, in which you can configure a specific module adapter, specify the active module adapter, or configure whether the adapter is not visible in the Adapter ring control in the sequence editor.
- Result Processing 
 —Launches the default
 Result Processing 
 dialog box, in
which you enable or disable the installed built-in and custom result processing model plug-ins
in the active result processing configuration, such as the Generate Reports model plug-in and the Database model plug-in, and also configure how the model plug-ins process
test results. You can insert multiple instances of the same plug-in with various configuration
options. Click the icon in the Options column for each built-in plug-in to launch the Options
dialog box, in which you set options specific to the plug-in. For example, click the options icon
for the Offline Results File plug-in to launch the
 Offline Results File Generation Options 
 dialog
box, in which you specify options for determining the directory location for result files, writing
the results to the file on-the-fly or after each UUT completes, limiting the number of UUTs per
file, automatically starting and/or exiting the
 TestStand Offline Results Processing Utility 
 .
 Note 
 If you are using the equivalent legacy TestStand 2010 process models, the Configure menu includes the following items:
 Report Options
 —Launches the
 [Report Options](report-options-dialog-box.html)
 dialog box, in which you enable UUT report generation and configure the report type and content of report files.
 Database Options
 —Launches the
 [Database Options](database-options-dialog-box.html)
 dialog box, in which you enable UUT result logging and configure the schema for mapping results to database tables and columns.
- Model Options 
 —Launches the
 Model Options 
 dialog box, in which you configure the number of test sockets and other process model-related options.

#### See Also

[Adapter Configuration dialog box](adapter-configuration-dialog-box.html)

[Configure External Viewers dialog box](configure-external-viewers-dialog-box.html)

[Database Options dialog box](database-options-dialog-box.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Generating a Test Report](../tsreports/teststand-xml-report-schema.html)

[Model Options dialog box](model-options-dialog-box.html)

[Offline Results File Generation Options dialog box](offline-results-file-generation-options-dialo.html)

[Report Options dialog box](report-options-dialog-box.html)

[Result Processing dialog box](result-processing-dialog-box.html)

[Sequence Editor Options dialog box](sequence-editor-options-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

[TestStand Offline Results Processing Utility](/csh?context=ts_tsref_offline_processing_utility)

Parent topic:

Menus

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-menu2.html language=enus -->
## TOPIC 03466: Configure Menu

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-menu2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-menu2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The Configure menu in a TestStand User Interface contains the following options for editing sequences and steps: Station Options —Launches the Station Options dialog box, in which you can set preferences for a TestStand station. These settings affect all sequence editor and user interface sessions y

### Configure Menu

The Configure menu in a
 [TestStand User Interface](teststand-user-interfaces.html)
 contains the following options for editing sequences and steps:

- Station Options 
 —Launches the
 Station Options 
 dialog box, in which you can set preferences for a TestStand station. These settings affect all sequence editor and user interface sessions you run on the computer.
- Search Directories 
 —Launches the
 Edit Search Directories 
 dialog box, in which you can customize the
 search paths 
 for finding files. The Edit Search Directories dialog box displays a list of paths. The paths that appear first in the list take precedence over the paths that appear later in the list. When you first run TestStand, the list contains a default set of directory paths.
- External Viewers 
 —Launches the
 Configure External Viewers 
 dialog box, in which you can specify the external viewer, such as Microsoft Notepad or Microsoft Edge, for each
 report format 
 .
- Adapters 
 —Launches the
 Adapter Configuration 
 dialog box, in which you can configure a specific module adapter, specify the active module adapter, or configure whether the adapter is not visible on the Insertion Palette pane.
- Result Processing 
 —Launches the default
 Result Processing 
 dialog box, in
which you enable or disable the installed built-in and custom result processing model plug-ins
in the active result processing configuration, such as the Generate Reports model plug-in and the Database model plug-in, and also configure how the model plug-ins process
test results. You can insert multiple instances of the same plug-in with various configuration
options. Click the icon in the Options column for each built-in plug-in to launch the Options
dialog box, in which you set options specific to the plug-in. For example, click the options icon
for the Offline Results File plug-in to launch the
 Offline Results File Generation Options 
 dialog
box, in which you specify options for determining the directory location for result files, writing
the results to the file on-the-fly or after each UUT completes, limiting the number of UUTs per
file, automatically starting and/or exiting the TestStand Offline Results Processing Utility.
 Note 
 If you are using the equivalent legacy TestStand 2010 process models, the Configure menu includes the following items:
 Report Options
 —Launches the Report Options dialog box, in which you enable UUT report generation and configure the report type and content of report files.
 Database Options
 —Launches the Database Options dialog box, in which you enable UUT result logging and configure the schema for mapping results to database tables and columns.
- Model Options 
 —Launches the
 Model Options 
 dialog box, in which you configure the number of test sockets and other process model-related options.

#### See Also

[Adapter Configuration dialog box](adapter-configuration-dialog-box.html)

[Configure External Viewers dialog box](configure-external-viewers-dialog-box.html)

[Database Options dialog box](database-options-dialog-box.html)

[Edit Search Directories dialog box](edit-search-directories-dialog-box.html)

[Generating a Test Report](../tsreports/teststand-xml-report-schema.html)

[Model Options dialog box](model-options-dialog-box.html)

[Offline Results File Generation Options dialog box](offline-results-file-generation-options-dialo.html)

[Report Options dialog box](report-options-dialog-box.html)

[Result Processing dialog box](result-processing-dialog-box.html)

[Station Options dialog box](station-options-dialog-box.html)

Parent topic:

TestStand User Interface Menus and Tabs

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-message-popup-step-dialog-box.html language=enus -->
## TOPIC 03467: Configure Message Popup Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-message-popup-step-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-message-popup-step-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Edit Message Settings in the context menu for the step or click Edit Message Settings on the General tab of the Step Properties dialog box to launch the Configure Message Popup Step dialog box from a TestStand User Interface . Use this dialog box to specify the expression for a Message Popup

### Configure Message Popup Step Dialog Box

Select
 Edit Message Settings
 in the context menu for the step or click
 Edit Message Settings
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure Message Popup Step dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to specify the expression for a Message Popup step.

The Configure Message Popup Step dialog box contains the following tabs:

- Text and Buttons 
 —The text for the title and buttons, as well as button behaviors.
- Options 
 —Specifies whether the dialog box displays a response text box, and an image or a web page.
- Layout 
 —The modality settings, the location of the dialog box, and the arrangement of the controls in the dialog box.

Note

#### See Also

[Built-In Step Types](built-in-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Message Popup Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-dmm-step-dialog.html language=enus -->
## TOPIC 03468: Configure Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-dmm-step-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-dmm-step-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Advanced Tab The Advanced tab for the Configure operation contains the following options: Sample Count —The number of measurements the DMM takes each time it receives a trigger. The value of this setting only affects instrument behavior when the Multi Point extension is enabled.

### Configure Operation - Edit IVI Dmm Step Dialog Box

#### Configure Operation

#### Advanced Tab

The Advanced tab for the Configure operation contains the following options:

- Sample Count 
 —The number of measurements the DMM takes each time it receives a trigger. The value of this setting only affects instrument behavior when the Multi Point extension is enabled.
- Sample Interval (mS) 
 —The interval between samples, in seconds. This setting affects instrument behavior only when Sample Count is greater than 1, Sample Trigger is set to Interval ST, and the Multi Point extension is enabled. If the Sample Interval value does not exactly match a value an instrument driver supports, the instrument driver will coerce up to the next supported value.
- Trigger Count 
 —The number of triggers the DMM accepts before it returns to the idle state. The value of this setting affects instrument behavior only when the Multi Point extension is enabled.
- Sample Trigger 
 —The trigger source for each sample. The Sample Trigger setting is typically used when handshaking with a switching system. For example, you can set up a switching system to go through a scan that a switch scan list specifies and set up the DMM to take a measurement at each channel specified in the scan list. You can connect the DMM VMC (voltmeter complete) signal to trigger input on the switching system. Also, you can set up the switching system so once it finishes a step in the scan, it sends out a pulse on the scanner advanced line, which can be hooked to the DMM sample trigger. If the value of the Sample Count is greater than 1, the DMM waits until a sample trigger occurs after taking a single measurement. When the sample trigger this setting specifies occurs, the DMM takes the next measurement. This setting only affects instrument behavior when Sample Count is greater than 1 and the Multi Point extension is enabled.
 
 Supported Value
 DescriptionImmediate (1)
 Specifies that the DMM does not wait for a trigger before acquiring a sample.
 External (2)
 Specifies that the DMM waits until a sample trigger occurs on the external trigger input and then acquires a sample.
 Software (3)
 Specifies that the DMM waits for a sample trigger until the Send Software Trigger operation executes and then acquires a sample.
 TTL0 (111)
 Specifies that the DMM waits until a sample trigger occurs on TTL0 and then acquires a sample.
 TTL1 (112)
 Specifies that the DMM waits until a sample trigger occurs on TTL1 and then acquires a sample.
 TTL2 (113)
 Specifies that the DMM waits until a sample trigger occurs on TTL2 and then acquires a sample.
 TTL3 (114)
 Specifies that the DMM waits until a sample trigger occurs on TTL3 and then acquires a sample.
 TTL4 (115)
 Specifies that the DMM waits until a sample trigger occurs on TTL4 and then acquires a sample.
 TTL5 (116)
 Specifies that the DMM waits until a sample trigger occurs on TTL5 and then acquires a sample.
 TTL6 (117)
 Specifies that the DMM waits until a sample trigger occurs on TTL6 and then acquires a sample.
 TTL7 (118)
 Specifies that the DMM waits until a sample trigger occurs on TTL7 and then acquires a sample.
 ECL0 (119)
 Specifies that the DMM waits until a sample trigger occurs on ECLO and then acquires a sample.
 ECL1 (120)
 Specifies that the DMM waits until a sample trigger occurs on ECL1 and then acquires a sample.
 PXI Star (131
 Specifies that the DMM waits until a sample trigger occurs on the PXI Star trigger bus and then acquires a sample.
 RTSI0 (140)
 Specifies that the DMM waits until a sample trigger occurs on RTSI0 and then acquires a sample.
 RTSI1 (141)
 Specifies that the DMM waits until a sample trigger occurs on RTSI1 and then acquires a sample.
 RTSI2 (142)
 Specifies that the DMM waits until a sample trigger occurs on RTSI2 and then acquires a sample.
 RTSI3 (143)
 Specifies that the DMM waits until a sample trigger occurs on RTSI3 and then acquires a sample.
 RTSI4 (144)
 Specifies that the DMM waits until a sample trigger occurs on RTSI4 and then acquires a sample.
 RTSI5 (145)
 Specifies that the DMM waits until a sample trigger occurs on RTSI5 and then acquires a sample.
 RTSI6 (146)
 Specifies that the DMM waits until a sample trigger occurs on RTSI6 and then acquires a sample.
 Interval (10)
 Specifies that the DMM waits for a sample trigger to occur for the amount of time Sample Interval specifies and then acquires a sample.
- Meas Complete Dest 
 —The destination of the measurement complete signal. After each measurement, the DMM generates a measurement complete signal. This signal is sometimes referred to as Voltmeter Complete (VMC). The value of this setting only affects instrument behavior when the Multi Point extension is enabled.
 
 Supported Value
 DescriptionNone (-1)
 Does not route the measurement complete signal.
 External (2)
 Routes the measurement complete signal to the external connector.
 TTL0 (111)
 Routes the measurement complete signal to TTL0.
 TTL1 (112)
 Routes the measurement complete signal to TTL1.
 TTL2 (113)
 Routes the measurement complete signal to TTL2.
 TTL3 (114)
 Routes the measurement complete signal to TTL3.
 TTL4 (115)
 Routes the measurement complete signal to TTL4.
 TTL5 (116)
 Routes the measurement complete signal to TTL5.
 TTL6 (117)
 Routes the measurement complete signal to TTL6.
 TTL7 (118)
 Routes the measurement complete signal to TTL7.
 ECL0 (119)
 Routes the measurement complete signal to ECL0.
 ECL1 (120)
 Routes the measurement complete signal to ECL 1.
 PXI Star (131)
 Routes the measurement complete signal to PXI Star trigger bus.
 RTSI0 (140)
 Routes the measurement complete signal to RTSI0.
 RTSI1 (141)
 Routes the measurement complete signal to RTSI1.
 RTSI2 (142)
 Routes the measurement complete signal to RTSI2.
 RTSI3 (143)
 Routes the measurement complete signal to RTSI3.
 RTSI4 (144)
 Routes the measurement complete signal to RTSI4.
 RTSI5 (145)
 Routes the measurement complete signal to RTSI5.
 RTSI6 (146)
 Routes the measurement complete signal to RTSI6.
- Voltage Range for Freq (Vrms) 
 —The expected range of the amplitude of the input signal in Vrms for frequency and period measurements. If the Voltage Range For Freq setting does not exactly match a value an instrument driver supports, the instrument driver will coerce up to the next supported value. The value of this setting only affects instrument behavior when the Frequency Measurement extension and the Measurement Function setting are set to a frequency or period measurement.
- Auto Zero 
 —The auto-zero mode. When you enable the Auto Zero setting, the DMM internally disconnects the input signal and takes a zero reading. The DMM then subtracts the zero reading from the measurement to prevent offset voltages present in the input circuitry of the instrument from affecting measurement accuracy. The value of this setting affects instrument behavior only when the Auto Zero extension is enabled.
 
 Supported Value
 DescriptionAuto Zero Off (0)
 Disables the auto-zero feature.
 Auto Zero On (1)
 Configures the DMM to take a zero reading for each measurement. The DMM subtracts the zero reading from the value it measures.
 Auto Zero Once (2)
 Configures the DMM to take a zero reading immediately. The DMM then subtracts this zero reading from all subsequent values it measures.
- Powerline Freq 
 —The power line frequency in hertz. Some devices require that the frequency of the power line to which they are connected is specified for accurate measurements. The value of this setting affects instrument behavior only when the Powerline Freq extension is enabled.
- Trigger Slope 
 —The polarity of the external trigger slope. The DMM triggers on either the rising or the falling edge of the external trigger source depending on the value of the Trigger Slope setting. The value of this setting affects instrument behavior only when the Trigger Slope extension is enabled.
 
 Supported Value
 DescriptionPositive (0)
 Sets the trigger event to occur on the rising edge of the trigger pulse.
 Negative (1)
 Sets the trigger event to occur on the falling edge of the trigger pulse.

Parent topic:

Configure Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-dmm-step-dialog2.html language=enus -->
## TOPIC 03469: Configure Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-dmm-step-dialog2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-dmm-step-dialog2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Extensions Tab The Configure operation handles only settings the base IVI class specification supports and the extension groups you specify on the Extensions tab. For best results, enable only the extensions the application requires. The Extensions tab for the Configure operation

### Configure Operation - Edit IVI Dmm Step Dialog Box

#### Configure Operation

#### Extensions Tab

Note

The Extensions tab for the Configure operation contains the following options:

- AC Measurement 
 —Supports the iviDmmACMeasurement extension group.
- Frequency Measurement 
 —Supports the iviDmmFrequencyMeasurement extension group.
- Temperature Measurement 
 —Supports the iviDmmTemperatureMeasurement extension group.
- Multi Point 
 —Supports the iviDmmMultiPoint extension group.
- Trigger Slope 
 —Supports the iviDmmTriggerSlope extension group.
- Software Trigger 
 —Supports the iviDmmSoftwareTrigger extension group.
- Device Info 
 —Supports the iviDmmDeviceInfo extension group.
- Auto Range Value 
 —Supports the iviDmmAutoRangeValue extension group.
- Auto Zero 
 —Supports the iviDmmAutoZero extension group.
- Powerline Frequency 
 —Supports the iviDmmPowerLineFrequency extension group.

Parent topic:

Configure Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-dmm-step-dialog3.html language=enus -->
## TOPIC 03470: Configure Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-dmm-step-dialog3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-dmm-step-dialog3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Operation Settings Tab The Operation Settings tab for the Configure operation contains the following options: Configuration Source —The name of the property or variable in which TestStand stores the settings when you click OK . Load —Specifies the property or variable to which th

### Configure Operation - Edit IVI Dmm Step Dialog Box

#### Configure Operation

#### Operation Settings Tab

The Operation Settings tab for the Configure operation contains the following options:

- Configuration Source 
 —The name of the property or variable in which TestStand stores the settings when you click
 OK 
 .
- Load 
 —Specifies the property or variable to which the step saves the operation settings when closing the Edit IVI DMM Step dialog box, and reloads the operation settings when launching the Edit IVI DMM Step dialog box.

Parent topic:

Configure Operation - Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-dmm-step-dialog4.html language=enus -->
## TOPIC 03471: Configure Operation - Edit IVI Dmm Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-dmm-step-dialog4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-dmm-step-dialog4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation The Configure operation configures a DMM for a typical measurement, which includes setting the measurement function, desired range, desired resolution, and trigger source. Additional configurable settings include the minimum and maximum frequency of the input signal for AC measur

### Configure Operation - Edit IVI Dmm Step Dialog Box

#### Configure Operation

The Configure operation configures a DMM for a typical measurement, which includes setting the measurement function, desired range, desired resolution, and trigger source. Additional configurable settings include the minimum and maximum frequency of the input signal for AC measurements and acquiring multiple measurements based on multiple triggers and taking multiple measurements per trigger.

Note

The Edit IVI Dmm Step dialog box for the Configure operation contains the following tabs:

- Basic 
 —The function the DMM performs and specifies resolution, frequency, triggering, and range settings.
- Advanced 
 —Additional settings for multipoint measurements and other extensions.
- Temperature 
 —Additional information for the temperature measurements.
- Extensions 
 —The extensions to enable in the dialog box.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Dmm Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-fgen-step-dialog.html language=enus -->
## TOPIC 03472: Configure Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-fgen-step-dialog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-fgen-step-dialog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Extensions Tab The Configure operation handles only settings the base IVI class specification supports and the extension groups you specify on the Extensions tab. For best results, enable only the extensions the application requires. The Extensions tab for the Configure operation

### Configure Operation - Edit IVI Fgen Step Dialog Box

#### Configure Operation

#### Extensions Tab

Note

The Extensions tab for the Configure operation contains the following options:

- Standard Function 
 —Supports extensions for function generators that can produce manufacturer-supplied periodic waveforms.
- Arb Waveform 
 —Supports extensions for function generators that can produce user-defined arbitrary waveforms.
- Arb Sequences 
 —Supports extensions for function generators that can produce sequences of arbitrary waveforms.
- Arb Frequency 
 —Supports extensions for function generators that can produce arbitrary waveforms and setting the rate at which an entire waveform buffer is generated.
- Modulate AM 
 —Supports extensions for function generators that can apply amplitude modulation to an output signal.
- Modulate FM 
 —Supports extensions for function generators that can apply frequency modulation to an output signal.
- Burst 
 —Supports extensions for function generators that can generate a discrete number of waveform cycles based on a trigger.
- Trigger 
 —Supports extensions for function generators that can configure a trigger.
- Internal Trigger 
 —Supports extensions for function generators that can generate output based on an internally generated trigger signal.
- Software Trigger 
 —Supports extensions for function generators that can generate output based on a software trigger signal.

Parent topic:

Configure Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-fgen-step-dialog2.html language=enus -->
## TOPIC 03473: Configure Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-fgen-step-dialog2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-fgen-step-dialog2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Operation Settings Tab The Operation Settings tab for the Configure operation contains the following option: Settings Property/Variable —Specifies the property or variable to which the step saves the operation settings when closing the Edit IVI Fgen Step dialog box, and reloads t

### Configure Operation - Edit IVI Fgen Step Dialog Box

#### Configure Operation

#### Operation Settings Tab

The Operation Settings tab for the Configure operation contains the following option:

- Settings Property/Variable 
 —Specifies the property or variable to which the step saves the operation settings when closing the Edit IVI Fgen Step dialog box, and reloads the operation settings when launching the Edit IVI Fgen Step dialog box.

Parent topic:

Configure Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-fgen-step-dialog3.html language=enus -->
## TOPIC 03474: Configure Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-fgen-step-dialog3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-fgen-step-dialog3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Sequences Tab The Sequences tab contains a list control of defined sequences. Use the Add and Remove buttons to add new sequences and remove existing sequences from the list. Preserve Existing Sequences —When you enable this option, the step adds to or modifies any existing, prev

### Configure Operation - Edit IVI Fgen Step Dialog Box

#### Configure Operation

#### Sequences Tab

The Sequences tab contains a list control of defined sequences. Use the
 Add
 and
 Remove
 buttons to add new sequences and remove existing sequences from the list.

- Preserve Existing Sequences 
 —When you enable this option, the step adds to or modifies any existing, previously configured sequences. When you disable this option, the step deletes all previously configured sequences before configuring the specified sequence in the list.

The Sequences tab for the Configure operation also contains the following sequence-specific options:

- Name 
 —The name of the sequence.
- Sequence Items 
 —A list of waveforms and how many times to generate each waveform. Use the
 Add 
 ,
 Remove 
 ,
 Up 
 , and
 Down 
 buttons to edit the list of waveforms in the list.
 When you select a list item, you can use the following controls to end the selected item:
  - Waveform 
 —The name of a waveform defined on the Waveforms tab.
  - Iterations 
 —The number of times the associated Waveform appears in the sequence for this sequence item.
 Note 
 The Iterations setting must be less than or equal to the maximum number of iterations the function generator allows.

Parent topic:

Configure Operation - Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-fgen-step-dialog4.html language=enus -->
## TOPIC 03475: Configure Operation - Edit IVI Fgen Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-fgen-step-dialog4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-fgen-step-dialog4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Configures a function generator to generate an analog voltage waveform. The output signal is typically functional in nature, such as a sinusoidal or square waveform. Some instruments support the generation of arbitrary waveforms, which consist of user-specified data. If the funct

### Configure Operation - Edit IVI Fgen Step Dialog Box

#### Configure Operation

Configures a function generator to generate an analog voltage waveform. The output signal is typically functional in nature, such as a sinusoidal or square waveform. Some instruments support the generation of arbitrary waveforms, which consist of user-specified data. If the function generator also supports the generation of arbitrary waveform sequences, the output signal can consist of a sequence of repeated arbitrary waveforms.

Note

The Edit IVI Fgen Step dialog box for the Configure operation contains the following tabs:

- Basic 
 —The output mode, clocking, triggering, and modulation of generated signals.
- Channels 
 —The channel name and settings the function generator outputs.
  - Output Signal Tab 
 —The standard waveform, arb waveform, or sequence the channel outputs.
  - Operation Tab 
 —The impedance and trigger settings for a channel.
  - Modulation Tab 
 —The modulation settings for a channel.
- Waveforms 
 —The waveforms to download to the function generator.
- Sequences 
 —The sequences to download to the function generator.
- Extensions 
 —The extensions to enable in the dialog box.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Fgen Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-power-supply-ste.html language=enus -->
## TOPIC 03476: Configure Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-power-supply-ste.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-power-supply-ste.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation The Configure operation configures a power supply’s voltage level, current limit, current limit behavior, and over voltage protection limit, as well as enabling and disabling output channels. You can also use this operation to configure the output range in which the power supply

### Configure Operation - Edit IVI Power Supply Step Dialog Box

#### Configure Operation

The Configure operation configures a power supply’s voltage level, current limit, current limit behavior, and over voltage protection limit, as well as enabling and disabling output channels. You can also use this operation to configure the output range in which the power supply operates.

Note

The Edit IVI Power Supply Step dialog box for the Configure operation contains the following tabs:

- Channels 
 —The channel names the step configures.
  - Output Tab 
 —The voltage and current range settings for a channel.
  - Limits Tab 
 —The current limit settings for a channel.
  - Trigger Tab 
 —The trigger settings for a channel.
- Extensions 
 —The extensions to enable in the dialog box.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-power-supply-ste2.html language=enus -->
## TOPIC 03477: Configure Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-power-supply-ste2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-power-supply-ste2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Extensions Tab The Configure operation handles only settings the base IVI class specification supports and the extension groups you specify on the Extensions tab. For best results, enable only the extensions the application requires. The Extensions tab for the Configure operation

### Configure Operation - Edit IVI Power Supply Step Dialog Box

#### Configure Operation

#### Extensions Tab

Note

The Extensions tab for the Configure operation contains the following options:

- Trigger 
 —Supports extensions for DC power supplies that can change the voltage at the output terminals based on a Trigger event.
- Software Trigger 
 —Supports extensions for DC power supplies that can change the voltage at the output terminals based on the Software Trigger operation.
- Measurement 
 —Supports extensions for DC power supplies that can take measurements, such as voltage, at the output terminals.

Parent topic:

Configure Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-power-supply-ste3.html language=enus -->
## TOPIC 03478: Configure Operation - Edit IVI Power Supply Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-power-supply-ste3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-power-supply-ste3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Operation Settings Tab The Operation Settings tab for the Configure operation contains the following option: Settings Property/Variable —Specifies the property or variable to which the step saves the operation settings when closing the Edit IVI Power Supply Step dialog box, and r

### Configure Operation - Edit IVI Power Supply Step Dialog Box

#### Configure Operation

#### Operation Settings Tab

The Operation Settings tab for the Configure operation contains the following option:

- Settings Property/Variable 
 —Specifies the property or variable to which the step saves the operation settings when closing the Edit IVI Power Supply Step dialog box, and reloads the operation settings when launching the Edit IVI Power Supply Step dialog box.

Parent topic:

Configure Operation - Edit IVI Power Supply Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-scope-step-dialo.html language=enus -->
## TOPIC 03479: Configure Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-scope-step-dialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-scope-step-dialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Advanced Tab The Advanced tab for the Configure operation contains the following options: Low Reference —The low reference the oscilloscope uses for waveform measurements. The value is a percentage of the difference between voltage high and voltage low. The value of this setting

### Configure Operation - Edit IVI Scope Step Dialog Box

#### Configure Operation

#### Advanced Tab

The Advanced tab for the Configure operation contains the following options:

- Low Reference 
 —The low reference the oscilloscope uses for waveform measurements. The value is a percentage of the difference between voltage high and voltage low. The value of this setting affects instrument behavior only when the Waveform Measurement extension is enabled.
- Middle Reference 
 —The middle reference in percentage the oscilloscope uses for waveform measurements. The value is a percentage of the difference between voltage high and voltage low. The value of this setting affects instrument behavior only when the Waveform Measurement extension is enabled.
- High Reference 
 —The high reference the oscilloscope uses for waveform measurements. The value is a percentage of the difference between voltage high and voltage low. The value of this setting affects instrument behavior only when the Waveform Measurement extension is enabled.

Parent topic:

Configure Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-scope-step-dialo2.html language=enus -->
## TOPIC 03480: Configure Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-scope-step-dialo2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-scope-step-dialo2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Basic Tab The Basic tab for the Configure operation contains the following options: Acquisition Type —Specifies how the oscilloscope acquires data and fills the waveform record. Supported Value Description Normal (0) Configures the oscilloscope to acquire one sample for each poin

### Configure Operation - Edit IVI Scope Step Dialog Box

#### Configure Operation

#### Basic Tab

The Basic tab for the Configure operation contains the following options:

- Acquisition Type 
 —Specifies how the oscilloscope acquires data and fills the waveform record.
 
 Supported Value
 DescriptionNormal (0)
 Configures the oscilloscope to acquire one sample for each point in the waveform record. The oscilloscope uses real-time or equivalent-time sampling.
 Peak Detect (1)
 Sets the oscilloscope to the peak-detect acquisition mode. The oscilloscope oversamples the input signal and keeps the minimum and maximum values that correspond to each position in the waveform record. The oscilloscope uses only real-time sampling.
 Hi Res (2)
 Configures the oscilloscope to oversample the input signal. The oscilloscope calculates the average value that corresponds to each position in the waveform record. The oscilloscope uses only real-time sampling.
 Envelope (3)
 Sets the oscilloscope to the envelope acquisition mode. The oscilloscope acquires multiple waveforms and keeps the minimum and maximum voltages it acquires for each point in the waveform record. Specify the number of waveforms the oscilloscope acquires with the Num Envelopes setting. The oscilloscope can use real-time or equivalent-time sampling.
 Average (4)
 Configures the oscilloscope to acquire multiple waveforms and calculate the average value for each point in the waveform record. Specify the number of waveforms to acquire with the Num Averages setting. The oscilloscope uses real-time or equivalent-time sampling.
- Interpolation 
 —The interpolation method the oscilloscope uses when it cannot resolve a voltage for every point in the waveform record. The value of this setting only affects instrument behavior when the interpolation extension is enabled.
 
 Supported Value
 DescriptionNo Interpolation (1)
 Specifies that the oscilloscope does not interpolate points in the waveform. Instead, the driver sets every element in the waveform record for which the oscilloscope cannot receive a value to an IEEE-defined NaN (not a number) value.
 Sine X (2)
 Specifies that the oscilloscope uses a sin(
 x
 )/
 x
 calculation to interpolate a value when it cannot resolve a voltage in the waveform record.
 Linear (3)
 Specifies that the oscilloscope uses a linear approximation to interpolate a value when it cannot resolve a voltage in the waveform record.
- Num Averages 
 —The number of waveforms the oscilloscope acquires and averages. After the oscilloscope acquires as many waveforms this setting specifies, the oscilloscope returns to the idle state. The value of this setting affects instrument behavior only when the Average Acquisition extension and the Acquisition Type are set to Average.
- Num Envelopes 
 —The number of waveforms the oscilloscope acquires and analyzes to create the minimum and maximum waveforms. When you set the Acquisition Type setting to Envelope, the oscilloscope acquires multiple waveforms. After each waveform acquisition, the oscilloscope keeps the minimum and maximum values it finds for each point in the waveform record. After the oscilloscope acquires as many waveforms this setting specifies, the oscilloscope returns to the idle state. The value of this setting affects instrument behavior only when you enable the Min Max Waveform extension and set the Acquisition Type setting to Envelope.
- Min Num Points 
 —The minimum number of points the end user requires in the waveform record for each channel. The instrument driver uses the value you specify to configure the record length the oscilloscope uses for waveform acquisition. If the instrument cannot support the requested record length, the driver must configure the instrument to the closest supported record length. The value of the supported record length is larger than the requested length. Use the Get Actual Record Length operation to obtain the actual record length for the acquisition.
- Time Per Record 
 —The length of time, in seconds, that corresponds to the record length. If Time Per Record does not exactly match a value an instrument driver supports, the instrument driver will coerce up to the next supported value.
- Acq Start Time 
 —The length of time, in seconds, from the trigger event to the first point in the waveform record. When the value of Acquisition Start Time is positive, the first point in the waveform record occurs after the trigger event. When the value is negative, the first point in the waveform record occurs before the trigger event.

Parent topic:

Configure Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-scope-step-dialo3.html language=enus -->
## TOPIC 03481: Configure Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-scope-step-dialo3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-scope-step-dialo3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Channels Tab The Channels tab contains a list control with the default channels for the selected logical name. Use the Add and Remove buttons to add new channels and remove existing channels from the list. You can specify whether the oscilloscope acquires a waveform for the chann

### Configure Operation - Edit IVI Scope Step Dialog Box

#### Configure Operation

#### Channels Tab

The Channels tab contains a list control with the default channels for the selected logical name. Use the
 Add
 and
 Remove
 buttons to add new channels and remove existing channels from the list. You can specify whether the oscilloscope acquires a waveform for the channel by enabling the channel in the list control.

- Preserve Existing Channels 
 —When you enable this option, the step adds to or modifies any previously configured channels. When you disable this option, the step deletes all previously configured channels before configuring the specified channels in the list.

The Channels tab for the Configure operation also contains the following channel-specific options:

- Name 
 —The name of the channel. The channel name must be a valid virtual channel name as the IVI configuration for the logical name being used defines.
- Vertical Coupling 
 —Specifies how the oscilloscope couples the input signal for the channel.
 
 Supported Value
 DescriptionAC (0)
 Specifies that the oscilloscope AC couples the input signal.
 DC (1)
 Specifies that the oscilloscope DC couples the input signal.
 Gnd (2)
 Specifies that the oscilloscope couples the channel to the ground.
- Vertical Range 
 —The absolute value of the input range, in volts (V), for a channel. For example, to acquire a sine wave that spans between -5.0 and 5.0 V, set the value to 10.0 V. If the vertical range value does not exactly match a value an instrument driver supports, the instrument driver will coerce up to the next supported value.
- Vertical Offset 
 —The center of the range, in volts, the Vertical Range setting specifies. This setting value is set with respect to ground. For example, set vertical offset to 5.0 V to acquire a sine wave that spans between 0.0 and 10.0 V.
- Max Input Freq 
 —The maximum frequency for the input signal you want the instrument to accommodate without attenuating it by more than 3 dB. If the bandwidth limit frequency of the instrument is greater than this maximum frequency, the driver enables the bandwidth limit to attenuate the input signal by at least 3 dB at frequencies greater than the bandwidth limit. If the max input frequency value does not exactly match a value an instrument driver supports, the instrument driver will coerce up to the next supported value.
- Probe Attenuation 
 —The scaling factor to which the probe attached the channel uses to attenuate the input. When the value is
 -1 
 , the oscilloscope is configured to use automatic probe sensing. When the value is positive, the oscilloscope is configured to use the specified manual probe attenuation. For example, for a 10:1 probe, set Probe Attenuation to
 10.0 
 . If you are using automatic probe sensing, use the Get Auto Probe Sense Value operation to determine the actual probe.
- Input Impedance 
 —The input impedance for the channel in ohms. Common values are 50.0, 75.0, and 1,000,000.0.

Parent topic:

Configure Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-scope-step-dialo4.html language=enus -->
## TOPIC 03482: Configure Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-scope-step-dialo4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-scope-step-dialo4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Extensions Tab The Configure operation handles only settings the base IVI class specification supports and the extension groups you specify on the Extensions tab. For best results, enable only the extensions the application requires. The Extensions tab for the Configure operation

### Configure Operation - Edit IVI Scope Step Dialog Box

#### Configure Operation

#### Extensions Tab

Note

The Extensions tab for the Configure operation contains the following options:

- TV Trigger 
 —Supports extensions for oscilloscopes that can trigger on TV signals.
- Runt Trigger 
 —Supports extensions for oscilloscopes that can trigger on runt pulses. A runt condition occurs when the oscilloscope detects a positive or negative pulse that crosses one voltage threshold but fails to cross a second threshold before recrossing the first. You can select whether a positive runt, negative runt, or either runt type triggers the acquisition.
- Glitch Trigger 
 —Supports extensions for oscilloscopes that can trigger on glitch pulses. A glitch occurs when the oscilloscope detects a pulse width less than or greater than a specified glitch duration. You can select a positive glitch, negative glitch, or either glitch to trigger the acquisition.
- Width Trigger 
 —Supports extensions for oscilloscopes that can trigger on user-specified pulse widths. Width triggering occurs when the oscilloscope detects a positive or negative pulse with a width between, or optionally outside, the user-specified threshold.
- AC Line Trigger 
 —Supports extensions for oscilloscopes that can synchronize the trigger with the AC Line. AC Line triggering occurs when the oscilloscope detects a positive zero crossing, negative zero crossing, or either positive or negative zero crossing on the network supply voltage.
- Trigger Modifier 
 —Supports extensions for oscilloscopes that can specify the behavior of the triggering subsystem in the absence of the configured trigger.
- Waveform Measurement 
 —Supports extensions for oscilloscopes that can calculate various measurements—such as rise time, fall time, period, and frequency—from an acquired waveform.
- Min Max Waveform 
 —Supports extensions for oscilloscopes that can acquire minimum and maximum waveforms that correspond to the same range of time. The two most common acquisition types in which oscilloscopes return minimum and maximum waveforms are envelope and peak detect.
- Average Acquisition 
 —Supports extensions for oscilloscopes that can perform the average acquisition.
- Interpolation 
 —Supports extensions for oscilloscopes that can interpolate values in the waveform record the oscilloscope acquisition subsystem was unable to digitize.
- Probe Auto Sense 
 —Supports extensions for oscilloscopes that can return the probe attenuation of the attached probe.
- Sample Mode 
 —Supports extensions for oscilloscopes that can return whether the scope is using equivalent-time or real-time sampling to acquire waveform.
- Auto Setup 
 —Supports extensions for oscilloscopes that can perform an automatic setup operation.
- Continuous Acquisition 
 —Supports extensions for oscilloscopes that can perform a continuous acquisition.

Parent topic:

Configure Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-scope-step-dialo5.html language=enus -->
## TOPIC 03483: Configure Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-scope-step-dialo5.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-scope-step-dialo5.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Operation Settings Tab The Operation Settings tab for the Configure operation contains the following channel-specific option: Settings Property/Variable —The property or variable to which the step saves the operation settings when you close the Edit IVI Scope Step dialog box. Thi

### Configure Operation - Edit IVI Scope Step Dialog Box

#### Configure Operation

#### Operation Settings Tab

The Operation Settings tab for the Configure operation contains the following channel-specific option:

- Settings Property/Variable 
 —The property or variable to which the step saves the operation settings when you close the Edit IVI Scope Step dialog box. This property or variable also reloads the operation settings when you launch the Edit IVI Scope Step dialog box.

Parent topic:

Configure Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-scope-step-dialo6.html language=enus -->
## TOPIC 03484: Configure Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-scope-step-dialo6.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-scope-step-dialo6.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation Trigger Tab The Trigger tab for the Configure operation contains the following options: Type —The event that triggers the oscilloscope. Supported Value Description AC Line (7) Configures the oscilloscope for AC Line triggering. Edge (1) Configures the oscilloscope for edge trigge

### Configure Operation - Edit IVI Scope Step Dialog Box

#### Configure Operation

#### Trigger Tab

The Trigger tab for the Configure operation contains the following options:

- Type 
 —The event that triggers the oscilloscope.
 
 Supported Value
 DescriptionAC Line (7)
 Configures the oscilloscope for AC Line triggering.
 Edge (1)
 Configures the oscilloscope for edge triggering. An edge trigger occurs when the trigger signal specified with the Trigger Source setting passes the voltage threshold specified with the Trigger Level setting and has the slope specified with the Trigger Slope setting.
 Glitch (4)
 Configures the oscilloscope for glitch triggering.
 Immediate (6)
 Configures the oscilloscope for immediate triggering. The oscilloscope does not wait for a trigger of any kind upon initialization.
 Runt (3)
 Configures the oscilloscope for runt triggering.
 TV (5)
 Configures the oscilloscope for triggering on TV signals.
 Width (2)
 Configures the oscilloscope for width triggering.
- Source 
 —The source the oscilloscope monitors for the trigger event. Source is a string that can be a defined virtual channel name, an instrument specific channel string, or one of the following
 
 defined values:
 
 "IVISCOPE_VAL_EXTERNAL"
 "IVISCOPE_VAL_TTL5"
 "IVISCOPE_VAL_RTSI_1"
 "IVISCOPE_VAL_GPIB_GET"
 "IVISCOPE_VAL_TTL6"
 "IVISCOPE_VAL_RTSI_2"
 "IVISCOPE_VAL_TTL0"
 "IVISCOPE_VAL_TTL7"
 "IVISCOPE_VAL_RTSI_3"
 "IVISCOPE_VAL_TTL1"
 "IVISCOPE_VAL_ECL0"
 "IVISCOPE_VAL_RTSI_4"
 "IVISCOPE_VAL_TTL2"
 "IVISCOPE_VAL_ECL1"
 "IVISCOPE_VAL_RTSI_5"
 "IVISCOPE_VAL_TTL3"
 "IVISCOPE_VAL_PXI_STAR"
 "IVISCOPE_VAL_RTSI_6"
 "IVISCOPE_VAL_TTL4"
 "IVISCOPE_VAL_RTSI_0"
- Holdoff 
 —The length of time, in seconds, the oscilloscope waits between detecting a trigger and enabling the trigger subsystem to detect another trigger. The Holdoff setting only affects instrument operation when the oscilloscope requires multiple acquisitions to build a complete waveform, such as when the oscilloscope uses equivalent time sampling or when the Acquisition Type is set to Envelope or Average. Many scopes have a small, nonzero value as the minimum value for this setting. To configure the instrument to use the shortest trigger holdoff, specify a value of
 0 
 . The instrument driver coerces any value between
 0 
 and the minimum value you specify to the minimum supported value.
- Coupling 
 —Specifies how the oscilloscope couples the trigger source.
 
 Supported Value
 DescriptionAC (0)
 Specifies that the oscilloscope AC couples the trigger signal.
 DC (1)
 Specifies that the oscilloscope DC couples the trigger signal.
 HF Reject (3)
 Specifies that the oscilloscope filters out the high frequencies from the trigger signal.
 LF Reject (4)
 Specifies that the oscilloscope filters out the low frequencies from the trigger signal.
 Noise Reject (5)
 Specifies that the oscilloscope filters out the noise from the trigger signal.
- Modifier 
 —Determines the behavior of the oscilloscope in the absence of the configured trigger. The value of this setting only affects instrument behavior when the Trigger Modifier extension is enabled.
 
 Supported Value
 DescriptionAuto (2)
 Specifies that the oscilloscope automatically triggers if the configured trigger does not occur within the timeout period.
 Auto Level (3)
 Specifies that the oscilloscope adjusts the trigger level if the trigger you specify does not occur.
 No Trigger Mod (1)
 Specifies that the oscilloscope waits until the specified trigger occurs.
- Initiate Continuous 
 —Continuously initiates waveform acquisition when set to
 True 
 . The value of this setting only affects instrument behavior when the Continuous Acquisition extension is enabled. This setting does not affect the behavior of the Read and Fetch operations because these operations are instrument specific. Set this setting to
 True 
 when you need continuous updates of the oscilloscope display.
- Level 
 —A level setting for the following trigger types:
  - Edge 
 —The threshold, in volts, for the trigger subsystem. The value of this setting only affects instrument behavior when the Trigger Type setting is set to Edge.
  - Glitch 
 —The threshold, in volts, for the trigger subsystem. The value of this setting only affects instrument behavior when the Glitch Trigger extension and the Trigger Type setting are set to Glitch.
  - Width 
 —The level, in volts, at which the pulse causes a trigger. The value of this setting only affects instrument behavior when the Width Trigger extension and the Trigger Type setting are set to Width.
- Condition 
 —Specifies the condition for the following trigger types:
  - Glitch 
 —The range in which the glitch trigger occurs. This setting determines whether the glitch trigger happens when the oscilloscope detects a pulse with a width less than or greater than the width value. The value of this setting only affects instrument behavior when the Glitch Trigger extension and the Trigger Type setting is set to Glitch.
 
 Supported Value
 DescriptionGreater Than (2)
 Triggers the oscilloscope when the pulse width is greater than the value you specify with the Glitch Width setting.
 Less Than (1)
 Triggers the oscilloscope when the pulse width is less than the value you specify with the Glitch Width setting.
  - Width 
 —Specifies whether a pulse inside or outside the high and low thresholds triggers the oscilloscope. The value of this setting only affects instrument behavior when the Width Trigger extension and the Trigger Type setting are set to Width.
 
 Supported Value
 DescriptionWidth Outside (2)
 Configures the oscilloscope to trigger on pulses that have a width greater than the high threshold or less than the low threshold. You can specify the high and low thresholds with the High Threshold and Low Threshold settings.
 Width Within (1)
 Configures the oscilloscope to trigger on pulses that have a width less than the high threshold and greater than the low threshold. You can specify the high and low thresholds with the High Threshold and Low Threshold settings.
- Event 
 —The event on which the oscilloscope triggers. The value of this setting only affects instrument behavior when the TV Trigger extension and the Trigger Type setting are set to TV.
 
 Supported Value
 DescriptionAny Field (3)
 Sets the oscilloscope to trigger on any field.
 Any Line (4)
 Sets the oscilloscope to trigger on any line.
 Field1 (1)
 Sets the oscilloscope to trigger on field 1 of the video signal.
 Field2 (2)
 Sets the oscilloscope to trigger on field 2 of the video signal.
 Line Number (5)
 Sets the oscilloscope to trigger on any line.
- Line Number 
 —The line on which the oscilloscope triggers. The line number setting is independent of the field. To trigger on the first line of the second field, you must configure the line number to the value of 263 (if you presume that the first field has 262 lines). The value of this setting only affects instrument behavior when the TV Trigger extension, the Trigger Type setting is set to TV, and the TV Event setting is set to TV Line Number.
- Signal Format 
 —The format of TV signal on which the oscilloscope triggers. The value of this setting only affects instrument behavior when the TV Trigger extension and the Trigger Type setting are set to TV.
 
 Supported Value
 DescriptionNTSC (1)
 Configures the oscilloscope to trigger on the NTSC signal format.
 PAL (2)
 Configures the oscilloscope to trigger on the PAL signal format.
 SECAM (3)
 Configures the oscilloscope to trigger on the SECAM signal format.
- Polarity 
 —Specifies the Polarity setting for the following trigger types:
  - Glitch 
 —The polarity of the glitch. The value of this setting only affects instrument behavior when the Glitch Trigger extension and the Trigger Type setting are set to Glitch.
 
 Supported Value
 DescriptionPositive (1)
 Triggers the oscilloscope on a positive glitch.
 Negative (2)
 Triggers the oscilloscope on a negative glitch.
 Either (3)
 Triggers the oscilloscope on either a positive or negative glitch.
  - Runt 
 —The polarity of the runt that triggers the oscilloscope. The value of this setting only affects instrument behavior when the Runt Trigger extension and the Trigger Type setting are set to Runt.
 
 Supported Value
 DescriptionPositive (1)
 Triggers the oscilloscope on a positive runt. A positive runt occurs when a rising edge crosses the low runt threshold and does not cross the high runt threshold before recrossing the low runt threshold.
 Negative (2)
 Triggers the oscilloscope on a negative runt. A negative runt occurs when a falling edge crosses the high runt threshold and does not cross the low runt threshold before recrossing the high runt threshold.
 Either (3)
 Triggers the oscilloscope on either a positive or negative runt.
  - TV 
 —The polarity of the TV signal. The value of this setting only affects instrument behavior when the TV Trigger extension and the Trigger Type setting are set to TV.
 
 Supported Value
 DescriptionNegative (0)
 Configures the oscilloscope to trigger on a negative video sync pulse.
 Positive (1)
 Configures the oscilloscope to trigger on a positive video sync pulse.
  - Width 
 —The polarity of the pulse that triggers the oscilloscope. The value of this setting only affects instrument behavior when the Width Trigger extension and Trigger Type is Width.
 
 Supported Value
 DescriptionNegative (2)
 Configures the oscilloscope to trigger on negative pulses that have a width that meets the condition specified with the Condition setting.
 Positive (1)
 Configures the oscilloscope to trigger on positive pulses that have a width that meets the condition specified with the Condition setting.
- Slope 
 —A Slope setting for the following trigger types.
  - AC Line 
 —The slope of the zero crossing upon which the oscilloscope triggers. The value of this setting only affects instrument behavior when the AC Line Trigger extension and the Trigger Type setting are set to AC Line.
 
 Supported Value
 DescriptionPositive (1)
 Configures the oscilloscope to trigger on positive slope zero crossings of the network supply voltage.
 Negative (2)
 Configures the oscilloscope to trigger on negative slope zero crossings of the network supply voltage.
 Either (3)
 Configures the oscilloscope to trigger on either positive or negative slope zero crossings of the network supply voltage.
  - Edge 
 —Specifies whether a rising or falling edge triggers the oscilloscope. The value of this setting only affects instrument behavior when the Trigger Type is Edge.
 
 Supported Value
 DescriptionNegative (0)
 Specifies that a negative (falling) edge passing through the trigger level triggers the oscilloscope.
 Positive (1)
 Specifies that a positive (rising) edge passing through the trigger level triggers the oscilloscope.
- Width 
 —Specifies the width setting for the following trigger type:
  - Glitch 
 —The glitch width, in seconds. The oscilloscope triggers when it detects a pulse with a width less than or greater than this value, depending on the value of the Glitch Condition setting. The value of this setting only affects instrument behavior when the Glitch Trigger extension and the Trigger Type setting are set to Glitch.
- High Threshold 
 —The high threshold for the following trigger types:
  - Runt 
 —The high threshold, in volts, the oscilloscope uses for runt triggering. The value of this setting only affects instrument behavior when the Runt Trigger extension and the Trigger Type setting are set to Runt.
  - Width 
 —The high width threshold time, in seconds. For the instrument to trigger, the pulse length must be between the High Threshold and Low Threshold values. The value of this setting only affects instrument behavior when the Width Trigger extension and the Trigger Type setting are set to Width.
- Low Threshold 
 —The high threshold for the following trigger types:
  - Runt 
 —The low threshold, in volts, the oscilloscope uses for runt triggering. The value of this setting only affects instrument behavior when the Runt Trigger extension and the Trigger Type setting are set to Runt.
  - Width 
 —The low width threshold time, in seconds. For the instrument to trigger, the pulse length must be between the High Threshold and Low Threshold values. The value of this setting only affects instrument behavior when the Width Trigger extension and the Trigger Type setting are set to Width.

Parent topic:

Configure Operation - Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-operation-edit-ivi-scope-step-dialo7.html language=enus -->
## TOPIC 03485: Configure Operation - Edit IVI Scope Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-operation-edit-ivi-scope-step-dialo7.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-operation-edit-ivi-scope-step-dialo7.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Operation The Configure operation configures an oscilloscope for a typical waveform measurement. An instrument acquires a waveform at a configurable interval, sequentially in real-time sampling, or interleaved from multiple waveform acquisitions in equivalent-time sampling. You can also co

### Configure Operation - Edit IVI Scope Step Dialog Box

#### Configure Operation

The Configure operation configures an oscilloscope for a typical waveform measurement. An instrument acquires a waveform at a configurable interval, sequentially in real-time sampling, or interleaved from multiple waveform acquisitions in equivalent-time sampling. You can also configure the instrument to perform more complex acquisitions, such as average, envelope, and peak detect using trigger types such as TV, runt, and glitch.

Note

The Edit IVI Scope Step dialog box for the Configure operation contains the following tabs:

- Basic 
 —The type of acquisition the oscilloscope performs.
- Advanced 
 —Low, middle, and high references for waveform measurements.
- Channels 
 —The channel names and their settings to configure.
- Trigger 
 —The trigger settings for the oscilloscope.
- Extensions 
 —The extensions to enable in the dialog box.
- Operation Settings 
 —Specifies where the dialog box saves and reloads the operation settings.

Parent topic:

Edit IVI Scope Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-package-attributes-dialog-box.html language=enus -->
## TOPIC 03486: Configure Package Attributes Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-package-attributes-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-package-attributes-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Launch the TestStand Deployment Utility and click Configure Package Attributes on the Package Distribution Options tab to launch the Configure Package Attributes dialog box. The Configure Package Attributes dialog box contains the following options: Version Number —Current software version number th

### Configure Package Attributes Dialog Box

Launch the TestStand Deployment Utility and click
 Configure Package Attributes
 on the Package Distribution Options tab to launch the Configure Package Attributes dialog box.

The Configure Package Attributes dialog box contains the following options:

- Version Number 
 —Current software version number that NI Package Manager uses to determine the action to perform when a package is already installed on a computer on which you want to deploy a test system. Increment the version number when you change the contents of the installer to ensure that the package overwrites previous versions of the package that exist on the test station computer.
 Note 
 This control is disables when the Auto Increment option is enabled.
  - Auto Increment 
 —Indicates whether the deployment utility automatically increases the version number when you build a package to ensure the package upgrades previous versions of the package on the test station computer. This control is enabled by default. Enabling this control disables the Version control.
 Note 
 You must save the deployment before closing the deployment utility to reain the new version number.
  - Lock to Deployment Version 
 —Forces the package to use the same version number as the software version number the deployment utility uses to identify the deployment. If you enable this option, the Version option on the Mode tab determines the installer version number, and the deployment utility automatically increments the package version number each time you build the installer.
- Package Name 
 —Displays the generated package name for the product. This field cannot be configured, and is generated based on the Company and Product Name fields. NI Package Manager uses this field to uniquely identify packages.
- Category 
 —Configures the category for the package, which is shown in NI Package Manager in the category column. If you select Infrastructure, the package will be hidden by default in NI Package Manager.
- Package Synopsis 
 —A single line summary of the package.
- Description 
 —A detailed multi-line description of the package.
- Maintainer 
 —The person, organization, or company responsible for maintaining the package.
- Contact Email 
 —The email address used to contact the package maintainer.
- Homepage 
 —Specifies a URL that provides more information about the package.
- Custom License Agreement 
 —Specify a rich text file (*.rtf) containing a custom license agreement. When installing the package, the user will be prompted to read and accept this agreement.
- Include NI Certificates Package 
 —Enable this option to include the NI Certificates package in the package distribution, which reduces the number of prompts during installation of the package. This option applies only to the Repository and package Installer output types, and is not available for the Single Package output type.
- Display in the Runtime Deployment Packages List 
 —Configures whether the package is shown in package builders, which only display runtime packages. Typically, you enable this for packages you intend to redeploy as a dependency of other packages.

#### See Also

[Advanced Installer Options dialog box](advanced-installer-options-dialog-box.html)

[Custom Commands dialog box](custom-commands-dialog-box.html)

[Deploying TestStand Systems](/csh?context=ts_10203)

[Drivers and Components dialog box](drivers-and-components-dialog-box.html)

Licensing Options for TestStand Systems
 section of Chapter 1,
 Introduction to TestStand
 , of the
 [Getting Started with TestStand](/csh?context=ts_8010)
 manual

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Package Distribution Tab - TestStand Deployment Utility

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-parameter-filter-dialog-box.html language=enus -->
## TOPIC 03487: Configure Parameter Filter Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-parameter-filter-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-parameter-filter-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Check or uncheck parameters using a filter button on the Additional Results panel and select the Configure Parameter Filter menu item to launch the Configure Parameter Filter dialog box in the TestStand Sequence Editor . Click the Check or uncheck parameters using a filter button in the Ad

### Configure Parameter Filter Dialog Box

Click the
 Check or uncheck parameters using a filter
 button on the
 [Additional Results panel](additional-results-panel-step-settings-pane.html)
 and select the
 Configure Parameter Filter
 menu item to launch the Configure Parameter Filter dialog box in the
 [TestStand Sequence Editor](/csh?context=ts_tsref_seqeditor)
 . Click the
 Check or uncheck parameters using a filter
 button in the
 [Additional Results](additional-results-dialog-box.html)
 dialog box and select the
 Configure Parameter Filter
 menu item to launch the Configure Parameter Filter dialog box in a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

Use this dialog box to specify the parameter results you normally do not want to log. Then enable the
 Check Non-Filtered Parameters
 or
 Uncheck Filtered Parameters
 options in this dialog box to log or not log parameters according to the specified filter. You can also click the
 Check or uncheck parameters using a filter
 button on the Additional Results panel or in the Additional Results dialog box and select the
 Check Non-Filtered Parameters
 or
 Uncheck Filtered Parameters
 menu items to log or not log parameters according to the specified filter.

The Configure Parameter Filter dialog box contains the following options:

- Select parameters to filter out 
 —Contains the categories of parameters you can include in the filter.
  - [In] Parameters 
 —Enable to filter out
 [In] 
 parameters.
  - [Out] Parameters 
 —Enable to filter out
 [Out] 
 parameters.
  - Subproperties of Step.Result 
 —Enable to filter out properties that are subproperties of
 Step.Result 
 , such as
 Step.Result.Numeric 
 . You normally do not need to log subproperties of
 Step.Result 
 because TestStand already copies subproperties of
 Step.Result 
 to the result list.
  - Object References 
 —Enable to filter out Object Reference objects.
  - Uncopyable Objects (e.g. Sequence Context) 
 —Enable to filter out objects TestStand cannot copy to the result list. Objects TestStand cannot copy include the
 SequenceContext 
 ,
 Execution 
 ,
 Thread 
 , and
 Report 
 objects. When TestStand logs one of these objects, TestStand logs a string description of the object instead of a copy of the object.
- On OK 
 —The action you want to take after you specify the parameters to include in the filter.
  - Check Non-Filtered Parameters 
 —Places a checkmark in all parameters not included in the parameter filter when you click
 OK 
 .
  - Uncheck Filtered Parameters 
 —Removes the checkmark from all parameters included in the parameter filter when you click
 OK 
 .

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Additional Results Panel](additional-results-panel-step-settings-pane.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-preconfigured-additional-results-di.html language=enus -->
## TOPIC 03488: Configure Preconfigured Additional Results Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-preconfigured-additional-results-di.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-preconfigured-additional-results-di.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Preconfigured Additional Results from the context menu for the Advanced button on the General tab of the Step Type Properties dialog box to launch the Configure Preconfigured Additional Results dialog box. This dialog box has the same appearance and behavior as the Additional Results dialog b

### Configure Preconfigured Additional Results Dialog Box

Select
 Preconfigured Additional Results
 from the context menu for the
 Advanced
 button on the
 [General](general-tab-step-type-properties-dialog-box.html)
 tab of the
 [Step Type Properties](step-type-properties-dialog-box.html)
 dialog box to launch the Configure Preconfigured Additional Results dialog box. This dialog box has the same appearance and behavior as the
 [Additional Results](additional-results-dialog-box.html)
 dialog box, except that this dialog box edits the preconfigured custom additional results for the step type.

Use this dialog box to define additional preconfigured custom additional results for instances of this step type. The preconfigured custom additional results menu appears for step instances when you click the
 Add Result From List
 or
 Select Result From List
 button on the
 [Additional Results panel](additional-results-panel-step-settings-pane.html)
 of the
 [Step Settings](step-settings-pane.html)
 pane and in the Additional Results dialog box. The preconfigured custom additional results menu contains standard items for every step type plus any additional step type specific items you define in this dialog box.

If the step type defines multiple operations and some preconfigured custom additional results only apply to certain operations, add those items to the
 [Step.AdditionalResultsHints](../tsapiref/step-additionalresultshints.html)
 property programmatically in the Edit substep for this step type when the user changes the operation of the step instance instead of adding those items in this dialog box. The items the
 Step.AdditionalResultsHints
 property defines also appear in the preconfigured custom additional results menu for step instances.

#### See Also

[Additional Results dialog box](additional-results-dialog-box.html)

[Step.AdditionalResultsHints](../tsapiref/step-additionalresultshints.html)

[Step Settings Pane](step-settings-pane.html)

[Step Type Properties dialog box](step-type-properties-dialog-box.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-property-node-dialog-box.html language=enus -->
## TOPIC 03489: Configure Property Node Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-property-node-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-property-node-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: On the LabVIEW Module tab, select Property Node Call from the Call Type ring control and click the Configure Settings for Property Node button to launch the Configure Property Node dialog box, which you can use to configure the Property Node call . You must configure a Property Node call before addi

### Configure Property Node Dialog Box

LabVIEW Module

Property Node Call

Configure Settings for Property Node

[IMAGE alt='image' src='../images/propnode.gif']

configure the Property Node call

Note

The Configure Property Node dialog box contains the following options:

- Project Path 
 —The path of the LabVIEW project the step uses. The control contains a most recently used (MRU) list of the last five selected LabVIEW projects. Specifying a LabVIEW project is optional.
- Property Node Type 
 —Specifies the I/O Reference type. Select
 LabVIEW Class 
 as the I/O Reference type to enable the LabVIEW
 Class Path 
 control.
 Note 
 Modifying the Property Node Type control clears any previously selected properties.
- Create LabVIEW Project 
 —Creates an empty LabVIEW project. If the LabVIEW project you specify does not already exist, the LabVIEW Adapter creates it. If the file already exists, the LabVIEW Adapter prompts you to overwrite the existing file.
- Edit LabVIEW Project 
 —Edits an existing LabVIEW project.
- Edit LabVIEW Class 
 —Edits an existing LabVIEW class.
- Property Node Class 
 —Specifies the I/O Reference class.
- Use Data Value Reference (DVR) 
 —When you enable this control, the property call uses a LabVIEW class in a DVR instead of the LabVIEW class. This option is only available when you select a LabVIEW class.
- Ignore internal Property Node errors 
 —When you enable this option, the Property Node continues processing the remaining properties of the Property Node if it encounters an error while accessing one of these properties.
- Available Properties 
 —Enter a search string to filter the Available Properties list. TestStand displays only the properties which contain the string.
- Available Properties List 
 —Lists the properties available for the currently selected I/O Reference type or LabVIEW class.
- Selected Properties 
 —Lists the selected properties.
 Note 
 LabVIEW allows a maximum of 24 properties in one Property Node step.
  - Property Icon 
 —Selects a property row without activating the controls in the list.
  - Property Name 
 —Specifies the name of the property.
  - Direction 
 —
Specifies the direction of the property. Possible values include
 In 
 and
 Out 
 . Some properties may also support the
 Default 
 direction.
- Add to Selected Properties 
 —Moves the properties selected in the Available Properties list to the bottom of the Selected Properties list. Selected properties use the In direction by default, unless the selected properties are read-only.
- Add Next property 
 —When you have selected a property in the Selected Properties list, click
 Add Next Property 
 to move the next property in the Available Properties list to the Selected Properties list. The newly added property appears in the list immediately after the selected property. If no properties are selected in either the Available Properties or Selected Properties lists, TestStand moves the first property in the Available Properties list to the end of the Selected Properties list. If you select an item in the Available Properties list, TestStand moves that property from the Available Properties list to the end of the Selected Properties list. The Add Next control is enabled by default. TestStand disables the control if there are no available properties to select.
 Note 
 You can use the Search text box to filter the list of available properties. However, the Add Next Property control uses the full, unfiltered list of available properties to determine the order in which to add properties to the Selected Properties list.
- Remove from Selected Properties 
 —Removes the properties selected in the Selected Properties list.
- Move Selected Properties Up 
 —Moves all selected properties higher in the Selected Properties list.
- Move Selected Properties Down 
 —Moves all selected properties lower in the Selected Properties list.
- Description for 
 —Displays the LabVIEW description of the first selected property in the Available Properties list or the Selected Properties list.
- LabVIEW VI Help 
 —Launches the LabVIEW help topic for the selected property.
- OK 
 —Saves the selected configuration to the step and creates the Property Node Call VI.
- Cancel 
 —Closes the Configure Property Node dialog box and discards any unsaved changes.

#### See Also

[Calling LabVIEW Property Nodes from TestStand](/csh?context=ts_tslabview_property_node)

[LabVIEW Module Tab](labview-module-tab.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-scan-operation-ivi-switching-mode-e.html language=enus -->
## TOPIC 03490: Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-scan-operation-ivi-switching-mode-e.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-scan-operation-ivi-switching-mode-e.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Scan Operation (IVI Switching Mode) Scan Details Tab The Scan Details tab for the Configure Scan operation contains the following options: Advanced Output —Specifies where the instrument routes the scan advanced output trigger. This trigger asserts each time the instrument creates a path.

### Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Configure Scan Operation (IVI Switching Mode)

#### Scan Details Tab

The Scan Details tab for the Configure Scan operation contains the following options:

- Advanced Output 
 —Specifies where the instrument routes the scan advanced output trigger. This trigger asserts each time the instrument creates a path. This trigger must not assert until sufficient settling time is provided for the path.
 
 Supported Value
 DescriptionNone (0)
 No trigger is sent out of the switch module.
 External (2)
 The switch sends a trigger to an external device through a trigger output connection.
 GPIB SRQ (5)
 The switch sends a GPIB SRQ event.
 TTL0 (111)
 The switch asserts TTL0.
 TTL1 (112)
 The switch asserts TTL1.
 TTL2 (113)
 The switch asserts TTL2.
 TTL3 (114)
 The switch asserts TTL3.
 TTL4 (115)
 The switch asserts TTL4.
 TTL5 (116)
 The switch asserts TTL5.
 TTL6 (117)
 The switch asserts TTL6.
 TTL7 (118)
 The switch asserts TTL7.
 ECL0 (119)
 The switch asserts ECL0 line.
 ECL1 (120)
 The switch asserts ECL1 line.
 PXI Star (125)
 The switch asserts PXI Star trigger bus.
 RTSI0 (140)
 The switch asserts RTSI0.
 RTSI1 (141)
 The switch asserts RTSI1.
 RTSI2 (142)
 The switch asserts RTSI2.
 RTSI3 (143)
 The switch asserts RTSI3.
 RTSI4 (144)
 The switch asserts RTSI4.
 RTSI5 (145)
 The switch asserts RTSI5.
 RTSI6 (146)
 The switch asserts RTSI6.
- Mode 
 —Specifies whether the connections made in the previous trigger event must be broken, and if so, how they must be broken.
 
 Supported Value
 DescriptionNo Action (0)
 Indicates no action must be taken on the previous paths.
 Break Before Make (1)
 Breaks the previous path before making the new path. This is useful when you want to prevent two channels from connecting together in the transitional period.
 Break After Make (2)
 Makes a new path before breaking the previous path. This is useful when you want to prevent damage from occurring on inductive elements of a circuit that cannot stand rapid changes in the current flow.
- Software Mode 
 —Specifies whether the scan is executed in hardware or software.
 
 Supported Value
 DescriptionDisable (0)
 Assures hardware scanning. If hardware scanning fails, the attempt to scan fails.
 Allow (1)
 Attempts hardware scanning. If hardware scanning fails, attempts software scanning.
 Force (2)
 Assures software scanning. There is no attempt to scan with hardware.
- Trigger Input 
 —The source of the trigger input. The trigger tells the switch module to advance to the next entry in the scan list and set the specified path.
 
 Supported Value
 DescriptionImmediate (1)
 The switch module does not wait for a trigger before starting the next entry in the scan list. You typically use this option for switch modules that support the Scan Delay option and can therefore have the switch module pace itself.
 External (2)
 The trigger comes from an external source through a trigger input connection.
 Software (3)
 The switch waits for a trigger until the Send Software Trigger operation executes.
 TTL0 (111)
 The switch waits for a trigger on TTL0.
 TTL1 (112)
 The switch waits for a trigger on TTL1.
 TTL2 (113)
 The switch waits for a trigger on TTL2.
 TTL3 (114)
 The switch waits for a trigger on TTL3.
 TTL4 (115)
 The switch waits for a trigger on TTL4.
 TTL5 (116)
 The switch waits for a trigger on TTL5.
 TTL6 (117)
 The switch waits for a trigger on TTL6.
 TTL7 (118)
 The switch waits for a trigger on TTL7.
 ECL0 (119)
 The switch waits for a trigger on the ECL0 line.
 ECL1 (120)
 The switch waits for a trigger on the ECL1 line.
 PXI Star (125)
 The switch waits for a trigger on the PXI Star trigger bus.
 RTSI0 (140)
 The switch waits for a trigger on RTSI0.
 RTSI1 (141)
 The switch waits for a trigger on RTSI1.
 RTSI2 (142)
 The switch waits for a trigger on RTSI2.
 RTSI3 (143)
 The switch waits for a trigger on RTSI3.
 RTSI4 (144)
 The switch waits for a trigger on RTSI4.
 RTSI5 (145)
 The switch waits for a trigger on RTSI5.
 RTSI6 (146)
 The switch waits for a trigger on RTSI6.
- Delay 
 —The minimum length of time, in milliseconds, from when the path is created to when the scan advanced output trigger is asserted.
 Note 
 Because of the design of the switch module, the actual delay time may be longer than the scan delay value.
- Continuous 
 —When you enable this option, the scan restarts from the beginning of the scan list when it reaches the end of the scan list.

Parent topic:

Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-scan-operation-ivi-switching-mode-e2.html language=enus -->
## TOPIC 03491: Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-scan-operation-ivi-switching-mode-e2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-scan-operation-ivi-switching-mode-e2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Scan Operation (IVI Switching Mode) Scan List Tab Use the Scan List tab to build a list of scanning actions. Scanning actions include connecting a path, disconnecting a path, and waiting for a trigger. The Scan List tab for the Configure Scan operation contains the following options: Sourc

### Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Configure Scan Operation (IVI Switching Mode)

#### Scan List Tab

Use the Scan List tab to build a list of scanning actions. Scanning actions include connecting a path, disconnecting a path, and waiting for a trigger.

The Scan List tab for the Configure Scan operation contains the following options:

- Source 
 —The name of the Source channel you are connecting or disconnecting. The string expression must evaluate at run time to a valid virtual channel name as the IVI configuration tool for the logical name being used defines.
- Destination 
 —The name of the Destination channel you are connecting or disconnecting. The string expression must evaluate at run time to a valid virtual channel name as the IVI configuration tool for the logical name being used defines.
 Use the following three buttons, located below the Destination control, to insert new items into the Scan List listbox: 
 
 You can reorder the items in the scan list using the up and down arrow buttons located below the Scan List listbox. Click
 Delete 
 to remove an item from the list.
  - Connect 
 —Inserts a connect path item into the scan list using the specified Source and Destination channels.
  - Disconnect 
 —Inserts a disconnect path item into the scan list using the specified Source and Destination channels.
  - Wait for Trigger 
 —Inserts a wait for trigger item into the scan list.

Parent topic:

Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-scan-operation-ivi-switching-mode-e3.html language=enus -->
## TOPIC 03492: Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-scan-operation-ivi-switching-mode-e3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-scan-operation-ivi-switching-mode-e3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Scan Operation (IVI Switching Mode) Operation Settings Tab The Operation Settings tab specifies to which property or variable the step saves the operation when closing the Edit IVI Switch Step dialog box. The Operation Settings tab for the Configure Scan operation contains the following op

### Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Configure Scan Operation (IVI Switching Mode)

#### Operation Settings Tab

The Operation Settings tab specifies to which property or variable the step saves the operation when closing the Edit IVI Switch Step dialog box.

The Operation Settings tab for the Configure Scan operation contains the following option:

- Settings Property/Variable 
 —Specifies which property or value reloads the operation settings when launching the Edit Step dialog box.

Parent topic:

Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-scan-operation-ivi-switching-mode-e4.html language=enus -->
## TOPIC 03493: Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-scan-operation-ivi-switching-mode-e4.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-scan-operation-ivi-switching-mode-e4.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Scan Operation (IVI Switching Mode) The Configure Scan operation configures the switch module for scanning the step specifies. The switch module must support the IVI Scanner extension. You can set the scan list on the Scan List tab and set other scan related options on the Scan Details tab

### Configure Scan Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Configure Scan Operation (IVI Switching Mode)

The Configure Scan operation configures the switch module for scanning the step specifies. The switch module must support the IVI Scanner extension. You can set the scan list on the Scan List tab and set other scan related options on the Scan Details tab. Once you configure the scan list, you must use the Start Scan operation to instruct the instrument to initiate the scan.

The Edit IVI Switch Step dialog box for the Configure Scan operation in IVI Switching mode contains the following tabs:

- Scan List Tab 
 —The list of connect, disconnect, and wait for trigger items in the scan list.
- Scan Details Tab 
 —Trigger-related settings for the scan list.
- Operation Settings Tab 
 —Specifies where the dialog saves and reloads the operation settings.

Parent topic:

IVI Switching Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-select-dialog-box.html language=enus -->
## TOPIC 03494: Configure Select Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-select-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-select-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Configure Select in the context menu for the step or click Configure Select on the General tab of the Step Properties dialog box to launch the Configure Select dialog box from a TestStand User Interface . The Configure Select dialog box contains the following options: Item to Compare —The exp

### Configure Select Dialog Box

Select
 Configure Select
 in the context menu for the step or click
 Configure Select
 on the
 [General](general-tab-step-properties-dialog-box.html)
 tab of the
 [Step Properties](step-properties-dialog-box.html)
 dialog box to launch the Configure Select dialog box from a
 [TestStand User Interface](teststand-user-interfaces.html)
 .

The Configure Select dialog box contains the following options:

- Item to Compare 
 —The expression that determines which Case block within the Select block executes.
- Case Sensitive (for string values) 
 —Specifies whether to use a case-sensitive string comparison when the value for the step contains strings. The default value is
 OFF 
 , or case-insensitive.

#### See Also

[Flow Control Step Types](flow-control-step-types.html)

[Step Properties dialog box](step-properties-dialog-box.html)

Parent topic:

Select Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-sequence-analyzer-available-rules-d.html language=enus -->
## TOPIC 03495: Configure Sequence Analyzer Available Rules Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-sequence-analyzer-available-rules-d.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-sequence-analyzer-available-rules-d.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Click the Available Rules button in the Sequence Analyzer Options dialog box in the TestStand Sequence Editor or click Available Rules on the toolbar in the stand-alone TestStand Sequence Analyzer application to launch the Configure Sequence Analyzer Available Rules dialog box, in which you create a

### Configure Sequence Analyzer Available Rules Dialog Box

Available Rules

Sequence Analyzer Options

TestStand Sequence Editor

Available Rules

toolbar

TestStand Sequence Analyzer application

analyzer rules

analysis modules

Note

ConfigApp user privilege

The Configure Sequence Analyzer Available Rules dialog box contains the following tabs and controls:

- Rules 
 —Adds, removes, and edits custom rules on the computer.
- Analysis Modules 
 —Adds, removes, and edits custom analysis modules on the computer.
- Export 
 —Launches the
 Export Items to File 
 dialog box, in which you can export custom rules and analysis module specifications from the computer to a rules file.
- Import 
 —Launches the
 Import Items from File 
 dialog box, in which you can import custom rules and analysis module specifications from a rules file to the computer.

Click
 OK
 to save the edits to the custom rules file, located at
 [<TestStand Application Data>](/csh?context=ts_tsfundamentals_directories)
 \Cfg\CustomRules.tsarules
 .

#### See Also

[Creating Analysis Modules for Custom Rules](/csh?context=ts_tsref_sa_creating_analysis_modules)

[Creating Custom Rules](/csh?context=ts_tsref_sa_creating_custom_rules)

[Export Items to File dialog box](export-items-to-file-dialog-box.html)

[Import Items from File dialog box](import-items-from-file-dialog-box.html)

[Sequence Analyzer Options dialog box](sequence-analyzer-options-dialog-box.html)

[TestStand Sequence Analyzer Application](teststand-sequence-analyzer-application.html)

[Toolbar Buttons and Shortcuts](toolbar-buttons-and-shortcuts-teststand-seque.html)

[User and Group Privileges](user-and-group-privileges.html)

Parent topic:

TestStand Environment Reference Help

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-sweep-loop-dialog-box.html language=enus -->
## TOPIC 03496: Configure Sweep Loop Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-sweep-loop-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-sweep-loop-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sweep Parameters tab , Input tab , Output tab , and Loop Information tab in a TestStand User Interface to define a set of sweep parameters and a block of steps to sweep over. See Also Data Streams Step Types

### Configure Sweep Loop Dialog Box

Use the
 [Sweep Parameters tab](sweep-parameters-tab-configure-sweep-loop-dia.html)
 ,
 [Input tab](input-tab.html)
 ,
 [Output tab](output-tab.html)
 , and
 [Loop Information tab](loop-information-tab2.html)
 in a
 [TestStand User Interface](teststand-user-interfaces.html)
 to define a set of sweep parameters and a block of steps to sweep over.

#### See Also

[Data Streams Step Types](/csh?context=ts_tsref_data_streams_types)

Parent topic:

Sweep Loop Step

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-switch-operation-ivi-switching-mode.html language=enus -->
## TOPIC 03497: Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-switch-operation-ivi-switching-mode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-switch-operation-ivi-switching-mode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Switch Operation (IVI Switching Mode) Channels Tab If you specify a column-to-column connection in a matrix, the specific driver typically must use at least a one row channel to create the connection. Specifying a channel as a Configuration channel allows the instrument driver to use the c

### Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Configure Switch Operation (IVI Switching Mode)

#### Channels Tab

If you specify a column-to-column connection in a matrix, the specific driver typically must use at least a one row channel to create the connection. Specifying a channel as a Configuration channel allows the instrument driver to use the channel to create the path.

If you attempt to connect two channels that are either sources or have their own connections to sources, the path creation operation returns an error. The term source can be from either the instrument or the UUT perspective. As a result, the driver must ensure for each connection that another connection within the switch module does not connect to another source. Defining a channel as a source prevents connection with channels that may cause damage to the channels, devices, or system.

The Channels tab for the Configure Switch operation contains the following channel-specific options:

- Name 
 —The name of a channel. The channel name must evaluate to be a valid virtual channel name as the IVI configuration tool for the logical name being used defines.
- Type 
 —The type of channel for which the state is set.
 
 Supported Value
 DescriptionConfiguration (0)
 The specific driver reserves the channel as a Configuration channel for internal path creation.
 Source (1)
 The specific driver reserves the channel as a Source channel.
- State 
 —Specifies whether the Configuration or Source channel state is set or reset. A value of
 True 
 adds the channel to the configuration or source channel list. A value of
 False 
 removes the channel from either the Configuration or Source channel list.

The Channels tab also contains a listbox with a list of channels. Use the
 Add
 and
 Remove
 buttons to add new channels and remove existing ones. You can also specify whether to set or reset the state of the channel as either a Configuration or a Source channel.

Parent topic:

Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-switch-operation-ivi-switching-mode2.html language=enus -->
## TOPIC 03498: Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-switch-operation-ivi-switching-mode2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-switch-operation-ivi-switching-mode2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Switch Operation (IVI Switching Mode) Path Tab Because of issues like calibration, you may want to have deterministic control over the path the instrument creates between two channels. Use the Paths tab to specify the exact path, in terms of the Configuration channels used, to create. The

### Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Configure Switch Operation (IVI Switching Mode)

#### Path Tab

Because of issues like calibration, you may want to have deterministic control over the path the instrument creates between two channels. Use the Paths tab to specify the exact path, in terms of the Configuration channels used, to create.

The instrument creates a connection between the channels using Configuration channels. These intermediary steps are called the legs of the path. The format of the leg of the path is
 "ch1->conf1"
 , where the
 "ch1"
 and
 "conf1"
 are the two channels used to establish the connection between the first and the last channel. The path syntax is a comma-delimited list of path legs that obey the following rules:

- The second channel of a leg in the path must be the same as the first channel in the subsequent leg.
- Every channel in the path, other than the first and last channels, must be Configuration channel.

An example of a path is:
 "ch1->conf1,conf1->ch2"
 .

This string is not interchangeable because the names of switches within the switch module are not required to be interchangeable and depend on the internal architecture of the switch module.

The Path tab for the Configure Switch operation contains the following channel-specific option:

- Expression 
 —The expression TestStand evaluates at run time to determine the path set.

The Path tab also contains a listbox with a list of paths. The display name in the listbox contains the end channel names from the specified paths. Use the
 Add
 and
 Remove
 buttons to add new paths and remove existing paths from the list.

Parent topic:

Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-switch-operation-ivi-switching-mode3.html language=enus -->
## TOPIC 03499: Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-switch-operation-ivi-switching-mode3.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-switch-operation-ivi-switching-mode3.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure Switch Operation (IVI Switching Mode) The Configure Switch operation in IVI Switching mode configures channels as Configuration or Source channels and configures specific paths between channels. The Edit IVI Switch Step dialog box for the Configure Switch operation in IVI Switching mode co

### Configure Switch Operation (IVI Switching Mode) - Edit IVI Switch Step Dialog Box

#### Configure Switch Operation (IVI Switching Mode)

The Configure Switch operation in IVI Switching mode configures channels as Configuration or Source channels and configures specific paths between channels.

The Edit IVI Switch Step dialog box for the Configure Switch operation in IVI Switching mode contains the following tabs:

- Channels Tab 
 —Specifies which channels are configuration or source channels.
- Path Tab 
 —Sets specific paths between channels.

Parent topic:

IVI Switching Mode - Edit IVI Switch Step Dialog Box

<!--NI_TOPIC bundle=teststand-api-reference path=tsref/configure-type-palettes-dialog-box.html language=enus -->
## TOPIC 03500: Configure Type Palettes Dialog Box

- bundle_id: `teststand-api-reference`
- source_path: `tsref/configure-type-palettes-dialog-box.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsref/configure-type-palettes-dialog-box.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Select Customize Type Palettes from the context menu of the Type Files control of the Type Palettes document to launch the Configure Type Palettes dialog box, in which you can specify which type palette files TestStand loads and the order in which they appear in the list. The Configure Type Palettes

### Configure Type Palettes Dialog Box

Select
 Customize Type Palettes
 from the context menu of the Type Files control of the Type Palettes document to launch the Configure Type Palettes dialog box, in which you can specify which type palette files TestStand loads and the order in which they appear in the list.

The Configure Type Palettes dialog box contains the following options:

- <
 Type Palette List
 > 
 —The type palette files TestStand loads in the order TestStand loads them.
- Create 
 —Creates a new type palette file and adds the file to the list.
- Add 
 —Adds an existing type palette file to the list.
- Remove 
 —Removes the selected file from the list.
- Move Up/Move Down 
 —Changes the order of the type palette files in the list.

Parent topic:

TestStand Environment Reference Help
