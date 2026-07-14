# NI DOCUMENT BUNDLE: teststand-api-reference

<!--NI_BUNDLE_CHUNK bundle=teststand-api-reference start=501 end=750 -->
<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllargument.html language=enus -->
## TOPIC 00501: DllArgument

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllargument.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllargument.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DllArgument class to set the argument value to pass to a DLL module function using the DllModule.Execute method. Properties ImaginaryPartValue Value See Also DllArguments DllModule.Execute

### DllArgument

Use objects from the
 DllArgument
 class to set the argument value to pass to a DLL module function using the
 [DllModule.Execute](dllmodule-execute.html)
 method.

#### Properties

| ImaginaryPartValue |
| --- |
| Value |

#### See Also

[DllArguments](dllarguments.html)

[DllModule.Execute](dllmodule-execute.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllarguments-count.html language=enus -->
## TOPIC 00502: DllArguments.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllarguments-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllarguments-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllArguments.Count Data Type Long Purpose Returns the number of items in the collection.

### DllArguments.Count

#### Syntax

[DllArguments](dllarguments.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllarguments-item.html language=enus -->
## TOPIC 00503: DllArguments.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllarguments-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllarguments-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllArguments.Item( index) Data Type DllArgument Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the DllArguments collection corresponds

### DllArguments.Item

#### Syntax

[DllArguments](dllarguments.html).Item( index)

#### Data Type

[DllArgument](dllargument.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve. An argument at a specific index in the
 [DllArguments](dllarguments.html)
 collection corresponds to the parameter at the same index in the
 [DllParameters](dllparameters.html)
 collection that you used to create the
 DllArguments
 collection.

#### See Also

[DllArguments](dllarguments.html)

[DllParameters](dllparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllarguments.html language=enus -->
## TOPIC 00504: DllArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DllArguments class to pass specific argument values to a DLL module function using the DllModule.Execute method. Use the DllParameters.NewArguments method to create a new arguments collection. Properties Count (Read Only) Item (Read Only) See Also DllModule.Execute DllParameters

### DllArguments

Use objects from the
 DllArguments
 class to pass specific argument values to a DLL module function using the
 [DllModule.Execute](dllmodule-execute.html)
 method. Use the
 [DllParameters.NewArguments](dllparameters-newarguments.html)
 method to create a new arguments collection.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[DllModule.Execute](dllmodule-execute.html)

[DllParameters.NewArguments](dllparameters-newarguments.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllcodecreationtargets.html language=enus -->
## TOPIC 00505: DllCodeCreationTargets

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllcodecreationtargets.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllcodecreationtargets.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants for the DllModule.CodeCreationTarget property. DllCodeCreationTarget_TextFile –(Value: 0) Specifies that the C/C++ DLL Module creates and edits code using the default application Microsoft Windows associates with the file extension of the source file. DllCodeCreationTarget_Visual

### DllCodeCreationTargets

Use these constants for the
 [DllModule.CodeCreationTarget](dllmodule-codecreationtarget.html)
 property.

- DllCodeCreationTarget_TextFile 
 –(Value: 0) Specifies that the C/C++ DLL Module creates and edits code using the default application Microsoft Windows associates with the file extension of the source file.
- DllCodeCreationTarget_VisualStudio 
 –(Value: 1) Specifies the C/C++ DLL Module creates and edits code in Microsoft Visual Studio.

#### See Also

[DllModule.CodeCreationTarget](dllmodule-codecreationtarget.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction-displayname.html language=enus -->
## TOPIC 00506: DllFunction.DisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction-displayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction-displayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunction.DisplayName Data Type String Purpose Returns the name of a function in a DLL. Remarks There can be up to three different names for a function: DisplayName , UniqueDisplayName and SymbolName . The DisplayName is the simple function name. The UniqueDisplayName is a name that contain

### DllFunction.DisplayName

#### Syntax

[DllFunction](dllfunction.html).DisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of a function in a DLL.

#### Remarks

There can be up to three different names for a function:
 DisplayName
 ,
 [UniqueDisplayName](dllfunction-uniquedisplayname.html)
 and
 [SymbolName](dllfunction-symbolname.html)
 .

The
 DisplayName
 is the simple function name. The
 UniqueDisplayName
 is a name that contains parameter type information to distinguish different function overloads in the DLL. If no overloads for a function exist,
 DisplayName
 is the same as
 UniqueDisplayName
 . The
 SymbolName
 is the name exported from the DLL. For C++ functions, the
 SymbolName
 contains decorations that encode parameter type information.
 SymbolName
 is also a unique name, but it is not intended to be displayed.

#### See Also

[DllFunction.SymbolName](dllfunction-symbolname.html)

[DllFunction.UniqueDisplayName](dllfunction-uniquedisplayname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction-hasparameterinformation.html language=enus -->
## TOPIC 00507: DllFunction.HasParameterInformation

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction-hasparameterinformation.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction-hasparameterinformation.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunction.HasParameterInformation Data Type Boolean Purpose Returns a value that indicates whether TestStand obtained type information for the parameters of the function in the DLL. Remarks TestStand obtains type information for parameters from the DLL or from a type library. See Also DllFu

### DllFunction.HasParameterInformation

#### Syntax

[DllFunction](dllfunction.html).HasParameterInformation

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether TestStand obtained type information for the parameters of the function in the DLL.

#### Remarks

TestStand obtains type information for parameters from the DLL or from a type library.

#### See Also

[DllFunction.ParameterTypeWarnings](dllfunction-parametertypewarnings.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction-helpcontext.html language=enus -->
## TOPIC 00508: DllFunction.HelpContext

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction-helpcontext.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction-helpcontext.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunction.HelpContext Data Type Long Purpose Returns a tag for the help topic for the function in the help file the DllFunction.HelpFilePath property specifies. Remarks You can associate a help file with a function in a type library. See Also DllFunction.HelpFilePath

### DllFunction.HelpContext

#### Syntax

[DllFunction](dllfunction.html).HelpContext

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a tag for the help topic for the function in the help file the
 [DllFunction.HelpFilePath](dllfunction-helpfilepath.html)
 property specifies.

#### Remarks

You can associate a help file with a function in a type library.

#### See Also

[DllFunction.HelpFilePath](dllfunction-helpfilepath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction-helpfilepath.html language=enus -->
## TOPIC 00509: DllFunction.HelpFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction-helpfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction-helpfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunction.HelpFilePath Data Type String Purpose Returns the absolute path of the help file associated with the function. Remarks You can associate a help file with a function in a type library. See Also DllFunction.HelpContext

### DllFunction.HelpFilePath

#### Syntax

[DllFunction](dllfunction.html).HelpFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the absolute path of the help file associated with the function.

#### Remarks

You can associate a help file with a function in a type library.

#### See Also

[DllFunction.HelpContext](dllfunction-helpcontext.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction-parametertypewarnings.html language=enus -->
## TOPIC 00510: DllFunction.ParameterTypeWarnings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction-parametertypewarnings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction-parametertypewarnings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunction.ParameterTypeWarnings Data Type String Purpose Returns a warning message if TestStand could not obtain type information for the parameters from the type library associated with the DLL. Remarks TestStand reads a type library to obtain type information for parameters. If TestStand

### DllFunction.ParameterTypeWarnings

#### Syntax

[DllFunction](dllfunction.html).ParameterTypeWarnings

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a warning message if TestStand could not obtain type information for the parameters from the type library associated with the DLL.

#### Remarks

TestStand reads a type library to obtain type information for parameters. If TestStand cannot read the type library for some reason, it sets this property to a message that explains what failed.

#### See Also

[DllFunction.HasParameterInformation](dllfunction-hasparameterinformation.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction-symbolname.html language=enus -->
## TOPIC 00511: DllFunction.SymbolName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction-symbolname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction-symbolname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunction.SymbolName Data Type String Purpose Returns the symbol name of a function in a DLL. Remarks There can be up to three different names for a function: DisplayName , UniqueDisplayName and SymbolName . The DisplayName is the simple function name. The UniqueDisplayName is a name that c

### DllFunction.SymbolName

#### Syntax

[DllFunction](dllfunction.html).SymbolName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the symbol name of a function in a DLL.

#### Remarks

There can be up to three different names for a function:
 [DisplayName](dllfunction-displayname.html)
 ,
 [UniqueDisplayName](dllfunction-uniquedisplayname.html)
 and
 SymbolName
 .

The
 DisplayName
 is the simple function name. The
 UniqueDisplayName
 is a name that contains parameter type information to distinguish different function overloads in the DLL. If no overloads for a function exist,
 DisplayName
 is the same as
 UniqueDisplayName
 . The
 SymbolName
 is the name exported from the DLL. For C++ functions, the
 SymbolName
 contains decorations that encode parameter type information.
 SymbolName
 is also a unique name, but it is not intended to be displayed.

#### See Also

[DllFunction.DisplayName](dllfunction-displayname.html)

[DllFunction.SymbolName](dllfunction-symbolname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction-uniquedisplayname.html language=enus -->
## TOPIC 00512: DllFunction.UniqueDisplayName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction-uniquedisplayname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction-uniquedisplayname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunction.UniqueDisplayName Data Type String Purpose Returns a unique name for a function in a DLL. Remarks There can be up to three different names for a function: DisplayName , UniqueDisplayName and SymbolName . The DisplayName is the simple function name. The UniqueDisplayName is a name

### DllFunction.UniqueDisplayName

#### Syntax

[DllFunction](dllfunction.html).UniqueDisplayName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a unique name for a function in a DLL.

#### Remarks

There can be up to three different names for a function:
 [DisplayName](dllfunction-displayname.html)
 ,
 UniqueDisplayName
 and
 [SymbolName](dllfunction-symbolname.html)
 .

The
 DisplayName
 is the simple function name. The
 UniqueDisplayName
 is a name that contains parameter type information to distinguish different function overloads in the DLL. If no overloads exist for a function,
 DisplayName
 is the same as
 UniqueDisplayName
 . The
 SymbolName
 is the name exported from the DLL. For C++ functions, the
 SymbolName
 contains decorations that encode parameter type information.
 SymbolName
 is also a unique name, but it is not intended to be displayed.

#### See Also

[DllFunction.DisplayName](dllfunction-displayname.html)

[DllFunction.SymbolName](dllfunction-symbolname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunction.html language=enus -->
## TOPIC 00513: DllFunction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DllFunction class to obtain information about a function exported from a DLL. Use the CommonCAdapter.GetDllFunctions method to obtain a collection of functions from a DLL. Properties DisplayName (Read Only) HasParameterInformation (Read Only) HelpContext (Read Only) HelpFilePath

### DllFunction

Use objects from the DllFunction class to obtain information about a function exported from a DLL. Use the
 [CommonCAdapter.GetDllFunctions](commoncadapter-getdllfunctions.html)
 method to obtain a collection of functions from a DLL.

#### Properties

| DisplayName (Read Only) |
| --- |
| HasParameterInformation (Read Only) |
| HelpContext (Read Only) |
| HelpFilePath (Read Only) |
| ParameterTypeWarnings (Read Only) |
| SymbolName (Read Only) |
| UniqueDisplayName (Read Only) |

#### See Also

[CommonCAdapter.GetDllFunctions](commoncadapter-getdllfunctions.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunctions-count.html language=enus -->
## TOPIC 00514: DllFunctions.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunctions-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunctions-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunctions.Count Data Type Long Purpose Returns the number of items in the collection. See Also DllFunctions.Item

### DllFunctions.Count

#### Syntax

[DllFunctions](dllfunctions.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[DllFunctions.Item](dllfunctions-item.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunctions-item.html language=enus -->
## TOPIC 00515: DllFunctions.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunctions-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunctions-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllFunctions.Item( index) Data Type DllFunction Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index. See Also DllFunction DllFunctions.Count

### DllFunctions.Item

#### Syntax

[DllFunctions](dllfunctions.html).Item( index)

#### Data Type

[DllFunction](dllfunction.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index.

#### See Also

[DllFunction](dllfunction.html)

[DllFunctions.Count](dllfunctions-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllfunctions.html language=enus -->
## TOPIC 00516: DllFunctions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllfunctions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllfunctions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: This class is a collection of DllFunction objects. Each item in the collection represents a function exported from a DLL that can be called from TestStand using the LabWindows/CVI or C/C++ DLL adapter. Use the CommonCAdapter.GetDllFunctions method to obtain a collection of functions from a DLL. Prop

### DllFunctions

This class is a collection of DllFunction objects. Each item in the collection represents a function exported from a DLL that can be called from TestStand using the LabWindows/CVI or C/C++ DLL adapter.

Use the
 [CommonCAdapter.GetDllFunctions](commoncadapter-getdllfunctions.html)
 method to obtain a collection of functions from a DLL.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[CommonCAdapter.GetDllFunctions](commoncadapter-getdllfunctions.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllinfotypes.html language=enus -->
## TOPIC 00517: DllInfoTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllinfotypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllinfotypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type info for the DLL. DllInfoType_Enumeration –(Value: 1) DllInfoType_None –(Value: 0) DllInfoType_Struct –(Value: 2)

### DllInfoTypes

Specifies the type info for the DLL.

- DllInfoType_Enumeration 
 –(Value: 1)
- DllInfoType_None 
 –(Value: 0)
- DllInfoType_Struct 
 –(Value: 2)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllmodule-ascommoncmodule.html language=enus -->
## TOPIC 00518: DllModule.AsCommonCModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllmodule-ascommoncmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllmodule-ascommoncmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllModule.AsCommonCModule Return Value CommonCModule Purpose Returns the underlying CommonCModule object that represents the DllModule. Remarks Use the CommonCModule object to access properties and methods common to all modules derived from this class. See Also CommonCModule Module

### DllModule.AsCommonCModule

#### Syntax

[DllModule](dllmodule.html).AsCommonCModule

#### Return Value

[CommonCModule](commoncmodule.html)

#### Purpose

Returns the underlying CommonCModule object that represents the DllModule.

#### Remarks

Use the CommonCModule object to access properties and methods common to all modules derived from this class.

#### See Also

[CommonCModule](commoncmodule.html)

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllmodule-codecreationtarget.html language=enus -->
## TOPIC 00519: DllModule.CodeCreationTarget

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllmodule-codecreationtarget.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllmodule-codecreationtarget.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllModule.CodeCreationTarget Data Type DllCodeCreationTargets Use the following constants with this data type: DllCodeCreationTarget_TextFile –(Value: 0) Specifies that the C/C++ DLL Module creates and edits code using the default application Microsoft Windows associates with the file extensi

### DllModule.CodeCreationTarget

#### Syntax

[DllModule](dllmodule.html).CodeCreationTarget

#### Data Type

[DllCodeCreationTargets](dllcodecreationtargets.html)

Use the following constants with this data type:

- DllCodeCreationTarget_TextFile 
 –(Value: 0) Specifies that the C/C++ DLL Module creates and edits code using the default application Microsoft Windows associates with the file extension of the source file.
- DllCodeCreationTarget_VisualStudio 
 –(Value: 1) Specifies the C/C++ DLL Module creates and edits code in Microsoft Visual Studio.

#### Purpose

Specifies where the module creates and edits code.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllmodule-execute.html language=enus -->
## TOPIC 00520: DllModule.Execute

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllmodule-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllmodule-execute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllModule.Execute( sequenceContextParam, argumentsParam) Purpose Use this method to call a DLL module function directly without using a step, sequence, or execution. Remarks When you call a DLL module function using this method you can evaluate the parameter expressions to determine the argum

### DllModule.Execute

#### Syntax

[DllModule](dllmodule.html).Execute( sequenceContextParam, argumentsParam)

#### Purpose

Use this method to call a DLL module function directly without using a step, sequence, or execution.

#### Remarks

When you call a DLL module function using this method you can evaluate the parameter expressions to determine the argument values or specify the argument values directly using a
 [DllArguments](dllarguments.html)
 collection.

To use the parameter value expressions, pass a valid
 [SequenceContext](sequencecontext.html)
 object to the
 sequenceContextParam
 to use to evaluate the
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 expressions.

To pass specific argument values, use the
 [DllParameters.NewArguments](dllparameters-newarguments.html)
 method to create a collection of
 [DllArgument](dllargument.html)
 objects and set the
 [DllArgument.Value](dllargument-value.html)
 property on each item in the collection.

#### Parameters

sequenceContextParam
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 object that this method uses to evaluate each of the
 CommonCParameter.ValueExpr
 expressions in the module parameters. Pass
 NULL
 for this parameter if you pass a
 DllArguments
 collection to the
 argumentsParam
 parameter.

argumentsParam
 As
 [DllArguments](dllarguments.html)

[In] Specifies the argument collection that contains the argument values to pass to the function. Pass
 NULL
 for this parameter to pass the values obtained from evaluating each of the
 CommonCParameter.ValueExpr
 expressions in the module parameters.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[DllArgument.Value](dllargument-value.html)

[DllArgument](dllargument.html)

[DllArguments](dllarguments.html)

[DllParameters.NewArguments](dllparameters-newarguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllmodule-parameters.html language=enus -->
## TOPIC 00521: DllModule.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllmodule-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllmodule-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllModule.Parameters Data Type DllParameters Purpose Returns the DllParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module. Remarks If you need to add or modify a parameter, you must first obtain the DllParameters collection

### DllModule.Parameters

#### Syntax

[DllModule](dllmodule.html).Parameters

#### Data Type

[DllParameters](dllparameters.html)

#### Purpose

Returns the DllParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module.

#### Remarks

If you need to add or modify a parameter, you must first obtain the DllParameters collection.

#### See Also

[DllParameters](dllparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllmodule.html language=enus -->
## TOPIC 00522: DllModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DllModule class to specify and obtain C/C++ DLL Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a DllModule object. To access the properties and methods of a specific module class,

### DllModule

Use objects from the DllModule class to specify and obtain C/C++ DLL Adapter-specific information about the code module that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to a DllModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the CommonCModule class, use the
 [DllModule.AsCommonCModule](dllmodule-ascommoncmodule.html)
 method to obtain an object.

You can use the
 
 [Module.LoadPrototype](module-loadprototype.html)
 method to load the prototype for the module the step specifies.

#### Properties

| CodeCreationTarget |
| --- |
| Parameters (Read Only) |

#### Methods

| AsCommonCModule |
| --- |
| Execute |

#### See Also

[CommonCModule](commoncmodule.html)

[Module](module.html)

[Module.LoadPrototype](module-loadprototype.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameter-ascommoncparameter.html language=enus -->
## TOPIC 00523: DllParameter.AsCommonCParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameter-ascommoncparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameter-ascommoncparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameter.AsCommonCParameter Return Value CommonCParameter Purpose Returns the underlying CommonCParameter that represents the DllParameter. Remarks Use the CommonCParameter object to access properties and methods common to all parameters derived from this class. See Also CommonCParameter

### DllParameter.AsCommonCParameter

#### Syntax

[DllParameter](dllparameter.html).AsCommonCParameter

#### Return Value

[CommonCParameter](commoncparameter.html)

#### Purpose

Returns the underlying CommonCParameter that represents the DllParameter.

#### Remarks

Use the CommonCParameter object to access properties and methods common to all parameters derived from this class.

#### See Also

[CommonCParameter](commoncparameter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameter-category.html language=enus -->
## TOPIC 00524: DllParameter.Category

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameter-category.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameter-category.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameter.Category Data Type DllParameterCategories Purpose Returns the category of the parameter. See Also CommonCParameter.GetArrayDimensionSizeExpr CommonCParameter.SetArrayDimensionSizeExpr CommonCParameter.StringBufferSizeExpr CommonCParameter.StructType DllParameter.Type DllParameter

### DllParameter.Category

#### Syntax

[DllParameter](dllparameter.html).Category

#### Data Type

[DllParameterCategories](dllparametercategories.html)

#### Purpose

Returns the category of the parameter.

#### See Also

[CommonCParameter.GetArrayDimensionSizeExpr](commoncparameter-getarraydimensionsizeexpr.html)

[CommonCParameter.SetArrayDimensionSizeExpr](commoncparameter-setarraydimensionsizeexpr.html)

[CommonCParameter.StringBufferSizeExpr](commoncparameter-stringbuffersizeexpr.html)

[CommonCParameter.StructType](commoncparameter-structtype.html)

[DllParameter.Type](dllparameter-type.html)

[DllParameterCategories](dllparametercategories.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameter-imaginarypartvalueexpr.html language=enus -->
## TOPIC 00525: DllParameter.ImaginaryPartValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameter-imaginarypartvalueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameter-imaginarypartvalueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameter.ImaginaryPartValueExpr Data Type String Purpose Specifies the argument expression for the imaginary part of a DllParamCategory_CNiComplex or DllParamCategory_CNiComplexVector parameter. Remarks Parameters using the DllParamCategory_CNiComplexVector type and the DllParamCategory_C

### DllParameter.ImaginaryPartValueExpr

#### Syntax

[DllParameter](dllparameter.html).ImaginaryPartValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the argument expression for the imaginary part of a
 DllParamCategory_CNiComplex
 or
 DllParamCategory_CNiComplexVector
 parameter.

#### Remarks

Parameters using the
 DllParamCategory_CNiComplexVector
 type and the
 DllParamCategory_CNiComplex
 type take two argument expressions: one for the real part and one for the imaginary part. The argument expression for the real part is stored in the
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 property. The imaginary part argument expression is stored in this property.

#### See Also

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[DllParameterCategories](dllparametercategories.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameter-tsobjectparametertype.html language=enus -->
## TOPIC 00526: DllParameter.TSObjectParameterType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameter-tsobjectparametertype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameter-tsobjectparametertype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameter.TSObjectParameterType Data Type String Purpose Use the TS Object category to pass TestStand objects to DLL functions that use the Microsoft Visual Studio #import classes. Use the #import statement in Visual Studio to access the TestStand API and to define C++ classes. When you se

### DllParameter.TSObjectParameterType

#### Syntax

[DllParameter](dllparameter.html).TSObjectParameterType

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Use the TS Object category to pass TestStand objects to DLL functions that use the Microsoft Visual Studio #import classes. Use the #import statement in Visual Studio to access the TestStand API and to define C++ classes. When you select the TS object category for the parameter, this property specifies the name of the object you pass to the function.

#### Remarks

Ensure that the DLL function does not call the
 Release
 COM method on the object passed in.

#### See Also

[DllParameter.Category](dllparameter-category.html)

[DllParameterCategories](dllparametercategories.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameter-type.html language=enus -->
## TOPIC 00527: DllParameter.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameter-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameter-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameter.Type Data Type CommonCParameterTypes Purpose Specifies the type of parameter. Remarks The parameter category depends on the parameter type. Be sure to select the correct category before selecting the type. See Also DllParameter.Category CommonCParameter.StringBufferSizeExpr Commo

### DllParameter.Type

#### Syntax

[DllParameter](dllparameter.html).Type

#### Data Type

[CommonCParameterTypes](commoncparametertypes.html)

#### Purpose

Specifies the type of parameter.

#### Remarks

The parameter category depends on the parameter type. Be sure to select the correct category before selecting the type.

#### See Also

[DllParameter.Category](dllparameter-category.html)

[CommonCParameter.StringBufferSizeExpr](commoncparameter-stringbuffersizeexpr.html)

[CommonCParameter.StructType](commoncparameter-structtype.html)

[CommonCParameterTypes](commoncparametertypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameter.html language=enus -->
## TOPIC 00528: DllParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DllParameter class to configure and obtain C/C++ DLL parameter-specific information for an item in the DllParameters collection class. To access the properties and methods of the CommonCParameter class, use the DllParameter.AsCommonCParameter method. Properties Category Imaginar

### DllParameter

Use objects from the DllParameter class to configure and obtain C/C++ DLL parameter-specific information for an item in the DllParameters collection class.

To access the properties and methods of the CommonCParameter class, use the
 [DllParameter.AsCommonCParameter](dllparameter-ascommoncparameter.html)
 method.

#### Properties

| Category |
| --- |
| ImaginaryPartValueExpr |
| TSObjectParameterType |
| Type |

#### Method

| AsCommonCParameter |
| --- |

#### See Also

[CommonCParameter](commoncparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparametercategories.html language=enus -->
## TOPIC 00529: DllParameterCategories

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparametercategories.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparametercategories.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the DllParameter.Category property and the parameterCategory parameter of the DllParameters.New module to specify the group of data types to which the parameter belongs. When you get or set the category of the parameter, also get or set the data type with the DllPara

### DllParameterCategories

Use the following constants with the
 [DllParameter.Category](dllparameter-category.html)
 property and the
 parameterCategory
 parameter of the
 [DllParameters.New](dllparameters-new.html)
 module to specify the group of data types to which the parameter belongs. When you get or set the category of the parameter, also get or set the data type with the
 [DllParameter.Type](dllparameter-type.html)
 property, or set the
 parameterType
 parameter of the
 DllParameters.New
 method. Some categories do not have an associated data type; for these categories, the only valid value for the
 DllParameter.Type
 property is
 [CParamType_NotUsed](commoncparametertypes.html)

- DllParamCategory_Boolean 
 –(Value: 100) Specifies that the parameter is a Boolean type. This category does not have any associated data types.
- DllParamCategory_BooleanArray 
 –(Value: 101) Specifies that the parameter is an array of Boolean values. This category does not have any associated data types.
- DllParamCategory_bstr_t 
 –(Value: 209) Specifies that the parameter is an instance of the Microsoft Visual Studio
 _bstr_t 
 class. This category does not have any associated data types.
- DllParamCategory_CNiBoolVector 
 –(Value: 206) Specifies that the parameter is an instance of the Measurement Studio
 CNiBoolVector 
 class. This category does not have any associated data types.
- DllParamCategory_CNiComplex 
 –(Value: 202) Specifies that the parameter is an instance of the Measurement Studio
 CNiComplexT 
 template class. If you get or set this category, also get or set the
 DllParameter.Type 
 property. This category is associated with numeric data types, such as
 CParamType_Float32 
 .
- DllParamCategory_CNiComplexVector 
 –(Value: 204) Specifies that the parameter is an instance of the Measurement Studio
 CNiComplexVector 
 class. If you get or set this category, also get or set the
 DllParameter.Type 
 property. This category is associated with numeric data types, such as
 CParamType_Float32 
 .
- DllParamCategory_CNiMatrix 
 –(Value: 201) Specifies that the parameter is an instance of the Measurement Studio
 CNiScalarMatrix 
 template class. If you get or set this category, also get or set the
 DllParameter.Type 
 property. This category is associated with numeric data types, such as
 CParamType_Float32 
 .
- DllParamCategory_CNiString 
 –(Value: 203) Specifies that the parameter is an instance of the Measurement Studio
 CNiString 
 class. This category does not have any associated data types.
- DllParamCategory_CNiStringVector 
 –(Value: 210) Specifies that the parameter is an instance of the Measurement Studio
 CNiStringVector 
 class. This category does not have any associated data types.
- DllParamCategory_CNiVector 
 –(Value: 200) Specifies that the parameter is an instance of the Measurement Studio
 CNiScalarVector 
 template class. If you get or set this category, also get or set the
 DllParameter.Type 
 property. This category is associated with numeric data types, such as
 CParamType_Float32 
 .
- DllParamCategory_CString 
 –(Value: 207) Specifies that the parameter is an instance of the Microsoft Foundation Classes (MFC) CString class. This category does not have any associated data types.
- DllParamCategory_CStringArray 
 –(Value: 208) Specifies that the parameter is an instance of the MFC CStringArray class. This category does not have any associated data types.
- DllParamCategory_CStruct 
 –(Value: 5) Specifies that the parameter is a C-style struct. This category does not have any associated data types. However, you can use the
 CommonCParameter.StructType 
 property to specify the name of the TestStand type the parameter represents.
- DllParamCategory_CStructArray 
 –(Value: 8) Specifies that the parameter is an array of C-style structs. This category does not have any associated data types. However, you can use the
 CommonCParameter.StructType 
 property to specify the name of the TestStand type the parameter represents.
- DllParamCategory_Enum 
 –(Value: 10) Specifies that the parameter is an enumeration data type. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 . You can use the CommonCParameter.StructType property to specify the name of the TestStand type that the parameter represents.
- DllParamCategory_EnumArray 
 –(Value: 11) Specifies that the parameter is an array of C-style structs. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 . You can use the CommonCParameter.StructType property to specify the name of the TestStand type that the parameter represents.
- DllParamCategory_Numeric 
 –(Value: 0) Specifies that the parameter is a numeric data type. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 .
- DllParamCategory_NumericArray 
 –(Value: 1) Specifies that the parameter is an array of numbers. Valid data types for this category include
 CParamType_Float32 
 ,
 CParamType_Float64 
 ,
 CParamType_Int16 
 ,
 CParamType_Int32 
 ,
 CParamType_Int8 
 ,
 CParamType_UInt16 
 ,
 CParamType_UInt32 
 ,
 CParamType_UInt8 
 ,
 CParamType_UInt64 
 , and
 CParamType_Int64 
 .
- DllParamCategory_Object 
 –(Value: 4) Specifies that the parameter is an ActiveX object reference. Valid data types for this category include
 CParamType_CVIHandle 
 ,
 CParamType_IDispatch 
 , and
 CParamType_IUnknown 
 .
- DllParamCategory_ObjectArray 
 –(Value: 7) Specifies that the parameter is an array of ActiveX object references. Valid data types for this category include
 CParamType_CVIHandle 
 ,
 CParamType_IDispatch 
 , and
 CParamType_IUnknown 
 .
- DllParamCategory_Pointer 
 –(Value: 9) Specifies that the parameter is a pointer. This category does not have any associated data types.
- DllParamCategory_String 
 –(Value: 2) Specifies that the parameter is a string. Valid data types for this category include
 CParamType_CString 
 ,
 CParamType_CStringBuffer 
 ,
 CParamType_UnicodeString 
 , and
 CParamType_UnicodeStringBuffer 
 .
- DllParamCategory_StringArray 
 –(Value: 6) Specifies that the parameter is an array of strings. Valid data types for this category include
 CParamType_CString 
 ,
 CParamType_CStringBuffer 
 ,
 CParamType_UnicodeString 
 , and
 CParamType_UnicodeStringBuffer 
 .
- DllParamCategory_TSObject 
 –(Value: 205) Specifies that the parameter is an object from the TestStand ActiveX API. This category does not have any associated parameters. However, the
 DllParameter.TSObjectParameterType 
 property specifies what kind of TestStand object the parameter represents.
- DllParamCategory_Void 
 –(Value: 3) Specifies that the parameter is a void parameter, meaning it has no value. This category applies only to return values.

#### See Also

[CommonCParameter.ParameterName](commoncparameter-parametername.html)

[CommonCParameter.SetArrayDimensionSizeExpr](commoncparameter-setarraydimensionsizeexpr.html)

[CommonCParameter.StringBufferSizeExpr](commoncparameter-stringbuffersizeexpr.html)

[CommonCParameter.StructType](commoncparameter-structtype.html)

[CommonCParameterTypes](commoncparametertypes.html)

[DllParameter.Category](dllparameter-category.html)

[DllParameter.TSObjectParameterType](dllparameter-tsobjectparametertype.html)

[DllParameter.Type](dllparameter-type.html)

[DllParameters.New](dllparameters-new.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameters-count.html language=enus -->
## TOPIC 00530: DllParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameters.Count Data Type Long Purpose Returns the number of items in the collection.

### DllParameters.Count

#### Syntax

[DllParameters](dllparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameters-delete.html language=enus -->
## TOPIC 00531: DllParameters.Delete

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameters-delete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameters-delete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameters.Delete( index) Purpose Removes the DllParameter object located at the specified index. Parameters index As Long [In] Specifies the zero-based index of the parameter to delete.

### DllParameters.Delete

#### Syntax

[DllParameters](dllparameters.html).Delete( index)

#### Purpose

Removes the DllParameter object located at the specified index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to delete.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameters-item.html language=enus -->
## TOPIC 00532: DllParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameters.Item( index) Data Type DllParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also DllParameter

### DllParameters.Item

#### Syntax

[DllParameters](dllparameters.html).Item( index)

#### Data Type

[DllParameter](dllparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[DllParameter](dllparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameters-move.html language=enus -->
## TOPIC 00533: DllParameters.Move

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameters-move.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameters-move.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameters.Move( index, newIndex) Purpose Moves a DllParameter object within a collection. Parameters index As Long [In] Specifies the zero-based index indicating the current position of the parameter to move. newIndex As Long [In] Specifies the zero-based index indicating the new position

### DllParameters.Move

#### Syntax

[DllParameters](dllparameters.html).Move( index, newIndex)

#### Purpose

Moves a DllParameter object within a collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index indicating the current position of the parameter to move.

newIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index indicating the new position of the parameter.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameters-new.html language=enus -->
## TOPIC 00534: DllParameters.New

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameters-new.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameters-new.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameters.New( index, parameterName, parameterValueExpr, parameterCategory, parameterPass, parameterType) Purpose Adds a new parameter to the collection. Parameters index As Long [In] Specifies the zero-based index of where to insert the parameter. parameterName As String [In] Specifies t

### DllParameters.New

#### Syntax

[DllParameters](dllparameters.html).New( index, parameterName, parameterValueExpr, parameterCategory, parameterPass, parameterType)

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

If the parameter is an input, this expression corresponds to the value to pass. If the parameter is an output, this expression specifies where TestStand stores the result value.

parameterCategory
 As
 [DllParameterCategories](dllparametercategories.html)

[In] Specifies the parameter category.

parameterPass
 As
 [CommonCParameterPassOptions](commoncparameterpassoptions.html)

[In] Specifies how to pass the value specified in the argument expression property,
 [CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)
 , to the specific function and sets the
 [CommonCParameter.Pass](commoncparameter-pass.html)
 property.

parameterType
 As
 [CommonCParameterTypes](commoncparametertypes.html)

[In] Specifies the parameter type.

#### See Also

[CommonCParameter.Pass](commoncparameter-pass.html)

[CommonCParameter.ValueExpr](commoncparameter-valueexpr.html)

[CommonCParameterPassOptions](commoncparameterpassoptions.html)

[CommonCParameterTypes](commoncparametertypes.html)

[DllParameterCategories](dllparametercategories.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameters-newarguments.html language=enus -->
## TOPIC 00535: DllParameters.NewArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameters-newarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameters-newarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DllParameters.NewArguments Return Value DllArguments Purpose Creates and returns a new DllArguments collection. Use this collection to pass argument values to a DLL module function using the DllModule.Execute method. Remarks The new collection contains the same number of items as the DllParam

### DllParameters.NewArguments

#### Syntax

[DllParameters](dllparameters.html).NewArguments

#### Return Value

[DllArguments](dllarguments.html)

#### Purpose

Creates and returns a new
 [DllArguments](dllarguments.html)
 collection. Use this collection to pass argument values to a DLL module function using the
 [DllModule.Execute](dllmodule-execute.html)
 method.

#### Remarks

The new collection contains the same number of items as the
 [DllParameters](dllparameters.html)
 collection. To pass an argument value to a function parameter, set the
 [DllArgument.Value](dllargument-value.html)
 property on the item in the
 DllArguments
 collection that has the same index as the parameter in the
 DllParameters
 collection.

#### See Also

[DllArgument.Value](dllargument-value.html)

[DllArguments](dllarguments.html)

[DllModule.Execute](dllmodule-execute.html)

[DllParameters](dllparameters.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dllparameters.html language=enus -->
## TOPIC 00536: DllParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dllparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dllparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DllParameters class to configure and obtain parameters for a module that uses the C/C++ DLL Adapter. Use the DllModule.Parameters property to obtain the collection of parameters for a module. Properties Count (Read Only) Item (Read Only) Methods Delete Move New NewArguments See

### DllParameters

Use objects from the DllParameters class to configure and obtain parameters for a module that uses the C/C++ DLL Adapter. Use the
 [DllModule.Parameters](dllmodule-parameters.html)
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
| NewArguments |

#### See Also

[DllModule.Parameters](dllmodule-parameters.html)

[DllParameter](dllparameter.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-asadapter.html language=enus -->
## TOPIC 00537: DotNetAdapter.AsAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-asadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-asadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.AsAdapter Return Value Adapter Purpose Returns the underlying module Adapter object that represents the DotNetAdapter object. Remarks Use the underlying module Adapter object to access properties and methods common to all adapters. See Also Adapter

### DotNetAdapter.AsAdapter

#### Syntax

[DotNetAdapter](dotnetadapter.html).AsAdapter

#### Return Value

[Adapter](adapter.html)

#### Purpose

Returns the underlying module Adapter object that represents the DotNetAdapter object.

#### Remarks

Use the underlying module Adapter object to access properties and methods common to all adapters.

#### See Also

[Adapter](adapter.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-cacheassemblyinfo.html language=enus -->
## TOPIC 00538: DotNetAdapter.CacheAssemblyInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-cacheassemblyinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-cacheassemblyinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.CacheAssemblyInfo( assemblyLocationParam, assemblyPathParam) Purpose Reads the specified assembly and caches type information for later use in TestStand. This method also reads and caches types and assemblies this assembly references. If a cached assembly changes, TestStand dete

### DotNetAdapter.CacheAssemblyInfo

#### Syntax

[DotNetAdapter](dotnetadapter.html).CacheAssemblyInfo( assemblyLocationParam, assemblyPathParam)

#### Purpose

Reads the specified assembly and caches type information for later use in TestStand. This method also reads and caches types and assemblies this assembly references. If a cached assembly changes, TestStand detects the change and updates the cache.

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[In] Specifies whether the assembly is located in a file or in the Global Assembly Cache (GAC).

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the assembly.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-cacheassemblyinfoex.html language=enus -->
## TOPIC 00539: DotNetAdapter.CacheAssemblyInfoEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-cacheassemblyinfoex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-cacheassemblyinfoex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.CacheAssemblyInfoEx( assemblyLocationParam, assemblyPathParam, options) Purpose Reads the specified assembly and caches type information for later use in TestStand. This method also reads and caches types and assemblies this assembly references. If a cached assembly changes, Tes

### DotNetAdapter.CacheAssemblyInfoEx

#### Syntax

[DotNetAdapter](dotnetadapter.html).CacheAssemblyInfoEx( assemblyLocationParam, assemblyPathParam, options)

#### Purpose

Reads the specified assembly and caches type information for later use in TestStand. This method also reads and caches types and assemblies this assembly references. If a cached assembly changes, TestStand detects the change and updates the cache.

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[In] Specifies whether the assembly is located in a file or in the Global Assembly Cache (GAC).

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the assembly.

options
 As
 [long](data-types-for-teststand.html)

[In] Specifies one or more
 [DotNetAdapterCacheAssemblyInfoExOptions](dotnetadaptercacheassemblyinfoexoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-getclassnames.html language=enus -->
## TOPIC 00540: DotNetAdapter.GetClassNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-getclassnames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-getclassnames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.GetClassNames( assemblyLocationParam, assemblyPathParam, options, typeNames, displayNames) Purpose Retrieves the list of class names found in the given assembly. Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported. Para

### DotNetAdapter.GetClassNames

#### Syntax

[DotNetAdapter](dotnetadapter.html).GetClassNames( assemblyLocationParam, assemblyPathParam, options, typeNames, displayNames)

#### Purpose

Retrieves the list of class names found in the given assembly.

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[In] Specifies whether the assembly is located in a file or in the Global Assembly Cache (GAC).

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the assembly.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [DotNetAdapterGetClassNamesOptions](dotnetadaptergetclassnamesoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

typeNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns an array that contains the fully qualified type names of all classes found in the specified assembly. This array is parallel to the
 displayNames
 array.

displayNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns an array that contains the display names for all classes found in the assembly. This array is parallel to the
 typeNames
 array.

The display name for a class might be slightly different than the fully qualified name. For example, if all classes in the assembly share a common namespace, the display names do not include the namespace.

#### See Also

[DotNetAdapter.GetMemberNames](dotnetadapter-getmembernames.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-getexcludefromstructure.html language=enus -->
## TOPIC 00541: DotNetAdapter.GetExcludeFromStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-getexcludefromstructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-getexcludefromstructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.GetExcludeFromStructure( typeDefinition, propertyLookupString) Return Value Boolean Purpose Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as .NET parameters. Para

### DotNetAdapter.GetExcludeFromStructure

#### Syntax

[DotNetAdapter](dotnetadapter.html).GetExcludeFromStructure( typeDefinition, propertyLookupString)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as .NET parameters.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[DotNetAdapter.SetExcludeFromStructure](dotnetadapter-setexcludefromstructure.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-getgacassemblystrongnames.html language=enus -->
## TOPIC 00542: DotNetAdapter.GetGACAssemblyStrongNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-getgacassemblystrongnames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-getgacassemblystrongnames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.GetGACAssemblyStrongNames Return Value Object Array Purpose Returns the strong name of each assembly found in the Global Assembly Cache (GAC). This method is obsolete. Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported

### DotNetAdapter.GetGACAssemblyStrongNames

#### Syntax

[DotNetAdapter](dotnetadapter.html).GetGACAssemblyStrongNames

#### Return Value

[Object Array](data-types-for-teststand.html)

#### Purpose

Returns the strong name of each assembly found in the Global Assembly Cache (GAC).

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-getgacassemblystrongnames_2.html language=enus -->
## TOPIC 00543: DotNetAdapter.GetGACAssemblyStrongNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-getgacassemblystrongnames_2.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-getgacassemblystrongnames_2.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.GetGACAssemblyStrongNames Return Value Object Array Purpose Returns the strong name of each assembly found in the Global Assembly Cache (GAC). This method is obsolete. Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported

### DotNetAdapter.GetGACAssemblyStrongNames

#### Syntax

[DotNetAdapter](dotnetadapter.html).GetGACAssemblyStrongNames

#### Return Value

[Object Array](data-types-for-teststand.html)

#### Purpose

Returns the strong name of each assembly found in the Global Assembly Cache (GAC).

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

Parent topic:

Obsolete DotNetAdapter Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-getmembernames.html language=enus -->
## TOPIC 00544: DotNetAdapter.GetMemberNames

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-getmembernames.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-getmembernames.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.GetMemberNames( assemblyLocationParam, assemblyPathParam, classTypeNameParam, options, signatures, displayNames) Purpose Retrieves the list of public member names found in the given class. Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) i

### DotNetAdapter.GetMemberNames

#### Syntax

[DotNetAdapter](dotnetadapter.html).GetMemberNames( assemblyLocationParam, assemblyPathParam, classTypeNameParam, options, signatures, displayNames)

#### Purpose

Retrieves the list of public member names found in the given class.

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[In] Specifies whether the assembly is located in a file or in the Global Assembly Cache (GAC).

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the assembly.

classTypeNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the fully specified type name for the class, including namespaces.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [DotNetAdapterGetMemberNamesOptions](dotnetadaptergetmembernamesoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

signatures
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns an array that contains the full signature for each member found in the specified class. This array is parallel to the
 displayNames
 array.

displayNames
 As
 [String Array](data-types-for-teststand.html)

[Out] Returns an array that contains the display name for each member found in the specified class. This array is parallel to the
 signatures
 array.

Display names may be slightly different than the member signatures. For example, static members have the
 static
 suffix at the end of the display name.

#### See Also

[DotNetAdapter.GetClassNames](dotnetadapter-getclassnames.html)

[DotNetAdapterGetMemberNamesOptions](dotnetadaptergetmembernamesoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-getstructurememberlabel.html language=enus -->
## TOPIC 00545: DotNetAdapter.GetStructureMemberLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-getstructurememberlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-getstructurememberlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.GetStructureMemberLabel( typeDefinition, propertyLookupString) Return Value String Purpose Returns the label of the structure member that corresponds to the specified type definition property. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This m

### DotNetAdapter.GetStructureMemberLabel

#### Syntax

[DotNetAdapter](dotnetadapter.html).GetStructureMemberLabel( typeDefinition, propertyLookupString)

#### Return Value

[String](data-types-for-teststand.html)

#### Purpose

Returns the label of the structure member that corresponds to the specified type definition property.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

#### See Also

[DotNetAdapter.SetStructureMemberLabel](dotnetadapter-setstructurememberlabel.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-getstructurepassingenabled.html language=enus -->
## TOPIC 00546: DotNetAdapter.GetStructurePassingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-getstructurepassingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-getstructurepassingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.GetStructurePassingEnabled( typeDefinition) Return Value Boolean Purpose Returns a value that indicates whether a type definition allows the .NET Adapter to pass instances of the type as structure parameters. Parameters typeDefinition As PropertyObject [In] Specifies the type de

### DotNetAdapter.GetStructurePassingEnabled

#### Syntax

[DotNetAdapter](dotnetadapter.html).GetStructurePassingEnabled( typeDefinition)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether a type definition allows the .NET Adapter to pass instances of the type as structure parameters.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

#### See Also

[DotNetAdapter.SetStructurePassingEnabled](dotnetadapter-setstructurepassingenabled.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-isclassvalid.html language=enus -->
## TOPIC 00547: DotNetAdapter.IsClassValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-isclassvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-isclassvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.IsClassValid( assemblyLocationParam, assemblyPathParam, classTypeNameParam) Return Value Boolean Purpose Returns True if the .NET Adapter finds the given class in the given assembly. Otherwise, this method returns False . Starting with TestStand 2024 Q4, loading assemblies from

### DotNetAdapter.IsClassValid

#### Syntax

[DotNetAdapter](dotnetadapter.html).IsClassValid( assemblyLocationParam, assemblyPathParam, classTypeNameParam)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the .NET Adapter finds the given class in the given assembly. Otherwise, this method returns
 False
 .

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[In] Specifies whether the assembly is located in a file or in the Global Assembly Cache (GAC).

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the assembly.

classTypeNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the fully specified type name for the class, including namespaces.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-isclassvalidex.html language=enus -->
## TOPIC 00548: DotNetAdapter.IsClassValidEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-isclassvalidex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-isclassvalidex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.IsClassValidEx( assemblyLocationParam, assemblyPathParam, classTypeNameParam, options) Return Value Boolean Purpose Returns True if the .NET Adapter finds the given class in the given assembly. Otherwise, this method returns False . Starting with TestStand 2024 Q4, loading assem

### DotNetAdapter.IsClassValidEx

#### Syntax

[DotNetAdapter](dotnetadapter.html).IsClassValidEx( assemblyLocationParam, assemblyPathParam, classTypeNameParam, options)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the .NET Adapter finds the given class in the given assembly. Otherwise, this method returns
 False
 .

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[In] Specifies whether the assembly is located in a file or in the Global Assembly Cache (GAC).

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the assembly.

classTypeNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the fully specified type name for the class, including namespaces.

options
 As
 [long](data-types-for-teststand.html)

[In] Specifies one or more
 [DotNetAdapterIsClassValidExOptions](dotnetadapterisclassvalidexoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-newmodule.html language=enus -->
## TOPIC 00549: DotNetAdapter.NewModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-newmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-newmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.NewModule Return Value DotNetModule Purpose Creates and returns a new DotNetModule object you can call directly without using a step, sequence, or execution. See Also DotNetModule DotNetModule.Execute DotNetModule.NewModuleArguments

### DotNetAdapter.NewModule

#### Syntax

[DotNetAdapter](dotnetadapter.html).NewModule

#### Return Value

[DotNetModule](dotnetmodule.html)

#### Purpose

Creates and returns a new
 [DotNetModule](dotnetmodule.html)
 object you can call directly without using a step, sequence, or execution.

#### See Also

[DotNetModule](dotnetmodule.html)

[DotNetModule.Execute](dotnetmodule-execute.html)

[DotNetModule.NewModuleArguments](dotnetmodule-newmodulearguments.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-setexcludefromstructure.html language=enus -->
## TOPIC 00550: DotNetAdapter.SetExcludeFromStructure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-setexcludefromstructure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-setexcludefromstructure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.SetExcludeFromStructure( typeDefinition, propertyLookupString, excludeFromStructure) Purpose Specifies whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as .NET parameters. Parameters typeDefinitio

### DotNetAdapter.SetExcludeFromStructure

#### Syntax

[DotNetAdapter](dotnetadapter.html).SetExcludeFromStructure( typeDefinition, propertyLookupString, excludeFromStructure)

#### Purpose

Specifies whether the specified type definition property is excluded when converting instances of the type definition into structures to pass as .NET parameters.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

excludeFromStructure
 As
 [Boolean](data-types-for-teststand.html)

[In] Pass
 True
 to exclude the corresponding property. Otherwise, set this parameter to
 False
 .

#### See Also

[DotNetAdapter.GetExcludeFromStructure](dotnetadapter-getexcludefromstructure.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-setstructurememberlabel.html language=enus -->
## TOPIC 00551: DotNetAdapter.SetStructureMemberLabel

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-setstructurememberlabel.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-setstructurememberlabel.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.SetStructureMemberLabel( typeDefinition, propertyLookupString, structureMemberLabel) Purpose Specifies the label of the structure member that corresponds to the specified type definition property. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. Th

### DotNetAdapter.SetStructureMemberLabel

#### Syntax

[DotNetAdapter](dotnetadapter.html).SetStructureMemberLabel( typeDefinition, propertyLookupString, structureMemberLabel)

#### Purpose

Specifies the label of the structure member that corresponds to the specified type definition property.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

propertyLookupString
 As
 [String](data-types-for-teststand.html)

[In] Specifies the location of the property in the type definition.

structureMemberLabel
 As
 [String](data-types-for-teststand.html)

[In] Specifies the label of the structure member.

#### See Also

[DotNetAdapter.GetStructureMemberLabel](dotnetadapter-getstructurememberlabel.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-setstructurepassingenabled.html language=enus -->
## TOPIC 00552: DotNetAdapter.SetStructurePassingEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-setstructurepassingenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-setstructurepassingenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.SetStructurePassingEnabled( typeDefinition, structPassingEnabled) Purpose Specifies whether a type definition allows the .NET Adapter to pass instances of the type as structure parameters. Parameters typeDefinition As PropertyObject [In] Specifies the type definition. This metho

### DotNetAdapter.SetStructurePassingEnabled

#### Syntax

[DotNetAdapter](dotnetadapter.html).SetStructurePassingEnabled( typeDefinition, structPassingEnabled)

#### Purpose

Specifies whether a type definition allows the .NET Adapter to pass instances of the type as structure parameters.

#### Parameters

typeDefinition
 As
 
 [PropertyObject](propertyobject.html)

[In] Specifies the type definition. This method returns an error if the property object is not a type definition.

structPassingEnabled
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether structure passing is enabled.

#### See Also

[DotNetAdapter.GetStructurePassingEnabled](dotnetadapter-getstructurepassingenabled.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-visualstudiodteversionfordebugg.html language=enus -->
## TOPIC 00553: DotNetAdapter.VisualStudioDTEVersionForDebugging

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-visualstudiodteversionfordebugg.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-visualstudiodteversionfordebugg.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.VisualStudioDTEVersionForDebugging Data Type String Purpose Specifies the Microsoft Visual Studio development environment (DTE) version the .NET Adapter uses when debugging into code modules when more than one version of Visual Studio is installed. Remarks If you have only one v

### DotNetAdapter.VisualStudioDTEVersionForDebugging

#### Syntax

[DotNetAdapter](dotnetadapter.html).VisualStudioDTEVersionForDebugging

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the Microsoft Visual Studio development environment (DTE) version the .NET Adapter uses when debugging into code modules when more than one version of Visual Studio is installed.

#### Remarks

If you have only one version of Visual Studio installed, the .NET Adapter always uses that version for debugging.

You can set this property to a supported value of the
 [VisualStudioDTEVersions](visualstudiodteversions.html)
 constants or to the programmatic identifier of the DTE version you want to use.

Note

VisualStudioDTEVersion_MatchProject

#### See Also

[VisualStudioDTEVersions](visualstudiodteversions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter-visualstudiodteversionforeditin.html language=enus -->
## TOPIC 00554: DotNetAdapter.VisualStudioDTEVersionForEditing

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter-visualstudiodteversionforeditin.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter-visualstudiodteversionforeditin.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetAdapter.VisualStudioDTEVersionForEditing Data Type String Purpose Specifies the Microsoft Visual Studio development environment (DTE) version the .NET Adapter uses when creating and editing code when more than one version of Visual Studio is installed. Remarks If you have only one versi

### DotNetAdapter.VisualStudioDTEVersionForEditing

#### Syntax

[DotNetAdapter](dotnetadapter.html).VisualStudioDTEVersionForEditing

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the Microsoft Visual Studio development environment (DTE) version the .NET Adapter uses when creating and editing code when more than one version of Visual Studio is installed.

#### Remarks

If you have only one version of Visual Studio installed, the .NET Adapter always uses that version for debugging.

You can set this property to a supported value of the
 [VisualStudioDTEVersions](visualstudiodteversions.html)
 constants or to the programmatic identifier of the DTE version you want to use.

#### See Also

[VisualStudioDTEVersions](visualstudiodteversions.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapter.html language=enus -->
## TOPIC 00555: DotNetAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DotNetAdapter class to configure and obtain .NET Adapter-specific information about the module adapter. Call the Engine.GetAdapter or Engine.GetAdapterByKeyName method to obtain a reference to the adapter object. To access the properties and methods of the Adapter class, use the

### DotNetAdapter

Use objects from the DotNetAdapter class to configure and obtain .NET Adapter-specific information about the module adapter. Call the
 
 [Engine.GetAdapter](engine-getadapter.html)
 or
 
 [Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)
 method to obtain a reference to the adapter object.

To access the properties and methods of the Adapter class, use the
 [DotNetAdapter.AsAdapter](dotnetadapter-asadapter.html)
 method to obtain an object.

#### Properties

| VisualStudioDTEVersionForDebugging |
| --- |
| VisualStudioDTEVersionForEditing |

#### Methods

| AsAdapter |
| --- |
| CacheAssemblyInfo |
| GetClassNames |
| GetExcludeFromStructure |
| GetMemberNames |
| GetStructureMemberLabel |
| GetStructurePassingEnabled |
| IsClassValid |
| NewModule |
| SetExcludeFromStructure |
| SetStructureMemberLabel |
| SetStructurePassingEnabled |

#### See Also

[Adapter](adapter.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.GetAdapterByKeyName](engine-getadapterbykeyname.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadaptercacheassemblyinfoexoptions.html language=enus -->
## TOPIC 00556: DotNetAdapterCacheAssemblyInfoExOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadaptercacheassemblyinfoexoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadaptercacheassemblyinfoexoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the options parameter of the DotNetAdapter.CacheAssemblyInfoEx method. If you pass no option (Value: 0x0), the adapter allows unloading of the assembly on which the method acts. DotNetAdapterCacheAssemblyInfoExOption_AllowLoadingMixedAssemblies –(Value: 0x1) The DotNetAdapte

### DotNetAdapterCacheAssemblyInfoExOptions

Use these constants with the options parameter of the
 [DotNetAdapter.CacheAssemblyInfoEx](dotnetadapter-cacheassemblyinfoex.html)
 method. If you pass no option (Value: 0x0), the adapter allows unloading of the assembly on which the method acts.

- DotNetAdapterCacheAssemblyInfoExOption_AllowLoadingMixedAssemblies 
 –(Value: 0x1) The
 DotNetAdapter.CacheAssemblyInfoEx 
 method will allow loading and caching of all assembly info for C++/CLI (mixed-mode) assemblies, but these assemblies can't be unloaded. .NET Core doesn't allow loading C++/CLI assemblies into AssemblyLoadContexts which can be unloaded (collectible).

#### See Also

[DotNetAdapter.CacheAssemblyInfoEx](dotnetadapter-cacheassemblyinfoex.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadaptergetclassnamesoptions.html language=enus -->
## TOPIC 00557: DotNetAdapterGetClassNamesOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadaptergetclassnamesoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadaptergetclassnamesoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the options parameter of the DotNetAdapter.GetClassNames method. If you pass no option (Value: 0x0), the adapter supports unloading of the assembly for which the API fetches the class names. DotNetAdapterGetClassNamesOption__AllowLoadingMixedAssemblies –(Value: 0x1) The DotN

### DotNetAdapterGetClassNamesOptions

Use these constants with the options parameter of the
 [DotNetAdapter.GetClassNames](dotnetadapter-getclassnames.html)
 method. If you pass no option (Value: 0x0), the adapter supports unloading of the assembly for which the API fetches the class names.

- DotNetAdapterGetClassNamesOption__AllowLoadingMixedAssemblies 
 –(Value: 0x1) The
 DotNetAdapter.GetClassNames 
 method will allow fetching class data for C++/CLI (mixed-mode) assemblies, but these assemblies can't be unloaded. .NET Core doesn't allow loading C++/CLI assemblies into AssemblyLoadContexts which can be unloaded (collectible).

#### See Also

[DotNetAdapter.GetClassNames](dotnetadapter-getclassnames.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadaptergetmembernamesoptions.html language=enus -->
## TOPIC 00558: DotNetAdapterGetMemberNamesOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadaptergetmembernamesoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadaptergetmembernamesoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the options parameter of the DotNetAdapter.GetMemberNames method. If you pass no option (Value: 0x0), the adapter retrieves non-instance members only, including constructors, static members, and special options, such as Create Remote Object and Use Existing Object. Starting

### DotNetAdapterGetMemberNamesOptions

DotNetAdapter.GetMemberNames

Note

Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.

- DotNetAdapterGetMemberNamesOption_InstanceMembers 
 –(Value: 0x1) The
 DotNetAdapter.GetMemberNames 
 method retrieves only instance members. The adapter does not retrieve static members or constructors.
- DotNetAdapterGetMemberNamesOption_AllowLoadingMixedAssemblies 
 –(Value: 0x2) The
 DotNetAdapter.GetMemberNames 
 method will allow retrieving member names for C++/CLI (mixed-mode) assemblies, but these assemblies can't be unloaded. .NET Core doesn't allow loading C++/CLI assemblies into AssemblyLoadContexts which can be unloaded(collectible).

#### See Also

[DotNetAdapter.GetMemberNames](dotnetadapter-getmembernames.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetadapterisclassvalidexoptions.html language=enus -->
## TOPIC 00559: DotNetAdapterIsClassValidExOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetadapterisclassvalidexoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetadapterisclassvalidexoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the options parameter of the DotNetAdapter.IsClassValidEx method. If you pass no option (Value: 0x0), the adapter allows unloading of the assembly on which the method acts. DotNetAdapterIsClassValidExOption_AllowLoadingMixedAssemblies –(Value: 0x1) The DotNetAdapter.IsClassV

### DotNetAdapterIsClassValidExOptions

Use these constants with the options parameter of the
 [DotNetAdapter.IsClassValidEx](dotnetadapter-isclassvalidex.html)
 method. If you pass no option (Value: 0x0), the adapter allows unloading of the assembly on which the method acts.

- DotNetAdapterIsClassValidExOption_AllowLoadingMixedAssemblies 
 –(Value: 0x1) The
 DotNetAdapter.IsClassValidEx 
 method will allow loading and checking the validity of classes from C++/CLI (mixed-mode) assemblies, but these assemblies can't be unloaded. .NET Core doesn't allow loading C++/CLI assemblies into AssemblyLoadContexts which can be unloaded (collectible).

#### See Also

[DotNetAdapter.IsClassValidEx](dotnetadapter-isclassvalidex.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetargument-elements.html language=enus -->
## TOPIC 00560: DotNetArgument.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetargument-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetargument-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetArgument.Elements Data Type DotNetArguments Purpose Returns a collection of DotNetArgument objects to pass to a struct or an array parameter. Remarks The collection contains the same number of items as the corresponding DotNetParameter.Elements collection. See Also DotNetArgument DotNet

### DotNetArgument.Elements

#### Syntax

[DotNetArgument](dotnetargument.html).Elements

#### Data Type

[DotNetArguments](dotnetarguments.html)

#### Purpose

Returns a collection of
 [DotNetArgument](dotnetargument.html)
 objects to pass to a struct or an array parameter.

#### Remarks

The collection contains the same number of items as the corresponding
 [DotNetParameter.Elements](dotnetparameter-elements.html)
 collection.

#### See Also

[DotNetArgument](dotnetargument.html)

[DotNetModule.Execute](dotnetmodule-execute.html)

[DotNetModuleArguments](dotnetmodulearguments.html)

[DotNetParameter.Elements](dotnetparameter-elements.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetargument-parametername.html language=enus -->
## TOPIC 00561: DotNetArgument.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetargument-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetargument-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetArgument.ParameterName Data Type String Purpose Returns the name of the parameter with the argument. See Also DotNetArgument.ParameterName

### DotNetArgument.ParameterName

#### Syntax

[DotNetArgument](dotnetargument.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter with the argument.

#### See Also

[DotNetArgument.ParameterName](dotnetargument-parametername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetargument-value.html language=enus -->
## TOPIC 00562: DotNetArgument.Value

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetargument-value.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetargument-value.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetArgument.Value Data Type PropertyObject Purpose Specifies the argument value to pass for the corresponding parameter. Remarks When you pass a DotNetModuleArguments collection to the DotNetModule.Execute method, the adapter passes this property to the function instead of evaluating the D

### DotNetArgument.Value

#### Syntax

[DotNetArgument](dotnetargument.html).Value

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Specifies the argument value to pass for the corresponding parameter.

#### Remarks

When you pass a
 [DotNetModuleArguments](dotnetmodulearguments.html)
 collection to the
 [DotNetModule.Execute](dotnetmodule-execute.html)
 method, the adapter passes this property to the function instead of evaluating the
 [DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)
 expression.

#### See Also

[DotNetModule.Execute](dotnetmodule-execute.html)

[DotNetModuleArguments](dotnetmodulearguments.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetargument.html language=enus -->
## TOPIC 00563: DotNetArgument

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetargument.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetargument.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from this class to specify the argument value to pass to a DotNetCall object using the DotNetModule.Execute method. Properties Elements (Read Only) ParameterName (Read Only) Value See Also DotNetCall DotNetModule.Execute

### DotNetArgument

Use objects from this class to specify the argument value to pass to a
 [DotNetCall](dotnetcall.html)
 object using the
 [DotNetModule.Execute](dotnetmodule-execute.html)
 method.

#### Properties

| Elements (Read Only) |
| --- |
| ParameterName (Read Only) |
| Value |

#### See Also

[DotNetCall](dotnetcall.html)

[DotNetModule.Execute](dotnetmodule-execute.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetarguments-count.html language=enus -->
## TOPIC 00564: DotNetArguments.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetarguments-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetarguments-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetArguments.Count Data Type Long Purpose Returns the number of items in the collection. See Also DotNetArgument DotNetArguments

### DotNetArguments.Count

#### Syntax

[DotNetArguments](dotnetarguments.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[DotNetArgument](dotnetargument.html)

[DotNetArguments](dotnetarguments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetarguments-item.html language=enus -->
## TOPIC 00565: DotNetArguments.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetarguments-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetarguments-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetArguments.Item( index) Data Type DotNetArgument Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to obtain. See Also DotNetArgument DotNetArguments

### DotNetArguments.Item

#### Syntax

[DotNetArguments](dotnetarguments.html).Item( index)

#### Data Type

[DotNetArgument](dotnetargument.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to obtain.

#### See Also

[DotNetArgument](dotnetargument.html)

[DotNetArguments](dotnetarguments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetarguments.html language=enus -->
## TOPIC 00566: DotNetArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from this class to pass specific argument values to a specific DotNetCall object using the DotNetModule.Execute method. Use the DotNetModule.NewModuleArguments method to create a new DotNetModuleArguments collection of DotNetArguments objects. Properties Count (Read Only) Item (Read Only

### DotNetArguments

Use objects from this class to pass specific argument values to a specific
 [DotNetCall](dotnetcall.html)
 object using the
 [DotNetModule.Execute](dotnetmodule-execute.html)
 method. Use the
 [DotNetModule.NewModuleArguments](dotnetmodule-newmodulearguments.html)
 method to create a new
 [DotNetModuleArguments](dotnetmodulearguments.html)
 collection of
 DotNetArguments
 objects.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[DotNetCall](dotnetcall.html)

[DotNetModule.Execute](dotnetmodule-execute.html)

[DotNetModule.NewModuleArguments](dotnetmodule-newmodulearguments.html)

[DotNetModuleArguments](dotnetmodulearguments.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-callindex.html language=enus -->
## TOPIC 00567: DotNetCall.CallIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-callindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-callindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.CallIndex Data Type Long Purpose Returns the index of the DotNetCall object in the DotNetCalls collection on the DotNetModule object. See Also DotNetCalls DotNetModule

### DotNetCall.CallIndex

#### Syntax

[DotNetCall](dotnetcall.html).CallIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the index of the
 DotNetCall
 object in the
 [DotNetCalls](dotnetcalls.html)
 collection on the
 [DotNetModule](dotnetmodule.html)
 object.

#### See Also

[DotNetCalls](dotnetcalls.html)

[DotNetModule](dotnetmodule.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-classhelpstring.html language=enus -->
## TOPIC 00568: DotNetCall.ClassHelpString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-classhelpstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-classhelpstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.ClassHelpString Data Type String Purpose Returns the help string the assembly associates with the class for this call. See Also DotNetCall.ClassName DotNetCall.MemberHelpString

### DotNetCall.ClassHelpString

#### Syntax

[DotNetCall](dotnetcall.html).ClassHelpString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the help string the assembly associates with the class for this call.

#### See Also

[DotNetCall.ClassName](dotnetcall-classname.html)

[DotNetCall.MemberHelpString](dotnetcall-memberhelpstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-classname.html language=enus -->
## TOPIC 00569: DotNetCall.ClassName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-classname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-classname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.ClassName Data Type String Purpose Returns the name of the class on which to perform the call. This property is based on the DotNetModule.ClassName property if the current DotNetCall object is the first call on the step. Otherwise, this property is based on the return value of the

### DotNetCall.ClassName

#### Syntax

[DotNetCall](dotnetcall.html).ClassName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the class on which to perform the call. This property is based on the
 [DotNetModule.ClassName](dotnetmodule-classname.html)
 property if the current
 DotNetCall
 object is the first call on the step. Otherwise, this property is based on the return value of the previous
 DotNetCall
 object in the chain of calls.

#### See Also

[DotNetModule.ClassName](dotnetmodule-classname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-classnamefornextcall.html language=enus -->
## TOPIC 00570: DotNetCall.ClassNameForNextCall

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-classnamefornextcall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-classnamefornextcall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.ClassNameForNextCall Data Type String Purpose If you add a new call to the call chain after the current call, this property returns the class name the new call uses. If the current call does not have a return value of a type on which TestStand supports making another call, this pro

### DotNetCall.ClassNameForNextCall

#### Syntax

[DotNetCall](dotnetcall.html).ClassNameForNextCall

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

If you add a new call to the call chain after the current call, this property returns the class name the new call uses. If the current call does not have a return value of a type on which TestStand supports making another call, this property returns an empty string.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-createcode.html language=enus -->
## TOPIC 00571: DotNetCall.CreateCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-createcode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-createcode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.CreateCode Return Value Boolean Specifies whether the DotNetCall object was modified. Purpose Launches Microsoft Visual Studio to create code for the .NET call. Remarks For DotNetModule objects, use this method instead of the Module.CreateCode method. This method creates a method i

### DotNetCall.CreateCode

#### Syntax

[DotNetCall](dotnetcall.html).CreateCode

#### Return Value

[Boolean](data-types-for-teststand.html)

Specifies whether the
 DotNetCall
 object was modified.

#### Purpose

Launches Microsoft Visual Studio to create code for the .NET call.

#### Remarks

For
 [DotNetModule](dotnetmodule.html)
 objects, use this method instead of the
 [Module.CreateCode](module-createcode.html)
 method.

This method creates a method in the class the
 [DotNetCall.ClassName](dotnetcall-classname.html)
 property specifies. This method uses the
 [DotNetCall.MemberName](dotnetcall-membername.html)
 property as the name of the method to create. The content of the code depends on the code templates configured for the step type of the step that contains the
 DotNetCall
 object. Use the
 [Module.CanCreateCode](module-cancreatecode.html)
 property to determine whether this step can create code.

If you do not specify any files for the
 [DotNetModule.ProjectFilePath](dotnetmodule-projectfilepath.html)
 or
 [DotNetModule.SourceFilePath](dotnetmodule-sourcefilepath.html)
 properties, call this method to prompt the user to specify the project and source files. The adapter stores the specified project file in the step, but the source file you select applies only to the current .NET call.

When you call this method, you might receive additional prompts to determine whether any of the following conditions exist:

- Multiple versions of Visual Studio exist on the computer and you select the
 Always Prompt for Version 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the
 .NET Adapter Configuration 
 dialog box.
- Multiple versions of Visual Studio exist on the computer and you select the
 use the Version that Matches the Project File 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the .NET Adapter Configuration dialog box, and TestStand cannot match the version of the file.
- A method already exists with the same signature.
- The specified solution does not contain the specified project.
- The specified project does not contain the specified source file.

#### See Also

[.NET Adapter Configuration dialog box](../tsref/net-adapter-configuration-dialog-box.html)

[DotNetCall.ClassName](dotnetcall-classname.html)

[DotNetCall.EditCode](dotnetcall-editcode.html)

[DotNetCall.MemberName](dotnetcall-membername.html)

[DotNetModule](dotnetmodule.html)

[DotNetModule.ProjectFilePath](dotnetmodule-projectfilepath.html)

[DotNetModule.SourceFilePath](dotnetmodule-sourcefilepath.html)

[Module.CanCreateCode](module-cancreatecode.html)

[Module.CreateCode](module-createcode.html)

[Step.CanCreateCode](step-cancreatecode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-editcode.html language=enus -->
## TOPIC 00572: DotNetCall.EditCode

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-editcode.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-editcode.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.EditCode Return Value Boolean Purpose Attempts to launch Microsoft Visual Studio to edit the code associated with the .NET call. Remarks For DotNetModule objects, use this method instead of the Module.EditCode method. Use the Module.CanCreateCode property to determine whether this

### DotNetCall.EditCode

#### Syntax

[DotNetCall](dotnetcall.html).EditCode

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Attempts to launch Microsoft Visual Studio to edit the code associated with the .NET call.

#### Remarks

For
 [DotNetModule](dotnetmodule.html)
 objects, use this method instead of the
 [Module.EditCode](module-editcode.html)
 method.

Use the
 [Module.CanCreateCode](module-cancreatecode.html)
 property to determine whether this step can edit code.

If you do not specify any files for the
 [DotNetModule.ProjectFilePath](dotnetmodule-projectfilepath.html)
 or
 [DotNetModule.SourceFilePath](dotnetmodule-sourcefilepath.html)
 properties, call this method to prompt the user to specify the project and source files. The adapter stores the specified project file in the step, but the source file you select applies only to the current .NET call.

When you call this method, you might receive additional prompts to determine whether any of the following conditions exist:

- Multiple versions of Visual Studio exist on the computer and you select the
 Always Prompt for Version 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the
 .NET Adapter Configuration 
 dialog box.
- Multiple versions of Visual Studio exist on the computer and you select the
 use the Version that Matches the Project File 
 option from the Version of Visual Studio to Use for Create and Edit Code ring control in the .NET Adapter Configuration dialog box, and TestStand cannot match the version of the file.
- The specified solution does not contain the specified project.
- The specified project does not contain the specified source file.

#### See Also

[.NET Adapter Configuration dialog box](../tsref/net-adapter-configuration-dialog-box.html)

[DotNetCall.ClassName](dotnetcall-classname.html)

[DotNetCall.EditCode](dotnetcall-editcode.html)

[DotNetCall.MemberName](dotnetcall-membername.html)

[DotNetModule](dotnetmodule.html)

[DotNetModule.ProjectFilePath](dotnetmodule-projectfilepath.html)

[DotNetModule.SourceFilePath](dotnetmodule-sourcefilepath.html)

[Module.CanCreateCode](module-cancreatecode.html)

[Module.EditCode](module-editcode.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-getassembly.html language=enus -->
## TOPIC 00573: DotNetCall.GetAssembly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-getassembly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-getassembly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.GetAssembly( assemblyLocationParam, assemblyPathParam) Purpose Returns the pathname of the assembly. Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported. Remarks Returns the assembly that contains the type information for

### DotNetCall.GetAssembly

#### Syntax

[DotNetCall](dotnetcall.html).GetAssembly( assemblyLocationParam, assemblyPathParam)

#### Purpose

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Remarks

Returns the assembly that contains the type information for the class that corresponds to the
 [DotNetCall.ClassName](dotnetcall-classname.html)
 property. All calls before this call in the
 [DotNetCalls](dotnetcalls.html)
 collection must be valid before calling this method.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[Out] Returns a value that indicates whether the assembly is in a file or in the GAC.

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[Out] Returns the pathname of the assembly.

#### See Also

[DotNetCall.ClassName](dotnetcall-classname.html)

[DotNetCall.GetAssemblyForNextCall](dotnetcall-getassemblyfornextcall.html)

[DotNetCalls](dotnetcalls.html)

[DotNetModule.GetAssembly](dotnetmodule-getassembly.html)

[DotNetModule.SetAssembly](dotnetmodule-setassembly.html)

[DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-getassemblyfornextcall.html language=enus -->
## TOPIC 00574: DotNetCall.GetAssemblyForNextCall

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-getassemblyfornextcall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-getassemblyfornextcall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.GetAssemblyForNextCall( assemblyLocationParam, assemblyPathParam) Purpose Obtains assembly information for a subsequent call based on the return value for the current call and all previous calls in the call chain. This method returns the pathname of the assembly. Starting with Test

### DotNetCall.GetAssemblyForNextCall

#### Syntax

[DotNetCall](dotnetcall.html).GetAssemblyForNextCall( assemblyLocationParam, assemblyPathParam)

#### Purpose

Obtains assembly information for a subsequent call based on the return value for the current call and all previous calls in the call chain. This method returns the pathname of the assembly.

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Remarks

If the current or any previous
 DotNetCall
 object in the call chain does not have a return value or does not return a callable type, this method returns an error.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[Out] Returns a value that indicates whether the assembly is located in a file or in the GAC.

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[Out] Returns the pathname of the assembly.

#### See Also

[DotNetCall.GetAssembly](dotnetcall-getassembly.html)

[DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-iscallvalid.html language=enus -->
## TOPIC 00575: DotNetCall.IsCallValid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-iscallvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-iscallvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.IsCallValid( errorDescription) Return Value Boolean Purpose Returns True if the DotNetCall object specification matches the actual member found in the corresponding class and assembly. Otherwise, returns False . Remarks This method also returns False when the .NET Adapter cannot lo

### DotNetCall.IsCallValid

#### Syntax

[DotNetCall](dotnetcall.html).IsCallValid( errorDescription)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the
 DotNetCall
 object specification matches the actual member found in the corresponding class and assembly. Otherwise, returns
 False
 .

#### Remarks

This method also returns
 False
 when the .NET Adapter cannot load the assembly or the class or member name does not exist.

#### Parameters

errorDescription
 As
 [String](data-types-for-teststand.html)

[Out] If this method returns
 False
 , this parameter returns the explanation.

#### See Also

[DotNetCall.IsPrototypeIncompatible](dotnetcall-isprototypeincompatible.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-isprototypeincompatible.html language=enus -->
## TOPIC 00576: DotNetCall.IsPrototypeIncompatible

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-isprototypeincompatible.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-isprototypeincompatible.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.IsPrototypeIncompatible Data Type Boolean Purpose Returns a value that indicates whether the DotNetCall object prototype is incompatible with the actual prototype of the .NET member in the assembly. Remarks If this property cannot determine the prototype information because the ass

### DotNetCall.IsPrototypeIncompatible

#### Syntax

[DotNetCall](dotnetcall.html).IsPrototypeIncompatible

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the
 DotNetCall
 object prototype is incompatible with the actual prototype of the .NET member in the assembly.

#### Remarks

If this property cannot determine the prototype information because the assembly is not loadable, the class does not exist, or no member with the specified name exists, this property returns
 False
 . This property returns
 True
 only when a member with the specified name exists in the specified assembly and class, but does not match the specified prototype.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetCall.UnmappedArgumentValues](dotnetcall-unmappedargumentvalues.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-loadprototypefromsignature.html language=enus -->
## TOPIC 00577: DotNetCall.LoadPrototypeFromSignature

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-loadprototypefromsignature.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-loadprototypefromsignature.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.LoadPrototypeFromSignature( signatureOrMemberName, allowMemberNameMatching, options = 0) Return Value Boolean Purpose Returns True if the .NET Adapter successfully loaded the prototype for the specified call. This method returns False if the adapter cannot find the signature or mem

### DotNetCall.LoadPrototypeFromSignature

#### Syntax

[DotNetCall](dotnetcall.html).LoadPrototypeFromSignature( signatureOrMemberName, allowMemberNameMatching, options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns
 True
 if the .NET Adapter successfully loaded the prototype for the specified call. This method returns
 False
 if the adapter cannot find the signature or member name. This method loads the parameters and prototype information for a .NET member given the signature or name of the member.

#### Remarks

This method replaces the obsolete
 [DotNetModule.LoadPrototypeFromMetadataToken](dotnetmodule-loadprototypefrommetadatatoken.html)
 method.

This method is the primary mechanism for specify
 DotNetCall
 member prototypes. TestStand finds the member in the assembly that matches the given signature (or member name if you pass
 True
 for the
 allowMemberNameMatching
 parameter) and loads the prototype while setting all parameters and member information for the call. Use the suffix
 - Get
 or
 - Set
 to specify a get or set property or field operation. When you specify a property or field, you can omit the suffix and TestStand attempts to find a match by giving priority to properties with a
 - Get
 suffix. This behavior occurs even when you pass
 False
 for the
 allowMemberNameMatching
 parameter.

Note

True

allowMemberNameMatching

Use the following guidelines to specify a signature string:

- For methods and constructors 
 —Specify the method or class name followed by the data types of the parameters in parentheses, separated by commas. For example:
 MyClass(Int32, System.String[] ByRef) 
 MyMethod(MyNamespace.MyClass ByRef, Double, Int32[,] ByRef) 
 Use the
 DotNetAdapter.GetMemberNames 
 method to obtain a list of signatures for a particular assembly and class or to review more examples of the format for signatures.
- For Use Existing Objects calls 
 —To use an existing object reference, pass
 Use Existing Object(MyNameSpace.MyClass) 
 , such as
 Use Existing Object(System.Collections.Queue) 
 . The .NET Adapter treats the class name as a parameter and uses it to specify the TestStand variable that holds the object reference you want to use.
- For properties and fields 
 —If a property or field does not have an indexer, specify the property or field name followed by the
 - Get 
 or
 - Set 
 suffix to specify the type of operation to perform, as in
 MyProperty - Get 
 or
 MyField - Set 
 . If a property or field does have an indexer, add a space after the property name and add square brackets with the indexer types specified in a comma-separated list, as in:
 MyPropertyWithIndexers [Int32, System.String ByRef] - Get 
 .
- For parameter strings 
 —For basic types other than
 System.String 
 , such as 32-bit integers and doubles, omit the
 System. 
 prefix. For arrays, include the square brackets with commas inside to specify the number of dimensions. For
 ByRef 
 and output parameters, include the string
 ByRef 
 , including the initial space, after the parameter data type.

#### Signatures for the First Call in the Collection

You can set the first call in the collection only to a constructor or static member or use an existing object.

Note

Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.

#### Example Signature Formats for System.String Class Members

- Simple member name 
 —
 Replace 
 . No overload exists for this method so the adapter requires only a simple name (as long as you pass
 True 
 for the
 allowMemberNameMatching 
 parameter).
- Full signature with parameter types 
 —
 Split(Char[], Int32, System.StringSplitOptions) 
 . Overloads exist for this method, so the adapter requires the full signature to choose a specific overload (even if you pass
 True 
 for the
 allowMemberNameMatching 
 parameter). Note that
 Char 
 and
 Int32 
 types do not have the
 System. 
 prefix before the type name because they are basic types.
- Property simple member name 
 —
 Length 
 . This property is read-only so the adapter does not require the
 - Get 
 suffix because
 Get 
 is the only option.
- Property 
 —
 Length - Get 
 . If this property has both public read access and public write access, the adapter requires the
 - Get 
 or
 - Set 
 suffix to specify the operation to perform. However, if no suffix is provided, the adapter chooses
 - Get 
 by default.
- Constructor 
 —
 String(Char[], Int32, Int32) 
 . Multiple constructors exist so the adapter requires a full signature to specify a specific constructor. If only one public constructor exists, you can pass
 String 
 as the signature (as long as you pass
 True 
 for the
 allowMemberNameMatching 
 parameter).

#### Parameters

signatureOrMemberName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the signature or member name of the member with the prototype you want to load. If you want to pass a member name instead of a full signature, you must also pass
 True
 for the
 allowMemberNameMatching
 parameter.

allowMemberNameMatching
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to allow matching simply by member name instead of requiring a match to the full signature. If you pass
 False
 for this parameter, the .NET Adapter loads the prototype only if the
 signatureOrMemberName
 parameter exactly matches the full signature of a member. If you pass
 True
 for this parameter, the adapter first looks for a full signature match to the
 signatureOrMemberName
 parameter. If the adapter cannot find a match, it looks for a member name that matches the
 signatureOrMemberName
 parameter. To choose a specific overload, you must specify a signature instead of a member name. Refer to the
 Remarks
 section of this topic for more information about specifying a signature.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [LoadPrototypeOptions](loadprototypeoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

This parameter has a default value of
 0
 .

#### See Also

[DotNetCall.IsCallValid](dotnetcall-iscallvalid.html)

[DotNetCall.IsPrototypeIncompatible](dotnetcall-isprototypeincompatible.html)

[DotNetCall.SetIncompleteSignature](dotnetcall-setincompletesignature.html)

[LoadPrototypeOptions](loadprototypeoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-memberflags.html language=enus -->
## TOPIC 00578: DotNetCall.MemberFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-memberflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-memberflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.MemberFlags Data Type Long Purpose Returns certain attributes of the member the DotNetCall object calls. Use the DotNetCall.LoadPrototypeFromSignature method to change the member specifications for a DotNetCall object. See Also DotNetCall.LoadPrototypeFromSignature DotNetMemberFlag

### DotNetCall.MemberFlags

#### Syntax

[DotNetCall](dotnetcall.html).MemberFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns certain attributes of the member the
 DotNetCall
 object calls. Use the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method to change the member specifications for a
 DotNetCall
 object.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetMemberFlags](dotnetmemberflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-memberhelpstring.html language=enus -->
## TOPIC 00579: DotNetCall.MemberHelpString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-memberhelpstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-memberhelpstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.MemberHelpString Data Type String Purpose Returns the help string the assembly associates with the member. See Also DotNetCall.ClassHelpString DotNetCall.MemberName

### DotNetCall.MemberHelpString

#### Syntax

[DotNetCall](dotnetcall.html).MemberHelpString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the help string the assembly associates with the member.

#### See Also

[DotNetCall.ClassHelpString](dotnetcall-classhelpstring.html)

[DotNetCall.MemberName](dotnetcall-membername.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-membername.html language=enus -->
## TOPIC 00580: DotNetCall.MemberName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-membername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-membername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.MemberName Data Type String Purpose Returns the name of the member function to call or property or field to access. Use the DotNetCall.LoadPrototypeFromSignature method to change the member specifications for a DotNetCall object. See Also DotNetCall.ClassName DotNetCall.LoadPrototy

### DotNetCall.MemberName

#### Syntax

[DotNetCall](dotnetcall.html).MemberName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the member function to call or property or field to access. Use the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method to change the member specifications for a
 DotNetCall
 object.

#### See Also

[DotNetCall.ClassName](dotnetcall-classname.html)

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetCall.MemberType](dotnetcall-membertype.html)

[DotNetCall.Signature](dotnetcall-signature.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-membertype.html language=enus -->
## TOPIC 00581: DotNetCall.MemberType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-membertype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-membertype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.MemberType Data Type DotNetModuleMemberTypes Use the following constants with this data type: DotNetMember_CallConstructor –(Value: 4) Specifies that the DotNetCall object calls a constructor. DotNetMember_CallMethod –(Value: 1) Specifies that the DotNetCall object calls a method.

### DotNetCall.MemberType

#### Syntax

[DotNetCall](dotnetcall.html).MemberType

#### Data Type

[DotNetModuleMemberTypes](dotnetmodulemembertypes.html)

Use the following constants with this data type:

- DotNetMember_CallConstructor 
 –(Value: 4) Specifies that the
 DotNetCall 
 object calls a constructor.
- DotNetMember_CallMethod 
 –(Value: 1) Specifies that the
 DotNetCall 
 object calls a method.
- DotNetMember_CreateRemote 
 –(Value: 5) Specifies that the
 DotNetCall 
 object creates a remote object.
 Note 
 Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.
- DotNetMember_DoNotCall 
 –(Value: 0) Specifies that you have not completely specified the
 DotNetCall 
 object and that the object does not call a method or access a property or field.
- DotNetMember_GetProperty 
 –(Value: 2) Specifies that the
 DotNetCall 
 object gets a property.
- DotNetMember_SetProperty 
 –(Value: 3) Specifies that the
 DotNetCall 
 object sets a property.
- DotNetMember_UseExisting 
 –(Value: 6) Specifies that the
 DotNetCall 
 object uses an existing object a TestStand variable specifies as the .NET object on which to make the next call.

#### Purpose

Returns the type of call the current
 DotNetCall
 object is configured to make. Use the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method to change the member specifications for a
 DotNetCall
 object.

#### See Also

[DotNetCall.MemberName](dotnetcall-membername.html)

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModuleMemberTypes](dotnetmodulemembertypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-parameters.html language=enus -->
## TOPIC 00582: DotNetCall.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.Parameters Data Type DotNetParameters Purpose Returns the DotNetParameters collection that contains a list of the current parameters used as inputs and outputs for the corresponding DotNetCall object. Use the DotNetCall.LoadPrototypeFromSignature method to change the member specifi

### DotNetCall.Parameters

#### Syntax

[DotNetCall](dotnetcall.html).Parameters

#### Data Type

[DotNetParameters](dotnetparameters.html)

#### Purpose

Returns the
 [DotNetParameters](dotnetparameters.html)
 collection that contains a list of the current parameters used as inputs and outputs for the corresponding
 DotNetCall
 object. Use the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method to change the member specification and parameters for a
 DotNetCall
 object.

#### Remarks

Call the
 DotNetCall.LoadPrototypeFromSignature
 method to specify a call before accessing this property.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetParameters](dotnetparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-reloadprototype.html language=enus -->
## TOPIC 00583: DotNetCall.ReloadPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-reloadprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-reloadprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.ReloadPrototype( options = 0) Return Value Boolean Purpose Attempts to reload prototype information for the selected member, including parameter types and return value types. For each parameter, this method updates in/out information, struct definitions, and array dimensions, if ap

### DotNetCall.ReloadPrototype

#### Syntax

[DotNetCall](dotnetcall.html).ReloadPrototype( options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Attempts to reload prototype information for the selected member, including parameter types and return value types. For each parameter, this method updates in/out information, struct definitions, and array dimensions, if applicable.

#### Remarks

If the .NET Adapter cannot find an assembly, class, or member anywhere in the call chain up to and including the current call, this method returns an error.

#### Parameters

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [LoadPrototypeOptions](loadprototypeoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

This parameter has a default value of
 0
 .

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[LoadPrototypeOptions](loadprototypeoptions.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-setincompletesignature.html language=enus -->
## TOPIC 00584: DotNetCall.SetIncompleteSignature

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-setincompletesignature.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-setincompletesignature.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.SetIncompleteSignature( partialSignature) Purpose Stores the given partial signature for the .NET call as the member name, but does not attempt to actually load the prototype. Instead, this method clears parameters and sets the DotNetCall.MemberType property to DotNetMember_DoNotCa

### DotNetCall.SetIncompleteSignature

#### Syntax

[DotNetCall](dotnetcall.html).SetIncompleteSignature( partialSignature)

#### Purpose

Stores the given partial signature for the .NET call as the member name, but does not attempt to actually load the prototype. Instead, this method clears parameters and sets the
 [DotNetCall.MemberType](dotnetcall-membertype.html)
 property to
 [DotNetMember_DoNotCall](dotnetmodulemembertypes.html)
 .

#### Remarks

Use this method to store signature information on a
 DotNetCall
 object without trying to actually load prototype for the call. For example, if the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method cannot load the prototype for a given signature, you can store the signature on the
 DotNetCall
 object by calling this method.

#### Parameters

partialSignature
 As
 [String](data-types-for-teststand.html)

[In] Specifies the partial signature to store on the
 DotNetCall
 object.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetCall.MemberType](dotnetcall-membertype.html)

[DotNetModuleMemberTypes](dotnetmodulemembertypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-signature.html language=enus -->
## TOPIC 00585: DotNetCall.Signature

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-signature.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-signature.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.Signature Data Type String Purpose Returns the signature of the specified .NET member. Use the DotNetCall.LoadPrototypeFromSignature method to specify a signature for a call. See Also DotNetCall.LoadPrototypeFromSignature

### DotNetCall.Signature

#### Syntax

[DotNetCall](dotnetcall.html).Signature

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the signature of the specified .NET member. Use the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method to specify a signature for a call.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall-unmappedargumentvalues.html language=enus -->
## TOPIC 00586: DotNetCall.UnmappedArgumentValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall-unmappedargumentvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall-unmappedargumentvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCall.UnmappedArgumentValues Data Type UnmappedArgumentValues Purpose Returns the UnmappedArgumentValues collection that contains a list of the arguments not used as inputs or outputs for the corresponding DotNetCall object. Remarks For DotNetModule objects, use this property instead of

### DotNetCall.UnmappedArgumentValues

#### Syntax

[DotNetCall](dotnetcall.html).UnmappedArgumentValues

#### Data Type

[UnmappedArgumentValues](unmappedargumentvalues.html)

#### Purpose

Returns the
 [UnmappedArgumentValues](unmappedargumentvalues.html)
 collection that contains a list of the arguments not used as inputs or outputs for the corresponding
 DotNetCall
 object.

#### Remarks

For
 [DotNetModule](dotnetmodule.html)
 objects, use this property instead of the
 [Module.UnmappedArgumentValues](module-unmappedargumentvalues.html)
 property.

When you use the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method to change a
 DotNetCall
 object prototype and pass the
 [LoadPrototypeOption_MapExistingParameters](loadprototypeoptions.html)
 option, TestStand attempts to map the current
 DotNetCall
 arguments to the new prototype by looking for matching argument names and data types and by matching argument positions and data types. If TestStand cannot assign an argument to the new prototype or if you do not pass the
 LoadPrototypeOption_MapExistingParameters
 option, the argument is added the current collection.

TestStand does not clear the collection when you load a new prototype. Use the
 [UnmappedArgumentValues.Clear](unmappedargumentvalues-clear.html)
 method to clear the collection after you call the
 DotNetCall.LoadPrototypeFromSignature
 method.

#### See Also

[Module.UnmappedArgumentValues](module-unmappedargumentvalues.html)

[UnmappedArgumentValue](unmappedargumentvalue.html)

[UnmappedArgumentValues](unmappedargumentvalues.html)

[UnmappedArgumentValues.Clear](unmappedargumentvalues-clear.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcall.html language=enus -->
## TOPIC 00587: DotNetCall

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DotNetCall class to specify and obtain .NET Adapter-specific information about the code module that steps or step type substeps execute. Typically, you use this class only when you are writing a sequence editor. You can use the DotNetCall.LoadPrototypeFromSignature method to loa

### DotNetCall

Use objects from the DotNetCall class to specify and obtain .NET Adapter-specific information about the code module that steps or step type substeps execute.

Typically, you use this class only when you are writing a sequence editor.

You can use the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method to load the prototype for the call.

#### Properties

| CallIndex (Read Only) |
| --- |
| ClassHelpString (Read Only) |
| ClassName (Read Only) |
| ClassNameForNextCall (Read Only) |
| IsPrototypeIncompatible (Read Only) |
| MemberFlags (Read Only) |
| MemberHelpString (Read Only) |
| MemberName (Read Only) |
| MemberType (Read Only) |
| Parameters (Read Only) |
| Signature (Read Only) |
| UnmappedArgumentValues (Read Only) |

#### Methods

| CreateCode |
| --- |
| EditCode |
| GetAssembly |
| GetAssemblyForNextCall |
| IsCallValid |
| LoadPrototypeFromSignature |
| ReloadPrototype |
| SetIncompleteSignature |

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule](dotnetmodule.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcalls-clear.html language=enus -->
## TOPIC 00588: DotNetCalls.Clear

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcalls-clear.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcalls-clear.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCalls.Clear Purpose Removes all items from the collection.

### DotNetCalls.Clear

#### Syntax

[DotNetCalls](dotnetcalls.html).Clear

#### Purpose

Removes all items from the collection.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcalls-count.html language=enus -->
## TOPIC 00589: DotNetCalls.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcalls-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcalls-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCalls.Count Data Type Long Purpose Returns the number of items in the collection. See Also DotNetCall

### DotNetCalls.Count

#### Syntax

[DotNetCalls](dotnetcalls.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[DotNetCall](dotnetcall.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcalls-delete.html language=enus -->
## TOPIC 00590: DotNetCalls.Delete

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcalls-delete.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcalls-delete.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCalls.Delete( index) Purpose Removes the DotNetCall object at the specified index from the DotNetCalls collection. Parameters index As Long [In] Specifies the zero-based index of the DotNetCall object to remove from the DotNetCalls collection. See Also DotNetCall

### DotNetCalls.Delete

#### Syntax

[DotNetCalls](dotnetcalls.html).Delete( index)

#### Purpose

Removes the
 [DotNetCall](dotnetcall.html)
 object at the specified index from the
 DotNetCalls
 collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the
 DotNetCall
 object to remove from the
 DotNetCalls
 collection.

#### See Also

[DotNetCall](dotnetcall.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcalls-deleteallafterindex.html language=enus -->
## TOPIC 00591: DotNetCalls.DeleteAllAfterIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcalls-deleteallafterindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcalls-deleteallafterindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCalls.DeleteAllAfterIndex( index) Purpose Removes all items after, but not including, the specified index from the collection. Parameters index As Long [In] Specifies the zero-based index after which this method removes all DotNetCall objects from the collection. See Also DotNetCall

### DotNetCalls.DeleteAllAfterIndex

#### Syntax

[DotNetCalls](dotnetcalls.html).DeleteAllAfterIndex( index)

#### Purpose

Removes all items after, but not including, the specified index from the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index after which this method removes all
 [DotNetCall](dotnetcall.html)
 objects from the collection.

#### See Also

[DotNetCall](dotnetcall.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcalls-item.html language=enus -->
## TOPIC 00592: DotNetCalls.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcalls-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcalls-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCalls.Item( index) Data Type DotNetCall Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Long [In] Specifies the zero-based index of the item to retrieve. See Also DotNetCall

### DotNetCalls.Item

#### Syntax

[DotNetCalls](dotnetcalls.html).Item( index)

#### Data Type

[DotNetCall](dotnetcall.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[DotNetCall](dotnetcall.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcalls-new.html language=enus -->
## TOPIC 00593: DotNetCalls.New

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcalls-new.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcalls-new.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetCalls.New( index) Purpose Creates a new DotNetCall object and inserts it into the collection at the specified index. Parameters index As Long [In] Specifies the zero-based index at which to insert the new DotNetCall object into the collection. See Also DotNetCall

### DotNetCalls.New

#### Syntax

[DotNetCalls](dotnetcalls.html).New( index)

#### Purpose

Creates a new
 [DotNetCall](dotnetcall.html)
 object and inserts it into the collection at the specified index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index at which to insert the new DotNetCall object into the collection.

#### See Also

[DotNetCall](dotnetcall.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetcalls.html language=enus -->
## TOPIC 00594: DotNetCalls

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetcalls.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetcalls.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DotNetCalls class to configure and obtain calls for a module the .NET Adapter uses. Use the DotNetModule.Calls property to obtain the collection of calls for a module. Properties Count (Read Only) Item (Read Only) Methods Clear Delete DeleteAllAfterIndex New See Also DotNetCall

### DotNetCalls

Use objects from the DotNetCalls class to configure and obtain calls for a module the .NET Adapter uses. Use the
 [DotNetModule.Calls](dotnetmodule-calls.html)
 property to obtain the collection of calls for a module.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Clear |
| --- |
| Delete |
| DeleteAllAfterIndex |
| New |

#### See Also

[DotNetCall](dotnetcall.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmemberflags.html language=enus -->
## TOPIC 00595: DotNetMemberFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmemberflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmemberflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the following constants with the DotNetCall.MemberFlags property to determine certain attributes of the member the DotNetCall object calls. Use the bitwise-AND operator to determine whether any of these flags are set when obtaining the property value. DotNetMemberFlags_Static –(Value: 0x1) Indic

### DotNetMemberFlags

Use the following constants with the
 [DotNetCall.MemberFlags](dotnetcall-memberflags.html)
 property to determine certain attributes of the member the
 [DotNetCall](dotnetcall.html)
 object calls. Use the bitwise-AND operator to determine whether any of these flags are set when obtaining the property value.

- DotNetMemberFlags_Static 
 –(Value: 0x1) Indicates that the member is a static member. A static member does not use or require a class instance. A static member can access only static data on its class.
- DotNetMemberFlags_TopLevel 
 –(Value: 0x2) Indicates whether the adapter shows members that are at a base class level when specifying the module. This flag is obsolete and will never be set. Instead, the adapter always shows and supports calling base class members.

#### See Also

[DotNetCall.MemberFlags](dotnetcall-memberflags.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-allowunload.html language=enus -->
## TOPIC 00596: DotNetModule.AllowUnload

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-allowunload.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-allowunload.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.AllowUnload Data Type Boolean Purpose When AllowUnload is true (default), the assemblies specified in the module are loaded into a collectible AssemblyLoadContext and can be unloaded by calling UnloadAllModules. When AllowUnload is false, the assemblies are not loaded into a coll

### DotNetModule.AllowUnload

#### Syntax

[DotNetModule](dotnetmodule.html).AllowUnload

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

When AllowUnload is true (default), the assemblies specified in the module are loaded into a collectible AssemblyLoadContext and can be unloaded by calling UnloadAllModules. When AllowUnload is false, the assemblies are not loaded into a collectible AssemblyLoadContext and can't be unloaded. 
 C++/CLI (mixed mode assemblies) can't be loaded into a collectible AssemblyLoadContext. Setting this option to false allows TestStand to load and run C++/CLI assemblies from a .NET module.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-asmodule.html language=enus -->
## TOPIC 00597: DotNetModule.AsModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-asmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-asmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.AsModule Return Value Module Purpose Returns the underlying Module object that represents the DotNetModule object. Remarks Use the Module object to access properties and methods common to all modules. See Also Module

### DotNetModule.AsModule

#### Syntax

[DotNetModule](dotnetmodule.html).AsModule

#### Return Value

[Module](module.html)

#### Purpose

Returns the underlying Module object that represents the DotNetModule object.

#### Remarks

Use the Module object to access properties and methods common to all modules.

#### See Also

[Module](module.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-assemblywarnings.html language=enus -->
## TOPIC 00598: DotNetModule.AssemblyWarnings

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-assemblywarnings.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-assemblywarnings.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.AssemblyWarnings Data Type String Purpose Returns warning messages, if any, associated with the use of the currently specified assembly. Returns an empty string if no warnings exist or if TestStand could not load the assembly.

### DotNetModule.AssemblyWarnings

#### Syntax

[DotNetModule](dotnetmodule.html).AssemblyWarnings

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns warning messages, if any, associated with the use of the currently specified assembly. Returns an empty string if no warnings exist or if TestStand could not load the assembly.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-calls.html language=enus -->
## TOPIC 00599: DotNetModule.Calls

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-calls.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-calls.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.Calls Data Type DotNetCalls Purpose Returns the collection of calls for the module.

### DotNetModule.Calls

#### Syntax

[DotNetModule](dotnetmodule.html).Calls

#### Data Type

[DotNetCalls](dotnetcalls.html)

#### Purpose

Returns the collection of calls for the module.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-classhelpstring.html language=enus -->
## TOPIC 00600: DotNetModule.ClassHelpString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-classhelpstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-classhelpstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ClassHelpString Data Type String Purpose Returns the help string the assembly associates with the selected class. See Also DotNetCall.MemberHelpString DotNetModule.ClassName

### DotNetModule.ClassHelpString

#### Syntax

[DotNetModule](dotnetmodule.html).ClassHelpString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the help string the assembly associates with the selected class.

#### See Also

[DotNetCall.MemberHelpString](dotnetcall-memberhelpstring.html)

[DotNetModule.ClassName](dotnetmodule-classname.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-classname.html language=enus -->
## TOPIC 00601: DotNetModule.ClassName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-classname.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-classname.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ClassName Data Type String Purpose Specifies the full type name, including the namespace, of the root class to which the first DotNetCall applies. See Also DotNetCall

### DotNetModule.ClassName

#### Syntax

[DotNetModule](dotnetmodule.html).ClassName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the full type name, including the namespace, of the root class to which the first
 [DotNetCall](dotnetcall.html)
 applies.

#### See Also

[DotNetCall](dotnetcall.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-classreference.html language=enus -->
## TOPIC 00602: DotNetModule.ClassReference

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-classreference.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-classreference.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ClassReference Data Type String Purpose This method is obsolete . Create a Use Existing Object or constructor call as the first call in the module and specify a value for the first parameter instead of using this property. Starting with TestStand 2024 Q4, 'Create Remote Object' i

### DotNetModule.ClassReference

#### Syntax

[DotNetModule](dotnetmodule.html).ClassReference

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

obsolete

Use Existing Object

Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.

#### Remarks

Specifies a variable or property for a reference to the class instance or struct definition to call. If the object being called is an instance of a class, the instance can be stored in an object reference variable. If the object being called is a struct, the members of the struct can be stored in an object reference variable or a variable of a data type that has mapping defined for the struct.

#### See Also

[DotNetModule.LoadPrototypeFromMetadataToken](dotnetmodule-loadprototypefrommetadatatoken.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-clearunmappedconstructorargument.html language=enus -->
## TOPIC 00603: DotNetModule.ClearUnmappedConstructorArgumentValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-clearunmappedconstructorargument.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-clearunmappedconstructorargument.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ClearUnmappedConstructorArgumentValues Purpose This method is obsolete . The Use the DotNetCall.UnmappedArgumentValues method on a constructor call instead. Remarks Removes the items in the UnmappedArgumentValues collection. Clear the items if you do not want them available for t

### DotNetModule.ClearUnmappedConstructorArgumentValues

#### Syntax

[DotNetModule](dotnetmodule.html).ClearUnmappedConstructorArgumentValues

#### Purpose

Note

obsolete

DotNetCall.UnmappedArgumentValues

#### Remarks

Removes the items in the
 [UnmappedArgumentValues](unmappedargumentvalues.html)
 collection.

Clear the items if you do not want them available for the next prototype change.

#### See Also

[DotNetCall.UnmappedArgumentValues](dotnetcall-unmappedargumentvalues.html)

[DotNetModule.UnmappedConstructorArgumentValues](dotnetmodule-unmappedconstructorargumentvalue.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

[UnmappedArgumentValues](unmappedargumentvalues.html)

Parent topic:

Obsolete DotNetModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-constructorindex.html language=enus -->
## TOPIC 00604: DotNetModule.ConstructorIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-constructorindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-constructorindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ConstructorIndex Data Type Long Purpose This property is obsolete. Use the DotNetCall.LoadPrototypeFromSignature method instead. Remarks Specifies the index of the constructor the module invokes to create the reference. A class can contain more than one constructor. Constructors

### DotNetModule.ConstructorIndex

#### Syntax

[DotNetModule](dotnetmodule.html).ConstructorIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Specifies the index of the constructor the module invokes to create the reference. A class can contain more than one constructor. Constructors do not have names. This property specifies the currently selected constructor.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.GetConstructorMetadataToken](dotnetmodule-getconstructormetadatatoken.html)

[DotNetModule.LoadConstructorPrototypeFromMetadataToken](dotnetmodule-loadconstructorprototypefrommeta.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-constructorparameters.html language=enus -->
## TOPIC 00605: DotNetModule.ConstructorParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-constructorparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-constructorparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ConstructorParameters Data Type DotNetParameters The collection of parameters. Purpose This property is obsolete . Use a constructor as the first call in the DotNetModule class and then use the DotNetCall.Parameters property instead. You can specify a constructor by adding a call

### DotNetModule.ConstructorParameters

#### Syntax

[DotNetModule](dotnetmodule.html).ConstructorParameters

#### Data Type

[DotNetParameters](dotnetparameters.html)

The collection of parameters.

#### Purpose

Note

obsolete

DotNetModule

DotNetCall.Parameters

DotNetModule.Calls

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Returns the DotNetParameters collection that contains a list of the current parameters used as inputs and outputs of the constructor.

Call the
 [DotNetModule.LoadConstructorPrototypeFromMetadataToken](dotnetmodule-loadconstructorprototypefrommeta.html)
 method before accessing this property.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetCall.Parameters](dotnetcall-parameters.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

[DotNetModule.CreateObject](dotnetmodule-createobject.html)

[DotNetModule.LoadConstructorPrototypeFromMetadataToken](dotnetmodule-loadconstructorprototypefrommeta.html)

[DotNetParameters](dotnetparameters.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-constructorprototype.html language=enus -->
## TOPIC 00606: DotNetModule.ConstructorPrototype

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-constructorprototype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-constructorprototype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ConstructorPrototype Data Type String Purpose This property is obsolete . Use the DotNetCall.Signature property instead. Remarks Returns a display string for the constructor prototype. See Also DotNetCall.Signature DotNetModule.ConstructorParameters DotNetModule.LoadConstructorPr

### DotNetModule.ConstructorPrototype

#### Syntax

[DotNetModule](dotnetmodule.html).ConstructorPrototype

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetCall.Signature

#### Remarks

Returns a display string for the constructor prototype.

#### See Also

[DotNetCall.Signature](dotnetcall-signature.html)

[DotNetModule.ConstructorParameters](dotnetmodule-constructorparameters.html)

[DotNetModule.LoadConstructorPrototypeFromMetaDataToken](dotnetmodule-loadconstructorprototypefrommeta.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-createobject.html language=enus -->
## TOPIC 00607: DotNetModule.CreateObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-createobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-createobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.CreateObject Data Type Boolean Purpose This property is obsolete . Use a constructor or a remote creation call as the first call in the DotNetModule class instead of setting this property to True . You can specify a constructor or remote creation call by adding a call to the modu

### DotNetModule.CreateObject

#### Syntax

[DotNetModule](dotnetmodule.html).CreateObject

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetModule

True

DotNetModule.Calls

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Specifies whether to create a new instance of the class.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

[DotNetModule.ConstructorParameters](dotnetmodule-constructorparameters.html)

[DotNetModule.DisposeObject](dotnetmodule-disposeobject.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-displaycreatecustomdatatypedialo.html language=enus -->
## TOPIC 00608: DotNetModule.DisplayCreateCustomDataTypeDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-displaycreatecustomdatatypedialo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-displaycreatecustomdatatypedialo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.DisplayCreateCustomDataTypeDialog( sequenceContext) Return Value Boolean Returns True if you click OK in the dialog box and False if you click Cancel . Purpose Launches the Create Custom Data Type from Struct dialog box, in which you can create a new data type that you can use as

### DotNetModule.DisplayCreateCustomDataTypeDialog

#### Syntax

[DotNetModule](dotnetmodule.html).DisplayCreateCustomDataTypeDialog( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box and
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Create Custom Data Type from Struct](../tsref/create-custom-data-type-from-struct-dialog-bo.html)
 dialog box, in which you can create a new data type that you can use as the reference that the module operates on.

#### Remarks

Call this method only if the class name specified for the module is a struct, otherwise this method returns without launching the Create Custom Data Type from Struct dialog box. Use the
 [DotNetModule.IsStruct](dotnetmodule-isstruct.html)
 property to determine whether the class name is a struct.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context the Create Custom Data Type from Struct dialog box uses to obtain information about the sequence file. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

#### See Also

[Create Custom Data Type from Struct dialog box](../tsref/create-custom-data-type-from-struct-dialog-bo.html)

[DotNetModule.IsStruct](dotnetmodule-isstruct.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-disposeobject.html language=enus -->
## TOPIC 00609: DotNetModule.DisposeObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-disposeobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-disposeobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.DisposeObject Data Type Boolean Purpose This property is obsolete . Use a constructor or a remote creation call as the first call in the DotNetModule class and then use the DotNetParameter.DisposeObject property on the return value parameter instead. You can specify a constructor

### DotNetModule.DisposeObject

#### Syntax

[DotNetModule](dotnetmodule.html).DisposeObject

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetModule

DotNetParameter.DisposeObject

DotNetModule.Calls

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Specifies whether TestStand attempts to dispose of the object when the object is released or goes out of scope.

If the
 [DotNetModule.CreateObject](dotnetmodule-createobject.html)
 property is
 False
 or if the object does not implement the IDisposable interface, this property is ignored.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

[DotNetModule.CreateObject](dotnetmodule-createobject.html)

[DotNetParameter.DisposeObject](dotnetparameter-disposeobject.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-execute.html language=enus -->
## TOPIC 00610: DotNetModule.Execute

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-execute.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-execute.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.Execute( sequenceContextParam, argumentsParam) Purpose Use this method to call a .NET code module directly without using a step, sequence, or execution. Remarks When you call a .NET code module using this method, you can evaluate the parameter expressions to determine the argumen

### DotNetModule.Execute

#### Syntax

[DotNetModule](dotnetmodule.html).Execute( sequenceContextParam, argumentsParam)

#### Purpose

Use this method to call a .NET code module directly without using a step, sequence, or execution.

#### Remarks

When you call a .NET code module using this method, you can evaluate the parameter expressions to determine the argument values or specify the argument values directly using a
 [DotNetModuleArguments](dotnetmodulearguments.html)
 collection.

To use the parameter value expressions, pass a valid
 [SequenceContext](sequencecontext.html)
 object to the
 sequenceContextParam
 parameter to evaluate the
 [DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)
 expressions.

To pass specific argument values, use the
 [DotNetModule.NewModuleArguments](dotnetmodule-newmodulearguments.html)
 method to create a collection of
 [DotNetArguments](dotnetarguments.html)
 objects. Each
 DotNetArguments
 object in the collection is itself a collection of
 [DotNetArgument](dotnetargument.html)
 objects that represents the arguments to pass to the corresponding
 [DotNetCall](dotnetcall.html)
 object in the collection the
 [DotNetModule.Calls](dotnetmodule-calls.html)
 property returns. Set the
 [DotNetArgument.Value](dotnetargument-value.html)
 property on each item in the
 DotNetArguments
 collection to the argument value you want to pass to the
 DotNetCall
 object.

#### Parameters

sequenceContextParam
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the
 SequenceContext
 object this method uses to evaluate each of the
 DotNetParameter.ValueExpr
 expressions in the module parameters. Pass
 NULL
 for this parameter if you pass a
 DotNetModuleArguments
 collection to the
 argumentsParam
 parameter.

argumentsParam
 As
 [DotNetModuleArguments](dotnetmodulearguments.html)

[In] Specifies the collection of argument collections that contain the argument values to pass to each
 DotNetCall
 object. Pass
 NULL
 for this parameter to pass the values obtained from evaluating each of the
 DotNetParameter.ValueExpr
 expressions in the module parameters.

#### See Also

[DotNetArgument](dotnetargument.html)

[DotNetArgument.Value](dotnetargument-value.html)

[DotNetArguments](dotnetarguments.html)

[DotNetCall](dotnetcall.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

[DotNetModule.NewModuleArguments](dotnetmodule-newmodulearguments.html)

[DotNetModuleArguments](dotnetmodulearguments.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-getassembly.html language=enus -->
## TOPIC 00611: DotNetModule.GetAssembly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-getassembly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-getassembly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.GetAssembly( assemblyLocationParam, assemblyPathParam) Purpose Returns the pathname of the assembly. Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported. Parameters assemblyLocationParam As DotNetModuleAssemblyLocations

### DotNetModule.GetAssembly

#### Syntax

[DotNetModule](dotnetmodule.html).GetAssembly( assemblyLocationParam, assemblyPathParam)

#### Purpose

Returns the pathname of the assembly.

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[Out] Returns a value that indicates whether the assembly is located in a file or in the Global Assembly Cache.

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[Out] Returns the pathname of the assembly.

#### See Also

[DotNetModule.SetAssembly](dotnetmodule-setassembly.html)

[DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-getconstructormetadatatoken.html language=enus -->
## TOPIC 00612: DotNetModule.GetConstructorMetadataToken

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-getconstructormetadatatoken.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-getconstructormetadatatoken.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.GetConstructorMetadataToken Return Value Long Purpose This method is obsolete . The .NET Adapter no longer uses metadata tokens to load the prototype. Use the DotNetCall.LoadPrototypeFromSignature method to specify a signature for a call instead. Remarks Returns the metadata toke

### DotNetModule.GetConstructorMetadataToken

#### Syntax

[DotNetModule](dotnetmodule.html).GetConstructorMetadataToken

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Returns the metadata token for the specified constructor prototype. If the prototype is not compatible, the method returns
 -1
 .

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.GetMetadataToken](dotnetmodule-getmetadatatoken.html)

[DotNetModule.IsConstructorPrototypeIncompatible](dotnetmodule-isconstructorprototypeincompatib.html)

[DotNetModule.LoadConstructorPrototypeFromMetadataToken](dotnetmodule-loadconstructorprototypefrommeta.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-getmetadatatoken.html language=enus -->
## TOPIC 00613: DotNetModule.GetMetadataToken

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-getmetadatatoken.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-getmetadatatoken.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.GetMetadataToken Return Value Long Purpose This method is obsolete . The .NET Adapter no longer uses metadata tokens to load the prototype. Use the DotNetCall.LoadPrototypeFromSignature method to specify a signature for a call instead. Remarks Returns the metadata token for the s

### DotNetModule.GetMetadataToken

#### Syntax

[DotNetModule](dotnetmodule.html).GetMetadataToken

#### Return Value

[Long](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Returns the metadata token for the specified prototype. If the prototype is not compatible, the method returns
 -1
 .

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.GetConstructorMetadataToken](dotnetmodule-getconstructormetadatatoken.html)

[DotNetModule.LoadPrototypeFromMetadataToken](dotnetmodule-loadprototypefrommetadatatoken.html)

[Module.IsPrototypeIncompatible](module-isprototypeincompatible.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-isconstructorprototypeincompatib.html language=enus -->
## TOPIC 00614: DotNetModule.IsConstructorPrototypeIncompatible

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-isconstructorprototypeincompatib.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-isconstructorprototypeincompatib.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.IsConstructorPrototypeIncompatible Data Type Boolean Purpose This property is obsolete . Use the DotNetCall.IsPrototypeIncompatible property on a constructor call instead. Remarks Returns a value that indicates whether the prototype the current constructor parameters specify is i

### DotNetModule.IsConstructorPrototypeIncompatible

#### Syntax

[DotNetModule](dotnetmodule.html).IsConstructorPrototypeIncompatible

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetCall.IsPrototypeIncompatible

#### Remarks

Returns a value that indicates whether the prototype the current constructor parameters specify is incompatible with the constructor prototype of the specified module.

This property obtains the prototype for the specified .NET constructor and compares it to the current constructor parameters. This property returns
 True
 if TestStand successfully reads the prototype from the .NET constructor and the current constructor parameters do not match the prototype the .NET constructor specifies. Accessing this property loads the assembly to determine the constructor prototype.

#### See Also

[DotNetCall.IsPrototypeIncompatible](dotnetcall-isprototypeincompatible.html)

[DotNetModule.GetConstructorMetaDataToken](dotnetmodule-getconstructormetadatatoken.html)

[DotNetModule.LoadConstructorPrototypeFromMetaDataToken](dotnetmodule-loadconstructorprototypefrommeta.html)

[Module.IsPrototypeIncompatible](module-isprototypeincompatible.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-isstruct.html language=enus -->
## TOPIC 00615: DotNetModule.IsStruct

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-isstruct.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-isstruct.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.IsStruct Data Type Boolean Purpose Returns a value that indicates whether the class the module calls is a struct. See Also DotNetModule.ClassName DotNetModule.DisplayCreateCustomDataTypeDialog

### DotNetModule.IsStruct

#### Syntax

[DotNetModule](dotnetmodule.html).IsStruct

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the class the module calls is a struct.

#### See Also

[DotNetModule.ClassName](dotnetmodule-classname.html)

[DotNetModule.DisplayCreateCustomDataTypeDialog](dotnetmodule-displaycreatecustomdatatypedialo.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-loadconstructorinfo.html language=enus -->
## TOPIC 00616: DotNetModule.LoadConstructorInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-loadconstructorinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-loadconstructorinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.LoadConstructorInfo( discardParameterValues = False) Return Value Boolean Returns a value that indicates whether the constructor information of the module was loaded. This method usually returns True . Purpose This method is obsolete. Use the DotNetCall.LoadPrototypeFromSignature

### DotNetModule.LoadConstructorInfo

#### Syntax

[DotNetModule](dotnetmodule.html).LoadConstructorInfo( discardParameterValues = False)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether the constructor information of the module was loaded. This method usually returns
 True
 .

#### Purpose

Note

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Loads information for the parameters of the class constructor, if the module has specified one.

You must set the
 [DotNetModule.ClassName](dotnetmodule-classname.html)
 and
 [DotNetModule.ConstructorIndex](dotnetmodule-constructorindex.html)
 properties on the module before calling this method to access the
 [DotNetModule.ConstructorParameters](dotnetmodule-constructorparameters.html)
 property of the module.

#### Parameters

discardParameterValues
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to reset the
 [DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)
 property of existing parameter values when loading a new constructor prototype.

This parameter has a default value of
 False
 .

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.ClassName](dotnetmodule-classname.html)

[DotNetModule.ConstructorIndex](dotnetmodule-constructorindex.html)

[DotNetModule.ConstructorParameters](dotnetmodule-constructorparameters.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

Parent topic:

Obsolete DotNetModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-loadconstructorprototypefrommeta.html language=enus -->
## TOPIC 00617: DotNetModule.LoadConstructorPrototypeFromMetadataToken

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-loadconstructorprototypefrommeta.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-loadconstructorprototypefrommeta.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.LoadConstructorPrototypeFromMetadataToken( metadataToken, options = 0) Return Value Boolean Return True if the prototype for the constructor in the specified assembly is different from the current constructor prototype of the module. Otherwise, return False . Purpose This method

### DotNetModule.LoadConstructorPrototypeFromMetadataToken

#### Syntax

[DotNetModule](dotnetmodule.html).LoadConstructorPrototypeFromMetadataToken( metadataToken, options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Return
 True
 if the prototype for the constructor in the specified assembly is different from the current constructor prototype of the module. Otherwise, return
 False
 .

#### Purpose

Note

obsolete

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Loads the prototype information for the constructor from the specified assembly. Calling this method updates the
 [DotNetModule.ConstructorPrototype](dotnetmodule-constructorprototype.html)
 property and the
 [DotNetModule.ConstructorParameters](dotnetmodule-constructorparameters.html)
 collection.

This method replaces the
 [DotNetModule.LoadConstructorInfo](dotnetmodule-loadconstructorinfo.html)
 and
 [DotNetModule.LoadMemberInfo](dotnetmodule-loadmemberinfo.html)
 obsolete methods.

#### Parameters

metadataToken
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the metadata token property from the .NET class MemberInfo, which you can retrieve using reflection on an assembly.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [LoadPrototypeOptions](loadprototypeoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

This parameter has a default value of
 0
 .

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.ConstructorParameters](dotnetmodule-constructorparameters.html)

[DotNetModule.ConstructorPrototype](dotnetmodule-constructorprototype.html)

[DotNetModule.LoadConstructorInfo](dotnetmodule-loadconstructorinfo.html)

[DotNetModule.LoadMemberInfo](dotnetmodule-loadmemberinfo.html)

[LoadPrototypeOptions](loadprototypeoptions.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-loadmemberinfo.html language=enus -->
## TOPIC 00618: DotNetModule.LoadMemberInfo

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-loadmemberinfo.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-loadmemberinfo.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.LoadMemberInfo( discardParameterValues = False) Return Value Boolean Returns a value that indicates whether TestStand loaded the member information of the module. This method usually returns True . Purpose This method is obsolete. Use the DotNetCall.LoadPrototypeFromSignature met

### DotNetModule.LoadMemberInfo

#### Syntax

[DotNetModule](dotnetmodule.html).LoadMemberInfo( discardParameterValues = False)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns a value that indicates whether TestStand loaded the member information of the module. This method usually returns
 True
 .

#### Purpose

Note

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Loads information for the parameters of the specified member of the module and for constructor parameters of the class constructor, if the module has specified one.

You must set the
 [DotNetModule.ClassName](dotnetmodule-classname.html)
 ,
 [DotNetModule.MemberName](dotnetmodule-membername.html)
 , and
 [DotNetModule.MemberIndex](dotnetmodule-memberindex.html)
 properties on the module before calling LoadMemberInfo to access the
 [DotNetModule.Parameters](dotnetmodule-parameters.html)
 property of the module.

#### Parameters

discardParameterValues
 As
 [Boolean](data-types-for-teststand.html)

[In] Specifies whether to reset the
 [DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)
 property of existing parameter values when loading a new prototype.

This parameter has a default value of
 False
 .

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.ClassName](dotnetmodule-classname.html)

[DotNetModule.MemberIndex](dotnetmodule-memberindex.html)

[DotNetModule.MemberName](dotnetmodule-membername.html)

[DotNetModule.Parameters](dotnetmodule-parameters.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

Parent topic:

Obsolete DotNetModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-loadprototypefrommetadatatoken.html language=enus -->
## TOPIC 00619: DotNetModule.LoadPrototypeFromMetadataToken

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-loadprototypefrommetadatatoken.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-loadprototypefrommetadatatoken.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.LoadPrototypeFromMetadataToken( metadataToken, options = 0) Return Value Boolean Return True if the prototype for the class in the specified assembly is different from the current prototype of the module. Otherwise, return False . Purpose This method is obsolete . Use the DotNetC

### DotNetModule.LoadPrototypeFromMetadataToken

#### Syntax

[DotNetModule](dotnetmodule.html).LoadPrototypeFromMetadataToken( metadataToken, options = 0)

#### Return Value

[Boolean](data-types-for-teststand.html)

Return
 True
 if the prototype for the class in the specified assembly is different from the current prototype of the module. Otherwise, return
 False
 .

#### Purpose

Note

obsolete

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Loads the prototype information for the class, method, or property from the specified assembly. Calling this method updates the
 [DotNetModule.Parameters](dotnetmodule-parameters.html)
 collection.

This method replaces the
 [DotNetModule.LoadConstructorInfo](dotnetmodule-loadconstructorinfo.html)
 and
 [DotNetModule.LoadMemberInfo](dotnetmodule-loadmemberinfo.html)
 obsolete methods.

#### Parameters

metadataToken
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the metadata token property from the .NET class MemberInfo, which you can retrieve using reflection on an assembly.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [LoadPrototypeOptions](loadprototypeoptions.html)
 constants. Use the bitwise-OR operator to specify multiple flags.

This parameter has a default value of
 0
 .

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.GetMetadataToken](dotnetmodule-getmetadatatoken.html)

[DotNetModule.LoadConstructorInfo](dotnetmodule-loadconstructorinfo.html)

[DotNetModule.LoadConstructorPrototypeFromMetadataToken](dotnetmodule-loadconstructorprototypefrommeta.html)

[DotNetModule.LoadMemberInfo](dotnetmodule-loadmemberinfo.html)

[DotNetModule.Parameters](dotnetmodule-parameters.html)

[LoadPrototypeOptions](loadprototypeoptions.html)

[Module.IsPrototypeIncompatible](module-isprototypeincompatible.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-memberflags.html language=enus -->
## TOPIC 00620: DotNetModule.MemberFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-memberflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-memberflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.MemberFlags Data Type Long Purpose This property is obsolete . Use the DotNetCall.MemberFlags property instead. Remarks Specifies certain attributes of the member the module calls. Use the constants defined by DotNetMemberFlags with this property. See Also DotNetCall.MemberFlags

### DotNetModule.MemberFlags

#### Syntax

[DotNetModule](dotnetmodule.html).MemberFlags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetCall.MemberFlags

#### Remarks

Specifies certain attributes of the member the module calls.

Use the constants defined by
 [DotNetMemberFlags](dotnetmemberflags.html)
 with this property.

#### See Also

[DotNetCall.MemberFlags](dotnetcall-memberflags.html)

[DotNetMemberFlags](dotnetmemberflags.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-memberhelpstring.html language=enus -->
## TOPIC 00621: DotNetModule.MemberHelpString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-memberhelpstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-memberhelpstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.MemberHelpString Data Type String Purpose This property is obsolete . Use the DotNetCall.MemberHelpString property instead. Remarks Returns the help string the assembly associates with the member. See Also DotNetCall.MemberHelpString DotNetModule.ClassHelpString DotNetModule.Memb

### DotNetModule.MemberHelpString

#### Syntax

[DotNetModule](dotnetmodule.html).MemberHelpString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetCall.MemberHelpString

#### Remarks

Returns the help string the assembly associates with the member.

#### See Also

[DotNetCall.MemberHelpString](dotnetcall-memberhelpstring.html)

[DotNetModule.ClassHelpString](dotnetmodule-classhelpstring.html)

[DotNetModule.MemberName](dotnetmodule-membername.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-memberindex.html language=enus -->
## TOPIC 00622: DotNetModule.MemberIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-memberindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-memberindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.MemberIndex Data Type Long Purpose This property is obsolete. Use the DotNetCall.LoadPrototypeFromSignature method instead. See Also DotNetCall.LoadPrototypeFromSignature DotNetModule.GetMetadataToken DotNetModule.MemberName DotNetModule.Parameters Module.LoadPrototype

### DotNetModule.MemberIndex

#### Syntax

[DotNetModule](dotnetmodule.html).MemberIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

DotNetCall.LoadPrototypeFromSignature

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.GetMetadataToken](dotnetmodule-getmetadatatoken.html)

[DotNetModule.MemberName](dotnetmodule-membername.html)

[DotNetModule.Parameters](dotnetmodule-parameters.html)

[Module.LoadPrototype](module-loadprototype.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-membername.html language=enus -->
## TOPIC 00623: DotNetModule.MemberName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-membername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-membername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.MemberName Data Type String Purpose This property is obsolete . Use the DotNetCall.MemberName property instead. Remarks Specifies the name of the member function to call or property to access. See Also DotNetCall.MemberName DotNetModule.ClassName DotNetModule.GetMetadataToken Dot

### DotNetModule.MemberName

#### Syntax

[DotNetModule](dotnetmodule.html).MemberName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetCall.MemberName

#### Remarks

Specifies the name of the member function to call or property to access.

#### See Also

[DotNetCall.MemberName](dotnetcall-membername.html)

[DotNetModule.ClassName](dotnetmodule-classname.html)

[DotNetModule.GetMetadataToken](dotnetmodule-getmetadatatoken.html)

[DotNetModule.MemberType](dotnetmodule-membertype.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-membertype.html language=enus -->
## TOPIC 00624: DotNetModule.MemberType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-membertype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-membertype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.MemberType Data Type DotNetModuleMemberTypes Use the following constants with this data type: DotNetMember_CallConstructor –(Value: 4) Specifies that the DotNetCall object calls a constructor. DotNetMember_CallMethod –(Value: 1) Specifies that the DotNetCall object calls a method

### DotNetModule.MemberType

#### Syntax

[DotNetModule](dotnetmodule.html).MemberType

#### Data Type

[DotNetModuleMemberTypes](dotnetmodulemembertypes.html)

Use the following constants with this data type:

- DotNetMember_CallConstructor 
 –(Value: 4) Specifies that the
 DotNetCall 
 object calls a constructor.
- DotNetMember_CallMethod 
 –(Value: 1) Specifies that the
 DotNetCall 
 object calls a method.
- DotNetMember_CreateRemote 
 –(Value: 5) Specifies that the
 DotNetCall 
 object creates a remote object.
 Note 
 Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.
- DotNetMember_DoNotCall 
 –(Value: 0) Specifies that you have not completely specified the
 DotNetCall 
 object and that the object does not call a method or access a property or field.
- DotNetMember_GetProperty 
 –(Value: 2) Specifies that the
 DotNetCall 
 object gets a property.
- DotNetMember_SetProperty 
 –(Value: 3) Specifies that the
 DotNetCall 
 object sets a property.
- DotNetMember_UseExisting 
 –(Value: 6) Specifies that the
 DotNetCall 
 object uses an existing object a TestStand variable specifies as the .NET object on which to make the next call.

#### Purpose

Note

obsolete

DotNetCall.MemberType

#### Remarks

Specifies whether to call a method or access a property.

#### See Also

[DotNetCall.MemberType](dotnetcall-membertype.html)

[DotNetModule.MemberName](dotnetmodule-membername.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-nameofmethodtocreate.html language=enus -->
## TOPIC 00625: DotNetModule.NameOfMethodToCreate

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-nameofmethodtocreate.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-nameofmethodtocreate.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.NameOfMethodToCreate Data Type String Purpose This property is obsolete. Use the DotNetCall.MemberName property as the name of the method to create for the DotNetCall.CreateCode method instead. Remarks Specifies the method name the Module.CreateCode method uses. See Also DotNetCa

### DotNetModule.NameOfMethodToCreate

#### Syntax

[DotNetModule](dotnetmodule.html).NameOfMethodToCreate

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

DotNetCall.MemberName

DotNetCall.CreateCode

#### Remarks

Specifies the method name the
 [Module.CreateCode](module-createcode.html)
 method uses.

#### See Also

[DotNetCall.CreateCode](dotnetcall-createcode.html)

[DotNetCall.MemberName](dotnetcall-membername.html)

[DotNetModule.ProjectFilePath](dotnetmodule-projectfilepath.html)

[DotNetModule.SolutionFilePath](dotnetmodule-solutionfilepath.html)

[DotNetModule.SourceFilePath](dotnetmodule-sourcefilepath.html)

[Module.CreateCode](module-createcode.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-newmodulearguments.html language=enus -->
## TOPIC 00626: DotNetModule.NewModuleArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-newmodulearguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-newmodulearguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.NewModuleArguments Return Value DotNetModuleArguments Purpose Creates and returns a new DotNetModuleArguments collection. Use this collection to pass argument values to a DotNetModule object using the DotNetModule.Execute method. Remarks The new collection contains the same numbe

### DotNetModule.NewModuleArguments

#### Syntax

[DotNetModule](dotnetmodule.html).NewModuleArguments

#### Return Value

[DotNetModuleArguments](dotnetmodulearguments.html)

#### Purpose

Creates and returns a new
 [DotNetModuleArguments](dotnetmodulearguments.html)
 collection. Use this collection to pass argument values to a
 [DotNetModule](dotnetmodule.html)
 object using the
 [DotNetModule.Execute](dotnetmodule-execute.html)
 method.

#### Remarks

The new collection contains the same number of items as the
 [DotNetModule.Calls](dotnetmodule-calls.html)
 collection. Each item in the collection is a collection of
 [DotNetArguments](dotnetarguments.html)
 that contains the same number of items as the corresponding
 [DotNetCall.Parameters](dotnetcall-parameters.html)
 collection.

To pass an argument value to a parameter, set the
 [DotNetArgument.Value](dotnetargument-value.html)
 property to an item in the
 DotNetArguments
 collection that has the same index as the parameter in the
 [DotNetParameters](dotnetparameters.html)
 collection.

#### See Also

[DotNetArgument.Value](dotnetargument-value.html)

[DotNetArguments](dotnetarguments.html)

[DotNetCall.Parameters](dotnetcall-parameters.html)

[DotNetModule](dotnetmodule.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

[DotNetModule.Execute](dotnetmodule-execute.html)

[DotNetModuleArguments](dotnetmodulearguments.html)

[DotNetParameters](dotnetparameters.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-parameters.html language=enus -->
## TOPIC 00627: DotNetModule.Parameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-parameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-parameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.Parameters Data Type DotNetParameters The collection of parameters for the method the module calls or the property the module accesses. Purpose This property is obsolete . Use the DotNetCall.Parameters property instead. Remarks Returns the DotNetParameters collection that contain

### DotNetModule.Parameters

#### Syntax

[DotNetModule](dotnetmodule.html).Parameters

#### Data Type

[DotNetParameters](dotnetparameters.html)

The collection of parameters for the method the module calls or the property the module accesses.

#### Purpose

Note

obsolete

DotNetCall.Parameters

#### Remarks

Returns the DotNetParameters collection that contains a list of the current parameters used as inputs and outputs of the corresponding module.

Call the
 [DotNetModule.LoadPrototypeFromMetadataToken](dotnetmodule-loadprototypefrommetadatatoken.html)
 method before accessing this property.

#### See Also

[DotNetCall.Parameters](dotnetcall-parameters.html)

[DotNetModule.ConstructorParameters](dotnetmodule-constructorparameters.html)

[DotNetModule.LoadPrototypeFromMetadataToken](dotnetmodule-loadprototypefrommetadatatoken.html)

[DotNetParameters](dotnetparameters.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-projectfilepath.html language=enus -->
## TOPIC 00628: DotNetModule.ProjectFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-projectfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-projectfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.ProjectFilePath Data Type String Purpose Specifies the pathname of the project file for the class the module calls. TestStand uses the project file path when integrating with Microsoft Visual Studio. You can enter an absolute or relative pathname. Relative pathnames are relative

### DotNetModule.ProjectFilePath

#### Syntax

[DotNetModule](dotnetmodule.html).ProjectFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the project file for the class the module calls. TestStand uses the project file path when integrating with Microsoft Visual Studio. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[DotNetModule.SolutionFilePath](dotnetmodule-solutionfilepath.html)

[Module.CreateCode](module-createcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-remotehost.html language=enus -->
## TOPIC 00629: DotNetModule.RemoteHost

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-remotehost.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-remotehost.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.RemoteHost Data Type String Purpose This property is obsolete . Use a remote creation call as the first call in the DotNetModule class instead, and specify the remote host using the first parameter of the call that is not a return value. You can specify a remote creation call by

### DotNetModule.RemoteHost

#### Syntax

[DotNetModule](dotnetmodule.html).RemoteHost

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetModule

DotNetModule.Calls

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Specifies the Universal Resource Identifier (URI) the .NET Adapter uses to execute the assembly remotely. The URI specifies the type of channel, port number, and endpoint. If the
 [DotNetModule.SpecifyHostByExpression](dotnetmodule-specifyhostbyexpression.html)
 property is
 True
 , the value of this property must be in the form of an expression.

Leave this property empty to instruct the .NET Adapter to not use a remote endpoint and create the object on the local computer instead.

The following is an example of a HTTP channel URI:

http://remotecomputername:65100/theEndPointName

The following is an example of a TCP channel URI:

tcp://localhost:8085/theEndPointName

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

[DotNetModule.CreateObject](dotnetmodule-createobject.html)

[DotNetModule.SpecifyHostByExpression](dotnetmodule-specifyhostbyexpression.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-setassembly.html language=enus -->
## TOPIC 00630: DotNetModule.SetAssembly

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-setassembly.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-setassembly.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.SetAssembly( assemblyLocationParam, assemblyPathParam) Purpose Specifies the pathname of the assembly. Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported. Remarks You can specify an absolute or relative pathname for a f

### DotNetModule.SetAssembly

#### Syntax

[DotNetModule](dotnetmodule.html).SetAssembly( assemblyLocationParam, assemblyPathParam)

#### Purpose

Specifies the pathname of the assembly.

Note

Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### Remarks

You can specify an absolute or relative pathname for a file. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### Parameters

assemblyLocationParam
 As
 [DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

[In] Specifies whether the assembly is in a file or in the Global Assembly Cache.

assemblyPathParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the pathname of the assembly.

#### See Also

[DotNetModule.GetAssembly](dotnetmodule-getassembly.html)

[DotNetModuleAssemblyLocations](dotnetmoduleassemblylocations.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-solutionfilepath.html language=enus -->
## TOPIC 00631: DotNetModule.SolutionFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-solutionfilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-solutionfilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.SolutionFilePath Data Type String Purpose Specifies the pathname of the solution file for the class the module calls. TestStand uses the solution file path when integrating with Microsoft Visual Studio. You can enter an absolute or relative pathname. Relative pathnames are relati

### DotNetModule.SolutionFilePath

#### Syntax

[DotNetModule](dotnetmodule.html).SolutionFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the solution file for the class the module calls. TestStand uses the solution file path when integrating with Microsoft Visual Studio. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[DotNetModule.ProjectFilePath](dotnetmodule-projectfilepath.html)

[DotNetModule.SourceFilePath](dotnetmodule-sourcefilepath.html)

[Module.CreateCode](module-createcode.html)

[Module.EditCode](module-editcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-sourcefilepath.html language=enus -->
## TOPIC 00632: DotNetModule.SourceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-sourcefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-sourcefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.SourceFilePath Data Type String Purpose Specifies the pathname of the source file for the class the module calls. TestStand uses the source file path when integrating with Microsoft Visual Studio. You can enter an absolute or relative pathname. Relative pathnames are relative to

### DotNetModule.SourceFilePath

#### Syntax

[DotNetModule](dotnetmodule.html).SourceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the pathname of the source file for the class the module calls. TestStand uses the source file path when integrating with Microsoft Visual Studio. You can enter an absolute or relative pathname. Relative pathnames are relative to the TestStand
 [search directory paths](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 .

#### See Also

[DotNetModule.ProjectFilePath](dotnetmodule-projectfilepath.html)

[DotNetModule.SolutionFilePath](dotnetmodule-solutionfilepath.html)

[Module.CreateCode](module-createcode.html)

[Module.EditCode](module-editcode.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-specifyhostbyexpression.html language=enus -->
## TOPIC 00633: DotNetModule.SpecifyHostByExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-specifyhostbyexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-specifyhostbyexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.SpecifyHostByExpression Data Type Boolean Purpose This property is obsolete . Use a remote creation call as the first call in the DotNetModule class instead, and specify the remote host using the first parameter of the call that is not a return value. The parameter value is alway

### DotNetModule.SpecifyHostByExpression

#### Syntax

[DotNetModule](dotnetmodule.html).SpecifyHostByExpression

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

obsolete

DotNetModule

DotNetModule.Calls

DotNetCall.LoadPrototypeFromSignature

#### Remarks

Specifies if the
 [DotNetModule.RemoteHost](dotnetmodule-remotehost.html)
 property contains an expression the module evaluates at run time to determine the name of the remote host.

The module ignores this property if RemoteHost is empty.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetModule.Calls](dotnetmodule-calls.html)

[DotNetModule.CreateObject](dotnetmodule-createobject.html)

[DotNetModule.RemoteHost](dotnetmodule-remotehost.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-unmappedconstructorargumentvalue.html language=enus -->
## TOPIC 00634: DotNetModule.UnmappedConstructorArgumentValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-unmappedconstructorargumentvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-unmappedconstructorargumentvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.UnmappedConstructorArgumentValues Data Type UnmappedArgumentValues Purpose This property is obsolete . Use the DotNetCall.UnmappedArgumentValues property on a constructor call instead. Remarks Returns the UnmappedArgumentValues collection that contains a list of the arguments not

### DotNetModule.UnmappedConstructorArgumentValues

#### Syntax

[DotNetModule](dotnetmodule.html).UnmappedConstructorArgumentValues

#### Data Type

[UnmappedArgumentValues](unmappedargumentvalues.html)

#### Purpose

Note

obsolete

DotNetCall.UnmappedArgumentValues

#### Remarks

Returns the
 [UnmappedArgumentValues](unmappedargumentvalues.html)
 collection that contains a list of the arguments not used as inputs and outputs of the corresponding constructor for the module.

When the constructor prototype changes, TestStand attempts to map the current constructor arguments to the new prototype by looking for matching argument names and data types, and by matching argument positions and data types. If TestStand fails to assign an argument to the new prototype, the argument is added to this collection.

TestStand does not clear the collection when you load a new prototype. Use the
 [DotNetModule.ClearUnmappedConstructorArgumentValues](dotnetmodule-clearunmappedconstructorargument.html)
 method to clear the collection before calling the
 [DotNetModule.LoadConstructorPrototypeFromMetadataToken](dotnetmodule-loadconstructorprototypefrommeta.html)
 method.

#### See Also

[DotNetCall.UnmappedArgumentValues](dotnetcall-unmappedargumentvalues.html)

[DotNetModule.ClearUnmappedConstructorArgumentValues](dotnetmodule-clearunmappedconstructorargument.html)

[DotNetModule.LoadConstructorPrototypeFromMetadataToken](dotnetmodule-loadconstructorprototypefrommeta.html)

[Obsolete DotNetModule Properties](obsolete-dotnetmodule-properties.html)

[UnmappedArgumentValue](unmappedargumentvalue.html)

[UnmappedArgumentValues](unmappedargumentvalues.html)

Parent topic:

Obsolete DotNetModule Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule-usesteploadoptions.html language=enus -->
## TOPIC 00635: DotNetModule.UseStepLoadOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule-usesteploadoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule-usesteploadoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModule.UseStepLoadOptions Data Type Boolean Purpose Controls the lifetime of an object the module creates. If this property is False , the module creates the object when it begins executing. Then, the module releases its internal reference to the object when it completes executing. If t

### DotNetModule.UseStepLoadOptions

#### Syntax

[DotNetModule](dotnetmodule.html).UseStepLoadOptions

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Controls the lifetime of an object the module creates. If this property is
 False
 , the module creates the object when it begins executing. Then, the module releases its internal reference to the object when it completes executing. If this property is
 True
 , the module creates the object when the step loads according to
 [Step.ModuleLoadOption](step-moduleloadoption.html)
 and then holds an internal reference to the object until the step unloads according to
 [Step.ModuleUnloadOption](step-moduleunloadoption.html)
 .

#### See Also

[Step.ModuleLoadOption](step-moduleloadoption.html)

[Step.ModuleUnloadOption](step-moduleunloadoption.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodule.html language=enus -->
## TOPIC 00636: DotNetModule

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodule.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodule.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DotNetModule class to specify and obtain .NET Adapter-specific information about the code module that steps or step type substeps execute. Use the Step.Module property to obtain a reference to a DotNetModule object. To access the properties and methods of a specific module class

### DotNetModule

Use objects from the DotNetModule class to specify and obtain .NET Adapter-specific information about the code module that steps or step type substeps execute. Use the
 
 [Step.Module](step-module.html)
 property to obtain a reference to a DotNetModule object. To access the properties and methods of a specific module class, query the Module object for the interface of the module-specific interface you want to acquire.

Typically, you use this class only when you are writing a sequence editor.

To access the properties and methods of the Module class, use the
 [DotNetModule.AsModule](dotnetmodule-asmodule.html)
 method to obtain an object.

#### Properties

| AssemblyWarnings (Read Only) |
| --- |
| Calls (Read Only) |
| ClassHelpString (Read Only) |
| ClassName |
| IsStruct |
| ProjectFilePath |
| SolutionFilePath |
| SourceFilePath |
| UseStepLoadOptions |

#### Methods

| AsModule |
| --- |
| DisplayCreateCustomDataTypeDialog |
| Execute |
| GetAssembly |
| NewModuleArguments |
| SetAssembly |

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[Module](module.html)

[Step.Module](step-module.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodulearguments-count.html language=enus -->
## TOPIC 00637: DotNetModuleArguments.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodulearguments-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodulearguments-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModuleArguments.Count Data Type Long Purpose Returns the number of items in the collection. See Also DotNetArguments DotNetModuleArguments

### DotNetModuleArguments.Count

#### Syntax

[DotNetModuleArguments](dotnetmodulearguments.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[DotNetArguments](dotnetarguments.html)

[DotNetModuleArguments](dotnetmodulearguments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodulearguments-item.html language=enus -->
## TOPIC 00638: DotNetModuleArguments.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodulearguments-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodulearguments-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetModuleArguments.Item( index) Data Type DotNetArguments Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also DotNetArguments DotNetModuleArguments

### DotNetModuleArguments.Item

#### Syntax

[DotNetModuleArguments](dotnetmodulearguments.html).Item( index)

#### Data Type

[DotNetArguments](dotnetarguments.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[DotNetArguments](dotnetarguments.html)

[DotNetModuleArguments](dotnetmodulearguments.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodulearguments.html language=enus -->
## TOPIC 00639: DotNetModuleArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodulearguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodulearguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from this class to pass specific argument values to a DotNetModule object using the DotNetModule.Execute method. Use the DotNetModule.NewModuleArguments method to create a new DotNetModuleArguments collection. Properties Count (Read Only) Item (Read Only) See Also DotNetModule DotNetModu

### DotNetModuleArguments

Use objects from this class to pass specific argument values to a
 [DotNetModule](dotnetmodule.html)
 object using the
 [DotNetModule.Execute](dotnetmodule-execute.html)
 method. Use the
 [DotNetModule.NewModuleArguments](dotnetmodule-newmodulearguments.html)
 method to create a new
 DotNetModuleArguments
 collection.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[DotNetModule](dotnetmodule.html)

[DotNetModule.Execute](dotnetmodule-execute.html)

[DotNetModule.NewModuleArguments](dotnetmodule-newmodulearguments.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmoduleassemblylocations.html language=enus -->
## TOPIC 00640: DotNetModuleAssemblyLocations

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmoduleassemblylocations.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmoduleassemblylocations.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the DotNetModule.SetAssembly method to specify the path of the assembly file. DotNetModule_AssemblyLocation_File –(Value: 0) Located in a file, such as a DLL. DotNetModule_AssemblyLocation_GAC –(Value: 1) Located in the GAC. Starting with TestStand 2024 Q4, loading assemblie

### DotNetModuleAssemblyLocations

Use these constants with the
 [DotNetModule.SetAssembly](dotnetmodule-setassembly.html)
 method to specify the path of the assembly file.

- DotNetModule_AssemblyLocation_File 
 –(Value: 0) Located in a file, such as a DLL.
- DotNetModule_AssemblyLocation_GAC 
 –(Value: 1) Located in the GAC.
 Note 
 Starting with TestStand 2024 Q4, loading assemblies from the Global Assembly Cache (GAC) is no longer supported.

#### See Also

[DotNetModule.SetAssembly](dotnetmodule-setassembly.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetmodulemembertypes.html language=enus -->
## TOPIC 00641: DotNetModuleMemberTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetmodulemembertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetmodulemembertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use these constants with the DotNetCall.MemberType property to specify the type of member the module accesses when it executes. DotNetMember_CallConstructor –(Value: 4) Specifies that the DotNetCall object calls a constructor. DotNetMember_CallMethod –(Value: 1) Specifies that the DotNetCall object

### DotNetModuleMemberTypes

Use these constants with the
 [DotNetCall.MemberType](dotnetcall-membertype.html)
 property to specify the type of member the module accesses when it executes.

- DotNetMember_CallConstructor 
 –(Value: 4) Specifies that the
 DotNetCall 
 object calls a constructor.
- DotNetMember_CallMethod 
 –(Value: 1) Specifies that the
 DotNetCall 
 object calls a method.
- DotNetMember_CreateRemote 
 –(Value: 5) Specifies that the
 DotNetCall 
 object creates a remote object.
 Note 
 Starting with TestStand 2024 Q4, 'Create Remote Object' is no longer supported.
- DotNetMember_DoNotCall 
 –(Value: 0) Specifies that you have not completely specified the
 DotNetCall 
 object and that the object does not call a method or access a property or field.
- DotNetMember_GetProperty 
 –(Value: 2) Specifies that the
 DotNetCall 
 object gets a property.
- DotNetMember_SetProperty 
 –(Value: 3) Specifies that the
 DotNetCall 
 object sets a property.
- DotNetMember_UseExisting 
 –(Value: 6) Specifies that the
 DotNetCall 
 object uses an existing object a TestStand variable specifies as the .NET object on which to make the next call.

#### See Also

[DotNetCall.MemberType](dotnetcall-membertype.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-arraydimensions.html language=enus -->
## TOPIC 00642: DotNetParameter.ArrayDimensions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-arraydimensions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-arraydimensions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.ArrayDimensions Data Type Long Purpose This property is obsolete. Use the DotNetParameter.ArrayDimensionsEx property instead. Remarks Returns the number of dimensions for array parameters. See Also ArrayDimensionsEx

### DotNetParameter.ArrayDimensions

#### Syntax

[DotNetParameter](dotnetparameter.html).ArrayDimensions

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Note

DotNetParameter.ArrayDimensionsEx

#### Remarks

Returns the number of dimensions for array parameters.

#### See Also

[ArrayDimensionsEx](dotnetparameter-arraydimensionsex.html)

Parent topic:

Obsolete DotNetParameter Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-arraydimensionsex.html language=enus -->
## TOPIC 00643: DotNetParameter.ArrayDimensionsEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-arraydimensionsex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-arraydimensionsex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.ArrayDimensionsEx Data Type Object Array Purpose Returns the number of dimensions for array parameters. This property supports arrays of arrays, also known as jagged arrays, which can specify more than one number of dimensions. Remarks For non-array parameters, this property r

### DotNetParameter.ArrayDimensionsEx

#### Syntax

[DotNetParameter](dotnetparameter.html).ArrayDimensionsEx

#### Data Type

[Object Array](data-types-for-teststand.html)

#### Purpose

Returns the number of dimensions for array parameters. This property supports arrays of arrays, also known as jagged arrays, which can specify more than one number of dimensions.

#### Remarks

For non-array parameters, this property returns an empty array.

For regular array parameters, this property returns an array with a single element that specifies a value that is the number of dimensions of the array.

For jagged arrays, this property returns an array with elements that represent the number of dimensions for each array level.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-aspropertyobject.html language=enus -->
## TOPIC 00644: DotNetParameter.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the DotNetParameter object. Remarks Use the PropertyObject to modify, add, or remove custom properties of the object. See Also PropertyObject

### DotNetParameter.AsPropertyObject

#### Syntax

[DotNetParameter](dotnetparameter.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the DotNetParameter object.

#### Remarks

Use the PropertyObject to modify, add, or remove custom properties of the object.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-defaultvalue.html language=enus -->
## TOPIC 00645: DotNetParameter.DefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-defaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.DefaultValue Data Type String Purpose Returns a display string that represents the default value defined for the parameter. Remarks This value loads dynamically from the metadata stored in the assembly. The assembly you specify for the DotNetCall must exist and you must be abl

### DotNetParameter.DefaultValue

#### Syntax

[DotNetParameter](dotnetparameter.html).DefaultValue

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a display string that represents the default value defined for the parameter.

#### Remarks

This value loads dynamically from the metadata stored in the assembly. The assembly you specify for the
 [DotNetCall](dotnetcall.html)
 must exist and you must be able to load the assembly for TestStand to successfully retrieve this value.

The DefaultValue property does not apply to
 DotNetParameter
 objects that represent fields of a structure or elements of an array.

#### See Also

[DotNetParameter.UseDefaultValue](dotnetparameter-usedefaultvalue.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-deletearrayelement.html language=enus -->
## TOPIC 00646: DotNetParameter.DeleteArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-deletearrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-deletearrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.DeleteArrayElement( index) Purpose Deletes an element from an array at the specified index. Remarks Call this method only on array parameters. Use the DotNetParameter.Flags property to determine whether a parameter is an array. This method is valid only for one-dimensional arr

### DotNetParameter.DeleteArrayElement

#### Syntax

[DotNetParameter](dotnetparameter.html).DeleteArrayElement( index)

#### Purpose

Deletes an element from an array at the specified index.

#### Remarks

Call this method only on array parameters. Use the
 [DotNetParameter.Flags](dotnetparameter-flags.html)
 property to determine whether a parameter is an array.

This method is valid only for one-dimensional array parameters. Use
 [DotNetParameter.ArrayDimensionsEx](dotnetparameter-arraydimensionsex.html)
 to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index that specifies the location where to delete the element.

#### See Also

[DotNetParameter.ArrayDimensionsEx](dotnetparameter-arraydimensionsex.html)

[DotNetParameter.Flags](dotnetparameter-flags.html)

[DotNetParameter.InsertArrayElement](dotnetparameter-insertarrayelement.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-direction.html language=enus -->
## TOPIC 00647: DotNetParameter.Direction

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-direction.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-direction.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.Direction Data Type Long Purpose Returns a value that indicates whether the parameter is an input parameter, output parameter, input/output parameter, or a return value. Refer to DotNetParameterDirections for all the possible values. Remarks The Direction property does not app

### DotNetParameter.Direction

#### Syntax

[DotNetParameter](dotnetparameter.html).Direction

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns a value that indicates whether the parameter is an input parameter, output parameter, input/output parameter, or a return value. Refer to
 [DotNetParameterDirections](dotnetparameterdirections.html)
 for all the possible values.

#### Remarks

The Direction property does not apply to DotNetParameter objects that represent fields of a structure or elements of an array.

The .NET Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method before you retrieve this property value.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetParameterDirections](dotnetparameterdirections.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-displaycreatecustomdatatypedi.html language=enus -->
## TOPIC 00648: DotNetParameter.DisplayCreateCustomDataTypeDialog

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-displaycreatecustomdatatypedi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-displaycreatecustomdatatypedi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.DisplayCreateCustomDataTypeDialog( sequenceContext) Return Value Boolean Returns True if you click OK in the dialog box and False if you click Cancel . Purpose Launches the Create Custom Data Type from Struct dialog box, in which you can create a new data type you can pass to

### DotNetParameter.DisplayCreateCustomDataTypeDialog

#### Syntax

[DotNetParameter](dotnetparameter.html).DisplayCreateCustomDataTypeDialog( sequenceContext)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if you click
 OK
 in the dialog box and
 False
 if you click
 Cancel
 .

#### Purpose

Launches the
 [Create Custom Data Type from Struct](../tsref/create-custom-data-type-from-struct-dialog-bo.html)
 dialog box, in which you can create a new data type you can pass to a .NET struct parameter.

#### Remarks

Call this method only if the parameter is a struct. Otherwise, this method returns without launching the Create Custom Data Type from Struct dialog box. Use the
 [DotNetParameter.Type](dotnetparameter-type.html)
 property to determine whether a parameter is a struct.

#### Parameters

sequenceContext
 As
 
 [SequenceContext](sequencecontext.html)

[In] Specifies the sequence context the Create Custom Data Type from Struct dialog box uses to obtain information about the sequence file. You can use the
 [Engine.NewEditContext](engine-neweditcontext.html)
 method to obtain an edit-time sequence context.

#### See Also

[Create Custom Data Type from Struct dialog box](../tsref/create-custom-data-type-from-struct-dialog-bo.html)

[DotNetParameter.Type](dotnetparameter-type.html)

[Engine.NewEditContext](engine-neweditcontext.html)

[SequenceContext](sequencecontext.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-displaytype.html language=enus -->
## TOPIC 00649: DotNetParameter.DisplayType

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-displaytype.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-displaytype.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.DisplayType Data Type String Purpose Returns a localized display value for the data type of the parameter. See Also DotNetParameter.Type

### DotNetParameter.DisplayType

#### Syntax

[DotNetParameter](dotnetparameter.html).DisplayType

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns a localized display value for the data type of the parameter.

#### See Also

[DotNetParameter.Type](dotnetparameter-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-disposeobject.html language=enus -->
## TOPIC 00650: DotNetParameter.DisposeObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-disposeobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-disposeobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.DisposeObject Data Type Boolean Purpose Specifies whether TestStand attempts to dispose the object the DotNetParameter returns when the object is released or goes out of scope. Remarks If the parameter is not an object reference or if the object does not implement the IDisposa

### DotNetParameter.DisposeObject

#### Syntax

[DotNetParameter](dotnetparameter.html).DisposeObject

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether TestStand attempts to dispose the object the DotNetParameter returns when the object is released or goes out of scope.

#### Remarks

If the parameter is not an object reference or if the object does not implement the IDisposable interface, TestStand ignores this property.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-elements.html language=enus -->
## TOPIC 00651: DotNetParameter.Elements

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-elements.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-elements.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.Elements Data Type DotNetParameters Purpose Returns a collection that represents the following types of parameters, depending on the data type of the parameter: Struct parameters —Fields of the struct. Array parameters —Elements of the array for the case in which you configure

### DotNetParameter.Elements

#### Syntax

[DotNetParameter](dotnetparameter.html).Elements

#### Data Type

[DotNetParameters](dotnetparameters.html)

#### Purpose

Returns a collection that represents the following types of parameters, depending on the data type of the parameter:

- Struct parameters 
 —Fields of the struct.
- Array parameters 
 —Elements of the array for the case in which you configure the code module to explicitly pass each element instead of the entire array.
- Array of struct parameters 
 —Fields of the struct definition for the array.

#### See Also

[DotNetParameters](dotnetparameters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-flags.html language=enus -->
## TOPIC 00652: DotNetParameter.Flags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-flags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-flags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.Flags Data Type Long Purpose Returns flags that indicate certain attributes of the DotNetParameter. Refer to DotNetParameterFlags for a description of these flags. Remarks You must call the DotNetCall.LoadPrototypeFromSignature method before retrieving this property value. See

### DotNetParameter.Flags

#### Syntax

[DotNetParameter](dotnetparameter.html).Flags

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns flags that indicate certain attributes of the DotNetParameter. Refer to
 [DotNetParameterFlags](dotnetparameterflags.html)
 for a description of these flags.

#### Remarks

You must call the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method before retrieving this property value.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetParameterFlags](dotnetparameterflags.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-getenumvalues.html language=enus -->
## TOPIC 00653: DotNetParameter.GetEnumValues

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-getenumvalues.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-getenumvalues.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.GetEnumValues Return Value Object Array Returns an array of property objects where each property object represents an enumeration value. Purpose Returns the enumeration constants for a parameter that is an enumeration. Remarks The property objects in the array that this method

### DotNetParameter.GetEnumValues

#### Syntax

[DotNetParameter](dotnetparameter.html).GetEnumValues

#### Return Value

[Object Array](data-types-for-teststand.html)

Returns an array of property objects where each property object represents an enumeration value.

#### Purpose

Returns the enumeration constants for a parameter that is an enumeration.

#### Remarks

The property objects in the array that this method returns have a name and value that corresponds to the name and value of the enumeration constant.

Pass the return value of this method as the
 additionalConstants
 parameter of
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 when checking the
 [DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)
 property for errors.

If you are using an ExpressionEdit control to specify the
 DotNetParameter.ValueExpr
 property, pass the return value of this method to
 
 [ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)
 to direct the ExpressionEdit control to recognize the enumeration constants.

#### See Also

[DotNetParameter.ValidEvaluationTypes](dotnetparameter-validevaluationtypes.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.SetAdditionalEvaluationConstants](../tsuiref/expressionedit-setadditionalevaluationconstan.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-helpstring.html language=enus -->
## TOPIC 00654: DotNetParameter.HelpString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-helpstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-helpstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.HelpString Data Type String Purpose Returns the help string the assembly associates with the parameter. See Also DotNetCall.MemberHelpString DotNetModule.ClassHelpString

### DotNetParameter.HelpString

#### Syntax

[DotNetParameter](dotnetparameter.html).HelpString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the help string the assembly associates with the parameter.

#### See Also

[DotNetCall.MemberHelpString](dotnetcall-memberhelpstring.html)

[DotNetModule.ClassHelpString](dotnetmodule-classhelpstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-insertarrayelement.html language=enus -->
## TOPIC 00655: DotNetParameter.InsertArrayElement

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-insertarrayelement.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-insertarrayelement.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.InsertArrayElement( index) Purpose Inserts an element into an array at the specified index. Remarks Call this method only on array parameters. Use the DotNetParameter.Flags property to determine whether a parameter is an array. This method is valid only for one-dimensional arr

### DotNetParameter.InsertArrayElement

#### Syntax

[DotNetParameter](dotnetparameter.html).InsertArrayElement( index)

#### Purpose

Inserts an element into an array at the specified index.

#### Remarks

Call this method only on array parameters. Use the
 [DotNetParameter.Flags](dotnetparameter-flags.html)
 property to determine whether a parameter is an array.

This method is valid only for one-dimensional array parameters. Use
 [DotNetParameter.ArrayDimensionsEx](dotnetparameter-arraydimensionsex.html)
 to determine the number of array dimensions.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index that specifies the location where to insert the element.

#### See Also

[DotNetParameter.ArrayDimensionsEx](dotnetparameter-arraydimensionsex.html)

[DotNetParameter.DeleteArrayElement](dotnetparameter-deletearrayelement.html)

[DotNetParameter.Flags](dotnetparameter-flags.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-isparametermappinginvalid.html language=enus -->
## TOPIC 00656: DotNetParameter.IsParameterMappingInvalid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-isparametermappinginvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-isparametermappinginvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.IsParameterMappingInvalid( reasonNotValid) Return Value Boolean Returns true if the parameter in the code module is a struct or enum, the argument expression is valid and non-empty, and the mapping of the argument to the parameter in the code module is invalid. Returns false o

### DotNetParameter.IsParameterMappingInvalid

#### Syntax

[DotNetParameter](dotnetparameter.html).IsParameterMappingInvalid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns true if the parameter in the code module is a struct or enum, the argument expression is valid and non-empty, and the mapping of the argument to the parameter in the code module is invalid. Returns false otherwise.

#### Purpose

Indicates if the TestStand container or enumeration data type of the argument conflicts with the definition of the corresponding struct or enum parameter in the code module.

#### Remarks

The primary purpose of this method is to support error reporting. Therefore, cases where the mapping is not well defined, for example when the argument expression is empty, are not considered invalid. If an empty expression is considered an error condition, the application must check for it separately.

This method does not load the specified assembly. The method relies on the type information stored for the parameter when the module was last specified.

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] If the mapping is invalid,
 reasonNotValid
 contains an error message explaining why the type definitions do not match. If the mapping is valid,
 reasonNotValid
 is set to an empty string.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-isstructmappinginvalid.html language=enus -->
## TOPIC 00657: DotNetParameter.IsStructMappingInvalid

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-isstructmappinginvalid.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-isstructmappinginvalid.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.IsStructMappingInvalid( reasonNotValid) Return Value Boolean Returns True when the parameter is a struct or struct array, the argument expression is valid and non-empty, and the argument or struct mapping of the argument is invalid. In all other cases, this method returns Fals

### DotNetParameter.IsStructMappingInvalid

#### Syntax

[DotNetParameter](dotnetparameter.html).IsStructMappingInvalid( reasonNotValid)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 when the parameter is a struct or struct array, the argument expression is valid and non-empty, and the argument or struct mapping of the argument is invalid. In all other cases, this method returns
 False
 .

#### Purpose

Indicates whether the argument you specify for a .NET struct or struct array parameter is valid by checking the struct passing information for any custom data types used to ensure that it matches the struct definition stored when you specified the module.

Note

#### Parameters

reasonNotValid
 As
 [String](data-types-for-teststand.html)

[Out] When this method returns
 True
 , this parameter returns the reason why the argument is invalid.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-parametername.html language=enus -->
## TOPIC 00658: DotNetParameter.ParameterName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-parametername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-parametername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.ParameterName Data Type String Purpose Returns the name of the parameter. Remarks The .NET Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the DotNetCall.LoadPrototypeFromSignature method before you retriev

### DotNetParameter.ParameterName

#### Syntax

[DotNetParameter](dotnetparameter.html).ParameterName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the parameter.

#### Remarks

The .NET Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method before you retrieve this property value.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-type.html language=enus -->
## TOPIC 00659: DotNetParameter.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.Type Data Type DotNetParameterTypes Purpose Returns the data type of the parameter. Remarks The .NET Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the DotNetCall.LoadPrototypeFromSignature method before y

### DotNetParameter.Type

#### Syntax

[DotNetParameter](dotnetparameter.html).Type

#### Data Type

[DotNetParameterTypes](dotnetparametertypes.html)

#### Purpose

Returns the data type of the parameter.

#### Remarks

The .NET Adapter persists this property value when you specify a code module for a step. For an unspecified step, you must call the
 [DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)
 method before you retrieve this property value.

#### See Also

[DotNetCall.LoadPrototypeFromSignature](dotnetcall-loadprototypefromsignature.html)

[DotNetParameter.DisplayType](dotnetparameter-displaytype.html)

[DotNetParameterTypes](dotnetparametertypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-typename.html language=enus -->
## TOPIC 00660: DotNetParameter.TypeName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-typename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-typename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.TypeName Data Type String Purpose Returns the .NET name for the data type of the parameter. Remarks This property is similar to the DotNetParameter.DisplayType property, which contains the TestStand type followed by the .NET type name in parentheses. The DotNetParameter.TypeNa

### DotNetParameter.TypeName

#### Syntax

[DotNetParameter](dotnetparameter.html).TypeName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the .NET name for the data type of the parameter.

#### Remarks

This property is similar to the
 [DotNetParameter.DisplayType](dotnetparameter-displaytype.html)
 property, which contains the TestStand type followed by the .NET type name in parentheses. The
 DotNetParameter.TypeName
 property contains only the .NET type name.

For the following .NET types, the
 DotNetParameter.TypeName
 property omits the
 System
 namespace prefix:
 Boolean
 ,
 Byte
 ,
 Char
 ,
 Double
 ,
 Int16
 ,
 Int32
 ,
 Int64
 ,
 IntPtr
 ,
 SByte
 ,
 Single
 ,
 UInt16
 ,
 UInt32
 ,
 UInt64
 , and
 UIntPtr
 .

#### See Also

[DotNetParameter.DisplayType](dotnetparameter-displaytype.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-usedefaultvalue.html language=enus -->
## TOPIC 00661: DotNetParameter.UseDefaultValue

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-usedefaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-usedefaultvalue.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.UseDefaultValue Data Type Boolean Purpose Specifies whether to use the default value of the parameter when calling the assembly. Remarks You can only use the default value for optional parameters. This property does not apply to DotNetParameter objects that represent fields of

### DotNetParameter.UseDefaultValue

#### Syntax

[DotNetParameter](dotnetparameter.html).UseDefaultValue

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether to use the default value of the parameter when calling the assembly.

#### Remarks

You can only use the default value for optional parameters. This property does not apply to DotNetParameter objects that represent fields of a structure or elements of an array.

#### See Also

[DotNetParameter.DefaultValue](dotnetparameter-defaultvalue.html)

[DotNetParameter.Flags](dotnetparameter-flags.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-userdata.html language=enus -->
## TOPIC 00662: DotNetParameter.UserData

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-userdata.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-userdata.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.UserData Data Type PropertyObject Purpose Holds a data item you associate with the parameter object. Remarks Typically, you do not use this property. See Also PropertyObject

### DotNetParameter.UserData

#### Syntax

[DotNetParameter](dotnetparameter.html).UserData

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Holds a data item you associate with the parameter object.

#### Remarks

Typically, you do not use this property.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-validevaluationtypes.html language=enus -->
## TOPIC 00663: DotNetParameter.ValidEvaluationTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-validevaluationtypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-validevaluationtypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.ValidEvaluationTypes Data Type EvaluationTypes Purpose Returns the valid types to which this parameter can evaluate. Remarks You can pass the value of this property to the validEvaluationTypes parameter of the Expression.ValidateEvaluationType method to determine whether the v

### DotNetParameter.ValidEvaluationTypes

#### Syntax

[DotNetParameter](dotnetparameter.html).ValidEvaluationTypes

#### Data Type

[EvaluationTypes](evaluationtypes.html)

#### Purpose

Returns the valid types to which this parameter can evaluate.

#### Remarks

You can pass the value of this property to the
 validEvaluationTypes
 parameter of the
 [Expression.ValidateEvaluationType](expression-validateevaluationtype.html)
 method to determine whether the value of the
 [DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)
 property contains errors.

If you are using an ExpressionEdit control to display the value of the
 DotNetParameter.ValueExpr
 property, pass the value of this property to the
 
 [ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)
 method.

#### See Also

[DotNetParameter.GetEnumValues](dotnetparameter-getenumvalues.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

[EvaluationTypes](evaluationtypes.html)

[EvaluationTypes.PropertyValueTypeFlags](evaluationtypes-propertyvaluetypeflags.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[ExpressionEdit.GetValidEvaluationTypes](../tsuiref/expressionedit-getvalidevaluationtypes.html)

[ExpressionEdit.SetValidEvaluationTypes](../tsuiref/expressionedit-setvalidevaluationtypes.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-valueexpr.html language=enus -->
## TOPIC 00664: DotNetParameter.ValueExpr

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-valueexpr.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-valueexpr.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.ValueExpr Data Type String Purpose Specifies an expression defining the argument to pass for the parameter when calling the member. See Also DotNetParameter.UseDefaultValue

### DotNetParameter.ValueExpr

#### Syntax

[DotNetParameter](dotnetparameter.html).ValueExpr

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression defining the argument to pass for the parameter when calling the member.

#### See Also

[DotNetParameter.UseDefaultValue](dotnetparameter-usedefaultvalue.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-valueexprisignored.html language=enus -->
## TOPIC 00665: DotNetParameter.ValueExprIsIgnored

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-valueexprisignored.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-valueexprisignored.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.ValueExprIsIgnored Data Type Boolean Purpose Use this property to determine whether the .NET Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values. See Also DotNetParamet

### DotNetParameter.ValueExprIsIgnored

#### Syntax

[DotNetParameter](dotnetparameter.html).ValueExprIsIgnored

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the .NET Adapter ignores the argument value expression when it calls the module. The adapter ignores the argument value expression for parameters that use default values.

#### See Also

[DotNetParameter.UseDefaultValue](dotnetparameter-usedefaultvalue.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

[DotNetParameter.ValueExprIsOptional](dotnetparameter-valueexprisoptional.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter-valueexprisoptional.html language=enus -->
## TOPIC 00666: DotNetParameter.ValueExprIsOptional

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter-valueexprisoptional.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter-valueexprisoptional.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameter.ValueExprIsOptional Data Type Boolean Purpose Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for return values are optional. See Also D

### DotNetParameter.ValueExprIsOptional

#### Syntax

[DotNetParameter](dotnetparameter.html).ValueExprIsOptional

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Use this property to determine whether the argument value expression is optional. You do not have to specify an optional value expression to call the module successfully. Value expressions for return values are optional.

#### See Also

[DotNetParameter.Direction](dotnetparameter-direction.html)

[DotNetParameter.ValueExpr](dotnetparameter-valueexpr.html)

[DotNetParameter.ValueExprIsIgnored](dotnetparameter-valueexprisignored.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameter.html language=enus -->
## TOPIC 00667: DotNetParameter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DotNetParameters class to configure and obtain parameters for a module that uses the .NET Adapter. Use the DotNetCall.Parameters property to obtain the collection of parameters for a module and the DotNetParameter.Elements property to obtain the collection that represents the me

### DotNetParameter

Use objects from the DotNetParameters class to configure and obtain parameters for a module that uses the .NET Adapter. Use the
 [DotNetCall.Parameters](dotnetcall-parameters.html)
 property to obtain the collection of parameters for a module and the
 [DotNetParameter.Elements](dotnetparameter-elements.html)
 property to obtain the collection that represents the members of a structure parameter or the elements of an array of structures parameter.

#### Properties

| ArrayDimensionsEx (Read Only) |
| --- |
| DefaultValue (Read Only) |
| Direction (Read Only) |
| DisplayType (Read Only) |
| DisposeObject |
| Elements (Read Only) |
| Flags (Read Only) |
| HelpString (Read Only) |
| ParameterName (Read Only) |
| Type (Read Only) |
| TypeName (Read Only) |
| UseDefaultValue |
| UserData (Read Only) |
| ValidEvaluationTypes (Read Only) |
| ValueExpr |
| ValueExprIsIgnored (Read Only) |
| ValueExprIsOptional (Read Only) |

#### Methods

| AsPropertyObject |
| --- |
| DeleteArrayElement |
| DisplayCreateCustomDataTypeDialog |
| GetEnumValues |
| InsertArrayElement |
| IsParameterMappingInvalid |
| IsStructMappingInvalid |

#### See Also

[DotNetCall.Parameters](dotnetcall-parameters.html)

[DotNetParameters](dotnetparameters.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameterdirections.html language=enus -->
## TOPIC 00668: DotNetParameterDirections

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameterdirections.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameterdirections.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DotNetParameter.Direction property returns one or more of the following constants to indicate the direction of the parameter. Use the bitwise-AND operator to determine which of these flags are set when obtaining the property value. DotNetParamDirection_In –(Value: 0x1) Indicates that the paramet

### DotNetParameterDirections

The
 [DotNetParameter.Direction](dotnetparameter-direction.html)
 property returns one or more of the following constants to indicate the direction of the parameter. Use the bitwise-AND operator to determine which of these flags are set when obtaining the property value.

- DotNetParamDirection_In 
 –(Value: 0x1) Indicates that the parameter is an input parameter.
- DotNetParamDirection_Out 
 –(Value: 0x2) Indicates that the parameter is an output parameter.
- DotNetParamDirection_Return 
 –(Value: 0x4) Indicates that the parameter is a return value.

#### See Also

[DotNetParameter.Direction](dotnetparameter-direction.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameterflags.html language=enus -->
## TOPIC 00669: DotNetParameterFlags

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameterflags.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameterflags.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DotNetParameter.Flags property returns the following constants to indicate certain attributes of the parameter. Use the bitwise-AND operator to determine whether any of these flags are set when obtaining the property value. DotNetParamFlags_IsArray –(Value: 0x100) Indicates that the parameter is

### DotNetParameterFlags

The
 [DotNetParameter.Flags](dotnetparameter-flags.html)
 property returns the following constants to indicate certain attributes of the parameter. Use the bitwise-AND operator to determine whether any of these flags are set when obtaining the property value.

- DotNetParamFlags_IsArray 
 –(Value: 0x100) Indicates that the parameter is an array.
- DotNetParamFlags_Lcid 
 –(Value: 0x4) Indicates that the parameter is a locale identifier.
- DotNetParamFlags_Optional 
 –(Value: 0x10) Indicates that the parameter is optional.

#### See Also

[DotNetParameter.Flags](dotnetparameter-flags.html)

Parent topic:

Adapter API-Related Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameters-count.html language=enus -->
## TOPIC 00670: DotNetParameters.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameters-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameters-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameters.Count Data Type Long Purpose Returns the number of items in the collection. See Also DotNetParameter

### DotNetParameters.Count

#### Syntax

[DotNetParameters](dotnetparameters.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

#### See Also

[DotNetParameter](dotnetparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameters-item.html language=enus -->
## TOPIC 00671: DotNetParameters.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameters-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameters-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax DotNetParameters.Item( index) Data Type DotNetParameter Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the parameter to retrieve. See Also DotNetParameter

### DotNetParameters.Item

#### Syntax

[DotNetParameters](dotnetparameters.html).Item( index)

#### Data Type

[DotNetParameter](dotnetparameter.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the parameter to retrieve.

#### See Also

[DotNetParameter](dotnetparameter.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparameters.html language=enus -->
## TOPIC 00672: DotNetParameters

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparameters.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparameters.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects from the DotNetParameters class to configure and obtain parameters for a DotNetCall . Use the DotNetCall.Parameters property to obtain the collection of parameters for a call and the DotNetParameter.Elements method to obtain the collection that represents the members of a structure param

### DotNetParameters

Use objects from the DotNetParameters class to configure and obtain parameters for a
 [DotNetCall](dotnetcall.html)
 . Use the
 [DotNetCall.Parameters](dotnetcall-parameters.html)
 property to obtain the collection of parameters for a call and the
 [DotNetParameter.Elements](dotnetparameter-elements.html)
 method to obtain the collection that represents the members of a structure parameter or the elements of an array of structures parameter.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### See Also

[DotNetCall](dotnetcall.html)

[DotNetCall.Parameters](dotnetcall-parameters.html)

[DotNetParameter](dotnetparameter.html)

[DotNetParameter.Elements](dotnetparameter-elements.html)

Parent topic:

TestStand Adapter API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/dotnetparametertypes.html language=enus -->
## TOPIC 00673: DotNetParameterTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/dotnetparametertypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/dotnetparametertypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DotNetParameter.Type property returns one of the following constants to indicate the data type of the parameter: DotNetParamType_Boolean –(Value: 2) Indicates that the parameter is a Boolean type. DotNetParamType_Byte –(Value: 3) Indicates that the parameter is a single-byte value. DotNetParamTy

### DotNetParameterTypes

The
 [DotNetParameter.Type](dotnetparameter-type.html)
 property returns one of the following constants to indicate the data type of the parameter:

- DotNetParamType_Boolean 
 –(Value: 2) Indicates that the parameter is a Boolean type.
- DotNetParamType_Byte 
 –(Value: 3) Indicates that the parameter is a single-byte value.
- DotNetParamType_Char 
 –(Value: 14) Indicates that the parameter is a 16-bit Unicode character.
- DotNetParamType_Class 
 –(Value: 0) Indicates that the parameter is a class reference.
- DotNetParamType_Decimal 
 –(Value: 13) Indicates that the parameter is a 96-bit numeric value. TestStand treats parameters of this type as 64-bit floating point numbers, so some data could be lost.
- DotNetParamType_Double 
 –(Value: 12) Indicates that the parameter is a 64-bit double-precision floating point number.
- DotNetParamType_Enum 
 –(Value: 16) Indicates that the parameter is an enumeration value.
- DotNetParamType_Int16 
 –(Value: 5) Indicates that the parameter is a 16-bit integer.
- DotNetParamType_Int32 
 –(Value: 6) Indicates that the parameter is a 32-bit integer.
- DotNetParamType_Int64 
 –(Value: 7) Indicates that the parameter is a 64-bit integer.
- DotNetParamType_IntPtr 
 –(Value: 15) A platform-specific type that stores a pointer or a handle. For a 32-bit process, the pointer or handle is stored as a 32-bit integer. For a 64-bit process, the pointer or handle is stored as a 64-bit integer.
- DotNetParamType_Object 
 –(Value: 17) Indicates that the parameter is an object reference.
- DotNetParamType_SByte 
 –(Value: 4) Indicates that the parameter is a signed-byte value.
- DotNetParamType_Single 
 –(Value: 11) Indicates that the parameter is a 32-bit single-precision floating point number.
- DotNetParamType_String 
 –(Value: 1) Indicates that the parameter is a string.
- DotNetParamType_Struct 
 –(Value: 18) Indicates that the parameter is a struct.
- DotNetParamType_UInt16 
 –(Value: 8) Indicates that the parameter is a 16-bit unsigned integer.
- DotNetParamType_UInt32 
 –(Value: 9) Indicates that the parameter is a 32-bit unsigned integer.
- DotNetParamType_UInt64 
 –(Value: 10) Indicates that the parameter is a 64-bit unsigned integer.
- DotNetParamType_UIntPtr 
 –(Value: 20) A platform-specific type that stores a pointer or a handle. For a 32-bit process, the pointer or handle is stored as an unsigned 32-bit integer. For a 64-bit process, the pointer or handle is stored as an unsigned 64-bit integer.
- DotNetParamType_Void 
 –(Value: 19) Indicates that the parameter is a void parameter; therefore, it has no value. This type applies only to return values.

#### See Also

[DotNetParameter.Type](dotnetparameter-type.html)

Parent topic:

Adapter API-Related Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-addselectedpropertyobject.html language=enus -->
## TOPIC 00674: EditArgs.AddSelectedPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-addselectedpropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-addselectedpropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.AddSelectedPropertyObject( propertyToAdd) Purpose Adds a PropertyObject to the list of currently selected property objects. Remarks Stores the selected PropertyObject so you can use it in the sequence context. Parameters propertyToAdd As PropertyObject [In] Specifies the PropertyObje

### EditArgs.AddSelectedPropertyObject

#### Syntax

[EditArgs](editargs.html).AddSelectedPropertyObject( propertyToAdd)

#### Purpose

Adds a PropertyObject to the list of currently selected property objects.

#### Remarks

Stores the selected PropertyObject so you can use it in the sequence context.

#### Parameters

propertyToAdd
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the PropertyObject being added to the list.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-addselectedsequence.html language=enus -->
## TOPIC 00675: EditArgs.AddSelectedSequence

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-addselectedsequence.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-addselectedsequence.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.AddSelectedSequence( sequence) Purpose Adds a sequence to the list of currently selected sequences. Remarks Stores the selected sequence so you can use it in the sequence context. Parameters sequence As Sequence [In] Specifies the sequence object being added to the list. See Also Seq

### EditArgs.AddSelectedSequence

#### Syntax

[EditArgs](editargs.html).AddSelectedSequence( sequence)

#### Purpose

Adds a sequence to the list of currently selected sequences.

#### Remarks

Stores the selected sequence so you can use it in the sequence context.

#### Parameters

sequence
 As
 [Sequence](sequence.html)

[In] Specifies the sequence object being added to the list.

#### See Also

[Sequence](sequence.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-addselectedstep.html language=enus -->
## TOPIC 00676: EditArgs.AddSelectedStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-addselectedstep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-addselectedstep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.AddSelectedStep( step) Purpose Adds a step to the list of currently selected steps. Remarks Stores the selected step so you can use it in the sequence context. Parameters step As Step [In] Specifies the step object being added to the list. See Also Step

### EditArgs.AddSelectedStep

#### Syntax

[EditArgs](editargs.html).AddSelectedStep( step)

#### Purpose

Adds a step to the list of currently selected steps.

#### Remarks

Stores the selected step so you can use it in the sequence context.

#### Parameters

step
 As
 [Step](step.html)

[In] Specifies the step object being added to the list.

#### See Also

[Step](step.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-aspropertyobject.html language=enus -->
## TOPIC 00677: EditArgs.AsPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-aspropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-aspropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.AsPropertyObject Return Value PropertyObject Purpose Returns the underlying PropertyObject that represents the EditArgs object. Remarks Use the PropertyObject class to modify, add, or remove the custom properties of the object. Do not use this method to remove or modify the dynamic p

### EditArgs.AsPropertyObject

#### Syntax

[EditArgs](editargs.html).AsPropertyObject

#### Return Value

[PropertyObject](propertyobject.html)

#### Purpose

Returns the underlying PropertyObject that represents the EditArgs object.

#### Remarks

Use the PropertyObject class to modify, add, or remove the custom properties of the object.

Do not use this method to remove or modify the dynamic properties TestStand already provides for EditArgs objects. Instead, use any of the other methods of the EditArgs class to remove or modify the dynamic properties.

#### See Also

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-clearselectedpropertyobjects.html language=enus -->
## TOPIC 00678: EditArgs.ClearSelectedPropertyObjects

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-clearselectedpropertyobjects.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-clearselectedpropertyobjects.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.ClearSelectedPropertyObjects Purpose Clears the list of currently selected property objects.

### EditArgs.ClearSelectedPropertyObjects

#### Syntax

[EditArgs](editargs.html).ClearSelectedPropertyObjects

#### Purpose

Clears the list of currently selected property objects.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-clearselectedsequences.html language=enus -->
## TOPIC 00679: EditArgs.ClearSelectedSequences

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-clearselectedsequences.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-clearselectedsequences.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.ClearSelectedSequences Purpose Clears the list of currently selected sequences.

### EditArgs.ClearSelectedSequences

#### Syntax

[EditArgs](editargs.html).ClearSelectedSequences

#### Purpose

Clears the list of currently selected sequences.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-clearselectedsteps.html language=enus -->
## TOPIC 00680: EditArgs.ClearSelectedSteps

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-clearselectedsteps.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-clearselectedsteps.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.ClearSelectedSteps Purpose Clears the list of currently selected steps.

### EditArgs.ClearSelectedSteps

#### Syntax

[EditArgs](editargs.html).ClearSelectedSteps

#### Purpose

Clears the list of currently selected steps.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-setselectedexecution.html language=enus -->
## TOPIC 00681: EditArgs.SetSelectedExecution

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-setselectedexecution.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-setselectedexecution.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.SetSelectedExecution( execution) Purpose Use this property to set the currently active execution as the selected execution. Remarks Stores the selected execution so you can use it in the sequence context. Parameters execution As Execution [In] Specifies the selected Execution object.

### EditArgs.SetSelectedExecution

#### Syntax

[EditArgs](editargs.html).SetSelectedExecution( execution)

#### Purpose

Use this property to set the currently active execution as the selected execution.

#### Remarks

Stores the selected execution so you can use it in the sequence context.

#### Parameters

execution
 As
 [Execution](execution.html)

[In] Specifies the selected Execution object.

#### See Also

[Execution](execution.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-setselectedpropertyobjectfile.html language=enus -->
## TOPIC 00682: EditArgs.SetSelectedPropertyObjectFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-setselectedpropertyobjectfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-setselectedpropertyobjectfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.SetSelectedPropertyObjectFile( propertyFile) Purpose Use this property to set the currently active property object file as the selected property object file. Remarks Stores the selected property object file so you can use it in the sequence context. Parameters propertyFile As Propert

### EditArgs.SetSelectedPropertyObjectFile

#### Syntax

[EditArgs](editargs.html).SetSelectedPropertyObjectFile( propertyFile)

#### Purpose

Use this property to set the currently active property object file as the selected property object file.

#### Remarks

Stores the selected property object file so you can use it in the sequence context.

#### Parameters

propertyFile
 As
 [PropertyObjectFile](propertyobjectfile.html)

[In] Specifies the selected PropertyObjectFile object.

#### See Also

[PropertyObjectFile](propertyobjectfile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-setselectedsequencefile.html language=enus -->
## TOPIC 00683: EditArgs.SetSelectedSequenceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-setselectedsequencefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-setselectedsequencefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.SetSelectedSequenceFile( sequenceFile) Purpose Use this property to set the currently active sequence file as the selected sequence file. Remarks Stores the selected sequence file so you can use it in the sequence context. Parameters sequenceFile As SequenceFile [In] Specifies the ac

### EditArgs.SetSelectedSequenceFile

#### Syntax

[EditArgs](editargs.html).SetSelectedSequenceFile( sequenceFile)

#### Purpose

Use this property to set the currently active sequence file as the selected sequence file.

#### Remarks

Stores the selected sequence file so you can use it in the sequence context.

#### Parameters

sequenceFile
 As
 [SequenceFile](sequencefile.html)

[In] Specifies the active SequenceFile object.

#### See Also

[SequenceFile](sequencefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs-setselectedstepgroup.html language=enus -->
## TOPIC 00684: EditArgs.SetSelectedStepGroup

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs-setselectedstepgroup.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs-setselectedstepgroup.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditArgs.SetSelectedStepGroup( stepGroupParam) Purpose Use this property to set the currently active step group as the selected step group. Remarks Stores the selected step group so you can use it in the sequence context. Parameters stepGroupParam As StepGroups [In] Specifies an active step g

### EditArgs.SetSelectedStepGroup

#### Syntax

[EditArgs](editargs.html).SetSelectedStepGroup( stepGroupParam)

#### Purpose

Use this property to set the currently active step group as the selected step group.

#### Remarks

Stores the selected step group so you can use it in the sequence context.

#### Parameters

stepGroupParam
 As
 [StepGroups](stepgroups.html)

[In] Specifies an active step group object.

#### See Also

[StepGroups](stepgroups.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editargs.html language=enus -->
## TOPIC 00685: EditArgs

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editargs.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editargs.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use objects of the EditArgs class to pass information about the current state of the user interface to methods such as Engine.NewExecution , Sequence.EvalEntryPointNameExpressionEx , Engine.GetEditTimeToolMenuItems , and Engine.GetRunTimeToolMenuItems . Objects of this class contain information abou

### EditArgs

Use objects of the EditArgs class to pass information about the current state of the user interface to methods such as
 [Engine.NewExecution](engine-newexecution.html)
 ,
 [Sequence.EvalEntryPointNameExpressionEx](sequence-evalentrypointnameexpressionex.html)
 ,
 [Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)
 , and
 [Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)
 . Objects of this class contain information about currently selected sequences, steps, sequence files, and executions. This selection information appears in the
 RunState.InitialSelection
 property of the sequence context.

Create objects of this class using the
 [Engine.NewEditArgs](engine-neweditargs.html)
 method. Typically, you use this class only when you are writing a user interface or sequence editor.

#### Methods

| AddSelectedPropertyObject |
| --- |
| AddSelectedSequence |
| AddSelectedStep |
| AsPropertyObject |
| ClearSelectedPropertyObjects |
| ClearSelectedSequences |
| ClearSelectedSteps |
| SetSelectedExecution |
| SetSelectedPropertyObjectFile |
| SetSelectedSequenceFile |
| SetSelectedStepGroup |

#### See Also

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Engine.NewEditArgs](engine-neweditargs.html)

[Engine.NewExecution](engine-newexecution.html)

[Engine.NewHierarchicalExecution](engine-newhierarchicalexecution.html)

[Sequence.EvalEntryPointEnabledExpressionEx](sequence-evalentrypointenabledexpressionex.html)

[Sequence.EvalEntryPointNameExpressionEx](sequence-evalentrypointnameexpressionex.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editbreakandwatchoptions.html language=enus -->
## TOPIC 00686: EditBreakAndWatchOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editbreakandwatchoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editbreakandwatchoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the dlgOptions parameter of the Engine.DisplayEditBreakAndWatchDialog method. Use the bitwise-OR operator to specify more than one option. By default, TestStand displays both the Breakpoints and Watch Expression tabs. EditBreakAndWatch_DisplayBr

### EditBreakAndWatchOptions

These constants represent the options you can use with the
 dlgOptions
 parameter of the
 [Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)
 method. Use the bitwise-OR operator to specify more than one option.

By default, TestStand displays both the Breakpoints and Watch Expression tabs.

- EditBreakAndWatch_DisplayBreakpointTab 
 –(Value: 0x1) Use this option to display only the
 Breakpoints tab 
 of the
 Edit Breakpoints/Watch Expressions 
 dialog box.
- EditBreakAndWatch_DisplayWatchExpressionTab 
 –( Value: 0x2) Use this option to display only the
 Watch Expressions tab 
 of the Edit Breakpoints/Watch Expressions dialog box.
- EditBreakAndWatch_ModalToAppMainWind 
 –(Value : 0x10000) By default, the Edit Breakpoints/Watch Expressions dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from AppMainHwnd. If you set this option, the Edit Breakpoints/Watch Expressions dialog box is modal with respect to the window handle of the
 Engine.AppMainHwnd 
 property. Typically, you do not need to set this option.
- EditBreakAndWatch_NoOptions 
 –(Value: 0x0) Specifies no options. TestStand displays both the Breakpoints and Watch Expressions tabs.
- EditBreakAndWatch_ReadOnly 
 –(Value: 0x20000) Use this option to create a read-only version of the Edit Breakpoints/Watch Expressions dialog box.

#### See Also

[Breakpoints tab](../tsref/breakpoints-tab-edit-breakpoints-watch-expres.html)

[Edit Breakpoints/Watch Expressions dialog box](../tsref/edit-breakpoints-watch-expressions-dialog-box.html)

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayEditBreakAndWatchDialog](engine-displayeditbreakandwatchdialog.html)

[Watch Expressions tab](../tsref/watch-expressions-tab-edit-breakpoints-watch.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editkinds.html language=enus -->
## TOPIC 00687: EditKinds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editkinds.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editkinds.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this enumeration to refer to a specific kind of edit for the Engine.NewUndoItemCreator , UndoItem.RedoEditKind , UndoItem.UndoEditKind , UndoItemCreator.BeginBatchEdit , and UndoItemCreator.BeginEditEx methods, and the BeginEdit, CanEdit and EndEdit methods and events of the ApplicationMgr class

### EditKinds

Use this enumeration to refer to a specific kind of edit for the
 [Engine.NewUndoItemCreator](engine-newundoitemcreator.html)
 ,
 [UndoItem.RedoEditKind](undoitem-redoeditkind.html)
 ,
 [UndoItem.UndoEditKind](undoitem-undoeditkind.html)
 ,
 [UndoItemCreator.BeginBatchEdit](undoitemcreator-beginbatchedit.html)
 , and
 [UndoItemCreator.BeginEditEx](undoitemcreator-begineditex.html)
 methods, and the BeginEdit, CanEdit and EndEdit methods and events of the
 
 [ApplicationMgr](../tsuiref/applicationmgr.html)
 class.

- EditKind_ChangeNumericFormat 
 –(Value: 5) Specifies changing the numeric format of a
 PropertyObject 
 .
- EditKind_ChangeObject 
 –(Value: 16) Specifies any change to a TestStand object.
- EditKind_ChangeRepresentation 
 –(Value: 22)
- EditKind_ChangeRunMode 
 –(Value: 20) Specifies changing the run mode of a step.
- EditKind_ChangeSequenceFileProperties 
 –(Value: 19) Specifies modifying a sequence file though the
 Sequence File Properties 
 dialog box.
- EditKind_ChangeSequenceProperties 
 –(Value: 18) Specifies modifying a sequence though the
 Sequence Properties 
 dialog box.
- EditKind_ChangeStep 
 –(Value: 17) Specifies modifying subproperties of a step.
- EditKind_ChangeValue 
 –(Value: 1) Specifies changing the value of a PropertyObject.
- EditKind_DeleteProperty 
 –(Value: 7) Specifies deleting a PropertyObject.
- EditKind_DeleteSequence 
 –(Value: 14) Specifies deleting a sequence.
- EditKind_DeleteStep 
 –(Value: 11) Specifies deleting a step.
- EditKind_InsertProperty 
 –(Value: 6) Specifies inserting a PropertyObject.
- EditKind_InsertSequence 
 –(Value: 13) Specifies inserting a sequence.
- EditKind_InsertStep 
 –(Value: 10) Specifies inserting a step.
- EditKind_InsertType 
 –(Value: 21) Specifies inserting a new type.
- EditKind_ModifyAttributes 
 –(Value: 23) Specifies modifying the attributes of a PropertyObject.
- EditKind_ModifyComment 
 –(Value: 3) Specifies modifying the comment of a PropertyObject.
- EditKind_ModifyFlags 
 –(Value: 4) Specifies modifying the flags of a PropertyObject.
- EditKind_MoveProperty 
 –(Value: 8) Specifies moving a PropertyObject.
- EditKind_MoveSequence 
 –(Value: 15) Specifies moving a sequence.
- EditKind_MoveStep 
 –(Value: 12) Specifies moving a step.
- EditKind_MoveType 
 –(Value: #) Specifies moving a type. Does not support undo.
- EditKind_None 
 –(Value: 0) No edit.
- EditKind_Rename 
 –(Value: 2) Specifies renaming a PropertyObject.
- EditKind_ReplaceProperty 
 –(Value: 9) Specifies replacing a PropertyObject.

#### See Also

[ApplicationMgr](../tsuiref/applicationmgr.html)

[Engine.NewUndoItemCreator](engine-newundoitemcreator.html)

[Sequence File Properties dialog box](../tsref/sequence-file-properties-dialog-box.html)

[Sequence Properties dialog box](../tsref/sequence-properties-dialog-box.html)

[UndoItem.RedoEditKind](undoitem-redoeditkind.html)

[UndoItem.UndoEditKind](undoitem-undoeditkind.html)

[UndoItemCreator.BeginBatchEdit](undoitemcreator-beginbatchedit.html)

[UndoItemCreator.BeginEditEx](undoitemcreator-begineditex.html)

Parent topic:

Core API Enumerations

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editnumericformatoptions.html language=enus -->
## TOPIC 00688: EditNumericFormatOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editnumericformatoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editnumericformatoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the evaluationOptions parameter of the Engine.DisplayEditNumericFormatDialogEx method. Use the bitwise-OR operator to specify more than one option. EditNumFormat_AllowDefaultFormat –(Value: 0x1) Use this option to allow the user to set the numer

### EditNumericFormatOptions

These constants represent the options you can use with the
 evaluationOptions
 parameter of the
 [Engine.DisplayEditNumericFormatDialogEx](engine-displayeditnumericformatdialogex.html)
 method. Use the bitwise-OR operator to specify more than one option.

- EditNumFormat_AllowDefaultFormat 
 –(Value: 0x1) Use this option to allow the user to set the numeric format to the default value in the
 Numeric Format 
 dialog box.
- EditNumFormat_ModalToAppMainWind 
 –(Value: 0x10000) By default, the dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 Engine.AppMainHwnd 
 property. Typically, you do not need to set this option.
- EditNumFormat_NoOptions 
 –(Value: 0) No options.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayEditNumericFormatDialogEx](engine-displayeditnumericformatdialogex.html)

[Numeric Format dialog box](../tsref/numeric-format-dialog-box.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/editpathsdialogoptions.html language=enus -->
## TOPIC 00689: EditPathsDialogOptions

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/editpathsdialogoptions.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/editpathsdialogoptions.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: These constants represent the options you can use with the dlgOptions parameter of the Engine.DisplayEditPathsInFilesDialog method. Use the bitwise-OR operator to specify more than one option. EditPaths_AllowEditOfReadOnlyFiles –(Value: 0x1) Allows modifications to paths in read-only files in the di

### EditPathsDialogOptions

These constants represent the options you can use with the
 dlgOptions
 parameter of the
 [Engine.DisplayEditPathsInFilesDialog](engine-displayeditpathsinfilesdialog.html)
 method. Use the bitwise-OR operator to specify more than one option.

- EditPaths_AllowEditOfReadOnlyFiles 
 –(Value: 0x1) Allows modifications to paths in read-only files in the dialog box.
- EditPaths_ModalToAppMainWind 
 –(Value: 0x10000) By default, the dialog box is modal to the last active window of the calling thread, or if none exists, to the last active window from AppMainHwnd. If you set this option, the dialog box is modal with respect to the window handle of the
 Engine.AppMainHwnd 
 property. Typically, you do not need to set this option.
- EditPaths_NoOptions 
 –(Value: 0x0) No options.
- EditPaths_ReadOnly 
 –(Value: 0x20000) Creates a read-only version of the dialog box.

#### See Also

[Engine.AppMainHwnd](engine-appmainhwnd.html)

[Engine.DisplayEditPathsInFilesDialog](engine-displayeditpathsinfilesdialog.html)

Parent topic:

Core API Constants

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-commandarguments.html language=enus -->
## TOPIC 00690: EditTimeMenuItem.CommandArguments

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-commandarguments.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-commandarguments.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.CommandArguments Data Type String Purpose Specifies the command-line arguments to pass to the command the EditTimeMenuItem.CommandPath property specifies. Remarks This property applies only when the EditTimeMenuItem.Type property is set to ToolMenuType_Command . See Also Edit

### EditTimeMenuItem.CommandArguments

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).CommandArguments

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the command-line arguments to pass to the command the
 [EditTimeMenuItem.CommandPath](edittimemenuitem-commandpath.html)
 property specifies.

#### Remarks

This property applies only when the
 [EditTimeMenuItem.Type](edittimemenuitem-type.html)
 property is set to
 ToolMenuType_Command
 .

#### See Also

[EditTimeMenuItem.CommandInitialDirectory](edittimemenuitem-commandinitialdirectory.html)

[EditTimeMenuItem.CommandPath](edittimemenuitem-commandpath.html)

[EditTimeMenuItem.Type](edittimemenuitem-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-commandargumentsexpression.html language=enus -->
## TOPIC 00691: EditTimeMenuItem.CommandArgumentsExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-commandargumentsexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-commandargumentsexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.CommandArgumentsExpression Data Type String Purpose Specifies an expression defining the command-line arguments to pass to the command that the EditTimeMenuItem.CommandPath property specifies. Remarks This property applies only when the EditTimeMenuItem.Type property is set t

### EditTimeMenuItem.CommandArgumentsExpression

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).CommandArgumentsExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies an expression defining the command-line arguments to pass to the command that the EditTimeMenuItem.CommandPath property specifies.

#### Remarks

This property applies only when the EditTimeMenuItem.Type property is set to ToolMenuType_Command.

#### See Also

[CommandPath](edittimemenuitem-commandpath.html)

[CommandArguments](edittimemenuitem-commandarguments.html)

[Type](edittimemenuitem-type.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-commandinitialdirectory.html language=enus -->
## TOPIC 00692: EditTimeMenuItem.CommandInitialDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-commandinitialdirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-commandinitialdirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.CommandInitialDirectory Data Type String Purpose Specifies the initial working directory when invoking the command the EditTimeMenuItem.CommandPath property specifies. See Also EditTimeMenuItem.CommandArguments EditTimeMenuItem.CommandPath

### EditTimeMenuItem.CommandInitialDirectory

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).CommandInitialDirectory

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the initial working directory when invoking the command the
 [EditTimeMenuItem.CommandPath](edittimemenuitem-commandpath.html)
 property specifies.

#### See Also

[EditTimeMenuItem.CommandArguments](edittimemenuitem-commandarguments.html)

[EditTimeMenuItem.CommandPath](edittimemenuitem-commandpath.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-commandpath.html language=enus -->
## TOPIC 00693: EditTimeMenuItem.CommandPath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-commandpath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-commandpath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.CommandPath Data Type String Purpose Specifies the path to the executable or system command the menu item invokes. See Also EditTimeMenuItem.CommandArguments EditTimeMenuItem.CommandInitialDirectory RunTimeMenuItem.InvokeItem

### EditTimeMenuItem.CommandPath

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).CommandPath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path to the executable or system command the menu item invokes.

#### See Also

[EditTimeMenuItem.CommandArguments](edittimemenuitem-commandarguments.html)

[EditTimeMenuItem.CommandInitialDirectory](edittimemenuitem-commandinitialdirectory.html)

[RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-editable.html language=enus -->
## TOPIC 00694: EditTimeMenuItem.Editable

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-editable.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-editable.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.Editable Data Type Boolean Purpose Specifies whether the properties of the menu item display as read-only. See Also EditTimeMenuItem.ItemTextExpression

### EditTimeMenuItem.Editable

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).Editable

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether the properties of the menu item display as read-only.

#### See Also

[EditTimeMenuItem.ItemTextExpression](edittimemenuitem-itemtextexpression.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-editsselectedfile.html language=enus -->
## TOPIC 00695: EditTimeMenuItem.EditsSelectedFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-editsselectedfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-editsselectedfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.EditsSelectedFile Data Type Boolean Purpose Specifies if the Tools menu item edits the selected sequence file. Remarks This property applies only to sequence and sequence file item types. The sequence editor uses this option to determine whether to prompt the user to check ou

### EditTimeMenuItem.EditsSelectedFile

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).EditsSelectedFile

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies if the Tools menu item edits the selected sequence file.

#### Remarks

This property applies only to sequence and sequence file item types. The sequence editor uses this option to determine whether to prompt the user to check out the selected file from source control if it is not already checked out.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-enabledexpression.html language=enus -->
## TOPIC 00696: EditTimeMenuItem.EnabledExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-enabledexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-enabledexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.EnabledExpression Data Type String Purpose Specifies the expression TestStand uses to determine whether the menu item is enabled at run time. See Also EditTimeMenuItem.HiddenExpression EditTimeMenuItem.ItemTextExpression RunTimeMenuItem.ItemEnabled

### EditTimeMenuItem.EnabledExpression

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).EnabledExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the expression TestStand uses to determine whether the menu item is enabled at run time.

#### See Also

[EditTimeMenuItem.HiddenExpression](edittimemenuitem-hiddenexpression.html)

[EditTimeMenuItem.ItemTextExpression](edittimemenuitem-itemtextexpression.html)

[RunTimeMenuItem.ItemEnabled](runtimemenuitem-itemenabled.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-hiddenexpression.html language=enus -->
## TOPIC 00697: EditTimeMenuItem.HiddenExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-hiddenexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-hiddenexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.HiddenExpression Data Type String Purpose Specifies the expression TestStand uses to determine whether the menu item is visible at run time. Remarks TestStand excludes any edit-time menu items with hidden expressions that evaluate to False from the run-time collection.

### EditTimeMenuItem.HiddenExpression

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).HiddenExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the expression TestStand uses to determine whether the menu item is visible at run time.

#### Remarks

TestStand excludes any edit-time menu items with hidden expressions that evaluate to
 False
 from the run-time collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-itemtextexpression.html language=enus -->
## TOPIC 00698: EditTimeMenuItem.ItemTextExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-itemtextexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-itemtextexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.ItemTextExpression Data Type String Purpose Specifies the expression TestStand uses to determine the menu item text at run time. See Also EditTimeMenuItem.EnabledExpression EditTimeMenuItem.HiddenExpression RunTimeMenuItem.Text

### EditTimeMenuItem.ItemTextExpression

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).ItemTextExpression

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the expression TestStand uses to determine the menu item text at run time.

#### See Also

[EditTimeMenuItem.EnabledExpression](edittimemenuitem-enabledexpression.html)

[EditTimeMenuItem.HiddenExpression](edittimemenuitem-hiddenexpression.html)

[RunTimeMenuItem.Text](runtimemenuitem-text.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-separatorbefore.html language=enus -->
## TOPIC 00699: EditTimeMenuItem.SeparatorBefore

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-separatorbefore.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-separatorbefore.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.SeparatorBefore Data Type Boolean Purpose Specifies that a menu separator precedes the Tools menu item.

### EditTimeMenuItem.SeparatorBefore

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).SeparatorBefore

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies that a menu separator precedes the Tools menu item.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-sequencefilepath.html language=enus -->
## TOPIC 00700: EditTimeMenuItem.SequenceFilePath

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-sequencefilepath.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-sequencefilepath.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.SequenceFilePath Data Type String Purpose Specifies the path to the sequence file for sequence and sequence file menu types. Remarks This property applies only when the EditTimeMenuItem.Type property is set to ToolMenuType_SequenceFile or ToolMenuType_Sequence . The run-time

### EditTimeMenuItem.SequenceFilePath

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).SequenceFilePath

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the path to the sequence file for sequence and sequence file menu types.

#### Remarks

This property applies only when the
 [EditTimeMenuItem.Type](edittimemenuitem-type.html)
 property is set to
 ToolMenuType_SequenceFile
 or
 ToolMenuType_Sequence
 .

The run-time copy of the Tools menu automatically expands submenus for menu items using the
 ToolMenuType_SequenceFile
 type, where each submenu item is a menu item using the
 ToolMenuType_Sequence
 type.

#### See Also

[EditTimeMenuItem.SequenceName](edittimemenuitem-sequencename.html)

[EditTimeMenuItem.Type](edittimemenuitem-type.html)

[RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-sequencename.html language=enus -->
## TOPIC 00701: EditTimeMenuItem.SequenceName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-sequencename.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-sequencename.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.SequenceName Data Type String Purpose Specifies the name of the sequence that TestStand launches in an execution for sequence menu item types. See Also EditTimeMenuItem.SequenceFilePath RunTimeMenuItem.InvokeItem

### EditTimeMenuItem.SequenceName

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).SequenceName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the name of the sequence that TestStand launches in an execution for sequence menu item types.

#### See Also

[EditTimeMenuItem.SequenceFilePath](edittimemenuitem-sequencefilepath.html)

[RunTimeMenuItem.InvokeItem](runtimemenuitem-invokeitem.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-submenuitems.html language=enus -->
## TOPIC 00702: EditTimeMenuItem.SubMenuItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-submenuitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-submenuitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.SubMenuItems Data Type EditTimeMenuItems Purpose Returns a collection of Tools menu items that represent the submenu for the menu item. Remarks The collection exists only when the EditTimeMenuItem.Type property is set to ToolMenuType_SubMenu . Otherwise, this property returns

### EditTimeMenuItem.SubMenuItems

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).SubMenuItems

#### Data Type

[EditTimeMenuItems](edittimemenuitems.html)

#### Purpose

Returns a collection of Tools menu items that represent the submenu for the menu item.

#### Remarks

The collection exists only when the
 [EditTimeMenuItem.Type](edittimemenuitem-type.html)
 property is set to
 ToolMenuType_SubMenu
 . Otherwise, this property returns
 NULL
 .

#### See Also

[EditTimeMenuItem.Type](edittimemenuitem-type.html)

[EditTimeMenuItems](edittimemenuitems.html)

[RunTimeMenuItem.SubMenuItems](runtimemenuitem-submenuitems.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem-type.html language=enus -->
## TOPIC 00703: EditTimeMenuItem.Type

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem-type.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem-type.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItem.Type Data Type ToolMenuTypes Use the following constants with this data type: ToolMenuType_Command –(Value: 1) Invokes a Microsoft Windows executable or command with optional arguments. ToolMenuType_Sequence –(Value: 2) Initiates an execution on a sequence in a sequence file.

### EditTimeMenuItem.Type

#### Syntax

[EditTimeMenuItem](edittimemenuitem.html).Type

#### Data Type

[ToolMenuTypes](toolmenutypes.html)

Use the following constants with this data type:

- ToolMenuType_Command 
 –(Value: 1) Invokes a Microsoft Windows executable or command with optional arguments.
- ToolMenuType_Sequence 
 –(Value: 2) Initiates an execution on a sequence in a sequence file.
- ToolMenuType_SequenceFile 
 –(Value: 4) Creates a submenu that lists all sequences in a sequence file as menu items.
- ToolMenuType_SubMenu 
 –(Value: 3) Contains additional menu items in a submenu.

#### Purpose

Specifies the type of Tools menu item.

#### Remarks

If you set this property to
 ToolMenuType_SubMenu
 , TestStand assigns an
 [EditTimeMenuItems](edittimemenuitems.html)
 collection object to
 [SubMenuItems](edittimemenuitem-submenuitems.html)
 .

#### See Also

[EditTimeMenuItems](edittimemenuitems.html)

[SubMenuItems](edittimemenuitem-submenuitems.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitem.html language=enus -->
## TOPIC 00704: EditTimeMenuItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Objects of the EditTimeMenuItem class represent menu items in the sequence editor or user interface. A menu item is a command, a call to a sequence, a submenu, or a submenu of calls to sequences in a sequence file. EditTimeMenuItem objects specify the menu item type, which includes paths and argumen

### EditTimeMenuItem

Objects of the EditTimeMenuItem class represent menu items in the sequence editor or user interface. A menu item is a command, a call to a sequence, a submenu, or a submenu of calls to sequences in a sequence file. EditTimeMenuItem objects specify the menu item type, which includes paths and arguments for commands, paths for sequence files, and names of sequences. Each object specifies an expression for evaluating item text at run time, and expressions that determine whether the item is enabled or visible at run time.

Use the
 [Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)
 method to obtain a reference to a collection of EditTimeMenuItem objects for the TestStand Tools menu. Use this collection to customize the contents of the Tools menu.

Use the
 [Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)
 method to obtain a reference to a collection of RunTimeMenuItem objects, which represent an evaluated version of the Tools menu. Use this collection to determine what is displayed in the Tools menu at run time.

#### Properties

| CommandArguments |
| --- |
| CommandArgumentsExpression |
| CommandInitialDirectory |
| CommandPath |
| Editable |
| EditsSelectedFile |
| EnabledExpression |
| HiddenExpression |
| ItemTextExpression |
| SeparatorBefore |
| SequenceFilePath |
| SequenceName |
| SubMenuItems (Read Only) |
| Type |

#### See Also

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitems-count.html language=enus -->
## TOPIC 00705: EditTimeMenuItems.Count

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitems-count.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitems-count.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItems.Count Data Type Long Purpose Returns the number of items in the collection.

### EditTimeMenuItems.Count

#### Syntax

[EditTimeMenuItems](edittimemenuitems.html).Count

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the number of items in the collection.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitems-insert.html language=enus -->
## TOPIC 00706: EditTimeMenuItems.Insert

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitems-insert.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitems-insert.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItems.Insert( type, index = -1) Return Value EditTimeMenuItem Purpose Adds a new item to the collection. Parameters type As ToolMenuTypes [In] Specifies the type of menu item to insert. index As Long [In] Specifies the index where the new menu item is inserted. If you pass -1, the

### EditTimeMenuItems.Insert

#### Syntax

[EditTimeMenuItems](edittimemenuitems.html).Insert( type, index = -1)

#### Return Value

[EditTimeMenuItem](edittimemenuitem.html)

#### Purpose

Adds a new item to the collection.

#### Parameters

type
 As
 [ToolMenuTypes](toolmenutypes.html)

[In] Specifies the type of menu item to insert.

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the index where the new menu item is inserted. If you pass -1, the new item is inserted at the end of the list.

This parameter has a default value of
 -1
 .

#### See Also

[EditTimeMenuItem](edittimemenuitem.html)

[EditTimeMenuItems.Count](edittimemenuitems-count.html)

[EditTimeMenuItems.Remove](edittimemenuitems-remove.html)

[ToolMenuTypes](toolmenutypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitems-item.html language=enus -->
## TOPIC 00707: EditTimeMenuItems.Item

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitems-item.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitems-item.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItems.Item( index) Data Type EditTimeMenuItem Purpose Returns a reference to an item at the specified index in the collection. Parameters index As Variant [In] Specifies the zero-based index of the item to retrieve. See Also EditTimeMenuItem EditTimeMenuItems.Count

### EditTimeMenuItems.Item

#### Syntax

[EditTimeMenuItems](edittimemenuitems.html).Item( index)

#### Data Type

[EditTimeMenuItem](edittimemenuitem.html)

#### Purpose

Returns a reference to an item at the specified index in the collection.

#### Parameters

index
 As
 [Variant](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to retrieve.

#### See Also

[EditTimeMenuItem](edittimemenuitem.html)

[EditTimeMenuItems.Count](edittimemenuitems-count.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitems-moveitem.html language=enus -->
## TOPIC 00708: EditTimeMenuItems.MoveItem

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitems-moveitem.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitems-moveitem.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItems.MoveItem( index, newIndex) Purpose Moves the menu item specified by a specific index to a new index within the list. Parameters index As Long [In] Specifies the zero-based index of the item to move. newIndex As Long [In] Specifies a zero-based index determining where to move

### EditTimeMenuItems.MoveItem

#### Syntax

[EditTimeMenuItems](edittimemenuitems.html).MoveItem( index, newIndex)

#### Purpose

Moves the menu item specified by a specific index to a new index within the list.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to move.

newIndex
 As
 [Long](data-types-for-teststand.html)

[In] Specifies a zero-based index determining where to move the menu item to.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitems-remove.html language=enus -->
## TOPIC 00709: EditTimeMenuItems.Remove

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitems-remove.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitems-remove.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax EditTimeMenuItems.Remove( index) Purpose Removes the menu item at the specified index. Parameters index As Long [In] Specifies the zero-based index of the item to remove.

### EditTimeMenuItems.Remove

#### Syntax

[EditTimeMenuItems](edittimemenuitems.html).Remove( index)

#### Purpose

Removes the menu item at the specified index.

#### Parameters

index
 As
 [Long](data-types-for-teststand.html)

[In] Specifies the zero-based index of the item to remove.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/edittimemenuitems.html language=enus -->
## TOPIC 00710: EditTimeMenuItems

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/edittimemenuitems.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/edittimemenuitems.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: The EditTimeMenuItems class specifies a collection of EditTimeMenuItem objects. An EditTimeMenuItem object represents a menu item such as a command, a call to a sequence, a submenu, or a submenu of calls to sequence in a sequence file. Each object in the collection specifies the menu item type and t

### EditTimeMenuItems

The EditTimeMenuItems class specifies a collection of EditTimeMenuItem objects. An EditTimeMenuItem object represents a menu item such as a command, a call to a sequence, a submenu, or a submenu of calls to sequence in a sequence file. Each object in the collection specifies the menu item type and the expressions which determine the item text, hidden state, and enabled state. A submenu item specifies a collection of menu items in the submenu.

Use the
 [Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)
 method to obtain a reference to a collection of this class for the Tools menu. Use this collection to customize the contents of the Tools menu.

#### Properties

| Count (Read Only) |
| --- |
| Item (Read Only) |

#### Methods

| Insert |
| --- |
| MoveItem |
| Remove |

#### See Also

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

Parent topic:

TestStand API Reference

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-abortall.html language=enus -->
## TOPIC 00711: Engine.AbortAll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-abortall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-abortall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.AbortAll Purpose Aborts all existing executions. See Also Engine.BreakAll Engine.TerminateAll Execution.Abort

### Engine.AbortAll

#### Syntax

[Engine](engine.html).AbortAll

#### Purpose

Aborts all existing executions.

#### See Also

[Engine.BreakAll](engine-breakall.html)

[Engine.TerminateAll](engine-terminateall.html)

[Execution.Abort](execution-abort.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-acquirelicense.html language=enus -->
## TOPIC 00712: Engine.AcquireLicense

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-acquirelicense.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-acquirelicense.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.AcquireLicense( license, options) Return Value Long A handle to the acquired license . Purpose Instructs TestStand to acquire a type of license for the application. When the license is no longer required, call the Engine.ReleaseLicense method using the handle this method returns. An ap

### Engine.AcquireLicense

#### Syntax

[Engine](engine.html).AcquireLicense( license, options)

#### Return Value

[Long](data-types-for-teststand.html)

A handle to the acquired
 
 [license](/csh?context=ts_9050)
 .

#### Purpose

Instructs TestStand to acquire a type of license for the application. When the license is no longer required, call the
 [Engine.ReleaseLicense](engine-releaselicense.html)
 method using the handle this method returns. An application requires a type of license until you release all license handles for the license type.

#### Remarks

If TestStand cannot acquire the license and you do not pass
 [AcquireLicenseOption_SuppressStartupDialog](acquirelicenseoptions.html)
 to the
 options
 parameter, TestStand launches a dialog box that prompts you to evaluate, activate, or purchase TestStand. This method returns an error if TestStand cannot acquire the required license.

The Application Manager control automatically calls this method when you call the
 
 [ApplicationMgr.Start](../tsuiref/applicationmgr-start.html)
 method. When using an Application Manager control to start the engine, set the
 
 [ApplicationMgr.IsEditor](../tsuiref/applicationmgr-iseditor.html)
 property before calling
 ApplicationMgr.Start
 .

#### Parameters

license
 As
 [ApplicationLicenses](applicationlicenses.html)

[In] Specifies the type of license to acquire.

options
 As
 [Long](data-types-for-teststand.html)

[In] Specifies one or more
 [AcquireLicenseOptions](acquirelicenseoptions.html)
 options.

#### See Also

[Activating Your Software with the NI License Manager](../tshelp/activating-your-software.html)

[AcquireLicenseOptions](acquirelicenseoptions.html)

[ApplicationLicenses](applicationlicenses.html)

[ApplicationMgr.IsEditor](../tsuiref/applicationmgr-iseditor.html)

[ApplicationMgr.Start](../tsuiref/applicationmgr-start.html)

[Engine.ReleaseLicense](engine-releaselicense.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-addimage.html language=enus -->
## TOPIC 00713: Engine.AddImage

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-addimage.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-addimage.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.AddImage( image, imageName) Return Value Long The index of the added image. Purpose Adds an image to the list of images the engine maintains. Remarks The engine maintains lists of images for all the icons from the <TestStand> \Components\Icons and <TestStand Public>\Components\Icons di

### Engine.AddImage

#### Syntax

[Engine](engine.html).AddImage( image, imageName)

#### Return Value

[Long](data-types-for-teststand.html)

The index of the added image.

#### Purpose

Adds an image to the list of images the engine maintains.

#### Remarks

The engine maintains lists of images for all the icons from the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Icons
 and
 <TestStand Public>\Components\Icons
 directories and images you add using this method. This method adds an image to the engine image lists and the
 [Images](images.html)
 collection.

#### Parameters

image
 As
 [Picture](data-types-for-teststand.html)

[In] Must specify an icon image.

imageName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name to associate with the image. The name must be unique among all images.

#### See Also

[Engine.GetImageIndex](engine-getimageindex.html)

[Engine.GetImageName](engine-getimagename.html)

[Engine.LargeImageListEx](engine-largeimagelistex.html)

[Engine.SmallImageListEx](engine-smallimagelistex.html)

[Images](images.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-alwaysgotocleanuponfailure.html language=enus -->
## TOPIC 00714: Engine.AlwaysGotoCleanupOnFailure

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-alwaysgotocleanuponfailure.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-alwaysgotocleanuponfailure.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.AlwaysGotoCleanupOnFailure Data Type Boolean Purpose This property is obsolete. Use the StationOptions.AlwaysGotoCleanupOnFailure property instead. Remarks Overrides the Sequence.GotoCleanupOnFailure property setting when this property is True . See Also Sequence.GotoCleanupOnFailure S

### Engine.AlwaysGotoCleanupOnFailure

#### Syntax

[Engine](engine.html).AlwaysGotoCleanupOnFailure

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.AlwaysGotoCleanupOnFailure

#### Remarks

Overrides the
 [Sequence.GotoCleanupOnFailure](sequence-gotocleanuponfailure.html)
 property setting when this property is
 True
 .

#### See Also

[Sequence.GotoCleanupOnFailure](sequence-gotocleanuponfailure.html)

[StationOptions.AlwaysGotoCleanupOnFailure](stationoptions-alwaysgotocleanuponfailure.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-applicationiseditor.html language=enus -->
## TOPIC 00715: Engine.ApplicationIsEditor

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-applicationiseditor.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-applicationiseditor.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ApplicationIsEditor Data Type Boolean Purpose Specifies whether the application is a sequence editor. Remarks The default setting is False . Set this property to True if you are using the TestStand API to write a sequence editor. If you are writing a user interface, use the default set

### Engine.ApplicationIsEditor

#### Syntax

[Engine](engine.html).ApplicationIsEditor

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Specifies whether the application is a sequence editor.

#### Remarks

The default setting is
 False
 . Set this property to
 True
 if you are using the TestStand API to write a sequence editor. If you are writing a user interface, use the default setting.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-applicationlicense.html language=enus -->
## TOPIC 00716: Engine.ApplicationLicense

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-applicationlicense.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-applicationlicense.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ApplicationLicense Data Type ApplicationLicenses Use the following constants with this data type: ApplicationLicense_CustomEditor –(Value: 200) Specifies that the application requires a license to perform custom editor operations, such as editing and saving sequence files. ApplicationL

### Engine.ApplicationLicense

#### Syntax

[Engine](engine.html).ApplicationLicense

#### Data Type

[ApplicationLicenses](applicationlicenses.html)

Use the following constants with this data type:

- ApplicationLicense_CustomEditor 
 –(Value: 200) Specifies that the application requires a license to perform custom editor operations, such as editing and saving sequence files.
- ApplicationLicense_OperatorInterface 
 –(Value: 100) Specifies that the application requires a license to perform non-editing operations.
- ApplicationLicense_SequenceEditor 
 –(Value: 300) Specifies that the application requires a license to use the TestStand Sequence Editor.
- ApplicationLicense_Unspecified 
 –(Value: 0) Specifies that the application license requirements are unspecified.

#### Purpose

Returns the type of
 
 [license](/csh?context=ts_9050)
 the application is using. Use the
 [Engine.AcquireLicense](engine-acquirelicense.html)
 method to instruct TestStand to acquire a type of license for the application, and use the
 [Engine.ReleaseLicense](engine-releaselicense.html)
 method to inform TestStand when an acquired license is no longer needed.

#### See Also

[Engine.AcquireLicense](engine-acquirelicense.html)

[Engine.ReleaseLicense](engine-releaselicense.html)

[TestStand Licensing Options](/csh?context=ts_9050)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-applicationversionstring.html language=enus -->
## TOPIC 00717: Engine.ApplicationVersionString

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-applicationversionstring.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-applicationversionstring.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ApplicationVersionString Data Type String Purpose Returns the major and minor version of the TestStand product as a string.

### Engine.ApplicationVersionString

#### Syntax

[Engine](engine.html).ApplicationVersionString

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the major and minor version of the TestStand product as a string.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-appmainhwnd.html language=enus -->
## TOPIC 00718: Engine.AppMainHwnd

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-appmainhwnd.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-appmainhwnd.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.AppMainHwnd Data Type Long Purpose Specifies the Window handle of the owner of modal dialog boxes. Remarks TestStand uses this property to make dialog boxes modal to the application. Do not set this property because TestStand sets it automatically when the application creates the TestS

### Engine.AppMainHwnd

#### Syntax

[Engine](engine.html).AppMainHwnd

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the Window handle of the owner of modal dialog boxes.

#### Remarks

TestStand uses this property to make dialog boxes modal to the application. Do not set this property because TestStand sets it automatically when the application creates the TestStand Engine. Setting this property can cause dialog boxes to be modal to the wrong window. This property usually refers to the main window of the application but refers to the window of the dialog box when the application displays a modal dialog box.

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-autologinsystemuser.html language=enus -->
## TOPIC 00719: Engine.AutoLoginSystemUser

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-autologinsystemuser.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-autologinsystemuser.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.AutoLoginSystemUser Data Type Boolean Purpose This property is obsolete. Use the StationOptions.AutoLoginSystemUser property instead. Remarks Specifies if the LoginLogout callback sequence uses the current user login for the operating system as the login for TestStand when first launch

### Engine.AutoLoginSystemUser

#### Syntax

[Engine](engine.html).AutoLoginSystemUser

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.AutoLoginSystemUser

#### Remarks

Specifies if the LoginLogout callback sequence uses the current user login for the operating system as the login for TestStand when first launching a user interface or sequence editor.

If the user login for the operating system does not exist in TestStand, the Login dialog box launches. If the user login for the operating system exists in TestStand, TestStand automatically logs the user in using the operating system login.

Note

#### See Also

[Engine.CallFrontEndCallbackEx](engine-callfrontendcallbackex.html)

[StationOptions.AutoLoginSystemUser](stationoptions-autologinsystemuser.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-beginprofiling.html language=enus -->
## TOPIC 00720: Engine.BeginProfiling

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-beginprofiling.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-beginprofiling.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.BeginProfiling Purpose Enables profiling. Profiling remains enabled until every call to BeginProfiling is balanced by a call to Engine.EndProfiling.

### Engine.BeginProfiling

#### Syntax

[Engine](engine.html).BeginProfiling

#### Purpose

Enables profiling. Profiling remains enabled until every call to BeginProfiling is balanced by a call to Engine.EndProfiling.

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-bindirectory.html language=enus -->
## TOPIC 00721: Engine.BinDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-bindirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-bindirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.BinDirectory Data Type String Purpose This property is obsolete. Use the Engine.GetTestStandPath method instead. Remarks Returns the pathname of the <TestStand> \Bin directory. The pathname does not contain a trailing backslash. See Also Engine.ConfigDirectory Engine.GetTestStandPath E

### Engine.BinDirectory

#### Syntax

[Engine](engine.html).BinDirectory

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Engine.GetTestStandPath

#### Remarks

Returns the pathname of the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Bin
 directory. The pathname does not contain a trailing backslash.

#### See Also

[Engine.ConfigDirectory](engine-configdirectory.html)

[Engine.GetTestStandPath](engine-getteststandpath.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

[Engine.TestStandDirectory](engine-teststanddirectory.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-breakall.html language=enus -->
## TOPIC 00722: Engine.BreakAll

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-breakall.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-breakall.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.BreakAll Purpose Suspends all existing executions. See Also Engine.AbortAll Engine.TerminateAll Execution.Break Execution.Resume

### Engine.BreakAll

#### Syntax

[Engine](engine.html).BreakAll

#### Purpose

Suspends all existing executions.

#### See Also

[Engine.AbortAll](engine-abortall.html)

[Engine.TerminateAll](engine-terminateall.html)

[Execution.Break](execution-break.html)

[Execution.Resume](execution-resume.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-breakonrte.html language=enus -->
## TOPIC 00723: Engine.BreakOnRTE

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-breakonrte.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-breakonrte.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.BreakOnRTE Data Type Boolean Purpose This property is obsolete. Use the StationOptions.RTEOption property instead. Remarks Specifies whether the sequence editor or user interface breaks on run-time errors. In most sequence editors and user interfaces, breaking on a run-time error launc

### Engine.BreakOnRTE

#### Syntax

[Engine](engine.html).BreakOnRTE

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.RTEOption

#### Remarks

Specifies whether the sequence editor or user interface breaks on run-time errors. In most sequence editors and user interfaces, breaking on a run-time error launches a dialog box in which you can choose how to proceed.

#### See Also

[StationOptions.RTEOption](stationoptions-rteoption.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-breakpointsenabled.html language=enus -->
## TOPIC 00724: Engine.BreakpointsEnabled

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-breakpointsenabled.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-breakpointsenabled.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.BreakpointsEnabled Data Type Boolean Purpose This property is obsolete. Use the StationOptions.BreakpointsEnabled property instead. Remarks Specifies whether to stop on breakpoints. Set this property to True to stop on breakpoints. Set this property to False to ignore breakpoints. See

### Engine.BreakpointsEnabled

#### Syntax

[Engine](engine.html).BreakpointsEnabled

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.BreakpointsEnabled

#### Remarks

Specifies whether to stop on breakpoints. Set this property to
 True
 to stop on breakpoints. Set this property to
 False
 to ignore breakpoints.

#### See Also

[StationOptions.BreakpointsEnabled](stationoptions-breakpointsenabled.html)

[StationOptions.TracingEnabled](stationoptions-tracingenabled.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-buildversion.html language=enus -->
## TOPIC 00725: Engine.BuildVersion

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-buildversion.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-buildversion.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.BuildVersion Data Type Long Purpose Returns the build version number for the current version of TestStand. Remarks The full version number format is MajorVersion.MinorVersion.RevisionVersion.BuildVersion . See Also Engine.MajorVersion Engine.MinorVersion Engine.PatchVersion Engine.Revi

### Engine.BuildVersion

#### Syntax

[Engine](engine.html).BuildVersion

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Returns the build version number for the current version of TestStand.

#### Remarks

The full version number format is
 MajorVersion.MinorVersion.RevisionVersion.BuildVersion
 .

#### See Also

[Engine.MajorVersion](engine-majorversion.html)

[Engine.MinorVersion](engine-minorversion.html)

[Engine.PatchVersion](engine-patchversion.html)

[Engine.RevisionVersion](engine-revisionversion.html)

[Engine.VersionString](engine-versionstring.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-builtindatatypes.html language=enus -->
## TOPIC 00726: Engine.BuiltinDataTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-builtindatatypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-builtindatatypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.BuiltinDataTypes Data Type PropertyObject Purpose This property is obsolete. Use the Engine.GetTypeNames and Engine.GetTypeDefinition methods instead. Remarks If you attempt to read this property, TestStand returns an error. See Also Engine.GetTypeDefinition Engine.GetTypeNames Propert

### Engine.BuiltinDataTypes

#### Syntax

[Engine](engine.html).BuiltinDataTypes

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Note

Engine.GetTypeNames

Engine.GetTypeDefinition

#### Remarks

If you attempt to read this property, TestStand returns an error.

#### See Also

[Engine.GetTypeDefinition](engine-gettypedefinition.html)

[Engine.GetTypeNames](engine-gettypenames.html)

[PropertyObject](propertyobject.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-callfrontendcallback.html language=enus -->
## TOPIC 00727: Engine.CallFrontEndCallback

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-callfrontendcallback.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-callfrontendcallback.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CallFrontEndCallback( sequenceNameParam, argumentList) Return Value Execution The Execution object of the newly created execution. Purpose This method is obsolete. Use the Engine.CallFrontEndCallbackEx method instead. Remarks Calls the Front-End callback sequence specified by sequenceN

### Engine.CallFrontEndCallback

#### Syntax

[Engine](engine.html).CallFrontEndCallback( sequenceNameParam, argumentList)

#### Return Value

[Execution](execution.html)

The Execution object of the newly created execution.

#### Purpose

Note

Engine.CallFrontEndCallbackEx

#### Remarks

Calls the Front-End callback sequence specified by sequenceName.

#### Parameters

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the Front-End callback sequence to call.

argumentList
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a PropertyObject object that contains the parameters to pass to the sequence. Each subproperty of the PropertyObject object represents a parameter to the sequence. The subproperties must appear in the same order as the sequence parameters.

#### See Also

[Engine.CallFrontEndCallbackEx](engine-callfrontendcallbackex.html)

[FrontEndCallbacks](frontendcallbacks.html)

[PropertyObject](propertyobject.html)

[TypeConflictHandlerTypes](typeconflicthandlertypes.html)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-callfrontendcallbackex.html language=enus -->
## TOPIC 00728: Engine.CallFrontEndCallbackEx

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-callfrontendcallbackex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-callfrontendcallbackex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CallFrontEndCallbackEx( sequenceNameParam, argumentList, handlerType = ConflictHandler_Error, reservedParam = 0) Return Value Execution The Execution object of the newly created execution. Purpose Calls the Front-End callback sequence the sequenceNameParam parameter specifies. Remarks

### Engine.CallFrontEndCallbackEx

#### Syntax

[Engine](engine.html).CallFrontEndCallbackEx( sequenceNameParam, argumentList, handlerType = ConflictHandler_Error, reservedParam = 0)

#### Return Value

[Execution](execution.html)

The Execution object of the newly created execution.

#### Purpose

Calls the Front-End callback sequence the
 sequenceNameParam
 parameter specifies.

#### Remarks

Front-End callbacks, which are callbacks the TestStand Sequence Editor or a TestStand User Interface call, allow you to customize the sequence editors and user interfaces on the system. Each sequence editor or user interface chooses which Front-End callbacks it calls. The
 FrontEndCallbacks.seq
 file in the
 [<TestStand>](/csh?context=ts_tsfundamentals_directories)
 \Components\Callbacks\FrontEnd
 directory contains the Front-End callbacks National Instruments defines. Currently, National Instruments defines only the LoginLogout Front-End callback. You can override the National Instruments version of LoginLogout or add custom Front-End callbacks in the
 FrontEndCallbacks.seq
 file, which is located in the
 <TestStand Public>\Components\Callbacks\FrontEnd
 directory.

#### Parameters

sequenceNameParam
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the
 [Front-End callback](frontendcallbacks.html)
 sequence to call.

argumentList
 As
 [PropertyObject](propertyobject.html)

[In] Specifies a PropertyObject that contains the parameters to pass to the sequence. Each subproperty of the PropertyObject represents a parameter to the sequence. The subproperties must appear in the same order as the sequence parameters.

handlerType
 As
 [TypeConflictHandlerTypes](typeconflicthandlertypes.html)

[In] Specifies how to handle
 [type conflicts](/csh?context=ts_tsfundamentals_types_revision)
 .

This parameter has a default value of
 ConflictHandler_Error
 .

reservedParam
 As
 [Long](data-types-for-teststand.html)

[In]

Note

This parameter has a default value of
 0
 .

#### See Also

[CallbackTypes](callbacktypes.html)

[DefaultModelCallbacks](defaultmodelcallbacks.html)

[Execution](execution.html)

[FrontEndCallbacks](frontendcallbacks.html)

[PropertyObject](propertyobject.html)

[SeqFileCallbacks](seqfilecallbacks.html)

[TypeConflictHandlerTypes](typeconflicthandlertypes.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-cancreatestep.html language=enus -->
## TOPIC 00729: Engine.CanCreateStep

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-cancreatestep.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-cancreatestep.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CanCreateStep( adapterKeyNameVal, stepTypeName) Return Value Boolean Purpose Determines whether you can create a new step of the specified type. Remarks The Engine.NewStep method reports an error if this method returns False . Parameters adapterKeyNameVal As String [In] Specifies the k

### Engine.CanCreateStep

#### Syntax

[Engine](engine.html).CanCreateStep( adapterKeyNameVal, stepTypeName)

#### Return Value

[Boolean](data-types-for-teststand.html)

#### Purpose

Determines whether you can create a new step of the specified type.

#### Remarks

The
 [Engine.NewStep](engine-newstep.html)
 method reports an error if this method returns
 False
 .

#### Parameters

adapterKeyNameVal
 As
 [String](data-types-for-teststand.html)

[In] Specifies the key name of the module Adapter object to use to create the step. Pass an empty string to use the adapter the step type designates or to use the adapter the
 [Engine.DefaultAdapter](engine-defaultadapter.html)
 property specifies if the step has no designated adapter.

stepTypeName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the step type with which to create the step. The step type must already be in memory. Refer to
 [Engine.GetTypeNames](engine-gettypenames.html)
 for a list of names for the built-in step types and other types.

#### See Also

[AdapterKeyNames](adapterkeynames.html)

[Engine.DefaultAdapter](engine-defaultadapter.html)

[Engine.GetTypeNames](engine-gettypenames.html)

[Engine.NewStep](engine-newstep.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-checkexpression.html language=enus -->
## TOPIC 00730: Engine.CheckExpression

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-checkexpression.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-checkexpression.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CheckExpression( evaluationContext, expressionStr, evaluationOptions, errorDescription, startErrPos, endErrPos) Return Value Boolean Returns True if the expression is correct. Returns False if the expression contains an error. If it returns False , check the errorDescription , startErr

### Engine.CheckExpression

#### Syntax

[Engine](engine.html).CheckExpression( evaluationContext, expressionStr, evaluationOptions, errorDescription, startErrPos, endErrPos)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the expression is correct. Returns
 False
 if the expression contains an error. If it returns
 False
 , check the
 errorDescription
 ,
 startErrPos
 , and
 endErrPos
 parameters for more information.

#### Purpose

Checks the validity of the expression parameter and returns error information.

#### Remarks

This method is similar to the
 [Engine.CheckExprSyntax](engine-checkexprsyntax.html)
 method, except it checks the validity of variables in the expression.

#### Parameters

evaluationContext
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the context in which to evaluate the expression. This method uses this object to determine whether variables in the expression are valid. If you pass a
 NULL
 reference, this method checks only the expression syntax.

expressionStr
 As
 [String](data-types-for-teststand.html)

[In] Specifies the expression to check.

evaluationOptions
 As
 [Long](data-types-for-teststand.html)

[In] Pass
 0
 to specify the default behavior, or pass one or more
 [EvaluationOptions](evaluationoptions.html)
 constants. Use the bitwise-OR operator to specify multiple options.

errorDescription
 As
 [String](data-types-for-teststand.html)

[Out] When an error exists, this parameter returns an error message describing the type of error.

startErrPos
 As
 [Long](data-types-for-teststand.html)

[Out] When an error exists, this parameter returns the index of the location in the string where the error begins.

endErrPos
 As
 [Long](data-types-for-teststand.html)

[Out] When an error exists, this parameter returns the index of the location in the string of the first character beyond the error.

#### See Also

[Engine.CheckExprSyntax](engine-checkexprsyntax.html)

[EvaluationOptions](evaluationoptions.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

[PropertyObject](propertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-checkexprsyntax.html language=enus -->
## TOPIC 00731: Engine.CheckExprSyntax

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-checkexprsyntax.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-checkexprsyntax.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CheckExprSyntax( expressionStr, errorDescription, startErrPos, endErrPos) Return Value Boolean Returns True if the syntax is correct. Returns False if the expression contains a syntax error. If this method returns False , check the errorDescription , startErrPos , and endErrPos paramet

### Engine.CheckExprSyntax

#### Syntax

[Engine](engine.html).CheckExprSyntax( expressionStr, errorDescription, startErrPos, endErrPos)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the syntax is correct. Returns
 False
 if the expression contains a syntax error. If this method returns
 False
 , check the
 errorDescription
 ,
 startErrPos
 , and
 endErrPos
 parameters for more information.

#### Purpose

Checks the syntax of the expression parameter and returns error information.

#### Remarks

Calling this method is equivalent to calling the
 [Engine.CheckExpression](engine-checkexpression.html)
 method and passing a
 NULL
 reference to the
 evaluationContext
 parameter and passing
 EvalOption_NoOptions
 to the
 evaluationOptions
 parameter.

#### Parameters

expressionStr
 As
 [String](data-types-for-teststand.html)

[In] Specifies the expression for which to check the syntax.

errorDescription
 As
 [String](data-types-for-teststand.html)

[Out] When a syntax error exists, this parameter returns an error message describing the type of error.

startErrPos
 As
 [Long](data-types-for-teststand.html)

[Out] When a syntax error exists, this parameter returns the index of the location in the string where the error begins.

endErrPos
 As
 [Long](data-types-for-teststand.html)

[Out] When a syntax error exists, this parameter returns the index of the location in the string of the first character beyond the syntax error.

#### See Also

[Engine.CheckExpression](engine-checkexpression.html)

[EvaluationOptions](evaluationoptions.html)

[Expression.ValidateEvaluationType](expression-validateevaluationtype.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-checkoutfileswhenedited.html language=enus -->
## TOPIC 00732: Engine.CheckOutFilesWhenEdited

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-checkoutfileswhenedited.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-checkoutfileswhenedited.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CheckOutFilesWhenEdited Data Type Boolean Purpose This property is obsolete. Use the StationOptions.CheckOutFilesWhenEdited property instead. Remarks Specifies if the sequence editor checks a file out from source code control when you attempt to modify the file in the sequence editor.

### Engine.CheckOutFilesWhenEdited

#### Syntax

[Engine](engine.html).CheckOutFilesWhenEdited

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.CheckOutFilesWhenEdited

#### Remarks

Specifies if the sequence editor checks a file out from source code control when you attempt to modify the file in the sequence editor.

The default value is
 True
 . When this property is
 True
 while a current workspace is specified, attempts to edit a file that is checked in the sequence editor launch a prompt to check the file out from source code control. If this property is
 False
 , the sequence editor edits the file without checking the file out.

#### See Also

[Engine.CurrentWorkspaceFile](engine-currentworkspacefile.html)

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.CheckOutOnlySelectedFiles](stationoptions-checkoutonlyselectedfiles.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-checkoutonlyselectedfiles.html language=enus -->
## TOPIC 00733: Engine.CheckOutOnlySelectedFiles

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-checkoutonlyselectedfiles.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-checkoutonlyselectedfiles.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CheckOutOnlySelectedFiles Data Type Boolean Purpose This property is obsolete. Use the StationOptions.CheckOutOnlySelectedFiles property instead. Remarks A workspace file contains a list of project files, each project file contains a lists of sequence files, and a sequence file can con

### Engine.CheckOutOnlySelectedFiles

#### Syntax

[Engine](engine.html).CheckOutOnlySelectedFiles

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

StationOptions.CheckOutOnlySelectedFiles

#### Remarks

A workspace file contains a list of project files, each project file contains a lists of sequence files, and a sequence file can contain lists of code modules and other files. When you set this option to
 True
 , the sequence editor displays only the selected file, such as a project file, in the
 [Source Code Control Operations](../tsref/source-code-control-operations-dialog-box.html)
 dialog box. When this option is
 False
 , the sequence editor displays the selected item and all the items it contains in the Source Code Control Operations dialog box.

#### See Also

[Source Code Control Operations dialog box](../tsref/source-code-control-operations-dialog-box.html)

[StationOptions.CheckOutFilesWhenEdited](stationoptions-checkoutfileswhenedited.html)

[StationOptions.CheckOutOnlySelectedFiles](stationoptions-checkoutonlyselectedfiles.html)

[StationOptions.PromptWhenAddingFilesToSC](stationoptions-promptwhenaddingfilestosc.html)

[StationOptions.UseDialogForCheckOut](stationoptions-usedialogforcheckout.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-clearfilepasswordcache.html language=enus -->
## TOPIC 00734: Engine.ClearFilePasswordCache

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-clearfilepasswordcache.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-clearfilepasswordcache.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ClearFilePasswordCache Purpose Use this method to remove all the passwords the Remember Password option in the Unlock File dialog box and the Unlock Type Definitions dialog box specifies to store in the file password cache. See Also Unlock File dialog box Unlock Type Definitions dialog

### Engine.ClearFilePasswordCache

#### Syntax

[Engine](engine.html).ClearFilePasswordCache

#### Purpose

Use this method to remove all the passwords the Remember Password option in the
 [Unlock File](../tsref/lock-unlock-file-dialog-box.html)
 dialog box and the
 [Unlock Type Definitions](../tsref/unlock-type-definitions-dialog-box.html)
 dialog box specifies to store in the file password cache.

#### See Also

[Unlock File dialog box](../tsref/lock-unlock-file-dialog-box.html)

[Unlock Type Definitions dialog box](../tsref/unlock-type-definitions-dialog-box.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-commitglobalstodisk.html language=enus -->
## TOPIC 00735: Engine.CommitGlobalsToDisk

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-commitglobalstodisk.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-commitglobalstodisk.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CommitGlobalsToDisk( promptOnSaveConflicts = True) Purpose Saves the current state of the station globals to disk. Remarks Calling this method with an argument of True is equivalent to calling the PropertyObjectFile.WriteFile method on the object the Engine.GlobalsFile property returns

### Engine.CommitGlobalsToDisk

#### Syntax

[Engine](engine.html).CommitGlobalsToDisk( promptOnSaveConflicts = True)

#### Purpose

Saves the current state of the station globals to disk.

#### Remarks

Calling this method with an argument of
 True
 is equivalent to calling the
 [PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)
 method on the object the
 [Engine.GlobalsFile](engine-globalsfile.html)
 property returns.

#### Parameters

promptOnSaveConflicts
 As
 [Boolean](data-types-for-teststand.html)

[In] TestStand writes the station globals to disk only if they change after TestStand has loaded or saved them. If another application changes the station globals on disk after TestStand has loaded or saved them, the action TestStand takes depends on the value you pass in this parameter. If you pass
 True
 , TestStand gives users the option to overwrite the changes the other application made. If you pass
 False
 , TestStand saves the station globals without prompting the user to resolve any conflicts between the changes in memory and the changes on disk.

This parameter has a default value of
 True
 .

#### See Also

[Engine.Globals](engine-globals.html)

[Engine.GlobalsFile](engine-globalsfile.html)

[PropertyObjectFile.WriteFile](propertyobjectfile-writefile.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-computername.html language=enus -->
## TOPIC 00736: Engine.ComputerName

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-computername.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-computername.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ComputerName Data Type String Purpose Returns the name of the computer on which the TestStand Engine was created. See Also Engine.UniqueEngineId

### Engine.ComputerName

#### Syntax

[Engine](engine.html).ComputerName

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Returns the name of the computer on which the TestStand Engine was created.

#### See Also

[Engine.UniqueEngineId](engine-uniqueengineid.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-configdirectory.html language=enus -->
## TOPIC 00737: Engine.ConfigDirectory

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-configdirectory.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-configdirectory.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ConfigDirectory Data Type String Purpose This property is obsolete. Use the Engine.GetTestStandPath method instead. Remarks Returns the pathname of the TestStand configuration directory. The pathname does not contain a trailing backslash. The configuration directory contains engine and

### Engine.ConfigDirectory

#### Syntax

[Engine](engine.html).ConfigDirectory

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

Engine.GetTestStandPath

#### Remarks

Returns the pathname of the TestStand configuration directory. The pathname does not contain a trailing backslash.

The configuration directory contains engine and sequence editor option files, the users file, the globals file, and the tools menu file.

#### See Also

[Engine.BinDirectory](engine-bindirectory.html)

[Engine.GetTestStandPath](engine-getteststandpath.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

[Engine.SetConfigDirectory](engine-setconfigdirectory.html)

[Engine.TestStandDirectory](engine-teststanddirectory.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-configfile.html language=enus -->
## TOPIC 00738: Engine.ConfigFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-configfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-configfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ConfigFile Data Type PropertyObjectFile Purpose This property is obsolete. Use the Engine.GetEngineConfigFile property instead. Remarks You can set the station options using the Station Options dialog box and the Search Directories dialog box. See Also Engine.GlobalsFile Engine.SearchD

### Engine.ConfigFile

#### Syntax

[Engine](engine.html).ConfigFile

#### Data Type

[PropertyObjectFile](propertyobjectfile.html)

#### Purpose

Note

Engine.GetEngineConfigFile

#### Remarks

You can set the station options using the
 [Station Options](../tsref/station-options-dialog-box.html)
 dialog box and the
 [Search Directories](../tsref/edit-search-directories-dialog-box.html)
 dialog box.

#### See Also

[Engine.GlobalsFile](engine-globalsfile.html)

[Engine.SearchDirectories](engine-searchdirectories.html)

[Engine.UsersFile](engine-usersfile.html)

[PropertyObjectFile](propertyobjectfile.html)

[Search Directories dialog box](../tsref/edit-search-directories-dialog-box.html)

[StationOptions](stationoptions.html)

[Station Options dialog box](../tsref/station-options-dialog-box.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-constructtoolmenus.html language=enus -->
## TOPIC 00739: Engine.ConstructToolMenus

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-constructtoolmenus.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-constructtoolmenus.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.ConstructToolMenus( [editArgsParam]) Return Value Long The number of Tools menus that exist. This number includes the Tools menu and submenus. Purpose This method is obsolete. Use the Engine.GetEditTimeToolMenuItems and Engine.GetRunTimeToolMenuItems methods instead. Remarks Creates th

### Engine.ConstructToolMenus

#### Syntax

[Engine](engine.html).ConstructToolMenus( [editArgsParam])

#### Return Value

[Long](data-types-for-teststand.html)

The number of Tools menus that exist. This number includes the Tools menu and submenus.

#### Purpose

Note

Engine.GetEditTimeToolMenuItems

Engine.GetRunTimeToolMenuItems

#### Remarks

Creates the internal data for the Tools menu that is visible in user interfaces and sequence editors.

Call this function to initialize the Tools menu and submenus for the first time or whenever the
 [Engine.DisplayToolMenuDialog](engine-displaytoolmenudialog.html)
 method modifies the Tools menu or submenus. This method also evaluates the hidden expressions to determine which items to include in the Tools menu. The number of Tools menu items and submenus remains fixed until the next time you call this function.

#### Parameters

editArgsParam
 As
 [Variant](data-types-for-teststand.html)

[In] [
 [Optional](/csh?context=ts_tsapiref_optional_parameters)
 ] Specifies which items in the user interface are currently selected. The method uses this information to calculate the item text, hidden, and enabled states of each menu item by evaluating its item text, hidden, and enabled expressions.

#### See Also

[EditArgs](editargs.html)

[Engine.DisplayToolMenuDialog](engine-displaytoolmenudialog.html)

[Engine.GetEditTimeToolMenuItems](engine-getedittimetoolmenuitems.html)

[Engine.GetRunTimeToolMenuItems](engine-getruntimetoolmenuitems.html)

[Omitting Optional Parameters](/csh?context=ts_tsapiref_optional_parameters)

Parent topic:

Obsolete Engine Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-copypropertyobject.html language=enus -->
## TOPIC 00740: Engine.CopyPropertyObject

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-copypropertyobject.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-copypropertyobject.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CopyPropertyObject( srcObj) Return Value PropertyObject New copy of the PropertyObject object created in the process space of the engine on which the method is called. Purpose Use this function to copy a PropertyObject object you receive from a remote execution to the local computer. R

### Engine.CopyPropertyObject

#### Syntax

[Engine](engine.html).CopyPropertyObject( srcObj)

#### Return Value

[PropertyObject](propertyobject.html)

New copy of the PropertyObject object created in the process space of the engine on which the method is called.

#### Purpose

Use this function to copy a PropertyObject object you receive from a remote execution to the local computer.

#### Remarks

Some API functions, such as the
 [PropertyObject.SetPropertyObject](propertyobject-setpropertyobject.html)
 method, work only with objects created on the local computer.

#### Parameters

srcObj
 As
 [PropertyObject](propertyobject.html)

[In] Specifies the property object from an external instance of the TestStand Engine (that is, another process or computer) you want to copy.

#### See Also

[PropertyObject](propertyobject.html)

[PropertyObject.Clone](propertyobject-clone.html)

[PropertyObject.SetPropertyObject](propertyobject-setpropertyobject.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-createnewuniquestepids.html language=enus -->
## TOPIC 00741: Engine.CreateNewUniqueStepIds

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-createnewuniquestepids.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-createnewuniquestepids.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CreateNewUniqueStepIds( steps) Purpose Creates new unique step IDs for a set of steps. Remarks Call this method after cloning or copying a group of steps to ensure that the steps in the copy contain unique IDs. This method also modifies certain steps, such as Goto steps, that refer to

### Engine.CreateNewUniqueStepIds

#### Syntax

[Engine](engine.html).CreateNewUniqueStepIds( steps)

#### Purpose

Creates new unique step IDs for a set of steps.

#### Remarks

Call this method after cloning or copying a group of steps to ensure that the steps in the copy contain unique IDs. This method also modifies certain steps, such as Goto steps, that refer to unique IDs so they refer to the newly generated IDs.

#### Parameters

steps
 As
 [Object Array](data-types-for-teststand.html)

[In] Specifies an array of steps for which new unique step IDs are created.

#### See Also

[Sequence.CreateNewUniqueStepIds](sequence-createnewuniquestepids.html)

[Step.CreateNewUniqueStepId](step-createnewuniquestepid.html)

[Step.UniqueStepId](step-uniquestepid.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-createtempfile.html language=enus -->
## TOPIC 00742: Engine.CreateTempFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-createtempfile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-createtempfile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CreateTempFile( baseName, extension, directory) Return Value String The pathname of the temporary file. Purpose Creates a unique temporary file with a specific basename and extension. Remarks When TestStand shuts down, it automatically deletes the temporary file. Parameters baseName As

### Engine.CreateTempFile

#### Syntax

[Engine](engine.html).CreateTempFile( baseName, extension, directory)

#### Return Value

[String](data-types-for-teststand.html)

The pathname of the temporary file.

#### Purpose

Creates a unique temporary file with a specific basename and extension.

#### Remarks

When TestStand shuts down, it automatically deletes the temporary file.

#### Parameters

baseName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the base name of the temporary file. If necessary, TestStand adds other characters to the name to make it unique.

extension
 As
 [String](data-types-for-teststand.html)

[In] Specifies the file extension for the temporary file.

directory
 As
 [String](data-types-for-teststand.html)

[In] Specifies the directory in which to store the temporary file. You can include a trailing backslash, but it is not required. Pass an empty string to use the
 TestStand
 subdirectory in the directory the TEMP environment variable specifies, which by default is
 %USERPROFILE%\AppData\Local\Temp
 on Windows 8.1/8/7/Vista and
 %USERPROFILE%\Local Settings\Temp
 on Microsoft Windows XP.

#### See Also

[Engine.TestStandDirectory](engine-teststanddirectory.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-currentuser.html language=enus -->
## TOPIC 00743: Engine.CurrentUser

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-currentuser.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-currentuser.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CurrentUser Data Type User Purpose Specifies the user who is currently logged in. Remarks Use this property to obtain or set the User object for the user who is currently logged in. If no one is currently logged in, this property returns a NULL dispatch pointer or object reference. Aft

### Engine.CurrentUser

#### Syntax

[Engine](engine.html).CurrentUser

#### Data Type

[User](user.html)

#### Purpose

Specifies the user who is currently logged in.

#### Remarks

Use this property to obtain or set the User object for the user who is currently logged in. If no one is currently logged in, this property returns a
 NULL
 dispatch pointer or object reference. After you obtain the User object, call the
 [User.HasPrivilege](user-hasprivilege.html)
 method to determine whether the user or a user group of which the user is a member has a specific privilege. If you set the property to
 0
 or
 NULL
 , you log out the current user.

If you are developing an application that uses the TestStand User Interface (UI) Controls, use the
 
 [ApplicationMgr.Login](../tsuiref/applicationmgr-login.html)
 method to change the current user to ensure that the Application Manager control properly sends an event to a user interface.

#### See Also

[ApplicationMgr.Login](../tsuiref/applicationmgr-login.html)

[Engine.CurrentUserHasPrivilege](engine-currentuserhasprivilege.html)

[User](user.html)

[User.HasPrivilege](user-hasprivilege.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-currentuserhasprivilege.html language=enus -->
## TOPIC 00744: Engine.CurrentUserHasPrivilege

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-currentuserhasprivilege.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-currentuserhasprivilege.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CurrentUserHasPrivilege( privilegeName) Return Value Boolean Returns True if the current user has the privilege. Purpose Confirms whether the current user or any user group of which the user is a member has a specific privilege. Remarks Returns True when the privilege property is True

### Engine.CurrentUserHasPrivilege

#### Syntax

[Engine](engine.html).CurrentUserHasPrivilege( privilegeName)

#### Return Value

[Boolean](data-types-for-teststand.html)

Returns
 True
 if the current user has the privilege.

#### Purpose

Confirms whether the current user or any user group of which the user is a member has a specific privilege.

#### Remarks

Returns
 True
 when the privilege property is
 True
 , when the privilege property of any group that contains the privilege is
 True
 , or when privilege checking is disabled, the
 [StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)
 property is
 False
 . If privilege checking is disabled but the
 [StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)
 property is
 True
 , this function returns
 True
 only if a user is currently logged on.

#### Parameters

privilegeName
 As
 [String](data-types-for-teststand.html)

[In] Specifies the name of the
 [privilege](userprivileges.html)
 to check. You can specify the name of any privilege property. You can specify the full privilege path in the user privileges property view, such as
 Debug.RunSelectedTests
 , or you can specify the base privilege name, such as
 RunSelectedTests
 . If you specify only the base privilege name and more than one instance of the base privilege name exists, the method returns the value of the first base privilege it finds with that name. You can pass
 "*"
 as the string argument to determine whether a user is currently logged in.

#### See Also

[StationOptions.EnableUserPrivilegeChecking](stationoptions-enableuserprivilegechecking.html)

[StationOptions.RequireUserLogin](stationoptions-requireuserlogin.html)

[User](user.html)

[User.HasPrivilege](user-hasprivilege.html)

[UserPrivileges](userprivileges.html)

Parent topic:

Methods

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-currentworkspacefile.html language=enus -->
## TOPIC 00745: Engine.CurrentWorkspaceFile

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-currentworkspacefile.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-currentworkspacefile.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CurrentWorkspaceFile Data Type WorkspaceFile Purpose Specifies the current workspace file. Remarks Use this property to establish a connection to the source code control provider specified in the workspace file. If no current workspace file exists, this property is a NULL dispatch poin

### Engine.CurrentWorkspaceFile

#### Syntax

[Engine](engine.html).CurrentWorkspaceFile

#### Data Type

[WorkspaceFile](workspacefile.html)

#### Purpose

Specifies the current workspace file.

#### Remarks

Use this property to establish a connection to the source code control provider specified in the workspace file. If no current workspace file exists, this property is a
 NULL
 dispatch pointer or object reference. To disconnect the current source code control provider, set this property to
 NULL
 .

#### See Also

[WorkspaceFile](workspacefile.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-customdatatypes.html language=enus -->
## TOPIC 00746: Engine.CustomDataTypes

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-customdatatypes.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-customdatatypes.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CustomDataTypes Data Type PropertyObject Purpose This property is obsolete. Use the Engine.GetTypeNames and Engine.GetTypeDefinition methods instead. Remarks If you attempt to read this property, TestStand returns an error. See Also Engine.GetTypeDefinition Engine.GetTypeNames Property

### Engine.CustomDataTypes

#### Syntax

[Engine](engine.html).CustomDataTypes

#### Data Type

[PropertyObject](propertyobject.html)

#### Purpose

Note

Engine.GetTypeNames

Engine.GetTypeDefinition

#### Remarks

If you attempt to read this property, TestStand returns an error.

#### See Also

[Engine.GetTypeDefinition](engine-gettypedefinition.html)

[Engine.GetTypeNames](engine-gettypenames.html)

[PropertyObject](propertyobject.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-cviadapter-executestepsincvi.html language=enus -->
## TOPIC 00747: Engine.CVIAdapter_ExecuteStepsInCVI

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-cviadapter-executestepsincvi.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-cviadapter-executestepsincvi.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CVIAdapter_ExecuteStepsInCVI Data Type Boolean Purpose This property is obsolete. Use the CVIAdapter.ExecuteStepsInExternalInstance property instead. Remarks Indicates whether the LabWindows/CVI Adapter executes steps in an external LabWindows/CVI process rather than internally. While

### Engine.CVIAdapter_ExecuteStepsInCVI

#### Syntax

[Engine](engine.html).CVIAdapter_ExecuteStepsInCVI

#### Data Type

[Boolean](data-types-for-teststand.html)

#### Purpose

Note

CVIAdapter.ExecuteStepsInExternalInstance

#### Remarks

Indicates whether the LabWindows/CVI Adapter executes steps in an external LabWindows/CVI process rather than internally.

While running steps in an external LabWindows/CVI process is slower, you can use this property to debug steps more easily. Changing this setting causes all modules to be unloaded.

#### See Also

[CVIAdapter.ExecuteStepsInExternalInstance](cviadapter-executestepsinexternalinstance.html)

[CVIAdapter.ExecutionServerProjectPathName](cviadapter-executionserverprojectpathname.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-cviadapter-externalcviprj.html language=enus -->
## TOPIC 00748: Engine.CVIAdapter_ExternalCVIPrj

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-cviadapter-externalcviprj.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-cviadapter-externalcviprj.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.CVIAdapter_ExternalCVIPrj Data Type String Purpose This property is obsolete. Use the CVIAdapter.ExecutionServerProjectPathName property instead. Remarks Changes the project in which LabWindows/CVI Adapter steps are executed when the CVIAdapter.ExecuteStepsInCVI property is True . The

### Engine.CVIAdapter_ExternalCVIPrj

#### Syntax

[Engine](engine.html).CVIAdapter_ExternalCVIPrj

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Note

CVIAdapter.ExecutionServerProjectPathName

#### Remarks

Changes the project in which LabWindows/CVI Adapter steps are executed when the
 CVIAdapter.ExecuteStepsInCVI
 property is
 True
 .

The value of this property can be a relative or absolute path. If you specify a relative path, TestStand looks in the
 [search directories](/csh?context=ts_tsfundamentals_module_adapters_search_paths)
 for the file.

Note

CVIAdapter_ExecuteStepsInCVI

CVIAdapter.ExecuteStepsInExternalInstance

#### See Also

[CVIAdapter.ExecuteStepsInExternalInstance](cviadapter-executestepsinexternalinstance.html)

[CVIAdapter.ExecutionServerProjectPathName](cviadapter-executionserverprojectpathname.html)

Parent topic:

Obsolete Engine Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-defaultadapter.html language=enus -->
## TOPIC 00749: Engine.DefaultAdapter

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-defaultadapter.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-defaultadapter.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DefaultAdapter Data Type String Purpose Specifies the key name of the default adapter TestStand uses to create steps. Remarks TestStand maintains a list of available module adapters. The adapter this property specifies is designated as the default adapter. This property contains the ke

### Engine.DefaultAdapter

#### Syntax

[Engine](engine.html).DefaultAdapter

#### Data Type

[String](data-types-for-teststand.html)

#### Purpose

Specifies the key name of the default adapter TestStand uses to create steps.

#### Remarks

TestStand maintains a list of available module adapters. The adapter this property specifies is designated as the default adapter. This property contains the
 [key name](adapterkeynames.html)
 of the default module adapter. The
 [Engine.DefaultAdapterIndex](engine-defaultadapterindex.html)
 property indicates the index of the default module adapter.

#### See Also

[Adapter](adapter.html)

[AdapterKeyNames](adapterkeynames.html)

[Engine.DefaultAdapterIndex](engine-defaultadapterindex.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.NewStep](engine-newstep.html)

[Engine.NumAdapters](engine-numadapters.html)

Parent topic:

Properties

<!--NI_TOPIC bundle=teststand-api-reference path=tsapiref/engine-defaultadapterindex.html language=enus -->
## TOPIC 00750: Engine.DefaultAdapterIndex

- bundle_id: `teststand-api-reference`
- source_path: `tsapiref/engine-defaultadapterindex.html`
- source_url: https://docs-be.ni.com/bundle/teststand-api-reference/raw/resource/enus/tsapiref/engine-defaultadapterindex.html
- document_id: `teststand-api-reference`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntax Engine.DefaultAdapterIndex Data Type Long Purpose Specifies the index of the default module adapter TestStand uses to create steps. Remarks TestStand maintains a list of available module adapters. The adapter this property specifies is designated as the default adapter. This property contains

### Engine.DefaultAdapterIndex

#### Syntax

[Engine](engine.html).DefaultAdapterIndex

#### Data Type

[Long](data-types-for-teststand.html)

#### Purpose

Specifies the index of the default module adapter TestStand uses to create steps.

#### Remarks

TestStand maintains a list of available module adapters. The adapter this property specifies is designated as the default adapter. This property contains the list index of the default module adapter. Use the
 [Engine.GetAdapter](engine-getadapter.html)
 method to obtain a module adapter object by index. The
 [Engine.DefaultAdapter](engine-defaultadapter.html)
 property indicates the key name of the default modules adapter.

#### See Also

[Engine.DefaultAdapter](engine-defaultadapter.html)

[Engine.GetAdapter](engine-getadapter.html)

[Engine.NewStep](engine-newstep.html)

[Engine.NumAdapters](engine-numadapters.html)

Parent topic:

Properties
