# NI DOCUMENT BUNDLE: veristand-net-api-reference

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-reference start=251 end=500 -->
<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep__ctor_1.htm language=enus -->
## TOPIC 00251: OpenProjectStep Constructor (OpenProjectStep)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

OpenProjectStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As OpenProjectStep _ ) |

| C# |
| --- |
| public OpenProjectStep( OpenProjectStep node ) |

| Visual C++ |
| --- |
| public: OpenProjectStep( OpenProjectStep^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.OpenProjectStepThe instance of OpenProjectStep to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenProjectStep Class

OpenProjectStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep__ctor_2.htm language=enus -->
## TOPIC 00252: OpenProjectStep Constructor (String, String, String, Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

OpenProjectStep

path

userName

password

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ path As String, _ userName As String, _ password As String, _ showProject As Boolean _ ) |

| C# |
| --- |
| public OpenProjectStep( string path, string userName, string password, bool showProject ) |

| Visual C++ |
| --- |
| public: OpenProjectStep( String^ path, String^ userName, String^ password, bool showProject ) |

###### Parameters

- **path**
  - Type: System.StringThe path to the NI VeriStand project (.nivsproj) file on disk.

- **userName**
  - Type: System.StringThe user name to use to open the project.

- **password**
  - Type: System.StringThe password for the specified userName.

- **showProject**
  - Type: System.Boolean true (True in Visual Basic) to display the project in the NI VeriStand Project Explorer window. false (False in Visual Basic) to keep it hidden.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenProjectStep Class

OpenProjectStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep_checkforerrors.htm language=enus -->
## TOPIC 00253: OpenProjectStep.CheckForErrors Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep_checkforerrors.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openprojectstep_checkforerrors.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function CheckForErrors As CompilationEvent() |

| C# |
| --- |
| public override CompilationEvent[] CheckForErrors() |

| Visual C++ |
| --- |
| public: virtual array<CompilationEvent^>^ CheckForErrors() override |

###### Return Value

CompilationEvent

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

ActionStep.CheckForErrors

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenProjectStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep__ctor.htm language=enus -->
## TOPIC 00254: OpenWorkspaceToolStep Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

OpenWorkspaceToolStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public OpenWorkspaceToolStep() |

| Visual C++ |
| --- |
| public: OpenWorkspaceToolStep() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

WorkspaceToolPath

String.Empty

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenWorkspaceToolStep Class

OpenWorkspaceToolStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep__ctor_1.htm language=enus -->
## TOPIC 00255: OpenWorkspaceToolStep Constructor (OpenWorkspaceToolStep)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

OpenWorkspaceToolStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As OpenWorkspaceToolStep _ ) |

| C# |
| --- |
| public OpenWorkspaceToolStep( OpenWorkspaceToolStep node ) |

| Visual C++ |
| --- |
| public: OpenWorkspaceToolStep( OpenWorkspaceToolStep^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.OpenWorkspaceToolStepThe instance of OpenWorkspaceToolStep to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenWorkspaceToolStep Class

OpenWorkspaceToolStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep_checkforerrors.htm language=enus -->
## TOPIC 00256: OpenWorkspaceToolStep.CheckForErrors Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep_checkforerrors.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_openworkspacetoolstep_checkforerrors.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function CheckForErrors As CompilationEvent() |

| C# |
| --- |
| public override CompilationEvent[] CheckForErrors() |

| Visual C++ |
| --- |
| public: virtual array<CompilationEvent^>^ CheckForErrors() override |

###### Return Value

CompilationEvent

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

ActionStep.CheckForErrors

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

OpenWorkspaceToolStep Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor.htm language=enus -->
## TOPIC 00257: RealTimeSequenceCallParameterAssignment Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

RealTimeSequenceCallParameterAssignment

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public RealTimeSequenceCallParameterAssignment() |

| Visual C++ |
| --- |
| public: RealTimeSequenceCallParameterAssignment() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

ParameterName

String.Empty

Value

VoidValue

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequenceCallParameterAssignment Class

RealTimeSequenceCallParameterAssignment Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor_1.htm language=enus -->
## TOPIC 00258: RealTimeSequenceCallParameterAssignment Constructor (RealTimeSequenceCallParameterAssignment)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

RealTimeSequenceCallParameterAssignment

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As RealTimeSequenceCallParameterAssignment _ ) |

| C# |
| --- |
| public RealTimeSequenceCallParameterAssignment( RealTimeSequenceCallParameterAssignment node ) |

| Visual C++ |
| --- |
| public: RealTimeSequenceCallParameterAssignment( RealTimeSequenceCallParameterAssignment^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.RealTimeSequenceCallParameterAssignmentThe instance of RealTimeSequenceCallParameterAssignment to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequenceCallParameterAssignment Class

RealTimeSequenceCallParameterAssignment Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor_3.htm language=enus -->
## TOPIC 00259: RealTimeSequenceCallParameterAssignment Constructor (String, SystemDefinitionChannelResource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencecallparameterassignment__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

RealTimeSequenceCallParameterAssignment

parameterName

value

value

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ parameterName As String, _ value As SystemDefinitionChannelResource _ ) |

| C# |
| --- |
| public RealTimeSequenceCallParameterAssignment( string parameterName, SystemDefinitionChannelResource value ) |

| Visual C++ |
| --- |
| public: RealTimeSequenceCallParameterAssignment( String^ parameterName, SystemDefinitionChannelResource^ value ) |

###### Parameters

- **parameterName**
  - Type: System.StringThe name of the sequence parameter.

- **value**
  - Type: NationalInstruments.VeriStand.Data.SystemDefinitionChannelResourceThe system definition channel that provides the value for parameterName. You can access this object from the NationalInstruments.VeriStand.Data assembly.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequenceCallParameterAssignment Class

RealTimeSequenceCallParameterAssignment Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencegroupstep__ctor_1.htm language=enus -->
## TOPIC 00260: RealTimeSequenceGroupStep Constructor (RealTimeSequenceGroupStep)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencegroupstep__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_realtimesequencegroupstep__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

RealTimeSequenceGroupStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As RealTimeSequenceGroupStep _ ) |

| C# |
| --- |
| public RealTimeSequenceGroupStep( RealTimeSequenceGroupStep node ) |

| Visual C++ |
| --- |
| public: RealTimeSequenceGroupStep( RealTimeSequenceGroupStep^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.RealTimeSequenceGroupStepThe instance of RealTimeSequenceGroupStep to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RealTimeSequenceGroupStep Class

RealTimeSequenceGroupStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendprojectcommandstep__ctor_1.htm language=enus -->
## TOPIC 00261: SendProjectCommandStep Constructor (SendProjectCommandStep)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendprojectcommandstep__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_sendprojectcommandstep__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SendProjectCommandStep

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As SendProjectCommandStep _ ) |

| C# |
| --- |
| public SendProjectCommandStep( SendProjectCommandStep node ) |

| Visual C++ |
| --- |
| public: SendProjectCommandStep( SendProjectCommandStep^ node ) |

###### Parameters

- **node**
  - Type: NationalInstruments.VeriStand.StimulusProfileDefinitionApi.SendProjectCommandStepThe instance of SendProjectCommandStep to copy.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SendProjectCommandStep Class

SendProjectCommandStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_startloggingstep__ctor_2.htm language=enus -->
## TOPIC 00262: StartLoggingStep Constructor (String, String, Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_startloggingstep__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_startloggingstep__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

StartLoggingStep

configurationName

filePath

rate

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ configurationName As String, _ filePath As String, _ rate As Double _ ) |

| C# |
| --- |
| public StartLoggingStep( string configurationName, string filePath, double rate ) |

| Visual C++ |
| --- |
| public: StartLoggingStep( String^ configurationName, String^ filePath, double rate ) |

###### Parameters

- **configurationName**
  - Type: System.StringThe name of the logging configuration, which you can use to control data logging after it starts.

- **filePath**
  - Type: System.StringThe path to the log file (.tdms) on disk.

- **rate**
  - Type: System.DoubleThe rate in hertz at which to log data.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StartLoggingStep Class

StartLoggingStep Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_stimulusprofile_checkforerrors.htm language=enus -->
## TOPIC 00263: StimulusProfile.CheckForErrors Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_stimulusprofile_checkforerrors.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_stimulusprofile_checkforerrors.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Performs checks on the stimulus profile and returns any errors, warnings, or messages that are relevant to the stimulus profile's current configuration.

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function CheckForErrors As CompilationEvent() |

| C# |
| --- |
| public CompilationEvent[] CheckForErrors() |

| Visual C++ |
| --- |
| public: array<CompilationEvent^>^ CheckForErrors() |

###### Return Value

CompilationEvent

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StimulusProfile Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_stimulusprofile_savestimulusprofile.htm language=enus -->
## TOPIC 00264: StimulusProfile.SaveStimulusProfile Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_stimulusprofile_savestimulusprofile.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_stimulusprofile_savestimulusprofile.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

file

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SaveStimulusProfile ( _ file As String _ ) |

| C# |
| --- |
| public void SaveStimulusProfile( string file ) |

| Visual C++ |
| --- |
| public: void SaveStimulusProfile( String^ file ) |

###### Parameters

- **file**
  - Type: System.StringThe name of the stimulus profile file. This can be a fully qualified or relative path, including the file name.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

StimulusProfile Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_updatemodelparametersfromfile__ctor.htm language=enus -->
## TOPIC 00265: UpdateModelParametersFromFile Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_updatemodelparametersfromfile__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_updatemodelparametersfromfile__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

UpdateModelParametersFromFile

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public UpdateModelParametersFromFile() |

| Visual C++ |
| --- |
| public: UpdateModelParametersFromFile() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Target

Controller

Delimiter

Tab

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

UpdateModelParametersFromFile Class

UpdateModelParametersFromFile Overload

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_updatemodelparametersfromfile_checkforerrors.htm language=enus -->
## TOPIC 00266: UpdateModelParametersFromFile.CheckForErrors Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_updatemodelparametersfromfile_checkforerrors.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_stimulusprofiledefinitionapi_updatemodelparametersfromfile_checkforerrors.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Performs checks on a step and returns any errors, warnings, or messages that are relevant to the step's current configuration.

Namespace:

NationalInstruments.VeriStand.StimulusProfileDefinitionApi

Assembly:

NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function CheckForErrors As CompilationEvent() |

| C# |
| --- |
| public override CompilationEvent[] CheckForErrors() |

| Visual C++ |
| --- |
| public: virtual array<CompilationEvent^>^ CheckForErrors() override |

###### Return Value

CompilationEvent

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

ActionStep.CheckForErrors

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

UpdateModelParametersFromFile Class

NationalInstruments.VeriStand.StimulusProfileDefinitionApi Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor.htm language=enus -->
## TOPIC 00267: Alarm Constructor (String, String, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, Double, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarm

UpperLimit

LowerLimit

AlarmSource

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ AlarmSource As Channel, _ UpperLimit As BaseNode, _ LowerLimit As BaseNode, _ AlarmAction As Procedure, _ Mode As AlarmMode, _ DefaultState As AlarmState, _ Priority As AlarmPriority, _ Delay As Double, _ TripMessage As String _ ) |

| C# |
| --- |
| public Alarm( string Name, string Description, Channel AlarmSource, BaseNode UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage ) |

| Visual C++ |
| --- |
| public: Alarm( String^ Name, String^ Description, Channel^ AlarmSource, BaseNode^ UpperLimit, BaseNode^ LowerLimit, Procedure^ AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, String^ TripMessage ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Alarm.

- **Description**
  - Type: System.StringThe description of the Alarm.

- **AlarmSource**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelThe channel to monitor for alarm conditions.

- **UpperLimit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered.

- **LowerLimit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered.

- **AlarmAction**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ProcedureThe Procedure to initiate when the alarm occurs.

- **Mode**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmModeThe AlarmMode (Normal or IndicateOnly).

- **DefaultState**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmStateThe default AlarmState (Enabled or Disabled).

- **Priority**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriorityThe AlarmPriority level (Low, Medium, or High).

- **Delay**
  - Type: System.DoubleThe amount of time to wait before triggering the alarm.

- **TripMessage**
  - Type: System.StringThe message to display when the alarm is tripped.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarm Class

Alarm Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_2.htm language=enus -->
## TOPIC 00268: Alarm Constructor (String, String, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, UInt32, UInt32, Double, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarm

UpperLimit

LowerLimit

AlarmSource

GroupNumber

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ AlarmSource As Channel, _ UpperLimit As ValueSource, _ LowerLimit As ValueSource, _ AlarmAction As Procedure, _ Mode As AlarmMode, _ DefaultState As AlarmState, _ GroupNumber As UInteger, _ PriorityNumber As UInteger, _ Delay As Double, _ TripMessage As String _ ) |

| C# |
| --- |
| public Alarm( string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, uint GroupNumber, uint PriorityNumber, double Delay, string TripMessage ) |

| Visual C++ |
| --- |
| public: Alarm( String^ Name, String^ Description, Channel^ AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure^ AlarmAction, AlarmMode Mode, AlarmState DefaultState, unsigned int GroupNumber, unsigned int PriorityNumber, double Delay, String^ TripMessage ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Alarm.

- **Description**
  - Type: System.StringThe description of the Alarm.

- **AlarmSource**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelThe channel to monitor for alarm conditions.

- **UpperLimit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ValueSourceThe channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered.

- **LowerLimit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ValueSourceThe channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered.

- **AlarmAction**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ProcedureThe Procedure to initiate when the alarm occurs.

- **Mode**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmModeThe AlarmMode (Normal or IndicateOnly).

- **DefaultState**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmStateThe default AlarmState (Enabled or Disabled).

- **GroupNumber**
  - Type: System.UInt32The number of the group to which the Alarm belongs.

- **PriorityNumber**
  - Type: System.UInt32The priority of the alarm. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31.

- **Delay**
  - Type: System.DoubleThe amount of time to wait before triggering the alarm.

- **TripMessage**
  - Type: System.StringThe message to display when the alarm is tripped.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarm Class

Alarm Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_3.htm language=enus -->
## TOPIC 00269: Alarm Constructor (String, String, Channel, Double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, Double, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarm

UpperLimit

LowerLimit

AlarmSource

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ AlarmSource As Channel, _ UpperLimit As Double, _ LowerLimit As BaseNode, _ AlarmAction As Procedure, _ Mode As AlarmMode, _ DefaultState As AlarmState, _ Priority As AlarmPriority, _ Delay As Double, _ TripMessage As String _ ) |

| C# |
| --- |
| public Alarm( string Name, string Description, Channel AlarmSource, double UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage ) |

| Visual C++ |
| --- |
| public: Alarm( String^ Name, String^ Description, Channel^ AlarmSource, double UpperLimit, BaseNode^ LowerLimit, Procedure^ AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, String^ TripMessage ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Alarm.

- **Description**
  - Type: System.StringThe description of the Alarm.

- **AlarmSource**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelThe channel to monitor for alarm conditions.

- **UpperLimit**
  - Type: System.DoubleThe constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered.

- **LowerLimit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered.

- **AlarmAction**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ProcedureThe Procedure to initiate when the alarm occurs.

- **Mode**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmModeThe AlarmMode (Normal or IndicateOnly).

- **DefaultState**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmStateThe default AlarmState (Enabled or Disabled).

- **Priority**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriorityThe AlarmPriority level (Low, Medium, or High).

- **Delay**
  - Type: System.DoubleThe amount of time to wait before triggering the alarm.

- **TripMessage**
  - Type: System.StringThe message to display when the alarm is tripped.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarm Class

Alarm Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_4.htm language=enus -->
## TOPIC 00270: Alarm Constructor (String, String, Channel, Double, Double, Procedure, AlarmMode, AlarmState, AlarmPriority, Double, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_4.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm__ctor_4.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarm

UpperLimit

LowerLimit

AlarmSource

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ AlarmSource As Channel, _ UpperLimit As Double, _ LowerLimit As Double, _ AlarmAction As Procedure, _ Mode As AlarmMode, _ DefaultState As AlarmState, _ Priority As AlarmPriority, _ Delay As Double, _ TripMessage As String _ ) |

| C# |
| --- |
| public Alarm( string Name, string Description, Channel AlarmSource, double UpperLimit, double LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage ) |

| Visual C++ |
| --- |
| public: Alarm( String^ Name, String^ Description, Channel^ AlarmSource, double UpperLimit, double LowerLimit, Procedure^ AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, String^ TripMessage ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Alarm.

- **Description**
  - Type: System.StringThe description of the Alarm.

- **AlarmSource**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelThe channel to monitor for alarm conditions.

- **UpperLimit**
  - Type: System.DoubleThe constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered.

- **LowerLimit**
  - Type: System.DoubleThe constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered.

- **AlarmAction**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ProcedureThe Procedure to initiate when the alarm occurs.

- **Mode**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmModeThe AlarmMode (Normal or IndicateOnly).

- **DefaultState**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmStateThe default AlarmState (Enabled or Disabled).

- **Priority**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmPriorityThe AlarmPriority level (Low, Medium, or High).

- **Delay**
  - Type: System.DoubleThe amount of time to wait before triggering the alarm.

- **TripMessage**
  - Type: System.StringThe message to display when the alarm is tripped.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarm Class

Alarm Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm_setlowerlimit.htm language=enus -->
## TOPIC 00271: Alarm.SetLowerLimit Method (BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm_setlowerlimit.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm_setlowerlimit.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the low limit to the specified channel value.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetLowerLimit ( _ LowerLimit As BaseNode _ ) |

| C# |
| --- |
| public void SetLowerLimit( BaseNode LowerLimit ) |

| Visual C++ |
| --- |
| public: void SetLowerLimit( BaseNode^ LowerLimit ) |

###### Parameters

- **LowerLimit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel that determines the low limit value of the alarm.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarm Class

SetLowerLimit Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm_setupperlimit_1.htm language=enus -->
## TOPIC 00272: Alarm.SetUpperLimit Method (ValueSource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm_setupperlimit_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarm_setupperlimit_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the high limit to the specified channel or constant value.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetUpperLimit ( _ Limit As ValueSource _ ) |

| C# |
| --- |
| public void SetUpperLimit( ValueSource Limit ) |

| Visual C++ |
| --- |
| public: void SetUpperLimit( ValueSource Limit ) |

###### Parameters

- **Limit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ValueSourceThe channel or constant that determines the high limit value of the alarm.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarm Class

SetUpperLimit Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarmfolder_addalarm.htm language=enus -->
## TOPIC 00273: AlarmFolder.AddAlarm Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarmfolder_addalarm.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarmfolder_addalarm.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarm

AlarmFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddAlarm ( _ alarm As Alarm _ ) As Boolean |

| C# |
| --- |
| public bool AddAlarm( Alarm alarm ) |

| Visual C++ |
| --- |
| public: bool AddAlarm( Alarm^ alarm ) |

###### Parameters

- **alarm**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmThe Alarm to add.

###### Return Value

true

True

Alarm

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AlarmFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarmfolder_getalarmlist.htm language=enus -->
## TOPIC 00274: AlarmFolder.GetAlarmList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarmfolder_getalarmlist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarmfolder_getalarmlist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarm

AlarmFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAlarmList As Alarm() |

| C# |
| --- |
| public Alarm[] GetAlarmList() |

| Visual C++ |
| --- |
| public: array<Alarm^>^ GetAlarmList() |

###### Return Value

Alarm

AlarmFolder

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

AlarmFolder

| Note: |
| --- |
| Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AlarmFolder Class

GetAlarmList Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarming__ctor.htm language=enus -->
## TOPIC 00275: Alarming Constructor (String, String, AlarmingStepFunction, BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarming__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarming__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarming

Name

Description

Function

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ Function As AlarmingStepFunction, _ Alarm As BaseNode _ ) |

| C# |
| --- |
| public Alarming( string Name, string Description, AlarmingStepFunction Function, BaseNode Alarm ) |

| Visual C++ |
| --- |
| public: Alarming( String^ Name, String^ Description, AlarmingStepFunction Function, BaseNode^ Alarm ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Alarming step.

- **Description**
  - Type: System.StringThe description of the Alarming step.

- **Function**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AlarmingStepFunctionThe AlarmingStepFunction. For example, an Alarming step can enable or disable an alarm or adjust the alarm settings.

- **Alarm**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe Alarm to configure.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarming Class

Alarming Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarming_setupperlimit_1.htm language=enus -->
## TOPIC 00276: Alarming.SetUpperLimit Method (ValueSource)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarming_setupperlimit_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarming_setupperlimit_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the high limit to the specified channel or constant value.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetUpperLimit ( _ UpperLimit As ValueSource _ ) |

| C# |
| --- |
| public void SetUpperLimit( ValueSource UpperLimit ) |

| Visual C++ |
| --- |
| public: void SetUpperLimit( ValueSource UpperLimit ) |

###### Parameters

- **UpperLimit**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ValueSourceThe channel or constant that determines the high limit value of the alarm.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarming Class

SetUpperLimit Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarms_getalarmlist_1.htm language=enus -->
## TOPIC 00277: Alarms.GetAlarmList Method (Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarms_getalarmlist_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alarms_getalarmlist_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alarm

Alarms

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAlarmList ( _ deep As Boolean _ ) As Alarm() |

| C# |
| --- |
| public Alarm[] GetAlarmList( bool deep ) |

| Visual C++ |
| --- |
| public: array<Alarm^>^ GetAlarmList( bool deep ) |

###### Parameters

- **deep**
  - Type: System.BooleanSpecifies whether the method traverses each child AlarmFolder element of the Alarms section. true (True in Visual Basic) if the method traverses each child AlarmFolder instance to search for other AlarmFolder instances to traverse or other Alarm elements to add to the result list; otherwise false (False in Visual Basic).

###### Return Value

Alarm

Alarms

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alarms Class

GetAlarmList Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alias__ctor_1.htm language=enus -->
## TOPIC 00278: Alias Constructor (String, String, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alias__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alias__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alias

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ LinkedChannelPath As String _ ) |

| C# |
| --- |
| public Alias( string Name, string Description, string LinkedChannelPath ) |

| Visual C++ |
| --- |
| public: Alias( String^ Name, String^ Description, String^ LinkedChannelPath ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the alias.

- **Description**
  - Type: System.StringThe description of the alias.

- **LinkedChannelPath**
  - Type: System.StringThe path to the channel that alias represents.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alias Class

Alias Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alias_finalize.htm language=enus -->
## TOPIC 00279: Alias.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alias_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_alias_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Alias Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_addnewaliasbyreference.htm language=enus -->
## TOPIC 00280: Aliases.AddNewAliasByReference Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_addnewaliasbyreference.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_addnewaliasbyreference.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alias

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddNewAliasByReference ( _ Name As String, _ Description As String, _ LinkedChannelReference As Channel _ ) As Boolean |

| C# |
| --- |
| public bool AddNewAliasByReference( string Name, string Description, Channel LinkedChannelReference ) |

| Visual C++ |
| --- |
| public: bool AddNewAliasByReference( String^ Name, String^ Description, Channel^ LinkedChannelReference ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Alias.

- **Description**
  - Type: System.StringThe description of the Alias.

- **LinkedChannelReference**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ChannelThe reference to the channel that Alias represents.

###### Return Value

true

True

Alias

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Aliases Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_getaliaseslist.htm language=enus -->
## TOPIC 00281: Aliases.GetAliasesList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_getaliaseslist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_getaliaseslist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alias

Aliases

Aliases

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAliasesList As Alias() |

| C# |
| --- |
| public Alias[] GetAliasesList() |

| Visual C++ |
| --- |
| public: array<Alias^>^ GetAliasesList() |

###### Return Value

Alias

Aliases

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Aliases Class

GetAliasesList Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_getaliaseslist_1.htm language=enus -->
## TOPIC 00282: Aliases.GetAliasesList Method (Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_getaliaseslist_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliases_getaliaseslist_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alias

Aliases

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAliasesList ( _ deep As Boolean _ ) As Alias() |

| C# |
| --- |
| public Alias[] GetAliasesList( bool deep ) |

| Visual C++ |
| --- |
| public: array<Alias^>^ GetAliasesList( bool deep ) |

###### Parameters

- **deep**
  - Type: System.BooleanSpecifies whether the method traverses each child AliasFolder element of the Aliases section. true (True in Visual Basic) if the method traverses each child AliasFolder instance to search for other AliasFolder instances to traverse or other Alias elements to add to the result list; otherwise false (False in Visual Basic).

###### Return Value

Alias

Aliases

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Aliases Class

GetAliasesList Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_addaliasfolder.htm language=enus -->
## TOPIC 00283: AliasFolder.AddAliasFolder Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_addaliasfolder.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_addaliasfolder.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

AliasFolder

AliasFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddAliasFolder ( _ folder As AliasFolder _ ) As Boolean |

| C# |
| --- |
| public bool AddAliasFolder( AliasFolder folder ) |

| Visual C++ |
| --- |
| public: bool AddAliasFolder( AliasFolder^ folder ) |

###### Parameters

- **folder**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AliasFolderThe AliasFolder to add.

###### Return Value

true

True

AliasFolder

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AliasFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_getaliaseslist.htm language=enus -->
## TOPIC 00284: AliasFolder.GetAliasesList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_getaliaseslist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_getaliaseslist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alias

AliasFolder

AliasFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAliasesList As Alias() |

| C# |
| --- |
| public Alias[] GetAliasesList() |

| Visual C++ |
| --- |
| public: array<Alias^>^ GetAliasesList() |

###### Return Value

Alias

AliasFolder

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AliasFolder Class

GetAliasesList Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_getaliaseslist_1.htm language=enus -->
## TOPIC 00285: AliasFolder.GetAliasesList Method (Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_getaliaseslist_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_aliasfolder_getaliaseslist_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Alias

AliasFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAliasesList ( _ deep As Boolean _ ) As Alias() |

| C# |
| --- |
| public Alias[] GetAliasesList( bool deep ) |

| Visual C++ |
| --- |
| public: array<Alias^>^ GetAliasesList( bool deep ) |

###### Parameters

- **deep**
  - Type: System.BooleanSpecifies whether the method traverses each child AliasFolder element of the AliasFolder instance. true (True in Visual Basic) if the method traverses each child AliasFolder instance to search for other AliasFolder instances to traverse or other Alias elements to add to the result list; otherwise false (False in Visual Basic).

###### Return Value

Alias

AliasFolder

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

AliasFolder Class

GetAliasesList Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findchildrenbyguid.htm language=enus -->
## TOPIC 00286: BaseNode.FindChildrenByGUID Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findchildrenbyguid.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findchildrenbyguid.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

BaseNode

TypeGUID

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function FindChildrenByGUID ( _ TypeGUID As String _ ) As BaseNode() |

| C# |
| --- |
| public BaseNode[] FindChildrenByGUID( string TypeGUID ) |

| Visual C++ |
| --- |
| public: array<BaseNode^>^ FindChildrenByGUID( String^ TypeGUID ) |

###### Parameters

- **TypeGUID**
  - Type: System.StringThe GUID to find.

###### Return Value

BaseNode

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BaseNode Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findfirstchildwithname.htm language=enus -->
## TOPIC 00287: BaseNode.FindFirstChildWithName Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findfirstchildwithname.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findfirstchildwithname.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets the first child node with the specified name.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function FindFirstChildWithName ( _ Name As String, _ <OutAttribute> ByRef Child As BaseNode, _ DeepHierarchy As Boolean _ ) As Boolean |

| C# |
| --- |
| public bool FindFirstChildWithName( string Name, out BaseNode Child, bool DeepHierarchy ) |

| Visual C++ |
| --- |
| public: bool FindFirstChildWithName( String^ Name, [OutAttribute] BaseNode^% Child, bool DeepHierarchy ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the node to find.

- **Child**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode %Upon return, contains the child node, or a null reference (Nothing in Visual Basic) if not found.

- **DeepHierarchy**
  - Type: System.Boolean true (True in Visual Basic) to search the entire hierarchy beneath this node. FALSE to search only the children of this node.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BaseNode Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findnodebypath.htm language=enus -->
## TOPIC 00288: BaseNode.FindNodeByPath Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findnodebypath.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_findnodebypath.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Gets a node using the specified path.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function FindNodeByPath ( _ nodepath As String, _ <OutAttribute> ByRef Node As BaseNode _ ) As Boolean |

| C# |
| --- |
| public bool FindNodeByPath( string nodepath, out BaseNode Node ) |

| Visual C++ |
| --- |
| public: bool FindNodeByPath( String^ nodepath, [OutAttribute] BaseNode^% Node ) |

###### Parameters

- **nodepath**
  - Type: System.StringThe path to the node. The path is relative to path of this node.

- **Node**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode %Upon return, contains the node with the specified nodepath, or a null reference (Nothing in Visual Basic) if not found.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BaseNode Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_getchildren.htm language=enus -->
## TOPIC 00289: BaseNode.GetChildren Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_getchildren.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_getchildren.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

BaseNode

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetChildren As BaseNode() |

| C# |
| --- |
| public BaseNode[] GetChildren() |

| Visual C++ |
| --- |
| public: array<BaseNode^>^ GetChildren() |

###### Return Value

BaseNode

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BaseNode Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_removenode.htm language=enus -->
## TOPIC 00290: BaseNode.RemoveNode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_removenode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_removenode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Removes this node from the hierarchy, if the node can be removed.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overridable Function RemoveNode As Boolean |

| C# |
| --- |
| public virtual bool RemoveNode() |

| Visual C++ |
| --- |
| public: virtual bool RemoveNode() |

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BaseNode Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_renamenode.htm language=enus -->
## TOPIC 00291: BaseNode.RenameNode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_renamenode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_basenode_renamenode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overridable Function RenameNode ( _ NewName As String _ ) As Boolean |

| C# |
| --- |
| public virtual bool RenameNode( string NewName ) |

| Visual C++ |
| --- |
| public: virtual bool RenameNode( String^ NewName ) |

###### Parameters

- **NewName**
  - Type: System.StringThe name of the node.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

BaseNode Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannel_downcast.htm language=enus -->
## TOPIC 00292: CalculatedChannel.Downcast Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannel_downcast.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannel_downcast.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CalculatedChannel

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Downcast As CalculatedChannel |

| C# |
| --- |
| public CalculatedChannel Downcast() |

| Visual C++ |
| --- |
| public: CalculatedChannel^ Downcast() |

###### Return Value

CalculatedChannel

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CalculatedChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannel_finalize.htm language=enus -->
## TOPIC 00293: CalculatedChannel.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannel_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannel_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CalculatedChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addacceleration.htm language=enus -->
## TOPIC 00294: CalculatedChannels.AddAcceleration Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addacceleration.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addacceleration.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Acceleration

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddAcceleration ( _ acceleration As Acceleration _ ) As Boolean |

| C# |
| --- |
| public bool AddAcceleration( Acceleration acceleration ) |

| Visual C++ |
| --- |
| public: bool AddAcceleration( Acceleration^ acceleration ) |

###### Parameters

- **acceleration**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AccelerationThe Acceleration calculated channel to add.

###### Return Value

true

True

Acceleration

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CalculatedChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addaverage.htm language=enus -->
## TOPIC 00295: CalculatedChannels.AddAverage Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addaverage.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addaverage.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Average

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddAverage ( _ average As Average _ ) As Boolean |

| C# |
| --- |
| public bool AddAverage( Average average ) |

| Visual C++ |
| --- |
| public: bool AddAverage( Average^ average ) |

###### Parameters

- **average**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.AverageThe Average calculated channel to add.

###### Return Value

true

True

Average

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CalculatedChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addcalculatedchannel.htm language=enus -->
## TOPIC 00296: CalculatedChannels.AddCalculatedChannel Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addcalculatedchannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_calculatedchannels_addcalculatedchannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CalculatedChannel

CalculatedChannels

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddCalculatedChannel ( _ calculatedChannel As CalculatedChannel _ ) As Boolean |

| C# |
| --- |
| public bool AddCalculatedChannel( CalculatedChannel calculatedChannel ) |

| Visual C++ |
| --- |
| public: bool AddCalculatedChannel( CalculatedChannel^ calculatedChannel ) |

###### Parameters

- **calculatedChannel**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.CalculatedChannelThe CalculatedChannel to add.

###### Return Value

true

True

CalculatedChannel

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CalculatedChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_callprocedure_finalize.htm language=enus -->
## TOPIC 00297: CallProcedure.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_callprocedure_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_callprocedure_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CallProcedure Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_addcanport.htm language=enus -->
## TOPIC 00298: CAN.AddCANPort Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_addcanport.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_addcanport.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CANPort

CAN

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddCANPort ( _ canPort As CANPort _ ) As Boolean |

| C# |
| --- |
| public bool AddCANPort( CANPort canPort ) |

| Visual C++ |
| --- |
| public: bool AddCANPort( CANPort^ canPort ) |

###### Parameters

- **canPort**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.CANPortThe CAN port to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

[LabVIEW Walkthrough: Modifying a System Definition File](../../vsnetapis/lv_sysdef_creating.html)

[C# Walkthrough: Modifying a System Definition File](../../vsnetapis/c_sysdef_creating.html)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CAN Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_finalize.htm language=enus -->
## TOPIC 00299: CAN.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CAN Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_getcanportlist.htm language=enus -->
## TOPIC 00300: CAN.GetCANPortList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_getcanportlist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_can_getcanportlist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CANPort

CAN

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetCANPortList As CANPort() |

| C# |
| --- |
| public CANPort[] GetCANPortList() |

| Visual C++ |
| --- |
| public: array<CANPort^>^ GetCANPortList() |

###### Return Value

CANPort

CAN

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

For example code and more information about this method, refer to one of the following help topics:

[LabVIEW Walkthrough: Modifying a System Definition File](../../vsnetapis/lv_sysdef_creating.html)

[C# Walkthrough: Modifying a System Definition File](../../vsnetapis/c_sysdef_creating.html)

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CAN Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_remove986xsupport.htm language=enus -->
## TOPIC 00301: CANPort.Remove986xSupport Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_remove986xsupport.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_remove986xsupport.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

x

Set986xSupport

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Remove986xSupport |

| C# |
| --- |
| public void Remove986xSupport() |

| Visual C++ |
| --- |
| public: void Remove986xSupport() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CANPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_removeautomaticframeprocessing.htm language=enus -->
## TOPIC 00302: CANPort.RemoveAutomaticFrameProcessing Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_removeautomaticframeprocessing.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_removeautomaticframeprocessing.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CANPort

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub RemoveAutomaticFrameProcessing |

| C# |
| --- |
| public void RemoveAutomaticFrameProcessing() |

| Visual C++ |
| --- |
| public: void RemoveAutomaticFrameProcessing() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CANPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_set986xsupport.htm language=enus -->
## TOPIC 00303: CANPort.Set986xSupport Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_set986xsupport.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_canport_set986xsupport.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

x

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Set986xSupport ( _ file As DependentFile, _ rioPortNumber As UShort _ ) |

| C# |
| --- |
| public void Set986xSupport( DependentFile file, ushort rioPortNumber ) |

| Visual C++ |
| --- |
| public: void Set986xSupport( DependentFile^ file, unsigned short rioPortNumber ) |

###### Parameters

- **file**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile The reference to the bitfile for the 986x devices.

- **rioPortNumber**
  - Type: System.UInt16 The port to download file to.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| If the bitfile contains configuration information for anything other than CompactRIO 986x devices, you also must add the bitfile as a configuration file under FPGA. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CANPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_channel__ctor_1.htm language=enus -->
## TOPIC 00304: Channel Constructor ()

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_channel__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_channel__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Channel

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ node As ChannelType _ ) |

| C# |
| --- |
| public Channel( ChannelType node ) |

| Visual C++ |
| --- |
| public: Channel( ChannelType^ node ) |

###### Parameters

- **node**
  - Type: ChannelTypeThe ChannelType object.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Channel Class

Channel Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_clearchassismasterdevice.htm language=enus -->
## TOPIC 00305: Chassis.ClearChassisMasterDevice Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_clearchassismasterdevice.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_clearchassismasterdevice.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Clears the chassis master hardware synchronization device setting.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ClearChassisMasterDevice |

| C# |
| --- |
| public void ClearChassisMasterDevice() |

| Visual C++ |
| --- |
| public: void ClearChassisMasterDevice() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Chassis Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_getfpga.htm language=enus -->
## TOPIC 00306: Chassis.GetFPGA Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_getfpga.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_getfpga.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FPGA

Chassis

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetFPGA As FPGA |

| C# |
| --- |
| public FPGA GetFPGA() |

| Visual C++ |
| --- |
| public: FPGA^ GetFPGA() |

###### Return Value

FPGA

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Chassis Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_gettimingandsync.htm language=enus -->
## TOPIC 00307: Chassis.GetTimingAndSync Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_gettimingandsync.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_gettimingandsync.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

TimingAndSync

Chassis

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetTimingAndSync As TimingAndSync |

| C# |
| --- |
| public TimingAndSync GetTimingAndSync() |

| Visual C++ |
| --- |
| public: TimingAndSync^ GetTimingAndSync() |

###### Return Value

TimingAndSync

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Chassis Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_setchassismastertotimingandsync.htm language=enus -->
## TOPIC 00308: Chassis.SetChassisMasterToTimingAndSync Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_setchassismastertotimingandsync.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_chassis_setchassismastertotimingandsync.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the chassis master hardware synchronization device to the timing and sync device you specify.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function SetChassisMasterToTimingAndSync ( _ TimingAndSyncName As String _ ) As Boolean |

| C# |
| --- |
| public bool SetChassisMasterToTimingAndSync( string TimingAndSyncName ) |

| Visual C++ |
| --- |
| public: bool SetChassisMasterToTimingAndSync( String^ TimingAndSyncName ) |

###### Parameters

- **TimingAndSyncName**
  - Type: System.StringThe name of the timing and sync device.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Chassis Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_condition_setvalue.htm language=enus -->
## TOPIC 00309: Condition.SetValue Method (BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_condition_setvalue.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_condition_setvalue.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Variable

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetValue ( _ Value As BaseNode _ ) |

| C# |
| --- |
| public void SetValue( BaseNode Value ) |

| Visual C++ |
| --- |
| public: void SetValue( BaseNode^ Value ) |

###### Parameters

- **Value**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel to compare with Variable.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Condition Class

SetValue Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_2.htm language=enus -->
## TOPIC 00310: Conditional Constructor (String, String, UInt16, BaseNode, BaseNode, Double, BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Conditional

X

Y

W

Z

Y

Z

W

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ ComparisonMode As UShort, _ XValue As BaseNode, _ YValue As BaseNode, _ WValue As Double, _ ZValue As BaseNode _ ) |

| C# |
| --- |
| public Conditional( string Name, string Description, ushort ComparisonMode, BaseNode XValue, BaseNode YValue, double WValue, BaseNode ZValue ) |

| Visual C++ |
| --- |
| public: Conditional( String^ Name, String^ Description, unsigned short ComparisonMode, BaseNode^ XValue, BaseNode^ YValue, double WValue, BaseNode^ ZValue ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Conditional calculated channel.

- **Description**
  - Type: System.StringThe description of the Conditional calculated channel.

- **ComparisonMode**
  - Type: System.UInt16The comparison condition. Use class constants such as Greater.

- **XValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel to be compared.

- **YValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel value to which X is compared.

- **WValue**
  - Type: System.DoubleThe constant that determines the value of W.

- **ZValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel that determines the value of Z.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Conditional Class

Conditional Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_3.htm language=enus -->
## TOPIC 00311: Conditional Constructor (String, String, UInt16, BaseNode, BaseNode, Double, Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Conditional

X

Y

W

Z

Y

W

Z

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ ComparisonMode As UShort, _ XValue As BaseNode, _ YValue As BaseNode, _ WValue As Double, _ ZValue As Double _ ) |

| C# |
| --- |
| public Conditional( string Name, string Description, ushort ComparisonMode, BaseNode XValue, BaseNode YValue, double WValue, double ZValue ) |

| Visual C++ |
| --- |
| public: Conditional( String^ Name, String^ Description, unsigned short ComparisonMode, BaseNode^ XValue, BaseNode^ YValue, double WValue, double ZValue ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Conditional calculated channel.

- **Description**
  - Type: System.StringThe description of the Conditional calculated channel.

- **ComparisonMode**
  - Type: System.UInt16The comparison condition. Use class constants such as Greater.

- **XValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel to be compared.

- **YValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel value to which X is compared.

- **WValue**
  - Type: System.DoubleThe constant that determines the value of W.

- **ZValue**
  - Type: System.DoubleThe constant that determines the value of Z.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Conditional Class

Conditional Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_5.htm language=enus -->
## TOPIC 00312: Conditional Constructor (String, String, UInt16, BaseNode, Double, BaseNode, Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_5.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional__ctor_5.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Conditional

X

Y

W

Z

Y

Z

W

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ ComparisonMode As UShort, _ XValue As BaseNode, _ YValue As Double, _ WValue As BaseNode, _ ZValue As Double _ ) |

| C# |
| --- |
| public Conditional( string Name, string Description, ushort ComparisonMode, BaseNode XValue, double YValue, BaseNode WValue, double ZValue ) |

| Visual C++ |
| --- |
| public: Conditional( String^ Name, String^ Description, unsigned short ComparisonMode, BaseNode^ XValue, double YValue, BaseNode^ WValue, double ZValue ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the Conditional calculated channel.

- **Description**
  - Type: System.StringThe description of the Conditional calculated channel.

- **ComparisonMode**
  - Type: System.UInt16The comparison condition. Use class constants such as Greater.

- **XValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel to be compared.

- **YValue**
  - Type: System.DoubleThe constant that determines the value of Y.

- **WValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel that determines the value of W.

- **ZValue**
  - Type: System.DoubleThe constant that determines the value of Z.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Conditional Class

Conditional Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional_finalize.htm language=enus -->
## TOPIC 00313: Conditional.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Conditional Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional_setwvalue_1.htm language=enus -->
## TOPIC 00314: Conditional.SetWValue Method (Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional_setwvalue_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_conditional_setwvalue_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

W

X

Y

W

Z

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetWValue ( _ WValue As Double _ ) |

| C# |
| --- |
| public void SetWValue( double WValue ) |

| Visual C++ |
| --- |
| public: void SetWValue( double WValue ) |

###### Parameters

- **WValue**
  - Type: System.DoubleThe value of W.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Conditional Class

SetWValue Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_crc_setalternatechannel.htm language=enus -->
## TOPIC 00315: CRC.SetAlternateChannel Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_crc_setalternatechannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_crc_setalternatechannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

UseAlternateChannel

true

True

AlternateChannel

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetAlternateChannel ( _ AlternateChannel As BaseNode _ ) |

| C# |
| --- |
| public void SetAlternateChannel( BaseNode AlternateChannel ) |

| Visual C++ |
| --- |
| public: void SetAlternateChannel( BaseNode^ AlternateChannel ) |

###### Parameters

- **AlternateChannel**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode The channel to use to trigger writing data.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CRC Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice__ctor.htm language=enus -->
## TOPIC 00316: CustomDevice Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CustomDevice

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ GUID As String _ ) |

| C# |
| --- |
| public CustomDevice( string Name, string GUID ) |

| Visual C++ |
| --- |
| public: CustomDevice( String^ Name, String^ GUID ) |

###### Parameters

- **Name**
  - Type: System.String The name associated with the custom device, as specified in the Custom Device XML file.

- **GUID**
  - Type: System.String The GUID associated with the custom device, as specified in the Custom Device XML file.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice_adddependencies.htm language=enus -->
## TOPIC 00317: CustomDevice.AddDependencies Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice_adddependencies.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice_adddependencies.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds dependencies to a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub AddDependencies ( _ dependencies As DependentFile() _ ) |

| C# |
| --- |
| public void AddDependencies( DependentFile[] dependencies ) |

| Visual C++ |
| --- |
| public: void AddDependencies( array<DependentFile^>^ dependencies ) |

###### Parameters

- **dependencies**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile An array of type DependentFile that contains references to the dependencies.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice_setdrivervis.htm language=enus -->
## TOPIC 00318: CustomDevice.SetDriverVIs Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice_setdrivervis.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevice_setdrivervis.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the RT Driver VIs to associate with the custom device. A custom device requires at least one RT Driver VI. A single custom device can have multiple RT Driver VIs if the device supports multiple real-time operating systems or multiple execution modes.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetDriverVIs ( _ driverVIs As DependentFile() _ ) |

| C# |
| --- |
| public void SetDriverVIs( DependentFile[] driverVIs ) |

| Visual C++ |
| --- |
| public: void SetDriverVIs( array<DependentFile^>^ driverVIs ) |

###### Parameters

- **driverVIs**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFile An array of references to the RT Driver VIs.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_finalize.htm language=enus -->
## TOPIC 00319: CustomDeviceBase.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceBase Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getpropertytype.htm language=enus -->
## TOPIC 00320: CustomDeviceBase.GetPropertyType Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getpropertytype.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getpropertytype.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetPropertyType ( _ propertyName As String, _ <OutAttribute> ByRef type As PropertyContent _ ) As Boolean |

| C# |
| --- |
| public bool GetPropertyType( string propertyName, out PropertyContent type ) |

| Visual C++ |
| --- |
| public: bool GetPropertyType( String^ propertyName, [OutAttribute] PropertyContent% type ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property. Property names are case sensitive.

- **type**
  - Type: PropertyContent %The data type of the property.

###### Return Value

true

True

propertyName

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceBase Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getu16property.htm language=enus -->
## TOPIC 00321: CustomDeviceBase.GetU16Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getu16property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getu16property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

name

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetU16Property ( _ name As String, _ <OutAttribute> ByRef value As UShort _ ) As Boolean |

| C# |
| --- |
| public bool GetU16Property( string name, out ushort value ) |

| Visual C++ |
| --- |
| public: bool GetU16Property( String^ name, [OutAttribute] unsigned short% value ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the property. Property names are case-sensitive.

- **value**
  - Type: System.UInt16 %The value of the property.

###### Return Value

true

True

name

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceBase Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getu32arrayproperty.htm language=enus -->
## TOPIC 00322: CustomDeviceBase.GetU32ArrayProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getu32arrayproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_getu32arrayproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

name

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetU32ArrayProperty ( _ name As String, _ <OutAttribute> ByRef value As UInteger() _ ) As Boolean |

| C# |
| --- |
| public bool GetU32ArrayProperty( string name, out uint[] value ) |

| Visual C++ |
| --- |
| public: bool GetU32ArrayProperty( String^ name, [OutAttribute] array<unsigned int>^% value ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the property. Property names are case-sensitive.

- **value**
  - Type: System.UInt32 %The value of the property.

###### Return Value

true

True

name

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceBase Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_setdictionaryarrayproperty.htm language=enus -->
## TOPIC 00323: CustomDeviceBase.SetDictionaryArrayProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_setdictionaryarrayproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_setdictionaryarrayproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Dictionary

name

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function SetDictionaryArrayProperty ( _ name As String, _ value As Dictionary() _ ) As Boolean |

| C# |
| --- |
| public bool SetDictionaryArrayProperty( string name, Dictionary[] value ) |

| Visual C++ |
| --- |
| public: bool SetDictionaryArrayProperty( String^ name, array<Dictionary^>^ value ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the property. Property names are case-sensitive.

- **value**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.Dictionary The reference to the Dictionary array.

###### Return Value

true

True

name

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceBase Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_setu32property.htm language=enus -->
## TOPIC 00324: CustomDeviceBase.SetU32Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_setu32property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicebase_setu32property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

name

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function SetU32Property ( _ name As String, _ value As UInteger _ ) As Boolean |

| C# |
| --- |
| public bool SetU32Property( string name, uint value ) |

| Visual C++ |
| --- |
| public: bool SetU32Property( String^ name, unsigned int value ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the property. Property names are case-sensitive.

- **value**
  - Type: System.UInt32The value of the property.

###### Return Value

true

True

name

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceBase Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicesection_addcustomdevicesectionifnotfound.htm language=enus -->
## TOPIC 00325: CustomDeviceSection.AddCustomDeviceSectionIfNotFound Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicesection_addcustomdevicesectionifnotfound.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicesection_addcustomdevicesectionifnotfound.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

name

guid

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddCustomDeviceSectionIfNotFound ( _ name As String, _ guid As String, _ <OutAttribute> ByRef newItem As Boolean _ ) As CustomDeviceSection |

| C# |
| --- |
| public CustomDeviceSection AddCustomDeviceSectionIfNotFound( string name, string guid, out bool newItem ) |

| Visual C++ |
| --- |
| public: CustomDeviceSection^ AddCustomDeviceSectionIfNotFound( String^ name, String^ guid, [OutAttribute] bool% newItem ) |

###### Parameters

- **name**
  - Type: System.String The name associated with the section, as specified in the Custom Device XML file.

- **guid**
  - Type: System.String The GUID associated with the section, as specified in the Custom Device XML file.

- **newItem**
  - Type: System.Boolean % Returns true (True in Visual Basic) if the section was added.

###### Return Value

CustomDeviceSection

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceSection Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicewaveform__ctor.htm language=enus -->
## TOPIC 00326: CustomDeviceWaveform Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicewaveform__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_customdevicewaveform__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

CustomDeviceWaveform

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ guid As String, _ dataType As WaveformTypeDataType _ ) |

| C# |
| --- |
| public CustomDeviceWaveform( string name, string guid, WaveformTypeDataType dataType ) |

| Visual C++ |
| --- |
| public: CustomDeviceWaveform( String^ name, String^ guid, WaveformTypeDataType dataType ) |

###### Parameters

- **name**
  - Type: System.StringThe name of CustomDeviceWaveform, as specified in the Custom Device XML file.

- **guid**
  - Type: System.String The GUID of CustomDeviceWaveform, as specified in the Custom Device XML file.

- **dataType**
  - Type: WaveformTypeDataType The data type of CustomDeviceWaveform, which is an enumeration value of WaveformTypeDataType

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

CustomDeviceWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_cyclic_getsignalbasedframelist.htm language=enus -->
## TOPIC 00327: Cyclic.GetSignalBasedFrameList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_cyclic_getsignalbasedframelist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_cyclic_getsignalbasedframelist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SignalBasedFrame

Cyclic

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetSignalBasedFrameList As SignalBasedFrame() |

| C# |
| --- |
| public SignalBasedFrame[] GetSignalBasedFrameList() |

| Visual C++ |
| --- |
| public: array<SignalBasedFrame^>^ GetSignalBasedFrameList() |

###### Return Value

SignalBasedFrame

Cyclic

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Cyclic Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daq_getdevicelist.htm language=enus -->
## TOPIC 00328: DAQ.GetDeviceList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daq_getdevicelist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daq_getdevicelist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQDevice

DAQ

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDeviceList As DAQDevice() |

| C# |
| --- |
| public DAQDevice[] GetDeviceList() |

| Visual C++ |
| --- |
| public: array<DAQDevice^>^ GetDeviceList() |

###### Return Value

DAQDevice

DAQ

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQ Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginput__ctor.htm language=enus -->
## TOPIC 00329: DAQAnalogInput Constructor (String, String, Double, Double, Double, UInt32, DAQAnalogChannelType)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginput__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginput__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQAnalogInput

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Units As String, _ InitialValue As Double, _ LowLevel As Double, _ HighLevel As Double, _ Channel As UInteger, _ ChannelType As DAQAnalogChannelType _ ) |

| C# |
| --- |
| public DAQAnalogInput( string Name, string Units, double InitialValue, double LowLevel, double HighLevel, uint Channel, DAQAnalogChannelType ChannelType ) |

| Visual C++ |
| --- |
| public: DAQAnalogInput( String^ Name, String^ Units, double InitialValue, double LowLevel, double HighLevel, unsigned int Channel, DAQAnalogChannelType ChannelType ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the analog input channel.

- **Units**
  - Type: System.StringThe units to associate with the analog input channel.

- **InitialValue**
  - Type: System.DoubleThe initial value of the analog input channel.

- **LowLevel**
  - Type: System.DoubleThe minimum value of the analog input channel.

- **HighLevel**
  - Type: System.DoubleThe maximum value of the analog input channel.

- **Channel**
  - Type: System.UInt32The number for the analog input channel.

- **ChannelType**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQAnalogChannelTypeThe DAQAnalogChannelType as Current or Voltage.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

measurementType

DAQMeasurementType

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQAnalogInput Class

DAQAnalogInput Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginput__ctor_3.htm language=enus -->
## TOPIC 00330: DAQAnalogInput Constructor (String, UInt32, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginput__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginput__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQAnalogInput

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ channel As UInteger, _ pluginGUID As String _ ) |

| C# |
| --- |
| public DAQAnalogInput( string name, uint channel, string pluginGUID ) |

| Visual C++ |
| --- |
| public: DAQAnalogInput( String^ name, unsigned int channel, String^ pluginGUID ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the analog input channel.

- **channel**
  - Type: System.UInt32The channel number of the analog input channel.

- **pluginGUID**
  - Type: System.StringThe GUID for the DAQ measurement type plug-in.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

pluginGUID

<GUID>

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](t_nationalinstruments_veristand_systemdefinitionapi_daqmeasurementtype.htm).

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQAnalogInput Class

DAQAnalogInput Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginputs_addwaveformanaloginput.htm language=enus -->
## TOPIC 00331: DAQAnalogInputs.AddWaveformAnalogInput Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginputs_addwaveformanaloginput.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginputs_addwaveformanaloginput.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQWaveformAnalogInput

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddWaveformAnalogInput ( _ waveformAnalogInput As DAQWaveformAnalogInput _ ) As Boolean |

| C# |
| --- |
| public bool AddWaveformAnalogInput( DAQWaveformAnalogInput waveformAnalogInput ) |

| Visual C++ |
| --- |
| public: bool AddWaveformAnalogInput( DAQWaveformAnalogInput^ waveformAnalogInput ) |

###### Parameters

- **waveformAnalogInput**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQWaveformAnalogInputThe DAQWaveformAnalogInput channel to add.

###### Return Value

true

True

DAQWaveformAnalogInput

false

False

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQAnalogInputs Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginputs_getanaloginputlist.htm language=enus -->
## TOPIC 00332: DAQAnalogInputs.GetAnalogInputList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginputs_getanaloginputlist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanaloginputs_getanaloginputlist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQAnalogInput

DAQAnalogInputs

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAnalogInputList As DAQAnalogInput() |

| C# |
| --- |
| public DAQAnalogInput[] GetAnalogInputList() |

| Visual C++ |
| --- |
| public: array<DAQAnalogInput^>^ GetAnalogInputList() |

###### Return Value

DAQAnalogInput

DAQAnalogInputs

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQAnalogInputs Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanalogoutputs_getanalogoutputlist.htm language=enus -->
## TOPIC 00333: DAQAnalogOutputs.GetAnalogOutputList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanalogoutputs_getanalogoutputlist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqanalogoutputs_getanalogoutputlist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQAnalogOutput

DAQAnalogOutputs

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAnalogOutputList As DAQAnalogOutput() |

| C# |
| --- |
| public DAQAnalogOutput[] GetAnalogOutputList() |

| Visual C++ |
| --- |
| public: array<DAQAnalogOutput^>^ GetAnalogOutputList() |

###### Return Value

DAQAnalogOutput

DAQAnalogOutputs

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQAnalogOutputs Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_geti32property.htm language=enus -->
## TOPIC 00334: DAQChannel.GetI32Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_geti32property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_geti32property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetI32Property ( _ propertyName As String, _ <OutAttribute> ByRef value As Integer _ ) |

| C# |
| --- |
| public void GetI32Property( string propertyName, out int value ) |

| Visual C++ |
| --- |
| public: void GetI32Property( String^ propertyName, [OutAttribute] int% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property.

- **value**
  - Type: System.Int32 %The value of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

propertyName

list of DAQ channel properties

This method throws an exception if the propertyName does not exist in the plug-in XML file that defines the measurement type of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_geti64property.htm language=enus -->
## TOPIC 00335: DAQChannel.GetI64Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_geti64property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_geti64property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetI64Property ( _ propertyName As String, _ <OutAttribute> ByRef value As Long _ ) |

| C# |
| --- |
| public void GetI64Property( string propertyName, out long value ) |

| Visual C++ |
| --- |
| public: void GetI64Property( String^ propertyName, [OutAttribute] long long% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property.

- **value**
  - Type: System.Int64 %The value of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

propertyName

list of DAQ channel properties

This method throws an exception if the propertyName does not exist in the plug-in XML file that defines the measurement type of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getproperties.htm language=enus -->
## TOPIC 00336: DAQChannel.GetProperties Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getproperties.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getproperties.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Returns a list of all properties specified by the DAQ plugin for the channel.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetProperties ( _ <OutAttribute> ByRef propertyNames As String(), _ <OutAttribute> ByRef propertyTypes As ValueDataType() _ ) |

| C# |
| --- |
| public void GetProperties( out string[] propertyNames, out ValueDataType[] propertyTypes ) |

| Visual C++ |
| --- |
| public: void GetProperties( [OutAttribute] array<String^>^% propertyNames, [OutAttribute] array<ValueDataType>^% propertyTypes ) |

###### Parameters

- **propertyNames**
  - Type: System.String %The names of the properties.

- **propertyTypes**
  - Type: ValueDataType %An enum defining the data type of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getstringproperty.htm language=enus -->
## TOPIC 00337: DAQChannel.GetStringProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getstringproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getstringproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetStringProperty ( _ propertyName As String, _ <OutAttribute> ByRef value As String _ ) |

| C# |
| --- |
| public void GetStringProperty( string propertyName, out string value ) |

| Visual C++ |
| --- |
| public: void GetStringProperty( String^ propertyName, [OutAttribute] String^% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property.

- **value**
  - Type: System.String %The value of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

propertyName

list of DAQ channel properties

This method throws an exception if the propertyName does not exist in the plug-in XML file that defines the measurement type of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getu64property.htm language=enus -->
## TOPIC 00338: DAQChannel.GetU64Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getu64property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_getu64property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetU64Property ( _ propertyName As String, _ <OutAttribute> ByRef value As ULong _ ) |

| C# |
| --- |
| public void GetU64Property( string propertyName, out ulong value ) |

| Visual C++ |
| --- |
| public: void GetU64Property( String^ propertyName, [OutAttribute] unsigned long long% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property.

- **value**
  - Type: System.UInt64 %The value of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

propertyName

list of DAQ channel properties

This method throws an exception if the propertyName does not exist in the plug-in XML file that defines the measurement type of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_seti16property.htm language=enus -->
## TOPIC 00339: DAQChannel.SetI16Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_seti16property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_seti16property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetI16Property ( _ propertyName As String, _ value As Short _ ) |

| C# |
| --- |
| public void SetI16Property( string propertyName, short value ) |

| Visual C++ |
| --- |
| public: void SetI16Property( String^ propertyName, short value ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property.

- **value**
  - Type: System.Int16The value of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

propertyName

list of DAQ channel properties

This method throws an exception if the propertyName does not exist in the plug-in XML file that defines the measurement type of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_seti64property.htm language=enus -->
## TOPIC 00340: DAQChannel.SetI64Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_seti64property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_seti64property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetI64Property ( _ propertyName As String, _ value As Long _ ) |

| C# |
| --- |
| public void SetI64Property( string propertyName, long value ) |

| Visual C++ |
| --- |
| public: void SetI64Property( String^ propertyName, long long value ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property.

- **value**
  - Type: System.Int64The value of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

propertyName

list of DAQ channel properties

This method throws an exception if the propertyName does not exist in the plug-in XML file that defines the measurement type of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_setu32property.htm language=enus -->
## TOPIC 00341: DAQChannel.SetU32Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_setu32property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqchannel_setu32property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

propertyName

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetU32Property ( _ propertyName As String, _ value As UInteger _ ) |

| C# |
| --- |
| public void SetU32Property( string propertyName, uint value ) |

| Visual C++ |
| --- |
| public: void SetU32Property( String^ propertyName, unsigned int value ) |

###### Parameters

- **propertyName**
  - Type: System.StringThe name of the property.

- **value**
  - Type: System.UInt32The value of the property.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

propertyName

list of DAQ channel properties

This method throws an exception if the propertyName does not exist in the plug-in XML file that defines the measurement type of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor.htm language=enus -->
## TOPIC 00342: DAQCounter Constructor (String, UInt32, DAQMeasurementType)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the DAQCounter class.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ index As UInteger, _ measurementType As DAQMeasurementType _ ) |

| C# |
| --- |
| public DAQCounter( string name, uint index, DAQMeasurementType measurementType ) |

| Visual C++ |
| --- |
| public: DAQCounter( String^ name, unsigned int index, DAQMeasurementType measurementType ) |

###### Parameters

- **name**
  - Type: System.StringThe name of counter.

- **index**
  - Type: System.UInt32The counter index

- **measurementType**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementTypeAn enumeration of DAQMeasurementType.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounter Class

DAQCounter Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_1.htm language=enus -->
## TOPIC 00343: DAQCounter Constructor (String, UInt32, DAQMeasurementType, Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the DAQCounter class.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ index As UInteger, _ measurementType As DAQMeasurementType, _ initialValue As Double _ ) |

| C# |
| --- |
| public DAQCounter( string name, uint index, DAQMeasurementType measurementType, double initialValue ) |

| Visual C++ |
| --- |
| public: DAQCounter( String^ name, unsigned int index, DAQMeasurementType measurementType, double initialValue ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the counter.

- **index**
  - Type: System.UInt32The counter index.

- **measurementType**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementTypeAn enumeration of DAQMeasurementType.

- **initialValue**
  - Type: System.DoubleThe initial value of counter.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounter Class

DAQCounter Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_2.htm language=enus -->
## TOPIC 00344: DAQCounter Constructor (String, UInt32, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the DAQCounter class.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ index As UInteger, _ pluginGUID As String _ ) |

| C# |
| --- |
| public DAQCounter( string name, uint index, string pluginGUID ) |

| Visual C++ |
| --- |
| public: DAQCounter( String^ name, unsigned int index, String^ pluginGUID ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the counter.

- **index**
  - Type: System.UInt32The counter index.

- **pluginGUID**
  - Type: System.StringThe GUID for the DAQ measurement type plug-in.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

pluginGUID

<GUID>

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](t_nationalinstruments_veristand_systemdefinitionapi_daqmeasurementtype.htm).

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounter Class

DAQCounter Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_3.htm language=enus -->
## TOPIC 00345: DAQCounter Constructor (String, UInt32, String, Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the DAQCounter class.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ index As UInteger, _ pluginGUID As String, _ initialValue As Double _ ) |

| C# |
| --- |
| public DAQCounter( string name, uint index, string pluginGUID, double initialValue ) |

| Visual C++ |
| --- |
| public: DAQCounter( String^ name, unsigned int index, String^ pluginGUID, double initialValue ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the counter.

- **index**
  - Type: System.UInt32The counter index.

- **pluginGUID**
  - Type: System.StringThe GUID for the DAQ measurement type plug-in.

- **initialValue**
  - Type: System.DoubleThe initial value of the counter.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

pluginGUID

<GUID>

To create a channel with a measurement type built into NI VeriStand, National Instruments recommends that you use a version of this constructor that contains the *measurementType* parameter, which allows you to specify an enumeration of [DAQMeasurementType](t_nationalinstruments_veristand_systemdefinitionapi_daqmeasurementtype.htm).

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounter Class

DAQCounter Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter_downcast.htm language=enus -->
## TOPIC 00346: DAQCounter.Downcast Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter_downcast.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter_downcast.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQCounter

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function Downcast As DAQCounter |

| C# |
| --- |
| public DAQCounter Downcast() |

| Visual C++ |
| --- |
| public: DAQCounter^ Downcast() |

###### Return Value

DAQCounter

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounter Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter_setcounterindex.htm language=enus -->
## TOPIC 00347: DAQCounter.SetCounterIndex Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter_setcounterindex.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounter_setcounterindex.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the index value of the counter.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function SetCounterIndex ( _ Index As UInteger _ ) As Boolean |

| C# |
| --- |
| public bool SetCounterIndex( uint Index ) |

| Visual C++ |
| --- |
| public: bool SetCounterIndex( unsigned int Index ) |

###### Parameters

- **Index**
  - Type: System.UInt32The index value of the channel.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounter Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_addcounterinput.htm language=enus -->
## TOPIC 00348: DAQCounters.AddCounterInput Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_addcounterinput.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_addcounterinput.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQCounterInput

Counter

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddCounterInput ( _ counter As DAQCounterInput _ ) As Boolean |

| C# |
| --- |
| public bool AddCounterInput( DAQCounterInput counter ) |

| Visual C++ |
| --- |
| public: bool AddCounterInput( DAQCounterInput^ counter ) |

###### Parameters

- **counter**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterInputThe DAQCounter to add.

###### Return Value

true

True

DAQCounter

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounters Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_addcounteroutput.htm language=enus -->
## TOPIC 00349: DAQCounters.AddCounterOutput Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_addcounteroutput.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_addcounteroutput.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQCounterOutput

Counter

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddCounterOutput ( _ counter As DAQCounterOutput _ ) As Boolean |

| C# |
| --- |
| public bool AddCounterOutput( DAQCounterOutput counter ) |

| Visual C++ |
| --- |
| public: bool AddCounterOutput( DAQCounterOutput^ counter ) |

###### Parameters

- **counter**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQCounterOutputThe DAQCounter to add.

###### Return Value

true

True

DAQCounter

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounters Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_finalize.htm language=enus -->
## TOPIC 00350: DAQCounters.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounters Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_getcounterinputs.htm language=enus -->
## TOPIC 00351: DAQCounters.GetCounterInputs Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_getcounterinputs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_getcounterinputs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQCounterInput

DAQCounters

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetCounterInputs As DAQCounterInput() |

| C# |
| --- |
| public DAQCounterInput[] GetCounterInputs() |

| Visual C++ |
| --- |
| public: array<DAQCounterInput^>^ GetCounterInputs() |

###### Return Value

DAQCounterInput

DAQCounters

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounters Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_getcounteroutputs.htm language=enus -->
## TOPIC 00352: DAQCounters.GetCounterOutputs Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_getcounteroutputs.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcounters_getcounteroutputs.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQCounterOutput

DAQCounters

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetCounterOutputs As DAQCounterOutput() |

| C# |
| --- |
| public DAQCounterOutput[] GetCounterOutputs() |

| Visual C++ |
| --- |
| public: array<DAQCounterOutput^>^ GetCounterOutputs() |

###### Return Value

DAQCounterOutput

DAQCounters

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCounters Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcountupdown_finalize.htm language=enus -->
## TOPIC 00353: DAQCountUpDown.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcountupdown_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqcountupdown_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQCountUpDown Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice__ctor.htm language=enus -->
## TOPIC 00354: DAQDevice Constructor (String, String, DAQDeviceInputConfiguration)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQDevice

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ InputConfiguration As DAQDeviceInputConfiguration _ ) |

| C# |
| --- |
| public DAQDevice( string Name, string Description, DAQDeviceInputConfiguration InputConfiguration ) |

| Visual C++ |
| --- |
| public: DAQDevice( String^ Name, String^ Description, DAQDeviceInputConfiguration InputConfiguration ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the device.

- **Description**
  - Type: System.StringThe description of the device.

- **InputConfiguration**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDeviceInputConfigurationThe input terminal configuration.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDevice Class

DAQDevice Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_finalize.htm language=enus -->
## TOPIC 00355: DAQDevice.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getanalogoutputsection.htm language=enus -->
## TOPIC 00356: DAQDevice.GetAnalogOutputSection Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getanalogoutputsection.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getanalogoutputsection.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQAnalogOutputs

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAnalogOutputSection As DAQAnalogOutputs |

| C# |
| --- |
| public DAQAnalogOutputs GetAnalogOutputSection() |

| Visual C++ |
| --- |
| public: DAQAnalogOutputs^ GetAnalogOutputSection() |

###### Return Value

DAQAnalogOutputs

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getdigitalinputsection.htm language=enus -->
## TOPIC 00357: DAQDevice.GetDigitalInputSection Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getdigitalinputsection.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getdigitalinputsection.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQDigitalInputs

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDigitalInputSection As DAQDigitalInputs |

| C# |
| --- |
| public DAQDigitalInputs GetDigitalInputSection() |

| Visual C++ |
| --- |
| public: DAQDigitalInputs^ GetDigitalInputSection() |

###### Return Value

DAQDigitalInputs

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getdigitaloutputsection.htm language=enus -->
## TOPIC 00358: DAQDevice.GetDigitalOutputSection Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getdigitaloutputsection.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_getdigitaloutputsection.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQDigitalOutputs

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDigitalOutputSection As DAQDigitalOutputs |

| C# |
| --- |
| public DAQDigitalOutputs GetDigitalOutputSection() |

| Visual C++ |
| --- |
| public: DAQDigitalOutputs^ GetDigitalOutputSection() |

###### Return Value

DAQDigitalOutputs

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDevice Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_populatedevice.htm language=enus -->
## TOPIC 00359: DAQDevice.PopulateDevice Method (UInt32, UInt32, UInt32, UInt32, UInt32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_populatedevice.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdevice_populatedevice.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Removes all existing channels from the DAQ device and repopulates the device with the specified channels.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub PopulateDevice ( _ NumAIChannels As UInteger, _ NumAOChannels As UInteger, _ NumDIChannels As UInteger, _ NumDOChannels As UInteger, _ PortWidth As UInteger _ ) |

| C# |
| --- |
| public void PopulateDevice( uint NumAIChannels, uint NumAOChannels, uint NumDIChannels, uint NumDOChannels, uint PortWidth ) |

| Visual C++ |
| --- |
| public: void PopulateDevice( unsigned int NumAIChannels, unsigned int NumAOChannels, unsigned int NumDIChannels, unsigned int NumDOChannels, unsigned int PortWidth ) |

###### Parameters

- **NumAIChannels**
  - Type: System.UInt32The number of analog input channels.

- **NumAOChannels**
  - Type: System.UInt32The number of analog output channels.

- **NumDIChannels**
  - Type: System.UInt32The number of digital input channels.

- **NumDOChannels**
  - Type: System.UInt32The number of digital output channels.

- **PortWidth**
  - Type: System.UInt32The total number of lines per port.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDevice Class

PopulateDevice Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdigitalinputs_adddioport.htm language=enus -->
## TOPIC 00360: DAQDigitalInputs.AddDIOPort Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdigitalinputs_adddioport.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdigitalinputs_adddioport.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQDIOPort

Digital Input

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddDIOPort ( _ dioPort As DAQDIOPort _ ) As Boolean |

| C# |
| --- |
| public bool AddDIOPort( DAQDIOPort dioPort ) |

| Visual C++ |
| --- |
| public: bool AddDIOPort( DAQDIOPort^ dioPort ) |

###### Parameters

- **dioPort**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQDIOPortThe DIO port to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDigitalInputs Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdigitalinputs_getdioports.htm language=enus -->
## TOPIC 00361: DAQDigitalInputs.GetDIOPorts Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdigitalinputs_getdioports.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqdigitalinputs_getdioports.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQDIOPort

DAQDigitalInputs

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDIOPorts As DAQDIOPort() |

| C# |
| --- |
| public DAQDIOPort[] GetDIOPorts() |

| Visual C++ |
| --- |
| public: array<DAQDIOPort^>^ GetDIOPorts() |

###### Return Value

DAQDIOPort

DAQDigitalInputs

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQDigitalInputs Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqfrequencymeasurement_finalize.htm language=enus -->
## TOPIC 00362: DAQFrequencyMeasurement.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqfrequencymeasurement_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqfrequencymeasurement_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQFrequencyMeasurement Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqlogging_getloggingenabledchannel.htm language=enus -->
## TOPIC 00363: DAQLogging.GetLoggingEnabledChannel Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqlogging_getloggingenabledchannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqlogging_getloggingenabledchannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQTaskAI

LoggingEnabled

true

True

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetLoggingEnabledChannel As DAQTaskCommand |

| C# |
| --- |
| public DAQTaskCommand GetLoggingEnabledChannel() |

| Visual C++ |
| --- |
| public: DAQTaskCommand^ GetLoggingEnabledChannel() |

###### Return Value

DAQTaskCommand

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQLogging Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpositionmeasurement_finalize.htm language=enus -->
## TOPIC 00364: DAQPositionMeasurement.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpositionmeasurement_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpositionmeasurement_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQPositionMeasurement Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpulsegeneration_initchannels.htm language=enus -->
## TOPIC 00365: DAQPulseGeneration.InitChannels Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpulsegeneration_initchannels.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpulsegeneration_initchannels.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initialize the data channels array.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Function InitChannels As Channel() |

| C# |
| --- |
| protected override Channel[] InitChannels() |

| Visual C++ |
| --- |
| protected: virtual array<Channel^>^ InitChannels() override |

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQPulseGeneration Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpulsemeasurement_setcounterindex.htm language=enus -->
## TOPIC 00366: DAQPulseMeasurement.SetCounterIndex Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpulsemeasurement_setcounterindex.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqpulsemeasurement_setcounterindex.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the index value of the counter.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetCounterIndex ( _ index As UInteger _ ) |

| C# |
| --- |
| public void SetCounterIndex( uint index ) |

| Visual C++ |
| --- |
| public: void SetCounterIndex( unsigned int index ) |

###### Parameters

- **index**
  - Type: System.UInt32The index value of the channel.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQPulseMeasurement Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_getdoubleproperty.htm language=enus -->
## TOPIC 00367: DAQSectionType.GetDoubleProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_getdoubleproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_getdoubleproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetDoubleProperty ( _ propertyName As String, _ <OutAttribute> ByRef value As Double _ ) |

| C# |
| --- |
| public void GetDoubleProperty( string propertyName, out double value ) |

| Visual C++ |
| --- |
| public: void GetDoubleProperty( String^ propertyName, [OutAttribute] double% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.Double %Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQSectionType Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_resetpropertyvalues.htm language=enus -->
## TOPIC 00368: DAQSectionType.ResetPropertyValues Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_resetpropertyvalues.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_resetpropertyvalues.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Reset all properties specified in the DAQ Plugin XML to their defaults.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ResetPropertyValues |

| C# |
| --- |
| public void ResetPropertyValues() |

| Visual C++ |
| --- |
| public: void ResetPropertyValues() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQSectionType Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setdoubleproperty.htm language=enus -->
## TOPIC 00369: DAQSectionType.SetDoubleProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setdoubleproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setdoubleproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Set value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetDoubleProperty ( _ propertyName As String, _ value As Double _ ) |

| C# |
| --- |
| public void SetDoubleProperty( string propertyName, double value ) |

| Visual C++ |
| --- |
| public: void SetDoubleProperty( String^ propertyName, double value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.DoubleValue of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQSectionType Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setenumproperty.htm language=enus -->
## TOPIC 00370: DAQSectionType.SetEnumProperty Method (String, Int32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setenumproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setenumproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Set value of a property of type enum specified by propertyName. Enum is specified by integer value. Throws exception if property 
 of this type does not exist in the Plugin XML, or if value is an invalid enumeration.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetEnumProperty ( _ propertyName As String, _ value As Integer _ ) |

| C# |
| --- |
| public void SetEnumProperty( string propertyName, int value ) |

| Visual C++ |
| --- |
| public: void SetEnumProperty( String^ propertyName, int value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.Int32Integer value of enum

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQSectionType Class

SetEnumProperty Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setenumproperty_1.htm language=enus -->
## TOPIC 00371: DAQSectionType.SetEnumProperty Method (String, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setenumproperty_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setenumproperty_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Set value of a property of type enum specified by propertyName. Enum is specified by a string. Throws exception if property 
 of this type does not exist in the Plugin XML, or if enumString is an invalid enumeration.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetEnumProperty ( _ propertyName As String, _ enumString As String _ ) |

| C# |
| --- |
| public void SetEnumProperty( string propertyName, string enumString ) |

| Visual C++ |
| --- |
| public: void SetEnumProperty( String^ propertyName, String^ enumString ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **enumString**
  - Type: System.StringValue of enum as a string

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQSectionType Class

SetEnumProperty Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setu32property.htm language=enus -->
## TOPIC 00372: DAQSectionType.SetU32Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setu32property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setu32property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Set value of a property of type U32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetU32Property ( _ propertyName As String, _ value As UInteger _ ) |

| C# |
| --- |
| public void SetU32Property( string propertyName, uint value ) |

| Visual C++ |
| --- |
| public: void SetU32Property( String^ propertyName, unsigned int value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.UInt32Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQSectionType Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setu64property.htm language=enus -->
## TOPIC 00373: DAQSectionType.SetU64Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setu64property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqsectiontype_setu64property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Set value of a property of type U64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetU64Property ( _ propertyName As String, _ value As ULong _ ) |

| C# |
| --- |
| public void SetU64Property( string propertyName, ulong value ) |

| Visual C++ |
| --- |
| public: void SetU64Property( String^ propertyName, unsigned long long value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.UInt64Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQSectionType Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtasks_reordertasklist.htm language=enus -->
## TOPIC 00374: DAQTasks.ReorderTaskList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtasks_reordertasklist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtasks_reordertasklist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQTask

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function ReorderTaskList ( _ tasks As DAQTask() _ ) As Boolean |

| C# |
| --- |
| public bool ReorderTaskList( DAQTask[] tasks ) |

| Visual C++ |
| --- |
| public: bool ReorderTaskList( array<DAQTask^>^ tasks ) |

###### Parameters

- **tasks**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQTask An array of DAQTask objects in the order you want the VeriStand Engine to start them.

###### Return Value

true

True

DAQTask

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

Setting the execution order for tasks is useful if you want to synchronize the start of multiple tasks that are triggered off of each other.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQTasks Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggeranalogedge__ctor.htm language=enus -->
## TOPIC 00375: DAQTriggerAnalogEdge Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggeranalogedge__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggeranalogedge__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQTriggerAnalogEdge

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ source As String, _ slope As DirectionType, _ level As Double _ ) |

| C# |
| --- |
| public DAQTriggerAnalogEdge( string source, DirectionType slope, double level ) |

| Visual C++ |
| --- |
| public: DAQTriggerAnalogEdge( String^ source, DirectionType slope, double level ) |

###### Parameters

- **source**
  - Type: System.StringThe name of a virtual channel or terminal that is the source of the analog signal used as the trigger. For E Series DAQ devices, if you specify a channel name as source, the channel must be the first channel in the task. Also, the only terminal you can use for E Series devices is PFI0.

- **slope**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DirectionTypeA DirectionType value that specifies the direction of a signal slope that causes a trigger when the signal crosses the threshold level.

- **level**
  - Type: System.DoubleThe threshold value, in the units of the measurement, at which to start acquiring samples. Set the slope to specify on which type of slope the level causes the task to start acquiring data.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQTriggerAnalogEdge Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggeranalogwindow__ctor.htm language=enus -->
## TOPIC 00376: DAQTriggerAnalogWindow Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggeranalogwindow__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggeranalogwindow__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQTriggerAnalogWindow

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ source As String, _ windowTop As Double, _ windowBottom As Double, _ windowCondition As WindowConditionType _ ) |

| C# |
| --- |
| public DAQTriggerAnalogWindow( string source, double windowTop, double windowBottom, WindowConditionType windowCondition ) |

| Visual C++ |
| --- |
| public: DAQTriggerAnalogWindow( String^ source, double windowTop, double windowBottom, WindowConditionType windowCondition ) |

###### Parameters

- **source**
  - Type: System.StringThe name of a virtual channel or terminal that is the source of the analog signal used as the trigger. For E Series DAQ devices, if you specify a channel name as source, the channel must be the first channel in the task. Also, the only terminal you can use for E Series devices is PFI0.

- **windowTop**
  - Type: System.DoubleThe upper limit of the window, in the units of the measurement.

- **windowBottom**
  - Type: System.DoubleThe lower limit of the window, in the units of the measurement.

- **windowCondition**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.WindowConditionTypeA WindowConditionType value that specifies whether the task starts acquiring samples when the signal enters the window between windowBottom and windowTop or when it leaves the window.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQTriggerAnalogWindow Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggerdigitaledge__ctor.htm language=enus -->
## TOPIC 00377: DAQTriggerDigitalEdge Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggerdigitaledge__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggerdigitaledge__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQTriggerDigitalEdge

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ source As String, _ edge As DirectionType _ ) |

| C# |
| --- |
| public DAQTriggerDigitalEdge( string source, DirectionType edge ) |

| Visual C++ |
| --- |
| public: DAQTriggerDigitalEdge( String^ source, DirectionType edge ) |

###### Parameters

- **source**
  - Type: System.StringThe name of a terminal that is the source of the digital signal used as the trigger.

- **edge**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DirectionTypeA DirectionType value that specifies on which edge of the digital signal to start acquiring samples.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQTriggerDigitalEdge Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggernone__ctor.htm language=enus -->
## TOPIC 00378: DAQTriggerNone Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggernone__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggernone__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQTriggerNone

StartTrigger

ReferenceTrigger

DAQTriggerNone

DAQTaskAI

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public DAQTriggerNone() |

| Visual C++ |
| --- |
| public: DAQTriggerNone() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQTriggerNone Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggersoftware__ctor.htm language=enus -->
## TOPIC 00379: DAQTriggerSoftware Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggersoftware__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqtriggersoftware__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DAQTriggerSoftware

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public DAQTriggerSoftware() |

| Visual C++ |
| --- |
| public: DAQTriggerSoftware() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQTriggerSoftware Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform__ctor.htm language=enus -->
## TOPIC 00380: DAQWaveform Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the DAQWaveform class, with default properties from the DAQPlugin XML specified by the pluginGUID

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Friend Sub New ( _ name As String, _ pluginGUID As String, _ waveformGUID As String _ ) |

| C# |
| --- |
| protected internal DAQWaveform( string name, string pluginGUID, string waveformGUID ) |

| Visual C++ |
| --- |
| protected public: DAQWaveform( String^ name, String^ pluginGUID, String^ waveformGUID ) |

###### Parameters

- **name**
  - Type: System.StringName of Channel

- **pluginGUID**
  - Type: System.StringGUID specifying the DAQ Plugin/Measurement Type

- **waveformGUID**
  - Type: System.StringGUID specifying Waveform type. Used to verify if specified Plugin is valid for this channel type

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getbooleanproperty.htm language=enus -->
## TOPIC 00381: DAQWaveform.GetBooleanProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getbooleanproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getbooleanproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Get value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetBooleanProperty ( _ propertyName As String, _ <OutAttribute> ByRef value As Boolean _ ) |

| C# |
| --- |
| public void GetBooleanProperty( string propertyName, out bool value ) |

| Visual C++ |
| --- |
| public: void GetBooleanProperty( String^ propertyName, [OutAttribute] bool% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.Boolean %Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getdoubleproperty.htm language=enus -->
## TOPIC 00382: DAQWaveform.GetDoubleProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getdoubleproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getdoubleproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Get value of a property of type double specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetDoubleProperty ( _ propertyName As String, _ <OutAttribute> ByRef value As Double _ ) |

| C# |
| --- |
| public void GetDoubleProperty( string propertyName, out double value ) |

| Visual C++ |
| --- |
| public: void GetDoubleProperty( String^ propertyName, [OutAttribute] double% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.Double %Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getenumproperty.htm language=enus -->
## TOPIC 00383: DAQWaveform.GetEnumProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getenumproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_getenumproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Get value of a property of type enum specified by propertyName. This gets the enum value as a string as well as the underlying integer value. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetEnumProperty ( _ propertyName As String, _ <OutAttribute> ByRef enumString As String, _ <OutAttribute> ByRef enumValue As Integer _ ) |

| C# |
| --- |
| public void GetEnumProperty( string propertyName, out string enumString, out int enumValue ) |

| Visual C++ |
| --- |
| public: void GetEnumProperty( String^ propertyName, [OutAttribute] String^% enumString, [OutAttribute] int% enumValue ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **enumString**
  - Type: System.String %String value of the enum

- **enumValue**
  - Type: System.Int32 % Integer value of the enum

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti16property.htm language=enus -->
## TOPIC 00384: DAQWaveform.GetI16Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti16property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti16property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Get value of a property of type I16 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetI16Property ( _ propertyName As String, _ <OutAttribute> ByRef value As Short _ ) |

| C# |
| --- |
| public void GetI16Property( string propertyName, out short value ) |

| Visual C++ |
| --- |
| public: void GetI16Property( String^ propertyName, [OutAttribute] short% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.Int16 %Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti32property.htm language=enus -->
## TOPIC 00385: DAQWaveform.GetI32Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti32property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti32property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Get value of a property of type I32 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetI32Property ( _ propertyName As String, _ <OutAttribute> ByRef value As Integer _ ) |

| C# |
| --- |
| public void GetI32Property( string propertyName, out int value ) |

| Visual C++ |
| --- |
| public: void GetI32Property( String^ propertyName, [OutAttribute] int% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.Int32 %Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti64property.htm language=enus -->
## TOPIC 00386: DAQWaveform.GetI64Property Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti64property.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_geti64property.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Get value of a property of type I64 specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub GetI64Property ( _ propertyName As String, _ <OutAttribute> ByRef value As Long _ ) |

| C# |
| --- |
| public void GetI64Property( string propertyName, out long value ) |

| Visual C++ |
| --- |
| public: void GetI64Property( String^ propertyName, [OutAttribute] long long% value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.Int64 %Value of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_resetpropertyvalues.htm language=enus -->
## TOPIC 00387: DAQWaveform.ResetPropertyValues Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_resetpropertyvalues.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_resetpropertyvalues.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Reset all properties specified in the DAQ Plugin XML to their defaults.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ResetPropertyValues |

| C# |
| --- |
| public void ResetPropertyValues() |

| Visual C++ |
| --- |
| public: void ResetPropertyValues() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_setbooleanproperty.htm language=enus -->
## TOPIC 00388: DAQWaveform.SetBooleanProperty Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_setbooleanproperty.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveform_setbooleanproperty.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Set value of a property of type Boolean specified by propertyName. Throws exception if property of this type does not exist in the Plugin XML.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetBooleanProperty ( _ propertyName As String, _ value As Boolean _ ) |

| C# |
| --- |
| public void SetBooleanProperty( string propertyName, bool value ) |

| Visual C++ |
| --- |
| public: void SetBooleanProperty( String^ propertyName, bool value ) |

###### Parameters

- **propertyName**
  - Type: System.StringName of Property

- **value**
  - Type: System.BooleanValue of property

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveform Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveformanaloginput__ctor.htm language=enus -->
## TOPIC 00389: DAQWaveformAnalogInput Constructor (String, UInt32, DAQMeasurementType)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveformanaloginput__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_daqwaveformanaloginput__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the DAQWaveformAnalogInput class.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ channel As UInteger, _ measurementType As DAQMeasurementType _ ) |

| C# |
| --- |
| public DAQWaveformAnalogInput( string name, uint channel, DAQMeasurementType measurementType ) |

| Visual C++ |
| --- |
| public: DAQWaveformAnalogInput( String^ name, unsigned int channel, DAQMeasurementType measurementType ) |

###### Parameters

- **name**
  - Type: System.StringName of AI Channel

- **channel**
  - Type: System.UInt32Channel Number of Analog Input

- **measurementType**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DAQMeasurementTypeDAQ Measurement Type

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DAQWaveformAnalogInput Class

DAQWaveformAnalogInput Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay__ctor.htm language=enus -->
## TOPIC 00390: DataFileReplay Constructor (String, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataFileReplay

.ncl

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Path As String _ ) |

| C# |
| --- |
| public DataFileReplay( string Name, string Path ) |

| Visual C++ |
| --- |
| public: DataFileReplay( String^ Name, String^ Path ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the data replay file to access.

- **Path**
  - Type: System.StringThe path to the data replay file on disk.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataFileReplay Class

DataFileReplay Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay__ctor_1.htm language=enus -->
## TOPIC 00391: DataFileReplay Constructor (String, String, String, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataFileReplay

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Path As String, _ TDMSGroupName As String, _ TDMSChannelName As String _ ) |

| C# |
| --- |
| public DataFileReplay( string Name, string Path, string TDMSGroupName, string TDMSChannelName ) |

| Visual C++ |
| --- |
| public: DataFileReplay( String^ Name, String^ Path, String^ TDMSGroupName, String^ TDMSChannelName ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the data replay file to access.

- **Path**
  - Type: System.StringThe path to the data replay file on disk.

- **TDMSGroupName**
  - Type: System.StringThe name of the group in the TDMS file that contains the logged data.

- **TDMSChannelName**
  - Type: System.StringThe name of the channel in the TDMS file that contains the logged data.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataFileReplay Class

DataFileReplay Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay_getdatafileerror.htm language=enus -->
## TOPIC 00392: DataFileReplay.GetDataFileError Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay_getdatafileerror.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay_getdatafileerror.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataFileError

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDataFileError As DataFileError |

| C# |
| --- |
| public DataFileError GetDataFileError() |

| Visual C++ |
| --- |
| public: DataFileError^ GetDataFileError() |

###### Return Value

DataFileError

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataFileReplay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay_getdatafilestatus.htm language=enus -->
## TOPIC 00393: DataFileReplay.GetDataFileStatus Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay_getdatafilestatus.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilereplay_getdatafilestatus.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataFileStatus

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDataFileStatus As DataFileStatus |

| C# |
| --- |
| public DataFileStatus GetDataFileStatus() |

| Visual C++ |
| --- |
| public: DataFileStatus^ GetDataFileStatus() |

###### Return Value

DataFileStatus

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataFileReplay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilestatus_finalize.htm language=enus -->
## TOPIC 00394: DataFileStatus.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilestatus_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datafilestatus_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataFileStatus Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile__ctor.htm language=enus -->
## TOPIC 00395: DataLoggingFile Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataLoggingFile

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Filename As String, _ Destination As String _ ) |

| C# |
| --- |
| public DataLoggingFile( string Name, string Filename, string Destination ) |

| Visual C++ |
| --- |
| public: DataLoggingFile( String^ Name, String^ Filename, String^ Destination ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the data logging file, as it appears in the system definition.

- **Filename**
  - Type: System.StringThe filename of the data logging file.

- **Destination**
  - Type: System.StringThe destination for the data logging file on disk.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataLoggingFile Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile_finalize.htm language=enus -->
## TOPIC 00396: DataLoggingFile.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataLoggingFile Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile_getdatafilestatus.htm language=enus -->
## TOPIC 00397: DataLoggingFile.GetDataFileStatus Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile_getdatafilestatus.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dataloggingfile_getdatafilestatus.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataFileStatus

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDataFileStatus As DataFileStatus |

| C# |
| --- |
| public DataFileStatus GetDataFileStatus() |

| Visual C++ |
| --- |
| public: DataFileStatus^ GetDataFileStatus() |

###### Return Value

DataFileStatus

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataLoggingFile Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_adddatafilereplay.htm language=enus -->
## TOPIC 00398: DataReplay.AddDataFileReplay Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_adddatafilereplay.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_adddatafilereplay.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds the specified data replay file.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddDataFileReplay ( _ dataFileReplay As DataFileReplay _ ) As Boolean |

| C# |
| --- |
| public bool AddDataFileReplay( DataFileReplay dataFileReplay ) |

| Visual C++ |
| --- |
| public: bool AddDataFileReplay( DataFileReplay^ dataFileReplay ) |

###### Parameters

- **dataFileReplay**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DataFileReplaySpecifies the data replay file to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataReplay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_finalize.htm language=enus -->
## TOPIC 00399: DataReplay.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataReplay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_getdatafilereplaylist.htm language=enus -->
## TOPIC 00400: DataReplay.GetDataFileReplayList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_getdatafilereplaylist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datareplay_getdatafilereplaylist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataFileReplay

DataReplay

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDataFileReplayList As DataFileReplay() |

| C# |
| --- |
| public DataFileReplay[] GetDataFileReplayList() |

| Visual C++ |
| --- |
| public: array<DataFileReplay^>^ GetDataFileReplayList() |

###### Return Value

DataFileReplay

DataReplay

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataReplay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datasharing_addreflectivememory.htm language=enus -->
## TOPIC 00401: DataSharing.AddReflectiveMemory Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datasharing_addreflectivememory.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datasharing_addreflectivememory.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds the specified reflective memory device.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddReflectiveMemory ( _ Name As String _ ) As Boolean |

| C# |
| --- |
| public bool AddReflectiveMemory( string Name ) |

| Visual C++ |
| --- |
| public: bool AddReflectiveMemory( String^ Name ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the reflective memory device.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataSharing Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datasharingnetwork_finalize.htm language=enus -->
## TOPIC 00402: DataSharingNetwork.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datasharingnetwork_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_datasharingnetwork_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DataSharingNetwork Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile__ctor.htm language=enus -->
## TOPIC 00403: DependentFile Constructor (String, DependentFileType, String, Boolean, String, String, String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DependentFile

FilePath

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ FilePath As String, _ Type As DependentFileType, _ Version As String, _ ForceDownload As Boolean, _ RTDestination As String, _ SupportedTarget As String, _ MD5 As String _ ) |

| C# |
| --- |
| public DependentFile( string FilePath, DependentFileType Type, string Version, bool ForceDownload, string RTDestination, string SupportedTarget, string MD5 ) |

| Visual C++ |
| --- |
| public: DependentFile( String^ FilePath, DependentFileType Type, String^ Version, bool ForceDownload, String^ RTDestination, String^ SupportedTarget, String^ MD5 ) |

###### Parameters

- **FilePath**
  - Type: System.StringThe path to the file on the host.

- **Type**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.DependentFileTypeThe DependentFileType used for the FilePath.

- **Version**
  - Type: System.StringAn arbitrary string to store with the file. You can use this parameter to store version information with the file.

- **ForceDownload**
  - Type: System.BooleanIf true (True in Visual Basic), specifies to force-download the file to the target when you deploy the system definition.

- **RTDestination**
  - Type: System.StringThe destination path, including the filename, for the file on the target. This must be an absolute path.

- **SupportedTarget**
  - Type: System.Stringthe target operating system(s) to which the file is deployed. Standard values include All, PharLap, VxWorks, Windows, PharLap & Windows, PharLap & VxWorks, and VxWorks & Windows.

- **MD5**
  - Type: System.StringThe MD5 message-digest for the file.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DependentFile Class

DependentFile Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile_getabsolutepath.htm language=enus -->
## TOPIC 00404: DependentFile.GetAbsolutePath Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile_getabsolutepath.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile_getabsolutepath.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

baseAbsolutePath

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAbsolutePath ( _ baseAbsolutePath As String _ ) As String |

| C# |
| --- |
| public string GetAbsolutePath( string baseAbsolutePath ) |

| Visual C++ |
| --- |
| public: String^ GetAbsolutePath( String^ baseAbsolutePath ) |

###### Parameters

- **baseAbsolutePath**
  - Type: System.StringThe base path to append to the path to the file to form the absolute bath.

###### Return Value

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DependentFile Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile_setpath.htm language=enus -->
## TOPIC 00405: DependentFile.SetPath Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile_setpath.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dependentfile_setpath.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DependentFile

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetPath ( _ FilePath As String, _ SDFPath As String _ ) |

| C# |
| --- |
| public void SetPath( string FilePath, string SDFPath ) |

| Visual C++ |
| --- |
| public: void SetPath( String^ FilePath, String^ SDFPath ) |

###### Parameters

- **FilePath**
  - Type: System.StringThe path to the DependentFile.

- **SDFPath**
  - Type: System.StringThe path to the system definition file that requires the DependentFile.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DependentFile Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addbooleanarray.htm language=enus -->
## TOPIC 00406: Dictionary.AddBooleanArray Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addbooleanarray.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addbooleanarray.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds an Boolean array element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddBooleanArray ( _ name As String, _ value As Boolean() _ ) As Boolean |

| C# |
| --- |
| public bool AddBooleanArray( string name, bool[] value ) |

| Visual C++ |
| --- |
| public: bool AddBooleanArray( String^ name, array<bool>^ value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.Boolean The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_adddouble.htm language=enus -->
## TOPIC 00407: Dictionary.AddDouble Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_adddouble.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_adddouble.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds a double-precision floating-point numeric element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddDouble ( _ name As String, _ value As Double _ ) As Boolean |

| C# |
| --- |
| public bool AddDouble( string name, double value ) |

| Visual C++ |
| --- |
| public: bool AddDouble( String^ name, double value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.DoubleThe initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_adddoublearray.htm language=enus -->
## TOPIC 00408: Dictionary.AddDoubleArray Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_adddoublearray.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_adddoublearray.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds a double-precision floating-point numeric array element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddDoubleArray ( _ name As String, _ value As Double() _ ) As Boolean |

| C# |
| --- |
| public bool AddDoubleArray( string name, double[] value ) |

| Visual C++ |
| --- |
| public: bool AddDoubleArray( String^ name, array<double>^ value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.Double The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi16.htm language=enus -->
## TOPIC 00409: Dictionary.AddI16 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi16.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi16.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds a signed 16-bit integer element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddI16 ( _ name As String, _ value As Short _ ) As Boolean |

| C# |
| --- |
| public bool AddI16( string name, short value ) |

| Visual C++ |
| --- |
| public: bool AddI16( String^ name, short value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.Int16The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi16array.htm language=enus -->
## TOPIC 00410: Dictionary.AddI16Array Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi16array.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi16array.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds a signed 16-bit integer array element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddI16Array ( _ name As String, _ value As Short() _ ) As Boolean |

| C# |
| --- |
| public bool AddI16Array( string name, short[] value ) |

| Visual C++ |
| --- |
| public: bool AddI16Array( String^ name, array<short>^ value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.Int16 The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi32.htm language=enus -->
## TOPIC 00411: Dictionary.AddI32 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi32.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi32.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds a signed 32-bit integer element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddI32 ( _ name As String, _ value As Integer _ ) As Boolean |

| C# |
| --- |
| public bool AddI32( string name, int value ) |

| Visual C++ |
| --- |
| public: bool AddI32( String^ name, int value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.Int32The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi32array.htm language=enus -->
## TOPIC 00412: Dictionary.AddI32Array Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi32array.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addi32array.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds a signed 32-bit integer array element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddI32Array ( _ name As String, _ value As Integer() _ ) As Boolean |

| C# |
| --- |
| public bool AddI32Array( string name, int[] value ) |

| Visual C++ |
| --- |
| public: bool AddI32Array( String^ name, array<int>^ value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.Int32 The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addu16array.htm language=enus -->
## TOPIC 00413: Dictionary.AddU16Array Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addu16array.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addu16array.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds an unsigned 16-bit integer array element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddU16Array ( _ name As String, _ value As UShort() _ ) As Boolean |

| C# |
| --- |
| public bool AddU16Array( string name, ushort[] value ) |

| Visual C++ |
| --- |
| public: bool AddU16Array( String^ name, array<unsigned short>^ value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.UInt16 The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addu32.htm language=enus -->
## TOPIC 00414: Dictionary.AddU32 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addu32.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_addu32.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Adds an unsigned 32-bit integer element to the dictionary.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddU32 ( _ name As String, _ value As UInteger _ ) As Boolean |

| C# |
| --- |
| public bool AddU32( string name, uint value ) |

| Visual C++ |
| --- |
| public: bool AddU32( String^ name, unsigned int value ) |

###### Parameters

- **name**
  - Type: System.StringThe name, or key, for the element.

- **value**
  - Type: System.UInt32The initial value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_clear.htm language=enus -->
## TOPIC 00415: Dictionary.Clear Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_clear.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_clear.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Clears the dictionary of all elements.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub Clear |

| C# |
| --- |
| public void Clear() |

| Visual C++ |
| --- |
| public: void Clear() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_geti64.htm language=enus -->
## TOPIC 00416: Dictionary.GetI64 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_geti64.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_geti64.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

name

value

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetI64 ( _ name As String, _ <OutAttribute> ByRef value As Long _ ) As Boolean |

| C# |
| --- |
| public bool GetI64( string name, out long value ) |

| Visual C++ |
| --- |
| public: bool GetI64( String^ name, [OutAttribute] long long% value ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the element.

- **value**
  - Type: System.Int64 %The current value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_getu16.htm language=enus -->
## TOPIC 00417: Dictionary.GetU16 Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_getu16.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dictionary_getu16.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

name

value

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetU16 ( _ name As String, _ <OutAttribute> ByRef value As UShort _ ) As Boolean |

| C# |
| --- |
| public bool GetU16( string name, out ushort value ) |

| Visual C++ |
| --- |
| public: bool GetU16( String^ name, [OutAttribute] unsigned short% value ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the element.

- **value**
  - Type: System.UInt16 %The current value of the element.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dictionary Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell__ctor.htm language=enus -->
## TOPIC 00418: Dwell Constructor (String, String, BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Dwell

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ DwellTime As BaseNode _ ) |

| C# |
| --- |
| public Dwell( string Name, string Description, BaseNode DwellTime ) |

| Visual C++ |
| --- |
| public: Dwell( String^ Name, String^ Description, BaseNode^ DwellTime ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the step.

- **Description**
  - Type: System.StringThe description of the step.

- **DwellTime**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel whose value specifies the amount of time to suspend the procedure.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dwell Class

Dwell Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell_finalize.htm language=enus -->
## TOPIC 00419: Dwell.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dwell Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell_setdwelltime_1.htm language=enus -->
## TOPIC 00420: Dwell.SetDwellTime Method (Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell_setdwelltime_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dwell_setdwelltime_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the amount of time to suspend the procedure using a constant value.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetDwellTime ( _ DwellTime As Double _ ) |

| C# |
| --- |
| public void SetDwellTime( double DwellTime ) |

| Visual C++ |
| --- |
| public: void SetDwellTime( double DwellTime ) |

###### Parameters

- **DwellTime**
  - Type: System.DoubleThe constant value that determines the amount of time to suspend the procedure.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Dwell Class

SetDwellTime Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dynamicsignal_finalize.htm language=enus -->
## TOPIC 00421: DynamicSignal.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dynamicsignal_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_dynamicsignal_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

DynamicSignal Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_finalize.htm language=enus -->
## TOPIC 00422: EventTriggered.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

EventTriggered Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_getrawdatabasedframelist.htm language=enus -->
## TOPIC 00423: EventTriggered.GetRawDataBasedFrameList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_getrawdatabasedframelist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_getrawdatabasedframelist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

RawDataBasedFrame

EventTriggered

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetRawDataBasedFrameList As RawDataBasedFrame() |

| C# |
| --- |
| public RawDataBasedFrame[] GetRawDataBasedFrameList() |

| Visual C++ |
| --- |
| public: array<RawDataBasedFrame^>^ GetRawDataBasedFrameList() |

###### Return Value

RawDataBasedFrame

EventTriggered

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

EventTriggered Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_getsignalbasedframelist.htm language=enus -->
## TOPIC 00424: EventTriggered.GetSignalBasedFrameList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_getsignalbasedframelist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_eventtriggered_getsignalbasedframelist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SignalBasedFrame

EventTriggered

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetSignalBasedFrameList As SignalBasedFrame() |

| C# |
| --- |
| public SignalBasedFrame[] GetSignalBasedFrameList() |

| Visual C++ |
| --- |
| public: array<SignalBasedFrame^>^ GetSignalBasedFrameList() |

###### Return Value

SignalBasedFrame

EventTriggered

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

EventTriggered Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_finalize.htm language=enus -->
## TOPIC 00425: Execution.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Execution Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_getmodelcommand.htm language=enus -->
## TOPIC 00426: Execution.GetModelCommand Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_getmodelcommand.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_getmodelcommand.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ModelCommand

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetModelCommand As ModelCommand |

| C# |
| --- |
| public ModelCommand GetModelCommand() |

| Visual C++ |
| --- |
| public: ModelCommand^ GetModelCommand() |

###### Return Value

ModelCommand

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Execution Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_getmodelstatus.htm language=enus -->
## TOPIC 00427: Execution.GetModelStatus Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_getmodelstatus.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_execution_getmodelstatus.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ModelStatus

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetModelStatus As ModelStatus |

| C# |
| --- |
| public ModelStatus GetModelStatus() |

| Visual C++ |
| --- |
| public: ModelStatus^ GetModelStatus() |

###### Return Value

ModelStatus

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Execution Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_exitsubroutine__ctor.htm language=enus -->
## TOPIC 00428: ExitSubroutine Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_exitsubroutine__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_exitsubroutine__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ExitSubroutine

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String _ ) |

| C# |
| --- |
| public ExitSubroutine( string Name, string Description ) |

| Visual C++ |
| --- |
| public: ExitSubroutine( String^ Name, String^ Description ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the ExitSubroutine step.

- **Description**
  - Type: System.StringThe description of the ExitSubroutine step.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ExitSubroutine Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_exitsubroutine_finalize.htm language=enus -->
## TOPIC 00429: ExitSubroutine.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_exitsubroutine_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_exitsubroutine_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ExitSubroutine Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_finishedfiles_finalize.htm language=enus -->
## TOPIC 00430: FinishedFiles.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_finishedfiles_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_finishedfiles_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FinishedFiles Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_addflexrayport.htm language=enus -->
## TOPIC 00431: FlexRay.AddFlexRayPort Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_addflexrayport.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_addflexrayport.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FlexRayPort

FlexRay

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddFlexRayPort ( _ flexRayPort As FlexRayPort _ ) As Boolean |

| C# |
| --- |
| public bool AddFlexRayPort( FlexRayPort flexRayPort ) |

| Visual C++ |
| --- |
| public: bool AddFlexRayPort( FlexRayPort^ flexRayPort ) |

###### Parameters

- **flexRayPort**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.FlexRayPortThe port to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FlexRay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_finalize.htm language=enus -->
## TOPIC 00432: FlexRay.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FlexRay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_getflexrayportlist.htm language=enus -->
## TOPIC 00433: FlexRay.GetFlexRayPortList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_getflexrayportlist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexray_getflexrayportlist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FlexRayPort

FlexRay

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetFlexRayPortList As FlexRayPort() |

| C# |
| --- |
| public FlexRayPort[] GetFlexRayPortList() |

| Visual C++ |
| --- |
| public: array<FlexRayPort^>^ GetFlexRayPortList() |

###### Return Value

FlexRayPort

FlexRay

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FlexRay Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport__ctor.htm language=enus -->
## TOPIC 00434: FlexRayPort Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FlexRayPort

Name

PortNumber

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ PortNumber As UShort, _ LinkedDatabase As Database, _ ClusterName As String, _ BaudRate As UInteger _ ) |

| C# |
| --- |
| public FlexRayPort( string Name, ushort PortNumber, Database LinkedDatabase, string ClusterName, uint BaudRate ) |

| Visual C++ |
| --- |
| public: FlexRayPort( String^ Name, unsigned short PortNumber, Database^ LinkedDatabase, String^ ClusterName, unsigned int BaudRate ) |

###### Parameters

- **Name**
  - Type: System.String The name of the port.

- **PortNumber**
  - Type: System.UInt16 The physical address of the port.

- **LinkedDatabase**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.Database The XNET database associated with the port.

- **ClusterName**
  - Type: System.String The cluster in LinkedDatabase that is associated with the port.

- **BaudRate**
  - Type: System.UInt32 The baud rate all cluster nodes under the port use. This rate can be 2500000, 5000000, or 10000000.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FlexRayPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_finalize.htm language=enus -->
## TOPIC 00435: FlexRayPort.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FlexRayPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_getincoming.htm language=enus -->
## TOPIC 00436: FlexRayPort.GetIncoming Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_getincoming.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_getincoming.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Incoming

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetIncoming As Incoming |

| C# |
| --- |
| public Incoming GetIncoming() |

| Visual C++ |
| --- |
| public: Incoming^ GetIncoming() |

###### Return Value

Incoming

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FlexRayPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_getoutgoing.htm language=enus -->
## TOPIC 00437: FlexRayPort.GetOutgoing Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_getoutgoing.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_flexrayport_getoutgoing.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Outgoing

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetOutgoing As Outgoing |

| C# |
| --- |
| public Outgoing GetOutgoing() |

| Visual C++ |
| --- |
| public: Outgoing^ GetOutgoing() |

###### Return Value

Outgoing

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FlexRayPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula__ctor.htm language=enus -->
## TOPIC 00438: Formula Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Formula

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ Formula As String, _ VariableNames As String(), _ Variables As BaseNode() _ ) |

| C# |
| --- |
| public Formula( string Name, string Description, string Formula, string[] VariableNames, BaseNode[] Variables ) |

| Visual C++ |
| --- |
| public: Formula( String^ Name, String^ Description, String^ Formula, array<String^>^ VariableNames, array<BaseNode^>^ Variables ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the calculated channel.

- **Description**
  - Type: System.StringThe description of the calculated channel.

- **Formula**
  - Type: System.StringThe formula for which the channel calculates the result.

- **VariableNames**
  - Type: System.String A list of names to display in the formula for the Variables.

- **Variables**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode A list of channels to assign as variables in the formula.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Formula Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_finalize.htm language=enus -->
## TOPIC 00439: Formula.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Formula Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_resetformula.htm language=enus -->
## TOPIC 00440: Formula.ResetFormula Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_resetformula.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_resetformula.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Clears the formula string and removes all variables.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub ResetFormula |

| C# |
| --- |
| public void ResetFormula() |

| Visual C++ |
| --- |
| public: void ResetFormula() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Formula Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_setformula.htm language=enus -->
## TOPIC 00441: Formula.SetFormula Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_setformula.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_formula_setformula.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Sets the formula string and adds the specified variables.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetFormula ( _ Formula As String, _ VariableNames As String(), _ Variables As BaseNode() _ ) |

| C# |
| --- |
| public void SetFormula( string Formula, string[] VariableNames, BaseNode[] Variables ) |

| Visual C++ |
| --- |
| public: void SetFormula( String^ Formula, array<String^>^ VariableNames, array<BaseNode^>^ Variables ) |

###### Parameters

- **Formula**
  - Type: System.StringThe formula for which the channel calculates the result.

- **VariableNames**
  - Type: System.String A list of names to display in the formula for the Variables.

- **Variables**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNode A list of channels to assign as variables in the formula.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Formula Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpga_getfpgadevicelist.htm language=enus -->
## TOPIC 00442: FPGA.GetFPGADeviceList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpga_getfpgadevicelist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpga_getfpgadevicelist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FPGADevice

FPGA

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetFPGADeviceList As FPGADevice() |

| C# |
| --- |
| public FPGADevice[] GetFPGADeviceList() |

| Visual C++ |
| --- |
| public: array<FPGADevice^>^ GetFPGADeviceList() |

###### Return Value

FPGADevice

FPGA

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGA Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgaaicategory_finalize.htm language=enus -->
## TOPIC 00443: FPGAAICategory.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgaaicategory_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgaaicategory_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGAAICategory Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgacategory_getchannellist.htm language=enus -->
## TOPIC 00444: FPGACategory.GetChannelList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgacategory_getchannellist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgacategory_getchannellist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

FPGAChannel

FPGACategory

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetChannelList As FPGAChannel() |

| C# |
| --- |
| public FPGAChannel[] GetChannelList() |

| Visual C++ |
| --- |
| public: array<FPGAChannel^>^ GetChannelList() |

###### Return Value

FPGAChannel

FPGACategory

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGACategory Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadigitalinput_finalize.htm language=enus -->
## TOPIC 00445: FPGADigitalInput.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadigitalinput_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadigitalinput_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGADigitalInput Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadigitaloutput_finalize.htm language=enus -->
## TOPIC 00446: FPGADigitalOutput.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadigitaloutput_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadigitaloutput_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGADigitalOutput Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadocategory_finalize.htm language=enus -->
## TOPIC 00447: FPGADOCategory.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadocategory_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgadocategory_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGADOCategory Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgapwmincategory_finalize.htm language=enus -->
## TOPIC 00448: FPGAPWMInCategory.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgapwmincategory_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgapwmincategory_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGAPWMInCategory Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgapwminput_finalize.htm language=enus -->
## TOPIC 00449: FPGAPWMInput.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgapwminput_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_fpgapwminput_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FPGAPWMInput Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_frameinformation_finalize.htm language=enus -->
## TOPIC 00450: FrameInformation.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_frameinformation_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_frameinformation_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

FrameInformation Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_gotolabel_finalize.htm language=enus -->
## TOPIC 00451: GotoLabel.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_gotolabel_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_gotolabel_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

GotoLabel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_hardware_addchassis.htm language=enus -->
## TOPIC 00452: Hardware.AddChassis Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_hardware_addchassis.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_hardware_addchassis.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Chassis

Hardware

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddChassis ( _ chassis As Chassis _ ) As Boolean |

| C# |
| --- |
| public bool AddChassis( Chassis chassis ) |

| Visual C++ |
| --- |
| public: bool AddChassis( Chassis^ chassis ) |

###### Parameters

- **chassis**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ChassisThe chassis to add.

###### Return Value

true

True

Chassis

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Hardware Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_hardware_addnewchassis.htm language=enus -->
## TOPIC 00453: Hardware.AddNewChassis Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_hardware_addnewchassis.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_hardware_addnewchassis.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Chassis

Hardware

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddNewChassis ( _ Name As String _ ) As Boolean |

| C# |
| --- |
| public bool AddNewChassis( string Name ) |

| Visual C++ |
| --- |
| public: bool AddNewChassis( String^ Name ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the chassis.

###### Return Value

true

True

Chassis

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Hardware Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_incoming_getsinglepoint.htm language=enus -->
## TOPIC 00454: Incoming.GetSinglePoint Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_incoming_getsinglepoint.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_incoming_getsinglepoint.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SinglePoint

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetSinglePoint As SinglePoint |

| C# |
| --- |
| public SinglePoint GetSinglePoint() |

| Visual C++ |
| --- |
| public: SinglePoint^ GetSinglePoint() |

###### Return Value

SinglePoint

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Incoming Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inport_finalize.htm language=enus -->
## TOPIC 00455: Inport.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inport_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inport_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Inport Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inportgroup_getinportgroups.htm language=enus -->
## TOPIC 00456: InportGroup.GetInportGroups Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inportgroup_getinportgroups.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inportgroup_getinportgroups.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

InportGroup

InportGroup

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetInportGroups As InportGroup() |

| C# |
| --- |
| public InportGroup[] GetInportGroups() |

| Visual C++ |
| --- |
| public: array<InportGroup^>^ GetInportGroups() |

###### Return Value

InportGroup

InportGroup

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

InportGroup Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inportgroup_getinports.htm language=enus -->
## TOPIC 00457: InportGroup.GetInports Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inportgroup_getinports.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inportgroup_getinports.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Inport

InportGroup

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetInports As Inport() |

| C# |
| --- |
| public Inport[] GetInports() |

| Visual C++ |
| --- |
| public: array<Inport^>^ GetInports() |

###### Return Value

Inport

InportGroup

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

InportGroup Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inports_getinportgroups.htm language=enus -->
## TOPIC 00458: Inports.GetInportGroups Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inports_getinportgroups.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inports_getinportgroups.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

InportGroup

Inports

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetInportGroups As InportGroup() |

| C# |
| --- |
| public InportGroup[] GetInportGroups() |

| Visual C++ |
| --- |
| public: array<InportGroup^>^ GetInportGroups() |

###### Return Value

InportGroup

Inports

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Inports Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inports_getinports.htm language=enus -->
## TOPIC 00459: Inports.GetInports Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inports_getinports.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_inports_getinports.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Inport

Inports

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetInports As Inport() |

| C# |
| --- |
| public Inport[] GetInports() |

| Visual C++ |
| --- |
| public: array<Inport^>^ GetInports() |

###### Return Value

Inport

Inports

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Inports Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_interfacechannels_finalize.htm language=enus -->
## TOPIC 00460: InterfaceChannels.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_interfacechannels_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_interfacechannels_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

InterfaceChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_interfacechannels_getsleepmodechannel.htm language=enus -->
## TOPIC 00461: InterfaceChannels.GetSleepModeChannel Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_interfacechannels_getsleepmodechannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_interfacechannels_getsleepmodechannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Transceiver State

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetSleepModeChannel As SleepMode |

| C# |
| --- |
| public SleepMode GetSleepModeChannel() |

| Visual C++ |
| --- |
| public: SleepMode^ GetSleepModeChannel() |

###### Return Value

SleepMode

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

InterfaceChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lin_addlinport.htm language=enus -->
## TOPIC 00462: LIN.AddLINPort Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lin_addlinport.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lin_addlinport.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LIN

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddLINPort ( _ linPort As LINPort _ ) As Boolean |

| C# |
| --- |
| public bool AddLINPort( LINPort linPort ) |

| Visual C++ |
| --- |
| public: bool AddLINPort( LINPort^ linPort ) |

###### Parameters

- **linPort**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.LINPortThe LIN port to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LIN Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lin_finalize.htm language=enus -->
## TOPIC 00463: LIN.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lin_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lin_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LIN Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linport_getlinscheduler.htm language=enus -->
## TOPIC 00464: LINPort.GetLINScheduler Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linport_getlinscheduler.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linport_getlinscheduler.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LINScheduler

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetLINScheduler As LINScheduler |

| C# |
| --- |
| public LINScheduler GetLINScheduler() |

| Visual C++ |
| --- |
| public: LINScheduler^ GetLINScheduler() |

###### Return Value

LINScheduler

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| A LIN schedule is valid only if the port is configured as the master port (IsMaster is true (True in Visual Basic)). |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LINPort Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_finalize.htm language=enus -->
## TOPIC 00465: LINScheduler.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LINScheduler Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_setactiveschedule.htm language=enus -->
## TOPIC 00466: LINScheduler.SetActiveSchedule Method (String[], String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_setactiveschedule.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_setactiveschedule.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LINPort

LINSchedules

ActiveSchedule

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function SetActiveSchedule ( _ LINSchedules As String(), _ ActiveSchedule As String _ ) As Boolean |

| C# |
| --- |
| public bool SetActiveSchedule( string[] LINSchedules, string ActiveSchedule ) |

| Visual C++ |
| --- |
| public: bool SetActiveSchedule( array<String^>^ LINSchedules, String^ ActiveSchedule ) |

###### Parameters

- **LINSchedules**
  - Type: System.String The array of all available LIN schedules.

- **ActiveSchedule**
  - Type: System.String The name of the schedule to set as the active schedule.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LINScheduler Class

SetActiveSchedule Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_setactiveschedule_1.htm language=enus -->
## TOPIC 00467: LINScheduler.SetActiveSchedule Method (String[], UInt32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_setactiveschedule_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_linscheduler_setactiveschedule_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LINPort

LINSchedules

ActiveScheduleIndex

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function SetActiveSchedule ( _ LINSchedules As String(), _ ActiveScheduleIndex As UInteger _ ) As Boolean |

| C# |
| --- |
| public bool SetActiveSchedule( string[] LINSchedules, uint ActiveScheduleIndex ) |

| Visual C++ |
| --- |
| public: bool SetActiveSchedule( array<String^>^ LINSchedules, unsigned int ActiveScheduleIndex ) |

###### Parameters

- **LINSchedules**
  - Type: System.String The array of all available LIN schedules.

- **ActiveScheduleIndex**
  - Type: System.UInt32 The array index of the schedule to set as the active schedule.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LINScheduler Class

SetActiveSchedule Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lookuptable__ctor_2.htm language=enus -->
## TOPIC 00468: LookupTable Constructor (String, LUTValue[], String)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lookuptable__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lookuptable__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Initializes a new instance of the LookupTable class with the specified name and properties.

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ name As String, _ lookupTableValues As LUTValue(), _ scaleUnit As String _ ) |

| C# |
| --- |
| public LookupTable( string name, LUTValue[] lookupTableValues, string scaleUnit ) |

| Visual C++ |
| --- |
| public: LookupTable( String^ name, array<LUTValue^>^ lookupTableValues, String^ scaleUnit ) |

###### Parameters

- **name**
  - Type: System.StringThe name of the LookupTable instance.

- **lookupTableValues**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.LUTValue An array of LUTValue elements.

- **scaleUnit**
  - Type: System.StringThe units of the scale. This can be any arbitrary string.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LookupTable Class

LookupTable Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lutvalue__ctor.htm language=enus -->
## TOPIC 00469: LUTValue Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lutvalue__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_lutvalue__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

LUTValue

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New |

| C# |
| --- |
| public LUTValue() |

| Visual C++ |
| --- |
| public: LUTValue() |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

LUTValue Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor.htm language=enus -->
## TOPIC 00470: Maximum Constructor (String, String, BaseNode, BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Maximum

x

y

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ XValue As BaseNode, _ YValue As BaseNode _ ) |

| C# |
| --- |
| public Maximum( string Name, string Description, BaseNode XValue, BaseNode YValue ) |

| Visual C++ |
| --- |
| public: Maximum( String^ Name, String^ Description, BaseNode^ XValue, BaseNode^ YValue ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the calculated channel.

- **Description**
  - Type: System.StringThe description of the calculated channel.

- **XValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel to be compared.

- **YValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel value to which x is compared.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Maximum Class

Maximum Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor_1.htm language=enus -->
## TOPIC 00471: Maximum Constructor (String, String, BaseNode, Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Maximum

x

y

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ XValue As BaseNode, _ YValue As Double _ ) |

| C# |
| --- |
| public Maximum( string Name, string Description, BaseNode XValue, double YValue ) |

| Visual C++ |
| --- |
| public: Maximum( String^ Name, String^ Description, BaseNode^ XValue, double YValue ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the calculated channel.

- **Description**
  - Type: System.StringThe description of the calculated channel.

- **XValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel to be compared.

- **YValue**
  - Type: System.DoubleThe constant value to which x is compared.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Maximum Class

Maximum Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor_2.htm language=enus -->
## TOPIC 00472: Maximum Constructor (String, String, Double, BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_maximum__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Maximum

x

y

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ XValue As Double, _ YValue As BaseNode _ ) |

| C# |
| --- |
| public Maximum( string Name, string Description, double XValue, BaseNode YValue ) |

| Visual C++ |
| --- |
| public: Maximum( String^ Name, String^ Description, double XValue, BaseNode^ YValue ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the calculated channel.

- **Description**
  - Type: System.StringThe description of the calculated channel.

- **XValue**
  - Type: System.DoubleThe constant value to be compared.

- **YValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel value to which x is compared.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Maximum Class

Maximum Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_minimum_setxvalue.htm language=enus -->
## TOPIC 00473: Minimum.SetXValue Method (BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_minimum_setxvalue.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_minimum_setxvalue.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

x

x

y

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetXValue ( _ XValue As BaseNode _ ) |

| C# |
| --- |
| public void SetXValue( BaseNode XValue ) |

| Visual C++ |
| --- |
| public: void SetXValue( BaseNode^ XValue ) |

###### Parameters

- **XValue**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel that specifies the value of x.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Minimum Class

SetXValue Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_minimum_setyvalue_1.htm language=enus -->
## TOPIC 00474: Minimum.SetYValue Method (Double)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_minimum_setyvalue_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_minimum_setyvalue_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

y

x

y

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub SetYValue ( _ YValue As Double _ ) |

| C# |
| --- |
| public void SetYValue( double YValue ) |

| Visual C++ |
| --- |
| public: void SetYValue( double YValue ) |

###### Parameters

- **YValue**
  - Type: System.DoubleThe value of y.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Minimum Class

SetYValue Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_2.htm language=enus -->
## TOPIC 00475: Model Constructor (String, String, String, Int32, Int32, UInt16, Boolean, Boolean, String, GlobalParameterScopes, Boolean, String, Boolean, UInt32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_2.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_2.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Model

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ ModelPath As String, _ Processor As Integer, _ Decimation As Integer, _ InitialState As UShort, _ SegmentVectors As Boolean, _ ImportParameters As Boolean, _ ParameterRegularExpression As String, _ GlobalParameterScope As GlobalParameterScopes, _ ImportSignals As Boolean, _ SignalRegularExpression As String, _ ImportOnlyNamedSignals As Boolean, _ NIVeriStandServerPort As UInteger _ ) |

| C# |
| --- |
| public Model( string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, GlobalParameterScopes GlobalParameterScope, bool ImportSignals, string SignalRegularExpression, bool ImportOnlyNamedSignals, uint NIVeriStandServerPort ) |

| Visual C++ |
| --- |
| public: Model( String^ Name, String^ Description, String^ ModelPath, int Processor, int Decimation, unsigned short InitialState, bool SegmentVectors, bool ImportParameters, String^ ParameterRegularExpression, GlobalParameterScopes GlobalParameterScope, bool ImportSignals, String^ SignalRegularExpression, bool ImportOnlyNamedSignals, unsigned int NIVeriStandServerPort ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the model.

- **Description**
  - Type: System.StringThe description of the model.

- **ModelPath**
  - Type: System.StringThe path to the uncompiled model.

- **Processor**
  - Type: System.Int32The processor on which the model runs.

- **Decimation**
  - Type: System.Int32The decimation of the model.

- **InitialState**
  - Type: System.UInt16The initial execution state of the model. 0: Running. 1: Paused.

- **SegmentVectors**
  - Type: System.Boolean true (True in Visual Basic) to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded.

- **ImportParameters**
  - Type: System.Boolean true (True in Visual Basic) to import parameters.

- **ParameterRegularExpression**
  - Type: System.StringThe regular expression to use to filter parameters. Parameters that match the regular expression are not imported.

- **GlobalParameterScope**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.GlobalParameterScopesThe scope of the global parameters. They can be either target or model scoped.

- **ImportSignals**
  - Type: System.Boolean true (True in Visual Basic) to import signals.

- **SignalRegularExpression**
  - Type: System.StringThe regular expression to use to filter signals. Signals that match the regular expression are not imported.

- **ImportOnlyNamedSignals**
  - Type: System.Boolean true (True in Visual Basic) to import only named signals.

- **NIVeriStandServerPort**
  - Type: System.UInt32The network port that the model uses for communication via TCP. This parameter is only valid for .mdl files.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Model Class

Model Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_3.htm language=enus -->
## TOPIC 00476: Model Constructor (String, String, String, Int32, Int32, UInt16, Boolean, Boolean, String, Boolean, String, Boolean)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Model

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ ModelPath As String, _ Processor As Integer, _ Decimation As Integer, _ InitialState As UShort, _ SegmentVectors As Boolean, _ ImportParameters As Boolean, _ ParameterRegularExpression As String, _ ImportSignals As Boolean, _ SignalRegularExpression As String, _ ImportOnlyNamedSignals As Boolean _ ) |

| C# |
| --- |
| public Model( string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, bool ImportSignals, string SignalRegularExpression, bool ImportOnlyNamedSignals ) |

| Visual C++ |
| --- |
| public: Model( String^ Name, String^ Description, String^ ModelPath, int Processor, int Decimation, unsigned short InitialState, bool SegmentVectors, bool ImportParameters, String^ ParameterRegularExpression, bool ImportSignals, String^ SignalRegularExpression, bool ImportOnlyNamedSignals ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the model.

- **Description**
  - Type: System.StringThe description of the model.

- **ModelPath**
  - Type: System.StringThe path to the uncompiled model.

- **Processor**
  - Type: System.Int32The processor on which the model runs.

- **Decimation**
  - Type: System.Int32The decimation of the model.

- **InitialState**
  - Type: System.UInt16The initial execution state of the model. 0: Running. 1: Paused.

- **SegmentVectors**
  - Type: System.Boolean true (True in Visual Basic) to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded.

- **ImportParameters**
  - Type: System.Boolean true (True in Visual Basic) to import parameters.

- **ParameterRegularExpression**
  - Type: System.StringThe regular expression to use to filter parameters. Parameters that match the regular expression are not imported.

- **ImportSignals**
  - Type: System.Boolean true (True in Visual Basic) to import signals.

- **SignalRegularExpression**
  - Type: System.StringThe regular expression to use to filter signals. Signals that match the regular expression are not imported.

- **ImportOnlyNamedSignals**
  - Type: System.Boolean true (True in Visual Basic) to import only named signals.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Model Class

Model Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_4.htm language=enus -->
## TOPIC 00477: Model Constructor (String, String, String, Int32, Int32, UInt16, Boolean, Boolean, String, Boolean, String, Boolean, UInt32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_4.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_model__ctor_4.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Model

.mdl

.lvmodel

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String, _ ModelPath As String, _ Processor As Integer, _ Decimation As Integer, _ InitialState As UShort, _ SegmentVectors As Boolean, _ ImportParameters As Boolean, _ ParameterRegularExpression As String, _ ImportSignals As Boolean, _ SignalRegularExpression As String, _ ImportOnlyNamedSignals As Boolean, _ NIVeriStandServerPort As UInteger _ ) |

| C# |
| --- |
| public Model( string Name, string Description, string ModelPath, int Processor, int Decimation, ushort InitialState, bool SegmentVectors, bool ImportParameters, string ParameterRegularExpression, bool ImportSignals, string SignalRegularExpression, bool ImportOnlyNamedSignals, uint NIVeriStandServerPort ) |

| Visual C++ |
| --- |
| public: Model( String^ Name, String^ Description, String^ ModelPath, int Processor, int Decimation, unsigned short InitialState, bool SegmentVectors, bool ImportParameters, String^ ParameterRegularExpression, bool ImportSignals, String^ SignalRegularExpression, bool ImportOnlyNamedSignals, unsigned int NIVeriStandServerPort ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the model.

- **Description**
  - Type: System.StringThe description of the model.

- **ModelPath**
  - Type: System.StringThe path to the uncompiled model.

- **Processor**
  - Type: System.Int32The processor on which the model runs.

- **Decimation**
  - Type: System.Int32The decimation of the model.

- **InitialState**
  - Type: System.UInt16The initial execution state of the model. 0: Running. 1: Paused.

- **SegmentVectors**
  - Type: System.Boolean true (True in Visual Basic) to split up vector inputs, outputs, parameters, and signals into scalar channels when the model is loaded.

- **ImportParameters**
  - Type: System.Boolean true (True in Visual Basic) to import parameters.

- **ParameterRegularExpression**
  - Type: System.StringThe regular expression to use to filter parameters. Parameters that match the regular expression are not imported.

- **ImportSignals**
  - Type: System.Boolean true (True in Visual Basic) to import signals.

- **SignalRegularExpression**
  - Type: System.StringThe regular expression to use to filter signals. Signals that match the regular expression are not imported.

- **ImportOnlyNamedSignals**
  - Type: System.Boolean true (True in Visual Basic) to import only named signals.

- **NIVeriStandServerPort**
  - Type: System.UInt32The network port that the model uses for communication via TCP. This parameter is only valid for .mdl files.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

Model Class

Model Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawdatabasedframe_getautomaticframeprocessing.htm language=enus -->
## TOPIC 00478: RawDataBasedFrame.GetAutomaticFrameProcessing Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawdatabasedframe_getautomaticframeprocessing.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawdatabasedframe_getautomaticframeprocessing.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Automatic Frame Processing

CRC

Counter

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetAutomaticFrameProcessing As AutomaticFrameProcessing |

| C# |
| --- |
| public AutomaticFrameProcessing GetAutomaticFrameProcessing() |

| Visual C++ |
| --- |
| public: AutomaticFrameProcessing^ GetAutomaticFrameProcessing() |

###### Return Value

AutomaticFrameProcessing

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

This method is only valid for outgoing CAN frames.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RawDataBasedFrame Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawdatabasedframe_getframeinformation.htm language=enus -->
## TOPIC 00479: RawDataBasedFrame.GetFrameInformation Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawdatabasedframe_getframeinformation.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawdatabasedframe_getframeinformation.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Frame Information

ReceiveTime

TimeDifference

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetFrameInformation As FrameInformation |

| C# |
| --- |
| public FrameInformation GetFrameInformation() |

| Visual C++ |
| --- |
| public: FrameInformation^ GetFrameInformation() |

###### Return Value

FrameInformation

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

This method is only valid for incoming frames.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RawDataBasedFrame Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawframedatalogging_getdataloggingfilelist.htm language=enus -->
## TOPIC 00480: RawFrameDataLogging.GetDataLoggingFileList Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawframedatalogging_getdataloggingfilelist.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_rawframedatalogging_getdataloggingfilelist.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

DataLoggingFile

RawFrameDataLogging

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDataLoggingFileList As DataLoggingFile() |

| C# |
| --- |
| public DataLoggingFile[] GetDataLoggingFileList() |

| Visual C++ |
| --- |
| public: array<DataLoggingFile^>^ GetDataLoggingFileList() |

###### Return Value

DataLoggingFile

RawFrameDataLogging

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

RawFrameDataLogging Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_receivetime_finalize.htm language=enus -->
## TOPIC 00481: ReceiveTime.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_receivetime_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_receivetime_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReceiveTime Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_receivetime_removenode.htm language=enus -->
## TOPIC 00482: ReceiveTime.RemoveNode Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_receivetime_removenode.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_receivetime_removenode.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Receive Time

FrameInformation

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Overrides Function RemoveNode As Boolean |

| C# |
| --- |
| public override bool RemoveNode() |

| Visual C++ |
| --- |
| public: virtual bool RemoveNode() override |

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReceiveTime Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt.htm language=enus -->
## TOPIC 00483: ReflectiveMemory.EnableInterrupt Method (ReflectiveMemoryInterruptType, BaseNode)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

type

interruptChannel

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub EnableInterrupt ( _ type As ReflectiveMemoryInterruptType, _ interruptChannel As BaseNode _ ) |

| C# |
| --- |
| public void EnableInterrupt( ReflectiveMemoryInterruptType type, BaseNode interruptChannel ) |

| Visual C++ |
| --- |
| public: void EnableInterrupt( ReflectiveMemoryInterruptType type, BaseNode^ interruptChannel ) |

###### Parameters

- **type**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptTypeThe type of interrupt, such as LinkResetInterrupt or NetworkInitInterrupt, to enable.

- **interruptChannel**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.BaseNodeThe channel to use for the interrupt value.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

All interrupts are sent in packets that contain the node ID of the sender, the node ID of the receiver, the type of the interrupt, and 32 bits of data you define.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemory Class

EnableInterrupt Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt_1.htm language=enus -->
## TOPIC 00484: ReflectiveMemory.EnableInterrupt Method (ReflectiveMemoryInterruptType, UInt32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt_1.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt_1.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

type

interruptConstantValue

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub EnableInterrupt ( _ type As ReflectiveMemoryInterruptType, _ interruptConstantValue As UInteger _ ) |

| C# |
| --- |
| public void EnableInterrupt( ReflectiveMemoryInterruptType type, uint interruptConstantValue ) |

| Visual C++ |
| --- |
| public: void EnableInterrupt( ReflectiveMemoryInterruptType type, unsigned int interruptConstantValue ) |

###### Parameters

- **type**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptTypeThe type of interrupt, such as LinkResetInterrupt or NetworkInitInterrupt, to enable.

- **interruptConstantValue**
  - Type: System.UInt32The constant value to assign the interrupt signal.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

All interrupts are sent in packets that contain the node ID of the sender, the node ID of the receiver, the type of the interrupt, and 32 bits of data you define.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemory Class

EnableInterrupt Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt_3.htm language=enus -->
## TOPIC 00485: ReflectiveMemory.EnableInterrupt Method (UInt16, ReflectiveMemoryInterruptType, UInt32)

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt_3.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_enableinterrupt_3.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

type

interruptTargetNode

interruptConstantValue

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub EnableInterrupt ( _ interruptTargetNode As UShort, _ type As ReflectiveMemoryInterruptType, _ interruptConstantValue As UInteger _ ) |

| C# |
| --- |
| public void EnableInterrupt( ushort interruptTargetNode, ReflectiveMemoryInterruptType type, uint interruptConstantValue ) |

| Visual C++ |
| --- |
| public: void EnableInterrupt( unsigned short interruptTargetNode, ReflectiveMemoryInterruptType type, unsigned int interruptConstantValue ) |

###### Parameters

- **interruptTargetNode**
  - Type: System.UInt16The decimal ID of the target node that receives the interrupt.

- **type**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryInterruptTypeThe type of interrupt, such as LinkResetInterrupt or NetworkInitInterrupt, to enable.

- **interruptConstantValue**
  - Type: System.UInt32The constant value to assign the interrupt signal.

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Refer to the hardware documentation for your reflective memory board for a list of target node ID numbers. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemory Class

EnableInterrupt Overload

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_finalize.htm language=enus -->
## TOPIC 00486: ReflectiveMemory.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememory_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemory Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannel_finalize.htm language=enus -->
## TOPIC 00487: ReflectiveMemoryDataChannel.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannel_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannel_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryDataChannel Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_adddatachannel.htm language=enus -->
## TOPIC 00488: ReflectiveMemoryDataChannels.AddDataChannel Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_adddatachannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_adddatachannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryDataChannel

Data Channels

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddDataChannel ( _ reflectiveMemoryDataChannel As ReflectiveMemoryDataChannel _ ) As Boolean |

| C# |
| --- |
| public bool AddDataChannel( ReflectiveMemoryDataChannel reflectiveMemoryDataChannel ) |

| Visual C++ |
| --- |
| public: bool AddDataChannel( ReflectiveMemoryDataChannel^ reflectiveMemoryDataChannel ) |

###### Parameters

- **reflectiveMemoryDataChannel**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannel The data channel to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryDataChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_addfolder.htm language=enus -->
## TOPIC 00489: ReflectiveMemoryDataChannels.AddFolder Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_addfolder.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_addfolder.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryFolder

Data Channels

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddFolder ( _ reflectiveMemoryFolder As ReflectiveMemoryFolder _ ) As Boolean |

| C# |
| --- |
| public bool AddFolder( ReflectiveMemoryFolder reflectiveMemoryFolder ) |

| Visual C++ |
| --- |
| public: bool AddFolder( ReflectiveMemoryFolder^ reflectiveMemoryFolder ) |

###### Parameters

- **reflectiveMemoryFolder**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryFolder The folder to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryDataChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_finalize.htm language=enus -->
## TOPIC 00490: ReflectiveMemoryDataChannels.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryDataChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_getdatachannels.htm language=enus -->
## TOPIC 00491: ReflectiveMemoryDataChannels.GetDataChannels Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_getdatachannels.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememorydatachannels_getdatachannels.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryDataChannel

ReflectiveMemoryDataChannels

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDataChannels As ReflectiveMemoryDataChannel() |

| C# |
| --- |
| public ReflectiveMemoryDataChannel[] GetDataChannels() |

| Visual C++ |
| --- |
| public: array<ReflectiveMemoryDataChannel^>^ GetDataChannels() |

###### Return Value

ReflectiveMemoryDataChannel

ReflectiveMemoryDataChannels

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryDataChannels Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder__ctor.htm language=enus -->
## TOPIC 00492: ReflectiveMemoryFolder Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String, _ Description As String _ ) |

| C# |
| --- |
| public ReflectiveMemoryFolder( string Name, string Description ) |

| Visual C++ |
| --- |
| public: ReflectiveMemoryFolder( String^ Name, String^ Description ) |

###### Parameters

- **Name**
  - Type: System.String The name of the folder.

- **Description**
  - Type: System.String The description of the folder.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_adddatachannel.htm language=enus -->
## TOPIC 00493: ReflectiveMemoryFolder.AddDataChannel Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_adddatachannel.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_adddatachannel.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryDataChannel

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddDataChannel ( _ reflectiveMemoryDataChannel As ReflectiveMemoryDataChannel _ ) As Boolean |

| C# |
| --- |
| public bool AddDataChannel( ReflectiveMemoryDataChannel reflectiveMemoryDataChannel ) |

| Visual C++ |
| --- |
| public: bool AddDataChannel( ReflectiveMemoryDataChannel^ reflectiveMemoryDataChannel ) |

###### Parameters

- **reflectiveMemoryDataChannel**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryDataChannelThe data channel to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_addfolder.htm language=enus -->
## TOPIC 00494: ReflectiveMemoryFolder.AddFolder Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_addfolder.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_addfolder.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function AddFolder ( _ reflectiveMemoryFolder As ReflectiveMemoryFolder _ ) As Boolean |

| C# |
| --- |
| public bool AddFolder( ReflectiveMemoryFolder reflectiveMemoryFolder ) |

| Visual C++ |
| --- |
| public: bool AddFolder( ReflectiveMemoryFolder^ reflectiveMemoryFolder ) |

###### Parameters

- **reflectiveMemoryFolder**
  - Type: NationalInstruments.VeriStand.SystemDefinitionAPI.ReflectiveMemoryFolderThe sub-folder to add.

###### Return Value

true

True

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_finalize.htm language=enus -->
## TOPIC 00495: ReflectiveMemoryFolder.Finalize Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_finalize.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_finalize.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

Class Destructor

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Protected Overrides Sub Finalize |

| C# |
| --- |
| protected override void Finalize() |

| Visual C++ |
| --- |
| protected: virtual void Finalize() override |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_getdatachannels.htm language=enus -->
## TOPIC 00496: ReflectiveMemoryFolder.GetDataChannels Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_getdatachannels.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_getdatachannels.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryDataChannel

ReflectiveMemoryFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetDataChannels As ReflectiveMemoryDataChannel() |

| C# |
| --- |
| public ReflectiveMemoryDataChannel[] GetDataChannels() |

| Visual C++ |
| --- |
| public: array<ReflectiveMemoryDataChannel^>^ GetDataChannels() |

###### Return Value

ReflectiveMemoryDataChannel

ReflectiveMemoryFolder

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_getfolders.htm language=enus -->
## TOPIC 00497: ReflectiveMemoryFolder.GetFolders Method

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_getfolders.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_reflectivememoryfolder_getfolders.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

ReflectiveMemoryFolder

ReflectiveMemoryFolder

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Function GetFolders As ReflectiveMemoryFolder() |

| C# |
| --- |
| public ReflectiveMemoryFolder[] GetFolders() |

| Visual C++ |
| --- |
| public: array<ReflectiveMemoryFolder^>^ GetFolders() |

###### Return Value

ReflectiveMemoryFolder

ReflectiveMemoryFolder

### [IMAGE alt='image' src='../icons/collapse_all.gif']Remarks

| Note: |
| --- |
| Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition. |

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

ReflectiveMemoryFolder Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1141__ctor.htm language=enus -->
## TOPIC 00498: SCXI1141 Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1141__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1141__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SCXI1141

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String _ ) |

| C# |
| --- |
| public SCXI1141( string Name ) |

| Visual C++ |
| --- |
| public: SCXI1141( String^ Name ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the module.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SCXI1141 Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1142__ctor.htm language=enus -->
## TOPIC 00499: SCXI1142 Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1142__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1142__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SCXI1142

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String _ ) |

| C# |
| --- |
| public SCXI1142( string Name ) |

| Visual C++ |
| --- |
| public: SCXI1142( String^ Name ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the module.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SCXI1142 Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace

<!--NI_TOPIC bundle=veristand-net-api-reference path=veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1162hv__ctor.htm language=enus -->
## TOPIC 00500: SCXI1162HV Constructor

- bundle_id: `veristand-net-api-reference`
- source_path: `veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1162hv__ctor.htm`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-reference/raw/resource/enus/veristandsdapi/html/m_nationalinstruments_veristand_systemdefinitionapi_scxi1162hv__ctor.htm
- document_id: `veristand-net-api-reference`
- page_type: `leaf`
- content_type: ``

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

SCXI1162HV

Namespace:

NationalInstruments.VeriStand.SystemDefinitionAPI

Assembly:

NationalInstruments.VeriStand.SystemDefinitionAPI

### [IMAGE alt='image' src='../icons/collapse_all.gif']Syntax

| Visual Basic (Declaration) |
| --- |
| Public Sub New ( _ Name As String _ ) |

| C# |
| --- |
| public SCXI1162HV( string Name ) |

| Visual C++ |
| --- |
| public: SCXI1162HV( String^ Name ) |

###### Parameters

- **Name**
  - Type: System.StringThe name of the module.

### [IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Reference

SCXI1162HV Class

NationalInstruments.VeriStand.SystemDefinitionAPI Namespace
