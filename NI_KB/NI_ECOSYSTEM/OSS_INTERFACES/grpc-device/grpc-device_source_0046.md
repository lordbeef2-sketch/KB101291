# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/functions_addon.py sha256=c35da99081e870b8764deebcb68d431250b7d74efa85cf06db6540921111e83a bytes=1808 -->
## FILE: source/codegen/metadata/nifake/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/functions_addon.py`
- sha256: `c35da99081e870b8764deebcb68d431250b7d74efa85cf06db6540921111e83a`
- bytes: 1808

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
}

functions_validation_suppressions = {
    "AcceptViSessionArray": {
        "parameters": {
            "sessionArray": ["INPUT_ARRAY_SHOULD_NOT_HAVE_PASSED_IN_SIZE"]
        }
    },
    "BoolArrayInputFunction": {
        "parameters": {
            "anArray": ["INPUT_ARRAY_SHOULD_NOT_HAVE_PASSED_IN_SIZE"]
        }
    },
    "ViUInt8ArrayInputFunction": {
        "parameters": {
            "anArray": ["INPUT_ARRAY_SHOULD_NOT_HAVE_PASSED_IN_SIZE"]
        }
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/nifake.proto sha256=0149be0887291ee6c9d0143725e496529ad5c04caa99974f080ac1b189f64565 bytes=36393 -->
## FILE: source/codegen/metadata/nifake/nifake.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/nifake.proto`
- sha256: `0149be0887291ee6c9d0143725e496529ad5c04caa99974f080ac1b189f64565`
- bytes: 36393

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-FAKE API metadata version 26.5.0d5
//---------------------------------------------------------------------
// Proto file for the NI-FAKE Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.fake";
option java_outer_classname = "NiFake";
option csharp_namespace = "NationalInstruments.Grpc.Fake";

package nifake_grpc;

import "session.proto";

service NiFake {
  rpc Abort(AbortRequest) returns (AbortResponse);
  rpc AcceptListOfDurationsInSeconds(AcceptListOfDurationsInSecondsRequest) returns (AcceptListOfDurationsInSecondsResponse);
  rpc AcceptViSessionArray(AcceptViSessionArrayRequest) returns (AcceptViSessionArrayResponse);
  rpc AcceptViUInt32Array(AcceptViUInt32ArrayRequest) returns (AcceptViUInt32ArrayResponse);
  rpc BoolArrayInputFunction(BoolArrayInputFunctionRequest) returns (BoolArrayInputFunctionResponse);
  rpc BoolArrayOutputFunction(BoolArrayOutputFunctionRequest) returns (BoolArrayOutputFunctionResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc CloseExtCal(CloseExtCalRequest) returns (CloseExtCalResponse);
  rpc CommandWithReservedParam(CommandWithReservedParamRequest) returns (CommandWithReservedParamResponse);
  rpc ConfigureAbc(ConfigureAbcRequest) returns (ConfigureAbcResponse);
  rpc ConfigureEnums(ConfigureEnumsRequest) returns (ConfigureEnumsResponse);
  rpc Control4022(Control4022Request) returns (Control4022Response);
  rpc CreateConfigurationList(CreateConfigurationListRequest) returns (CreateConfigurationListResponse);
  rpc CustomNestedStructRoundtrip(CustomNestedStructRoundtripRequest) returns (CustomNestedStructRoundtripResponse);
  rpc DoubleAllTheNums(DoubleAllTheNumsRequest) returns (DoubleAllTheNumsResponse);
  rpc EnumArrayOutputFunction(EnumArrayOutputFunctionRequest) returns (EnumArrayOutputFunctionResponse);
  rpc EnumInputFunctionWithDefaults(EnumInputFunctionWithDefaultsRequest) returns (EnumInputFunctionWithDefaultsResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationBufferEx(ExportAttributeConfigurationBufferExRequest) returns (ExportAttributeConfigurationBufferExResponse);
  rpc FetchWaveform(FetchWaveformRequest) returns (FetchWaveformResponse);
  rpc FetchWithCustomSize(FetchWithCustomSizeRequest) returns (FetchWithCustomSizeResponse);
  rpc FunctionWithOverriddenGrpcName2x(FunctionWithOverriddenGrpcName2xRequest) returns (FunctionWithOverriddenGrpcName2xResponse);
  rpc GetABoolean(GetABooleanRequest) returns (GetABooleanResponse);
  rpc GetANumber(GetANumberRequest) returns (GetANumberResponse);
  rpc GetAStringOfFixedMaximumSize(GetAStringOfFixedMaximumSizeRequest) returns (GetAStringOfFixedMaximumSizeResponse);
  rpc GetAnIviDanceCharArray(GetAnIviDanceCharArrayRequest) returns (GetAnIviDanceCharArrayResponse);
  rpc GetAnIviDanceWithATwistArray(GetAnIviDanceWithATwistArrayRequest) returns (GetAnIviDanceWithATwistArrayResponse);
  rpc GetAnIviDanceWithATwistArrayOfCustomType(GetAnIviDanceWithATwistArrayOfCustomTypeRequest) returns (GetAnIviDanceWithATwistArrayOfCustomTypeResponse);
  rpc GetAnIviDanceWithATwistArrayWithInputArray(GetAnIviDanceWithATwistArrayWithInputArrayRequest) returns (GetAnIviDanceWithATwistArrayWithInputArrayResponse);
  rpc GetAnIviDanceWithATwistByteArray(GetAnIviDanceWithATwistByteArrayRequest) returns (GetAnIviDanceWithATwistByteArrayResponse);
  rpc GetAnIviDanceWithATwistString(GetAnIviDanceWithATwistStringRequest) returns (GetAnIviDanceWithATwistStringResponse);
  rpc GetAnIviDanceWithATwistStringStrlenBug(GetAnIviDanceWithATwistStringStrlenBugRequest) returns (GetAnIviDanceWithATwistStringStrlenBugResponse);
  rpc GetArraySizeForCustomCode(GetArraySizeForCustomCodeRequest) returns (GetArraySizeForCustomCodeResponse);
  rpc GetArrayUsingIviDance(GetArrayUsingIviDanceRequest) returns (GetArrayUsingIviDanceResponse);
  rpc GetArrayViUInt8WithEnum(GetArrayViUInt8WithEnumRequest) returns (GetArrayViUInt8WithEnumResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetBitfieldAsEnumArray(GetBitfieldAsEnumArrayRequest) returns (GetBitfieldAsEnumArrayResponse);
  rpc GetCalDateAndTime(GetCalDateAndTimeRequest) returns (GetCalDateAndTimeResponse);
  rpc GetCalInterval(GetCalIntervalRequest) returns (GetCalIntervalResponse);
  rpc GetCustomType(GetCustomTypeRequest) returns (GetCustomTypeResponse);
  rpc GetCustomTypeArray(GetCustomTypeArrayRequest) returns (GetCustomTypeArrayResponse);
  rpc GetEnumValue(GetEnumValueRequest) returns (GetEnumValueResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetParameterWithOverriddenGrpcName(GetParameterWithOverriddenGrpcNameRequest) returns (GetParameterWithOverriddenGrpcNameResponse);
  rpc GetViInt32Array(GetViInt32ArrayRequest) returns (GetViInt32ArrayResponse);
  rpc GetViUInt32Array(GetViUInt32ArrayRequest) returns (GetViUInt32ArrayResponse);
  rpc GetViUInt8(GetViUInt8Request) returns (GetViUInt8Response);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ImportAttributeConfigurationBufferEx(ImportAttributeConfigurationBufferExRequest) returns (ImportAttributeConfigurationBufferExResponse);
  rpc InitExtCal(InitExtCalRequest) returns (InitExtCalResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc InitWithVarArgs(InitWithVarArgsRequest) returns (InitWithVarArgsResponse);
  rpc IviDanceWithATwistCalculatedSizeOut(IviDanceWithATwistCalculatedSizeOutRequest) returns (IviDanceWithATwistCalculatedSizeOutResponse);
  rpc IviDanceWithTwistWithMultipleArraysAndOneBufferSize(IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest) returns (IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse);
  rpc MethodUsingEnumWithGrpcNameValues(MethodUsingEnumWithGrpcNameValuesRequest) returns (MethodUsingEnumWithGrpcNameValuesResponse);
  rpc MethodUsingWholeAndFractionalNumbers(MethodUsingWholeAndFractionalNumbersRequest) returns (MethodUsingWholeAndFractionalNumbersResponse);
  rpc MethodUsingWholeMappedNumbers(MethodUsingWholeMappedNumbersRequest) returns (MethodUsingWholeMappedNumbersResponse);
  rpc MethodWithGetLastErrorParam(MethodWithGetLastErrorParamRequest) returns (MethodWithGetLastErrorParamResponse);
  rpc MethodWithGrpcFieldNumber(MethodWithGrpcFieldNumberRequest) returns (MethodWithGrpcFieldNumberResponse);
  rpc MethodWithGrpcOnlyParam(MethodWithGrpcOnlyParamRequest) returns (MethodWithGrpcOnlyParamResponse);
  rpc MethodWithProtoOnlyParameter(MethodWithProtoOnlyParameterRequest) returns (MethodWithProtoOnlyParameterResponse);
  rpc MultipleArrayTypes(MultipleArrayTypesRequest) returns (MultipleArrayTypesResponse);
  rpc MultipleArraysSameSize(MultipleArraysSameSizeRequest) returns (MultipleArraysSameSizeResponse);
  rpc MultipleArraysSameSizeWithOptional(MultipleArraysSameSizeWithOptionalRequest) returns (MultipleArraysSameSizeWithOptionalResponse);
  rpc OneInputFunction(OneInputFunctionRequest) returns (OneInputFunctionResponse);
  rpc ParametersAreMultipleTypes(ParametersAreMultipleTypesRequest) returns (ParametersAreMultipleTypesResponse);
  rpc PoorlyNamedSimpleFunction(PoorlyNamedSimpleFunctionRequest) returns (PoorlyNamedSimpleFunctionResponse);
  rpc Read(ReadRequest) returns (ReadResponse);
  rpc ReadDataWithInOutIviTwist(ReadDataWithInOutIviTwistRequest) returns (ReadDataWithInOutIviTwistResponse);
  rpc ReadDataWithMultipleIviTwistParamSets(ReadDataWithMultipleIviTwistParamSetsRequest) returns (ReadDataWithMultipleIviTwistParamSetsResponse);
  rpc ReadFromChannel(ReadFromChannelRequest) returns (ReadFromChannelResponse);
  rpc ReturnANumberAndAString(ReturnANumberAndAStringRequest) returns (ReturnANumberAndAStringResponse);
  rpc ReturnDurationInSeconds(ReturnDurationInSecondsRequest) returns (ReturnDurationInSecondsResponse);
  rpc ReturnListOfDurationsInSeconds(ReturnListOfDurationsInSecondsRequest) returns (ReturnListOfDurationsInSecondsResponse);
  rpc ReturnMultipleTypes(ReturnMultipleTypesRequest) returns (ReturnMultipleTypesResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetCustomType(SetCustomTypeRequest) returns (SetCustomTypeResponse);
  rpc SetCustomTypeArray(SetCustomTypeArrayRequest) returns (SetCustomTypeArrayResponse);
  rpc StringValuedEnumInputFunctionWithDefaults(StringValuedEnumInputFunctionWithDefaultsRequest) returns (StringValuedEnumInputFunctionWithDefaultsResponse);
  rpc StringValuedEnumNoEnumGenerated(StringValuedEnumNoEnumGeneratedRequest) returns (StringValuedEnumNoEnumGeneratedResponse);
  rpc TwoInputFunction(TwoInputFunctionRequest) returns (TwoInputFunctionResponse);
  rpc Use64BitNumber(Use64BitNumberRequest) returns (Use64BitNumberResponse);
  rpc UseATwoDimensionParameter(UseATwoDimensionParameterRequest) returns (UseATwoDimensionParameterResponse);
  rpc ViInt16ArrayInputFunction(ViInt16ArrayInputFunctionRequest) returns (ViInt16ArrayInputFunctionResponse);
  rpc ViUInt8ArrayInputFunction(ViUInt8ArrayInputFunctionRequest) returns (ViUInt8ArrayInputFunctionResponse);
  rpc ViUInt8ArrayOutputFunction(ViUInt8ArrayOutputFunctionRequest) returns (ViUInt8ArrayOutputFunctionResponse);
  rpc WriteWaveform(WriteWaveformRequest) returns (WriteWaveformResponse);
}

enum NiFakeAttribute {
  NIFAKE_ATTRIBUTE_UNSPECIFIED = 0;
  NIFAKE_ATTRIBUTE_READ_WRITE_BOOL = 1000000;
  NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE = 1000001;
  NIFAKE_ATTRIBUTE_READ_WRITE_STRING = 1000002;
  NIFAKE_ATTRIBUTE_READ_WRITE_COLOR = 1000003;
  NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER = 1000004;
  NIFAKE_ATTRIBUTE_FLOAT_ENUM_NAME_OVERRIDE = 1000005;
  NIFAKE_ATTRIBUTE_READ_WRITE_INT64 = 1000006;
  NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_CONVERTER = 1000007;
  NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER_WITH_CONVERTER = 1000008;
  NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY = 1000009;
  NIFAKE_ATTRIBUTE_READ_WRITE_STRING_REPEATED_CAPABILITY = 1000010;
  NIFAKE_ATTRIBUTE_SAMPLE_COUNT = 1000012;
  NIFAKE_ATTRIBUTE_SAMPLE_INTERVAL = 1000013;
}

enum Bitfield {
  BITFIELD_UNSPECIFIED = 0;
  BITFIELD_FLAG_A = 1;
  BITFIELD_FLAG_B = 2;
  BITFIELD_FLAG_C = 4;
  BITFIELD_FLAG_D = 8;
}

enum DecimalMixedNumber {
  DECIMAL_MIXED_NUMBER_UNSPECIFIED = 0;
  DECIMAL_MIXED_NUMBER_TWENTY_TWO = 1;
  DECIMAL_MIXED_NUMBER_TWO_POINT_TWO = 2;
  DECIMAL_MIXED_NUMBER_NEGATIVE_THREE = 3;
  DECIMAL_MIXED_NUMBER_MAX_INT_32 = 4;
  DECIMAL_MIXED_NUMBER_MAX_INT_32_PLUS_ONE = 5;
  DECIMAL_MIXED_NUMBER_MIN_INT_32 = 6;
  DECIMAL_MIXED_NUMBER_MIN_INT_32_MINUS_ONE = 7;
}

enum DecimalWholeNumber {
  DECIMAL_WHOLE_NUMBER_ZERO = 0;
  DECIMAL_WHOLE_NUMBER_NEGATIVE_ONE = -1;
  DECIMAL_WHOLE_NUMBER_TWENTY_TWO = 22;
}

enum DecimalWholeNumberMapped {
  DECIMAL_WHOLE_NUMBER_MAPPED_UNSPECIFIED = 0;
  DECIMAL_WHOLE_NUMBER_MAPPED_ZERO = 1;
  DECIMAL_WHOLE_NUMBER_MAPPED_NEGATIVE_ONE = 2;
  DECIMAL_WHOLE_NUMBER_MAPPED_TWENTY_TWO = 3;
}

enum EnumWithGrpcNameValues {
  ENUM_WITH_GRPC_NAME_VALUES_UNSPECIFIED = 0;
  ENUM_WITH_GRPC_NAME_VALUES_ALTERED_GRPC_NAME_ONE = 1;
  ENUM_WITH_GRPC_NAME_VALUES_TWO = 2;
}

enum FloatEnum {
  FLOAT_ENUM_UNSPECIFIED = 0;
  FLOAT_ENUM_THREE_POINT_FIVE = 1;
  FLOAT_ENUM_FOUR_POINT_FIVE = 2;
  FLOAT_ENUM_FIVE_POINT_FIVE = 3;
  FLOAT_ENUM_SIX_POINT_FIVE = 4;
  FLOAT_ENUM_SEVEN_POINT_FIVE = 5;
}

enum GrpcColorOverride {
  GRPC_COLOR_OVERRIDE_UNSPECIFIED = 0;
  GRPC_COLOR_OVERRIDE_RED = 1;
  GRPC_COLOR_OVERRIDE_BLUE = 2;
  GRPC_COLOR_OVERRIDE_YELLOW = 5;
  GRPC_COLOR_OVERRIDE_BLACK = 42;
}

enum MobileOSNames {
  MOBILE_OS_NAMES_UNSPECIFIED = 0;
  MOBILE_OS_NAMES_ANDROID = 1;
  MOBILE_OS_NAMES_IOS = 2;
  MOBILE_OS_NAMES_NONE = 3;
}

enum NiFakeInt32AttributeValues {
  option allow_alias = true;
  NIFAKE_INT32_UNSPECIFIED = 0;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_RED = 1;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLUE = 2;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_YELLOW = 5;
  NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLACK = 42;
  NIFAKE_INT32_SAMPLE_COUNT_SAMPLE_COUNT_INFINITE = 0;
}

enum NiFakeReal64AttributeValues {
  NIFAKE_REAL64_UNSPECIFIED = 0;
  NIFAKE_REAL64_SAMPLE_INTERVAL_AUTO_DELAY = -1;
}

enum NiFakeReal64AttributeValuesMapped {
  NIFAKE_REAL64_MAPPED_UNSPECIFIED = 0;
  NIFAKE_REAL64_FLOAT_ENUM_THREE_POINT_FIVE = 1;
  NIFAKE_REAL64_FLOAT_ENUM_FOUR_POINT_FIVE = 2;
  NIFAKE_REAL64_FLOAT_ENUM_FIVE_POINT_FIVE = 3;
  NIFAKE_REAL64_FLOAT_ENUM_SIX_POINT_FIVE = 4;
  NIFAKE_REAL64_FLOAT_ENUM_SEVEN_POINT_FIVE = 5;
}

enum SampleCount {
  SAMPLE_COUNT_SAMPLE_COUNT_INFINITE = 0;
}

enum SampleInterval {
  SAMPLE_INTERVAL_UNSPECIFIED = 0;
  SAMPLE_INTERVAL_AUTO_DELAY = -1;
}

enum Turtle {
  TURTLE_LEONARDO = 0;
  TURTLE_DONATELLO = 1;
  TURTLE_RAPHAEL = 2;
  TURTLE_MICHELANGELO = 3;
}

message FakeCustomStruct {
  sint32 struct_int = 1;
  double struct_double = 2;
}

message CustomStructNestedTypedef {
  FakeCustomStruct struct_custom_struct = 1;
  CustomStructTypedef struct_custom_struct_typedef = 2;
}

message CustomStructTypedef {
  sint32 struct_int = 1;
  double struct_double = 2;
}

message NIComplexI16_struct {
  sint32 real = 1;
  sint32 imaginary = 2;
}

message NIComplexNumber_struct {
  double real = 1;
  double imaginary = 2;
}

message NIComplexNumberF32_struct {
  float real = 1;
  float imaginary = 2;
}

message StringAndTurtle {
  string string_arg = 1;
  Turtle turtle = 2;
}

message CustomNamedType {
  string string_arg = 1;
}

message AbortRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortResponse {
  int32 status = 1;
}

message AcceptListOfDurationsInSecondsRequest {
  nidevice_grpc.Session vi = 1;
  repeated double delays = 2;
}

message AcceptListOfDurationsInSecondsResponse {
  int32 status = 1;
}

message AcceptViSessionArrayRequest {
  uint32 session_count = 1;
  repeated nidevice_grpc.Session session_array = 2;
}

message AcceptViSessionArrayResponse {
  int32 status = 1;
}

message AcceptViUInt32ArrayRequest {
  nidevice_grpc.Session vi = 1;
  repeated uint32 u_int32_array = 2;
}

message AcceptViUInt32ArrayResponse {
  int32 status = 1;
}

message BoolArrayInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
  repeated bool an_array = 3;
}

message BoolArrayInputFunctionResponse {
  int32 status = 1;
}

message BoolArrayOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message BoolArrayOutputFunctionResponse {
  int32 status = 1;
  repeated bool an_array = 2;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message CloseExtCalRequest {
  nidevice_grpc.Session vi = 1;
  sint32 action = 2;
}

message CloseExtCalResponse {
  int32 status = 1;
}

message CommandWithReservedParamRequest {
  nidevice_grpc.Session vi = 1;
}

message CommandWithReservedParamResponse {
  int32 status = 1;
}

message ConfigureAbcRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureAbcResponse {
  int32 status = 1;
}

message ConfigureEnumsRequest {
  nidevice_grpc.Session vi = 1;
  oneof sample_count_enum {
    SampleCount sample_count = 2;
    sint32 sample_count_raw = 3;
  }
  oneof sample_interval_enum {
    SampleInterval sample_interval = 4;
    double sample_interval_raw = 5;
  }
}

message ConfigureEnumsResponse {
  int32 status = 1;
}

message Control4022Request {
  string resource_name = 1;
  sint32 configuration = 2;
}

message Control4022Response {
  int32 status = 1;
}

message CreateConfigurationListRequest {
  repeated NiFakeAttribute list_attribute_ids = 1;
}

message CreateConfigurationListResponse {
  int32 status = 1;
}

message CustomNestedStructRoundtripRequest {
  CustomStructNestedTypedef nested_custom_type_in = 1;
}

message CustomNestedStructRoundtripResponse {
  int32 status = 1;
  CustomStructNestedTypedef nested_custom_type_out = 2;
}

message DoubleAllTheNumsRequest {
  nidevice_grpc.Session vi = 1;
  repeated double numbers = 2;
}

message DoubleAllTheNumsResponse {
  int32 status = 1;
}

message EnumArrayOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message EnumArrayOutputFunctionResponse {
  int32 status = 1;
  repeated Turtle an_array = 2;
  repeated sint32 an_array_raw = 3;
}

message EnumInputFunctionWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
  oneof a_turtle_enum {
    Turtle a_turtle = 2;
    sint32 a_turtle_raw = 3;
  }
}

message EnumInputFunctionWithDefaultsResponse {
  int32 status = 1;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message ExportAttributeConfigurationBufferExRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferExResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message FetchWaveformRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_samples = 2;
}

message FetchWaveformResponse {
  int32 status = 1;
  repeated double waveform_data = 2;
  sint32 actual_number_of_samples = 3;
}

message FetchWithCustomSizeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_waveforms = 2;
  sint32 number_of_samples = 3;
}

message FetchWithCustomSizeResponse {
  int32 status = 1;
  repeated double waveform_data = 2;
}

message FunctionWithOverriddenGrpcName2xRequest {
  nidevice_grpc.Session vi = 1;
}

message FunctionWithOverriddenGrpcName2xResponse {
  int32 status = 1;
}

message GetABooleanRequest {
  nidevice_grpc.Session vi = 1;
}

message GetABooleanResponse {
  int32 status = 1;
  bool a_boolean = 2;
}

message GetANumberRequest {
  nidevice_grpc.Session vi = 1;
}

message GetANumberResponse {
  int32 status = 1;
  sint32 a_number = 2;
}

message GetAStringOfFixedMaximumSizeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAStringOfFixedMaximumSizeResponse {
  int32 status = 1;
  string a_string = 2;
}

message GetAnIviDanceCharArrayRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAnIviDanceCharArrayResponse {
  int32 status = 1;
  string char_array = 2;
}

message GetAnIviDanceWithATwistArrayRequest {
  nidevice_grpc.Session vi = 1;
  string a_string = 2;
}

message GetAnIviDanceWithATwistArrayResponse {
  int32 status = 1;
  repeated sint32 array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistArrayOfCustomTypeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAnIviDanceWithATwistArrayOfCustomTypeResponse {
  int32 status = 1;
  repeated FakeCustomStruct array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistArrayWithInputArrayRequest {
  repeated sint32 data_in = 1;
}

message GetAnIviDanceWithATwistArrayWithInputArrayResponse {
  int32 status = 1;
  repeated sint32 array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistByteArrayRequest {
}

message GetAnIviDanceWithATwistByteArrayResponse {
  int32 status = 1;
  bytes array_out = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistStringRequest {
  nidevice_grpc.Session vi = 1;
}

message GetAnIviDanceWithATwistStringResponse {
  int32 status = 1;
  string a_string = 2;
  sint32 actual_size = 3;
}

message GetAnIviDanceWithATwistStringStrlenBugRequest {
}

message GetAnIviDanceWithATwistStringStrlenBugResponse {
  int32 status = 1;
  string string_out = 2;
  sint32 actual_size = 3;
}

message GetArraySizeForCustomCodeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetArraySizeForCustomCodeResponse {
  int32 status = 1;
  sint32 size_out = 2;
}

message GetArrayUsingIviDanceRequest {
  nidevice_grpc.Session vi = 1;
}

message GetArrayUsingIviDanceResponse {
  int32 status = 1;
  repeated double array_out = 2;
}

message GetArrayViUInt8WithEnumRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_len = 2;
}

message GetArrayViUInt8WithEnumResponse {
  int32 status = 1;
  repeated GrpcColorOverride u_int8_enum_array = 2;
  bytes u_int8_enum_array_raw = 3;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetBitfieldAsEnumArrayRequest {
}

message GetBitfieldAsEnumArrayResponse {
  int32 status = 1;
  repeated Bitfield flags_array = 2;
  int64 flags_raw = 3;
}

message GetCalDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
  sint32 cal_type = 2;
}

message GetCalDateAndTimeResponse {
  int32 status = 1;
  sint32 month = 2;
  sint32 day = 3;
  sint32 year = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetCalIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetCalIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
}

message GetCustomTypeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetCustomTypeResponse {
  int32 status = 1;
  FakeCustomStruct cs = 2;
}

message GetCustomTypeArrayRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message GetCustomTypeArrayResponse {
  int32 status = 1;
  repeated FakeCustomStruct cs = 2;
}

message GetEnumValueRequest {
  nidevice_grpc.Session vi = 1;
}

message GetEnumValueResponse {
  int32 status = 1;
  sint32 a_quantity = 2;
  Turtle a_turtle = 3;
  sint32 a_turtle_raw = 4;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string description = 3;
}

message GetParameterWithOverriddenGrpcNameRequest {
  nidevice_grpc.Session vi = 1;
  oneof enum_parameter_raw_enum {
    Turtle enum_parameter_raw = 2;
    sint32 enum_parameter_raw_raw = 3;
  }
}

message GetParameterWithOverriddenGrpcNameResponse {
  int32 status = 1;
  sint32 overridden_parameter = 2;
}

message GetViInt32ArrayRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_len = 2;
}

message GetViInt32ArrayResponse {
  int32 status = 1;
  repeated sint32 int32_array = 2;
}

message GetViUInt32ArrayRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_len = 2;
}

message GetViUInt32ArrayResponse {
  int32 status = 1;
  repeated uint32 u_int32_array = 2;
}

message GetViUInt8Request {
  nidevice_grpc.Session vi = 1;
}

message GetViUInt8Response {
  int32 status = 1;
  uint32 a_uint8_number = 2;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationBufferExRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferExResponse {
  int32 status = 1;
}

message InitExtCalRequest {
  string session_name = 1;
  string resource_name = 2;
  string calibration_password = 3;
}

message InitExtCalResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  bool new_session_initialized = 3;
}

message InitWithVarArgsRequest {
  string session_name = 1;
  string resource_name = 2;
  repeated StringAndTurtle name_and_turtle = 3;
}

message InitWithVarArgsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
}

message IviDanceWithATwistCalculatedSizeOutRequest {
  nidevice_grpc.Session vi = 1;
}

message IviDanceWithATwistCalculatedSizeOutResponse {
  int32 status = 1;
  repeated uint32 data = 2;
  sint32 actual_num_waveforms = 3;
  sint32 actual_samples_per_waveform = 4;
}

message IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest {
  nidevice_grpc.Session vi = 1;
}

message IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse {
  int32 status = 1;
  repeated sint32 array1 = 2;
  repeated sint32 array2 = 3;
  repeated sint32 array3 = 4;
  sint32 actual_num_elements = 5;
}

message MethodUsingEnumWithGrpcNameValuesRequest {
  oneof using_enum_enum {
    EnumWithGrpcNameValues using_enum = 1;
    sint32 using_enum_raw = 2;
  }
}

message MethodUsingEnumWithGrpcNameValuesResponse {
  int32 status = 1;
}

message MethodUsingWholeAndFractionalNumbersRequest {
}

message MethodUsingWholeAndFractionalNumbersResponse {
  int32 status = 1;
  DecimalWholeNumber whole_number = 2;
  sint32 whole_number_raw = 3;
  DecimalMixedNumber fractional_number_mapped = 4;
  double fractional_number_raw = 5;
}

message MethodUsingWholeMappedNumbersRequest {
}

message MethodUsingWholeMappedNumbersResponse {
  int32 status = 1;
  DecimalWholeNumberMapped whole_number_mapped = 2;
  double whole_number_raw = 3;
}

message MethodWithGetLastErrorParamRequest {
}

message MethodWithGetLastErrorParamResponse {
  int32 status = 1;
  string last_error = 2 [deprecated = true];
}

message MethodWithGrpcFieldNumberRequest {
  sint32 attribute_value = 5;
}

message MethodWithGrpcFieldNumberResponse {
  int32 status = 1;
}

message MethodWithGrpcOnlyParamRequest {
  sint32 simple_param = 1;
}

message MethodWithGrpcOnlyParamResponse {
  int32 status = 1;
  sint32 grpc_only_param = 2;
}

message MethodWithProtoOnlyParameterRequest {
  sint32 attribute_value = 1;
}

message MethodWithProtoOnlyParameterResponse {
  int32 status = 1;
}

message MultipleArrayTypesRequest {
  nidevice_grpc.Session vi = 1;
  sint32 output_array_size = 2;
  repeated double input_array_of_floats = 3;
  repeated sint32 input_array_of_integers = 4;
}

message MultipleArrayTypesResponse {
  int32 status = 1;
  repeated double output_array = 2;
  repeated double output_array_of_fixed_length = 3;
}

message MultipleArraysSameSizeRequest {
  nidevice_grpc.Session vi = 1;
  repeated double values1 = 2;
  repeated double values2 = 3;
  repeated double values3 = 4;
  repeated double values4 = 5;
}

message MultipleArraysSameSizeResponse {
  int32 status = 1;
}

message MultipleArraysSameSizeWithOptionalRequest {
  nidevice_grpc.Session vi = 1;
  repeated double values1 = 2;
  repeated double values2 = 3;
  repeated double values3 = 4;
  repeated double values4 = 5;
  repeated FakeCustomStruct values5 = 6;
}

message MultipleArraysSameSizeWithOptionalResponse {
  int32 status = 1;
}

message OneInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 a_number = 2;
}

message OneInputFunctionResponse {
  int32 status = 1;
}

message ParametersAreMultipleTypesRequest {
  nidevice_grpc.Session vi = 1;
  bool a_boolean = 2;
  sint32 an_int32 = 3;
  int64 an_int64 = 4;
  oneof an_int_enum_enum {
    Turtle an_int_enum = 5;
    sint32 an_int_enum_raw = 6;
  }
  double a_float = 7;
  oneof a_float_enum_enum {
    FloatEnum a_float_enum_mapped = 8;
    double a_float_enum_raw = 9;
  }
  string a_string = 10;
}

message ParametersAreMultipleTypesResponse {
  int32 status = 1;
}

message PoorlyNamedSimpleFunctionRequest {
  nidevice_grpc.Session vi = 1;
}

message PoorlyNamedSimpleFunctionResponse {
  int32 status = 1;
}

message ReadRequest {
  nidevice_grpc.Session vi = 1;
  double maximum_time = 2;
}

message ReadResponse {
  int32 status = 1;
  double reading = 2;
}

message ReadDataWithInOutIviTwistRequest {
}

message ReadDataWithInOutIviTwistResponse {
  int32 status = 1;
  repeated sint32 data = 2;
  sint32 buffer_size = 3;
}

message ReadDataWithMultipleIviTwistParamSetsRequest {
}

message ReadDataWithMultipleIviTwistParamSetsResponse {
  int32 status = 1;
  repeated sint32 array_out = 2;
  sint32 actual_size = 3;
  repeated sint32 other_array_out = 4;
  sint32 other_actual_size = 5;
}

message ReadFromChannelRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 maximum_time = 3;
}

message ReadFromChannelResponse {
  int32 status = 1;
  double reading = 2;
}

message ReturnANumberAndAStringRequest {
  nidevice_grpc.Session vi = 1;
}

message ReturnANumberAndAStringResponse {
  int32 status = 1;
  sint32 a_number = 2;
  string a_string = 3;
}

message ReturnDurationInSecondsRequest {
  nidevice_grpc.Session vi = 1;
}

message ReturnDurationInSecondsResponse {
  int32 status = 1;
  double timedelta = 2;
}

message ReturnListOfDurationsInSecondsRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message ReturnListOfDurationsInSecondsResponse {
  int32 status = 1;
  repeated double timedeltas = 2;
}

message ReturnMultipleTypesRequest {
  nidevice_grpc.Session vi = 1;
  sint32 array_size = 2;
}

message ReturnMultipleTypesResponse {
  int32 status = 1;
  bool a_boolean = 2;
  sint32 an_int32 = 3;
  int64 an_int64 = 4;
  Turtle an_int_enum = 5;
  sint32 an_int_enum_raw = 6;
  double a_float = 7;
  FloatEnum a_float_enum_mapped = 8;
  double a_float_enum_raw = 9;
  repeated double an_array = 10;
  string a_string = 11;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFakeInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  int64 attribute_value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFakeReal64AttributeValues attribute_value = 4;
    NiFakeReal64AttributeValuesMapped attribute_value_mapped = 5;
    double attribute_value_raw = 6;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFakeAttribute attribute_id = 3;
  string attribute_value_raw = 4;
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetCustomTypeRequest {
  nidevice_grpc.Session vi = 1;
  FakeCustomStruct cs = 2;
}

message SetCustomTypeResponse {
  int32 status = 1;
}

message SetCustomTypeArrayRequest {
  nidevice_grpc.Session vi = 1;
  repeated FakeCustomStruct cs = 2;
}

message SetCustomTypeArrayResponse {
  int32 status = 1;
}

message StringValuedEnumInputFunctionWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
  oneof a_mobile_os_name_enum {
    MobileOSNames a_mobile_os_name_mapped = 2;
    string a_mobile_os_name_raw = 3;
  }
}

message StringValuedEnumInputFunctionWithDefaultsResponse {
  int32 status = 1;
}

message StringValuedEnumNoEnumGeneratedRequest {
  nidevice_grpc.Session vi = 1;
  string a_string_enum = 2;
}

message StringValuedEnumNoEnumGeneratedResponse {
  int32 status = 1;
}

message TwoInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  double a_number = 2;
  string a_string = 3;
}

message TwoInputFunctionResponse {
  int32 status = 1;
}

message Use64BitNumberRequest {
  nidevice_grpc.Session vi = 1;
  int64 input = 2;
}

message Use64BitNumberResponse {
  int32 status = 1;
  int64 output = 2;
}

message UseATwoDimensionParameterRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 array = 2;
  repeated sint32 array_lengths = 3;
}

message UseATwoDimensionParameterResponse {
  int32 status = 1;
}

message ViInt16ArrayInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 an_array = 2;
}

message ViInt16ArrayInputFunctionResponse {
  int32 status = 1;
}

message ViUInt8ArrayInputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
  bytes an_array = 3;
}

message ViUInt8ArrayInputFunctionResponse {
  int32 status = 1;
}

message ViUInt8ArrayOutputFunctionRequest {
  nidevice_grpc.Session vi = 1;
  sint32 number_of_elements = 2;
}

message ViUInt8ArrayOutputFunctionResponse {
  int32 status = 1;
  bytes an_array = 2;
}

message WriteWaveformRequest {
  nidevice_grpc.Session vi = 1;
  repeated double waveform = 2;
}

message WriteWaveformResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake/README.md sha256=90d97c9c68cdce2bf02e0d5b87caf59783c4af5e604038d2b400637ae06cb1d2 bytes=209 -->
## FILE: source/codegen/metadata/nifake/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake/README.md`
- sha256: `90d97c9c68cdce2bf02e0d5b87caf59783c4af5e604038d2b400637ae06cb1d2`
- bytes: 209

````markdown
# Updating

To update this metadata folder. Find the nifake_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/__init__.py sha256=bf3565cfb4e9a085febbe4145a805c70e9623f3099a4d169f8c58bf8427d65d5 bytes=248 -->
## FILE: source/codegen/metadata/nifake_extension/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/__init__.py`
- sha256: `bf3565cfb4e9a085febbe4145a805c70e9623f3099a4d169f8c58bf8427d65d5`
- bytes: 248

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/attributes.py sha256=3a750f30b7b8e33d393645e7b18404232e4e667cf26df4daa5a56af7b0ce1afa bytes=110 -->
## FILE: source/codegen/metadata/nifake_extension/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/attributes.py`
- sha256: `3a750f30b7b8e33d393645e7b18404232e4e667cf26df4daa5a56af7b0ce1afa`
- bytes: 110

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 1.2.0d9
attributes = {}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nifake_extension/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/config.py sha256=888ddc1f5d3e94bf0f489df45f4147a86d5eb4d375e1d046e244f92d130629fd bytes=1236 -->
## FILE: source/codegen/metadata/nifake_extension/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/config.py`
- sha256: `888ddc1f5d3e94bf0f489df45f4147a86d5eb4d375e1d046e244f92d130629fd`
- bytes: 1236

````python
# -*- coding: utf-8 -*-
# An NI-FAKE Extension that adds fake features to ni-fake sessions
config = {
    'api_version': '1.2.0d9',
    'c_header': 'niFake.h',
    'c_function_prefix': 'niFakeExtension_',
    'service_class_prefix': 'NiFakeExtension',
    'java_package': 'com.ni.grpc.fakeextension',
    'csharp_namespace': 'NationalInstruments.Grpc.FakeExtension',
    'namespace_component': 'nifake_extension',
    'close_function': None,
    'driver_name': 'NI-FAKE-EXTENSION',
    'custom_types': [],
    'status_ok': 'status >= 0',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifake',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nifake_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nifake_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '2.0',
    'module_name': 'nifake_extension',
    'session_class_description': 'An NI-FAKE Extension that adds fake features to ni-fake sessions',
    'session_handle_parameter_name': 'vi',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/config_addon.py sha256=e6b1ac77e5483d879a9918d233d21e26e9a461e36a1d51d0341004417cbec305 bytes=170 -->
## FILE: source/codegen/metadata/nifake_extension/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/config_addon.py`
- sha256: `e6b1ac77e5483d879a9918d233d21e26e9a461e36a1d51d0341004417cbec305`
- bytes: 170

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/enums.py sha256=70f6c78f5fa18eb3a5b5b8cdae123d5aad340f07ecf7935a0d1cb802c5558318 bytes=105 -->
## FILE: source/codegen/metadata/nifake_extension/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/enums.py`
- sha256: `70f6c78f5fa18eb3a5b5b8cdae123d5aad340f07ecf7935a0d1cb802c5558318`
- bytes: 105

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 1.2.0d9
enums = {}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nifake_extension/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/functions.py sha256=9b565af8dd7cd5233450a6855619a3315a9ea0ba6b88f7a86e56063172f7f722 bytes=1212 -->
## FILE: source/codegen/metadata/nifake_extension/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/functions.py`
- sha256: `9b565af8dd7cd5233450a6855619a3315a9ea0ba6b88f7a86e56063172f7f722`
- bytes: 1212

````python
# -*- coding: utf-8 -*-
functions = {
   'AddCoolFunctionality': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'param',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'TestAddressParameters': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'space',
                'type': 'ViInt16'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViUInt64'
            },
            {
                'direction': 'in',
                'name': 'suggested',
                'type': 'ViAddr'
            },
            {
                'direction': 'out',
                'name': 'actual',
                'type': 'ViAddr'
            },
        ],
        'returns': 'ViStatus'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_extension/functions_addon.py sha256=2baced8307d23f1fceb2b39befd2ea9702c4a8ea8094614a02db2ab889ce5f21 bytes=243 -->
## FILE: source/codegen/metadata/nifake_extension/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_extension/functions_addon.py`
- sha256: `2baced8307d23f1fceb2b39befd2ea9702c4a8ea8094614a02db2ab889ce5f21`
- bytes: 243

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/__init__.py sha256=09e582155cc2826d659723c34fa701b97f8cccd2839c07081fdeb78d91c45605 bytes=391 -->
## FILE: source/codegen/metadata/nifake_non_ivi/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/__init__.py`
- sha256: `09e582155cc2826d659723c34fa701b97f8cccd2839c07081fdeb78d91c45605`
- bytes: 391

````python
from .functions import functions
from .functions_addon import functions_validation_suppressions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions" : functions,
    "functions_validation_suppressions": functions_validation_suppressions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/attributes.py sha256=16a13ea73efefe052c6bd21a8ef29b80177d6a59a0a870045114c51873ad9577 bytes=964 -->
## FILE: source/codegen/metadata/nifake_non_ivi/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/attributes.py`
- sha256: `16a13ea73efefe052c6bd21a8ef29b80177d6a59a0a870045114c51873ad9577`
- bytes: 964

````python
attributes = {
    'Marble': {
        10: {
            'access': 'read-write',
            'enum': 'BeautifulColor',
            'name': 'TEN_FAVORITE_COLORS',
            'resettable': False,
            'type': 'int32[]'
        },
        345: {
            'access': 'read-write',
            'name': 'TEN_RANDOM_NUMBERS',
            'resettable': False,
            'type': 'int32[]'
        },
        1234: {
            'access': 'read-write',
            'enum': 'BeautifulColor',
            'name': 'COLOR',
            'resettable': False,
            'type': 'int32'
        },
        1551: {
            'access': 'read-write',
            'name': 'NUMBER_OF_FAILED_ATTEMPTS',
            'resettable': False,
            'type': 'int32'
        },
        4444: {
            'access': 'read-write',
            'name': 'WEIGHT',
            'resettable': True,
            'type': 'double'
        }
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nifake_non_ivi/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/config.py sha256=fe5a3e54bec8585e5780973359dbcbcb6382a541bce5b91d79856ae4333c5f21 bytes=3029 -->
## FILE: source/codegen/metadata/nifake_non_ivi/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/config.py`
- sha256: `fe5a3e54bec8585e5780973359dbcbcb6382a541bce5b91d79856ae4333c5f21`
- bytes: 3029

````python
# -*- coding: utf-8 -*-
# An NI-FAKE driver that does not use IVI types
config = {
    'api_version': '1.2.0d9',
    'c_header': 'niFakeNonIvi.h',
    'c_function_prefix': 'niFakeNonIvi_',
    'service_class_prefix': 'NiFakeNonIvi',
    'java_package': 'com.ni.grpc.fakenonivi',
    'csharp_namespace': 'NationalInstruments.Grpc.FakeNonIvi',
    'namespace_component': 'nifake_non_ivi',
    'close_function': 'Close',
    'driver_name': 'NI-FAKE-NON-IVI',
    'resource_handle_type': ['FakeHandle', 'SecondarySessionHandle'],
    'status_ok': 'status >= 0',
    'additional_headers': { 'custom/nifake_non_ivi_errors.h': ['service.cpp'] },
    'custom_types': [
        {
            'name': 'StringAndEnum',
            'grpc_name': 'StringAndEnum',
            'fields': [
                {
                    'type': 'const char[]',
                    'name': 'channelName',
                },
                {
                    'type': 'int32',
                    'enum': 'BeautifulColor',
                    'name': 'color',
                },
                {
                    'type': 'double',
                    'name': 'powerUpState',
                },
            ]
        },
        {
            'name': 'StructWithCoercion_struct',
            'grpc_name': 'StructWithCoercion',
            'fields': [
                {
                    'type': 'myInt16',
                    'name': 'first',
                    'coerced': True
                },
                {
                    'type': 'myUInt16',
                    'name': 'second',
                    'coerced': True
                },
                {
                    'type': 'myInt8',
                    'name': 'third',
                    'coerced': True
                }
            ],
        }
    ],
    'type_to_grpc_type': {
        'FakeHandle': 'nidevice_grpc.Session',
        'char[]': 'string',
        'myInt16': 'int32',
        'myUInt16': 'uint32',
        'myInt8': 'int32',
        'myUInt8[]': 'bytes',
        'CallbackPtr': 'void'
    },
    'code_readiness': 'NextRelease',
    'feature_toggles': {
        'nifake_non_ivi.allow_undefined_attributes': 'Prototype' 
    },
    'split_attributes_by_type': True,
    'supports_raw_attributes': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifakenonivi',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nifakenonivi_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nifakenonivi_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '2.0',
    'module_name': 'nifake_non_ivi',
    'session_class_description': 'An NI-FAKE driver that does not use IVI types',
    'session_handle_parameter_name': 'handle',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/config_addon.py sha256=e6b1ac77e5483d879a9918d233d21e26e9a461e36a1d51d0341004417cbec305 bytes=170 -->
## FILE: source/codegen/metadata/nifake_non_ivi/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/config_addon.py`
- sha256: `e6b1ac77e5483d879a9918d233d21e26e9a461e36a1d51d0341004417cbec305`
- bytes: 170

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/enums.py sha256=b6db4612aedc2a975f45ce1a267ebb683781ba175f2f2632b8b3b51788a3f6d1 bytes=939 -->
## FILE: source/codegen/metadata/nifake_non_ivi/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/enums.py`
- sha256: `b6db4612aedc2a975f45ce1a267ebb683781ba175f2f2632b8b3b51788a3f6d1`
- bytes: 939

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FAKE API metadata version 1.2.0d9
enums = {
    'BeautifulColor': {
        'values': [
            {
                'name': 'PINK',
                'value': 44
            },
            {
                'name': 'AQUA',
                'value': 43
            },
            {
                'name': 'GREEN',
                'value': 45
            },
            {
                'name': 'BLACK',
                'value': 42
            }
        ]
    },
    'MobileOSNames': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'ANDROID',
                'value': 'Android'
            },
            {
                'name': 'IOS',
                'value': 'iOS'
            },
            {
                'name': 'NONE',
                'value': 'None'
            }
        ]
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nifake_non_ivi/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/functions.py sha256=25d9cef24a7712bbc1824ab482da8b706792c2468c93afc4a126f873fb233a23 bytes=21448 -->
## FILE: source/codegen/metadata/nifake_non_ivi/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/functions.py`
- sha256: `25d9cef24a7712bbc1824ab482da8b706792c2468c93afc4a126f873fb233a23`
- bytes: 21448

````python
# -*- coding: utf-8 -*-
functions = {
    'Close': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            }
        ],
        'returns': 'int32'
    },
    'CloseSecondarySession': {
        'custom_close_method': True,
        'parameters': [
            {
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'secondarySessionHandle',
                'type': 'SecondarySessionHandle',
            },
        ],
        'returns': 'int32',
    },
    'GetCrossDriverSession': {
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'cross_driver_session': 'FakeCrossDriverHandle',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'crossDriverSession',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    },
    'GetLatestErrorMessage': {
        'parameters': [
            {
                'direction': 'out',
                'name': 'message',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetStringAsReturnedValue': {
        'status_expression': 'string_out ? 0 : -1',
        'parameters': [
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'buf',
                'size': {
                    'mechanism': 'fixed',
                    'value': '512'
                },
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'string_out',
                'return_value': True,
                'type': 'const char[]'
            },
        ],
        'returns': 'const char*'
    },
    'GetMarbleAttributeDouble': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'MarbleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'double'
            },
        ],
        'returns': 'int32'
    },
    'GetMarbleAttributeInt32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'MarbleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    },
    'GetMarbleAttributeInt32Array': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'MarbleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '10'
                },
                'type': 'int32[]'
            }
        ],
        'returns': 'int32'
    },
    'Init': {
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'sessionName',
                'type': 'const char[]',
                'is_session_name': True
            },
            {
                'direction': 'out',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'direction': 'out',
                'get_last_error': 'deprecated',
                'name': 'errorMessage',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'InitFromCrossDriverSession': {
        'init_method': True,
        'parameters': [
            {
                'cross_driver_session': 'FakeCrossDriverHandle',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'crossDriverSession',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'handle',
                'type': 'FakeHandle'
            }
        ],
        'returns': 'int32'
    },
    'InitFromCrossDriverSessionArray': {
        'init_method': True,
        'parameters': [
            {
                'cross_driver_session': 'FakeCrossDriverHandle',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.Session',
                'name': 'crossDriverSessionArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfCrossDriverSessions'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfCrossDriverSessions',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'handle',
                'type': 'FakeHandle'
            }
        ],
        'returns': 'int32'
    },
    'InitSecondarySession': {
        'init_method': True,
        'custom_close': 'CloseSecondarySession(id)',
        'parameters': [
            {
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'secondarySessionHandle',
                'type': 'SecondarySessionHandle',
            },
        ],
        'returns': 'int32',
    },
    'InitWithHandleNameAsSessionName': {
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'handleName',
                'type': 'const char[]',
                'is_session_name': True
            },
            {
                'direction': 'out',
                'name': 'handle',
                'type': 'FakeHandle'
            }
        ],
        'returns': 'int32'
    },
    'InitWithReturnedSession': {     
        'init_method' : True,
        'status_expression': 'handle == 0xDEADBEEF ? -1 : 0',
        'parameters': [
            {
                'direction': 'in',
                'name': 'handleName',
                'type': 'const char[]',
                'is_session_name': True
            },
            {
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'handle',
                'return_value': True,
                'type': 'FakeHandle'
            },
        ],
    'returns': 'FakeHandle'
    },
    'InputArraysWithNarrowIntegerTypes': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'u16Array',
                'type': 'const myUInt16[]',
                'coerced': True
            },
            {
                'direction': 'in',
                'name': 'i16Array',
                'type': 'const myInt16[]',
                'coerced': True
            },
            {
                'direction': 'in',
                'name': 'i8Array',
                'type': 'const myInt8[]',
                'coerced': True
            }
        ],
        'returns': 'int32'
    },
    'IotaWithCustomSize': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'sizeOne',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'sizeTwo',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'custom-code',
                    'value': '(sizeOne < 0) ? sizeTwo : sizeOne + 1'
                },
                'type': 'int32[]'
            },
        ],
        'returns': 'int32'
    },
    'OutputArraysWithNarrowIntegerTypes': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'numberOfU16Samples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'u16Data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfU16Samples'
                },
                'type': 'myUInt16[]',
                'coerced': True
            },
            {
                'direction': 'in',
                'name': 'numberOfI16Samples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'i16Data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfI16Samples'
                },
                'type': 'myInt16[]',
                'coerced': True
            },
            {
                'direction': 'in',
                'name': 'numberOfI8Samples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'i8Data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfI8Samples'
                },
                'type': 'myInt8[]',
                'coerced': True
            },
        ],
        'returns': 'int32'
    },
    'InputArrayOfBytes': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'u8Array',
                'type': 'const myUInt8[]',
            },
        ],
        'returns': 'int32'
    },
    'OutputArrayOfBytes': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'numberOfU8Samples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'u8Data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfU8Samples'
                },
                'type': 'myUInt8[]',
            },
        ],
        'returns': 'int32'
    },
    'OutputArraysWithPassedInByPtrMechanism': {
        'parameters': [
            {
                'direction': 'out',
                'name': 'i32Data',
                'size': {
                    'mechanism': 'passed-in-by-ptr',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'out',
                'name': 'u16Data',
                'size': {
                    'mechanism': 'passed-in-by-ptr',
                    'value': 'arraySize'
                },
                'coerced': True,
                'type': 'myUInt16[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RegisterCallback': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'inputData',
                'type': 'myInt16'
            },
            {
                'callback_params': [
                    {
                        'direction': 'out',
                        'name': 'dataOut',
                        'type': 'myInt16'
                    },
                ],
                'direction': 'in',
                'include_in_proto': False,
                'name': 'callbackFunction',
                'type': 'CallbackPtr'
            },
            {
                'callback_token': True,
                'direction': 'out',
                'include_in_proto': False,
                'name': 'callbackData',
                'type': 'void'
            }
        ],
        'stream_response': True,
        'returns': 'int32'
    },
    'ReadStream': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'start',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'stop',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32'
            }
        ],
        'stream_response': True,
        'returns': 'int32'
    },
    'InputTimestamp': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'when',
                'type': 'CVIAbsoluteTime',
                'grpc_type': 'google.protobuf.Timestamp',
            },
        ],
        'returns': 'int32'
    },
    'OutputTimestamp': {
        'parameters': [
            {
                'direction': 'out',
                'name': 'when',
                'type': 'CVIAbsoluteTime',
                'grpc_type': 'google.protobuf.Timestamp',
            },
        ],
        'returns': 'int32'
    },
    'InputVarArgs': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'inputName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'repeating_argument': True,
                'name': 'channelName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'repeating_argument': True,
                'enum': 'BeautifulColor',
                'name': 'color',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'repeating_argument': True,
                'name': 'powerUpState',
                'type': 'double'
            },
            {
                'direction': 'in',
                'repeated_var_args': True,
                'name': 'stringAndEnums',
                'is_compound_type': True,
                'grpc_type': 'repeated StringAndEnum',
                'max_length': 3
            }
        ],
        'returns': 'int32'
    },
    'OutputVarArgs': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'inputName',
                'type': 'const char[]'
            },
            {
                'direction': 'in',
                'include_in_proto': False,
                'repeating_argument': True,
                'name': 'channelName',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'repeating_argument': True,
                'enum': 'BeautifulColor',
                'name': 'color',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'repeated_var_args': True,
                'name': 'channelNames',
                'grpc_type': 'repeated string',
                'max_length': 3
            },
            {
                'direction': 'out',
                'repeated_var_args': True,
                'name': 'colors',
                'grpc_type': 'repeated BeautifulColor',
                'max_length': 4
            }
        ],
        'returns': 'int32'
    },
    'ResetMarbleAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'MarbleAttribute',
                'name': 'attribute',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ScalarsWithNarrowIntegerTypes': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'u16',
                'type': 'myUInt16',
                'coerced': True
            },
            {
                'direction': 'in',
                'name': 'i16',
                'type': 'myInt16',
                'coerced': True
            },
            {
                'direction': 'in',
                'name': 'i8',
                'type': 'myInt8',
                'coerced': True
            }
        ],
        'returns': 'int32'
    },
    'SetMarbleAttributeDouble': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'MarbleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'double'
            },
        ],
        'returns': 'int32'
    },
    'SetMarbleAttributeInt32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'handle',
                'type': 'FakeHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'MarbleAttribute',
                'name': 'attribute',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32'
            },
        ],
        'returns': 'int32'
    },
    'SetColors': {
        'parameters': [
            {
                'direction': 'in',
                'enum': 'BeautifulColor',
                'name': 'colors',
                'type': 'int32[]',
                'size': {
                    'mechanism': 'fixed',
                    'value': '3'
                }
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetStructsWithCoercion': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'numberOfStructs',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'structs',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfStructs'
                },
                'type': 'struct StructWithCoercion_struct[]',
                'grpc_type': 'repeated StructWithCoercion'
            },
        ],
        'returns': 'int32'
    },
    'SetStructsWithCoercion': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'structs',
                'type': 'struct StructWithCoercion_struct[]',
                'grpc_type': 'repeated StructWithCoercion',
                'size': {
                    'mechanism': 'fixed',
                    'value': '3'
                }
            },
        ],
        'returns': 'int32'
    },
    'InputStringValuedEnum': {
        'parameters': [
            {
                'direction': 'in',
                'enum': 'MobileOSNames',
                'name': 'aName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'WriteBooleanArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_type': 'repeated bool',
                'name': 'bools',
                'type': 'int32[]',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                }
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifake_non_ivi/functions_addon.py sha256=922ded788624b101252535134db6ef5bf80379a439189224bbb0a62344d00941 bytes=667 -->
## FILE: source/codegen/metadata/nifake_non_ivi/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifake_non_ivi/functions_addon.py`
- sha256: `922ded788624b101252535134db6ef5bf80379a439189224bbb0a62344d00941`
- bytes: 667

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

functions_validation_suppressions = {
    "InputArraysWithNarrowIntegerTypes": {
        "parameters": {
            "u16Array": ["ARRAY_PARAMETER_NEEDS_SIZE"],
            "i16Array": ["ARRAY_PARAMETER_NEEDS_SIZE"],
            "i8Array": ["ARRAY_PARAMETER_NEEDS_SIZE"],
        }
    },
    "InputArrayOfBytes": {
        "parameters": {
            "u8Array": ["ARRAY_PARAMETER_NEEDS_SIZE"],
        }
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/__init__.py sha256=4f7091ddacba9e112e08cde0cd52181f876a59f36f39519bc0c6d3ce904da0a4 bytes=714 -->
## FILE: source/codegen/metadata/nifgen/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/__init__.py`
- sha256: `4f7091ddacba9e112e08cde0cd52181f876a59f36f39519bc0c6d3ce904da0a4`
- bytes: 714

````python
from .functions import functions
from .functions_addon import functions_override_metadata
from .attributes import attributes
from .attributes_addon import attributes_override_metadata
from .enums import enums
from .enums_addon import enums_override_metadata
from .enums_addon import enums_validation_suppressions
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config" : config
}

metadata['functions'].update(functions_override_metadata)
metadata['attributes'].update(attributes_override_metadata)
metadata['enums'].update(enums_override_metadata)
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/attributes.py sha256=dfb0c6de505280940b0e224e19bf7cbe35039532a3a01fd2ca2e890d1bbe22e4 bytes=44909 -->
## FILE: source/codegen/metadata/nifgen/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/attributes.py`
- sha256: `dfb0c6de505280940b0e224e19bf7cbe35039532a3a01fd2ca2e890d1bbe22e4`
- bytes: 44909

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 26.0.0f146
attributes = {
    1050002: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050004: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'CACHE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050005: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'SIMULATE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050006: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'RECORD_COERCIONS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050007: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DRIVER_SETUP',
        'resettable': True,
        'type': 'ViString'
    },
    1050021: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'INTERCHANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050203: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050327: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050503: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050504: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050510: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150001: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'ID_QUERY_RESPONSE',
        'resettable': True,
        'type': 'ViString'
    },
    1150101: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DIGITAL_PATTERN_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150102: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DIGITAL_FILTER_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150103: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'ANALOG_FILTER_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150104: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FILTER_CORRECTION_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150105: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SYNC_DUTY_CYCLE_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150106: {
        'codegen_method': 'public',
        'enum': 'UpdateClockSource',
        'grpc_type': 'sint32',
        'name': 'UPDATE_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150107: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'REF_CLOCK_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150108: {
        'codegen_method': 'public',
        'enum': 'TriggerMode',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150110: {
        'codegen_method': 'public',
        'enum': 'ClockMode',
        'grpc_type': 'sint32',
        'name': 'CLOCK_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150111: {
        'codegen_method': 'public',
        'enum': 'SynchronizationSource',
        'grpc_type': 'sint32',
        'name': 'SYNCHRONIZATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150112: {
        'codegen_method': 'public',
        'enum': 'SampleClockSource',
        'grpc_type': 'string',
        'name': 'SAMPLE_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150113: {
        'codegen_method': 'public',
        'enum': 'ReferenceClockSource',
        'grpc_type': 'string',
        'name': 'REFERENCE_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150208: {
        'codegen_method': 'public',
        'enum': 'FrequencyListHandle',
        'grpc_type': 'sint32',
        'name': 'FREQ_LIST_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150209: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MAX_NUM_FREQ_LISTS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150210: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MIN_FREQ_LIST_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150211: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MAX_FREQ_LIST_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150212: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MIN_FREQ_LIST_DURATION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150213: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MAX_FREQ_LIST_DURATION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150214: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FREQ_LIST_DURATION_QUANTUM',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150215: {
        'codegen_method': 'public',
        'enum': 'BusType',
        'grpc_type': 'sint32',
        'name': 'BUS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150216: {
        'codegen_method': 'public',
        'enum': 'VideoWaveformType',
        'grpc_type': 'sint32',
        'name': 'VIDEO_WAVEFORM_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150218: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DIGITAL_FILTER_INTERPOLATION_FACTOR',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150219: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'EXPORTED_SAMPLE_CLOCK_DIVISOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150220: {
        'codegen_method': 'public',
        'enum': 'LoadImpedance',
        'grpc_type': 'double',
        'name': 'LOAD_IMPEDANCE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150222: {
        'codegen_method': 'public',
        'enum': 'AnalogPath',
        'grpc_type': 'sint32',
        'name': 'ANALOG_PATH',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150223: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'GAIN_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150224: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'OFFSET_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150225: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'OSCILLATOR_FREQ_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150228: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'PRE_AMPLIFIER_ATTENUATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150229: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'POST_AMPLIFIER_ATTENUATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150230: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150231: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SAMPLE_CLOCK_ABSOLUTE_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150232: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'OSCILLATOR_PHASE_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150233: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'EXTERNAL_CLOCK_DELAY_BINARY_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150234: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ANALOG_DATA_MASK',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150235: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ANALOG_STATIC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150236: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_DATA_MASK',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150237: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_STATIC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150238: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FUNC_BUFFER_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150239: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FUNC_MAX_BUFFER_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150240: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'FILE_TRANSFER_BLOCK_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150241: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150242: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MEMORY_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150243: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150244: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DIRECT_DMA_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150245: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DIRECT_DMA_WINDOW_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150246: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OSP_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150247: {
        'codegen_method': 'public',
        'enum': 'DataProcessingMode',
        'grpc_type': 'sint32',
        'name': 'OSP_DATA_PROCESSING_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150248: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_IQ_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150249: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OSP_CARRIER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150250: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_CARRIER_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150251: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_CARRIER_PHASE_I',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150252: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_CARRIER_PHASE_Q',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150253: {
        'codegen_method': 'public',
        'enum': 'FilterType',
        'grpc_type': 'sint32',
        'name': 'OSP_FIR_FILTER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150254: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DIGITAL_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150255: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OSP_FIR_FILTER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150256: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_FIR_FILTER_INTERPOLATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150257: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OSP_CIC_FILTER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150258: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_CIC_FILTER_INTERPOLATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150259: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150260: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_FIR_FILTER_RAISED_COSINE_ALPHA',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150261: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_FIR_FILTER_FLAT_PASSBAND',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150262: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_FIR_FILTER_GAUSSIAN_BT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150263: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_CIC_FILTER_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150264: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_PRE_FILTER_GAIN_I',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150265: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_PRE_FILTER_GAIN_Q',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150266: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_PRE_FILTER_OFFSET_I',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150267: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_PRE_FILTER_OFFSET_Q',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150268: {
        'codegen_method': 'public',
        'enum': 'OspOverflowErrorReporting',
        'grpc_type': 'sint32',
        'name': 'OSP_OVERFLOW_ERROR_REPORTING',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150269: {
        'codegen_method': 'public',
        'enum': 'OspOverflowStatus',
        'grpc_type': 'sint32',
        'name': 'OSP_OVERFLOW_STATUS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150270: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SCRIPT_TO_GENERATE',
        'resettable': False,
        'type': 'ViString'
    },
    1150271: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MARKER_EVENTS_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150272: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'SCRIPT_TRIGGERS_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150273: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DATA_MARKER_EVENTS_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150274: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DIRECT_DMA_WINDOW_ADDRESS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150280: {
        'codegen_method': 'public',
        'enum': 'StartTriggerType',
        'grpc_type': 'sint32',
        'name': 'START_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150281: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150282: {
        'codegen_method': 'public',
        'enum': 'StartTriggerDigitalEdgeEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150283: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150290: {
        'codegen_method': 'public',
        'enum': 'ScriptTriggerType',
        'grpc_type': 'sint32',
        'name': 'SCRIPT_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150291: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150292: {
        'codegen_method': 'public',
        'enum': 'ScriptTriggerDigitalEdgeEdge',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150293: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150294: {
        'codegen_method': 'public',
        'enum': 'ScriptTriggerDigitalLevelActiveLevel',
        'grpc_type': 'sint32',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150295: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150310: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150311: {
        'codegen_method': 'public',
        'enum': 'ReadyForStartEventActiveLevel',
        'grpc_type': 'sint32',
        'name': 'READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150312: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'MARKER_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150313: {
        'codegen_method': 'public',
        'enum': 'MarkerEventPulsePolarity',
        'grpc_type': 'sint32',
        'name': 'MARKER_EVENT_PULSE_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150314: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'STARTED_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150315: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DONE_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150316: {
        'codegen_method': 'public',
        'enum': 'StartedEventActiveLevel',
        'grpc_type': 'sint32',
        'name': 'STARTED_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150317: {
        'codegen_method': 'public',
        'enum': 'DoneEventActiveLevel',
        'grpc_type': 'sint32',
        'name': 'DONE_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150318: {
        'codegen_method': 'public',
        'enum': 'StartedEventPulsePolarity',
        'grpc_type': 'sint32',
        'name': 'STARTED_EVENT_PULSE_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150319: {
        'codegen_method': 'public',
        'enum': 'DoneEventPulsePolarity',
        'grpc_type': 'sint32',
        'name': 'DONE_EVENT_PULSE_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150320: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150321: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150322: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150323: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'FLATNESS_CORRECTION_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150324: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'STREAMING_WAVEFORM_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150325: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'STREAMING_SPACE_AVAILABLE_IN_WAVEFORM',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150326: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'STREAMING_WAVEFORM_NAME',
        'resettable': True,
        'type': 'ViString'
    },
    1150327: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ARB_MARKER_POSITION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150328: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ARB_REPEAT_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150329: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150330: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'SYNC_OUT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150331: {
        'codegen_method': 'public',
        'enum': 'StartedEventOutputBehavior',
        'grpc_type': 'sint32',
        'name': 'STARTED_EVENT_OUTPUT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150332: {
        'codegen_method': 'public',
        'enum': 'DoneEventOutputBehavior',
        'grpc_type': 'sint32',
        'name': 'DONE_EVENT_OUTPUT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150333: {
        'codegen_method': 'public',
        'enum': 'StartedEventPulseWidthUnits',
        'grpc_type': 'sint32',
        'name': 'STARTED_EVENT_PULSE_WIDTH_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150334: {
        'codegen_method': 'public',
        'enum': 'DoneEventPulseWidthUnits',
        'grpc_type': 'sint32',
        'name': 'DONE_EVENT_PULSE_WIDTH_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150335: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'STARTED_EVENT_PULSE_WIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150336: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DONE_EVENT_PULSE_WIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150337: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DATA_MARKER_EVENT_DATA_BIT_NUMBER',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150338: {
        'codegen_method': 'public',
        'enum': 'DataMarkerEventLevelPolarity',
        'grpc_type': 'sint32',
        'name': 'DATA_MARKER_EVENT_LEVEL_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150339: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'DATA_MARKER_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150340: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MARKER_EVENT_PULSE_WIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150341: {
        'codegen_method': 'public',
        'enum': 'MarkerEventPulseWidthUnits',
        'grpc_type': 'sint32',
        'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150342: {
        'codegen_method': 'public',
        'enum': 'MarkerEventOutputBehavior',
        'grpc_type': 'sint32',
        'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150343: {
        'codegen_method': 'public',
        'enum': 'MarkerEventToggleInitialState',
        'grpc_type': 'sint32',
        'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150344: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ALL_MARKER_EVENTS_LIVE_STATUS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150345: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'MARKER_EVENT_LIVE_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150348: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'READY_FOR_START_EVENT_LIVE_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150349: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'ALL_MARKER_EVENTS_LATCHED_STATUS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150350: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'MARKER_EVENT_LATCHED_STATUS',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150351: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'DONE_EVENT_LATCHED_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150352: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'STARTED_EVENT_LATCHED_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150354: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'MARKER_EVENT_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150355: {
        'codegen_method': 'public',
        'enum': 'MarkerEventDelayUnits',
        'grpc_type': 'sint32',
        'name': 'MARKER_EVENT_DELAY_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150356: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'STARTED_EVENT_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150357: {
        'codegen_method': 'public',
        'enum': 'StartedEventDelayUnits',
        'grpc_type': 'sint32',
        'name': 'STARTED_EVENT_DELAY_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150358: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DONE_EVENT_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150359: {
        'codegen_method': 'public',
        'enum': 'DoneEventDelayUnits',
        'grpc_type': 'sint32',
        'name': 'DONE_EVENT_DELAY_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150362: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'PCI_DMA_OPTIMIZATIONS_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150365: {
        'codegen_method': 'public',
        'enum': 'TerminalConfiguration',
        'grpc_type': 'sint32',
        'name': 'TERMINAL_CONFIGURATION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150366: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'COMMON_MODE_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150367: {
        'codegen_method': 'public',
        'enum': 'SampleClockTimebaseSource',
        'grpc_type': 'string',
        'name': 'SAMPLE_CLOCK_TIMEBASE_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150368: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'SAMPLE_CLOCK_TIMEBASE_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150369: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'CHANNEL_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150370: {
        'codegen_method': 'public',
        'enum': 'OspMode',
        'grpc_type': 'sint32',
        'name': 'OSP_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150371: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'OSP_FREQUENCY_SHIFT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150373: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150374: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150375: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150376: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'EXTERNAL_SAMPLE_CLOCK_MULTIPLIER',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150377: {
        'codegen_method': 'public',
        'enum': 'IdleBehavior',
        'grpc_type': 'sint32',
        'name': 'IDLE_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150378: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'IDLE_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150379: {
        'codegen_method': 'public',
        'enum': 'WaitBehavior',
        'grpc_type': 'sint32',
        'name': 'WAIT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150380: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'WAIT_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150389: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150390: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'MODULE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150391: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'P2P_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150392: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'P2P_DESTINATION_CHANNELS',
        'resettable': False,
        'type': 'ViString'
    },
    1150393: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_ENDPOINT_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150394: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_SPACE_AVAILABLE_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150395: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150396: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_ENDPOINT_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150397: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'P2P_MANUAL_CONFIGURATION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150398: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_ADDRESS',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150399: {
        'codegen_method': 'public',
        'enum': 'AddressType',
        'grpc_type': 'sint32',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150400: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INTERVAL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150401: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_ENDPOINT_WINDOW_ADDRESS',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150402: {
        'codegen_method': 'public',
        'enum': 'AddressType',
        'grpc_type': 'sint32',
        'name': 'P2P_ENDPOINT_WINDOW_ADDRESS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150403: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_ENDPOINT_WINDOW_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150405: {
        'codegen_method': 'public',
        'grpc_type': 'int64',
        'name': 'P2P_DONE_NOTIFICATION_ADDRESS',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150406: {
        'codegen_method': 'public',
        'enum': 'AddressType',
        'grpc_type': 'sint32',
        'name': 'P2P_DONE_NOTIFICATION_ADDRESS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150407: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_DONE_NOTIFICATION_VALUE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150408: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150409: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'STREAMING_WRITE_TIMEOUT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150410: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150411: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'AUX_POWER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150412: {
        'codegen_method': 'public',
        'grpc_type': 'string',
        'name': 'FPGA_BITFILE_PATH',
        'resettable': False,
        'type': 'ViString'
    },
    1150413: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ABSOLUTE_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250001: {
        'codegen_method': 'public',
        'enum': 'OutputMode',
        'grpc_type': 'sint32',
        'name': 'OUTPUT_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250003: {
        'codegen_method': 'public',
        'grpc_type': 'bool',
        'name': 'OUTPUT_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1250004: {
        'codegen_method': 'public',
        'enum': 'OutputImpedance',
        'grpc_type': 'double',
        'name': 'OUTPUT_IMPEDANCE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250101: {
        'codegen_method': 'public',
        'enum': 'Waveform',
        'grpc_type': 'sint32',
        'name': 'FUNC_WAVEFORM',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250102: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FUNC_AMPLITUDE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250103: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FUNC_DC_OFFSET',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250104: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FUNC_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250105: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FUNC_START_PHASE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250106: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'FUNC_DUTY_CYCLE_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250201: {
        'codegen_method': 'public',
        'enum': 'ArbitraryWaveformHandle',
        'grpc_type': 'sint32',
        'name': 'ARB_WAVEFORM_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250202: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ARB_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250203: {
        'codegen_method': 'public',
        'grpc_type': 'double',
        'name': 'ARB_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250204: {
        'codegen_method': 'public',
        'enum': 'SampleRate',
        'grpc_type': 'double',
        'name': 'ARB_SAMPLE_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250205: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MAX_NUM_WAVEFORMS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250206: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'WAVEFORM_QUANTUM',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250207: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MIN_WAVEFORM_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250208: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MAX_WAVEFORM_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250211: {
        'codegen_method': 'public',
        'enum': 'ArbitrarySequenceHandle',
        'grpc_type': 'sint32',
        'name': 'ARB_SEQUENCE_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250212: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MAX_NUM_SEQUENCES',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250213: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MIN_SEQUENCE_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250214: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MAX_SEQUENCE_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250215: {
        'codegen_method': 'public',
        'grpc_type': 'sint32',
        'name': 'MAX_LOOP_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250302: {
        'codegen_method': 'public',
        'enum': 'TriggerSource',
        'grpc_type': 'sint32',
        'name': 'TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250350: {
        'codegen_method': 'public',
        'enum': 'BurstCount',
        'grpc_type': 'sint32',
        'name': 'BURST_COUNT',
        'resettable': True,
        'type': 'ViInt32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nifgen/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/config.py sha256=ae31b81612c4c7833405d58ce781dd1106d83d2c66c3c0bd6a5d1b9e9e3ed63e bytes=1158 -->
## FILE: source/codegen/metadata/nifgen/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/config.py`
- sha256: `ae31b81612c4c7833405d58ce781dd1106d83d2c66c3c0bd6a5d1b9e9e3ed63e`
- bytes: 1158

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 26.0.0f146
config = {
    'additional_headers': {
        'custom/ivi_errors.h': [
            'service.cpp'
        ]
    },
    'api_version': '26.0.0f146',
    'c_function_prefix': 'niFgen_',
    'c_header': 'niFgen.h',
    'close_function': 'Close',
    'csharp_namespace': 'NationalInstruments.Grpc.Fgen',
    'custom_types': [
    ],
    'driver_name': 'NI-FGEN',
    'java_package': 'com.ni.grpc.fgen',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nifgen',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niFgen_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niFgen_64.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'module_name': 'nifgen',
    'namespace_component': 'nifgen',
    'service_class_prefix': 'NiFgen',
    'session_handle_parameter_name': 'vi',
    'status_ok': 'status >= 0'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/config_addon.py sha256=ab226f65092356895748859400d84500ff52b274f9db5cfe4c818b32037079e1 bytes=226 -->
## FILE: source/codegen/metadata/nifgen/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/config_addon.py`
- sha256: `ab226f65092356895748859400d84500ff52b274f9db5cfe4c818b32037079e1`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.4.dev0',
    'latest_runtime_version_tested_against': '20.0.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/enums.py sha256=76618d74d2460391bd2a9d6a134f2207d067de480e9cc7f3f46cbffd4a039ac4 bytes=65102 -->
## FILE: source/codegen/metadata/nifgen/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/enums.py`
- sha256: `76618d74d2460391bd2a9d6a134f2207d067de480e9cc7f3f46cbffd4a039ac4`
- bytes: 65102

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 26.0.0f146
enums = {
    'AddressType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_ADDR_VIRTUAL',
                'value': 1
            }
        ]
    },
    'AnalogPath': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_MAIN_ANALOG_PATH',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_DIRECT_ANALOG_PATH',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_FIXED_LOW_GAIN_ANALOG_PATH',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_FIXED_HIGH_GAIN_ANALOG_PATH',
                'value': 3
            }
        ]
    },
    'ArbitrarySequenceHandle': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_FIRST_SEQUENCE_HANDLE',
                'value': 100000
            },
            {
                'name': 'NIFGEN_VAL_LAST_SEQUENCE_HANDLE',
                'value': 109999
            },
            {
                'name': 'NIFGEN_VAL_NO_SEQUENCE',
                'value': -1
            }
        ]
    },
    'ArbitraryWaveformHandle': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_FIRST_WAVEFORM_HANDLE',
                'value': 10000
            },
            {
                'name': 'NIFGEN_VAL_LAST_WAVEFORM_HANDLE',
                'value': 10999
            },
            {
                'name': 'NIFGEN_VAL_NO_WAVEFORM',
                'value': -1
            }
        ]
    },
    'BurstCount': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_GENERATE_CONTINUOUS',
                'value': -1
            }
        ]
    },
    'BusType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_BUS_INVALID',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_BUS_AT',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_BUS_PCI',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_BUS_PXI',
                'value': 3
            },
            {
                'name': 'NIFGEN_VAL_BUS_VXI',
                'value': 4
            },
            {
                'name': 'NIFGEN_VAL_BUS_PCMCIA',
                'value': 5
            },
            {
                'name': 'NIFGEN_VAL_BUS_PXIE',
                'value': 6
            }
        ]
    },
    'ByteOrder': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_LITTLE_ENDIAN',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_BIG_ENDIAN',
                'value': 1
            }
        ]
    },
    'ClockMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_HIGH_RESOLUTION',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_DIVIDE_DOWN',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_AUTOMATIC',
                'value': 2
            }
        ]
    },
    'DataMarkerEventLevelPolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DataProcessingMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_OSP_REAL',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_OSP_COMPLEX',
                'value': 1
            }
        ]
    },
    'DoneEventActiveLevel': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DoneEventDelayUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'DoneEventOutputBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            }
        ]
    },
    'DoneEventPulsePolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'DoneEventPulseWidthUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'FilterType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_OSP_FLAT',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_OSP_RAISED_COSINE',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_OSP_ROOT_RAISED_COSINE',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_OSP_GAUSSIAN',
                'value': 3
            },
            {
                'name': 'NIFGEN_VAL_OSP_CUSTOM',
                'value': 4
            }
        ]
    },
    'FrequencyListHandle': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_FIRST_FREQ_LIST_HANDLE',
                'value': 200000
            },
            {
                'name': 'NIFGEN_VAL_LAST_FREQ_LIST_HANDLE',
                'value': 209999
            },
            {
                'name': 'NIFGEN_VAL_NO_FREQ_LIST',
                'value': -1
            }
        ]
    },
    'FrequencyListOptions': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ALL_FLISTS',
                'value': -1
            }
        ]
    },
    'HardwareState': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_IDLE',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_WAITING_FOR_START_TRIGGER',
                'value': 100
            },
            {
                'name': 'NIFGEN_VAL_RUNNING',
                'value': 200
            },
            {
                'name': 'NIFGEN_VAL_DONE',
                'value': 600
            },
            {
                'name': 'NIFGEN_VAL_HARDWARE_ERROR',
                'value': 1000
            }
        ]
    },
    'IdleBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'name': 'NIFGEN_VAL_JUMP_TO_VALUE',
                'value': 401
            }
        ]
    },
    'LoadImpedance': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE',
                'value': -1
            }
        ]
    },
    'MarkerEventDelayUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'MarkerEventOutputBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            },
            {
                'name': 'NIFGEN_VAL_TOGGLE',
                'value': 103
            }
        ]
    },
    'MarkerEventPulsePolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'MarkerEventPulseWidthUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'MarkerEventToggleInitialState': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_LOW',
                'value': 102
            }
        ]
    },
    'NiFgenInt32AttributeValues': {
        'enum-value-prefix': 'NIFGEN_INT32',
        'generate-mappings': False,
        'values': [
            {
                'name': 'ADDRESS_TYPE_VAL_ADDR_PHYSICAL',
                'value': 0
            },
            {
                'name': 'ADDRESS_TYPE_VAL_ADDR_VIRTUAL',
                'value': 1
            },
            {
                'name': 'ANALOG_PATH_VAL_MAIN_ANALOG_PATH',
                'value': 0
            },
            {
                'name': 'ANALOG_PATH_VAL_DIRECT_ANALOG_PATH',
                'value': 1
            },
            {
                'name': 'ANALOG_PATH_VAL_FIXED_LOW_GAIN_ANALOG_PATH',
                'value': 2
            },
            {
                'name': 'ANALOG_PATH_VAL_FIXED_HIGH_GAIN_ANALOG_PATH',
                'value': 3
            },
            {
                'name': 'ARBITRARY_SEQUENCE_HANDLE_VAL_FIRST_SEQUENCE_HANDLE',
                'value': 100000
            },
            {
                'name': 'ARBITRARY_SEQUENCE_HANDLE_VAL_LAST_SEQUENCE_HANDLE',
                'value': 109999
            },
            {
                'name': 'ARBITRARY_SEQUENCE_HANDLE_VAL_NO_SEQUENCE',
                'value': -1
            },
            {
                'name': 'ARBITRARY_WAVEFORM_HANDLE_VAL_FIRST_WAVEFORM_HANDLE',
                'value': 10000
            },
            {
                'name': 'ARBITRARY_WAVEFORM_HANDLE_VAL_LAST_WAVEFORM_HANDLE',
                'value': 10999
            },
            {
                'name': 'ARBITRARY_WAVEFORM_HANDLE_VAL_NO_WAVEFORM',
                'value': -1
            },
            {
                'name': 'BURST_COUNT_VAL_GENERATE_CONTINUOUS',
                'value': -1
            },
            {
                'name': 'BUS_TYPE_VAL_BUS_INVALID',
                'value': 0
            },
            {
                'name': 'BUS_TYPE_VAL_BUS_AT',
                'value': 1
            },
            {
                'name': 'BUS_TYPE_VAL_BUS_PCI',
                'value': 2
            },
            {
                'name': 'BUS_TYPE_VAL_BUS_PXI',
                'value': 3
            },
            {
                'name': 'BUS_TYPE_VAL_BUS_VXI',
                'value': 4
            },
            {
                'name': 'BUS_TYPE_VAL_BUS_PCMCIA',
                'value': 5
            },
            {
                'name': 'BUS_TYPE_VAL_BUS_PXIE',
                'value': 6
            },
            {
                'name': 'CLOCK_MODE_VAL_HIGH_RESOLUTION',
                'value': 0
            },
            {
                'name': 'CLOCK_MODE_VAL_DIVIDE_DOWN',
                'value': 1
            },
            {
                'name': 'CLOCK_MODE_VAL_AUTOMATIC',
                'value': 2
            },
            {
                'name': 'DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'DATA_PROCESSING_MODE_VAL_OSP_REAL',
                'value': 0
            },
            {
                'name': 'DATA_PROCESSING_MODE_VAL_OSP_COMPLEX',
                'value': 1
            },
            {
                'name': 'DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'DONE_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'DONE_EVENT_DELAY_UNITS_VAL_SECONDS',
                'value': 102
            },
            {
                'name': 'DONE_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE',
                'value': 101
            },
            {
                'name': 'DONE_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL',
                'value': 102
            },
            {
                'name': 'DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS',
                'value': 102
            },
            {
                'name': 'FILTER_TYPE_VAL_OSP_FLAT',
                'value': 0
            },
            {
                'name': 'FILTER_TYPE_VAL_OSP_RAISED_COSINE',
                'value': 1
            },
            {
                'name': 'FILTER_TYPE_VAL_OSP_ROOT_RAISED_COSINE',
                'value': 2
            },
            {
                'name': 'FILTER_TYPE_VAL_OSP_GAUSSIAN',
                'value': 3
            },
            {
                'name': 'FILTER_TYPE_VAL_OSP_CUSTOM',
                'value': 4
            },
            {
                'name': 'FREQUENCY_LIST_HANDLE_VAL_FIRST_FREQ_LIST_HANDLE',
                'value': 200000
            },
            {
                'name': 'FREQUENCY_LIST_HANDLE_VAL_LAST_FREQ_LIST_HANDLE',
                'value': 209999
            },
            {
                'name': 'FREQUENCY_LIST_HANDLE_VAL_NO_FREQ_LIST',
                'value': -1
            },
            {
                'name': 'IDLE_BEHAVIOR_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'name': 'IDLE_BEHAVIOR_VAL_JUMP_TO_VALUE',
                'value': 401
            },
            {
                'name': 'MARKER_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'MARKER_EVENT_DELAY_UNITS_VAL_SECONDS',
                'value': 102
            },
            {
                'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE',
                'value': 101
            },
            {
                'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL',
                'value': 102
            },
            {
                'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_TOGGLE',
                'value': 103
            },
            {
                'name': 'MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS',
                'value': 102
            },
            {
                'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_HIGH',
                'value': 101
            },
            {
                'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_LOW',
                'value': 102
            },
            {
                'name': 'OSP_MODE_VAL_OSP_IF',
                'value': 0
            },
            {
                'name': 'OSP_MODE_VAL_OSP_BASEBAND',
                'value': 1
            },
            {
                'name': 'OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'name': 'OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_NONE',
                'value': 0
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I',
                'value': 1
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q',
                'value': 2
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I',
                'value': 4
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q',
                'value': 8
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_I',
                'value': 16
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_I',
                'value': 16
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_Q',
                'value': 32
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_Q',
                'value': 32
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_I',
                'value': 64
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_Q',
                'value': 128
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_COMPLEX_DATA',
                'value': 256
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_I',
                'value': 512
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_Q',
                'value': 1024
            },
            {
                'name': 'OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_EQUALIZER',
                'value': 2048
            },
            {
                'name': 'OUTPUT_MODE_VAL_OUTPUT_FUNC',
                'value': 0
            },
            {
                'name': 'OUTPUT_MODE_VAL_OUTPUT_ARB',
                'value': 1
            },
            {
                'name': 'OUTPUT_MODE_VAL_OUTPUT_SEQ',
                'value': 2
            },
            {
                'name': 'OUTPUT_MODE_VAL_OUTPUT_FREQ_LIST',
                'value': 101
            },
            {
                'name': 'OUTPUT_MODE_VAL_OUTPUT_SCRIPT',
                'value': 102
            },
            {
                'name': 'READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'name': 'SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE',
                'value': 102
            },
            {
                'name': 'SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'SCRIPT_TRIGGER_TYPE_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'name': 'SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'name': 'SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_LEVEL',
                'value': 103
            },
            {
                'name': 'SCRIPT_TRIGGER_TYPE_VAL_SOFTWARE_EDGE',
                'value': 104
            },
            {
                'name': 'START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'name': 'START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE',
                'value': 102
            },
            {
                'name': 'START_TRIGGER_TYPE_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'name': 'START_TRIGGER_TYPE_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'name': 'START_TRIGGER_TYPE_VAL_SOFTWARE_EDGE',
                'value': 104
            },
            {
                'name': 'START_TRIGGER_TYPE_VAL_P2P_ENDPOINT_FULLNESS',
                'value': 106
            },
            {
                'name': 'STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'STARTED_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'STARTED_EVENT_DELAY_UNITS_VAL_SECONDS',
                'value': 102
            },
            {
                'name': 'STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE',
                'value': 101
            },
            {
                'name': 'STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL',
                'value': 102
            },
            {
                'name': 'STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW',
                'value': 102
            },
            {
                'name': 'STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS',
                'value': 102
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'SYNCHRONIZATION_SOURCE_VAL_NONE',
                'value': 1000
            },
            {
                'name': 'TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED',
                'value': 300
            },
            {
                'name': 'TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL',
                'value': 301
            },
            {
                'name': 'TRIGGER_MODE_VAL_SINGLE',
                'value': 1
            },
            {
                'name': 'TRIGGER_MODE_VAL_CONTINUOUS',
                'value': 2
            },
            {
                'name': 'TRIGGER_MODE_VAL_STEPPED',
                'value': 3
            },
            {
                'name': 'TRIGGER_MODE_VAL_BURST',
                'value': 4
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_IMMEDIATE',
                'value': 0
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_EXTERNAL',
                'value': 1
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_SOFTWARE_TRIG',
                'value': 2
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_0',
                'value': 1011
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_1',
                'value': 1012
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_2',
                'value': 1013
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_PFI_3',
                'value': 1014
            },
            {
                'name': 'TRIGGER_SOURCE_VAL_OTHER_TERMINAL',
                'value': 1018
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_INTERNAL',
                'value': 0
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_EXTERNAL',
                'value': 1
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_OTHER_TERMINAL',
                'value': 1018
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_CLK_IN',
                'value': 1202
            },
            {
                'name': 'UPDATE_CLOCK_SOURCE_VAL_DDC_CLK_IN',
                'value': 1203
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_PAL_B',
                'value': 0
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_PAL_D',
                'value': 1
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_PAL_G',
                'value': 2
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_PAL_H',
                'value': 3
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_PAL_I',
                'value': 4
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_PAL_M',
                'value': 5
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_PAL_N',
                'value': 6
            },
            {
                'name': 'VIDEO_WAVEFORM_TYPE_VAL_NTSC_M',
                'value': 7
            },
            {
                'name': 'WAIT_BEHAVIOR_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'name': 'WAIT_BEHAVIOR_VAL_JUMP_TO_VALUE',
                'value': 401
            },
            {
                'name': 'WAVEFORM_VAL_WFM_SINE',
                'value': 1
            },
            {
                'name': 'WAVEFORM_VAL_WFM_SQUARE',
                'value': 2
            },
            {
                'name': 'WAVEFORM_VAL_WFM_TRIANGLE',
                'value': 3
            },
            {
                'name': 'WAVEFORM_VAL_WFM_RAMP_UP',
                'value': 4
            },
            {
                'name': 'WAVEFORM_VAL_WFM_RAMP_DOWN',
                'value': 5
            },
            {
                'name': 'WAVEFORM_VAL_WFM_DC',
                'value': 6
            },
            {
                'name': 'WAVEFORM_VAL_WFM_NOISE',
                'value': 101
            },
            {
                'name': 'WAVEFORM_VAL_WFM_USER',
                'value': 102
            }
        ]
    },
    'NiFgenReal64AttributeValues': {
        'enum-value-prefix': 'NIFGEN_REAL64',
        'generate-mappings': False,
        'values': [
            {
                'name': 'LOAD_IMPEDANCE_VAL_MATCHED_LOAD_IMPEDANCE',
                'value': -1
            },
            {
                'name': 'OUTPUT_IMPEDANCE_VAL_50_OHMS',
                'value': 50
            },
            {
                'name': 'OUTPUT_IMPEDANCE_VAL_75_OHMS',
                'value': 75
            },
            {
                'name': 'SAMPLE_RATE_VAL_EXTERNAL_SAMPLE_RATE',
                'value': -1
            }
        ]
    },
    'NiFgenStringAttributeValuesMapped': {
        'enum-value-prefix': 'NIFGEN_STRING',
        'generate-mappings': True,
        'values': [
            {
                'name': 'REFERENCE_CLOCK_SOURCE_VAL_CLOCK_IN_COLLISION_AVOIDANCE',
                'value': 'ClkIn'
            },
            {
                'name': 'REFERENCE_CLOCK_SOURCE_VAL_NONE_COLLISION_AVOIDANCE',
                'value': 'None'
            },
            {
                'name': 'REFERENCE_CLOCK_SOURCE_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE',
                'value': 'OnboardRefClk'
            },
            {
                'name': 'REFERENCE_CLOCK_SOURCE_VAL_PXI_CLOCK_COLLISION_AVOIDANCE',
                'value': 'PXI_Clk'
            },
            {
                'name': 'REFERENCE_CLOCK_SOURCE_VAL_RTSI_7_COLLISION_AVOIDANCE',
                'value': 'RTSI7'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_DDC_CLOCK_IN',
                'value': 'DDC_ClkIn'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_STAR_LINE',
                'value': 'PXI_Star'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_0_RTSI_0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_1_RTSI_1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_2_RTSI_2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_3_RTSI_3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_4_RTSI_4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_5_RTSI_5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_6_RTSI_6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_7_RTSI_7',
                'value': 'PXI_Trig7'
            },
            {
                'name': 'SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'name': 'SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            }
        ]
    },
    'OspMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_OSP_IF',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_OSP_BASEBAND',
                'value': 1
            }
        ]
    },
    'OspOverflowErrorReporting': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ERROR_REPORTING_ERROR',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_ERROR_REPORTING_DISABLED',
                'value': 2
            }
        ]
    },
    'OspOverflowStatus': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_NONE',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I',
                'value': 4
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q',
                'value': 8
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_FIR_FILTER_I',
                'value': 16
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PFIR_FILTER_I',
                'value': 16
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_FIR_FILTER_Q',
                'value': 32
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_PFIR_FILTER_Q',
                'value': 32
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CIC_FILTER_I',
                'value': 64
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CIC_FILTER_Q',
                'value': 128
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_COMPLEX_DATA',
                'value': 256
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CFIR_FILTER_I',
                'value': 512
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_CFIR_FILTER_Q',
                'value': 1024
            },
            {
                'name': 'NIFGEN_VAL_OSP_OVERFLOW_EQUALIZER',
                'value': 2048
            }
        ]
    },
    'OutputImpedance': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_50_OHMS',
                'value': 50
            },
            {
                'name': 'NIFGEN_VAL_75_OHMS',
                'value': 75
            }
        ]
    },
    'OutputMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_OUTPUT_FUNC',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_OUTPUT_ARB',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_OUTPUT_SEQ',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_OUTPUT_FREQ_LIST',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_OUTPUT_SCRIPT',
                'value': 102
            }
        ]
    },
    'ReadyForStartEventActiveLevel': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'ReferenceClockSource': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NIFGEN_VAL_CLOCK_IN_COLLISION_AVOIDANCE',
                'value': 'ClkIn'
            },
            {
                'name': 'NIFGEN_VAL_NONE_COLLISION_AVOIDANCE',
                'value': 'None'
            },
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE',
                'value': 'OnboardRefClk'
            },
            {
                'name': 'NIFGEN_VAL_PXI_CLOCK_COLLISION_AVOIDANCE',
                'value': 'PXI_Clk'
            },
            {
                'name': 'NIFGEN_VAL_RTSI_7_COLLISION_AVOIDANCE',
                'value': 'RTSI7'
            }
        ]
    },
    'RelativeTo': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_START',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT',
                'value': 1
            }
        ]
    },
    'RouteSignalFrom': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_MARKER',
                'value': 1001
            },
            {
                'name': 'NIFGEN_VAL_SYNC_OUT',
                'value': 1002
            },
            {
                'name': 'NIFGEN_VAL_OUT_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_BOARD_CLOCK',
                'value': 1006
            },
            {
                'name': 'NIFGEN_VAL_SYNCHRONIZATION',
                'value': 1007
            },
            {
                'name': 'NIFGEN_VAL_SOFTWARE_TRIG',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_REF_OUT',
                'value': 1008
            },
            {
                'name': 'NIFGEN_VAL_CLOCK_OUT',
                'value': 1009
            },
            {
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'NIFGEN_VAL_PFI_0',
                'value': 1011
            },
            {
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                'value': 1019
            }
        ]
    },
    'RouteSignalTo': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'NIFGEN_VAL_REF_OUT',
                'value': 1008
            },
            {
                'name': 'NIFGEN_VAL_PFI_0',
                'value': 1011
            },
            {
                'name': 'NIFGEN_VAL_PFI_1',
                'value': 1012
            },
            {
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            }
        ]
    },
    'SampleClockSource': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NIFGEN_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'name': 'NIFGEN_VAL_DDC_CLOCK_IN',
                'value': 'DDC_ClkIn'
            },
            {
                'name': 'NIFGEN_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'name': 'NIFGEN_VAL_PXI_STAR_LINE',
                'value': 'PXI_Star'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_0_RTSI_0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_1_RTSI_1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_2_RTSI_2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_3_RTSI_3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_4_RTSI_4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_5_RTSI_5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_6_RTSI_6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'NIFGEN_VAL_PXI_TRIGGER_LINE_7_RTSI_7',
                'value': 'PXI_Trig7'
            }
        ]
    },
    'SampleClockTimebaseSource': {
        'codegen_method': 'public',
        'generate-mappings': True,
        'values': [
            {
                'name': 'NIFGEN_VAL_CLOCK_IN',
                'value': 'ClkIn'
            },
            {
                'name': 'NIFGEN_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            }
        ]
    },
    'SampleRate': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_EXTERNAL_SAMPLE_RATE',
                'value': -1
            }
        ]
    },
    'ScriptTriggerDigitalEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_FALLING_EDGE',
                'value': 102
            }
        ]
    },
    'ScriptTriggerDigitalLevelActiveLevel': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'ScriptTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'name': 'NIFGEN_VAL_DIGITAL_LEVEL',
                'value': 103
            },
            {
                'name': 'NIFGEN_VAL_SOFTWARE_EDGE',
                'value': 104
            }
        ]
    },
    'SequenceHandle': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ALL_SEQUENCES',
                'value': -1
            }
        ]
    },
    'Signal': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                'value': 1019
            },
            {
                'name': 'NIFGEN_VAL_SYNC_OUT',
                'value': 1002
            },
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_MARKER_EVENT',
                'value': 1001
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE',
                'value': 1006
            },
            {
                'name': 'NIFGEN_VAL_SYNCHRONIZATION',
                'value': 1007
            },
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_REFERENCE_CLOCK',
                'value': 102
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103
            },
            {
                'name': 'NIFGEN_VAL_READY_FOR_START_EVENT',
                'value': 105
            },
            {
                'name': 'NIFGEN_VAL_STARTED_EVENT',
                'value': 106
            },
            {
                'name': 'NIFGEN_VAL_DONE_EVENT',
                'value': 107
            },
            {
                'name': 'NIFGEN_VAL_DATA_MARKER_EVENT',
                'value': 108
            }
        ]
    },
    'StartTriggerDigitalEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_RISING_EDGE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_FALLING_EDGE',
                'value': 102
            }
        ]
    },
    'StartTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_TRIG_NONE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_DIGITAL_EDGE',
                'value': 102
            },
            {
                'name': 'NIFGEN_VAL_SOFTWARE_EDGE',
                'value': 104
            },
            {
                'name': 'NIFGEN_VAL_P2P_ENDPOINT_FULLNESS',
                'value': 106
            }
        ]
    },
    'StartedEventActiveLevel': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'StartedEventDelayUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'StartedEventOutputBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_PULSE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_LEVEL',
                'value': 102
            }
        ]
    },
    'StartedEventPulsePolarity': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'StartedEventPulseWidthUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_SECONDS',
                'value': 102
            }
        ]
    },
    'SynchronizationSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'NIFGEN_VAL_NONE',
                'value': 1000
            }
        ]
    },
    'TerminalConfiguration': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SINGLE_ENDED',
                'value': 300
            },
            {
                'name': 'NIFGEN_VAL_DIFFERENTIAL',
                'value': 301
            }
        ]
    },
    'Trigger': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_START_TRIGGER',
                'value': 1004
            },
            {
                'name': 'NIFGEN_VAL_SCRIPT_TRIGGER',
                'value': 103
            }
        ]
    },
    'TriggerMode': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_SINGLE',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_CONTINUOUS',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_STEPPED',
                'value': 3
            },
            {
                'name': 'NIFGEN_VAL_BURST',
                'value': 4
            }
        ]
    },
    'TriggerSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_IMMEDIATE',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_EXTERNAL',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_SOFTWARE_TRIG',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_TTL0',
                'value': 111
            },
            {
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'NIFGEN_VAL_PFI_0',
                'value': 1011
            },
            {
                'name': 'NIFGEN_VAL_PFI_1',
                'value': 1012
            },
            {
                'name': 'NIFGEN_VAL_PFI_2',
                'value': 1013
            },
            {
                'name': 'NIFGEN_VAL_PFI_3',
                'value': 1014
            },
            {
                'name': 'NIFGEN_VAL_OTHER_TERMINAL',
                'value': 1018
            }
        ]
    },
    'TriggerWhen': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ACTIVE_HIGH',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_ACTIVE_LOW',
                'value': 102
            }
        ]
    },
    'UpdateClockSource': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_INTERNAL',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_EXTERNAL',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_TTL1',
                'value': 112
            },
            {
                'name': 'NIFGEN_VAL_TTL2',
                'value': 113
            },
            {
                'name': 'NIFGEN_VAL_TTL3',
                'value': 114
            },
            {
                'name': 'NIFGEN_VAL_TTL4',
                'value': 115
            },
            {
                'name': 'NIFGEN_VAL_TTL5',
                'value': 116
            },
            {
                'name': 'NIFGEN_VAL_TTL6',
                'value': 117
            },
            {
                'name': 'NIFGEN_VAL_PXI_STAR',
                'value': 131
            },
            {
                'name': 'NIFGEN_VAL_RTSI_0',
                'value': 141
            },
            {
                'name': 'NIFGEN_VAL_RTSI_1',
                'value': 142
            },
            {
                'name': 'NIFGEN_VAL_RTSI_2',
                'value': 143
            },
            {
                'name': 'NIFGEN_VAL_RTSI_3',
                'value': 144
            },
            {
                'name': 'NIFGEN_VAL_RTSI_4',
                'value': 145
            },
            {
                'name': 'NIFGEN_VAL_RTSI_5',
                'value': 146
            },
            {
                'name': 'NIFGEN_VAL_RTSI_6',
                'value': 147
            },
            {
                'name': 'NIFGEN_VAL_RTSI_7',
                'value': 1010
            },
            {
                'name': 'NIFGEN_VAL_OTHER_TERMINAL',
                'value': 1018
            },
            {
                'name': 'NIFGEN_VAL_CLK_IN',
                'value': 1202
            },
            {
                'name': 'NIFGEN_VAL_DDC_CLK_IN',
                'value': 1203
            }
        ]
    },
    'VideoWaveformType': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_PAL_B',
                'value': 0
            },
            {
                'name': 'NIFGEN_VAL_PAL_D',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_PAL_G',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_PAL_H',
                'value': 3
            },
            {
                'name': 'NIFGEN_VAL_PAL_I',
                'value': 4
            },
            {
                'name': 'NIFGEN_VAL_PAL_M',
                'value': 5
            },
            {
                'name': 'NIFGEN_VAL_PAL_N',
                'value': 6
            },
            {
                'name': 'NIFGEN_VAL_NTSC_M',
                'value': 7
            }
        ]
    },
    'WaitBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_HOLD_LAST_VALUE',
                'value': 400
            },
            {
                'name': 'NIFGEN_VAL_JUMP_TO_VALUE',
                'value': 401
            }
        ]
    },
    'Waveform': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_WFM_SINE',
                'value': 1
            },
            {
                'name': 'NIFGEN_VAL_WFM_SQUARE',
                'value': 2
            },
            {
                'name': 'NIFGEN_VAL_WFM_TRIANGLE',
                'value': 3
            },
            {
                'name': 'NIFGEN_VAL_WFM_RAMP_UP',
                'value': 4
            },
            {
                'name': 'NIFGEN_VAL_WFM_RAMP_DOWN',
                'value': 5
            },
            {
                'name': 'NIFGEN_VAL_WFM_DC',
                'value': 6
            },
            {
                'name': 'NIFGEN_VAL_WFM_NOISE',
                'value': 101
            },
            {
                'name': 'NIFGEN_VAL_WFM_USER',
                'value': 102
            }
        ]
    },
    'WaveformHandle': {
        'codegen_method': 'public',
        'values': [
            {
                'name': 'NIFGEN_VAL_ALL_WAVEFORMS',
                'value': -1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/enums_addon.py sha256=931df863da5ec6a1cc3b4e50ee9b500c369168a905567c8b47160aec077c2dfd bytes=297 -->
## FILE: source/codegen/metadata/nifgen/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/enums_addon.py`
- sha256: `931df863da5ec6a1cc3b4e50ee9b500c369168a905567c8b47160aec077c2dfd`
- bytes: 297

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "OspOverflowStatus": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/functions.py sha256=1ffee880fcc90f8eaeb02a628de3a59cded57897d1ee9d50f04fbfe821b1bfa4 bytes=133595 -->
## FILE: source/codegen/metadata/nifgen/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/functions.py`
- sha256: `1ffee880fcc90f8eaeb02a628de3a59cded57897d1ee9d50f04fbfe821b1bfa4`
- bytes: 133595

````python
# -*- coding: utf-8 -*-
# This file is generated from NI-FGEN API metadata version 26.0.0f146
functions = {
    'AbortGeneration': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AdjustSampleClockRelativeDelay': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'adjustmentTime',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'adjustmentTime',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateNamedWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiFgenInt32AttributeValues',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'attribute_value_raw',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiFgenReal64AttributeValues',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_mapped_field_number': '5',
                'grpc_raw_field_number': '4',
                'grpc_type': 'string',
                'mapped-enum': 'NiFgenStringAttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbMemory': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbSequence': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sequenceHandle',
                'direction': 'in',
                'enum': 'SequenceHandle',
                'grpc_type': 'sint32',
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'in',
                'enum': 'WaveformHandle',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearFreqList': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'frequencyListHandle',
                'direction': 'in',
                'enum': 'FrequencyListOptions',
                'grpc_type': 'sint32',
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearInterchangeWarnings': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearUserStandardWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Close': {
        'cname': 'niFgen_close',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAmplitude': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'amplitude',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'amplitude',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureArbSequence': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'sequenceHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            },
            {
                'cppName': 'gain',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'cppName': 'offset',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'offset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureArbWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'cppName': 'gain',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'cppName': 'offset',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'offset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureChannels': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channels',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channels',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureClockMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'clockMode',
                'direction': 'in',
                'enum': 'ClockMode',
                'grpc_type': 'sint32',
                'name': 'clockMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCustomFIRFilterCoefficients': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfCoefficients',
                'determine_size_from': [
                    'coefficientsArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coefficientsArray',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'coefficientsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeScriptTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerId',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerId',
                'type': 'ViConstString'
            },
            {
                'cppName': 'source',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'ScriptTriggerDigitalEdgeEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'source',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'cppName': 'edge',
                'direction': 'in',
                'enum': 'StartTriggerDigitalEdgeEdge',
                'grpc_type': 'sint32',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalLevelScriptTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerId',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerId',
                'type': 'ViConstString'
            },
            {
                'cppName': 'source',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'cppName': 'triggerWhen',
                'direction': 'in',
                'enum': 'TriggerWhen',
                'grpc_type': 'sint32',
                'name': 'triggerWhen',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFreqList': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'frequencyListHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            },
            {
                'cppName': 'amplitude',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'amplitude',
                'type': 'ViReal64'
            },
            {
                'cppName': 'dcOffset',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'dcOffset',
                'type': 'ViReal64'
            },
            {
                'cppName': 'startPhase',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'startPhase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFrequency': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'frequency',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'frequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOperationMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'operationMode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'operationMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputEnabled': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'enabled',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputImpedance': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'impedance',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'impedance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'outputMode',
                'direction': 'in',
                'enum': 'OutputMode',
                'grpc_type': 'sint32',
                'name': 'outputMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureP2PEndpointFullnessStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'p2pEndpointFullnessLevel',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'p2pEndpointFullnessLevel',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureReferenceClock': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'referenceClockSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'referenceClockSource',
                'type': 'ViConstString'
            },
            {
                'cppName': 'referenceClockFrequency',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'referenceClockFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleClockSource': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sampleClockSource',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'sampleClockSource',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleRate': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sampleRate',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'sampleRate',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeScriptTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerId',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerId',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureStandardWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveform',
                'direction': 'in',
                'enum': 'Waveform',
                'grpc_type': 'sint32',
                'name': 'waveform',
                'type': 'ViInt32'
            },
            {
                'cppName': 'amplitude',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'amplitude',
                'type': 'ViReal64'
            },
            {
                'cppName': 'dcOffset',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'dcOffset',
                'type': 'ViReal64'
            },
            {
                'cppName': 'frequency',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'cppName': 'startPhase',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'startPhase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSynchronization': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'synchronizationSource',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'synchronizationSource',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerMode': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'triggerMode',
                'direction': 'in',
                'enum': 'TriggerMode',
                'grpc_type': 'sint32',
                'name': 'triggerMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedArbSequence': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sequenceLength',
                'determine_size_from': [
                    'waveformHandlesArray',
                    'loopCountsArray',
                    'sampleCountsArray',
                    'markerLocationArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sequenceLength',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformHandlesArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'waveformHandlesArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'loopCountsArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'loopCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'sampleCountsArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'sampleCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'markerLocationArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'markerLocationArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'coercedMarkersArray',
                'direction': 'out',
                'grpc_type': 'repeated sint32',
                'name': 'coercedMarkersArray',
                'size': {
                    'mechanism': 'custom-code',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'sequenceHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateArbSequence': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sequenceLength',
                'determine_size_from': [
                    'waveformHandlesArray',
                    'loopCountsArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sequenceLength',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformHandlesArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'waveformHandlesArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'loopCountsArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'loopCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'cppName': 'sequenceHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateFreqList': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'waveform',
                'direction': 'in',
                'enum': 'Waveform',
                'grpc_type': 'sint32',
                'name': 'waveform',
                'type': 'ViInt32'
            },
            {
                'cppName': 'frequencyListLength',
                'determine_size_from': [
                    'frequencyArray',
                    'durationArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'frequencyListLength',
                'type': 'ViInt32'
            },
            {
                'cppName': 'frequencyArray',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'frequencyArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyListLength'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'durationArray',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'durationArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyListLength'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'frequencyListHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformComplexF64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfSamples',
                'determine_size_from': [
                    'waveformDataArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformDataArray',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'waveformDataArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'struct NIComplexNumber_struct[]'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformF64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformSize',
                'determine_size_from': [
                    'waveformDataArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformDataArray',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'waveformDataArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileF64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'fileName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'byteOrder',
                'direction': 'in',
                'enum': 'ByteOrder',
                'grpc_type': 'sint32',
                'name': 'byteOrder',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileHWS': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'fileName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'useRateFromWaveform',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'useRateFromWaveform',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'useGainAndOffsetFromWaveform',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'useGainAndOffsetFromWaveform',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileI16': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'fileName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'byteOrder',
                'direction': 'in',
                'enum': 'ByteOrder',
                'grpc_type': 'sint32',
                'name': 'byteOrder',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformI16': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformSize',
                'determine_size_from': [
                    'waveformDataArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformDataArray',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'waveformDataArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViInt16[]'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'DefineUserStandardWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformSize',
                'determine_size_from': [
                    'waveformDataArray'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformDataArray',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'waveformDataArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteNamedWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteScript': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'scriptName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'scriptName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableAnalogFilter': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableDigitalFilter': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableDigitalPatterning': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableScriptTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'triggerId',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerId',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableAnalogFilter': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'filterCorrectionFrequency',
                'direction': 'in',
                'grpc_type': 'double',
                'name': 'filterCorrectionFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableDigitalFilter': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableDigitalPatterning': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorHandler': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorMessage': {
        'cname': 'niFgen_error_message',
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorQuery': {
        'cname': 'niFgen_error_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sizeInBytes',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'out',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'signal',
                'direction': 'in',
                'enum': 'Signal',
                'grpc_type': 'sint32',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'cppName': 'signalIdentifier',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'cppName': 'outputTerminal',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'int64',
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'index',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'cppName': 'bufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'channelString',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'channelString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'public',
        'is_error_handling': True,
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorCode',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'cppName': 'errorDescriptionBufferSize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'errorDescription',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'cppName': 'hour',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minute',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'months',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'months',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetFIRFilterCoefficients': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'arraySize',
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'coefficientsArray',
                'direction': 'out',
                'grpc_type': 'repeated double',
                'name': 'coefficientsArray',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'numberOfCoefficientsRead'
                },
                'type': 'ViReal64[]'
            },
            {
                'cppName': 'numberOfCoefficientsRead',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'numberOfCoefficientsRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetHardwareState': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'state',
                'direction': 'out',
                'enum': 'HardwareState',
                'grpc_type': 'sint32',
                'name': 'state',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'year',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'cppName': 'month',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'cppName': 'day',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'cppName': 'hour',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minute',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastTemp': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalSupported': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfCalSupported',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'selfCalSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStreamEndpointHandle': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'streamEndpoint',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'streamEndpoint',
                'type': 'ViConstString'
            },
            {
                'cppName': 'readerHandle',
                'direction': 'out',
                'grpc_type': 'uint32',
                'name': 'readerHandle',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'sizeInBytes',
                'determine_size_from': [
                    'configuration'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'sizeInBytes',
                'type': 'ViInt32'
            },
            {
                'cppName': 'configuration',
                'direction': 'in',
                'grpc_type': 'bytes',
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'sizeInBytes'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'filePath',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Init': {
        'cname': 'niFgen_init',
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'idQuery',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeWithChannels': {
        'codegen_method': 'public',
        'init_method': True,
        'parameters': [
            {
                'cppName': 'resourceName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'resetDevice',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'cppName': 'optionString',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'cppName': 'vi',
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'errorMessage',
                'direction': 'out',
                'get_last_error': 'deprecated',
                'grpc_type': 'string',
                'name': 'errorMessage',
                'type': 'ViChar[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'ViInt32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitiateGeneration': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InvalidateAllAttributes': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'done',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ManualEnableP2PStream': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'endpointName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'endpointName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryArbSeqCapabilities': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumNumberOfSequences',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'maximumNumberOfSequences',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minimumSequenceLength',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minimumSequenceLength',
                'type': 'ViInt32'
            },
            {
                'cppName': 'maximumSequenceLength',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'maximumSequenceLength',
                'type': 'ViInt32'
            },
            {
                'cppName': 'maximumLoopCount',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'maximumLoopCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryArbWfmCapabilities': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumNumberOfWaveforms',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'maximumNumberOfWaveforms',
                'type': 'ViInt32'
            },
            {
                'cppName': 'waveformQuantum',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'waveformQuantum',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minimumWaveformSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minimumWaveformSize',
                'type': 'ViInt32'
            },
            {
                'cppName': 'maximumWaveformSize',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'maximumWaveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryFreqListCapabilities': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maximumNumberOfFreqLists',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'maximumNumberOfFreqLists',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minimumFrequencyListLength',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'minimumFrequencyListLength',
                'type': 'ViInt32'
            },
            {
                'cppName': 'maximumFrequencyListLength',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'maximumFrequencyListLength',
                'type': 'ViInt32'
            },
            {
                'cppName': 'minimumFrequencyListDuration',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'minimumFrequencyListDuration',
                'type': 'ViReal64'
            },
            {
                'cppName': 'maximumFrequencyListDuration',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'maximumFrequencyListDuration',
                'type': 'ViReal64'
            },
            {
                'cppName': 'frequencyListDurationQuantum',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'frequencyListDurationQuantum',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCurrentTemperature': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'temperature',
                'direction': 'out',
                'grpc_type': 'double',
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Reset': {
        'cname': 'niFgen_reset',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetAttribute': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetInterchangeCheck': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevisionQuery': {
        'cname': 'niFgen_revision_query',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'instrumentDriverRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            },
            {
                'cppName': 'firmwareRevision',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteSignalOut': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'routeSignalFrom',
                'direction': 'in',
                'enum': 'RouteSignalFrom',
                'grpc_type': 'sint32',
                'name': 'routeSignalFrom',
                'type': 'ViInt32'
            },
            {
                'cppName': 'routeSignalTo',
                'direction': 'in',
                'enum': 'RouteSignalTo',
                'grpc_type': 'sint32',
                'name': 'routeSignalTo',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTest': {
        'cname': 'niFgen_self_test',
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'selfTestResult',
                'direction': 'out',
                'grpc_type': 'sint32',
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'cppName': 'selfTestMessage',
                'direction': 'out',
                'grpc_type': 'string',
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'trigger',
                'direction': 'in',
                'enum': 'Trigger',
                'grpc_type': 'sint32',
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'cppName': 'triggerId',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'triggerId',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiFgenInt32AttributeValues',
                'grpc_type': 'sint32',
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'int64',
                'name': 'attribute_value_raw',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'enum': 'NiFgenReal64AttributeValues',
                'grpc_type': 'double',
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'attributeId',
                'direction': 'in',
                'grpc_type': 'NiFgenAttribute',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'cppName': 'attributeValue',
                'direction': 'in',
                'grpc_mapped_field_number': '5',
                'grpc_raw_field_number': '4',
                'grpc_type': 'string',
                'mapped-enum': 'NiFgenStringAttributeValuesMapped',
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetNamedWaveformNextWritePosition': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'relativeTo',
                'direction': 'in',
                'enum': 'RelativeTo',
                'grpc_type': 'sint32',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'cppName': 'offset',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformNextWritePosition': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'cppName': 'relativeTo',
                'direction': 'in',
                'enum': 'RelativeTo',
                'grpc_type': 'sint32',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'cppName': 'offset',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'callerHasLock',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitUntilDone': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'maxTime',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'maxTime',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteBinary16Waveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteComplexBinary16Waveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexI16',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'struct NIComplexI16_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformComplexF64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'struct NIComplexNumber_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformComplexI16': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexI16',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'struct NIComplexI16_struct[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformF64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformI16': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteP2PEndpointI16': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'endpointName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'endpointName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfSamples',
                'determine_size_from': [
                    'endpointData'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'endpointData',
                'direction': 'in',
                'grpc_type': 'repeated sint32',
                'name': 'endpointData',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'ViInt16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteScript': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'script',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'script',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveform': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'cppName': 'size',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated double',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveformComplexF64': {
        'codegen_method': 'public',
        'parameters': [
            {
                'cppName': 'vi',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'cppName': 'channelName',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'cppName': 'numberOfSamples',
                'determine_size_from': [
                    'data'
                ],
                'direction': 'in',
                'grpc_type': 'sint32',
                'include_in_proto': False,
                'is_size_param': True,
                'linked_params_are_optional': False,
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'cppName': 'data',
                'direction': 'in',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfSamples'
                },
                'type': 'struct NIComplexNumber_struct[]'
            },
            {
                'cppName': 'waveformHandle',
                'direction': 'in',
                'grpc_type': 'sint32',
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/functions_addon.py sha256=509cdb9ccc9aa05529c706d6ca32bf420ee698835bf29cf7fb30bb80c58a3144 bytes=1318 -->
## FILE: source/codegen/metadata/nifgen/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/functions_addon.py`
- sha256: `509cdb9ccc9aa05529c706d6ca32bf420ee698835bf29cf7fb30bb80c58a3144`
- bytes: 1318

````python
# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'SetRuntimeEnvironment': {
        'codegen_method': 'private',
        'parameters': [
            {
                'cppName': 'environment',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environment',
                'type': 'ViConstString'
            },
            {
                'cppName': 'environmentVersion',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'environmentVersion',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved1',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved1',
                'type': 'ViConstString'
            },
            {
                'cppName': 'reserved2',
                'direction': 'in',
                'grpc_type': 'string',
                'name': 'reserved2',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/nifgen.proto sha256=d96c3f71d74d702b5eacc5dfa75344f9982848ea3d0c9f62625046f6bcadf134 bytes=73002 -->
## FILE: source/codegen/metadata/nifgen/nifgen.proto

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/nifgen.proto`
- sha256: `d96c3f71d74d702b5eacc5dfa75344f9982848ea3d0c9f62625046f6bcadf134`
- bytes: 73002

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-FGEN API metadata version 26.0.0f146
//---------------------------------------------------------------------
// Proto file for the NI-FGEN Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.fgen";
option java_outer_classname = "NiFgen";
option csharp_namespace = "NationalInstruments.Grpc.Fgen";

package nifgen_grpc;

import "nidevice.proto";
import "session.proto";

service NiFgen {
  rpc AbortGeneration(AbortGenerationRequest) returns (AbortGenerationResponse);
  rpc AdjustSampleClockRelativeDelay(AdjustSampleClockRelativeDelayRequest) returns (AdjustSampleClockRelativeDelayResponse);
  rpc AllocateNamedWaveform(AllocateNamedWaveformRequest) returns (AllocateNamedWaveformResponse);
  rpc AllocateWaveform(AllocateWaveformRequest) returns (AllocateWaveformResponse);
  rpc CheckAttributeViBoolean(CheckAttributeViBooleanRequest) returns (CheckAttributeViBooleanResponse);
  rpc CheckAttributeViInt32(CheckAttributeViInt32Request) returns (CheckAttributeViInt32Response);
  rpc CheckAttributeViInt64(CheckAttributeViInt64Request) returns (CheckAttributeViInt64Response);
  rpc CheckAttributeViReal64(CheckAttributeViReal64Request) returns (CheckAttributeViReal64Response);
  rpc CheckAttributeViSession(CheckAttributeViSessionRequest) returns (CheckAttributeViSessionResponse);
  rpc CheckAttributeViString(CheckAttributeViStringRequest) returns (CheckAttributeViStringResponse);
  rpc ClearArbMemory(ClearArbMemoryRequest) returns (ClearArbMemoryResponse);
  rpc ClearArbSequence(ClearArbSequenceRequest) returns (ClearArbSequenceResponse);
  rpc ClearArbWaveform(ClearArbWaveformRequest) returns (ClearArbWaveformResponse);
  rpc ClearError(ClearErrorRequest) returns (ClearErrorResponse);
  rpc ClearFreqList(ClearFreqListRequest) returns (ClearFreqListResponse);
  rpc ClearInterchangeWarnings(ClearInterchangeWarningsRequest) returns (ClearInterchangeWarningsResponse);
  rpc ClearUserStandardWaveform(ClearUserStandardWaveformRequest) returns (ClearUserStandardWaveformResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc ConfigureAmplitude(ConfigureAmplitudeRequest) returns (ConfigureAmplitudeResponse);
  rpc ConfigureArbSequence(ConfigureArbSequenceRequest) returns (ConfigureArbSequenceResponse);
  rpc ConfigureArbWaveform(ConfigureArbWaveformRequest) returns (ConfigureArbWaveformResponse);
  rpc ConfigureChannels(ConfigureChannelsRequest) returns (ConfigureChannelsResponse);
  rpc ConfigureClockMode(ConfigureClockModeRequest) returns (ConfigureClockModeResponse);
  rpc ConfigureCustomFIRFilterCoefficients(ConfigureCustomFIRFilterCoefficientsRequest) returns (ConfigureCustomFIRFilterCoefficientsResponse);
  rpc ConfigureDigitalEdgeScriptTrigger(ConfigureDigitalEdgeScriptTriggerRequest) returns (ConfigureDigitalEdgeScriptTriggerResponse);
  rpc ConfigureDigitalEdgeStartTrigger(ConfigureDigitalEdgeStartTriggerRequest) returns (ConfigureDigitalEdgeStartTriggerResponse);
  rpc ConfigureDigitalLevelScriptTrigger(ConfigureDigitalLevelScriptTriggerRequest) returns (ConfigureDigitalLevelScriptTriggerResponse);
  rpc ConfigureFreqList(ConfigureFreqListRequest) returns (ConfigureFreqListResponse);
  rpc ConfigureFrequency(ConfigureFrequencyRequest) returns (ConfigureFrequencyResponse);
  rpc ConfigureOperationMode(ConfigureOperationModeRequest) returns (ConfigureOperationModeResponse);
  rpc ConfigureOutputEnabled(ConfigureOutputEnabledRequest) returns (ConfigureOutputEnabledResponse);
  rpc ConfigureOutputImpedance(ConfigureOutputImpedanceRequest) returns (ConfigureOutputImpedanceResponse);
  rpc ConfigureOutputMode(ConfigureOutputModeRequest) returns (ConfigureOutputModeResponse);
  rpc ConfigureP2PEndpointFullnessStartTrigger(ConfigureP2PEndpointFullnessStartTriggerRequest) returns (ConfigureP2PEndpointFullnessStartTriggerResponse);
  rpc ConfigureReferenceClock(ConfigureReferenceClockRequest) returns (ConfigureReferenceClockResponse);
  rpc ConfigureSampleClockSource(ConfigureSampleClockSourceRequest) returns (ConfigureSampleClockSourceResponse);
  rpc ConfigureSampleRate(ConfigureSampleRateRequest) returns (ConfigureSampleRateResponse);
  rpc ConfigureSoftwareEdgeScriptTrigger(ConfigureSoftwareEdgeScriptTriggerRequest) returns (ConfigureSoftwareEdgeScriptTriggerResponse);
  rpc ConfigureSoftwareEdgeStartTrigger(ConfigureSoftwareEdgeStartTriggerRequest) returns (ConfigureSoftwareEdgeStartTriggerResponse);
  rpc ConfigureStandardWaveform(ConfigureStandardWaveformRequest) returns (ConfigureStandardWaveformResponse);
  rpc ConfigureSynchronization(ConfigureSynchronizationRequest) returns (ConfigureSynchronizationResponse);
  rpc ConfigureTriggerMode(ConfigureTriggerModeRequest) returns (ConfigureTriggerModeResponse);
  rpc CreateAdvancedArbSequence(CreateAdvancedArbSequenceRequest) returns (CreateAdvancedArbSequenceResponse);
  rpc CreateArbSequence(CreateArbSequenceRequest) returns (CreateArbSequenceResponse);
  rpc CreateFreqList(CreateFreqListRequest) returns (CreateFreqListResponse);
  rpc CreateWaveformComplexF64(CreateWaveformComplexF64Request) returns (CreateWaveformComplexF64Response);
  rpc CreateWaveformF64(CreateWaveformF64Request) returns (CreateWaveformF64Response);
  rpc CreateWaveformFromFileF64(CreateWaveformFromFileF64Request) returns (CreateWaveformFromFileF64Response);
  rpc CreateWaveformFromFileHWS(CreateWaveformFromFileHWSRequest) returns (CreateWaveformFromFileHWSResponse);
  rpc CreateWaveformFromFileI16(CreateWaveformFromFileI16Request) returns (CreateWaveformFromFileI16Response);
  rpc CreateWaveformI16(CreateWaveformI16Request) returns (CreateWaveformI16Response);
  rpc DefineUserStandardWaveform(DefineUserStandardWaveformRequest) returns (DefineUserStandardWaveformResponse);
  rpc DeleteNamedWaveform(DeleteNamedWaveformRequest) returns (DeleteNamedWaveformResponse);
  rpc DeleteScript(DeleteScriptRequest) returns (DeleteScriptResponse);
  rpc Disable(DisableRequest) returns (DisableResponse);
  rpc DisableAnalogFilter(DisableAnalogFilterRequest) returns (DisableAnalogFilterResponse);
  rpc DisableDigitalFilter(DisableDigitalFilterRequest) returns (DisableDigitalFilterResponse);
  rpc DisableDigitalPatterning(DisableDigitalPatterningRequest) returns (DisableDigitalPatterningResponse);
  rpc DisableScriptTrigger(DisableScriptTriggerRequest) returns (DisableScriptTriggerResponse);
  rpc DisableStartTrigger(DisableStartTriggerRequest) returns (DisableStartTriggerResponse);
  rpc EnableAnalogFilter(EnableAnalogFilterRequest) returns (EnableAnalogFilterResponse);
  rpc EnableDigitalFilter(EnableDigitalFilterRequest) returns (EnableDigitalFilterResponse);
  rpc EnableDigitalPatterning(EnableDigitalPatterningRequest) returns (EnableDigitalPatterningResponse);
  rpc ErrorHandler(ErrorHandlerRequest) returns (ErrorHandlerResponse);
  rpc ErrorMessage(ErrorMessageRequest) returns (ErrorMessageResponse);
  rpc ErrorQuery(ErrorQueryRequest) returns (ErrorQueryResponse);
  rpc ExportAttributeConfigurationBuffer(ExportAttributeConfigurationBufferRequest) returns (ExportAttributeConfigurationBufferResponse);
  rpc ExportAttributeConfigurationFile(ExportAttributeConfigurationFileRequest) returns (ExportAttributeConfigurationFileResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc GetAttributeViBoolean(GetAttributeViBooleanRequest) returns (GetAttributeViBooleanResponse);
  rpc GetAttributeViInt32(GetAttributeViInt32Request) returns (GetAttributeViInt32Response);
  rpc GetAttributeViInt64(GetAttributeViInt64Request) returns (GetAttributeViInt64Response);
  rpc GetAttributeViReal64(GetAttributeViReal64Request) returns (GetAttributeViReal64Response);
  rpc GetAttributeViSession(GetAttributeViSessionRequest) returns (GetAttributeViSessionResponse);
  rpc GetAttributeViString(GetAttributeViStringRequest) returns (GetAttributeViStringResponse);
  rpc GetChannelName(GetChannelNameRequest) returns (GetChannelNameResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetExtCalLastDateAndTime(GetExtCalLastDateAndTimeRequest) returns (GetExtCalLastDateAndTimeResponse);
  rpc GetExtCalLastTemp(GetExtCalLastTempRequest) returns (GetExtCalLastTempResponse);
  rpc GetExtCalRecommendedInterval(GetExtCalRecommendedIntervalRequest) returns (GetExtCalRecommendedIntervalResponse);
  rpc GetFIRFilterCoefficients(GetFIRFilterCoefficientsRequest) returns (GetFIRFilterCoefficientsResponse);
  rpc GetHardwareState(GetHardwareStateRequest) returns (GetHardwareStateResponse);
  rpc GetSelfCalLastDateAndTime(GetSelfCalLastDateAndTimeRequest) returns (GetSelfCalLastDateAndTimeResponse);
  rpc GetSelfCalLastTemp(GetSelfCalLastTempRequest) returns (GetSelfCalLastTempResponse);
  rpc GetSelfCalSupported(GetSelfCalSupportedRequest) returns (GetSelfCalSupportedResponse);
  rpc GetStreamEndpointHandle(GetStreamEndpointHandleRequest) returns (GetStreamEndpointHandleResponse);
  rpc ImportAttributeConfigurationBuffer(ImportAttributeConfigurationBufferRequest) returns (ImportAttributeConfigurationBufferResponse);
  rpc ImportAttributeConfigurationFile(ImportAttributeConfigurationFileRequest) returns (ImportAttributeConfigurationFileResponse);
  rpc Init(InitRequest) returns (InitResponse);
  rpc InitWithOptions(InitWithOptionsRequest) returns (InitWithOptionsResponse);
  rpc InitializeWithChannels(InitializeWithChannelsRequest) returns (InitializeWithChannelsResponse);
  rpc InitiateGeneration(InitiateGenerationRequest) returns (InitiateGenerationResponse);
  rpc InvalidateAllAttributes(InvalidateAllAttributesRequest) returns (InvalidateAllAttributesResponse);
  rpc IsDone(IsDoneRequest) returns (IsDoneResponse);
  rpc ManualEnableP2PStream(ManualEnableP2PStreamRequest) returns (ManualEnableP2PStreamResponse);
  rpc QueryArbSeqCapabilities(QueryArbSeqCapabilitiesRequest) returns (QueryArbSeqCapabilitiesResponse);
  rpc QueryArbWfmCapabilities(QueryArbWfmCapabilitiesRequest) returns (QueryArbWfmCapabilitiesResponse);
  rpc QueryFreqListCapabilities(QueryFreqListCapabilitiesRequest) returns (QueryFreqListCapabilitiesResponse);
  rpc ReadCurrentTemperature(ReadCurrentTemperatureRequest) returns (ReadCurrentTemperatureResponse);
  rpc Reset(ResetRequest) returns (ResetResponse);
  rpc ResetAttribute(ResetAttributeRequest) returns (ResetAttributeResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc ResetInterchangeCheck(ResetInterchangeCheckRequest) returns (ResetInterchangeCheckResponse);
  rpc ResetWithDefaults(ResetWithDefaultsRequest) returns (ResetWithDefaultsResponse);
  rpc RevisionQuery(RevisionQueryRequest) returns (RevisionQueryResponse);
  rpc RouteSignalOut(RouteSignalOutRequest) returns (RouteSignalOutResponse);
  rpc SelfCal(SelfCalRequest) returns (SelfCalResponse);
  rpc SelfTest(SelfTestRequest) returns (SelfTestResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc SetAttributeViBoolean(SetAttributeViBooleanRequest) returns (SetAttributeViBooleanResponse);
  rpc SetAttributeViInt32(SetAttributeViInt32Request) returns (SetAttributeViInt32Response);
  rpc SetAttributeViInt64(SetAttributeViInt64Request) returns (SetAttributeViInt64Response);
  rpc SetAttributeViReal64(SetAttributeViReal64Request) returns (SetAttributeViReal64Response);
  rpc SetAttributeViSession(SetAttributeViSessionRequest) returns (SetAttributeViSessionResponse);
  rpc SetAttributeViString(SetAttributeViStringRequest) returns (SetAttributeViStringResponse);
  rpc SetNamedWaveformNextWritePosition(SetNamedWaveformNextWritePositionRequest) returns (SetNamedWaveformNextWritePositionResponse);
  rpc SetWaveformNextWritePosition(SetWaveformNextWritePositionRequest) returns (SetWaveformNextWritePositionResponse);
  rpc WaitUntilDone(WaitUntilDoneRequest) returns (WaitUntilDoneResponse);
  rpc WriteBinary16Waveform(WriteBinary16WaveformRequest) returns (WriteBinary16WaveformResponse);
  rpc WriteComplexBinary16Waveform(WriteComplexBinary16WaveformRequest) returns (WriteComplexBinary16WaveformResponse);
  rpc WriteNamedWaveformComplexF64(WriteNamedWaveformComplexF64Request) returns (WriteNamedWaveformComplexF64Response);
  rpc WriteNamedWaveformComplexI16(WriteNamedWaveformComplexI16Request) returns (WriteNamedWaveformComplexI16Response);
  rpc WriteNamedWaveformF64(WriteNamedWaveformF64Request) returns (WriteNamedWaveformF64Response);
  rpc WriteNamedWaveformI16(WriteNamedWaveformI16Request) returns (WriteNamedWaveformI16Response);
  rpc WriteP2PEndpointI16(WriteP2PEndpointI16Request) returns (WriteP2PEndpointI16Response);
  rpc WriteScript(WriteScriptRequest) returns (WriteScriptResponse);
  rpc WriteWaveform(WriteWaveformRequest) returns (WriteWaveformResponse);
  rpc WriteWaveformComplexF64(WriteWaveformComplexF64Request) returns (WriteWaveformComplexF64Response);
}

enum NiFgenAttribute {
  NIFGEN_ATTRIBUTE_UNSPECIFIED = 0;
  NIFGEN_ATTRIBUTE_RANGE_CHECK = 1050002;
  NIFGEN_ATTRIBUTE_QUERY_INSTRUMENT_STATUS = 1050003;
  NIFGEN_ATTRIBUTE_CACHE = 1050004;
  NIFGEN_ATTRIBUTE_SIMULATE = 1050005;
  NIFGEN_ATTRIBUTE_RECORD_COERCIONS = 1050006;
  NIFGEN_ATTRIBUTE_DRIVER_SETUP = 1050007;
  NIFGEN_ATTRIBUTE_INTERCHANGE_CHECK = 1050021;
  NIFGEN_ATTRIBUTE_CHANNEL_COUNT = 1050203;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX = 1050302;
  NIFGEN_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR = 1050304;
  NIFGEN_ATTRIBUTE_LOGICAL_NAME = 1050305;
  NIFGEN_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS = 1050327;
  NIFGEN_ATTRIBUTE_GROUP_CAPABILITIES = 1050401;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MAJOR_VERSION = 1050503;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MINOR_VERSION = 1050504;
  NIFGEN_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION = 1050510;
  NIFGEN_ATTRIBUTE_INSTRUMENT_MANUFACTURER = 1050511;
  NIFGEN_ATTRIBUTE_INSTRUMENT_MODEL = 1050512;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR = 1050513;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION = 1050514;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION = 1050515;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION = 1050516;
  NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_REVISION = 1050551;
  NIFGEN_ATTRIBUTE_ID_QUERY_RESPONSE = 1150001;
  NIFGEN_ATTRIBUTE_DIGITAL_PATTERN_ENABLED = 1150101;
  NIFGEN_ATTRIBUTE_DIGITAL_FILTER_ENABLED = 1150102;
  NIFGEN_ATTRIBUTE_ANALOG_FILTER_ENABLED = 1150103;
  NIFGEN_ATTRIBUTE_FILTER_CORRECTION_FREQUENCY = 1150104;
  NIFGEN_ATTRIBUTE_SYNC_DUTY_CYCLE_HIGH = 1150105;
  NIFGEN_ATTRIBUTE_UPDATE_CLOCK_SOURCE = 1150106;
  NIFGEN_ATTRIBUTE_REF_CLOCK_FREQUENCY = 1150107;
  NIFGEN_ATTRIBUTE_TRIGGER_MODE = 1150108;
  NIFGEN_ATTRIBUTE_CLOCK_MODE = 1150110;
  NIFGEN_ATTRIBUTE_SYNCHRONIZATION = 1150111;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_SOURCE = 1150112;
  NIFGEN_ATTRIBUTE_REFERENCE_CLOCK_SOURCE = 1150113;
  NIFGEN_ATTRIBUTE_FREQ_LIST_HANDLE = 1150208;
  NIFGEN_ATTRIBUTE_MAX_NUM_FREQ_LISTS = 1150209;
  NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_LENGTH = 1150210;
  NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_LENGTH = 1150211;
  NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_DURATION = 1150212;
  NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_DURATION = 1150213;
  NIFGEN_ATTRIBUTE_FREQ_LIST_DURATION_QUANTUM = 1150214;
  NIFGEN_ATTRIBUTE_BUS_TYPE = 1150215;
  NIFGEN_ATTRIBUTE_VIDEO_WAVEFORM_TYPE = 1150216;
  NIFGEN_ATTRIBUTE_DIGITAL_FILTER_INTERPOLATION_FACTOR = 1150218;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_DIVISOR = 1150219;
  NIFGEN_ATTRIBUTE_LOAD_IMPEDANCE = 1150220;
  NIFGEN_ATTRIBUTE_ANALOG_PATH = 1150222;
  NIFGEN_ATTRIBUTE_GAIN_DAC_VALUE = 1150223;
  NIFGEN_ATTRIBUTE_OFFSET_DAC_VALUE = 1150224;
  NIFGEN_ATTRIBUTE_OSCILLATOR_FREQ_DAC_VALUE = 1150225;
  NIFGEN_ATTRIBUTE_PRE_AMPLIFIER_ATTENUATION = 1150228;
  NIFGEN_ATTRIBUTE_POST_AMPLIFIER_ATTENUATION = 1150229;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR = 1150230;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_ABSOLUTE_DELAY = 1150231;
  NIFGEN_ATTRIBUTE_OSCILLATOR_PHASE_DAC_VALUE = 1150232;
  NIFGEN_ATTRIBUTE_EXTERNAL_CLOCK_DELAY_BINARY_VALUE = 1150233;
  NIFGEN_ATTRIBUTE_ANALOG_DATA_MASK = 1150234;
  NIFGEN_ATTRIBUTE_ANALOG_STATIC_VALUE = 1150235;
  NIFGEN_ATTRIBUTE_DIGITAL_DATA_MASK = 1150236;
  NIFGEN_ATTRIBUTE_DIGITAL_STATIC_VALUE = 1150237;
  NIFGEN_ATTRIBUTE_FUNC_BUFFER_SIZE = 1150238;
  NIFGEN_ATTRIBUTE_FUNC_MAX_BUFFER_SIZE = 1150239;
  NIFGEN_ATTRIBUTE_FILE_TRANSFER_BLOCK_SIZE = 1150240;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE = 1150241;
  NIFGEN_ATTRIBUTE_MEMORY_SIZE = 1150242;
  NIFGEN_ATTRIBUTE_SERIAL_NUMBER = 1150243;
  NIFGEN_ATTRIBUTE_DIRECT_DMA_ENABLED = 1150244;
  NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_SIZE = 1150245;
  NIFGEN_ATTRIBUTE_OSP_ENABLED = 1150246;
  NIFGEN_ATTRIBUTE_OSP_DATA_PROCESSING_MODE = 1150247;
  NIFGEN_ATTRIBUTE_OSP_IQ_RATE = 1150248;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_ENABLED = 1150249;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_FREQUENCY = 1150250;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_I = 1150251;
  NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_Q = 1150252;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_TYPE = 1150253;
  NIFGEN_ATTRIBUTE_DIGITAL_GAIN = 1150254;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ENABLED = 1150255;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_INTERPOLATION = 1150256;
  NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_ENABLED = 1150257;
  NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_INTERPOLATION = 1150258;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA = 1150259;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_RAISED_COSINE_ALPHA = 1150260;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_FLAT_PASSBAND = 1150261;
  NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_GAUSSIAN_BT = 1150262;
  NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_GAIN = 1150263;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_I = 1150264;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_Q = 1150265;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_I = 1150266;
  NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_Q = 1150267;
  NIFGEN_ATTRIBUTE_OSP_OVERFLOW_ERROR_REPORTING = 1150268;
  NIFGEN_ATTRIBUTE_OSP_OVERFLOW_STATUS = 1150269;
  NIFGEN_ATTRIBUTE_SCRIPT_TO_GENERATE = 1150270;
  NIFGEN_ATTRIBUTE_MARKER_EVENTS_COUNT = 1150271;
  NIFGEN_ATTRIBUTE_SCRIPT_TRIGGERS_COUNT = 1150272;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENTS_COUNT = 1150273;
  NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_ADDRESS = 1150274;
  NIFGEN_ATTRIBUTE_START_TRIGGER_TYPE = 1150280;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE = 1150281;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE = 1150282;
  NIFGEN_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL = 1150283;
  NIFGEN_ATTRIBUTE_SCRIPT_TRIGGER_TYPE = 1150290;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE = 1150291;
  NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE = 1150292;
  NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE = 1150293;
  NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL = 1150294;
  NIFGEN_ATTRIBUTE_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL = 1150295;
  NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL = 1150310;
  NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL = 1150311;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_TERMINAL = 1150312;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_POLARITY = 1150313;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_TERMINAL = 1150314;
  NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_TERMINAL = 1150315;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_LEVEL_ACTIVE_LEVEL = 1150316;
  NIFGEN_ATTRIBUTE_DONE_EVENT_LEVEL_ACTIVE_LEVEL = 1150317;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_POLARITY = 1150318;
  NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_POLARITY = 1150319;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL = 1150320;
  NIFGEN_ATTRIBUTE_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL = 1150321;
  NIFGEN_ATTRIBUTE_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL = 1150322;
  NIFGEN_ATTRIBUTE_FLATNESS_CORRECTION_ENABLED = 1150323;
  NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_HANDLE = 1150324;
  NIFGEN_ATTRIBUTE_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM = 1150325;
  NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_NAME = 1150326;
  NIFGEN_ATTRIBUTE_ARB_MARKER_POSITION = 1150327;
  NIFGEN_ATTRIBUTE_ARB_REPEAT_COUNT = 1150328;
  NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL = 1150329;
  NIFGEN_ATTRIBUTE_SYNC_OUT_OUTPUT_TERMINAL = 1150330;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_BEHAVIOR = 1150331;
  NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_BEHAVIOR = 1150332;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH_UNITS = 1150333;
  NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH_UNITS = 1150334;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH = 1150335;
  NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH = 1150336;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_DATA_BIT_NUMBER = 1150337;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_LEVEL_POLARITY = 1150338;
  NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_OUTPUT_TERMINAL = 1150339;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH = 1150340;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH_UNITS = 1150341;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_BEHAVIOR = 1150342;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_TOGGLE_INITIAL_STATE = 1150343;
  NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LIVE_STATUS = 1150344;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_LIVE_STATUS = 1150345;
  NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LIVE_STATUS = 1150348;
  NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LATCHED_STATUS = 1150349;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_LATCHED_STATUS = 1150350;
  NIFGEN_ATTRIBUTE_DONE_EVENT_LATCHED_STATUS = 1150351;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_LATCHED_STATUS = 1150352;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY = 1150354;
  NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY_UNITS = 1150355;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY = 1150356;
  NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY_UNITS = 1150357;
  NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY = 1150358;
  NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY_UNITS = 1150359;
  NIFGEN_ATTRIBUTE_PCI_DMA_OPTIMIZATIONS_ENABLED = 1150362;
  NIFGEN_ATTRIBUTE_TERMINAL_CONFIGURATION = 1150365;
  NIFGEN_ATTRIBUTE_COMMON_MODE_OFFSET = 1150366;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_SOURCE = 1150367;
  NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_RATE = 1150368;
  NIFGEN_ATTRIBUTE_CHANNEL_DELAY = 1150369;
  NIFGEN_ATTRIBUTE_OSP_MODE = 1150370;
  NIFGEN_ATTRIBUTE_OSP_FREQUENCY_SHIFT = 1150371;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH = 1150373;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE = 1150374;
  NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS = 1150375;
  NIFGEN_ATTRIBUTE_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER = 1150376;
  NIFGEN_ATTRIBUTE_IDLE_BEHAVIOR = 1150377;
  NIFGEN_ATTRIBUTE_IDLE_VALUE = 1150378;
  NIFGEN_ATTRIBUTE_WAIT_BEHAVIOR = 1150379;
  NIFGEN_ATTRIBUTE_WAIT_VALUE = 1150380;
  NIFGEN_ATTRIBUTE_OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY = 1150389;
  NIFGEN_ATTRIBUTE_MODULE_REVISION = 1150390;
  NIFGEN_ATTRIBUTE_P2P_ENABLED = 1150391;
  NIFGEN_ATTRIBUTE_P2P_DESTINATION_CHANNELS = 1150392;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_SIZE = 1150393;
  NIFGEN_ATTRIBUTE_P2P_SPACE_AVAILABLE_IN_ENDPOINT = 1150394;
  NIFGEN_ATTRIBUTE_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT = 1150395;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_COUNT = 1150396;
  NIFGEN_ATTRIBUTE_P2P_MANUAL_CONFIGURATION_ENABLED = 1150397;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS = 1150398;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE = 1150399;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INTERVAL = 1150400;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS = 1150401;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE = 1150402;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_SIZE = 1150403;
  NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS = 1150405;
  NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS_TYPE = 1150406;
  NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_VALUE = 1150407;
  NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS = 1150408;
  NIFGEN_ATTRIBUTE_STREAMING_WRITE_TIMEOUT = 1150409;
  NIFGEN_ATTRIBUTE_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL = 1150410;
  NIFGEN_ATTRIBUTE_AUX_POWER_ENABLED = 1150411;
  NIFGEN_ATTRIBUTE_FPGA_BITFILE_PATH = 1150412;
  NIFGEN_ATTRIBUTE_ABSOLUTE_DELAY = 1150413;
  NIFGEN_ATTRIBUTE_OUTPUT_MODE = 1250001;
  NIFGEN_ATTRIBUTE_OUTPUT_ENABLED = 1250003;
  NIFGEN_ATTRIBUTE_OUTPUT_IMPEDANCE = 1250004;
  NIFGEN_ATTRIBUTE_FUNC_WAVEFORM = 1250101;
  NIFGEN_ATTRIBUTE_FUNC_AMPLITUDE = 1250102;
  NIFGEN_ATTRIBUTE_FUNC_DC_OFFSET = 1250103;
  NIFGEN_ATTRIBUTE_FUNC_FREQUENCY = 1250104;
  NIFGEN_ATTRIBUTE_FUNC_START_PHASE = 1250105;
  NIFGEN_ATTRIBUTE_FUNC_DUTY_CYCLE_HIGH = 1250106;
  NIFGEN_ATTRIBUTE_ARB_WAVEFORM_HANDLE = 1250201;
  NIFGEN_ATTRIBUTE_ARB_GAIN = 1250202;
  NIFGEN_ATTRIBUTE_ARB_OFFSET = 1250203;
  NIFGEN_ATTRIBUTE_ARB_SAMPLE_RATE = 1250204;
  NIFGEN_ATTRIBUTE_MAX_NUM_WAVEFORMS = 1250205;
  NIFGEN_ATTRIBUTE_WAVEFORM_QUANTUM = 1250206;
  NIFGEN_ATTRIBUTE_MIN_WAVEFORM_SIZE = 1250207;
  NIFGEN_ATTRIBUTE_MAX_WAVEFORM_SIZE = 1250208;
  NIFGEN_ATTRIBUTE_ARB_SEQUENCE_HANDLE = 1250211;
  NIFGEN_ATTRIBUTE_MAX_NUM_SEQUENCES = 1250212;
  NIFGEN_ATTRIBUTE_MIN_SEQUENCE_LENGTH = 1250213;
  NIFGEN_ATTRIBUTE_MAX_SEQUENCE_LENGTH = 1250214;
  NIFGEN_ATTRIBUTE_MAX_LOOP_COUNT = 1250215;
  NIFGEN_ATTRIBUTE_TRIGGER_SOURCE = 1250302;
  NIFGEN_ATTRIBUTE_BURST_COUNT = 1250350;
}

enum ByteOrder {
  BYTE_ORDER_NIFGEN_VAL_LITTLE_ENDIAN = 0;
  BYTE_ORDER_NIFGEN_VAL_BIG_ENDIAN = 1;
}

enum ClockMode {
  CLOCK_MODE_NIFGEN_VAL_HIGH_RESOLUTION = 0;
  CLOCK_MODE_NIFGEN_VAL_DIVIDE_DOWN = 1;
  CLOCK_MODE_NIFGEN_VAL_AUTOMATIC = 2;
}

enum FrequencyListOptions {
  FREQUENCY_LIST_OPTIONS_UNSPECIFIED = 0;
  FREQUENCY_LIST_OPTIONS_NIFGEN_VAL_ALL_FLISTS = -1;
}

enum HardwareState {
  HARDWARE_STATE_NIFGEN_VAL_IDLE = 0;
  HARDWARE_STATE_NIFGEN_VAL_WAITING_FOR_START_TRIGGER = 100;
  HARDWARE_STATE_NIFGEN_VAL_RUNNING = 200;
  HARDWARE_STATE_NIFGEN_VAL_DONE = 600;
  HARDWARE_STATE_NIFGEN_VAL_HARDWARE_ERROR = 1000;
}

enum NiFgenInt32AttributeValues {
  option allow_alias = true;
  NIFGEN_INT32_UNSPECIFIED = 0;
  NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_PHYSICAL = 0;
  NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_VIRTUAL = 1;
  NIFGEN_INT32_ANALOG_PATH_VAL_MAIN_ANALOG_PATH = 0;
  NIFGEN_INT32_ANALOG_PATH_VAL_DIRECT_ANALOG_PATH = 1;
  NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_LOW_GAIN_ANALOG_PATH = 2;
  NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_HIGH_GAIN_ANALOG_PATH = 3;
  NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_FIRST_SEQUENCE_HANDLE = 100000;
  NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_LAST_SEQUENCE_HANDLE = 109999;
  NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_NO_SEQUENCE = -1;
  NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_FIRST_WAVEFORM_HANDLE = 10000;
  NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_LAST_WAVEFORM_HANDLE = 10999;
  NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_NO_WAVEFORM = -1;
  NIFGEN_INT32_BURST_COUNT_VAL_GENERATE_CONTINUOUS = -1;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_INVALID = 0;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_AT = 1;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCI = 2;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXI = 3;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_VXI = 4;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCMCIA = 5;
  NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXIE = 6;
  NIFGEN_INT32_CLOCK_MODE_VAL_HIGH_RESOLUTION = 0;
  NIFGEN_INT32_CLOCK_MODE_VAL_DIVIDE_DOWN = 1;
  NIFGEN_INT32_CLOCK_MODE_VAL_AUTOMATIC = 2;
  NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_REAL = 0;
  NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_COMPLEX = 1;
  NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE = 101;
  NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL = 102;
  NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_FLAT = 0;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_RAISED_COSINE = 1;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_ROOT_RAISED_COSINE = 2;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_GAUSSIAN = 3;
  NIFGEN_INT32_FILTER_TYPE_VAL_OSP_CUSTOM = 4;
  NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_FIRST_FREQ_LIST_HANDLE = 200000;
  NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_LAST_FREQ_LIST_HANDLE = 209999;
  NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_NO_FREQ_LIST = -1;
  NIFGEN_INT32_IDLE_BEHAVIOR_VAL_HOLD_LAST_VALUE = 400;
  NIFGEN_INT32_IDLE_BEHAVIOR_VAL_JUMP_TO_VALUE = 401;
  NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE = 101;
  NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL = 102;
  NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_TOGGLE = 103;
  NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_HIGH = 101;
  NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_LOW = 102;
  NIFGEN_INT32_OSP_MODE_VAL_OSP_IF = 0;
  NIFGEN_INT32_OSP_MODE_VAL_OSP_BASEBAND = 1;
  NIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR = 0;
  NIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED = 2;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_NONE = 0;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I = 1;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q = 2;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I = 4;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q = 8;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_I = 16;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_I = 16;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_Q = 32;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_Q = 32;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_I = 64;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_Q = 128;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_COMPLEX_DATA = 256;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_I = 512;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_Q = 1024;
  NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_EQUALIZER = 2048;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FUNC = 0;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_ARB = 1;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SEQ = 2;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FREQ_LIST = 101;
  NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SCRIPT = 102;
  NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE = 101;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_TRIG_NONE = 101;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_EDGE = 102;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_LEVEL = 103;
  NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_SOFTWARE_EDGE = 104;
  NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE = 101;
  NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE = 102;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_TRIG_NONE = 101;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_DIGITAL_EDGE = 102;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_SOFTWARE_EDGE = 104;
  NIFGEN_INT32_START_TRIGGER_TYPE_VAL_P2P_ENDPOINT_FULLNESS = 106;
  NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE = 101;
  NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL = 102;
  NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH = 101;
  NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW = 102;
  NIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS = 101;
  NIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS = 102;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL0 = 111;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL1 = 112;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL2 = 113;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL3 = 114;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL4 = 115;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL5 = 116;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL6 = 117;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_0 = 141;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_1 = 142;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_2 = 143;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_3 = 144;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_4 = 145;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_5 = 146;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_6 = 147;
  NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_NONE = 1000;
  NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED = 300;
  NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL = 301;
  NIFGEN_INT32_TRIGGER_MODE_VAL_SINGLE = 1;
  NIFGEN_INT32_TRIGGER_MODE_VAL_CONTINUOUS = 2;
  NIFGEN_INT32_TRIGGER_MODE_VAL_STEPPED = 3;
  NIFGEN_INT32_TRIGGER_MODE_VAL_BURST = 4;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE = 0;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_EXTERNAL = 1;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG = 2;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL0 = 111;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL1 = 112;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL2 = 113;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL3 = 114;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL4 = 115;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL5 = 116;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL6 = 117;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PXI_STAR = 131;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_0 = 141;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_1 = 142;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_2 = 143;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_3 = 144;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_4 = 145;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_5 = 146;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_6 = 147;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_7 = 1010;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_0 = 1011;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_1 = 1012;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_2 = 1013;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_3 = 1014;
  NIFGEN_INT32_TRIGGER_SOURCE_VAL_OTHER_TERMINAL = 1018;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_INTERNAL = 0;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_EXTERNAL = 1;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL1 = 112;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL2 = 113;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL3 = 114;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL4 = 115;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL5 = 116;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL6 = 117;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_PXI_STAR = 131;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_0 = 141;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_1 = 142;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_2 = 143;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_3 = 144;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_4 = 145;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_5 = 146;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_6 = 147;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_7 = 1010;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_OTHER_TERMINAL = 1018;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_CLK_IN = 1202;
  NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_DDC_CLK_IN = 1203;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_B = 0;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_D = 1;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_G = 2;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_H = 3;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_I = 4;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_M = 5;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_N = 6;
  NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_NTSC_M = 7;
  NIFGEN_INT32_WAIT_BEHAVIOR_VAL_HOLD_LAST_VALUE = 400;
  NIFGEN_INT32_WAIT_BEHAVIOR_VAL_JUMP_TO_VALUE = 401;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_SINE = 1;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_SQUARE = 2;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_TRIANGLE = 3;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_UP = 4;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_DOWN = 5;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_DC = 6;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_NOISE = 101;
  NIFGEN_INT32_WAVEFORM_VAL_WFM_USER = 102;
}

enum NiFgenReal64AttributeValues {
  option allow_alias = true;
  NIFGEN_REAL64_UNSPECIFIED = 0;
  NIFGEN_REAL64_LOAD_IMPEDANCE_VAL_MATCHED_LOAD_IMPEDANCE = -1;
  NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_50_OHMS = 50;
  NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_75_OHMS = 75;
  NIFGEN_REAL64_SAMPLE_RATE_VAL_EXTERNAL_SAMPLE_RATE = -1;
}

enum NiFgenStringAttributeValuesMapped {
  NIFGEN_STRING_MAPPED_UNSPECIFIED = 0;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_CLOCK_IN_COLLISION_AVOIDANCE = 1;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_NONE_COLLISION_AVOIDANCE = 2;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE = 3;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_PXI_CLOCK_COLLISION_AVOIDANCE = 4;
  NIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_RTSI_7_COLLISION_AVOIDANCE = 5;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_CLOCK_IN = 6;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_DDC_CLOCK_IN = 7;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_ONBOARD_CLOCK = 8;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_STAR_LINE = 9;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_0_RTSI_0 = 10;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_1_RTSI_1 = 11;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_2_RTSI_2 = 12;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_3_RTSI_3 = 13;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_4_RTSI_4 = 14;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_5_RTSI_5 = 15;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_6_RTSI_6 = 16;
  NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_7_RTSI_7 = 17;
  NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_CLOCK_IN = 18;
  NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_ONBOARD_CLOCK = 19;
}

enum OutputMode {
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FUNC = 0;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB = 1;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SEQ = 2;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FREQ_LIST = 101;
  OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SCRIPT = 102;
}

enum RelativeTo {
  RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_START = 0;
  RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_CURRENT = 1;
}

enum RouteSignalFrom {
  ROUTE_SIGNAL_FROM_UNSPECIFIED = 0;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_MARKER = 1001;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNC_OUT = 1002;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_OUT_START_TRIGGER = 1004;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_BOARD_CLOCK = 1006;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNCHRONIZATION = 1007;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_SOFTWARE_TRIG = 2;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_REF_OUT = 1008;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_CLOCK_OUT = 1009;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_PXI_STAR = 131;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_PFI_0 = 1011;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_0 = 141;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_1 = 142;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_2 = 143;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_3 = 144;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_4 = 145;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_5 = 146;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_6 = 147;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_7 = 1010;
  ROUTE_SIGNAL_FROM_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK = 1019;
}

enum RouteSignalTo {
  ROUTE_SIGNAL_TO_UNSPECIFIED = 0;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_0 = 141;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_1 = 142;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_2 = 143;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_3 = 144;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_4 = 145;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_5 = 146;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_6 = 147;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_7 = 1010;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_REF_OUT = 1008;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_0 = 1011;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_1 = 1012;
  ROUTE_SIGNAL_TO_NIFGEN_VAL_PXI_STAR = 131;
}

enum ScriptTriggerDigitalEdgeEdge {
  SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_UNSPECIFIED = 0;
  SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_NIFGEN_VAL_RISING_EDGE = 101;
  SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_NIFGEN_VAL_FALLING_EDGE = 102;
}

enum SequenceHandle {
  SEQUENCE_HANDLE_UNSPECIFIED = 0;
  SEQUENCE_HANDLE_NIFGEN_VAL_ALL_SEQUENCES = -1;
}

enum Signal {
  SIGNAL_UNSPECIFIED = 0;
  SIGNAL_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK = 1019;
  SIGNAL_NIFGEN_VAL_SYNC_OUT = 1002;
  SIGNAL_NIFGEN_VAL_START_TRIGGER = 1004;
  SIGNAL_NIFGEN_VAL_MARKER_EVENT = 1001;
  SIGNAL_NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE = 1006;
  SIGNAL_NIFGEN_VAL_SYNCHRONIZATION = 1007;
  SIGNAL_NIFGEN_VAL_SAMPLE_CLOCK = 101;
  SIGNAL_NIFGEN_VAL_REFERENCE_CLOCK = 102;
  SIGNAL_NIFGEN_VAL_SCRIPT_TRIGGER = 103;
  SIGNAL_NIFGEN_VAL_READY_FOR_START_EVENT = 105;
  SIGNAL_NIFGEN_VAL_STARTED_EVENT = 106;
  SIGNAL_NIFGEN_VAL_DONE_EVENT = 107;
  SIGNAL_NIFGEN_VAL_DATA_MARKER_EVENT = 108;
}

enum StartTriggerDigitalEdgeEdge {
  START_TRIGGER_DIGITAL_EDGE_EDGE_UNSPECIFIED = 0;
  START_TRIGGER_DIGITAL_EDGE_EDGE_NIFGEN_VAL_RISING_EDGE = 101;
  START_TRIGGER_DIGITAL_EDGE_EDGE_NIFGEN_VAL_FALLING_EDGE = 102;
}

enum Trigger {
  TRIGGER_UNSPECIFIED = 0;
  TRIGGER_NIFGEN_VAL_START_TRIGGER = 1004;
  TRIGGER_NIFGEN_VAL_SCRIPT_TRIGGER = 103;
}

enum TriggerMode {
  TRIGGER_MODE_UNSPECIFIED = 0;
  TRIGGER_MODE_NIFGEN_VAL_SINGLE = 1;
  TRIGGER_MODE_NIFGEN_VAL_CONTINUOUS = 2;
  TRIGGER_MODE_NIFGEN_VAL_STEPPED = 3;
  TRIGGER_MODE_NIFGEN_VAL_BURST = 4;
}

enum TriggerWhen {
  TRIGGER_WHEN_UNSPECIFIED = 0;
  TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_HIGH = 101;
  TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_LOW = 102;
}

enum Waveform {
  WAVEFORM_UNSPECIFIED = 0;
  WAVEFORM_NIFGEN_VAL_WFM_SINE = 1;
  WAVEFORM_NIFGEN_VAL_WFM_SQUARE = 2;
  WAVEFORM_NIFGEN_VAL_WFM_TRIANGLE = 3;
  WAVEFORM_NIFGEN_VAL_WFM_RAMP_UP = 4;
  WAVEFORM_NIFGEN_VAL_WFM_RAMP_DOWN = 5;
  WAVEFORM_NIFGEN_VAL_WFM_DC = 6;
  WAVEFORM_NIFGEN_VAL_WFM_NOISE = 101;
  WAVEFORM_NIFGEN_VAL_WFM_USER = 102;
}

enum WaveformHandle {
  WAVEFORM_HANDLE_UNSPECIFIED = 0;
  WAVEFORM_HANDLE_NIFGEN_VAL_ALL_WAVEFORMS = -1;
}

message AbortGenerationRequest {
  nidevice_grpc.Session vi = 1;
}

message AbortGenerationResponse {
  int32 status = 1;
}

message AdjustSampleClockRelativeDelayRequest {
  nidevice_grpc.Session vi = 1;
  double adjustment_time = 2;
}

message AdjustSampleClockRelativeDelayResponse {
  int32 status = 1;
}

message AllocateNamedWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  sint32 waveform_size = 4;
}

message AllocateNamedWaveformResponse {
  int32 status = 1;
}

message AllocateWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_size = 3;
}

message AllocateWaveformResponse {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CheckAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message CheckAttributeViBooleanResponse {
  int32 status = 1;
}

message CheckAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message CheckAttributeViInt32Response {
  int32 status = 1;
}

message CheckAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  int64 attribute_value_raw = 4;
}

message CheckAttributeViInt64Response {
  int32 status = 1;
}

message CheckAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
  }
}

message CheckAttributeViReal64Response {
  int32 status = 1;
}

message CheckAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message CheckAttributeViSessionResponse {
  int32 status = 1;
}

message CheckAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    string attribute_value_raw = 4;
    NiFgenStringAttributeValuesMapped attribute_value_mapped = 5;
  }
}

message CheckAttributeViStringResponse {
  int32 status = 1;
}

message ClearArbMemoryRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearArbMemoryResponse {
  int32 status = 1;
}

message ClearArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  oneof sequence_handle_enum {
    SequenceHandle sequence_handle = 2;
    sint32 sequence_handle_raw = 3;
  }
}

message ClearArbSequenceResponse {
  int32 status = 1;
}

message ClearArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  oneof waveform_handle_enum {
    WaveformHandle waveform_handle = 2;
    sint32 waveform_handle_raw = 3;
  }
}

message ClearArbWaveformResponse {
  int32 status = 1;
}

message ClearErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearErrorResponse {
  int32 status = 1;
}

message ClearFreqListRequest {
  nidevice_grpc.Session vi = 1;
  oneof frequency_list_handle_enum {
    FrequencyListOptions frequency_list_handle = 2;
    sint32 frequency_list_handle_raw = 3;
  }
}

message ClearFreqListResponse {
  int32 status = 1;
}

message ClearInterchangeWarningsRequest {
  nidevice_grpc.Session vi = 1;
}

message ClearInterchangeWarningsResponse {
  int32 status = 1;
}

message ClearUserStandardWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message ClearUserStandardWaveformResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session vi = 1;
}

message CloseResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session vi = 1;
}

message CommitResponse {
  int32 status = 1;
}

message ConfigureAmplitudeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double amplitude = 3;
}

message ConfigureAmplitudeResponse {
  int32 status = 1;
}

message ConfigureArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 sequence_handle = 3;
  double gain = 4;
  double offset = 5;
}

message ConfigureArbSequenceResponse {
  int32 status = 1;
}

message ConfigureArbWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  double gain = 4;
  double offset = 5;
}

message ConfigureArbWaveformResponse {
  int32 status = 1;
}

message ConfigureChannelsRequest {
  nidevice_grpc.Session vi = 1;
  string channels = 2;
}

message ConfigureChannelsResponse {
  int32 status = 1;
}

message ConfigureClockModeRequest {
  nidevice_grpc.Session vi = 1;
  oneof clock_mode_enum {
    ClockMode clock_mode = 2;
    sint32 clock_mode_raw = 3;
  }
}

message ConfigureClockModeResponse {
  int32 status = 1;
}

message ConfigureCustomFIRFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double coefficients_array = 3;
}

message ConfigureCustomFIRFilterCoefficientsResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
  string source = 3;
  oneof edge_enum {
    ScriptTriggerDigitalEdgeEdge edge = 4;
    sint32 edge_raw = 5;
  }
}

message ConfigureDigitalEdgeScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string source = 2;
  oneof edge_enum {
    StartTriggerDigitalEdgeEdge edge = 3;
    sint32 edge_raw = 4;
  }
}

message ConfigureDigitalEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureDigitalLevelScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
  string source = 3;
  oneof trigger_when_enum {
    TriggerWhen trigger_when = 4;
    sint32 trigger_when_raw = 5;
  }
}

message ConfigureDigitalLevelScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureFreqListRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 frequency_list_handle = 3;
  double amplitude = 4;
  double dc_offset = 5;
  double start_phase = 6;
}

message ConfigureFreqListResponse {
  int32 status = 1;
}

message ConfigureFrequencyRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double frequency = 3;
}

message ConfigureFrequencyResponse {
  int32 status = 1;
}

message ConfigureOperationModeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 operation_mode = 3;
}

message ConfigureOperationModeResponse {
  int32 status = 1;
}

message ConfigureOutputEnabledRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  bool enabled = 3;
}

message ConfigureOutputEnabledResponse {
  int32 status = 1;
}

message ConfigureOutputImpedanceRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double impedance = 3;
}

message ConfigureOutputImpedanceResponse {
  int32 status = 1;
}

message ConfigureOutputModeRequest {
  nidevice_grpc.Session vi = 1;
  oneof output_mode_enum {
    OutputMode output_mode = 2;
    sint32 output_mode_raw = 3;
  }
}

message ConfigureOutputModeResponse {
  int32 status = 1;
}

message ConfigureP2PEndpointFullnessStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
  sint32 p2p_endpoint_fullness_level = 2;
}

message ConfigureP2PEndpointFullnessStartTriggerResponse {
  int32 status = 1;
}

message ConfigureReferenceClockRequest {
  nidevice_grpc.Session vi = 1;
  string reference_clock_source = 2;
  double reference_clock_frequency = 3;
}

message ConfigureReferenceClockResponse {
  int32 status = 1;
}

message ConfigureSampleClockSourceRequest {
  nidevice_grpc.Session vi = 1;
  string sample_clock_source = 2;
}

message ConfigureSampleClockSourceResponse {
  int32 status = 1;
}

message ConfigureSampleRateRequest {
  nidevice_grpc.Session vi = 1;
  double sample_rate = 2;
}

message ConfigureSampleRateResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
}

message ConfigureSoftwareEdgeScriptTriggerResponse {
  int32 status = 1;
}

message ConfigureSoftwareEdgeStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message ConfigureSoftwareEdgeStartTriggerResponse {
  int32 status = 1;
}

message ConfigureStandardWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof waveform_enum {
    Waveform waveform = 3;
    sint32 waveform_raw = 4;
  }
  double amplitude = 5;
  double dc_offset = 6;
  double frequency = 7;
  double start_phase = 8;
}

message ConfigureStandardWaveformResponse {
  int32 status = 1;
}

message ConfigureSynchronizationRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 synchronization_source = 3;
}

message ConfigureSynchronizationResponse {
  int32 status = 1;
}

message ConfigureTriggerModeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof trigger_mode_enum {
    TriggerMode trigger_mode = 3;
    sint32 trigger_mode_raw = 4;
  }
}

message ConfigureTriggerModeResponse {
  int32 status = 1;
}

message CreateAdvancedArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 waveform_handles_array = 2;
  repeated sint32 loop_counts_array = 3;
  repeated sint32 sample_counts_array = 4;
  repeated sint32 marker_location_array = 5;
}

message CreateAdvancedArbSequenceResponse {
  int32 status = 1;
  repeated sint32 coerced_markers_array = 2;
  sint32 sequence_handle = 3;
}

message CreateArbSequenceRequest {
  nidevice_grpc.Session vi = 1;
  repeated sint32 waveform_handles_array = 2;
  repeated sint32 loop_counts_array = 3;
}

message CreateArbSequenceResponse {
  int32 status = 1;
  sint32 sequence_handle = 2;
}

message CreateFreqListRequest {
  nidevice_grpc.Session vi = 1;
  oneof waveform_enum {
    Waveform waveform = 2;
    sint32 waveform_raw = 3;
  }
  repeated double frequency_array = 4;
  repeated double duration_array = 5;
}

message CreateFreqListResponse {
  int32 status = 1;
  sint32 frequency_list_handle = 2;
}

message CreateWaveformComplexF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated nidevice_grpc.NIComplexNumber waveform_data_array = 3;
}

message CreateWaveformComplexF64Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double waveform_data_array = 3;
}

message CreateWaveformF64Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformFromFileF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_name = 3;
  oneof byte_order_enum {
    ByteOrder byte_order = 4;
    sint32 byte_order_raw = 5;
  }
}

message CreateWaveformFromFileF64Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformFromFileHWSRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_name = 3;
  bool use_rate_from_waveform = 4;
  bool use_gain_and_offset_from_waveform = 5;
}

message CreateWaveformFromFileHWSResponse {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformFromFileI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string file_name = 3;
  oneof byte_order_enum {
    ByteOrder byte_order = 4;
    sint32 byte_order_raw = 5;
  }
}

message CreateWaveformFromFileI16Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message CreateWaveformI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated sint32 waveform_data_array = 3;
}

message CreateWaveformI16Response {
  int32 status = 1;
  sint32 waveform_handle = 2;
}

message DefineUserStandardWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated double waveform_data_array = 3;
}

message DefineUserStandardWaveformResponse {
  int32 status = 1;
}

message DeleteNamedWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
}

message DeleteNamedWaveformResponse {
  int32 status = 1;
}

message DeleteScriptRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string script_name = 3;
}

message DeleteScriptResponse {
  int32 status = 1;
}

message DisableRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableResponse {
  int32 status = 1;
}

message DisableAnalogFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableAnalogFilterResponse {
  int32 status = 1;
}

message DisableDigitalFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableDigitalFilterResponse {
  int32 status = 1;
}

message DisableDigitalPatterningRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message DisableDigitalPatterningResponse {
  int32 status = 1;
}

message DisableScriptTriggerRequest {
  nidevice_grpc.Session vi = 1;
  string trigger_id = 2;
}

message DisableScriptTriggerResponse {
  int32 status = 1;
}

message DisableStartTriggerRequest {
  nidevice_grpc.Session vi = 1;
}

message DisableStartTriggerResponse {
  int32 status = 1;
}

message EnableAnalogFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  double filter_correction_frequency = 3;
}

message EnableAnalogFilterResponse {
  int32 status = 1;
}

message EnableDigitalFilterRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message EnableDigitalFilterResponse {
  int32 status = 1;
}

message EnableDigitalPatterningRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message EnableDigitalPatterningResponse {
  int32 status = 1;
}

message ErrorHandlerRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorHandlerResponse {
  int32 status = 1;
  string error_message = 2;
}

message ErrorMessageRequest {
  nidevice_grpc.Session vi = 1;
  sint32 error_code = 2;
}

message ErrorMessageResponse {
  int32 status = 1;
  string error_message = 2;
}

message ErrorQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message ErrorQueryResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_message = 3;
}

message ExportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
}

message ExportAttributeConfigurationBufferResponse {
  int32 status = 1;
  bytes configuration = 2;
}

message ExportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ExportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message ExportSignalRequest {
  nidevice_grpc.Session vi = 1;
  oneof signal_enum {
    Signal signal = 2;
    sint32 signal_raw = 3;
  }
  string signal_identifier = 4;
  string output_terminal = 5;
}

message ExportSignalResponse {
  int32 status = 1;
}

message GetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViBooleanResponse {
  int32 status = 1;
  bool attribute_value = 2;
}

message GetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViInt32Response {
  int32 status = 1;
  sint32 attribute_value = 2;
}

message GetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViInt64Response {
  int32 status = 1;
  int64 attribute_value = 2;
}

message GetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViReal64Response {
  int32 status = 1;
  double attribute_value = 2;
}

message GetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViSessionResponse {
  int32 status = 1;
  nidevice_grpc.Session attribute_value = 2;
}

message GetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message GetAttributeViStringResponse {
  int32 status = 1;
  string attribute_value = 2;
}

message GetChannelNameRequest {
  nidevice_grpc.Session vi = 1;
  sint32 index = 2;
}

message GetChannelNameResponse {
  int32 status = 1;
  string channel_string = 2;
}

message GetErrorRequest {
  nidevice_grpc.Session vi = 1;
}

message GetErrorResponse {
  int32 status = 1;
  sint32 error_code = 2;
  string error_description = 3;
}

message GetExtCalLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetExtCalLastTempRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalLastTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetExtCalRecommendedIntervalRequest {
  nidevice_grpc.Session vi = 1;
}

message GetExtCalRecommendedIntervalResponse {
  int32 status = 1;
  sint32 months = 2;
}

message GetFIRFilterCoefficientsRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
}

message GetFIRFilterCoefficientsResponse {
  int32 status = 1;
  repeated double coefficients_array = 2;
  sint32 number_of_coefficients_read = 3;
}

message GetHardwareStateRequest {
  nidevice_grpc.Session vi = 1;
}

message GetHardwareStateResponse {
  int32 status = 1;
  HardwareState state = 2;
  sint32 state_raw = 3;
}

message GetSelfCalLastDateAndTimeRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalLastDateAndTimeResponse {
  int32 status = 1;
  sint32 year = 2;
  sint32 month = 3;
  sint32 day = 4;
  sint32 hour = 5;
  sint32 minute = 6;
}

message GetSelfCalLastTempRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalLastTempResponse {
  int32 status = 1;
  double temperature = 2;
}

message GetSelfCalSupportedRequest {
  nidevice_grpc.Session vi = 1;
}

message GetSelfCalSupportedResponse {
  int32 status = 1;
  bool self_cal_supported = 2;
}

message GetStreamEndpointHandleRequest {
  nidevice_grpc.Session vi = 1;
  string stream_endpoint = 2;
}

message GetStreamEndpointHandleResponse {
  int32 status = 1;
  uint32 reader_handle = 2;
}

message ImportAttributeConfigurationBufferRequest {
  nidevice_grpc.Session vi = 1;
  bytes configuration = 2;
}

message ImportAttributeConfigurationBufferResponse {
  int32 status = 1;
}

message ImportAttributeConfigurationFileRequest {
  nidevice_grpc.Session vi = 1;
  string file_path = 2;
}

message ImportAttributeConfigurationFileResponse {
  int32 status = 1;
}

message InitRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message InitResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitWithOptionsRequest {
  string session_name = 1;
  string resource_name = 2;
  bool id_query = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitWithOptionsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitializeWithChannelsRequest {
  string session_name = 1;
  string resource_name = 2;
  string channel_name = 3;
  bool reset_device = 4;
  string option_string = 5;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 6;
}

message InitializeWithChannelsResponse {
  int32 status = 1;
  nidevice_grpc.Session vi = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitiateGenerationRequest {
  nidevice_grpc.Session vi = 1;
}

message InitiateGenerationResponse {
  int32 status = 1;
}

message InvalidateAllAttributesRequest {
  nidevice_grpc.Session vi = 1;
}

message InvalidateAllAttributesResponse {
  int32 status = 1;
}

message IsDoneRequest {
  nidevice_grpc.Session vi = 1;
}

message IsDoneResponse {
  int32 status = 1;
  bool done = 2;
}

message ManualEnableP2PStreamRequest {
  nidevice_grpc.Session vi = 1;
  string endpoint_name = 2;
}

message ManualEnableP2PStreamResponse {
  int32 status = 1;
}

message QueryArbSeqCapabilitiesRequest {
  nidevice_grpc.Session vi = 1;
}

message QueryArbSeqCapabilitiesResponse {
  int32 status = 1;
  sint32 maximum_number_of_sequences = 2;
  sint32 minimum_sequence_length = 3;
  sint32 maximum_sequence_length = 4;
  sint32 maximum_loop_count = 5;
}

message QueryArbWfmCapabilitiesRequest {
  nidevice_grpc.Session vi = 1;
}

message QueryArbWfmCapabilitiesResponse {
  int32 status = 1;
  sint32 maximum_number_of_waveforms = 2;
  sint32 waveform_quantum = 3;
  sint32 minimum_waveform_size = 4;
  sint32 maximum_waveform_size = 5;
}

message QueryFreqListCapabilitiesRequest {
  nidevice_grpc.Session vi = 1;
}

message QueryFreqListCapabilitiesResponse {
  int32 status = 1;
  sint32 maximum_number_of_freq_lists = 2;
  sint32 minimum_frequency_list_length = 3;
  sint32 maximum_frequency_list_length = 4;
  double minimum_frequency_list_duration = 5;
  double maximum_frequency_list_duration = 6;
  double frequency_list_duration_quantum = 7;
}

message ReadCurrentTemperatureRequest {
  nidevice_grpc.Session vi = 1;
}

message ReadCurrentTemperatureResponse {
  int32 status = 1;
  double temperature = 2;
}

message ResetRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetResponse {
  int32 status = 1;
}

message ResetAttributeRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
}

message ResetAttributeResponse {
  int32 status = 1;
}

message ResetDeviceRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetDeviceResponse {
  int32 status = 1;
}

message ResetInterchangeCheckRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetInterchangeCheckResponse {
  int32 status = 1;
}

message ResetWithDefaultsRequest {
  nidevice_grpc.Session vi = 1;
}

message ResetWithDefaultsResponse {
  int32 status = 1;
}

message RevisionQueryRequest {
  nidevice_grpc.Session vi = 1;
}

message RevisionQueryResponse {
  int32 status = 1;
  string instrument_driver_revision = 2;
  string firmware_revision = 3;
}

message RouteSignalOutRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  oneof route_signal_from_enum {
    RouteSignalFrom route_signal_from = 3;
    sint32 route_signal_from_raw = 4;
  }
  oneof route_signal_to_enum {
    RouteSignalTo route_signal_to = 5;
    sint32 route_signal_to_raw = 6;
  }
}

message RouteSignalOutResponse {
  int32 status = 1;
}

message SelfCalRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfCalResponse {
  int32 status = 1;
}

message SelfTestRequest {
  nidevice_grpc.Session vi = 1;
}

message SelfTestResponse {
  int32 status = 1;
  sint32 self_test_result = 2;
  string self_test_message = 3;
}

message SendSoftwareEdgeTriggerRequest {
  nidevice_grpc.Session vi = 1;
  oneof trigger_enum {
    Trigger trigger = 2;
    sint32 trigger_raw = 3;
  }
  string trigger_id = 4;
}

message SendSoftwareEdgeTriggerResponse {
  int32 status = 1;
}

message SetAttributeViBooleanRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  bool attribute_value = 4;
}

message SetAttributeViBooleanResponse {
  int32 status = 1;
}

message SetAttributeViInt32Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenInt32AttributeValues attribute_value = 4;
    sint32 attribute_value_raw = 5;
  }
}

message SetAttributeViInt32Response {
  int32 status = 1;
}

message SetAttributeViInt64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  int64 attribute_value_raw = 4;
}

message SetAttributeViInt64Response {
  int32 status = 1;
}

message SetAttributeViReal64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    NiFgenReal64AttributeValues attribute_value = 4;
    double attribute_value_raw = 5;
  }
}

message SetAttributeViReal64Response {
  int32 status = 1;
}

message SetAttributeViSessionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  nidevice_grpc.Session attribute_value = 4;
}

message SetAttributeViSessionResponse {
  int32 status = 1;
}

message SetAttributeViStringRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  NiFgenAttribute attribute_id = 3;
  oneof attribute_value_enum {
    string attribute_value_raw = 4;
    NiFgenStringAttributeValuesMapped attribute_value_mapped = 5;
  }
}

message SetAttributeViStringResponse {
  int32 status = 1;
}

message SetNamedWaveformNextWritePositionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  oneof relative_to_enum {
    RelativeTo relative_to = 4;
    sint32 relative_to_raw = 5;
  }
  sint32 offset = 6;
}

message SetNamedWaveformNextWritePositionResponse {
  int32 status = 1;
}

message SetWaveformNextWritePositionRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  oneof relative_to_enum {
    RelativeTo relative_to = 4;
    sint32 relative_to_raw = 5;
  }
  sint32 offset = 6;
}

message SetWaveformNextWritePositionResponse {
  int32 status = 1;
}

message WaitUntilDoneRequest {
  nidevice_grpc.Session vi = 1;
  sint32 max_time = 2;
}

message WaitUntilDoneResponse {
  int32 status = 1;
}

message WriteBinary16WaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  repeated sint32 data = 4;
}

message WriteBinary16WaveformResponse {
  int32 status = 1;
}

message WriteComplexBinary16WaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  repeated nidevice_grpc.NIComplexI16 data = 4;
}

message WriteComplexBinary16WaveformResponse {
  int32 status = 1;
}

message WriteNamedWaveformComplexF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated nidevice_grpc.NIComplexNumber data = 4;
}

message WriteNamedWaveformComplexF64Response {
  int32 status = 1;
}

message WriteNamedWaveformComplexI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated nidevice_grpc.NIComplexI16 data = 4;
}

message WriteNamedWaveformComplexI16Response {
  int32 status = 1;
}

message WriteNamedWaveformF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated double data = 4;
}

message WriteNamedWaveformF64Response {
  int32 status = 1;
}

message WriteNamedWaveformI16Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string waveform_name = 3;
  repeated sint32 data = 4;
}

message WriteNamedWaveformI16Response {
  int32 status = 1;
}

message WriteP2PEndpointI16Request {
  nidevice_grpc.Session vi = 1;
  string endpoint_name = 2;
  repeated sint32 endpoint_data = 3;
}

message WriteP2PEndpointI16Response {
  int32 status = 1;
}

message WriteScriptRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  string script = 3;
}

message WriteScriptResponse {
  int32 status = 1;
}

message WriteWaveformRequest {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  sint32 waveform_handle = 3;
  repeated double data = 4;
}

message WriteWaveformResponse {
  int32 status = 1;
}

message WriteWaveformComplexF64Request {
  nidevice_grpc.Session vi = 1;
  string channel_name = 2;
  repeated nidevice_grpc.NIComplexNumber data = 3;
  sint32 waveform_handle = 4;
}

message WriteWaveformComplexF64Response {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifgen/README.md sha256=c6705733df41879986897b9901bc0119e7e8506566b43d91e0f9dec1cc509fed bytes=209 -->
## FILE: source/codegen/metadata/nifgen/README.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifgen/README.md`
- sha256: `c6705733df41879986897b9901bc0119e7e8506566b43d91e0f9dec1cc509fed`
- bytes: 209

````markdown
# Updating

To update this metadata folder. Find the nifgen_grpc_device export and copy the contents of its metadata folder here.

# More info

Refer to source/codegen/metadata/Imported_From_Hapigen.md
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/__init__.py sha256=80aa5e93c151b9a34e9755e0c4a699cb31ceb6c43e74436ffb5e5770ebb452ad bytes=250 -->
## FILE: source/codegen/metadata/nifpga/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/__init__.py`
- sha256: `80aa5e93c151b9a34e9755e0c4a699cb31ceb6c43e74436ffb5e5770ebb452ad`
- bytes: 250

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions" : functions,
    "attributes" : attributes,
    "enums" : enums,
    "config" : config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/attributes.py sha256=b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4 bytes=19 -->
## FILE: source/codegen/metadata/nifpga/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/attributes.py`
- sha256: `b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4`
- bytes: 19

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/attributes_addon.py sha256=cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f bytes=207 -->
## FILE: source/codegen/metadata/nifpga/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/attributes_addon.py`
- sha256: `cc1c959f4897331962afb88b70c9113f69792f3a401b5f826fa1e45f4d27261f`
- bytes: 207

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/config.py sha256=4eccfde9f4c82e7e0fe378d4d9b24add94ee13491ecda2d90403b28785245583 bytes=1807 -->
## FILE: source/codegen/metadata/nifpga/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/config.py`
- sha256: `4eccfde9f4c82e7e0fe378d4d9b24add94ee13491ecda2d90403b28785245583`
- bytes: 1807

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '24.3.0',
    'c_header': 'NiFpga.h',
    'c_function_prefix': 'NiFpga_',
    'c_dll_function_prefix': 'NiFpgaDll_',
    'service_class_prefix': 'NiFpga',
    'java_package': 'com.ni.grpc.nifpga',
    'csharp_namespace': 'NationalInstruments.Grpc.NiFpga',
    'namespace_component': 'nifpga',
    'init_function': 'Open',
    'close_function': 'Close',
    'code_readiness': 'Release',
    'driver_name': 'NI-FPGA',
    'status_ok': 'status >= 0',
    'additional_protos': ['data_moniker.proto'],
    'resource_handle_type': ['NiFpga_Session'],
    'type_to_grpc_type': {
        'NiFpga_Session': 'nidevice_grpc.Session',
        'char[]': 'string',
        'NiFpga_Status': 'int32',
        'size_t': 'uint32',
        'int8_t': 'int32',
        'int16_t': 'int32',
        'int32_t': 'int32',
        'int64_t': 'int64',       
        'uint8_t':'uint32',
        'uint16_t': 'uint32',
        'uint32_t': 'uint32',
        'uint64_t': 'uint64',  
        'NiFpga_Bool': 'bool',
        'NiFpga_FifoProperty': 'uint32',
    },
    'has_moniker_streaming_apis': True,
    'custom_types': [],
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'NiFpga',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'NiFpga.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'NiFpga.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': True,
    'metadata_version': '0.1',
    'module_name': 'nifpga',
    'session_class_description': 'An NI-FPGA session.',
    'session_handle_parameter_name': 'session'
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/config_addon.py sha256=d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58 bytes=226 -->
## FILE: source/codegen/metadata/nifpga/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/config_addon.py`
- sha256: `d89084eb696ad3171488ab595af6d7415b8f7b9e66cd2472808ce19490a19b58`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '20.5.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/enums.py sha256=929e5021702bbfa6e4533d7d313da423e706186a1a4f05247afa665ea301e514 bytes=6447 -->
## FILE: source/codegen/metadata/nifpga/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/enums.py`
- sha256: `929e5021702bbfa6e4533d7d313da423e706186a1a4f05247afa665ea301e514`
- bytes: 6447

````python
enums = {
    'CloseAttribute': {
        'values': [
            {
                'name': 'NO_RESET_IF_LAST_SESSION',
                'value': 1
            }
        ]
    },
    'FifoFlowControl': {
        'force-include': True,
        'values': [
            {
                'name': 'DISABLED',
                'value': 1
            },
            {
                'name': 'ENABLED',
                'value': 2
            }
        ]
    },
    'FifoProperty': {
        'values': [
            {
                'name': 'BYTES_PER_ELEMENT',
                'value': 1
            },
            {
                'name': 'HOST_BUFFER_ALLOCATION_GRANULARITY',
                'value': 2
            },
            {
                'name': 'HOST_BUFFER_SIZE',
                'value': 3
            },
            {
                'name': 'HOST_BUFFER_MIRROR_SIZE',
                'value': 4
            },
            {
                'name': 'HOST_BUFFER_TYPE',
                'value': 5
            },
            {
                'name': 'HOST_BUFFER',
                'value': 6
            },
            {
                'name': 'FLOW_CONTROL',
                'value': 7
            },
            {
                'name': 'ELEMENTS_CURRENTLY_ACQUIRED',
                'value': 8
            },
            {
                'name': 'PREFERRED_NUMA_NODE',
                'value': 9
            },
            {
                'name': 'NUMBER_OF_ZERO_COPY_REGIONS',
                'value': 10
            },
            {
                'name': 'NOT_SUPPORTED',
                'value': 0
            }
        ]
    },
    'FpgaViState': {
        'values': [
            {
                'name': 'NOT_RUNNING',
                'value': 0
            },
            {
                'name': 'INVALID',
                'value': 1
            },
            {
                'name': 'RUNNING',
                'value': 2
            },
            {
                'name': 'NATURALLY_STOPPED',
                'value': 3
            }
        ]
    },
    'HostBufferType': {
        'force-include': True,
        'values': [
            {
                'name': 'ALLOCATED_BY_RIO',
                'value': 1
            },
            {
                'name': 'ALLOCATED_BY_USER',
                'value': 2
            }
        ]
    },
    'Irq': {
        'force-include': True,
        'generate-mappings': True,
        'values': [
            {
                'name': 'Irq_0',
                'value': 1
            },
            {
                'name': 'Irq_1',
                'value': 2
            },
            {
                'name': 'Irq_2',
                'value': 4
            },
            {
                'name': 'Irq_3',
                'value': 8
            },
            {
                'name': 'Irq_4',
                'value': 16
            },
            {
                'name': 'Irq_5',
                'value': 32
            },
            {
                'name': 'Irq_6',
                'value': 64
            },
            {
                'name': 'Irq_7',
                'value': 128
            },
            {
                'name': 'Irq_8',
                'value': 256
            },
            {
                'name': 'Irq_9',
                'value': 512
            },
            {
                'name': 'Irq_10',
                'value': 1024
            },
            {
                'name': 'Irq_11',
                'value': 2048
            },
            {
                'name': 'Irq_12',
                'value': 4096
            },
            {
                'name': 'Irq_13',
                'value': 8192
            },
            {
                'name': 'Irq_14',
                'value': 16384
            },
            {
                'name': 'Irq_15',
                'value': 32768
            },
            {
                'name': 'Irq_16',
                'value': 65536
            },
            {
                'name': 'Irq_17',
                'value': 131072
            },
            {
                'name': 'Irq_18',
                'value': 262144
            },
            {
                'name': 'Irq_19',
                'value': 524288
            },
            {
                'name': 'Irq_20',
                'value': 1048576
            },
            {
                'name': 'Irq_21',
                'value': 2097152
            },
            {
                'name': 'Irq_22',
                'value': 4194304
            },
            {
                'name': 'Irq_23',
                'value': 8388608
            },
            {
                'name': 'Irq_24',
                'value': 16777216
            },
            {
                'name': 'Irq_25',
                'value': 33554432
            },
            {
                'name': 'Irq_26',
                'value': 67108864
            },
            {
                'name': 'Irq_27',
                'value': 134217728
            },
            {
                'name': 'Irq_28',
                'value': 268435456
            },
            {
                'name': 'Irq_29',
                'value': 536870912
            },
            {
                'name': 'Irq_30',
                'value': 1073741824
            },
            {
                'name': 'Irq_31',
                'value': 2147483648
            }
        ]
    },
    'OpenAttribute': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'NO_RUN',
                'value': 1
            },
            {
                'name': 'BITFILE_PATH_IS_UTF8',
                'value': 2
            },
            {
                'name': 'BITFILE_CONTENTS_NOT_PATH',
                'value': 1073741824
            },
            {
                'name': 'IGNORE_SIGNATURE_ARGUMENT',
                'value': 2147483648
            }
        ]
    },
    'RunAttribute': {
        'values': [
            {
                'name': 'WAIT_UNTIL_DONE',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/enums_addon.py sha256=9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900 bytes=192 -->
## FILE: source/codegen/metadata/nifpga/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/enums_addon.py`
- sha256: `9f25172e660fd7e043e0a5b4bbd8669084c5cf552aa295713232ee352147b900`
- bytes: 192

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/functions.py sha256=e0f55514695be243eda710864eb8c3b5beeca75b58bb557f518412b8e096d3d8 bytes=115146 -->
## FILE: source/codegen/metadata/nifpga/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/functions.py`
- sha256: `e0f55514695be243eda710864eb8c3b5beeca75b58bb557f518412b8e096d3d8`
- bytes: 115146

````python
functions = {
    'Abort': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcknowledgeIrqs': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'irqs',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsBool': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'NiFpga_Bool *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsDbl': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'double *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsI16': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int16_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsI32': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int32_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsI64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int64_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsI8': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int8_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsSgl': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'float *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsU16': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint16_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsU32': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint32_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsU64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint64_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadElementsU8': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint8_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoReadRegion': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'region',
                'type': 'void *'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'void *'
            },
            {
                'direction': 'in',
                'name': 'isSigned',
                'type': 'NiFpga_Bool'
            },
            {
                'direction': 'in',
                'name': 'elementSizeBytes',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsBool': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'NiFpga_Bool *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsDbl': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'double *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsI16': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int16_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsI32': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int32_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsI64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int64_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsI8': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'int8_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsSgl': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'float *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsU16': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint16_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsU32': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint32_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsU64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint64_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteElementsU8': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'uint8_t *'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'AcquireFifoWriteRegion': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'region',
                'type': 'void *'
            },
            {
                'direction': 'out',
                'name': 'elements',
                'type': 'void *'
            },
            {
                'direction': 'in',
                'name': 'isSigned',
                'type': 'NiFpga_Bool'
            },
            {
                'direction': 'in',
                'name': 'elementSizeBytes',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'elementsRequested',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsAcquired',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'CalculateFxpDeltaDouble': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            }
        ],
        'returns': 'static'
    },
    'CalculateFxpDeltaFloat': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            }
        ],
        'returns': 'static'
    },
    'Close': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'enum': 'CloseAttribute',
                'name': 'attribute',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'CloseHostMemoryBuffer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'memoryName',
                'type': 'char[]'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'CloseLowLatencyBuffer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'memoryName',
                'type': 'char[]'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'CommitFifoConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ConfigureFifo': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'depth',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ConfigureFifo2': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'requestedDepth',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'actualDepth',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ConvertFromDoubleToFxp': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'double'
            }
        ],
        'returns': 'static'
    },
    'ConvertFromFloatToFxp': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'float'
            }
        ],
        'returns': 'static'
    },
    'ConvertFromFxpToDouble': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'uint64_t'
            }
        ],
        'returns': 'static'
    },
    'ConvertFromFxpToFloat': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'uint64_t'
            }
        ],
        'returns': 'static'
    },
    'Download': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'Finalize': {
        'codegen_method': 'no',
        'parameters': [
        ],
        'returns': 'NiFpga_Status'
    },
    'FindFifo': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifoName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'fifoNumber',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'FindRegister': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'registerName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'registerOffset',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetBitfileSignature': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'out',
                'name': 'signature',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'signatureSize',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetFifoPropertyI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetFifoPropertyI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'int64_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetFifoPropertyPtr': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'void *'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetFifoPropertyU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetFifoPropertyU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uint64_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetFpgaViState': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'out',
                'enum': 'FpgaViState',
                'name': 'state',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'GetPeerToPeerFifoEndpoint': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'endpoint',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'Initialize': {
        'codegen_method': 'no',
        'parameters': [
        ],
        'returns': 'NiFpga_Status'
    },
    'IsError': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'status',
                'type': 'NiFpga_Status'
            }
        ],
        'returns': 'static'
    },
    'IsNotError': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'status',
                'type': 'NiFpga_Status'
            }
        ],
        'returns': 'static'
    },
    'MapP2PSinkFifo': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'size',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'virtualAddress',
                'type': 'void *'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'MergeStatus': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'status',
                'type': 'NiFpga_Status * const'
            },
            {
                'direction': 'in',
                'name': 'newStatus',
                'type': 'NiFpga_Status'
            }
        ],
        'returns': 'static'
    },
    'Open': {
        'custom_close': 'Close(id, 0)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'bitfile',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'signature',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'OpenAttribute',
                'name': 'attribute',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'OpenHostMemoryBuffer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'memoryName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'memorySize',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'virtualAddress',
                'type': 'void *'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'OpenLowLatencyBuffer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'memoryName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'memorySizeToHost',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'virtualAddressToHost',
                'type': 'void *'
            },
            {
                'direction': 'out',
                'name': 'memorySizeToFpga',
                'type': 'size_t'
            },
            {
                'direction': 'out',
                'name': 'virtualAddressToFpga',
                'type': 'void *'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadArrayBool': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'NiFpga_Bool[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayDbl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'double[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'int16_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'int32_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'int64_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayI8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'int8_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArraySgl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'float[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayU16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'uint16_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'uint32_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'uint64_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadArrayU8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'size'
                },
                'type': 'uint8_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadBool': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'NiFpga_Bool'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadDbl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'double'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadFifoBool': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'NiFpga_Bool[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoComposite': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'void'
            },
            {
                'direction': 'in',
                'name': 'bytesPerElement',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoDbl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'double[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'int16_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'int32_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'int64_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoI8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'int8_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoSgl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'float[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoU16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'uint16_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'uint32_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'uint64_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFifoU8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'numberOfElements'
                },
                'type': 'uint8_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'elementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadFxp64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'uint64_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReadI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int16_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int32_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int64_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadI8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int8_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadSgl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'float'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadU16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint16_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint64_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReadU8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'indicator',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint8_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'ReleaseFifoElements': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'elements',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReleaseFifoRegion': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'region',
                'type': 'void'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'ReserveIrqContext': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'irqContext',
                'type': 'NiFpga_IrqContext'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'Reset': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'Run': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'enum': 'RunAttribute',
                'name': 'attribute',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'SetFifoPropertyI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'SetFifoPropertyI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'int64_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'SetFifoPropertyPtr': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'void'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'SetFifoPropertyU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'SetFifoPropertyU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'enum': 'FifoProperty',
                'name': 'property',
                'type': 'NiFpga_FifoProperty'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uint64_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'StartFifo': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'StopFifo': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'UnmapP2PSinkFifo': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'UnreserveFifo': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'UnreserveIrqContext': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'irqContext',
                'type': 'NiFpga_IrqContext'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WaitOnIrqs': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'out',
                'include_in_proto': False,
                'name': 'irqContext',
                'type': 'NiFpga_IrqContext'
            },
            {
                'direction': 'in',
                'name': 'irqs',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'irqsAsserted',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'timedOut',
                'type': 'NiFpga_Bool'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteArrayBool': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'NiFpga_Bool[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayDbl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'double[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'int16_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'int32_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'int64_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayI8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'int8_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArraySgl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'float[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayU16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'uint16_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'uint32_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'uint64_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteArrayU8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'array',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'uint8_t[]'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteBool': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'NiFpga_Bool'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteDbl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'double'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteFifoBool': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'NiFpga_Bool[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoComposite': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'type': 'void'
            },
            {
                'direction': 'in',
                'name': 'bytesPerElement',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoDbl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'double[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'int16_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'int32_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'int64_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoI8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'int8_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoSgl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'float[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoU16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'uint16_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'uint32_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'uint64_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFifoU8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'fifo',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfElements'
                },
                'type': 'uint8_t[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfElements',
                'type': 'size_t'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'name': 'emptyElementsRemaining',
                'type': 'size_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteFxp64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'name': 'typeInfo',
                'type': 'NiFpga_FxpTypeInfo'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'uint64_t'
            }
        ],
        'returns': 'NiFpga_Status'
    },
    'WriteI16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int16_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteI32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int32_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteI64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int64_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteI8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'int8_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteSgl': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'float'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteU16': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint16_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteU32': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint32_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteU64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint64_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    },
    'WriteU8': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'NiFpga_Session'
            },
            {
                'direction': 'in',
                'name': 'control',
                'type': 'uint32_t'
            },
            {
                'direction': 'in',
                'is_streaming_type': True,
                'name': 'value',
                'type': 'uint8_t'
            }
        ],
        'returns': 'NiFpga_Status',
        'supports_streaming': True
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nifpga/functions_addon.py sha256=72ad9906d470d1a254b3623957a6c84dc086f58c60383515e9ceed7c086d92e5 bytes=204 -->
## FILE: source/codegen/metadata/nifpga/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nifpga/functions_addon.py`
- sha256: `72ad9906d470d1a254b3623957a6c84dc086f58c60383515e9ceed7c086d92e5`
- bytes: 204

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/__init__.py`
- sha256: `b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41`
- bytes: 246

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/attributes.py sha256=b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4 bytes=19 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/attributes.py`
- sha256: `b140ace8cf4d1acb760f9841497697247ec57ec8df32230daa36040378f691b4`
- bytes: 19

````python
attributes = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/attributes_addon.py sha256=c0383d595caa7d3c2499e64d9382f66788dc9f088396d2ef40b404af5ada3845 bytes=39 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/attributes_addon.py`
- sha256: `c0383d595caa7d3c2499e64d9382f66788dc9f088396d2ef40b404af5ada3845`
- bytes: 39

````python
attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/config.py sha256=6c27050d0434bc59923bbed1b92d623fabaf022167d91c66b29a740279e5050e bytes=2339 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/config.py`
- sha256: `6c27050d0434bc59923bbed1b92d623fabaf022167d91c66b29a740279e5050e`
- bytes: 2339

````python
# -*- coding: utf-8 -*-
config = {
    "code_readiness": "Release",
    "is_restricted": True,
    'api_version': '21.0.0',
    'c_header': 'TerminalAdaptorTypes.h',
    'c_function_prefix': 'nimxlc_ta_nimxlc_',
    'service_class_prefix': 'NimxlcTerminalAdaptorRestricted',
    'java_package': 'com.ni.grpc.nimxlcterminaladaptorrestricted',
    'csharp_namespace': 'NationalInstruments.Grpc.NimxlcTerminalAdaptorRestricted',
    'namespace_component': 'nimxlcterminaladaptor_restricted',
    'close_function': 'destroySession',
    'additional_headers': { 
        "custom/nimxlcterminaladaptor_restricted_converters.h": ["service.cpp"],
    },
    'custom_types': [],
    "type_to_grpc_type": {
        'char[]': 'string',
        'float32': 'float',
        'float64': 'double',
        'int16': 'int32',
        'int32': 'int32',
        'int64': 'int64',
        'nimxlc_Session': 'nidevice_grpc.Session',
        'int8': 'int32',
        'uInt16': 'uint32',
        'uInt32': 'uint32',
        'uint32_t': 'uint32',
        'uInt64': 'uint64',
        'uInt8': 'uint32',
        'uInt8[]': 'bytes',
        'NIComplexSingle': 'nidevice_grpc.NIComplexNumberF32',
        'NIComplexDouble': 'nidevice_grpc.NIComplexNumber',
        'nierr_Status': 'NIErrStatus',
        'nimxlc_DeviceContainer': 'repeated NIMXLCDevice',
    },
    'driver_name': 'NI-MXLCTERMINALADAPTOR-RESTRICTED',
    "resource_handle_type": "nimxlc_Session",
    'status_ok': 'status >= 0',
    "windows_only": True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'libnimxlcTerminalAdaptor',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nimxlcTerminalAdaptor.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nimxlcTerminalAdaptor.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nimxlcterminaladaptor_restricted',
    'session_class_description': 'An handle to a Routing Adaptor session.',
    'session_handle_parameter_name': 'session',
    "duplicate_resource_handles_allowed": True,
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/custom_proto.mako sha256=3544e1cdd2447dbb63bc869a316d700414a6dcb3567397a0ab3ed0d0c2a31781 bytes=265 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/custom_proto.mako

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/custom_proto.mako`
- sha256: `3544e1cdd2447dbb63bc869a316d700414a6dcb3567397a0ab3ed0d0c2a31781`
- bytes: 265

````mako
message NIErrStatus {
  int32 code = 1;
  string json = 2;
}

message NIMXLCDevice {
  string name = 1;
  bool supportsOnboardClock = 2;
  repeated NIMXLCTerminal terminals = 3;
}

message NIMXLCTerminal {
  string name = 1;
  string visibility = 2;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/enums.py sha256=b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc bytes=14 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/enums.py`
- sha256: `b31b371d1c40b66f8d32c54c307920490097f6652fff5317cd0a30d4ac65b5cc`
- bytes: 14

````python
enums = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/enums_addon.py sha256=d6860cbdd07fa9f028dfe03e59952cc2da6f0b002389912f9d8492f9151cef2f bytes=32 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/enums_addon.py`
- sha256: `d6860cbdd07fa9f028dfe03e59952cc2da6f0b002389912f9d8492f9151cef2f`
- bytes: 32

````python
enums_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/functions.py sha256=83b5a022a45f4c7f25405e93af75d66f51df4b0e0d44e7273c535c6dbcf78743 bytes=14662 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/functions.py`
- sha256: `83b5a022a45f4c7f25405e93af75d66f51df4b0e0d44e7273c535c6dbcf78743`
- bytes: 14662

````python
functions = {
    'createSession': {
        'init_method': True,
        'status_expression': '(&c_status)->code',
        'parameters': [
            {
                'direction': 'in',
                'name': 'hostname',
                'type': 'const char[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'c_status',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'handle',
                'return_value': True,
                'type': 'nimxlc_Session'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'nimxlc_Session'
    },
    'destroySession': {
        'status_expression' : '0',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nimxlc_Session',
            },
        ],
        'returns': 'void',
    },
    'refreshTerminalCache': {
        'status_expression': '(&c_status)->code',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nimxlc_Session',
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'c_status',
                'type': 'nierr_Status',
            },
        ],
        'returns': 'void',
    },
    'hasTerminalInformationChanged': {
        'status_expression': '(&c_status)->code',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nimxlc_Session'
            },
            {
                'direction': 'in',
                'name': 'systemChangeNumber',
                'type': 'uint32_t'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'c_status',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'name': 'terminal_information_changed',
                'return_value': True,
                'type': 'bool'
            }
        ],
        'returns': 'bool'
    },
    'getSystemChangeNumber': {
        'status_expression': '(&c_status)->code',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nimxlc_Session'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'c_status',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'name': 'system_change_number',
                'return_value': True,
                'type': 'uint32_t'
            }
        ],
        'returns': 'uint32_t'
    },
    'getDeviceContainer': {
        'codegen_method': 'CustomCode',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'nimxlc_Session'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'c_status',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'pointer': True,
                'grpc_type': 'repeated NIMXLCDevice',
                'name': 'container_out',
                'return_value': True,
                'type': 'nimxlc_DeviceContainer'
            }
        ],
        'returns': 'nimxlc_DeviceContainer'
    },
    'DeviceContainer_begin': {
        'status_expression': '(&c_status)->code',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_DeviceContainer'
            },
            {
                'direction': 'out',
                'name': 'iterator_out',
                'return_value': True,
                'type': 'nimxlc_DeviceIterator'
            }
        ],
        'returns': 'nimxlc_DeviceIterator'
    },
    'DeviceIterator_next': {
        'status_expression': 'iterator ? 0 : 1',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'out',
                'name': 'iterator',
                'type': 'nimxlc_DeviceIterator'
            }
        ],
        'returns': 'void'
    },
    'DeviceIterator_getTerminalContainer': {
        'status_expression': '(&c_status)->code',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_DeviceContainer'
            },
            {
                'direction': 'in',
                'name': 'iterator',
                'type': 'nimxlc_DeviceIterator'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'cStatus',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'name': 'container_out',
                'return_value': True,
                'type': 'nimxlc_TerminalContainer'
            }
        ],
        'returns': 'nimxlc_TerminalContainer'
    },
    'DeviceIterator_getDeviceName': {
        'status_expression': '(&c_status)->code',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_DeviceContainer'
            },
            {
                'direction': 'in',
                'name': 'iterator',
                'type': 'nimxlc_DeviceIterator'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'cStatus',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'name': 'string_out',
                'return_value': True,
                'type': 'const char[]'
            }
        ],
        'returns': 'const char*'
    },
    'DeviceIterator_supportsOnBoardClock': {
        'status_expression': '(&c_status)->code',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_DeviceContainer'
            },
            {
                'direction': 'in',
                'name': 'iterator',
                'type': 'nimxlc_DeviceIterator'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'cStatus',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'name': 'bool_out',
                'return_value': True,
                'type': 'bool'
            }
        ],
        'returns': 'bool'
    },
    'DeviceIterator_isEnd': {
        'status_expression': '0',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_DeviceContainer'
            },
            {
                'direction': 'in',
                'name': 'iterator',
                'type': 'nimxlc_DeviceIterator'
            },
            {
                'direction': 'out',
                'name': 'bool_out',
                'return_value': True,
                'type': 'bool'
            }
        ],
        'returns': 'bool'
    },
    'DeviceContainer_destroy': {
        'status_expression': '0',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_DeviceContainer'
            }
        ],
        'returns': 'void'
    },
    'TerminalContainer_begin': {
        'status_expression': '0',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_TerminalContainer'
            },
            {
                'direction': 'out',
                'name': 'iterator_out',
                'return_value': True,
                'type': 'nimxlc_TerminalIterator'
            }
        ],
        'returns': 'nimxlc_TerminalIterator'
    },
    'TerminalIterator_next': {
        'status_expression': '0',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'out',
                'name': 'iterator',
                'type': 'nimxlc_TerminalIterator'
            }
        ],
        'returns': 'void'
    },
    'TerminalIterator_isEnd': {
        'status_expression': '0',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_TerminalContainer'
            },
            {
                'direction': 'in',
                'name': 'iterator',
                'type': 'nimxlc_TerminalIterator'
            },
            {
                'direction': 'out',
                'name': 'bool_out',
                'return_value': True,
                'type': 'bool'
            }
        ],
        'returns': 'bool'
    },
    'TerminalContainer_destroy': {
        'status_expression': '0',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_TerminalContainer'
            }
        ],
        'returns': 'void'
    },
    'TerminalIterator_getTerminalName': {
        'status_expression': '(&c_status)->code',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_TerminalContainer'
            },
            {
                'direction': 'in',
                'name': 'iterator',
                'type': 'nimxlc_TerminalIterator'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'cStatus',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'name': 'string_out',
                'return_value': True,
                'type': 'const char[]'
            }
        ],
        'returns': 'const char*'
    },
    'TerminalIterator_getVisibility': {
        'status_expression': '(&c_status)->code',
        'codegen_method': 'private',
        'parameters': [
            {
                'direction': 'in',
                'name': 'container',
                'type': 'nimxlc_TerminalContainer'
            },
            {
                'direction': 'in',
                'name': 'iterator',
                'type': 'nimxlc_TerminalIterator'
            },
            {
                'direction': 'out',
                'grpc_type': 'NIErrStatus',
                'supports_standard_output_allocation': True,
                'supports_standard_copy_convert': True,
                'additional_arguments_to_output_allocation': ['context'],
                'name': 'cStatus',
                'type': 'nierr_Status'
            },
            {
                'direction': 'out',
                'name': 'string_out',
                'return_value': True,
                'type': 'const char[]'
            }
        ],
        'returns': 'const char*'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nimxlcterminaladaptor_restricted/functions_addon.py sha256=65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45 bytes=36 -->
## FILE: source/codegen/metadata/nimxlcterminaladaptor_restricted/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nimxlcterminaladaptor_restricted/functions_addon.py`
- sha256: `65ef19d24dc5cc4d8e9d9e522a7690156666019979d2fee753b76dca82352d45`
- bytes: 36

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/__init__.py sha256=7b0ae43d6eb981467469b65bbabafc850e880c9460094ccb87885db68b3cbf7c bytes=371 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/__init__.py`
- sha256: `7b0ae43d6eb981467469b65bbabafc850e880c9460094ccb87885db68b3cbf7c`
- bytes: 371

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .enums_addon import enums_validation_suppressions
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/attributes.py sha256=0d2be5213182b35efe33778223bc4ec2e0cae1fa361c26ac2a348b4e558892a7 bytes=25865 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/attributes.py`
- sha256: `0d2be5213182b35efe33778223bc4ec2e0cae1fa361c26ac2a348b4e558892a7`
- bytes: 25865

````python
attributes = {
    11534337: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    11534338: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    11534339: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    11534340: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    11534341: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    11534342: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    11534343: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    11534344: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    11534345: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    11534346: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    11534347: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    11534348: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    11534349: {
        'access': 'read-write',
        'enum': 'PacketType',
        'name': 'PACKET_TYPE',
        'type': 'int32'
    },
    11534350: {
        'access': 'read-write',
        'name': 'DATA_RATE',
        'type': 'int32'
    },
    11534351: {
        'access': 'read-write',
        'name': 'BD_ADDRESS_LAP',
        'type': 'int32'
    },
    11534353: {
        'access': 'read-write',
        'name': 'ACCESS_ADDRESS',
        'type': 'int32'
    },
    11534354: {
        'access': 'read-write',
        'enum': 'PayloadBitPattern',
        'name': 'PAYLOAD_BIT_PATTERN',
        'type': 'int32'
    },
    11534355: {
        'access': 'read-write',
        'enum': 'PayloadLengthMode',
        'name': 'PAYLOAD_LENGTH_MODE',
        'type': 'int32'
    },
    11534356: {
        'access': 'read-write',
        'name': 'PAYLOAD_LENGTH',
        'type': 'int32'
    },
    11534359: {
        'access': 'read-write',
        'name': 'CHANNEL_NUMBER',
        'type': 'int32'
    },
    11534361: {
        'access': 'read-write',
        'name': 'DETECTED_PACKET_TYPE',
        'type': 'int32'
    },
    11534378: {
        'access': 'read-write',
        'name': 'DETECTED_DATA_RATE',
        'type': 'int32'
    },
    11534379: {
        'access': 'read-write',
        'name': 'DETECTED_PAYLOAD_LENGTH',
        'type': 'int32'
    },
    11534380: {
        'access': 'read-write',
        'enum': 'DirectionFindingMode',
        'name': 'DIRECTION_FINDING_MODE',
        'type': 'int32'
    },
    11534381: {
        'access': 'read-write',
        'name': 'CTE_LENGTH',
        'type': 'float64'
    },
    11534382: {
        'access': 'read-write',
        'name': 'CTE_SLOT_DURATION',
        'type': 'float64'
    },
    11534383: {
        'access': 'read-write',
        'name': 'CTE_NUMBER_OF_TRANSMIT_SLOTS',
        'type': 'int32'
    },
    11534384: {
        'access': 'read-write',
        'enum': 'ChannelSoundingPacketFormat',
        'name': 'CHANNEL_SOUNDING_PACKET_FORMAT',
        'type': 'int32'
    },
    11534385: {
        'access': 'read-write',
        'enum': 'ChannelSoundingSyncSequence',
        'name': 'CHANNEL_SOUNDING_SYNC_SEQUENCE',
        'type': 'int32'
    },
    11534386: {
        'access': 'read-write',
        'name': 'CHANNEL_SOUNDING_PHASE_MEASUREMENT_PERIOD',
        'type': 'float64'
    },
    11534387: {
        'access': 'read-write',
        'enum': 'ChannelSoundingToneExtensionSlot',
        'name': 'CHANNEL_SOUNDING_TONE_EXTENSION_SLOT',
        'type': 'int32'
    },
    11534388: {
        'access': 'read-write',
        'name': 'BANDWIDTH_BIT_PERIOD_PRODUCT',
        'type': 'float64'
    },
    11534389: {
        'access': 'read-write',
        'name': 'CHANNEL_SOUNDING_ANTENNA_SWITCH_TIME',
        'type': 'float64'
    },
    11534390: {
        'access': 'read-write',
        'name': 'CHANNEL_SOUNDING_NUMBER_OF_ANTENNA_PATH',
        'type': 'int32'
    },
    11534392: {
        'access': 'read-write',
        'enum': 'HighDataThroughputPacketFormat',
        'name': 'HIGH_DATA_THROUGHPUT_PACKET_FORMAT',
        'type': 'int32'
    },
    11534393: {
        'access': 'read-write',
        'name': 'ZADOFF_CHU_INDEX',
        'type': 'int32'
    },
    11534400: {
        'access': 'read-write',
        'enum': 'VhdtModeEnabled',
        'name': 'VHDT_MODE_ENABLED',
        'type': 'int32'
    },
    11534401: {
        'access': 'read-write',
        'name': 'NUMBER_OF_BLOCK_REPETITION_SEQUENCES',
        'type': 'int32'
    },
    11534402: {
        'access': 'read-write',
        'enum': 'AutoPreambleDetectionEnabled',
        'name': 'AUTO_PREAMBLE_DETECTION_ENABLED',
        'type': 'int32'
    },
    11534403: {
        'access': 'read-write',
        'name': 'DETECTED_PACKET_FORMAT',
        'type': 'int32'
    },
    11534404: {
        'access': 'read-write',
        'name': 'POWERRAMP_RESULTS_40DB_RISE_TIME_MEAN',
        'type': 'float64'
    },
    11534405: {
        'access': 'read-write',
        'enum': 'FrequencyBand',
        'name': 'FREQUENCY_BAND',
        'type': 'int32'
    },
    11538428: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    11538429: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    11538431: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    11538432: {
        'access': 'read-write',
        'name': 'TXP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    11538434: {
        'access': 'read-write',
        'enum': 'TxpAveragingEnabled',
        'name': 'TXP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    11538435: {
        'access': 'read-write',
        'name': 'TXP_AVERAGING_COUNT',
        'type': 'int32'
    },
    11538436: {
        'access': 'read-write',
        'name': 'TXP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    11538437: {
        'access': 'read-write',
        'name': 'TXP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    11538439: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    11538440: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MAXIMUM',
        'type': 'float64'
    },
    11538441: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_AVERAGE_POWER_MINIMUM',
        'type': 'float64'
    },
    11538442: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_POWER_MAXIMUM',
        'type': 'float64'
    },
    11538443: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_PEAK_TO_AVERAGE_POWER_RATIO_MAXIMUM',
        'type': 'float64'
    },
    11538444: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_EDR_GFSK_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    11538445: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_EDR_DPSK_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    11538448: {
        'access': 'read-write',
        'enum': 'TxpBurstSynchronizationType',
        'name': 'TXP_BURST_SYNCHRONIZATION_TYPE',
        'type': 'int32'
    },
    11538451: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_EDR_DPSK_GFSK_AVERAGE_POWER_RATIO_MEAN',
        'type': 'float64'
    },
    11538452: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_LE_CTE_REFERENCE_PERIOD_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    11538453: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_LE_CTE_REFERENCE_PERIOD_PEAK_ABSOLUTE_POWER_DEVIATION_MAXIMUM',
        'type': 'float64'
    },
    11538454: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_LE_CTE_TRANSMIT_SLOT_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    11538455: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_LE_CTE_TRANSMIT_SLOT_PEAK_ABSOLUTE_POWER_DEVIATION_MAXIMUM',
        'type': 'float64'
    },
    11538456: {
        'access': 'read-write',
        'name': 'TXP_RESULTS_LE_CS_PHASE_MEASUREMENT_PERIOD_AVERAGE_POWER_MEAN',
        'type': 'float64'
    },
    11542528: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    11542530: {
        'access': 'read-write',
        'enum': 'TwentydBBandwidthAveragingEnabled',
        'name': 'TWENTY_DB_BANDWIDTH_AVERAGING_ENABLED',
        'type': 'int32'
    },
    11542531: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_AVERAGING_COUNT',
        'type': 'int32'
    },
    11542532: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    11542533: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    11542535: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_RESULTS_PEAK_POWER',
        'type': 'float64'
    },
    11542536: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_RESULTS_BANDWIDTH',
        'type': 'float64'
    },
    11542537: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_RESULTS_HIGH_FREQUENCY',
        'type': 'float64'
    },
    11542538: {
        'access': 'read-write',
        'name': 'TWENTY_DB_BANDWIDTH_RESULTS_LOW_FREQUENCY',
        'type': 'float64'
    },
    11546624: {
        'access': 'read-write',
        'name': 'FREQUENCY_RANGE_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    11546626: {
        'access': 'read-write',
        'name': 'FREQUENCY_RANGE_SPAN',
        'type': 'float64'
    },
    11546627: {
        'access': 'read-write',
        'enum': 'FrequencyRangeAveragingEnabled',
        'name': 'FREQUENCY_RANGE_AVERAGING_ENABLED',
        'type': 'int32'
    },
    11546628: {
        'access': 'read-write',
        'name': 'FREQUENCY_RANGE_AVERAGING_COUNT',
        'type': 'int32'
    },
    11546629: {
        'access': 'read-write',
        'name': 'FREQUENCY_RANGE_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    11546630: {
        'access': 'read-write',
        'name': 'FREQUENCY_RANGE_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    11546632: {
        'access': 'read-write',
        'name': 'FREQUENCY_RANGE_RESULTS_HIGH_FREQUENCY',
        'type': 'float64'
    },
    11546633: {
        'access': 'read-write',
        'name': 'FREQUENCY_RANGE_RESULTS_LOW_FREQUENCY',
        'type': 'float64'
    },
    11550720: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    11550723: {
        'access': 'read-write',
        'enum': 'ModAccIQOriginOffsetCorrectionEnabled',
        'name': 'MODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED',
        'type': 'int32'
    },
    11550724: {
        'access': 'read-write',
        'enum': 'ModAccAveragingEnabled',
        'name': 'MODACC_AVERAGING_ENABLED',
        'type': 'int32'
    },
    11550725: {
        'access': 'read-write',
        'name': 'MODACC_AVERAGING_COUNT',
        'type': 'int32'
    },
    11550726: {
        'access': 'read-write',
        'name': 'MODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    11550727: {
        'access': 'read-write',
        'name': 'MODACC_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    11550729: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DF1AVG_MEAN',
        'type': 'float64'
    },
    11550730: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DF1AVG_MAXIMUM',
        'type': 'float64'
    },
    11550731: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DF1AVG_MINIMUM',
        'type': 'float64'
    },
    11550732: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DF1MAX_MAXIMUM',
        'type': 'float64'
    },
    11550733: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MINIMUM_DF1MAX_MINIMUM',
        'type': 'float64'
    },
    11550734: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DF2AVG_MEAN',
        'type': 'float64'
    },
    11550735: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DF2AVG_MAXIMUM',
        'type': 'float64'
    },
    11550736: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DF2AVG_MINIMUM',
        'type': 'float64'
    },
    11550737: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DF2MAX_MAXIMUM',
        'type': 'float64'
    },
    11550738: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_MINIMUM_DF2MAX_MINIMUM',
        'type': 'float64'
    },
    11550739: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_ABOVE_DF2MAX_THRESHOLD',
        'type': 'float64'
    },
    11550740: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_BR_INITIAL_FREQUENCY_ERROR_MAXIMUM',
        'type': 'float64'
    },
    11550741: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_BR_PEAK_FREQUENCY_DRIFT_MAXIMUM',
        'type': 'float64'
    },
    11550742: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_BR_PEAK_FREQUENCY_DRIFT_RATE_MAXIMUM',
        'type': 'float64'
    },
    11550743: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EDR_HEADER_FREQUENCY_ERROR_WI_MAXIMUM',
        'type': 'float64'
    },
    11550744: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EDR_PEAK_FREQUENCY_ERROR_WI_PLUS_W0_MAXIMUM',
        'type': 'float64'
    },
    11550745: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_EDR_PEAK_FREQUENCY_ERROR_W0_MAXIMUM',
        'type': 'float64'
    },
    11550746: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_LE_PEAK_FREQUENCY_ERROR_MAXIMUM',
        'type': 'float64'
    },
    11550747: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_LE_INITIAL_FREQUENCY_DRIFT_MAXIMUM',
        'type': 'float64'
    },
    11550748: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_LE_PEAK_FREQUENCY_DRIFT_MAXIMUM',
        'type': 'float64'
    },
    11550749: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_LE_PEAK_FREQUENCY_DRIFT_RATE_MAXIMUM',
        'type': 'float64'
    },
    11550750: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_RMS_DEVM_MAXIMUM',
        'type': 'float64'
    },
    11550751: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_DEVM_MEAN',
        'type': 'float64'
    },
    11550752: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_DEVM_MAXIMUM',
        'type': 'float64'
    },
    11550753: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_99_PERCENT_DEVM',
        'type': 'float64'
    },
    11550754: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_BELOW_99_PERCENT_DEVM_LIMIT',
        'type': 'float64'
    },
    11550755: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_ORIGIN_OFFSET_MEAN',
        'type': 'float64'
    },
    11550763: {
        'access': 'read-write',
        'enum': 'ModAccBurstSynchronizationType',
        'name': 'MODACC_BURST_SYNCHRONIZATION_TYPE',
        'type': 'int32'
    },
    11550764: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_ABOVE_DF1MAX_THRESHOLD',
        'type': 'float64'
    },
    11550765: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_AVERAGE_RMS_MAGNITUDE_ERROR_MEAN',
        'type': 'float64'
    },
    11550766: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_RMS_MAGNITUDE_ERROR_MAXIMUM',
        'type': 'float64'
    },
    11550767: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_AVERAGE_RMS_PHASE_ERROR_MEAN',
        'type': 'float64'
    },
    11550768: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_RMS_PHASE_ERROR_MAXIMUM',
        'type': 'float64'
    },
    11550769: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_LE_INITIAL_FREQUENCY_ERROR_MAXIMUM',
        'type': 'float64'
    },
    11550770: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_CLOCK_DRIFT_MEAN',
        'type': 'float64'
    },
    11550771: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PREAMBLE_START_TIME_MEAN',
        'type': 'float64'
    },
    11550772: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DF3AVG_MEAN',
        'type': 'float64'
    },
    11550773: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PERCENTAGE_OF_SYMBOLS_ABOVE_DF4AVG_THRESHOLD',
        'type': 'float64'
    },
    11550774: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PREAMBLE_RMS_EVM_MEAN',
        'type': 'float64'
    },
    11550775: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_CONTROL_HEADER_RMS_EVM_MEAN',
        'type': 'float64'
    },
    11550776: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PAYLOAD_RMS_EVM_MEAN',
        'type': 'float64'
    },
    11550777: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_FRACTIONAL_TIME_OFFSET_MEAN',
        'type': 'float64'
    },
    11550778: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PREAMBLE_FREQUENCY_ERROR_W0_MAXIMUM',
        'type': 'float64'
    },
    11550779: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PAYLOAD_FREQUENCY_ERROR_W1_MAXIMUM',
        'type': 'float64'
    },
    11550780: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_FREQUENCY_ERROR_W0_PLUS_W1_MAXIMUM',
        'type': 'float64'
    },
    11550781: {
        'access': 'read-write',
        'enum': 'ModAccIQMismatchCorrectionEnabled',
        'name': 'MODACC_IQ_MISMATCH_CORRECTION_ENABLED',
        'type': 'int32'
    },
    11550782: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_GAIN_IMBALANCE_MEAN',
        'type': 'float64'
    },
    11550783: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_QUADRATURE_ERROR_MEAN',
        'type': 'float64'
    },
    11550784: {
        'access': 'read-write',
        'enum': 'ModAccFrequencyTrackingEnabled',
        'name': 'MODACC_FREQUENCY_TRACKING_ENABLED',
        'type': 'int32'
    },
    11554816: {
        'access': 'read-write',
        'name': 'ACP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    11554818: {
        'access': 'read-write',
        'enum': 'AcpOffsetChannelMode',
        'name': 'ACP_OFFSET_CHANNEL_MODE',
        'type': 'int32'
    },
    11554819: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    11554820: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    11554821: {
        'access': 'read-write',
        'enum': 'AcpAveragingEnabled',
        'name': 'ACP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    11554822: {
        'access': 'read-write',
        'name': 'ACP_AVERAGING_COUNT',
        'type': 'int32'
    },
    11554823: {
        'access': 'read-write',
        'name': 'ACP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    11554824: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    11554826: {
        'access': 'read-write',
        'enum': 'AcpResultsMeasurementStatus',
        'name': 'ACP_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    11554827: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_REFERENCE_CHANNEL_POWER',
        'type': 'float64'
    },
    11554828: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    11554829: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    11554830: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    11554831: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    11554832: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    11554833: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    11554834: {
        'access': 'read-write',
        'enum': 'AcpBurstSynchronizationType',
        'name': 'ACP_BURST_SYNCHRONIZATION_TYPE',
        'type': 'int32'
    },
    11554837: {
        'access': 'read-write',
        'name': 'ACP_REFERENCE_CHANNEL_BANDWIDTH',
        'type': 'float64'
    },
    11554838: {
        'access': 'read-write',
        'enum': 'AcpReferenceChannelBandwidthMode',
        'name': 'ACP_REFERENCE_CHANNEL_BANDWIDTH_MODE',
        'type': 'int32'
    },
    11583488: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    11587584: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    11587585: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    11591680: {
        'access': 'read-write',
        'name': 'POWERRAMP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    11591682: {
        'access': 'read-write',
        'enum': 'PowerRampBurstSynchronizationType',
        'name': 'POWERRAMP_BURST_SYNCHRONIZATION_TYPE',
        'type': 'int32'
    },
    11591685: {
        'access': 'read-write',
        'enum': 'PowerRampAveragingEnabled',
        'name': 'POWERRAMP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    11591686: {
        'access': 'read-write',
        'name': 'POWERRAMP_AVERAGING_COUNT',
        'type': 'int32'
    },
    11591687: {
        'access': 'read-write',
        'name': 'POWERRAMP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    11591689: {
        'access': 'read-write',
        'name': 'POWERRAMP_RESULTS_RISE_TIME_MEAN',
        'type': 'float64'
    },
    11591690: {
        'access': 'read-write',
        'name': 'POWERRAMP_RESULTS_FALL_TIME_MEAN',
        'type': 'float64'
    },
    11591691: {
        'access': 'read-write',
        'name': 'POWERRAMP_RESULTS_40DB_FALL_TIME_MEAN',
        'type': 'float64'
    },
    11595776: {
        'access': 'read-write',
        'name': 'MODSPECTRUM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    11595778: {
        'access': 'read-write',
        'enum': 'ModSpectrumBurstSynchronizationType',
        'name': 'MODSPECTRUM_BURST_SYNCHRONIZATION_TYPE',
        'type': 'int32'
    },
    11595779: {
        'access': 'read-write',
        'enum': 'ModSpectrumAveragingEnabled',
        'name': 'MODSPECTRUM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    11595780: {
        'access': 'read-write',
        'name': 'MODSPECTRUM_AVERAGING_COUNT',
        'type': 'int32'
    },
    11595781: {
        'access': 'read-write',
        'name': 'MODSPECTRUM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    11595782: {
        'access': 'read-write',
        'name': 'MODSPECTRUM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    11595784: {
        'access': 'read-write',
        'name': 'MODSPECTRUM_RESULTS_BANDWIDTH',
        'type': 'float64'
    },
    11595785: {
        'access': 'read-write',
        'name': 'MODSPECTRUM_RESULTS_HIGH_FREQUENCY',
        'type': 'float64'
    },
    11595786: {
        'access': 'read-write',
        'name': 'MODSPECTRUM_RESULTS_LOW_FREQUENCY',
        'type': 'float64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/config.py sha256=e05ce7904293a7943866dba2723fa2d3715b0d76f19394934b69fb2a67703eaa bytes=2076 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/config.py`
- sha256: `e05ce7904293a7943866dba2723fa2d3715b0d76f19394934b69fb2a67703eaa`
- bytes: 2076

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niRFmxBT.h',
    'c_function_prefix': 'RFmxBT_',
    'service_class_prefix': 'NiRFmxBluetooth',
    'java_package': 'com.ni.grpc.nirfmxbluetooth',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxBluetooth',
    'namespace_component': 'nirfmxbluetooth',
    'close_function': 'Close',
    'custom_types': [],
    'additional_headers': { 'custom/nirfmx_errors.h': ['service.cpp'] },
    'type_to_grpc_type': {
        "char[]": "string",
        "float32": "float",
        "float64": "double",
        "int16": "int32",
        "int32": "int32",
        "int64": "int64",
        "niRFmxInstrHandle": "nidevice_grpc.Session",
        "int8": "int32",
        "uInt16": "uint32",
        "uInt32": "uint32",
        "uInt64": "uint64",
        "uInt8": "uint32",
        "uInt8[]": "bytes",
        "NIComplexSingle": "nidevice_grpc.NIComplexNumberF32",
        "NIComplexDouble": "nidevice_grpc.NIComplexNumber",
    },
    'code_readiness': 'Release',
    'feature_toggles': {},
    'driver_name': 'NI-RFMXBLUETOOTH',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxbt',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxBT.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxBT.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxbluetooth',
    'session_class_description': 'An NI-RFmxBluetooth instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'windows_only': True,
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/config_addon.py sha256=15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa bytes=224 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/config_addon.py`
- sha256: `15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa`
- bytes: 224

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/enums.py sha256=1b8f81f18eafee270d9994d76956105b694a202754e1fbb91910cc9eea57fb9c bytes=18343 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/enums.py`
- sha256: `1b8f81f18eafee270d9994d76956105b694a202754e1fbb91910cc9eea57fb9c`
- bytes: 18343

````python
enums = {
    'AcpAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AcpBurstSynchronizationType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'PREAMBLE',
                'value': 1
            },
            {
                'name': 'SYNC_WORD',
                'value': 2
            }
        ]
    },
    'AcpOffsetChannelMode': {
        'values': [
            {
                'name': 'SYMMETRIC',
                'value': 0
            },
            {
                'name': 'INBAND',
                'value': 1
            }
        ]
    },
    'AcpReferenceChannelBandwidthMode': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'MANUAL',
                'value': 1
            }
        ]
    },
    'AcpResultsMeasurementStatus': {
        'values': [
            {
                'name': 'NOT_APPLICABLE',
                'value': -1
            },
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'AutoPreambleDetectionEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ChannelSoundingPacketFormat': {
        'values': [
            {
                'name': 'SYNC',
                'value': 0
            },
            {
                'name': 'CS_TONE',
                'value': 1
            },
            {
                'name': 'CS_TONE_AFTER_SYNC',
                'value': 2
            },
            {
                'name': 'CS_TONE_BEFORE_SYNC',
                'value': 3
            }
        ]
    },
    'ChannelSoundingSyncSequence': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'SOUNDING_SEQUENCE_32_BIT',
                'value': 1
            },
            {
                'name': 'SOUNDING_SEQUENCE_96_BIT',
                'value': 2
            },
            {
                'name': 'PAYLOAD_PATTERN',
                'value': 3
            }
        ]
    },
    'ChannelSoundingToneExtensionSlot': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'ENABLED',
                'value': 1
            }
        ]
    },
    'DigitalEdgeTriggerEdge': {
        'values': [
            {
                'name': 'RISING',
                'value': 0
            },
            {
                'name': 'FALLING',
                'value': 1
            }
        ]
    },
    'DigitalEdgeTriggerSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'name': 'PXIE_DSTARB',
                'value': 'PXIe_DStarB'
            },
            {
                'name': 'TIMER_EVENT',
                'value': 'TimerEvent'
            },
            {
                'name': 'PULSE_IN',
                'value': 'PulseIn'
            },
            {
                'name': 'DIO_PFI0',
                'value': 'DIO/PFI0'
            },
            {
                'name': 'DIO_PFI1',
                'value': 'DIO/PFI1'
            },
            {
                'name': 'DIO_PFI2',
                'value': 'DIO/PFI2'
            },
            {
                'name': 'DIO_PFI3',
                'value': 'DIO/PFI3'
            },
            {
                'name': 'DIO_PFI4',
                'value': 'DIO/PFI4'
            },
            {
                'name': 'DIO_PFI5',
                'value': 'DIO/PFI5'
            },
            {
                'name': 'DIO_PFI6',
                'value': 'DIO/PFI6'
            },
            {
                'name': 'DIO_PFI7',
                'value': 'DIO/PFI7'
            }
        ]
    },
    'DirectionFindingMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'ANGLE_OF_ARRIVAL',
                'value': 1
            },
            {
                'name': 'ANGLE_OF_DEPARTURE',
                'value': 2
            }
        ]
    },
    'FrequencyBand': {
        'values': [
            {
                'name': '2_4_GHZ',
                'value': 0
            },
            {
                'name': '5_GHZ_1',
                'value': 1
            },
            {
                'name': '5_GHZ_3',
                'value': 2
            },
            {
                'name': '5_GHZ_4',
                'value': 3
            },
            {
                'name': '5_GHZ_3_4',
                'value': 4
            }
        ]
    },
    'FrequencyRangeAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'FrequencyReferenceSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'name': 'REF_IN',
                'value': 'RefIn'
            },
            {
                'name': 'PXI_CLK',
                'value': 'PXI_Clk'
            },
            {
                'name': 'CLK_IN',
                'value': 'ClkIn'
            }
        ]
    },
    'HighDataThroughputPacketFormat': {
        'values': [
            {
                'name': 'SHORT_FORMAT',
                'value': 0
            },
            {
                'name': 'FORMAT0',
                'value': 1
            },
            {
                'name': 'FORMAT1',
                'value': 2
            }
        ]
    },
    'IQPowerEdgeTriggerLevelType': {
        'values': [
            {
                'name': 'RELATIVE',
                'value': 0
            },
            {
                'name': 'ABSOLUTE',
                'value': 1
            }
        ]
    },
    'IQPowerEdgeTriggerSlope': {
        'values': [
            {
                'name': 'RISING',
                'value': 0
            },
            {
                'name': 'FALLING',
                'value': 1
            }
        ]
    },
    'LimitedConfigurationChange': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'NO_CHANGE',
                'value': 1
            },
            {
                'name': 'FREQUENCY',
                'value': 2
            },
            {
                'name': 'REFERENCE_LEVEL',
                'value': 3
            },
            {
                'name': 'FREQUENCY_AND_REFERENCE_LEVEL',
                'value': 4
            },
            {
                'name': 'SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL',
                'value': 5
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'TXP',
                'value': 1
            },
            {
                'name': 'MODACC',
                'value': 2
            },
            {
                'name': 'TWENTY_DB_BANDWIDTH',
                'value': 4
            },
            {
                'name': 'FREQUENCY_RANGE',
                'value': 8
            },
            {
                'name': 'ACP',
                'value': 16
            },
            {
                'name': 'POWERRAMP',
                'value': 32
            },
            {
                'name': 'MODSPECTRUM',
                'value': 64
            }
        ]
    },
    'MechanicalAttenuationAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccAveragingEnabled': {
        'enum-value-prefix': 'MODACC_AVERAGING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccBurstSynchronizationType': {
        'enum-value-prefix': 'MODACC_BURST_SYNCHRONIZATION_TYPE',
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'PREAMBLE',
                'value': 1
            },
            {
                'name': 'SYNC_WORD',
                'value': 2
            }
        ]
    },
    'ModAccFrequencyTrackingEnabled': {
        'enum-value-prefix': 'MODACC_FREQUENCY_TRACKING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQMismatchCorrectionEnabled': {
        'enum-value-prefix': 'MODACC_IQ_MISMATCH_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQOriginOffsetCorrectionEnabled': {
        'enum-value-prefix': 'MODACC_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModSpectrumAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModSpectrumBurstSynchronizationType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'PREAMBLE',
                'value': 1
            },
            {
                'name': 'SYNC_WORD',
                'value': 2
            }
        ]
    },
    'PacketType': {
        'values': [
            {
                'name': 'UNKNOWN',
                'value': -1
            },
            {
                'name': 'DH1',
                'value': 0
            },
            {
                'name': 'DH3',
                'value': 1
            },
            {
                'name': 'DH5',
                'value': 2
            },
            {
                'name': 'DM1',
                'value': 3
            },
            {
                'name': 'DM3',
                'value': 4
            },
            {
                'name': 'DM5',
                'value': 5
            },
            {
                'name': '2_DH1',
                'value': 6
            },
            {
                'name': '2_DH3',
                'value': 7
            },
            {
                'name': '2_DH5',
                'value': 8
            },
            {
                'name': '3_DH1',
                'value': 9
            },
            {
                'name': '3_DH3',
                'value': 10
            },
            {
                'name': '3_DH5',
                'value': 11
            },
            {
                'name': '2_EV3',
                'value': 12
            },
            {
                'name': '2_EV5',
                'value': 13
            },
            {
                'name': '3_EV3',
                'value': 14
            },
            {
                'name': '3_EV5',
                'value': 15
            },
            {
                'name': 'LE',
                'value': 16
            },
            {
                'name': 'LE_CS',
                'value': 17
            },
            {
                'name': 'LE_HDT',
                'value': 18
            }
        ]
    },
    'PayloadBitPattern': {
        'values': [
            {
                'name': 'STANDARD_DEFINED',
                'value': 0
            },
            {
                'name': '11110000',
                'value': 1
            },
            {
                'name': '10101010',
                'value': 2
            }
        ]
    },
    'PayloadLengthMode': {
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'AUTO',
                'value': 1
            }
        ]
    },
    'PowerRampAveragingEnabled': {
        'enum-value-prefix': 'POWERRAMP_AVERAGING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PowerRampBurstSynchronizationType': {
        'enum-value-prefix': 'POWERRAMP_BURST_SYNCHRONIZATION_TYPE',
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'PREAMBLE',
                'value': 1
            },
            {
                'name': 'SYNC_WORD',
                'value': 2
            }
        ]
    },
    'RFAttenuationAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'Standard': {
        'values': [
            {
                'name': 'BR',
                'value': 0
            },
            {
                'name': 'EDR',
                'value': 0
            },
            {
                'name': 'LE',
                'value': 1
            },
            {
                'name': 'LE_CS',
                'value': 2
            }
        ]
    },
    'TriggerMinimumQuietTimeMode': {
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'AUTO',
                'value': 1
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'DIGITAL_EDGE',
                'value': 1
            },
            {
                'name': 'IQ_POWER_EDGE',
                'value': 2
            },
            {
                'name': 'SOFTWARE',
                'value': 3
            }
        ]
    },
    'TwentydBBandwidthAveragingEnabled': {
        'enum-value-prefix': 'TWENTY_DB_BANDWIDTH_AVERAGING_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'TxpAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'TxpBurstSynchronizationType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'PREAMBLE',
                'value': 1
            },
            {
                'name': 'SYNC_WORD',
                'value': 2
            }
        ]
    },
    'VhdtModeEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/enums_addon.py sha256=ecf620c4ed7abf45dc84e4e7d9b9bfaa94c69de8c3d76e57ebc9f4ba50706c57 bytes=290 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/enums_addon.py`
- sha256: `ecf620c4ed7abf45dc84e4e7d9b9bfaa94c69de8c3d76e57ebc9f4ba50706c57`
- bytes: 290

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "Standard": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/functions.py sha256=5fd96ef0c341e10ae40f4588759ae80554b1399f157bc33c34af944eb54e4736 bytes=144237 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/functions.py`
- sha256: `5fd96ef0c341e10ae40f4588759ae80554b1399f157bc33c34af944eb54e4736`
- bytes: 144237

````python
functions = {
    'ACPCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AcpAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgBurstSynchronizationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AcpBurstSynchronizationType',
                'name': 'burstSynchronizationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgNumberOfOffsets': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'numberOfOffsets',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPCfgOffsetChannelMode': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'AcpOffsetChannelMode',
                'name': 'offsetChannelMode',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchAbsolutePowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'absolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchMaskTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'limitWithExceptionMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'limitWithoutExceptionMask',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchMeasurementStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'enum': 'AcpResultsMeasurementStatus',
                'name': 'measurementStatus',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchOffsetMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowerAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperAbsolutePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowerRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperRelativePower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowerMargin',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'upperMargin',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchOffsetMeasurementArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowerAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'upperAbsolutePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'lowerRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'upperRelativePower',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'lowerMargin',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'upperMargin',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchReferenceChannelPower': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceChannelPower',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ACPFetchSpectrum': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectrum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'AbortMeasurements': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeIQ1Waveform': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeIQ1WaveformInterleavedIQ': {
        'cname': 'RFmxBT_AnalyzeIQ1Waveform',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iq',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(iq)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32',
                'value_converted_to_c_representation': 'arraySize/2'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'AnalyzeIQ1WaveformSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'iqi',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'iqq',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'hardcoded_value': '0',
                'include_in_proto': False,
                'name': 'reserved',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'AutoDetectSignal': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'AutoLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'measurementInterval',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referenceLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'BuildOffsetString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offsetNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildSignalString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'signalName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'selectorStringLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorString',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'BuildSlotString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'slotNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'selectorStringOutLength',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'selectorStringOut',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'selectorStringOutLength'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CfgChannelNumber': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgDataRate': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'dataRate',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgDigitalEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'digitalEdgeSource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DigitalEdgeTriggerEdge',
                'name': 'digitalEdge',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'enableTrigger',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgExternalAttenuation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'externalAttenuation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'centerFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgFrequencyChannelNumber': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'Standard',
                'name': 'standard',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgFrequencyReference': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'FrequencyReferenceSource',
                'name': 'frequencyReferenceSource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'frequencyReferenceFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgIQPowerEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'iqPowerEdgeSource',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'IQPowerEdgeTriggerSlope',
                'name': 'iqPowerEdgeSlope',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'iqPowerEdgeLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'TriggerMinimumQuietTimeMode',
                'name': 'triggerMinQuietTimeMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'triggerMinQuietTimeDuration',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'enum': 'IQPowerEdgeTriggerLevelType',
                'name': 'iqPowerEdgeLevelType',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'enableTrigger',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgLEDirectionFinding': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'DirectionFindingMode',
                'name': 'directionFindingMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'cteLength',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'cteSlotDuration',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgMechanicalAttenuation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MechanicalAttenuationAuto',
                'name': 'mechanicalAttenuationAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'mechanicalAttenuationValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgPacketType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PacketType',
                'name': 'packetType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPayloadBitPattern': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PayloadBitPattern',
                'name': 'payloadBitPattern',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgPayloadLength': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PayloadLengthMode',
                'name': 'payloadLengthMode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'payloadLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CfgRF': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'centerFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'referenceLevel',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'externalAttenuation',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgRFAttenuation': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'RFAttenuationAuto',
                'name': 'rfAttenuationAuto',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'rfAttenuationValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgReferenceLevel': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'referenceLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CfgSoftwareEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'enableTrigger',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CheckMeasurementStatus': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isDone',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ClearAllNamedResults': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'ClearNamedResult': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CloneSignalConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'oldSignalName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'newSignalName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'Close': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'forceDestroy',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'Commit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'CreateSignalConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'signalName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'DeleteSignalConfiguration': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'signalName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'DisableTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'FrequencyRangeCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'FrequencyRangeAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'FrequencyRangeCfgSpan': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'span',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'FrequencyRangeFetchMeasurement': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'highFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'FrequencyRangeFetchSpectrum': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectrum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAllNamedResultNames': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'resultNames',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'resultNamesBufferSize',
                    'value_twist': 'actualResultNamesSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultNamesBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualResultNamesSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'defaultResultExists',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'float32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeF64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int16'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'name': 'attrVal',
                'type': 'int8'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeI8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeNIComplexDoubleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexDouble[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeNIComplexSingleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'out',
                'name': 'attrVal',
                'type': 'uInt16'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'uInt64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'type': 'uInt8'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeU8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'GetErrorString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'errorDescriptionBufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'Initialize': {
        'custom_close': 'Close(id, RFMXBT_VAL_FALSE)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'grpc_name': 'instrument',
                'name': 'handleOut',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'name': 'isNewSession',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'get_last_error': 'deprecated',
                'name': 'errorMessage',
                'type': 'char[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'int32'
    },
    'InitializeFromNIRFSASession': {
        'custom_close': 'Close(id, RFMXBT_VAL_FALSE)',
        'init_method': True,
        'parameters': [
            {
                'cross_driver_session': 'ViSession',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.Session',
                'name': 'nirfsaSession',
                'type': 'uInt32'
            },
            {
                'direction': 'out',
                'grpc_name': 'instrument',
                'name': 'handleOut',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'out',
                'get_last_error': 'deprecated',
                'name': 'errorMessage',
                'type': 'char[]'
            },
            {
                'cppName': 'initializationBehavior',
                'direction': 'in',
                'grpc_type': 'nidevice_grpc.SessionInitializationBehavior',
                'name': 'initializationBehavior',
                'proto_only': True,
                'type': 'int32'
            },
            {
                'cppName': 'newSessionInitialized',
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'newSessionInitialized',
                'proto_only': True,
                'type': 'bool'
            }
        ],
        'returns': 'int32'
    },
    'Initiate': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'resultName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccCfgBurstSynchronizationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModAccBurstSynchronizationType',
                'name': 'burstSynchronizationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchCSDetrendedPhaseTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'csDetrendedPhase',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchCSToneTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'csToneAmplitude',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'csTonePhase',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchConstellationTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchConstellationTraceInterleavedIQ': {
        'cname': 'RFmxBT_ModAccFetchConstellationTrace',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellation',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexSingle*>(constellation)'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchConstellationTraceSplit': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'constellationI',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'constellationQ',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDEVM': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'peak_rms_devm_maximum',
                'name': 'peakRMSDEVMMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakDEVMMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'ninetyninePercentDEVM',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDEVMMagnitudeError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageRMSMagnitudeErrorMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakRMSMagnitudeErrorMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDEVMPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'devmPerSymbol',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDEVMPhaseError': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averageRMSPhaseErrorMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakRMSPhaseErrorMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDemodulatedBitTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'coerced': True,
                'direction': 'out',
                'name': 'demodulatedBits',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'int8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDf1': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'df1avgMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'df1avgMinimum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDf1maxTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'time',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'df1max',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDf2': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'df2avgMinimum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'percentageOfSymbolsAboveDf2maxThreshold',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDf2maxTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'time',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'df2max',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchDf4avgTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'time',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'df4avg',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchEVMPerSymbolTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'evmPerSymbol',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyErrorBR': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'initialFrequencyErrorMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequencyDriftMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequencyDriftRateMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyErrorEDR': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'headerFrequencyErrorWiMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequencyErrorWiPlusW0Maximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequencyErrorW0Maximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyErrorLE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequencyErrorMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'initialFrequencyDriftMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequencyDriftMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakFrequencyDriftRateMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyErrorTraceBR': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'time',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'frequencyError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyErrorTraceLE': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'time',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'frequencyError',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyErrorWiPlusW0TraceEDR': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'time',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'out',
                'name': 'frequencyErrorWiPlusW0',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchFrequencyTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'frequency',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModAccFetchRMSDEVMTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'rms_devm',
                'name': 'rmsdevm',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModSpectrumCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModSpectrumAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModSpectrumCfgBurstSynchronizationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'ModSpectrumBurstSynchronizationType',
                'name': 'burstSynchronizationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ModSpectrumFetchSpectrum': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectrum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PowerRampCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PowerRampAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'PowerRampCfgBurstSynchronizationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'PowerRampBurstSynchronizationType',
                'name': 'burstSynchronizationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetToDefault': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SelectMeasurements': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'MeasurementTypes',
                'name': 'measurements',
                'type': 'uInt32'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'enableAllTraces',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SendSoftwareEdgeTrigger': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'float32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeF64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int16'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'in',
                'name': 'attrVal',
                'type': 'int8'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeI8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'int8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeNIComplexDoubleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexDouble[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeNIComplexSingleArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'NIComplexSingle[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU16': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'coerced': True,
                'direction': 'in',
                'name': 'attrVal',
                'type': 'uInt16'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'uInt32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU32Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'uInt32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU64Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'uInt64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU8': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'type': 'uInt8'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeU8Array': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attrVal',
                'size': {
                    'mechanism': 'len',
                    'value': 'arraySize'
                },
                'type': 'uInt8[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgAveraging': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'TxpAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPCfgBurstSynchronizationType': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'TxpBurstSynchronizationType',
                'name': 'burstSynchronizationType',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchEDRPowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'edr_gfsk_average_power_mean',
                'name': 'edrgfskAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'edr_dpsk_average_power_mean',
                'name': 'edrdpskAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_name': 'edr_dpsk_gfsk_average_power_ratio_mean',
                'name': 'edr_DPSK_GFSKAveragePowerRatioMean',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchLECTEReferencePeriodPowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referencePeriodAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'referencePeriodPeakAbsolutePowerDeviationMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchLECTETransmitSlotPowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'transmitSlotAveragePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'transmitSlotPeakAbsolutePowerDeviationMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchLECTETransmitSlotPowersArray': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'transmitSlotAveragePowerMean',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'out',
                'name': 'transmitSlotPeakAbsolutePowerDeviationMaximum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchPowerTrace': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'power',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TXPFetchPowers': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePowerMean',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePowerMaximum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'averagePowerMinimum',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakToAveragePowerRatioMaximum',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TwentydBBandwidthCfgAveraging': {
        'cname': 'RFmxBT_20dBBandwidthCfgAveraging',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'TwentydBBandwidthAveragingEnabled',
                'name': 'averagingEnabled',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'averagingCount',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'TwentydBBandwidthFetchMeasurement': {
        'cname': 'RFmxBT_20dBBandwidthFetchMeasurement',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'peakPower',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'bandwidth',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'highFrequency',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'lowFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'TwentydBBandwidthFetchSpectrum': {
        'cname': 'RFmxBT_20dBBandwidthFetchSpectrum',
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'x0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dx',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'spectrum',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'arraySize',
                    'value_twist': 'actualArraySize'
                },
                'type': 'float32[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'WaitForAcquisitionComplete': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'WaitForMeasurementComplete': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'instrument',
                'name': 'instrumentHandle',
                'type': 'niRFmxInstrHandle'
            },
            {
                'direction': 'in',
                'name': 'selectorString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetooth/functions_addon.py sha256=2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679 bytes=34 -->
## FILE: source/codegen/metadata/nirfmxbluetooth/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetooth/functions_addon.py`
- sha256: `2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679`
- bytes: 34

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/__init__.py sha256=7b0ae43d6eb981467469b65bbabafc850e880c9460094ccb87885db68b3cbf7c bytes=371 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/__init__.py`
- sha256: `7b0ae43d6eb981467469b65bbabafc850e880c9460094ccb87885db68b3cbf7c`
- bytes: 371

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .enums_addon import enums_validation_suppressions
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "enums_validation_suppressions": enums_validation_suppressions,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/attributes.py sha256=0bf3d4a82d966951372d750361485b0415a21ed360684c6a3f0f915e65f99756 bytes=14050 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/attributes.py`
- sha256: `0bf3d4a82d966951372d750361485b0415a21ed360684c6a3f0f915e65f99756`
- bytes: 14050

````python
attributes = {
    1: {
        'access': 'read-write',
        'enum': 'CarrierMode',
        'name': 'CARRIER_MODE',
        'type': 'int32'
    },
    3: {
        'access': 'read-write',
        'enum': 'AutoHeadroomEnabled',
        'name': 'AUTO_HEADROOM_ENABLED',
        'type': 'int32'
    },
    4: {
        'access': 'read-write',
        'name': 'HEADROOM',
        'type': 'float64'
    },
    5: {
        'access': 'read-write',
        'name': 'IQ_RATE',
        'type': 'float64'
    },
    6: {
        'access': 'read-write',
        'name': 'ACTUAL_HEADROOM',
        'type': 'float64'
    },
    7: {
        'access': 'read-write',
        'enum': 'PacketType',
        'name': 'PACKET_TYPE',
        'type': 'int32'
    },
    8: {
        'access': 'read-write',
        'name': 'BD_ADDRESS_LAP',
        'type': 'int32'
    },
    9: {
        'access': 'read-write',
        'name': 'BD_ADDRESS_UAP',
        'type': 'int32'
    },
    10: {
        'access': 'read-write',
        'name': 'BD_ADDRESS_NAP',
        'type': 'int32'
    },
    11: {
        'access': 'read-write',
        'name': 'PACKET_HEADER_LT_ADDRESS',
        'type': 'int32'
    },
    12: {
        'access': 'read-write',
        'name': 'PACKET_HEADER_FLOW',
        'type': 'int32'
    },
    13: {
        'access': 'read-write',
        'enum': 'PacketHeaderArqn',
        'name': 'PACKET_HEADER_ARQN',
        'type': 'int32'
    },
    14: {
        'access': 'read-write',
        'name': 'PACKET_HEADER_SEQN',
        'type': 'int32'
    },
    15: {
        'access': 'read-write',
        'name': 'PAYLOAD_HEADER_LLID',
        'type': 'int32'
    },
    16: {
        'access': 'read-write',
        'name': 'PAYLOAD_HEADER_FLOW',
        'type': 'int32'
    },
    17: {
        'access': 'read-write',
        'name': 'PAYLOAD_LENGTH',
        'type': 'int32'
    },
    18: {
        'access': 'read-write',
        'enum': 'PayloadDataType',
        'name': 'PAYLOAD_DATA_TYPE',
        'type': 'int32'
    },
    20: {
        'access': 'read-write',
        'name': 'PAYLOAD_USER_DEFINED_BITS',
        'type': 'int32[]'
    },
    21: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_LT_ADDRESS',
        'type': 'int32'
    },
    22: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_DEVICE_CLASS',
        'type': 'int32'
    },
    23: {
        'access': 'read-write',
        'enum': 'AllIQImpairmentsEnabled',
        'name': 'ALL_IQ_IMPAIRMENTS_ENABLED',
        'type': 'int32'
    },
    24: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_SCAN_REPETITION',
        'type': 'int32'
    },
    25: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_PAGE_SCAN_MODE',
        'type': 'int32'
    },
    26: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_DEVICE_CLOCK',
        'type': 'int32'
    },
    27: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_BD_ADDRESS_LAP',
        'type': 'int32'
    },
    28: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_BD_ADDRESS_UAP',
        'type': 'int32'
    },
    29: {
        'access': 'read-write',
        'name': 'FHS_PAYLOAD_BD_ADDRESS_NAP',
        'type': 'int32'
    },
    30: {
        'access': 'read-write',
        'enum': 'DirtyTxEnabled',
        'name': 'DIRTY_TX_ENABLED',
        'type': 'int32'
    },
    31: {
        'access': 'read-write',
        'enum': 'WhiteningEnabled',
        'name': 'WHITENING_ENABLED',
        'type': 'int32'
    },
    32: {
        'access': 'read-write',
        'name': 'WHITENING_CLOCK',
        'type': 'int32'
    },
    33: {
        'access': 'read-write',
        'name': 'IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    34: {
        'access': 'read-write',
        'name': 'QUADRATURE_SKEW',
        'type': 'float64'
    },
    35: {
        'access': 'read-write',
        'name': 'I_DC_OFFSET',
        'type': 'float64'
    },
    36: {
        'access': 'read-write',
        'name': 'Q_DC_OFFSET',
        'type': 'float64'
    },
    37: {
        'access': 'read-write',
        'name': 'CARRIER_FREQUENCY_OFFSET',
        'type': 'float64'
    },
    38: {
        'access': 'read-write',
        'enum': 'AwgnEnabled',
        'name': 'AWGN_ENABLED',
        'type': 'int32'
    },
    39: {
        'access': 'read-write',
        'name': 'CARRIER_TO_NOISE_RATIO',
        'type': 'float64'
    },
    40: {
        'access': 'read-write',
        'enum': 'CompatibilityVersion',
        'name': 'TOOLKIT_COMPATIBILITY_VERSION',
        'type': 'int32'
    },
    41: {
        'access': 'read-write',
        'name': 'PAYLOAD_PN_ORDER',
        'type': 'int32'
    },
    42: {
        'access': 'read-write',
        'name': 'PAYLOAD_PN_SEED',
        'type': 'int32'
    },
    43: {
        'access': 'read-write',
        'enum': 'PayloadLengthMode',
        'name': 'PAYLOAD_LENGTH_MODE',
        'type': 'int32'
    },
    44: {
        'access': 'read-write',
        'name': 'ACTUAL_PAYLOAD_LENGTH',
        'type': 'int32'
    },
    45: {
        'access': 'read-write',
        'name': 'IQ_WAVEFORM_SIZE',
        'type': 'int32'
    },
    46: {
        'access': 'read-write',
        'name': 'DV_VOICE_PAYLOAD_PN_ORDER',
        'type': 'int32'
    },
    47: {
        'access': 'read-write',
        'name': 'DV_VOICE_PAYLOAD_PN_SEED',
        'type': 'int32'
    },
    48: {
        'access': 'read-write',
        'name': 'DV_VOICE_PAYLOAD_USER_DEFINED_BITS',
        'type': 'int32[]'
    },
    49: {
        'access': 'read-write',
        'enum': 'DVVoicePayloadDataType',
        'name': 'DV_VOICE_PAYLOAD_DATA_TYPE',
        'type': 'int32'
    },
    50: {
        'access': 'read-write',
        'enum': 'LETPPayloadType',
        'name': 'LE_TP_PAYLOAD_TYPE',
        'type': 'int32'
    },
    51: {
        'access': 'read-write',
        'name': 'NUMBER_OF_UNIQUE_PACKETS',
        'type': 'int32'
    },
    52: {
        'access': 'read-write',
        'name': 'NUMBER_OF_IDLE_SLOTS',
        'type': 'int32'
    },
    54: {
        'access': 'read-write',
        'enum': 'LETPCorruptAlternateCrc',
        'name': 'LE_TP_CORRUPT_ALTERNATE_CRC',
        'type': 'int32'
    },
    55: {
        'access': 'read-write',
        'enum': 'DirtyTxMode',
        'name': 'DIRTY_TX_MODE',
        'type': 'int32'
    },
    56: {
        'access': 'read-write',
        'enum': 'DirtyTxParametersEnabledSet',
        'name': 'DIRTY_TX_PARAMETERS_ENABLED_SET',
        'type': 'int32[]'
    },
    57: {
        'access': 'read-write',
        'name': 'DIRTY_TX_CARRIER_FREQUENCY_OFFSET_SET',
        'type': 'int32[]'
    },
    58: {
        'access': 'read-write',
        'name': 'DIRTY_TX_MODULATION_INDEX_SET',
        'type': 'float64[]'
    },
    59: {
        'access': 'read-write',
        'name': 'DIRTY_TX_SYMBOL_TIMING_ERROR_SET',
        'type': 'int32[]'
    },
    61: {
        'access': 'read-write',
        'name': 'LE_ACCESS_ADDRESS',
        'type': 'int32'
    },
    62: {
        'access': 'read-write',
        'name': 'DIRTY_TX_RESIDUAL_FM_DEVIATION',
        'type': 'float64'
    },
    63: {
        'access': 'read-write',
        'name': 'DIRTY_TX_RESIDUAL_FM_FREQUENCY',
        'type': 'float64'
    },
    64: {
        'access': 'read-write',
        'name': 'CARRIER_FREQUENCY',
        'type': 'float64'
    },
    66: {
        'access': 'read-write',
        'enum': 'PayloadHeaderEnabled',
        'name': 'PAYLOAD_HEADER_ENABLED',
        'type': 'int32'
    },
    67: {
        'access': 'read-write',
        'enum': 'DirtyTxModulationIndexType',
        'name': 'DIRTY_TX_MODULATION_INDEX_TYPE',
        'type': 'int32'
    },
    68: {
        'access': 'read-write',
        'name': 'MODULATION_INDEX',
        'type': 'float64'
    },
    69: {
        'access': 'read-write',
        'name': 'MAXIMUM_HARDWARE_IQ_RATE',
        'type': 'float64'
    },
    70: {
        'access': 'read-write',
        'name': 'OVERSAMPLING_FACTOR',
        'type': 'int32'
    },
    71: {
        'access': 'read-write',
        'name': 'POWER_RAMP_SETTLING_TIME',
        'type': 'float64'
    },
    72: {
        'access': 'read-write',
        'name': 'POWER_RAMP_TIME',
        'type': 'float64'
    },
    73: {
        'access': 'read-write',
        'enum': 'PacketBitSequenceTraceEnabled',
        'name': 'PACKET_BIT_SEQUENCE_TRACE_ENABLED',
        'type': 'int32'
    },
    75: {
        'access': 'read-write',
        'enum': 'DirectionFindingMode',
        'name': 'DIRECTION_FINDING_MODE',
        'type': 'int32'
    },
    77: {
        'access': 'read-write',
        'name': 'DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_LENGTH',
        'type': 'float64'
    },
    78: {
        'access': 'read-write',
        'name': 'DIRECTION_FINDING_CONSTANT_TONE_EXTENSION_SLOT_DURATION',
        'type': 'float64'
    },
    79: {
        'access': 'read-write',
        'name': 'RUN_TIME_SCALING',
        'type': 'float64'
    },
    81: {
        'access': 'read-write',
        'enum': 'WaveformFileVersion',
        'name': 'WAVEFORM_FILE_VERSION',
        'type': 'int32'
    },
    82: {
        'access': 'read-write',
        'name': 'DIRECTION_FINDING_NUMBER_OF_ANTENNAS',
        'type': 'int32'
    },
    85: {
        'access': 'read-write',
        'name': 'DIRECTION_FINDING_ANTENNA_SWITCHING_PATTERN',
        'type': 'char[]'
    },
    86: {
        'access': 'read-write',
        'enum': 'AntennaSwitchingEnabled',
        'name': 'DIRECTION_FINDING_ANTENNA_SWITCHING_ENABLED',
        'type': 'int32'
    },
    87: {
        'access': 'read-write',
        'name': 'DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION',
        'type': 'float64'
    },
    88: {
        'access': 'read-write',
        'name': 'DIRECTION_FINDING_ANTENNA_SWITCHING_DURATION_USED',
        'type': 'float64'
    },
    90: {
        'access': 'read-write',
        'name': 'BURST_START_LOCATIONS',
        'type': 'int32[]'
    },
    91: {
        'access': 'read-write',
        'name': 'BURST_STOP_LOCATIONS',
        'type': 'int32[]'
    },
    92: {
        'access': 'read-write',
        'enum': 'CSPacketFormat',
        'name': 'CS_PACKET_FORMAT',
        'type': 'int32'
    },
    93: {
        'access': 'read-write',
        'enum': 'CSSyncSequence',
        'name': 'CS_SYNC_SEQUENCE',
        'type': 'int32'
    },
    94: {
        'access': 'read-write',
        'name': 'CS_PHASE_MEASUREMENT_PERIOD',
        'type': 'float64'
    },
    95: {
        'access': 'read-write',
        'name': 'SOUNDING_SEQUENCE_LENGTH',
        'type': 'int32'
    },
    96: {
        'access': 'read-write',
        'enum': 'SoundingSequenceMarkerSignals',
        'name': 'SOUNDING_SEQUENCE_MARKER_SIGNALS',
        'type': 'int32[]'
    },
    97: {
        'access': 'read-write',
        'name': 'SOUNDING_SEQUENCE_MARKER_POSITIONS',
        'type': 'int32[]'
    },
    98: {
        'access': 'read-write',
        'enum': 'CSToneExtensionSlotEnabled',
        'name': 'CS_TONE_EXTENSION_SLOT_ENABLED',
        'type': 'int32'
    },
    99: {
        'access': 'read-write',
        'name': 'SAMPLE_CLOCK_OFFSET',
        'type': 'float64'
    },
    100: {
        'access': 'read-write',
        'name': 'TIME_DELAY',
        'type': 'float64'
    },
    101: {
        'access': 'read-write',
        'name': 'BANDWIDTH_BIT_PERIOD_PRODUCT',
        'type': 'float64'
    },
    102: {
        'access': 'read-write',
        'enum': 'DataRate',
        'name': 'DATA_RATE',
        'type': 'int32'
    },
    103: {
        'access': 'read-write',
        'enum': 'HdtPacketFormat',
        'name': 'HDT_PACKET_FORMAT',
        'type': 'int32'
    },
    104: {
        'access': 'read-write',
        'name': 'HDT_PHY_INTERVAL',
        'type': 'float64'
    },
    105: {
        'access': 'read-write',
        'name': 'ZADOFF_CHU_INDEX',
        'type': 'int32'
    },
    106: {
        'access': 'read-write',
        'name': 'PHYSICAL_CHANNEL_ADDRESS',
        'type': 'int64'
    },
    107: {
        'access': 'read-write',
        'name': 'VHDT_MODE_ENABLED',
        'type': 'int32'
    },
    108: {
        'access': 'read-write',
        'name': 'NUMBER_OF_BLOCK_REPETITION_SEQUENCES',
        'type': 'int32'
    },
    109: {
        'access': 'read-write',
        'name': 'NUMBER_OF_PAYLOADS',
        'type': 'int32'
    },
    110: {
        'access': 'read-write',
        'enum': 'Format1PayloadZoneConfigurationMode',
        'name': 'FORMAT1_PAYLOAD_ZONE_CONFIGURATION_MODE',
        'type': 'int32'
    },
    111: {
        'access': 'read-write',
        'enum': 'TxlenSequenceNumber',
        'name': 'TXLEN_SEQUENCE_NUMBER',
        'type': 'int32'
    },
    112: {
        'access': 'read-write',
        'name': 'NUMBER_OF_BLOCKS',
        'type': 'int32'
    },
    113: {
        'access': 'read-write',
        'name': 'BLOCK_SIZE',
        'type': 'int32'
    },
    114: {
        'access': 'read-write',
        'name': 'LAST_BLOCK_SIZE',
        'type': 'int32'
    },
    115: {
        'access': 'read-write',
        'name': 'TXBLOCK_MAP',
        'type': 'int32'
    },
    117: {
        'access': 'read-write',
        'name': 'PAYLOAD_ZONE_LENGTH',
        'type': 'int32'
    },
    118: {
        'access': 'read-write',
        'name': 'PAYLOAD_CRC_SEED',
        'type': 'int64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/config.py sha256=b97c3b857b512ddf8d61ccb20af5233dcfcdf406c69f75f638eb3b8f1f0a9119 bytes=2345 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/config.py`
- sha256: `b97c3b857b512ddf8d61ccb20af5233dcfcdf406c69f75f638eb3b8f1f0a9119`
- bytes: 2345

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '26.5.0',
    'c_header': 'niBTGeneration.h',
    'c_function_prefix': 'niBTSG_',
    'service_class_prefix': 'NiRFmxBluetoothGen',
    'java_package': 'com.ni.grpc.nirfmxbluetoothgen',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxBluetoothGen',
    'namespace_component': 'nirfmxbluetoothgen',
    'close_function': 'CloseSession',
    'custom_types': [],
    'additional_headers': { 
        'custom/nirfmx_errors.h': ['service.cpp'], 
        'niBTGenerationRfsg.h': ['library.h', 'library.cpp', 'library_interface.h', 'compilation_test.cpp']
    },
    'type_to_grpc_type': {
        "char[]": "string",
        "float32": "float",
        "float64": "double",
        "int16": "int32",
        "int32": "int32",
        "int64": "int64",
        "int8": "int32",
        "uInt16": "uint32",
        "uInt32": "uint32",
        "uInt64": "uint64",
        "uInt8": "uint32",
        "uInt8[]": "bytes",
        "NIComplexSingle": "nidevice_grpc.NIComplexNumberF32",
        "NIComplexDouble": "nidevice_grpc.NIComplexNumber",
        "NIComplexNumber": "nidevice_grpc.NIComplexNumber", 
        "niBTSGSession": "nidevice_grpc.Session",
        "ViSession": "nidevice_grpc.Session"
    },
    'code_readiness': 'Release',
    'feature_toggles': {},
    'driver_name': 'NI-RFMXBLUETOOTHGEN',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': ['niBTSGSession', 'ViSession'],
    'status_ok': 'status >= 0',
    'library_info': { 
        'Linux': {
            '64bit': {
                'name': 'nirfmxbtgen',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxBTSG.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niBTSG_net.dll',
                'type': 'cdll'
            }
        }
    },
    'linux_rt_support': False,
    'metadata_version': '0.1',
    'module_name': 'nirfmxbluetoothgen',
    'session_class_description': 'An RFmx Bluetooth Generation handle',
    'session_handle_parameter_name': 'session',
    'windows_only': True,
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/config_addon.py sha256=15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa bytes=224 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/config_addon.py`
- sha256: `15c2d3b3a2eb111c2afae1c4b954020e66a6d86d8e707439a3f7295f04a738aa`
- bytes: 224

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/enums.py sha256=d676748af6725347e3b632b34c46d781b47f582baa20d7ec9f7a0f5dc0d7086d bytes=13258 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/enums.py`
- sha256: `d676748af6725347e3b632b34c46d781b47f582baa20d7ec9f7a0f5dc0d7086d`
- bytes: 13258

````python
enums = {
    'AllIQImpairmentsEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AntennaSwitchingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AutoHeadroomEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AwgnEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CSPacketFormat': {
        'values': [
            {
                'name': 'SYNC',
                'value': 0
            },
            {
                'name': 'CS_TONE',
                'value': 1
            },
            {
                'name': 'CS_TONE_AFTER_SYNC',
                'value': 2
            },
            {
                'name': 'CS_TONE_BEFORE_SYNC',
                'value': 3
            }
        ]
    },
    'CSSyncSequence': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'SOUNDING_SEQUENCE',
                'value': 1
            },
            {
                'name': 'PAYLOAD_PATTERN',
                'value': 2
            }
        ]
    },
    'CSToneExtensionSlotEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CarrierMode': {
        'values': [
            {
                'name': 'BURST',
                'value': 0
            },
            {
                'name': 'CONTINUOUS',
                'value': 1
            }
        ]
    },
    'CompatibilityVersion': {
        'values': [
            {
                'name': '010000',
                'value': 10000
            },
            {
                'name': '020000',
                'value': 20000
            }
        ]
    },
    'DVVoicePayloadDataType': {
        'values': [
            {
                'name': 'PN_SEQUENCE',
                'value': 0
            },
            {
                'name': 'USER_DEFINED_BITS',
                'value': 1
            }
        ]
    },
    'DataRate': {
        'values': [
            {
                'name': '2M',
                'value': 2000000
            },
            {
                'name': '3M',
                'value': 3000000
            },
            {
                'name': '4M',
                'value': 4000000
            },
            {
                'name': '6M',
                'value': 6000000
            },
            {
                'name': '7_5M',
                'value': 7500000
            }
        ]
    },
    'DirectionFindingMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'ANGLE_OF_ARRIVAL',
                'value': 1
            },
            {
                'name': 'ANGLE_OF_DEPARTURE',
                'value': 2
            }
        ]
    },
    'DirtyTxEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DirtyTxMode': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            },
            {
                'name': 'FREQUENCY_DRIFT',
                'value': 2
            }
        ]
    },
    'DirtyTxModulationIndexType': {
        'values': [
            {
                'name': 'STANDARD',
                'value': 0
            },
            {
                'name': 'STABLE',
                'value': 1
            }
        ]
    },
    'DirtyTxParametersEnabledSet': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'FileOperationMode': {
        'values': [
            {
                'name': 'OPEN',
                'value': 0
            },
            {
                'name': 'OPEN_OR_CREATE',
                'value': 1
            },
            {
                'name': 'CREATE_OR_REPLACE',
                'value': 2
            },
            {
                'name': 'CREATE',
                'value': 3
            }
        ]
    },
    'Format1PayloadZoneConfigurationMode': {
        'values': [
            {
                'name': 'AUTO',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'HdtPacketFormat': {
        'values': [
            {
                'name': 'SHORT_FORMAT',
                'value': 0
            },
            {
                'name': 'FORMAT0',
                'value': 1
            },
            {
                'name': 'FORMAT1',
                'value': 2
            }
        ]
    },
    'LETPCorruptAlternateCrc': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'LETPPayloadType': {
        'values': [
            {
                'name': 'PRBS9',
                'value': 0
            },
            {
                'name': '11110000',
                'value': 1
            },
            {
                'name': '10101010',
                'value': 2
            },
            {
                'name': 'PRBS15',
                'value': 3
            },
            {
                'name': '11111111',
                'value': 4
            },
            {
                'name': '00000000',
                'value': 5
            },
            {
                'name': '00001111',
                'value': 6
            },
            {
                'name': '01010101',
                'value': 7
            },
            {
                'name': 'USER_DEFINED_BITS',
                'value': 8
            }
        ]
    },
    'PacketBitSequenceTraceEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PacketHeaderArqn': {
        'values': [
            {
                'name': 'NAK',
                'value': 0
            },
            {
                'name': 'ACK',
                'value': 1
            }
        ]
    },
    'PacketType': {
        'values': [
            {
                'name': 'NULL',
                'value': 0
            },
            {
                'name': 'POLL',
                'value': 1
            },
            {
                'name': 'FHS',
                'value': 2
            },
            {
                'name': 'DM1',
                'value': 3
            },
            {
                'name': 'DH1',
                'value': 4
            },
            {
                'name': '2DH1',
                'value': 5
            },
            {
                'name': 'HV1',
                'value': 6
            },
            {
                'name': 'HV2',
                'value': 7
            },
            {
                'name': '2EV3',
                'value': 8
            },
            {
                'name': 'HV3',
                'value': 9
            },
            {
                'name': 'EV3',
                'value': 10
            },
            {
                'name': '3EV3',
                'value': 11
            },
            {
                'name': 'DV',
                'value': 12
            },
            {
                'name': '3DH1',
                'value': 13
            },
            {
                'name': 'AUX1',
                'value': 14
            },
            {
                'name': 'DM3',
                'value': 15
            },
            {
                'name': '2DH3',
                'value': 16
            },
            {
                'name': 'DH3',
                'value': 17
            },
            {
                'name': '3DH3',
                'value': 18
            },
            {
                'name': 'EV4',
                'value': 19
            },
            {
                'name': '2EV5',
                'value': 20
            },
            {
                'name': 'EV5',
                'value': 21
            },
            {
                'name': '3EV5',
                'value': 22
            },
            {
                'name': 'DM5',
                'value': 23
            },
            {
                'name': '2DH5',
                'value': 24
            },
            {
                'name': 'DH5',
                'value': 25
            },
            {
                'name': '3DH5',
                'value': 26
            },
            {
                'name': 'LE_TP',
                'value': 27
            },
            {
                'name': 'LE_TP_EXT',
                'value': 28
            },
            {
                'name': 'LE_ENHANCED',
                'value': 29
            },
            {
                'name': 'LE_LR_125K',
                'value': 30
            },
            {
                'name': 'LE_LR_500K',
                'value': 31
            },
            {
                'name': 'LE_CS_1M',
                'value': 32
            },
            {
                'name': 'LE_CS_2M',
                'value': 33
            },
            {
                'name': 'LE_HDT',
                'value': 34
            },
            {
                'name': 'ID',
                'value': 254
            },
            {
                'name': 'IDLE',
                'value': 255
            }
        ]
    },
    'PayloadDataType': {
        'values': [
            {
                'name': 'PN_SEQUENCE',
                'value': 0
            },
            {
                'name': 'USER_DEFINED_BITS',
                'value': 1
            }
        ]
    },
    'PayloadHeaderEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'PayloadLengthMode': {
        'values': [
            {
                'name': 'MAXIMUM_LENGTH',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'SoundingSequenceMarkerSignals': {
        'values': [
            {
                'name': '1100',
                'value': 0
            },
            {
                'name': '0011',
                'value': 1
            }
        ]
    },
    'TxlenSequenceNumber': {
        'values': [
            {
                'name': '00',
                'value': 0
            },
            {
                'name': '01',
                'value': 1
            },
            {
                'name': '10',
                'value': 2
            },
            {
                'name': '11',
                'value': 3
            }
        ]
    },
    'WaveformFileVersion': {
        'values': [
            {
                'name': '1_0',
                'value': 0
            },
            {
                'name': '2_0',
                'value': 1
            }
        ]
    },
    'WhiteningEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/enums_addon.py sha256=ecf620c4ed7abf45dc84e4e7d9b9bfaa94c69de8c3d76e57ebc9f4ba50706c57 bytes=290 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/enums_addon.py`
- sha256: `ecf620c4ed7abf45dc84e4e7d9b9bfaa94c69de8c3d76e57ebc9f4ba50706c57`
- bytes: 290

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}

enums_validation_suppressions = {
    "Standard": ["ENUMS_SHOULD_NOT_HAVE_DUPLICATE_VALUES"]
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/functions.py sha256=a5ce671121561d7ffa9f38b82d584f8500b6f0dfa3910174cacb7ae5d356d72e bytes=32312 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/functions.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/functions.py`
- sha256: `a5ce671121561d7ffa9f38b82d584f8500b6f0dfa3910174cacb7ae5d356d72e`
- bytes: 32312

````python
functions = {
    'CarrierFrequencyToChannelNumber': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'carrierFrequency',
                'type': 'float64'
            },
            {
                'direction': 'in',
                'name': 'standard',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'channelNumber',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ChannelNumberToCarrierFrequency': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'standard',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ChannelNumberToCarrierFrequencyV2': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'channelNumber',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'standard',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'frequencyBand',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'carrierFrequency',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'CloseSession': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            }
        ],
        'returns': 'int32'
    },
    'CreateAndWriteWaveformsToFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'FileOperationMode',
                'name': 'fileOperation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateWaveformComplexF64': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualWaveformSize'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualWaveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'generationDone',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'CreateWaveformComplexF64InterleavedIQ': {
        'cname': 'niBTSG_CreateWaveformComplexF64',
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualWaveformSize'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexNumber*>(waveform)'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualWaveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'generationDone',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetAttributeString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualStringSize'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualStringSize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetErrorString': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorMessageLength'
                },
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'errorMessageLength',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetScalarAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'GetScalarAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetScalarAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'attributeValue',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'GetVectorAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualNumDataArrayElements'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumDataArrayElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'GetVectorAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataArraySize',
                    'value_twist': 'actualNumDataArrayElements'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumDataArrayElements',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'LoadConfigurationFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'bool',
                'name': 'reset',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'OpenSession': {
        'custom_close': 'CloseSession(id)',
        'init_method': True,
        'parameters': [
            {
                'direction': 'in',
                'is_session_name': True,
                'name': 'sessionName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'enum': 'CompatibilityVersion',
                'name': 'toolkitCompatibilityVersion',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'isNewSession',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'RFSGClearDatabase': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'RFSGConfigureScript': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'powerLevel',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGCreateAndDownloadWaveform': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveHeadroom': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'headroom',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveIQRate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveIQRateAllWaveforms': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGRetrieveMinimumHeadroomAllWaveforms': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'script',
                'type': 'char[]'
            },
            {
                'direction': 'out',
                'name': 'headroom',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGStoreHeadroom': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'headroom',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'RFSGStoreIQRate': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'rfsgHandle',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'iqRate',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'ReadWaveformFromFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'int64'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'int64'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'repeated nidevice_grpc.NIComplexNumber',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualNumWaveformSamples'
                },
                'type': 'NIComplexNumber_struct[]'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumWaveformSamples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'headroom',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'eof',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ReadWaveformFromFileInterleavedIQ': {
        'cname': 'niBTSG_ReadWaveformFromFile',
        'parameters': [
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'int64'
            },
            {
                'direction': 'in',
                'name': 'count',
                'type': 'int64'
            },
            {
                'direction': 'out',
                'name': 't0',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'dt',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'waveform',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'waveformSize',
                    'value_twist': 'actualNumWaveformSamples'
                },
                'type': 'float64[]',
                'value_converted_to_c_representation': 'reinterpret_cast<NIComplexNumber*>(waveform)'
            },
            {
                'direction': 'in',
                'name': 'waveformSize',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'actualNumWaveformSamples',
                'type': 'int32'
            },
            {
                'direction': 'out',
                'name': 'iqRate',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'name': 'headroom',
                'type': 'float64'
            },
            {
                'direction': 'out',
                'grpc_type': 'bool',
                'name': 'eof',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetAttribute': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'ResetSession': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            }
        ],
        'returns': 'int32'
    },
    'SaveConfigurationToFile': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'operation',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAntennaRelativePhaseAndAmplitude': {
        'parameters': [
            {
                'direction': 'in',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'name': 'relativeAmplitudeDb',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'relativePhaseDeg',
                'size': {
                    'mechanism': 'len',
                    'tags': [
                        'optional'
                    ],
                    'value': 'arraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetAttributeString': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'char[]'
            }
        ],
        'returns': 'int32'
    },
    'SetScalarAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'float64'
            }
        ],
        'returns': 'int32'
    },
    'SetScalarAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetScalarAttributeI64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'attributeValue',
                'type': 'int64'
            }
        ],
        'returns': 'int32'
    },
    'SetVectorAttributeF64': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'float64[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    },
    'SetVectorAttributeI32': {
        'parameters': [
            {
                'direction': 'in',
                'grpc_name': 'session',
                'name': 'session',
                'type': 'niBTSGSession'
            },
            {
                'direction': 'in',
                'name': 'channelString',
                'type': 'char[]'
            },
            {
                'direction': 'in',
                'grpc_type': 'NiRFmxBluetoothGenAttribute',
                'name': 'attributeID',
                'type': 'int32'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'dataArraySize'
                },
                'type': 'int32[]'
            },
            {
                'direction': 'in',
                'name': 'dataArraySize',
                'type': 'int32'
            }
        ],
        'returns': 'int32'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxbluetoothgen/functions_addon.py sha256=2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679 bytes=34 -->
## FILE: source/codegen/metadata/nirfmxbluetoothgen/functions_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxbluetoothgen/functions_addon.py`
- sha256: `2cda4addcf571b52789d7b16d42a9e3a214a0589818dc2dcf97a25cb1150e679`
- bytes: 34

````python
functions_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/__init__.py sha256=b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41 bytes=246 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/__init__.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/__init__.py`
- sha256: `b0e667d43a382e67d757ae94299b01d8fd715dbebe22c7b4d9a61f1d7156df41`
- bytes: 246

````python
from .functions import functions
from .attributes import attributes
from .enums import enums
from .config import config

metadata = {
    "functions": functions,
    "attributes": attributes,
    "enums": enums,
    "config": config
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/attributes.py sha256=35c23b3b49150ed32ad58d8532a81f53fa9af330bf01ab9d8e21e2f859fcfeb5 bytes=34145 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/attributes.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/attributes.py`
- sha256: `35c23b3b49150ed32ad58d8532a81f53fa9af330bf01ab9d8e21e2f859fcfeb5`
- bytes: 34145

````python
attributes = {
    6291457: {
        'access': 'read-write',
        'name': 'CENTER_FREQUENCY',
        'type': 'float64'
    },
    6291458: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL',
        'type': 'float64'
    },
    6291459: {
        'access': 'read-write',
        'name': 'EXTERNAL_ATTENUATION',
        'type': 'float64'
    },
    6291460: {
        'access': 'read-write',
        'enum': 'TriggerType',
        'name': 'TRIGGER_TYPE',
        'type': 'int32'
    },
    6291461: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerSource',
        'name': 'DIGITAL_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    6291462: {
        'access': 'read-write',
        'enum': 'DigitalEdgeTriggerEdge',
        'name': 'DIGITAL_EDGE_TRIGGER_EDGE',
        'type': 'int32'
    },
    6291463: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_SOURCE',
        'type': 'char[]'
    },
    6291464: {
        'access': 'read-write',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL',
        'type': 'float64'
    },
    6291465: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerSlope',
        'name': 'IQ_POWER_EDGE_TRIGGER_SLOPE',
        'type': 'int32'
    },
    6291466: {
        'access': 'read-write',
        'name': 'TRIGGER_DELAY',
        'type': 'float64'
    },
    6291467: {
        'access': 'read-write',
        'enum': 'TriggerMinimumQuietTimeMode',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_MODE',
        'type': 'int32'
    },
    6291468: {
        'access': 'read-write',
        'name': 'TRIGGER_MINIMUM_QUIET_TIME_DURATION',
        'type': 'float64'
    },
    6291469: {
        'access': 'read-write',
        'enum': 'LinkDirection',
        'name': 'LINK_DIRECTION',
        'type': 'int32'
    },
    6291472: {
        'access': 'read-write',
        'name': 'BAND_CLASS',
        'type': 'int32'
    },
    6291473: {
        'access': 'read-write',
        'enum': 'RadioConfiguration',
        'name': 'RADIO_CONFIGURATION',
        'type': 'int32'
    },
    6291474: {
        'access': 'read-write',
        'enum': 'ChannelConfigurationMode',
        'name': 'CHANNEL_CONFIGURATION_MODE',
        'type': 'int32'
    },
    6291478: {
        'access': 'read-write',
        'name': 'NUMBER_OF_CHANNELS',
        'type': 'int32'
    },
    6291479: {
        'access': 'read-write',
        'name': 'WALSH_CODE_LENGTH',
        'type': 'int32'
    },
    6291480: {
        'access': 'read-write',
        'name': 'WALSH_CODE_NUMBER',
        'type': 'int32'
    },
    6291481: {
        'access': 'read-write',
        'enum': 'Branch',
        'name': 'BRANCH',
        'type': 'int32'
    },
    6291486: {
        'access': 'read-write',
        'name': 'UPLINK_SPREADING_LONG_CODE_MASK',
        'type': 'int64'
    },
    6291488: {
        'access': 'read-write',
        'name': 'DOWNLINK_SPREADING_PN_OFFSET',
        'type': 'int32'
    },
    6295548: {
        'access': 'read-write',
        'name': 'REFERENCE_LEVEL_HEADROOM',
        'type': 'float64'
    },
    6295549: {
        'access': 'read-write',
        'name': 'SELECTED_PORTS',
        'type': 'char[]'
    },
    6295551: {
        'access': 'read-write',
        'enum': 'IQPowerEdgeTriggerLevelType',
        'name': 'IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE',
        'type': 'int32'
    },
    6295552: {
        'access': 'read-write',
        'name': 'ACP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6295557: {
        'access': 'read-write',
        'name': 'ACP_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    6295560: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    6295562: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_FREQUENCY',
        'type': 'float64'
    },
    6295566: {
        'access': 'read-write',
        'name': 'ACP_OFFSET_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    6295570: {
        'access': 'read-write',
        'enum': 'AcpMeasurementMethod',
        'name': 'ACP_MEASUREMENT_METHOD',
        'type': 'int32'
    },
    6295572: {
        'access': 'read-write',
        'name': 'ACP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    6295573: {
        'access': 'read-write',
        'name': 'ACP_AVERAGING_COUNT',
        'type': 'int32'
    },
    6295574: {
        'access': 'read-write',
        'enum': 'AcpAveragingEnabled',
        'name': 'ACP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    6295576: {
        'access': 'read-write',
        'enum': 'AcpAveragingType',
        'name': 'ACP_AVERAGING_TYPE',
        'type': 'int32'
    },
    6295579: {
        'access': 'read-write',
        'enum': 'AcpRbwAutoBandwidth',
        'name': 'ACP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    6295580: {
        'access': 'read-write',
        'name': 'ACP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    6295581: {
        'access': 'read-write',
        'enum': 'AcpRbwFilterType',
        'name': 'ACP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    6295582: {
        'access': 'read-write',
        'enum': 'AcpSweepTimeAuto',
        'name': 'ACP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    6295583: {
        'access': 'read-write',
        'name': 'ACP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    6295584: {
        'access': 'read-write',
        'enum': 'AcpNoiseCompensationEnabled',
        'name': 'ACP_NOISE_COMPENSATION_ENABLED',
        'type': 'int32'
    },
    6295585: {
        'access': 'read-write',
        'name': 'ACP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6295590: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    6295596: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    6295597: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    6295602: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER',
        'type': 'float64'
    },
    6295603: {
        'access': 'read-write',
        'name': 'ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER',
        'type': 'float64'
    },
    6295604: {
        'access': 'read-write',
        'enum': 'AcpIFOutputPowerOffsetAuto',
        'name': 'ACP_IF_OUTPUT_POWER_OFFSET_AUTO',
        'type': 'int32'
    },
    6295605: {
        'access': 'read-write',
        'name': 'ACP_NEAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    6295606: {
        'access': 'read-write',
        'name': 'ACP_FAR_IF_OUTPUT_POWER_OFFSET',
        'type': 'float64'
    },
    6295608: {
        'access': 'read-write',
        'name': 'ACP_SEQUENTIAL_FFT_SIZE',
        'type': 'int32'
    },
    6295609: {
        'access': 'read-write',
        'enum': 'AcpFftOverlapMode',
        'name': 'ACP_FFT_OVERLAP_MODE',
        'type': 'int32'
    },
    6295610: {
        'access': 'read-write',
        'name': 'ACP_FFT_OVERLAP',
        'type': 'float64'
    },
    6303744: {
        'access': 'read-write',
        'name': 'CHP_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6303746: {
        'access': 'read-write',
        'name': 'CHP_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    6303747: {
        'access': 'read-write',
        'name': 'CHP_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    6303750: {
        'access': 'read-write',
        'name': 'CHP_AVERAGING_COUNT',
        'type': 'int32'
    },
    6303751: {
        'access': 'read-write',
        'enum': 'ChpAveragingEnabled',
        'name': 'CHP_AVERAGING_ENABLED',
        'type': 'int32'
    },
    6303753: {
        'access': 'read-write',
        'enum': 'ChpAveragingType',
        'name': 'CHP_AVERAGING_TYPE',
        'type': 'int32'
    },
    6303756: {
        'access': 'read-write',
        'enum': 'ChpRbwAutoBandwidth',
        'name': 'CHP_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    6303757: {
        'access': 'read-write',
        'name': 'CHP_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    6303758: {
        'access': 'read-write',
        'enum': 'ChpRbwFilterType',
        'name': 'CHP_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    6303761: {
        'access': 'read-write',
        'enum': 'ChpSweepTimeAuto',
        'name': 'CHP_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    6303762: {
        'access': 'read-write',
        'name': 'CHP_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    6303764: {
        'access': 'read-write',
        'name': 'CHP_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6303765: {
        'access': 'read-write',
        'name': 'CHP_RESULTS_CARRIER_ABSOLUTE_POWER',
        'type': 'float64'
    },
    6316032: {
        'access': 'read-write',
        'name': 'OBW_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6316035: {
        'access': 'read-write',
        'name': 'OBW_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    6316036: {
        'access': 'read-write',
        'name': 'OBW_SPAN',
        'type': 'float64'
    },
    6316038: {
        'access': 'read-write',
        'name': 'OBW_AVERAGING_COUNT',
        'type': 'int32'
    },
    6316039: {
        'access': 'read-write',
        'enum': 'ObwAveragingEnabled',
        'name': 'OBW_AVERAGING_ENABLED',
        'type': 'int32'
    },
    6316041: {
        'access': 'read-write',
        'enum': 'ObwAveragingType',
        'name': 'OBW_AVERAGING_TYPE',
        'type': 'int32'
    },
    6316044: {
        'access': 'read-write',
        'enum': 'ObwRbwAutoBandwidth',
        'name': 'OBW_RBW_FILTER_AUTO_BANDWIDTH',
        'type': 'int32'
    },
    6316045: {
        'access': 'read-write',
        'name': 'OBW_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    6316046: {
        'access': 'read-write',
        'enum': 'ObwRbwFilterType',
        'name': 'OBW_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    6316047: {
        'access': 'read-write',
        'enum': 'ObwSweepTimeAuto',
        'name': 'OBW_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    6316048: {
        'access': 'read-write',
        'name': 'OBW_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    6316050: {
        'access': 'read-write',
        'name': 'OBW_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6316051: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_OCCUPIED_BANDWIDTH',
        'type': 'float64'
    },
    6316052: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_ABSOLUTE_POWER',
        'type': 'float64'
    },
    6316053: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_START_FREQUENCY',
        'type': 'float64'
    },
    6316054: {
        'access': 'read-write',
        'name': 'OBW_RESULTS_STOP_FREQUENCY',
        'type': 'float64'
    },
    6324224: {
        'access': 'read-write',
        'name': 'SEM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6324229: {
        'access': 'read-write',
        'name': 'SEM_CARRIER_INTEGRATION_BANDWIDTH',
        'type': 'float64'
    },
    6324235: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_OFFSETS',
        'type': 'int32'
    },
    6324236: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_BANDWIDTH_INTEGRAL',
        'type': 'int32'
    },
    6324244: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_START_FREQUENCY',
        'type': 'float64'
    },
    6324245: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_STOP_FREQUENCY',
        'type': 'float64'
    },
    6324247: {
        'access': 'read-write',
        'name': 'SEM_OFFSET_RBW_FILTER_BANDWIDTH',
        'type': 'float64'
    },
    6324248: {
        'access': 'read-write',
        'enum': 'SemOffsetRbwFilterType',
        'name': 'SEM_OFFSET_RBW_FILTER_TYPE',
        'type': 'int32'
    },
    6324253: {
        'access': 'read-write',
        'name': 'SEM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    6324254: {
        'access': 'read-write',
        'name': 'SEM_AVERAGING_COUNT',
        'type': 'int32'
    },
    6324255: {
        'access': 'read-write',
        'enum': 'SemAveragingEnabled',
        'name': 'SEM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    6324257: {
        'access': 'read-write',
        'enum': 'SemAveragingType',
        'name': 'SEM_AVERAGING_TYPE',
        'type': 'int32'
    },
    6324261: {
        'access': 'read-write',
        'enum': 'SemSweepTimeAuto',
        'name': 'SEM_SWEEP_TIME_AUTO',
        'type': 'int32'
    },
    6324262: {
        'access': 'read-write',
        'name': 'SEM_SWEEP_TIME_INTERVAL',
        'type': 'float64'
    },
    6324263: {
        'access': 'read-write',
        'name': 'SEM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6324265: {
        'access': 'read-write',
        'enum': 'SemMeasurementStatus',
        'name': 'SEM_RESULTS_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    6324269: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    6324276: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    6324277: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    6324278: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    6324279: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    6324280: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    6324281: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN',
        'type': 'float64'
    },
    6324282: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    6324283: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    6324284: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    6324285: {
        'access': 'read-write',
        'enum': 'SemLowerOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    6324289: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER',
        'type': 'float64'
    },
    6324290: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER',
        'type': 'float64'
    },
    6324291: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER',
        'type': 'float64'
    },
    6324292: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER',
        'type': 'float64'
    },
    6324293: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY',
        'type': 'float64'
    },
    6324294: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN',
        'type': 'float64'
    },
    6324295: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER',
        'type': 'float64'
    },
    6324296: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER',
        'type': 'float64'
    },
    6324297: {
        'access': 'read-write',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY',
        'type': 'float64'
    },
    6324298: {
        'access': 'read-write',
        'enum': 'SemUpperOffsetMeasurementStatus',
        'name': 'SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS',
        'type': 'int32'
    },
    6340608: {
        'access': 'read-write',
        'name': 'RESULT_FETCH_TIMEOUT',
        'type': 'float64'
    },
    6344704: {
        'access': 'read-write',
        'name': 'AUTO_LEVEL_INITIAL_REFERENCE_LEVEL',
        'type': 'float64'
    },
    6344707: {
        'access': 'read-write',
        'enum': 'LimitedConfigurationChange',
        'name': 'LIMITED_CONFIGURATION_CHANGE',
        'type': 'int32'
    },
    6361088: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6361093: {
        'access': 'read-write',
        'enum': 'ModAccSynchronizationMode',
        'name': 'MODACC_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    6361094: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    6361095: {
        'access': 'read-write',
        'name': 'MODACC_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    6361096: {
        'access': 'read-write',
        'enum': 'ModAccIQOffsetRemovalEnabled',
        'name': 'MODACC_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6361097: {
        'access': 'read-write',
        'enum': 'ModAccSpectrumInverted',
        'name': 'MODACC_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    6361104: {
        'access': 'read-write',
        'enum': 'ModAccMultiCarrierFilterEnabled',
        'name': 'MODACC_MULTI_CARRIER_FILTER_ENABLED',
        'type': 'int32'
    },
    6361109: {
        'access': 'read-write',
        'name': 'MODACC_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6361120: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_EVM',
        'type': 'float64'
    },
    6361121: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_EVM',
        'type': 'float64'
    },
    6361122: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    6361123: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RMS_PHASE_ERROR',
        'type': 'float64'
    },
    6361124: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    6361125: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    6361126: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_IQ_QUADRATURE_ERROR',
        'type': 'float64'
    },
    6361127: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_FREQUENCY_ERROR',
        'type': 'float64'
    },
    6361128: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_RHO',
        'type': 'float64'
    },
    6361129: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_CDE',
        'type': 'float64'
    },
    6361131: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_CDE_WALSH_CODE_NUMBER',
        'type': 'int32'
    },
    6361132: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE',
        'type': 'float64'
    },
    6361133: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_LENGTH',
        'type': 'int32'
    },
    6361135: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER',
        'type': 'int32'
    },
    6361136: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_SLOT_TIMING_ERROR',
        'type': 'float64'
    },
    6361139: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    6361140: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS',
        'type': 'int32'
    },
    6361141: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTH',
        'type': 'int32'
    },
    6361142: {
        'access': 'read-write',
        'name': 'MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBER',
        'type': 'int32'
    },
    6361143: {
        'access': 'read-write',
        'enum': 'ModAccDetectedBranch',
        'name': 'MODACC_RESULTS_DETECTED_BRANCH',
        'type': 'int32'
    },
    6361144: {
        'access': 'read-write',
        'enum': 'ModAccPeakCdeBranch',
        'name': 'MODACC_RESULTS_PEAK_CDE_BRANCH',
        'type': 'int32'
    },
    6361145: {
        'access': 'read-write',
        'enum': 'ModAccPeakActiveCdeBranch',
        'name': 'MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH',
        'type': 'int32'
    },
    6361249: {
        'access': 'read-write',
        'enum': 'ModAccIQGainImbalanceRemovalEnabled',
        'name': 'MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6361250: {
        'access': 'read-write',
        'enum': 'ModAccIQQuadratureErrorRemovalEnabled',
        'name': 'MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6361251: {
        'access': 'read-write',
        'enum': 'ModAccReceiveFilterEnabled',
        'name': 'MODACC_RECEIVE_FILTER_ENABLED',
        'type': 'int32'
    },
    6365184: {
        'access': 'read-write',
        'name': 'QEVM_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6365186: {
        'access': 'read-write',
        'name': 'QEVM_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    6365187: {
        'access': 'read-write',
        'enum': 'QevmAveragingEnabled',
        'name': 'QEVM_AVERAGING_ENABLED',
        'type': 'int32'
    },
    6365188: {
        'access': 'read-write',
        'name': 'QEVM_AVERAGING_COUNT',
        'type': 'int32'
    },
    6365189: {
        'access': 'read-write',
        'enum': 'QevmSpectrumInverted',
        'name': 'QEVM_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    6365190: {
        'access': 'read-write',
        'enum': 'QevmIQOffsetRemovalEnabled',
        'name': 'QEVM_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6365191: {
        'access': 'read-write',
        'enum': 'QevmIQGainImbalanceRemovalEnabled',
        'name': 'QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6365192: {
        'access': 'read-write',
        'enum': 'QevmIQQuadratureErrorRemovalEnabled',
        'name': 'QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6365193: {
        'access': 'read-write',
        'enum': 'QevmReceiveFilterEnabled',
        'name': 'QEVM_RECEIVE_FILTER_ENABLED',
        'type': 'int32'
    },
    6365194: {
        'access': 'read-write',
        'name': 'QEVM_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6365195: {
        'access': 'read-write',
        'name': 'QEVM_NUMBER_OF_ANALYSIS_THREADS',
        'type': 'int32'
    },
    6365197: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_RMS_EVM',
        'type': 'float64'
    },
    6365198: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_RMS_EVM',
        'type': 'float64'
    },
    6365199: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_PEAK_EVM',
        'type': 'float64'
    },
    6365200: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_PEAK_EVM',
        'type': 'float64'
    },
    6365201: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    6365202: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    6365203: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_PHASE_ERROR',
        'type': 'float64'
    },
    6365204: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_PHASE_ERROR',
        'type': 'float64'
    },
    6365205: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_FREQUENCY_ERROR',
        'type': 'float64'
    },
    6365206: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR',
        'type': 'float64'
    },
    6365207: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    6365208: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    6365209: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    6365210: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    6365211: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR',
        'type': 'float64'
    },
    6365212: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR',
        'type': 'float64'
    },
    6365213: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MEAN_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    6365214: {
        'access': 'read-write',
        'name': 'QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    6369280: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6369282: {
        'access': 'read-write',
        'enum': 'CdaSynchronizationMode',
        'name': 'CDA_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    6369283: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    6369284: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    6369285: {
        'access': 'read-write',
        'name': 'CDA_BASE_SPREADING_FACTOR',
        'type': 'int32'
    },
    6369286: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_CHANNEL_WALSH_CODE_LENGTH',
        'type': 'int32'
    },
    6369287: {
        'access': 'read-write',
        'name': 'CDA_MEASUREMENT_CHANNEL_WALSH_CODE_NUMBER',
        'type': 'int32'
    },
    6369288: {
        'access': 'read-write',
        'enum': 'CdaMeasurementChannelBranch',
        'name': 'CDA_MEASUREMENT_CHANNEL_BRANCH',
        'type': 'int32'
    },
    6369289: {
        'access': 'read-write',
        'enum': 'CdaPowerUnit',
        'name': 'CDA_POWER_UNIT',
        'type': 'int32'
    },
    6369290: {
        'access': 'read-write',
        'enum': 'CdaSpectrumInverted',
        'name': 'CDA_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    6369291: {
        'access': 'read-write',
        'enum': 'CdaIQOffsetRemovalEnabled',
        'name': 'CDA_IQ_OFFSET_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6369292: {
        'access': 'read-write',
        'enum': 'CdaIQGainImbalanceRemovalEnabled',
        'name': 'CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6369293: {
        'access': 'read-write',
        'enum': 'CdaIQQuadratureErrorRemovalEnabled',
        'name': 'CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'type': 'int32'
    },
    6369294: {
        'access': 'read-write',
        'enum': 'CdaReceiveFilterEnabled',
        'name': 'CDA_RECEIVE_FILTER_ENABLED',
        'type': 'int32'
    },
    6369295: {
        'access': 'read-write',
        'name': 'CDA_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6369298: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_RMS_SYMBOL_EVM',
        'type': 'float64'
    },
    6369299: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_PEAK_SYMBOL_EVM',
        'type': 'float64'
    },
    6369300: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR',
        'type': 'float64'
    },
    6369301: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_RMS_SYMBOL_PHASE_ERROR',
        'type': 'float64'
    },
    6369302: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_SYMBOL_POWER',
        'type': 'float64'
    },
    6369303: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_TOTAL_POWER',
        'type': 'float64'
    },
    6369304: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_TOTAL_ACTIVE_POWER',
        'type': 'float64'
    },
    6369305: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_ACTIVE_POWER',
        'type': 'float64'
    },
    6369306: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_PEAK_ACTIVE_POWER',
        'type': 'float64'
    },
    6369307: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_INACTIVE_POWER',
        'type': 'float64'
    },
    6369308: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_PEAK_INACTIVE_POWER',
        'type': 'float64'
    },
    6369309: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_I_MEAN_ACTIVE_POWER',
        'type': 'float64'
    },
    6369310: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_I_PEAK_INACTIVE_POWER',
        'type': 'float64'
    },
    6369311: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_Q_MEAN_ACTIVE_POWER',
        'type': 'float64'
    },
    6369312: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_Q_PEAK_INACTIVE_POWER',
        'type': 'float64'
    },
    6369313: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_MEAN_PILOT_POWER',
        'type': 'float64'
    },
    6369314: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_IQ_ORIGIN_OFFSET',
        'type': 'float64'
    },
    6369315: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_IQ_GAIN_IMBALANCE',
        'type': 'float64'
    },
    6369316: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_IQ_QUADRATURE_ERROR',
        'type': 'float64'
    },
    6369317: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_FREQUENCY_ERROR',
        'type': 'float64'
    },
    6369318: {
        'access': 'read-write',
        'name': 'CDA_RESULTS_CHIP_RATE_ERROR',
        'type': 'float64'
    },
    6373376: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6373378: {
        'access': 'read-write',
        'enum': 'SlotPowerSynchronizationMode',
        'name': 'SLOTPOWER_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    6373379: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    6373380: {
        'access': 'read-write',
        'name': 'SLOTPOWER_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    6373381: {
        'access': 'read-write',
        'enum': 'SlotPowerSpectrumInverted',
        'name': 'SLOTPOWER_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    6373382: {
        'access': 'read-write',
        'enum': 'SlotPowerReceiveFilterEnabled',
        'name': 'SLOTPOWER_RECEIVE_FILTER_ENABLED',
        'type': 'int32'
    },
    6377472: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_ENABLED',
        'type': 'int32'
    },
    6377474: {
        'access': 'read-write',
        'enum': 'SlotPhaseSynchronizationMode',
        'name': 'SLOTPHASE_SYNCHRONIZATION_MODE',
        'type': 'int32'
    },
    6377475: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_OFFSET',
        'type': 'int32'
    },
    6377476: {
        'access': 'read-write',
        'name': 'SLOTPHASE_MEASUREMENT_LENGTH',
        'type': 'int32'
    },
    6377477: {
        'access': 'read-write',
        'enum': 'SlotPhaseSpectrumInverted',
        'name': 'SLOTPHASE_SPECTRUM_INVERTED',
        'type': 'int32'
    },
    6377478: {
        'access': 'read-write',
        'enum': 'SlotPhaseReceiveFilterEnabled',
        'name': 'SLOTPHASE_RECEIVE_FILTER_ENABLED',
        'type': 'int32'
    },
    6377479: {
        'access': 'read-write',
        'name': 'SLOTPHASE_TRANSIENT_DURATION',
        'type': 'float64'
    },
    6377480: {
        'access': 'read-write',
        'name': 'SLOTPHASE_ALL_TRACES_ENABLED',
        'type': 'int32'
    },
    6377483: {
        'access': 'read-write',
        'name': 'SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY',
        'type': 'float64'
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/attributes_addon.py sha256=8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7 bytes=205 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/attributes_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/attributes_addon.py`
- sha256: `8a2f9107808c1475e28dafa94a15f7b4116e0edc1faa34fa660f21904cba4ca7`
- bytes: 205

````python
# These dictionaries are applied to the generated attributes dictionary at build time
# Any changes to the API should be made here. attributes.py is code generated

attributes_override_metadata = {
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/CHANGES.md sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/CHANGES.md

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/CHANGES.md`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````markdown

````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/config.py sha256=c6a5e41f9e92943356217782d7de871c4decdedbb32f99a187eaa81ef872640c bytes=2000 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/config.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/config.py`
- sha256: `c6a5e41f9e92943356217782d7de871c4decdedbb32f99a187eaa81ef872640c`
- bytes: 2000

````python
# -*- coding: utf-8 -*-
config = {
    'api_version': '25.3.0',
    'c_header': 'niRFmxCDMA2k.h',
    'c_function_prefix': 'RFmxCDMA2k_',
    'service_class_prefix': 'NiRFmxCDMA2k',
    'java_package': 'com.ni.grpc.nirfmxcdma2k',
    'csharp_namespace': 'NationalInstruments.Grpc.NiRFmxCDMA2k',
    'namespace_component': 'nirfmxcdma2k',
    'close_function': 'Close',
    'custom_types': [],
    'additional_headers': {},
    'type_to_grpc_type': {
        "char[]": "string",
        "float32": "float",
        "float64": "double",
        "int16": "int32",
        "int32": "int32",
        "int64": "int64",
        "niRFmxInstrHandle": "nidevice_grpc.Session",
        "int8": "int32",
        "uInt16": "uint32",
        "uInt32": "uint32",
        "uInt64": "uint64",
        "uInt8": "uint32",
        "uInt8[]": "bytes",
        "NIComplexSingle": "nidevice_grpc.NIComplexNumberF32",
        "NIComplexDouble": "nidevice_grpc.NIComplexNumber",
    },
    'code_readiness': 'Release',
    'feature_toggles': {},
    'driver_name': 'NI-rfmxcdma2k',
    'extra_errors_used': [
    ],
    'init_function': 'Initialize',
    'resource_handle_type': 'niRFmxInstrHandle',
    'status_ok': 'status >= 0',
    'windows_only': True,
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nirfmxcdma2k',
                'type': 'cdll',
                'abi_version': '1'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'niRFmxCDMA2k.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'niRFmxCDMA2k.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '0.1',
    'module_name': 'nirfmxcdma2k',
    'session_class_description': 'An NI-RFmxCDMA2k instrument handle',
    'session_handle_parameter_name': 'instrumentHandle',
    'duplicate_resource_handles_allowed': True
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/config_addon.py sha256=57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb bytes=226 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/config_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/config_addon.py`
- sha256: `57b24306425b12029c7d7c2338937084edcd8de296db8ca03d5565ffcf9a88cb`
- bytes: 226

````python
# We need to maintain the version here since it needs to be updated by the build process on GitHub
config_additional_config = {
    'module_version': '1.3.3.dev0',
    'latest_runtime_version_tested_against': '21.3.0',
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/enums.py sha256=b774bd7b4c07a00994737da92f7c6611dc88f8b50e100957cacea715854d8828 bytes=25274 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/enums.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/enums.py`
- sha256: `b774bd7b4c07a00994737da92f7c6611dc88f8b50e100957cacea715854d8828`
- bytes: 25274

````python
enums = {
    'AcpAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AcpAveragingType': {
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'LOG',
                'value': 1
            },
            {
                'name': 'SCALAR',
                'value': 2
            },
            {
                'name': 'MAXIMUM',
                'value': 3
            },
            {
                'name': 'MINIMUM',
                'value': 4
            }
        ]
    },
    'AcpFftOverlapMode': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'AUTOMATIC',
                'value': 1
            }
        ]
    },
    'AcpIFOutputPowerOffsetAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AcpMeasurementMethod': {
        'values': [
            {
                'name': 'NORMAL',
                'value': 0
            },
            {
                'name': 'DYNAMIC_RANGE',
                'value': 1
            },
            {
                'name': 'SEQUENTIAL_FFT',
                'value': 2
            }
        ]
    },
    'AcpNoiseCompensationEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AcpRbwAutoBandwidth': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'AcpRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'AcpSweepTimeAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'Branch': {
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'CdaIQGainImbalanceRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaIQOffsetRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaIQQuadratureErrorRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaMeasurementChannelBranch': {
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            }
        ]
    },
    'CdaPowerUnit': {
        'values': [
            {
                'name': 'DB',
                'value': 0
            },
            {
                'name': 'DBM',
                'value': 1
            }
        ]
    },
    'CdaReceiveFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'CdaSynchronizationMode': {
        'values': [
            {
                'name': 'FRAME',
                'value': 0
            },
            {
                'name': 'SLOT',
                'value': 1
            },
            {
                'name': 'ARBITRARY',
                'value': 2
            }
        ]
    },
    'ChannelConfigurationMode': {
        'values': [
            {
                'name': 'AUTO_DETECT',
                'value': 0
            },
            {
                'name': 'USER_DEFINED',
                'value': 1
            }
        ]
    },
    'ChpAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ChpAveragingType': {
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'LOG',
                'value': 1
            },
            {
                'name': 'SCALAR',
                'value': 2
            },
            {
                'name': 'MAXIMUM',
                'value': 3
            },
            {
                'name': 'MINIMUM',
                'value': 4
            }
        ]
    },
    'ChpRbwAutoBandwidth': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ChpRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'ChpSweepTimeAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'DigitalEdgeTriggerEdge': {
        'values': [
            {
                'name': 'RISING',
                'value': 0
            },
            {
                'name': 'FALLING',
                'value': 1
            }
        ]
    },
    'DigitalEdgeTriggerSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'PFI0',
                'value': 'PFI0'
            },
            {
                'name': 'PFI1',
                'value': 'PFI1'
            },
            {
                'name': 'PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'name': 'PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'name': 'PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'name': 'PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'name': 'PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'name': 'PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'name': 'PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'name': 'PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'name': 'PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'name': 'PXIE_DSTARB',
                'value': 'PXIe_DStarB'
            },
            {
                'name': 'TIMER_EVENT',
                'value': 'TimerEvent'
            },
            {
                'name': 'PULSE_IN',
                'value': 'PulseIn'
            },
            {
                'name': 'DIO_PFI0',
                'value': 'DIO/PFI0'
            },
            {
                'name': 'DIO_PFI1',
                'value': 'DIO/PFI1'
            },
            {
                'name': 'DIO_PFI2',
                'value': 'DIO/PFI2'
            },
            {
                'name': 'DIO_PFI3',
                'value': 'DIO/PFI3'
            },
            {
                'name': 'DIO_PFI4',
                'value': 'DIO/PFI4'
            },
            {
                'name': 'DIO_PFI5',
                'value': 'DIO/PFI5'
            },
            {
                'name': 'DIO_PFI6',
                'value': 'DIO/PFI6'
            },
            {
                'name': 'DIO_PFI7',
                'value': 'DIO/PFI7'
            }
        ]
    },
    'FrequencyReferenceSource': {
        'generate-mappings': True,
        'values': [
            {
                'name': 'ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'name': 'REF_IN',
                'value': 'RefIn'
            },
            {
                'name': 'PXI_CLK',
                'value': 'PXI_Clk'
            },
            {
                'name': 'CLK_IN',
                'value': 'ClkIn'
            }
        ]
    },
    'IQPowerEdgeTriggerLevelType': {
        'values': [
            {
                'name': 'RELATIVE',
                'value': 0
            },
            {
                'name': 'ABSOLUTE',
                'value': 1
            }
        ]
    },
    'IQPowerEdgeTriggerSlope': {
        'values': [
            {
                'name': 'RISING',
                'value': 0
            },
            {
                'name': 'FALLING',
                'value': 1
            }
        ]
    },
    'LimitedConfigurationChange': {
        'values': [
            {
                'name': 'DISABLED',
                'value': 0
            },
            {
                'name': 'NO_CHANGE',
                'value': 1
            },
            {
                'name': 'FREQUENCY',
                'value': 2
            },
            {
                'name': 'REFERENCE_LEVEL',
                'value': 3
            },
            {
                'name': 'FREQUENCY_AND_REFERENCE_LEVEL',
                'value': 4
            },
            {
                'name': 'SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL',
                'value': 5
            }
        ]
    },
    'LinkDirection': {
        'values': [
            {
                'name': 'UPLINK',
                'value': 1
            }
        ]
    },
    'MeasurementTypes': {
        'values': [
            {
                'name': 'MODACC',
                'value': 1
            },
            {
                'name': 'ACP',
                'value': 2
            },
            {
                'name': 'CHP',
                'value': 4
            },
            {
                'name': 'OBW',
                'value': 8
            },
            {
                'name': 'SEM',
                'value': 16
            },
            {
                'name': 'QEVM',
                'value': 32
            },
            {
                'name': 'CDA',
                'value': 64
            },
            {
                'name': 'SLOTPHASE',
                'value': 128
            },
            {
                'name': 'SLOTPOWER',
                'value': 256
            }
        ]
    },
    'MechanicalAttenuationAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccDetectedBranch': {
        'enum-value-prefix': 'MODACC_DETECTED_BRANCH',
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'ModAccIQGainImbalanceRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQOffsetRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_OFFSET_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccIQQuadratureErrorRemovalEnabled': {
        'enum-value-prefix': 'MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccMultiCarrierFilterEnabled': {
        'enum-value-prefix': 'MODACC_MULTI_CARRIER_FILTER_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccPeakActiveCdeBranch': {
        'enum-value-prefix': 'MODACC_PEAK_ACTIVE_CDE_BRANCH',
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'ModAccPeakCdeBranch': {
        'enum-value-prefix': 'MODACC_PEAK_CDE_BRANCH',
        'values': [
            {
                'name': 'I',
                'value': 0
            },
            {
                'name': 'Q',
                'value': 1
            },
            {
                'name': 'I_AND_Q',
                'value': 2
            }
        ]
    },
    'ModAccReceiveFilterEnabled': {
        'enum-value-prefix': 'MODACC_RECEIVE_FILTER_ENABLED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccSpectrumInverted': {
        'enum-value-prefix': 'MODACC_SPECTRUM_INVERTED',
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ModAccSynchronizationMode': {
        'enum-value-prefix': 'MODACC_SYNCHRONIZATION_MODE',
        'values': [
            {
                'name': 'FRAME',
                'value': 0
            },
            {
                'name': 'SLOT',
                'value': 1
            },
            {
                'name': 'ARBITRARY',
                'value': 2
            }
        ]
    },
    'ObwAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ObwAveragingType': {
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'LOG',
                'value': 1
            },
            {
                'name': 'SCALAR',
                'value': 2
            },
            {
                'name': 'MAXIMUM',
                'value': 3
            },
            {
                'name': 'MINIMUM',
                'value': 4
            }
        ]
    },
    'ObwRbwAutoBandwidth': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'ObwRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            }
        ]
    },
    'ObwSweepTimeAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmIQGainImbalanceRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmIQOffsetRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmIQQuadratureErrorRemovalEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmReceiveFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'QevmSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'RFAttenuationAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'RadioConfiguration': {
        'values': [
            {
                'name': 'RC1',
                'value': 0
            },
            {
                'name': 'RC2',
                'value': 1
            },
            {
                'name': 'RC3',
                'value': 2
            },
            {
                'name': 'RC4',
                'value': 3
            },
            {
                'name': 'RC5',
                'value': 4
            }
        ]
    },
    'SemAveragingEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SemAveragingType': {
        'values': [
            {
                'name': 'RMS',
                'value': 0
            },
            {
                'name': 'LOG',
                'value': 1
            },
            {
                'name': 'SCALAR',
                'value': 2
            },
            {
                'name': 'MAXIMUM',
                'value': 3
            },
            {
                'name': 'MINIMUM',
                'value': 4
            }
        ]
    },
    'SemLowerOffsetMeasurementStatus': {
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'SemMeasurementStatus': {
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'SemOffsetRbwFilterType': {
        'values': [
            {
                'name': 'FFT_BASED',
                'value': 0
            },
            {
                'name': 'GAUSSIAN',
                'value': 1
            },
            {
                'name': 'FLAT',
                'value': 2
            },
            {
                'name': 'SYNCH_TUNED_4',
                'value': 3
            },
            {
                'name': 'SYNCH_TUNED_5',
                'value': 4
            }
        ]
    },
    'SemSweepTimeAuto': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SemUpperOffsetMeasurementStatus': {
        'values': [
            {
                'name': 'FAIL',
                'value': 0
            },
            {
                'name': 'PASS',
                'value': 1
            }
        ]
    },
    'SlotPhaseReceiveFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPhaseSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPhaseSynchronizationMode': {
        'values': [
            {
                'name': 'FRAME',
                'value': 0
            },
            {
                'name': 'SLOT',
                'value': 1
            }
        ]
    },
    'SlotPowerReceiveFilterEnabled': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPowerSpectrumInverted': {
        'values': [
            {
                'name': 'FALSE',
                'value': 0
            },
            {
                'name': 'TRUE',
                'value': 1
            }
        ]
    },
    'SlotPowerSynchronizationMode': {
        'values': [
            {
                'name': 'FRAME',
                'value': 0
            },
            {
                'name': 'SLOT',
                'value': 1
            }
        ]
    },
    'TriggerMinimumQuietTimeMode': {
        'values': [
            {
                'name': 'MANUAL',
                'value': 0
            },
            {
                'name': 'AUTO',
                'value': 1
            }
        ]
    },
    'TriggerType': {
        'values': [
            {
                'name': 'NONE',
                'value': 0
            },
            {
                'name': 'DIGITAL_EDGE',
                'value': 1
            },
            {
                'name': 'IQ_POWER_EDGE',
                'value': 2
            },
            {
                'name': 'SOFTWARE',
                'value': 3
            }
        ]
    }
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=source/codegen/metadata/nirfmxcdma2k/enums_addon.py sha256=ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e bytes=190 -->
## FILE: source/codegen/metadata/nirfmxcdma2k/enums_addon.py

- repository: `ni/grpc-device`
- source_path: `source/codegen/metadata/nirfmxcdma2k/enums_addon.py`
- sha256: `ac06c73354b9c04f0145a994373cc801d22779eab924afbba804b47e50fca14e`
- bytes: 190

````python
# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
}
````
