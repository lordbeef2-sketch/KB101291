# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=2251 end=2500 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparameter.html language=enus -->
## TOPIC 02251: PythonParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the PythonParameter class to configure and obtain parameter-specific information for an item in the PythonParameters collection class. Use the PythonModule.Parameters property to obtain the collection of parameters for a module. Properties Category ParameterName ValidEvaluationTypes

### PythonParameter

Use objects from the
 PythonParameter
 class to configure and obtain parameter-specific information for an item in the
 PythonParameters
 collection class. Use the
 PythonModule.Parameters
 property to obtain the collection of parameters for a module.

#### Properties

| Category |
| --- |
| ParameterName |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |

#### Method

| AsPropertyObject |
| --- |

#### See Also

[PythonParameters](pythonparameters.html)

[PythonModule.Parameters](pythonmodule-parameters.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparametercategories.html language=enus -->
## TOPIC 02252: PythonParameterCategories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparametercategories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparametercategories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the PythonParameter.Category property to specify the Python compatible data type that TestStand should consider for the parameter, return value, or attribute for the Python Adapter step. PythonParamCategory_Boolean –(Value: 0x3) Specifies that the parameter is a bool

### PythonParameterCategories

Use the following constants with the
 PythonParameter.Category
 property to specify the Python compatible data type that TestStand should consider for the parameter, return value, or attribute for the Python Adapter step.

- PythonParamCategory_Boolean 
 –(Value: 0x3) Specifies that the parameter is a boolean.
- PythonParamCategory_Dispatch 
 –(Value: 0x8) Specifies that the parameter is an object reference variable that stores either an ActiveX object that implements IDispatch or a TestStand object. You must install pywin32 in order to pass TestStand objects or ActiveX objects between TestStand and Python.
- PythonParamCategory_Dynamic 
 –(Value: 0x7) Specifies the type of the parameter is dynamically detected based on the input provided to the parameter.
- PythonParamCategory_Enum 
 –(Value: 0x9) Specifies that the parameter is an enum.
- PythonParamCategory_List 
 –(Value: 0x5) Specifies that the TestStand array passes to the Python module as a list.
- PythonParamCategory_None 
 –(Value: 0x0) Specifies that the parameter is a None parameter, meaning it has no value. This category applies only to return value.
- PythonParamCategory_Numeric 
 –(Value: 0x1) Specifies that the parameter is a number.
- PythonParamCategory_NumPyArray 
 –(Value: 0x10) Specifies that the TestStand array passes to the Python module as a NumPy array.
- PythonParamCategory_Object 
 –(Value: 0x6) Specifies that the parameter is a PyObject.
- PythonParamCategory_String 
 –(Value: 0x2) Specifies that the parameter is a string.
- PythonParamCategory_Tuple 
 –(Value: 0x4) Specifies that the parameter is a tuple.

#### See Also

[PythonParameter.Category](pythonparameter-category.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparameters-count.html language=enus -->
## TOPIC 02253: PythonParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax PythonParameters.Count Data Type Long Purpose Returns the number of items in the collection. See Also PythonParameter

### PythonParameters.Count

#### Syntax

[PythonParameters](pythonparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[PythonParameter](pythonparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparameters-delete.html language=enus -->
## TOPIC 02254: PythonParameters.Delete

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparameters-delete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparameters-delete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax PythonParameters.Delete( index) Purpose Removes the PythonParameter object located at the specified index. Parameters index As Long [In] Specifies the zero-based index of the parameter to delete.

### PythonParameters.Delete

#### Syntax

[PythonParameters](pythonparameters.html).Delete( index)

#### Purpose

Removes the
 PythonParameter
 object located at the specified index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to delete.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparameters-item.html language=enus -->
## TOPIC 02255: PythonParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax PythonParameters.Item( index) Data Type PythonParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also PythonParameter

### PythonParameters.Item

#### Syntax

[PythonParameters](pythonparameters.html).Item( index)

#### Data Type

[PythonParameter](pythonparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[PythonParameter](pythonparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparameters-move.html language=enus -->
## TOPIC 02256: PythonParameters.Move

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparameters-move.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparameters-move.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax PythonParameters.Move( index, newIndex) Purpose Moves a PythonParameter object within a collection. Parameters index As Long [In] Specifies the zero-based index indicating the current position of the parameter to move. newIndex As Long [In] Specifies the zero-based index indicating the new po

### PythonParameters.Move

#### Syntax

[PythonParameters](pythonparameters.html).Move( index, newIndex)

#### Purpose

Moves a
 PythonParameter
 object within a collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index indicating the current position of the parameter to move.

newIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index indicating the new position of the parameter.

#### See Also

[PythonParameter](pythonparameter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparameters-new.html language=enus -->
## TOPIC 02257: PythonParameters.New

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparameters-new.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparameters-new.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax PythonParameters.New( index, parameterName, parameterValueExpr, parameterCategory) Purpose Adds a new parameter to the collection. Parameters index As Long [In] Specifies the zero-based index of where to insert the parameter. parameterName As String [In] Specifies the name assigned to the new

### PythonParameters.New

#### Syntax

[PythonParameters](pythonparameters.html).New( index, parameterName, parameterValueExpr, parameterCategory)

#### Purpose

Adds a new parameter to the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of where to insert the parameter.

parameterName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name assigned to the new parameter.

parameterValueExpr
 As
 [String](data-types-for-teststand.html)

[In] Specifies the argument expression.

If the parameter is an input, this expression corresponds to the value to pass. If the parameter is a return value or returned property, this expression specifies where TestStand stores the result value.

parameterCategory
 As
 [PythonParameterCategories](pythonparametercategories.html)

[In] Specifies the parameter category.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/pythonparameters.html language=enus -->
## TOPIC 02258: PythonParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/pythonparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/pythonparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the PythonParameters class to configure and obtain parameters for a module that uses the Python Adapter. Use the PythonModule.Parameters property to obtain the collection of parameters for a module. Properties Count (Read Only) Item (Read Only) Methods Delete Move New See Also Pytho

### PythonParameters

Use objects from the
 PythonParameters
 class to configure and obtain parameters for a module that uses the Python Adapter. Use the
 PythonModule.Parameters
 property to obtain the collection of parameters for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Delete |
| --- |
| Move |
| New |

#### See Also

[PythonModule.Parameters](pythonmodule-parameters.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/readpropertyobjectfileoptions.html language=enus -->
## TOPIC 02259: ReadPropertyObjectFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/readpropertyobjectfileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/readpropertyobjectfileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the Engine.ReadPropertyObjectFile method. Use the bitwise-OR operator to specify more than one option. ReadPropertyObjectFileOption_None –(Value: 0x0) No options. ReadPropertyObjectFileOption_TypesOnly –(Value: 0x2) Pass this option to read only

### ReadPropertyObjectFileOptions

These constants represent the options you can use with the
 [Engine.ReadPropertyObjectFile](engine-readpropertyobjectfile.html)
 method. Use the bitwise-OR operator to specify more than one option.

- ReadPropertyObjectFileOption_None 
 –(Value: 0x0) No options.
- ReadPropertyObjectFileOption_TypesOnly 
 –(Value: 0x2) Pass this option to read only the types for the specified file. The method does not read the main data object when you select this option.

#### See Also

[Engine.ReadPropertyObjectFile](engine-readpropertyobjectfile.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/readwriteoptions.html language=enus -->
## TOPIC 02260: ReadWriteOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/readwriteoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/readwriteoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the RWOptions parameter of the methods that read and write PropertyObjects. Use the bitwise-OR operator to specify more than one option. RWOption_DoNotWriteTypes –(Value: 0x8) Do not write any type definitions when writing type definition instan

### ReadWriteOptions

These constants represent the options you can use with the
 RWOptions
 parameter of the methods that read and write PropertyObjects. Use the bitwise-OR operator to specify more than one option.

- RWOption_DoNotWriteTypes 
 –(Value: 0x8) Do not write any type definitions when writing type definition instances.

TestStand writes only values that are not the default value for a type. If you use the
 PropertyObject.ReadEx 
 or
 PropertyObject.UnserializeEx 
 methods to read the contents of a persisted object written using this option, the type definitions must already be loaded. If the types are no loaded, the
 PropertyObject.ReadEx 
 fails.
- RWOption_EraseAll 
 –(Value: 0x4) When writing an object to a file, use this option to clear the entire contents of the existing file.
- RWOption_EraseExistingObject 
 –(Value: 0x2) When writing an object, use this option to clear out any existing object with the same name.
- RWOption_NoOptions 
 –(Value: 0x0) No options.
- RWOption_ValuesOnly 
 –(Value: 0x1) Use this option to read or write the value of the object and the value of each subproperty. TestStand does not write the type information for the object and subproperties when you use this flag.

TestStand writes all values even if the value is the default value for a type. If you use
 PropertyObject.ReadEx 
 or
 PropertyObject.UnserializeEx 
 to read the contents of a persisted object written using this option, the structure of the target object must match the structure of the values read. If the target structure is incorrect, the values in the target object do not update.

#### See Also

[PropertyObject.ReadEx](propertyobject-readex.html)

[PropertyObject.Serialize](propertyobject-serialize.html)

[PropertyObject.UnserializeEx](propertyobject-unserializeex.html)

[PropertyObject.Write](propertyobject-write.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/releaseseqfileoptions.html language=enus -->
## TOPIC 02261: ReleaseSeqFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/releaseseqfileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/releaseseqfileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the Engine.ReleaseSequenceFileEx method. Use the bitwise-OR operator to specify more than one option. ReleaseSeqFile_DoNotRunUnloadCallback –(Value: 0x2) Use this option to prevent the SequenceFileUnload callback sequenc

### ReleaseSeqFileOptions

These constants represent the options you can use with the
 options
 parameter of the
 [Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)
 method. Use the bitwise-OR operator to specify more than one option.

- ReleaseSeqFile_DoNotRunUnloadCallback 
 –(Value: 0x2) Use this option to prevent the SequenceFileUnload callback sequence from running if the callback exists and the reference being released is the last reference. If other references exist to the sequence file, TestStand might execute the SequenceFileUnload callback when these references are released using the
 Engine.ReleaseSequenceFileEx 
 method. Regardless of whether you use this option, TestStand does not execute the SequenceFileUnload callback if the SequenceFileLoad callback was not executed because all references to the sequence file were obtained by passing the
 GetSeqFile_DoNotRunLoadCallback 
 option to the
 Engine.GetSequenceFileEx 
 method.

Use the
 SequenceFile.UnloadCallbackEnabled 
 property to prevent the SequenceFileUnload callback from ever being executed.
- ReleaseSeqFile_NoOptions 
 –(Value: 0x0) No options.
- ReleaseSeqFile_UnloadFile 
 –(Value: 0x4) Use this option to request TestStand to remove a sequence file from the internal cache of the engine. When you specify this option, it does not guarantee that TestStand removes the sequence file from the cache because there might be multiple references to it or it might be executing. If TestStand cannot remove a sequence file from the cache, the
 Engine.ReleaseSequenceFileEx 
 method generates an error. If your development environment requires you to explicitly release COM references, do not release the COM reference to a SequenceFile object until a call to the
 Engine.ReleaseSequenceFileEx 
 method succeeds. If you do not specify this option, TestStand might remove the sequence file from the cache if TestStand no longer needs the file.
- ReleaseSeqFile_UnloadFileIfModified 
 –(Value: 0x1) Use this option to remove a modified sequence file from the internal cache of the engine. If TestStand cannot remove a modified sequence file from the cache, the
 Engine.ReleaseSequenceFileEx 
 method generates an error. If your development environment requires you to explicitly release COM references, do not release the COM reference to a SequenceFile object until a call to the
 Engine.ReleaseSequenceFileEx 
 method succeeds.

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[GetSeqFileOptions](getseqfileoptions.html)

[SequenceFile.UnloadCallbackEnabled](sequencefile-unloadcallbackenabled.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-all.html language=enus -->
## TOPIC 02262: Report.All

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-all.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-all.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.All Data Type String Purpose Returns the entire report as a string. See Also Report.GetSection

### Report.All

#### Syntax

[Report](report.html).All

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the entire report as a string.

#### See Also

[Report.GetSection](report-getsection.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-append.html language=enus -->
## TOPIC 02263: Report.Append

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-append.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-append.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.Append( stringToAppend) Return Value Long Returns an index that refers to this append operation. Use this value with the Report.GetSection method. Calling the Report.Reset method invalidates the index. Purpose Appends a string to the report. Remarks TestStand releases any ReportSection

### Report.Append

#### Syntax

[Report](report.html).Append( stringToAppend)

#### Return Value

[Long](data-types-for-teststand.html)

Returns an index that refers to this append operation. Use this value with the
 [Report.GetSection](report-getsection.html)
 method. Calling the
 [Report.Reset](report-reset.html)
 method invalidates the index.

#### Purpose

Appends a string to the report.

#### Remarks

Note

ReportSection

Report

#### Parameters

stringToAppend
 As
 [String](data-types-for-teststand.html)

[In] Specifies the string to append to the report.

#### See Also

[Report.GetSection](report-getsection.html)

[Report.LatestAppendIndex](report-latestappendindex.html)

[Report.Reset](report-reset.html)

[ReportSection](reportsection.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-aspropertyobject.html language=enus -->
## TOPIC 02264: Report.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the Report object. Use the PropertyObject to modify, add, or remove custom properties for the object. See Also PropertyObject

### Report.AsPropertyObject

#### Syntax

[Report](report.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the Report object. Use the PropertyObject to modify, add, or remove custom properties for the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-format.html language=enus -->
## TOPIC 02265: Report.Format

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-format.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-format.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.Format Data Type String Purpose Specifies the file format of the report. Specify the file format by passing the file extension for that format, such as txt for ASCII text files, htm or html for HTML files, and rtf for rich text format files.

### Report.Format

#### Syntax

[Report](report.html).Format

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the file format of the report. Specify the file format by passing the file extension for that format, such as
 txt
 for ASCII text files,
 htm
 or
 html
 for HTML files, and
 rtf
 for rich text format files.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-getsection.html language=enus -->
## TOPIC 02266: Report.GetSection

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-getsection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-getsection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.GetSection( oldestIndex, latestIndex) Return Value String The content of the report that the index parameters specify. Purpose Returns a section of the report. Remarks After calling the Report.Append method multiple times, call this method to obtain the section of text associated with

### Report.GetSection

#### Syntax

[Report](report.html).GetSection( oldestIndex, latestIndex)

#### Return Value

[String](data-types-for-teststand.html)

The content of the report that the index parameters specify.

#### Purpose

Returns a section of the report.

#### Remarks

After calling the
 [Report.Append](report-append.html)
 method multiple times, call this method to obtain the section of text associated with the specified append index.

Note

ReportSection

Report

#### Parameters

oldestIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index of the
 [Report.Append](report-append.html)
 method that starts the section.

latestIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index of the
 [Report.Append](report-append.html)
 method that ends the section.

#### See Also

[Report.Append](report-append.html)

[Report.LatestAppendIndex](report-latestappendindex.html)

[Report.Reset](report-reset.html)

[ReportSection](reportsection.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-gettempfile.html language=enus -->
## TOPIC 02267: Report.GetTempFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-gettempfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-gettempfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.GetTempFile( linefeedConversion, [extensionString]) Return Value String The pathname of the temporary file used by this method to store the report. Purpose Stores the report in a temporary file and returns the pathname of the file. Parameters linefeedConversion As ReportConversion [In]

### Report.GetTempFile

#### Syntax

[Report](report.html).GetTempFile( linefeedConversion, [extensionString])

#### Return Value

[String](data-types-for-teststand.html)

The pathname of the temporary file used by this method to store the report.

#### Purpose

Stores the report in a temporary file and returns the pathname of the file.

#### Parameters

linefeedConversion
 As
 [ReportConversion](reportconversion.html)

[In] Specifies a linefeed conversion for the report text.

extensionString
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] String parameter that specifies the file extension for the temporary file. If you do not specify an extension string, the
 [Report.Format](report-format.html)
 property of the report determines the file extension.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Report.Format](report-format.html)

[Report.TempFileDirectory](report-tempfiledirectory.html)

[ReportConversion](reportconversion.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-id.html language=enus -->
## TOPIC 02268: Report.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.Id Data Type Long Purpose Returns a unique ID that distinguishes this report from all other reports. The ID number is never zero.

### Report.Id

#### Syntax

[Report](report.html).Id

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique ID that distinguishes this report from all other reports.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-isempty.html language=enus -->
## TOPIC 02269: Report.IsEmpty

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-isempty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-isempty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.IsEmpty Data Type Boolean Purpose Returns if the report is empty.

### Report.IsEmpty

#### Syntax

[Report](report.html).IsEmpty

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns if the report is empty.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-latestappendindex.html language=enus -->
## TOPIC 02270: Report.LatestAppendIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-latestappendindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-latestappendindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.LatestAppendIndex Data Type Long Purpose Returns the most recent index the Report.Append method returns. Remarks Use this value with the Report.GetSection method to obtain the last section of the report. When a ReportSection object is assigned to the Report object, this property return

### Report.LatestAppendIndex

#### Syntax

[Report](report.html).LatestAppendIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the most recent index the
 [Report.Append](report-append.html)
 method returns.

#### Remarks

Use this value with the
 [Report.GetSection](report-getsection.html)
 method to obtain the last section of the report.

Note

ReportSection

Report

#### See Also

[Report.Append](report-append.html)

[Report.GetSection](report-getsection.html)

[Report.Reset](report-reset.html)

[ReportSection](reportsection.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-launchviewer.html language=enus -->
## TOPIC 02271: Report.LaunchViewer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-launchviewer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-launchviewer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.LaunchViewer( linefeedConversion) Purpose Launches an external file viewer to allow the user to view the report. Remarks If the current TestStand configuration specifies an external viewer for the format, TestStand launches that viewer. Otherwise, TestStand launches the viewer that Mic

### Report.LaunchViewer

#### Syntax

[Report](report.html).LaunchViewer( linefeedConversion)

#### Purpose

Launches an external file viewer to allow the user to view the report.

#### Remarks

If the current TestStand configuration specifies an external viewer for the format, TestStand launches that viewer. Otherwise, TestStand launches the viewer that Microsoft Windows associates with the file extension the report format specifies.

#### Parameters

linefeedConversion
 As
 [ReportConversion](reportconversion.html)

[In] Specifies a linefeed conversion for the report text.

#### See Also

[Engine.ExternalReportViewers](engine-externalreportviewers.html)

[Engine.LaunchExternalViewer](engine-launchexternalviewer.html)

[ReportConversion](reportconversion.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-load.html language=enus -->
## TOPIC 02272: Report.Load

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-load.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-load.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.Load( pathString, linefeedConversion) Purpose Replaces the current report data with the data in the file you specify. Remarks Calling this method updates the Report.Location property. Parameters pathString As String [In] Specifies the pathname of the file that contains the report data.

### Report.Load

#### Syntax

[Report](report.html).Load( pathString, linefeedConversion)

#### Purpose

Replaces the current report data with the data in the file you specify.

#### Remarks

Calling this method updates the
 [Report.Location](report-location.html)
 property.

#### Parameters

pathString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the file that contains the report data.

linefeedConversion
 As
 [ReportConversion](reportconversion.html)

[In] Specifies a linefeed conversion for the report text.

#### See Also

[Report.Location](report-location.html)

[ReportConversion](reportconversion.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-location.html language=enus -->
## TOPIC 02273: Report.Location

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-location.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-location.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.Location Data Type String Purpose Specifies a string that indicates the display value for the report location. Remarks If you call the Report.Load or Report.Save method of this class, this property is automatically set to the pathname of the report file. You cannot use this property to

### Report.Location

#### Syntax

[Report](report.html).Location

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a string that indicates the display value for the report location.

#### Remarks

If you call the
 [Report.Load](report-load.html)
 or
 [Report.Save](report-save.html)
 method of this class, this property is automatically set to the pathname of the report file. You cannot use this property to set the location of the report.

#### See Also

[Report.Load](report-load.html)

[Report.Save](report-save.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-newreportsection.html language=enus -->
## TOPIC 02274: Report.NewReportSection

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-newreportsection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-newreportsection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.NewReportSection Return Value ReportSection Purpose Creates and returns a reference to a ReportSection object. Remarks The ReportSection object this method returns is empty. See Also ReportSection

### Report.NewReportSection

#### Syntax

[Report](report.html).NewReportSection

#### Return Value

[ReportSection](reportsection.html)

#### Purpose

Creates and returns a reference to a
 [ReportSection](reportsection.html)
 object.

#### Remarks

The
 ReportSection
 object this method returns is empty.

#### See Also

[ReportSection](reportsection.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-refreshdisplay.html language=enus -->
## TOPIC 02275: Report.RefreshDisplay

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-refreshdisplay.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-refreshdisplay.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.RefreshDisplay Purpose Call this method to refresh the ReportView control after you make changes to an associated Report.ReportSection object to indicate that a report has changed and that the user interface must be refreshed. Remarks Calling the Report.Append or Report.Reset methods o

### Report.RefreshDisplay

#### Syntax

[Report](report.html).RefreshDisplay

#### Purpose

Call this method to refresh the
 
 [ReportView](../tsuiref/reportview.html)
 control after you make changes to an associated
 [Report.ReportSection](report-reportsection.html)
 object to indicate that a report has changed and that the user interface must be refreshed.

#### Remarks

Calling the
 [Report.Append](report-append.html)
 or
 [Report.Reset](report-reset.html)
 methods or assigning a new reference to the
 Report.ReportSection
 property automatically refreshes the
 ReportView
 control. However, when you make changes to a
 ReportSection
 object already assigned to a
 Report.ReportSection
 property, the
 [Report](report.html)
 object does not automatically notify the
 ReportView
 control. You must call the
 Report.RefreshDisplay
 method to notify the
 ReportView
 control to refresh in this case.

#### See Also

[Report.Append](report-append.html)

[Report.ReportSection](report-reportsection.html)

[Report.Reset](report-reset.html)

[ReportView](../tsuiref/reportview.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-reportsection.html language=enus -->
## TOPIC 02276: Report.ReportSection

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-reportsection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-reportsection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.ReportSection Data Type ReportSection Purpose Specifies the ReportSection object associated with the Report object, which uses the report data stored in the ReportSection object as the report. If no ReportSection object was previously set, this property returns NULL . Remarks If you ca

### Report.ReportSection

#### Syntax

[Report](report.html).ReportSection

#### Data Type

[ReportSection](reportsection.html)

#### Purpose

Specifies the
 [ReportSection](reportsection.html)
 object associated with the
 Report
 object, which uses the report data stored in the
 ReportSection
 object as the report. If no
 ReportSection
 object was previously set, this property returns
 NULL
 .

#### Remarks

If you call the
 [Report.Append](report-append.html)
 ,
 [Report.Load](report-load.html)
 , or
 [Report.Reset](report-reset.html)
 methods, this property returns
 NULL
 .

If this property is set, the
 [Report.LatestAppendIndex](report-latestappendindex.html)
 method always returns
 -1
 .

Setting this property discards any report data set from prior calls to the
 Report.Append
 or
 Report.Reset
 methods.

#### See Also

[Report.Append](report-append.html)

[Report.LatestAppendIndex](report-latestappendindex.html)

[Report.Load](report-load.html)

[Report.Reset](report-reset.html)

[ReportSection](reportsection.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-reset.html language=enus -->
## TOPIC 02277: Report.Reset

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-reset.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-reset.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.Reset( newValue) Return Value Long Returns the number of times you have reset the report. Purpose Replaces the current report data with the data in the string you specify. Remarks This method sets the Report.LatestAppendIndex property to 0. Any ReportSection object assigned to the Repo

### Report.Reset

#### Syntax

[Report](report.html).Reset( newValue)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the number of times you have reset the report.

#### Purpose

Replaces the current report data with the data in the string you specify.

#### Remarks

This method sets the
 [Report.LatestAppendIndex](report-latestappendindex.html)
 property to 0.

Note

ReportSection

Report

#### Parameters

newValue
 As
 [String](data-types-for-teststand.html)

[In] Specifies the new report string.

#### See Also

[Report.LatestAppendIndex](report-latestappendindex.html)

[Report.ResetCount](report-resetcount.html)

[ReportSection](reportsection.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-resetcount.html language=enus -->
## TOPIC 02278: Report.ResetCount

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-resetcount.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-resetcount.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.ResetCount Data Type Long Purpose Returns the number of times you have reset the report. See Also Report.Reset

### Report.ResetCount

#### Syntax

[Report](report.html).ResetCount

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of times you have reset the report.

#### See Also

[Report.Reset](report-reset.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-save.html language=enus -->
## TOPIC 02279: Report.Save

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-save.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-save.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.Save( pathString, appendIfAlreadyExists, linefeedConversion) Purpose Saves the report to the file you specify. Remarks Calling this method updates the Report.Location property. If a ReportSection object is assigned to the report, this method saves the report obtained by calling the Rep

### Report.Save

#### Syntax

[Report](report.html).Save( pathString, appendIfAlreadyExists, linefeedConversion)

#### Purpose

Saves the report to the file you specify.

#### Remarks

Calling this method updates the
 [Report.Location](report-location.html)
 property.

Note

ReportSection

ReportSection.GetAllText

#### Parameters

pathString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the file in which to save the report.

appendIfAlreadyExists
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to append or overwrite the file if it already exists. Pass
 True
 to append to the file. Pass
 False
 to overwrite it.

linefeedConversion
 As
 [ReportConversion](reportconversion.html)

[In] Specifies a linefeed conversion for the report text.

#### See Also

[Report.Location](report-location.html)

[ReportConversion](reportconversion.html)

[ReportSection](reportsection.html)

[ReportSection.GetAllText](reportsection-getalltext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-settempfiledirectoryex.html language=enus -->
## TOPIC 02280: Report.SetTempFileDirectoryEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-settempfiledirectoryex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-settempfiledirectoryex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.SetTempFileDirectoryEx( directory, tempFileDirectoryOption = SetTempFileDirectoryOption_Default) Purpose Specifies the directory path where TestStand saves the file the Report.GetTempFile method creates. Remarks When you use the SetTempFileDirectoryOption_Default option with this metho

### Report.SetTempFileDirectoryEx

#### Syntax

[Report](report.html).SetTempFileDirectoryEx( directory, tempFileDirectoryOption = SetTempFileDirectoryOption_Default)

#### Purpose

Specifies the directory path where TestStand saves the file the
 [Report.GetTempFile](report-gettempfile.html)
 method creates.

#### Remarks

When you use the
 [SetTempFileDirectoryOption_Default](settempfiledirectoryoptions.html)
 option with this method, calling the
 [Report.Load](report-load.html)
 or
 [Report.Save](report-save.html)
 method modifies the directory path where TestStand saves the file the
 Report.GetTempFile
 method creates. Using the
 SetTempFileDirectoryOption_Default
 option with this method results in the same behavior as using the
 [Report.TempFileDirectory](report-tempfiledirectory.html)
 property to specify the directory path where TestStand saves the file the
 Report.GetTempFile
 method creates.

Use the
 [SetTempFileDirectoryOption_NeverOverride](settempfiledirectoryoptions.html)
 option to ensure that TestStand saves the file the
 Report.GetTempFile
 method creates in the directory path this method specifies. You can override the directory path by calling this method again to set the directory path.

By default, TestStand saves the file the
 Report.GetTempFile
 method creates in the directory path of the report file. Typically, if you save generated reports on a network drive to which you do not have delete permission, you cannot delete the file the
 Report.GetTempFile
 method creates after the execution. To work around this situation, use the
 Report.SetTempFileDirectoryEx
 method with the
 SetTempFileDirectoryOption_NeverOverride
 option to save the file the
 Report.GetTempFile
 method creates to a local drive.

#### Parameters

directory
 As
 [String](data-types-for-teststand.html)

[In] Specifies the directory path to save the file.

tempFileDirectoryOption
 As
 [SetTempFileDirectoryOptions](settempfiledirectoryoptions.html)

[In] Pass
 0
 to specify the default behavior or an option from the
 [SetTempFileDirectoryOptions](settempfiledirectoryoptions.html)
 enumeration.

This parameter has a default value of
 SetTempFileDirectoryOption_Default
 .

#### See Also

[Report.GetTempFile](report-gettempfile.html)

[Report.TempFileDirectory](report-tempfiledirectory.html)

[SetTempFileDirectoryOptions](settempfiledirectoryoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-stylesheetpath.html language=enus -->
## TOPIC 02281: Report.StyleSheetPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-stylesheetpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-stylesheetpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.StyleSheetPath Data Type String Purpose Specifies a string which specifies the absolute pathname of the style sheet used to transform XML reports. Remarks If this property is not specified, the default style sheet is used to transform the XML report.

### Report.StyleSheetPath

#### Syntax

[Report](report.html).StyleSheetPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a string which specifies the absolute pathname of the style sheet used to transform XML reports.

#### Remarks

If this property is not specified, the default style sheet is used to transform the XML report.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-suspendreportrefresh.html language=enus -->
## TOPIC 02282: Report.SuspendReportRefresh

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-suspendreportrefresh.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-suspendreportrefresh.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.SuspendReportRefresh Data Type Boolean Purpose Set this property to True to suspend report refreshes when modifying the ReportSection associated with the report. You typically use this property with on-the-fly report generation to avoid generating a partial report, when you are more li

### Report.SuspendReportRefresh

#### Syntax

[Report](report.html).SuspendReportRefresh

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 to suspend report refreshes when modifying the
 [ReportSection](reportsection.html)
 associated with the report. You typically use this property with on-the-fly report generation to avoid generating a partial report, when you are more likely to modify the
 ReportSection
 object associated with the report while TestStand processes the report for display purposes.

#### Remarks

Call this property only from a code module or a statement step used for report generation, not from an executing sequence or the user interface code.

After you set this property to
 True
 , you must reset this property to
 False
 in the same code module or statement step for the user interfaces and report generation to function correctly.

When this property is
 True
 , the
 [Report.IsEmpty](report-isempty.html)
 property always returns
 True
 and the
 [Report.All](report-all.html)
 property returns an empty string.

#### See Also

[Report.All](report-all.html)

[Report.IsEmpty](report-isempty.html)

[ReportSection](reportsection.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report-tempfiledirectory.html language=enus -->
## TOPIC 02283: Report.TempFileDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report-tempfiledirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report-tempfiledirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Report.TempFileDirectory Data Type String Purpose Specifies a string that specifies the directory path where TestStand saves the file the Report.GetTempFile method creates. If you call the Report.Load or Report.Save method of this class, this property is automatically set to the directory pat

### Report.TempFileDirectory

#### Syntax

[Report](report.html).TempFileDirectory

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a string that specifies the directory path where TestStand saves the file the
 [Report.GetTempFile](report-gettempfile.html)
 method creates. If you call the
 [Report.Load](report-load.html)
 or
 [Report.Save](report-save.html)
 method of this class, this property is automatically set to the directory path of the report file.

#### Remarks

Note

Report.SetTempFileDirectoryEx

Report.SetTempFileDirectoryEx

tempFileDirectoryOptions

SetTempFileDirectoryOption_NeverOverride

#### See Also

[Report.GetTempFile](report-gettempfile.html)

[Report.Load](report-load.html)

[Report.Save](report-save.html)

Parent topic:

Obsolete Report Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/report.html language=enus -->
## TOPIC 02284: Report

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/report.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/report.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects of the Report class to modify, save, load, retrieve, and view reports. To obtain the Report object for an execution, retrieve the value of the Execution.Report property. Usually, the process model updates the Report object associated with the execution, and the sequence editor or user in

### Report

Use objects of the Report class to modify, save, load, retrieve, and view reports. To obtain the Report object for an execution, retrieve the value of the
 [Execution.Report](execution-report.html)
 property.

Usually, the process model updates the Report object associated with the execution, and the sequence editor or user interface displays it.

#### Properties

| All (Read Only) |
| --- |
| Format |
| Id (Read Only) |
| IsEmpty (Read Only) |
| LatestAppendIndex (Read Only) |
| Location |
| ReportSection |
| ResetCount (Read Only) |
| StyleSheetPath |
| SuspendReportRefresh |

#### Methods

| Append |
| --- |
| AsPropertyObject |
| GetSection |
| GetTempFile |
| LaunchViewer |
| Load |
| NewReportSection |
| RefreshDisplay |
| Reset |
| Save |
| SetTempFileDirectoryEx |

#### See Also

[Engine.ExternalReportViewers](engine-externalreportviewers.html)

[Execution.Report](execution-report.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportconversion.html language=enus -->
## TOPIC 02285: ReportConversion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportconversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportconversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify how to handle linefeeds and carriage returns in report text. ReportConv_FromCRLF –(Value: 2) Convert carriage return/linefeed combinations to linefeeds. You usually use this option when reading a report from disk into memory. ReportConv_NoConversion –(Valu

### ReportConversion

This data type contains values that specify how to handle linefeeds and carriage returns in report text.

- ReportConv_FromCRLF 
 –(Value: 2) Convert carriage return/linefeed combinations to linefeeds. You usually use this option when reading a report from disk into memory.
- ReportConv_NoConversion 
 –(Value: 0) Do not convert carriage returns and linefeeds.
- ReportConv_ToCRLF 
 –(Value: 1) Convert each linefeed to a carriage return followed by a linefeed. You usually use this option when writing a report from memory to disk.

#### See Also

[Report.GetTempFile](report-gettempfile.html)

[Report.LaunchViewer](report-launchviewer.html)

[Report.Save](report-save.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-activereport.html language=enus -->
## TOPIC 02286: Reports.ActiveReport

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-activereport.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-activereport.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.ActiveReport Data Type Report Purpose Specifies the active report in the collection. The TestStand ReportView control displays the currently active report. See Also Report ReportView

### Reports.ActiveReport

#### Syntax

[Reports](reports.html).ActiveReport

#### Data Type

[Report](report.html)

#### Purpose

Specifies the active report in the collection. The TestStand
 
 [ReportView](../tsuiref/reportview.html)
 control displays the currently active report.

#### See Also

[Report](report.html)

[ReportView](../tsuiref/reportview.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-clear.html language=enus -->
## TOPIC 02287: Reports.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.Clear Purpose Removes all items from the collection. The collection must contain at least one Report object because this method also creates and adds a new empty Report object to the collection. See Also Report

### Reports.Clear

#### Syntax

[Reports](reports.html).Clear

#### Purpose

Removes all items from the collection. The collection must contain at least one
 Report
 object because this method also creates and adds a new empty
 Report
 object to the collection.

#### See Also

[Report](report.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-count.html language=enus -->
## TOPIC 02288: Reports.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.Count Data Type Long Purpose Returns the number of items in the collection. See Also Report

### Reports.Count

#### Syntax

[Reports](reports.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[Report](report.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-insert.html language=enus -->
## TOPIC 02289: Reports.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.Insert( index = -1) Return Value Report Purpose Adds a new item to the collection and returns the Report object. Parameters index As Long [In] Specifies the zero-based index of the location in the collection where you want to insert the Report object. Pass -1 to insert the Report obje

### Reports.Insert

#### Syntax

[Reports](reports.html).Insert( index = -1)

#### Return Value

[Report](report.html)

#### Purpose

Adds a new item to the collection and returns the
 Report
 object.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the location in the collection where you want to insert the
 Report
 object. Pass
 -1
 to insert the
 Report
 object at the end of the collection.

This parameter has a default value of
 -1
 .

#### See Also

[Report](report.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-insertexisting.html language=enus -->
## TOPIC 02290: Reports.InsertExisting

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-insertexisting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-insertexisting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.InsertExisting( val, index = -1) Purpose Inserts back into the collection a report you previously removed using Reports.Remove . The report must not be in another Reports collection. Parameters val As Report [In] Specifies an existing Report object to insert into the collection. index

### Reports.InsertExisting

#### Syntax

[Reports](reports.html).InsertExisting( val, index = -1)

#### Purpose

Inserts back into the collection a report you previously removed using
 [Reports.Remove](reports-remove.html)
 . The report must not be in another
 [Reports](reports.html)
 collection.

#### Parameters

val
 As
 [Report](report.html)

[In] Specifies an existing
 Report
 object to insert into the collection.

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the location in the collection where you want to insert the
 Report
 object. Pass
 -1
 to insert the
 Report
 object at the end of the collection.

This parameter has a default value of
 -1
 .

#### See Also

[Report](report.html)

[Reports](reports.html)

[Reports.Remove](reports-remove.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-item.html language=enus -->
## TOPIC 02291: Reports.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.Item( index) Data Type Report Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the Report object to retrieve. See Also Report

### Reports.Item

#### Syntax

[Reports](reports.html).Item( index)

#### Data Type

[Report](report.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the
 Report
 object to retrieve.

#### See Also

[Report](report.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-remove.html language=enus -->
## TOPIC 02292: Reports.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.Remove( index) Return Value Report Purpose Removes the specified item from this collection and returns the Report object. The collection must always contain at least one Report object. If the collection contains only one Report object, the Report is not removed until another Report is

### Reports.Remove

#### Syntax

[Reports](reports.html).Remove( index)

#### Return Value

[Report](report.html)

#### Purpose

Removes the specified item from this collection and returns the
 Report
 object. The collection must always contain at least one
 Report
 object. If the collection contains only one
 Report
 object, the Report is not removed until another Report is added to the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the
 Report
 object you want to remove.

#### See Also

[Report](report.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports-replace.html language=enus -->
## TOPIC 02293: Reports.Replace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports-replace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports-replace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Reports.Replace( oldVal, newVal) Return Value Report Purpose Replaces the Report object you specify in the collection and returns the Report object. Parameters oldVal As Report [In] Specifies the Report object in the collection to replace. If the Report object you specify is the active report

### Reports.Replace

#### Syntax

[Reports](reports.html).Replace( oldVal, newVal)

#### Return Value

[Report](report.html)

#### Purpose

Replaces the
 [Report](report.html)
 object you specify in the collection and returns the
 Report
 object.

#### Parameters

oldVal
 As
 [Report](report.html)

[In] Specifies the
 Report
 object in the collection to replace. If the
 Report
 object you specify is the active report, the replacement
 Report
 object becomes the active report.

newVal
 As
 [Report](report.html)

[In] Specifies the replacement
 Report
 object. Pass
 NULL
 to create a new empty replacement
 Report
 object.

#### See Also

[Report](report.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reports.html language=enus -->
## TOPIC 02294: Reports

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reports.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reports.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class is a collection of Report objects. Properties ActiveReport Count (Read Only) Item (Read Only) Methods Clear Insert InsertExisting Remove Replace See Also Report

### Reports

This class is a collection of
 [Report](report.html)
 objects.

#### Properties

| ActiveReport |
| --- |
| Count (Read Only) |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| InsertExisting |
| Remove |
| Replace |

#### See Also

[Report](report.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection-body.html language=enus -->
## TOPIC 02295: ReportSection.Body

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection-body.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection-body.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSection.Body Data Type String Purpose Specifies the string stored in the body of the ReportSection . See Also ReportSection.Footer ReportSection.GetAllText ReportSection.Header

### ReportSection.Body

#### Syntax

[ReportSection](reportsection.html).Body

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the string stored in the body of the
 ReportSection
 .

#### See Also

[ReportSection.Footer](reportsection-footer.html)

[ReportSection.GetAllText](reportsection-getalltext.html)

[ReportSection.Header](reportsection-header.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection-footer.html language=enus -->
## TOPIC 02296: ReportSection.Footer

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection-footer.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection-footer.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSection.Footer Data Type String Purpose Specifies the string stored in the footer of the ReportSection . See Also ReportSection.Body ReportSection.GetAllText ReportSection.Header

### ReportSection.Footer

#### Syntax

[ReportSection](reportsection.html).Footer

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the string stored in the footer of the
 ReportSection
 .

#### See Also

[ReportSection.Body](reportsection-body.html)

[ReportSection.GetAllText](reportsection-getalltext.html)

[ReportSection.Header](reportsection-header.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection-getalltext.html language=enus -->
## TOPIC 02297: ReportSection.GetAllText

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection-getalltext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection-getalltext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSection.GetAllText Return Value String Purpose Returns all the content of the ReportSection as a string. Remarks The returned string is a concatenation of the ReportSection.Header , ReportSection.Body , and ReportSection.GetAllText strings of all child ReportSection objects and the Repo

### ReportSection.GetAllText

#### Syntax

[ReportSection](reportsection.html).GetAllText

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns all the content of the
 ReportSection
 as a string.

#### Remarks

The returned string is a concatenation of the
 [ReportSection.Header](reportsection-header.html)
 ,
 [ReportSection.Body](reportsection-body.html)
 , and
 ReportSection.GetAllText
 strings of all child
 ReportSection
 objects and the
 [ReportSectionFooter](reportsection-footer.html)
 string, in that order.

#### See Also

[ReportSection.Body](reportsection-body.html)

[ReportSection.Footer](reportsection-footer.html)

[ReportSection.Header](reportsection-header.html)

[ReportSection.IsEmpty](reportsection-isempty.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection-header.html language=enus -->
## TOPIC 02298: ReportSection.Header

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection-header.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection-header.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSection.Header Data Type String Purpose Specifies the string stored in the header of the ReportSection . See Also ReportSection.Body ReportSection.Footer ReportSection.GetAllText

### ReportSection.Header

#### Syntax

[ReportSection](reportsection.html).Header

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the string stored in the header of the
 ReportSection
 .

#### See Also

[ReportSection.Body](reportsection-body.html)

[ReportSection.Footer](reportsection-footer.html)

[ReportSection.GetAllText](reportsection-getalltext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection-id.html language=enus -->
## TOPIC 02299: ReportSection.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSection.Id Data Type Long Purpose Returns a unique ID that distinguishes the ReportSection from all other ReportSection objects. The ID number is never zero.

### ReportSection.Id

#### Syntax

[ReportSection](reportsection.html).Id

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique ID that distinguishes the
 ReportSection
 from all other
 ReportSection
 objects.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection-isempty.html language=enus -->
## TOPIC 02300: ReportSection.IsEmpty

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection-isempty.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection-isempty.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSection.IsEmpty Data Type Boolean Purpose Returns True only if the header, body, and footer of the ReportSection and the children are empty.

### ReportSection.IsEmpty

#### Syntax

[ReportSection](reportsection.html).IsEmpty

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 only if the header, body, and footer of the ReportSection and the children are empty.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection-reportsubsections.html language=enus -->
## TOPIC 02301: ReportSection.ReportSubsections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection-reportsubsections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection-reportsubsections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSection.ReportSubsections Data Type ReportSections Purpose Specifies a reference to the ReportSections object, which is a collection that contains a list of child ReportSection objects to the current object. See Also ReportSections

### ReportSection.ReportSubsections

#### Syntax

[ReportSection](reportsection.html).ReportSubsections

#### Data Type

[ReportSections](reportsections.html)

#### Purpose

Specifies a reference to the
 [ReportSections](reportsections.html)
 object, which is a collection that contains a list of child
 ReportSection
 objects to the current object.

#### See Also

[ReportSections](reportsections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsection.html language=enus -->
## TOPIC 02302: ReportSection

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsection.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsection.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects of this class to store, update, and transfer reports. You typically use ReportSection objects to avoid creating copies of a report as the report is transferred between the report generator, process models, Report object, and ReportView control. You can create a new ReportSection object b

### ReportSection

Use objects of this class to store, update, and transfer reports. You typically use
 ReportSection
 objects to avoid creating copies of a report as the report is transferred between the report generator, process models,
 [Report](report.html)
 object, and
 
 [ReportView](../tsuiref/reportview.html)
 control. You can create a new
 ReportSection
 object by calling the
 [Report.NewReportSection](report-newreportsection.html)
 method.
 ReportSection
 objects can contain other
 ReportSection
 objects.

Typically, a process model creates and updates the
 ReportSection
 object and assigns it to the
 Report
 object by setting the
 [Report.ReportSection](report-reportsection.html)
 property.

#### Properties

| Body |
| --- |
| Footer |
| Header |
| Id (Read Only) |
| IsEmpty (Read Only) |
| ReportSubsections |

#### Method

| GetAllText |
| --- |

#### See Also

[Report](report.html)

[Report.NewReportSection](report-newreportsection.html)

[Report.ReportSection](report-reportsection.html)

[ReportView](../tsuiref/reportview.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsections-clear.html language=enus -->
## TOPIC 02303: ReportSections.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsections-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsections-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSections.Clear Purpose Removes all items from the collection.

### ReportSections.Clear

#### Syntax

[ReportSections](reportsections.html).Clear

#### Purpose

Removes all items from the collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsections-count.html language=enus -->
## TOPIC 02304: ReportSections.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsections-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsections-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSections.Count Data Type Long Purpose Returns the number of items in the collection.

### ReportSections.Count

#### Syntax

[ReportSections](reportsections.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsections-insert.html language=enus -->
## TOPIC 02305: ReportSections.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsections-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsections-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSections.Insert( index = -1, Header = "", Body = "", Footer = "") Return Value ReportSection The ReportSection this method inserts into the collection. Purpose Adds a new item to the collection. Parameters index As Long [In] Specifies the zero-based index at which to insert the new item

### ReportSections.Insert

#### Syntax

[ReportSections](reportsections.html).Insert( index = -1, Header = "", Body = "", Footer = "")

#### Return Value

[ReportSection](reportsection.html)

The
 [ReportSection](reportsection.html)
 this method inserts into the collection.

#### Purpose

Adds a new item to the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index at which to insert the new item. Pass
 -1
 to insert the item at the end of the collection.

This parameter has a default value of
 -1
 .

Header
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 [ReportSection.Header](reportsection-header.html)
 property of the new
 ReportSection
 .

This parameter has a default value of
 ""
 .

Body
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 [ReportSection.Body](reportsection-body.html)
 property of the new
 ReportSection
 .

This parameter has a default value of
 ""
 .

Footer
 As
 [String](data-types-for-teststand.html)

[In] Specifies the
 [ReportSection.Footer](reportsection-footer.html)
 property of the new
 ReportSection
 .

This parameter has a default value of
 ""
 .

#### See Also

[Report.NewReportSection](report-newreportsection.html)

[ReportSection](reportsection.html)

[ReportSection.Body](reportsection-body.html)

[ReportSection.Footer](reportsection-footer.html)

[ReportSection.Header](reportsection-header.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsections-insertexisting.html language=enus -->
## TOPIC 02306: ReportSections.InsertExisting

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsections-insertexisting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsections-insertexisting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSections.InsertExisting( val, index = -1) Purpose Inserts an existing ReportSection object into the collection. Parameters val As ReportSection [In] Specifies existing ReportSection to insert into the collection. index As Long [In] Specifies the zero-based index at which to insert the n

### ReportSections.InsertExisting

#### Syntax

[ReportSections](reportsections.html).InsertExisting( val, index = -1)

#### Purpose

Inserts an existing
 [ReportSection](reportsection.html)
 object into the collection.

#### Parameters

val
 As
 [ReportSection](reportsection.html)

[In] Specifies existing
 ReportSection
 to insert into the collection.

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index at which to insert the new item. Pass
 -1
 to insert the item at the end of the collection.

This parameter has a default value of
 -1
 .

#### See Also

[Report.NewReportSection](report-newreportsection.html)

[ReportSection](reportsection.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsections-item.html language=enus -->
## TOPIC 02307: ReportSections.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsections-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsections-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSections.Item( index) Data Type ReportSection Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also ReportSection

### ReportSections.Item

#### Syntax

[ReportSections](reportsections.html).Item( index)

#### Data Type

[ReportSection](reportsection.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[ReportSection](reportsection.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsections-remove.html language=enus -->
## TOPIC 02308: ReportSections.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsections-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsections-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ReportSections.Remove( index) Return Value ReportSection The ReportSection this method removes from the collection. Purpose Removes the specified item from this collection, if it exists. Parameters index As Long [In] Specifies the zero-based index of the item to remove. See Also ReportSection

### ReportSections.Remove

#### Syntax

[ReportSections](reportsections.html).Remove( index)

#### Return Value

[ReportSection](reportsection.html)

The
 [ReportSection](reportsection.html)
 this method removes from the collection.

#### Purpose

Removes the specified item from this collection, if it exists.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to remove.

#### See Also

[ReportSection](reportsection.html)

[ReportSections.Clear](reportsections-clear.html)

[ReportSections.Insert](reportsections-insert.html)

[ReportSections.InsertExisting](reportsections-insertexisting.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/reportsections.html language=enus -->
## TOPIC 02309: ReportSections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/reportsections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/reportsections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class is a collection of ReportSection objects. The collection contains a list of ReportSection objects that are children of the ReportSection object from which the ReportSections object was obtained. Properties Count (Read Only) Item (Read Only) Methods Clear Insert InsertExisting Remove See A

### ReportSections

This class is a collection of
 [ReportSection](reportsection.html)
 objects. The collection contains a list of
 ReportSection
 objects that are children of the
 ReportSection
 object from which the
 ReportSections
 object was obtained.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Insert |
| InsertExisting |
| Remove |

#### See Also

[ReportSection](reportsection.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resettypeinstanceoptions.html language=enus -->
## TOPIC 02310: ResetTypeInstanceOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resettypeinstanceoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resettypeinstanceoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the Engine.ResetTypeInstances method. Use the bitwise-OR operator to specify more than one option. Avoid using the ResetTypeInst_ResetFlags flag because it might result in unexpected behavior. In most cases, you should n

### ResetTypeInstanceOptions

These constants represent the options you can use with the
 options
 parameter of the
 [Engine.ResetTypeInstances](engine-resettypeinstances.html)
 method. Use the bitwise-OR operator to specify more than one option.

Note

ResetTypeInst_ResetFlags

PropFlags_PassByReference

Sequence Call

Engine.ResetTypeInstances

- ResetTypeInst_NoOptions 
 –(Value: 0x0) No options.
- ResetTypeInst_RecurseSubProperties 
 –(Value: 0x4) Resets flags or values of subproperties of type instances in addition to the top level object.
- ResetTypeInst_ResetFlags 
 –(Value: 0x2) Resets the property flags of type instances to the flags of the type definition.
- ResetTypeInst_ResetValues 
 –(Value: 0x1) Resets the property values of type instances to the value of the type definition.

#### See Also

[Engine.ResetTypeInstances](engine-resettypeinstances.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/restartoptions.html language=enus -->
## TOPIC 02311: RestartOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/restartoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/restartoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the Execution.RestartEx method. Use the bitwise-OR operator to specify more than one option. RestartOption_BreakOnEntry –(Value: 0x1) Use this option to suspend execution before executing the first step. RestartOption_Br

### RestartOptions

These constants represent the options you can use with the
 options
 parameter of the
 [Execution.RestartEx](execution-restartex.html)
 method. Use the bitwise-OR operator to specify more than one option.

- RestartOption_BreakOnEntry 
 –(Value: 0x1) Use this option to suspend execution before executing the first step.
- RestartOption_BreakOnSequenceFailure 
 –(Value: 0x8) Specifies if the sequence editor and user interfaces suspend when a failing step causes a sequence failure to first occur. TestStand does not suspend on failing Sequence Call steps already in the stack. If the sequence failure setting is reset, TestStand suspends when the next failing step causes sequence failure.
- RestartOption_BreakOnStepFailure 
 –(Value: 0x4) Specifies if the sequence editor and user interfaces suspend when a step fails. TestStand does not suspend an execution on a failing Sequence Call step if the step that caused the sequence failure already suspended execution.
- RestartOption_NoOptions 
 –(Value: 0x0) No options.
- RestartOption_OverrideNotRestartable 
 –(Value: 0x2) Use this option to restart an execution created with the
 ExecutionTypeMask.ExecTypeMask_NotRestartable 
 option.

#### See Also

[Execution.RestartEx](execution-restartex.html)

[ExecutionTypeMask](executiontypemask.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-close.html language=enus -->
## TOPIC 02312: ResultLog.Close

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-close.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-close.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.Close Purpose Closes the results file.

### ResultLog.Close

#### Syntax

[ResultLog](resultlog.html).Close

#### Purpose

Closes the results file.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-closedwhenwritten.html language=enus -->
## TOPIC 02313: ResultLog.ClosedWhenWritten

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-closedwhenwritten.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-closedwhenwritten.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.ClosedWhenWritten Data Type Boolean Purpose Returns True if the ResultLogger.Close method was called when the file was written. A False value indicates that the writing process was aborted and that the file might be incomplete or corrupt.

### ResultLog.ClosedWhenWritten

#### Syntax

[ResultLog](resultlog.html).ClosedWhenWritten

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the
 [ResultLogger.Close](resultlogger-close.html)
 method was called when the file was written. A
 False
 value indicates that the writing process was aborted and that the file might be incomplete or corrupt.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-getreportpaths.html language=enus -->
## TOPIC 02314: ResultLog.GetReportPaths

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-getreportpaths.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-getreportpaths.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.GetReportPaths Return Value PropertyObject Purpose Returns the array of file paths the ResultLog.SetReportPaths method stores. If no paths have been stored, the method returns an empty array.

### ResultLog.GetReportPaths

#### Syntax

[ResultLog](resultlog.html).GetReportPaths

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the array of file paths the
 [ResultLog.SetReportPaths](resultlog-setreportpaths.html)
 method stores. If no paths have been stored, the method returns an empty array.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-onthefly.html language=enus -->
## TOPIC 02315: ResultLog.OnTheFly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-onthefly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-onthefly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.OnTheFly Data Type Boolean Purpose Returns a value that indicates whether the results file contains results stored on-the-fly in ResultLogRecordType_OnTheFlyStepResults records or if the results are stored as a subproperty tree under the uut result in ResultLogRecordType_PostUUT rec

### ResultLog.OnTheFly

#### Syntax

[ResultLog](resultlog.html).OnTheFly

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the results file contains results stored on-the-fly in
 ResultLogRecordType_OnTheFlyStepResults
 records or if the results are stored as a subproperty tree under the
 uut
 result in
 ResultLogRecordType_PostUUT
 records.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-open.html language=enus -->
## TOPIC 02316: ResultLog.Open

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-open.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-open.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.Open( path) Purpose Opens the results file for reading. Parameters path As String [In] Specifies the path of the TestStand results ( .tsr ) file to open.

### ResultLog.Open

#### Syntax

[ResultLog](resultlog.html).Open( path)

#### Purpose

Opens the results file for reading.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the path of the TestStand results (
 .tsr
 ) file to open.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-path.html language=enus -->
## TOPIC 02317: ResultLog.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.Path Data Type String Purpose Returns the absolute path of the results file.

### ResultLog.Path

#### Syntax

[ResultLog](resultlog.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the results file.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-readnextrecord.html language=enus -->
## TOPIC 02318: ResultLog.ReadNextRecord

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-readnextrecord.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-readnextrecord.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.ReadNextRecord( resultLogRecordType, executionId, threadId, objects) Return Value Boolean Purpose Reads one record from the TestStand results ( .tsr ) file. Returns False if no more records exist. Parameters resultLogRecordType As ResultLogRecordTypes [Out] Returns the type of recor

### ResultLog.ReadNextRecord

#### Syntax

[ResultLog](resultlog.html).ReadNextRecord( resultLogRecordType, executionId, threadId, objects)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Reads one record from the TestStand results (
 .tsr
 ) file. Returns
 False
 if no more records exist.

#### Parameters

resultLogRecordType
 As
 [ResultLogRecordTypes](resultlogrecordtypes.html)

[Out] Returns the type of record read.

executionId
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the ID of the execution that logged the record.

threadId
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the ID of the thread that logged the record.

objects
 As
 [Object Array](data-types-for-teststand.html)

[Out] Returns the objects logged to the record.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-secondsatstartin1970universalcoordi.html language=enus -->
## TOPIC 02319: ResultLog.SecondsAtStartIn1970UniversalCoordinatedTime

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-secondsatstartin1970universalcoordi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-secondsatstartin1970universalcoordi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.SecondsAtStartIn1970UniversalCoordinatedTime Data Type Double Purpose Returns the value of the Engine.SecondsAtStartIn1970UniversalCoordinatedTime property for the engine that created the TestStand results .tsr file. If the log file contains any custom properties that contain time v

### ResultLog.SecondsAtStartIn1970UniversalCoordinatedTime

#### Syntax

[ResultLog](resultlog.html).SecondsAtStartIn1970UniversalCoordinatedTime

#### Data Type

[Double](data-types-for-teststand.html)

#### Purpose

Returns the value of the
 [Engine.SecondsAtStartIn1970UniversalCoordinatedTime](engine-secondsatstartin1970universalcoordinat.html)
 property for the engine that created the TestStand results
 .tsr
 file. If the log file contains any custom properties that contain time values relative to the time the engine that created the
 .tsr
 started, you can use this value to adjust the values to be relative to the time the current engine started. The
 Seconds
 [expression function](../tsfundamentals/expression-functions.html)
 and the
 [Engine.SecondsSinceStart](engine-secondssincestart.html)
 property return times relative to engine startup.

#### Remarks

The
 [ResultLog.ReadNextRecord](resultlog-readnextrecord.html)
 method uses this property to automatically adjust the values of
 TS.StartTime
 result subproperties to be relative to the start time of the current engine.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-setreportpaths.html language=enus -->
## TOPIC 02320: ResultLog.SetReportPaths

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-setreportpaths.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-setreportpaths.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.SetReportPaths( pathStringArray) Purpose Stores an array of file paths. TestStand writes the file paths to a file with the same name as the ResultLog file with the addition of a .reportlist suffix. Use this method to record the paths of reports that are created from processing a Res

### ResultLog.SetReportPaths

#### Syntax

[ResultLog](resultlog.html).SetReportPaths( pathStringArray)

#### Purpose

Stores an array of file paths. TestStand writes the file paths to a file with the same name as the
 ResultLog
 file with the addition of a
 .reportlist
 suffix. Use this method to record the paths of reports that are created from processing a
 ResultLog
 file.

#### Parameters

pathStringArray
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a property object array of strings that contains report paths.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-simulateonthefly.html language=enus -->
## TOPIC 02321: ResultLog.SimulateOnTheFly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-simulateonthefly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-simulateonthefly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.SimulateOnTheFly Data Type Boolean Purpose This property is reserved for internal use. Do not access it.

### ResultLog.SimulateOnTheFly

#### Syntax

[ResultLog](resultlog.html).SimulateOnTheFly

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog-uniqueid.html language=enus -->
## TOPIC 02322: ResultLog.UniqueId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog-uniqueid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog-uniqueid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLog.UniqueId Data Type String Purpose Returns a string that is globally unique to the result log file. Two result log files can return the same unique ID only if one file is a copy of the other. This property returns an empty string if you access it before a successful call to the Resul

### ResultLog.UniqueId

#### Syntax

[ResultLog](resultlog.html).UniqueId

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a string that is globally unique to the result log file. Two result log files can return the same unique ID only if one file is a copy of the other. This property returns an empty string if you access it before a successful call to the
 [ResultLog.Open](resultlog-open.html)
 method.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlog.html language=enus -->
## TOPIC 02323: ResultLog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlog.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlog.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: ResultLog objects read TestStand results from a file that a ResultLogger object creates. Properties ClosedWhenWritten (Read Only) OnTheFly (Read Only) Path (Read Only) SecondsAtStartIn1970UniversalCoordinatedTime (Read Only) SimulateOnTheFly UniqueId (Read Only) Methods Close GetReportPaths Open Rea

### ResultLog

ResultLog
 objects read TestStand results from a file that a
 [ResultLogger](resultlogger.html)
 object creates.

#### Properties

| ClosedWhenWritten (Read Only) |
| --- |
| OnTheFly (Read Only) |
| Path (Read Only) |
| SecondsAtStartIn1970UniversalCoordinatedTime (Read Only) |
| SimulateOnTheFly |
| UniqueId (Read Only) |

#### Methods

| Close |
| --- |
| GetReportPaths |
| Open |
| ReadNextRecord |
| SetReportPaths |

#### See Also

[ResultLogger](resultlogger.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-close.html language=enus -->
## TOPIC 02324: ResultLogger.Close

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-close.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-close.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.Close Purpose Completes all writing to the TestStand results ( .tsr ) file and closes the file.

### ResultLogger.Close

#### Syntax

[ResultLogger](resultlogger.html).Close

#### Purpose

Completes all writing to the TestStand results (
 .tsr
 ) file and closes the file.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-continueinnewfile.html language=enus -->
## TOPIC 02325: ResultLogger.ContinueInNewFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-continueinnewfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-continueinnewfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.ContinueInNewFile( path) Purpose Completes writing to the current TestStand results ( .tsr ) file, closes the file, and then opens a new file for future writing. Remarks If a Begin record does not have a corresponding End record, this method creates an End record in the old file

### ResultLogger.ContinueInNewFile

#### Syntax

[ResultLogger](resultlogger.html).ContinueInNewFile( path)

#### Purpose

Completes writing to the current TestStand results (
 .tsr
 ) file, closes the file, and then opens a new file for future writing.

#### Remarks

If a Begin record does not have a corresponding End record, this method creates an End record in the old file and copies the Begin record to the new file. This method deletes any records for in-progress UUTs or batches from the old file and copies the records to the new file.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the path of the new file.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-deferrablerename.html language=enus -->
## TOPIC 02326: ResultLogger.DeferrableRename

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-deferrablerename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-deferrablerename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.DeferrableRename( path) Return Value Boolean A return value of True indicates that the rename operation succeeded and that the ResultLogger object updated the corresponding path property and renamed the TestStand results ( .tsr ) file on disk. A return value of False indicates th

### ResultLogger.DeferrableRename

#### Syntax

[ResultLogger](resultlogger.html).DeferrableRename( path)

#### Return Value

[Boolean](data-types-for-teststand.html)

A return value of
 True
 indicates that the rename operation succeeded and that the
 ResultLogger
 object updated the corresponding path property and renamed the TestStand results (
 .tsr
 ) file on disk. A return value of
 False
 indicates that the rename operation failed and that the
 ResultLogger
 object did not update the corresponding path property and deferred renaming the file.

#### Purpose

Calling this method is similar to assigning a new value to the
 [ResultLogger.Path](resultlogger-path.html)
 property. However, when you use this method, the
 ResultLogger
 object does not update the path property and execution continues if renaming the underlying file fails, such as in the case of remote file systems that do not support the rename operation. If the initial renaming operation fails, the
 ResultLogger
 object defers updating the path property. The
 ResultLogger
 object updates the path property and the name of the file on disk when the
 ResultLogger
 object closes or the
 [ResultLogger.ContinueInNewFile](resultlogger-continueinnewfile.html)
 method is invoked. If at this point the rename operation remains impossible, the
 ResultLogger
 object simulates renaming the file by copying the file to the new path and deleting the existing file.

While a deferred renaming operation is pending, if the value of the
 ResultLogger.Path
 property changes or an additional call to the
 ResultLogger.DeferrableRename
 method occurs, the
 ResultLogger
 object cancels any previously deferred renaming operation.

#### Remarks

National Instruments recommends using the
 ResultLogger.Path
 property directly instead of the
 ResultLogger.DeferrableRename
 method whenever possible. The
 ResultLogger.DeferrableRename
 method is generally useful only in situations in which you repeatedly rename a single file to indicate status. For example, the default offline results generator process model plug-in uses the
 ResultLogger.DeferrableRename
 method to update the range of UUT serial numbers stored in the TestStand results (
 .tsr
 ) file as UUTs execute.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path to use to rename the TestStand results (
 .tsr
 ) file, such as
 C:\OfflineResults\MyResults.tsr
 .

#### See Also

[ResultLogger.Close](resultlogger-close.html)

[ResultLogger.ContinueInNewFile](resultlogger-continueinnewfile.html)

[ResultLogger.Path](resultlogger-path.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-flush.html language=enus -->
## TOPIC 02327: ResultLogger.Flush

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-flush.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-flush.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.Flush Purpose Completes all pending writes to the TestStand results ( .tsr ) file before returning, including writes queued to the writing thread if you enabled the logInSeparateThread parameter of the ResultLogger.Open method. See Also ResultLogger.Open

### ResultLogger.Flush

#### Syntax

[ResultLogger](resultlogger.html).Flush

#### Purpose

Completes all pending writes to the TestStand results (
 .tsr
 ) file before returning, including writes queued to the writing thread if you enabled the
 logInSeparateThread
 parameter of the
 [ResultLogger.Open](resultlogger-open.html)
 method.

#### See Also

[ResultLogger.Open](resultlogger-open.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-getfileswritten.html language=enus -->
## TOPIC 02328: ResultLogger.GetFilesWritten

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-getfileswritten.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-getfileswritten.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.GetFilesWritten( clear) Return Value PropertyObject Purpose Returns the paths of all the completed offline results ( .tsr ) files TestStand recorded. You can also use this method to clear the internal record of completed paths. Parameters clear As Boolean [In] Specifies to clear

### ResultLogger.GetFilesWritten

#### Syntax

[ResultLogger](resultlogger.html).GetFilesWritten( clear)

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the paths of all the completed offline results (
 .tsr
 ) files TestStand recorded. You can also use this method to clear the internal record of completed paths.

#### Parameters

clear
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies to clear the internal record of completed
 .tsr
 files. When the
 clear
 parameter is
 True
 , subsequent calls to the
 ResultLogger.GetFilesWritten
 method return only files completed since the most recent call to the method. When the
 clear
 parameter is
 False
 , TestStand does not clear the internal record of completed
 .tsr
 files and subsequent calls to the
 ResultLogger.GetFilesWritten
 method return files returned from previous calls to the method and any files completed since the most recent call to the method.

#### See Also

[ResultLogger.RecordFilesWritten](resultlogger-recordfileswritten.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logbatchdone.html language=enus -->
## TOPIC 02329: ResultLogger.LogBatchDone

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logbatchdone.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logbatchdone.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogBatchDone( thread, modelData, uut, uutStatus) Purpose Logs parameters to the Model Plugin - Batch Done entry point. Parameters thread As Thread [In] Specifies the process model controller or test socket thread that invokes this method. modelData As PropertyObject [In] Specifie

### ResultLogger.LogBatchDone

#### Syntax

[ResultLogger](resultlogger.html).LogBatchDone( thread, modelData, uut, uutStatus)

#### Purpose

Logs parameters to the
 [Model Plugin - Batch Done](/csh?context=ts_tsfundamentals_pmpbatchdoneep)
 entry point.

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the UUT.

uutStatus
 As
 [String](data-types-for-teststand.html)

[In] Specifies the result status for the UUT.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logbatchstart.html language=enus -->
## TOPIC 02330: ResultLogger.LogBatchStart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logbatchstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logbatchstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogBatchStart( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut) Purpose Logs parameters to the Model Plugin - Batch Start entry point. Remarks Model Plugin - Batch Start Parameters thread As Thread [In] Specifies the process model controller

### ResultLogger.LogBatchStart

#### Syntax

[ResultLogger](resultlogger.html).LogBatchStart( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut)

#### Purpose

Logs parameters to the
 [Model Plugin - Batch Start](/csh?context=ts_tsfundamentals_pmpbatchstartep)
 entry point.

#### Remarks

[Model Plugin - Batch Start](/csh?context=ts_tsfundamentals_pmpbatchstartep)

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelThreadType
 As
 [PropertyObject](propertyobject.html)

[In] Pass an instance of an
 NI_ModelThreadType
 type that describes the thread parameter.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

processModelClientPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the process model client file. Pass an empty string if no such file exists.

startDate
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the DateDetails custom data type that indicates the date on which the batch test began.

startTime
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the TimeDetails custom data type that indicates the time at which the batch test began.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the batch.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logbegin.html language=enus -->
## TOPIC 02331: ResultLogger.LogBegin

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logbegin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logbegin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogBegin( thread, parentThread, modelThreadType, modelData, processModelClientPath, numberOfSockets, socketIndex) Purpose Logs parameters to the Model Plugin - Begin entry point. Parameters thread As Thread [In] Specifies the process model controller or test socket thread that in

### ResultLogger.LogBegin

#### Syntax

[ResultLogger](resultlogger.html).LogBegin( thread, parentThread, modelThreadType, modelData, processModelClientPath, numberOfSockets, socketIndex)

#### Purpose

Logs parameters to the
 [Model Plugin - Begin](/csh?context=ts_tsfundamentals_pmpbeginep)
 entry point.

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

parentThread
 As
 [Thread](thread.html)

[In] Specifies the parent controller thread of the test socket thread. Pass
 NULL
 if no such thread exists.

modelThreadType
 As
 [PropertyObject](propertyobject.html)

[In] Pass an instance of an
 NI_ModelThreadType
 type that describes the thread parameter.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

processModelClientPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the process model client file. Pass an empty string if no such file exists.

numberOfSockets
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the number of test sockets in the execution.

socketIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the test socket index for the
 thread
 parameter.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logend.html language=enus -->
## TOPIC 02332: ResultLogger.LogEnd

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logend.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logend.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogEnd( thread, modelData) Purpose Logs parameters to the Model Plugin - End entry point. Remarks Model Plugin - End Parameters thread As Thread [In] Specifies the process model controller or test socket thread that invokes this method. modelData As PropertyObject [In] Specifies

### ResultLogger.LogEnd

#### Syntax

[ResultLogger](resultlogger.html).LogEnd( thread, modelData)

#### Purpose

Logs parameters to the
 [Model Plugin - End](/csh?context=ts_tsfundamentals_pmpendep)
 entry point.

#### Remarks

[Model Plugin - End](/csh?context=ts_tsfundamentals_pmpendep)

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logontheflystepresults.html language=enus -->
## TOPIC 02333: ResultLogger.LogOnTheFlyStepResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logontheflystepresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logontheflystepresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogOnTheFlyStepResults( thread, uut, steps, results, callbackNames, parentIds) Purpose Logs parameters to the Model Plugin - OnTheFly Step Results entry point. Parameters thread As Thread [In] Specifies the test socket thread that invokes this method. uut As PropertyObject [In] S

### ResultLogger.LogOnTheFlyStepResults

#### Syntax

[ResultLogger](resultlogger.html).LogOnTheFlyStepResults( thread, uut, steps, results, callbackNames, parentIds)

#### Purpose

Logs parameters to the
 [Model Plugin - OnTheFly Step Results](/csh?context=ts_tsfundamentals_pmpontheflystepresultsep)
 entry point.

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the test socket thread that invokes this method.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the UUT.

steps
 As
 [PropertyObject](propertyobject.html)

[In] Pass the
 Steps
 parameter TestStand passed to the PostResults callback.

results
 As
 [PropertyObject](propertyobject.html)

[In] Pass the
 Results
 parameter TestStand passed to the PostResults callback.

callbackNames
 As
 [PropertyObject](propertyobject.html)

[In] Pass the
 CallbackNames
 parameter TestStand passed to the PostResults callback.

parentIds
 As
 [PropertyObject](propertyobject.html)

[In] Pass the
 ParentIds
 parameter TestStand passed to the PostResults callback.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logpostbatch.html language=enus -->
## TOPIC 02334: ResultLogger.LogPostBatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logpostbatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logpostbatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogPostBatch( thread, modelData, uut, uutStatus) Purpose Logs parameters to the Model Plugin - Post Batch entry point. Remarks Model Plugin - Post Batch Parameters thread As Thread [In] Specifies the process model controller or test socket thread that invokes this method. modelDa

### ResultLogger.LogPostBatch

#### Syntax

[ResultLogger](resultlogger.html).LogPostBatch( thread, modelData, uut, uutStatus)

#### Purpose

Logs parameters to the
 [Model Plugin - Post Batch](/csh?context=ts_tsfundamentals_pmppostbatchep)
 entry point.

#### Remarks

[Model Plugin - Post Batch](/csh?context=ts_tsfundamentals_pmppostbatchep)

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the UUT.

uutStatus
 As
 [String](data-types-for-teststand.html)

[In] Specifies the result status for the UUT.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logpostuut.html language=enus -->
## TOPIC 02335: ResultLogger.LogPostUUT

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logpostuut.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logpostuut.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogPostUUT( thread, modelData, uut, uutStatus) Purpose Logs parameters to the Model Plugin - Post UUT entry point. Remarks Model Plugin - Post UUT Parameters thread As Thread [In] Specifies the process model controller or test socket thread that invokes this method. modelData As

### ResultLogger.LogPostUUT

#### Syntax

[ResultLogger](resultlogger.html).LogPostUUT( thread, modelData, uut, uutStatus)

#### Purpose

Logs parameters to the
 [Model Plugin - Post UUT](/csh?context=ts_tsfundamentals_pmppostuutep)
 entry point.

#### Remarks

[Model Plugin - Post UUT](/csh?context=ts_tsfundamentals_pmppostuutep)

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the UUT.

uutStatus
 As
 [String](data-types-for-teststand.html)

[In] Specifies the result status for the UUT.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logprebatch.html language=enus -->
## TOPIC 02336: ResultLogger.LogPreBatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logprebatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logprebatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogPreBatch( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut, continueTesting) Purpose Logs parameters to the Model Plugin - Pre Batch entry point. Parameters thread As Thread [In] Specifies the process model controller or test socket thread

### ResultLogger.LogPreBatch

#### Syntax

[ResultLogger](resultlogger.html).LogPreBatch( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut, continueTesting)

#### Purpose

Logs parameters to the
 [Model Plugin - Pre Batch](/csh?context=ts_tsfundamentals_pmpprebatchep)
 entry point.

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelThreadType
 As
 [PropertyObject](propertyobject.html)

[In] Pass an instance of an
 NI_ModelThreadType
 type that describes the thread parameter.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

processModelClientPath
 As
 [String](data-types-for-teststand.html)

[In] Pass the absolute path of the process model client file or an empty string if none exists.

startDate
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the DateDetails custom data type that indicates the date on which the batch test began.

startTime
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the TimeDetails custom data type that indicates the time at which the batch test began.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the batch.

continueTesting
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether testing continues to the next batch.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-logpreuut.html language=enus -->
## TOPIC 02337: ResultLogger.LogPreUUT

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-logpreuut.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-logpreuut.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogPreUUT( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut, continueTesting) Purpose Logs parameters to the Model Plugin - Pre UUT entry point. Parameters thread As Thread [In] Specifies the process model controller or test socket thread that

### ResultLogger.LogPreUUT

#### Syntax

[ResultLogger](resultlogger.html).LogPreUUT( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut, continueTesting)

#### Purpose

Logs parameters to the
 [Model Plugin - Pre UUT](/csh?context=ts_tsfundamentals_pmppreuutep)
 entry point.

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelThreadType
 As
 [PropertyObject](propertyobject.html)

[In] Pass an instance of an
 NI_ModelThreadType
 type that describes the thread parameter.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

processModelClientPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the process model client file. Pass an empty string if no such file exists.

startDate
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the DateDetails custom data type that indicates the date on which the UUT test began.

startTime
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the TimeDetails custom data type that indicates the time at which the UUT test began.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the UUT.

continueTesting
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether testing continues to the next UUT.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-loguutdone.html language=enus -->
## TOPIC 02338: ResultLogger.LogUUTDone

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-loguutdone.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-loguutdone.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogUUTDone( thread, modelData, uut, uutStatus, uutResult) Purpose Logs parameters to the Model Plugin - UUT Done entry point. Remarks Model Plugin - UUT Done Parameters thread As Thread [In] Specifies the process model controller or test socket thread that invokes this method. mo

### ResultLogger.LogUUTDone

#### Syntax

[ResultLogger](resultlogger.html).LogUUTDone( thread, modelData, uut, uutStatus, uutResult)

#### Purpose

Logs parameters to the
 [Model Plugin - UUT Done](/csh?context=ts_tsfundamentals_pmpuutdoneep)
 entry point.

#### Remarks

[Model Plugin - UUT Done](/csh?context=ts_tsfundamentals_pmpuutdoneep)

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the UUT.

uutStatus
 As
 [String](data-types-for-teststand.html)

[In] Specifies the result status for the UUT.

uutResult
 As
 [PropertyObject](propertyobject.html)

[In] Pass the result of the sequence call that invoked the
 MainSequence
 in the client sequence file.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-loguutstart.html language=enus -->
## TOPIC 02339: ResultLogger.LogUUTStart

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-loguutstart.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-loguutstart.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.LogUUTStart( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut) Purpose Logs parameters to the Model Plugin - UUT Start entry point. Parameters thread As Thread [In] Specifies the process model controller or test socket thread that invokes this

### ResultLogger.LogUUTStart

#### Syntax

[ResultLogger](resultlogger.html).LogUUTStart( thread, modelThreadType, modelData, processModelClientPath, startDate, startTime, uut)

#### Purpose

Logs parameters to the
 [Model Plugin - UUT Start](/csh?context=ts_tsfundamentals_pmpuutstartep)
 entry point.

#### Parameters

thread
 As
 [Thread](thread.html)

[In] Specifies the process model controller or test socket thread that invokes this method.

modelThreadType
 As
 [PropertyObject](propertyobject.html)

[In] Pass an instance of an
 NI_ModelThreadType
 type that describes the thread parameter.

modelData
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the process model-specific data. At a minimum, this parameter must be a container with a field named
 ModelType
 using the
 NI_ModelType
 type. For controller threads, this parameter must also contain a field named
 TestSockets
 using a container array type, where each element in the array contains a field named
 MainSequenceResults
 using an object reference type.

processModelClientPath
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the process model client file. Pass an empty string if no such file exists.

startDate
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the DateDetails custom data type that indicates the date on which the UUT test began.

startTime
 As
 [PropertyObject](propertyobject.html)

[In] Specifies an instance of the TimeDetails custom data type that indicates the time at which the UUT test began.

uut
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the container that describes the UUT.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-open.html language=enus -->
## TOPIC 02340: ResultLogger.Open

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-open.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-open.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.Open( path, isOnTheFly, logInSeparateThread) Purpose Opens the results file you specify for writing and creates the file if it does not exist. Parameters path As String [In] Specifies the absolute path of the file in which to store results. isOnTheFly As Boolean [In] Specifies to

### ResultLogger.Open

#### Syntax

[ResultLogger](resultlogger.html).Open( path, isOnTheFly, logInSeparateThread)

#### Purpose

Opens the results file you specify for writing and creates the file if it does not exist.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute path of the file in which to store results.

isOnTheFly
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies to log results on-the-fly by calling the
 [ResultLogger.LogOnTheFlyStepResults](resultlogger-logontheflystepresults.html)
 method. If you pass
 True
 , TestStand does not log results attached as subproperties of the
 uutResult
 parameter of the
 [ResultLogger.LogPostUUT](resultlogger-logpostuut.html)
 method because TestStand logs those values when you call the
 ResultLogger.LogOnTheFlyStepResults
 method.

logInSeparateThread
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies to write the results to the file from a separate thread. If you pass
 True
 , the
 [ResultLogger.LogBatchDone](resultlogger-logbatchdone.html)
 ,
 [ResultLogger.LogBatchStart](resultlogger-logbatchstart.html)
 ,
 [ResultLogger.LogBegin](resultlogger-logbegin.html)
 ,
 [ResultLogger.LogEnd](resultlogger-logend.html)
 ,
 [ResultLogger.LogOnTheFlyStepResults](resultlogger-logontheflystepresults.html)
 ,
 [ResultLogger.LogPostBatch](resultlogger-logpostbatch.html)
 ,
 [ResultLogger.LogPostUUT](resultlogger-logpostuut.html)
 ,
 [ResultLogger.LogPreBatch](resultlogger-logprebatch.html)
 ,
 [ResultLogger.LogPreUUT](resultlogger-logpreuut.html)
 ,
 [ResultLogger.LogUUTDone](resultlogger-loguutdone.html)
 , and
 [ResultLogger.LogUUTStart](resultlogger-loguutstart.html)
 methods return immediately after queuing data to the writing thread.

#### See Also

[ResultLogger.LogBatchDone](resultlogger-logbatchdone.html)

[ResultLogger.LogBatchStart](resultlogger-logbatchstart.html)

[ResultLogger.LogBegin](resultlogger-logbegin.html)

[ResultLogger.LogEnd](resultlogger-logend.html)

[ResultLogger.LogOnTheFlyStepResults](resultlogger-logontheflystepresults.html)

[ResultLogger.LogPostBatch](resultlogger-logpostbatch.html)

[ResultLogger.LogPostUUT](resultlogger-logpostuut.html)

[ResultLogger.LogPreBatch](resultlogger-logprebatch.html)

[ResultLogger.LogPreUUT](resultlogger-logpreuut.html)

[ResultLogger.LogUUTDone](resultlogger-loguutdone.html)

[ResultLogger.LogUUTStart](resultlogger-loguutstart.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-path.html language=enus -->
## TOPIC 02341: ResultLogger.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.Path Data Type String Purpose Specifies the name of the TestStand results ( .tsr ) file on disk. You can change the path while logging to rename the file to best describe the contents of the file.

### ResultLogger.Path

#### Syntax

[ResultLogger](resultlogger.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the TestStand results (
 .tsr
 ) file on disk. You can change the path while logging to rename the file to best describe the contents of the file.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger-recordfileswritten.html language=enus -->
## TOPIC 02342: ResultLogger.RecordFilesWritten

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger-recordfileswritten.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger-recordfileswritten.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax ResultLogger.RecordFilesWritten Data Type Boolean Purpose Specifies to store the paths of all offline results ( .tsr ) files when TestStand completes writing the file. The default value is False , which specifies to not record the filepaths. When this property is True , the internal record of

### ResultLogger.RecordFilesWritten

#### Syntax

[ResultLogger](resultlogger.html).RecordFilesWritten

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to store the paths of all offline results (
 .tsr
 ) files when TestStand completes writing the file. The default value is
 False
 , which specifies to not record the filepaths. When this property is
 True
 , the internal record of completed files grows without bound unless you periodically pass
 True
 to the
 [ResultLogger.GetFilesWritten](resultlogger-getfileswritten.html)
 method to clear the internal record.

#### Remarks

Changing the value of the
 ResultLogger.RecordFilesWritten
 property from
 True
 to
 False
 only prevents TestStand from recording additional completed files and does not clear the internal record of files already completed. Call the
 ResultLogger.GetFilesWritten
 method to obtain or clear the list of complete offline results files.

You can also modify the PreUUTLoop callback to record completed files.

#### See Also

[ResultLogger.GetFilesWritten](resultlogger-getfileswritten.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogger.html language=enus -->
## TOPIC 02343: ResultLogger

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogger.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogger.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: ResultLogger objects write TestStand results to a file. Use a ResultLog object to read the results from the file. Properties Path RecordFilesWritten Methods Close ContinueInNewFile DeferrableRename Flush GetFilesWritten LogBatchDone LogBatchStart LogBegin LogEnd LogOnTheFlyStepResults LogPostBatch L

### ResultLogger

ResultLogger
 objects write TestStand results to a file. Use a
 [ResultLog](resultlog.html)
 object to read the results from the file.

#### Properties

| Path |
| --- |
| RecordFilesWritten |

#### Methods

| Close |
| --- |
| ContinueInNewFile |
| DeferrableRename |
| Flush |
| GetFilesWritten |
| LogBatchDone |
| LogBatchStart |
| LogBegin |
| LogEnd |
| LogOnTheFlyStepResults |
| LogPostBatch |
| LogPostUUT |
| LogPreBatch |
| LogPreUUT |
| LogUUTDone |
| LogUUTStart |
| Open |

#### See Also

[ResultLog](resultlog.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultlogrecordtypes.html language=enus -->
## TOPIC 02344: ResultLogRecordTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultlogrecordtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultlogrecordtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these options with the ResultLogger methods. ResultLogRecordType_BatchDone –(Value: 9) Indicates a record the ResultLogger.LogBatchDone method creates. The record contains the following objects: [0] ModelData (container) [1] UUT (container) [2] UUTStatus (String) [3] UUTResult (Result) ResultLog

### ResultLogRecordTypes

Use these options with the
 [ResultLogger](resultlogger.html)
 methods.

- ResultLogRecordType_BatchDone 
 –(Value: 9) Indicates a record the
 ResultLogger.LogBatchDone 
 method creates. The record contains the following objects:
  - [0] ModelData (container)
  - [1] UUT (container)
  - [2] UUTStatus (String)
  - [3] UUTResult (Result)
- ResultLogRecordType_BatchStart 
 –(Value: 3) Indicates a record the
 ResultLogger.LogBatchStart 
 method creates. The record contains the following objects:
  - [0] ModelThreadType (NI_ModelThreadType)
  - [1] ModelData (container)
  - [2] ProcessModelClientPath (Path)
  - [3] StartDate (DateDetails)
  - [4] StartTime (TimeDetails)
  - [5] UUT (container)
- ResultLogRecordType_Begin 
 –(Value: 1) Indicates a record the
 ResultLogger.LogBegin 
 method creates. The record contains the following objects:
  - [0] ModelThreadType (NI_ModelThreadType)
  - [1] ModelData (container)
  - [2] ProcessModelClientPath (Path)
  - [3] NumberOfSockets (number)
  - [4] SocketIndex (number)
  - [5] ParentThreadId (number)
  - [6] ParentExecutionId (number)
- ResultLogRecordType_Deleted 
 –(Value: 12) Indicates a result that has been deleted from a TestStand results (
 .tsr 
 ) file.
- ResultLogRecordType_End 
 –(Value: 11) Indicates a record the
 ResultLogger.LogEnd 
 method creates. The record contains the
 [0] ModelData (container) 
 object.
- ResultLogRecordType_NotARecordType 
 –(Value: 0) Indicates a value that is not a valid
 ResultLogRecordType 
 .
- ResultLogRecordType_OnTheFlyStepResults 
 –(Value: 6) Indicates a record the
 ResultLogger.LogOnTheFlyStepResults 
 method creates. The record contains the following objects:
  - [0] UUT (container)
  - [1] CallbackNames (string array)
  - [2] ParentIds (number array)
  - [3] Results(container)
- ResultLogRecordType_PostBatch 
 –(Value: 10) Indicates a record the
 ResultLogger.LogPostBatch 
 method creates. The record contains the following objects:
  - [0] ModelData (container)
  - [1] UUT (container)
  - [2] UUTStatus (String)
  - [3] UUTResult (Result)
- ResultLogRecordType_PostUUT 
 –(Value: 8) Indicates a report the
 ResultLogger.LogPostUUT 
 method creates. The record contains the following objects:
  - [0] ModelData (container)
  - [1] UUT (container)
  - [2] UUTStatus (string)
  - [3] UUTResult (container)
- ResultLogRecordType_PreBatch 
 –(Value: 2) Indicates a record the
 ResultLogger.LogPreBatch 
 method creates. The record contains the following objects:
  - [0] ModelThreadType (NI_ModelThreadType)
  - [1] ModelData (container)
  - [2] ProcessModelClientPath (Path)
  - [3] StartDate (DateDetails)
  - [4] StartTime (TimeDetails)
  - [5] UUT (container)
  - [6] continueTesting (Boolean output parameter)
- ResultLogRecordType_PreUUT 
 –(Value: 4) Indicates a record the
 ResultLogger.LogPreUUT 
 method creates. The record contains the following objects:
  - [0] ModelThreadType (NI_ModelThreadType)
  - [1] ModelData (container)
  - [2] ProcessModelClientPath (Path)
  - [3] StartDate (DateDetails)
  - [4] StartTime (TimeDetails)
  - [5] UUT (container)
  - [6] continueTesting (Boolean output parameter)
- ResultLogRecordType_UUTDone 
 –(Value: 7) Indicates a record the
 ResultLogger.LogUUTDone 
 method creates. The record contains the following objects:
  - [0] ModelData (container)
  - [1] UUT (container)
  - [2] UUTStatus (String)
  - [3] UUTResult (Result)
- ResultLogRecordType_UUTStart 
 –(Value: 5) Indicates a record the
 ResultLogger.LogUUTStart 
 method creates. The record contains the following objects:
  - [0] ModelThreadType (NI_ModelThreadType)
  - [1] ModelData (container)
  - [2] ProcessModelClientPath (Path)
  - [3] StartDate (DateDetails)
  - [4] StartTime (TimeDetails)
  - [5] UUT (container)

#### See Also

[ResultLogger](resultlogger.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/resultrecordingoptions.html language=enus -->
## TOPIC 02345: ResultRecordingOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/resultrecordingoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/resultrecordingoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these options to specify whether a step records a result. ResultRecordingOption_Disabled –(Value: 0) Specifies that the step does not record results. ResultRecordingOption_Enabled –(Value: 1) Specifies that the step records results unless the Sequence.DisableResults or StationOptions.DisableResu

### ResultRecordingOptions

Use these options to specify whether a step records a result.

- ResultRecordingOption_Disabled 
 –(Value: 0) Specifies that the step does not record results.
- ResultRecordingOption_Enabled 
 –(Value: 1) Specifies that the step records results unless the
 Sequence.DisableResults 
 or
 StationOptions.DisableResults 
 property is
 True 
 .
- ResultRecordingOption_EnabledAndOverrideSequenceSetting 
 –(Value: 2) Specifies that the step records results unless the
 StationOptions.DisableResults 
 property is
 True 
 .

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/rteoptions.html language=enus -->
## TOPIC 02346: RTEOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/rteoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/rteoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the StationOptions.RTEOption and Execution.RTEOptionForThisExecution properties, the Thread.SetBatchRTEOption method, the ApplicationMgr.DisplayCustomRunTimeErrorDialog event, or to check the return value for runTimeErrorAction parameter of Engine.DisplayRunTimeErrorDialogEx

### RTEOptions

Use these constants with the
 [StationOptions.RTEOption](stationoptions-rteoption.html)
 and
 [Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)
 properties, the
 [Thread.SetBatchRTEOption](thread-setbatchrteoption.html)
 method, the
 
 [ApplicationMgr.DisplayCustomRunTimeErrorDialog](../tsuiref/applicationmgr-displaycustomruntimeerrordialo.html)
 event, or to check the return value for
 runTimeErrorAction
 parameter of
 [Engine.DisplayRunTimeErrorDialogEx](engine-displayruntimeerrordialogex.html)
 method.

- RTEOption_Abort 
 –(Value: 3) Instructs the execution to abort the execution.
- RTEOption_Continue 
 –(Value: 1) Instructs the execution to process the error by propagating the error to the calling sequence, if one exists. If the current step group is Setup or Main, the execution jumps directly to the Cleanup step group.
- RTEOption_Ignore 
 –(Value: 2) Instructs the execution to ignore the error and continue normal execution.
- RTEOption_Retry 
 –(Value: 4) Instructs the execution to ignore the error and re-execute the step that caused the error condition. For the
 StationOptions.RTEOption 
 property, the
 Execution.RTEOptionForThisExecution 
 property, and the
 Thread.SetBatchRTEOption 
 method, TestStand interprets the
 RTEOption_Retry 
 value as
 RTEOption_Continue 
 .
- RTEOption_ShowDialog 
 –(Value: 0) Instructs the execution to launch the
 Run-Time Error 
 dialog box when an error occurs.

#### See Also

[Engine.DisplayRunTimeErrorDialogEx](engine-displayruntimeerrordialogex.html)

[Execution.RTEOptionForThisExecution](execution-rteoptionforthisexecution.html)

[Run-Time Error dialog box](../tsref/run-time-error-dialog-box.html)

[StationOptions.RTEOption](stationoptions-rteoption.html)

[Thread.SetBatchRTEOption](thread-setbatchrteoption.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runmodes.html language=enus -->
## TOPIC 02347: RunModes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runmodes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runmodes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants to specify the type of action you want to take before executing the step. RunMode_ForceFail –(Value: "Fail") The step does not execute. Instead, the step status is set to Failed . RunMode_ForcePass –(Value: "Pass") The step does not execute. Instead, the step status is set to Pas

### RunModes

Use these constants to specify the type of action you want to take before executing the step.

- RunMode_ForceFail 
 –(Value: "Fail") The step does not execute. Instead, the step status is set to
 Failed 
 .
- RunMode_ForcePass 
 –(Value: "Pass") The step does not execute. Instead, the step status is set to
 Passed 
 .
- RunMode_Normal 
 –(Value: "Normal") The step executes normally.
- RunMode_Skip 
 –(Value: "Skip") The step does not execute. Instead, the step status is set to
 Skipped 
 .

#### See Also

[Step.GetRunModeEx](step-getrunmodeex.html)

[Step.SetRunModeEx](step-setrunmodeex.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitem-editsselectedfile.html language=enus -->
## TOPIC 02348: RunTimeMenuItem.EditsSelectedFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitem-editsselectedfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitem-editsselectedfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItem.EditsSelectedFile Data Type Boolean Purpose Returns a value that indicates whether the tools menu item edits the selected sequence file. Remarks This property applies only to sequence and sequence file item types. The sequence editor uses this option to determine whether to pr

### RunTimeMenuItem.EditsSelectedFile

#### Syntax

[RunTimeMenuItem](runtimemenuitem.html).EditsSelectedFile

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the tools menu item edits the selected sequence file.

#### Remarks

This property applies only to sequence and sequence file item types. The sequence editor uses this option to determine whether to prompt the user to check out the selected file from source code control, if it is not already checked out.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitem-invokeitem.html language=enus -->
## TOPIC 02349: RunTimeMenuItem.InvokeItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitem-invokeitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitem-invokeitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItem.InvokeItem( editArgsParam, reserved = 0) Purpose Executes the action the menu item specifies. Remarks This method has no effect when called on a menu item that represents a submenu. Parameters editArgsParam As Variant [In] Specifies which items in the user interface are curren

### RunTimeMenuItem.InvokeItem

#### Syntax

[RunTimeMenuItem](runtimemenuitem.html).InvokeItem( editArgsParam, reserved = 0)

#### Purpose

Executes the action the menu item specifies.

#### Remarks

This method has no effect when called on a menu item that represents a submenu.

#### Parameters

editArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies which items in the user interface are currently selected.

reserved
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 for this parameter.

This parameter has a default value of
 0
 .

#### See Also

[EditTimeMenuItem.CommandPath](edittimemenuitem-commandpath.html)

[EditTimeMenuItem.SequenceFilePath](edittimemenuitem-sequencefilepath.html)

[EditTimeMenuItem.SequenceName](edittimemenuitem-sequencename.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitem-itemenabled.html language=enus -->
## TOPIC 02350: RunTimeMenuItem.ItemEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitem-itemenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitem-itemenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItem.ItemEnabled Data Type Boolean Purpose Returns a value that indicates whether the expression the EditTimeMenuItem.EnabledExpression property defines returned True or False . See Also EditTimeMenuItem.EnabledExpression EditTimeMenuItem.ItemTextExpression

### RunTimeMenuItem.ItemEnabled

#### Syntax

[RunTimeMenuItem](runtimemenuitem.html).ItemEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the expression the
 [EditTimeMenuItem.EnabledExpression](edittimemenuitem-enabledexpression.html)
 property defines returned
 True
 or
 False
 .

#### See Also

[EditTimeMenuItem.EnabledExpression](edittimemenuitem-enabledexpression.html)

[EditTimeMenuItem.ItemTextExpression](edittimemenuitem-itemtextexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitem-separatorbefore.html language=enus -->
## TOPIC 02351: RunTimeMenuItem.SeparatorBefore

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitem-separatorbefore.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitem-separatorbefore.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItem.SeparatorBefore Data Type Boolean Purpose Returns a value that indicates whether a menu separator precedes the Tools menu item.

### RunTimeMenuItem.SeparatorBefore

#### Syntax

[RunTimeMenuItem](runtimemenuitem.html).SeparatorBefore

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether a menu separator precedes the Tools menu item.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitem-submenuitems.html language=enus -->
## TOPIC 02352: RunTimeMenuItem.SubMenuItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitem-submenuitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitem-submenuitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItem.SubMenuItems Data Type RunTimeMenuItems Purpose Returns a collection of Tools menu items that represent the submenu for the menu item. Remarks This property only exists when the value of the EditTimeMenuItem.Type property is ToolMenuType_SubMenu or ToolMenuType_SequenceFile .

### RunTimeMenuItem.SubMenuItems

#### Syntax

[RunTimeMenuItem](runtimemenuitem.html).SubMenuItems

#### Data Type

[RunTimeMenuItems](runtimemenuitems.html)

#### Purpose

Returns a collection of Tools menu items that represent the submenu for the menu item.

#### Remarks

This property only exists when the value of the
 [EditTimeMenuItem.Type](edittimemenuitem-type.html)
 property is
 ToolMenuType_SubMenu
 or
 ToolMenuType_SequenceFile
 .

#### See Also

[EditTimeMenuItem.Type](edittimemenuitem-type.html)

[RunTimeMenuItems](runtimemenuitems.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitem-text.html language=enus -->
## TOPIC 02353: RunTimeMenuItem.Text

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitem-text.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitem-text.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItem.Text Data Type String Purpose Returns from the EditTimeMenuItem.ItemTextExpression property the menu item text the expression defines. See Also EditTimeMenuItem.ItemTextExpression

### RunTimeMenuItem.Text

#### Syntax

[RunTimeMenuItem](runtimemenuitem.html).Text

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns from the
 [EditTimeMenuItem.ItemTextExpression](edittimemenuitem-itemtextexpression.html)
 property the menu item text the expression defines.

#### See Also

[EditTimeMenuItem.ItemTextExpression](edittimemenuitem-itemtextexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitem.html language=enus -->
## TOPIC 02354: RunTimeMenuItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the RunTimeMenuItem class represent an evaluated version of a EditTimeMenuItem object. The properties of the RunTimeMenuItem object specify the item text, if the menu item is disabled, and if a separator appears before it. You can use the RunTimeMenuItem.InvokeItem method to execute the i

### RunTimeMenuItem

Objects of the
 RunTimeMenuItem
 class represent an evaluated version of a
 [EditTimeMenuItem](edittimemenuitem.html)
 object. The properties of the
 RunTimeMenuItem
 object specify the item text, if the menu item is disabled, and if a separator appears before it. You can use the
 [RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)
 method to execute the item, which launches a sequence in a new execution or an executable.

Use the
 [Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)
 method to obtain a reference to a collection of this class for the Tools menu. Use this collection to determine what to display in the Tools menu at run time.

#### Properties

| EditsSelectedFile (Read Only) |
| --- |
| ItemEnabled (Read Only) |
| SeparatorBefore (Read Only) |
| SubMenuItems (Read Only) |
| Text (Read Only) |

#### Method

| InvokeItem |
| --- |

#### See Also

[EditTimeMenuItem](edittimemenuitem.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitems-count.html language=enus -->
## TOPIC 02355: RunTimeMenuItems.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitems-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitems-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItems.Count Data Type Long Purpose Returns the number of items in the collection.

### RunTimeMenuItems.Count

#### Syntax

[RunTimeMenuItems](runtimemenuitems.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitems-item.html language=enus -->
## TOPIC 02356: RunTimeMenuItems.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitems-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitems-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax RunTimeMenuItems.Item( index) Data Type RunTimeMenuItem Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also RunTimeMenuItem RunTimeMenuItems.Count

### RunTimeMenuItems.Item

#### Syntax

[RunTimeMenuItems](runtimemenuitems.html).Item( index)

#### Data Type

[RunTimeMenuItem](runtimemenuitem.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[RunTimeMenuItem](runtimemenuitem.html)

[RunTimeMenuItems.Count](runtimemenuitems-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/runtimemenuitems.html language=enus -->
## TOPIC 02357: RunTimeMenuItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/runtimemenuitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/runtimemenuitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The RunTimeMenuItems class specifies a collection of RunTimeMenuItem objects, which represent an evaluated version of a EditTimeMenuItem object. The properties of the RunTimeMenuItem object specify the item text and if the menu item is disabled. You can use the RunTimeMenuItem.InvokeItem method to e

### RunTimeMenuItems

The RunTimeMenuItems class specifies a collection of RunTimeMenuItem objects, which represent an evaluated version of a EditTimeMenuItem object. The properties of the RunTimeMenuItem object specify the item text and if the menu item is disabled. You can use the
 [RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)
 method to execute the item, which launches an executable or a sequence in a new execution.

Use this collection to determine what to display in the Tools menu at run time. Use the
 [Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)
 method to obtain a reference to a collection of this class for the Tools menu.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/saveallseqfileoptions.html language=enus -->
## TOPIC 02358: SaveAllSeqFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/saveallseqfileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/saveallseqfileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the Engine.SaveAllModifiedSeqFiles method. Use the bitwise-OR operator to specify more than one option. SaveAllSeqFiles_NoOptions –(Value: 0x0) No options. SaveAllSeqFiles_PromptUser –(Value: 0x1) Prompts the user with a

### SaveAllSeqFileOptions

These constants represent the options you can use with the
 options
 parameter of the
 [Engine.SaveAllModifiedSeqFiles](engine-saveallmodifiedseqfiles.html)
 method. Use the bitwise-OR operator to specify more than one option.

- SaveAllSeqFiles_NoOptions 
 –(Value: 0x0) No options.
- SaveAllSeqFiles_PromptUser 
 –(Value: 0x1) Prompts the user with a dialog box containing Yes, No, and Cancel buttons before saving the file.

#### See Also

[Engine.SaveAllModifiedSeqFiles](engine-saveallmodifiedseqfiles.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/saveworkspacefileoptions.html language=enus -->
## TOPIC 02359: SaveWorkspaceFileOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/saveworkspacefileoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/saveworkspacefileoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the options parameter of the WorkspaceFile.SaveWorkspaceAndProjectFiles method. Use the bitwise-OR operator to specify more than one option. SaveWorkspaceFile_NoOptions –(Value: 0x0) No options. SaveWorkspaceFile_PromptUser –(Value: 0x1) If this

### SaveWorkspaceFileOptions

These constants represent the options you can use with the
 options
 parameter of the
 [WorkspaceFile.SaveWorkspaceAndProjectFiles](workspacefile-saveworkspaceandprojectfiles.html)
 method. Use the bitwise-OR operator to specify more than one option.

- SaveWorkspaceFile_NoOptions 
 –(Value: 0x0) No options.
- SaveWorkspaceFile_PromptUser 
 –(Value: 0x1) If this flag is set, TestStand prompts the user to save all modified files.
- SaveWorkspaceFile_SkipReadOnlyFiles 
 –(Value: 0x4) If this flag is set, TestStand skips all read-only files.
- SaveWorkspaceFile_SkipWorkspaceFile 
 –(Value: 0x2) If this flag is set, TestStand skips the workspace file.

#### See Also

[WorkspaceFile.SaveWorkspaceAndProjectFiles](workspacefile-saveworkspaceandprojectfiles.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectories-count.html language=enus -->
## TOPIC 02360: SearchDirectories.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectories-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectories-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectories.Count Data Type Long Purpose Returns the number of items in the collection.

### SearchDirectories.Count

#### Syntax

[SearchDirectories](searchdirectories.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectories-insert.html language=enus -->
## TOPIC 02361: SearchDirectories.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectories-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectories-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectories.Insert( path, index = -1, searchSubDirs = False, fileExtRestrict = "", exclude = False, disabled = False) Purpose Adds a new item to the collection. Remarks A search directory is a search path for finding files. Parameters path As String [In] Specifies the path used to find

### SearchDirectories.Insert

#### Syntax

[SearchDirectories](searchdirectories.html).Insert( path, index = -1, searchSubDirs = False, fileExtRestrict = "", exclude = False, disabled = False)

#### Purpose

Adds a new item to the collection.

#### Remarks

A
 [search directory](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 is a search path for finding files.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the path used to find files.

index
 As
 [Long](data-types-for-teststand.html)

[In] TestStand maintains an internal list of search directories in which the lower index paths take precedence over the higher index paths. The
 index
 parameter specifies the index where the new search directory must be inserted. If you pass a value of -1, the new directory is inserted at the end of the list.

This parameter has a default value of
 -1
 .

searchSubDirs
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to include all subdirectories within the selected path in the overall search path.

This parameter has a default value of
 False
 .

fileExtRestrict
 As
 [String](data-types-for-teststand.html)

[In] Specifies the specific file extensions that restrict which files apply to the search directory. If the
 exclude
 parameter is
 False
 , TestStand searches in the directories only for files with the specified extensions. If the
 exclude
 parameter is
 True
 , TestStand searches in the directories for files that do not have the specified file extensions. For example, to search for only DLLs and executable files, pass
 "DLL,EXE"
 for this parameter and
 False
 for the
 exclude
 parameter.

This parameter has a default value of
 ""
 .

exclude
 As
 [Boolean](data-types-for-teststand.html)

[In] If you pass
 False
 , TestStand searches only for files with the specific file extensions specified in the fileExtRestrict parameter. If you pass
 True
 , TestStand searches for files without the specific extension.

This parameter has a default value of
 False
 .

disabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Set this parameter to
 False
 if you want the search directory to be included in the overall search path. This setting allows the user to disable the search directory without deleting it from the list.

This parameter has a default value of
 False
 .

#### See Also

[SearchDirectoryTypes](searchdirectorytypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectories-item.html language=enus -->
## TOPIC 02362: SearchDirectories.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectories-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectories-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectories.Item( index) Data Type SearchDirectory Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also SearchDirectory

### SearchDirectories.Item

#### Syntax

[SearchDirectories](searchdirectories.html).Item( index)

#### Data Type

[SearchDirectory](searchdirectory.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[SearchDirectory](searchdirectory.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectories-movesearchdirectory.html language=enus -->
## TOPIC 02363: SearchDirectories.MoveSearchDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectories-movesearchdirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectories-movesearchdirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectories.MoveSearchDirectory( index, newIndex) Purpose Moves a search directory within the collection. Remarks TestStand maintains an internal list of search directories in which the lower index paths take precedence over the higher index paths. Parameters index As Long [In] Specifie

### SearchDirectories.MoveSearchDirectory

#### Syntax

[SearchDirectories](searchdirectories.html).MoveSearchDirectory( index, newIndex)

#### Purpose

Moves a search directory within the collection.

#### Remarks

TestStand maintains an internal list of search directories in which the lower index paths take precedence over the higher index paths.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index indicating the new position of the search directory to move.

newIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index indicating the new position of the search directory to move.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectories-reload.html language=enus -->
## TOPIC 02364: SearchDirectories.Reload

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectories-reload.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectories-reload.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectories.Reload Purpose Instructs TestStand to discard the current search directory list and reload the list from disk. Remarks TestStand immediately updates the TestExec.ini configuration file when you make changes to the search directories programmatically or by using a user interf

### SearchDirectories.Reload

#### Syntax

[SearchDirectories](searchdirectories.html).Reload

#### Purpose

Instructs TestStand to discard the current
 [search directory](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 list and reload the list from disk.

#### Remarks

Note

TestExec.ini

SearchDirectories.Reload

TestExec.ini

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectories-remove.html language=enus -->
## TOPIC 02365: SearchDirectories.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectories-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectories-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectories.Remove( index) Purpose Removes the specified item from this collection, if it exists. Remarks You cannot delete predefined search directories . Parameters index As Long [In] Specifies the zero-based index of the item to remove.

### SearchDirectories.Remove

#### Syntax

[SearchDirectories](searchdirectories.html).Remove( index)

#### Purpose

Removes the specified item from this collection, if it exists.

#### Remarks

You cannot delete predefined
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to remove.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectories.html language=enus -->
## TOPIC 02366: SearchDirectories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This collection class contains elements using the SearchDirectory type. The collection specifies the directories TestStand searches for finding files. The directories listed first in the collection take precedence over those listed later in the collection. When you run TestStand for the first time,

### SearchDirectories

This collection class contains elements using the SearchDirectory type. The collection specifies the directories TestStand searches for finding files. The directories listed first in the collection take precedence over those listed later in the collection. When you run TestStand for the first time, the collection contains a default set of
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Insert |
| --- |
| MoveSearchDirectory |
| Reload |
| Remove |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory-disabled.html language=enus -->
## TOPIC 02367: SearchDirectory.Disabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory-disabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory-disabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectory.Disabled Data Type Boolean Purpose If you want the search directory to be included in the overall search path, set this property to False . If you set this property to True , the search directory is disabled but is included in the search directories list.

### SearchDirectory.Disabled

#### Syntax

[SearchDirectory](searchdirectory.html).Disabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If you want the search directory to be included in the overall search path, set this property to
 False
 . If you set this property to
 True
 , the search directory is disabled but is included in the
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 list.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory-excludefileextension.html language=enus -->
## TOPIC 02368: SearchDirectory.ExcludeFileExtension

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory-excludefileextension.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory-excludefileextension.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectory.ExcludeFileExtension Data Type Boolean Purpose Set this property to False if you want TestStand to search only for files with the file extensions you specify in the SearchDirectory.FileExtensionRestrictions property. Set this property to True if you want TestStand to search on

### SearchDirectory.ExcludeFileExtension

#### Syntax

[SearchDirectory](searchdirectory.html).ExcludeFileExtension

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 False
 if you want TestStand to search only for files with the file extensions you specify in the
 [SearchDirectory.FileExtensionRestrictions](searchdirectory-fileextensionrestrictions.html)
 property. Set this property to
 True
 if you want TestStand to search only for files that do not have the file extensions specified in the
 SearchDirectory.FileExtensionRestrictions
 property.

#### See Also

[SearchDirectory.FileExtensionRestrictions](searchdirectory-fileextensionrestrictions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory-excludehiddensubdirectories.html language=enus -->
## TOPIC 02369: SearchDirectory.ExcludeHiddenSubdirectories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory-excludehiddensubdirectories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory-excludehiddensubdirectories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectory.ExcludeHiddenSubdirectories Data Type Boolean Purpose Specifies to exclude search directory subdirectories that specify the Hidden attribute in the Microsoft Windows file system. This property is False by default and has no effect unless the SearchDirectory.SearchSubdirectorie

### SearchDirectory.ExcludeHiddenSubdirectories

#### Syntax

[SearchDirectory](searchdirectory.html).ExcludeHiddenSubdirectories

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to exclude search directory subdirectories that specify the Hidden attribute in the Microsoft Windows file system. This property is
 False
 by default and has no effect unless the
 [SearchDirectory.SearchSubdirectories](searchdirectory-searchsubdirectories.html)
 property is
 True
 .

#### See Also

[SearchDirectory.SearchSubdirectories](searchdirectory-searchsubdirectories.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory-fileextensionrestrictions.html language=enus -->
## TOPIC 02370: SearchDirectory.FileExtensionRestrictions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory-fileextensionrestrictions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory-fileextensionrestrictions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectory.FileExtensionRestrictions Data Type String Purpose Specifies the specific file extensions that restrict which files apply to the search directory . If the SearchDirectory.ExcludeFileExtension property is False , TestStand searches only for files in the directory with the speci

### SearchDirectory.FileExtensionRestrictions

#### Syntax

[SearchDirectory](searchdirectory.html).FileExtensionRestrictions

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the specific file extensions that restrict which files apply to the
 [search directory](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 . If the
 [SearchDirectory.ExcludeFileExtension](searchdirectory-excludefileextension.html)
 property is
 False
 , TestStand searches only for files in the directory with the specified extension. If the
 exclude
 parameter is
 True
 , TestStand searches only for files in the directory that does not have the specified file extensions. For example, to search only for DLLs and executable files, enter
 "DLL, EXE"
 and set the
 SearchDirectory.ExcludeFileExtension
 property to
 False
 .

#### See Also

[SearchDirectory.ExcludeFileExtension](searchdirectory-excludefileextension.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory-path.html language=enus -->
## TOPIC 02371: SearchDirectory.Path

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory-path.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory-path.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectory.Path Data Type String Purpose Specifies the path used to find files. Remarks Specifies the directory path when the value of the SearchDirectory.Type property is SearchDirectory_ExplicitDir . This property is read-only for all other directory types, and TestStand returns the pa

### SearchDirectory.Path

#### Syntax

[SearchDirectory](searchdirectory.html).Path

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path used to find files.

#### Remarks

Specifies the directory path when the value of the
 [SearchDirectory.Type](searchdirectory-type.html)
 property is
 SearchDirectory_ExplicitDir
 . This property is read-only for all other directory types, and TestStand returns the path of the non-explicit directory. TestStand returns an empty string when the directory type is
 SearchDirectoryType_ContainingProjectDir
 or
 SearchDirectoryType_CurrentSequenceFileDir
 . TestStand returns an empty string if the directory type is
 SearchDirectoryType_CurrentWorkspaceDir
 when no workspace is loaded.

#### See Also

[SearchDirectory.Type](searchdirectory-type.html)

[SearchDirectoryTypes](searchdirectorytypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory-searchsubdirectories.html language=enus -->
## TOPIC 02372: SearchDirectory.SearchSubdirectories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory-searchsubdirectories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory-searchsubdirectories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectory.SearchSubdirectories Data Type Boolean Purpose Specifies whether to include all subdirectories within the selected path in the overall search directory path . See Also SearchDirectory.ExcludeHiddenSubdirectories

### SearchDirectory.SearchSubdirectories

#### Syntax

[SearchDirectory](searchdirectory.html).SearchSubdirectories

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to include all subdirectories within the selected path in the overall
 [search directory path](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[SearchDirectory.ExcludeHiddenSubdirectories](searchdirectory-excludehiddensubdirectories.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory-type.html language=enus -->
## TOPIC 02373: SearchDirectory.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchDirectory.Type Data Type SearchDirectoryTypes Purpose Several types of search directories exist. This property returns the type of search directory . See Also SearchDirectoryTypes

### SearchDirectory.Type

#### Syntax

[SearchDirectory](searchdirectory.html).Type

#### Data Type

[SearchDirectoryTypes](searchdirectorytypes.html)

#### Purpose

Several types of search directories exist. This property returns the type of
 [search directory](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[SearchDirectoryTypes](searchdirectorytypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectory.html language=enus -->
## TOPIC 02374: SearchDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A SearchDirectory object specifies a directory in which TestStand searches for finding files. An object of this class specifies a path to an explicit directory or specifies a predefined directory, such as the TestStand directory or the Microsoft Windows directory. An object specifies any file extens

### SearchDirectory

A SearchDirectory object specifies a
 [directory](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 in which TestStand searches for finding files. An object of this class specifies a path to an explicit directory or specifies a predefined directory, such as the
 TestStand
 directory or the Microsoft
 Windows
 directory. An object specifies any file extension restrictions and whether to search subdirectories.

#### Properties

| Disabled |
| --- |
| ExcludeFileExtension |
| ExcludeHiddenSubdirectories |
| FileExtensionRestrictions |
| Path |
| SearchSubdirectories |
| Type (Read Only) |

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchdirectorytypes.html language=enus -->
## TOPIC 02375: SearchDirectoryTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchdirectorytypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchdirectorytypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SearchDirectoryTypes parameter of the SearchDirectories.Insert method and the SearchDirectory.Type property. SearchDirectoryType_AdapterSupportDir –(Value: 3) Adapter support directory. SearchDirectoryType_ApplicationDir –(Value: 4) Application directory. SearchDirectory

### SearchDirectoryTypes

Use these constants with the
 SearchDirectoryTypes
 parameter of the
 [SearchDirectories.Insert](searchdirectories-insert.html)
 method and the
 [SearchDirectory.Type](searchdirectory-type.html)
 property.

- SearchDirectoryType_AdapterSupportDir 
 –(Value: 3) Adapter support directory.
- SearchDirectoryType_ApplicationDir 
 –(Value: 4) Application directory.
- SearchDirectoryType_ContainingProjectDir 
 –(Value: 14) Containing project directory.
 Note 
 This constant is obsolete. To allow a user to select a file relative to a containing project directory, pass the
 [PropertyObjectFile](propertyobjectfile.html)
 object for the project to the
 currentFile
 parameter of the
 [Engine.DisplayFileDialog](engine-displayfiledialog.html)
 method.
- SearchDirectoryType_CurrentSequenceFileDir 
 –(Value: 9) Current sequence file directory.
- SearchDirectoryType_CurrentWorkspaceDir 
 –(Value: 13) Current workspace directory.
- SearchDirectoryType_ExplicitDir 
 –(Value: 15) Explicit directory.
- SearchDirectoryType_InitialWorkingDir 
 –(Value: 5) Initial working directory.
- SearchDirectoryType_NIComponentsDir 
 –(Value: 12) NI components directory.
- SearchDirectoryType_PathEnvironmentVarDir 
 –(Value: 8) Path environment variable.
- SearchDirectoryType_PublicComponentsDir 
 –(Value: 11) Public components directory.
- SearchDirectoryType_TestStandBinDir 
 –(Value: 2) TestStand Bin directory.
- SearchDirectoryType_TestStandDir 
 –(Value:1) TestStand directory.
- SearchDirectoryType_TestStandPublicDir 
 –(Value: 16) Public directory.
- SearchDirectoryType_UserComponentsDir 
 –(Value: 11) User components directory. This option is obsolete. Use SearchDirectoryType_PublicComponentsDir instead.
- SearchDirectoryType_WindowsDir 
 –(Value: 7) Microsoft Windows directory.
- SearchDirectoryType_WindowsSystemDir 
 –(Value: 6) Windows system directory.

#### See Also

[Engine.DisplayFileDialog](engine-displayfiledialog.html)

[PropertyObjectFile](propertyobjectfile.html)

[SearchDirectories.Insert](searchdirectories-insert.html)

[SearchDirectory.Type](searchdirectory-type.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchelements.html language=enus -->
## TOPIC 02376: SearchElements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchelements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchelements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the elementsToSearch parameter of the PropertyObject.Search and Engine.SearchFiles methods. Use the bitwise-OR operator to specify more than one option. SearchElement_All –(Value: 0xffffffff) A combination of all the SearchElement options. Searc

### SearchElements

These constants represent the options you can use with the
 elementsToSearch
 parameter of the
 [PropertyObject.Search](propertyobject-search.html)
 and
 [Engine.SearchFiles](engine-searchfiles.html)
 methods. Use the bitwise-OR operator to specify more than one option.

- SearchElement_All 
 –(Value: 0xffffffff) A combination of all the SearchElement options.
- SearchElement_AllValues 
 –(Value: 0x1c) A combination of the following SearchElements options:
 SearchElement_StringValue 
 ,
 SearchElement_NumericValue 
 , and
 SearchElement_BooleanValue 
 .
- SearchElement_Attributes 
 –(Value: 0x20) TestStand searches through the attributes and type attributes of properties.
- SearchElement_BooleanValue 
 –(Value: 0x10) TestStand searches the value of Boolean properties.
- SearchElement_Comment 
 –(Value: 0x2) TestStand searches the property comment.
- SearchElement_Enumerators 
 –(Value: 0x80) TestStand searches the enumerators of enumeration data types.
- SearchElement_Name 
 –(Value: 0x1) TestStand searches the property name.
- SearchElement_NumericValue 
 –(Value: 0x8) TestStand searches the value of numeric properties.
- SearchElement_StringValue 
 –(Value: 0x4) TestStand searches the value of string properties.
- SearchElement_TypeName 
 –(Value: 0x40) TestStand searches the type name of root type instance properties. Enable this option to find all the instances of a particular type definition.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchfilteroptions.html language=enus -->
## TOPIC 02377: SearchFilterOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchfilteroptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchfilteroptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the filterOptions parameter of the PropertyObject.Search and Engine.SearchFiles methods. Use the bitwise-OR operator to specify more than one option. SearchFilterOptions_All –(Value: 0x00ffffff) If this options is set, TestStand searches all par

### SearchFilterOptions

These constants represent the options you can use with the
 filterOptions
 parameter of the
 [PropertyObject.Search](propertyobject-search.html)
 and
 [Engine.SearchFiles](engine-searchfiles.html)
 methods. Use the bitwise-OR operator to specify more than one option.

- SearchFilterOptions_All 
 –(Value: 0x00ffffff) If this options is set, TestStand searches all parts of files.
- SearchFilterOptions_BuiltinSeqAndSeqFileProps 
 –(Value: 0x400) If this option is set, TestStand searches built-in sequence and sequence file properties. These properties contain the settings associated with sequences and sequence files. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_BuiltinStepProps 
 –(Value: 0x20) If this option is set, TestStand searches built-in step properties. You must use
 SearchFilterOptions_Steps 
 in combination with this option.
- SearchFilterOptions_CustomDataTypes 
 –(Value: 0x100) If this option is set, TestStand searches custom data types. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_CustomStepProps 
 –(Value: 0x10) If this option is set, TestStand searches custom step properties. You must use
 SearchFilterOptions_Steps 
 in combination with this option.
- SearchFilterOptions_FileGlobals 
 –(Value: 0x4) If this option is set, TestStand searches sequence file global variables. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_Locals 
 –(Value: 0x1) If this option is set, TestStand searches sequence local variables. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_ModuleStepProps 
 –(Value: 0x40) If this option is set, TestStand searches module step properties. You must use
 SearchFilterOptions_Steps 
 in combination with this option.
- SearchFilterOptions_Parameters 
 –(Value: 0x2) If this option is set, TestStand searches sequence parameter variables. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_StandardDataTypes 
 –(Value: 0x200) If this option is set, TestStand searches standard data types. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_Steps 
 –(Value: 0x8) If this option is set, TestStand searches steps. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_StepTypes 
 –(Value: 0x80) If this option is set, TestStand searches step types. This option applies only to the
 Engine.SearchFiles 
 method.
- SearchFilterOptions_TypesOnly 
 –(Value: 0x01000000) If this option is set, TestStand searches only types. You must specify which category of types to search by setting one or more of the following options:
 SearchFilterOptions_StepTypes 
 ,
 SearchFilterOptions_CustomDataTypes 
 , or
 SearchFilterOptions_StandardDataTypes 
 . This option applies only to the
 Engine.SearchFiles 
 method.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-filedisplayname.html language=enus -->
## TOPIC 02378: SearchMatch.FileDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-filedisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-filedisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.FileDisplayName Data Type String Purpose Returns the display name of the file in which the match was found. See Also PropertyObjectFile.DisplayName SearchResults

### SearchMatch.FileDisplayName

#### Syntax

[SearchMatch](searchmatch.html).FileDisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the display name of the file in which the match was found.

#### See Also

[PropertyObjectFile.DisplayName](propertyobjectfile-displayname.html)

[SearchResults](searchresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-fileid.html language=enus -->
## TOPIC 02379: SearchMatch.FileId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-fileid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-fileid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.FileId Data Type Long Purpose Returns the unique file ID of the file in which the match was found. This value is the same as the value the PropertyObjectFile.Id property returns. Remarks ID numbers change when a file is closed and reopened. Therefore, even if a file has a differen

### SearchMatch.FileId

#### Syntax

[SearchMatch](searchmatch.html).FileId

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the unique file ID of the file in which the match was found. This value is the same as the value the
 [PropertyObjectFile.Id](propertyobjectfile-id.html)
 property returns.

#### Remarks

ID numbers change when a file is closed and reopened. Therefore, even if a file has a different ID than what this property contains, it might be the same file. Check the
 [SearchMatch.FilePath](searchmatch-filepath.html)
 property against the absolute path of the file, if one is available, to determine whether the file is the same.

#### See Also

[PropertyObjectFile.Id](propertyobjectfile-id.html)

[SearchMatch.FilePath](searchmatch-filepath.html)

[SearchResults](searchresults.html)

[SequenceFile.Id](sequencefile-id.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-filepath.html language=enus -->
## TOPIC 02380: SearchMatch.FilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-filepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-filepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.FilePath Data Type String Purpose Returns the absolute file path of the file in which the match was found. Remarks Returns an empty string for unsaved files. Use the SearchMatch.FileDisplayName property to obtain a unique name for unsaved files. See Also PropertyObjectFile.Path Se

### SearchMatch.FilePath

#### Syntax

[SearchMatch](searchmatch.html).FilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute file path of the file in which the match was found.

#### Remarks

Returns an empty string for unsaved files. Use the
 [SearchMatch.FileDisplayName](searchmatch-filedisplayname.html)
 property to obtain a unique name for unsaved files.

#### See Also

[PropertyObjectFile.Path](propertyobjectfile-path.html)

[SearchMatch.FileDisplayName](searchmatch-filedisplayname.html)

[SearchResults](searchresults.html)

[SequenceFile.Path](sequencefile-path.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-getlocation.html language=enus -->
## TOPIC 02381: SearchMatch.GetLocation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-getlocation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-getlocation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.GetLocation( matchElement, matchStart, matchLength) Purpose Returns the element of the property where the match was found and the location of the match within the property when the value is coerced to a string. Remarks Use the SearchMatch.MatchedText property to obtain the entire

### SearchMatch.GetLocation

#### Syntax

[SearchMatch](searchmatch.html).GetLocation( matchElement, matchStart, matchLength)

#### Purpose

Returns the element of the property where the match was found and the location of the match within the property when the value is coerced to a string.

#### Remarks

Use the
 [SearchMatch.MatchedText](searchmatch-matchedtext.html)
 property to obtain the entire element value as a coerced string in which the match was found.

#### Parameters

matchElement
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the element of the property in which the match was found. The value of this parameter is one of the
 [SearchElements](searchelements.html)
 constants.

matchStart
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the zero-based index within the string of the starting character location of the match. Use the
 [SearchMatch.MatchedText](searchmatch-matchedtext.html)
 property to obtain the entire string in which the match was found.

matchLength
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of characters of the text that are part of the match.

#### See Also

[SearchElements](searchelements.html)

[SearchMatch.MatchedText](searchmatch-matchedtext.html)

[SearchResults](searchresults.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-getpropertypath.html language=enus -->
## TOPIC 02382: SearchMatch.GetPropertyPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-getpropertypath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-getpropertypath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.GetPropertyPath( useNamesForIndices) Return Value String Purpose Call this method to obtain the lookup string that indicates the location of the property that contains the match. Remarks If the match is from a SearchResults object that the Engine.SearchFiles method returns and the

### SearchMatch.GetPropertyPath

#### Syntax

[SearchMatch](searchmatch.html).GetPropertyPath( useNamesForIndices)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Call this method to obtain the lookup string that indicates the location of the property that contains the match.

#### Remarks

If the match is from a
 [SearchResults](searchresults.html)
 object that the
 [Engine.SearchFiles](engine-searchfiles.html)
 method returns and the
 [SearchMatch.TypeCategoryOfMatch](searchmatch-typecategoryofmatch.html)
 property is
 TypeCategory_None
 , the
 SearchMatch.GetPropertyPath
 method returns a lookup string relative to the
 [PropertyObjectFile.Data](propertyobjectfile-data.html)
 property. Prepend
 Data.
 to use this lookup string relative to the root of the
 [PropertyObjectFile](propertyobjectfile.html)
 object.

#### Parameters

useNamesForIndices
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to obtain a property path that uses property names for array indexes when possible. The name of an object element in an array is not guaranteed to be unique within the array. If you pass
 True
 for this parameter, do not use the returned property path with methods that have a
 lookupString
 parameter, such as the
 [PropertyObject.GetPropertyObject](propertyobject-getpropertyobject.html)
 method and the
 [PropertyObject.Exists](propertyobject-exists.html)
 method.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Exists](propertyobject-exists.html)

[PropertyObject.GetPropertyObject](propertyobject-getpropertyobject.html)

[SearchMatch.TypeCategoryOfMatch](searchmatch-typecategoryofmatch.html)

[SearchResults](searchresults.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-matchedtext.html language=enus -->
## TOPIC 02383: SearchMatch.MatchedText

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-matchedtext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-matchedtext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.MatchedText Data Type String Purpose Returns the text string which contains the match. Use the SearchMatch.GetLocation method to determine which element of the property the string is from. Remarks Use the SearchMatch.UpdateForReplace method to alter the matched text. Use the Searc

### SearchMatch.MatchedText

#### Syntax

[SearchMatch](searchmatch.html).MatchedText

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the text string which contains the match. Use the
 [SearchMatch.GetLocation](searchmatch-getlocation.html)
 method to determine which element of the property the string is from.

#### Remarks

Use the
 [SearchMatch.UpdateForReplace](searchmatch-updateforreplace.html)
 method to alter the matched text. Use the
 [SearchMatch.UpdateForReplaceValue](searchmatch-updateforreplacevalue.html)
 method to alter the value of the property in which the match was found.

#### See Also

[SearchMatch.GetLocation](searchmatch-getlocation.html)

[SearchMatch.UpdateForReplace](searchmatch-updateforreplace.html)

[SearchMatch.UpdateForReplaceValue](searchmatch-updateforreplacevalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-matchisvalid.html language=enus -->
## TOPIC 02384: SearchMatch.MatchIsValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-matchisvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-matchisvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.MatchIsValid Data Type Boolean Purpose Returns a value that indicates whether the match is valid. When this property is False , do not call the SearchMatch.UpdateForReplace method. Remarks This property is set to False when a call to the SearchMatch.UpdateForReplaceValue method in

### SearchMatch.MatchIsValid

#### Syntax

[SearchMatch](searchmatch.html).MatchIsValid

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the match is valid. When this property is
 False
 , do not call the
 [SearchMatch.UpdateForReplace](searchmatch-updateforreplace.html)
 method.

#### Remarks

This property is set to
 False
 when a call to the
 [SearchMatch.UpdateForReplaceValue](searchmatch-updateforreplacevalue.html)
 method invalidates or replaces the text that the match found.

#### See Also

[SearchMatch.UpdateForReplace](searchmatch-updateforreplace.html)

[SearchMatch.UpdateForReplaceValue](searchmatch-updateforreplacevalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-propertyvalueasstring.html language=enus -->
## TOPIC 02385: SearchMatch.PropertyValueAsString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-propertyvalueasstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-propertyvalueasstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.PropertyValueAsString Data Type String Purpose Returns a string that describes the value of the property that contains the match. This string is equivalent to the string the PropertyObject.GetFormattedValue method returns. If the property that contains the match does not have a va

### SearchMatch.PropertyValueAsString

#### Syntax

[SearchMatch](searchmatch.html).PropertyValueAsString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a string that describes the value of the property that contains the match. This string is equivalent to the string the
 [PropertyObject.GetFormattedValue](propertyobject-getformattedvalue.html)
 method returns. If the property that contains the match does not have a value, this property returns an empty string.

#### See Also

[PropertyObject.GetFormattedValue](propertyobject-getformattedvalue.html)

[SearchResults](searchresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-propertyvaluetype.html language=enus -->
## TOPIC 02386: SearchMatch.PropertyValueType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-propertyvaluetype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-propertyvaluetype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.PropertyValueType Data Type PropertyValueTypes Use the following constants with this data type: PropValType_Array –(Value: 6) Specifies an array. This is not a valid value for PropertyObject creation methods such as Engine.NewPropertyObject and PropertyObject.NewSubProperty . Prop

### SearchMatch.PropertyValueType

#### Syntax

[SearchMatch](searchmatch.html).PropertyValueType

#### Data Type

[PropertyValueTypes](propertyvaluetypes.html)

Use the following constants with this data type:

- PropValType_Array 
 –(Value: 6) Specifies an array. This is not a valid value for PropertyObject creation methods such as
 Engine.NewPropertyObject 
 and
 PropertyObject.NewSubProperty 
 .
- PropValType_Boolean 
 –(Value: 2) Specifies a Boolean type.
- PropValType_Container 
 –(Value: 0) Specifies a container.
- PropValType_Enum 
 –(Value: 7) Specifies an enumeration.
- PropValType_NamedType 
 –(Value: 4) Use this value with PropertyObject creation methods such as
 Engine.NewPropertyObject 
 and
 PropertyObject.NewSubProperty 
 to create an instance of a named type. This is not a valid value for the
 PropertyObjectType.ValueType 
 property.
- PropValType_Number 
 –(Value: 3) Specifies a number.
- PropValType_Reference 
 –(Value: 5) Specifies an object reference.
- PropValType_String 
 –(Value: 1) Specifies a string.

#### Purpose

Returns the data type of the property that contains the match.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-typecategoryofmatch.html language=enus -->
## TOPIC 02387: SearchMatch.TypeCategoryOfMatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-typecategoryofmatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-typecategoryofmatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.TypeCategoryOfMatch Data Type TypeCategories Use the following constants with this data type: TypeCategory_BuiltinDataTypes –(Value: 3) Specifies a built-in data type. TypeCategory_CustomDataTypes –(Value: 2) Specifies a custom data type. TypeCategory_None –(Value: 0) Specifies no

### SearchMatch.TypeCategoryOfMatch

#### Syntax

[SearchMatch](searchmatch.html).TypeCategoryOfMatch

#### Data Type

[TypeCategories](typecategories.html)

Use the following constants with this data type:

- TypeCategory_BuiltinDataTypes 
 –(Value: 3) Specifies a built-in data type.
- TypeCategory_CustomDataTypes 
 –(Value: 2) Specifies a custom data type.
- TypeCategory_None 
 –(Value: 0) Specifies no data type.
- TypeCategory_StepTypes 
 –(Value: 1) Specifies a step type.

#### Purpose

Returns the
 [TypeCategories](typecategories.html)
 constant that corresponds to the category of the type in which the match was found. If the match was not found in a type, this property returns
 TypeCategory_None
 .

#### Remarks

This property always returns
 TypeCategory_None
 when you create the search using the
 [PropertyObject.Search](propertyobject-search.html)
 method. The value is valid only when you create the search with the
 [Engine.SearchFiles](engine-searchfiles.html)
 method.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchResults](searchresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-updateforreplace.html language=enus -->
## TOPIC 02388: SearchMatch.UpdateForReplace

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-updateforreplace.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-updateforreplace.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.UpdateForReplace( replacementString) Purpose Updates all the SearchMatch objects a replace operation affects. This method updates all the property paths and match locations of the current and neighboring SearchMatch objects as needed to make them consistent with the replace operat

### SearchMatch.UpdateForReplace

#### Syntax

[SearchMatch](searchmatch.html).UpdateForReplace( replacementString)

#### Purpose

Updates all the SearchMatch objects a replace operation affects. This method updates all the property paths and match locations of the current and neighboring SearchMatch objects as needed to make them consistent with the replace operation the
 replacementString
 parameter specifies.

#### Remarks

This method does not perform the actual replace operation. Use
 [PropertyObject](propertyobject.html)
 objects to edit the file or property before calling this method.

#### Parameters

replacementString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the string with which the matched item was replaced.

#### See Also

[PropertyObject](propertyobject.html)

[SearchResults](searchresults.html)

[TypeCategories](typecategories.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-updateforreplacevalue.html language=enus -->
## TOPIC 02389: SearchMatch.UpdateForReplaceValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-updateforreplacevalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-updateforreplacevalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.UpdateForReplaceValue( newValue) Purpose Updates the value of the property the SearchMatch object references. This method sets the SearchMatch.MatchIsValid property to False for the current and neighboring SearchMatch objects as needed if the location of their match is the value.

### SearchMatch.UpdateForReplaceValue

#### Syntax

[SearchMatch](searchmatch.html).UpdateForReplaceValue( newValue)

#### Purpose

Updates the value of the property the SearchMatch object references. This method sets the
 [SearchMatch.MatchIsValid](searchmatch-matchisvalid.html)
 property to
 False
 for the current and neighboring SearchMatch objects as needed if the location of their match is the value.

#### Remarks

This method does not perform the actual replace operation. Use
 [PropertyObject](propertyobject.html)
 objects to edit the file or property before calling this method.

#### Parameters

newValue
 As
 [String](data-types-for-teststand.html)

[In] Specifies the string with which the value was replaced.

#### See Also

[PropertyObject](propertyobject.html)

[SearchMatch.MatchIsValid](searchmatch-matchisvalid.html)

[SearchResults](searchresults.html)

[TypeCategories](typecategories.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch-userdata.html language=enus -->
## TOPIC 02390: SearchMatch.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchMatch.UserData Data Type Long Purpose Use this property to store any additional data you want to associate with the SearchMatch object. The value of this property is initially 0 . See Also SearchResults

### SearchMatch.UserData

#### Syntax

[SearchMatch](searchmatch.html).UserData

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Use this property to store any additional data you want to associate with the SearchMatch object. The value of this property is initially
 0
 .

#### See Also

[SearchResults](searchresults.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchmatch.html language=enus -->
## TOPIC 02391: SearchMatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchmatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchmatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The SearchResults object return objects of the SearchMatch class. SearchResults objects contain details about a match found as a result of a call to the PropertyObject.Search or Engine.SearchFiles methods. Properties FileDisplayName (Read Only) FileId (Read Only) FilePath (Read Only) MatchedText (Re

### SearchMatch

The
 [SearchResults](searchresults.html)
 object return objects of the SearchMatch class. SearchResults objects contain details about a match found as a result of a call to the
 [PropertyObject.Search](propertyobject-search.html)
 or
 [Engine.SearchFiles](engine-searchfiles.html)
 methods.

#### Properties

| FileDisplayName (Read Only) |
| --- |
| FileId (Read Only) |
| FilePath (Read Only) |
| MatchedText (Read Only) |
| MatchIsValid (Read Only) |
| PropertyValueAsString (Read Only) |
| PropertyValueType (Read Only) |
| TypeCategoryOfMatch (Read Only) |
| UserData |

#### Methods

| GetLocation |
| --- |
| GetPropertyPath |
| UpdateForReplace |
| UpdateForReplaceValue |

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchResults](searchresults.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchoptions.html language=enus -->
## TOPIC 02392: SearchOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the searchOptions parameter of the PropertyObject.Search and Engine.SearchFiles methods. Use the bitwise-OR operator to specify more than one option. SearchOptions_IncludeSubsequenceFiles –(Value: 0x8) If this option is set, TestStand searches a

### SearchOptions

These constants represent the options you can use with the
 searchOptions
 parameter of the
 [PropertyObject.Search](propertyobject-search.html)
 and
 [Engine.SearchFiles](engine-searchfiles.html)
 methods. Use the bitwise-OR operator to specify more than one option.

- SearchOptions_IncludeSubsequenceFiles 
 –(Value: 0x8) If this option is set, TestStand searches all the sequence files the Sequence Call steps specify.
 Note 
 This option applies only to the
 [Engine.SearchFiles](engine-searchfiles.html)
 method.
- SearchOptions_MatchCase 
 –(Value: 0x1) If this option is set, TestStand finds only those instances in which the capitalization matches the text you specify. For example, if
 CHR 
 is the specified text, this option finds
 CHR 
 but not
 Chr 
 .
- SearchOptions_RegExpr 
 –(Value: 0x4) If this option is set, TestStand treats certain characters in the search text as
 regular expression characters 
 instead of literal characters.
- SearchOptions_WholeWordOnly 
 –(Value: 0x2) If this option is set, TestStand searches for occurrences of the specified text only where the text that surrounds the occurrence is a space, punctuation mark, or other character not considered as part of a word. TestStand treats the characters A through Z, a through z, 0 through 9, and the underscore (_) as parts of a word.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

[Regular Expressions](../tsref/regular-expressions.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults-cancel.html language=enus -->
## TOPIC 02393: SearchResults.Cancel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults-cancel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults-cancel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchResults.Cancel( waitForComplete, processWindowsMsgsWhileWaiting) Purpose Cancels a search in progress. Calling this method after the search completes does nothing. Parameters waitForComplete As Boolean [In] Pass True if you want the method to wait until the search finishes canceling bef

### SearchResults.Cancel

#### Syntax

[SearchResults](searchresults.html).Cancel( waitForComplete, processWindowsMsgsWhileWaiting)

#### Purpose

Cancels a search in progress. Calling this method after the search completes does nothing.

#### Parameters

waitForComplete
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want the method to wait until the search finishes canceling before returning. Otherwise, the cancel operation is asynchronous.

processWindowsMsgsWhileWaiting
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want TestStand to process window messages while waiting for the search to complete. TestStand ignores this parameter if you do not pass
 True
 for the
 waitForComplete
 parameter.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults-getmatch.html language=enus -->
## TOPIC 02394: SearchResults.GetMatch

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults-getmatch.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults-getmatch.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchResults.GetMatch( index) Return Value SearchMatch Purpose Returns the SearchMatch object you specify. Remarks You can access the SearchMatch objects even as they accumulate asynchronously by using the SearchResults.NumMatches property to obtain the number of matches and then using this

### SearchResults.GetMatch

#### Syntax

[SearchResults](searchresults.html).GetMatch( index)

#### Return Value

[SearchMatch](searchmatch.html)

#### Purpose

Returns the
 [SearchMatch](searchmatch.html)
 object you specify.

#### Remarks

You can access the SearchMatch objects even as they accumulate asynchronously by using the
 [SearchResults.NumMatches](searchresults-nummatches.html)
 property to obtain the number of matches and then using this method to access only the SearchMatch objects up to that number. TestStand always appends new SearchMatch objects to the end.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the SearchMatch object you want the method to return.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchMatch](searchmatch.html)

[SearchResults.NumMatches](searchresults-nummatches.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults-getwarning.html language=enus -->
## TOPIC 02395: SearchResults.GetWarning

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults-getwarning.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults-getwarning.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchResults.GetWarning( index) Return Value String Purpose Returns the warning message you specify by index. Remarks You can access the warnings even as they accumulate asynchronously by using the SearchResults.NumWarnings property to obtain the number of matches and then using this method

### SearchResults.GetWarning

#### Syntax

[SearchResults](searchresults.html).GetWarning( index)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the warning message you specify by index.

#### Remarks

You can access the warnings even as they accumulate asynchronously by using the
 [SearchResults.NumWarnings](searchresults-numwarnings.html)
 property to obtain the number of matches and then using this method to access only the SearchMatch objects up to that number. TestStand always appends new warnings to the end of the result list.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the SearchMatch object you want the method to return.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchResults.NumWarnings](searchresults-numwarnings.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults-iscomplete.html language=enus -->
## TOPIC 02396: SearchResults.IsComplete

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults-iscomplete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults-iscomplete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchResults.IsComplete( waitForComplete, processWindowsMsgsWhileWaiting) Return Value Boolean Purpose Returns a value that indicates whether a search is complete or waits until the search is complete. Parameters waitForComplete As Boolean [In] Pass True if you want the method to wait until

### SearchResults.IsComplete

#### Syntax

[SearchResults](searchresults.html).IsComplete( waitForComplete, processWindowsMsgsWhileWaiting)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether a search is complete or waits until the search is complete.

#### Parameters

waitForComplete
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want the method to wait until the search is complete before it returns.

processWindowsMsgsWhileWaiting
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want TestStand to process window messages while waiting for the search to complete. TestStand ignores this parameter if you do not pass
 True
 for the
 waitForComplete
 parameter.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults-nummatches.html language=enus -->
## TOPIC 02397: SearchResults.NumMatches

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults-nummatches.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults-nummatches.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchResults.NumMatches Data Type Long Purpose Returns the number of matches found up to a certain point. If the search is not yet complete, this number can continue to increase as TestStand finds new matches. Remarks You can access the SearchMatch objects even as they accumulate asynchronou

### SearchResults.NumMatches

#### Syntax

[SearchResults](searchresults.html).NumMatches

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of matches found up to a certain point. If the search is not yet complete, this number can continue to increase as TestStand finds new matches.

#### Remarks

You can access the SearchMatch objects even as they accumulate asynchronously by using this property to obtain the number of matches and then accessing only the
 [SearchMatch](searchmatch.html)
 objects up to that number using the
 [SearchResults.GetMatch](searchresults-getmatch.html)
 method. TestStand always appends new SearchMatch objects to the end of the result list.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchMatch](searchmatch.html)

[SearchResults.GetMatch](searchresults-getmatch.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults-numwarnings.html language=enus -->
## TOPIC 02398: SearchResults.NumWarnings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults-numwarnings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults-numwarnings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchResults.NumWarnings Data Type Long Purpose Returns the number of warnings. If the search is not yet complete, this number can increase in the future as TestStand adds new warning messages. TestStand adds warning messages when it encounters an error while performing a search. A common er

### SearchResults.NumWarnings

#### Syntax

[SearchResults](searchresults.html).NumWarnings

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of warnings. If the search is not yet complete, this number can increase in the future as TestStand adds new warning messages. TestStand adds warning messages when it encounters an error while performing a search. A common error that can occur is when TestStand cannot load a file because of type conflicts.

#### Remarks

You can access the warnings even as they accumulate asynchronously by using the
 [SearchResults.GetWarning](searchresults-getwarning.html)
 method to obtain the number of warnings and then using this method to access only the SearchMatch objects up to that number. TestStand always appends new warnings to the end of the result list.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchResults.GetWarning](searchresults-getwarning.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults-statusmessage.html language=enus -->
## TOPIC 02399: SearchResults.StatusMessage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults-statusmessage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults-statusmessage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SearchResults.StatusMessage Data Type String Purpose Returns a real-time description of what the search is doing while in progress. The status message describes the file TestStand is currently loading or searching as well as other activities that relate to the search, such as building the lis

### SearchResults.StatusMessage

#### Syntax

[SearchResults](searchresults.html).StatusMessage

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a real-time description of what the search is doing while in progress. The status message describes the file TestStand is currently loading or searching as well as other activities that relate to the search, such as building the list of files to search.

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[PropertyObject.Search](propertyobject-search.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/searchresults.html language=enus -->
## TOPIC 02400: SearchResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/searchresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/searchresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects in the SearchResult class are both a handle to a search in progress and a container for the results of that search. When you call the PropertyObject.Search or Engine.SearchFiles method, TestStand returns a SearchResults object. The search runs asynchronously, which means you obtain the Searc

### SearchResults

Objects in the SearchResult class are both a handle to a search in progress and a container for the results of that search. When you call the
 [PropertyObject.Search](propertyobject-search.html)
 or
 [Engine.SearchFiles](engine-searchfiles.html)
 method, TestStand returns a SearchResults object. The search runs asynchronously, which means you obtain the SearchResults object before the search finishes. To wait for the search to complete, call the
 [SearchResults.IsComplete](searchresults-iscomplete.html)
 method. Alternatively, you can access the results as they accumulate asynchronously by using the
 [SearchResults.NumMatches](searchresults-nummatches.html)
 property to obtain the number of matches and then accessing only the SearchMatch objects up to that number. TestStand always appends new
 [SearchMatch](searchmatch.html)
 objects to the end of the result list.

#### Properties

| NumMatches (Read Only) |
| --- |
| NumWarnings (Read Only) |
| StatusMessage (Read Only) |

#### Methods

| Cancel |
| --- |
| GetMatch |
| GetWarning |
| IsComplete |

#### See Also

[Engine.SearchFiles](engine-searchfiles.html)

[IsComplete](searchresults-iscomplete.html)

[NumMatches](searchresults-nummatches.html)

[PropertyObject.Search](propertyobject-search.html)

[SearchMatch](searchmatch.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/selectedbreakpointitem-isendselected.html language=enus -->
## TOPIC 02401: SelectedBreakpointItem.IsEndSelected

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/selectedbreakpointitem-isendselected.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/selectedbreakpointitem-isendselected.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedBreakpointItem.IsEndSelected Return Value Boolean Returns True if the selected breakpoint is on the End marker. Otherwise, returns False . Purpose Returns a value that indicates whether the selected breakpoint was on the End marker in the sequence. See Also Engine.DisplayEditBreakAndW

### SelectedBreakpointItem.IsEndSelected

#### Syntax

[SelectedBreakpointItem](selectedbreakpointitem.html).IsEndSelected

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the selected breakpoint is on the End marker. Otherwise, returns
 False
 .

#### Purpose

Returns a value that indicates whether the selected breakpoint was on the End marker in the sequence.

#### See Also

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/selectedbreakpointitem-sequencefile.html language=enus -->
## TOPIC 02402: SelectedBreakpointItem.SequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/selectedbreakpointitem-sequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/selectedbreakpointitem-sequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedBreakpointItem.SequenceFile Data Type SequenceFile Purpose Returns the selected sequence file. TestStand returns an empty reference if no item was selected. See Also Engine.DisplayEditBreakAndWatchDialog SequenceFile

### SelectedBreakpointItem.SequenceFile

#### Syntax

[SelectedBreakpointItem](selectedbreakpointitem.html).SequenceFile

#### Data Type

[SequenceFile](sequencefile.html)

#### Purpose

Returns the selected sequence file. TestStand returns an empty reference if no item was selected.

#### See Also

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

[SequenceFile](sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/selectedbreakpointitem-sequencename.html language=enus -->
## TOPIC 02403: SelectedBreakpointItem.SequenceName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/selectedbreakpointitem-sequencename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/selectedbreakpointitem-sequencename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedBreakpointItem.SequenceName Data Type String Purpose Returns the name of the selected sequence. TestStand returns an empty string if only the sequence file of a breakpoint was selected. See Also Engine.DisplayEditBreakAndWatchDialog

### SelectedBreakpointItem.SequenceName

#### Syntax

[SelectedBreakpointItem](selectedbreakpointitem.html).SequenceName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the selected sequence. TestStand returns an empty string if only the sequence file of a breakpoint was selected.

#### See Also

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/selectedbreakpointitem-stepgroup.html language=enus -->
## TOPIC 02404: SelectedBreakpointItem.StepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/selectedbreakpointitem-stepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/selectedbreakpointitem-stepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedBreakpointItem.StepGroup Data Type StepGroups Use the following constants with this data type: StepGroup_Cleanup –(Value: 2) Specifies the Cleanup step group. StepGroup_Main –(Value: 1) Specifies the Main step group. StepGroup_Setup –(Value: 0) Specifies the Setup step group. Purpose

### SelectedBreakpointItem.StepGroup

#### Syntax

[SelectedBreakpointItem](selectedbreakpointitem.html).StepGroup

#### Data Type

[StepGroups](stepgroups.html)

Use the following constants with this data type:

- StepGroup_Cleanup 
 –(Value: 2) Specifies the Cleanup step group.
- StepGroup_Main 
 –(Value: 1) Specifies the Main step group.
- StepGroup_Setup 
 –(Value: 0) Specifies the Setup step group.

#### Purpose

Returns the step group that contains the selected breakpoint. The return value for this parameter is meaningless if only the sequence file or sequence of a breakpoint was selected.

#### See Also

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/selectedbreakpointitem-stepid.html language=enus -->
## TOPIC 02405: SelectedBreakpointItem.StepId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/selectedbreakpointitem-stepid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/selectedbreakpointitem-stepid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SelectedBreakpointItem.StepId Data Type String Purpose Returns the ID of the step that has the selected breakpoint. TestStand returns an empty string if only a sequence file or sequence was selected. See Also Engine.DisplayEditBreakAndWatchDialog

### SelectedBreakpointItem.StepId

#### Syntax

[SelectedBreakpointItem](selectedbreakpointitem.html).StepId

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the ID of the step that has the selected breakpoint. TestStand returns an empty string if only a sequence file or sequence was selected.

#### See Also

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/selectedbreakpointitem.html language=enus -->
## TOPIC 02406: SelectedBreakpointItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/selectedbreakpointitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/selectedbreakpointitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: A SelectedBreakpointItem object specifies a breakpoint in a sequence file. Use this object for the selectedItemParam parameter of the Engine.DisplayEditBreakAndWatchDialog method, which returns the last selected item on the Breakpoints tab of the Edit Breakpoints/Watch Expressions dialog box when th

### SelectedBreakpointItem

A SelectedBreakpointItem object specifies a breakpoint in a sequence file. Use this object for the
 selectedItemParam
 parameter of the
 [Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)
 method, which returns the last selected item on the
 [Breakpoints tab](../tsref/breakpoints-tab-edit-breakpoints-watch-expres.html)
 of the
 [Edit Breakpoints/Watch Expressions](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)
 dialog box when the user clicks the Goto button. The selected item can be a sequence file, sequence, or step.

#### Properties

| SequenceFile (Read Only) |
| --- |
| SequenceName (Read Only) |
| StepGroup (Read Only) |
| StepId (Read Only) |

#### Method

| IsEndSelected |
| --- |

#### See Also

[Breakpoints tab](../tsref/breakpoints-tab-edit-breakpoints-watch-expres.html)

[Edit Breakpoints/Watch Expressions dialog box](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/seqcallmultithreadoptions.html language=enus -->
## TOPIC 02407: SeqCallMultithreadOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/seqcallmultithreadoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/seqcallmultithreadoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SequenceCallModule.MultithreadingAndRemoteExecOption property to call the subsequence in a new execution, a new thread, or on a remote computer when executing the module. SeqCallMultithread_NewExecution –(Value: 2) Specifies to call the subsequence in a new execution. Se

### SeqCallMultithreadOptions

Use these constants with the
 [SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)
 property to call the subsequence in a new execution, a new thread, or on a remote computer when executing the module.

- SeqCallMultithread_NewExecution 
 –(Value: 2) Specifies to call the subsequence in a new execution.
- SeqCallMultithread_NewThread 
 –(Value: 1) Specifies to call the subsequence in a new thread.
- SeqCallMultithread_None 
 –(Value: 0) Specifies to call the subsequence in the current thread and execution on the current computer.
- SeqCallMultithread_Remote 
 –(Value: 0x100) Specifies to call the subsequence on a remote computer.

#### See Also

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/seqcallnewexecmodeloptions.html language=enus -->
## TOPIC 02408: SeqCallNewExecModelOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/seqcallnewexecmodeloptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/seqcallnewexecmodeloptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SequenceCallModule.NewExecutionModelOption property to specify which process model the new execution uses. SeqCallNewExecModel_None –(Value: 0) The new execution does not run under a process model. SeqCallNewExecModel_SpecifyModel –(Value: 2) When you set this option, yo

### SeqCallNewExecModelOptions

Use these constants with the
 [SequenceCallModule.NewExecutionModelOption](sequencecallmodule-newexecutionmodeloption.html)
 property to specify which process model the new execution uses.

- SeqCallNewExecModel_None 
 –(Value: 0) The new execution does not run under a process model.
- SeqCallNewExecModel_SpecifyModel 
 –(Value: 2) When you set this option, you can use the
 SequenceCallModule.NewExecutionModelPath 
 property to specify the process model under which the new execution runs. You can also use the
 SequenceCallModule.SequenceName 
 property to specify which entry point to call in the process model. Typically, the Process Model entry point calls the
 MainSequence 
 in the client sequence file you specify.
- SeqCallNewExecModel_UseModelOfCurrentFile 
 –(Value: 1) When you set this option, the execution runs under the model the sequence file you call specifies. If the file you call does not specify a model, the execution runs under the default station model. You can use the
 SequenceCallModule.SequenceName 
 property to designate which entry point to call in the process model. Typically, the Process Model entry point calls the
 MainSequence 
 in the client sequence file you specify.

#### See Also

[SequenceCallModule.NewExecutionModelOption](sequencecallmodule-newexecutionmodeloption.html)

[SequenceCallModule.NewExecutionModelPath](sequencecallmodule-newexecutionmodelpath.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/seqcallnewthreadoptions.html language=enus -->
## TOPIC 02409: SeqCallNewThreadOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/seqcallnewthreadoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/seqcallnewthreadoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the SequenceCallModule.NewThreadOptions property to specify the options to apply when calling a subsequence in a separate thread. Use the bitwise-AND operator to determine whether any of these options are set when obtaining the property value. Use the bitwise-OR oper

### SeqCallNewThreadOptions

Use the following constants with the
 [SequenceCallModule.NewThreadOptions](sequencecallmodule-newthreadoptions.html)
 property to specify the options to apply when calling a subsequence in a separate thread. Use the bitwise-AND operator to determine whether any of these options are set when obtaining the property value. Use the bitwise-OR operator to set more than one option when setting the property value.

- SeqCallThread_InitiallySuspended 
 –(Value: 0x2) Specifies that TestStand creates the new thread in a suspended state. You can call the
 Thread.Resume 
 method to start the thread.
- SeqCallThread_UseSingleThreadedApartment 
 –(Value: 0x4) Specifies to initialize the concurrency model of the thread as single-threaded apartment. By default, TestStand initializes new executions and threads to use the multithreaded apartment model. A thread must use the single-threaded apartment model if the thread creates or launches a dialog box that contains ActiveX controls.
- SeqCallThread_WaitForThreadCompletion 
 –(Value: 0x1) Specifies that the calling sequence waits for the thread it launches to complete before the calling sequence returns.

#### See Also

[SequenceCallModule.NewThreadOptions](sequencecallmodule-newthreadoptions.html)

[Thread.Resume](thread-resume.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/seqcalltracesettings.html language=enus -->
## TOPIC 02410: SeqCallTraceSettings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/seqcalltracesettings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/seqcalltracesettings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SequenceCallModule.TraceSetting property to control tracing calls to the specified subsequence of the module. SeqCallTrace_Disable –(Value: 3) Specifies to disable tracing for calls to the subsequence and restores the original tracing state when the subsequence returns.

### SeqCallTraceSettings

Use these constants with the
 [SequenceCallModule.TraceSetting](sequencecallmodule-tracesetting.html)
 property to control tracing calls to the specified subsequence of the module.

- SeqCallTrace_Disable 
 –(Value: 3) Specifies to disable tracing for calls to the subsequence and restores the original tracing state when the subsequence returns. However, if you enable the Allow Tracing into Sequence Calls Marked with Tracing "Disabled" option on the
 Execution tab 
 of the
 Station Options 
 dialog box, TestStand ignores this setting and does not alter the tracing state.
- SeqCallTrace_Enable 
 –(Value: 2) Specifies to enable tracing for calls to the subsequence and restores the original tracing state when the subsequence returns.
- SeqCallTrace_UseCurrent 
 –(Value: 1) Specifies to maintain the current tracing state when calling the subsequence. This is the default value for the
 SequenceCallModule.TraceSetting 
 property. Usually, only process model files use other values for this option.
- SeqCallTrace_UseExecutionSetting 
 –(Value: 4) Specifies to enable the tracing state unless the execution was created with tracing disabled. Typically, a process model uses this setting to control the tracing state when the model calls the
 MainSequence 
 in the client sequence file.

#### See Also

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[SequenceCallModule.TraceSetting](sequencecallmodule-tracesetting.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/seqcallwaitforexecoptions.html language=enus -->
## TOPIC 02411: SeqCallWaitForExecOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/seqcallwaitforexecoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/seqcallwaitforexecoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the SequenceCallModule.NewExecutionWaitForCompletion property to specify whether to wait for the execution to complete. SeqCallWait_BeforeNextStep –(Value: 1) The calling sequence waits for the execution to complete before it executes another step. SeqCallWait_DoNotWait –(Va

### SeqCallWaitForExecOptions

Use these constants with the
 [SequenceCallModule.NewExecutionWaitForCompletion](sequencecallmodule-newexecutionwaitforcomplet.html)
 property to specify whether to wait for the execution to complete.

- SeqCallWait_BeforeNextStep 
 –(Value: 1) The calling sequence waits for the execution to complete before it executes another step.
- SeqCallWait_DoNotWait 
 –(Value: 0) The calling sequence does not wait for the execution to complete.
- SeqCallWait_EndOfSequence 
 –(Value: 2) The calling sequence waits for the execution to complete before the calling sequence returns.

#### See Also

[SequenceCallModule.NewExecutionWaitForCompletion](sequencecallmodule-newexecutionwaitforcomplet.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/seqfilebatchsynchronizationoptions.html language=enus -->
## TOPIC 02412: SeqFileBatchSynchronizationOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/seqfilebatchsynchronizationoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/seqfilebatchsynchronizationoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This data type contains values that specify the type of batch synchronization. The constants represent the possible values for the SequenceFile.BatchSyncOption property. SeqFileBatchSyncOption_NoSync –(Value: 2) Batch synchronization is not used on this step. SeqFileBatchSyncOption_OneThreadOnly –(V

### SeqFileBatchSynchronizationOptions

This data type contains values that specify the type of batch synchronization. The constants represent the possible values for the
 [SequenceFile.BatchSyncOption](sequencefile-batchsyncoption.html)
 property.

- SeqFileBatchSyncOption_NoSync 
 –(Value: 2) Batch synchronization is not used on this step.
- SeqFileBatchSyncOption_OneThreadOnly 
 –(Value: 5) Use a One Thread Only section to specify that only one thread in the batch executes the step in the section. Typically, you use this type of section to perform an operation that applies to the batch as a whole, such as raising the temperature in a test chamber. When all threads in a batch arrive at their respective instances of an Enter step for a One Thread Only section, TestStand releases only the thread with the lowest Order Number. When that thread arrives at Exit step for the section, all remaining threads in the batch jump from the Enter step to the Exit step, skipping the steps within the section. The threads in the batch then exit the section together.
- SeqFileBatchSyncOption_Parallel 
 –(Value: 4) When all threads in a batch arrive at their respective instances of an Enter step for a Parallel section, TestStand releases all the threads at once. Each thread waits at the Exit step for the section until all threads in the batch reach that step.
- SeqFileBatchSyncOption_Serial 
 –(Value: 3) Use a Serial section to ensure that each thread in the batch executes the steps in the section sequentially and in the order you specify when you create the batch. When all threads in a batch arrive at their respective instances of an Enter step for a Serial section, TestStand releases one thread at a time in ascending order according to the order number you assign to the threads when you add them to the batch using the Batch Specification step. As each thread reaches the Exit step for the section, the next thread in the batch proceeds from the Enter step. After all the threads in the batch arrive at the Exit step, they exit the section together.
- SeqFileBatchSyncOption_UseModelSetting 
 –(Value: 1) Uses the same option the model uses.

#### See Also

[SequenceFile.BatchSyncOption](sequencefile-batchsyncoption.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/seqfilecallbacks.html language=enus -->
## TOPIC 02413: SeqFileCallbacks

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/seqfilecallbacks.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/seqfilecallbacks.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these string constants to specify the callbackName parameter of the SequenceFile.CreateCallbackOverrideSequence method. SeqFileCback_Load –(Value: "SequenceFileLoad") SeqFileCback_PostInteractive –(Value: "SequenceFilePostInteractive") SeqFileCback_PostResultListEntry –(Value: "SequenceFilePostR

### SeqFileCallbacks

Use these string constants to specify the
 callbackName
 parameter of the
 [SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)
 method.

- SeqFileCback_Load 
 –(Value: "SequenceFileLoad")
- SeqFileCback_PostInteractive 
 –(Value: "SequenceFilePostInteractive")
- SeqFileCback_PostResultListEntry 
 –(Value: "SequenceFilePostResultListEntry")
- SeqFileCback_PostResults 
 –(Value: "SequenceFilePostResults")
- SeqFileCback_PostStep 
 –(Value: "SequenceFilePostStep")
- SeqFileCback_PostStepFailure 
 –(Value: "SequenceFilePostStepFailure")
- SeqFileCback_PostStepRuntimeError 
 –(Value: "SequenceFilePostStepRuntimeError")
- SeqFileCback_PreInteractive 
 –(Value: "SequenceFilePreInteractive")
- SeqFileCback_PreStep 
 –(Value: "SequenceFilePreStep")
- SeqFileCback_Unload 
 –(Value: "SequenceFileUnload")

#### See Also

[DefaultModelCallbacks](defaultmodelcallbacks.html)

[FrontEndCallbacks](frontendcallbacks.html)

[SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-allowinteractiveexecutionofentrypoin.html language=enus -->
## TOPIC 02414: Sequence.AllowInteractiveExecutionOfEntryPoint

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-allowinteractiveexecutionofentrypoin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-allowinteractiveexecutionofentrypoin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.AllowInteractiveExecutionOfEntryPoint Data Type Boolean Purpose Set this property to False to prohibit the user from using this entry point sequence to run an interactive execution in the sequence editor or user interface. Remarks This property applies only to an entry point sequence

### Sequence.AllowInteractiveExecutionOfEntryPoint

#### Syntax

[Sequence](sequence.html).AllowInteractiveExecutionOfEntryPoint

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 False
 to prohibit the user from using this entry point sequence to run an interactive execution in the sequence editor or user interface.

#### Remarks

This property applies only to an entry point sequence in a process model file.

#### See Also

[Sequence.Type](sequence-type.html)

[SequenceFile.SequenceFileType](sequencefile-sequencefiletype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-aspropertyobject.html language=enus -->
## TOPIC 02415: Sequence.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the Sequence object. Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### Sequence.AsPropertyObject

#### Syntax

[Sequence](sequence.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the Sequence object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-copystepsonoverride.html language=enus -->
## TOPIC 02416: Sequence.CopyStepsOnOverride

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-copystepsonoverride.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-copystepsonoverride.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.CopyStepsOnOverride Data Type Boolean Purpose Specifies the behavior of TestStand when you click Add in the Sequence File Callbacks dialog box to create an overriding sequence file in the client sequence file. Remarks If you set this property to True , TestStand copies all steps and

### Sequence.CopyStepsOnOverride

#### Syntax

[Sequence](sequence.html).CopyStepsOnOverride

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies the behavior of TestStand when you click
 Add
 in the
 [Sequence File Callbacks](../tsref/select-sequence-file-callbacks-dialog-box.html)
 dialog box to create an overriding sequence file in the client sequence file.

#### Remarks

If you set this property to
 True
 , TestStand copies all steps and local variables in the callback sequence of the model file to the callback sequence you create in the client sequence file.

Note

This property applies only to callback sequences that reside in a model sequence file.

#### See Also

[Engine.DisplaySequenceFileCallbacksDialog](engine-displaysequencefilecallbacksdialog.html)

[Sequence File Callbacks dialog box](../tsref/select-sequence-file-callbacks-dialog-box.html)

[Sequence.Type](sequence-type.html)

[SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-createnewuniquestepids.html language=enus -->
## TOPIC 02417: Sequence.CreateNewUniqueStepIds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-createnewuniquestepids.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-createnewuniquestepids.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.CreateNewUniqueStepIds Purpose Replaces the unique step ID with a new unique step ID in all the steps in a sequence. See Also Step.CreateNewUniqueStepId Step.UniqueStepId

### Sequence.CreateNewUniqueStepIds

#### Syntax

[Sequence](sequence.html).CreateNewUniqueStepIds

#### Purpose

Replaces the unique step ID with a new unique step ID in all the steps in a sequence.

#### See Also

[Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)

[Step.UniqueStepId](step-uniquestepid.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-deletestep.html language=enus -->
## TOPIC 02418: Sequence.DeleteStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-deletestep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-deletestep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.DeleteStep( index, stepGroupParam) Purpose Deletes a step from the sequence. Parameters index As Long [In] Specifies the zero-based step index that indicates the position of the step in the step group. stepGroupParam As StepGroups [In] Specifies the step group that contains the step

### Sequence.DeleteStep

#### Syntax

[Sequence](sequence.html).DeleteStep( index, stepGroupParam)

#### Purpose

Deletes a step from the sequence.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based step index that indicates the position of the step in the step group.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies the step group that contains the step you want to delete.

#### See Also

[Sequence.InsertStep](sequence-insertstep.html)

[Sequence.RemoveStep](sequence-removestep.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-disableresults.html language=enus -->
## TOPIC 02419: Sequence.DisableResults

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-disableresults.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-disableresults.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.DisableResults Data Type Boolean Purpose Specifies to disable result recording for any steps in the sequence. Remarks If this property is True , TestStand does not record results for any steps in the sequence. If this property is False , TestStand records results based on the setting

### Sequence.DisableResults

#### Syntax

[Sequence](sequence.html).DisableResults

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to disable result recording for any steps in the sequence.

#### Remarks

If this property is
 True
 , TestStand does not record results for any steps in the sequence. If this property is
 False
 , TestStand records results based on the setting of the
 [Step.ResultRecordingOption](step-resultrecordingoption.html)
 property of each individual step or the
 [StationOptions.DisableResults](stationoptions-disableresults.html)
 and
 [Execution.DisableResults](execution-disableresults.html)
 properties.

Note

#### See Also

[Execution.DisableResults](execution-disableresults.html)

[StationOptions.DisableResults](stationoptions-disableresults.html)

[Step.ResultRecordingOption](step-resultrecordingoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-entrypointchecktosavetitledseqfiles.html language=enus -->
## TOPIC 02420: Sequence.EntryPointCheckToSaveTitledSeqFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-entrypointchecktosavetitledseqfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-entrypointchecktosavetitledseqfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EntryPointCheckToSaveTitledSeqFiles Data Type Boolean Purpose Specifies if sequence files must be saved before the entry point executes. Remarks This property applies only to an entry point sequence in a process model file. The property indicates if the sequence editor must attempt t

### Sequence.EntryPointCheckToSaveTitledSeqFiles

#### Syntax

[Sequence](sequence.html).EntryPointCheckToSaveTitledSeqFiles

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if sequence files must be saved before the entry point executes.

#### Remarks

This property applies only to an entry point sequence in a process model file. The property indicates if the sequence editor must attempt to save modified sequence files before executing the entry point.

#### See Also

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-entrypointenabledexpression.html language=enus -->
## TOPIC 02421: Sequence.EntryPointEnabledExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-entrypointenabledexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-entrypointenabledexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EntryPointEnabledExpression Data Type String Purpose Specifies a Boolean expression the Sequence.EvalEntryPointEnabledExpressionEx method evaluates. Remarks If the expression evaluates to False , TestStand dims the entry point in the menu. If the expression is empty, the entry point

### Sequence.EntryPointEnabledExpression

#### Syntax

[Sequence](sequence.html).EntryPointEnabledExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a Boolean expression the
 [Sequence.EvalEntryPointEnabledExpressionEx](sequence-evalentrypointenabledexpressionex.html)
 method evaluates.

#### Remarks

If the expression evaluates to
 False
 , TestStand dims the entry point in the menu. If the expression is empty, the entry point is enabled in the menu.

#### See Also

[Sequence.EntryPointNameExpression](sequence-entrypointnameexpression.html)

[Sequence.EntryPointMenuHint](sequence-entrypointmenuhint.html)

[Sequence.EvalEntryPointEnabledExpressionEx](sequence-evalentrypointenabledexpressionex.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-entrypointignoreclient.html language=enus -->
## TOPIC 02422: Sequence.EntryPointIgnoreClient

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-entrypointignoreclient.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-entrypointignoreclient.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EntryPointIgnoreClient Data Type Boolean Purpose Specifies if the entry point ignores the client sequence file. Remarks This property applies only to an entry point sequence in a process model file. Set this property to True for entry points wholly contained in the process model and

### Sequence.EntryPointIgnoreClient

#### Syntax

[Sequence](sequence.html).EntryPointIgnoreClient

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the entry point ignores the client sequence file.

#### Remarks

This property applies only to an entry point sequence in a process model file. Set this property to
 True
 for entry points wholly contained in the process model and do not call into the client sequence file. User interfaces and the sequence editor use this option to determine whether to pass a client sequence file to the
 [Engine.NewExecution](engine-newexecution.html)
 method when they execute this entry point.

#### See Also

[Engine.NewExecution](engine-newexecution.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-entrypointinitiallyhidden.html language=enus -->
## TOPIC 02423: Sequence.EntryPointInitiallyHidden

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-entrypointinitiallyhidden.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-entrypointinitiallyhidden.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EntryPointInitiallyHidden Data Type Boolean Purpose Specifies if an execution of the entry point is hidden when it starts. Remarks This property applies only to an entry point sequence in a process model file. The property indicates if an execution of the entry point is hidden when i

### Sequence.EntryPointInitiallyHidden

#### Syntax

[Sequence](sequence.html).EntryPointInitiallyHidden

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if an execution of the entry point is hidden when it starts.

#### Remarks

This property applies only to an entry point sequence in a process model file. The property indicates if an execution of the entry point is hidden when it starts. In other words, if the property is
 True
 , the user interface does not display an Execution window for the entry point sequence when it begins executing it. The user interface does this by assigning the
 ExecTypeMask_InitiallyHidden
 value to the TypeMask property of the execution.

#### See Also

[Execution.TypeMask](execution-typemask.html)

[ExecutionTypeMask](executiontypemask.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-entrypointmenuhint.html language=enus -->
## TOPIC 02424: Sequence.EntryPointMenuHint

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-entrypointmenuhint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-entrypointmenuhint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EntryPointMenuHint Data Type String Purpose Specifies a menu name for the entry point. You can specify multiple menu names separated by commas. An empty string value specifies that the application determines the menu the entry point appears in based on the entry point sequence type.

### Sequence.EntryPointMenuHint

#### Syntax

[Sequence](sequence.html).EntryPointMenuHint

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a menu name for the entry point. You can specify multiple menu names separated by commas. An empty string value specifies that the application determines the menu the entry point appears in based on the entry point sequence type.

#### Remarks

Note

An application uses the first menu name in the list that it can find in the user interface. This option is useful if you use multiple user interfaces that have different menu names. If an application cannot find any menus in the user interface with the names that you specify, the application uses the default menu for the entry point type.

#### See Also

[Sequence.EntryPointEnabledExpression](sequence-entrypointenabledexpression.html)

[Sequence.EntryPointNameExpression](sequence-entrypointnameexpression.html)

[Sequence.GetEntryPointMenuFromHint](sequence-getentrypointmenufromhint.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-entrypointnameexpression.html language=enus -->
## TOPIC 02425: Sequence.EntryPointNameExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-entrypointnameexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-entrypointnameexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EntryPointNameExpression Data Type String Purpose Specifies a string expression that determines the menu item name of the entry point. Remarks This property applies only to an entry point sequence in a process model. See Also Sequence.EntryPointEnabledExpression Sequence.EntryPointMe

### Sequence.EntryPointNameExpression

#### Syntax

[Sequence](sequence.html).EntryPointNameExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies a string expression that determines the menu item name of the entry point.

#### Remarks

Note

#### See Also

[Sequence.EntryPointEnabledExpression](sequence-entrypointenabledexpression.html)

[Sequence.EntryPointMenuHint](sequence-entrypointmenuhint.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-evalentrypointenabledexpression.html language=enus -->
## TOPIC 02426: Sequence.EvalEntryPointEnabledExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-evalentrypointenabledexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-evalentrypointenabledexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EvalEntryPointEnabledExpression( sequenceFileParam) Return Value Boolean Returns True if the entry point is enabled in the user interface menu bar. Purpose This method is obsolete. Use the Sequence.EvalEntryPointEnabledExpressionEx method instead. Remarks Applies only to an entry poi

### Sequence.EvalEntryPointEnabledExpression

#### Syntax

[Sequence](sequence.html).EvalEntryPointEnabledExpression( sequenceFileParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the entry point is enabled in the user interface menu bar.

#### Purpose

Note

Sequence.EvalEntryPointEnabledExpressionEx

#### Remarks

Applies only to an entry point sequence in a process model file. Call this function to determine whether to enable the entry point in the user interface menu bar. The function evaluates the entry point-enabled expression for the entry point sequence in the context of the currently selected sequence file in the user interface.

#### Parameters

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the currently selected sequence file in the user interface.

#### See Also

[Sequence.EvalEntryPointEnabledExpressionEx](sequence-evalentrypointenabledexpressionex.html)

[SequenceFile](sequencefile.html)

Parent topic:

Obsolete Sequence Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-evalentrypointenabledexpressionex.html language=enus -->
## TOPIC 02427: Sequence.EvalEntryPointEnabledExpressionEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-evalentrypointenabledexpressionex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-evalentrypointenabledexpressionex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EvalEntryPointEnabledExpressionEx( editArgs) Return Value Boolean Returns True if you can enable the entry point in the user interface menu bar. Purpose Evaluates the entry point enabled expression. Remarks This method applies only to an entry point sequence in a process model file.

### Sequence.EvalEntryPointEnabledExpressionEx

#### Syntax

[Sequence](sequence.html).EvalEntryPointEnabledExpressionEx( editArgs)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you can enable the entry point in the user interface menu bar.

#### Purpose

Evaluates the entry point enabled expression.

#### Remarks

This method applies only to an entry point sequence in a process model file. Call this function to determine whether to enable the entry point in the user interface menu bar. The function evaluates the entry point enabled expression for the entry point sequence in the context of the
 editArgs
 parameter, which specifies the currently selected items in the sequence editor or user interface.

#### Parameters

editArgs
 As
 [EditArgs](editargs.html)

[In] Specifies which items in the user interface are currently selected.

#### See Also

[EditArgs](editargs.html)

[Sequence.EntryPointEnabledExpression](sequence-entrypointenabledexpression.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-evalentrypointnameexpression.html language=enus -->
## TOPIC 02428: Sequence.EvalEntryPointNameExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-evalentrypointnameexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-evalentrypointnameexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EvalEntryPointNameExpression( sequenceFileParam) Return Value String Returns the name of the entry point. Purpose This method is obsolete. Use the Sequence.EvalEntryPointNameExpressionEx method instead. Remarks Applies only to an entry point sequence in a process model file. Call thi

### Sequence.EvalEntryPointNameExpression

#### Syntax

[Sequence](sequence.html).EvalEntryPointNameExpression( sequenceFileParam)

#### Return Value

[String](data-types-for-teststand.html)

Returns the name of the entry point.

#### Purpose

Note

Sequence.EvalEntryPointNameExpressionEx

#### Remarks

Applies only to an entry point sequence in a process model file. Call this function to determine the name to display for the entry point in the user interface menu bar. The function evaluates the entry point name expression for the entry point sequence in the context of the currently selected sequence file in the user interface.

#### Parameters

sequenceFileParam
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the currently selected sequence file in the user interface.

#### See Also

[Sequence.EvalEntryPointNameExpressionEx](sequence-evalentrypointnameexpressionex.html)

[SequenceFile](sequencefile.html)

Parent topic:

Obsolete Sequence Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-evalentrypointnameexpressionex.html language=enus -->
## TOPIC 02429: Sequence.EvalEntryPointNameExpressionEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-evalentrypointnameexpressionex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-evalentrypointnameexpressionex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.EvalEntryPointNameExpressionEx( editArgs) Return Value String Returns the name of the entry point. Purpose Evaluates the entry point name expression. Remarks This method applies only to an entry point sequence in a process model file. Call this function to determine the name to displ

### Sequence.EvalEntryPointNameExpressionEx

#### Syntax

[Sequence](sequence.html).EvalEntryPointNameExpressionEx( editArgs)

#### Return Value

[String](data-types-for-teststand.html)

Returns the name of the entry point.

#### Purpose

Evaluates the entry point name expression.

#### Remarks

This method applies only to an entry point sequence in a process model file. Call this function to determine the name to display for the entry point in the user interface menu bar. The function evaluates the entry point name expression for the entry point sequence in the context of the
 editArgs
 parameter, which specifies the currently selected items in the sequence editor or user interface.

#### Parameters

editArgs
 As
 [EditArgs](editargs.html)

[In] Specifies which items in the user interface are currently selected.

#### See Also

[EditArgs](editargs.html)

[Sequence.EntryPointNameExpression](sequence-entrypointnameexpression.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-failureaction.html language=enus -->
## TOPIC 02430: Sequence.FailureAction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-failureaction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-failureaction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.FailureAction Data Type FailureActions Use the following constants with this data type: FailureAction_GotoCleanup –(Value: 1) Specifies that execution flow proceeds to the Cleanup step group if the step sets the status property of the sequence to Failed . FailureAction_None –(Value:

### Sequence.FailureAction

#### Syntax

[Sequence](sequence.html).FailureAction

#### Data Type

[FailureActions](failureactions.html)

Use the following constants with this data type:

- FailureAction_GotoCleanup 
 –(Value: 1) Specifies that execution flow proceeds to the Cleanup step group if the step sets the status property of the sequence to
 Failed 
 .
- FailureAction_None 
 –(Value: 0) Specifies that execution flow does not proceed to the Cleanup step group if the step sets the status property of the sequence to
 Failed 
 .
- FailureAction_UseStationOption 
 –(Value: 2) Specifies that execution flow proceeds to the Cleanup step group if the step sets the status property of the sequence to
 Failed 
 and the value of the
 StationOptions.AlwaysGotoCleanupOnFailure 
 property is
 True 
 .

#### Purpose

Specifies whether execution flow jumps to the Cleanup step group when a step sets the status property of the sequence to
 Failed
 .

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getbreakonend.html language=enus -->
## TOPIC 02431: Sequence.GetBreakOnEnd

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getbreakonend.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getbreakonend.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetBreakOnEnd( stepGroupParam, [executionParam]) Return Value Boolean Purpose This method is obsolete. Use the Sequence.GetBreakOnEndSettings method instead. Remarks Returns True if the step group of the sequence is set to break when all the steps in the step group are done executing

### Sequence.GetBreakOnEnd

#### Syntax

[Sequence](sequence.html).GetBreakOnEnd( stepGroupParam, [executionParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Sequence.GetBreakOnEndSettings

#### Remarks

Returns
 True
 if the step group of the sequence is set to break when all the steps in the step group are done executing.

This method, along with the
 Sequence.SetBreakOnEnd
 method, implements breakpoints for breaking after the last step in a step group.

Note

Sequence.SetBreakOnEnd

Sequence.SetBreakOnEndSettings

#### Parameters

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Pass a reference to an Execution object to obtain the breakpoint settings on the End step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method returns the breakpoint setting on the End step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence.GetBreakOnEndSettings](sequence-getbreakonendsettings.html)

[Sequence.SetBreakOnEndSettings](sequence-setbreakonendsettings.html)

[Step.GetBreakSettings](step-getbreaksettings.html)

[StepGroups](stepgroups.html)

Parent topic:

Obsolete Sequence Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getbreakonendsettings.html language=enus -->
## TOPIC 02432: Sequence.GetBreakOnEndSettings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getbreakonendsettings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getbreakonendsettings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetBreakOnEndSettings( stepGroupParam, isSet, enabled, passCount, Condition, [executionParam]) Purpose Returns a value that indicates whether the step group of the sequence is set to break when all the steps in the sequence execute. Parameters stepGroupParam As StepGroups [In] Specif

### Sequence.GetBreakOnEndSettings

#### Syntax

[Sequence](sequence.html).GetBreakOnEndSettings( stepGroupParam, isSet, enabled, passCount, Condition, [executionParam])

#### Purpose

Returns a value that indicates whether the step group of the sequence is set to break when all the steps in the sequence execute.

#### Parameters

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

isSet
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the breakpoint is set.

enabled
 As
 [Boolean](data-types-for-teststand.html)

[Out] Returns a value that indicates whether the breakpoint is enabled. TestStand ignores disabled breakpoints during execution.

passCount
 As
 [Long](data-types-for-teststand.html)

[Out] Returns the number of times the execution must evaluate the condition expression before suspending the execution. Pass
 0
 if you do not want to use a conditional pass count.

Condition
 As
 [String](data-types-for-teststand.html)

[Out] Returns the expression that must evaluate to
 True
 before suspending the execution. An empty value defaults to
 True
 . If you specify a non-zero value for the
 passCount
 parameter and a condition expression for the breakpoint, the pass count decrements only when the expression evaluates to
 True
 .

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Pass a reference to an Execution object to obtain the breakpoint settings on the End step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method returns the breakpoint setting on the End step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence.SetBreakOnEndSettings](sequence-setbreakonendsettings.html)

[Step.GetBreakSettings](step-getbreaksettings.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-geteffectivetype.html language=enus -->
## TOPIC 02433: Sequence.GetEffectiveType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-geteffectivetype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-geteffectivetype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetEffectiveType Return Value SequenceTypes Use the following constants with this data type: SeqType_Callback –(Value: 1) The sequence is a Process Model callback. SeqType_CfgEntryPoint –(Value: 5) The sequence is a Configuration entry point. SeqType_ExeEntryPoint –(Value: 3) The seq

### Sequence.GetEffectiveType

#### Syntax

[Sequence](sequence.html).GetEffectiveType

#### Return Value

[SequenceTypes](sequencetypes.html)

Use the following constants with this data type:

- SeqType_Callback 
 –(Value: 1) The sequence is a Process Model callback.
- SeqType_CfgEntryPoint 
 –(Value: 5) The sequence is a Configuration entry point.
- SeqType_ExeEntryPoint 
 –(Value: 3) The sequence is an Execution entry point.
- SeqType_Normal 
 –(Value: 0) The sequence is not a callback or an entry point.
- SeqType_ReservedCallback 
 –(Value: 7) Only the
 Sequence.GetEffectiveType 
 method returns this value. The sequence is one of the predefined callbacks TestStand reserves.

#### Purpose

Returns the effective sequence type.

#### Remarks

Typically, the effective sequence type is the same as the value of the
 [Sequence.Type](sequence-type.html)
 property. One exception occurs when this sequence belongs to a sequence file that has a model file, and that model file has a callback with the same name as this sequence. In this case, the effective type is
 [SeqType_Callback](sequencetypes.html)
 . The other exception occurs when this sequence has a reserved name, in which case this method returns
 [SeqType_ReservedCallback](sequencetypes.html)
 .

#### See Also

[Sequence.GetEffectiveType](sequence-geteffectivetype.html)

[Sequence.Type](sequence-type.html)

[SequenceTypes](sequencetypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getentrypointmenufromhint.html language=enus -->
## TOPIC 02434: Sequence.GetEntryPointMenuFromHint

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getentrypointmenufromhint.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getentrypointmenufromhint.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetEntryPointMenuFromHint( menuNameList) Return Value Long Returns a zero-based index into the list of menu names you pass as the menuNameList parameter. This index indicates the menu to which the entry point belongs in the menu. If none of the menus in the list matches a menu hint f

### Sequence.GetEntryPointMenuFromHint

#### Syntax

[Sequence](sequence.html).GetEntryPointMenuFromHint( menuNameList)

#### Return Value

[Long](data-types-for-teststand.html)

Returns a zero-based index into the list of menu names you pass as the
 menuNameList
 parameter. This index indicates the menu to which the entry point belongs in the menu. If none of the menus in the list matches a menu hint for the entry point, the method returns
 -1
 . If this occurs, you must choose the menu in which to display the entry point. You can choose the menu based on the type of entry point.

#### Purpose

This method applies only to an entry point sequence in a process model file. Call this function to determine the user interface menu in which the entry point belongs. The method uses the Menu Hints option for the entry point sequence.

#### Parameters

menuNameList
 As
 [String](data-types-for-teststand.html)

[In] Pass a comma-separated list of the menu names in the user interface, such as "
 File,Configure,Debug
 ".

Note

_

&

#### See Also

[Sequence.EntryPointMenuHint](sequence-entrypointmenuhint.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getnumsteps.html language=enus -->
## TOPIC 02435: Sequence.GetNumSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getnumsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getnumsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetNumSteps( stepGroupParam) Return Value Long Purpose Returns the number of steps in the specified step group of the sequence. Parameters stepGroupParam As StepGroups [In] Specifies a particular step group. See Also Sequence.GetStep Sequence.GetStepByName Sequence.GetStepByUniqueId

### Sequence.GetNumSteps

#### Syntax

[Sequence](sequence.html).GetNumSteps( stepGroupParam)

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of steps in the specified step group of the sequence.

#### Parameters

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

#### See Also

[Sequence.GetStep](sequence-getstep.html)

[Sequence.GetStepByName](sequence-getstepbyname.html)

[Sequence.GetStepByUniqueId](sequence-getstepbyuniqueid.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getstep.html language=enus -->
## TOPIC 02436: Sequence.GetStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetStep( index, stepGroupParam) Return Value Step Purpose Returns a reference to the Step object that you specify by an index. Parameters index As Long [In] Specifies the zero-based step index that indicates the position of the step in the step group. stepGroupParam As StepGroups [In

### Sequence.GetStep

#### Syntax

[Sequence](sequence.html).GetStep( index, stepGroupParam)

#### Return Value

[Step](step.html)

#### Purpose

Returns a reference to the Step object that you specify by an index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based step index that indicates the position of the step in the step group.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

#### See Also

[Sequence.GetStepByName](sequence-getstepbyname.html)

[Sequence.GetStepByUniqueId](sequence-getstepbyuniqueid.html)

[Step](step.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getstepbyname.html language=enus -->
## TOPIC 02437: Sequence.GetStepByName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getstepbyname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getstepbyname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetStepByName( nameOfStep, stepGroupParam) Return Value Step Purpose Returns a reference to the Step object you specify by name. Remarks Returns an error if no Step object exists with the name you specify. Parameters nameOfStep As String [In] Specifies the name of the step for which

### Sequence.GetStepByName

#### Syntax

[Sequence](sequence.html).GetStepByName( nameOfStep, stepGroupParam)

#### Return Value

[Step](step.html)

#### Purpose

Returns a reference to the Step object you specify by name.

#### Remarks

Returns an error if no Step object exists with the name you specify.

#### Parameters

nameOfStep
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the step for which you want a reference. When more than one step using the same name exists in the step group, the method returns the first step with that name. Name comparison is case-insensitive.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

#### See Also

[Sequence.GetStep](sequence-getstep.html)

[Sequence.GetStepByUniqueId](sequence-getstepbyuniqueid.html)

[Sequence.GetStepIndex](sequence-getstepindex.html)

[Sequence.StepNameExists](sequence-stepnameexists.html)

[Step](step.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getstepbyuniqueid.html language=enus -->
## TOPIC 02438: Sequence.GetStepByUniqueId

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getstepbyuniqueid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getstepbyuniqueid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetStepByUniqueId( uniqueStepId) Return Value Step Purpose Returns a reference to the Step object you specify by unique ID. Remarks Returns a NULL reference if no step exists with the unique ID you specify. Parameters uniqueStepId As String [In] Specifies the unique ID of the step fo

### Sequence.GetStepByUniqueId

#### Syntax

[Sequence](sequence.html).GetStepByUniqueId( uniqueStepId)

#### Return Value

[Step](step.html)

#### Purpose

Returns a reference to the Step object you specify by unique ID.

#### Remarks

Returns a
 NULL
 reference if no step exists with the unique ID you specify.

#### Parameters

uniqueStepId
 As
 [String](data-types-for-teststand.html)

[In] Specifies the unique ID of the step for which you want a reference.

#### See Also

[Sequence.GetStep](sequence-getstep.html)

[Sequence.GetStepByName](sequence-getstepbyname.html)

[Step](step.html)

[Step.UniqueStepId](step-uniquestepid.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-getstepindex.html language=enus -->
## TOPIC 02439: Sequence.GetStepIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-getstepindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-getstepindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GetStepIndex( nameOfStep, stepGroupParam) Return Value Long Returns the index of the step with the name that matches the name you specify. Returns -1 if no such step exists. Purpose Returns the index of the step with the name that matches the name you specify. Parameters nameOfStep A

### Sequence.GetStepIndex

#### Syntax

[Sequence](sequence.html).GetStepIndex( nameOfStep, stepGroupParam)

#### Return Value

[Long](data-types-for-teststand.html)

Returns the index of the step with the name that matches the name you specify. Returns
 -1
 if no such step exists.

#### Purpose

Returns the index of the step with the name that matches the name you specify.

#### Parameters

nameOfStep
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the step for which you want the index. When more than one step using the same name exists in the step group, the method returns the index of the first step with that name. Name comparison is case-insensitive. You can also pass a unique step ID.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

#### See Also

[Sequence.GetStepByName](sequence-getstepbyname.html)

[Sequence.GetStepByUniqueId](sequence-getstepbyuniqueid.html)

[Sequence.StepNameExists](sequence-stepnameexists.html)

[Step.UniqueStepId](step-uniquestepid.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-gotocleanuponfailure.html language=enus -->
## TOPIC 02440: Sequence.GotoCleanupOnFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-gotocleanuponfailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-gotocleanuponfailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.GotoCleanupOnFailure Data Type Boolean Purpose This property is obsolete. Use the Sequence.FailureAction property instead. Remarks Execution flow jumps to the Cleanup step group if this property is True and if a step sets the status property of the sequence to Failed . If the Station

### Sequence.GotoCleanupOnFailure

#### Syntax

[Sequence](sequence.html).GotoCleanupOnFailure

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

Sequence.FailureAction

#### Remarks

Execution flow jumps to the Cleanup step group if this property is
 True
 and if a step sets the status property of the sequence to
 Failed
 . If the
 [StationOptions.AlwaysGotoCleanupOnFailure](stationoptions-alwaysgotocleanuponfailure.html)
 property is
 True
 , the flow of execution jumps to the Cleanup step group on failure regardless of the state of this property.

#### See Also

[Sequence.FailureAction](sequence-failureaction.html)

[StationOptions.AlwaysGotoCleanupOnFailure](stationoptions-alwaysgotocleanuponfailure.html)

Parent topic:

Obsolete Sequence Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-hasmismatchedblocks.html language=enus -->
## TOPIC 02441: Sequence.HasMismatchedBlocks

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-hasmismatchedblocks.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-hasmismatchedblocks.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.HasMismatchedBlocks Data Type Boolean Purpose If this property is True , the sequence contains steps that define block structure and the steps are not properly matched. For example, this property is True if a sequence contains a For step without a corresponding End step. A sequence w

### Sequence.HasMismatchedBlocks

#### Syntax

[Sequence](sequence.html).HasMismatchedBlocks

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

If this property is
 True
 , the sequence contains steps that define block structure and the steps are not properly matched. For example, this property is
 True
 if a sequence contains a For step without a corresponding End step.

Note

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-id.html language=enus -->
## TOPIC 02442: Sequence.Id

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-id.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-id.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.Id Data Type Long Purpose Returns a unique identification number for the sequence. The ID number is never zero. Remarks The ID number is unique with respect to all sequences that you open before you shut down the TestStand Engine. Use this ID number to compare two sequence object ref

### Sequence.Id

#### Syntax

[Sequence](sequence.html).Id

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a unique identification number for the sequence.

Note

#### Remarks

The ID number is unique with respect to all sequences that you open before you shut down the TestStand Engine.

Use this ID number to compare two sequence object references to determine whether they refer to the same underlying sequence. A run-time copy of a sequence has a different ID than the corresponding edit-time copy of the sequence.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-insertstep.html language=enus -->
## TOPIC 02443: Sequence.InsertStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-insertstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-insertstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.InsertStep( stepToInsert, index, stepGroupParam) Purpose Inserts a step into the sequence. Remarks Never insert a step into a sequence when that step resides in another sequence. The step reference you pass must be the only reference to the step. You can obtain the sole reference to

### Sequence.InsertStep

#### Syntax

[Sequence](sequence.html).InsertStep( stepToInsert, index, stepGroupParam)

#### Purpose

Inserts a step into the sequence.

#### Remarks

Note

Engine.NewStep

Sequence.RemoveStep

#### Parameters

stepToInsert
 As
 [Step](step.html)

[In] Specifies the step to insert.

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index that indicates the location where to insert the step in the step group.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

#### See Also

[Engine.NewStep](engine-newstep.html)

[Sequence.DeleteStep](sequence-deletestep.html)

[Sequence.RemoveStep](sequence-removestep.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-loadmodules.html language=enus -->
## TOPIC 02444: Sequence.LoadModules

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-loadmodules.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-loadmodules.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.LoadModules( loadOptions = 0, [sequenceContextParam]) Return Value Boolean Returns True on success, or False if a module fails to load. Purpose Call this method to load the code modules for the steps in the sequence. Parameters loadOptions As Long [In] Specifies one or more LoadModul

### Sequence.LoadModules

#### Syntax

[Sequence](sequence.html).LoadModules( loadOptions = 0, [sequenceContextParam])

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 on success, or
 False
 if a module fails to load.

#### Purpose

Call this method to load the code modules for the steps in the sequence.

#### Parameters

loadOptions
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [LoadModuleOptions](loadmoduleoptions.html)
 using the bitwise-OR operator to modify the behavior of this method.

This parameter has a default value of
 0
 .

sequenceContextParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] If passing the
 [LoadModule_EvaluateExpressions](loadmoduleoptions.html)
 flag to the
 loadOptions
 parameter, pass a
 [SequenceContext](sequencecontext.html)
 object for this parameter to use when evaluating the expressions. Also, if calling this method from a step in an execution, pass the sequence context of the execution.

#### See Also

[Engine.UnloadAllModules](engine-unloadallmodules.html)

[LoadModuleOptions](loadmoduleoptions.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence.UnloadModules](sequence-unloadmodules.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-locals.html language=enus -->
## TOPIC 02445: Sequence.Locals

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-locals.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-locals.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.Locals Data Type PropertyObject Purpose Returns the PropertyObject that contains the local variables for the sequence. See Also PropertyObject SequenceFile.FileGlobalsDefaultValues

### Sequence.Locals

#### Syntax

[Sequence](sequence.html).Locals

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the PropertyObject that contains the local variables for the sequence.

#### See Also

[PropertyObject](propertyobject.html)

[SequenceFile.FileGlobalsDefaultValues](sequencefile-fileglobalsdefaultvalues.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-name.html language=enus -->
## TOPIC 02446: Sequence.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.Name Data Type String Purpose Returns or specifies the name of the sequence. Remarks The name of a sequence must be unique if it is contained within a sequence file. Inserting two or more sequences with the same name into a sequence file might cause unexpected behavior. TestStand doe

### Sequence.Name

#### Syntax

[Sequence](sequence.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns or specifies the name of the sequence.

#### Remarks

Note

Note

PropertyObject.ValidateNewElementName

MyVariableName_2000

NI

#### See Also

[PropertyObject.ValidateNewElementName](propertyobject-validatenewelementname.html)

[Sequence.SequenceIndex](sequence-sequenceindex.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-optimizenonreentrantcalls.html language=enus -->
## TOPIC 02447: Sequence.OptimizeNonReentrantCalls

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-optimizenonreentrantcalls.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-optimizenonreentrantcalls.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.OptimizeNonReentrantCalls Data Type Boolean Purpose Specifies to decrease the amount of time required for TestStand to call the sequence after the first call to the sequence in an execution. Remarks If you set this property to False , TestStand initializes a new copy of each custom s

### Sequence.OptimizeNonReentrantCalls

#### Syntax

[Sequence](sequence.html).OptimizeNonReentrantCalls

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to decrease the amount of time required for TestStand to call the sequence after the first call to the sequence in an execution.

#### Remarks

If you set this property to
 False
 , TestStand initializes a new copy of each custom step property in a sequence each time it calls the sequence. TestStand performs the initialization so the sequence always begins executing with the initial property values the steps in the sequence specify. This initialization is necessary only if a sequence relies on the initial value of a custom step property and then modifies the value. Few sequences rely on this information.

When you set this property to
 True
 , TestStand initializes the value of the custom step properties in the sequence the first time it calls the sequence in an execution. TestStand reuses the custom step property values when it calls the sequence again. If the same sequence is in a different thread or recursively within the same thread simultaneously, TestStand creates unique copies of the custom step properties.

Note

True

False

#### See Also

[General tab of the Sequence File Properties dialog box](../tsref/general-tab-sequence-file-properties-dialog-b.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-parameters.html language=enus -->
## TOPIC 02448: Sequence.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.Parameters Data Type PropertyObject Purpose Returns the PropertyObject that contains the parameters for the sequence. See Also PropertyObject Sequence.Locals

### Sequence.Parameters

#### Syntax

[Sequence](sequence.html).Parameters

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the PropertyObject that contains the parameters for the sequence.

#### See Also

[PropertyObject](propertyobject.html)

[Sequence.Locals](sequence-locals.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-removestep.html language=enus -->
## TOPIC 02449: Sequence.RemoveStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-removestep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-removestep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.RemoveStep( index, stepGroupParam) Return Value Step Purpose Removes a step from a sequence and returns a reference to it. Parameters index As Long [In] Specifies the zero-based index that indicates the location where to insert the step in the step group. stepGroupParam As StepGroups

### Sequence.RemoveStep

#### Syntax

[Sequence](sequence.html).RemoveStep( index, stepGroupParam)

#### Return Value

[Step](step.html)

#### Purpose

Removes a step from a sequence and returns a reference to it.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index that indicates the location where to insert the step in the step group.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

#### See Also

[Sequence.DeleteStep](sequence-deletestep.html)

[Sequence.InsertStep](sequence-insertstep.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-requirements.html language=enus -->
## TOPIC 02450: Sequence.Requirements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-requirements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-requirements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.Requirements Data Type PropertyObject Purpose Returns the Requirements property for the sequence. The Links subproperty of the Requirements property is an array of string values that represents the product and unit requirements the sequence covers. Remarks You can use the following p

### Sequence.Requirements

#### Syntax

[Sequence](sequence.html).Requirements

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the Requirements property for the sequence. The Links subproperty of the Requirements property is an array of string values that represents the product and unit requirements the sequence covers.

#### Remarks

You can use the following pseudocode to add a new element to the list of requirements:

PropertyObject links = sequence.Requirements.GetPropertyObject("Links", 0);
 int nextAvailableIndex = links.GetNumElements();
 links.SetValStringByOffset(nextAvailableIndex, PropertyOptions.PropOption_InsertElement, "REQ_ABC");

#### See Also

[PropertyObject](propertyobject.html)

[PropertyObjectFile.Requirements](propertyobjectfile-requirements.html)

[Step.Requirements](step-requirements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-sequencefile.html language=enus -->
## TOPIC 02451: Sequence.SequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-sequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-sequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.SequenceFile Data Type SequenceFile Returns the containing sequence file or a NULL reference if this sequence does not belong to a sequence file. Purpose Returns the sequence file that contains this sequence. See Also SequenceFile

### Sequence.SequenceFile

#### Syntax

[Sequence](sequence.html).SequenceFile

#### Data Type

[SequenceFile](sequencefile.html)

Returns the containing sequence file or a
 NULL
 reference if this sequence does not belong to a sequence file.

#### Purpose

Returns the sequence file that contains this sequence.

#### See Also

[SequenceFile](sequencefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-sequenceindex.html language=enus -->
## TOPIC 02452: Sequence.SequenceIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-sequenceindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-sequenceindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.SequenceIndex Data Type Long Purpose Returns the zero-based index of the sequence within the containing sequence file. Returns -1 if the sequence is not within a sequence file. See Also Sequence.Name

### Sequence.SequenceIndex

#### Syntax

[Sequence](sequence.html).SequenceIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the zero-based index of the sequence within the containing sequence file. Returns
 -1
 if the sequence is not within a sequence file.

#### See Also

[Sequence.Name](sequence-name.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-setbreakonend.html language=enus -->
## TOPIC 02453: Sequence.SetBreakOnEnd

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-setbreakonend.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-setbreakonend.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.SetBreakOnEnd( stepGroupParam, breakOnEnd, [executionParam]) Purpose This method is obsolete. Use the Sequence.SetBreakOnEndSettings method instead. Remarks Notifies TestStand when executions of this sequence and step group break after executing steps. Use this method, along with the

### Sequence.SetBreakOnEnd

#### Syntax

[Sequence](sequence.html).SetBreakOnEnd( stepGroupParam, breakOnEnd, [executionParam])

#### Purpose

Note

Sequence.SetBreakOnEndSettings

#### Remarks

Notifies TestStand when executions of this sequence and step group break after executing steps.

Use this method, along with the
 Sequence.GetBreakOnEnd
 method, to implement breakpoints for breaking after the last step in a step group.

Note

Sequence.GetBreakOnEnd

Sequence.GetBreakOnEndSettings

#### Parameters

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

breakOnEnd
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 if you want executions of this sequence and step group to break after executing steps.

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Pass a reference to an Execution object to obtain the breakpoint settings on the End step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method returns the breakpoint setting on the End step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence.GetBreakOnEndSettings](sequence-getbreakonendsettings.html)

[Sequence.SetBreakOnEndSettings](sequence-setbreakonendsettings.html)

[Step.GetBreakSettings](step-getbreaksettings.html)

[StepGroups](stepgroups.html)

Parent topic:

Obsolete Sequence Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-setbreakonendsettings.html language=enus -->
## TOPIC 02454: Sequence.SetBreakOnEndSettings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-setbreakonendsettings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-setbreakonendsettings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.SetBreakOnEndSettings( stepGroupParam, isSet, enabled, passCount, Condition, [executionParam]) Purpose Specifies if the step group in the sequence is set to break after all the steps in the sequence execute. Parameters stepGroupParam As StepGroups [In] Specifies a particular step gro

### Sequence.SetBreakOnEndSettings

#### Syntax

[Sequence](sequence.html).SetBreakOnEndSettings( stepGroupParam, isSet, enabled, passCount, Condition, [executionParam])

#### Purpose

Specifies if the step group in the sequence is set to break after all the steps in the sequence execute.

#### Parameters

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

isSet
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether the breakpoint is set. If a breakpoint is set, this parameter returns
 True
 .

enabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether the breakpoint is enabled. TestStand ignores disabled breakpoints during execution.

passCount
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the number of iterations the execution skips the breakpoint before suspending execution. Pass
 0
 if you do not want to use a conditional pass count.

Condition
 As
 [String](data-types-for-teststand.html)

[In] Specifies the expression that must evaluate to
 True
 before suspending the execution. An empty value defaults to
 True
 . If you specify a non-zero pass count value and a condition expression for the breakpoint, the pass count only decrements when the expression evaluates to
 True
 .

executionParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies a reference to an Execution object to obtain the breakpoint settings on the End step, which apply to a particular execution. If there is no execution-specific breakpoint setting or if you do not pass an Execution object, the method returns the breakpoint setting on the End step of the sequence file.

#### See Also

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

[Sequence.GetBreakOnEndSettings](sequence-getbreakonendsettings.html)

[Step.SetBreakSettings](step-setbreaksettings.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-showentrypointforallwindows.html language=enus -->
## TOPIC 02455: Sequence.ShowEntryPointForAllWindows

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-showentrypointforallwindows.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-showentrypointforallwindows.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.ShowEntryPointForAllWindows Data Type Boolean Purpose Set this property to True if you want the entry point to appear in the menu bar, regardless of what type of window is active. Remarks This property applies only to an entry point sequence in a process model file. See Also Sequence

### Sequence.ShowEntryPointForAllWindows

#### Syntax

[Sequence](sequence.html).ShowEntryPointForAllWindows

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 if you want the entry point to appear in the menu bar, regardless of what type of window is active.

#### Remarks

This property applies only to an entry point sequence in a process model file.

#### See Also

[Sequence.ShowEntryPointForEditorOnly](sequence-showentrypointforeditoronly.html)

[Sequence.ShowEntryPointForExeWindow](sequence-showentrypointforexewindow.html)

[Sequence.ShowEntryPointForFileWindow](sequence-showentrypointforfilewindow.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-showentrypointforeditoronly.html language=enus -->
## TOPIC 02456: Sequence.ShowEntryPointForEditorOnly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-showentrypointforeditoronly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-showentrypointforeditoronly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.ShowEntryPointForEditorOnly Data Type Boolean Purpose Set this property to True if you want the entry point to appear only in the menu bar of a sequence editor and not in an operator interface. Remarks This property applies only to an entry point sequence in a process model file. See

### Sequence.ShowEntryPointForEditorOnly

#### Syntax

[Sequence](sequence.html).ShowEntryPointForEditorOnly

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 if you want the entry point to appear only in the menu bar of a sequence editor and not in an operator interface.

#### Remarks

This property applies only to an entry point sequence in a process model file.

#### See Also

[Sequence.ShowEntryPointForAllWindows](sequence-showentrypointforallwindows.html)

[Sequence.ShowEntryPointForExeWindow](sequence-showentrypointforexewindow.html)

[Sequence.ShowEntryPointForFileWindow](sequence-showentrypointforfilewindow.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-showentrypointforexewindow.html language=enus -->
## TOPIC 02457: Sequence.ShowEntryPointForExeWindow

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-showentrypointforexewindow.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-showentrypointforexewindow.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.ShowEntryPointForExeWindow Data Type Boolean Purpose Set this property to True if you want the entry point to appear in the menu bar when an Execution window is the active window. Remarks This property applies only to an entry point sequence in a process model file. See Also Sequence

### Sequence.ShowEntryPointForExeWindow

#### Syntax

[Sequence](sequence.html).ShowEntryPointForExeWindow

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 if you want the entry point to appear in the menu bar when an Execution window is the active window.

#### Remarks

This property applies only to an entry point sequence in a process model file.

#### See Also

[Sequence.ShowEntryPointForAllWindows](sequence-showentrypointforallwindows.html)

[Sequence.ShowEntryPointForEditorOnly](sequence-showentrypointforeditoronly.html)

[Sequence.ShowEntryPointForFileWindow](sequence-showentrypointforfilewindow.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-showentrypointforfilewindow.html language=enus -->
## TOPIC 02458: Sequence.ShowEntryPointForFileWindow

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-showentrypointforfilewindow.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-showentrypointforfilewindow.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.ShowEntryPointForFileWindow Data Type Boolean Purpose Set this property to True if you want the entry point to appear in the menu bar when a Sequence File window is the active window. Remarks This property applies only to an entry point sequence in a process model file. See Also Sequ

### Sequence.ShowEntryPointForFileWindow

#### Syntax

[Sequence](sequence.html).ShowEntryPointForFileWindow

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 if you want the entry point to appear in the menu bar when a Sequence File window is the active window.

#### Remarks

This property applies only to an entry point sequence in a process model file.

#### See Also

[Sequence.ShowEntryPointForAllWindows](sequence-showentrypointforallwindows.html)

[Sequence.ShowEntryPointForEditorOnly](sequence-showentrypointforeditoronly.html)

[Sequence.ShowEntryPointForExeWindow](sequence-showentrypointforexewindow.html)

[Sequence.Type](sequence-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-stepnameexists.html language=enus -->
## TOPIC 02459: Sequence.StepNameExists

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-stepnameexists.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-stepnameexists.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.StepNameExists( nameOfStep, stepGroupParam) Return Value Boolean Purpose Returns True if a step with the name you specify exists in the step group. Parameters nameOfStep As String [In] Specifies the name to search for. stepGroupParam As StepGroups [In] Specifies a particular step gro

### Sequence.StepNameExists

#### Syntax

[Sequence](sequence.html).StepNameExists( nameOfStep, stepGroupParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if a step with the name you specify exists in the step group.

#### Parameters

nameOfStep
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name to search for.

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies a particular step group.

#### See Also

[Sequence.GetStepByName](sequence-getstepbyname.html)

[Sequence.GetStepIndex](sequence-getstepindex.html)

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-type.html language=enus -->
## TOPIC 02460: Sequence.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.Type Data Type SequenceTypes Use the following constants with this data type: SeqType_Callback –(Value: 1) The sequence is a Process Model callback. SeqType_CfgEntryPoint –(Value: 5) The sequence is a Configuration entry point. SeqType_ExeEntryPoint –(Value: 3) The sequence is an Exe

### Sequence.Type

#### Syntax

[Sequence](sequence.html).Type

#### Data Type

[SequenceTypes](sequencetypes.html)

Use the following constants with this data type:

- SeqType_Callback 
 –(Value: 1) The sequence is a Process Model callback.
- SeqType_CfgEntryPoint 
 –(Value: 5) The sequence is a Configuration entry point.
- SeqType_ExeEntryPoint 
 –(Value: 3) The sequence is an Execution entry point.
- SeqType_Normal 
 –(Value: 0) The sequence is not a callback or an entry point.
- SeqType_ReservedCallback 
 –(Value: 7) Only the
 Sequence.GetEffectiveType 
 method returns this value. The sequence is one of the predefined callbacks TestStand reserves.

#### Purpose

Specifies the type of the sequence.

#### See Also

[Sequence.GetEffectiveType](sequence-geteffectivetype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence-unloadmodules.html language=enus -->
## TOPIC 02461: Sequence.UnloadModules

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence-unloadmodules.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence-unloadmodules.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Sequence.UnloadModules Return Value Boolean Returns True if all code modules are unloaded. Some code modules might not be unloaded because they are executing. Purpose Unloads code modules for all steps in the sequence. See Also Engine.UnloadAllModules Sequence.LoadModules

### Sequence.UnloadModules

#### Syntax

[Sequence](sequence.html).UnloadModules

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if all code modules are unloaded.

Note

#### Purpose

Unloads code modules for all steps in the sequence.

#### See Also

[Engine.UnloadAllModules](engine-unloadallmodules.html)

[Sequence.LoadModules](sequence-loadmodules.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequence.html language=enus -->
## TOPIC 02462: Sequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the Sequence class represent a sequence that can contain steps. Use the Sequence class to examine or modify sequence settings and the list of steps in the sequence. Sequences have three groups of steps. The StepGroups enumeration contains a value for each of the step groups. SequenceTypes

### Sequence

Objects of the Sequence class represent a sequence that can contain steps. Use the Sequence class to examine or modify sequence settings and the list of steps in the sequence. Sequences have three groups of steps. The
 [StepGroups](stepgroups.html)
 enumeration contains a value for each of the step groups.
 [SequenceTypes](sequencetypes.html)
 constants define several types of sequences. You can obtain a reference to the Sequence objects a sequence file contains by calling the
 [SequenceFile.GetSequence](sequencefile-getsequence.html)
 method. You can create new sequences by calling the
 [Engine.NewSequence](engine-newsequence.html)
 or
 [SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)
 methods.

Note

#### Properties

| AllowInteractiveExecutionOfEntryPoint |
| --- |
| CopyStepsOnOverride |
| DisableResults |
| EntryPointCheckToSaveTitledSeqFiles |
| EntryPointEnabledExpression |
| EntryPointIgnoreClient |
| EntryPointInitiallyHidden |
| EntryPointMenuHint |
| EntryPointNameExpression |
| FailureAction |
| HasMismatchedBlocks (Read Only) |
| Id (Read Only) |
| Locals (Read Only) |
| Name |
| OptimizeNonReentrantCalls |
| Parameters (Read Only) |
| Requirements (Read Only) |
| SequenceFile (Read Only) |
| SequenceIndex (Read Only) |
| ShowEntryPointForAllWindows |
| ShowEntryPointForEditorOnly |
| ShowEntryPointForExeWindow |
| ShowEntryPointForFileWindow |
| Type |

#### Methods

| AsPropertyObject |
| --- |
| CreateNewUniqueStepIds |
| DeleteStep |
| EvalEntryPointEnabledExpressionEx |
| EvalEntryPointNameExpressionEx |
| GetBreakOnEndSettings |
| GetEffectiveType |
| GetEntryPointMenuFromHint |
| GetNumSteps |
| GetStep |
| GetStepByName |
| GetStepByUniqueId |
| GetStepIndex |
| InsertStep |
| LoadModules |
| RemoveStep |
| SetBreakOnEndSettings |
| StepNameExists |
| UnloadModules |

#### See Also

[Engine.NewSequence](engine-newsequence.html)

[Step](step.html)

[SequenceFile.CreateCallbackOverrideSequence](sequencefile-createcallbackoverridesequence.html)

[SequenceFile.GetSequence](sequencefile-getsequence.html)

[SequenceTypes](sequencetypes.html)

[StepGroups](stepgroups.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequenceadapter-asadapter.html language=enus -->
## TOPIC 02463: SequenceAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequenceadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequenceadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter that represents the SequenceAdapter object. Remarks Use the underlying module Adapter object to access properties and methods common to all adapters. See Also Adapter

### SequenceAdapter.AsAdapter

#### Syntax

[SequenceAdapter](sequenceadapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter that represents the SequenceAdapter object.

#### Remarks

Use the underlying module Adapter object to access properties and methods common to all adapters.

#### See Also

[Adapter](adapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequenceadapter-getsequencefile.html language=enus -->
## TOPIC 02464: SequenceAdapter.GetSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequenceadapter-getsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequenceadapter-getsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceAdapter.GetSequenceFile( path) Return Value SequenceFile Returns a reference to a SequenceFile object that represents the sequence file the path parameter specifies. The returned reference is null if the path parameter is invalid or does not specify a valid sequence file. Purpose Retu

### SequenceAdapter.GetSequenceFile

#### Syntax

[SequenceAdapter](sequenceadapter.html).GetSequenceFile( path)

#### Return Value

[SequenceFile](sequencefile.html)

Returns a reference to a
 SequenceFile
 object that represents the sequence file the
 path
 parameter specifies. The returned reference is null if the
 path
 parameter is invalid or does not specify a valid sequence file.

#### Purpose

Returns a reference to a
 [SequenceFile](sequencefile.html)
 object for examining the contents of the file.

#### Remarks

Use this method to examine the contents of a sequence file without running load and unload callbacks, without preloading modules, and without merging types. Sequence files loaded by this method remain in memory until they have not been referenced after several minutes. As a result, calling this method multiple times for the same file does not usually cause the file to be loaded multiple times.

Do not call
 [Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)
 on this object before releasing it.

To execute or edit a sequence file, use the
 [Engine.GetSequenceFileEx](engine-getsequencefileex.html)
 method instead of this method.

#### Parameters

path
 As
 [String](data-types-for-teststand.html)

[In] Specifies the absolute pathname of the sequence file.

#### See Also

[Engine.GetSequenceFileEx](engine-getsequencefileex.html)

[Engine.ReleaseSequenceFileEx](engine-releasesequencefileex.html)

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequenceadapter.html language=enus -->
## TOPIC 02465: SequenceAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequenceadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequenceadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the Sequence Adapter class to configure and obtain Sequence Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class,

### SequenceAdapter

Use objects from the Sequence Adapter class to configure and obtain Sequence Adapter-specific information about the module adapter. Call the
 
 [Engine.GetAdapter](engine-getadapter.html)
 or
 
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 method to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use the
 [SequenceAdapter.AsAdapter](sequenceadapter-asadapter.html)
 method to obtain an object.

#### Methods

| AsAdapter |
| --- |
| GetSequenceFile |

#### See Also

[Adapter](adapter.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-asmodule.html language=enus -->
## TOPIC 02466: SequenceCallModule.AsModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-asmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-asmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.AsModule Return Value Module Purpose Returns the underlying Module object that represents the SequenceCallModule object. Remarks Use the Module object to access properties and methods common to all modules. See Also Module

### SequenceCallModule.AsModule

#### Syntax

[SequenceCallModule](sequencecallmodule.html).AsModule

#### Return Value

[Module](module.html)

#### Purpose

Returns the underlying Module object that represents the SequenceCallModule object.

#### Remarks

Use the Module object to access properties and methods common to all modules.

#### See Also

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-cpuaffinityfornewthreadopt.html language=enus -->
## TOPIC 02467: SequenceCallModule.CPUAffinityForNewThreadOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-cpuaffinityfornewthreadopt.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-cpuaffinityfornewthreadopt.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.CPUAffinityForNewThreadOption Data Type CPUAffinityForNewThreadOptions Use the following constants with this data type: CPUAffinityForNewThreadOption_UseAffinityOfCaller –(Value: 1) Specifies to use the CPU affinity of the calling sequence as the CPU affinity of the new thr

### SequenceCallModule.CPUAffinityForNewThreadOption

#### Syntax

[SequenceCallModule](sequencecallmodule.html).CPUAffinityForNewThreadOption

#### Data Type

[CPUAffinityForNewThreadOptions](cpuaffinityfornewthreadoptions.html)

Use the following constants with this data type:

- CPUAffinityForNewThreadOption_UseAffinityOfCaller 
 –(Value: 1) Specifies to use the CPU affinity of the calling sequence as the CPU affinity of the new thread.
- CPUAffinityForNewThreadOption_UseAllCPUs 
 –(Value: 2) Specifies to use all CPUs available to the process as the CPU affinity of the new thread.
- CPUAffinityForNewThreadOption_UseCustomAffinity 
 –(Value: 3) Specifies to use an expression to determine the CPU affinity of the new thread.
- CPUAffinityForNewThreadOption_UseStationOption 
 –(Value: 0) Specifies to use the
 StationOptions.DefaultCPUAffinityForThreadsEx 
 property as the CPU affinity of the new thread.

#### Purpose

Specifies the CPUs on which the new thread executes.

#### Remarks

The value this property specifies applies only if the value of the
 [SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)
 property is
 SeqCallMultithread_NewThread
 or
 SeqCallMultithread_NewExecution
 .

You can
 [optimize TestStand performance on symmetric multiprocessing (SMP) systems](/csh?context=ts_tsfundamentals_smp_clarification)
 for multithreaded applications.

#### See Also

[SeqCallMultithreadOptions](seqcallmultithreadoptions.html)

[SequenceCallModule.CustomCPUAffinityForNewThread](sequencecallmodule-customcpuaffinityfornewthr.html)

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[StationOptions.DefaultCPUAffinityForThreadsEx](stationoptions-defaultcpuaffinityforthreadsex.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-customcpuaffinityfornewthr.html language=enus -->
## TOPIC 02468: SequenceCallModule.CustomCPUAffinityForNewThread

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-customcpuaffinityfornewthr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-customcpuaffinityfornewthr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.CustomCPUAffinityForNewThread Data Type String Purpose A numeric expression that specifies the CPUs on which the new thread executes when the value of the SequenceCallModule.CPUAffinityForNewThreadOption property is CPUAffinityForNewThreadOption_UseCustomAffinity . Remarks

### SequenceCallModule.CustomCPUAffinityForNewThread

#### Syntax

[SequenceCallModule](sequencecallmodule.html).CustomCPUAffinityForNewThread

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

A numeric expression that specifies the CPUs on which the new thread executes when the value of the
 [SequenceCallModule.CPUAffinityForNewThreadOption](sequencecallmodule-cpuaffinityfornewthreadopt.html)
 property is
 CPUAffinityForNewThreadOption_UseCustomAffinity
 .

#### Remarks

This property evaluates to a numeric value in which each bit represents a CPU. The lowest-order bit represents the first CPU. For example, a value of
 12
 , which is
 1100
 in binary, represents CPUs 3 and 4 on a quad-core computer. A value of
 -1
 specifies to use all CPUs available to the process.

The value this property specifies applies only if the value of the
 [SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)
 property is
 SeqCallMultithread_NewThread
 or
 SeqCallMultithread_NewExecution
 .

Refer to
 [Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)
 for more information about optimizing TestStand performance on symmetric multiprocessing (SMP) systems for multithreaded applications.

#### See Also

[SeqCallMultithreadOptions](seqcallmultithreadoptions.html)

[SequenceCallModule.CPUAffinityForNewThreadOption](sequencecallmodule-cpuaffinityfornewthreadopt.html)

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[Using TestStand on SMP Systems](/csh?context=ts_tsfundamentals_smp_clarification)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-ignoretermination.html language=enus -->
## TOPIC 02469: SequenceCallModule.IgnoreTermination

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-ignoretermination.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-ignoretermination.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.IgnoreTermination Data Type Boolean Purpose Specifies what happens when the subsequence the module calls causes execution to terminate. If this property is True and TestStand terminates the subsequence, TestStand sets the status of the module step to Terminated but allows t

### SequenceCallModule.IgnoreTermination

#### Syntax

[SequenceCallModule](sequencecallmodule.html).IgnoreTermination

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies what happens when the subsequence the module calls causes execution to terminate. If this property is
 True
 and TestStand terminates the subsequence, TestStand sets the status of the module step to
 Terminated
 but allows the module sequence to proceed normally from the next step. Usually, only one process model file uses this option. This option has no effect when the execution aborts.

#### Remarks

This property corresponds to the Ignore Termination option on the
 [Run Options tab](../tsref/run-options-tab-step-properties-dialog-box.html)
 of the
 [Step Properties](../tsref/step-properties-dialog-box.html)
 dialog box.

#### See Also

[Run Options tab](../tsref/run-options-tab-step-properties-dialog-box.html)

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-initiallysuspended.html language=enus -->
## TOPIC 02470: SequenceCallModule.InitiallySuspended

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-initiallysuspended.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-initiallysuspended.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.InitiallySuspended Data Type Boolean Purpose Specifies to create the new execution or thread in a suspended state. You must call the Execution.Resume or Thread.Resume method, respectively, to continue execution. Remarks If you select Break or Resume in the Debug menu of the

### SequenceCallModule.InitiallySuspended

#### Syntax

[SequenceCallModule](sequencecallmodule.html).InitiallySuspended

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies to create the new execution or thread in a suspended state. You must call the
 [Execution.Resume](execution-resume.html)
 or
 [Thread.Resume](thread-resume.html)
 method, respectively, to continue execution.

#### Remarks

Note

Break

Resume

#### See Also

[Execution.Resume](execution-resume.html)

[Thread.Resume](thread-resume.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-loadparameters.html language=enus -->
## TOPIC 02471: SequenceCallModule.LoadParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-loadparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-loadparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.LoadParameters( useCurrentSeqFile, seqFilePath, seqName) Purpose This method is obsolete. Use the Module.LoadPrototype method instead. Remarks Loads parameter information from the sequence file and sequence of the module or a specific sequence file and sequence. If Sequence

### SequenceCallModule.LoadParameters

#### Syntax

[SequenceCallModule](sequencecallmodule.html).LoadParameters( useCurrentSeqFile, seqFilePath, seqName)

#### Purpose

Note

Module.LoadPrototype

#### Remarks

Loads parameter information from the sequence file and sequence of the module or a specific sequence file and sequence.

If
 [SequenceCallModule.UseSequenceParameterPrototype](sequencecallmodule-usesequenceparameterprotot.html)
 is
 True
 and
 [SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)
 is
 False
 , this method ignores the parameters and loads the parameter information from the sequence the
 [SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)
 ,
 [SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)
 , and
 [SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)
 properties specify. Otherwise, this method loads the parameter information from the sequence the parameters of this method specify.

You must call this method or the
 [SequenceCallModule.LoadParametersFromSequence](sequencecallmodule-loadparametersfromsequence.html)
 method before accessing the
 [SequenceCallModule.Parameters](sequencecallmodule-parameters.html)
 property of the module.

#### Parameters

useCurrentSeqFile
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies to use the sequence file and sequence of the sequence call.

seqFilePath
 As
 [String](data-types-for-teststand.html)

[In] Specifies a specific sequence file when the
 useCurrentSeqFile
 parameter is
 False
 .

seqName
 As
 [String](data-types-for-teststand.html)

[In] Specifies a specific sequence name.

#### See Also

[Module.LoadPrototype](module-loadprototype.html)

[SequenceCallModule.LoadParametersFromSequence](sequencecallmodule-loadparametersfromsequence.html)

[SequenceCallModule.Parameters](sequencecallmodule-parameters.html)

[SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

[SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)

[SequenceCallModule.UseSequenceParameterPrototype](sequencecallmodule-usesequenceparameterprotot.html)

[SequenceCallParameter.ValueExpr](sequencecallparameter-valueexpr.html)

Parent topic:

Obsolete SequenceCallModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-loadparametersfromsequence.html language=enus -->
## TOPIC 02472: SequenceCallModule.LoadParametersFromSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-loadparametersfromsequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-loadparametersfromsequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.LoadParametersFromSequence( sequence) Purpose This property is obsolete. Use the SequenceCallModule.LoadPrototypeFromSequence method instead. Remarks Loads parameter information from the specified sequence. If the SequenceCallModule.UseSequenceParameterPrototype property is

### SequenceCallModule.LoadParametersFromSequence

#### Syntax

[SequenceCallModule](sequencecallmodule.html).LoadParametersFromSequence( sequence)

#### Purpose

Note

SequenceCallModule.LoadPrototypeFromSequence

#### Remarks

Loads parameter information from the specified sequence. If the
 [SequenceCallModule.UseSequenceParameterPrototype](sequencecallmodule-usesequenceparameterprotot.html)
 property is
 True
 , this method ignores the parameters and loads the parameter information from the sequence the
 sequence
 parameter of this method specifies.

You must call the
 [SequenceCallModule.LoadParameters](sequencecallmodule-loadparameters.html)
 method or this method before accessing the
 [SequenceCallModule.Parameters](sequencecallmodule-parameters.html)
 property of the module.

#### Parameters

sequence
 As
 
 [Sequence](sequence.html)

[In] Specifies the sequence that contains the prototype to load.

#### See Also

[Sequence](sequence.html)

[SequenceCallModule.LoadParameters](sequencecallmodule-loadparameters.html)

[SequenceCallModule.LoadPrototypeFromSequence](sequencecallmodule-loadprototypefromsequence.html)

[SequenceCallModule.Parameters](sequencecallmodule-parameters.html)

[SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

[SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)

[SequenceCallModule.UseSequenceParameterPrototype](sequencecallmodule-usesequenceparameterprotot.html)

[SequenceCallParameter.ValueExpr](sequencecallparameter-valueexpr.html)

Parent topic:

Obsolete SequenceCallModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-loadprototypefromsequence.html language=enus -->
## TOPIC 02473: SequenceCallModule.LoadPrototypeFromSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-loadprototypefromsequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-loadprototypefromsequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.LoadPrototypeFromSequence( sequence, options) Return Value Boolean Returns a value that indicates whether the step was modified. Purpose Sets the prototype of the module to the prototype specified by a sequence. Remarks Use this method to set the parameters of the SequenceC

### SequenceCallModule.LoadPrototypeFromSequence

#### Syntax

[SequenceCallModule](sequencecallmodule.html).LoadPrototypeFromSequence( sequence, options)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the step was modified.

#### Purpose

Sets the prototype of the module to the prototype specified by a sequence.

#### Remarks

Use this method to set the parameters of the SequenceCallModule when the
 [SequenceCallModule.UseSequenceParameterPrototype](sequencecallmodule-usesequenceparameterprotot.html)
 property is
 False
 or if the
 [SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)
 property is
 True
 .

#### Parameters

sequence
 As
 
 [Sequence](sequence.html)

[In] Specifies the sequence with the prototype to use.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specify one or more
 [LoadPrototypeOptions](loadprototypeoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

#### See Also

[LoadPrototypeOptions](loadprototypeoptions.html)

[Module.LoadPrototype](module-loadprototype.html)

[Sequence](sequence.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

[SequenceCallModule.UseSequenceParameterPrototype](sequencecallmodule-usesequenceparameterprotot.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-multithreadingandremoteexe.html language=enus -->
## TOPIC 02474: SequenceCallModule.MultithreadingAndRemoteExecOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-multithreadingandremoteexe.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-multithreadingandremoteexe.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.MultithreadingAndRemoteExecOption Data Type SeqCallMultithreadOptions Use the following constants with this data type: SeqCallMultithread_NewExecution –(Value: 2) Specifies to call the subsequence in a new execution. SeqCallMultithread_NewThread –(Value: 1) Specifies to cal

### SequenceCallModule.MultithreadingAndRemoteExecOption

#### Syntax

[SequenceCallModule](sequencecallmodule.html).MultithreadingAndRemoteExecOption

#### Data Type

[SeqCallMultithreadOptions](seqcallmultithreadoptions.html)

Use the following constants with this data type:

- SeqCallMultithread_NewExecution 
 –(Value: 2) Specifies to call the subsequence in a new execution.
- SeqCallMultithread_NewThread 
 –(Value: 1) Specifies to call the subsequence in a new thread.
- SeqCallMultithread_None 
 –(Value: 0) Specifies to call the subsequence in the current thread and execution on the current computer.
- SeqCallMultithread_Remote 
 –(Value: 0x100) Specifies to call the subsequence on a remote computer.

#### Purpose

Specifies that the module calls the subsequence in a separate thread, separate execution, or on a remote computer.

#### See Also

[SequenceCallModule.NewExecutionModelOption](sequencecallmodule-newexecutionmodeloption.html)

[SequenceCallModule.NewThreadOptions](sequencecallmodule-newthreadoptions.html)

[SequenceCallModule.RemoteHost](sequencecallmodule-remotehost.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-newexecutionbreakonentryex.html language=enus -->
## TOPIC 02475: SequenceCallModule.NewExecutionBreakOnEntryExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-newexecutionbreakonentryex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-newexecutionbreakonentryex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.NewExecutionBreakOnEntryExpr Data Type String Purpose Specifies an expression that, when it evaluates to True , suspends execution before executing the first step when calling a subsequence. See Also SequenceCallModule.MultithreadingAndRemoteExecOption

### SequenceCallModule.NewExecutionBreakOnEntryExpr

#### Syntax

[SequenceCallModule](sequencecallmodule.html).NewExecutionBreakOnEntryExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression that, when it evaluates to
 True
 , suspends execution before executing the first step when calling a subsequence.

#### See Also

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-newexecutionmodeloption.html language=enus -->
## TOPIC 02476: SequenceCallModule.NewExecutionModelOption

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-newexecutionmodeloption.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-newexecutionmodeloption.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.NewExecutionModelOption Data Type SeqCallNewExecModelOptions Use the following constants with this data type: SeqCallNewExecModel_None –(Value: 0) The new execution does not run under a process model. SeqCallNewExecModel_SpecifyModel –(Value: 2) When you set this option, yo

### SequenceCallModule.NewExecutionModelOption

#### Syntax

[SequenceCallModule](sequencecallmodule.html).NewExecutionModelOption

#### Data Type

[SeqCallNewExecModelOptions](seqcallnewexecmodeloptions.html)

Use the following constants with this data type:

- SeqCallNewExecModel_None 
 –(Value: 0) The new execution does not run under a process model.
- SeqCallNewExecModel_SpecifyModel 
 –(Value: 2) When you set this option, you can use the
 SequenceCallModule.NewExecutionModelPath 
 property to specify the process model under which the new execution runs. You can also use the
 SequenceCallModule.SequenceName 
 property to specify which entry point to call in the process model. Typically, the Process Model entry point calls the
 MainSequence 
 in the client sequence file you specify.
- SeqCallNewExecModel_UseModelOfCurrentFile 
 –(Value: 1) When you set this option, the execution runs under the model the sequence file you call specifies. If the file you call does not specify a model, the execution runs under the default station model. You can use the
 SequenceCallModule.SequenceName 
 property to designate which entry point to call in the process model. Typically, the Process Model entry point calls the
 MainSequence 
 in the client sequence file you specify.

#### Purpose

Specifies which process model the new execution uses when calling a subsequence in a new execution.

#### See Also

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[SequenceCallModule.NewExecutionModelPath](sequencecallmodule-newexecutionmodelpath.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-newexecutionmodelpath.html language=enus -->
## TOPIC 02477: SequenceCallModule.NewExecutionModelPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-newexecutionmodelpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-newexecutionmodelpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.NewExecutionModelPath Data Type String Purpose Specifies the path to the process model the new execution uses when calling a subsequence in a new execution. Remarks Specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand searc

### SequenceCallModule.NewExecutionModelPath

#### Syntax

[SequenceCallModule](sequencecallmodule.html).NewExecutionModelPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path to the process model the new execution uses when calling a subsequence in a new execution.

#### Remarks

Specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

You must specify an expression for the file pathname if the
 [SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)
 property is
 True
 .

The Sequence Adapter ignores this property unless you set the
 [SequenceCallModule.NewExecutionModelOption](sequencecallmodule-newexecutionmodeloption.html)
 property equal to
 [SeqCallNewExecModel_SpecifyModel](seqcallnewexecmodeloptions.html)
 .

#### See Also

[SeqCallNewExecModelOptions](seqcallnewexecmodeloptions.html)

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[SequenceCallModule.NewExecutionModelOption](sequencecallmodule-newexecutionmodeloption.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-newexecutiontypemask.html language=enus -->
## TOPIC 02478: SequenceCallModule.NewExecutionTypeMask

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-newexecutiontypemask.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-newexecutiontypemask.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.NewExecutionTypeMask Data Type Long Purpose Specifies settings to apply when calling a subsequence in a new execution. The Sequence Adapter combines this value with the value to which the SequenceCallModule.NewExecutionTypeMaskExpr property evaluates when you call a subsequ

### SequenceCallModule.NewExecutionTypeMask

#### Syntax

[SequenceCallModule](sequencecallmodule.html).NewExecutionTypeMask

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies settings to apply when calling a subsequence in a new execution. The Sequence Adapter combines this value with the value to which the
 [SequenceCallModule.NewExecutionTypeMaskExpr](sequencecallmodule-newexecutiontypemaskexpr.html)
 property evaluates when you call a subsequence in a new execution.

#### See Also

[ExecutionTypeMask](executiontypemask.html)

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[SequenceCallModule.NewExecutionTypeMaskExpr](sequencecallmodule-newexecutiontypemaskexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-newexecutiontypemaskexpr.html language=enus -->
## TOPIC 02479: SequenceCallModule.NewExecutionTypeMaskExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-newexecutiontypemaskexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-newexecutiontypemaskexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.NewExecutionTypeMaskExpr Data Type String Purpose Specifies an expression that returns a numeric value to combine with the SequenceCallModule.NewExecutionTypeMask property value when calling a subsequence in a new execution. See Also ExecutionTypeMask SequenceCallModule.Mul

### SequenceCallModule.NewExecutionTypeMaskExpr

#### Syntax

[SequenceCallModule](sequencecallmodule.html).NewExecutionTypeMaskExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression that returns a numeric value to combine with the
 [SequenceCallModule.NewExecutionTypeMask](sequencecallmodule-newexecutiontypemask.html)
 property value when calling a subsequence in a new execution.

#### See Also

[ExecutionTypeMask](executiontypemask.html)

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[SequenceCallModule.NewExecutionTypeMask](sequencecallmodule-newexecutiontypemask.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-newexecutionwaitforcomplet.html language=enus -->
## TOPIC 02480: SequenceCallModule.NewExecutionWaitForCompletion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-newexecutionwaitforcomplet.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-newexecutionwaitforcomplet.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.NewExecutionWaitForCompletion Data Type SeqCallWaitForExecOptions Use the following constants with this data type: SeqCallWait_BeforeNextStep –(Value: 1) The calling sequence waits for the execution to complete before it executes another step. SeqCallWait_DoNotWait –(Value:

### SequenceCallModule.NewExecutionWaitForCompletion

#### Syntax

[SequenceCallModule](sequencecallmodule.html).NewExecutionWaitForCompletion

#### Data Type

[SeqCallWaitForExecOptions](seqcallwaitforexecoptions.html)

Use the following constants with this data type:

- SeqCallWait_BeforeNextStep 
 –(Value: 1) The calling sequence waits for the execution to complete before it executes another step.
- SeqCallWait_DoNotWait 
 –(Value: 0) The calling sequence does not wait for the execution to complete.
- SeqCallWait_EndOfSequence 
 –(Value: 2) The calling sequence waits for the execution to complete before the calling sequence returns.

#### Purpose

Specifies whether and when to wait for the execution to complete after calling a subsequence in a new execution.

#### See Also

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-newthreadoptions.html language=enus -->
## TOPIC 02481: SequenceCallModule.NewThreadOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-newthreadoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-newthreadoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.NewThreadOptions Data Type Long Purpose Specifies the options to apply when calling a subsequence in a separate thread. See Also SeqCallNewThreadOptions SequenceCallModule.MultithreadingAndRemoteExecOption

### SequenceCallModule.NewThreadOptions

#### Syntax

[SequenceCallModule](sequencecallmodule.html).NewThreadOptions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the options to apply when calling a subsequence in a separate thread.

#### See Also

[SeqCallNewThreadOptions](seqcallnewthreadoptions.html)

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-parameterprototype.html language=enus -->
## TOPIC 02482: SequenceCallModule.ParameterPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-parameterprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-parameterprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.ParameterPrototype Data Type PropertyObject The parameters container. Purpose Returns a copy of the parameters container from the sequence the module calls. See Also SequenceCallModule.Parameters PropertyObject

### SequenceCallModule.ParameterPrototype

#### Syntax

[SequenceCallModule](sequencecallmodule.html).ParameterPrototype

#### Data Type

[PropertyObject](propertyobject.html)

The parameters container.

#### Purpose

Returns a copy of the parameters container from the sequence the module calls.

#### See Also

[SequenceCallModule.Parameters](sequencecallmodule-parameters.html)

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-parameters.html language=enus -->
## TOPIC 02483: SequenceCallModule.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.Parameters Data Type SequenceCallParameters The collection of parameters. Purpose Returns the SequenceCallParameters collection, which contains a list of the current parameters used as inputs and outputs of the corresponding module. Remarks Use the Module.LoadPrototype meth

### SequenceCallModule.Parameters

#### Syntax

[SequenceCallModule](sequencecallmodule.html).Parameters

#### Data Type

[SequenceCallParameters](sequencecallparameters.html)

The collection of parameters.

#### Purpose

Returns the SequenceCallParameters collection, which contains a list of the current parameters used as inputs and outputs of the corresponding module.

#### Remarks

Use the
 [Module.LoadPrototype](module-loadprototype.html)
 method to load the parameter information from the sequence file and sequence of the module or a specific sequence file and sequence.

#### See Also

[Module.LoadPrototype](module-loadprototype.html)

[SequenceCallModule.ParameterPrototype](sequencecallmodule-parameterprototype.html)

[SequenceCallParameters](sequencecallparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-remotehost.html language=enus -->
## TOPIC 02484: SequenceCallModule.RemoteHost

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-remotehost.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-remotehost.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.RemoteHost Data Type String Purpose Specifies the name of the remote host when calling a subsequence on a remote computer. Remarks If the SequenceCallModule.SpecifyHostByExpression property is True , the value of this property must be in the form of an expression. The Seque

### SequenceCallModule.RemoteHost

#### Syntax

[SequenceCallModule](sequencecallmodule.html).RemoteHost

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the remote host when calling a subsequence on a remote computer.

#### Remarks

If the
 [SequenceCallModule.SpecifyHostByExpression](sequencecallmodule-specifyhostbyexpression.html)
 property is
 True
 , the value of this property must be in the form of an expression.

The Sequence Adapter ignores this property unless you set the
 [SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)
 property equal to
 SeqCallMultiThread_Remote
 .

#### See Also

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[SequenceCallModule.SpecifyHostByExpression](sequencecallmodule-specifyhostbyexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-sequencecomment.html language=enus -->
## TOPIC 02485: SequenceCallModule.SequenceComment

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-sequencecomment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-sequencecomment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.SequenceComment Data Type String Purpose Specifies the comment associated with the sequence that the step calls.

### SequenceCallModule.SequenceComment

#### Syntax

[SequenceCallModule](sequencecallmodule.html).SequenceComment

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the comment associated with the sequence that the step calls.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-sequencefilepath.html language=enus -->
## TOPIC 02486: SequenceCallModule.SequenceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-sequencefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-sequencefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.SequenceFilePath Data Type String Purpose Specifies the path of the sequence file that contains the sequence the module calls. Remarks You specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand search directory paths . You mu

### SequenceCallModule.SequenceFilePath

#### Syntax

[SequenceCallModule](sequencecallmodule.html).SequenceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path of the sequence file that contains the sequence the module calls.

#### Remarks

You specify an absolute or relative pathname for the file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

You must specify an expression for the file pathname if the
 [SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)
 property is
 True
 . The expression must evaluate to an absolute or relative pathname for the file or a reference to be a
 [SequenceFile](sequencefile.html)
 object.

If you set the
 [SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)
 property to
 True
 , TestStand ignores the value of this property.

#### See Also

[SequenceFile](sequencefile.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

[SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-sequencename.html language=enus -->
## TOPIC 02487: SequenceCallModule.SequenceName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-sequencename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-sequencename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.SequenceName Data Type String Purpose Specifies the name of the sequence the module calls. Remarks You must specify an expression for the file pathname if the SequenceCallModule.SpecifyByExpression property is True . See Also SequenceCallModule.SequenceFilePath SequenceCall

### SequenceCallModule.SequenceName

#### Syntax

[SequenceCallModule](sequencecallmodule.html).SequenceName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the sequence the module calls.

#### Remarks

You must specify an expression for the file pathname if the
 [SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)
 property is
 True
 .

#### See Also

[SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

[SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-specifybyexpression.html language=enus -->
## TOPIC 02488: SequenceCallModule.SpecifyByExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-specifybyexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-specifybyexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.SpecifyByExpression Data Type Boolean Purpose Specifies that the SequenceCallModule.SequenceFilePath , SequenceCallModule.SequenceName , and SequenceCallModule.NewExecutionModelPath properties contain expressions the Sequence Adapter evaluates at run time to determine the a

### SequenceCallModule.SpecifyByExpression

#### Syntax

[SequenceCallModule](sequencecallmodule.html).SpecifyByExpression

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the
 [SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)
 ,
 [SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)
 , and
 [SequenceCallModule.NewExecutionModelPath](sequencecallmodule-newexecutionmodelpath.html)
 properties contain expressions the Sequence Adapter evaluates at run time to determine the actual sequence file path, sequence name, and model file path.

#### See Also

[SequenceCallModule.NewExecutionModelPath](sequencecallmodule-newexecutionmodelpath.html)

[SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

[SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-specifyhostbyexpression.html language=enus -->
## TOPIC 02489: SequenceCallModule.SpecifyHostByExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-specifyhostbyexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-specifyhostbyexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.SpecifyHostByExpression Data Type Boolean Purpose Set this property to True to specify that the value of the SequenceCallModule.RemoteHost property is in the form of an expression. Remarks This property affects the behavior of the Module.LoadPrototype method. See Also Modul

### SequenceCallModule.SpecifyHostByExpression

#### Syntax

[SequenceCallModule](sequencecallmodule.html).SpecifyHostByExpression

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Set this property to
 True
 to specify that the value of the
 [SequenceCallModule.RemoteHost](sequencecallmodule-remotehost.html)
 property is in the form of an expression.

#### Remarks

This property affects the behavior of the
 [Module.LoadPrototype](module-loadprototype.html)
 method.

#### See Also

[Module.LoadPrototype](module-loadprototype.html)

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[SequenceCallModule.RemoteHost](sequencecallmodule-remotehost.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-storeactivexreferenceexpr.html language=enus -->
## TOPIC 02490: SequenceCallModule.StoreActiveXReferenceExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-storeactivexreferenceexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-storeactivexreferenceexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.StoreActiveXReferenceExpr Data Type String Purpose Specifies an ActiveX reference variable in which to store a reference to the new Thread object. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in the Wait step to wait f

### SequenceCallModule.StoreActiveXReferenceExpr

#### Syntax

[SequenceCallModule](sequencecallmodule.html).StoreActiveXReferenceExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an ActiveX reference variable in which to store a reference to the new Thread object. You can use this reference in subsequent calls to the TestStand API. You can also use this reference in the Wait step to wait for the thread to complete.

#### Remarks

This property can be left blank. The Sequence Adapter ignores this property unless you set the
 [SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)
 property to
 SeqCallMultiThread_NewThread
 or
 SeqCallMultiThread_NewExecution
 .

#### See Also

[SequenceCallModule.MultithreadingAndRemoteExecOption](sequencecallmodule-multithreadingandremoteexe.html)

[SequenceCallModule.NewExecutionWaitForCompletion](sequencecallmodule-newexecutionwaitforcomplet.html)

[SequenceCallModule.NewThreadOptions](sequencecallmodule-newthreadoptions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-tracesetting.html language=enus -->
## TOPIC 02491: SequenceCallModule.TraceSetting

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-tracesetting.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-tracesetting.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.TraceSetting Data Type SeqCallTraceSettings Use the following constants with this data type: SeqCallTrace_Disable –(Value: 3) Specifies to disable tracing for calls to the subsequence and restores the original tracing state when the subsequence returns. However, if you enab

### SequenceCallModule.TraceSetting

#### Syntax

[SequenceCallModule](sequencecallmodule.html).TraceSetting

#### Data Type

[SeqCallTraceSettings](seqcalltracesettings.html)

Use the following constants with this data type:

- SeqCallTrace_Disable 
 –(Value: 3) Specifies to disable tracing for calls to the subsequence and restores the original tracing state when the subsequence returns. However, if you enable the Allow Tracing into Sequence Calls Marked with Tracing "Disabled" option on the
 Execution tab 
 of the
 Station Options 
 dialog box, TestStand ignores this setting and does not alter the tracing state.
- SeqCallTrace_Enable 
 –(Value: 2) Specifies to enable tracing for calls to the subsequence and restores the original tracing state when the subsequence returns.
- SeqCallTrace_UseCurrent 
 –(Value: 1) Specifies to maintain the current tracing state when calling the subsequence. This is the default value for the
 SequenceCallModule.TraceSetting 
 property. Usually, only process model files use other values for this option.
- SeqCallTrace_UseExecutionSetting 
 –(Value: 4) Specifies to enable the tracing state unless the execution was created with tracing disabled. Typically, a process model uses this setting to control the tracing state when the model calls the
 MainSequence 
 in the client sequence file.

#### Purpose

Specifies to enable or disable tracing for calls to the subsequence.

#### Remarks

This property corresponds to the Sequence Call Trace Setting control on the
 [Run Options tab](../tsref/run-options-tab-step-properties-dialog-box.html)
 of the
 [Step Properties](../tsref/step-properties-dialog-box.html)
 dialog box.

#### See Also

[Execution tab](../tsref/execution-tab-station-options-dialog-box.html)

[Run Options tab](../tsref/run-options-tab-step-properties-dialog-box.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

[SequenceCallModule.TraceSetting](sequencecallmodule-tracesetting.html)

[StationOptions.TracingEnabled](stationoptions-tracingenabled.html)

[Step Properties dialog box](../tsref/step-properties-dialog-box.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-usecurrentfile.html language=enus -->
## TOPIC 02492: SequenceCallModule.UseCurrentFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-usecurrentfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-usecurrentfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.UseCurrentFile Data Type Boolean Purpose Specifies that the sequence file of the sequence call contains the sequence the module calls. If you set this property to True , TestStand ignores the value of the SequenceCallModule.SequenceFilePath property. See Also SequenceCallMo

### SequenceCallModule.UseCurrentFile

#### Syntax

[SequenceCallModule](sequencecallmodule.html).UseCurrentFile

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that the sequence file of the sequence call contains the sequence the module calls. If you set this property to
 True
 , TestStand ignores the value of the
 [SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)
 property.

#### See Also

[SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule-usesequenceparameterprotot.html language=enus -->
## TOPIC 02493: SequenceCallModule.UseSequenceParameterPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule-usesequenceparameterprotot.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule-usesequenceparameterprotot.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallModule.UseSequenceParameterPrototype Data Type Boolean Purpose This property affects the behavior of the Module.LoadPrototype method. When this property is True , Module.LoadPrototype loads the parameters of the module from the sequence the SequenceCallModule.UseCurrentFile , Sequ

### SequenceCallModule.UseSequenceParameterPrototype

#### Syntax

[SequenceCallModule](sequencecallmodule.html).UseSequenceParameterPrototype

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

This property affects the behavior of the
 [Module.LoadPrototype](module-loadprototype.html)
 method. When this property is
 True
 ,
 Module.LoadPrototype
 loads the parameters of the module from the sequence the
 [SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)
 ,
 [SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)
 , and
 [SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)
 properties specify.

#### Remarks

This property is ignored when the
 [SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)
 property is
 True
 .

#### See Also

[Module.LoadPrototype](module-loadprototype.html)

[SequenceCallModule.ParameterPrototype](sequencecallmodule-parameterprototype.html)

[SequenceCallModule.Parameters](sequencecallmodule-parameters.html)

[SequenceCallModule.SequenceFilePath](sequencecallmodule-sequencefilepath.html)

[SequenceCallModule.SequenceName](sequencecallmodule-sequencename.html)

[SequenceCallModule.SpecifyByExpression](sequencecallmodule-specifybyexpression.html)

[SequenceCallModule.UseCurrentFile](sequencecallmodule-usecurrentfile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallmodule.html language=enus -->
## TOPIC 02494: SequenceCallModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the SequenceCallModule class to specify and obtain Sequence Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a SequenceCallModule object. To access the properties and methods of a speci

### SequenceCallModule

Use objects from the SequenceCallModule class to specify and obtain Sequence Adapter-specific information about the code module that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to a SequenceCallModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the Module class, use the AsModule method to obtain an object.

You can use the
 
 [Module.LoadPrototype](module-loadprototype.html)
 method to load the prototype for the module that the step specifies.

#### Properties

| CPUAffinityForNewThreadOption |
| --- |
| CustomCPUAffinityForNewThread |
| IgnoreTermination |
| InitiallySuspended |
| MultithreadingAndRemoteExecOption |
| NewExecutionBreakOnEntryExpr |
| NewExecutionModelOption |
| NewExecutionModelPath |
| NewExecutionTypeMask |
| NewExecutionTypeMaskExpr |
| NewExecutionWaitForCompletion |
| NewThreadOptions |
| ParameterPrototype (Read Only) |
| Parameters (Read Only) |
| RemoteHost |
| SequenceComment (Read Only) |
| SequenceFilePath |
| SequenceName |
| SpecifyByExpression |
| SpecifyHostByExpression |
| StoreActiveXReferenceExpr |
| TraceSetting |
| UseCurrentFile |
| UseSequenceParameterPrototype |

#### Methods

| AsModule |
| --- |
| LoadPrototypeFromSequence |

#### See Also

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-argumentobject.html language=enus -->
## TOPIC 02495: SequenceCallParameter.ArgumentObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-argumentobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-argumentobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.ArgumentObject Data Type PropertyObject Purpose Returns the underlying PropertyObject that represents the SequenceCallParameter object. Remarks Use the PropertyObject to access the attributes associated with the parameter or to edit, add, or remove custom properties of t

### SequenceCallParameter.ArgumentObject

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).ArgumentObject

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying
 [PropertyObject](propertyobject.html)
 that represents the
 [SequenceCallParameter](sequencecallparameter.html)
 object.

#### Remarks

Use the
 PropertyObject
 to access the attributes associated with the parameter or to edit, add, or remove custom properties of the parameter.

#### See Also

[PropertyObject](propertyobject.html)

[PropertyObject.Attributes](propertyobject-attributes.html)

[SequenceCallParameter](sequencecallparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-aspropertyobject.html language=enus -->
## TOPIC 02496: SequenceCallParameter.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.AsPropertyObject Return Value PropertyObject Purpose This method is obsolete. Use the properties and methods in the SequenceCallParameter class to access the contents of the object. Remarks Returns the underlying PropertyObject that represents the SequenceCallParameter o

### SequenceCallParameter.AsPropertyObject

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Note

SequenceCallParameter

#### Remarks

Returns the underlying PropertyObject that represents the SequenceCallParameter object. Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

[SequenceCallParameter](sequencecallparameter.html)

Parent topic:

Obsolete SequenceCallParameter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-comment.html language=enus -->
## TOPIC 02497: SequenceCallParameter.Comment

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-comment.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-comment.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.Comment Data Type String Purpose Specifies the comment associated with the parameter for the sequence that the step calls.

### SequenceCallParameter.Comment

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).Comment

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the comment associated with the parameter for the sequence that the step calls.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-name.html language=enus -->
## TOPIC 02498: SequenceCallParameter.Name

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-name.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-name.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.Name Data Type String Purpose Returns the name of the parameter. See Also SequenceCallParameter.Type

### SequenceCallParameter.Name

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).Name

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter.

#### See Also

[SequenceCallParameter.Type](sequencecallparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-passbyreference.html language=enus -->
## TOPIC 02499: SequenceCallParameter.PassByReference

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-passbyreference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-passbyreference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.PassByReference Data Type Boolean Purpose Returns a value that indicates whether the parameter is passed by reference or passed by value. See Also SequenceCallParameter.Type

### SequenceCallParameter.PassByReference

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).PassByReference

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the parameter is passed by reference or passed by value.

#### See Also

[SequenceCallParameter.Type](sequencecallparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/sequencecallparameter-propertyobjecttype.html language=enus -->
## TOPIC 02500: SequenceCallParameter.PropertyObjectType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/sequencecallparameter-propertyobjecttype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/sequencecallparameter-propertyobjecttype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax SequenceCallParameter.PropertyObjectType Data Type PropertyObjectType Purpose Returns an object that provides type information about the parameter. See Also PropertyObjectType

### SequenceCallParameter.PropertyObjectType

#### Syntax

[SequenceCallParameter](sequencecallparameter.html).PropertyObjectType

#### Data Type

[PropertyObjectType](propertyobjecttype.html)

#### Purpose

Returns an object that provides type information about the parameter.

#### See Also

[PropertyObjectType](propertyobjecttype.html)

Parent topic:

Properties
