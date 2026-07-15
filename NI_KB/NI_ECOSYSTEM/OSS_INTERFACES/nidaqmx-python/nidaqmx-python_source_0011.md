# NI OSS SOURCE SNAPSHOT: nidaqmx-python

<!--NI_OSS_SNAPSHOT repo=ni/nidaqmx-python commit=03282e1b5c741b9f37e4a4e1b5de3a52ae72442e -->

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/metadata/functions_addon.py sha256=34c60161d14f328fd3d7742c590bec352e7c874c4340fb598b314992a3440919 bytes=3961 -->
## FILE: src/codegen/metadata/functions_addon.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/metadata/functions_addon.py`
- sha256: `34c60161d14f328fd3d7742c590bec352e7c874c4340fb598b314992a3440919`
- bytes: 3961

````python
functions_override_metadata = {
    'ReadAnalogF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadAnalogScalarF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryI16': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryI32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryU16': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadBinaryU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterF64Ex': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterScalarF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterScalarU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCounterU32Ex': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrFreq': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrFreqScalar': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTicks': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTicksScalar': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTime': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadCtrTimeScalar': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalLines': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalScalarU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalU16': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalU32': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadDigitalU8': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadPowerScalarF64': {
        'python_codegen_method': 'CustomCode_Read',
    },
    'WriteAnalogF64': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteAnalogScalarF64': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryI16': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryI32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryU16': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteBinaryU32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrFreq': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrFreqScalar': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTicks': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTicksScalar': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTime': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteCtrTimeScalar': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalLines': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalScalarU32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalU16': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalU32': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'WriteDigitalU8': {
        'python_codegen_method': 'CustomCode_Write',
    },
    'ReadPowerBinaryI16':{
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadPowerF64':{
        'python_codegen_method': 'CustomCode_Read',
    },
    'ReadRaw':{
        'python_codegen_method': 'CustomCode_Read',
    },
    'WriteRaw':{
        'python_codegen_method': 'CustomCode_Write',
    }
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/metadata/script_info.py sha256=a7b46e07ef049999e8458face0cd1ad17e3a00d18cf1d8c6c3611af952d1b1ef bytes=5177 -->
## FILE: src/codegen/metadata/script_info.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/metadata/script_info.py`
- sha256: `a7b46e07ef049999e8458face0cd1ad17e3a00d18cf1d8c6c3611af952d1b1ef`
- bytes: 5177

````python
script_info = {
    "modules": [
        {
            "relativeOutputPath": "_base_interpreter.py",
            "templateFile": "_base_interpreter.py.mako",
        },
        {
            "relativeOutputPath": "_library_interpreter.py",
            "templateFile": "_library_interpreter.py.mako",
        },
        {
            "relativeOutputPath": "_grpc_interpreter.py",
            "templateFile": "_grpc_interpreter.py.mako",
        },
        {
            "relativeOutputPath": "task\\channels\\_channel.py",
            "templateFile": "task\\channels\\_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\channels\\_ai_channel.py",
            "templateFile": "task\\channels\\_ai_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\_in_stream.py",
            "templateFile": "task\\_in_stream.py.mako",
        },
        {
            "relativeOutputPath": "task\\_out_stream.py",
            "templateFile": "task\\_out_stream.py.mako",
        },
        {
            "relativeOutputPath": "system\\_watchdog_modules\\expiration_state.py",
            "templateFile": "system\\_watchdog_modules\\expiration_state.py.mako",
        },
        {
            "relativeOutputPath": "system\\watchdog.py",
            "templateFile": "system\\watchdog.py.mako",
        },
        {
            "relativeOutputPath": "task\\channels\\_ao_channel.py",
            "templateFile": "task\\channels\\_ao_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\channels\\_ci_channel.py",
            "templateFile": "task\\channels\\_ci_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\channels\\_co_channel.py",
            "templateFile": "task\\channels\\_co_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\channels\\_di_channel.py",
            "templateFile": "task\\channels\\_di_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\channels\\_do_channel.py", 
            "templateFile": "task\\channels\\_do_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\collections\\_ai_channel_collection.py",
            "templateFile": "task\\collections\\_ai_channel_collection.py.mako",
        },
        {
            "relativeOutputPath": "task\\collections\\_ao_channel_collection.py",
            "templateFile": "task\\collections\\_ao_channel_collection.py.mako",
        },
        {
            "relativeOutputPath": "task\\collections\\_ci_channel_collection.py",
            "templateFile": "task\\collections\\_ci_channel_collection.py.mako",
        },
        {
            "relativeOutputPath": "task\\collections\\_co_channel_collection.py",
            "templateFile": "task\\collections\\_co_channel_collection.py.mako",
        },
        {
            "relativeOutputPath": "task\\collections\\_di_channel_collection.py",
            "templateFile": "task\\collections\\_di_channel_collection.py.mako",
        },
        {
            "relativeOutputPath": "task\\collections\\_do_channel_collection.py",
            "templateFile": "task\\collections\\_do_channel_collection.py.mako",
        },
        {
            "relativeOutputPath": "task\\_timing.py",
            "templateFile": "task\\_timing.py.mako",
        },  
        {
            "relativeOutputPath": "scale.py", 
            "templateFile": "scale.py.mako",
        },
        {
            "relativeOutputPath": "task\\_export_signals.py",
            "templateFile": "task\\_export_signals.py.mako",
        },
        {
            "relativeOutputPath": "task\\triggering\\_arm_start_trigger.py",
            "templateFile": "task\\triggering\\_arm_start_trigger.py.mako",
        },
        {
            "relativeOutputPath": "task\\triggering\\_handshake_trigger.py",
            "templateFile": "task\\triggering\\_handshake_trigger.py.mako",
        },
        {
            "relativeOutputPath": "task\\triggering\\_pause_trigger.py",
            "templateFile": "task\\triggering\\_pause_trigger.py.mako",
        },
        {
            "relativeOutputPath": "task\\triggering\\_reference_trigger.py",
            "templateFile": "task\\triggering\\_reference_trigger.py.mako",
        },
        {
            "relativeOutputPath": "task\\triggering\\_start_trigger.py",
            "templateFile": "task\\triggering\\_start_trigger.py.mako",
        },
        {
            "relativeOutputPath": "system\\system.py",
            "templateFile": "system\\system.py.mako",
        },
        {
            "relativeOutputPath": "system\\device.py",
            "templateFile": "system\\device.py.mako",
        },
        {
            "relativeOutputPath": "system\\physical_channel.py",
            "templateFile": "system\\physical_channel.py.mako",
        },
        {
            "relativeOutputPath": "task\\triggering\\_triggers.py",
            "templateFile": "task\\triggering\\_triggers.py.mako",
        },
    ]
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/properties/attribute.py sha256=fbc8c98403544454194476b9c22596882e3eb2e0f2a09eb1b801310a810e75ed bytes=12725 -->
## FILE: src/codegen/properties/attribute.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/properties/attribute.py`
- sha256: `fbc8c98403544454194476b9c22596882e3eb2e0f2a09eb1b801310a810e75ed`
- bytes: 12725

````python
"""Structure for storing attribute metadata from scrapigen."""

from codegen.properties.parameter import Parameter
from codegen.utilities.enum_helpers import merge_enums

ALTERNATE_CONSTRUCTOR_CLASSES = [
    "Task",
    "PhysicalChannel",
    "Device",
    "PersistedChannel",
    "PersistedTask",
    "PersistedScale",
    "Scale",
]


class Attribute:
    """Structure for storing attribute metadata from scrapigen."""

    def __init__(self, id, attribute_metadata):
        """Structure for storing attribute metadata from scrapigen."""
        self._id = id
        self._is_enum = False
        self._access = attribute_metadata["access"]
        self._name = (
            attribute_metadata["python_name"].lower()
            if "python_name" in attribute_metadata
            else attribute_metadata["name"].lower()
        )
        self._resettable = attribute_metadata["resettable"]
        self._type = attribute_metadata["type"]
        self._ctypes_data_type = attribute_metadata["ctypes_data_type"]
        self._python_data_type = attribute_metadata["python_data_type"]
        self._python_description = attribute_metadata["python_description"]
        self._has_explicit_read_buffer_size = attribute_metadata["has_explicit_read_buffer_size"]
        self._bitfield_enum = attribute_metadata.get("bitfield_enum", None)
        self._object_module_location = attribute_metadata.get("python_object_module_location", None)
        self._is_list = attribute_metadata["is_list"]
        self._calling_convention = attribute_metadata["calling_convention"]
        self._c_function_name = attribute_metadata["c_function_name"]
        self._is_object = attribute_metadata.get("is_python_object", False)
        self._read_buffer_size = attribute_metadata.get("read_buffer_size")
        self._python_class_name = attribute_metadata["python_class_name"]
        self._handle_parameters = []
        self._object_constructor_params = []
        if "handle_parameters" in attribute_metadata:
            for name, parameter_data in attribute_metadata["handle_parameters"].items():
                self._handle_parameters.append(Parameter(name, parameter_data))
            self._handle_parameters = sorted(self._handle_parameters, key=lambda x: x.accessor)
        self._has_explicit_write_buffer_size = attribute_metadata.get(
            "has_explicit_write_buffer_size", False
        )
        self._object_has_factory = attribute_metadata.get("python_object_has_factory", False)
        if "python_object_constructor_params" in attribute_metadata:
            for name, parameter_data in attribute_metadata[
                "python_object_constructor_params"
            ].items():
                self._object_constructor_params.append(Parameter(name, parameter_data))
            self._object_constructor_params = sorted(
                self._object_constructor_params, key=lambda x: x.accessor
            )
        self._has_explicit_write_buffer_size = attribute_metadata.get(
            "has_explicit_write_buffer_size", False
        )
        if "python_enum" in attribute_metadata:
            self._enum = attribute_metadata["python_enum"]
            self._python_data_type = self._enum
            self._is_enum = True
        elif "enum" in attribute_metadata:
            self._enum = merge_enums(attribute_metadata["enum"])
            self._python_data_type = self._enum
            self._is_enum = True
        self._object_type = attribute_metadata.get("python_object_type")
        self._has_alternate_constructor = self._object_type in ALTERNATE_CONSTRUCTOR_CLASSES

    @property
    def id(self):
        """str: Represents a unique integer value that represents an attribute.

        This is the key for the attribute itself
        """
        return self._id

    @property
    def access(self):
        """str: Specifies if the attribute is read/write.

        This is used to decide the generation of getters and setters of a property representing
        the attribute. The possible values can be read, write or read-write.
        """
        return self._access

    @property
    def name(self):
        """str: Name of the attribute.

        This name is used to generate the property name.
        """
        return self._name

    @property
    def resettable(self):
        """bool: This attribute can be reset back to default.

        This is also used to decide if a deleter has to be generated for the property.
        """
        return self._resettable

    @property
    def type(self):
        """str: Data type of the attribute.

        Here `enum` types are always represented as integers.
        """
        return self._type

    @property
    def object_module_location(self):
        """str: if return type is an object, its corresponding location will be returned."""
        return self._object_module_location

    @property
    def has_explicit_write_buffer_size(self):
        """bool: Specifies if an explicit write buffer size has to be provided.

        If True then an additional uint parameter would be provided.
        """
        if not hasattr(self, "_has_explicit_write_buffer_size"):
            return None
        return self._has_explicit_write_buffer_size

    @property
    def object_has_factory(self):
        """bool: If attribute is of an object type, this specifies if it uses a factory method.

        If the value is `True` then the `_factory` method is used for instantiation of the object.
        """
        return self._object_has_factory

    @property
    def is_enum(self):
        """bool: Represents if the attribute is an enum or not."""
        return self._is_enum

    @property
    def enum(self):
        """str: The enum type the attribute represents.

        This key will only be available for an enum type attribute.
        During code generation an attribute would be considered as an enum if it contains this key.
        """
        return self._enum

    @property
    def handle_parameters(self):
        """str: A list of parameters that represent handles that the attribute is part of.

        These are used when defining the c function parameters.
        """
        return self._handle_parameters

    @property
    def object_constructor_params(self):
        """str: This contains the additional parameters to be included in the object creation.

        These parameters are added as inputs when creating the object.
        """
        return self._object_constructor_params

    @property
    def python_class_name(self):
        """str: The name of the python class this attribute belongs to.

        This is map the attribute to the class which it belongs to.
        """
        return self._python_class_name

    @property
    def is_object(self):
        """str: This is used to determine if the value has to be used as an object."""
        return self._is_object

    @property
    def object_type(self):
        """str: The name of the object.

        During code generation, this is used to instantiate the object.
        """
        return self._object_type

    @property
    def c_function_name(self):
        """str: The name of the c function to be called when using the attribute.

        This name will be prefixed with `DAQmxSet', `DAQmxGet` and `DAQmxReset`
        for using in getters, setters and deleters respectively.
        """
        return self._c_function_name

    @property
    def calling_convention(self):
        """str: The calling convention to be followed when using the c functions."""
        return self._calling_convention

    @property
    def is_list(self):
        """bool: Determines if the attribute is of type list or not."""
        return self._is_list

    @property
    def bitfield_enum(self):
        """str: The name of the bitfield enum that the attribute represents.

        During code generation in python, this will be used to decide if the `enum_to_bitfield_list`
        method needs to called in the getter when returning the value.
        """
        if self._bitfield_enum == "N/A":
            return None
        return self._bitfield_enum

    @property
    def has_explicit_read_buffer_size(self):
        """bool: Specifies if an explicit read buffer size has to be provided for the attribute.

        If True then an additional uint parameter would be provided when calling the
        c function to mention the buffer size.
        """
        return self._has_explicit_read_buffer_size

    @property
    def read_buffer_size(self):
        """str: The read buffer size to be used when calling the c function.

        This key would only be applicable if `has_explicit_read_buffer_size` is `True`.
        In case the `has_explicit_read_buffer_size` is `True` and this key is not present,
        then the ivi dance method is used to get the buffer size.
        """
        if not hasattr(self, "_read_buffer_size"):
            return None
        return self._read_buffer_size

    @property
    def python_description(self):
        """str: The description of the attribute.

        This will be used to define the docstring of the attribute when generating the code.
        """
        return self._python_description

    @property
    def python_data_type(self):
        """str: The python data_type of the attribute.

        Currently this is used in the generation of the doc string for the attribute.
        """
        return self._python_data_type

    @property
    def ctypes_data_type(self):
        """str: The type of the attribute as per the ctypes definition in python.

        This is used to provide the type of the attribute when making c function calls in python.
        """
        return self._ctypes_data_type

    @property
    def has_alternate_constructor(self):
        """bool: Specifies if an alternate constructor is present for the attribute."""
        return self._has_alternate_constructor

    def get_lib_importer_type(self):
        """Returns the type of c function call."""
        return "windll" if self.calling_convention == "StdCall" else "cdll"

    def get_argument_types(self):
        """Returns a list of argument parameter types."""
        argtypes = []
        for handle_parameter in self.handle_parameters:
            if handle_parameter.ctypes_data_type == "ctypes.c_char_p":
                argtypes.append("ctypes_byte_str")
            else:
                argtypes.append(handle_parameter.ctypes_data_type)

        if (
            self.is_list
            and self.ctypes_data_type != "ctypes.c_char_p"
            and self.bitfield_enum is None
        ):
            argtypes.append(f"wrapped_ndpointer(dtype={self.ctypes_data_type}, flags=('C','W'))")

        elif self.ctypes_data_type == "ctypes.c_char_p":
            argtypes.append(self.ctypes_data_type)

        else:
            argtypes.append(f"ctypes.POINTER({self.ctypes_data_type})")

        if self.has_explicit_read_buffer_size:
            argtypes.append("ctypes.c_uint")

        return argtypes

    def get_handle_parameter_arguments(self):
        """Returns the list of handle parameters for the attribute."""
        argtypes = []
        for handle_parameter in self.handle_parameters:
            if handle_parameter.ctypes_data_type == "ctypes.c_char_p":
                argtypes.append("ctypes_byte_str")
            else:
                argtypes.append(handle_parameter.ctypes_data_type)
        return argtypes

    def get_return_type(self):
        """Gets the return type of attributes to be used in description."""
        constants_path = "nidaqmx.constants"
        if self.is_enum and not self.is_list:
            return f":class:`{constants_path}.{self.enum}`"
        elif self.is_object and not self.is_list:
            return f":class:`{self.object_module_location}.{self.object_type}`"
        elif self.is_enum and self.is_list:
            return f"List[:class:`{constants_path}.{self.enum}`]"
        elif self.is_object and self.is_list:
            return f"List[:class:`{self.object_module_location}.{self.object_type}`]"
        elif self.is_list:
            return f"List[{self.python_data_type}]"
        else:
            return self.python_data_type

    def update_attribute_name(self, attribute_name):
        """Updates the attribute name."""
        self._name = attribute_name.lower()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/properties/parameter.py sha256=fd09bea9adddd7811a8b0ce4f505d24ee481ca96d724150eaac91f554f160f51 bytes=1424 -->
## FILE: src/codegen/properties/parameter.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/properties/parameter.py`
- sha256: `fd09bea9adddd7811a8b0ce4f505d24ee481ca96d724150eaac91f554f160f51`
- bytes: 1424

````python
"""Structure for storing parameter metadata from scrapigen."""


class Parameter:
    """Structure for storing parameter metadata from scrapigen."""

    def __init__(self, name, parameter_metadata):
        """Structure for storing parameter metadata from scrapigen."""
        self._handle_name = name
        self._accessor = parameter_metadata.get(
            "python_accessor", parameter_metadata.get("accessor")
        )
        assert self._accessor is not None
        self._ctypes_data_type = parameter_metadata["ctypes_data_type"]
        self._cvi_name = parameter_metadata["cvi_name"]

    @property
    def handle_name(self):
        """str: The key of the parameter."""
        return self._handle_name

    @property
    def accessor(self):
        """str: Defines how to access the handle parameter.

        This value would be directly substituted when trying to use the handle parameter
        """
        return self._accessor

    @property
    def ctypes_data_type(self):
        """str: Defines the ctypes data_type of the handle parameter.

        This is used when mentioning the data_type of the handle parameter.
        """
        return self._ctypes_data_type

    @property
    def cvi_name(self):
        """str: The cvi name of the parameter.

        This is kept for the gRPC client implementation.
        """
        return self._cvi_name
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/protos/data_moniker.proto sha256=d7d7a52b04cba7e6f1a019e190be41b26c91eefb1e87c93d3356561375424d54 bytes=1782 -->
## FILE: src/codegen/protos/data_moniker.proto

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/protos/data_moniker.proto`
- sha256: `d7d7a52b04cba7e6f1a019e190be41b26c91eefb1e87c93d3356561375424d54`
- bytes: 1782

````protobuf
syntax = "proto3";

option cc_enable_arenas = true;
option csharp_namespace = "NationalInstruments.DataMonikers";

package ni.data_monikers;

import "google/protobuf/any.proto";

service DataMoniker {
  rpc BeginSidebandStream(BeginMonikerSidebandStreamRequest) returns (BeginMonikerSidebandStreamResponse) {};
  rpc StreamReadWrite(stream MonikerWriteRequest) returns (stream MonikerReadResponse) {};
  rpc StreamRead(MonikerList) returns (stream MonikerReadResponse) {};
  rpc StreamWrite(stream MonikerWriteRequest) returns (stream StreamWriteResponse) {};
}

enum SidebandStrategy
{
  UNKNOWN = 0;
  GRPC = 1;
  SHARED_MEMORY = 2;
  DOUBLE_BUFFERED_SHARED_MEMORY = 3;
  SOCKETS = 4;
  SOCKETS_LOW_LATENCY = 5;
  HYPERVISOR_SOCKETS = 6;
  RDMA = 7;
  RDMA_LOW_LATENCY = 8;
}

message BeginMonikerSidebandStreamRequest {
  SidebandStrategy strategy = 1;
  MonikerList monikers = 2;
}

message BeginMonikerSidebandStreamResponse {
  SidebandStrategy strategy = 1;
  string connection_url = 2;
  string sideband_identifier = 3;
  sint64 buffer_size = 4;
}

message Moniker {
  string service_location = 1;
  string data_source = 2;
  int64 data_instance = 3;
}

message MonikerWriteRequest {
  oneof write_data {
    MonikerList monikers = 1;
    MonikerValues data = 2;
  }
}

message MonikerReadResponse {
  MonikerValues data = 1;
}

message MonikerList {
  repeated Moniker read_monikers = 2;
  repeated Moniker write_monikers = 3;
}

message MonikerValues {
  repeated google.protobuf.Any values = 1;
}

message SidebandWriteRequest {
  bool cancel = 1;
  MonikerValues values = 2;
}

message SidebandReadResponse {
  bool cancel = 1;
  MonikerValues values = 2;
}

message StreamWriteResponse {
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/protos/nidaqmx.proto sha256=96575717232b04c5c6a5ba2f629fbbea5627cde68a77ccc2739ac5fe016bd56c bytes=405501 -->
## FILE: src/codegen/protos/nidaqmx.proto

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/protos/nidaqmx.proto`
- sha256: `96575717232b04c5c6a5ba2f629fbbea5627cde68a77ccc2739ac5fe016bd56c`
- bytes: 405501

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-DAQMX API metadata version 26.0.0
//---------------------------------------------------------------------
// Proto file for the NI-DAQMX Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option cc_enable_arenas = true;
option java_multiple_files = true;
option java_package = "com.ni.grpc.nidaqmx";
option java_outer_classname = "NiDAQmx";
option csharp_namespace = "NationalInstruments.Grpc.NiDAQmx";

package nidaqmx_grpc;

import "session.proto";
import "data_moniker.proto";
import "ni/protobuf/types/waveform.proto";
import "google/protobuf/timestamp.proto";

service NiDAQmx {
  rpc AddCDAQSyncConnection(AddCDAQSyncConnectionRequest) returns (AddCDAQSyncConnectionResponse);
  rpc AddGlobalChansToTask(AddGlobalChansToTaskRequest) returns (AddGlobalChansToTaskResponse);
  rpc AddNetworkDevice(AddNetworkDeviceRequest) returns (AddNetworkDeviceResponse);
  rpc AreConfiguredCDAQSyncPortsDisconnected(AreConfiguredCDAQSyncPortsDisconnectedRequest) returns (AreConfiguredCDAQSyncPortsDisconnectedResponse);
  rpc AutoConfigureCDAQSyncConnections(AutoConfigureCDAQSyncConnectionsRequest) returns (AutoConfigureCDAQSyncConnectionsResponse);
  rpc CalculateReversePolyCoeff(CalculateReversePolyCoeffRequest) returns (CalculateReversePolyCoeffResponse);
  rpc CfgAnlgEdgeRefTrig(CfgAnlgEdgeRefTrigRequest) returns (CfgAnlgEdgeRefTrigResponse);
  rpc CfgAnlgEdgeStartTrig(CfgAnlgEdgeStartTrigRequest) returns (CfgAnlgEdgeStartTrigResponse);
  rpc CfgAnlgMultiEdgeRefTrig(CfgAnlgMultiEdgeRefTrigRequest) returns (CfgAnlgMultiEdgeRefTrigResponse);
  rpc CfgAnlgMultiEdgeStartTrig(CfgAnlgMultiEdgeStartTrigRequest) returns (CfgAnlgMultiEdgeStartTrigResponse);
  rpc CfgAnlgWindowRefTrig(CfgAnlgWindowRefTrigRequest) returns (CfgAnlgWindowRefTrigResponse);
  rpc CfgAnlgWindowStartTrig(CfgAnlgWindowStartTrigRequest) returns (CfgAnlgWindowStartTrigResponse);
  rpc CfgBurstHandshakingTimingExportClock(CfgBurstHandshakingTimingExportClockRequest) returns (CfgBurstHandshakingTimingExportClockResponse);
  rpc CfgBurstHandshakingTimingImportClock(CfgBurstHandshakingTimingImportClockRequest) returns (CfgBurstHandshakingTimingImportClockResponse);
  rpc CfgChangeDetectionTiming(CfgChangeDetectionTimingRequest) returns (CfgChangeDetectionTimingResponse);
  rpc CfgDigEdgeRefTrig(CfgDigEdgeRefTrigRequest) returns (CfgDigEdgeRefTrigResponse);
  rpc CfgDigEdgeStartTrig(CfgDigEdgeStartTrigRequest) returns (CfgDigEdgeStartTrigResponse);
  rpc CfgDigPatternRefTrig(CfgDigPatternRefTrigRequest) returns (CfgDigPatternRefTrigResponse);
  rpc CfgDigPatternStartTrig(CfgDigPatternStartTrigRequest) returns (CfgDigPatternStartTrigResponse);
  rpc CfgHandshakingTiming(CfgHandshakingTimingRequest) returns (CfgHandshakingTimingResponse);
  rpc CfgImplicitTiming(CfgImplicitTimingRequest) returns (CfgImplicitTimingResponse);
  rpc CfgInputBuffer(CfgInputBufferRequest) returns (CfgInputBufferResponse);
  rpc CfgOutputBuffer(CfgOutputBufferRequest) returns (CfgOutputBufferResponse);
  rpc CfgPipelinedSampClkTiming(CfgPipelinedSampClkTimingRequest) returns (CfgPipelinedSampClkTimingResponse);
  rpc CfgSampClkTiming(CfgSampClkTimingRequest) returns (CfgSampClkTimingResponse);
  rpc CfgTimeStartTrig(CfgTimeStartTrigRequest) returns (CfgTimeStartTrigResponse);
  rpc CfgWatchdogAOExpirStates(CfgWatchdogAOExpirStatesRequest) returns (CfgWatchdogAOExpirStatesResponse);
  rpc CfgWatchdogCOExpirStates(CfgWatchdogCOExpirStatesRequest) returns (CfgWatchdogCOExpirStatesResponse);
  rpc CfgWatchdogDOExpirStates(CfgWatchdogDOExpirStatesRequest) returns (CfgWatchdogDOExpirStatesResponse);
  rpc ClearTEDS(ClearTEDSRequest) returns (ClearTEDSResponse);
  rpc ClearTask(ClearTaskRequest) returns (ClearTaskResponse);
  rpc ConfigureLogging(ConfigureLoggingRequest) returns (ConfigureLoggingResponse);
  rpc ConfigureTEDS(ConfigureTEDSRequest) returns (ConfigureTEDSResponse);
  rpc ConnectTerms(ConnectTermsRequest) returns (ConnectTermsResponse);
  rpc ControlWatchdogTask(ControlWatchdogTaskRequest) returns (ControlWatchdogTaskResponse);
  rpc CreateAIAccel4WireDCVoltageChan(CreateAIAccel4WireDCVoltageChanRequest) returns (CreateAIAccel4WireDCVoltageChanResponse);
  rpc CreateAIAccelChan(CreateAIAccelChanRequest) returns (CreateAIAccelChanResponse);
  rpc CreateAIAccelChargeChan(CreateAIAccelChargeChanRequest) returns (CreateAIAccelChargeChanResponse);
  rpc CreateAIBridgeChan(CreateAIBridgeChanRequest) returns (CreateAIBridgeChanResponse);
  rpc CreateAICalculatedPowerChan(CreateAICalculatedPowerChanRequest) returns (CreateAICalculatedPowerChanResponse);
  rpc CreateAIChargeChan(CreateAIChargeChanRequest) returns (CreateAIChargeChanResponse);
  rpc CreateAICurrentChan(CreateAICurrentChanRequest) returns (CreateAICurrentChanResponse);
  rpc CreateAICurrentRMSChan(CreateAICurrentRMSChanRequest) returns (CreateAICurrentRMSChanResponse);
  rpc CreateAIForceBridgePolynomialChan(CreateAIForceBridgePolynomialChanRequest) returns (CreateAIForceBridgePolynomialChanResponse);
  rpc CreateAIForceBridgeTableChan(CreateAIForceBridgeTableChanRequest) returns (CreateAIForceBridgeTableChanResponse);
  rpc CreateAIForceBridgeTwoPointLinChan(CreateAIForceBridgeTwoPointLinChanRequest) returns (CreateAIForceBridgeTwoPointLinChanResponse);
  rpc CreateAIForceIEPEChan(CreateAIForceIEPEChanRequest) returns (CreateAIForceIEPEChanResponse);
  rpc CreateAIFreqVoltageChan(CreateAIFreqVoltageChanRequest) returns (CreateAIFreqVoltageChanResponse);
  rpc CreateAIMicrophoneChan(CreateAIMicrophoneChanRequest) returns (CreateAIMicrophoneChanResponse);
  rpc CreateAIPosEddyCurrProxProbeChan(CreateAIPosEddyCurrProxProbeChanRequest) returns (CreateAIPosEddyCurrProxProbeChanResponse);
  rpc CreateAIPosLVDTChan(CreateAIPosLVDTChanRequest) returns (CreateAIPosLVDTChanResponse);
  rpc CreateAIPosRVDTChan(CreateAIPosRVDTChanRequest) returns (CreateAIPosRVDTChanResponse);
  rpc CreateAIPowerChan(CreateAIPowerChanRequest) returns (CreateAIPowerChanResponse);
  rpc CreateAIPressureBridgePolynomialChan(CreateAIPressureBridgePolynomialChanRequest) returns (CreateAIPressureBridgePolynomialChanResponse);
  rpc CreateAIPressureBridgeTableChan(CreateAIPressureBridgeTableChanRequest) returns (CreateAIPressureBridgeTableChanResponse);
  rpc CreateAIPressureBridgeTwoPointLinChan(CreateAIPressureBridgeTwoPointLinChanRequest) returns (CreateAIPressureBridgeTwoPointLinChanResponse);
  rpc CreateAIRTDChan(CreateAIRTDChanRequest) returns (CreateAIRTDChanResponse);
  rpc CreateAIResistanceChan(CreateAIResistanceChanRequest) returns (CreateAIResistanceChanResponse);
  rpc CreateAIRosetteStrainGageChan(CreateAIRosetteStrainGageChanRequest) returns (CreateAIRosetteStrainGageChanResponse);
  rpc CreateAIStrainGageChan(CreateAIStrainGageChanRequest) returns (CreateAIStrainGageChanResponse);
  rpc CreateAITempBuiltInSensorChan(CreateAITempBuiltInSensorChanRequest) returns (CreateAITempBuiltInSensorChanResponse);
  rpc CreateAIThrmcplChan(CreateAIThrmcplChanRequest) returns (CreateAIThrmcplChanResponse);
  rpc CreateAIThrmstrChanIex(CreateAIThrmstrChanIexRequest) returns (CreateAIThrmstrChanIexResponse);
  rpc CreateAIThrmstrChanVex(CreateAIThrmstrChanVexRequest) returns (CreateAIThrmstrChanVexResponse);
  rpc CreateAITorqueBridgePolynomialChan(CreateAITorqueBridgePolynomialChanRequest) returns (CreateAITorqueBridgePolynomialChanResponse);
  rpc CreateAITorqueBridgeTableChan(CreateAITorqueBridgeTableChanRequest) returns (CreateAITorqueBridgeTableChanResponse);
  rpc CreateAITorqueBridgeTwoPointLinChan(CreateAITorqueBridgeTwoPointLinChanRequest) returns (CreateAITorqueBridgeTwoPointLinChanResponse);
  rpc CreateAIVelocityIEPEChan(CreateAIVelocityIEPEChanRequest) returns (CreateAIVelocityIEPEChanResponse);
  rpc CreateAIVoltageChan(CreateAIVoltageChanRequest) returns (CreateAIVoltageChanResponse);
  rpc CreateAIVoltageChanWithExcit(CreateAIVoltageChanWithExcitRequest) returns (CreateAIVoltageChanWithExcitResponse);
  rpc CreateAIVoltageRMSChan(CreateAIVoltageRMSChanRequest) returns (CreateAIVoltageRMSChanResponse);
  rpc CreateAOCurrentChan(CreateAOCurrentChanRequest) returns (CreateAOCurrentChanResponse);
  rpc CreateAOFuncGenChan(CreateAOFuncGenChanRequest) returns (CreateAOFuncGenChanResponse);
  rpc CreateAOVoltageChan(CreateAOVoltageChanRequest) returns (CreateAOVoltageChanResponse);
  rpc CreateCIAngEncoderChan(CreateCIAngEncoderChanRequest) returns (CreateCIAngEncoderChanResponse);
  rpc CreateCIAngVelocityChan(CreateCIAngVelocityChanRequest) returns (CreateCIAngVelocityChanResponse);
  rpc CreateCICountEdgesChan(CreateCICountEdgesChanRequest) returns (CreateCICountEdgesChanResponse);
  rpc CreateCIDutyCycleChan(CreateCIDutyCycleChanRequest) returns (CreateCIDutyCycleChanResponse);
  rpc CreateCIFreqChan(CreateCIFreqChanRequest) returns (CreateCIFreqChanResponse);
  rpc CreateCIGPSTimestampChan(CreateCIGPSTimestampChanRequest) returns (CreateCIGPSTimestampChanResponse);
  rpc CreateCILinEncoderChan(CreateCILinEncoderChanRequest) returns (CreateCILinEncoderChanResponse);
  rpc CreateCILinVelocityChan(CreateCILinVelocityChanRequest) returns (CreateCILinVelocityChanResponse);
  rpc CreateCIPeriodChan(CreateCIPeriodChanRequest) returns (CreateCIPeriodChanResponse);
  rpc CreateCIPulseChanFreq(CreateCIPulseChanFreqRequest) returns (CreateCIPulseChanFreqResponse);
  rpc CreateCIPulseChanTicks(CreateCIPulseChanTicksRequest) returns (CreateCIPulseChanTicksResponse);
  rpc CreateCIPulseChanTime(CreateCIPulseChanTimeRequest) returns (CreateCIPulseChanTimeResponse);
  rpc CreateCIPulseWidthChan(CreateCIPulseWidthChanRequest) returns (CreateCIPulseWidthChanResponse);
  rpc CreateCISemiPeriodChan(CreateCISemiPeriodChanRequest) returns (CreateCISemiPeriodChanResponse);
  rpc CreateCITwoEdgeSepChan(CreateCITwoEdgeSepChanRequest) returns (CreateCITwoEdgeSepChanResponse);
  rpc CreateCOPulseChanFreq(CreateCOPulseChanFreqRequest) returns (CreateCOPulseChanFreqResponse);
  rpc CreateCOPulseChanTicks(CreateCOPulseChanTicksRequest) returns (CreateCOPulseChanTicksResponse);
  rpc CreateCOPulseChanTime(CreateCOPulseChanTimeRequest) returns (CreateCOPulseChanTimeResponse);
  rpc CreateDIChan(CreateDIChanRequest) returns (CreateDIChanResponse);
  rpc CreateDOChan(CreateDOChanRequest) returns (CreateDOChanResponse);
  rpc CreateLinScale(CreateLinScaleRequest) returns (CreateLinScaleResponse);
  rpc CreateMapScale(CreateMapScaleRequest) returns (CreateMapScaleResponse);
  rpc CreatePolynomialScale(CreatePolynomialScaleRequest) returns (CreatePolynomialScaleResponse);
  rpc CreateTEDSAIAccelChan(CreateTEDSAIAccelChanRequest) returns (CreateTEDSAIAccelChanResponse);
  rpc CreateTEDSAIBridgeChan(CreateTEDSAIBridgeChanRequest) returns (CreateTEDSAIBridgeChanResponse);
  rpc CreateTEDSAICurrentChan(CreateTEDSAICurrentChanRequest) returns (CreateTEDSAICurrentChanResponse);
  rpc CreateTEDSAIForceBridgeChan(CreateTEDSAIForceBridgeChanRequest) returns (CreateTEDSAIForceBridgeChanResponse);
  rpc CreateTEDSAIForceIEPEChan(CreateTEDSAIForceIEPEChanRequest) returns (CreateTEDSAIForceIEPEChanResponse);
  rpc CreateTEDSAIMicrophoneChan(CreateTEDSAIMicrophoneChanRequest) returns (CreateTEDSAIMicrophoneChanResponse);
  rpc CreateTEDSAIPosLVDTChan(CreateTEDSAIPosLVDTChanRequest) returns (CreateTEDSAIPosLVDTChanResponse);
  rpc CreateTEDSAIPosRVDTChan(CreateTEDSAIPosRVDTChanRequest) returns (CreateTEDSAIPosRVDTChanResponse);
  rpc CreateTEDSAIPressureBridgeChan(CreateTEDSAIPressureBridgeChanRequest) returns (CreateTEDSAIPressureBridgeChanResponse);
  rpc CreateTEDSAIRTDChan(CreateTEDSAIRTDChanRequest) returns (CreateTEDSAIRTDChanResponse);
  rpc CreateTEDSAIResistanceChan(CreateTEDSAIResistanceChanRequest) returns (CreateTEDSAIResistanceChanResponse);
  rpc CreateTEDSAIStrainGageChan(CreateTEDSAIStrainGageChanRequest) returns (CreateTEDSAIStrainGageChanResponse);
  rpc CreateTEDSAIThrmcplChan(CreateTEDSAIThrmcplChanRequest) returns (CreateTEDSAIThrmcplChanResponse);
  rpc CreateTEDSAIThrmstrChanIex(CreateTEDSAIThrmstrChanIexRequest) returns (CreateTEDSAIThrmstrChanIexResponse);
  rpc CreateTEDSAIThrmstrChanVex(CreateTEDSAIThrmstrChanVexRequest) returns (CreateTEDSAIThrmstrChanVexResponse);
  rpc CreateTEDSAITorqueBridgeChan(CreateTEDSAITorqueBridgeChanRequest) returns (CreateTEDSAITorqueBridgeChanResponse);
  rpc CreateTEDSAIVoltageChan(CreateTEDSAIVoltageChanRequest) returns (CreateTEDSAIVoltageChanResponse);
  rpc CreateTEDSAIVoltageChanWithExcit(CreateTEDSAIVoltageChanWithExcitRequest) returns (CreateTEDSAIVoltageChanWithExcitResponse);
  rpc CreateTableScale(CreateTableScaleRequest) returns (CreateTableScaleResponse);
  rpc CreateTask(CreateTaskRequest) returns (CreateTaskResponse);
  rpc CreateWatchdogTimerTask(CreateWatchdogTimerTaskRequest) returns (CreateWatchdogTimerTaskResponse);
  rpc CreateWatchdogTimerTaskEx(CreateWatchdogTimerTaskExRequest) returns (CreateWatchdogTimerTaskExResponse);
  rpc DeleteNetworkDevice(DeleteNetworkDeviceRequest) returns (DeleteNetworkDeviceResponse);
  rpc DeleteSavedGlobalChan(DeleteSavedGlobalChanRequest) returns (DeleteSavedGlobalChanResponse);
  rpc DeleteSavedScale(DeleteSavedScaleRequest) returns (DeleteSavedScaleResponse);
  rpc DeleteSavedTask(DeleteSavedTaskRequest) returns (DeleteSavedTaskResponse);
  rpc DeviceSupportsCal(DeviceSupportsCalRequest) returns (DeviceSupportsCalResponse);
  rpc DisableRefTrig(DisableRefTrigRequest) returns (DisableRefTrigResponse);
  rpc DisableStartTrig(DisableStartTrigRequest) returns (DisableStartTrigResponse);
  rpc DisconnectTerms(DisconnectTermsRequest) returns (DisconnectTermsResponse);
  rpc ExportSignal(ExportSignalRequest) returns (ExportSignalResponse);
  rpc GetAIChanCalCalDate(GetAIChanCalCalDateRequest) returns (GetAIChanCalCalDateResponse);
  rpc GetAIChanCalExpDate(GetAIChanCalExpDateRequest) returns (GetAIChanCalExpDateResponse);
  rpc GetAnalogPowerUpStates(GetAnalogPowerUpStatesRequest) returns (GetAnalogPowerUpStatesResponse);
  rpc GetAnalogPowerUpStatesWithOutputType(GetAnalogPowerUpStatesWithOutputTypeRequest) returns (GetAnalogPowerUpStatesWithOutputTypeResponse);
  rpc GetArmStartTrigTimestampVal(GetArmStartTrigTimestampValRequest) returns (GetArmStartTrigTimestampValResponse);
  rpc GetArmStartTrigTrigWhen(GetArmStartTrigTrigWhenRequest) returns (GetArmStartTrigTrigWhenResponse);
  rpc GetAutoConfiguredCDAQSyncConnections(GetAutoConfiguredCDAQSyncConnectionsRequest) returns (GetAutoConfiguredCDAQSyncConnectionsResponse);
  rpc GetBufferAttributeUInt32(GetBufferAttributeUInt32Request) returns (GetBufferAttributeUInt32Response);
  rpc GetCalInfoAttributeBool(GetCalInfoAttributeBoolRequest) returns (GetCalInfoAttributeBoolResponse);
  rpc GetCalInfoAttributeDouble(GetCalInfoAttributeDoubleRequest) returns (GetCalInfoAttributeDoubleResponse);
  rpc GetCalInfoAttributeString(GetCalInfoAttributeStringRequest) returns (GetCalInfoAttributeStringResponse);
  rpc GetCalInfoAttributeUInt32(GetCalInfoAttributeUInt32Request) returns (GetCalInfoAttributeUInt32Response);
  rpc GetChanAttributeBool(GetChanAttributeBoolRequest) returns (GetChanAttributeBoolResponse);
  rpc GetChanAttributeDouble(GetChanAttributeDoubleRequest) returns (GetChanAttributeDoubleResponse);
  rpc GetChanAttributeDoubleArray(GetChanAttributeDoubleArrayRequest) returns (GetChanAttributeDoubleArrayResponse);
  rpc GetChanAttributeInt32(GetChanAttributeInt32Request) returns (GetChanAttributeInt32Response);
  rpc GetChanAttributeString(GetChanAttributeStringRequest) returns (GetChanAttributeStringResponse);
  rpc GetChanAttributeUInt32(GetChanAttributeUInt32Request) returns (GetChanAttributeUInt32Response);
  rpc GetDeviceAttributeBool(GetDeviceAttributeBoolRequest) returns (GetDeviceAttributeBoolResponse);
  rpc GetDeviceAttributeDouble(GetDeviceAttributeDoubleRequest) returns (GetDeviceAttributeDoubleResponse);
  rpc GetDeviceAttributeDoubleArray(GetDeviceAttributeDoubleArrayRequest) returns (GetDeviceAttributeDoubleArrayResponse);
  rpc GetDeviceAttributeInt32(GetDeviceAttributeInt32Request) returns (GetDeviceAttributeInt32Response);
  rpc GetDeviceAttributeInt32Array(GetDeviceAttributeInt32ArrayRequest) returns (GetDeviceAttributeInt32ArrayResponse);
  rpc GetDeviceAttributeString(GetDeviceAttributeStringRequest) returns (GetDeviceAttributeStringResponse);
  rpc GetDeviceAttributeUInt32(GetDeviceAttributeUInt32Request) returns (GetDeviceAttributeUInt32Response);
  rpc GetDeviceAttributeUInt32Array(GetDeviceAttributeUInt32ArrayRequest) returns (GetDeviceAttributeUInt32ArrayResponse);
  rpc GetDigitalLogicFamilyPowerUpState(GetDigitalLogicFamilyPowerUpStateRequest) returns (GetDigitalLogicFamilyPowerUpStateResponse);
  rpc GetDigitalPowerUpStates(GetDigitalPowerUpStatesRequest) returns (GetDigitalPowerUpStatesResponse);
  rpc GetDigitalPullUpPullDownStates(GetDigitalPullUpPullDownStatesRequest) returns (GetDigitalPullUpPullDownStatesResponse);
  rpc GetDisconnectedCDAQSyncPorts(GetDisconnectedCDAQSyncPortsRequest) returns (GetDisconnectedCDAQSyncPortsResponse);
  rpc GetErrorString(GetErrorStringRequest) returns (GetErrorStringResponse);
  rpc GetExportedSignalAttributeBool(GetExportedSignalAttributeBoolRequest) returns (GetExportedSignalAttributeBoolResponse);
  rpc GetExportedSignalAttributeDouble(GetExportedSignalAttributeDoubleRequest) returns (GetExportedSignalAttributeDoubleResponse);
  rpc GetExportedSignalAttributeInt32(GetExportedSignalAttributeInt32Request) returns (GetExportedSignalAttributeInt32Response);
  rpc GetExportedSignalAttributeString(GetExportedSignalAttributeStringRequest) returns (GetExportedSignalAttributeStringResponse);
  rpc GetExportedSignalAttributeUInt32(GetExportedSignalAttributeUInt32Request) returns (GetExportedSignalAttributeUInt32Response);
  rpc GetExtCalLastDateAndTime(GetExtCalLastDateAndTimeRequest) returns (GetExtCalLastDateAndTimeResponse);
  rpc GetFirstSampClkWhen(GetFirstSampClkWhenRequest) returns (GetFirstSampClkWhenResponse);
  rpc GetFirstSampTimestampVal(GetFirstSampTimestampValRequest) returns (GetFirstSampTimestampValResponse);
  rpc GetNthTaskChannel(GetNthTaskChannelRequest) returns (GetNthTaskChannelResponse);
  rpc GetNthTaskDevice(GetNthTaskDeviceRequest) returns (GetNthTaskDeviceResponse);
  rpc GetNthTaskReadChannel(GetNthTaskReadChannelRequest) returns (GetNthTaskReadChannelResponse);
  rpc GetPersistedChanAttributeBool(GetPersistedChanAttributeBoolRequest) returns (GetPersistedChanAttributeBoolResponse);
  rpc GetPersistedChanAttributeString(GetPersistedChanAttributeStringRequest) returns (GetPersistedChanAttributeStringResponse);
  rpc GetPersistedScaleAttributeBool(GetPersistedScaleAttributeBoolRequest) returns (GetPersistedScaleAttributeBoolResponse);
  rpc GetPersistedScaleAttributeString(GetPersistedScaleAttributeStringRequest) returns (GetPersistedScaleAttributeStringResponse);
  rpc GetPersistedTaskAttributeBool(GetPersistedTaskAttributeBoolRequest) returns (GetPersistedTaskAttributeBoolResponse);
  rpc GetPersistedTaskAttributeString(GetPersistedTaskAttributeStringRequest) returns (GetPersistedTaskAttributeStringResponse);
  rpc GetPhysicalChanAttributeBool(GetPhysicalChanAttributeBoolRequest) returns (GetPhysicalChanAttributeBoolResponse);
  rpc GetPhysicalChanAttributeBytes(GetPhysicalChanAttributeBytesRequest) returns (GetPhysicalChanAttributeBytesResponse);
  rpc GetPhysicalChanAttributeDouble(GetPhysicalChanAttributeDoubleRequest) returns (GetPhysicalChanAttributeDoubleResponse);
  rpc GetPhysicalChanAttributeDoubleArray(GetPhysicalChanAttributeDoubleArrayRequest) returns (GetPhysicalChanAttributeDoubleArrayResponse);
  rpc GetPhysicalChanAttributeInt32(GetPhysicalChanAttributeInt32Request) returns (GetPhysicalChanAttributeInt32Response);
  rpc GetPhysicalChanAttributeInt32Array(GetPhysicalChanAttributeInt32ArrayRequest) returns (GetPhysicalChanAttributeInt32ArrayResponse);
  rpc GetPhysicalChanAttributeString(GetPhysicalChanAttributeStringRequest) returns (GetPhysicalChanAttributeStringResponse);
  rpc GetPhysicalChanAttributeUInt32(GetPhysicalChanAttributeUInt32Request) returns (GetPhysicalChanAttributeUInt32Response);
  rpc GetPhysicalChanAttributeUInt32Array(GetPhysicalChanAttributeUInt32ArrayRequest) returns (GetPhysicalChanAttributeUInt32ArrayResponse);
  rpc GetReadAttributeBool(GetReadAttributeBoolRequest) returns (GetReadAttributeBoolResponse);
  rpc GetReadAttributeDouble(GetReadAttributeDoubleRequest) returns (GetReadAttributeDoubleResponse);
  rpc GetReadAttributeInt32(GetReadAttributeInt32Request) returns (GetReadAttributeInt32Response);
  rpc GetReadAttributeString(GetReadAttributeStringRequest) returns (GetReadAttributeStringResponse);
  rpc GetReadAttributeUInt32(GetReadAttributeUInt32Request) returns (GetReadAttributeUInt32Response);
  rpc GetReadAttributeUInt64(GetReadAttributeUInt64Request) returns (GetReadAttributeUInt64Response);
  rpc GetRealTimeAttributeBool(GetRealTimeAttributeBoolRequest) returns (GetRealTimeAttributeBoolResponse);
  rpc GetRealTimeAttributeInt32(GetRealTimeAttributeInt32Request) returns (GetRealTimeAttributeInt32Response);
  rpc GetRealTimeAttributeUInt32(GetRealTimeAttributeUInt32Request) returns (GetRealTimeAttributeUInt32Response);
  rpc GetRefTrigTimestampVal(GetRefTrigTimestampValRequest) returns (GetRefTrigTimestampValResponse);
  rpc GetScaleAttributeDouble(GetScaleAttributeDoubleRequest) returns (GetScaleAttributeDoubleResponse);
  rpc GetScaleAttributeDoubleArray(GetScaleAttributeDoubleArrayRequest) returns (GetScaleAttributeDoubleArrayResponse);
  rpc GetScaleAttributeInt32(GetScaleAttributeInt32Request) returns (GetScaleAttributeInt32Response);
  rpc GetScaleAttributeString(GetScaleAttributeStringRequest) returns (GetScaleAttributeStringResponse);
  rpc GetSelfCalLastDateAndTime(GetSelfCalLastDateAndTimeRequest) returns (GetSelfCalLastDateAndTimeResponse);
  rpc GetStartTrigTimestampVal(GetStartTrigTimestampValRequest) returns (GetStartTrigTimestampValResponse);
  rpc GetStartTrigTrigWhen(GetStartTrigTrigWhenRequest) returns (GetStartTrigTrigWhenResponse);
  rpc GetSyncPulseTimeWhen(GetSyncPulseTimeWhenRequest) returns (GetSyncPulseTimeWhenResponse);
  rpc GetSystemInfoAttributeString(GetSystemInfoAttributeStringRequest) returns (GetSystemInfoAttributeStringResponse);
  rpc GetSystemInfoAttributeUInt32(GetSystemInfoAttributeUInt32Request) returns (GetSystemInfoAttributeUInt32Response);
  rpc GetTaskAttributeBool(GetTaskAttributeBoolRequest) returns (GetTaskAttributeBoolResponse);
  rpc GetTaskAttributeString(GetTaskAttributeStringRequest) returns (GetTaskAttributeStringResponse);
  rpc GetTaskAttributeUInt32(GetTaskAttributeUInt32Request) returns (GetTaskAttributeUInt32Response);
  rpc GetTimingAttributeBool(GetTimingAttributeBoolRequest) returns (GetTimingAttributeBoolResponse);
  rpc GetTimingAttributeDouble(GetTimingAttributeDoubleRequest) returns (GetTimingAttributeDoubleResponse);
  rpc GetTimingAttributeExBool(GetTimingAttributeExBoolRequest) returns (GetTimingAttributeExBoolResponse);
  rpc GetTimingAttributeExDouble(GetTimingAttributeExDoubleRequest) returns (GetTimingAttributeExDoubleResponse);
  rpc GetTimingAttributeExInt32(GetTimingAttributeExInt32Request) returns (GetTimingAttributeExInt32Response);
  rpc GetTimingAttributeExString(GetTimingAttributeExStringRequest) returns (GetTimingAttributeExStringResponse);
  rpc GetTimingAttributeExTimestamp(GetTimingAttributeExTimestampRequest) returns (GetTimingAttributeExTimestampResponse);
  rpc GetTimingAttributeExUInt32(GetTimingAttributeExUInt32Request) returns (GetTimingAttributeExUInt32Response);
  rpc GetTimingAttributeExUInt64(GetTimingAttributeExUInt64Request) returns (GetTimingAttributeExUInt64Response);
  rpc GetTimingAttributeInt32(GetTimingAttributeInt32Request) returns (GetTimingAttributeInt32Response);
  rpc GetTimingAttributeString(GetTimingAttributeStringRequest) returns (GetTimingAttributeStringResponse);
  rpc GetTimingAttributeTimestamp(GetTimingAttributeTimestampRequest) returns (GetTimingAttributeTimestampResponse);
  rpc GetTimingAttributeUInt32(GetTimingAttributeUInt32Request) returns (GetTimingAttributeUInt32Response);
  rpc GetTimingAttributeUInt64(GetTimingAttributeUInt64Request) returns (GetTimingAttributeUInt64Response);
  rpc GetTrigAttributeBool(GetTrigAttributeBoolRequest) returns (GetTrigAttributeBoolResponse);
  rpc GetTrigAttributeDouble(GetTrigAttributeDoubleRequest) returns (GetTrigAttributeDoubleResponse);
  rpc GetTrigAttributeDoubleArray(GetTrigAttributeDoubleArrayRequest) returns (GetTrigAttributeDoubleArrayResponse);
  rpc GetTrigAttributeInt32(GetTrigAttributeInt32Request) returns (GetTrigAttributeInt32Response);
  rpc GetTrigAttributeInt32Array(GetTrigAttributeInt32ArrayRequest) returns (GetTrigAttributeInt32ArrayResponse);
  rpc GetTrigAttributeString(GetTrigAttributeStringRequest) returns (GetTrigAttributeStringResponse);
  rpc GetTrigAttributeTimestamp(GetTrigAttributeTimestampRequest) returns (GetTrigAttributeTimestampResponse);
  rpc GetTrigAttributeUInt32(GetTrigAttributeUInt32Request) returns (GetTrigAttributeUInt32Response);
  rpc GetWatchdogAttributeBool(GetWatchdogAttributeBoolRequest) returns (GetWatchdogAttributeBoolResponse);
  rpc GetWatchdogAttributeDouble(GetWatchdogAttributeDoubleRequest) returns (GetWatchdogAttributeDoubleResponse);
  rpc GetWatchdogAttributeInt32(GetWatchdogAttributeInt32Request) returns (GetWatchdogAttributeInt32Response);
  rpc GetWatchdogAttributeString(GetWatchdogAttributeStringRequest) returns (GetWatchdogAttributeStringResponse);
  rpc GetWriteAttributeBool(GetWriteAttributeBoolRequest) returns (GetWriteAttributeBoolResponse);
  rpc GetWriteAttributeDouble(GetWriteAttributeDoubleRequest) returns (GetWriteAttributeDoubleResponse);
  rpc GetWriteAttributeInt32(GetWriteAttributeInt32Request) returns (GetWriteAttributeInt32Response);
  rpc GetWriteAttributeString(GetWriteAttributeStringRequest) returns (GetWriteAttributeStringResponse);
  rpc GetWriteAttributeUInt32(GetWriteAttributeUInt32Request) returns (GetWriteAttributeUInt32Response);
  rpc GetWriteAttributeUInt64(GetWriteAttributeUInt64Request) returns (GetWriteAttributeUInt64Response);
  rpc IsTaskDone(IsTaskDoneRequest) returns (IsTaskDoneResponse);
  rpc LoadTask(LoadTaskRequest) returns (LoadTaskResponse);
  rpc PerformBridgeOffsetNullingCalEx(PerformBridgeOffsetNullingCalExRequest) returns (PerformBridgeOffsetNullingCalExResponse);
  rpc PerformBridgeShuntCalEx(PerformBridgeShuntCalExRequest) returns (PerformBridgeShuntCalExResponse);
  rpc PerformStrainShuntCalEx(PerformStrainShuntCalExRequest) returns (PerformStrainShuntCalExResponse);
  rpc PerformThrmcplLeadOffsetNullingCal(PerformThrmcplLeadOffsetNullingCalRequest) returns (PerformThrmcplLeadOffsetNullingCalResponse);
  rpc ReadAnalogF64(ReadAnalogF64Request) returns (ReadAnalogF64Response);
  rpc BeginReadAnalogF64(BeginReadAnalogF64Request) returns (BeginReadAnalogF64Response);
  rpc ReadAnalogScalarF64(ReadAnalogScalarF64Request) returns (ReadAnalogScalarF64Response);
  rpc BeginReadAnalogScalarF64(BeginReadAnalogScalarF64Request) returns (BeginReadAnalogScalarF64Response);
  rpc ReadBinaryI16(ReadBinaryI16Request) returns (ReadBinaryI16Response);
  rpc BeginReadBinaryI16(BeginReadBinaryI16Request) returns (BeginReadBinaryI16Response);
  rpc ReadBinaryI32(ReadBinaryI32Request) returns (ReadBinaryI32Response);
  rpc BeginReadBinaryI32(BeginReadBinaryI32Request) returns (BeginReadBinaryI32Response);
  rpc ReadBinaryU16(ReadBinaryU16Request) returns (ReadBinaryU16Response);
  rpc BeginReadBinaryU16(BeginReadBinaryU16Request) returns (BeginReadBinaryU16Response);
  rpc ReadBinaryU32(ReadBinaryU32Request) returns (ReadBinaryU32Response);
  rpc BeginReadBinaryU32(BeginReadBinaryU32Request) returns (BeginReadBinaryU32Response);
  rpc ReadCounterF64(ReadCounterF64Request) returns (ReadCounterF64Response);
  rpc BeginReadCounterF64(BeginReadCounterF64Request) returns (BeginReadCounterF64Response);
  rpc ReadCounterF64Ex(ReadCounterF64ExRequest) returns (ReadCounterF64ExResponse);
  rpc BeginReadCounterF64Ex(BeginReadCounterF64ExRequest) returns (BeginReadCounterF64ExResponse);
  rpc ReadCounterScalarF64(ReadCounterScalarF64Request) returns (ReadCounterScalarF64Response);
  rpc BeginReadCounterScalarF64(BeginReadCounterScalarF64Request) returns (BeginReadCounterScalarF64Response);
  rpc ReadCounterScalarU32(ReadCounterScalarU32Request) returns (ReadCounterScalarU32Response);
  rpc BeginReadCounterScalarU32(BeginReadCounterScalarU32Request) returns (BeginReadCounterScalarU32Response);
  rpc ReadCounterU32(ReadCounterU32Request) returns (ReadCounterU32Response);
  rpc BeginReadCounterU32(BeginReadCounterU32Request) returns (BeginReadCounterU32Response);
  rpc ReadCounterU32Ex(ReadCounterU32ExRequest) returns (ReadCounterU32ExResponse);
  rpc BeginReadCounterU32Ex(BeginReadCounterU32ExRequest) returns (BeginReadCounterU32ExResponse);
  rpc ReadCtrFreq(ReadCtrFreqRequest) returns (ReadCtrFreqResponse);
  rpc BeginReadCtrFreq(BeginReadCtrFreqRequest) returns (BeginReadCtrFreqResponse);
  rpc ReadCtrFreqScalar(ReadCtrFreqScalarRequest) returns (ReadCtrFreqScalarResponse);
  rpc BeginReadCtrFreqScalar(BeginReadCtrFreqScalarRequest) returns (BeginReadCtrFreqScalarResponse);
  rpc ReadCtrTicks(ReadCtrTicksRequest) returns (ReadCtrTicksResponse);
  rpc BeginReadCtrTicks(BeginReadCtrTicksRequest) returns (BeginReadCtrTicksResponse);
  rpc ReadCtrTicksScalar(ReadCtrTicksScalarRequest) returns (ReadCtrTicksScalarResponse);
  rpc BeginReadCtrTicksScalar(BeginReadCtrTicksScalarRequest) returns (BeginReadCtrTicksScalarResponse);
  rpc ReadCtrTime(ReadCtrTimeRequest) returns (ReadCtrTimeResponse);
  rpc BeginReadCtrTime(BeginReadCtrTimeRequest) returns (BeginReadCtrTimeResponse);
  rpc ReadCtrTimeScalar(ReadCtrTimeScalarRequest) returns (ReadCtrTimeScalarResponse);
  rpc BeginReadCtrTimeScalar(BeginReadCtrTimeScalarRequest) returns (BeginReadCtrTimeScalarResponse);
  rpc ReadDigitalLines(ReadDigitalLinesRequest) returns (ReadDigitalLinesResponse);
  rpc BeginReadDigitalLines(BeginReadDigitalLinesRequest) returns (BeginReadDigitalLinesResponse);
  rpc ReadDigitalScalarU32(ReadDigitalScalarU32Request) returns (ReadDigitalScalarU32Response);
  rpc BeginReadDigitalScalarU32(BeginReadDigitalScalarU32Request) returns (BeginReadDigitalScalarU32Response);
  rpc ReadDigitalU16(ReadDigitalU16Request) returns (ReadDigitalU16Response);
  rpc BeginReadDigitalU16(BeginReadDigitalU16Request) returns (BeginReadDigitalU16Response);
  rpc ReadDigitalU32(ReadDigitalU32Request) returns (ReadDigitalU32Response);
  rpc BeginReadDigitalU32(BeginReadDigitalU32Request) returns (BeginReadDigitalU32Response);
  rpc ReadDigitalU8(ReadDigitalU8Request) returns (ReadDigitalU8Response);
  rpc BeginReadDigitalU8(BeginReadDigitalU8Request) returns (BeginReadDigitalU8Response);
  rpc ReadIDPinMemory(ReadIDPinMemoryRequest) returns (ReadIDPinMemoryResponse);
  rpc ReadPowerBinaryI16(ReadPowerBinaryI16Request) returns (ReadPowerBinaryI16Response);
  rpc BeginReadPowerBinaryI16(BeginReadPowerBinaryI16Request) returns (BeginReadPowerBinaryI16Response);
  rpc ReadPowerF64(ReadPowerF64Request) returns (ReadPowerF64Response);
  rpc BeginReadPowerF64(BeginReadPowerF64Request) returns (BeginReadPowerF64Response);
  rpc ReadPowerScalarF64(ReadPowerScalarF64Request) returns (ReadPowerScalarF64Response);
  rpc BeginReadPowerScalarF64(BeginReadPowerScalarF64Request) returns (BeginReadPowerScalarF64Response);
  rpc ReadRaw(ReadRawRequest) returns (ReadRawResponse);
  rpc BeginReadRaw(BeginReadRawRequest) returns (BeginReadRawResponse);
  rpc RegisterDoneEvent(RegisterDoneEventRequest) returns (stream RegisterDoneEventResponse);
  rpc RegisterEveryNSamplesEvent(RegisterEveryNSamplesEventRequest) returns (stream RegisterEveryNSamplesEventResponse);
  rpc RegisterSignalEvent(RegisterSignalEventRequest) returns (stream RegisterSignalEventResponse);
  rpc RemoveCDAQSyncConnection(RemoveCDAQSyncConnectionRequest) returns (RemoveCDAQSyncConnectionResponse);
  rpc ReserveNetworkDevice(ReserveNetworkDeviceRequest) returns (ReserveNetworkDeviceResponse);
  rpc ResetBufferAttribute(ResetBufferAttributeRequest) returns (ResetBufferAttributeResponse);
  rpc ResetChanAttribute(ResetChanAttributeRequest) returns (ResetChanAttributeResponse);
  rpc ResetDevice(ResetDeviceRequest) returns (ResetDeviceResponse);
  rpc ResetExportedSignalAttribute(ResetExportedSignalAttributeRequest) returns (ResetExportedSignalAttributeResponse);
  rpc ResetReadAttribute(ResetReadAttributeRequest) returns (ResetReadAttributeResponse);
  rpc ResetRealTimeAttribute(ResetRealTimeAttributeRequest) returns (ResetRealTimeAttributeResponse);
  rpc ResetTimingAttribute(ResetTimingAttributeRequest) returns (ResetTimingAttributeResponse);
  rpc ResetTimingAttributeEx(ResetTimingAttributeExRequest) returns (ResetTimingAttributeExResponse);
  rpc ResetTrigAttribute(ResetTrigAttributeRequest) returns (ResetTrigAttributeResponse);
  rpc ResetWatchdogAttribute(ResetWatchdogAttributeRequest) returns (ResetWatchdogAttributeResponse);
  rpc ResetWriteAttribute(ResetWriteAttributeRequest) returns (ResetWriteAttributeResponse);
  rpc RestoreLastExtCalConst(RestoreLastExtCalConstRequest) returns (RestoreLastExtCalConstResponse);
  rpc SaveGlobalChan(SaveGlobalChanRequest) returns (SaveGlobalChanResponse);
  rpc SaveScale(SaveScaleRequest) returns (SaveScaleResponse);
  rpc SaveTask(SaveTaskRequest) returns (SaveTaskResponse);
  rpc SelfCal(SelfCalRequest) returns (SelfCalResponse);
  rpc SelfTestDevice(SelfTestDeviceRequest) returns (SelfTestDeviceResponse);
  rpc SetAIChanCalCalDate(SetAIChanCalCalDateRequest) returns (SetAIChanCalCalDateResponse);
  rpc SetAIChanCalExpDate(SetAIChanCalExpDateRequest) returns (SetAIChanCalExpDateResponse);
  rpc SetAnalogPowerUpStates(SetAnalogPowerUpStatesRequest) returns (SetAnalogPowerUpStatesResponse);
  rpc SetAnalogPowerUpStatesWithOutputType(SetAnalogPowerUpStatesWithOutputTypeRequest) returns (SetAnalogPowerUpStatesWithOutputTypeResponse);
  rpc SetArmStartTrigTrigWhen(SetArmStartTrigTrigWhenRequest) returns (SetArmStartTrigTrigWhenResponse);
  rpc SetBufferAttributeUInt32(SetBufferAttributeUInt32Request) returns (SetBufferAttributeUInt32Response);
  rpc SetCalInfoAttributeBool(SetCalInfoAttributeBoolRequest) returns (SetCalInfoAttributeBoolResponse);
  rpc SetCalInfoAttributeDouble(SetCalInfoAttributeDoubleRequest) returns (SetCalInfoAttributeDoubleResponse);
  rpc SetCalInfoAttributeString(SetCalInfoAttributeStringRequest) returns (SetCalInfoAttributeStringResponse);
  rpc SetCalInfoAttributeUInt32(SetCalInfoAttributeUInt32Request) returns (SetCalInfoAttributeUInt32Response);
  rpc SetChanAttributeBool(SetChanAttributeBoolRequest) returns (SetChanAttributeBoolResponse);
  rpc SetChanAttributeDouble(SetChanAttributeDoubleRequest) returns (SetChanAttributeDoubleResponse);
  rpc SetChanAttributeDoubleArray(SetChanAttributeDoubleArrayRequest) returns (SetChanAttributeDoubleArrayResponse);
  rpc SetChanAttributeInt32(SetChanAttributeInt32Request) returns (SetChanAttributeInt32Response);
  rpc SetChanAttributeString(SetChanAttributeStringRequest) returns (SetChanAttributeStringResponse);
  rpc SetChanAttributeUInt32(SetChanAttributeUInt32Request) returns (SetChanAttributeUInt32Response);
  rpc SetDigitalLogicFamilyPowerUpState(SetDigitalLogicFamilyPowerUpStateRequest) returns (SetDigitalLogicFamilyPowerUpStateResponse);
  rpc SetDigitalPowerUpStates(SetDigitalPowerUpStatesRequest) returns (SetDigitalPowerUpStatesResponse);
  rpc SetDigitalPullUpPullDownStates(SetDigitalPullUpPullDownStatesRequest) returns (SetDigitalPullUpPullDownStatesResponse);
  rpc SetExportedSignalAttributeBool(SetExportedSignalAttributeBoolRequest) returns (SetExportedSignalAttributeBoolResponse);
  rpc SetExportedSignalAttributeDouble(SetExportedSignalAttributeDoubleRequest) returns (SetExportedSignalAttributeDoubleResponse);
  rpc SetExportedSignalAttributeInt32(SetExportedSignalAttributeInt32Request) returns (SetExportedSignalAttributeInt32Response);
  rpc SetExportedSignalAttributeString(SetExportedSignalAttributeStringRequest) returns (SetExportedSignalAttributeStringResponse);
  rpc SetExportedSignalAttributeUInt32(SetExportedSignalAttributeUInt32Request) returns (SetExportedSignalAttributeUInt32Response);
  rpc SetFirstSampClkWhen(SetFirstSampClkWhenRequest) returns (SetFirstSampClkWhenResponse);
  rpc SetReadAttributeBool(SetReadAttributeBoolRequest) returns (SetReadAttributeBoolResponse);
  rpc SetReadAttributeDouble(SetReadAttributeDoubleRequest) returns (SetReadAttributeDoubleResponse);
  rpc SetReadAttributeInt32(SetReadAttributeInt32Request) returns (SetReadAttributeInt32Response);
  rpc SetReadAttributeString(SetReadAttributeStringRequest) returns (SetReadAttributeStringResponse);
  rpc SetReadAttributeUInt32(SetReadAttributeUInt32Request) returns (SetReadAttributeUInt32Response);
  rpc SetReadAttributeUInt64(SetReadAttributeUInt64Request) returns (SetReadAttributeUInt64Response);
  rpc SetRealTimeAttributeBool(SetRealTimeAttributeBoolRequest) returns (SetRealTimeAttributeBoolResponse);
  rpc SetRealTimeAttributeInt32(SetRealTimeAttributeInt32Request) returns (SetRealTimeAttributeInt32Response);
  rpc SetRealTimeAttributeUInt32(SetRealTimeAttributeUInt32Request) returns (SetRealTimeAttributeUInt32Response);
  rpc SetScaleAttributeDouble(SetScaleAttributeDoubleRequest) returns (SetScaleAttributeDoubleResponse);
  rpc SetScaleAttributeDoubleArray(SetScaleAttributeDoubleArrayRequest) returns (SetScaleAttributeDoubleArrayResponse);
  rpc SetScaleAttributeInt32(SetScaleAttributeInt32Request) returns (SetScaleAttributeInt32Response);
  rpc SetScaleAttributeString(SetScaleAttributeStringRequest) returns (SetScaleAttributeStringResponse);
  rpc SetStartTrigTrigWhen(SetStartTrigTrigWhenRequest) returns (SetStartTrigTrigWhenResponse);
  rpc SetSyncPulseTimeWhen(SetSyncPulseTimeWhenRequest) returns (SetSyncPulseTimeWhenResponse);
  rpc SetTimingAttributeBool(SetTimingAttributeBoolRequest) returns (SetTimingAttributeBoolResponse);
  rpc SetTimingAttributeDouble(SetTimingAttributeDoubleRequest) returns (SetTimingAttributeDoubleResponse);
  rpc SetTimingAttributeExBool(SetTimingAttributeExBoolRequest) returns (SetTimingAttributeExBoolResponse);
  rpc SetTimingAttributeExDouble(SetTimingAttributeExDoubleRequest) returns (SetTimingAttributeExDoubleResponse);
  rpc SetTimingAttributeExInt32(SetTimingAttributeExInt32Request) returns (SetTimingAttributeExInt32Response);
  rpc SetTimingAttributeExString(SetTimingAttributeExStringRequest) returns (SetTimingAttributeExStringResponse);
  rpc SetTimingAttributeExTimestamp(SetTimingAttributeExTimestampRequest) returns (SetTimingAttributeExTimestampResponse);
  rpc SetTimingAttributeExUInt32(SetTimingAttributeExUInt32Request) returns (SetTimingAttributeExUInt32Response);
  rpc SetTimingAttributeExUInt64(SetTimingAttributeExUInt64Request) returns (SetTimingAttributeExUInt64Response);
  rpc SetTimingAttributeInt32(SetTimingAttributeInt32Request) returns (SetTimingAttributeInt32Response);
  rpc SetTimingAttributeString(SetTimingAttributeStringRequest) returns (SetTimingAttributeStringResponse);
  rpc SetTimingAttributeTimestamp(SetTimingAttributeTimestampRequest) returns (SetTimingAttributeTimestampResponse);
  rpc SetTimingAttributeUInt32(SetTimingAttributeUInt32Request) returns (SetTimingAttributeUInt32Response);
  rpc SetTimingAttributeUInt64(SetTimingAttributeUInt64Request) returns (SetTimingAttributeUInt64Response);
  rpc SetTrigAttributeBool(SetTrigAttributeBoolRequest) returns (SetTrigAttributeBoolResponse);
  rpc SetTrigAttributeDouble(SetTrigAttributeDoubleRequest) returns (SetTrigAttributeDoubleResponse);
  rpc SetTrigAttributeDoubleArray(SetTrigAttributeDoubleArrayRequest) returns (SetTrigAttributeDoubleArrayResponse);
  rpc SetTrigAttributeInt32(SetTrigAttributeInt32Request) returns (SetTrigAttributeInt32Response);
  rpc SetTrigAttributeInt32Array(SetTrigAttributeInt32ArrayRequest) returns (SetTrigAttributeInt32ArrayResponse);
  rpc SetTrigAttributeString(SetTrigAttributeStringRequest) returns (SetTrigAttributeStringResponse);
  rpc SetTrigAttributeTimestamp(SetTrigAttributeTimestampRequest) returns (SetTrigAttributeTimestampResponse);
  rpc SetTrigAttributeUInt32(SetTrigAttributeUInt32Request) returns (SetTrigAttributeUInt32Response);
  rpc SetWatchdogAttributeBool(SetWatchdogAttributeBoolRequest) returns (SetWatchdogAttributeBoolResponse);
  rpc SetWatchdogAttributeDouble(SetWatchdogAttributeDoubleRequest) returns (SetWatchdogAttributeDoubleResponse);
  rpc SetWatchdogAttributeInt32(SetWatchdogAttributeInt32Request) returns (SetWatchdogAttributeInt32Response);
  rpc SetWatchdogAttributeString(SetWatchdogAttributeStringRequest) returns (SetWatchdogAttributeStringResponse);
  rpc SetWriteAttributeBool(SetWriteAttributeBoolRequest) returns (SetWriteAttributeBoolResponse);
  rpc SetWriteAttributeDouble(SetWriteAttributeDoubleRequest) returns (SetWriteAttributeDoubleResponse);
  rpc SetWriteAttributeInt32(SetWriteAttributeInt32Request) returns (SetWriteAttributeInt32Response);
  rpc SetWriteAttributeString(SetWriteAttributeStringRequest) returns (SetWriteAttributeStringResponse);
  rpc SetWriteAttributeUInt32(SetWriteAttributeUInt32Request) returns (SetWriteAttributeUInt32Response);
  rpc SetWriteAttributeUInt64(SetWriteAttributeUInt64Request) returns (SetWriteAttributeUInt64Response);
  rpc StartNewFile(StartNewFileRequest) returns (StartNewFileResponse);
  rpc StartTask(StartTaskRequest) returns (StartTaskResponse);
  rpc StopTask(StopTaskRequest) returns (StopTaskResponse);
  rpc TaskControl(TaskControlRequest) returns (TaskControlResponse);
  rpc TristateOutputTerm(TristateOutputTermRequest) returns (TristateOutputTermResponse);
  rpc UnregisterDoneEvent(UnregisterDoneEventRequest) returns (UnregisterDoneEventResponse);
  rpc UnregisterEveryNSamplesEvent(UnregisterEveryNSamplesEventRequest) returns (UnregisterEveryNSamplesEventResponse);
  rpc UnregisterSignalEvent(UnregisterSignalEventRequest) returns (UnregisterSignalEventResponse);
  rpc UnreserveNetworkDevice(UnreserveNetworkDeviceRequest) returns (UnreserveNetworkDeviceResponse);
  rpc WaitForNextSampleClock(WaitForNextSampleClockRequest) returns (WaitForNextSampleClockResponse);
  rpc BeginWaitForNextSampleClock(BeginWaitForNextSampleClockRequest) returns (BeginWaitForNextSampleClockResponse);
  rpc WaitForValidTimestamp(WaitForValidTimestampRequest) returns (WaitForValidTimestampResponse);
  rpc WaitUntilTaskDone(WaitUntilTaskDoneRequest) returns (WaitUntilTaskDoneResponse);
  rpc WriteAnalogF64(WriteAnalogF64Request) returns (WriteAnalogF64Response);
  rpc BeginWriteAnalogF64(BeginWriteAnalogF64Request) returns (BeginWriteAnalogF64Response);
  rpc WriteAnalogScalarF64(WriteAnalogScalarF64Request) returns (WriteAnalogScalarF64Response);
  rpc BeginWriteAnalogScalarF64(BeginWriteAnalogScalarF64Request) returns (BeginWriteAnalogScalarF64Response);
  rpc WriteBinaryI16(WriteBinaryI16Request) returns (WriteBinaryI16Response);
  rpc BeginWriteBinaryI16(BeginWriteBinaryI16Request) returns (BeginWriteBinaryI16Response);
  rpc WriteBinaryI32(WriteBinaryI32Request) returns (WriteBinaryI32Response);
  rpc BeginWriteBinaryI32(BeginWriteBinaryI32Request) returns (BeginWriteBinaryI32Response);
  rpc WriteBinaryU16(WriteBinaryU16Request) returns (WriteBinaryU16Response);
  rpc BeginWriteBinaryU16(BeginWriteBinaryU16Request) returns (BeginWriteBinaryU16Response);
  rpc WriteBinaryU32(WriteBinaryU32Request) returns (WriteBinaryU32Response);
  rpc BeginWriteBinaryU32(BeginWriteBinaryU32Request) returns (BeginWriteBinaryU32Response);
  rpc WriteCtrFreq(WriteCtrFreqRequest) returns (WriteCtrFreqResponse);
  rpc BeginWriteCtrFreq(BeginWriteCtrFreqRequest) returns (BeginWriteCtrFreqResponse);
  rpc WriteCtrFreqScalar(WriteCtrFreqScalarRequest) returns (WriteCtrFreqScalarResponse);
  rpc BeginWriteCtrFreqScalar(BeginWriteCtrFreqScalarRequest) returns (BeginWriteCtrFreqScalarResponse);
  rpc WriteCtrTicks(WriteCtrTicksRequest) returns (WriteCtrTicksResponse);
  rpc BeginWriteCtrTicks(BeginWriteCtrTicksRequest) returns (BeginWriteCtrTicksResponse);
  rpc WriteCtrTicksScalar(WriteCtrTicksScalarRequest) returns (WriteCtrTicksScalarResponse);
  rpc BeginWriteCtrTicksScalar(BeginWriteCtrTicksScalarRequest) returns (BeginWriteCtrTicksScalarResponse);
  rpc WriteCtrTime(WriteCtrTimeRequest) returns (WriteCtrTimeResponse);
  rpc BeginWriteCtrTime(BeginWriteCtrTimeRequest) returns (BeginWriteCtrTimeResponse);
  rpc WriteCtrTimeScalar(WriteCtrTimeScalarRequest) returns (WriteCtrTimeScalarResponse);
  rpc BeginWriteCtrTimeScalar(BeginWriteCtrTimeScalarRequest) returns (BeginWriteCtrTimeScalarResponse);
  rpc WriteDigitalLines(WriteDigitalLinesRequest) returns (WriteDigitalLinesResponse);
  rpc BeginWriteDigitalLines(BeginWriteDigitalLinesRequest) returns (BeginWriteDigitalLinesResponse);
  rpc WriteDigitalScalarU32(WriteDigitalScalarU32Request) returns (WriteDigitalScalarU32Response);
  rpc BeginWriteDigitalScalarU32(BeginWriteDigitalScalarU32Request) returns (BeginWriteDigitalScalarU32Response);
  rpc WriteDigitalU16(WriteDigitalU16Request) returns (WriteDigitalU16Response);
  rpc BeginWriteDigitalU16(BeginWriteDigitalU16Request) returns (BeginWriteDigitalU16Response);
  rpc WriteDigitalU32(WriteDigitalU32Request) returns (WriteDigitalU32Response);
  rpc BeginWriteDigitalU32(BeginWriteDigitalU32Request) returns (BeginWriteDigitalU32Response);
  rpc WriteDigitalU8(WriteDigitalU8Request) returns (WriteDigitalU8Response);
  rpc BeginWriteDigitalU8(BeginWriteDigitalU8Request) returns (BeginWriteDigitalU8Response);
  rpc WriteIDPinMemory(WriteIDPinMemoryRequest) returns (WriteIDPinMemoryResponse);
  rpc WriteRaw(WriteRawRequest) returns (WriteRawResponse);
  rpc BeginWriteRaw(BeginWriteRawRequest) returns (BeginWriteRawResponse);
  rpc WriteToTEDSFromArray(WriteToTEDSFromArrayRequest) returns (WriteToTEDSFromArrayResponse);
  rpc WriteToTEDSFromFile(WriteToTEDSFromFileRequest) returns (WriteToTEDSFromFileResponse);
  rpc ReadAnalogWaveforms(ReadAnalogWaveformsRequest) returns (ReadAnalogWaveformsResponse);
  rpc ReadDigitalWaveforms(ReadDigitalWaveformsRequest) returns (ReadDigitalWaveformsResponse);
  rpc WriteAnalogWaveforms(WriteAnalogWaveformsRequest) returns (WriteAnalogWaveformsResponse);
  rpc WriteDigitalWaveforms(WriteDigitalWaveformsRequest) returns (WriteDigitalWaveformsResponse);
}

enum BufferUInt32Attribute {
  BUFFER_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  BUFFER_ATTRIBUTE_INPUT_BUF_SIZE = 6252;
  BUFFER_ATTRIBUTE_OUTPUT_BUF_SIZE = 6253;
  BUFFER_ATTRIBUTE_INPUT_ONBRD_BUF_SIZE = 8970;
  BUFFER_ATTRIBUTE_OUTPUT_ONBRD_BUF_SIZE = 8971;
}

enum BufferResetAttribute {
  BUFFER_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  BUFFER_RESET_ATTRIBUTE_INPUT_BUF_SIZE = 6252;
  BUFFER_RESET_ATTRIBUTE_OUTPUT_BUF_SIZE = 6253;
  BUFFER_RESET_ATTRIBUTE_OUTPUT_ONBRD_BUF_SIZE = 8971;
}

enum CalibrationInfoBoolAttribute {
  CALIBRATIONINFO_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  CALIBRATIONINFO_ATTRIBUTE_SELF_CAL_SUPPORTED = 6240;
}

enum CalibrationInfoStringAttribute {
  CALIBRATIONINFO_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  CALIBRATIONINFO_ATTRIBUTE_CAL_USER_DEFINED_INFO = 6241;
}

enum CalibrationInfoDoubleAttribute {
  CALIBRATIONINFO_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  CALIBRATIONINFO_ATTRIBUTE_SELF_CAL_LAST_TEMP = 6244;
  CALIBRATIONINFO_ATTRIBUTE_EXT_CAL_LAST_TEMP = 6247;
  CALIBRATIONINFO_ATTRIBUTE_CAL_DEV_TEMP = 8763;
}

enum CalibrationInfoUInt32Attribute {
  CALIBRATIONINFO_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  CALIBRATIONINFO_ATTRIBUTE_EXT_CAL_RECOMMENDED_INTERVAL = 6248;
  CALIBRATIONINFO_ATTRIBUTE_CAL_USER_DEFINED_INFO_MAX_SIZE = 6428;
  CALIBRATIONINFO_ATTRIBUTE_CAL_ACC_CONNECTION_COUNT = 12267;
  CALIBRATIONINFO_ATTRIBUTE_CAL_RECOMMENDED_ACC_CONNECTION_COUNT_LIMIT = 12268;
}

enum ChannelInt32Attribute {
  CHANNEL_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  CHANNEL_ATTRIBUTE_AI_RAW_SAMP_JUSTIFICATION = 80;
  CHANNEL_ATTRIBUTE_AI_COUPLING = 100;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_CFG = 135;
  CHANNEL_ATTRIBUTE_AO_DAC_REF_SRC = 306;
  CHANNEL_ATTRIBUTE_AO_DATA_XFER_MECH = 308;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_ACTIVE_EDGE = 322;
  CHANNEL_ATTRIBUTE_CI_FREQ_MEAS_METH = 324;
  CHANNEL_ATTRIBUTE_CI_OUTPUT_STATE = 329;
  CHANNEL_ATTRIBUTE_CI_DATA_XFER_MECH = 512;
  CHANNEL_ATTRIBUTE_CO_OUTPUT_STATE = 660;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_ACTIVE_EDGE = 833;
  CHANNEL_ATTRIBUTE_AI_ACCEL_UNITS = 1651;
  CHANNEL_ATTRIBUTE_AI_MEAS_TYPE = 1685;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIR = 1686;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_ACTIVE_EDGE = 1687;
  CHANNEL_ATTRIBUTE_AI_CURRENT_UNITS = 1793;
  CHANNEL_ATTRIBUTE_CI_FREQ_STARTING_EDGE = 1945;
  CHANNEL_ATTRIBUTE_AI_FREQ_UNITS = 2054;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_UNITS = 2083;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_STARTING_EDGE = 2085;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_EDGE = 2099;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_EDGE = 2100;
  CHANNEL_ATTRIBUTE_CI_PERIOD_STARTING_EDGE = 2130;
  CHANNEL_ATTRIBUTE_AI_RVDT_UNITS = 2167;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INDEX_PHASE = 2185;
  CHANNEL_ATTRIBUTE_AI_LVDT_UNITS = 2320;
  CHANNEL_ATTRIBUTE_AI_RESISTANCE_UNITS = 2389;
  CHANNEL_ATTRIBUTE_AI_STRAIN_UNITS = 2433;
  CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_CFG = 2434;
  CHANNEL_ATTRIBUTE_AI_RTD_TYPE = 4146;
  CHANNEL_ATTRIBUTE_AI_TEMP_UNITS = 4147;
  CHANNEL_ATTRIBUTE_AI_THRMCPL_CJC_SRC = 4149;
  CHANNEL_ATTRIBUTE_AI_THRMCPL_TYPE = 4176;
  CHANNEL_ATTRIBUTE_CI_GPS_SYNC_METHOD = 4242;
  CHANNEL_ATTRIBUTE_AI_VOLTAGE_UNITS = 4244;
  CHANNEL_ATTRIBUTE_AI_TERM_CFG = 4247;
  CHANNEL_ATTRIBUTE_AO_OUTPUT_TYPE = 4360;
  CHANNEL_ATTRIBUTE_AO_CURRENT_UNITS = 4361;
  CHANNEL_ATTRIBUTE_DO_OUTPUT_DRIVE_TYPE = 4407;
  CHANNEL_ATTRIBUTE_CO_PULSE_IDLE_STATE = 4464;
  CHANNEL_ATTRIBUTE_AO_VOLTAGE_UNITS = 4484;
  CHANNEL_ATTRIBUTE_AI_SOUND_PRESSURE_UNITS = 5416;
  CHANNEL_ATTRIBUTE_AI_AUTO_ZERO_MODE = 5984;
  CHANNEL_ATTRIBUTE_AI_RESOLUTION_UNITS = 5988;
  CHANNEL_ATTRIBUTE_AI_VOLTAGE_ACRMS_UNITS = 6114;
  CHANNEL_ATTRIBUTE_AI_CURRENT_ACRMS_UNITS = 6115;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_BALANCE_COARSE_POT = 6129;
  CHANNEL_ATTRIBUTE_AI_CURRENT_SHUNT_LOC = 6130;
  CHANNEL_ATTRIBUTE_AI_EXCIT_SRC = 6132;
  CHANNEL_ATTRIBUTE_AI_EXCIT_VOLTAGE_OR_CURRENT = 6134;
  CHANNEL_ATTRIBUTE_AI_EXCIT_D_COR_AC = 6139;
  CHANNEL_ATTRIBUTE_AI_HIGHPASS_TYPE = 6152;
  CHANNEL_ATTRIBUTE_AI_BANDPASS_TYPE = 6157;
  CHANNEL_ATTRIBUTE_AI_NOTCH_TYPE = 6161;
  CHANNEL_ATTRIBUTE_AI_DATA_XFER_MECH = 6177;
  CHANNEL_ATTRIBUTE_AO_RESOLUTION_UNITS = 6187;
  CHANNEL_ATTRIBUTE_AO_DATA_XFER_REQ_COND = 6204;
  CHANNEL_ATTRIBUTE_CHAN_TYPE = 6271;
  CHANNEL_ATTRIBUTE_AI_RESISTANCE_CFG = 6273;
  CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_CLK_SRC = 6276;
  CHANNEL_ATTRIBUTE_AI_DATA_XFER_REQ_COND = 6283;
  CHANNEL_ATTRIBUTE_AO_TERM_CFG = 6286;
  CHANNEL_ATTRIBUTE_CI_MEAS_TYPE = 6304;
  CHANNEL_ATTRIBUTE_CI_FREQ_UNITS = 6305;
  CHANNEL_ATTRIBUTE_CI_PERIOD_UNITS = 6307;
  CHANNEL_ATTRIBUTE_CI_ANG_ENCODER_UNITS = 6310;
  CHANNEL_ATTRIBUTE_CI_LIN_ENCODER_UNITS = 6313;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_UNITS = 6316;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_UNITS = 6319;
  CHANNEL_ATTRIBUTE_CO_OUTPUT_TYPE = 6325;
  CHANNEL_ATTRIBUTE_AI_AC_EXCIT_WIRE_MODE = 6349;
  CHANNEL_ATTRIBUTE_CO_PULSE_FREQ_UNITS = 6357;
  CHANNEL_ATTRIBUTE_CO_PULSE_TIME_UNITS = 6358;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_BALANCE_FINE_POT = 6388;
  CHANNEL_ATTRIBUTE_CI_PERIOD_MEAS_METH = 6444;
  CHANNEL_ATTRIBUTE_AI_LVDT_SENSITIVITY_UNITS = 8602;
  CHANNEL_ATTRIBUTE_AI_RVDT_SENSITIVITY_UNITS = 8603;
  CHANNEL_ATTRIBUTE_AI_ACCEL_SENSITIVITY_UNITS = 8604;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SELECT = 8661;
  CHANNEL_ATTRIBUTE_CI_ENCODER_DECODING_TYPE = 8678;
  CHANNEL_ATTRIBUTE_AO_IDLE_OUTPUT_BEHAVIOR = 8768;
  CHANNEL_ATTRIBUTE_AO_DAC_OFFSET_SRC = 8787;
  CHANNEL_ATTRIBUTE_DI_DATA_XFER_MECH = 8803;
  CHANNEL_ATTRIBUTE_DI_DATA_XFER_REQ_COND = 8804;
  CHANNEL_ATTRIBUTE_DO_DATA_XFER_MECH = 8806;
  CHANNEL_ATTRIBUTE_DO_DATA_XFER_REQ_COND = 8807;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_SCALE_TYPE = 8860;
  CHANNEL_ATTRIBUTE_CI_TIMESTAMP_UNITS = 8883;
  CHANNEL_ATTRIBUTE_AI_RAW_DATA_COMPRESSION_TYPE = 8920;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_STARTING_EDGE = 8958;
  CHANNEL_ATTRIBUTE_DI_ACQUIRE_ON = 10598;
  CHANNEL_ATTRIBUTE_DO_LINE_STATES_PAUSED_STATE = 10599;
  CHANNEL_ATTRIBUTE_DO_LINE_STATES_DONE_STATE = 10600;
  CHANNEL_ATTRIBUTE_DO_GENERATE_ON = 10601;
  CHANNEL_ATTRIBUTE_DI_LOGIC_FAMILY = 10605;
  CHANNEL_ATTRIBUTE_DO_LOGIC_FAMILY = 10606;
  CHANNEL_ATTRIBUTE_DO_LINE_STATES_START_STATE = 10610;
  CHANNEL_ATTRIBUTE_AI_THRMCPL_SCALE_TYPE = 10704;
  CHANNEL_ATTRIBUTE_CO_CONSTRAINED_GEN_MODE = 10738;
  CHANNEL_ATTRIBUTE_AI_ADC_TIMING_MODE = 10745;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_TYPE = 10776;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_MODULATION_TYPE = 10786;
  CHANNEL_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS = 10943;
  CHANNEL_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_UNITS = 10944;
  CHANNEL_ATTRIBUTE_CO_DATA_XFER_MECH = 11980;
  CHANNEL_ATTRIBUTE_CO_DATA_XFER_REQ_COND = 11981;
  CHANNEL_ATTRIBUTE_CI_DATA_XFER_REQ_COND = 12027;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_START_EDGE = 12037;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_UNITS = 12043;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_START_EDGE = 12045;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_UNITS = 12051;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_START_EDGE = 12053;
  CHANNEL_ATTRIBUTE_AI_FORCE_UNITS = 12149;
  CHANNEL_ATTRIBUTE_AI_PRESSURE_UNITS = 12150;
  CHANNEL_ATTRIBUTE_AI_TORQUE_UNITS = 12151;
  CHANNEL_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS = 12162;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_ELECTRICAL_UNITS = 12167;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_PHYSICAL_UNITS = 12168;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SCALE_TYPE = 12169;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_UNITS = 12178;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ACTIVE_EDGE = 12210;
  CHANNEL_ATTRIBUTE_AI_VELOCITY_UNITS = 12276;
  CHANNEL_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS = 12279;
  CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ROSETTE_MEAS_TYPE = 12285;
  CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ROSETTE_TYPE = 12286;
  CHANNEL_ATTRIBUTE_CI_TIMESTAMP_EDGE = 12346;
  CHANNEL_ATTRIBUTE_CI_TIMESTAMP_TIMESCALE = 12347;
  CHANNEL_ATTRIBUTE_NAV_MEAS_TYPE = 12349;
  CHANNEL_ATTRIBUTE_NAV_ALT_UNITS = 12350;
  CHANNEL_ATTRIBUTE_NAV_LAT_UNITS = 12351;
  CHANNEL_ATTRIBUTE_NAV_LONG_UNITS = 12352;
  CHANNEL_ATTRIBUTE_NAV_SPEED_OVER_GROUND_UNITS = 12353;
  CHANNEL_ATTRIBUTE_NAV_TRACK_UNITS = 12354;
  CHANNEL_ATTRIBUTE_NAV_VERT_VELOCITY_UNITS = 12355;
  CHANNEL_ATTRIBUTE_NAV_TIMESTAMP_UNITS = 12356;
  CHANNEL_ATTRIBUTE_NAV_TIMESTAMP_TIMESCALE = 12357;
  CHANNEL_ATTRIBUTE_AI_FILTER_DELAY_UNITS = 12401;
  CHANNEL_ATTRIBUTE_AO_FILTER_DELAY_UNITS = 12406;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_STARTING_EDGE = 12434;
  CHANNEL_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_BEHAVIOR = 12435;
  CHANNEL_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_SENTINEL_VAL = 12436;
  CHANNEL_ATTRIBUTE_CI_FREQ_TERM_CFG = 12439;
  CHANNEL_ATTRIBUTE_CI_FREQ_LOGIC_LVL_BEHAVIOR = 12440;
  CHANNEL_ATTRIBUTE_CI_PERIOD_TERM_CFG = 12441;
  CHANNEL_ATTRIBUTE_CI_PERIOD_LOGIC_LVL_BEHAVIOR = 12442;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_TERM_CFG = 12443;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_LOGIC_LVL_BEHAVIOR = 12444;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_TERM_CFG = 12445;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_LOGIC_LVL_BEHAVIOR = 12446;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM_CFG = 12447;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_LOGIC_LVL_BEHAVIOR = 12448;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_TERM_CFG = 12449;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_LOGIC_LVL_BEHAVIOR = 12450;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM_CFG = 12451;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR = 12452;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM_CFG = 12453;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR = 12454;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM_CFG = 12455;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_LOGIC_LVL_BEHAVIOR = 12456;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_TERM_CFG = 12457;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_LOGIC_LVL_BEHAVIOR = 12458;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM_CFG = 12459;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_LOGIC_LVL_BEHAVIOR = 12460;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM_CFG = 12461;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_LOGIC_LVL_BEHAVIOR = 12462;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_TERM_CFG = 12463;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_LOGIC_LVL_BEHAVIOR = 12464;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_TERM_CFG = 12465;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_LOGIC_LVL_BEHAVIOR = 12466;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_TERM_CFG = 12467;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_LOGIC_LVL_BEHAVIOR = 12468;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_TERM_CFG = 12469;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_LOGIC_LVL_BEHAVIOR = 12470;
  CHANNEL_ATTRIBUTE_AI_EXCIT_IDLE_OUTPUT_BEHAVIOR = 12472;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_TYPE = 12478;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_RESPONSE = 12479;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_SRC = 12490;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_UNITS = 12504;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_UNITS = 12506;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_DECODING_TYPE = 12508;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM_CFG = 12510;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR = 12511;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM_CFG = 12517;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR = 12518;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM_CFG = 12527;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_LOGIC_LVL_BEHAVIOR = 12528;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_WHEN = 12533;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC = 12535;
  CHANNEL_ATTRIBUTE_AI_EXCIT_SENSE = 12541;
  CHANNEL_ATTRIBUTE_AI_CHARGE_UNITS = 12562;
  CHANNEL_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY_UNITS = 12564;
  CHANNEL_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY_UNITS = 12566;
  CHANNEL_ATTRIBUTE_CHAN_SYNC_UNLOCK_BEHAVIOR = 12604;
  CHANNEL_ATTRIBUTE_AI_SENSOR_POWER_CFG = 12650;
  CHANNEL_ATTRIBUTE_AI_SENSOR_POWER_TYPE = 12651;
  CHANNEL_ATTRIBUTE_AI_FILTER_RESPONSE = 12661;
  CHANNEL_ATTRIBUTE_CI_FILTER_RESPONSE = 12729;
  CHANNEL_ATTRIBUTE_CI_FILTER_DELAY_UNITS = 12732;
  CHANNEL_ATTRIBUTE_PWR_OUTPUT_STATE = 12759;
  CHANNEL_ATTRIBUTE_PWR_IDLE_OUTPUT_BEHAVIOR = 12760;
  CHANNEL_ATTRIBUTE_PWR_REMOTE_SENSE = 12763;
  CHANNEL_ATTRIBUTE_AI_POWER_UNITS = 12780;
}

enum ChannelDoubleAttribute {
  CHANNEL_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  CHANNEL_ATTRIBUTE_AI_IMPEDANCE = 98;
  CHANNEL_ATTRIBUTE_AI_AC_EXCIT_FREQ = 257;
  CHANNEL_ATTRIBUTE_AO_GAIN = 280;
  CHANNEL_ATTRIBUTE_AO_LOAD_IMPEDANCE = 289;
  CHANNEL_ATTRIBUTE_CI_FREQ_MEAS_TIME = 325;
  CHANNEL_ATTRIBUTE_CO_PULSE_FREQ_INITIAL_DELAY = 665;
  CHANNEL_ATTRIBUTE_AI_ACCEL_SENSITIVITY = 1682;
  CHANNEL_ATTRIBUTE_AI_FREQ_HYST = 2068;
  CHANNEL_ATTRIBUTE_AI_FREQ_THRESH_VOLTAGE = 2069;
  CHANNEL_ATTRIBUTE_CI_ANG_ENCODER_INITIAL_ANGLE = 2177;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INDEX_VAL = 2184;
  CHANNEL_ATTRIBUTE_AI_RVDT_SENSITIVITY = 2307;
  CHANNEL_ATTRIBUTE_CI_LIN_ENCODER_DIST_PER_PULSE = 2321;
  CHANNEL_ATTRIBUTE_CI_LIN_ENCODER_INITIAL_POS = 2325;
  CHANNEL_ATTRIBUTE_AI_LVDT_SENSITIVITY = 2361;
  CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_GAGE_FACTOR = 2452;
  CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_POISSON_RATIO = 2456;
  CHANNEL_ATTRIBUTE_AI_RTD_A = 4112;
  CHANNEL_ATTRIBUTE_AI_RTD_B = 4113;
  CHANNEL_ATTRIBUTE_AI_RTD_C = 4115;
  CHANNEL_ATTRIBUTE_AI_RTD_R0 = 4144;
  CHANNEL_ATTRIBUTE_AI_THRMCPL_CJC_VAL = 4150;
  CHANNEL_ATTRIBUTE_AI_THRMSTR_R1 = 4193;
  CHANNEL_ATTRIBUTE_CO_PULSE_DUTY_CYC = 4470;
  CHANNEL_ATTRIBUTE_CO_PULSE_FREQ = 4472;
  CHANNEL_ATTRIBUTE_AO_MAX = 4486;
  CHANNEL_ATTRIBUTE_AO_MIN = 4487;
  CHANNEL_ATTRIBUTE_AO_OUTPUT_IMPEDANCE = 5264;
  CHANNEL_ATTRIBUTE_AI_MICROPHONE_SENSITIVITY = 5430;
  CHANNEL_ATTRIBUTE_AI_RESOLUTION = 5989;
  CHANNEL_ATTRIBUTE_AI_MAX = 6109;
  CHANNEL_ATTRIBUTE_AI_MIN = 6110;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_NOM_RESISTANCE = 6124;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_INITIAL_VOLTAGE = 6125;
  CHANNEL_ATTRIBUTE_AI_LEAD_WIRE_RESISTANCE = 6126;
  CHANNEL_ATTRIBUTE_AI_CURRENT_SHUNT_RESISTANCE = 6131;
  CHANNEL_ATTRIBUTE_AI_EXCIT_VAL = 6133;
  CHANNEL_ATTRIBUTE_AI_ATTEN = 6145;
  CHANNEL_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ = 6147;
  CHANNEL_ATTRIBUTE_AI_HIGHPASS_CUTOFF_FREQ = 6151;
  CHANNEL_ATTRIBUTE_AI_BANDPASS_CENTER_FREQ = 6156;
  CHANNEL_ATTRIBUTE_AI_BANDPASS_WIDTH = 6158;
  CHANNEL_ATTRIBUTE_AI_NOTCH_CENTER_FREQ = 6160;
  CHANNEL_ATTRIBUTE_AI_NOTCH_WIDTH = 6162;
  CHANNEL_ATTRIBUTE_AI_RNG_HIGH = 6165;
  CHANNEL_ATTRIBUTE_AI_RNG_LOW = 6166;
  CHANNEL_ATTRIBUTE_AI_GAIN = 6168;
  CHANNEL_ATTRIBUTE_AO_RESOLUTION = 6188;
  CHANNEL_ATTRIBUTE_AO_DAC_RNG_LOW = 6189;
  CHANNEL_ATTRIBUTE_AO_DAC_RNG_HIGH = 6190;
  CHANNEL_ATTRIBUTE_AO_DAC_REF_VAL = 6194;
  CHANNEL_ATTRIBUTE_AI_EXCIT_ACTUAL_VAL = 6275;
  CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_FREQ = 6277;
  CHANNEL_ATTRIBUTE_CI_MAX = 6300;
  CHANNEL_ATTRIBUTE_CI_MIN = 6301;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_RATE = 6322;
  CHANNEL_ATTRIBUTE_CO_PULSE_HIGH_TIME = 6330;
  CHANNEL_ATTRIBUTE_CO_PULSE_LOW_TIME = 6331;
  CHANNEL_ATTRIBUTE_CO_PULSE_TIME_INITIAL_DELAY = 6332;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_RATE = 6338;
  CHANNEL_ATTRIBUTE_AI_THRMSTR_A = 6345;
  CHANNEL_ATTRIBUTE_AI_THRMSTR_C = 6346;
  CHANNEL_ATTRIBUTE_AI_THRMSTR_B = 6347;
  CHANNEL_ATTRIBUTE_CI_PERIOD_MEAS_TIME = 6445;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_GAIN_ADJUST = 6463;
  CHANNEL_ATTRIBUTE_DI_DIG_FLTR_MIN_PULSE_WIDTH = 8663;
  CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_MIN_PULSE_WIDTH = 8680;
  CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_RATE = 8682;
  CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH = 8685;
  CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_RATE = 8687;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_MIN_PULSE_WIDTH = 8690;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_RATE = 8692;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_MIN_PULSE_WIDTH = 8695;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_RATE = 8697;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 8700;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE = 8702;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 8705;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE = 8707;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 8710;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_RATE = 8712;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_MIN_PULSE_WIDTH = 8715;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_RATE = 8717;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_MIN_PULSE_WIDTH = 8720;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_RATE = 8722;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_MIN_PULSE_WIDTH = 8725;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_RATE = 8727;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH = 8730;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_RATE = 8732;
  CHANNEL_ATTRIBUTE_AI_SOUND_PRESSURE_MAX_SOUND_PRESSURE_LVL = 8762;
  CHANNEL_ATTRIBUTE_AO_DAC_OFFSET_VAL = 8789;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH = 8818;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE = 8820;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH = 8823;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE = 8825;
  CHANNEL_ATTRIBUTE_AI_VOLTAGE_DB_REF = 10672;
  CHANNEL_ATTRIBUTE_AI_SOUND_PRESSURE_DB_REF = 10673;
  CHANNEL_ATTRIBUTE_AI_ACCEL_DB_REF = 10674;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_FREQ = 10777;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_AMPLITUDE = 10778;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_OFFSET = 10779;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_SQUARE_DUTY_CYCLE = 10780;
  CHANNEL_ATTRIBUTE_AO_VOLTAGE_CURRENT_LIMIT = 10781;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_FM_DEVIATION = 10787;
  CHANNEL_ATTRIBUTE_DO_OVERCURRENT_LIMIT = 10885;
  CHANNEL_ATTRIBUTE_DO_OVERCURRENT_REENABLE_PERIOD = 10887;
  CHANNEL_ATTRIBUTE_AI_PROBE_ATTEN = 10888;
  CHANNEL_ATTRIBUTE_AI_DC_OFFSET = 10889;
  CHANNEL_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY = 10942;
  CHANNEL_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_RATE = 11989;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_MIN_PULSE_WIDTH = 12039;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_RATE = 12041;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_MIN_PULSE_WIDTH = 12047;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_RATE = 12049;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_MIN_PULSE_WIDTH = 12055;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_RATE = 12057;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_RESISTANCE = 12152;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_ACTUAL_RESISTANCE = 12153;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_RESISTANCE = 12154;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_ACTUAL_RESISTANCE = 12155;
  CHANNEL_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY = 12161;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_INITIAL_RATIO = 12166;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_ELECTRICAL_VAL = 12170;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_PHYSICAL_VAL = 12171;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_ELECTRICAL_VAL = 12172;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_PHYSICAL_VAL = 12173;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_MIN_PULSE_WIDTH = 12212;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_RATE = 12214;
  CHANNEL_ATTRIBUTE_AI_THRMCPL_LEAD_OFFSET_VOLTAGE = 12216;
  CHANNEL_ATTRIBUTE_AI_FILTER_DELAY = 12269;
  CHANNEL_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_DB_REF = 12277;
  CHANNEL_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY = 12278;
  CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ORIENTATION = 12284;
  CHANNEL_ATTRIBUTE_AO_FILTER_DELAY_ADJUSTMENT = 12402;
  CHANNEL_ATTRIBUTE_AI_FILTER_DELAY_ADJUSTMENT = 12404;
  CHANNEL_ATTRIBUTE_AO_FILTER_DELAY = 12405;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_MIN_PULSE_WIDTH = 12431;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_RATE = 12433;
  CHANNEL_ATTRIBUTE_CI_MAX_MEAS_PERIOD = 12437;
  CHANNEL_ATTRIBUTE_CI_THRESH_VOLTAGE = 12471;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ = 12481;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_HIGHPASS_CUTOFF_FREQ = 12482;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_CENTER_FREQ = 12483;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_WIDTH = 12484;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_NOTCH_CENTER_FREQ = 12485;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_NOTCH_WIDTH = 12486;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_DIST_PER_PULSE = 12507;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 12513;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE = 12515;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 12520;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE = 12522;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_MEAS_TIME = 12523;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_MIN_PULSE_WIDTH = 12530;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_RATE = 12532;
  CHANNEL_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY = 12563;
  CHANNEL_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY = 12565;
  CHANNEL_ATTRIBUTE_AI_DATA_XFER_MAX_RATE = 12567;
  CHANNEL_ATTRIBUTE_AI_SENSOR_POWER_VOLTAGE = 12649;
  CHANNEL_ATTRIBUTE_AI_FILTER_FREQ = 12660;
  CHANNEL_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_UPPER_LIMIT = 12684;
  CHANNEL_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_LOWER_LIMIT = 12685;
  CHANNEL_ATTRIBUTE_CI_FREQ_THRESH_VOLTAGE = 12715;
  CHANNEL_ATTRIBUTE_CI_FREQ_HYST = 12716;
  CHANNEL_ATTRIBUTE_CI_PERIOD_THRESH_VOLTAGE = 12717;
  CHANNEL_ATTRIBUTE_CI_PERIOD_HYST = 12718;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_THRESH_VOLTAGE = 12719;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_HYST = 12720;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_THRESH_VOLTAGE = 12721;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_HYST = 12722;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_THRESH_VOLTAGE = 12723;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_HYST = 12724;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_THRESH_VOLTAGE = 12725;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_HYST = 12726;
  CHANNEL_ATTRIBUTE_CI_FILTER_FREQ = 12728;
  CHANNEL_ATTRIBUTE_CI_FILTER_DELAY = 12731;
  CHANNEL_ATTRIBUTE_AO_FUNC_GEN_START_PHASE = 12740;
  CHANNEL_ATTRIBUTE_AO_COMMON_MODE_OFFSET = 12748;
  CHANNEL_ATTRIBUTE_PWR_VOLTAGE_SETPOINT = 12756;
  CHANNEL_ATTRIBUTE_PWR_CURRENT_SETPOINT = 12757;
  CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MAX = 12781;
  CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MIN = 12782;
  CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MAX = 12783;
  CHANNEL_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MIN = 12784;
}

enum ChannelResetAttribute {
  CHANNEL_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  CHANNEL_RESET_ATTRIBUTE_AI_IMPEDANCE = 98;
  CHANNEL_RESET_ATTRIBUTE_AI_COUPLING = 100;
  CHANNEL_RESET_ATTRIBUTE_AI_DITHER_ENABLE = 104;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_CFG = 135;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_ENABLE = 148;
  CHANNEL_RESET_ATTRIBUTE_AI_AC_EXCIT_FREQ = 257;
  CHANNEL_RESET_ATTRIBUTE_AI_AC_EXCIT_SYNC_ENABLE = 258;
  CHANNEL_RESET_ATTRIBUTE_AO_GAIN = 280;
  CHANNEL_RESET_ATTRIBUTE_AO_LOAD_IMPEDANCE = 289;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_CONN_TO_GND = 304;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_SRC = 306;
  CHANNEL_RESET_ATTRIBUTE_AO_REGLITCH_ENABLE = 307;
  CHANNEL_RESET_ATTRIBUTE_AO_DATA_XFER_MECH = 308;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_ACTIVE_EDGE = 322;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_SRC = 323;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_MEAS_METH = 324;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_MEAS_TIME = 325;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIV = 327;
  CHANNEL_RESET_ATTRIBUTE_CI_DATA_XFER_MECH = 512;
  CHANNEL_RESET_ATTRIBUTE_CO_AUTO_INCR_CNT = 661;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TICKS_INITIAL_DELAY = 664;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_FREQ_INITIAL_DELAY = 665;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_SRC = 825;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_ACTIVE_EDGE = 833;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_UNITS = 1651;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_SENSITIVITY = 1682;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIR = 1686;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_ACTIVE_EDGE = 1687;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_INITIAL_CNT = 1688;
  CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_UNITS = 1793;
  CHANNEL_RESET_ATTRIBUTE_DI_INVERT_LINES = 1939;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_STARTING_EDGE = 1945;
  CHANNEL_RESET_ATTRIBUTE_AI_FREQ_UNITS = 2054;
  CHANNEL_RESET_ATTRIBUTE_AI_FREQ_HYST = 2068;
  CHANNEL_RESET_ATTRIBUTE_AI_FREQ_THRESH_VOLTAGE = 2069;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_UNITS = 2083;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_STARTING_EDGE = 2085;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_EDGE = 2099;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_EDGE = 2100;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_STARTING_EDGE = 2130;
  CHANNEL_RESET_ATTRIBUTE_CI_ANG_ENCODER_PULSES_PER_REV = 2165;
  CHANNEL_RESET_ATTRIBUTE_AI_RVDT_UNITS = 2167;
  CHANNEL_RESET_ATTRIBUTE_CI_ANG_ENCODER_INITIAL_ANGLE = 2177;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INDEX_VAL = 2184;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INDEX_PHASE = 2185;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INDEX_ENABLE = 2192;
  CHANNEL_RESET_ATTRIBUTE_AI_RVDT_SENSITIVITY = 2307;
  CHANNEL_RESET_ATTRIBUTE_AI_LVDT_UNITS = 2320;
  CHANNEL_RESET_ATTRIBUTE_CI_LIN_ENCODER_DIST_PER_PULSE = 2321;
  CHANNEL_RESET_ATTRIBUTE_CI_LIN_ENCODER_INITIAL_POS = 2325;
  CHANNEL_RESET_ATTRIBUTE_AI_LVDT_SENSITIVITY = 2361;
  CHANNEL_RESET_ATTRIBUTE_AI_RESISTANCE_UNITS = 2389;
  CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_UNITS = 2433;
  CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_CFG = 2434;
  CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_GAGE_FACTOR = 2452;
  CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_POISSON_RATIO = 2456;
  CHANNEL_RESET_ATTRIBUTE_AI_RTD_A = 4112;
  CHANNEL_RESET_ATTRIBUTE_AI_RTD_B = 4113;
  CHANNEL_RESET_ATTRIBUTE_AI_RTD_C = 4115;
  CHANNEL_RESET_ATTRIBUTE_AI_RTD_R0 = 4144;
  CHANNEL_RESET_ATTRIBUTE_AI_RTD_TYPE = 4146;
  CHANNEL_RESET_ATTRIBUTE_AI_TEMP_UNITS = 4147;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_CJC_VAL = 4150;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_TYPE = 4176;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_R1 = 4193;
  CHANNEL_RESET_ATTRIBUTE_CI_GPS_SYNC_METHOD = 4242;
  CHANNEL_RESET_ATTRIBUTE_CI_GPS_SYNC_SRC = 4243;
  CHANNEL_RESET_ATTRIBUTE_AI_VOLTAGE_UNITS = 4244;
  CHANNEL_RESET_ATTRIBUTE_AI_TERM_CFG = 4247;
  CHANNEL_RESET_ATTRIBUTE_AO_CURRENT_UNITS = 4361;
  CHANNEL_RESET_ATTRIBUTE_DO_INVERT_LINES = 4403;
  CHANNEL_RESET_ATTRIBUTE_DO_OUTPUT_DRIVE_TYPE = 4407;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_HIGH_TICKS = 4457;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_IDLE_STATE = 4464;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_LOW_TICKS = 4465;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_DUTY_CYC = 4470;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_FREQ = 4472;
  CHANNEL_RESET_ATTRIBUTE_AO_VOLTAGE_UNITS = 4484;
  CHANNEL_RESET_ATTRIBUTE_AO_MAX = 4486;
  CHANNEL_RESET_ATTRIBUTE_AO_MIN = 4487;
  CHANNEL_RESET_ATTRIBUTE_AO_CUSTOM_SCALE_NAME = 4488;
  CHANNEL_RESET_ATTRIBUTE_AO_OUTPUT_IMPEDANCE = 5264;
  CHANNEL_RESET_ATTRIBUTE_AI_SOUND_PRESSURE_UNITS = 5416;
  CHANNEL_RESET_ATTRIBUTE_AI_MICROPHONE_SENSITIVITY = 5430;
  CHANNEL_RESET_ATTRIBUTE_AI_AUTO_ZERO_MODE = 5984;
  CHANNEL_RESET_ATTRIBUTE_AI_MAX = 6109;
  CHANNEL_RESET_ATTRIBUTE_AI_MIN = 6110;
  CHANNEL_RESET_ATTRIBUTE_AI_CUSTOM_SCALE_NAME = 6112;
  CHANNEL_RESET_ATTRIBUTE_AI_VOLTAGE_ACRMS_UNITS = 6114;
  CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_ACRMS_UNITS = 6115;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_NOM_RESISTANCE = 6124;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_INITIAL_VOLTAGE = 6125;
  CHANNEL_RESET_ATTRIBUTE_AI_LEAD_WIRE_RESISTANCE = 6126;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_BALANCE_COARSE_POT = 6129;
  CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_SHUNT_LOC = 6130;
  CHANNEL_RESET_ATTRIBUTE_AI_CURRENT_SHUNT_RESISTANCE = 6131;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_SRC = 6132;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_VAL = 6133;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_VOLTAGE_OR_CURRENT = 6134;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_D_COR_AC = 6139;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_USE_FOR_SCALING = 6140;
  CHANNEL_RESET_ATTRIBUTE_AI_ATTEN = 6145;
  CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_ENABLE = 6146;
  CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ = 6147;
  CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_ENABLE = 6150;
  CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_CUTOFF_FREQ = 6151;
  CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_TYPE = 6152;
  CHANNEL_RESET_ATTRIBUTE_AI_HIGHPASS_ORDER = 6153;
  CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_ENABLE = 6155;
  CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_CENTER_FREQ = 6156;
  CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_TYPE = 6157;
  CHANNEL_RESET_ATTRIBUTE_AI_BANDPASS_WIDTH = 6158;
  CHANNEL_RESET_ATTRIBUTE_AI_NOTCH_CENTER_FREQ = 6160;
  CHANNEL_RESET_ATTRIBUTE_AI_NOTCH_TYPE = 6161;
  CHANNEL_RESET_ATTRIBUTE_AI_NOTCH_WIDTH = 6162;
  CHANNEL_RESET_ATTRIBUTE_AI_RNG_HIGH = 6165;
  CHANNEL_RESET_ATTRIBUTE_AI_RNG_LOW = 6166;
  CHANNEL_RESET_ATTRIBUTE_AI_GAIN = 6168;
  CHANNEL_RESET_ATTRIBUTE_AI_SAMP_AND_HOLD_ENABLE = 6170;
  CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_MECH = 6177;
  CHANNEL_RESET_ATTRIBUTE_AO_RESOLUTION_UNITS = 6187;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_RNG_LOW = 6189;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_RNG_HIGH = 6190;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_ALLOW_CONN_TO_GND = 6192;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_VAL = 6194;
  CHANNEL_RESET_ATTRIBUTE_AO_USE_ONLY_ON_BRD_MEM = 6202;
  CHANNEL_RESET_ATTRIBUTE_AO_DATA_XFER_REQ_COND = 6204;
  CHANNEL_RESET_ATTRIBUTE_AI_RESISTANCE_CFG = 6273;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_ACTUAL_VAL = 6275;
  CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_CLK_SRC = 6276;
  CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_FREQ = 6277;
  CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_DIV = 6278;
  CHANNEL_RESET_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_OUT_CLK_DIV = 6279;
  CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_REQ_COND = 6283;
  CHANNEL_RESET_ATTRIBUTE_AI_MEM_MAP_ENABLE = 6284;
  CHANNEL_RESET_ATTRIBUTE_AO_TERM_CFG = 6286;
  CHANNEL_RESET_ATTRIBUTE_AO_MEM_MAP_ENABLE = 6287;
  CHANNEL_RESET_ATTRIBUTE_DI_TRISTATE = 6288;
  CHANNEL_RESET_ATTRIBUTE_CI_MAX = 6300;
  CHANNEL_RESET_ATTRIBUTE_CI_MIN = 6301;
  CHANNEL_RESET_ATTRIBUTE_CI_CUSTOM_SCALE_NAME = 6302;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_UNITS = 6305;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_TERM = 6306;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_UNITS = 6307;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_TERM = 6308;
  CHANNEL_RESET_ATTRIBUTE_CI_ANG_ENCODER_UNITS = 6310;
  CHANNEL_RESET_ATTRIBUTE_CI_LIN_ENCODER_UNITS = 6313;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_TERM = 6314;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_UNITS = 6316;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM = 6317;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM = 6318;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_UNITS = 6319;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_TERM = 6320;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_RATE = 6322;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_MASTER_TIMEBASE_DIV = 6323;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_HIGH_TIME = 6330;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_LOW_TIME = 6331;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TIME_INITIAL_DELAY = 6332;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_RATE = 6338;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_MASTER_TIMEBASE_DIV = 6339;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_TERM = 6343;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_A = 6345;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_C = 6346;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMSTR_B = 6347;
  CHANNEL_RESET_ATTRIBUTE_AI_AC_EXCIT_WIRE_MODE = 6349;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_FREQ_UNITS = 6357;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TIME_UNITS = 6358;
  CHANNEL_RESET_ATTRIBUTE_CO_PULSE_TERM = 6369;
  CHANNEL_RESET_ATTRIBUTE_DO_TRISTATE = 6387;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_BALANCE_FINE_POT = 6388;
  CHANNEL_RESET_ATTRIBUTE_AI_FORCE_READ_FROM_CHAN = 6392;
  CHANNEL_RESET_ATTRIBUTE_CHAN_DESCR = 6438;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_MEAS_METH = 6444;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_MEAS_TIME = 6445;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIV = 6446;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_GAIN_ADJUST = 6463;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_USE_MULTIPLEXED = 8576;
  CHANNEL_RESET_ATTRIBUTE_AI_INPUT_SRC = 8600;
  CHANNEL_RESET_ATTRIBUTE_AI_LVDT_SENSITIVITY_UNITS = 8602;
  CHANNEL_RESET_ATTRIBUTE_AI_RVDT_SENSITIVITY_UNITS = 8603;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_SENSITIVITY_UNITS = 8604;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM = 8605;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM = 8606;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM = 8607;
  CHANNEL_RESET_ATTRIBUTE_CI_DUP_COUNT_PREVENT = 8620;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SELECT = 8661;
  CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_ENABLE = 8662;
  CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_MIN_PULSE_WIDTH = 8663;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIR_TERM = 8673;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_DECODING_TYPE = 8678;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_ENABLE = 8679;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_MIN_PULSE_WIDTH = 8680;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_SRC = 8681;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_RATE = 8682;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_DIG_SYNC_ENABLE = 8683;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_ENABLE = 8684;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH = 8685;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_SRC = 8686;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_RATE = 8687;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_DIG_SYNC_ENABLE = 8688;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_ENABLE = 8689;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_MIN_PULSE_WIDTH = 8690;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_SRC = 8691;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_RATE = 8692;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_SYNC_ENABLE = 8693;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_ENABLE = 8694;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_MIN_PULSE_WIDTH = 8695;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_SRC = 8696;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_RATE = 8697;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_DIG_SYNC_ENABLE = 8698;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_ENABLE = 8699;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 8700;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC = 8701;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE = 8702;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_SYNC_ENABLE = 8703;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_ENABLE = 8704;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 8705;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC = 8706;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE = 8707;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_SYNC_ENABLE = 8708;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_ENABLE = 8709;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 8710;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_SRC = 8711;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_RATE = 8712;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_SYNC_ENABLE = 8713;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_ENABLE = 8714;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_MIN_PULSE_WIDTH = 8715;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_SRC = 8716;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_RATE = 8717;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_DIG_SYNC_ENABLE = 8718;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_ENABLE = 8719;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_MIN_PULSE_WIDTH = 8720;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_SRC = 8721;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_RATE = 8722;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_SYNC_ENABLE = 8723;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_ENABLE = 8724;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_MIN_PULSE_WIDTH = 8725;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_SRC = 8726;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_RATE = 8727;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_SYNC_ENABLE = 8728;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_ENABLE = 8729;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_MIN_PULSE_WIDTH = 8730;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_SRC = 8731;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_RATE = 8732;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_DIG_SYNC_ENABLE = 8733;
  CHANNEL_RESET_ATTRIBUTE_CI_PRESCALER = 8761;
  CHANNEL_RESET_ATTRIBUTE_AI_SOUND_PRESSURE_MAX_SOUND_PRESSURE_LVL = 8762;
  CHANNEL_RESET_ATTRIBUTE_AO_IDLE_OUTPUT_BEHAVIOR = 8768;
  CHANNEL_RESET_ATTRIBUTE_AO_ENHANCED_IMAGE_REJECTION_ENABLE = 8769;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_REF_EXT_SRC = 8786;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_OFFSET_SRC = 8787;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_OFFSET_EXT_SRC = 8788;
  CHANNEL_RESET_ATTRIBUTE_AO_DAC_OFFSET_VAL = 8789;
  CHANNEL_RESET_ATTRIBUTE_DI_DATA_XFER_MECH = 8803;
  CHANNEL_RESET_ATTRIBUTE_DI_DATA_XFER_REQ_COND = 8804;
  CHANNEL_RESET_ATTRIBUTE_DO_USE_ONLY_ON_BRD_MEM = 8805;
  CHANNEL_RESET_ATTRIBUTE_DO_DATA_XFER_MECH = 8806;
  CHANNEL_RESET_ATTRIBUTE_DO_DATA_XFER_REQ_COND = 8807;
  CHANNEL_RESET_ATTRIBUTE_CO_PRESCALER = 8813;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_ENABLE = 8817;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH = 8818;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC = 8819;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE = 8820;
  CHANNEL_RESET_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_SYNC_ENABLE = 8821;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_ENABLE = 8822;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_MIN_PULSE_WIDTH = 8823;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC = 8824;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_RATE = 8825;
  CHANNEL_RESET_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_SYNC_ENABLE = 8826;
  CHANNEL_RESET_ATTRIBUTE_AI_ENHANCED_ALIAS_REJECTION_ENABLE = 8852;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_ENABLE_CAL = 8856;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_APPLY_CAL_IF_EXP = 8857;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_SCALE_TYPE = 8860;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_TABLE_PRE_SCALED_VALS = 8861;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_TABLE_SCALED_VALS = 8862;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_POLY_FORWARD_COEFF = 8863;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_POLY_REVERSE_COEFF = 8864;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_VERIF_REF_VALS = 8865;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_VERIF_ACQ_VALS = 8866;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_OPERATOR_NAME = 8867;
  CHANNEL_RESET_ATTRIBUTE_AI_CHAN_CAL_DESC = 8868;
  CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_UNITS = 8883;
  CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_INITIAL_SECONDS = 8884;
  CHANNEL_RESET_ATTRIBUTE_AI_RAW_DATA_COMPRESSION_TYPE = 8920;
  CHANNEL_RESET_ATTRIBUTE_AI_LOSSY_LSB_REMOVAL_COMPRESSED_SAMP_SIZE = 8921;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_STARTING_EDGE = 8958;
  CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_CUSTOM_THRESHOLD = 8972;
  CHANNEL_RESET_ATTRIBUTE_DI_ACQUIRE_ON = 10598;
  CHANNEL_RESET_ATTRIBUTE_DO_LINE_STATES_PAUSED_STATE = 10599;
  CHANNEL_RESET_ATTRIBUTE_DO_LINE_STATES_DONE_STATE = 10600;
  CHANNEL_RESET_ATTRIBUTE_DO_GENERATE_ON = 10601;
  CHANNEL_RESET_ATTRIBUTE_DI_MEM_MAP_ENABLE = 10602;
  CHANNEL_RESET_ATTRIBUTE_DO_MEM_MAP_ENABLE = 10603;
  CHANNEL_RESET_ATTRIBUTE_DI_LOGIC_FAMILY = 10605;
  CHANNEL_RESET_ATTRIBUTE_DO_LOGIC_FAMILY = 10606;
  CHANNEL_RESET_ATTRIBUTE_DO_LINE_STATES_START_STATE = 10610;
  CHANNEL_RESET_ATTRIBUTE_AI_VOLTAGE_DB_REF = 10672;
  CHANNEL_RESET_ATTRIBUTE_AI_SOUND_PRESSURE_DB_REF = 10673;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_DB_REF = 10674;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_SCALE_TYPE = 10704;
  CHANNEL_RESET_ATTRIBUTE_CO_CONSTRAINED_GEN_MODE = 10738;
  CHANNEL_RESET_ATTRIBUTE_AI_ADC_TIMING_MODE = 10745;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_TYPE = 10776;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_FREQ = 10777;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_AMPLITUDE = 10778;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_OFFSET = 10779;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_SQUARE_DUTY_CYCLE = 10780;
  CHANNEL_RESET_ATTRIBUTE_AO_VOLTAGE_CURRENT_LIMIT = 10781;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_MODULATION_TYPE = 10786;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_FM_DEVIATION = 10787;
  CHANNEL_RESET_ATTRIBUTE_DO_OVERCURRENT_LIMIT = 10885;
  CHANNEL_RESET_ATTRIBUTE_DO_OVERCURRENT_AUTO_REENABLE = 10886;
  CHANNEL_RESET_ATTRIBUTE_DO_OVERCURRENT_REENABLE_PERIOD = 10887;
  CHANNEL_RESET_ATTRIBUTE_AI_PROBE_ATTEN = 10888;
  CHANNEL_RESET_ATTRIBUTE_AI_DC_OFFSET = 10889;
  CHANNEL_RESET_ATTRIBUTE_AI_USB_XFER_REQ_SIZE = 10894;
  CHANNEL_RESET_ATTRIBUTE_AO_USB_XFER_REQ_SIZE = 10895;
  CHANNEL_RESET_ATTRIBUTE_DI_USB_XFER_REQ_SIZE = 10896;
  CHANNEL_RESET_ATTRIBUTE_DO_USB_XFER_REQ_SIZE = 10897;
  CHANNEL_RESET_ATTRIBUTE_CI_USB_XFER_REQ_SIZE = 10898;
  CHANNEL_RESET_ATTRIBUTE_CO_USB_XFER_REQ_SIZE = 10899;
  CHANNEL_RESET_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY = 10942;
  CHANNEL_RESET_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS = 10943;
  CHANNEL_RESET_ATTRIBUTE_AI_EDDY_CURRENT_PROX_PROBE_UNITS = 10944;
  CHANNEL_RESET_ATTRIBUTE_CO_ENABLE_INITIAL_DELAY_ON_RETRIGGER = 11977;
  CHANNEL_RESET_ATTRIBUTE_CO_USE_ONLY_ON_BRD_MEM = 11979;
  CHANNEL_RESET_ATTRIBUTE_CO_DATA_XFER_MECH = 11980;
  CHANNEL_RESET_ATTRIBUTE_CO_DATA_XFER_REQ_COND = 11981;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_ENABLE_AVERAGING = 11984;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_ENABLE_AVERAGING = 11985;
  CHANNEL_RESET_ATTRIBUTE_CI_MEM_MAP_ENABLE = 11986;
  CHANNEL_RESET_ATTRIBUTE_CO_MEM_MAP_ENABLE = 11987;
  CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_SRC = 11988;
  CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_RATE = 11989;
  CHANNEL_RESET_ATTRIBUTE_DI_DIG_SYNC_ENABLE = 11990;
  CHANNEL_RESET_ATTRIBUTE_CI_DATA_XFER_REQ_COND = 12027;
  CHANNEL_RESET_ATTRIBUTE_DI_DIG_FLTR_ENABLE_BUS_MODE = 12030;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_TERM = 12036;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_START_EDGE = 12037;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_ENABLE = 12038;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_MIN_PULSE_WIDTH = 12039;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_SRC = 12040;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_RATE = 12041;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_DIG_SYNC_ENABLE = 12042;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_UNITS = 12043;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_TERM = 12044;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_START_EDGE = 12045;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_ENABLE = 12046;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_MIN_PULSE_WIDTH = 12047;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_SRC = 12048;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_RATE = 12049;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_DIG_SYNC_ENABLE = 12050;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_UNITS = 12051;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_TERM = 12052;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_START_EDGE = 12053;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_ENABLE = 12054;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_MIN_PULSE_WIDTH = 12055;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_SRC = 12056;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_RATE = 12057;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_DIG_SYNC_ENABLE = 12058;
  CHANNEL_RESET_ATTRIBUTE_AI_ADC_CUSTOM_TIMING_MODE = 12139;
  CHANNEL_RESET_ATTRIBUTE_AI_OPEN_THRMCPL_DETECT_ENABLE = 12146;
  CHANNEL_RESET_ATTRIBUTE_AI_FORCE_UNITS = 12149;
  CHANNEL_RESET_ATTRIBUTE_AI_PRESSURE_UNITS = 12150;
  CHANNEL_RESET_ATTRIBUTE_AI_TORQUE_UNITS = 12151;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_RESISTANCE = 12152;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_ACTUAL_RESISTANCE = 12153;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_RESISTANCE = 12154;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_ACTUAL_RESISTANCE = 12155;
  CHANNEL_RESET_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY = 12161;
  CHANNEL_RESET_ATTRIBUTE_AI_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS = 12162;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_INITIAL_RATIO = 12166;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_ELECTRICAL_UNITS = 12167;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_PHYSICAL_UNITS = 12168;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SCALE_TYPE = 12169;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_ELECTRICAL_VAL = 12170;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_FIRST_PHYSICAL_VAL = 12171;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_ELECTRICAL_VAL = 12172;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TWO_POINT_LIN_SECOND_PHYSICAL_VAL = 12173;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TABLE_ELECTRICAL_VALS = 12174;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_TABLE_PHYSICAL_VALS = 12175;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_POLY_FORWARD_COEFF = 12176;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_POLY_REVERSE_COEFF = 12177;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_UNITS = 12178;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ENABLE = 12207;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_RESET_COUNT = 12208;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM = 12209;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ACTIVE_EDGE = 12210;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_ENABLE = 12211;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_MIN_PULSE_WIDTH = 12212;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_SRC = 12213;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_RATE = 12214;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_SYNC_ENABLE = 12215;
  CHANNEL_RESET_ATTRIBUTE_AI_THRMCPL_LEAD_OFFSET_VOLTAGE = 12216;
  CHANNEL_RESET_ATTRIBUTE_AI_REMOVE_FILTER_DELAY = 12221;
  CHANNEL_RESET_ATTRIBUTE_AI_AVERAGING_WIN_SIZE = 12270;
  CHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_UNITS = 12276;
  CHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_DB_REF = 12277;
  CHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY = 12278;
  CHANNEL_RESET_ATTRIBUTE_AI_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS = 12279;
  CHANNEL_RESET_ATTRIBUTE_AI_STRAIN_GAGE_FORCE_READ_FROM_CHAN = 12282;
  CHANNEL_RESET_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ORIENTATION = 12284;
  CHANNEL_RESET_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_ROSETTE_MEAS_TYPE = 12285;
  CHANNEL_RESET_ATTRIBUTE_AI_USB_XFER_REQ_COUNT = 12288;
  CHANNEL_RESET_ATTRIBUTE_AO_USB_XFER_REQ_COUNT = 12289;
  CHANNEL_RESET_ATTRIBUTE_DI_USB_XFER_REQ_COUNT = 12290;
  CHANNEL_RESET_ATTRIBUTE_DO_USB_XFER_REQ_COUNT = 12291;
  CHANNEL_RESET_ATTRIBUTE_CI_USB_XFER_REQ_COUNT = 12292;
  CHANNEL_RESET_ATTRIBUTE_CO_USB_XFER_REQ_COUNT = 12293;
  CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_TERM = 12345;
  CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_EDGE = 12346;
  CHANNEL_RESET_ATTRIBUTE_CI_TIMESTAMP_TIMESCALE = 12347;
  CHANNEL_RESET_ATTRIBUTE_NAV_CUSTOM_SCALE_NAME = 12348;
  CHANNEL_RESET_ATTRIBUTE_NAV_ALT_UNITS = 12350;
  CHANNEL_RESET_ATTRIBUTE_NAV_LAT_UNITS = 12351;
  CHANNEL_RESET_ATTRIBUTE_NAV_LONG_UNITS = 12352;
  CHANNEL_RESET_ATTRIBUTE_NAV_SPEED_OVER_GROUND_UNITS = 12353;
  CHANNEL_RESET_ATTRIBUTE_NAV_TRACK_UNITS = 12354;
  CHANNEL_RESET_ATTRIBUTE_NAV_VERT_VELOCITY_UNITS = 12355;
  CHANNEL_RESET_ATTRIBUTE_NAV_TIMESTAMP_UNITS = 12356;
  CHANNEL_RESET_ATTRIBUTE_NAV_TIMESTAMP_TIMESCALE = 12357;
  CHANNEL_RESET_ATTRIBUTE_AI_FILTER_DELAY_UNITS = 12401;
  CHANNEL_RESET_ATTRIBUTE_AO_FILTER_DELAY_ADJUSTMENT = 12402;
  CHANNEL_RESET_ATTRIBUTE_AI_FILTER_DELAY_ADJUSTMENT = 12404;
  CHANNEL_RESET_ATTRIBUTE_AO_FILTER_DELAY = 12405;
  CHANNEL_RESET_ATTRIBUTE_AO_FILTER_DELAY_UNITS = 12406;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_TERM = 12429;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_ENABLE = 12430;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_MIN_PULSE_WIDTH = 12431;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_SRC = 12432;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_RATE = 12433;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_STARTING_EDGE = 12434;
  CHANNEL_RESET_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_BEHAVIOR = 12435;
  CHANNEL_RESET_ATTRIBUTE_CI_SAMP_CLK_OVERRUN_SENTINEL_VAL = 12436;
  CHANNEL_RESET_ATTRIBUTE_CI_MAX_MEAS_PERIOD = 12437;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_TERM_CFG = 12439;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_LOGIC_LVL_BEHAVIOR = 12440;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_TERM_CFG = 12441;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_LOGIC_LVL_BEHAVIOR = 12442;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_TERM_CFG = 12443;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_LOGIC_LVL_BEHAVIOR = 12444;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_TERM_CFG = 12445;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_LOGIC_LVL_BEHAVIOR = 12446;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM_CFG = 12447;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_LOGIC_LVL_BEHAVIOR = 12448;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_TERM_CFG = 12449;
  CHANNEL_RESET_ATTRIBUTE_CI_DUTY_CYCLE_LOGIC_LVL_BEHAVIOR = 12450;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM_CFG = 12451;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR = 12452;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM_CFG = 12453;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR = 12454;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM_CFG = 12455;
  CHANNEL_RESET_ATTRIBUTE_CI_ENCODER_Z_INPUT_LOGIC_LVL_BEHAVIOR = 12456;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_TERM_CFG = 12457;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_WIDTH_LOGIC_LVL_BEHAVIOR = 12458;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM_CFG = 12459;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_LOGIC_LVL_BEHAVIOR = 12460;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM_CFG = 12461;
  CHANNEL_RESET_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_LOGIC_LVL_BEHAVIOR = 12462;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_TERM_CFG = 12463;
  CHANNEL_RESET_ATTRIBUTE_CI_SEMI_PERIOD_LOGIC_LVL_BEHAVIOR = 12464;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_TERM_CFG = 12465;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_FREQ_LOGIC_LVL_BEHAVIOR = 12466;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_TERM_CFG = 12467;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TIME_LOGIC_LVL_BEHAVIOR = 12468;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_TERM_CFG = 12469;
  CHANNEL_RESET_ATTRIBUTE_CI_PULSE_TICKS_LOGIC_LVL_BEHAVIOR = 12470;
  CHANNEL_RESET_ATTRIBUTE_CI_THRESH_VOLTAGE = 12471;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_IDLE_OUTPUT_BEHAVIOR = 12472;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_ENABLE = 12477;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_TYPE = 12478;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_RESPONSE = 12479;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_ORDER = 12480;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ = 12481;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_HIGHPASS_CUTOFF_FREQ = 12482;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_CENTER_FREQ = 12483;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_BANDPASS_WIDTH = 12484;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_NOTCH_CENTER_FREQ = 12485;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_NOTCH_WIDTH = 12486;
  CHANNEL_RESET_ATTRIBUTE_AI_DIG_FLTR_COEFF = 12487;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_A_SRC = 12490;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_UNITS = 12504;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_PULSES_PER_REV = 12505;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_UNITS = 12506;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_LIN_ENCODER_DIST_PER_PULSE = 12507;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_DECODING_TYPE = 12508;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM = 12509;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM_CFG = 12510;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_LOGIC_LVL_BEHAVIOR = 12511;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_ENABLE = 12512;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 12513;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC = 12514;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_RATE = 12515;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM = 12516;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM_CFG = 12517;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_LOGIC_LVL_BEHAVIOR = 12518;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_ENABLE = 12519;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_MIN_PULSE_WIDTH = 12520;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC = 12521;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_RATE = 12522;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_MEAS_TIME = 12523;
  CHANNEL_RESET_ATTRIBUTE_CI_VELOCITY_DIV = 12524;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_ENABLE = 12525;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM = 12526;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM_CFG = 12527;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_LOGIC_LVL_BEHAVIOR = 12528;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_ENABLE = 12529;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_MIN_PULSE_WIDTH = 12530;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_SRC = 12531;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_RATE = 12532;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_WHEN = 12533;
  CHANNEL_RESET_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC = 12535;
  CHANNEL_RESET_ATTRIBUTE_AI_EXCIT_SENSE = 12541;
  CHANNEL_RESET_ATTRIBUTE_AI_OPEN_CHAN_DETECT_ENABLE = 12543;
  CHANNEL_RESET_ATTRIBUTE_AI_CHARGE_UNITS = 12562;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY = 12563;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_CHARGE_SENSITIVITY_UNITS = 12564;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY = 12565;
  CHANNEL_RESET_ATTRIBUTE_AI_ACCEL_4_WIRE_DC_VOLTAGE_SENSITIVITY_UNITS = 12566;
  CHANNEL_RESET_ATTRIBUTE_AI_DATA_XFER_MAX_RATE = 12567;
  CHANNEL_RESET_ATTRIBUTE_CHAN_SYNC_UNLOCK_BEHAVIOR = 12604;
  CHANNEL_RESET_ATTRIBUTE_AI_CHOP_ENABLE = 12611;
  CHANNEL_RESET_ATTRIBUTE_AI_SENSOR_POWER_VOLTAGE = 12649;
  CHANNEL_RESET_ATTRIBUTE_AI_SENSOR_POWER_CFG = 12650;
  CHANNEL_RESET_ATTRIBUTE_AI_SENSOR_POWER_TYPE = 12651;
  CHANNEL_RESET_ATTRIBUTE_AI_FILTER_ENABLE = 12659;
  CHANNEL_RESET_ATTRIBUTE_AI_FILTER_FREQ = 12660;
  CHANNEL_RESET_ATTRIBUTE_AI_FILTER_RESPONSE = 12661;
  CHANNEL_RESET_ATTRIBUTE_AI_FILTER_ORDER = 12662;
  CHANNEL_RESET_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_UPPER_LIMIT = 12684;
  CHANNEL_RESET_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_LOWER_LIMIT = 12685;
  CHANNEL_RESET_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_ENABLE = 12686;
  CHANNEL_RESET_ATTRIBUTE_AI_POWER_SUPPLY_FAULT_DETECT_ENABLE = 12689;
  CHANNEL_RESET_ATTRIBUTE_AI_OVERCURRENT_DETECT_ENABLE = 12692;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_THRESH_VOLTAGE = 12715;
  CHANNEL_RESET_ATTRIBUTE_CI_FREQ_HYST = 12716;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_THRESH_VOLTAGE = 12717;
  CHANNEL_RESET_ATTRIBUTE_CI_PERIOD_HYST = 12718;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_THRESH_VOLTAGE = 12719;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_HYST = 12720;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_THRESH_VOLTAGE = 12721;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_HYST = 12722;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_THRESH_VOLTAGE = 12723;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_HYST = 12724;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_THRESH_VOLTAGE = 12725;
  CHANNEL_RESET_ATTRIBUTE_CI_COUNT_EDGES_GATE_HYST = 12726;
  CHANNEL_RESET_ATTRIBUTE_CI_FILTER_ENABLE = 12727;
  CHANNEL_RESET_ATTRIBUTE_CI_FILTER_FREQ = 12728;
  CHANNEL_RESET_ATTRIBUTE_CI_FILTER_RESPONSE = 12729;
  CHANNEL_RESET_ATTRIBUTE_CI_FILTER_ORDER = 12730;
  CHANNEL_RESET_ATTRIBUTE_CI_FILTER_DELAY_UNITS = 12732;
  CHANNEL_RESET_ATTRIBUTE_AO_FUNC_GEN_START_PHASE = 12740;
  CHANNEL_RESET_ATTRIBUTE_AO_COMMON_MODE_OFFSET = 12748;
  CHANNEL_RESET_ATTRIBUTE_PWR_VOLTAGE_SETPOINT = 12756;
  CHANNEL_RESET_ATTRIBUTE_PWR_CURRENT_SETPOINT = 12757;
  CHANNEL_RESET_ATTRIBUTE_PWR_OUTPUT_ENABLE = 12758;
  CHANNEL_RESET_ATTRIBUTE_PWR_IDLE_OUTPUT_BEHAVIOR = 12760;
  CHANNEL_RESET_ATTRIBUTE_PWR_REMOTE_SENSE = 12763;
  CHANNEL_RESET_ATTRIBUTE_AI_POWER_UNITS = 12780;
  CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MAX = 12781;
  CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_VOLTAGE_MIN = 12782;
  CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MAX = 12783;
  CHANNEL_RESET_ATTRIBUTE_AI_CALCULATED_POWER_CURRENT_MIN = 12784;
}

enum ChannelBoolAttribute {
  CHANNEL_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  CHANNEL_ATTRIBUTE_AI_DITHER_ENABLE = 104;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_SHUNT_CAL_ENABLE = 148;
  CHANNEL_ATTRIBUTE_AI_AC_EXCIT_SYNC_ENABLE = 258;
  CHANNEL_ATTRIBUTE_AO_DAC_REF_CONN_TO_GND = 304;
  CHANNEL_ATTRIBUTE_AO_REGLITCH_ENABLE = 307;
  CHANNEL_ATTRIBUTE_CI_TC_REACHED = 336;
  CHANNEL_ATTRIBUTE_DI_INVERT_LINES = 1939;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INDEX_ENABLE = 2192;
  CHANNEL_ATTRIBUTE_DO_INVERT_LINES = 4403;
  CHANNEL_ATTRIBUTE_AI_EXCIT_USE_FOR_SCALING = 6140;
  CHANNEL_ATTRIBUTE_AI_LOWPASS_ENABLE = 6146;
  CHANNEL_ATTRIBUTE_AI_HIGHPASS_ENABLE = 6150;
  CHANNEL_ATTRIBUTE_AI_BANDPASS_ENABLE = 6155;
  CHANNEL_ATTRIBUTE_AI_SAMP_AND_HOLD_ENABLE = 6170;
  CHANNEL_ATTRIBUTE_AO_DAC_REF_ALLOW_CONN_TO_GND = 6192;
  CHANNEL_ATTRIBUTE_AO_USE_ONLY_ON_BRD_MEM = 6202;
  CHANNEL_ATTRIBUTE_AI_MEM_MAP_ENABLE = 6284;
  CHANNEL_ATTRIBUTE_AO_MEM_MAP_ENABLE = 6287;
  CHANNEL_ATTRIBUTE_DI_TRISTATE = 6288;
  CHANNEL_ATTRIBUTE_DO_TRISTATE = 6387;
  CHANNEL_ATTRIBUTE_AI_FORCE_READ_FROM_CHAN = 6392;
  CHANNEL_ATTRIBUTE_CO_PULSE_DONE = 6414;
  CHANNEL_ATTRIBUTE_AI_EXCIT_USE_MULTIPLEXED = 8576;
  CHANNEL_ATTRIBUTE_CI_DUP_COUNT_PREVENT = 8620;
  CHANNEL_ATTRIBUTE_DI_DIG_FLTR_ENABLE = 8662;
  CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_ENABLE = 8679;
  CHANNEL_ATTRIBUTE_CI_FREQ_DIG_SYNC_ENABLE = 8683;
  CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_ENABLE = 8684;
  CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_SYNC_ENABLE = 8688;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_ENABLE = 8689;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_SYNC_ENABLE = 8693;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_ENABLE = 8694;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_SYNC_ENABLE = 8698;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_ENABLE = 8699;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_SYNC_ENABLE = 8703;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_ENABLE = 8704;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_SYNC_ENABLE = 8708;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_ENABLE = 8709;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_SYNC_ENABLE = 8713;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_ENABLE = 8714;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_SYNC_ENABLE = 8718;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_ENABLE = 8719;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_SYNC_ENABLE = 8723;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_ENABLE = 8724;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_SYNC_ENABLE = 8728;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_ENABLE = 8729;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_SYNC_ENABLE = 8733;
  CHANNEL_ATTRIBUTE_AO_ENHANCED_IMAGE_REJECTION_ENABLE = 8769;
  CHANNEL_ATTRIBUTE_DO_USE_ONLY_ON_BRD_MEM = 8805;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_ENABLE = 8817;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_SYNC_ENABLE = 8821;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_ENABLE = 8822;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_SYNC_ENABLE = 8826;
  CHANNEL_ATTRIBUTE_AI_ENHANCED_ALIAS_REJECTION_ENABLE = 8852;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_HAS_VALID_CAL_INFO = 8855;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_ENABLE_CAL = 8856;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_APPLY_CAL_IF_EXP = 8857;
  CHANNEL_ATTRIBUTE_CO_RDY_FOR_NEW_VAL = 8959;
  CHANNEL_ATTRIBUTE_CHAN_IS_GLOBAL = 8964;
  CHANNEL_ATTRIBUTE_DI_MEM_MAP_ENABLE = 10602;
  CHANNEL_ATTRIBUTE_DO_MEM_MAP_ENABLE = 10603;
  CHANNEL_ATTRIBUTE_AI_IS_TEDS = 10627;
  CHANNEL_ATTRIBUTE_DO_OVERCURRENT_AUTO_REENABLE = 10886;
  CHANNEL_ATTRIBUTE_CO_ENABLE_INITIAL_DELAY_ON_RETRIGGER = 11977;
  CHANNEL_ATTRIBUTE_CO_USE_ONLY_ON_BRD_MEM = 11979;
  CHANNEL_ATTRIBUTE_CI_FREQ_ENABLE_AVERAGING = 11984;
  CHANNEL_ATTRIBUTE_CI_PERIOD_ENABLE_AVERAGING = 11985;
  CHANNEL_ATTRIBUTE_CI_MEM_MAP_ENABLE = 11986;
  CHANNEL_ATTRIBUTE_CO_MEM_MAP_ENABLE = 11987;
  CHANNEL_ATTRIBUTE_DI_DIG_SYNC_ENABLE = 11990;
  CHANNEL_ATTRIBUTE_DI_DIG_FLTR_ENABLE_BUS_MODE = 12030;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_ENABLE = 12038;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_SYNC_ENABLE = 12042;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_ENABLE = 12046;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_SYNC_ENABLE = 12050;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_ENABLE = 12054;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_SYNC_ENABLE = 12058;
  CHANNEL_ATTRIBUTE_AI_OPEN_THRMCPL_DETECT_ENABLE = 12146;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_ENABLE = 12207;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_ENABLE = 12211;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_SYNC_ENABLE = 12215;
  CHANNEL_ATTRIBUTE_AI_REMOVE_FILTER_DELAY = 12221;
  CHANNEL_ATTRIBUTE_AI_STRAIN_GAGE_FORCE_READ_FROM_CHAN = 12282;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_ENABLE = 12430;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_ENABLE = 12477;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_ENABLE = 12512;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_ENABLE = 12519;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_ENABLE = 12525;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_ENABLE = 12529;
  CHANNEL_ATTRIBUTE_AI_OPEN_CHAN_DETECT_ENABLE = 12543;
  CHANNEL_ATTRIBUTE_AI_CHOP_ENABLE = 12611;
  CHANNEL_ATTRIBUTE_AI_FILTER_ENABLE = 12659;
  CHANNEL_ATTRIBUTE_AI_INPUT_LIMITS_FAULT_DETECT_ENABLE = 12686;
  CHANNEL_ATTRIBUTE_AI_POWER_SUPPLY_FAULT_DETECT_ENABLE = 12689;
  CHANNEL_ATTRIBUTE_AI_OVERCURRENT_DETECT_ENABLE = 12692;
  CHANNEL_ATTRIBUTE_CI_FILTER_ENABLE = 12727;
  CHANNEL_ATTRIBUTE_PWR_OUTPUT_ENABLE = 12758;
}

enum ChannelStringAttribute {
  CHANNEL_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_SRC = 323;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_SRC = 825;
  CHANNEL_ATTRIBUTE_AI_THRMCPL_CJC_CHAN = 4148;
  CHANNEL_ATTRIBUTE_CI_GPS_SYNC_SRC = 4243;
  CHANNEL_ATTRIBUTE_AO_CUSTOM_SCALE_NAME = 4488;
  CHANNEL_ATTRIBUTE_AI_CUSTOM_SCALE_NAME = 6112;
  CHANNEL_ATTRIBUTE_CI_CUSTOM_SCALE_NAME = 6302;
  CHANNEL_ATTRIBUTE_CI_FREQ_TERM = 6306;
  CHANNEL_ATTRIBUTE_CI_PERIOD_TERM = 6308;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_TERM = 6314;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_TERM = 6317;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_TERM = 6318;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_TERM = 6320;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_TERM = 6343;
  CHANNEL_ATTRIBUTE_CO_PULSE_TERM = 6369;
  CHANNEL_ATTRIBUTE_PHYSICAL_CHAN_NAME = 6389;
  CHANNEL_ATTRIBUTE_CHAN_DESCR = 6438;
  CHANNEL_ATTRIBUTE_AI_INPUT_SRC = 8600;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_TERM = 8605;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_TERM = 8606;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_TERM = 8607;
  CHANNEL_ATTRIBUTE_AI_TEDS_UNITS = 8672;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIR_TERM = 8673;
  CHANNEL_ATTRIBUTE_CI_FREQ_DIG_FLTR_TIMEBASE_SRC = 8681;
  CHANNEL_ATTRIBUTE_CI_PERIOD_DIG_FLTR_TIMEBASE_SRC = 8686;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_DIR_DIG_FLTR_TIMEBASE_SRC = 8691;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_DIG_FLTR_TIMEBASE_SRC = 8696;
  CHANNEL_ATTRIBUTE_CI_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC = 8701;
  CHANNEL_ATTRIBUTE_CI_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC = 8706;
  CHANNEL_ATTRIBUTE_CI_ENCODER_Z_INPUT_DIG_FLTR_TIMEBASE_SRC = 8711;
  CHANNEL_ATTRIBUTE_CI_PULSE_WIDTH_DIG_FLTR_TIMEBASE_SRC = 8716;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_FIRST_DIG_FLTR_TIMEBASE_SRC = 8721;
  CHANNEL_ATTRIBUTE_CI_TWO_EDGE_SEP_SECOND_DIG_FLTR_TIMEBASE_SRC = 8726;
  CHANNEL_ATTRIBUTE_CI_SEMI_PERIOD_DIG_FLTR_TIMEBASE_SRC = 8731;
  CHANNEL_ATTRIBUTE_AO_DAC_REF_EXT_SRC = 8786;
  CHANNEL_ATTRIBUTE_AO_DAC_OFFSET_EXT_SRC = 8788;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC = 8819;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_DIG_FLTR_TIMEBASE_SRC = 8824;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_OPERATOR_NAME = 8867;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_DESC = 8868;
  CHANNEL_ATTRIBUTE_DI_DIG_FLTR_TIMEBASE_SRC = 11988;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_TERM = 12036;
  CHANNEL_ATTRIBUTE_CI_PULSE_FREQ_DIG_FLTR_TIMEBASE_SRC = 12040;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_TERM = 12044;
  CHANNEL_ATTRIBUTE_CI_PULSE_TIME_DIG_FLTR_TIMEBASE_SRC = 12048;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_TERM = 12052;
  CHANNEL_ATTRIBUTE_CI_PULSE_TICKS_DIG_FLTR_TIMEBASE_SRC = 12056;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_TERM = 12209;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_DIG_FLTR_TIMEBASE_SRC = 12213;
  CHANNEL_ATTRIBUTE_AI_ROSETTE_STRAIN_GAGE_STRAIN_CHANS = 12283;
  CHANNEL_ATTRIBUTE_CI_TIMESTAMP_TERM = 12345;
  CHANNEL_ATTRIBUTE_NAV_CUSTOM_SCALE_NAME = 12348;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_TERM = 12429;
  CHANNEL_ATTRIBUTE_CI_DUTY_CYCLE_DIG_FLTR_TIMEBASE_SRC = 12432;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_TERM = 12509;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_A_INPUT_DIG_FLTR_TIMEBASE_SRC = 12514;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_TERM = 12516;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ENCODER_B_INPUT_DIG_FLTR_TIMEBASE_SRC = 12521;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_TERM = 12526;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_GATE_DIG_FLTR_TIMEBASE_SRC = 12531;
}

enum ChannelUInt32Attribute {
  CHANNEL_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  CHANNEL_ATTRIBUTE_CI_FREQ_DIV = 327;
  CHANNEL_ATTRIBUTE_CI_COUNT = 328;
  CHANNEL_ATTRIBUTE_CO_COUNT = 659;
  CHANNEL_ATTRIBUTE_CO_AUTO_INCR_CNT = 661;
  CHANNEL_ATTRIBUTE_CO_PULSE_TICKS_INITIAL_DELAY = 664;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_INITIAL_CNT = 1688;
  CHANNEL_ATTRIBUTE_CI_ANG_ENCODER_PULSES_PER_REV = 2165;
  CHANNEL_ATTRIBUTE_CO_PULSE_HIGH_TICKS = 4457;
  CHANNEL_ATTRIBUTE_CO_PULSE_LOW_TICKS = 4465;
  CHANNEL_ATTRIBUTE_AI_HIGHPASS_ORDER = 6153;
  CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_EXT_CLK_DIV = 6278;
  CHANNEL_ATTRIBUTE_AI_LOWPASS_SWITCH_CAP_OUT_CLK_DIV = 6279;
  CHANNEL_ATTRIBUTE_CI_CTR_TIMEBASE_MASTER_TIMEBASE_DIV = 6323;
  CHANNEL_ATTRIBUTE_CO_CTR_TIMEBASE_MASTER_TIMEBASE_DIV = 6339;
  CHANNEL_ATTRIBUTE_CI_PERIOD_DIV = 6446;
  CHANNEL_ATTRIBUTE_CI_NUM_POSSIBLY_INVALID_SAMPS = 6460;
  CHANNEL_ATTRIBUTE_DI_NUM_LINES = 8568;
  CHANNEL_ATTRIBUTE_DO_NUM_LINES = 8569;
  CHANNEL_ATTRIBUTE_CI_PRESCALER = 8761;
  CHANNEL_ATTRIBUTE_CO_PRESCALER = 8813;
  CHANNEL_ATTRIBUTE_CI_TIMESTAMP_INITIAL_SECONDS = 8884;
  CHANNEL_ATTRIBUTE_AI_LOSSY_LSB_REMOVAL_COMPRESSED_SAMP_SIZE = 8921;
  CHANNEL_ATTRIBUTE_AI_RAW_SAMP_SIZE = 8922;
  CHANNEL_ATTRIBUTE_AI_DATA_XFER_CUSTOM_THRESHOLD = 8972;
  CHANNEL_ATTRIBUTE_AI_USB_XFER_REQ_SIZE = 10894;
  CHANNEL_ATTRIBUTE_AO_USB_XFER_REQ_SIZE = 10895;
  CHANNEL_ATTRIBUTE_DI_USB_XFER_REQ_SIZE = 10896;
  CHANNEL_ATTRIBUTE_DO_USB_XFER_REQ_SIZE = 10897;
  CHANNEL_ATTRIBUTE_CI_USB_XFER_REQ_SIZE = 10898;
  CHANNEL_ATTRIBUTE_CO_USB_XFER_REQ_SIZE = 10899;
  CHANNEL_ATTRIBUTE_AI_ADC_CUSTOM_TIMING_MODE = 12139;
  CHANNEL_ATTRIBUTE_CI_COUNT_EDGES_COUNT_RESET_RESET_COUNT = 12208;
  CHANNEL_ATTRIBUTE_AI_AVERAGING_WIN_SIZE = 12270;
  CHANNEL_ATTRIBUTE_AI_USB_XFER_REQ_COUNT = 12288;
  CHANNEL_ATTRIBUTE_AO_USB_XFER_REQ_COUNT = 12289;
  CHANNEL_ATTRIBUTE_DI_USB_XFER_REQ_COUNT = 12290;
  CHANNEL_ATTRIBUTE_DO_USB_XFER_REQ_COUNT = 12291;
  CHANNEL_ATTRIBUTE_CI_USB_XFER_REQ_COUNT = 12292;
  CHANNEL_ATTRIBUTE_CO_USB_XFER_REQ_COUNT = 12293;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_ORDER = 12480;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_ANG_ENCODER_PULSES_PER_REV = 12505;
  CHANNEL_ATTRIBUTE_CI_VELOCITY_DIV = 12524;
  CHANNEL_ATTRIBUTE_AI_FILTER_ORDER = 12662;
  CHANNEL_ATTRIBUTE_CI_FILTER_ORDER = 12730;
}

enum ChannelDoubleArrayAttribute {
  CHANNEL_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  CHANNEL_ATTRIBUTE_AI_DEV_SCALING_COEFF = 6448;
  CHANNEL_ATTRIBUTE_AO_DEV_SCALING_COEFF = 6449;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_TABLE_PRE_SCALED_VALS = 8861;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_TABLE_SCALED_VALS = 8862;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_POLY_FORWARD_COEFF = 8863;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_POLY_REVERSE_COEFF = 8864;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_VERIF_REF_VALS = 8865;
  CHANNEL_ATTRIBUTE_AI_CHAN_CAL_VERIF_ACQ_VALS = 8866;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_TABLE_ELECTRICAL_VALS = 12174;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_TABLE_PHYSICAL_VALS = 12175;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_POLY_FORWARD_COEFF = 12176;
  CHANNEL_ATTRIBUTE_AI_BRIDGE_POLY_REVERSE_COEFF = 12177;
  CHANNEL_ATTRIBUTE_AI_DIG_FLTR_COEFF = 12487;
  CHANNEL_ATTRIBUTE_PWR_VOLTAGE_DEV_SCALING_COEFF = 12761;
  CHANNEL_ATTRIBUTE_PWR_CURRENT_DEV_SCALING_COEFF = 12762;
}

enum DeviceStringAttribute {
  DEVICE_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_PRODUCT_TYPE = 1585;
  DEVICE_ATTRIBUTE_AI_PHYSICAL_CHANS = 8990;
  DEVICE_ATTRIBUTE_AO_PHYSICAL_CHANS = 8991;
  DEVICE_ATTRIBUTE_DI_LINES = 8992;
  DEVICE_ATTRIBUTE_DI_PORTS = 8993;
  DEVICE_ATTRIBUTE_DO_LINES = 8994;
  DEVICE_ATTRIBUTE_DO_PORTS = 8995;
  DEVICE_ATTRIBUTE_CI_PHYSICAL_CHANS = 8996;
  DEVICE_ATTRIBUTE_CO_PHYSICAL_CHANS = 8997;
  DEVICE_ATTRIBUTE_CHASSIS_MODULE_DEV_NAMES = 10678;
  DEVICE_ATTRIBUTE_COMPACT_DAQ_CHASSIS_DEV_NAME = 10679;
  DEVICE_ATTRIBUTE_TERMINALS = 10816;
  DEVICE_ATTRIBUTE_TCPIP_HOSTNAME = 10891;
  DEVICE_ATTRIBUTE_TCPIP_ETHERNET_IP = 10892;
  DEVICE_ATTRIBUTE_TCPIP_WIRELESS_IP = 10893;
  DEVICE_ATTRIBUTE_ACCESSORY_PRODUCT_TYPES = 12141;
  DEVICE_ATTRIBUTE_NAV_PHYSICAL_CHANS = 12322;
  DEVICE_ATTRIBUTE_COMPACT_RIO_CHASSIS_DEV_NAME = 12641;
  DEVICE_ATTRIBUTE_FIELD_DAQ_DEV_NAME = 12657;
  DEVICE_ATTRIBUTE_FIELD_DAQ_BANK_DEV_NAMES = 12664;
  DEVICE_ATTRIBUTE_ID_PIN_PIN_NAMES = 12785;
  DEVICE_ATTRIBUTE_ID_PIN_MEM_SERIAL_NUMS = 12788;
}

enum DeviceUInt32Attribute {
  DEVICE_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_SERIAL_NUM = 1586;
  DEVICE_ATTRIBUTE_PRODUCT_NUM = 8989;
  DEVICE_ATTRIBUTE_PCI_BUS_NUM = 8999;
  DEVICE_ATTRIBUTE_PCI_DEV_NUM = 9000;
  DEVICE_ATTRIBUTE_PXI_CHASSIS_NUM = 9001;
  DEVICE_ATTRIBUTE_PXI_SLOT_NUM = 9002;
  DEVICE_ATTRIBUTE_NUM_DMA_CHANS = 9020;
  DEVICE_ATTRIBUTE_CI_MAX_SIZE = 10655;
  DEVICE_ATTRIBUTE_CO_MAX_SIZE = 10657;
  DEVICE_ATTRIBUTE_COMPACT_DAQ_SLOT_NUM = 10680;
  DEVICE_ATTRIBUTE_CARRIER_SERIAL_NUM = 10890;
  DEVICE_ATTRIBUTE_NAV_NUM_SURVEY_FIXES = 12331;
  DEVICE_ATTRIBUTE_NAV_REMAINING_SURVEY_FIXES = 12332;
  DEVICE_ATTRIBUTE_NAV_NUM_SATS = 12337;
  DEVICE_ATTRIBUTE_NUM_TIME_TRIGS = 12609;
  DEVICE_ATTRIBUTE_NUM_TIMESTAMP_ENGINES = 12610;
  DEVICE_ATTRIBUTE_COMPACT_RIO_SLOT_NUM = 12642;
  DEVICE_ATTRIBUTE_AI_NUM_SAMP_TIMING_ENGINES = 12643;
  DEVICE_ATTRIBUTE_AI_NUM_SYNC_PULSE_SRCS = 12644;
  DEVICE_ATTRIBUTE_AO_NUM_SAMP_TIMING_ENGINES = 12645;
  DEVICE_ATTRIBUTE_AO_NUM_SYNC_PULSE_SRCS = 12646;
  DEVICE_ATTRIBUTE_DI_NUM_SAMP_TIMING_ENGINES = 12647;
  DEVICE_ATTRIBUTE_DO_NUM_SAMP_TIMING_ENGINES = 12648;
}

enum DeviceBoolAttribute {
  DEVICE_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_IS_SIMULATED = 8906;
  DEVICE_ATTRIBUTE_ANLG_TRIG_SUPPORTED = 10628;
  DEVICE_ATTRIBUTE_DIG_TRIG_SUPPORTED = 10629;
  DEVICE_ATTRIBUTE_AI_SIMULTANEOUS_SAMPLING_SUPPORTED = 10639;
  DEVICE_ATTRIBUTE_AO_SAMP_CLK_SUPPORTED = 10646;
  DEVICE_ATTRIBUTE_CI_SAMP_CLK_SUPPORTED = 10654;
  DEVICE_ATTRIBUTE_CO_SAMP_CLK_SUPPORTED = 12123;
  DEVICE_ATTRIBUTE_TEDS_HWTEDS_SUPPORTED = 12246;
  DEVICE_ATTRIBUTE_TIME_TRIG_SUPPORTED = 12319;
  DEVICE_ATTRIBUTE_CI_UTC_OFFSET_READY = 12321;
  DEVICE_ATTRIBUTE_NAV_HAS_FIX = 12333;
  DEVICE_ATTRIBUTE_NAV_UTC_OFFSET_READY = 12335;
}

enum DeviceInt32Attribute {
  DEVICE_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_BUS_TYPE = 8998;
  DEVICE_ATTRIBUTE_AI_TRIG_USAGE = 10630;
  DEVICE_ATTRIBUTE_AO_TRIG_USAGE = 10631;
  DEVICE_ATTRIBUTE_DI_TRIG_USAGE = 10632;
  DEVICE_ATTRIBUTE_DO_TRIG_USAGE = 10633;
  DEVICE_ATTRIBUTE_CI_TRIG_USAGE = 10634;
  DEVICE_ATTRIBUTE_CO_TRIG_USAGE = 10635;
  DEVICE_ATTRIBUTE_AI_COUPLINGS = 10644;
  DEVICE_ATTRIBUTE_PRODUCT_CATEGORY = 10665;
  DEVICE_ATTRIBUTE_CI_CURRENT_UTC_OFFSET = 12320;
  DEVICE_ATTRIBUTE_NAV_MODE = 12325;
  DEVICE_ATTRIBUTE_NAV_ALT_REF = 12329;
  DEVICE_ATTRIBUTE_NAV_ANT_STATUS = 12334;
  DEVICE_ATTRIBUTE_NAV_CURRENT_UTC_OFFSET = 12336;
}

enum DeviceDoubleAttribute {
  DEVICE_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_AI_MAX_SINGLE_CHAN_RATE = 10636;
  DEVICE_ATTRIBUTE_AI_MAX_MULTI_CHAN_RATE = 10637;
  DEVICE_ATTRIBUTE_AI_MIN_RATE = 10638;
  DEVICE_ATTRIBUTE_AO_MAX_RATE = 10647;
  DEVICE_ATTRIBUTE_AO_MIN_RATE = 10648;
  DEVICE_ATTRIBUTE_DI_MAX_RATE = 10649;
  DEVICE_ATTRIBUTE_DO_MAX_RATE = 10650;
  DEVICE_ATTRIBUTE_CI_MAX_TIMEBASE = 10656;
  DEVICE_ATTRIBUTE_CO_MAX_TIMEBASE = 10658;
  DEVICE_ATTRIBUTE_NAV_PRESET_LAT = 12326;
  DEVICE_ATTRIBUTE_NAV_PRESET_LONG = 12327;
  DEVICE_ATTRIBUTE_NAV_PRESET_ALT = 12328;
  DEVICE_ATTRIBUTE_NAV_PPS_COMPEN = 12330;
  DEVICE_ATTRIBUTE_NAV_PDOP = 12338;
  DEVICE_ATTRIBUTE_NAV_HDOP = 12339;
  DEVICE_ATTRIBUTE_NAV_VDOP = 12340;
}

enum DeviceDoubleArrayAttribute {
  DEVICE_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_AI_VOLTAGE_RNGS = 10640;
  DEVICE_ATTRIBUTE_AI_CURRENT_RNGS = 10641;
  DEVICE_ATTRIBUTE_AI_FREQ_RNGS = 10642;
  DEVICE_ATTRIBUTE_AI_GAINS = 10643;
  DEVICE_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ_DISCRETE_VALS = 10645;
  DEVICE_ATTRIBUTE_AO_VOLTAGE_RNGS = 10651;
  DEVICE_ATTRIBUTE_AO_CURRENT_RNGS = 10652;
  DEVICE_ATTRIBUTE_AO_GAINS = 10653;
  DEVICE_ATTRIBUTE_AI_VOLTAGE_INT_EXCIT_DISCRETE_VALS = 10697;
  DEVICE_ATTRIBUTE_AI_VOLTAGE_INT_EXCIT_RANGE_VALS = 10698;
  DEVICE_ATTRIBUTE_AI_CURRENT_INT_EXCIT_DISCRETE_VALS = 10699;
  DEVICE_ATTRIBUTE_AI_LOWPASS_CUTOFF_FREQ_RANGE_VALS = 10703;
  DEVICE_ATTRIBUTE_AI_RESISTANCE_RNGS = 10773;
  DEVICE_ATTRIBUTE_AI_BRIDGE_RNGS = 12240;
  DEVICE_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ_DISCRETE_VALS = 12488;
  DEVICE_ATTRIBUTE_AI_DIG_FLTR_LOWPASS_CUTOFF_FREQ_RANGE_VALS = 12489;
  DEVICE_ATTRIBUTE_AI_CHARGE_RNGS = 12561;
}

enum DeviceUInt32ArrayAttribute {
  DEVICE_UINT32_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_ACCESSORY_PRODUCT_NUMS = 12142;
  DEVICE_ATTRIBUTE_ACCESSORY_SERIAL_NUMS = 12143;
  DEVICE_ATTRIBUTE_ID_PIN_MEM_FAMILY_CODES = 12787;
  DEVICE_ATTRIBUTE_ID_PIN_MEM_SIZES = 12789;
}

enum DeviceInt32ArrayAttribute {
  DEVICE_INT32_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  DEVICE_ATTRIBUTE_AI_SUPPORTED_MEAS_TYPES = 12242;
  DEVICE_ATTRIBUTE_AO_SUPPORTED_OUTPUT_TYPES = 12243;
  DEVICE_ATTRIBUTE_CI_SUPPORTED_MEAS_TYPES = 12244;
  DEVICE_ATTRIBUTE_CO_SUPPORTED_OUTPUT_TYPES = 12245;
  DEVICE_ATTRIBUTE_AI_SAMP_MODES = 12252;
  DEVICE_ATTRIBUTE_AO_SAMP_MODES = 12253;
  DEVICE_ATTRIBUTE_CI_SAMP_MODES = 12254;
  DEVICE_ATTRIBUTE_CO_SAMP_MODES = 12255;
  DEVICE_ATTRIBUTE_NAV_SUPPORTED_MEAS_TYPES = 12323;
  DEVICE_ATTRIBUTE_NAV_TRIG_USAGE = 12324;
  DEVICE_ATTRIBUTE_AI_DIG_FLTR_TYPES = 12551;
  DEVICE_ATTRIBUTE_ID_PIN_PIN_STATUSES = 12786;
}

enum ExportSignalDoubleAttribute {
  EXPORTSIGNAL_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_DELAY = 1409;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_PULSE_WIDTH = 1414;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_WIDTH = 5668;
  EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH = 5704;
  EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH = 5716;
  EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_WIDTH = 5728;
  EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_PULSE_WIDTH = 5734;
  EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_PULSE_WIDTH = 5776;
  EXPORTSIGNAL_ATTRIBUTE_FREQ_OUT_CLK_PULSE_WIDTH = 5908;
  EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_PULSE_WIDTH = 5920;
  EXPORTSIGNAL_ATTRIBUTE_REF_CLK_PULSE_WIDTH = 5944;
  EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_DELAY = 5975;
  EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_DELAY_OFFSET = 8644;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_DELAY = 8892;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_DEASSERT_DELAY = 8895;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_PULSE_WIDTH = 8897;
}

enum ExportSignalStringAttribute {
  EXPORTSIGNAL_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_OUTPUT_TERM = 1412;
  EXPORTSIGNAL_ATTRIBUTE_REF_TRIG_OUTPUT_TERM = 1424;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_START_EVENT_OUTPUT_TERM = 5641;
  EXPORTSIGNAL_ATTRIBUTE_PAUSE_TRIG_OUTPUT_TERM = 5653;
  EXPORTSIGNAL_ATTRIBUTE_DATA_ACTIVE_EVENT_OUTPUT_TERM = 5683;
  EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_OUTPUT_TERM = 5701;
  EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_OUTPUT_TERM = 5713;
  EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_OUTPUT_TERM = 5719;
  EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_OUTPUT_TERM = 5731;
  EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_OUTPUT_TERM = 5767;
  EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_TERM = 5911;
  EXPORTSIGNAL_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_OUTPUT_TERM = 6381;
  EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_TIMEBASE_OUTPUT_TERM = 6393;
  EXPORTSIGNAL_ATTRIBUTE_CHANGE_DETECT_EVENT_OUTPUT_TERM = 8599;
  EXPORTSIGNAL_ATTRIBUTE_DIVIDED_SAMP_CLK_TIMEBASE_OUTPUT_TERM = 8609;
  EXPORTSIGNAL_ATTRIBUTE_WATCHDOG_EXPIRED_EVENT_OUTPUT_TERM = 8618;
  EXPORTSIGNAL_ATTRIBUTE_SYNC_PULSE_EVENT_OUTPUT_TERM = 8764;
  EXPORTSIGNAL_ATTRIBUTE_10_MHZ_REF_CLK_OUTPUT_TERM = 8814;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_OUTPUT_TERM = 8885;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_OUTPUT_TERM = 8890;
}

enum ExportSignalResetAttribute {
  EXPORTSIGNAL_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_OUTPUT_TERM = 1412;
  EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_PULSE_POLARITY = 1413;
  EXPORTSIGNAL_RESET_ATTRIBUTE_REF_TRIG_OUTPUT_TERM = 1424;
  EXPORTSIGNAL_RESET_ATTRIBUTE_REF_TRIG_PULSE_POLARITY = 1425;
  EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_PULSE_WIDTH_UNITS = 5634;
  EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_START_EVENT_OUTPUT_TERM = 5641;
  EXPORTSIGNAL_RESET_ATTRIBUTE_PAUSE_TRIG_OUTPUT_TERM = 5653;
  EXPORTSIGNAL_RESET_ATTRIBUTE_PAUSE_TRIG_LVL_ACTIVE_LVL = 5654;
  EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_WIDTH_UNITS = 5667;
  EXPORTSIGNAL_RESET_ATTRIBUTE_DATA_ACTIVE_EVENT_OUTPUT_TERM = 5683;
  EXPORTSIGNAL_RESET_ATTRIBUTE_DATA_ACTIVE_EVENT_LVL_ACTIVE_LVL = 5684;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_TRIG_OUTPUT_TERM = 5701;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH_UNITS = 5703;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH = 5704;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_ENABLE = 5706;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_OUTPUT_TERM = 5713;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_POLARITY = 5714;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH_UNITS = 5715;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH = 5716;
  EXPORTSIGNAL_RESET_ATTRIBUTE_20_MHZ_TIMEBASE_DIVIDE_DOWN_BY_N = 5718;
  EXPORTSIGNAL_RESET_ATTRIBUTE_20_MHZ_TIMEBASE_OUTPUT_TERM = 5719;
  EXPORTSIGNAL_RESET_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_WIDTH_UNITS = 5721;
  EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_OUTPUT_TERM = 5731;
  EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_PULSE_POLARITY = 5732;
  EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_PULSE_WIDTH_UNITS = 5733;
  EXPORTSIGNAL_RESET_ATTRIBUTE_AI_CONV_CLK_OUTPUT_TERM = 5767;
  EXPORTSIGNAL_RESET_ATTRIBUTE_AI_CONV_CLK_PULSE_WIDTH_UNITS = 5769;
  EXPORTSIGNAL_RESET_ATTRIBUTE_FREQ_OUT_CLK_PULSE_WIDTH_UNITS = 5907;
  EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_TERM = 5911;
  EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_PULSE_POLARITY = 5912;
  EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_PULSE_WIDTH_UNITS = 5913;
  EXPORTSIGNAL_RESET_ATTRIBUTE_REF_CLK_PULSE_WIDTH_UNITS = 5943;
  EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_OUTPUT_BEHAVIOR = 5955;
  EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_TOGGLE_INITIAL_STATE = 5956;
  EXPORTSIGNAL_RESET_ATTRIBUTE_START_TRIG_DELAY_UNITS = 5965;
  EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_BEHAVIOR = 5967;
  EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_START_EVENT_LVL_ACTIVE_LVL = 5969;
  EXPORTSIGNAL_RESET_ATTRIBUTE_ADV_CMPLT_EVENT_DELAY = 5975;
  EXPORTSIGNAL_RESET_ATTRIBUTE_CTR_OUT_EVENT_TOGGLE_IDLE_STATE = 6250;
  EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_OUTPUT_BEHAVIOR = 6251;
  EXPORTSIGNAL_RESET_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_OUTPUT_TERM = 6381;
  EXPORTSIGNAL_RESET_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_PULSE_POLARITY = 6382;
  EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_OUTPUT_TERM = 6393;
  EXPORTSIGNAL_RESET_ATTRIBUTE_CHANGE_DETECT_EVENT_OUTPUT_TERM = 8599;
  EXPORTSIGNAL_RESET_ATTRIBUTE_DIVIDED_SAMP_CLK_TIMEBASE_OUTPUT_TERM = 8609;
  EXPORTSIGNAL_RESET_ATTRIBUTE_WATCHDOG_EXPIRED_EVENT_OUTPUT_TERM = 8618;
  EXPORTSIGNAL_RESET_ATTRIBUTE_SAMP_CLK_DELAY_OFFSET = 8644;
  EXPORTSIGNAL_RESET_ATTRIBUTE_SYNC_PULSE_EVENT_OUTPUT_TERM = 8764;
  EXPORTSIGNAL_RESET_ATTRIBUTE_10_MHZ_REF_CLK_OUTPUT_TERM = 8814;
  EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_OUTPUT_TERM = 8885;
  EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_LVL_ACTIVE_LVL = 8886;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_OUTPUT_TERM = 8890;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_OUTPUT_BEHAVIOR = 8891;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_DELAY = 8892;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERTED_LVL = 8893;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERT_ON_START = 8894;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_DEASSERT_DELAY = 8895;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_PULSE_POLARITY = 8896;
  EXPORTSIGNAL_RESET_ATTRIBUTE_HSHK_EVENT_PULSE_WIDTH = 8897;
  EXPORTSIGNAL_RESET_ATTRIBUTE_CHANGE_DETECT_EVENT_PULSE_POLARITY = 8963;
  EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND = 10595;
  EXPORTSIGNAL_RESET_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND_CUSTOM_THRESHOLD = 10596;
}

enum ExportSignalInt32Attribute {
  EXPORTSIGNAL_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_PULSE_POLARITY = 1413;
  EXPORTSIGNAL_ATTRIBUTE_REF_TRIG_PULSE_POLARITY = 1425;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_PULSE_WIDTH_UNITS = 5634;
  EXPORTSIGNAL_ATTRIBUTE_PAUSE_TRIG_LVL_ACTIVE_LVL = 5654;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_POLARITY = 5666;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_REF_EVENT_PULSE_WIDTH_UNITS = 5667;
  EXPORTSIGNAL_ATTRIBUTE_DATA_ACTIVE_EVENT_LVL_ACTIVE_LVL = 5684;
  EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_PULSE_POLARITY = 5702;
  EXPORTSIGNAL_ATTRIBUTE_ADV_TRIG_PULSE_WIDTH_UNITS = 5703;
  EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_POLARITY = 5714;
  EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_PULSE_WIDTH_UNITS = 5715;
  EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_POLARITY = 5720;
  EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_PULSE_WIDTH_UNITS = 5721;
  EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_PULSE_POLARITY = 5732;
  EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_PULSE_WIDTH_UNITS = 5733;
  EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_PULSE_POLARITY = 5768;
  EXPORTSIGNAL_ATTRIBUTE_AI_CONV_CLK_PULSE_WIDTH_UNITS = 5769;
  EXPORTSIGNAL_ATTRIBUTE_FREQ_OUT_CLK_PULSE_POLARITY = 5906;
  EXPORTSIGNAL_ATTRIBUTE_FREQ_OUT_CLK_PULSE_WIDTH_UNITS = 5907;
  EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_PULSE_POLARITY = 5912;
  EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_PULSE_WIDTH_UNITS = 5913;
  EXPORTSIGNAL_ATTRIBUTE_REF_CLK_PULSE_POLARITY = 5942;
  EXPORTSIGNAL_ATTRIBUTE_REF_CLK_PULSE_WIDTH_UNITS = 5943;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_OUTPUT_BEHAVIOR = 5955;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_TOGGLE_INITIAL_STATE = 5956;
  EXPORTSIGNAL_ATTRIBUTE_START_TRIG_DELAY_UNITS = 5965;
  EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_OUTPUT_BEHAVIOR = 5967;
  EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_LVL_POLARITY = 5968;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_START_EVENT_LVL_ACTIVE_LVL = 5969;
  EXPORTSIGNAL_ATTRIBUTE_CTR_OUT_EVENT_TOGGLE_IDLE_STATE = 6250;
  EXPORTSIGNAL_ATTRIBUTE_SAMP_CLK_OUTPUT_BEHAVIOR = 6251;
  EXPORTSIGNAL_ATTRIBUTE_AI_HOLD_CMPLT_EVENT_PULSE_POLARITY = 6382;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_LVL_ACTIVE_LVL = 8886;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_OUTPUT_BEHAVIOR = 8891;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERTED_LVL = 8893;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_PULSE_POLARITY = 8896;
  EXPORTSIGNAL_ATTRIBUTE_CHANGE_DETECT_EVENT_PULSE_POLARITY = 8963;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND = 10595;
}

enum ExportSignalBoolAttribute {
  EXPORTSIGNAL_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  EXPORTSIGNAL_ATTRIBUTE_ADV_CMPLT_EVENT_ENABLE = 5706;
  EXPORTSIGNAL_ATTRIBUTE_HSHK_EVENT_INTERLOCKED_ASSERT_ON_START = 8894;
}

enum ExportSignalUInt32Attribute {
  EXPORTSIGNAL_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  EXPORTSIGNAL_ATTRIBUTE_20_MHZ_TIMEBASE_DIVIDE_DOWN_BY_N = 5718;
  EXPORTSIGNAL_ATTRIBUTE_RDY_FOR_XFER_EVENT_DEASSERT_COND_CUSTOM_THRESHOLD = 10596;
}

enum PersistedChannelStringAttribute {
  PERSISTEDCHANNEL_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  PERSISTEDCHANNEL_ATTRIBUTE_ACTIVE_CHAN = 8911;
  PERSISTEDCHANNEL_ATTRIBUTE_AUTHOR = 8912;
}

enum PersistedChannelBoolAttribute {
  PERSISTEDCHANNEL_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  PERSISTEDCHANNEL_ATTRIBUTE_ALLOW_INTERACTIVE_EDITING = 8913;
  PERSISTEDCHANNEL_ATTRIBUTE_ALLOW_INTERACTIVE_DELETION = 8914;
}

enum PersistedScaleStringAttribute {
  PERSISTEDSCALE_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  PERSISTEDSCALE_ATTRIBUTE_ACTIVE_SCALE = 8915;
  PERSISTEDSCALE_ATTRIBUTE_AUTHOR = 8916;
}

enum PersistedScaleBoolAttribute {
  PERSISTEDSCALE_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  PERSISTEDSCALE_ATTRIBUTE_ALLOW_INTERACTIVE_EDITING = 8917;
  PERSISTEDSCALE_ATTRIBUTE_ALLOW_INTERACTIVE_DELETION = 8918;
}

enum PersistedTaskStringAttribute {
  PERSISTEDTASK_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  PERSISTEDTASK_ATTRIBUTE_ACTIVE_TASK = 8907;
  PERSISTEDTASK_ATTRIBUTE_AUTHOR = 8908;
}

enum PersistedTaskBoolAttribute {
  PERSISTEDTASK_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  PERSISTEDTASK_ATTRIBUTE_ALLOW_INTERACTIVE_EDITING = 8909;
  PERSISTEDTASK_ATTRIBUTE_ALLOW_INTERACTIVE_DELETION = 8910;
}

enum PhysicalChannelUInt32Attribute {
  PHYSICALCHANNEL_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_MFG_ID = 8666;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_MODEL_NUM = 8667;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_SERIAL_NUM = 8668;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_VERSION_NUM = 8669;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_PORT_WIDTH = 10660;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DO_PORT_WIDTH = 10663;
}

enum PhysicalChannelStringAttribute {
  PHYSICALCHANNEL_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_VERSION_LETTER = 8670;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_INPUT_SRCS = 12248;
}

enum PhysicalChannelBytesAttribute {
  PHYSICALCHANNEL_BYTES_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_BIT_STREAM = 8671;
}

enum PhysicalChannelUInt32ArrayAttribute {
  PHYSICALCHANNEL_UINT32_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_TEDS_TEMPLATE_I_DS = 8847;
}

enum PhysicalChannelInt32Attribute {
  PHYSICALCHANNEL_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_TERM_CFGS = 9026;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_TERM_CFGS = 10659;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_TYPE = 12654;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DIG_PORT_LOGIC_FAMILY = 12779;
}

enum PhysicalChannelBoolAttribute {
  PHYSICALCHANNEL_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_SAMP_CLK_SUPPORTED = 10661;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_CHANGE_DETECT_SUPPORTED = 10662;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DO_SAMP_CLK_SUPPORTED = 10664;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_ENABLE = 10782;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_SHORT_DETECTED = 11971;
  PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_CHANNEL_ENABLE = 12386;
  PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_OVERCURRENT = 12388;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_ENABLE = 12653;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_OPEN_CHAN = 12668;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_OVERCURRENT = 12669;
}

enum PhysicalChannelResetAttribute {
  PHYSICALCHANNEL_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_ENABLE = 10782;
  PHYSICALCHANNEL_RESET_ATTRIBUTE_AO_POWER_AMP_CHANNEL_ENABLE = 12386;
  PHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_VOLTAGE = 12652;
  PHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_ENABLE = 12653;
  PHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_TYPE = 12654;
  PHYSICALCHANNEL_RESET_ATTRIBUTE_PHYSICAL_CHAN_DIG_PORT_LOGIC_FAMILY = 12779;
}

enum PhysicalChannelDoubleAttribute {
  PHYSICALCHANNEL_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_AMPLITUDE = 10783;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_MANUAL_CONTROL_FREQ = 10784;
  PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_GAIN = 12389;
  PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_OFFSET = 12390;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_POWER_CONTROL_VOLTAGE = 12652;
}

enum PhysicalChannelInt32ArrayAttribute {
  PHYSICALCHANNEL_INT32_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SUPPORTED_MEAS_TYPES = 12247;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_SUPPORTED_OUTPUT_TYPES = 12249;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_CI_SUPPORTED_MEAS_TYPES = 12250;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_CO_SUPPORTED_OUTPUT_TYPES = 12251;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DI_SAMP_MODES = 12256;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_DO_SAMP_MODES = 12257;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_NAV_SUPPORTED_MEAS_TYPES = 12343;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AO_SUPPORTED_POWER_UP_OUTPUT_TYPES = 12366;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_TYPES = 12665;
}

enum PhysicalChannelDoubleArrayAttribute {
  PHYSICALCHANNEL_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  PHYSICALCHANNEL_ATTRIBUTE_AO_POWER_AMP_SCALING_COEFF = 12387;
  PHYSICALCHANNEL_ATTRIBUTE_PHYSICAL_CHAN_AI_SENSOR_POWER_VOLTAGE_RANGE_VALS = 12666;
}

enum ReadInt32Attribute {
  READ_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  READ_ATTRIBUTE_OVERWRITE = 4625;
  READ_ATTRIBUTE_RELATIVE_TO = 6410;
  READ_ATTRIBUTE_OFFSET = 6411;
  READ_ATTRIBUTE_WAIT_MODE = 8754;
  READ_ATTRIBUTE_LOGGING_MODE = 11973;
  READ_ATTRIBUTE_LOGGING_TDMS_OPERATION = 11975;
}

enum ReadResetAttribute {
  READ_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  READ_RESET_ATTRIBUTE_OVERWRITE = 4625;
  READ_RESET_ATTRIBUTE_READ_ALL_AVAIL_SAMP = 4629;
  READ_RESET_ATTRIBUTE_CHANNELS_TO_READ = 6179;
  READ_RESET_ATTRIBUTE_AUTO_START = 6182;
  READ_RESET_ATTRIBUTE_RELATIVE_TO = 6410;
  READ_RESET_ATTRIBUTE_OFFSET = 6411;
  READ_RESET_ATTRIBUTE_WAIT_MODE = 8754;
  READ_RESET_ATTRIBUTE_SLEEP_TIME = 8880;
  READ_RESET_ATTRIBUTE_LOGGING_FILE_PATH = 11972;
  READ_RESET_ATTRIBUTE_LOGGING_MODE = 11973;
  READ_RESET_ATTRIBUTE_LOGGING_TDMS_GROUP_NAME = 11974;
  READ_RESET_ATTRIBUTE_LOGGING_TDMS_OPERATION = 11975;
  READ_RESET_ATTRIBUTE_LOGGING_FILE_WRITE_SIZE = 12227;
  READ_RESET_ATTRIBUTE_LOGGING_FILE_PREALLOCATION_SIZE = 12230;
  READ_RESET_ATTRIBUTE_LOGGING_PAUSE = 12259;
  READ_RESET_ATTRIBUTE_LOGGING_SAMPS_PER_FILE = 12260;
}

enum ReadBoolAttribute {
  READ_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  READ_ATTRIBUTE_READ_ALL_AVAIL_SAMP = 4629;
  READ_ATTRIBUTE_AUTO_START = 6182;
  READ_ATTRIBUTE_OVERLOADED_CHANS_EXIST = 8564;
  READ_ATTRIBUTE_CHANGE_DETECT_HAS_OVERFLOWED = 8596;
  READ_ATTRIBUTE_OVERCURRENT_CHANS_EXIST = 10726;
  READ_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS_EXIST = 10761;
  READ_ATTRIBUTE_OPEN_THRMCPL_CHANS_EXIST = 10902;
  READ_ATTRIBUTE_COMMON_MODE_RANGE_ERROR_CHANS_EXIST = 10904;
  READ_ATTRIBUTE_ACCESSORY_INSERTION_OR_REMOVAL_DETECTED = 12144;
  READ_ATTRIBUTE_LOGGING_PAUSE = 12259;
  READ_ATTRIBUTE_NAV_FIX_LOST = 12341;
  READ_ATTRIBUTE_OVERTEMPERATURE_CHANS_EXIST = 12417;
  READ_ATTRIBUTE_EXCIT_FAULT_CHANS_EXIST = 12424;
  READ_ATTRIBUTE_OPEN_CHANS_EXIST = 12544;
  READ_ATTRIBUTE_PLL_UNLOCKED_CHANS_EXIST = 12568;
  READ_ATTRIBUTE_SYNC_UNLOCKED_CHANS_EXIST = 12605;
  READ_ATTRIBUTE_INPUT_LIMITS_FAULT_CHANS_EXIST = 12687;
  READ_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS_EXIST = 12690;
  READ_ATTRIBUTE_REMOTE_SENSE_ERROR_CHANS_EXIST = 12765;
  READ_ATTRIBUTE_AUX_POWER_ERROR_CHANS_EXIST = 12767;
  READ_ATTRIBUTE_REVERSE_VOLTAGE_ERROR_CHANS_EXIST = 12774;
}

enum ReadUInt64Attribute {
  READ_UINT64_ATTRIBUTE_UNSPECIFIED = 0;
  READ_ATTRIBUTE_CURR_READ_POS = 4641;
  READ_ATTRIBUTE_TOTAL_SAMP_PER_CHAN_ACQUIRED = 6442;
  READ_ATTRIBUTE_LOGGING_FILE_PREALLOCATION_SIZE = 12230;
  READ_ATTRIBUTE_LOGGING_SAMPS_PER_FILE = 12260;
}

enum ReadUInt32Attribute {
  READ_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  READ_ATTRIBUTE_AVAIL_SAMP_PER_CHAN = 4643;
  READ_ATTRIBUTE_RAW_DATA_WIDTH = 8570;
  READ_ATTRIBUTE_NUM_CHANS = 8571;
  READ_ATTRIBUTE_DIGITAL_LINES_BYTES_PER_CHAN = 8572;
  READ_ATTRIBUTE_LOGGING_FILE_WRITE_SIZE = 12227;
}

enum ReadStringAttribute {
  READ_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  READ_ATTRIBUTE_CHANNELS_TO_READ = 6179;
  READ_ATTRIBUTE_OVERLOADED_CHANS = 8565;
  READ_ATTRIBUTE_OVERCURRENT_CHANS = 10727;
  READ_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS = 10762;
  READ_ATTRIBUTE_OPEN_THRMCPL_CHANS = 10903;
  READ_ATTRIBUTE_COMMON_MODE_RANGE_ERROR_CHANS = 10905;
  READ_ATTRIBUTE_LOGGING_FILE_PATH = 11972;
  READ_ATTRIBUTE_LOGGING_TDMS_GROUP_NAME = 11974;
  READ_ATTRIBUTE_DEVS_WITH_INSERTED_OR_REMOVED_ACCESSORIES = 12145;
  READ_ATTRIBUTE_OVERTEMPERATURE_CHANS = 12418;
  READ_ATTRIBUTE_EXCIT_FAULT_CHANS = 12425;
  READ_ATTRIBUTE_OPEN_CHANS = 12545;
  READ_ATTRIBUTE_OPEN_CHANS_DETAILS = 12546;
  READ_ATTRIBUTE_PLL_UNLOCKED_CHANS = 12569;
  READ_ATTRIBUTE_SYNC_UNLOCKED_CHANS = 12606;
  READ_ATTRIBUTE_INPUT_LIMITS_FAULT_CHANS = 12688;
  READ_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS = 12691;
  READ_ATTRIBUTE_REMOTE_SENSE_ERROR_CHANS = 12766;
  READ_ATTRIBUTE_AUX_POWER_ERROR_CHANS = 12768;
  READ_ATTRIBUTE_REVERSE_VOLTAGE_ERROR_CHANS = 12775;
}

enum ReadDoubleAttribute {
  READ_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  READ_ATTRIBUTE_SLEEP_TIME = 8880;
}

enum RealTimeUInt32Attribute {
  REALTIME_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  REALTIME_ATTRIBUTE_NUM_OF_WARMUP_ITERS = 8941;
}

enum RealTimeResetAttribute {
  REALTIME_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  REALTIME_RESET_ATTRIBUTE_NUM_OF_WARMUP_ITERS = 8941;
  REALTIME_RESET_ATTRIBUTE_CONV_LATE_ERRORS_TO_WARNINGS = 8942;
  REALTIME_RESET_ATTRIBUTE_WAIT_FOR_NEXT_SAMP_CLK_WAIT_MODE = 8943;
  REALTIME_RESET_ATTRIBUTE_REPORT_MISSED_SAMP = 8985;
  REALTIME_RESET_ATTRIBUTE_WRITE_RECOVERY_MODE = 8986;
}

enum RealTimeBoolAttribute {
  REALTIME_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  REALTIME_ATTRIBUTE_CONV_LATE_ERRORS_TO_WARNINGS = 8942;
  REALTIME_ATTRIBUTE_REPORT_MISSED_SAMP = 8985;
}

enum RealTimeInt32Attribute {
  REALTIME_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  REALTIME_ATTRIBUTE_WAIT_FOR_NEXT_SAMP_CLK_WAIT_MODE = 8943;
  REALTIME_ATTRIBUTE_WRITE_RECOVERY_MODE = 8986;
}

enum ScaleStringAttribute {
  SCALE_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  SCALE_ATTRIBUTE_DESCR = 4646;
  SCALE_ATTRIBUTE_SCALED_UNITS = 6427;
}

enum ScaleDoubleAttribute {
  SCALE_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  SCALE_ATTRIBUTE_LIN_SLOPE = 4647;
  SCALE_ATTRIBUTE_LIN_Y_INTERCEPT = 4648;
  SCALE_ATTRIBUTE_MAP_SCALED_MAX = 4649;
  SCALE_ATTRIBUTE_MAP_SCALED_MIN = 4656;
  SCALE_ATTRIBUTE_MAP_PRE_SCALED_MAX = 4657;
  SCALE_ATTRIBUTE_MAP_PRE_SCALED_MIN = 4658;
}

enum ScaleDoubleArrayAttribute {
  SCALE_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  SCALE_ATTRIBUTE_POLY_FORWARD_COEFF = 4660;
  SCALE_ATTRIBUTE_POLY_REVERSE_COEFF = 4661;
  SCALE_ATTRIBUTE_TABLE_SCALED_VALS = 4662;
  SCALE_ATTRIBUTE_TABLE_PRE_SCALED_VALS = 4663;
}

enum ScaleInt32Attribute {
  SCALE_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  SCALE_ATTRIBUTE_PRE_SCALED_UNITS = 6391;
  SCALE_ATTRIBUTE_TYPE = 6441;
}

enum SystemStringAttribute {
  SYSTEM_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  SYSTEM_ATTRIBUTE_GLOBAL_CHANS = 4709;
  SYSTEM_ATTRIBUTE_SCALES = 4710;
  SYSTEM_ATTRIBUTE_TASKS = 4711;
  SYSTEM_ATTRIBUTE_DEV_NAMES = 6459;
}

enum SystemUInt32Attribute {
  SYSTEM_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  SYSTEM_ATTRIBUTE_NIDAQ_MAJOR_VERSION = 4722;
  SYSTEM_ATTRIBUTE_NIDAQ_MINOR_VERSION = 6435;
  SYSTEM_ATTRIBUTE_NIDAQ_UPDATE_VERSION = 12066;
}

enum TaskStringAttribute {
  TASK_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  TASK_ATTRIBUTE_CHANNELS = 4723;
  TASK_ATTRIBUTE_NAME = 4726;
  TASK_ATTRIBUTE_DEVICES = 8974;
}

enum TaskBoolAttribute {
  TASK_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  TASK_ATTRIBUTE_COMPLETE = 4724;
}

enum TaskUInt32Attribute {
  TASK_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  TASK_ATTRIBUTE_NUM_CHANS = 8577;
  TASK_ATTRIBUTE_NUM_DEVICES = 10682;
}

enum TimingInt32Attribute {
  TIMING_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_ATTRIBUTE_SAMP_QUANT_SAMP_MODE = 4864;
  TIMING_ATTRIBUTE_SAMP_CLK_ACTIVE_EDGE = 4865;
  TIMING_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY_UNITS = 4868;
  TIMING_ATTRIBUTE_AI_CONV_TIMEBASE_SRC = 4921;
  TIMING_ATTRIBUTE_SAMP_TIMING_TYPE = 4935;
  TIMING_ATTRIBUTE_AI_CONV_ACTIVE_EDGE = 6227;
  TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_ACTIVE_EDGE = 6380;
  TIMING_ATTRIBUTE_HSHK_START_COND = 8899;
  TIMING_ATTRIBUTE_HSHK_SAMPLE_INPUT_DATA_WHEN = 8900;
  TIMING_ATTRIBUTE_SAMP_CLK_UNDERFLOW_BEHAVIOR = 10593;
  TIMING_ATTRIBUTE_SAMP_CLK_OVERRUN_BEHAVIOR = 12028;
  TIMING_ATTRIBUTE_IMPLICIT_UNDERFLOW_BEHAVIOR = 12029;
  TIMING_ATTRIBUTE_SYNC_PULSE_TYPE = 12598;
  TIMING_ATTRIBUTE_SYNC_PULSE_TIME_TIMESCALE = 12600;
  TIMING_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_TIMESCALE = 12603;
  TIMING_ATTRIBUTE_FIRST_SAMP_CLK_TIMESCALE = 12675;
}

enum TimingResetAttribute {
  TIMING_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_RESET_ATTRIBUTE_SAMP_QUANT_SAMP_MODE = 4864;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_ACTIVE_EDGE = 4865;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_RATE = 4867;
  TIMING_RESET_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY_UNITS = 4868;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_MASTER_TIMEBASE_DIV = 4869;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC = 4872;
  TIMING_RESET_ATTRIBUTE_SAMP_QUANT_SAMP_PER_CHAN = 4880;
  TIMING_RESET_ATTRIBUTE_REF_CLK_RATE = 4885;
  TIMING_RESET_ATTRIBUTE_REF_CLK_SRC = 4886;
  TIMING_RESET_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY = 4887;
  TIMING_RESET_ATTRIBUTE_AI_CONV_TIMEBASE_DIV = 4917;
  TIMING_RESET_ATTRIBUTE_AI_CONV_TIMEBASE_SRC = 4921;
  TIMING_RESET_ATTRIBUTE_MASTER_TIMEBASE_SRC = 4931;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_RATE = 4932;
  TIMING_RESET_ATTRIBUTE_SAMP_TIMING_TYPE = 4935;
  TIMING_RESET_ATTRIBUTE_MASTER_TIMEBASE_RATE = 5269;
  TIMING_RESET_ATTRIBUTE_AI_CONV_SRC = 5378;
  TIMING_RESET_ATTRIBUTE_AI_CONV_RATE = 6216;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_SRC = 6226;
  TIMING_RESET_ATTRIBUTE_AI_CONV_ACTIVE_EDGE = 6227;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_DIV = 6379;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_TIMEBASE_ACTIVE_EDGE = 6380;
  TIMING_RESET_ATTRIBUTE_CHANGE_DETECT_DI_RISING_EDGE_PHYSICAL_CHANS = 8597;
  TIMING_RESET_ATTRIBUTE_CHANGE_DETECT_DI_FALLING_EDGE_PHYSICAL_CHANS = 8598;
  TIMING_RESET_ATTRIBUTE_ON_DEMAND_SIMULTANEOUS_AO_ENABLE = 8608;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_ENABLE = 8734;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_MIN_PULSE_WIDTH = 8735;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_SRC = 8736;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_RATE = 8737;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_DIG_SYNC_ENABLE = 8738;
  TIMING_RESET_ATTRIBUTE_SYNC_PULSE_SRC = 8765;
  TIMING_RESET_ATTRIBUTE_SYNC_PULSE_MIN_DELAY_TO_START = 8767;
  TIMING_RESET_ATTRIBUTE_HSHK_DELAY_AFTER_XFER = 8898;
  TIMING_RESET_ATTRIBUTE_HSHK_START_COND = 8899;
  TIMING_RESET_ATTRIBUTE_HSHK_SAMPLE_INPUT_DATA_WHEN = 8900;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_UNDERFLOW_BEHAVIOR = 10593;
  TIMING_RESET_ATTRIBUTE_SAMP_TIMING_ENGINE = 10790;
  TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_ENABLE = 11996;
  TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_MIN_PULSE_WIDTH = 11997;
  TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_SRC = 11998;
  TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_RATE = 11999;
  TIMING_RESET_ATTRIBUTE_AI_CONV_DIG_SYNC_ENABLE = 12000;
  TIMING_RESET_ATTRIBUTE_CHANGE_DETECT_DI_TRISTATE = 12026;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_OVERRUN_BEHAVIOR = 12028;
  TIMING_RESET_ATTRIBUTE_IMPLICIT_UNDERFLOW_BEHAVIOR = 12029;
  TIMING_RESET_ATTRIBUTE_SYNC_PULSE_RESET_DELAY = 12157;
  TIMING_RESET_ATTRIBUTE_SYNC_CLK_INTERVAL = 12158;
  TIMING_RESET_ATTRIBUTE_TIMING_SYNC_PULSE_FORCE = 12474;
  TIMING_RESET_ATTRIBUTE_SAMP_CLK_WRITE_WFM_USE_INITIAL_WFM_DT = 12540;
  TIMING_RESET_ATTRIBUTE_SYNC_PULSE_TYPE = 12598;
  TIMING_RESET_ATTRIBUTE_SYNC_PULSE_TIME_WHEN = 12599;
  TIMING_RESET_ATTRIBUTE_SYNC_PULSE_TIME_TIMESCALE = 12600;
  TIMING_RESET_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_ENABLE = 12601;
  TIMING_RESET_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_TIMESCALE = 12603;
  TIMING_RESET_ATTRIBUTE_FIRST_SAMP_CLK_WHEN = 12674;
  TIMING_RESET_ATTRIBUTE_FIRST_SAMP_CLK_TIMESCALE = 12675;
  TIMING_RESET_ATTRIBUTE_FIRST_SAMP_CLK_OFFSET = 12714;
}

enum TimingDoubleAttribute {
  TIMING_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_RATE = 4867;
  TIMING_ATTRIBUTE_REF_CLK_RATE = 4885;
  TIMING_ATTRIBUTE_DELAY_FROM_SAMP_CLK_DELAY = 4887;
  TIMING_ATTRIBUTE_SAMP_CLK_RATE = 4932;
  TIMING_ATTRIBUTE_MASTER_TIMEBASE_RATE = 5269;
  TIMING_ATTRIBUTE_AI_CONV_RATE = 6216;
  TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_MIN_PULSE_WIDTH = 8735;
  TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_RATE = 8737;
  TIMING_ATTRIBUTE_SYNC_PULSE_SYNC_TIME = 8766;
  TIMING_ATTRIBUTE_SYNC_PULSE_MIN_DELAY_TO_START = 8767;
  TIMING_ATTRIBUTE_HSHK_DELAY_AFTER_XFER = 8898;
  TIMING_ATTRIBUTE_SAMP_CLK_MAX_RATE = 8904;
  TIMING_ATTRIBUTE_AI_CONV_MAX_RATE = 8905;
  TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_MIN_PULSE_WIDTH = 11997;
  TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_RATE = 11999;
  TIMING_ATTRIBUTE_SYNC_PULSE_RESET_TIME = 12156;
  TIMING_ATTRIBUTE_SYNC_PULSE_RESET_DELAY = 12157;
  TIMING_ATTRIBUTE_FIRST_SAMP_CLK_OFFSET = 12714;
}

enum TimingUInt32Attribute {
  TIMING_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_MASTER_TIMEBASE_DIV = 4869;
  TIMING_ATTRIBUTE_AI_CONV_TIMEBASE_DIV = 4917;
  TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_DIV = 6379;
  TIMING_ATTRIBUTE_SAMP_TIMING_ENGINE = 10790;
  TIMING_ATTRIBUTE_SYNC_CLK_INTERVAL = 12158;
}

enum TimingStringAttribute {
  TIMING_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC = 4872;
  TIMING_ATTRIBUTE_REF_CLK_SRC = 4886;
  TIMING_ATTRIBUTE_MASTER_TIMEBASE_SRC = 4931;
  TIMING_ATTRIBUTE_AI_CONV_SRC = 5378;
  TIMING_ATTRIBUTE_SAMP_CLK_SRC = 6226;
  TIMING_ATTRIBUTE_CHANGE_DETECT_DI_RISING_EDGE_PHYSICAL_CHANS = 8597;
  TIMING_ATTRIBUTE_CHANGE_DETECT_DI_FALLING_EDGE_PHYSICAL_CHANS = 8598;
  TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_TIMEBASE_SRC = 8736;
  TIMING_ATTRIBUTE_SYNC_PULSE_SRC = 8765;
  TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_TIMEBASE_SRC = 11998;
  TIMING_ATTRIBUTE_SAMP_CLK_TERM = 12059;
  TIMING_ATTRIBUTE_SAMP_CLK_TIMEBASE_TERM = 12060;
  TIMING_ATTRIBUTE_SYNC_PULSE_TERM = 12165;
}

enum TimingUInt64Attribute {
  TIMING_UINT64_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_ATTRIBUTE_SAMP_QUANT_SAMP_PER_CHAN = 4880;
}

enum TimingBoolAttribute {
  TIMING_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_ATTRIBUTE_ON_DEMAND_SIMULTANEOUS_AO_ENABLE = 8608;
  TIMING_ATTRIBUTE_SAMP_CLK_DIG_FLTR_ENABLE = 8734;
  TIMING_ATTRIBUTE_SAMP_CLK_DIG_SYNC_ENABLE = 8738;
  TIMING_ATTRIBUTE_AI_CONV_DIG_FLTR_ENABLE = 11996;
  TIMING_ATTRIBUTE_AI_CONV_DIG_SYNC_ENABLE = 12000;
  TIMING_ATTRIBUTE_CHANGE_DETECT_DI_TRISTATE = 12026;
  TIMING_ATTRIBUTE_TIMING_SYNC_PULSE_FORCE = 12474;
  TIMING_ATTRIBUTE_SAMP_CLK_WRITE_WFM_USE_INITIAL_WFM_DT = 12540;
  TIMING_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_ENABLE = 12601;
}

enum TimingTimestampAttribute {
  TIMING_TIMESTAMP_ATTRIBUTE_UNSPECIFIED = 0;
  TIMING_ATTRIBUTE_SYNC_PULSE_TIME_WHEN = 12599;
  TIMING_ATTRIBUTE_FIRST_SAMP_TIMESTAMP_VAL = 12602;
  TIMING_ATTRIBUTE_FIRST_SAMP_CLK_WHEN = 12674;
}

enum TriggerInt32Attribute {
  TRIGGER_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ADV_TRIG_EDGE = 4960;
  TRIGGER_ATTRIBUTE_ADV_TRIG_TYPE = 4965;
  TRIGGER_ATTRIBUTE_PAUSE_TRIG_TYPE = 4966;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_WHEN = 4977;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_WHEN = 4980;
  TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_WHEN = 4992;
  TRIGGER_ATTRIBUTE_START_TRIG_TYPE = 5011;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_SLOPE = 5015;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_WHEN = 5121;
  TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_EDGE = 5124;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_START_TRIG_WHEN = 5137;
  TRIGGER_ATTRIBUTE_ARM_START_TRIG_TYPE = 5140;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_EDGE = 5141;
  TRIGGER_ATTRIBUTE_REF_TRIG_TYPE = 5145;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SLOPE = 5155;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_WHEN = 5159;
  TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_EDGE = 5168;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_REF_TRIG_WHEN = 5176;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_COUPLING = 6231;
  TRIGGER_ATTRIBUTE_START_TRIG_DELAY_UNITS = 6344;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_WHEN = 8560;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_COUPLING = 8755;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_COUPLING = 8756;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_COUPLING = 8757;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_COUPLING = 8758;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_COUPLING = 8759;
  TRIGGER_ATTRIBUTE_HSHK_TRIG_TYPE = 8887;
  TRIGGER_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_ASSERTED_LVL = 8889;
  TRIGGER_ATTRIBUTE_TRIGGER_SYNC_TYPE = 12160;
  TRIGGER_ATTRIBUTE_START_TRIG_TIMESCALE = 12342;
  TRIGGER_ATTRIBUTE_START_TRIG_TIMESTAMP_TIMESCALE = 12589;
  TRIGGER_ATTRIBUTE_REF_TRIG_TIMESTAMP_TIMESCALE = 12592;
  TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESCALE = 12594;
  TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_TIMESCALE = 12597;
}

enum TriggerResetAttribute {
  TRIGGER_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ADV_TRIG_EDGE = 4960;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ADV_TRIG_SRC = 4962;
  TRIGGER_RESET_ATTRIBUTE_ADV_TRIG_TYPE = 4965;
  TRIGGER_RESET_ATTRIBUTE_PAUSE_TRIG_TYPE = 4966;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_HYST = 4968;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_LVL = 4969;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_SRC = 4976;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_WHEN = 4977;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_SRC = 4979;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_WHEN = 4980;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_BTM = 4981;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_TOP = 4982;
  TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_SRC = 4985;
  TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_WHEN = 4992;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_TYPE = 5011;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_HYST = 5013;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_LVL = 5014;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_SLOPE = 5015;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_SRC = 5016;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_SRC = 5120;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_WHEN = 5121;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_BTM = 5122;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_TOP = 5123;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_EDGE = 5124;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_SRC = 5127;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_START_TRIG_SRC = 5136;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_START_TRIG_WHEN = 5137;
  TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TYPE = 5140;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_EDGE = 5141;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_SRC = 5143;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TYPE = 5145;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_HYST = 5153;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_LVL = 5154;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SLOPE = 5155;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SRC = 5156;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_SRC = 5158;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_WHEN = 5159;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_BTM = 5160;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_TOP = 5161;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_EDGE = 5168;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_SRC = 5172;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_REF_TRIG_SRC = 5175;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_REF_TRIG_WHEN = 5176;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_PRETRIG_SAMPLES = 5189;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_DELAY = 5251;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_DELAY = 6230;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_COUPLING = 6231;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_DELAY_UNITS = 6344;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_RETRIGGERABLE = 6415;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_SRC = 8559;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_WHEN = 8560;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_START_TRIG_PATTERN = 8582;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_REF_TRIG_PATTERN = 8583;
  TRIGGER_RESET_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_PATTERN = 8584;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_ENABLE = 8739;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 8740;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 8741;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 8742;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_SYNC_ENABLE = 8743;
  TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE = 8744;
  TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 8745;
  TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC = 8746;
  TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE = 8747;
  TRIGGER_RESET_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE = 8748;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_ENABLE = 8749;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 8750;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 8751;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 8752;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_SYNC_ENABLE = 8753;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_COUPLING = 8755;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_COUPLING = 8756;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_COUPLING = 8757;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_COUPLING = 8758;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_COUPLING = 8759;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_ADV_TRIG_DIG_FLTR_ENABLE = 8760;
  TRIGGER_RESET_ATTRIBUTE_HSHK_TRIG_TYPE = 8887;
  TRIGGER_RESET_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_SRC = 8888;
  TRIGGER_RESET_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_ASSERTED_LVL = 8889;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_AUTO_TRIG_ENABLE = 11969;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_ENABLE = 11991;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 11992;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC = 11993;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE = 11994;
  TRIGGER_RESET_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_SYNC_ENABLE = 11995;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_ENABLE = 12001;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12002;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 12003;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 12004;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_SYNC_ENABLE = 12005;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_ENABLE = 12006;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12007;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC = 12008;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE = 12009;
  TRIGGER_RESET_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_SYNC_ENABLE = 12010;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_ENABLE = 12011;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12012;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_SRC = 12013;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_RATE = 12014;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_SYNC_ENABLE = 12015;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE = 12016;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12017;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC = 12018;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE = 12019;
  TRIGGER_RESET_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE = 12020;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_ENABLE = 12021;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12022;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC = 12023;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE = 12024;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_SYNC_ENABLE = 12025;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_ENABLE = 12031;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12032;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 12033;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 12034;
  TRIGGER_RESET_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_SYNC_ENABLE = 12035;
  TRIGGER_RESET_ATTRIBUTE_TRIGGER_SYNC_TYPE = 12160;
  TRIGGER_RESET_ATTRIBUTE_TIME_START_TRIG_SRC = 12317;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_TIMESCALE = 12342;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_TRIG_WHEN = 12365;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_TRIG_WIN = 12570;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_RETRIGGER_WIN = 12571;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_MAX_NUM_TRIGS_TO_DETECT = 12572;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_RETRIGGERABLE = 12573;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TRIG_WIN = 12574;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_RETRIGGER_WIN = 12575;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_MAX_NUM_TRIGS_TO_DETECT = 12576;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SRCS = 12577;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SLOPES = 12578;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_LVLS = 12579;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_HYSTS = 12580;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_COUPLINGS = 12581;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SRCS = 12582;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SLOPES = 12583;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_LVLS = 12584;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_HYSTS = 12585;
  TRIGGER_RESET_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_COUPLINGS = 12586;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_TIMESTAMP_TIMESCALE = 12589;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TIMESTAMP_ENABLE = 12590;
  TRIGGER_RESET_ATTRIBUTE_REF_TRIG_TIMESTAMP_TIMESCALE = 12592;
  TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TRIG_WHEN = 12593;
  TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TIMESCALE = 12594;
  TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_ENABLE = 12595;
  TRIGGER_RESET_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_TIMESCALE = 12597;
  TRIGGER_RESET_ATTRIBUTE_START_TRIG_TIMESTAMP_ENABLE = 12618;
}

enum TriggerStringAttribute {
  TRIGGER_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ADV_TRIG_SRC = 4962;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_SRC = 4976;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_SRC = 4979;
  TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_SRC = 4985;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_SRC = 5016;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_SRC = 5120;
  TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_SRC = 5127;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_START_TRIG_SRC = 5136;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_SRC = 5143;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_SRC = 5156;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_SRC = 5158;
  TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_SRC = 5172;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_REF_TRIG_SRC = 5175;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_SRC = 8559;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_START_TRIG_PATTERN = 8582;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_REF_TRIG_PATTERN = 8583;
  TRIGGER_ATTRIBUTE_DIG_PATTERN_PAUSE_TRIG_PATTERN = 8584;
  TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 8741;
  TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC = 8746;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 8751;
  TRIGGER_ATTRIBUTE_INTERLOCKED_HSHK_TRIG_SRC = 8888;
  TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC = 11993;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 12003;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_SRC = 12008;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_SRC = 12013;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC = 12018;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_SRC = 12023;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_SRC = 12033;
  TRIGGER_ATTRIBUTE_START_TRIG_TERM = 12062;
  TRIGGER_ATTRIBUTE_REF_TRIG_TERM = 12063;
  TRIGGER_ATTRIBUTE_PAUSE_TRIG_TERM = 12064;
  TRIGGER_ATTRIBUTE_ARM_START_TERM = 12159;
  TRIGGER_ATTRIBUTE_TIME_START_TRIG_SRC = 12317;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SRCS = 12577;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SRCS = 12582;
}

enum TriggerDoubleAttribute {
  TRIGGER_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_HYST = 4968;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_LVL = 4969;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_BTM = 4981;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_TOP = 4982;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_HYST = 5013;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_LVL = 5014;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_BTM = 5122;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_TOP = 5123;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_HYST = 5153;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_LVL = 5154;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_BTM = 5160;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_TOP = 5161;
  TRIGGER_ATTRIBUTE_REF_TRIG_DELAY = 5251;
  TRIGGER_ATTRIBUTE_START_TRIG_DELAY = 6230;
  TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 8740;
  TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 8742;
  TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 8745;
  TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE = 8747;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 8750;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 8752;
  TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 11992;
  TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE = 11994;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12002;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 12004;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12007;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_TIMEBASE_RATE = 12009;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12012;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_TIMEBASE_RATE = 12014;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12017;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE = 12019;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12022;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_TIMEBASE_RATE = 12024;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_MIN_PULSE_WIDTH = 12032;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_TIMEBASE_RATE = 12034;
  TRIGGER_ATTRIBUTE_START_TRIG_TRIG_WIN = 12570;
  TRIGGER_ATTRIBUTE_START_TRIG_RETRIGGER_WIN = 12571;
  TRIGGER_ATTRIBUTE_REF_TRIG_TRIG_WIN = 12574;
  TRIGGER_ATTRIBUTE_REF_TRIG_RETRIGGER_WIN = 12575;
}

enum TriggerUInt32Attribute {
  TRIGGER_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_REF_TRIG_PRETRIG_SAMPLES = 5189;
  TRIGGER_ATTRIBUTE_START_TRIG_MAX_NUM_TRIGS_TO_DETECT = 12572;
  TRIGGER_ATTRIBUTE_REF_TRIG_MAX_NUM_TRIGS_TO_DETECT = 12576;
}

enum TriggerBoolAttribute {
  TRIGGER_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_START_TRIG_RETRIGGERABLE = 6415;
  TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_FLTR_ENABLE = 8739;
  TRIGGER_ATTRIBUTE_DIG_EDGE_START_TRIG_DIG_SYNC_ENABLE = 8743;
  TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE = 8744;
  TRIGGER_ATTRIBUTE_DIG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE = 8748;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_FLTR_ENABLE = 8749;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ARM_START_TRIG_DIG_SYNC_ENABLE = 8753;
  TRIGGER_ATTRIBUTE_DIG_EDGE_ADV_TRIG_DIG_FLTR_ENABLE = 8760;
  TRIGGER_ATTRIBUTE_REF_TRIG_AUTO_TRIG_ENABLE = 11969;
  TRIGGER_ATTRIBUTE_REF_TRIG_AUTO_TRIGGERED = 11970;
  TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_FLTR_ENABLE = 11991;
  TRIGGER_ATTRIBUTE_DIG_EDGE_REF_TRIG_DIG_SYNC_ENABLE = 11995;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_FLTR_ENABLE = 12001;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_START_TRIG_DIG_SYNC_ENABLE = 12005;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_FLTR_ENABLE = 12006;
  TRIGGER_ATTRIBUTE_ANLG_EDGE_REF_TRIG_DIG_SYNC_ENABLE = 12010;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_FLTR_ENABLE = 12011;
  TRIGGER_ATTRIBUTE_ANLG_WIN_REF_TRIG_DIG_SYNC_ENABLE = 12015;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_FLTR_ENABLE = 12016;
  TRIGGER_ATTRIBUTE_ANLG_LVL_PAUSE_TRIG_DIG_SYNC_ENABLE = 12020;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_FLTR_ENABLE = 12021;
  TRIGGER_ATTRIBUTE_ANLG_WIN_PAUSE_TRIG_DIG_SYNC_ENABLE = 12025;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_FLTR_ENABLE = 12031;
  TRIGGER_ATTRIBUTE_ANLG_WIN_START_TRIG_DIG_SYNC_ENABLE = 12035;
  TRIGGER_ATTRIBUTE_REF_TRIG_RETRIGGERABLE = 12573;
  TRIGGER_ATTRIBUTE_REF_TRIG_TIMESTAMP_ENABLE = 12590;
  TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_ENABLE = 12595;
  TRIGGER_ATTRIBUTE_START_TRIG_TIMESTAMP_ENABLE = 12618;
}

enum TriggerTimestampAttribute {
  TRIGGER_TIMESTAMP_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_START_TRIG_TRIG_WHEN = 12365;
  TRIGGER_ATTRIBUTE_REF_TRIG_TIMESTAMP_VAL = 12591;
  TRIGGER_ATTRIBUTE_ARM_START_TRIG_TRIG_WHEN = 12593;
  TRIGGER_ATTRIBUTE_ARM_START_TRIG_TIMESTAMP_VAL = 12596;
  TRIGGER_ATTRIBUTE_START_TRIG_TIMESTAMP_VAL = 12619;
}

enum TriggerInt32ArrayAttribute {
  TRIGGER_INT32_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_SLOPES = 12578;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_COUPLINGS = 12581;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_SLOPES = 12583;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_COUPLINGS = 12586;
}

enum TriggerDoubleArrayAttribute {
  TRIGGER_DOUBLE_ARRAY_ATTRIBUTE_UNSPECIFIED = 0;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_LVLS = 12579;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_START_TRIG_HYSTS = 12580;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_LVLS = 12584;
  TRIGGER_ATTRIBUTE_ANLG_MULTI_EDGE_REF_TRIG_HYSTS = 12585;
}

enum WatchdogInt32Attribute {
  WATCHDOG_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  WATCHDOG_ATTRIBUTE_EXPIR_TRIG_TYPE = 8611;
  WATCHDOG_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_EDGE = 8613;
  WATCHDOG_ATTRIBUTE_DO_EXPIR_STATE = 8615;
  WATCHDOG_ATTRIBUTE_AO_OUTPUT_TYPE = 12382;
  WATCHDOG_ATTRIBUTE_CO_EXPIR_STATE = 12384;
}

enum WatchdogResetAttribute {
  WATCHDOG_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  WATCHDOG_RESET_ATTRIBUTE_EXPIR_TRIG_TYPE = 8611;
  WATCHDOG_RESET_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_SRC = 8612;
  WATCHDOG_RESET_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_EDGE = 8613;
  WATCHDOG_RESET_ATTRIBUTE_DO_EXPIR_STATE = 8615;
  WATCHDOG_RESET_ATTRIBUTE_TIMEOUT = 8617;
  WATCHDOG_RESET_ATTRIBUTE_EXPIR_TRIG_TRIG_ON_NETWORK_CONN_LOSS = 12381;
  WATCHDOG_RESET_ATTRIBUTE_AO_OUTPUT_TYPE = 12382;
  WATCHDOG_RESET_ATTRIBUTE_AO_EXPIR_STATE = 12383;
  WATCHDOG_RESET_ATTRIBUTE_CO_EXPIR_STATE = 12384;
}

enum WatchdogStringAttribute {
  WATCHDOG_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  WATCHDOG_ATTRIBUTE_DIG_EDGE_WATCHDOG_EXPIR_TRIG_SRC = 8612;
}

enum WatchdogBoolAttribute {
  WATCHDOG_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  WATCHDOG_ATTRIBUTE_HAS_EXPIRED = 8616;
  WATCHDOG_ATTRIBUTE_EXPIR_TRIG_TRIG_ON_NETWORK_CONN_LOSS = 12381;
}

enum WatchdogDoubleAttribute {
  WATCHDOG_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  WATCHDOG_ATTRIBUTE_TIMEOUT = 8617;
  WATCHDOG_ATTRIBUTE_AO_EXPIR_STATE = 12383;
}

enum WriteInt32Attribute {
  WRITE_INT32_ATTRIBUTE_UNSPECIFIED = 0;
  WRITE_ATTRIBUTE_REGEN_MODE = 5203;
  WRITE_ATTRIBUTE_RELATIVE_TO = 6412;
  WRITE_ATTRIBUTE_OFFSET = 6413;
  WRITE_ATTRIBUTE_WAIT_MODE = 8881;
}

enum WriteResetAttribute {
  WRITE_RESET_ATTRIBUTE_UNSPECIFIED = 0;
  WRITE_RESET_ATTRIBUTE_REGEN_MODE = 5203;
  WRITE_RESET_ATTRIBUTE_RELATIVE_TO = 6412;
  WRITE_RESET_ATTRIBUTE_OFFSET = 6413;
  WRITE_RESET_ATTRIBUTE_WAIT_MODE = 8881;
  WRITE_RESET_ATTRIBUTE_SLEEP_TIME = 8882;
  WRITE_RESET_ATTRIBUTE_NEXT_WRITE_IS_LAST = 10604;
}

enum WriteUInt64Attribute {
  WRITE_UINT64_ATTRIBUTE_UNSPECIFIED = 0;
  WRITE_ATTRIBUTE_CURR_WRITE_POS = 5208;
  WRITE_ATTRIBUTE_TOTAL_SAMP_PER_CHAN_GENERATED = 6443;
}

enum WriteUInt32Attribute {
  WRITE_UINT32_ATTRIBUTE_UNSPECIFIED = 0;
  WRITE_ATTRIBUTE_SPACE_AVAIL = 5216;
  WRITE_ATTRIBUTE_RAW_DATA_WIDTH = 8573;
  WRITE_ATTRIBUTE_NUM_CHANS = 8574;
  WRITE_ATTRIBUTE_DIGITAL_LINES_BYTES_PER_CHAN = 8575;
}

enum WriteDoubleAttribute {
  WRITE_DOUBLE_ATTRIBUTE_UNSPECIFIED = 0;
  WRITE_ATTRIBUTE_SLEEP_TIME = 8882;
}

enum WriteBoolAttribute {
  WRITE_BOOL_ATTRIBUTE_UNSPECIFIED = 0;
  WRITE_ATTRIBUTE_NEXT_WRITE_IS_LAST = 10604;
  WRITE_ATTRIBUTE_OVERCURRENT_CHANS_EXIST = 10728;
  WRITE_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS_EXIST = 10730;
  WRITE_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS_EXIST = 10732;
  WRITE_ATTRIBUTE_OVERTEMPERATURE_CHANS_EXIST = 10884;
  WRITE_ATTRIBUTE_ACCESSORY_INSERTION_OR_REMOVAL_DETECTED = 12371;
  WRITE_ATTRIBUTE_OVERLOADED_CHANS_EXIST = 12420;
  WRITE_ATTRIBUTE_EXTERNAL_OVERVOLTAGE_CHANS_EXIST = 12475;
  WRITE_ATTRIBUTE_SYNC_UNLOCKED_CHANS_EXIST = 12607;
}

enum WriteStringAttribute {
  WRITE_STRING_ATTRIBUTE_UNSPECIFIED = 0;
  WRITE_ATTRIBUTE_OVERCURRENT_CHANS = 10729;
  WRITE_ATTRIBUTE_OPEN_CURRENT_LOOP_CHANS = 10731;
  WRITE_ATTRIBUTE_POWER_SUPPLY_FAULT_CHANS = 10733;
  WRITE_ATTRIBUTE_DEVS_WITH_INSERTED_OR_REMOVED_ACCESSORIES = 12372;
  WRITE_ATTRIBUTE_OVERTEMPERATURE_CHANS = 12419;
  WRITE_ATTRIBUTE_OVERLOADED_CHANS = 12421;
  WRITE_ATTRIBUTE_EXTERNAL_OVERVOLTAGE_CHANS = 12476;
  WRITE_ATTRIBUTE_SYNC_UNLOCKED_CHANS = 12608;
}

enum ACExcitWireMode {
  AC_EXCIT_WIRE_MODE_UNSPECIFIED = 0;
  AC_EXCIT_WIRE_MODE_4_WIRE = 4;
  AC_EXCIT_WIRE_MODE_5_WIRE = 5;
  AC_EXCIT_WIRE_MODE_6_WIRE = 6;
}

enum AccelChargeSensitivityUnits {
  ACCEL_CHARGE_SENSITIVITY_UNITS_UNSPECIFIED = 0;
  ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_G = 16099;
  ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED = 16100;
  ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_INCHES_PER_SECOND_SQUARED = 16101;
}

enum AccelSensitivityUnits1 {
  ACCEL_SENSITIVITY_UNITS1_UNSPECIFIED = 0;
  ACCEL_SENSITIVITY_UNITS1_M_VOLTS_PER_G = 12509;
  ACCEL_SENSITIVITY_UNITS1_VOLTS_PER_G = 12510;
}

enum AccelUnits2 {
  ACCEL_UNITS2_UNSPECIFIED = 0;
  ACCEL_UNITS2_ACCEL_UNIT_G = 10186;
  ACCEL_UNITS2_METERS_PER_SECOND_SQUARED = 12470;
  ACCEL_UNITS2_INCHES_PER_SECOND_SQUARED = 12471;
  ACCEL_UNITS2_FROM_CUSTOM_SCALE = 10065;
}

enum AcquisitionType {
  ACQUISITION_TYPE_UNSPECIFIED = 0;
  ACQUISITION_TYPE_FINITE_SAMPS = 10178;
  ACQUISITION_TYPE_CONT_SAMPS = 10123;
  ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT = 12522;
}

enum AngleUnits1 {
  ANGLE_UNITS1_UNSPECIFIED = 0;
  ANGLE_UNITS1_DEGREES = 10146;
  ANGLE_UNITS1_RADIANS = 10273;
  ANGLE_UNITS1_FROM_CUSTOM_SCALE = 10065;
}

enum AngleUnits2 {
  ANGLE_UNITS2_UNSPECIFIED = 0;
  ANGLE_UNITS2_DEGREES = 10146;
  ANGLE_UNITS2_RADIANS = 10273;
  ANGLE_UNITS2_TICKS = 10304;
  ANGLE_UNITS2_FROM_CUSTOM_SCALE = 10065;
}

enum AngularVelocityUnits {
  ANGULAR_VELOCITY_UNITS_UNSPECIFIED = 0;
  ANGULAR_VELOCITY_UNITS_RPM = 16080;
  ANGULAR_VELOCITY_UNITS_RADIANS_PER_SECOND = 16081;
  ANGULAR_VELOCITY_UNITS_DEGREES_PER_SECOND = 16082;
  ANGULAR_VELOCITY_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum BridgeConfiguration1 {
  BRIDGE_CONFIGURATION1_UNSPECIFIED = 0;
  BRIDGE_CONFIGURATION1_FULL_BRIDGE = 10182;
  BRIDGE_CONFIGURATION1_HALF_BRIDGE = 10187;
  BRIDGE_CONFIGURATION1_QUARTER_BRIDGE = 10270;
  BRIDGE_CONFIGURATION1_NO_BRIDGE = 10228;
}

enum BridgeElectricalUnits {
  BRIDGE_ELECTRICAL_UNITS_UNSPECIFIED = 0;
  BRIDGE_ELECTRICAL_UNITS_VOLTS_PER_VOLT = 15896;
  BRIDGE_ELECTRICAL_UNITS_M_VOLTS_PER_VOLT = 15897;
}

enum BridgePhysicalUnits {
  BRIDGE_PHYSICAL_UNITS_UNSPECIFIED = 0;
  BRIDGE_PHYSICAL_UNITS_NEWTONS = 15875;
  BRIDGE_PHYSICAL_UNITS_POUNDS = 15876;
  BRIDGE_PHYSICAL_UNITS_KILOGRAM_FORCE = 15877;
  BRIDGE_PHYSICAL_UNITS_PASCALS = 10081;
  BRIDGE_PHYSICAL_UNITS_POUNDS_PER_SQUARE_INCH = 15879;
  BRIDGE_PHYSICAL_UNITS_BAR = 15880;
  BRIDGE_PHYSICAL_UNITS_NEWTON_METERS = 15881;
  BRIDGE_PHYSICAL_UNITS_INCH_OUNCES = 15882;
  BRIDGE_PHYSICAL_UNITS_INCH_POUNDS = 15883;
  BRIDGE_PHYSICAL_UNITS_FOOT_POUNDS = 15884;
}

enum BridgeUnits {
  BRIDGE_UNITS_UNSPECIFIED = 0;
  BRIDGE_UNITS_VOLTS_PER_VOLT = 15896;
  BRIDGE_UNITS_M_VOLTS_PER_VOLT = 15897;
  BRIDGE_UNITS_FROM_CUSTOM_SCALE = 10065;
  BRIDGE_UNITS_FROM_TEDS = 12516;
}

enum CJCSource1 {
  CJC_SOURCE1_UNSPECIFIED = 0;
  CJC_SOURCE1_BUILT_IN = 10200;
  CJC_SOURCE1_CONST_VAL = 10116;
  CJC_SOURCE1_CHAN = 10113;
}

enum ChargeUnits {
  CHARGE_UNITS_UNSPECIFIED = 0;
  CHARGE_UNITS_COULOMBS = 16102;
  CHARGE_UNITS_PICO_COULOMBS = 16103;
  CHARGE_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum CountDirection1 {
  COUNT_DIRECTION1_UNSPECIFIED = 0;
  COUNT_DIRECTION1_COUNT_UP = 10128;
  COUNT_DIRECTION1_COUNT_DOWN = 10124;
  COUNT_DIRECTION1_EXT_CONTROLLED = 10326;
}

enum CounterFrequencyMethod {
  COUNTER_FREQUENCY_METHOD_UNSPECIFIED = 0;
  COUNTER_FREQUENCY_METHOD_LOW_FREQ_1_CTR = 10105;
  COUNTER_FREQUENCY_METHOD_HIGH_FREQ_2_CTR = 10157;
  COUNTER_FREQUENCY_METHOD_LARGE_RNG_2_CTR = 10205;
  COUNTER_FREQUENCY_METHOD_DYN_AVG = 16065;
}

enum CurrentShuntResistorLocationWithDefault {
  CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_UNSPECIFIED = 0;
  CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_DEFAULT = -1;
  CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_INTERNAL = 10200;
  CURRENT_SHUNT_RESISTOR_LOCATION_WITH_DEFAULT_EXTERNAL = 10167;
}

enum CurrentUnits2 {
  CURRENT_UNITS2_UNSPECIFIED = 0;
  CURRENT_UNITS2_AMPS = 10342;
  CURRENT_UNITS2_FROM_CUSTOM_SCALE = 10065;
}

enum DigitalLineState {
  DIGITAL_LINE_STATE_UNSPECIFIED = 0;
  DIGITAL_LINE_STATE_HIGH = 10192;
  DIGITAL_LINE_STATE_LOW = 10214;
  DIGITAL_LINE_STATE_TRISTATE = 10310;
  DIGITAL_LINE_STATE_NO_CHANGE = 10160;
}

enum DigitalPatternCondition1 {
  DIGITAL_PATTERN_CONDITION1_UNSPECIFIED = 0;
  DIGITAL_PATTERN_CONDITION1_PATTERN_MATCHES = 10254;
  DIGITAL_PATTERN_CONDITION1_PATTERN_DOES_NOT_MATCH = 10253;
}

enum DigitalWidthUnits3 {
  DIGITAL_WIDTH_UNITS3_UNSPECIFIED = 0;
  DIGITAL_WIDTH_UNITS3_SECONDS = 10364;
}

enum EddyCurrentProxProbeSensitivityUnits {
  EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_UNSPECIFIED = 0;
  EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MIL = 14836;
  EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MIL = 14837;
  EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MILLIMETER = 14838;
  EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MILLIMETER = 14839;
  EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MICRON = 14840;
}

enum Edge1 {
  EDGE1_UNSPECIFIED = 0;
  EDGE1_RISING = 10280;
  EDGE1_FALLING = 10171;
}

enum EncoderType2 {
  ENCODER_TYPE2_UNSPECIFIED = 0;
  ENCODER_TYPE2_X1 = 10090;
  ENCODER_TYPE2_X2 = 10091;
  ENCODER_TYPE2_X4 = 10092;
  ENCODER_TYPE2_TWO_PULSE_COUNTING = 10313;
}

enum EncoderZIndexPhase1 {
  ENCODER_Z_INDEX_PHASE1_UNSPECIFIED = 0;
  ENCODER_Z_INDEX_PHASE1_A_HIGH_B_HIGH = 10040;
  ENCODER_Z_INDEX_PHASE1_A_HIGH_B_LOW = 10041;
  ENCODER_Z_INDEX_PHASE1_A_LOW_B_HIGH = 10042;
  ENCODER_Z_INDEX_PHASE1_A_LOW_B_LOW = 10043;
}

enum EveryNSamplesEventType {
  EVERY_N_SAMPLES_EVENT_TYPE_UNSPECIFIED = 0;
  EVERY_N_SAMPLES_EVENT_TYPE_ACQUIRED_INTO_BUFFER = 1;
  EVERY_N_SAMPLES_EVENT_TYPE_TRANSFERRED_FROM_BUFFER = 2;
}

enum ExcitationSource {
  EXCITATION_SOURCE_UNSPECIFIED = 0;
  EXCITATION_SOURCE_INTERNAL = 10200;
  EXCITATION_SOURCE_EXTERNAL = 10167;
  EXCITATION_SOURCE_NONE = 10230;
}

enum ForceIEPESensorSensitivityUnits {
  FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_UNSPECIFIED = 0;
  FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_NEWTON = 15891;
  FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_POUND = 15892;
}

enum ForceIEPEUnits {
  FORCE_IEPE_UNITS_UNSPECIFIED = 0;
  FORCE_IEPE_UNITS_NEWTONS = 15875;
  FORCE_IEPE_UNITS_POUNDS = 15876;
  FORCE_IEPE_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum ForceUnits {
  FORCE_UNITS_UNSPECIFIED = 0;
  FORCE_UNITS_NEWTONS = 15875;
  FORCE_UNITS_POUNDS = 15876;
  FORCE_UNITS_KILOGRAM_FORCE = 15877;
  FORCE_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum FrequencyUnits {
  FREQUENCY_UNITS_UNSPECIFIED = 0;
  FREQUENCY_UNITS_HZ = 10373;
  FREQUENCY_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum FrequencyUnits2 {
  FREQUENCY_UNITS2_UNSPECIFIED = 0;
  FREQUENCY_UNITS2_HZ = 10373;
}

enum FrequencyUnits3 {
  FREQUENCY_UNITS3_UNSPECIFIED = 0;
  FREQUENCY_UNITS3_HZ = 10373;
  FREQUENCY_UNITS3_TICKS = 10304;
  FREQUENCY_UNITS3_FROM_CUSTOM_SCALE = 10065;
}

enum FuncGenType {
  FUNC_GEN_TYPE_UNSPECIFIED = 0;
  FUNC_GEN_TYPE_SINE = 14751;
  FUNC_GEN_TYPE_TRIANGLE = 14752;
  FUNC_GEN_TYPE_SQUARE = 14753;
  FUNC_GEN_TYPE_SAWTOOTH = 14754;
}

enum GpsSignalType1 {
  GPS_SIGNAL_TYPE1_UNSPECIFIED = 0;
  GPS_SIGNAL_TYPE1_IRIGB = 10070;
  GPS_SIGNAL_TYPE1_PPS = 10080;
  GPS_SIGNAL_TYPE1_NONE = 10230;
}

enum GroupBy {
  GROUP_BY_GROUP_BY_CHANNEL = 0;
  GROUP_BY_GROUP_BY_SCAN_NUMBER = 1;
}

enum InputTermCfgWithDefault {
  INPUT_TERM_CFG_WITH_DEFAULT_UNSPECIFIED = 0;
  INPUT_TERM_CFG_WITH_DEFAULT_CFG_DEFAULT = -1;
  INPUT_TERM_CFG_WITH_DEFAULT_RSE = 10083;
  INPUT_TERM_CFG_WITH_DEFAULT_NRSE = 10078;
  INPUT_TERM_CFG_WITH_DEFAULT_DIFF = 10106;
  INPUT_TERM_CFG_WITH_DEFAULT_PSEUDO_DIFF = 12529;
}

enum InvertPolarity {
  INVERT_POLARITY_DO_NOT_INVERT_POLARITY = 0;
  INVERT_POLARITY_INVERT_POLARITY = 1;
}

enum LVDTSensitivityUnits1 {
  LVDT_SENSITIVITY_UNITS1_UNSPECIFIED = 0;
  LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLIMETER = 12506;
  LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLI_INCH = 12505;
}

enum LengthUnits2 {
  LENGTH_UNITS2_UNSPECIFIED = 0;
  LENGTH_UNITS2_METERS = 10219;
  LENGTH_UNITS2_INCHES = 10379;
  LENGTH_UNITS2_FROM_CUSTOM_SCALE = 10065;
}

enum LengthUnits3 {
  LENGTH_UNITS3_UNSPECIFIED = 0;
  LENGTH_UNITS3_METERS = 10219;
  LENGTH_UNITS3_INCHES = 10379;
  LENGTH_UNITS3_TICKS = 10304;
  LENGTH_UNITS3_FROM_CUSTOM_SCALE = 10065;
}

enum Level1 {
  LEVEL1_UNSPECIFIED = 0;
  LEVEL1_HIGH = 10192;
  LEVEL1_LOW = 10214;
}

enum LineGrouping {
  LINE_GROUPING_CHAN_PER_LINE = 0;
  LINE_GROUPING_CHAN_FOR_ALL_LINES = 1;
}

enum LoggingMode {
  LOGGING_MODE_UNSPECIFIED = 0;
  LOGGING_MODE_OFF = 10231;
  LOGGING_MODE_LOG = 15844;
  LOGGING_MODE_LOG_AND_READ = 15842;
}

enum LoggingOperation {
  LOGGING_OPERATION_UNSPECIFIED = 0;
  LOGGING_OPERATION_OPEN = 10437;
  LOGGING_OPERATION_OPEN_OR_CREATE = 15846;
  LOGGING_OPERATION_CREATE_OR_REPLACE = 15847;
  LOGGING_OPERATION_CREATE = 15848;
}

enum LogicFamily {
  LOGIC_FAMILY_UNSPECIFIED = 0;
  LOGIC_FAMILY_1POINT_8_V = 16184;
  LOGIC_FAMILY_2POINT_5_V = 14620;
  LOGIC_FAMILY_3POINT_3_V = 14621;
  LOGIC_FAMILY_5_V = 14619;
}

enum Polarity2 {
  POLARITY2_UNSPECIFIED = 0;
  POLARITY2_ACTIVE_HIGH = 10095;
  POLARITY2_ACTIVE_LOW = 10096;
}

enum PowerUnits {
  POWER_UNITS_UNSPECIFIED = 0;
  POWER_UNITS_WATTS = 16203;
  POWER_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum PowerUpChannelType {
  POWER_UP_CHANNEL_TYPE_CHANNEL_VOLTAGE = 0;
  POWER_UP_CHANNEL_TYPE_CHANNEL_CURRENT = 1;
  POWER_UP_CHANNEL_TYPE_CHANNEL_HIGH_IMPEDANCE = 2;
}

enum PowerUpStates {
  POWER_UP_STATES_UNSPECIFIED = 0;
  POWER_UP_STATES_HIGH = 10192;
  POWER_UP_STATES_LOW = 10214;
  POWER_UP_STATES_TRISTATE = 10310;
}

enum PressureUnits {
  PRESSURE_UNITS_UNSPECIFIED = 0;
  PRESSURE_UNITS_PASCALS = 10081;
  PRESSURE_UNITS_POUNDS_PER_SQUARE_INCH = 15879;
  PRESSURE_UNITS_BAR = 15880;
  PRESSURE_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum RTDType1 {
  RTD_TYPE1_UNSPECIFIED = 0;
  RTD_TYPE1_PT_3750 = 12481;
  RTD_TYPE1_PT_3851 = 10071;
  RTD_TYPE1_PT_3911 = 12482;
  RTD_TYPE1_PT_3916 = 10069;
  RTD_TYPE1_PT_3920 = 10053;
  RTD_TYPE1_PT_3928 = 12483;
  RTD_TYPE1_CUSTOM = 10137;
}

enum RVDTSensitivityUnits1 {
  RVDT_SENSITIVITY_UNITS1_UNSPECIFIED = 0;
  RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_DEGREE = 12507;
  RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_RADIAN = 12508;
}

enum ResistanceConfiguration {
  RESISTANCE_CONFIGURATION_UNSPECIFIED = 0;
  RESISTANCE_CONFIGURATION_2_WIRE = 2;
  RESISTANCE_CONFIGURATION_3_WIRE = 3;
  RESISTANCE_CONFIGURATION_4_WIRE = 4;
}

enum ResistanceUnits2 {
  RESISTANCE_UNITS2_UNSPECIFIED = 0;
  RESISTANCE_UNITS2_OHMS = 10384;
  RESISTANCE_UNITS2_FROM_CUSTOM_SCALE = 10065;
}

enum ResistorState {
  RESISTOR_STATE_UNSPECIFIED = 0;
  RESISTOR_STATE_PULL_UP = 15950;
  RESISTOR_STATE_PULL_DOWN = 15951;
}

enum SaveOptions {
  SAVE_OPTIONS_UNSPECIFIED = 0;
  SAVE_OPTIONS_OVERWRITE = 1;
  SAVE_OPTIONS_ALLOW_INTERACTIVE_EDITING = 2;
  SAVE_OPTIONS_ALLOW_INTERACTIVE_DELETION = 4;
}

enum ShuntCalSelect {
  SHUNT_CAL_SELECT_UNSPECIFIED = 0;
  SHUNT_CAL_SELECT_A = 12513;
  SHUNT_CAL_SELECT_B = 12514;
  SHUNT_CAL_SELECT_A_AND_B = 12515;
}

enum ShuntCalSource {
  SHUNT_CAL_SOURCE_UNSPECIFIED = 0;
  SHUNT_CAL_SOURCE_DEFAULT = -1;
  SHUNT_CAL_SOURCE_BUILT_IN = 10200;
  SHUNT_CAL_SOURCE_USER_PROVIDED = 10167;
}

enum ShuntElementLocation {
  SHUNT_ELEMENT_LOCATION_UNSPECIFIED = 0;
  SHUNT_ELEMENT_LOCATION_R1 = 12465;
  SHUNT_ELEMENT_LOCATION_R2 = 12466;
  SHUNT_ELEMENT_LOCATION_R3 = 12467;
  SHUNT_ELEMENT_LOCATION_R4 = 14813;
  SHUNT_ELEMENT_LOCATION_NONE = 10230;
}

enum Signal {
  SIGNAL_UNSPECIFIED = 0;
  SIGNAL_AI_CONVERT_CLOCK = 12484;
  SIGNAL_10_MHZ_REF_CLOCK = 12536;
  SIGNAL_20_MHZ_TIMEBASE_CLOCK = 12486;
  SIGNAL_SAMPLE_CLOCK = 12487;
  SIGNAL_ADVANCE_TRIGGER = 12488;
  SIGNAL_REFERENCE_TRIGGER = 12490;
  SIGNAL_START_TRIGGER = 12491;
  SIGNAL_ADV_CMPLT_EVENT = 12492;
  SIGNAL_AI_HOLD_CMPLT_EVENT = 12493;
  SIGNAL_COUNTER_OUTPUT_EVENT = 12494;
  SIGNAL_CHANGE_DETECTION_EVENT = 12511;
  SIGNAL_WDT_EXPIRED_EVENT = 12512;
}

enum Signal2 {
  SIGNAL2_UNSPECIFIED = 0;
  SIGNAL2_SAMPLE_COMPLETE_EVENT = 12530;
  SIGNAL2_COUNTER_OUTPUT_EVENT = 12494;
  SIGNAL2_CHANGE_DETECTION_EVENT = 12511;
  SIGNAL2_SAMPLE_CLOCK = 12487;
}

enum Slope1 {
  SLOPE1_UNSPECIFIED = 0;
  SLOPE1_RISING_SLOPE = 10280;
  SLOPE1_FALLING_SLOPE = 10171;
}

enum SoundPressureUnits1 {
  SOUND_PRESSURE_UNITS1_UNSPECIFIED = 0;
  SOUND_PRESSURE_UNITS1_PASCALS = 10081;
  SOUND_PRESSURE_UNITS1_FROM_CUSTOM_SCALE = 10065;
}

enum StrainGageBridgeType1 {
  STRAIN_GAGE_BRIDGE_TYPE1_UNSPECIFIED = 0;
  STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_I = 10183;
  STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_II = 10184;
  STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_III = 10185;
  STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_I = 10188;
  STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_II = 10189;
  STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_I = 10271;
  STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_II = 10272;
}

enum StrainGageRosetteMeasurementType {
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_UNSPECIFIED = 0;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_1 = 15971;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_2 = 15972;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_ANGLE = 15973;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_X = 15974;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_Y = 15975;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_SHEAR_STRAIN_XY = 15976;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN = 15977;
  STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN_ANGLE = 15978;
}

enum StrainGageRosetteType {
  STRAIN_GAGE_ROSETTE_TYPE_UNSPECIFIED = 0;
  STRAIN_GAGE_ROSETTE_TYPE_RECTANGULAR_ROSETTE = 15968;
  STRAIN_GAGE_ROSETTE_TYPE_DELTA_ROSETTE = 15969;
  STRAIN_GAGE_ROSETTE_TYPE_TEE_ROSETTE = 15970;
}

enum StrainUnits1 {
  STRAIN_UNITS1_UNSPECIFIED = 0;
  STRAIN_UNITS1_STRAIN = 10299;
  STRAIN_UNITS1_FROM_CUSTOM_SCALE = 10065;
}

enum TEDSUnits {
  TEDS_UNITS_UNSPECIFIED = 0;
  TEDS_UNITS_FROM_CUSTOM_SCALE = 10065;
  TEDS_UNITS_FROM_TEDS = 12516;
}

enum TaskControlAction {
  TASK_CONTROL_ACTION_TASK_START = 0;
  TASK_CONTROL_ACTION_TASK_STOP = 1;
  TASK_CONTROL_ACTION_TASK_VERIFY = 2;
  TASK_CONTROL_ACTION_TASK_COMMIT = 3;
  TASK_CONTROL_ACTION_TASK_RESERVE = 4;
  TASK_CONTROL_ACTION_TASK_UNRESERVE = 5;
  TASK_CONTROL_ACTION_TASK_ABORT = 6;
}

enum TemperatureUnits {
  TEMPERATURE_UNITS_UNSPECIFIED = 0;
  TEMPERATURE_UNITS_DEG_C = 10143;
  TEMPERATURE_UNITS_DEG_F = 10144;
  TEMPERATURE_UNITS_KELVINS = 10325;
  TEMPERATURE_UNITS_DEG_R = 10145;
}

enum ThermocoupleType1 {
  THERMOCOUPLE_TYPE1_UNSPECIFIED = 0;
  THERMOCOUPLE_TYPE1_J_TYPE_TC = 10072;
  THERMOCOUPLE_TYPE1_K_TYPE_TC = 10073;
  THERMOCOUPLE_TYPE1_N_TYPE_TC = 10077;
  THERMOCOUPLE_TYPE1_R_TYPE_TC = 10082;
  THERMOCOUPLE_TYPE1_S_TYPE_TC = 10085;
  THERMOCOUPLE_TYPE1_T_TYPE_TC = 10086;
  THERMOCOUPLE_TYPE1_B_TYPE_TC = 10047;
  THERMOCOUPLE_TYPE1_E_TYPE_TC = 10055;
  THERMOCOUPLE_TYPE1_A_TYPE_TC = 16208;
  THERMOCOUPLE_TYPE1_C_TYPE_TC = 16209;
}

enum TimeUnits {
  TIME_UNITS_UNSPECIFIED = 0;
  TIME_UNITS_SECONDS = 10364;
  TIME_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum TimeUnits3 {
  TIME_UNITS3_UNSPECIFIED = 0;
  TIME_UNITS3_SECONDS = 10364;
  TIME_UNITS3_TICKS = 10304;
  TIME_UNITS3_FROM_CUSTOM_SCALE = 10065;
}

enum Timescale2 {
  TIMESCALE2_UNSPECIFIED = 0;
  TIMESCALE2_HOST_TIME = 16126;
  TIMESCALE2_IO_DEVICE_TIME = 16127;
}

enum TimestampEvent {
  TIMESTAMP_EVENT_UNSPECIFIED = 0;
  TIMESTAMP_EVENT_START_TRIGGER = 12491;
  TIMESTAMP_EVENT_REFERENCE_TRIGGER = 12490;
  TIMESTAMP_EVENT_ARM_START_TRIGGER = 14641;
  TIMESTAMP_EVENT_FIRST_SAMPLE_TIMESTAMP = 16130;
}

enum TorqueUnits {
  TORQUE_UNITS_UNSPECIFIED = 0;
  TORQUE_UNITS_NEWTON_METERS = 15881;
  TORQUE_UNITS_INCH_OUNCES = 15882;
  TORQUE_UNITS_INCH_POUNDS = 15883;
  TORQUE_UNITS_FOOT_POUNDS = 15884;
  TORQUE_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum UnitsPreScaled {
  UNITS_PRE_SCALED_UNSPECIFIED = 0;
  UNITS_PRE_SCALED_VOLTS = 10348;
  UNITS_PRE_SCALED_AMPS = 10342;
  UNITS_PRE_SCALED_DEG_F = 10144;
  UNITS_PRE_SCALED_DEG_C = 10143;
  UNITS_PRE_SCALED_DEG_R = 10145;
  UNITS_PRE_SCALED_KELVINS = 10325;
  UNITS_PRE_SCALED_STRAIN = 10299;
  UNITS_PRE_SCALED_OHMS = 10384;
  UNITS_PRE_SCALED_HZ = 10373;
  UNITS_PRE_SCALED_SECONDS = 10364;
  UNITS_PRE_SCALED_METERS = 10219;
  UNITS_PRE_SCALED_INCHES = 10379;
  UNITS_PRE_SCALED_DEGREES = 10146;
  UNITS_PRE_SCALED_RADIANS = 10273;
  UNITS_PRE_SCALED_TICKS = 10304;
  UNITS_PRE_SCALED_RPM = 16080;
  UNITS_PRE_SCALED_RADIANS_PER_SECOND = 16081;
  UNITS_PRE_SCALED_DEGREES_PER_SECOND = 16082;
  UNITS_PRE_SCALED_G = 10186;
  UNITS_PRE_SCALED_METERS_PER_SECOND_SQUARED = 12470;
  UNITS_PRE_SCALED_INCHES_PER_SECOND_SQUARED = 12471;
  UNITS_PRE_SCALED_METERS_PER_SECOND = 15959;
  UNITS_PRE_SCALED_INCHES_PER_SECOND = 15960;
  UNITS_PRE_SCALED_PASCALS = 10081;
  UNITS_PRE_SCALED_NEWTONS = 15875;
  UNITS_PRE_SCALED_POUNDS = 15876;
  UNITS_PRE_SCALED_KILOGRAM_FORCE = 15877;
  UNITS_PRE_SCALED_POUNDS_PER_SQUARE_INCH = 15879;
  UNITS_PRE_SCALED_BAR = 15880;
  UNITS_PRE_SCALED_NEWTON_METERS = 15881;
  UNITS_PRE_SCALED_INCH_OUNCES = 15882;
  UNITS_PRE_SCALED_INCH_POUNDS = 15883;
  UNITS_PRE_SCALED_FOOT_POUNDS = 15884;
  UNITS_PRE_SCALED_VOLTS_PER_VOLT = 15896;
  UNITS_PRE_SCALED_M_VOLTS_PER_VOLT = 15897;
  UNITS_PRE_SCALED_COULOMBS = 16102;
  UNITS_PRE_SCALED_PICO_COULOMBS = 16103;
  UNITS_PRE_SCALED_FROM_TEDS = 12516;
}

enum VelocityIEPESensorSensitivityUnits {
  VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_UNSPECIFIED = 0;
  VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLIVOLTS_PER_MILLIMETER_PER_SECOND = 15963;
  VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLI_VOLTS_PER_INCH_PER_SECOND = 15964;
}

enum VelocityUnits {
  VELOCITY_UNITS_UNSPECIFIED = 0;
  VELOCITY_UNITS_METERS_PER_SECOND = 15959;
  VELOCITY_UNITS_INCHES_PER_SECOND = 15960;
  VELOCITY_UNITS_FROM_CUSTOM_SCALE = 10065;
}

enum VoltageUnits2 {
  VOLTAGE_UNITS2_UNSPECIFIED = 0;
  VOLTAGE_UNITS2_VOLTS = 10348;
  VOLTAGE_UNITS2_FROM_CUSTOM_SCALE = 10065;
}

enum WatchdogAOOutputType {
  WATCHDOG_AO_OUTPUT_TYPE_UNSPECIFIED = 0;
  WATCHDOG_AO_OUTPUT_TYPE_VOLTAGE = 10322;
  WATCHDOG_AO_OUTPUT_TYPE_CURRENT = 10134;
  WATCHDOG_AO_OUTPUT_TYPE_NO_CHANGE = 10160;
}

enum WatchdogCOExpirState {
  WATCHDOG_CO_EXPIR_STATE_UNSPECIFIED = 0;
  WATCHDOG_CO_EXPIR_STATE_LOW = 10214;
  WATCHDOG_CO_EXPIR_STATE_HIGH = 10192;
  WATCHDOG_CO_EXPIR_STATE_NO_CHANGE = 10160;
}

enum WatchdogControlAction {
  WATCHDOG_CONTROL_ACTION_RESET_TIMER = 0;
  WATCHDOG_CONTROL_ACTION_CLEAR_EXPIRATION = 1;
}

enum WindowTriggerCondition1 {
  WINDOW_TRIGGER_CONDITION1_UNSPECIFIED = 0;
  WINDOW_TRIGGER_CONDITION1_ENTERING_WIN = 10163;
  WINDOW_TRIGGER_CONDITION1_LEAVING_WIN = 10208;
}

enum WriteBasicTEDSOptions {
  WRITE_BASIC_TEDS_OPTIONS_UNSPECIFIED = 0;
  WRITE_BASIC_TEDS_OPTIONS_WRITE_TO_EEPROM = 12538;
  WRITE_BASIC_TEDS_OPTIONS_WRITE_TO_PROM = 12539;
  WRITE_BASIC_TEDS_OPTIONS_DO_NOT_WRITE = 12540;
}

enum WaveformAttributeMode {
  WAVEFORM_ATTRIBUTE_MODE_NONE = 0;
  WAVEFORM_ATTRIBUTE_MODE_TIMING = 1;
  WAVEFORM_ATTRIBUTE_MODE_EXTENDED_PROPERTIES = 2;
}

enum ChannelInt32AttributeValues {
  option allow_alias = true;
  CHANNEL_INT32_UNSPECIFIED = 0;
  CHANNEL_INT32_AC_EXCIT_WIRE_MODE_4_WIRE = 4;
  CHANNEL_INT32_AC_EXCIT_WIRE_MODE_5_WIRE = 5;
  CHANNEL_INT32_AC_EXCIT_WIRE_MODE_6_WIRE = 6;
  CHANNEL_INT32_ADC_TIMING_MODE_AUTOMATIC = 16097;
  CHANNEL_INT32_ADC_TIMING_MODE_HIGH_RESOLUTION = 10195;
  CHANNEL_INT32_ADC_TIMING_MODE_HIGH_SPEED = 14712;
  CHANNEL_INT32_ADC_TIMING_MODE_BEST_50_HZ_REJECTION = 14713;
  CHANNEL_INT32_ADC_TIMING_MODE_BEST_60_HZ_REJECTION = 14714;
  CHANNEL_INT32_ADC_TIMING_MODE_CUSTOM = 10137;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE = 10322;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_RMS = 10350;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT = 10134;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT_RMS = 10351;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_CUSTOM_WITH_EXCITATION = 10323;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_BRIDGE = 15908;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_FREQ_VOLTAGE = 10181;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_RESISTANCE = 10278;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_TC = 10303;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_THRMSTR = 10302;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_RTD = 10301;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_BUILT_IN_SENSOR = 10311;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_STRAIN_GAGE = 10300;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_ROSETTE_STRAIN_GAGE = 15980;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_LVDT = 10352;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_RVDT = 10353;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_EDDY_CURRENT_PROXIMITY_PROBE = 14835;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELEROMETER = 10356;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_CHARGE = 16104;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_4_WIRE_DC_VOLTAGE = 16106;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_VELOCITY_IEPE_SENSOR = 15966;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_BRIDGE = 15899;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_IEPE_SENSOR = 15895;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_PRESSURE_BRIDGE = 15902;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_SOUND_PRESSURE_MICROPHONE = 10354;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_TORQUE_BRIDGE = 15905;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_TEDS_SENSOR = 12531;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_CHARGE = 16105;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_POWER = 16201;
  CHANNEL_INT32_AI_MEASUREMENT_TYPE_CALCULATED_POWER = 16204;
  CHANNEL_INT32_AO_IDLE_OUTPUT_BEHAVIOR_ZERO_VOLTS = 12526;
  CHANNEL_INT32_AO_IDLE_OUTPUT_BEHAVIOR_HIGH_IMPEDANCE = 12527;
  CHANNEL_INT32_AO_IDLE_OUTPUT_BEHAVIOR_MAINTAIN_EXISTING_VALUE = 12528;
  CHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_VOLTAGE = 10322;
  CHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_CURRENT = 10134;
  CHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_FUNC_GEN = 14750;
  CHANNEL_INT32_ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_G = 16099;
  CHANNEL_INT32_ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED = 16100;
  CHANNEL_INT32_ACCEL_CHARGE_SENSITIVITY_UNITS_PICO_COULOMBS_PER_INCHES_PER_SECOND_SQUARED = 16101;
  CHANNEL_INT32_ACCEL_SENSITIVITY_UNITS1_M_VOLTS_PER_G = 12509;
  CHANNEL_INT32_ACCEL_SENSITIVITY_UNITS1_VOLTS_PER_G = 12510;
  CHANNEL_INT32_ACCEL_UNITS2_ACCEL_UNIT_G = 10186;
  CHANNEL_INT32_ACCEL_UNITS2_METERS_PER_SECOND_SQUARED = 12470;
  CHANNEL_INT32_ACCEL_UNITS2_INCHES_PER_SECOND_SQUARED = 12471;
  CHANNEL_INT32_ACCEL_UNITS2_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_ANGLE_UNITS1_DEGREES = 10146;
  CHANNEL_INT32_ANGLE_UNITS1_RADIANS = 10273;
  CHANNEL_INT32_ANGLE_UNITS1_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_ANGLE_UNITS2_DEGREES = 10146;
  CHANNEL_INT32_ANGLE_UNITS2_RADIANS = 10273;
  CHANNEL_INT32_ANGLE_UNITS2_TICKS = 10304;
  CHANNEL_INT32_ANGLE_UNITS2_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_ANGLE_UNITS3_DEGREES = 10146;
  CHANNEL_INT32_ANGLE_UNITS3_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_RPM = 16080;
  CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_RADIANS_PER_SECOND = 16081;
  CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_DEGREES_PER_SECOND = 16082;
  CHANNEL_INT32_ANGULAR_VELOCITY_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_AUTO_ZERO_TYPE1_NONE = 10230;
  CHANNEL_INT32_AUTO_ZERO_TYPE1_ONCE = 10244;
  CHANNEL_INT32_AUTO_ZERO_TYPE1_EVERY_SAMPLE = 10164;
  CHANNEL_INT32_BRIDGE_CONFIGURATION1_FULL_BRIDGE = 10182;
  CHANNEL_INT32_BRIDGE_CONFIGURATION1_HALF_BRIDGE = 10187;
  CHANNEL_INT32_BRIDGE_CONFIGURATION1_QUARTER_BRIDGE = 10270;
  CHANNEL_INT32_BRIDGE_CONFIGURATION1_NO_BRIDGE = 10228;
  CHANNEL_INT32_BRIDGE_ELECTRICAL_UNITS_VOLTS_PER_VOLT = 15896;
  CHANNEL_INT32_BRIDGE_ELECTRICAL_UNITS_M_VOLTS_PER_VOLT = 15897;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_NEWTONS = 15875;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_POUNDS = 15876;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_KILOGRAM_FORCE = 15877;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_PASCALS = 10081;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_POUNDS_PER_SQUARE_INCH = 15879;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_BAR = 15880;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_NEWTON_METERS = 15881;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_INCH_OUNCES = 15882;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_INCH_POUNDS = 15883;
  CHANNEL_INT32_BRIDGE_PHYSICAL_UNITS_FOOT_POUNDS = 15884;
  CHANNEL_INT32_BRIDGE_SHUNT_CAL_SOURCE_BUILT_IN = 10200;
  CHANNEL_INT32_BRIDGE_SHUNT_CAL_SOURCE_USER_PROVIDED = 10167;
  CHANNEL_INT32_BRIDGE_UNITS_VOLTS_PER_VOLT = 15896;
  CHANNEL_INT32_BRIDGE_UNITS_M_VOLTS_PER_VOLT = 15897;
  CHANNEL_INT32_BRIDGE_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_BRIDGE_UNITS_FROM_TEDS = 12516;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_COUNT_EDGES = 10125;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_FREQ = 10179;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_PERIOD = 10256;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_WIDTH = 10359;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_SEMI_PERIOD = 10289;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_FREQUENCY = 15864;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TIME = 15865;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TICKS = 15866;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_DUTY_CYCLE = 16070;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_ANG_ENCODER = 10360;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_LIN_ENCODER = 10361;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_ANG_ENCODER = 16078;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_LIN_ENCODER = 16079;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_TWO_EDGE_SEP = 10267;
  CHANNEL_INT32_CI_MEASUREMENT_TYPE_GPS_TIMESTAMP = 10362;
  CHANNEL_INT32_CJC_SOURCE1_BUILT_IN = 10200;
  CHANNEL_INT32_CJC_SOURCE1_CONST_VAL = 10116;
  CHANNEL_INT32_CJC_SOURCE1_CHAN = 10113;
  CHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TIME = 10269;
  CHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_FREQ = 10119;
  CHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TICKS = 10268;
  CHANNEL_INT32_CHANNEL_TYPE_AI = 10100;
  CHANNEL_INT32_CHANNEL_TYPE_AO = 10102;
  CHANNEL_INT32_CHANNEL_TYPE_DI = 10151;
  CHANNEL_INT32_CHANNEL_TYPE_DO = 10153;
  CHANNEL_INT32_CHANNEL_TYPE_CI = 10131;
  CHANNEL_INT32_CHANNEL_TYPE_CO = 10132;
  CHANNEL_INT32_CHARGE_UNITS_COULOMBS = 16102;
  CHANNEL_INT32_CHARGE_UNITS_PICO_COULOMBS = 16103;
  CHANNEL_INT32_CHARGE_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_CONSTRAINED_GEN_MODE_UNCONSTRAINED = 14708;
  CHANNEL_INT32_CONSTRAINED_GEN_MODE_FIXED_HIGH_FREQ = 14709;
  CHANNEL_INT32_CONSTRAINED_GEN_MODE_FIXED_LOW_FREQ = 14710;
  CHANNEL_INT32_CONSTRAINED_GEN_MODE_FIXED_50_PERCENT_DUTY_CYCLE = 14711;
  CHANNEL_INT32_COUNT_DIRECTION1_COUNT_UP = 10128;
  CHANNEL_INT32_COUNT_DIRECTION1_COUNT_DOWN = 10124;
  CHANNEL_INT32_COUNT_DIRECTION1_EXT_CONTROLLED = 10326;
  CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_LOW_FREQ_1_CTR = 10105;
  CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_HIGH_FREQ_2_CTR = 10157;
  CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_LARGE_RNG_2_CTR = 10205;
  CHANNEL_INT32_COUNTER_FREQUENCY_METHOD_DYN_AVG = 16065;
  CHANNEL_INT32_COUPLING1_AC = 10045;
  CHANNEL_INT32_COUPLING1_DC = 10050;
  CHANNEL_INT32_COUPLING1_GND = 10066;
  CHANNEL_INT32_CURRENT_SHUNT_RESISTOR_LOCATION1_INTERNAL = 10200;
  CHANNEL_INT32_CURRENT_SHUNT_RESISTOR_LOCATION1_EXTERNAL = 10167;
  CHANNEL_INT32_CURRENT_UNITS1_AMPS = 10342;
  CHANNEL_INT32_CURRENT_UNITS1_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_CURRENT_UNITS1_FROM_TEDS = 12516;
  CHANNEL_INT32_DATA_JUSTIFICATION1_RIGHT_JUSTIFIED = 10279;
  CHANNEL_INT32_DATA_JUSTIFICATION1_LEFT_JUSTIFIED = 10209;
  CHANNEL_INT32_DATA_TRANSFER_MECHANISM_DMA = 10054;
  CHANNEL_INT32_DATA_TRANSFER_MECHANISM_INTERRUPTS = 10204;
  CHANNEL_INT32_DATA_TRANSFER_MECHANISM_PROGRAMMED_IO = 10264;
  CHANNEL_INT32_DATA_TRANSFER_MECHANISM_US_BBULK = 12590;
  CHANNEL_INT32_DIGITAL_DRIVE_TYPE_ACTIVE_DRIVE = 12573;
  CHANNEL_INT32_DIGITAL_DRIVE_TYPE_OPEN_COLLECTOR = 12574;
  CHANNEL_INT32_DIGITAL_LINE_STATE_HIGH = 10192;
  CHANNEL_INT32_DIGITAL_LINE_STATE_LOW = 10214;
  CHANNEL_INT32_DIGITAL_LINE_STATE_TRISTATE = 10310;
  CHANNEL_INT32_DIGITAL_LINE_STATE_NO_CHANGE = 10160;
  CHANNEL_INT32_DIGITAL_WIDTH_UNITS4_SECONDS = 10364;
  CHANNEL_INT32_DIGITAL_WIDTH_UNITS4_SAMPLE_CLK_PERIODS = 10286;
  CHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MIL = 14836;
  CHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MIL = 14837;
  CHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MILLIMETER = 14838;
  CHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_VOLTS_PER_MILLIMETER = 14839;
  CHANNEL_INT32_EDDY_CURRENT_PROX_PROBE_SENSITIVITY_UNITS_M_VOLTS_PER_MICRON = 14840;
  CHANNEL_INT32_EDGE1_RISING = 10280;
  CHANNEL_INT32_EDGE1_FALLING = 10171;
  CHANNEL_INT32_ENCODER_TYPE2_X1 = 10090;
  CHANNEL_INT32_ENCODER_TYPE2_X2 = 10091;
  CHANNEL_INT32_ENCODER_TYPE2_X4 = 10092;
  CHANNEL_INT32_ENCODER_TYPE2_TWO_PULSE_COUNTING = 10313;
  CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_HIGH_B_HIGH = 10040;
  CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_HIGH_B_LOW = 10041;
  CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_LOW_B_HIGH = 10042;
  CHANNEL_INT32_ENCODER_Z_INDEX_PHASE1_A_LOW_B_LOW = 10043;
  CHANNEL_INT32_EXCITATION_D_COR_AC_DC = 10050;
  CHANNEL_INT32_EXCITATION_D_COR_AC_AC = 10045;
  CHANNEL_INT32_EXCITATION_IDLE_OUTPUT_BEHAVIOR_ZERO_VOLTS_OR_AMPS = 12526;
  CHANNEL_INT32_EXCITATION_IDLE_OUTPUT_BEHAVIOR_MAINTAIN_EXISTING_VALUE = 12528;
  CHANNEL_INT32_EXCITATION_SOURCE_INTERNAL = 10200;
  CHANNEL_INT32_EXCITATION_SOURCE_EXTERNAL = 10167;
  CHANNEL_INT32_EXCITATION_SOURCE_NONE = 10230;
  CHANNEL_INT32_EXCITATION_VOLTAGE_OR_CURRENT_VOLTAGE = 10322;
  CHANNEL_INT32_EXCITATION_VOLTAGE_OR_CURRENT_CURRENT = 10134;
  CHANNEL_INT32_FILTER_RESPONSE_CONSTANT_GROUP_DELAY = 16075;
  CHANNEL_INT32_FILTER_RESPONSE_BUTTERWORTH = 16076;
  CHANNEL_INT32_FILTER_RESPONSE_ELLIPTICAL = 16077;
  CHANNEL_INT32_FILTER_RESPONSE_HARDWARE_DEFINED = 10191;
  CHANNEL_INT32_FILTER_RESPONSE1_COMB = 16152;
  CHANNEL_INT32_FILTER_RESPONSE1_BESSEL = 16153;
  CHANNEL_INT32_FILTER_RESPONSE1_BRICKWALL = 16155;
  CHANNEL_INT32_FILTER_RESPONSE1_BUTTERWORTH = 16076;
  CHANNEL_INT32_FILTER_TYPE1_HARDWARE_DEFINED = 10191;
  CHANNEL_INT32_FILTER_TYPE2_LOWPASS = 16071;
  CHANNEL_INT32_FILTER_TYPE2_HIGHPASS = 16072;
  CHANNEL_INT32_FILTER_TYPE2_BANDPASS = 16073;
  CHANNEL_INT32_FILTER_TYPE2_NOTCH = 16074;
  CHANNEL_INT32_FILTER_TYPE2_CUSTOM = 10137;
  CHANNEL_INT32_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_NEWTON = 15891;
  CHANNEL_INT32_FORCE_IEPE_SENSOR_SENSITIVITY_UNITS_M_VOLTS_PER_POUND = 15892;
  CHANNEL_INT32_FORCE_UNITS_NEWTONS = 15875;
  CHANNEL_INT32_FORCE_UNITS_POUNDS = 15876;
  CHANNEL_INT32_FORCE_UNITS_KILOGRAM_FORCE = 15877;
  CHANNEL_INT32_FORCE_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_FREQUENCY_UNITS_HZ = 10373;
  CHANNEL_INT32_FREQUENCY_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_FREQUENCY_UNITS2_HZ = 10373;
  CHANNEL_INT32_FREQUENCY_UNITS3_HZ = 10373;
  CHANNEL_INT32_FREQUENCY_UNITS3_TICKS = 10304;
  CHANNEL_INT32_FREQUENCY_UNITS3_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_FUNC_GEN_TYPE_SINE = 14751;
  CHANNEL_INT32_FUNC_GEN_TYPE_TRIANGLE = 14752;
  CHANNEL_INT32_FUNC_GEN_TYPE_SQUARE = 14753;
  CHANNEL_INT32_FUNC_GEN_TYPE_SAWTOOTH = 14754;
  CHANNEL_INT32_GPS_SIGNAL_TYPE1_IRIGB = 10070;
  CHANNEL_INT32_GPS_SIGNAL_TYPE1_PPS = 10080;
  CHANNEL_INT32_GPS_SIGNAL_TYPE1_NONE = 10230;
  CHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_MORE_THAN_HALF_FULL = 10237;
  CHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_NOT_EMPTY = 10241;
  CHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_ONBRD_MEM_CUSTOM_THRESHOLD = 12577;
  CHANNEL_INT32_INPUT_DATA_TRANSFER_CONDITION_WHEN_ACQ_COMPLETE = 12546;
  CHANNEL_INT32_INPUT_TERM_CFG_RSE = 10083;
  CHANNEL_INT32_INPUT_TERM_CFG_NRSE = 10078;
  CHANNEL_INT32_INPUT_TERM_CFG_DIFF = 10106;
  CHANNEL_INT32_INPUT_TERM_CFG_PSEUDO_DIFF = 12529;
  CHANNEL_INT32_INPUT_TERM_CFG2_DIFF = 10106;
  CHANNEL_INT32_INPUT_TERM_CFG2_RSE = 10083;
  CHANNEL_INT32_LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLIMETER = 12506;
  CHANNEL_INT32_LVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_MILLI_INCH = 12505;
  CHANNEL_INT32_LENGTH_UNITS2_METERS = 10219;
  CHANNEL_INT32_LENGTH_UNITS2_INCHES = 10379;
  CHANNEL_INT32_LENGTH_UNITS2_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_LENGTH_UNITS3_METERS = 10219;
  CHANNEL_INT32_LENGTH_UNITS3_INCHES = 10379;
  CHANNEL_INT32_LENGTH_UNITS3_TICKS = 10304;
  CHANNEL_INT32_LENGTH_UNITS3_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_LENGTH_UNITS4_METERS = 10219;
  CHANNEL_INT32_LENGTH_UNITS4_FEET = 10380;
  CHANNEL_INT32_LENGTH_UNITS4_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_LEVEL1_HIGH = 10192;
  CHANNEL_INT32_LEVEL1_LOW = 10214;
  CHANNEL_INT32_LOGIC_FAMILY_1POINT_8_V = 16184;
  CHANNEL_INT32_LOGIC_FAMILY_2POINT_5_V = 14620;
  CHANNEL_INT32_LOGIC_FAMILY_3POINT_3_V = 14621;
  CHANNEL_INT32_LOGIC_FAMILY_5_V = 14619;
  CHANNEL_INT32_LOGIC_LVL_BEHAVIOR_LOGIC_LEVEL_PULL_UP = 16064;
  CHANNEL_INT32_LOGIC_LVL_BEHAVIOR_NONE = 10230;
  CHANNEL_INT32_MODULATION_TYPE_AM = 14756;
  CHANNEL_INT32_MODULATION_TYPE_FM = 14757;
  CHANNEL_INT32_MODULATION_TYPE_NONE = 10230;
  CHANNEL_INT32_NAV_MEASUREMENT_TYPE_ALTITUDE = 15997;
  CHANNEL_INT32_NAV_MEASUREMENT_TYPE_LONGITUDE = 15998;
  CHANNEL_INT32_NAV_MEASUREMENT_TYPE_LATITUDE = 15999;
  CHANNEL_INT32_NAV_MEASUREMENT_TYPE_SPEED_OVER_GROUND = 16000;
  CHANNEL_INT32_NAV_MEASUREMENT_TYPE_TRACK = 16001;
  CHANNEL_INT32_NAV_MEASUREMENT_TYPE_TIMESTAMP = 15986;
  CHANNEL_INT32_NAV_MEASUREMENT_TYPE_VERT_VELOCITY = 16003;
  CHANNEL_INT32_OUTPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_EMPTY = 10235;
  CHANNEL_INT32_OUTPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_HALF_FULL_OR_LESS = 10239;
  CHANNEL_INT32_OUTPUT_DATA_TRANSFER_CONDITION_ON_BRD_MEM_NOT_FULL = 10242;
  CHANNEL_INT32_OUTPUT_TERM_CFG_RSE = 10083;
  CHANNEL_INT32_OUTPUT_TERM_CFG_DIFF = 10106;
  CHANNEL_INT32_OUTPUT_TERM_CFG_PSEUDO_DIFF = 12529;
  CHANNEL_INT32_POWER_IDLE_OUTPUT_BEHAVIOR_OUTPUT_DISABLED = 15503;
  CHANNEL_INT32_POWER_IDLE_OUTPUT_BEHAVIOR_MAINTAIN_EXISTING_VALUE = 12528;
  CHANNEL_INT32_POWER_OUTPUT_STATE_CONSTANT_VOLTAGE = 15500;
  CHANNEL_INT32_POWER_OUTPUT_STATE_CONSTANT_CURRENT = 15501;
  CHANNEL_INT32_POWER_OUTPUT_STATE_OVERVOLTAGE = 15502;
  CHANNEL_INT32_POWER_OUTPUT_STATE_OUTPUT_DISABLED = 15503;
  CHANNEL_INT32_POWER_UNITS_WATTS = 16203;
  CHANNEL_INT32_POWER_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_PRESSURE_UNITS_PASCALS = 10081;
  CHANNEL_INT32_PRESSURE_UNITS_POUNDS_PER_SQUARE_INCH = 15879;
  CHANNEL_INT32_PRESSURE_UNITS_BAR = 15880;
  CHANNEL_INT32_PRESSURE_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_RTD_TYPE1_PT_3750 = 12481;
  CHANNEL_INT32_RTD_TYPE1_PT_3851 = 10071;
  CHANNEL_INT32_RTD_TYPE1_PT_3911 = 12482;
  CHANNEL_INT32_RTD_TYPE1_PT_3916 = 10069;
  CHANNEL_INT32_RTD_TYPE1_PT_3920 = 10053;
  CHANNEL_INT32_RTD_TYPE1_PT_3928 = 12483;
  CHANNEL_INT32_RTD_TYPE1_CUSTOM = 10137;
  CHANNEL_INT32_RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_DEGREE = 12507;
  CHANNEL_INT32_RVDT_SENSITIVITY_UNITS1_M_VOLTS_PER_VOLT_PER_RADIAN = 12508;
  CHANNEL_INT32_RAW_DATA_COMPRESSION_TYPE_NONE = 10230;
  CHANNEL_INT32_RAW_DATA_COMPRESSION_TYPE_LOSSLESS_PACKING = 12555;
  CHANNEL_INT32_RAW_DATA_COMPRESSION_TYPE_LOSSY_LSB_REMOVAL = 12556;
  CHANNEL_INT32_RESISTANCE_CONFIGURATION_2_WIRE = 2;
  CHANNEL_INT32_RESISTANCE_CONFIGURATION_3_WIRE = 3;
  CHANNEL_INT32_RESISTANCE_CONFIGURATION_4_WIRE = 4;
  CHANNEL_INT32_RESISTANCE_UNITS1_OHMS = 10384;
  CHANNEL_INT32_RESISTANCE_UNITS1_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_RESISTANCE_UNITS1_FROM_TEDS = 12516;
  CHANNEL_INT32_RESOLUTION_TYPE1_BITS = 10109;
  CHANNEL_INT32_SAMP_CLK_OVERRUN_BEHAVIOR_REPEATED_DATA = 16062;
  CHANNEL_INT32_SAMP_CLK_OVERRUN_BEHAVIOR_SENTINEL_VALUE = 16063;
  CHANNEL_INT32_SAMPLE_CLOCK_ACTIVE_OR_INACTIVE_EDGE_SELECTION_SAMP_CLK_ACTIVE_EDGE = 14617;
  CHANNEL_INT32_SAMPLE_CLOCK_ACTIVE_OR_INACTIVE_EDGE_SELECTION_SAMP_CLK_INACTIVE_EDGE = 14618;
  CHANNEL_INT32_SCALE_TYPE2_POLYNOMIAL = 10449;
  CHANNEL_INT32_SCALE_TYPE2_TABLE = 10450;
  CHANNEL_INT32_SCALE_TYPE3_POLYNOMIAL = 10449;
  CHANNEL_INT32_SCALE_TYPE3_TABLE = 10450;
  CHANNEL_INT32_SCALE_TYPE3_NONE = 10230;
  CHANNEL_INT32_SCALE_TYPE4_NONE = 10230;
  CHANNEL_INT32_SCALE_TYPE4_TWO_POINT_LINEAR = 15898;
  CHANNEL_INT32_SCALE_TYPE4_TABLE = 10450;
  CHANNEL_INT32_SCALE_TYPE4_POLYNOMIAL = 10449;
  CHANNEL_INT32_SENSE_LOCAL = 16095;
  CHANNEL_INT32_SENSE_REMOTE = 16096;
  CHANNEL_INT32_SENSOR_POWER_CFG_NO_CHANGE = 10160;
  CHANNEL_INT32_SENSOR_POWER_CFG_ENABLED = 16145;
  CHANNEL_INT32_SENSOR_POWER_CFG_DISABLED = 16146;
  CHANNEL_INT32_SENSOR_POWER_TYPE_DC = 10050;
  CHANNEL_INT32_SENSOR_POWER_TYPE_AC = 10045;
  CHANNEL_INT32_SENSOR_POWER_TYPE_BIPOLAR_DC = 16147;
  CHANNEL_INT32_SHUNT_CAL_SELECT_A = 12513;
  CHANNEL_INT32_SHUNT_CAL_SELECT_B = 12514;
  CHANNEL_INT32_SHUNT_CAL_SELECT_A_AND_B = 12515;
  CHANNEL_INT32_SOUND_PRESSURE_UNITS1_PASCALS = 10081;
  CHANNEL_INT32_SOUND_PRESSURE_UNITS1_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_SOURCE_SELECTION_INTERNAL = 10200;
  CHANNEL_INT32_SOURCE_SELECTION_EXTERNAL = 10167;
  CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_I = 10183;
  CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_II = 10184;
  CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_FULL_BRIDGE_III = 10185;
  CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_I = 10188;
  CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_HALF_BRIDGE_II = 10189;
  CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_I = 10271;
  CHANNEL_INT32_STRAIN_GAGE_BRIDGE_TYPE1_QUARTER_BRIDGE_II = 10272;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_1 = 15971;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_2 = 15972;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_PRINCIPAL_STRAIN_ANGLE = 15973;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_X = 15974;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_STRAIN_Y = 15975;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_CARTESIAN_SHEAR_STRAIN_XY = 15976;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN = 15977;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_MEASUREMENT_TYPE_MAX_SHEAR_STRAIN_ANGLE = 15978;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_TYPE_RECTANGULAR_ROSETTE = 15968;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_TYPE_DELTA_ROSETTE = 15969;
  CHANNEL_INT32_STRAIN_GAGE_ROSETTE_TYPE_TEE_ROSETTE = 15970;
  CHANNEL_INT32_STRAIN_UNITS1_STRAIN = 10299;
  CHANNEL_INT32_STRAIN_UNITS1_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_SYNC_UNLOCK_BEHAVIOR_STOP_TASK_AND_ERROR = 15862;
  CHANNEL_INT32_SYNC_UNLOCK_BEHAVIOR_IGNORE_LOST_SYNC_LOCK = 16129;
  CHANNEL_INT32_TEMPERATURE_UNITS1_DEG_C = 10143;
  CHANNEL_INT32_TEMPERATURE_UNITS1_DEG_F = 10144;
  CHANNEL_INT32_TEMPERATURE_UNITS1_KELVINS = 10325;
  CHANNEL_INT32_TEMPERATURE_UNITS1_DEG_R = 10145;
  CHANNEL_INT32_TEMPERATURE_UNITS1_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_J_TYPE_TC = 10072;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_K_TYPE_TC = 10073;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_N_TYPE_TC = 10077;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_R_TYPE_TC = 10082;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_S_TYPE_TC = 10085;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_T_TYPE_TC = 10086;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_B_TYPE_TC = 10047;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_E_TYPE_TC = 10055;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_A_TYPE_TC = 16208;
  CHANNEL_INT32_THERMOCOUPLE_TYPE1_C_TYPE_TC = 16209;
  CHANNEL_INT32_TIME_UNITS_SECONDS = 10364;
  CHANNEL_INT32_TIME_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_TIME_UNITS2_SECONDS = 10364;
  CHANNEL_INT32_TIME_UNITS3_SECONDS = 10364;
  CHANNEL_INT32_TIME_UNITS3_TICKS = 10304;
  CHANNEL_INT32_TIME_UNITS3_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_TIMESCALE_TAI = 15988;
  CHANNEL_INT32_TIMESCALE_UTC = 15987;
  CHANNEL_INT32_TORQUE_UNITS_NEWTON_METERS = 15881;
  CHANNEL_INT32_TORQUE_UNITS_INCH_OUNCES = 15882;
  CHANNEL_INT32_TORQUE_UNITS_INCH_POUNDS = 15883;
  CHANNEL_INT32_TORQUE_UNITS_FOOT_POUNDS = 15884;
  CHANNEL_INT32_TORQUE_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLIVOLTS_PER_MILLIMETER_PER_SECOND = 15963;
  CHANNEL_INT32_VELOCITY_IEPE_SENSOR_SENSITIVITY_UNITS_MILLI_VOLTS_PER_INCH_PER_SECOND = 15964;
  CHANNEL_INT32_VELOCITY_UNITS_METERS_PER_SECOND = 15959;
  CHANNEL_INT32_VELOCITY_UNITS_INCHES_PER_SECOND = 15960;
  CHANNEL_INT32_VELOCITY_UNITS_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_VELOCITY_UNITS2_METERS_PER_SECOND = 15959;
  CHANNEL_INT32_VELOCITY_UNITS2_KILOMETERS_PER_HOUR = 16007;
  CHANNEL_INT32_VELOCITY_UNITS2_FEET_PER_SECOND = 16008;
  CHANNEL_INT32_VELOCITY_UNITS2_MILES_PER_HOUR = 16009;
  CHANNEL_INT32_VELOCITY_UNITS2_KNOTS = 16010;
  CHANNEL_INT32_VELOCITY_UNITS2_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_VOLTAGE_UNITS1_VOLTS = 10348;
  CHANNEL_INT32_VOLTAGE_UNITS1_FROM_CUSTOM_SCALE = 10065;
  CHANNEL_INT32_VOLTAGE_UNITS1_FROM_TEDS = 12516;
  CHANNEL_INT32_VOLTAGE_UNITS2_VOLTS = 10348;
  CHANNEL_INT32_VOLTAGE_UNITS2_FROM_CUSTOM_SCALE = 10065;
}

enum DeviceInt32AttributeValues {
  option allow_alias = true;
  DEVICE_INT32_UNSPECIFIED = 0;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE = 10322;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_RMS = 10350;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_CURRENT = 10134;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_CURRENT_RMS = 10351;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_CUSTOM_WITH_EXCITATION = 10323;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_BRIDGE = 15908;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_FREQ_VOLTAGE = 10181;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_RESISTANCE = 10278;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_TC = 10303;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_THRMSTR = 10302;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_RTD = 10301;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_TEMP_BUILT_IN_SENSOR = 10311;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_STRAIN_GAGE = 10300;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_ROSETTE_STRAIN_GAGE = 15980;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_POSITION_LVDT = 10352;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_POSITION_RVDT = 10353;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_POSITION_EDDY_CURRENT_PROXIMITY_PROBE = 14835;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_ACCELEROMETER = 10356;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_CHARGE = 16104;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_4_WIRE_DC_VOLTAGE = 16106;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_VELOCITY_IEPE_SENSOR = 15966;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_FORCE_BRIDGE = 15899;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_FORCE_IEPE_SENSOR = 15895;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_PRESSURE_BRIDGE = 15902;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_SOUND_PRESSURE_MICROPHONE = 10354;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_TORQUE_BRIDGE = 15905;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_TEDS_SENSOR = 12531;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_CHARGE = 16105;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_POWER = 16201;
  DEVICE_INT32_AI_MEASUREMENT_TYPE_CALCULATED_POWER = 16204;
  DEVICE_INT32_AO_OUTPUT_CHANNEL_TYPE_VOLTAGE = 10322;
  DEVICE_INT32_AO_OUTPUT_CHANNEL_TYPE_CURRENT = 10134;
  DEVICE_INT32_AO_OUTPUT_CHANNEL_TYPE_FUNC_GEN = 14750;
  DEVICE_INT32_ACQUISITION_TYPE_FINITE_SAMPS = 10178;
  DEVICE_INT32_ACQUISITION_TYPE_CONT_SAMPS = 10123;
  DEVICE_INT32_ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT = 12522;
  DEVICE_INT32_ALT_REF_MSL = 16005;
  DEVICE_INT32_ALT_REF_HAE = 16006;
  DEVICE_INT32_ANT_STATUS_UNKNOWN = 12588;
  DEVICE_INT32_ANT_STATUS_NORMAL = 10459;
  DEVICE_INT32_ANT_STATUS_ABSENT = 15994;
  DEVICE_INT32_ANT_STATUS_OVERCURRENT = 15995;
  DEVICE_INT32_BUS_TYPE_PCI = 12582;
  DEVICE_INT32_BUS_TYPE_PCIE = 13612;
  DEVICE_INT32_BUS_TYPE_PXI = 12583;
  DEVICE_INT32_BUS_TYPE_PXIE = 14706;
  DEVICE_INT32_BUS_TYPE_SCXI = 12584;
  DEVICE_INT32_BUS_TYPE_SCC = 14707;
  DEVICE_INT32_BUS_TYPE_PC_CARD = 12585;
  DEVICE_INT32_BUS_TYPE_USB = 12586;
  DEVICE_INT32_BUS_TYPE_COMPACT_DAQ = 14637;
  DEVICE_INT32_BUS_TYPE_COMPACT_RIO = 16143;
  DEVICE_INT32_BUS_TYPE_TCPIP = 14828;
  DEVICE_INT32_BUS_TYPE_UNKNOWN = 12588;
  DEVICE_INT32_BUS_TYPE_SWITCH_BLOCK = 15870;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_COUNT_EDGES = 10125;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_FREQ = 10179;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_PERIOD = 10256;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_WIDTH = 10359;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_SEMI_PERIOD = 10289;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_FREQUENCY = 15864;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_TIME = 15865;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_PULSE_TICKS = 15866;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_DUTY_CYCLE = 16070;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_POSITION_ANG_ENCODER = 10360;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_POSITION_LIN_ENCODER = 10361;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_VELOCITY_ANG_ENCODER = 16078;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_VELOCITY_LIN_ENCODER = 16079;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_TWO_EDGE_SEP = 10267;
  DEVICE_INT32_CI_MEASUREMENT_TYPE_GPS_TIMESTAMP = 10362;
  DEVICE_INT32_CO_OUTPUT_TYPE_PULSE_TIME = 10269;
  DEVICE_INT32_CO_OUTPUT_TYPE_PULSE_FREQ = 10119;
  DEVICE_INT32_CO_OUTPUT_TYPE_PULSE_TICKS = 10268;
  DEVICE_INT32_COUPLING_TYPES_AC = 1;
  DEVICE_INT32_COUPLING_TYPES_DC = 2;
  DEVICE_INT32_COUPLING_TYPES_GROUND = 4;
  DEVICE_INT32_COUPLING_TYPES_HF_REJECT = 8;
  DEVICE_INT32_COUPLING_TYPES_LF_REJECT = 16;
  DEVICE_INT32_COUPLING_TYPES_NOISE_REJECT = 32;
  DEVICE_INT32_FILTER_TYPE2_LOWPASS = 16071;
  DEVICE_INT32_FILTER_TYPE2_HIGHPASS = 16072;
  DEVICE_INT32_FILTER_TYPE2_BANDPASS = 16073;
  DEVICE_INT32_FILTER_TYPE2_NOTCH = 16074;
  DEVICE_INT32_FILTER_TYPE2_CUSTOM = 10137;
  DEVICE_INT32_ID_PIN_STATUS_MEMORY_NOT_PRESENT = 16205;
  DEVICE_INT32_ID_PIN_STATUS_MEMORY_PRESENT = 16206;
  DEVICE_INT32_NAV_MEASUREMENT_TYPE_ALTITUDE = 15997;
  DEVICE_INT32_NAV_MEASUREMENT_TYPE_LONGITUDE = 15998;
  DEVICE_INT32_NAV_MEASUREMENT_TYPE_LATITUDE = 15999;
  DEVICE_INT32_NAV_MEASUREMENT_TYPE_SPEED_OVER_GROUND = 16000;
  DEVICE_INT32_NAV_MEASUREMENT_TYPE_TRACK = 16001;
  DEVICE_INT32_NAV_MEASUREMENT_TYPE_TIMESTAMP = 15986;
  DEVICE_INT32_NAV_MEASUREMENT_TYPE_VERT_VELOCITY = 16003;
  DEVICE_INT32_NAV_MODE_MOBILE = 15989;
  DEVICE_INT32_NAV_MODE_STATIONARY_WITH_SURVEY = 15990;
  DEVICE_INT32_NAV_MODE_STATIONARY_WITH_PRESET_LOCATION = 15991;
  DEVICE_INT32_PRODUCT_CATEGORY_M_SERIES_DAQ = 14643;
  DEVICE_INT32_PRODUCT_CATEGORY_X_SERIES_DAQ = 15858;
  DEVICE_INT32_PRODUCT_CATEGORY_E_SERIES_DAQ = 14642;
  DEVICE_INT32_PRODUCT_CATEGORY_S_SERIES_DAQ = 14644;
  DEVICE_INT32_PRODUCT_CATEGORY_B_SERIES_DAQ = 14662;
  DEVICE_INT32_PRODUCT_CATEGORY_SC_SERIES_DAQ = 14645;
  DEVICE_INT32_PRODUCT_CATEGORY_USBDAQ = 14646;
  DEVICE_INT32_PRODUCT_CATEGORY_AO_SERIES = 14647;
  DEVICE_INT32_PRODUCT_CATEGORY_DIGITAL_IO = 14648;
  DEVICE_INT32_PRODUCT_CATEGORY_TIO_SERIES = 14661;
  DEVICE_INT32_PRODUCT_CATEGORY_DYNAMIC_SIGNAL_ACQUISITION = 14649;
  DEVICE_INT32_PRODUCT_CATEGORY_SWITCHES = 14650;
  DEVICE_INT32_PRODUCT_CATEGORY_COMPACT_DAQ_CHASSIS = 14658;
  DEVICE_INT32_PRODUCT_CATEGORY_COMPACT_RIO_CHASSIS = 16144;
  DEVICE_INT32_PRODUCT_CATEGORY_C_SERIES_MODULE = 14659;
  DEVICE_INT32_PRODUCT_CATEGORY_SCXI_MODULE = 14660;
  DEVICE_INT32_PRODUCT_CATEGORY_SCC_CONNECTOR_BLOCK = 14704;
  DEVICE_INT32_PRODUCT_CATEGORY_SCC_MODULE = 14705;
  DEVICE_INT32_PRODUCT_CATEGORY_NIELVIS = 14755;
  DEVICE_INT32_PRODUCT_CATEGORY_NETWORK_DAQ = 14829;
  DEVICE_INT32_PRODUCT_CATEGORY_SC_EXPRESS = 15886;
  DEVICE_INT32_PRODUCT_CATEGORY_FIELD_DAQ = 16151;
  DEVICE_INT32_PRODUCT_CATEGORY_TEST_SCALE_CHASSIS = 16180;
  DEVICE_INT32_PRODUCT_CATEGORY_TEST_SCALE_MODULE = 16181;
  DEVICE_INT32_PRODUCT_CATEGORY_MIO_DAQ = 16182;
  DEVICE_INT32_PRODUCT_CATEGORY_UNKNOWN = 12588;
  DEVICE_INT32_TRIGGER_USAGE_ADVANCE = 12488;
  DEVICE_INT32_TRIGGER_USAGE_PAUSE = 12489;
  DEVICE_INT32_TRIGGER_USAGE_REFERENCE = 12490;
  DEVICE_INT32_TRIGGER_USAGE_START = 12491;
  DEVICE_INT32_TRIGGER_USAGE_HANDSHAKE = 10389;
  DEVICE_INT32_TRIGGER_USAGE_ARM_START = 14641;
  DEVICE_INT32_TRIGGER_USAGE_TYPES_ADVANCE = 1;
  DEVICE_INT32_TRIGGER_USAGE_TYPES_PAUSE = 2;
  DEVICE_INT32_TRIGGER_USAGE_TYPES_REFERENCE = 4;
  DEVICE_INT32_TRIGGER_USAGE_TYPES_START = 8;
  DEVICE_INT32_TRIGGER_USAGE_TYPES_HANDSHAKE = 16;
  DEVICE_INT32_TRIGGER_USAGE_TYPES_ARM_START = 32;
}

enum ExportSignalInt32AttributeValues {
  option allow_alias = true;
  EXPORTSIGNAL_INT32_UNSPECIFIED = 0;
  EXPORTSIGNAL_INT32_DEASSERT_CONDITION_ONBRD_MEM_MORE_THAN_HALF_FULL = 10237;
  EXPORTSIGNAL_INT32_DEASSERT_CONDITION_ONBRD_MEM_FULL = 10236;
  EXPORTSIGNAL_INT32_DEASSERT_CONDITION_ONBRD_MEM_CUSTOM_THRESHOLD = 12577;
  EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS1_SAMP_CLK_PERIODS = 10286;
  EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS1_SECONDS = 10364;
  EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS1_TICKS = 10304;
  EXPORTSIGNAL_INT32_DIGITAL_WIDTH_UNITS3_SECONDS = 10364;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS_PULSE = 10265;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS_TOGGLE = 10307;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS_LVL = 10210;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS2_PULSE = 10265;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS2_TOGGLE = 10307;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS3_PULSE = 10265;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS3_LVL = 10210;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS5_INTERLOCKED = 12549;
  EXPORTSIGNAL_INT32_EXPORT_ACTIONS5_PULSE = 10265;
  EXPORTSIGNAL_INT32_LEVEL1_HIGH = 10192;
  EXPORTSIGNAL_INT32_LEVEL1_LOW = 10214;
  EXPORTSIGNAL_INT32_POLARITY2_ACTIVE_HIGH = 10095;
  EXPORTSIGNAL_INT32_POLARITY2_ACTIVE_LOW = 10096;
}

enum PhysicalChannelInt32AttributeValues {
  option allow_alias = true;
  PHYSICALCHANNEL_INT32_UNSPECIFIED = 0;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE = 10322;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_RMS = 10350;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT = 10134;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CURRENT_RMS = 10351;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VOLTAGE_CUSTOM_WITH_EXCITATION = 10323;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_BRIDGE = 15908;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_FREQ_VOLTAGE = 10181;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_RESISTANCE = 10278;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_TC = 10303;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_THRMSTR = 10302;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_RTD = 10301;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEMP_BUILT_IN_SENSOR = 10311;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_STRAIN_GAGE = 10300;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ROSETTE_STRAIN_GAGE = 15980;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_LVDT = 10352;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_RVDT = 10353;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POSITION_EDDY_CURRENT_PROXIMITY_PROBE = 14835;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELEROMETER = 10356;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_CHARGE = 16104;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_ACCELERATION_4_WIRE_DC_VOLTAGE = 16106;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_VELOCITY_IEPE_SENSOR = 15966;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_BRIDGE = 15899;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_FORCE_IEPE_SENSOR = 15895;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_PRESSURE_BRIDGE = 15902;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_SOUND_PRESSURE_MICROPHONE = 10354;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TORQUE_BRIDGE = 15905;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_TEDS_SENSOR = 12531;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CHARGE = 16105;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_POWER = 16201;
  PHYSICALCHANNEL_INT32_AI_MEASUREMENT_TYPE_CALCULATED_POWER = 16204;
  PHYSICALCHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_VOLTAGE = 10322;
  PHYSICALCHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_CURRENT = 10134;
  PHYSICALCHANNEL_INT32_AO_OUTPUT_CHANNEL_TYPE_FUNC_GEN = 14750;
  PHYSICALCHANNEL_INT32_AO_POWER_UP_OUTPUT_BEHAVIOR_VOLTAGE = 10322;
  PHYSICALCHANNEL_INT32_AO_POWER_UP_OUTPUT_BEHAVIOR_CURRENT = 10134;
  PHYSICALCHANNEL_INT32_AO_POWER_UP_OUTPUT_BEHAVIOR_HIGH_IMPEDANCE = 12527;
  PHYSICALCHANNEL_INT32_ACQUISITION_TYPE_FINITE_SAMPS = 10178;
  PHYSICALCHANNEL_INT32_ACQUISITION_TYPE_CONT_SAMPS = 10123;
  PHYSICALCHANNEL_INT32_ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT = 12522;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_COUNT_EDGES = 10125;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_FREQ = 10179;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PERIOD = 10256;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_WIDTH = 10359;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_SEMI_PERIOD = 10289;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_FREQUENCY = 15864;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TIME = 15865;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_PULSE_TICKS = 15866;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_DUTY_CYCLE = 16070;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_ANG_ENCODER = 10360;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_POSITION_LIN_ENCODER = 10361;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_ANG_ENCODER = 16078;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_VELOCITY_LIN_ENCODER = 16079;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_TWO_EDGE_SEP = 10267;
  PHYSICALCHANNEL_INT32_CI_MEASUREMENT_TYPE_GPS_TIMESTAMP = 10362;
  PHYSICALCHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TIME = 10269;
  PHYSICALCHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_FREQ = 10119;
  PHYSICALCHANNEL_INT32_CO_OUTPUT_TYPE_PULSE_TICKS = 10268;
  PHYSICALCHANNEL_INT32_LOGIC_FAMILY_1POINT_8_V = 16184;
  PHYSICALCHANNEL_INT32_LOGIC_FAMILY_2POINT_5_V = 14620;
  PHYSICALCHANNEL_INT32_LOGIC_FAMILY_3POINT_3_V = 14621;
  PHYSICALCHANNEL_INT32_LOGIC_FAMILY_5_V = 14619;
  PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_ALTITUDE = 15997;
  PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_LONGITUDE = 15998;
  PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_LATITUDE = 15999;
  PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_SPEED_OVER_GROUND = 16000;
  PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_TRACK = 16001;
  PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_TIMESTAMP = 15986;
  PHYSICALCHANNEL_INT32_NAV_MEASUREMENT_TYPE_VERT_VELOCITY = 16003;
  PHYSICALCHANNEL_INT32_SENSOR_POWER_TYPE_DC = 10050;
  PHYSICALCHANNEL_INT32_SENSOR_POWER_TYPE_AC = 10045;
  PHYSICALCHANNEL_INT32_SENSOR_POWER_TYPE_BIPOLAR_DC = 16147;
  PHYSICALCHANNEL_INT32_TERM_CFG_RSE = 1;
  PHYSICALCHANNEL_INT32_TERM_CFG_NRSE = 2;
  PHYSICALCHANNEL_INT32_TERM_CFG_DIFF = 4;
  PHYSICALCHANNEL_INT32_TERM_CFG_PSEUDO_DIFF = 8;
}

enum ReadInt32AttributeValues {
  READ_INT32_UNSPECIFIED = 0;
  READ_INT32_LOGGING_MODE_OFF = 10231;
  READ_INT32_LOGGING_MODE_LOG = 15844;
  READ_INT32_LOGGING_MODE_LOG_AND_READ = 15842;
  READ_INT32_LOGGING_OPERATION_OPEN = 10437;
  READ_INT32_LOGGING_OPERATION_OPEN_OR_CREATE = 15846;
  READ_INT32_LOGGING_OPERATION_CREATE_OR_REPLACE = 15847;
  READ_INT32_LOGGING_OPERATION_CREATE = 15848;
  READ_INT32_OVERWRITE_MODE1_OVERWRITE_UNREAD_SAMPS = 10252;
  READ_INT32_OVERWRITE_MODE1_DO_NOT_OVERWRITE_UNREAD_SAMPS = 10159;
  READ_INT32_READ_RELATIVE_TO_FIRST_SAMPLE = 10424;
  READ_INT32_READ_RELATIVE_TO_CURR_READ_POS = 10425;
  READ_INT32_READ_RELATIVE_TO_REF_TRIG = 10426;
  READ_INT32_READ_RELATIVE_TO_FIRST_PRETRIG_SAMP = 10427;
  READ_INT32_READ_RELATIVE_TO_MOST_RECENT_SAMP = 10428;
  READ_INT32_WAIT_MODE_WAIT_FOR_INTERRUPT = 12523;
  READ_INT32_WAIT_MODE_POLL = 12524;
  READ_INT32_WAIT_MODE_YIELD = 12525;
  READ_INT32_WAIT_MODE_SLEEP = 12547;
}

enum RealTimeInt32AttributeValues {
  option allow_alias = true;
  REALTIME_INT32_UNSPECIFIED = 0;
  REALTIME_INT32_WAIT_MODE3_WAIT_FOR_INTERRUPT = 12523;
  REALTIME_INT32_WAIT_MODE3_POLL = 12524;
  REALTIME_INT32_WAIT_MODE4_WAIT_FOR_INTERRUPT = 12523;
  REALTIME_INT32_WAIT_MODE4_POLL = 12524;
}

enum ScaleInt32AttributeValues {
  SCALE_INT32_UNSPECIFIED = 0;
  SCALE_INT32_SCALE_TYPE_LINEAR = 10447;
  SCALE_INT32_SCALE_TYPE_MAP_RANGES = 10448;
  SCALE_INT32_SCALE_TYPE_POLYNOMIAL = 10449;
  SCALE_INT32_SCALE_TYPE_TABLE = 10450;
  SCALE_INT32_UNITS_PRE_SCALED_VOLTS = 10348;
  SCALE_INT32_UNITS_PRE_SCALED_AMPS = 10342;
  SCALE_INT32_UNITS_PRE_SCALED_DEG_F = 10144;
  SCALE_INT32_UNITS_PRE_SCALED_DEG_C = 10143;
  SCALE_INT32_UNITS_PRE_SCALED_DEG_R = 10145;
  SCALE_INT32_UNITS_PRE_SCALED_KELVINS = 10325;
  SCALE_INT32_UNITS_PRE_SCALED_STRAIN = 10299;
  SCALE_INT32_UNITS_PRE_SCALED_OHMS = 10384;
  SCALE_INT32_UNITS_PRE_SCALED_HZ = 10373;
  SCALE_INT32_UNITS_PRE_SCALED_SECONDS = 10364;
  SCALE_INT32_UNITS_PRE_SCALED_METERS = 10219;
  SCALE_INT32_UNITS_PRE_SCALED_INCHES = 10379;
  SCALE_INT32_UNITS_PRE_SCALED_DEGREES = 10146;
  SCALE_INT32_UNITS_PRE_SCALED_RADIANS = 10273;
  SCALE_INT32_UNITS_PRE_SCALED_TICKS = 10304;
  SCALE_INT32_UNITS_PRE_SCALED_RPM = 16080;
  SCALE_INT32_UNITS_PRE_SCALED_RADIANS_PER_SECOND = 16081;
  SCALE_INT32_UNITS_PRE_SCALED_DEGREES_PER_SECOND = 16082;
  SCALE_INT32_UNITS_PRE_SCALED_G = 10186;
  SCALE_INT32_UNITS_PRE_SCALED_METERS_PER_SECOND_SQUARED = 12470;
  SCALE_INT32_UNITS_PRE_SCALED_INCHES_PER_SECOND_SQUARED = 12471;
  SCALE_INT32_UNITS_PRE_SCALED_METERS_PER_SECOND = 15959;
  SCALE_INT32_UNITS_PRE_SCALED_INCHES_PER_SECOND = 15960;
  SCALE_INT32_UNITS_PRE_SCALED_PASCALS = 10081;
  SCALE_INT32_UNITS_PRE_SCALED_NEWTONS = 15875;
  SCALE_INT32_UNITS_PRE_SCALED_POUNDS = 15876;
  SCALE_INT32_UNITS_PRE_SCALED_KILOGRAM_FORCE = 15877;
  SCALE_INT32_UNITS_PRE_SCALED_POUNDS_PER_SQUARE_INCH = 15879;
  SCALE_INT32_UNITS_PRE_SCALED_BAR = 15880;
  SCALE_INT32_UNITS_PRE_SCALED_NEWTON_METERS = 15881;
  SCALE_INT32_UNITS_PRE_SCALED_INCH_OUNCES = 15882;
  SCALE_INT32_UNITS_PRE_SCALED_INCH_POUNDS = 15883;
  SCALE_INT32_UNITS_PRE_SCALED_FOOT_POUNDS = 15884;
  SCALE_INT32_UNITS_PRE_SCALED_VOLTS_PER_VOLT = 15896;
  SCALE_INT32_UNITS_PRE_SCALED_M_VOLTS_PER_VOLT = 15897;
  SCALE_INT32_UNITS_PRE_SCALED_COULOMBS = 16102;
  SCALE_INT32_UNITS_PRE_SCALED_PICO_COULOMBS = 16103;
  SCALE_INT32_UNITS_PRE_SCALED_FROM_TEDS = 12516;
}

enum TimingInt32AttributeValues {
  TIMING_INT32_UNSPECIFIED = 0;
  TIMING_INT32_ACQUISITION_TYPE_FINITE_SAMPS = 10178;
  TIMING_INT32_ACQUISITION_TYPE_CONT_SAMPS = 10123;
  TIMING_INT32_ACQUISITION_TYPE_HW_TIMED_SINGLE_POINT = 12522;
  TIMING_INT32_DIGITAL_WIDTH_UNITS2_SECONDS = 10364;
  TIMING_INT32_DIGITAL_WIDTH_UNITS2_TICKS = 10304;
  TIMING_INT32_EDGE1_RISING = 10280;
  TIMING_INT32_EDGE1_FALLING = 10171;
  TIMING_INT32_HANDSHAKE_START_CONDITION_IMMEDIATE = 10198;
  TIMING_INT32_HANDSHAKE_START_CONDITION_WAIT_FOR_HANDSHAKE_TRIGGER_ASSERT = 12550;
  TIMING_INT32_HANDSHAKE_START_CONDITION_WAIT_FOR_HANDSHAKE_TRIGGER_DEASSERT = 12551;
  TIMING_INT32_MIOAI_CONVERT_TB_SRC_SAME_AS_SAMP_TIMEBASE = 10284;
  TIMING_INT32_MIOAI_CONVERT_TB_SRC_SAME_AS_MASTER_TIMEBASE = 10282;
  TIMING_INT32_MIOAI_CONVERT_TB_SRC_100_MHZ_TIMEBASE = 15857;
  TIMING_INT32_MIOAI_CONVERT_TB_SRC_80_MHZ_TIMEBASE = 14636;
  TIMING_INT32_MIOAI_CONVERT_TB_SRC_20_MHZ_TIMEBASE = 12537;
  TIMING_INT32_MIOAI_CONVERT_TB_SRC_8_MHZ_TIMEBASE = 16023;
  TIMING_INT32_OVERFLOW_BEHAVIOR_STOP_TASK_AND_ERROR = 15862;
  TIMING_INT32_OVERFLOW_BEHAVIOR_IGNORE_OVERRUNS = 15863;
  TIMING_INT32_SAMPLE_INPUT_DATA_WHEN_HANDSHAKE_TRIGGER_ASSERTS = 12552;
  TIMING_INT32_SAMPLE_INPUT_DATA_WHEN_HANDSHAKE_TRIGGER_DEASSERTS = 12553;
  TIMING_INT32_SAMPLE_TIMING_TYPE_SAMP_CLK = 10388;
  TIMING_INT32_SAMPLE_TIMING_TYPE_BURST_HANDSHAKE = 12548;
  TIMING_INT32_SAMPLE_TIMING_TYPE_HANDSHAKE = 10389;
  TIMING_INT32_SAMPLE_TIMING_TYPE_IMPLICIT = 10451;
  TIMING_INT32_SAMPLE_TIMING_TYPE_ON_DEMAND = 10390;
  TIMING_INT32_SAMPLE_TIMING_TYPE_CHANGE_DETECTION = 12504;
  TIMING_INT32_SAMPLE_TIMING_TYPE_PIPELINED_SAMP_CLK = 14668;
  TIMING_INT32_SYNC_PULSE_TYPE_ONBOARD = 16128;
  TIMING_INT32_SYNC_PULSE_TYPE_DIG_EDGE = 10150;
  TIMING_INT32_SYNC_PULSE_TYPE_TIME = 15996;
  TIMING_INT32_TIMESCALE2_HOST_TIME = 16126;
  TIMING_INT32_TIMESCALE2_IO_DEVICE_TIME = 16127;
  TIMING_INT32_UNDERFLOW_BEHAVIOR_HALT_OUTPUT_AND_ERROR = 14615;
  TIMING_INT32_UNDERFLOW_BEHAVIOR_PAUSE_UNTIL_DATA_AVAILABLE = 14616;
}

enum TriggerInt32AttributeValues {
  option allow_alias = true;
  TRIGGER_INT32_UNSPECIFIED = 0;
  TRIGGER_INT32_ACTIVE_LEVEL_ABOVE_LVL = 10093;
  TRIGGER_INT32_ACTIVE_LEVEL_BELOW_LVL = 10107;
  TRIGGER_INT32_COUPLING2_AC = 10045;
  TRIGGER_INT32_COUPLING2_DC = 10050;
  TRIGGER_INT32_DIGITAL_PATTERN_CONDITION1_PATTERN_MATCHES = 10254;
  TRIGGER_INT32_DIGITAL_PATTERN_CONDITION1_PATTERN_DOES_NOT_MATCH = 10253;
  TRIGGER_INT32_DIGITAL_WIDTH_UNITS1_SAMP_CLK_PERIODS = 10286;
  TRIGGER_INT32_DIGITAL_WIDTH_UNITS1_SECONDS = 10364;
  TRIGGER_INT32_DIGITAL_WIDTH_UNITS1_TICKS = 10304;
  TRIGGER_INT32_EDGE1_RISING = 10280;
  TRIGGER_INT32_EDGE1_FALLING = 10171;
  TRIGGER_INT32_LEVEL1_HIGH = 10192;
  TRIGGER_INT32_LEVEL1_LOW = 10214;
  TRIGGER_INT32_SLOPE1_RISING_SLOPE = 10280;
  TRIGGER_INT32_SLOPE1_FALLING_SLOPE = 10171;
  TRIGGER_INT32_SYNC_TYPE_NONE = 10230;
  TRIGGER_INT32_SYNC_TYPE_MASTER = 15888;
  TRIGGER_INT32_SYNC_TYPE_SLAVE = 15889;
  TRIGGER_INT32_TIMESCALE2_HOST_TIME = 16126;
  TRIGGER_INT32_TIMESCALE2_IO_DEVICE_TIME = 16127;
  TRIGGER_INT32_TRIGGER_TYPE10_ANLG_EDGE = 10099;
  TRIGGER_INT32_TRIGGER_TYPE10_ANLG_MULTI_EDGE = 16108;
  TRIGGER_INT32_TRIGGER_TYPE10_DIG_EDGE = 10150;
  TRIGGER_INT32_TRIGGER_TYPE10_DIG_PATTERN = 10398;
  TRIGGER_INT32_TRIGGER_TYPE10_ANLG_WIN = 10103;
  TRIGGER_INT32_TRIGGER_TYPE10_TIME = 15996;
  TRIGGER_INT32_TRIGGER_TYPE10_NONE = 10230;
  TRIGGER_INT32_TRIGGER_TYPE4_DIG_EDGE = 10150;
  TRIGGER_INT32_TRIGGER_TYPE4_TIME = 15996;
  TRIGGER_INT32_TRIGGER_TYPE4_NONE = 10230;
  TRIGGER_INT32_TRIGGER_TYPE5_DIG_EDGE = 10150;
  TRIGGER_INT32_TRIGGER_TYPE5_SOFTWARE = 10292;
  TRIGGER_INT32_TRIGGER_TYPE5_NONE = 10230;
  TRIGGER_INT32_TRIGGER_TYPE6_ANLG_LVL = 10101;
  TRIGGER_INT32_TRIGGER_TYPE6_ANLG_WIN = 10103;
  TRIGGER_INT32_TRIGGER_TYPE6_DIG_LVL = 10152;
  TRIGGER_INT32_TRIGGER_TYPE6_DIG_PATTERN = 10398;
  TRIGGER_INT32_TRIGGER_TYPE6_NONE = 10230;
  TRIGGER_INT32_TRIGGER_TYPE8_ANLG_EDGE = 10099;
  TRIGGER_INT32_TRIGGER_TYPE8_ANLG_MULTI_EDGE = 16108;
  TRIGGER_INT32_TRIGGER_TYPE8_DIG_EDGE = 10150;
  TRIGGER_INT32_TRIGGER_TYPE8_DIG_PATTERN = 10398;
  TRIGGER_INT32_TRIGGER_TYPE8_ANLG_WIN = 10103;
  TRIGGER_INT32_TRIGGER_TYPE8_TIME = 15996;
  TRIGGER_INT32_TRIGGER_TYPE8_NONE = 10230;
  TRIGGER_INT32_TRIGGER_TYPE9_INTERLOCKED = 12549;
  TRIGGER_INT32_TRIGGER_TYPE9_NONE = 10230;
  TRIGGER_INT32_WINDOW_TRIGGER_CONDITION1_ENTERING_WIN = 10163;
  TRIGGER_INT32_WINDOW_TRIGGER_CONDITION1_LEAVING_WIN = 10208;
  TRIGGER_INT32_WINDOW_TRIGGER_CONDITION2_INSIDE_WIN = 10199;
  TRIGGER_INT32_WINDOW_TRIGGER_CONDITION2_OUTSIDE_WIN = 10251;
}

enum WatchdogInt32AttributeValues {
  option allow_alias = true;
  WATCHDOG_INT32_UNSPECIFIED = 0;
  WATCHDOG_INT32_DIGITAL_LINE_STATE_HIGH = 10192;
  WATCHDOG_INT32_DIGITAL_LINE_STATE_LOW = 10214;
  WATCHDOG_INT32_DIGITAL_LINE_STATE_TRISTATE = 10310;
  WATCHDOG_INT32_DIGITAL_LINE_STATE_NO_CHANGE = 10160;
  WATCHDOG_INT32_EDGE1_RISING = 10280;
  WATCHDOG_INT32_EDGE1_FALLING = 10171;
  WATCHDOG_INT32_TRIGGER_TYPE4_DIG_EDGE = 10150;
  WATCHDOG_INT32_TRIGGER_TYPE4_TIME = 15996;
  WATCHDOG_INT32_TRIGGER_TYPE4_NONE = 10230;
  WATCHDOG_INT32_WATCHDOG_AO_EXPIR_STATE_VOLTAGE = 10322;
  WATCHDOG_INT32_WATCHDOG_AO_EXPIR_STATE_CURRENT = 10134;
  WATCHDOG_INT32_WATCHDOG_AO_EXPIR_STATE_NO_CHANGE = 10160;
  WATCHDOG_INT32_WATCHDOG_CO_EXPIR_STATE_LOW = 10214;
  WATCHDOG_INT32_WATCHDOG_CO_EXPIR_STATE_HIGH = 10192;
  WATCHDOG_INT32_WATCHDOG_CO_EXPIR_STATE_NO_CHANGE = 10160;
}

enum WriteInt32AttributeValues {
  WRITE_INT32_UNSPECIFIED = 0;
  WRITE_INT32_REGENERATION_MODE1_ALLOW_REGEN = 10097;
  WRITE_INT32_REGENERATION_MODE1_DO_NOT_ALLOW_REGEN = 10158;
  WRITE_INT32_WAIT_MODE2_POLL = 12524;
  WRITE_INT32_WAIT_MODE2_YIELD = 12525;
  WRITE_INT32_WAIT_MODE2_SLEEP = 12547;
  WRITE_INT32_WRITE_RELATIVE_TO_FIRST_SAMPLE = 10424;
  WRITE_INT32_WRITE_RELATIVE_TO_CURR_WRITE_POS = 10430;
}

message AnalogPowerUpChannelsAndState {
  string channel_names = 1;
  double state = 2;
  PowerUpChannelType channel_type = 3;
}

message WatchdogExpChannelsAndState {
  string lines = 1;
  DigitalLineState exp_state = 2;
}

message DigitalPowerUpTypeAndChannel {
  string channel_name = 1;
  PowerUpStates state = 2;
}

message DigitalPowerUpChannelsAndState {
  string channel_names = 1;
  PowerUpStates state = 2;
}

message DigitalPullUpPullDownChannelsAndState {
  string channel_names = 1;
  ResistorState state = 2;
}

message AnalogPowerUpChannelAndType {
  string channel_name = 1;
  PowerUpChannelType channel_type = 2;
}

message AddCDAQSyncConnectionRequest {
  string port_list = 1;
}

message AddCDAQSyncConnectionResponse {
  int32 status = 1;
}

message AddGlobalChansToTaskRequest {
  nidevice_grpc.Session task = 1;
  string channel_names = 2;
}

message AddGlobalChansToTaskResponse {
  int32 status = 1;
}

message AddNetworkDeviceRequest {
  string ip_address = 1;
  string device_name = 2;
  bool attempt_reservation = 3;
  double timeout = 4;
}

message AddNetworkDeviceResponse {
  int32 status = 1;
  string device_name_out = 2;
}

message AreConfiguredCDAQSyncPortsDisconnectedRequest {
  string chassis_devices_ports = 1;
  double timeout = 2;
}

message AreConfiguredCDAQSyncPortsDisconnectedResponse {
  int32 status = 1;
  bool disconnected_ports_exist = 2;
}

message AutoConfigureCDAQSyncConnectionsRequest {
  string chassis_devices_ports = 1;
  double timeout = 2;
}

message AutoConfigureCDAQSyncConnectionsResponse {
  int32 status = 1;
}

message CalculateReversePolyCoeffRequest {
  repeated double forward_coeffs = 1;
  double min_val_x = 2;
  double max_val_x = 3;
  int32 num_points_to_compute = 4;
  int32 reverse_poly_order = 5;
}

message CalculateReversePolyCoeffResponse {
  int32 status = 1;
  repeated double reverse_coeffs = 2;
}

message CfgAnlgEdgeRefTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  oneof trigger_slope_enum {
    Slope1 trigger_slope = 3;
    int32 trigger_slope_raw = 4;
  }
  double trigger_level = 5;
  uint32 pretrigger_samples = 6;
}

message CfgAnlgEdgeRefTrigResponse {
  int32 status = 1;
}

message CfgAnlgEdgeStartTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  oneof trigger_slope_enum {
    Slope1 trigger_slope = 3;
    int32 trigger_slope_raw = 4;
  }
  double trigger_level = 5;
}

message CfgAnlgEdgeStartTrigResponse {
  int32 status = 1;
}

message CfgAnlgMultiEdgeRefTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_sources = 2;
  repeated Slope1 trigger_slope_array = 3;
  repeated double trigger_level_array = 4;
  uint32 pretrigger_samples = 5;
}

message CfgAnlgMultiEdgeRefTrigResponse {
  int32 status = 1;
}

message CfgAnlgMultiEdgeStartTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_sources = 2;
  repeated Slope1 trigger_slope_array = 3;
  repeated double trigger_level_array = 4;
}

message CfgAnlgMultiEdgeStartTrigResponse {
  int32 status = 1;
}

message CfgAnlgWindowRefTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  oneof trigger_when_enum {
    WindowTriggerCondition1 trigger_when = 3;
    int32 trigger_when_raw = 4;
  }
  double window_top = 5;
  double window_bottom = 6;
  uint32 pretrigger_samples = 7;
}

message CfgAnlgWindowRefTrigResponse {
  int32 status = 1;
}

message CfgAnlgWindowStartTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  oneof trigger_when_enum {
    WindowTriggerCondition1 trigger_when = 3;
    int32 trigger_when_raw = 4;
  }
  double window_top = 5;
  double window_bottom = 6;
}

message CfgAnlgWindowStartTrigResponse {
  int32 status = 1;
}

message CfgBurstHandshakingTimingExportClockRequest {
  nidevice_grpc.Session task = 1;
  oneof sample_mode_enum {
    AcquisitionType sample_mode = 2;
    int32 sample_mode_raw = 3;
  }
  uint64 samps_per_chan = 4;
  double sample_clk_rate = 5;
  string sample_clk_outp_term = 6;
  oneof sample_clk_pulse_polarity_enum {
    Polarity2 sample_clk_pulse_polarity = 7;
    int32 sample_clk_pulse_polarity_raw = 8;
  }
  oneof pause_when_enum {
    Level1 pause_when = 9;
    int32 pause_when_raw = 10;
  }
  oneof ready_event_active_level_enum {
    Polarity2 ready_event_active_level = 11;
    int32 ready_event_active_level_raw = 12;
  }
}

message CfgBurstHandshakingTimingExportClockResponse {
  int32 status = 1;
}

message CfgBurstHandshakingTimingImportClockRequest {
  nidevice_grpc.Session task = 1;
  oneof sample_mode_enum {
    AcquisitionType sample_mode = 2;
    int32 sample_mode_raw = 3;
  }
  uint64 samps_per_chan = 4;
  double sample_clk_rate = 5;
  string sample_clk_src = 6;
  oneof sample_clk_active_edge_enum {
    Edge1 sample_clk_active_edge = 7;
    int32 sample_clk_active_edge_raw = 8;
  }
  oneof pause_when_enum {
    Level1 pause_when = 9;
    int32 pause_when_raw = 10;
  }
  oneof ready_event_active_level_enum {
    Polarity2 ready_event_active_level = 11;
    int32 ready_event_active_level_raw = 12;
  }
}

message CfgBurstHandshakingTimingImportClockResponse {
  int32 status = 1;
}

message CfgChangeDetectionTimingRequest {
  nidevice_grpc.Session task = 1;
  string rising_edge_chan = 2;
  string falling_edge_chan = 3;
  oneof sample_mode_enum {
    AcquisitionType sample_mode = 4;
    int32 sample_mode_raw = 5;
  }
  uint64 samps_per_chan = 6;
}

message CfgChangeDetectionTimingResponse {
  int32 status = 1;
}

message CfgDigEdgeRefTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  oneof trigger_edge_enum {
    Edge1 trigger_edge = 3;
    int32 trigger_edge_raw = 4;
  }
  uint32 pretrigger_samples = 5;
}

message CfgDigEdgeRefTrigResponse {
  int32 status = 1;
}

message CfgDigEdgeStartTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  oneof trigger_edge_enum {
    Edge1 trigger_edge = 3;
    int32 trigger_edge_raw = 4;
  }
}

message CfgDigEdgeStartTrigResponse {
  int32 status = 1;
}

message CfgDigPatternRefTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  string trigger_pattern = 3;
  oneof trigger_when_enum {
    DigitalPatternCondition1 trigger_when = 4;
    int32 trigger_when_raw = 5;
  }
  uint32 pretrigger_samples = 6;
}

message CfgDigPatternRefTrigResponse {
  int32 status = 1;
}

message CfgDigPatternStartTrigRequest {
  nidevice_grpc.Session task = 1;
  string trigger_source = 2;
  string trigger_pattern = 3;
  oneof trigger_when_enum {
    DigitalPatternCondition1 trigger_when = 4;
    int32 trigger_when_raw = 5;
  }
}

message CfgDigPatternStartTrigResponse {
  int32 status = 1;
}

message CfgHandshakingTimingRequest {
  nidevice_grpc.Session task = 1;
  oneof sample_mode_enum {
    AcquisitionType sample_mode = 2;
    int32 sample_mode_raw = 3;
  }
  uint64 samps_per_chan = 4;
}

message CfgHandshakingTimingResponse {
  int32 status = 1;
}

message CfgImplicitTimingRequest {
  nidevice_grpc.Session task = 1;
  oneof sample_mode_enum {
    AcquisitionType sample_mode = 2;
    int32 sample_mode_raw = 3;
  }
  uint64 samps_per_chan = 4;
}

message CfgImplicitTimingResponse {
  int32 status = 1;
}

message CfgInputBufferRequest {
  nidevice_grpc.Session task = 1;
  uint32 num_samps_per_chan = 2;
}

message CfgInputBufferResponse {
  int32 status = 1;
}

message CfgOutputBufferRequest {
  nidevice_grpc.Session task = 1;
  uint32 num_samps_per_chan = 2;
}

message CfgOutputBufferResponse {
  int32 status = 1;
}

message CfgPipelinedSampClkTimingRequest {
  nidevice_grpc.Session task = 1;
  string source = 2;
  double rate = 3;
  oneof active_edge_enum {
    Edge1 active_edge = 4;
    int32 active_edge_raw = 5;
  }
  oneof sample_mode_enum {
    AcquisitionType sample_mode = 6;
    int32 sample_mode_raw = 7;
  }
  uint64 samps_per_chan = 8;
}

message CfgPipelinedSampClkTimingResponse {
  int32 status = 1;
}

message CfgSampClkTimingRequest {
  nidevice_grpc.Session task = 1;
  string source = 2;
  double rate = 3;
  oneof active_edge_enum {
    Edge1 active_edge = 4;
    int32 active_edge_raw = 5;
  }
  oneof sample_mode_enum {
    AcquisitionType sample_mode = 6;
    int32 sample_mode_raw = 7;
  }
  uint64 samps_per_chan = 8;
}

message CfgSampClkTimingResponse {
  int32 status = 1;
}

message CfgTimeStartTrigRequest {
  nidevice_grpc.Session task = 1;
  google.protobuf.Timestamp when = 2;
  oneof timescale_enum {
    Timescale2 timescale = 3;
    int32 timescale_raw = 4;
  }
}

message CfgTimeStartTrigResponse {
  int32 status = 1;
}

message CfgWatchdogAOExpirStatesRequest {
  nidevice_grpc.Session task = 1;
  string channel_names = 2;
  repeated double expir_state_array = 3;
  repeated WatchdogAOOutputType output_type_array = 4;
}

message CfgWatchdogAOExpirStatesResponse {
  int32 status = 1;
}

message CfgWatchdogCOExpirStatesRequest {
  nidevice_grpc.Session task = 1;
  string channel_names = 2;
  repeated WatchdogCOExpirState expir_state_array = 3;
}

message CfgWatchdogCOExpirStatesResponse {
  int32 status = 1;
}

message CfgWatchdogDOExpirStatesRequest {
  nidevice_grpc.Session task = 1;
  string channel_names = 2;
  repeated DigitalLineState expir_state_array = 3;
}

message CfgWatchdogDOExpirStatesResponse {
  int32 status = 1;
}

message ClearTEDSRequest {
  string physical_channel = 1;
}

message ClearTEDSResponse {
  int32 status = 1;
}

message ClearTaskRequest {
  nidevice_grpc.Session task = 1;
}

message ClearTaskResponse {
  int32 status = 1;
}

message ConfigureLoggingRequest {
  nidevice_grpc.Session task = 1;
  string file_path = 2;
  oneof logging_mode_enum {
    LoggingMode logging_mode = 3;
    int32 logging_mode_raw = 4;
  }
  string group_name = 5;
  oneof operation_enum {
    LoggingOperation operation = 6;
    int32 operation_raw = 7;
  }
}

message ConfigureLoggingResponse {
  int32 status = 1;
}

message ConfigureTEDSRequest {
  string physical_channel = 1;
  string file_path = 2;
}

message ConfigureTEDSResponse {
  int32 status = 1;
}

message ConnectTermsRequest {
  string source_terminal = 1;
  string destination_terminal = 2;
  oneof signal_modifiers_enum {
    InvertPolarity signal_modifiers = 3;
    int32 signal_modifiers_raw = 4;
  }
}

message ConnectTermsResponse {
  int32 status = 1;
}

message ControlWatchdogTaskRequest {
  nidevice_grpc.Session task = 1;
  oneof action_enum {
    WatchdogControlAction action = 2;
    int32 action_raw = 3;
  }
}

message ControlWatchdogTaskResponse {
  int32 status = 1;
}

message CreateAIAccel4WireDCVoltageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    AccelUnits2 units = 8;
    int32 units_raw = 9;
  }
  double sensitivity = 10;
  oneof sensitivity_units_enum {
    AccelSensitivityUnits1 sensitivity_units = 11;
    int32 sensitivity_units_raw = 12;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 13;
    int32 voltage_excit_source_raw = 14;
  }
  double voltage_excit_val = 15;
  bool use_excit_for_scaling = 16;
  string custom_scale_name = 17;
}

message CreateAIAccel4WireDCVoltageChanResponse {
  int32 status = 1;
}

message CreateAIAccelChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    AccelUnits2 units = 8;
    int32 units_raw = 9;
  }
  double sensitivity = 10;
  oneof sensitivity_units_enum {
    AccelSensitivityUnits1 sensitivity_units = 11;
    int32 sensitivity_units_raw = 12;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 13;
    int32 current_excit_source_raw = 14;
  }
  double current_excit_val = 15;
  string custom_scale_name = 16;
}

message CreateAIAccelChanResponse {
  int32 status = 1;
}

message CreateAIAccelChargeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    AccelUnits2 units = 8;
    int32 units_raw = 9;
  }
  double sensitivity = 10;
  oneof sensitivity_units_enum {
    AccelChargeSensitivityUnits sensitivity_units = 11;
    int32 sensitivity_units_raw = 12;
  }
  string custom_scale_name = 13;
}

message CreateAIAccelChargeChanResponse {
  int32 status = 1;
}

message CreateAIBridgeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    BridgeUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  string custom_scale_name = 14;
}

message CreateAIBridgeChanResponse {
  int32 status = 1;
}

message CreateAICalculatedPowerChanRequest {
  nidevice_grpc.Session task = 1;
  string voltage_physical_channel = 2;
  string current_physical_channel = 3;
  string name_to_assign_to_channel = 4;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 5;
    int32 terminal_config_raw = 6;
  }
  double voltage_min_val = 7;
  double voltage_max_val = 8;
  double current_min_val = 9;
  double current_max_val = 10;
  oneof units_enum {
    PowerUnits units = 11;
    int32 units_raw = 12;
  }
  oneof shunt_resistor_loc_enum {
    CurrentShuntResistorLocationWithDefault shunt_resistor_loc = 13;
    int32 shunt_resistor_loc_raw = 14;
  }
  double ext_shunt_resistor_val = 15;
  string custom_scale_name = 16;
}

message CreateAICalculatedPowerChanResponse {
  int32 status = 1;
}

message CreateAIChargeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    ChargeUnits units = 8;
    int32 units_raw = 9;
  }
  string custom_scale_name = 10;
}

message CreateAIChargeChanResponse {
  int32 status = 1;
}

message CreateAICurrentChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    CurrentUnits2 units = 8;
    int32 units_raw = 9;
  }
  oneof shunt_resistor_loc_enum {
    CurrentShuntResistorLocationWithDefault shunt_resistor_loc = 10;
    int32 shunt_resistor_loc_raw = 11;
  }
  double ext_shunt_resistor_val = 12;
  string custom_scale_name = 13;
}

message CreateAICurrentChanResponse {
  int32 status = 1;
}

message CreateAICurrentRMSChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    CurrentUnits2 units = 8;
    int32 units_raw = 9;
  }
  oneof shunt_resistor_loc_enum {
    CurrentShuntResistorLocationWithDefault shunt_resistor_loc = 10;
    int32 shunt_resistor_loc_raw = 11;
  }
  double ext_shunt_resistor_val = 12;
  string custom_scale_name = 13;
}

message CreateAICurrentRMSChanResponse {
  int32 status = 1;
}

message CreateAIForceBridgePolynomialChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    ForceUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  repeated double forward_coeffs = 14;
  repeated double reverse_coeffs = 15;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 16;
    int32 electrical_units_raw = 17;
  }
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 18;
    int32 physical_units_raw = 19;
  }
  string custom_scale_name = 20;
}

message CreateAIForceBridgePolynomialChanResponse {
  int32 status = 1;
}

message CreateAIForceBridgeTableChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    ForceUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  repeated double electrical_vals = 14;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 15;
    int32 electrical_units_raw = 16;
  }
  repeated double physical_vals = 17;
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 18;
    int32 physical_units_raw = 19;
  }
  string custom_scale_name = 20;
}

message CreateAIForceBridgeTableChanResponse {
  int32 status = 1;
}

message CreateAIForceBridgeTwoPointLinChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    ForceUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  double first_electrical_val = 14;
  double second_electrical_val = 15;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 16;
    int32 electrical_units_raw = 17;
  }
  double first_physical_val = 18;
  double second_physical_val = 19;
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 20;
    int32 physical_units_raw = 21;
  }
  string custom_scale_name = 22;
}

message CreateAIForceBridgeTwoPointLinChanResponse {
  int32 status = 1;
}

message CreateAIForceIEPEChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    ForceIEPEUnits units = 8;
    int32 units_raw = 9;
  }
  double sensitivity = 10;
  oneof sensitivity_units_enum {
    ForceIEPESensorSensitivityUnits sensitivity_units = 11;
    int32 sensitivity_units_raw = 12;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 13;
    int32 current_excit_source_raw = 14;
  }
  double current_excit_val = 15;
  string custom_scale_name = 16;
}

message CreateAIForceIEPEChanResponse {
  int32 status = 1;
}

message CreateAIFreqVoltageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    FrequencyUnits units = 6;
    int32 units_raw = 7;
  }
  double threshold_level = 8;
  double hysteresis = 9;
  string custom_scale_name = 10;
}

message CreateAIFreqVoltageChanResponse {
  int32 status = 1;
}

message CreateAIMicrophoneChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  oneof units_enum {
    SoundPressureUnits1 units = 6;
    int32 units_raw = 7;
  }
  double mic_sensitivity = 8;
  double max_snd_press_level = 9;
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
  string custom_scale_name = 13;
}

message CreateAIMicrophoneChanResponse {
  int32 status = 1;
}

message CreateAIPosEddyCurrProxProbeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    LengthUnits2 units = 6;
    int32 units_raw = 7;
  }
  double sensitivity = 8;
  oneof sensitivity_units_enum {
    EddyCurrentProxProbeSensitivityUnits sensitivity_units = 9;
    int32 sensitivity_units_raw = 10;
  }
  string custom_scale_name = 11;
}

message CreateAIPosEddyCurrProxProbeChanResponse {
  int32 status = 1;
}

message CreateAIPosLVDTChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    LengthUnits2 units = 6;
    int32 units_raw = 7;
  }
  double sensitivity = 8;
  oneof sensitivity_units_enum {
    LVDTSensitivityUnits1 sensitivity_units = 9;
    int32 sensitivity_units_raw = 10;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 11;
    int32 voltage_excit_source_raw = 12;
  }
  double voltage_excit_val = 13;
  double voltage_excit_freq = 14;
  oneof ac_excit_wire_mode_enum {
    ACExcitWireMode ac_excit_wire_mode = 15;
    int32 ac_excit_wire_mode_raw = 16;
  }
  string custom_scale_name = 17;
}

message CreateAIPosLVDTChanResponse {
  int32 status = 1;
}

message CreateAIPosRVDTChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    AngleUnits1 units = 6;
    int32 units_raw = 7;
  }
  double sensitivity = 8;
  oneof sensitivity_units_enum {
    RVDTSensitivityUnits1 sensitivity_units = 9;
    int32 sensitivity_units_raw = 10;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 11;
    int32 voltage_excit_source_raw = 12;
  }
  double voltage_excit_val = 13;
  double voltage_excit_freq = 14;
  oneof ac_excit_wire_mode_enum {
    ACExcitWireMode ac_excit_wire_mode = 15;
    int32 ac_excit_wire_mode_raw = 16;
  }
  string custom_scale_name = 17;
}

message CreateAIPosRVDTChanResponse {
  int32 status = 1;
}

message CreateAIPowerChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double voltage_setpoint = 4;
  double current_setpoint = 5;
  bool output_enable = 6;
}

message CreateAIPowerChanResponse {
  int32 status = 1;
}

message CreateAIPressureBridgePolynomialChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    PressureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  repeated double forward_coeffs = 14;
  repeated double reverse_coeffs = 15;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 16;
    int32 electrical_units_raw = 17;
  }
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 18;
    int32 physical_units_raw = 19;
  }
  string custom_scale_name = 20;
}

message CreateAIPressureBridgePolynomialChanResponse {
  int32 status = 1;
}

message CreateAIPressureBridgeTableChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    PressureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  repeated double electrical_vals = 14;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 15;
    int32 electrical_units_raw = 16;
  }
  repeated double physical_vals = 17;
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 18;
    int32 physical_units_raw = 19;
  }
  string custom_scale_name = 20;
}

message CreateAIPressureBridgeTableChanResponse {
  int32 status = 1;
}

message CreateAIPressureBridgeTwoPointLinChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    PressureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  double first_electrical_val = 14;
  double second_electrical_val = 15;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 16;
    int32 electrical_units_raw = 17;
  }
  double first_physical_val = 18;
  double second_physical_val = 19;
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 20;
    int32 physical_units_raw = 21;
  }
  string custom_scale_name = 22;
}

message CreateAIPressureBridgeTwoPointLinChanResponse {
  int32 status = 1;
}

message CreateAIRTDChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof rtd_type_enum {
    RTDType1 rtd_type = 8;
    int32 rtd_type_raw = 9;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 10;
    int32 resistance_config_raw = 11;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 12;
    int32 current_excit_source_raw = 13;
  }
  double current_excit_val = 14;
  double r0 = 15;
}

message CreateAIRTDChanResponse {
  int32 status = 1;
}

message CreateAIResistanceChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    ResistanceUnits2 units = 6;
    int32 units_raw = 7;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 8;
    int32 resistance_config_raw = 9;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
  string custom_scale_name = 13;
}

message CreateAIResistanceChanResponse {
  int32 status = 1;
}

message CreateAIRosetteStrainGageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof rosette_type_enum {
    StrainGageRosetteType rosette_type = 6;
    int32 rosette_type_raw = 7;
  }
  double gage_orientation = 8;
  repeated StrainGageRosetteMeasurementType rosette_meas_types = 9;
  oneof strain_config_enum {
    StrainGageBridgeType1 strain_config = 10;
    int32 strain_config_raw = 11;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 12;
    int32 voltage_excit_source_raw = 13;
  }
  double voltage_excit_val = 14;
  double gage_factor = 15;
  double nominal_gage_resistance = 16;
  double poisson_ratio = 17;
  double lead_wire_resistance = 18;
}

message CreateAIRosetteStrainGageChanResponse {
  int32 status = 1;
}

message CreateAIStrainGageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    StrainUnits1 units = 6;
    int32 units_raw = 7;
  }
  oneof strain_config_enum {
    StrainGageBridgeType1 strain_config = 8;
    int32 strain_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double gage_factor = 13;
  double initial_bridge_voltage = 14;
  double nominal_gage_resistance = 15;
  double poisson_ratio = 16;
  double lead_wire_resistance = 17;
  string custom_scale_name = 18;
}

message CreateAIStrainGageChanResponse {
  int32 status = 1;
}

message CreateAITempBuiltInSensorChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof units_enum {
    TemperatureUnits units = 4;
    int32 units_raw = 5;
  }
}

message CreateAITempBuiltInSensorChanResponse {
  int32 status = 1;
}

message CreateAIThrmcplChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof thermocouple_type_enum {
    ThermocoupleType1 thermocouple_type = 8;
    int32 thermocouple_type_raw = 9;
  }
  oneof cjc_source_enum {
    CJCSource1 cjc_source = 10;
    int32 cjc_source_raw = 11;
  }
  double cjc_val = 12;
  string cjc_channel = 13;
}

message CreateAIThrmcplChanResponse {
  int32 status = 1;
}

message CreateAIThrmstrChanIexRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 8;
    int32 resistance_config_raw = 9;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
  double a = 13;
  double b = 14;
  double c = 15;
}

message CreateAIThrmstrChanIexResponse {
  int32 status = 1;
}

message CreateAIThrmstrChanVexRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 8;
    int32 resistance_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double a = 13;
  double b = 14;
  double c = 15;
  double r1 = 16;
}

message CreateAIThrmstrChanVexResponse {
  int32 status = 1;
}

message CreateAITorqueBridgePolynomialChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TorqueUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  repeated double forward_coeffs = 14;
  repeated double reverse_coeffs = 15;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 16;
    int32 electrical_units_raw = 17;
  }
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 18;
    int32 physical_units_raw = 19;
  }
  string custom_scale_name = 20;
}

message CreateAITorqueBridgePolynomialChanResponse {
  int32 status = 1;
}

message CreateAITorqueBridgeTableChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TorqueUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  repeated double electrical_vals = 14;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 15;
    int32 electrical_units_raw = 16;
  }
  repeated double physical_vals = 17;
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 18;
    int32 physical_units_raw = 19;
  }
  string custom_scale_name = 20;
}

message CreateAITorqueBridgeTableChanResponse {
  int32 status = 1;
}

message CreateAITorqueBridgeTwoPointLinChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TorqueUnits units = 6;
    int32 units_raw = 7;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 8;
    int32 bridge_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double nominal_bridge_resistance = 13;
  double first_electrical_val = 14;
  double second_electrical_val = 15;
  oneof electrical_units_enum {
    BridgeElectricalUnits electrical_units = 16;
    int32 electrical_units_raw = 17;
  }
  double first_physical_val = 18;
  double second_physical_val = 19;
  oneof physical_units_enum {
    BridgePhysicalUnits physical_units = 20;
    int32 physical_units_raw = 21;
  }
  string custom_scale_name = 22;
}

message CreateAITorqueBridgeTwoPointLinChanResponse {
  int32 status = 1;
}

message CreateAIVelocityIEPEChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    VelocityUnits units = 8;
    int32 units_raw = 9;
  }
  double sensitivity = 10;
  oneof sensitivity_units_enum {
    VelocityIEPESensorSensitivityUnits sensitivity_units = 11;
    int32 sensitivity_units_raw = 12;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 13;
    int32 current_excit_source_raw = 14;
  }
  double current_excit_val = 15;
  string custom_scale_name = 16;
}

message CreateAIVelocityIEPEChanResponse {
  int32 status = 1;
}

message CreateAIVoltageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    VoltageUnits2 units = 8;
    int32 units_raw = 9;
  }
  string custom_scale_name = 10;
}

message CreateAIVoltageChanResponse {
  int32 status = 1;
}

message CreateAIVoltageChanWithExcitRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    VoltageUnits2 units = 8;
    int32 units_raw = 9;
  }
  oneof bridge_config_enum {
    BridgeConfiguration1 bridge_config = 10;
    int32 bridge_config_raw = 11;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 12;
    int32 voltage_excit_source_raw = 13;
  }
  double voltage_excit_val = 14;
  bool use_excit_for_scaling = 15;
  string custom_scale_name = 16;
}

message CreateAIVoltageChanWithExcitResponse {
  int32 status = 1;
}

message CreateAIVoltageRMSChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    VoltageUnits2 units = 8;
    int32 units_raw = 9;
  }
  string custom_scale_name = 10;
}

message CreateAIVoltageRMSChanResponse {
  int32 status = 1;
}

message CreateAOCurrentChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    CurrentUnits2 units = 6;
    int32 units_raw = 7;
  }
  string custom_scale_name = 8;
}

message CreateAOCurrentChanResponse {
  int32 status = 1;
}

message CreateAOFuncGenChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof type_enum {
    FuncGenType type = 4;
    int32 type_raw = 5;
  }
  double freq = 6;
  double amplitude = 7;
  double offset = 8;
}

message CreateAOFuncGenChanResponse {
  int32 status = 1;
}

message CreateAOVoltageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    VoltageUnits2 units = 6;
    int32 units_raw = 7;
  }
  string custom_scale_name = 8;
}

message CreateAOVoltageChanResponse {
  int32 status = 1;
}

message CreateCIAngEncoderChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  oneof decoding_type_enum {
    EncoderType2 decoding_type = 4;
    int32 decoding_type_raw = 5;
  }
  bool zidx_enable = 6;
  double zidx_val = 7;
  oneof zidx_phase_enum {
    EncoderZIndexPhase1 zidx_phase = 8;
    int32 zidx_phase_raw = 9;
  }
  oneof units_enum {
    AngleUnits2 units = 10;
    int32 units_raw = 11;
  }
  uint32 pulses_per_rev = 12;
  double initial_angle = 13;
  string custom_scale_name = 14;
}

message CreateCIAngEncoderChanResponse {
  int32 status = 1;
}

message CreateCIAngVelocityChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof decoding_type_enum {
    EncoderType2 decoding_type = 6;
    int32 decoding_type_raw = 7;
  }
  oneof units_enum {
    AngularVelocityUnits units = 8;
    int32 units_raw = 9;
  }
  uint32 pulses_per_rev = 10;
  string custom_scale_name = 11;
}

message CreateCIAngVelocityChanResponse {
  int32 status = 1;
}

message CreateCICountEdgesChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  oneof edge_enum {
    Edge1 edge = 4;
    int32 edge_raw = 5;
  }
  uint32 initial_count = 6;
  oneof count_direction_enum {
    CountDirection1 count_direction = 7;
    int32 count_direction_raw = 8;
  }
}

message CreateCICountEdgesChanResponse {
  int32 status = 1;
}

message CreateCIDutyCycleChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_freq = 4;
  double max_freq = 5;
  oneof edge_enum {
    Edge1 edge = 6;
    int32 edge_raw = 7;
  }
  string custom_scale_name = 8;
}

message CreateCIDutyCycleChanResponse {
  int32 status = 1;
}

message CreateCIFreqChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    FrequencyUnits3 units = 6;
    int32 units_raw = 7;
  }
  oneof edge_enum {
    Edge1 edge = 8;
    int32 edge_raw = 9;
  }
  oneof meas_method_enum {
    CounterFrequencyMethod meas_method = 10;
    int32 meas_method_raw = 11;
  }
  double meas_time = 12;
  uint32 divisor = 13;
  string custom_scale_name = 14;
}

message CreateCIFreqChanResponse {
  int32 status = 1;
}

message CreateCIGPSTimestampChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  oneof units_enum {
    TimeUnits units = 4;
    int32 units_raw = 5;
  }
  oneof sync_method_enum {
    GpsSignalType1 sync_method = 6;
    int32 sync_method_raw = 7;
  }
  string custom_scale_name = 8;
}

message CreateCIGPSTimestampChanResponse {
  int32 status = 1;
}

message CreateCILinEncoderChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  oneof decoding_type_enum {
    EncoderType2 decoding_type = 4;
    int32 decoding_type_raw = 5;
  }
  bool zidx_enable = 6;
  double zidx_val = 7;
  oneof zidx_phase_enum {
    EncoderZIndexPhase1 zidx_phase = 8;
    int32 zidx_phase_raw = 9;
  }
  oneof units_enum {
    LengthUnits3 units = 10;
    int32 units_raw = 11;
  }
  double dist_per_pulse = 12;
  double initial_pos = 13;
  string custom_scale_name = 14;
}

message CreateCILinEncoderChanResponse {
  int32 status = 1;
}

message CreateCILinVelocityChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof decoding_type_enum {
    EncoderType2 decoding_type = 6;
    int32 decoding_type_raw = 7;
  }
  oneof units_enum {
    VelocityUnits units = 8;
    int32 units_raw = 9;
  }
  double dist_per_pulse = 10;
  string custom_scale_name = 11;
}

message CreateCILinVelocityChanResponse {
  int32 status = 1;
}

message CreateCIPeriodChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TimeUnits3 units = 6;
    int32 units_raw = 7;
  }
  oneof edge_enum {
    Edge1 edge = 8;
    int32 edge_raw = 9;
  }
  oneof meas_method_enum {
    CounterFrequencyMethod meas_method = 10;
    int32 meas_method_raw = 11;
  }
  double meas_time = 12;
  uint32 divisor = 13;
  string custom_scale_name = 14;
}

message CreateCIPeriodChanResponse {
  int32 status = 1;
}

message CreateCIPulseChanFreqRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    FrequencyUnits2 units = 6;
    int32 units_raw = 7;
  }
}

message CreateCIPulseChanFreqResponse {
  int32 status = 1;
}

message CreateCIPulseChanTicksRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  string source_terminal = 4;
  double min_val = 5;
  double max_val = 6;
}

message CreateCIPulseChanTicksResponse {
  int32 status = 1;
}

message CreateCIPulseChanTimeRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    DigitalWidthUnits3 units = 6;
    int32 units_raw = 7;
  }
}

message CreateCIPulseChanTimeResponse {
  int32 status = 1;
}

message CreateCIPulseWidthChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TimeUnits3 units = 6;
    int32 units_raw = 7;
  }
  oneof starting_edge_enum {
    Edge1 starting_edge = 8;
    int32 starting_edge_raw = 9;
  }
  string custom_scale_name = 10;
}

message CreateCIPulseWidthChanResponse {
  int32 status = 1;
}

message CreateCISemiPeriodChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TimeUnits3 units = 6;
    int32 units_raw = 7;
  }
  string custom_scale_name = 8;
}

message CreateCISemiPeriodChanResponse {
  int32 status = 1;
}

message CreateCITwoEdgeSepChanRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TimeUnits3 units = 6;
    int32 units_raw = 7;
  }
  oneof first_edge_enum {
    Edge1 first_edge = 8;
    int32 first_edge_raw = 9;
  }
  oneof second_edge_enum {
    Edge1 second_edge = 10;
    int32 second_edge_raw = 11;
  }
  string custom_scale_name = 12;
}

message CreateCITwoEdgeSepChanResponse {
  int32 status = 1;
}

message CreateCOPulseChanFreqRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  oneof units_enum {
    FrequencyUnits2 units = 4;
    int32 units_raw = 5;
  }
  oneof idle_state_enum {
    Level1 idle_state = 6;
    int32 idle_state_raw = 7;
  }
  double initial_delay = 8;
  double freq = 9;
  double duty_cycle = 10;
}

message CreateCOPulseChanFreqResponse {
  int32 status = 1;
}

message CreateCOPulseChanTicksRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  string source_terminal = 4;
  oneof idle_state_enum {
    Level1 idle_state = 5;
    int32 idle_state_raw = 6;
  }
  int32 initial_delay = 7;
  int32 low_ticks = 8;
  int32 high_ticks = 9;
}

message CreateCOPulseChanTicksResponse {
  int32 status = 1;
}

message CreateCOPulseChanTimeRequest {
  nidevice_grpc.Session task = 1;
  string counter = 2;
  string name_to_assign_to_channel = 3;
  oneof units_enum {
    DigitalWidthUnits3 units = 4;
    int32 units_raw = 5;
  }
  oneof idle_state_enum {
    Level1 idle_state = 6;
    int32 idle_state_raw = 7;
  }
  double initial_delay = 8;
  double low_time = 9;
  double high_time = 10;
}

message CreateCOPulseChanTimeResponse {
  int32 status = 1;
}

message CreateDIChanRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  string name_to_assign_to_lines = 3;
  oneof line_grouping_enum {
    LineGrouping line_grouping = 4;
    int32 line_grouping_raw = 5;
  }
}

message CreateDIChanResponse {
  int32 status = 1;
}

message CreateDOChanRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  string name_to_assign_to_lines = 3;
  oneof line_grouping_enum {
    LineGrouping line_grouping = 4;
    int32 line_grouping_raw = 5;
  }
}

message CreateDOChanResponse {
  int32 status = 1;
}

message CreateLinScaleRequest {
  string name = 1;
  double slope = 2;
  double y_intercept = 3;
  oneof pre_scaled_units_enum {
    UnitsPreScaled pre_scaled_units = 4;
    int32 pre_scaled_units_raw = 5;
  }
  string scaled_units = 6;
}

message CreateLinScaleResponse {
  int32 status = 1;
}

message CreateMapScaleRequest {
  string name = 1;
  double prescaled_min = 2;
  double prescaled_max = 3;
  double scaled_min = 4;
  double scaled_max = 5;
  oneof pre_scaled_units_enum {
    UnitsPreScaled pre_scaled_units = 6;
    int32 pre_scaled_units_raw = 7;
  }
  string scaled_units = 8;
}

message CreateMapScaleResponse {
  int32 status = 1;
}

message CreatePolynomialScaleRequest {
  string name = 1;
  repeated double forward_coeffs = 2;
  repeated double reverse_coeffs = 3;
  oneof pre_scaled_units_enum {
    UnitsPreScaled pre_scaled_units = 4;
    int32 pre_scaled_units_raw = 5;
  }
  string scaled_units = 6;
}

message CreatePolynomialScaleResponse {
  int32 status = 1;
}

message CreateTEDSAIAccelChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    AccelUnits2 units = 8;
    int32 units_raw = 9;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
  string custom_scale_name = 13;
}

message CreateTEDSAIAccelChanResponse {
  int32 status = 1;
}

message CreateTEDSAIBridgeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TEDSUnits units = 6;
    int32 units_raw = 7;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 8;
    int32 voltage_excit_source_raw = 9;
  }
  double voltage_excit_val = 10;
  string custom_scale_name = 11;
}

message CreateTEDSAIBridgeChanResponse {
  int32 status = 1;
}

message CreateTEDSAICurrentChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    TEDSUnits units = 8;
    int32 units_raw = 9;
  }
  oneof shunt_resistor_loc_enum {
    CurrentShuntResistorLocationWithDefault shunt_resistor_loc = 10;
    int32 shunt_resistor_loc_raw = 11;
  }
  double ext_shunt_resistor_val = 12;
  string custom_scale_name = 13;
}

message CreateTEDSAICurrentChanResponse {
  int32 status = 1;
}

message CreateTEDSAIForceBridgeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    ForceUnits units = 6;
    int32 units_raw = 7;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 8;
    int32 voltage_excit_source_raw = 9;
  }
  double voltage_excit_val = 10;
  string custom_scale_name = 11;
}

message CreateTEDSAIForceBridgeChanResponse {
  int32 status = 1;
}

message CreateTEDSAIForceIEPEChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    ForceIEPEUnits units = 8;
    int32 units_raw = 9;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
  string custom_scale_name = 13;
}

message CreateTEDSAIForceIEPEChanResponse {
  int32 status = 1;
}

message CreateTEDSAIMicrophoneChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  oneof units_enum {
    SoundPressureUnits1 units = 6;
    int32 units_raw = 7;
  }
  double max_snd_press_level = 8;
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 9;
    int32 current_excit_source_raw = 10;
  }
  double current_excit_val = 11;
  string custom_scale_name = 12;
}

message CreateTEDSAIMicrophoneChanResponse {
  int32 status = 1;
}

message CreateTEDSAIPosLVDTChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    LengthUnits2 units = 6;
    int32 units_raw = 7;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 8;
    int32 voltage_excit_source_raw = 9;
  }
  double voltage_excit_val = 10;
  double voltage_excit_freq = 11;
  oneof ac_excit_wire_mode_enum {
    ACExcitWireMode ac_excit_wire_mode = 12;
    int32 ac_excit_wire_mode_raw = 13;
  }
  string custom_scale_name = 14;
}

message CreateTEDSAIPosLVDTChanResponse {
  int32 status = 1;
}

message CreateTEDSAIPosRVDTChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    AngleUnits1 units = 6;
    int32 units_raw = 7;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 8;
    int32 voltage_excit_source_raw = 9;
  }
  double voltage_excit_val = 10;
  double voltage_excit_freq = 11;
  oneof ac_excit_wire_mode_enum {
    ACExcitWireMode ac_excit_wire_mode = 12;
    int32 ac_excit_wire_mode_raw = 13;
  }
  string custom_scale_name = 14;
}

message CreateTEDSAIPosRVDTChanResponse {
  int32 status = 1;
}

message CreateTEDSAIPressureBridgeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    PressureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 8;
    int32 voltage_excit_source_raw = 9;
  }
  double voltage_excit_val = 10;
  string custom_scale_name = 11;
}

message CreateTEDSAIPressureBridgeChanResponse {
  int32 status = 1;
}

message CreateTEDSAIRTDChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 8;
    int32 resistance_config_raw = 9;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
}

message CreateTEDSAIRTDChanResponse {
  int32 status = 1;
}

message CreateTEDSAIResistanceChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TEDSUnits units = 6;
    int32 units_raw = 7;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 8;
    int32 resistance_config_raw = 9;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
  string custom_scale_name = 13;
}

message CreateTEDSAIResistanceChanResponse {
  int32 status = 1;
}

message CreateTEDSAIStrainGageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    StrainUnits1 units = 6;
    int32 units_raw = 7;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 8;
    int32 voltage_excit_source_raw = 9;
  }
  double voltage_excit_val = 10;
  double initial_bridge_voltage = 11;
  double lead_wire_resistance = 12;
  string custom_scale_name = 13;
}

message CreateTEDSAIStrainGageChanResponse {
  int32 status = 1;
}

message CreateTEDSAIThrmcplChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof cjc_source_enum {
    CJCSource1 cjc_source = 8;
    int32 cjc_source_raw = 9;
  }
  double cjc_val = 10;
  string cjc_channel = 11;
}

message CreateTEDSAIThrmcplChanResponse {
  int32 status = 1;
}

message CreateTEDSAIThrmstrChanIexRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 8;
    int32 resistance_config_raw = 9;
  }
  oneof current_excit_source_enum {
    ExcitationSource current_excit_source = 10;
    int32 current_excit_source_raw = 11;
  }
  double current_excit_val = 12;
}

message CreateTEDSAIThrmstrChanIexResponse {
  int32 status = 1;
}

message CreateTEDSAIThrmstrChanVexRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TemperatureUnits units = 6;
    int32 units_raw = 7;
  }
  oneof resistance_config_enum {
    ResistanceConfiguration resistance_config = 8;
    int32 resistance_config_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  double r1 = 13;
}

message CreateTEDSAIThrmstrChanVexResponse {
  int32 status = 1;
}

message CreateTEDSAITorqueBridgeChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  double min_val = 4;
  double max_val = 5;
  oneof units_enum {
    TorqueUnits units = 6;
    int32 units_raw = 7;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 8;
    int32 voltage_excit_source_raw = 9;
  }
  double voltage_excit_val = 10;
  string custom_scale_name = 11;
}

message CreateTEDSAITorqueBridgeChanResponse {
  int32 status = 1;
}

message CreateTEDSAIVoltageChanRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    TEDSUnits units = 8;
    int32 units_raw = 9;
  }
  string custom_scale_name = 10;
}

message CreateTEDSAIVoltageChanResponse {
  int32 status = 1;
}

message CreateTEDSAIVoltageChanWithExcitRequest {
  nidevice_grpc.Session task = 1;
  string physical_channel = 2;
  string name_to_assign_to_channel = 3;
  oneof terminal_config_enum {
    InputTermCfgWithDefault terminal_config = 4;
    int32 terminal_config_raw = 5;
  }
  double min_val = 6;
  double max_val = 7;
  oneof units_enum {
    TEDSUnits units = 8;
    int32 units_raw = 9;
  }
  oneof voltage_excit_source_enum {
    ExcitationSource voltage_excit_source = 10;
    int32 voltage_excit_source_raw = 11;
  }
  double voltage_excit_val = 12;
  string custom_scale_name = 13;
}

message CreateTEDSAIVoltageChanWithExcitResponse {
  int32 status = 1;
}

message CreateTableScaleRequest {
  string name = 1;
  repeated double prescaled_vals = 2;
  repeated double scaled_vals = 3;
  oneof pre_scaled_units_enum {
    UnitsPreScaled pre_scaled_units = 4;
    int32 pre_scaled_units_raw = 5;
  }
  string scaled_units = 6;
}

message CreateTableScaleResponse {
  int32 status = 1;
}

message CreateTaskRequest {
  string session_name = 1;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 2;
}

message CreateTaskResponse {
  int32 status = 1;
  nidevice_grpc.Session task = 2;
  bool new_session_initialized = 3;
}

message CreateWatchdogTimerTaskRequest {
  string device_name = 1;
  string session_name = 2;
  double timeout = 3;
  repeated WatchdogExpChannelsAndState exp_states = 4;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 5;
}

message CreateWatchdogTimerTaskResponse {
  int32 status = 1;
  nidevice_grpc.Session task = 2;
  bool new_session_initialized = 3;
}

message CreateWatchdogTimerTaskExRequest {
  string device_name = 1;
  string session_name = 2;
  double timeout = 3;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 4;
}

message CreateWatchdogTimerTaskExResponse {
  int32 status = 1;
  nidevice_grpc.Session task = 2;
  bool new_session_initialized = 3;
}

message DeleteNetworkDeviceRequest {
  string device_name = 1;
}

message DeleteNetworkDeviceResponse {
  int32 status = 1;
}

message DeleteSavedGlobalChanRequest {
  string channel_name = 1;
}

message DeleteSavedGlobalChanResponse {
  int32 status = 1;
}

message DeleteSavedScaleRequest {
  string scale_name = 1;
}

message DeleteSavedScaleResponse {
  int32 status = 1;
}

message DeleteSavedTaskRequest {
  string task_name = 1;
}

message DeleteSavedTaskResponse {
  int32 status = 1;
}

message DeviceSupportsCalRequest {
  string device_name = 1;
}

message DeviceSupportsCalResponse {
  int32 status = 1;
  bool cal_supported = 2;
}

message DisableRefTrigRequest {
  nidevice_grpc.Session task = 1;
}

message DisableRefTrigResponse {
  int32 status = 1;
}

message DisableStartTrigRequest {
  nidevice_grpc.Session task = 1;
}

message DisableStartTrigResponse {
  int32 status = 1;
}

message DisconnectTermsRequest {
  string source_terminal = 1;
  string destination_terminal = 2;
}

message DisconnectTermsResponse {
  int32 status = 1;
}

message ExportSignalRequest {
  nidevice_grpc.Session task = 1;
  oneof signal_id_enum {
    Signal signal_id = 2;
    int32 signal_id_raw = 3;
  }
  string output_terminal = 4;
}

message ExportSignalResponse {
  int32 status = 1;
}

message GetAIChanCalCalDateRequest {
  nidevice_grpc.Session task = 1;
  string channel_name = 2;
}

message GetAIChanCalCalDateResponse {
  int32 status = 1;
  uint32 year = 2;
  uint32 month = 3;
  uint32 day = 4;
  uint32 hour = 5;
  uint32 minute = 6;
}

message GetAIChanCalExpDateRequest {
  nidevice_grpc.Session task = 1;
  string channel_name = 2;
}

message GetAIChanCalExpDateResponse {
  int32 status = 1;
  uint32 year = 2;
  uint32 month = 3;
  uint32 day = 4;
  uint32 hour = 5;
  uint32 minute = 6;
}

message GetAnalogPowerUpStatesRequest {
  string device_name = 1;
  repeated AnalogPowerUpChannelAndType channels = 2;
}

message GetAnalogPowerUpStatesResponse {
  int32 status = 1;
  repeated double power_up_states = 2;
}

message GetAnalogPowerUpStatesWithOutputTypeRequest {
  string channel_names = 1;
  uint32 array_size = 2;
}

message GetAnalogPowerUpStatesWithOutputTypeResponse {
  int32 status = 1;
  repeated double state_array = 2;
  repeated PowerUpChannelType channel_type_array = 3;
  repeated int32 channel_type_array_raw = 4;
}

message GetArmStartTrigTimestampValRequest {
  nidevice_grpc.Session task = 1;
}

message GetArmStartTrigTimestampValResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetArmStartTrigTrigWhenRequest {
  nidevice_grpc.Session task = 1;
}

message GetArmStartTrigTrigWhenResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetAutoConfiguredCDAQSyncConnectionsRequest {
}

message GetAutoConfiguredCDAQSyncConnectionsResponse {
  int32 status = 1;
  string port_list = 2;
}

message GetBufferAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    BufferUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetBufferAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetCalInfoAttributeBoolRequest {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetCalInfoAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetCalInfoAttributeDoubleRequest {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetCalInfoAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetCalInfoAttributeStringRequest {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetCalInfoAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetCalInfoAttributeUInt32Request {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetCalInfoAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetChanAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelBoolAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetChanAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetChanAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelDoubleAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetChanAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetChanAttributeDoubleArrayRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelDoubleArrayAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetChanAttributeDoubleArrayResponse {
  int32 status = 1;
  repeated double value = 2;
}

message GetChanAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetChanAttributeInt32Response {
  int32 status = 1;
  ChannelInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetChanAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelStringAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetChanAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetChanAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelUInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetChanAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetDeviceAttributeBoolRequest {
  string device_name = 1;
  oneof attribute_enum {
    DeviceBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetDeviceAttributeDoubleRequest {
  string device_name = 1;
  oneof attribute_enum {
    DeviceDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetDeviceAttributeDoubleArrayRequest {
  string device_name = 1;
  oneof attribute_enum {
    DeviceDoubleArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeDoubleArrayResponse {
  int32 status = 1;
  repeated double value = 2;
}

message GetDeviceAttributeInt32Request {
  string device_name = 1;
  oneof attribute_enum {
    DeviceInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeInt32Response {
  int32 status = 1;
  DeviceInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetDeviceAttributeInt32ArrayRequest {
  string device_name = 1;
  oneof attribute_enum {
    DeviceInt32ArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeInt32ArrayResponse {
  int32 status = 1;
  repeated DeviceInt32AttributeValues value = 2;
  repeated int32 value_raw = 3;
}

message GetDeviceAttributeStringRequest {
  string device_name = 1;
  oneof attribute_enum {
    DeviceStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetDeviceAttributeUInt32Request {
  string device_name = 1;
  oneof attribute_enum {
    DeviceUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetDeviceAttributeUInt32ArrayRequest {
  string device_name = 1;
  oneof attribute_enum {
    DeviceUInt32ArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetDeviceAttributeUInt32ArrayResponse {
  int32 status = 1;
  repeated uint32 value = 2;
}

message GetDigitalLogicFamilyPowerUpStateRequest {
  string device_name = 1;
}

message GetDigitalLogicFamilyPowerUpStateResponse {
  int32 status = 1;
  int32 logic_family = 2;
}

message GetDigitalPowerUpStatesRequest {
  string device_name = 1;
  repeated string channel_name = 2;
}

message GetDigitalPowerUpStatesResponse {
  int32 status = 1;
  repeated PowerUpStates power_up_states = 2;
}

message GetDigitalPullUpPullDownStatesRequest {
  string device_name = 1;
  repeated string channel_name = 2;
}

message GetDigitalPullUpPullDownStatesResponse {
  int32 status = 1;
  repeated ResistorState pull_up_pull_down_states = 2;
}

message GetDisconnectedCDAQSyncPortsRequest {
}

message GetDisconnectedCDAQSyncPortsResponse {
  int32 status = 1;
  string port_list = 2;
}

message GetErrorStringRequest {
  int32 error_code = 1;
}

message GetErrorStringResponse {
  int32 status = 1;
  string error_string = 2;
}

message GetExportedSignalAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetExportedSignalAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetExportedSignalAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetExportedSignalAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetExportedSignalAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetExportedSignalAttributeInt32Response {
  int32 status = 1;
  ExportSignalInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetExportedSignalAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetExportedSignalAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetExportedSignalAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetExportedSignalAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetExtCalLastDateAndTimeRequest {
  string device_name = 1;
}

message GetExtCalLastDateAndTimeResponse {
  int32 status = 1;
  uint32 year = 2;
  uint32 month = 3;
  uint32 day = 4;
  uint32 hour = 5;
  uint32 minute = 6;
}

message GetFirstSampClkWhenRequest {
  nidevice_grpc.Session task = 1;
}

message GetFirstSampClkWhenResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetFirstSampTimestampValRequest {
  nidevice_grpc.Session task = 1;
}

message GetFirstSampTimestampValResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetNthTaskChannelRequest {
  nidevice_grpc.Session task = 1;
  uint32 index = 2;
}

message GetNthTaskChannelResponse {
  int32 status = 1;
  string buffer = 2;
}

message GetNthTaskDeviceRequest {
  nidevice_grpc.Session task = 1;
  uint32 index = 2;
}

message GetNthTaskDeviceResponse {
  int32 status = 1;
  string buffer = 2;
}

message GetNthTaskReadChannelRequest {
  nidevice_grpc.Session task = 1;
  uint32 index = 2;
}

message GetNthTaskReadChannelResponse {
  int32 status = 1;
  string buffer = 2;
}

message GetPersistedChanAttributeBoolRequest {
  string channel = 1;
  oneof attribute_enum {
    PersistedChannelBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPersistedChanAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetPersistedChanAttributeStringRequest {
  string channel = 1;
  oneof attribute_enum {
    PersistedChannelStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPersistedChanAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetPersistedScaleAttributeBoolRequest {
  string scale_name = 1;
  oneof attribute_enum {
    PersistedScaleBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPersistedScaleAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetPersistedScaleAttributeStringRequest {
  string scale_name = 1;
  oneof attribute_enum {
    PersistedScaleStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPersistedScaleAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetPersistedTaskAttributeBoolRequest {
  string task_name = 1;
  oneof attribute_enum {
    PersistedTaskBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPersistedTaskAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetPersistedTaskAttributeStringRequest {
  string task_name = 1;
  oneof attribute_enum {
    PersistedTaskStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPersistedTaskAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetPhysicalChanAttributeBoolRequest {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetPhysicalChanAttributeBytesRequest {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelBytesAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeBytesResponse {
  int32 status = 1;
  bytes value = 2;
}

message GetPhysicalChanAttributeDoubleRequest {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetPhysicalChanAttributeDoubleArrayRequest {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelDoubleArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeDoubleArrayResponse {
  int32 status = 1;
  repeated double value = 2;
}

message GetPhysicalChanAttributeInt32Request {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeInt32Response {
  int32 status = 1;
  PhysicalChannelInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetPhysicalChanAttributeInt32ArrayRequest {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelInt32ArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeInt32ArrayResponse {
  int32 status = 1;
  repeated PhysicalChannelInt32AttributeValues value = 2;
  repeated int32 value_raw = 3;
}

message GetPhysicalChanAttributeStringRequest {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetPhysicalChanAttributeUInt32Request {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetPhysicalChanAttributeUInt32ArrayRequest {
  string physical_channel = 1;
  oneof attribute_enum {
    PhysicalChannelUInt32ArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetPhysicalChanAttributeUInt32ArrayResponse {
  int32 status = 1;
  repeated uint32 value = 2;
}

message GetReadAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetReadAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetReadAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetReadAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetReadAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetReadAttributeInt32Response {
  int32 status = 1;
  ReadInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetReadAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetReadAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetReadAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetReadAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetReadAttributeUInt64Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadUInt64Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetReadAttributeUInt64Response {
  int32 status = 1;
  uint64 value = 2;
}

message GetRealTimeAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    RealTimeBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetRealTimeAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetRealTimeAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    RealTimeInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetRealTimeAttributeInt32Response {
  int32 status = 1;
  RealTimeInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetRealTimeAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    RealTimeUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetRealTimeAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetRefTrigTimestampValRequest {
  nidevice_grpc.Session task = 1;
}

message GetRefTrigTimestampValResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetScaleAttributeDoubleRequest {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetScaleAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetScaleAttributeDoubleArrayRequest {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleDoubleArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetScaleAttributeDoubleArrayResponse {
  int32 status = 1;
  repeated double value = 2;
}

message GetScaleAttributeInt32Request {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetScaleAttributeInt32Response {
  int32 status = 1;
  ScaleInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetScaleAttributeStringRequest {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetScaleAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetSelfCalLastDateAndTimeRequest {
  string device_name = 1;
}

message GetSelfCalLastDateAndTimeResponse {
  int32 status = 1;
  uint32 year = 2;
  uint32 month = 3;
  uint32 day = 4;
  uint32 hour = 5;
  uint32 minute = 6;
}

message GetStartTrigTimestampValRequest {
  nidevice_grpc.Session task = 1;
}

message GetStartTrigTimestampValResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetStartTrigTrigWhenRequest {
  nidevice_grpc.Session task = 1;
}

message GetStartTrigTrigWhenResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetSyncPulseTimeWhenRequest {
  nidevice_grpc.Session task = 1;
}

message GetSyncPulseTimeWhenResponse {
  int32 status = 1;
  google.protobuf.Timestamp data = 2;
}

message GetSystemInfoAttributeStringRequest {
  oneof attribute_enum {
    SystemStringAttribute attribute = 1;
    int32 attribute_raw = 2;
  }
}

message GetSystemInfoAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetSystemInfoAttributeUInt32Request {
  oneof attribute_enum {
    SystemUInt32Attribute attribute = 1;
    int32 attribute_raw = 2;
  }
}

message GetSystemInfoAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetTaskAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TaskBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTaskAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetTaskAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TaskStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTaskAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetTaskAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TaskUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTaskAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetTimingAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTimingAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetTimingAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTimingAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetTimingAttributeExBoolRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingBoolAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetTimingAttributeExBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetTimingAttributeExDoubleRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingDoubleAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetTimingAttributeExDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetTimingAttributeExInt32Request {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetTimingAttributeExInt32Response {
  int32 status = 1;
  TimingInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetTimingAttributeExStringRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingStringAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetTimingAttributeExStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetTimingAttributeExTimestampRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingTimestampAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetTimingAttributeExTimestampResponse {
  int32 status = 1;
  google.protobuf.Timestamp value = 2;
}

message GetTimingAttributeExUInt32Request {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingUInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetTimingAttributeExUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetTimingAttributeExUInt64Request {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingUInt64Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetTimingAttributeExUInt64Response {
  int32 status = 1;
  uint64 value = 2;
}

message GetTimingAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTimingAttributeInt32Response {
  int32 status = 1;
  TimingInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetTimingAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTimingAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetTimingAttributeTimestampRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingTimestampAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTimingAttributeTimestampResponse {
  int32 status = 1;
  google.protobuf.Timestamp value = 2;
}

message GetTimingAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTimingAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetTimingAttributeUInt64Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingUInt64Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTimingAttributeUInt64Response {
  int32 status = 1;
  uint64 value = 2;
}

message GetTrigAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetTrigAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetTrigAttributeDoubleArrayRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerDoubleArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeDoubleArrayResponse {
  int32 status = 1;
  repeated double value = 2;
}

message GetTrigAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeInt32Response {
  int32 status = 1;
  TriggerInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetTrigAttributeInt32ArrayRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerInt32ArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeInt32ArrayResponse {
  int32 status = 1;
  repeated TriggerInt32AttributeValues value = 2;
  repeated int32 value_raw = 3;
}

message GetTrigAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetTrigAttributeTimestampRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerTimestampAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeTimestampResponse {
  int32 status = 1;
  google.protobuf.Timestamp value = 2;
}

message GetTrigAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetTrigAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetWatchdogAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogBoolAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetWatchdogAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetWatchdogAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogDoubleAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetWatchdogAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetWatchdogAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetWatchdogAttributeInt32Response {
  int32 status = 1;
  WatchdogInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetWatchdogAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogStringAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message GetWatchdogAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetWriteAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetWriteAttributeBoolResponse {
  int32 status = 1;
  bool value = 2;
}

message GetWriteAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetWriteAttributeDoubleResponse {
  int32 status = 1;
  double value = 2;
}

message GetWriteAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetWriteAttributeInt32Response {
  int32 status = 1;
  WriteInt32AttributeValues value = 2;
  int32 value_raw = 3;
}

message GetWriteAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetWriteAttributeStringResponse {
  int32 status = 1;
  string value = 2;
}

message GetWriteAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetWriteAttributeUInt32Response {
  int32 status = 1;
  uint32 value = 2;
}

message GetWriteAttributeUInt64Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteUInt64Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message GetWriteAttributeUInt64Response {
  int32 status = 1;
  uint64 value = 2;
}

message IsTaskDoneRequest {
  nidevice_grpc.Session task = 1;
}

message IsTaskDoneResponse {
  int32 status = 1;
  bool is_task_done = 2;
}

message LoadTaskRequest {
  string session_name = 1;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 2;
}

message LoadTaskResponse {
  int32 status = 1;
  nidevice_grpc.Session task = 2;
  bool new_session_initialized = 3;
}

message PerformBridgeOffsetNullingCalExRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  bool skip_unsupported_channels = 3;
}

message PerformBridgeOffsetNullingCalExResponse {
  int32 status = 1;
}

message PerformBridgeShuntCalExRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  double shunt_resistor_value = 3;
  oneof shunt_resistor_location_enum {
    ShuntElementLocation shunt_resistor_location = 4;
    int32 shunt_resistor_location_raw = 5;
  }
  oneof shunt_resistor_select_enum {
    ShuntCalSelect shunt_resistor_select = 6;
    int32 shunt_resistor_select_raw = 7;
  }
  oneof shunt_resistor_source_enum {
    ShuntCalSource shunt_resistor_source = 8;
    int32 shunt_resistor_source_raw = 9;
  }
  double bridge_resistance = 10;
  bool skip_unsupported_channels = 11;
}

message PerformBridgeShuntCalExResponse {
  int32 status = 1;
}

message PerformStrainShuntCalExRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  double shunt_resistor_value = 3;
  oneof shunt_resistor_location_enum {
    ShuntElementLocation shunt_resistor_location = 4;
    int32 shunt_resistor_location_raw = 5;
  }
  oneof shunt_resistor_select_enum {
    ShuntCalSelect shunt_resistor_select = 6;
    int32 shunt_resistor_select_raw = 7;
  }
  oneof shunt_resistor_source_enum {
    ShuntCalSource shunt_resistor_source = 8;
    int32 shunt_resistor_source_raw = 9;
  }
  bool skip_unsupported_channels = 10;
}

message PerformStrainShuntCalExResponse {
  int32 status = 1;
}

message PerformThrmcplLeadOffsetNullingCalRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  bool skip_unsupported_channels = 3;
}

message PerformThrmcplLeadOffsetNullingCalResponse {
  int32 status = 1;
}

message ReadAnalogF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadAnalogF64Response {
  int32 status = 1;
  repeated double read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadAnalogF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadAnalogF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadAnalogF64Response {
  int32 status = 1;
  repeated double read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadAnalogScalarF64Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadAnalogScalarF64Response {
  int32 status = 1;
  double value = 2;
}

message BeginReadAnalogScalarF64Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadAnalogScalarF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadAnalogScalarF64Response {
  int32 status = 1;
  double value = 2;
}

message ReadBinaryI16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadBinaryI16Response {
  int32 status = 1;
  repeated int32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadBinaryI16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadBinaryI16Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadBinaryI16Response {
  int32 status = 1;
  repeated int32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadBinaryI32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadBinaryI32Response {
  int32 status = 1;
  repeated int32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadBinaryI32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadBinaryI32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadBinaryI32Response {
  int32 status = 1;
  repeated int32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadBinaryU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadBinaryU16Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadBinaryU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadBinaryU16Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadBinaryU16Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadBinaryU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadBinaryU32Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadBinaryU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadBinaryU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadBinaryU32Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadCounterF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  uint32 array_size_in_samps = 4;
}

message ReadCounterF64Response {
  int32 status = 1;
  repeated double read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadCounterF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  uint32 array_size_in_samps = 4;
}

message BeginReadCounterF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCounterF64Response {
  int32 status = 1;
  repeated double read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadCounterF64ExRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadCounterF64ExResponse {
  int32 status = 1;
  repeated double read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadCounterF64ExRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadCounterF64ExResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCounterF64ExResponse {
  int32 status = 1;
  repeated double read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadCounterScalarF64Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadCounterScalarF64Response {
  int32 status = 1;
  double value = 2;
}

message BeginReadCounterScalarF64Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadCounterScalarF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCounterScalarF64Response {
  int32 status = 1;
  double value = 2;
}

message ReadCounterScalarU32Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadCounterScalarU32Response {
  int32 status = 1;
  uint32 value = 2;
}

message BeginReadCounterScalarU32Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadCounterScalarU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCounterScalarU32Response {
  int32 status = 1;
  uint32 value = 2;
}

message ReadCounterU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  uint32 array_size_in_samps = 4;
}

message ReadCounterU32Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadCounterU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  uint32 array_size_in_samps = 4;
}

message BeginReadCounterU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCounterU32Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadCounterU32ExRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadCounterU32ExResponse {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadCounterU32ExRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadCounterU32ExResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCounterU32ExResponse {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadCtrFreqRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof interleaved_enum {
    GroupBy interleaved = 4;
    int32 interleaved_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadCtrFreqResponse {
  int32 status = 1;
  repeated double read_array_frequency = 2;
  repeated double read_array_duty_cycle = 3;
  int32 samps_per_chan_read = 4;
}

message BeginReadCtrFreqRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof interleaved_enum {
    GroupBy interleaved = 4;
    int32 interleaved_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadCtrFreqResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCtrFreqResponse {
  int32 status = 1;
  repeated double read_array_frequency = 2;
  repeated double read_array_duty_cycle = 3;
  int32 samps_per_chan_read = 4;
}

message ReadCtrFreqScalarRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadCtrFreqScalarResponse {
  int32 status = 1;
  double frequency = 2;
  double duty_cycle = 3;
}

message BeginReadCtrFreqScalarRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadCtrFreqScalarResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCtrFreqScalarResponse {
  int32 status = 1;
  double frequency = 2;
  double duty_cycle = 3;
}

message ReadCtrTicksRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof interleaved_enum {
    GroupBy interleaved = 4;
    int32 interleaved_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadCtrTicksResponse {
  int32 status = 1;
  repeated uint32 read_array_high_ticks = 2;
  repeated uint32 read_array_low_ticks = 3;
  int32 samps_per_chan_read = 4;
}

message BeginReadCtrTicksRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof interleaved_enum {
    GroupBy interleaved = 4;
    int32 interleaved_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadCtrTicksResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCtrTicksResponse {
  int32 status = 1;
  repeated uint32 read_array_high_ticks = 2;
  repeated uint32 read_array_low_ticks = 3;
  int32 samps_per_chan_read = 4;
}

message ReadCtrTicksScalarRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadCtrTicksScalarResponse {
  int32 status = 1;
  uint32 high_ticks = 2;
  uint32 low_ticks = 3;
}

message BeginReadCtrTicksScalarRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadCtrTicksScalarResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCtrTicksScalarResponse {
  int32 status = 1;
  uint32 high_ticks = 2;
  uint32 low_ticks = 3;
}

message ReadCtrTimeRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof interleaved_enum {
    GroupBy interleaved = 4;
    int32 interleaved_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadCtrTimeResponse {
  int32 status = 1;
  repeated double read_array_high_time = 2;
  repeated double read_array_low_time = 3;
  int32 samps_per_chan_read = 4;
}

message BeginReadCtrTimeRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof interleaved_enum {
    GroupBy interleaved = 4;
    int32 interleaved_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadCtrTimeResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCtrTimeResponse {
  int32 status = 1;
  repeated double read_array_high_time = 2;
  repeated double read_array_low_time = 3;
  int32 samps_per_chan_read = 4;
}

message ReadCtrTimeScalarRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadCtrTimeScalarResponse {
  int32 status = 1;
  double high_time = 2;
  double low_time = 3;
}

message BeginReadCtrTimeScalarRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadCtrTimeScalarResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadCtrTimeScalarResponse {
  int32 status = 1;
  double high_time = 2;
  double low_time = 3;
}

message ReadDigitalLinesRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_bytes = 6;
}

message ReadDigitalLinesResponse {
  int32 status = 1;
  bytes read_array = 2;
  int32 samps_per_chan_read = 3;
  int32 num_bytes_per_samp = 4;
}

message BeginReadDigitalLinesRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_bytes = 6;
}

message BeginReadDigitalLinesResponse {
  int32 status = 1;
  int32 num_bytes_per_samp = 2;
  ni.data_monikers.Moniker moniker = 3;
}

message MonikerReadDigitalLinesResponse {
  int32 status = 1;
  bytes read_array = 2;
  int32 samps_per_chan_read = 3;
  int32 num_bytes_per_samp = 4;
}

message ReadDigitalScalarU32Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadDigitalScalarU32Response {
  int32 status = 1;
  uint32 value = 2;
}

message BeginReadDigitalScalarU32Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadDigitalScalarU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadDigitalScalarU32Response {
  int32 status = 1;
  uint32 value = 2;
}

message ReadDigitalU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadDigitalU16Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadDigitalU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadDigitalU16Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadDigitalU16Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadDigitalU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadDigitalU32Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadDigitalU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadDigitalU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadDigitalU32Response {
  int32 status = 1;
  repeated uint32 read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadDigitalU8Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadDigitalU8Response {
  int32 status = 1;
  bytes read_array = 2;
  int32 samps_per_chan_read = 3;
}

message BeginReadDigitalU8Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadDigitalU8Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadDigitalU8Response {
  int32 status = 1;
  bytes read_array = 2;
  int32 samps_per_chan_read = 3;
}

message ReadIDPinMemoryRequest {
  string device_name = 1;
  string id_pin_name = 2;
  uint32 array_size = 3;
}

message ReadIDPinMemoryResponse {
  int32 status = 1;
  bytes data = 2;
  uint32 data_length_read = 3;
  uint32 format_code = 4;
}

message ReadPowerBinaryI16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadPowerBinaryI16Response {
  int32 status = 1;
  repeated int32 read_array_voltage = 2;
  repeated int32 read_array_current = 3;
  int32 samps_per_chan_read = 4;
}

message BeginReadPowerBinaryI16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadPowerBinaryI16Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadPowerBinaryI16Response {
  int32 status = 1;
  repeated int32 read_array_voltage = 2;
  repeated int32 read_array_current = 3;
  int32 samps_per_chan_read = 4;
}

message ReadPowerF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message ReadPowerF64Response {
  int32 status = 1;
  repeated double read_array_voltage = 2;
  repeated double read_array_current = 3;
  int32 samps_per_chan_read = 4;
}

message BeginReadPowerF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof fill_mode_enum {
    GroupBy fill_mode = 4;
    int32 fill_mode_raw = 5;
  }
  uint32 array_size_in_samps = 6;
}

message BeginReadPowerF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadPowerF64Response {
  int32 status = 1;
  repeated double read_array_voltage = 2;
  repeated double read_array_current = 3;
  int32 samps_per_chan_read = 4;
}

message ReadPowerScalarF64Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message ReadPowerScalarF64Response {
  int32 status = 1;
  double voltage = 2;
  double current = 3;
}

message BeginReadPowerScalarF64Request {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginReadPowerScalarF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadPowerScalarF64Response {
  int32 status = 1;
  double voltage = 2;
  double current = 3;
}

message ReadRawRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  uint32 array_size_in_bytes = 4;
}

message ReadRawResponse {
  int32 status = 1;
  bytes read_array = 2;
  int32 samps_read = 3;
  int32 num_bytes_per_samp = 4;
}

message BeginReadRawRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  uint32 array_size_in_bytes = 4;
}

message BeginReadRawResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerReadRawResponse {
  int32 status = 1;
  bytes read_array = 2;
  int32 samps_read = 3;
  int32 num_bytes_per_samp = 4;
}

message RegisterDoneEventRequest {
  nidevice_grpc.Session task = 1;
}

message RegisterDoneEventResponse {
  int32 status = 1;
}

message RegisterEveryNSamplesEventRequest {
  nidevice_grpc.Session task = 1;
  oneof every_n_samples_event_type_enum {
    EveryNSamplesEventType every_n_samples_event_type = 2;
    int32 every_n_samples_event_type_raw = 3;
  }
  uint32 n_samples = 4;
}

message RegisterEveryNSamplesEventResponse {
  int32 status = 1;
  EveryNSamplesEventType every_n_samples_event_type = 2;
  int32 every_n_samples_event_type_raw = 3;
  uint32 n_samples = 4;
}

message RegisterSignalEventRequest {
  nidevice_grpc.Session task = 1;
  oneof signal_id_enum {
    Signal2 signal_id = 2;
    int32 signal_id_raw = 3;
  }
}

message RegisterSignalEventResponse {
  int32 status = 1;
  int32 signal_id = 2;
}

message RemoveCDAQSyncConnectionRequest {
  string port_list = 1;
}

message RemoveCDAQSyncConnectionResponse {
  int32 status = 1;
}

message ReserveNetworkDeviceRequest {
  string device_name = 1;
  bool override_reservation = 2;
}

message ReserveNetworkDeviceResponse {
  int32 status = 1;
}

message ResetBufferAttributeRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    BufferResetAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message ResetBufferAttributeResponse {
  int32 status = 1;
}

message ResetChanAttributeRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelResetAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message ResetChanAttributeResponse {
  int32 status = 1;
}

message ResetDeviceRequest {
  string device_name = 1;
}

message ResetDeviceResponse {
  int32 status = 1;
}

message ResetExportedSignalAttributeRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalResetAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message ResetExportedSignalAttributeResponse {
  int32 status = 1;
}

message ResetReadAttributeRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadResetAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message ResetReadAttributeResponse {
  int32 status = 1;
}

message ResetRealTimeAttributeRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    RealTimeResetAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message ResetRealTimeAttributeResponse {
  int32 status = 1;
}

message ResetTimingAttributeRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingResetAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message ResetTimingAttributeResponse {
  int32 status = 1;
}

message ResetTimingAttributeExRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingResetAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message ResetTimingAttributeExResponse {
  int32 status = 1;
}

message ResetTrigAttributeRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerResetAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message ResetTrigAttributeResponse {
  int32 status = 1;
}

message ResetWatchdogAttributeRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogResetAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
}

message ResetWatchdogAttributeResponse {
  int32 status = 1;
}

message ResetWriteAttributeRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteResetAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
}

message ResetWriteAttributeResponse {
  int32 status = 1;
}

message RestoreLastExtCalConstRequest {
  string device_name = 1;
}

message RestoreLastExtCalConstResponse {
  int32 status = 1;
}

message SaveGlobalChanRequest {
  nidevice_grpc.Session task = 1;
  string channel_name = 2;
  string save_as = 3;
  string author = 4;
  oneof options_enum {
    SaveOptions options = 5;
    uint32 options_raw = 6;
  }
}

message SaveGlobalChanResponse {
  int32 status = 1;
}

message SaveScaleRequest {
  string scale_name = 1;
  string save_as = 2;
  string author = 3;
  oneof options_enum {
    SaveOptions options = 4;
    uint32 options_raw = 5;
  }
}

message SaveScaleResponse {
  int32 status = 1;
}

message SaveTaskRequest {
  nidevice_grpc.Session task = 1;
  string save_as = 2;
  string author = 3;
  oneof options_enum {
    SaveOptions options = 4;
    uint32 options_raw = 5;
  }
}

message SaveTaskResponse {
  int32 status = 1;
}

message SelfCalRequest {
  string device_name = 1;
}

message SelfCalResponse {
  int32 status = 1;
}

message SelfTestDeviceRequest {
  string device_name = 1;
}

message SelfTestDeviceResponse {
  int32 status = 1;
}

message SetAIChanCalCalDateRequest {
  nidevice_grpc.Session task = 1;
  string channel_name = 2;
  uint32 year = 3;
  uint32 month = 4;
  uint32 day = 5;
  uint32 hour = 6;
  uint32 minute = 7;
}

message SetAIChanCalCalDateResponse {
  int32 status = 1;
}

message SetAIChanCalExpDateRequest {
  nidevice_grpc.Session task = 1;
  string channel_name = 2;
  uint32 year = 3;
  uint32 month = 4;
  uint32 day = 5;
  uint32 hour = 6;
  uint32 minute = 7;
}

message SetAIChanCalExpDateResponse {
  int32 status = 1;
}

message SetAnalogPowerUpStatesRequest {
  string device_name = 1;
  repeated AnalogPowerUpChannelsAndState power_up_states = 2;
}

message SetAnalogPowerUpStatesResponse {
  int32 status = 1;
}

message SetAnalogPowerUpStatesWithOutputTypeRequest {
  string channel_names = 1;
  repeated double state_array = 2;
  repeated PowerUpChannelType channel_type_array = 3;
}

message SetAnalogPowerUpStatesWithOutputTypeResponse {
  int32 status = 1;
}

message SetArmStartTrigTrigWhenRequest {
  nidevice_grpc.Session task = 1;
  google.protobuf.Timestamp data = 2;
}

message SetArmStartTrigTrigWhenResponse {
  int32 status = 1;
}

message SetBufferAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    BufferUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetBufferAttributeUInt32Response {
  int32 status = 1;
}

message SetCalInfoAttributeBoolRequest {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  bool value = 4;
}

message SetCalInfoAttributeBoolResponse {
  int32 status = 1;
}

message SetCalInfoAttributeDoubleRequest {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  double value = 4;
}

message SetCalInfoAttributeDoubleResponse {
  int32 status = 1;
}

message SetCalInfoAttributeStringRequest {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  string value = 4;
}

message SetCalInfoAttributeStringResponse {
  int32 status = 1;
}

message SetCalInfoAttributeUInt32Request {
  string device_name = 1;
  oneof attribute_enum {
    CalibrationInfoUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetCalInfoAttributeUInt32Response {
  int32 status = 1;
}

message SetChanAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelBoolAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  bool value = 5;
}

message SetChanAttributeBoolResponse {
  int32 status = 1;
}

message SetChanAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelDoubleAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  double value = 5;
}

message SetChanAttributeDoubleResponse {
  int32 status = 1;
}

message SetChanAttributeDoubleArrayRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelDoubleArrayAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  repeated double value = 5;
}

message SetChanAttributeDoubleArrayResponse {
  int32 status = 1;
}

message SetChanAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
  oneof value_enum {
    ChannelInt32AttributeValues value = 5;
    int32 value_raw = 6;
  }
}

message SetChanAttributeInt32Response {
  int32 status = 1;
}

message SetChanAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelStringAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  string value = 5;
}

message SetChanAttributeStringResponse {
  int32 status = 1;
}

message SetChanAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  string channel = 2;
  oneof attribute_enum {
    ChannelUInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
  uint32 value = 5;
}

message SetChanAttributeUInt32Response {
  int32 status = 1;
}

message SetDigitalLogicFamilyPowerUpStateRequest {
  string device_name = 1;
  oneof logic_family_enum {
    LogicFamily logic_family = 2;
    int32 logic_family_raw = 3;
  }
}

message SetDigitalLogicFamilyPowerUpStateResponse {
  int32 status = 1;
}

message SetDigitalPowerUpStatesRequest {
  string device_name = 1;
  repeated DigitalPowerUpChannelsAndState power_up_states = 2;
}

message SetDigitalPowerUpStatesResponse {
  int32 status = 1;
}

message SetDigitalPullUpPullDownStatesRequest {
  string device_name = 1;
  repeated DigitalPullUpPullDownChannelsAndState pull_up_pull_down_states = 2;
}

message SetDigitalPullUpPullDownStatesResponse {
  int32 status = 1;
}

message SetExportedSignalAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  bool value = 4;
}

message SetExportedSignalAttributeBoolResponse {
  int32 status = 1;
}

message SetExportedSignalAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  double value = 4;
}

message SetExportedSignalAttributeDoubleResponse {
  int32 status = 1;
}

message SetExportedSignalAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  oneof value_enum {
    ExportSignalInt32AttributeValues value = 4;
    int32 value_raw = 5;
  }
}

message SetExportedSignalAttributeInt32Response {
  int32 status = 1;
}

message SetExportedSignalAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  string value = 4;
}

message SetExportedSignalAttributeStringResponse {
  int32 status = 1;
}

message SetExportedSignalAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ExportSignalUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetExportedSignalAttributeUInt32Response {
  int32 status = 1;
}

message SetFirstSampClkWhenRequest {
  nidevice_grpc.Session task = 1;
  google.protobuf.Timestamp data = 2;
}

message SetFirstSampClkWhenResponse {
  int32 status = 1;
}

message SetReadAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  bool value = 4;
}

message SetReadAttributeBoolResponse {
  int32 status = 1;
}

message SetReadAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  double value = 4;
}

message SetReadAttributeDoubleResponse {
  int32 status = 1;
}

message SetReadAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  oneof value_enum {
    ReadInt32AttributeValues value = 4;
    int32 value_raw = 5;
  }
}

message SetReadAttributeInt32Response {
  int32 status = 1;
}

message SetReadAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  string value = 4;
}

message SetReadAttributeStringResponse {
  int32 status = 1;
}

message SetReadAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetReadAttributeUInt32Response {
  int32 status = 1;
}

message SetReadAttributeUInt64Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    ReadUInt64Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint64 value = 4;
}

message SetReadAttributeUInt64Response {
  int32 status = 1;
}

message SetRealTimeAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    RealTimeBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  bool value = 4;
}

message SetRealTimeAttributeBoolResponse {
  int32 status = 1;
}

message SetRealTimeAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    RealTimeInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  oneof value_enum {
    RealTimeInt32AttributeValues value = 4;
    int32 value_raw = 5;
  }
}

message SetRealTimeAttributeInt32Response {
  int32 status = 1;
}

message SetRealTimeAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    RealTimeUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetRealTimeAttributeUInt32Response {
  int32 status = 1;
}

message SetScaleAttributeDoubleRequest {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  double value = 4;
}

message SetScaleAttributeDoubleResponse {
  int32 status = 1;
}

message SetScaleAttributeDoubleArrayRequest {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleDoubleArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  repeated double value = 4;
}

message SetScaleAttributeDoubleArrayResponse {
  int32 status = 1;
}

message SetScaleAttributeInt32Request {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  oneof value_enum {
    ScaleInt32AttributeValues value = 4;
    int32 value_raw = 5;
  }
}

message SetScaleAttributeInt32Response {
  int32 status = 1;
}

message SetScaleAttributeStringRequest {
  string scale_name = 1;
  oneof attribute_enum {
    ScaleStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  string value = 4;
}

message SetScaleAttributeStringResponse {
  int32 status = 1;
}

message SetStartTrigTrigWhenRequest {
  nidevice_grpc.Session task = 1;
  google.protobuf.Timestamp data = 2;
}

message SetStartTrigTrigWhenResponse {
  int32 status = 1;
}

message SetSyncPulseTimeWhenRequest {
  nidevice_grpc.Session task = 1;
  google.protobuf.Timestamp data = 2;
}

message SetSyncPulseTimeWhenResponse {
  int32 status = 1;
}

message SetTimingAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  bool value = 4;
}

message SetTimingAttributeBoolResponse {
  int32 status = 1;
}

message SetTimingAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  double value = 4;
}

message SetTimingAttributeDoubleResponse {
  int32 status = 1;
}

message SetTimingAttributeExBoolRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingBoolAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  bool value = 5;
}

message SetTimingAttributeExBoolResponse {
  int32 status = 1;
}

message SetTimingAttributeExDoubleRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingDoubleAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  double value = 5;
}

message SetTimingAttributeExDoubleResponse {
  int32 status = 1;
}

message SetTimingAttributeExInt32Request {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
  oneof value_enum {
    TimingInt32AttributeValues value = 5;
    int32 value_raw = 6;
  }
}

message SetTimingAttributeExInt32Response {
  int32 status = 1;
}

message SetTimingAttributeExStringRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingStringAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  string value = 5;
}

message SetTimingAttributeExStringResponse {
  int32 status = 1;
}

message SetTimingAttributeExTimestampRequest {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingTimestampAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  google.protobuf.Timestamp value = 5;
}

message SetTimingAttributeExTimestampResponse {
  int32 status = 1;
}

message SetTimingAttributeExUInt32Request {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingUInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
  uint32 value = 5;
}

message SetTimingAttributeExUInt32Response {
  int32 status = 1;
}

message SetTimingAttributeExUInt64Request {
  nidevice_grpc.Session task = 1;
  string device_names = 2;
  oneof attribute_enum {
    TimingUInt64Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
  uint64 value = 5;
}

message SetTimingAttributeExUInt64Response {
  int32 status = 1;
}

message SetTimingAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  oneof value_enum {
    TimingInt32AttributeValues value = 4;
    int32 value_raw = 5;
  }
}

message SetTimingAttributeInt32Response {
  int32 status = 1;
}

message SetTimingAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  string value = 4;
}

message SetTimingAttributeStringResponse {
  int32 status = 1;
}

message SetTimingAttributeTimestampRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingTimestampAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  google.protobuf.Timestamp value = 4;
}

message SetTimingAttributeTimestampResponse {
  int32 status = 1;
}

message SetTimingAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetTimingAttributeUInt32Response {
  int32 status = 1;
}

message SetTimingAttributeUInt64Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TimingUInt64Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint64 value = 4;
}

message SetTimingAttributeUInt64Response {
  int32 status = 1;
}

message SetTrigAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  bool value = 4;
}

message SetTrigAttributeBoolResponse {
  int32 status = 1;
}

message SetTrigAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  double value = 4;
}

message SetTrigAttributeDoubleResponse {
  int32 status = 1;
}

message SetTrigAttributeDoubleArrayRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerDoubleArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  repeated double value = 4;
}

message SetTrigAttributeDoubleArrayResponse {
  int32 status = 1;
}

message SetTrigAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  oneof value_enum {
    TriggerInt32AttributeValues value = 4;
    int32 value_raw = 5;
  }
}

message SetTrigAttributeInt32Response {
  int32 status = 1;
}

message SetTrigAttributeInt32ArrayRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerInt32ArrayAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  repeated int32 value = 4;
}

message SetTrigAttributeInt32ArrayResponse {
  int32 status = 1;
}

message SetTrigAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  string value = 4;
}

message SetTrigAttributeStringResponse {
  int32 status = 1;
}

message SetTrigAttributeTimestampRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerTimestampAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  google.protobuf.Timestamp value = 4;
}

message SetTrigAttributeTimestampResponse {
  int32 status = 1;
}

message SetTrigAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    TriggerUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetTrigAttributeUInt32Response {
  int32 status = 1;
}

message SetWatchdogAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogBoolAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  bool value = 5;
}

message SetWatchdogAttributeBoolResponse {
  int32 status = 1;
}

message SetWatchdogAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogDoubleAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  double value = 5;
}

message SetWatchdogAttributeDoubleResponse {
  int32 status = 1;
}

message SetWatchdogAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogInt32Attribute attribute = 3;
    int32 attribute_raw = 4;
  }
  oneof value_enum {
    WatchdogInt32AttributeValues value = 5;
    int32 value_raw = 6;
  }
}

message SetWatchdogAttributeInt32Response {
  int32 status = 1;
}

message SetWatchdogAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  string lines = 2;
  oneof attribute_enum {
    WatchdogStringAttribute attribute = 3;
    int32 attribute_raw = 4;
  }
  string value = 5;
}

message SetWatchdogAttributeStringResponse {
  int32 status = 1;
}

message SetWriteAttributeBoolRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteBoolAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  bool value = 4;
}

message SetWriteAttributeBoolResponse {
  int32 status = 1;
}

message SetWriteAttributeDoubleRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteDoubleAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  double value = 4;
}

message SetWriteAttributeDoubleResponse {
  int32 status = 1;
}

message SetWriteAttributeInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  oneof value_enum {
    WriteInt32AttributeValues value = 4;
    int32 value_raw = 5;
  }
}

message SetWriteAttributeInt32Response {
  int32 status = 1;
}

message SetWriteAttributeStringRequest {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteStringAttribute attribute = 2;
    int32 attribute_raw = 3;
  }
  string value = 4;
}

message SetWriteAttributeStringResponse {
  int32 status = 1;
}

message SetWriteAttributeUInt32Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteUInt32Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint32 value = 4;
}

message SetWriteAttributeUInt32Response {
  int32 status = 1;
}

message SetWriteAttributeUInt64Request {
  nidevice_grpc.Session task = 1;
  oneof attribute_enum {
    WriteUInt64Attribute attribute = 2;
    int32 attribute_raw = 3;
  }
  uint64 value = 4;
}

message SetWriteAttributeUInt64Response {
  int32 status = 1;
}

message StartNewFileRequest {
  nidevice_grpc.Session task = 1;
  string file_path = 2;
}

message StartNewFileResponse {
  int32 status = 1;
}

message StartTaskRequest {
  nidevice_grpc.Session task = 1;
}

message StartTaskResponse {
  int32 status = 1;
}

message StopTaskRequest {
  nidevice_grpc.Session task = 1;
}

message StopTaskResponse {
  int32 status = 1;
}

message TaskControlRequest {
  nidevice_grpc.Session task = 1;
  oneof action_enum {
    TaskControlAction action = 2;
    int32 action_raw = 3;
  }
}

message TaskControlResponse {
  int32 status = 1;
}

message TristateOutputTermRequest {
  string output_terminal = 1;
}

message TristateOutputTermResponse {
  int32 status = 1;
}

message UnregisterDoneEventRequest {
  nidevice_grpc.Session task = 1;
}

message UnregisterDoneEventResponse {
  int32 status = 1;
}

message UnregisterEveryNSamplesEventRequest {
  nidevice_grpc.Session task = 1;
  oneof every_n_samples_event_type_enum {
    EveryNSamplesEventType every_n_samples_event_type = 2;
    int32 every_n_samples_event_type_raw = 3;
  }
}

message UnregisterEveryNSamplesEventResponse {
  int32 status = 1;
}

message UnregisterSignalEventRequest {
  nidevice_grpc.Session task = 1;
  oneof signal_id_enum {
    Signal2 signal_id = 2;
    int32 signal_id_raw = 3;
  }
}

message UnregisterSignalEventResponse {
  int32 status = 1;
}

message UnreserveNetworkDeviceRequest {
  string device_name = 1;
}

message UnreserveNetworkDeviceResponse {
  int32 status = 1;
}

message WaitForNextSampleClockRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message WaitForNextSampleClockResponse {
  int32 status = 1;
  bool is_late = 2;
}

message BeginWaitForNextSampleClockRequest {
  nidevice_grpc.Session task = 1;
  double timeout = 2;
}

message BeginWaitForNextSampleClockResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWaitForNextSampleClockResponse {
  int32 status = 1;
  bool is_late = 2;
}

message WaitForValidTimestampRequest {
  nidevice_grpc.Session task = 1;
  oneof timestamp_event_enum {
    TimestampEvent timestamp_event = 2;
    int32 timestamp_event_raw = 3;
  }
  double timeout = 4;
}

message WaitForValidTimestampResponse {
  int32 status = 1;
  google.protobuf.Timestamp timestamp = 2;
}

message WaitUntilTaskDoneRequest {
  nidevice_grpc.Session task = 1;
  double time_to_wait = 2;
}

message WaitUntilTaskDoneResponse {
  int32 status = 1;
}

message WriteAnalogF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated double write_array = 7;
}

message WriteAnalogF64Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteAnalogF64Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteAnalogF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteAnalogF64Request {
  repeated double write_array = 1;
}

message MonikerWriteAnalogF64Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteAnalogScalarF64Request {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
  double value = 4;
}

message WriteAnalogScalarF64Response {
  int32 status = 1;
}

message BeginWriteAnalogScalarF64Request {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
}

message BeginWriteAnalogScalarF64Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteAnalogScalarF64Request {
  double value = 1;
}

message MonikerWriteAnalogScalarF64Response {
  int32 status = 1;
}

message WriteBinaryI16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated int32 write_array = 7;
}

message WriteBinaryI16Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteBinaryI16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteBinaryI16Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteBinaryI16Request {
  repeated int32 write_array = 1;
}

message MonikerWriteBinaryI16Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteBinaryI32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated int32 write_array = 7;
}

message WriteBinaryI32Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteBinaryI32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteBinaryI32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteBinaryI32Request {
  repeated int32 write_array = 1;
}

message MonikerWriteBinaryI32Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteBinaryU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated uint32 write_array = 7;
}

message WriteBinaryU16Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteBinaryU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteBinaryU16Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteBinaryU16Request {
  repeated uint32 write_array = 1;
}

message MonikerWriteBinaryU16Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteBinaryU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated uint32 write_array = 7;
}

message WriteBinaryU32Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteBinaryU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteBinaryU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteBinaryU32Request {
  repeated uint32 write_array = 1;
}

message MonikerWriteBinaryU32Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteCtrFreqRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated double frequency = 7;
  repeated double duty_cycle = 8;
}

message WriteCtrFreqResponse {
  int32 status = 1;
  int32 num_samps_per_chan_written = 2;
}

message BeginWriteCtrFreqRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteCtrFreqResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteCtrFreqRequest {
  repeated double frequency = 1;
  repeated double duty_cycle = 2;
}

message MonikerWriteCtrFreqResponse {
  int32 status = 1;
  int32 num_samps_per_chan_written = 2;
}

message WriteCtrFreqScalarRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
  double frequency = 4;
  double duty_cycle = 5;
}

message WriteCtrFreqScalarResponse {
  int32 status = 1;
}

message BeginWriteCtrFreqScalarRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
}

message BeginWriteCtrFreqScalarResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteCtrFreqScalarRequest {
  double frequency = 1;
  double duty_cycle = 2;
}

message MonikerWriteCtrFreqScalarResponse {
  int32 status = 1;
}

message WriteCtrTicksRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated uint32 high_ticks = 7;
  repeated uint32 low_ticks = 8;
}

message WriteCtrTicksResponse {
  int32 status = 1;
  int32 num_samps_per_chan_written = 2;
}

message BeginWriteCtrTicksRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteCtrTicksResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteCtrTicksRequest {
  repeated uint32 high_ticks = 1;
  repeated uint32 low_ticks = 2;
}

message MonikerWriteCtrTicksResponse {
  int32 status = 1;
  int32 num_samps_per_chan_written = 2;
}

message WriteCtrTicksScalarRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
  uint32 high_ticks = 4;
  uint32 low_ticks = 5;
}

message WriteCtrTicksScalarResponse {
  int32 status = 1;
}

message BeginWriteCtrTicksScalarRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
}

message BeginWriteCtrTicksScalarResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteCtrTicksScalarRequest {
  uint32 high_ticks = 1;
  uint32 low_ticks = 2;
}

message MonikerWriteCtrTicksScalarResponse {
  int32 status = 1;
}

message WriteCtrTimeRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated double high_time = 7;
  repeated double low_time = 8;
}

message WriteCtrTimeResponse {
  int32 status = 1;
  int32 num_samps_per_chan_written = 2;
}

message BeginWriteCtrTimeRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteCtrTimeResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteCtrTimeRequest {
  repeated double high_time = 1;
  repeated double low_time = 2;
}

message MonikerWriteCtrTimeResponse {
  int32 status = 1;
  int32 num_samps_per_chan_written = 2;
}

message WriteCtrTimeScalarRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
  double high_time = 4;
  double low_time = 5;
}

message WriteCtrTimeScalarResponse {
  int32 status = 1;
}

message BeginWriteCtrTimeScalarRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
}

message BeginWriteCtrTimeScalarResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteCtrTimeScalarRequest {
  double high_time = 1;
  double low_time = 2;
}

message MonikerWriteCtrTimeScalarResponse {
  int32 status = 1;
}

message WriteDigitalLinesRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  bytes write_array = 7;
}

message WriteDigitalLinesResponse {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteDigitalLinesRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteDigitalLinesResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteDigitalLinesRequest {
  bytes write_array = 1;
}

message MonikerWriteDigitalLinesResponse {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteDigitalScalarU32Request {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
  uint32 value = 4;
}

message WriteDigitalScalarU32Response {
  int32 status = 1;
}

message BeginWriteDigitalScalarU32Request {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
}

message BeginWriteDigitalScalarU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteDigitalScalarU32Request {
  uint32 value = 1;
}

message MonikerWriteDigitalScalarU32Response {
  int32 status = 1;
}

message WriteDigitalU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated uint32 write_array = 7;
}

message WriteDigitalU16Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteDigitalU16Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteDigitalU16Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteDigitalU16Request {
  repeated uint32 write_array = 1;
}

message MonikerWriteDigitalU16Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteDigitalU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  repeated uint32 write_array = 7;
}

message WriteDigitalU32Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteDigitalU32Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteDigitalU32Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteDigitalU32Request {
  repeated uint32 write_array = 1;
}

message MonikerWriteDigitalU32Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteDigitalU8Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
  bytes write_array = 7;
}

message WriteDigitalU8Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteDigitalU8Request {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  bool auto_start = 3;
  double timeout = 4;
  oneof data_layout_enum {
    GroupBy data_layout = 5;
    int32 data_layout_raw = 6;
  }
}

message BeginWriteDigitalU8Response {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteDigitalU8Request {
  bytes write_array = 1;
}

message MonikerWriteDigitalU8Response {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteIDPinMemoryRequest {
  string device_name = 1;
  string id_pin_name = 2;
  bytes data = 3;
  uint32 format_code = 4;
}

message WriteIDPinMemoryResponse {
  int32 status = 1;
}

message WriteRawRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps = 2;
  bool auto_start = 3;
  double timeout = 4;
  bytes write_array = 5;
}

message WriteRawResponse {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message BeginWriteRawRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps = 2;
  bool auto_start = 3;
  double timeout = 4;
}

message BeginWriteRawResponse {
  int32 status = 1;
  ni.data_monikers.Moniker moniker = 2;
}

message MonikerWriteRawRequest {
  bytes write_array = 1;
}

message MonikerWriteRawResponse {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteToTEDSFromArrayRequest {
  string physical_channel = 1;
  bytes bit_stream = 2;
  oneof basic_teds_options_enum {
    WriteBasicTEDSOptions basic_teds_options = 3;
    int32 basic_teds_options_raw = 4;
  }
}

message WriteToTEDSFromArrayResponse {
  int32 status = 1;
}

message WriteToTEDSFromFileRequest {
  string physical_channel = 1;
  string file_path = 2;
  oneof basic_teds_options_enum {
    WriteBasicTEDSOptions basic_teds_options = 3;
    int32 basic_teds_options_raw = 4;
  }
}

message WriteToTEDSFromFileResponse {
  int32 status = 1;
}

message ReadAnalogWaveformsRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof waveform_attribute_mode_enum {
    WaveformAttributeMode waveform_attribute_mode = 4;
    int32 waveform_attribute_mode_raw = 5;
  }
}

message ReadAnalogWaveformsResponse {
  int32 status = 1;
  repeated ni.protobuf.types.DoubleAnalogWaveform waveforms = 2;
  int32 samps_per_chan_read = 3;
}

message ReadDigitalWaveformsRequest {
  nidevice_grpc.Session task = 1;
  int32 num_samps_per_chan = 2;
  double timeout = 3;
  oneof waveform_attribute_mode_enum {
    WaveformAttributeMode waveform_attribute_mode = 4;
    int32 waveform_attribute_mode_raw = 5;
  }
}

message ReadDigitalWaveformsResponse {
  int32 status = 1;
  repeated ni.protobuf.types.DigitalWaveform waveforms = 2;
  int32 samps_per_chan_read = 3;
}

message WriteAnalogWaveformsRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
  repeated ni.protobuf.types.DoubleAnalogWaveform waveforms = 4;
}

message WriteAnalogWaveformsResponse {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}

message WriteDigitalWaveformsRequest {
  nidevice_grpc.Session task = 1;
  bool auto_start = 2;
  double timeout = 3;
  repeated ni.protobuf.types.DigitalWaveform waveforms = 4;
}

message WriteDigitalWaveformsResponse {
  int32 status = 1;
  int32 samps_per_chan_written = 2;
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/stub_generator.py sha256=042606dd0f4b4c5578be9ac98e7718a30d6685826c447a3a383b25dc00f16024 bytes=3571 -->
## FILE: src/codegen/stub_generator.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/stub_generator.py`
- sha256: `042606dd0f4b4c5578be9ac98e7718a30d6685826c447a3a383b25dc00f16024`
- bytes: 3571

````python
"""Generates gRPC Python stubs from proto files."""

import os
import pathlib
from collections.abc import Sequence

import grpc_tools.protoc
import pkg_resources

STUBS_NAMESPACE = "nidaqmx._stubs"
PROTO_PARENT_NAMESPACES = ["src.codegen", "protos"]
STUBS_PATH = (
    pathlib.Path(__file__).parent.parent.parent / "generated" / STUBS_NAMESPACE.replace(".", "/")
)
PROTO_PATH = pathlib.Path(__file__).parent.parent.parent / "src" / "codegen" / "protos"
NI_APIS_PATH = pathlib.Path(__file__).parent.parent.parent / "third_party" / "ni-apis"
PROTO_FILES = list(PROTO_PATH.rglob("*.proto"))


def generate_stubs():
    """Generate and fixup gRPC Python stubs."""
    generate_python_files(STUBS_PATH, PROTO_PATH, PROTO_FILES)
    fix_import_paths(STUBS_PATH, STUBS_NAMESPACE, PROTO_PARENT_NAMESPACES)
    add_init_files(STUBS_PATH, PROTO_PATH)


def is_relative_to(path: pathlib.PurePath, other: pathlib.PurePath) -> bool:
    """Return whether or not this path is relative to the other path."""
    try:
        path.relative_to(other)
        return True
    except ValueError:
        return False


def generate_python_files(
    stubs_path: pathlib.Path, proto_path: pathlib.Path, proto_files: Sequence[pathlib.Path]
):
    """Generate python files from .proto files with protoc."""
    os.makedirs(stubs_path, exist_ok=True)
    arguments = [
        "protoc",
        f"--proto_path={str(proto_path)}",
        f"--proto_path={str(NI_APIS_PATH)}",  # ni-apis root path for ni.protobuf.types import resolution
        f"--proto_path={str(NI_APIS_PATH / 'ni' / 'grpcdevice' / 'v1')}",  # ni-apis session.proto location for import resolution
        f"--proto_path={pkg_resources.resource_filename('grpc_tools', '_proto')}",
        f"--python_out={str(stubs_path)}",
        f"--mypy_out={str(stubs_path)}",
        f"--grpc_python_out={str(stubs_path)}",
        f"--mypy_grpc_out={str(stubs_path)}",
    ]
    arguments += [str(path.relative_to(proto_path)).replace("\\", "/") for path in proto_files]

    print(proto_files)

    grpc_tools.protoc.main(arguments)


def fix_import_paths(
    stubs_path: pathlib.Path, stubs_namespace: str, proto_parent_namespaces: Sequence[str]
):
    """Fix import paths of generated files."""
    print("Fixing import paths")
    grpc_code_generated_file_paths = list(stubs_path.rglob("*pb2*py"))
    imports_to_fix = [
        path.stem for path in grpc_code_generated_file_paths if path.parent == stubs_path
    ]
    grpc_code_generated_file_paths.extend(stubs_path.rglob("*pb2*pyi"))
    for path in grpc_code_generated_file_paths:
        print(f"Processing {path}")
        data = path.read_text()
        for name in imports_to_fix:
            data = data.replace(f"import {name}", f"from {stubs_namespace} import {name}")

        for namespace in proto_parent_namespaces:
            data = data.replace(
                f"from {namespace}",
                f"from {stubs_namespace}.{namespace}",
            )
        path.write_text(data)


def add_init_files(stubs_path: pathlib.Path, proto_path: pathlib.Path):
    """Add __init__.py files to generated file directories."""
    for dir in stubs_path.rglob(""):
        if not is_relative_to(dir, proto_path) and dir.is_dir():
            python_files = list(dir.glob("*.py"))
            if python_files:
                init_path = dir / "__init__.py"
                print(f"Creating {init_path}")
                init_path.write_text('"""Auto generated gRPC files."""\n')
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/_base_interpreter.py.mako sha256=38bc949bba892993bb2251a43a21a3bd0cffca164ae7277f8577d9fd69214b67 bytes=5009 -->
## FILE: src/codegen/templates/_base_interpreter.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/_base_interpreter.py.mako`
- sha256: `38bc949bba892993bb2251a43a21a3bd0cffca164ae7277f8577d9fd69214b67`
- bytes: 5009

````mako
<%
    from codegen.utilities.interpreter_helpers import (
        get_interpreter_functions,
        get_interpreter_parameter_signature,
        get_params_for_function_signature,
        INCLUDE_SIZE_HINT_FUNCTIONS
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
    functions = get_interpreter_functions(data)
%>\
# Do not edit this file; it was automatically generated.
from __future__ import annotations

import abc
import numpy
from nitypes.waveform import AnalogWaveform, DigitalWaveform
from typing import Any

from collections.abc import Sequence
from nidaqmx.constants import WaveformAttributeMode


class BaseEventHandler(abc.ABC):
    """Interpreter-specific object that is returned from register_*_event()."""
    __slots__ = ()

    @abc.abstractmethod
    def close(self) -> None:
        """Release resources used by the event handler.

        After releasing the resources, this method may report handler-specific errors
        (e.g. gRPC stream errors) by raising an exception.
        """
        raise NotImplementedError


class BaseInterpreter(abc.ABC):
    """
    Contains signature of functions for all DAQmx APIs.
    """
    __slots__ = ()

% for func in functions:
<%
    params = get_params_for_function_signature(func)
    sorted_params = order_function_parameters_by_optional(params)
    parameter_signature = get_interpreter_parameter_signature(is_python_factory, sorted_params)
    if func.function_name in INCLUDE_SIZE_HINT_FUNCTIONS:
        parameter_signature = ", ".join([parameter_signature, "size_hint=0"])
%>\
    @abc.abstractmethod
%if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
%else:
    def ${func.function_name}(${parameter_signature}):
%endif
        raise NotImplementedError

% endfor
    @abc.abstractmethod
    def hash_task_handle(self, task_handle):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def driver_version(self):
        raise NotImplementedError

    @abc.abstractmethod
    def read_analog_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: AnalogWaveform[numpy.float64],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_analog_waveforms(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveforms: Sequence[AnalogWaveform[numpy.float64]],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: DigitalWaveform[Any],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveforms: Sequence[DigitalWaveform[Any]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def read_new_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> Sequence[DigitalWaveform[numpy.uint8]]:
        raise NotImplementedError

    @abc.abstractmethod
    def write_analog_waveform(
        self,
        task_handle: object,
        waveform: AnalogWaveform[Any],
        auto_start: bool,
        timeout: float
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def write_analog_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[AnalogWaveform[Any]],
        auto_start: bool,
        timeout: float
    ) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def write_digital_waveform(
        self,
        task_handle: object,
        waveform: DigitalWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int:
        raise NotImplementedError

    def write_digital_waveforms(
        self,
        task_handle: object,
        waveform: Sequence[DigitalWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int:
        raise NotImplementedError
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/_grpc_interpreter.py.mako sha256=34d77c5d3e62c115c08e3575183e0db928046a52e6f835ae1f645ad89ec0c0cc bytes=21037 -->
## FILE: src/codegen/templates/_grpc_interpreter.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/_grpc_interpreter.py.mako`
- sha256: `34d77c5d3e62c115c08e3575183e0db928046a52e6f835ae1f645ad89ec0c0cc`
- bytes: 21037

````mako
<%
    from codegen.utilities.interpreter_helpers import (
        get_grpc_function_call_template,
        get_interpreter_functions,
        get_interpreter_parameter_signature,
        get_output_params,
        get_params_for_function_signature,
        get_response_parameters,
        is_event_register_function,
        GRPC_INTERPRETER_IGNORED_FUNCTIONS,
        INCLUDE_SIZE_HINT_FUNCTIONS,
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    functions = get_interpreter_functions(data)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations
import logging
import threading
import typing
import warnings
from nitypes.waveform import AnalogWaveform, DigitalWaveform
from typing import Any, Generic, TypeVar

from collections.abc import Callable, Sequence

import google.protobuf.message
import grpc
import numpy

from . import errors as errors
from nidaqmx._base_interpreter import BaseEventHandler, BaseInterpreter
from nidaqmx._stubs import nidaqmx_pb2 as grpc_types
from nidaqmx._stubs import nidaqmx_pb2_grpc as nidaqmx_grpc
from ni.protobuf.types.waveform_conversion import (
    digital_waveform_from_protobuf,
    digital_waveform_to_protobuf,
    float64_analog_waveform_from_protobuf,
    float64_analog_waveform_to_protobuf
)
from nidaqmx.constants import WaveformAttributeMode
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.types import DriverVersion
from nidaqmx._grpc_time import convert_time_to_timestamp, convert_timestamp_to_time
from nidaqmx._waveform_utils import get_num_samps_per_chan
from session_pb2 import Session

_logger = logging.getLogger(__name__)

_UNABLE_TO_LOCATE_ERROR_RESOURCES_ERROR_MESSAGE = (
    "Error code could not be found. Reinstalling the driver might fix the issue. "
    "Otherwise, contact National Instruments technical support."
)


TEventResponse = TypeVar("TEventResponse", bound=google.protobuf.message.Message)

class GrpcEventHandler(BaseEventHandler, Generic[TEventResponse]):
    """Manage the lifetime of a gRPC event stream."""
    __slots__ = [
        "_event_name",
        "_interpreter",
        "_event_stream",
        "_event_callback",
        "_event_stream_exception",
        "_thread",
    ]

    def __init__(
        self,
        event_name: str,
        interpreter: GrpcStubInterpreter,
        event_stream: grpc._CallIterator[TEventResponse],
        event_callback: Callable[[TEventResponse], None],
    ) -> None:
        self._event_name = event_name
        self._interpreter = interpreter
        self._event_stream = event_stream
        self._event_callback = event_callback
        self._event_stream_exception: Exception | None = None
        self._thread = threading.Thread(target=self._thread_main, name=f"nidaqmx {event_name} thread")

        self._thread.start()

    def close(self) -> None:
        self._event_stream.cancel()
        self._thread.join()
        if self._event_stream_exception is not None:
            raise self._event_stream_exception

    def _thread_main(self) -> None:
        try:
            for event_response in self._event_stream:
                self._event_callback(event_response)
        except Exception as ex:
            if _is_cancelled(ex):
                return
            _logger.exception(
                "Unhandled exception raised while reading nidaqmx %s stream.", self._event_name
            )
            # Save the exception and re-raise it at the end of close().
            self._event_stream_exception = ex
            return


class GrpcStubInterpreter(BaseInterpreter):
    '''Interpreter for interacting with a gRPC Stub class'''
    # Do not add per-task state to the interpreter class.
    __slots__ = [
        '_grpc_options',
        '_client',
        '_driver_version',
    ]

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._client = nidaqmx_grpc.NiDAQmxStub(grpc_options.grpc_channel)
        try:
            major_version = self.get_system_info_attribute_uint32(0x1272)
            minor_version = self.get_system_info_attribute_uint32(0x1923)
            update_version = self.get_system_info_attribute_uint32(0x2f22)
        except Exception:
            major_version = 0
            minor_version = 0
            update_version = 0
        self._driver_version = DriverVersion(major_version, minor_version, update_version)

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)
        return response

    def _handle_rpc_error(self, rpc_error):
        error_message = rpc_error.details()
        error_code = None
        samps_per_chan_read = None
        samps_per_chan_written = None
        for entry in rpc_error.trailing_metadata() or []:
            if entry.key == 'ni-error':
                try:
                    error_code = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nError status: {entry.value}'
            elif entry.key == "ni-samps-per-chan-read":
                try:
                    samps_per_chan_read = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nSamples per channel read: {entry.value}'
            elif entry.key == "ni-samps-per-chan-written":
                try:
                    samps_per_chan_written = int(typing.cast(str, entry.value))
                except ValueError:
                    error_message += f'\nSamples per channel written: {entry.value}'
        grpc_error = rpc_error.code()
        if grpc_error == grpc.StatusCode.UNAVAILABLE:
            error_message = 'Failed to connect to server'
        elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
            error_message = (
                'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
            )
        if error_code is None:
            raise errors.RpcError(grpc_error, error_message) from None
        else:
            self._raise_error(error_code, error_message, samps_per_chan_written, samps_per_chan_read)

    def _check_for_error_from_response(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None):
        if error_code != 0:
            # This is an optimization for the partial read operation.
            error_message = _ERROR_MESSAGES.get(error_code, None)
            if not error_message:
                error_message = self.get_error_string(error_code)
            self._raise_error(error_code, error_message, samps_per_chan_written=samps_per_chan_written, samps_per_chan_read=samps_per_chan_read)

    def _raise_error(self, error_code, error_message, samps_per_chan_written=None, samps_per_chan_read=None):
        if error_code < 0:
            if samps_per_chan_read is not None:
                raise errors.DaqReadError(error_message, error_code, samps_per_chan_read) from None
            elif samps_per_chan_written is not None:
                raise errors.DaqWriteError(error_message, error_code, samps_per_chan_written) from None
            else:
                raise errors.DaqError(error_message, error_code) from None
        elif error_code > 0:
            if not error_message:
                error_message = self.get_error_string(error_code)
            warnings.warn(errors.DaqWarning(error_message, error_code))

    def _check_for_event_registration_error(self, event_stream):
        try:
            # Wait for initial metadata to ensure that the server has received the event
            # registration request and called the event registration function. Otherwise,
            # there is no guarantee that the event registration function is called before
            # the application sends the next RPC request (e.g. start_task).
            _ = event_stream.initial_metadata()

            # When the event registration function returns an error, the server should close
            # the event stream with an error before sending initial metadata. This behavior
            # requires NI gRPC Device Server version 2.2 or later.
            if event_stream.done() and event_stream.exception() is not None:
                raise event_stream.exception()
        except grpc.RpcError as rpc_error:
            self._handle_rpc_error(rpc_error)

    @property
    def driver_version(self):
        return self._driver_version

%for func in functions:
<%
    if func.function_name in GRPC_INTERPRETER_IGNORED_FUNCTIONS:
        continue
    params = get_params_for_function_signature(func)
    sorted_params = order_function_parameters_by_optional(params)
    parameter_signature = get_interpreter_parameter_signature(is_python_factory, sorted_params)
    if func.function_name in INCLUDE_SIZE_HINT_FUNCTIONS:
        parameter_signature = ", ".join([parameter_signature, "size_hint=0"])
    output_parameters = get_output_params(func)
%>\
    %if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
    %else:
    def ${func.function_name}(${parameter_signature}):
    %endif
\
<%include file="${'/grpc_interpreter' + get_grpc_function_call_template(func)}" args="function=func" />\
    %if len(output_parameters)  > 0:
        return ${get_response_parameters(func)}
    %endif

%endfor
    def hash_task_handle(self, task_handle):
        return hash(task_handle.name)

    ## get_error_string has special error handling.
    def get_error_string(self, error_code):
        try:
            # Do not use self._invoke() because it may call back into self.get_error_string().
            response = self._client.GetErrorString(
                grpc_types.GetErrorStringRequest(error_code=error_code))
            if not response.error_string:
                return _UNABLE_TO_LOCATE_ERROR_RESOURCES_ERROR_MESSAGE
            return response.error_string
        except grpc.RpcError:
            _logger.exception('Failed to get error string for error code %d.', error_code)
            return 'Failed to retrieve error description.'

    ## DAQmxReadIDPinMemory returns the size if given a 0 for arraySize.
    ## So, we read 1st time to get the size, then read 2nd time to get the data.
    def read_id_pin_memory(self, device_name, id_pin_name):
        response = self._invoke(
            self._client.ReadIDPinMemory,
            grpc_types.ReadIDPinMemoryRequest(device_name=device_name, id_pin_name=id_pin_name, array_size=0))
        if response.status <= 0:
            self._check_for_error_from_response(response.status)
        response = self._invoke(
            self._client.ReadIDPinMemory,
            grpc_types.ReadIDPinMemoryRequest(device_name=device_name, id_pin_name=id_pin_name, array_size=response.status))
        self._check_for_error_from_response(response.status)
        return list(response.data), response.data_length_read, response.format_code

    def set_runtime_environment(
            self, environment, environment_version, reserved_1, reserved_2):
        raise NotImplementedError

    def internal_get_last_created_chan(self):
        raise NotImplementedError

    def read_analog_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: AnalogWaveform[numpy.float64],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        return self.read_analog_waveforms(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            [waveform],
            waveform_attribute_mode
        )

    def read_analog_waveforms(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveforms: Sequence[AnalogWaveform[numpy.float64]],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        assert isinstance(task_handle, Session)
        response = self._invoke(
            self._client.ReadAnalogWaveforms,
            grpc_types.ReadAnalogWaveformsRequest(
                task=task_handle,
                num_samps_per_chan=number_of_samples_per_channel,
                timeout=timeout,
                waveform_attribute_mode_raw=waveform_attribute_mode.value
            ))

        if len(response.waveforms) != len(waveforms):
            raise ValueError(f"Expected {len(waveforms)} waveforms but received {len(response.waveforms)} from server")

        for i, grpc_waveform in enumerate(response.waveforms):
            temp_waveform = float64_analog_waveform_from_protobuf(grpc_waveform)
            waveforms[i].load_data(temp_waveform.scaled_data)

            waveforms[i].scale_mode = temp_waveform.scale_mode
            waveforms[i].timing = temp_waveform.timing
            waveforms[i].extended_properties.clear()
            waveforms[i].extended_properties.update(temp_waveform.extended_properties)

        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return response.samps_per_chan_read

    def read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: DigitalWaveform[Any],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        return self.read_digital_waveforms(
            task_handle,
            1,  # channel_count
            number_of_samples_per_channel,
            waveform.signal_count,  # number_of_signals_per_sample
            timeout,
            [waveform],
            waveform_attribute_mode
        )

    def read_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveforms: Sequence[DigitalWaveform[Any]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int:
        assert isinstance(task_handle, Session)
        response = self._invoke(
            self._client.ReadDigitalWaveforms,
            grpc_types.ReadDigitalWaveformsRequest(
                task=task_handle,
                num_samps_per_chan=number_of_samples_per_channel,
                timeout=timeout,
                waveform_attribute_mode_raw=waveform_attribute_mode.value
            ))

        if len(response.waveforms) != len(waveforms):
            raise ValueError(f"Expected {len(waveforms)} waveforms but received {len(response.waveforms)} from server")

        for i, grpc_waveform in enumerate(response.waveforms):
            temp_waveform = digital_waveform_from_protobuf(grpc_waveform)
            data = temp_waveform.data
            if data.dtype != waveforms[i].dtype:
                data = data.view(waveforms[i].dtype)
            waveforms[i].load_data(data)

            waveforms[i].timing = temp_waveform.timing
            waveforms[i].extended_properties.clear()
            waveforms[i].extended_properties.update(temp_waveform.extended_properties)

        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return response.samps_per_chan_read

    def read_new_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> Sequence[DigitalWaveform[numpy.uint8]]:
        assert isinstance(task_handle, Session)
        response = self._invoke(
            self._client.ReadDigitalWaveforms,
            grpc_types.ReadDigitalWaveformsRequest(
                task=task_handle,
                num_samps_per_chan=number_of_samples_per_channel,
                timeout=timeout,
                waveform_attribute_mode_raw=waveform_attribute_mode.value
            ))

        waveforms = [digital_waveform_from_protobuf(grpc_waveform) for grpc_waveform in response.waveforms]

        self._check_for_error_from_response(response.status, samps_per_chan_read=response.samps_per_chan_read)
        return waveforms

    def write_analog_waveform(
        self,
        task_handle: object,
        waveform: AnalogWaveform[typing.Any],
        auto_start: bool,
        timeout: float
    ) -> int:
        return self.write_analog_waveforms(task_handle, [waveform], auto_start, timeout)

    def write_analog_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[AnalogWaveform[typing.Any]],
        auto_start: bool,
        timeout: float
    ) -> int:
        assert isinstance(task_handle, Session)
        num_samps_per_chan = get_num_samps_per_chan(waveforms)

        grpc_waveforms = [float64_analog_waveform_to_protobuf(waveform) for waveform in waveforms]

        response = self._invoke(
            self._client.WriteAnalogWaveforms,
            grpc_types.WriteAnalogWaveformsRequest(
                task=task_handle,
                auto_start=auto_start,
                timeout=timeout,
                waveforms=grpc_waveforms
            ))

        self._check_for_error_from_response(response.status, samps_per_chan_written=response.samps_per_chan_written)
        return response.samps_per_chan_written

    def write_digital_waveform(
        self,
        task_handle: object,
        waveform: DigitalWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int:
        return self.write_digital_waveforms(task_handle, [waveform], auto_start, timeout)

    def write_digital_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[DigitalWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int:
        assert isinstance(task_handle, Session)
        num_samps_per_chan = get_num_samps_per_chan(waveforms)

        grpc_waveforms = [digital_waveform_to_protobuf(waveform) for waveform in waveforms]

        response = self._invoke(
            self._client.WriteDigitalWaveforms,
            grpc_types.WriteDigitalWaveformsRequest(
                task=task_handle,
                auto_start=auto_start,
                timeout=timeout,
                waveforms=grpc_waveforms
            ))

        self._check_for_error_from_response(response.status, samps_per_chan_written=response.samps_per_chan_written)
        return response.samps_per_chan_written

def _assign_numpy_array(numpy_array, grpc_array):
    """
    Assigns grpc array to numpy array maintaining the original shape.

    Checks for the instance of grpc_array with bytes, if validated to True,
    the numpy array is assigned to a 1D array of the grpc array.
    """
    grpc_array_size = len(grpc_array)
    if isinstance(grpc_array, bytes):
        assert numpy_array.nbytes >= grpc_array_size
        numpy_array.flat[:grpc_array_size] = numpy.frombuffer(grpc_array, dtype=numpy_array.dtype)
    else:
        assert numpy_array.size >= grpc_array_size
        numpy_array.flat[:grpc_array_size] = grpc_array

def _validate_array_dtype(numpy_array, expected_numpy_array_dtype):
    """Raises TypeError if array type doesn't match with expected numpy.dtype"""
    if expected_numpy_array_dtype != numpy.generic and numpy_array.dtype != expected_numpy_array_dtype:
        raise TypeError(f"array must have data type {expected_numpy_array_dtype}")

def _is_cancelled(ex: Exception) -> bool:
    """Returns True if the given exception is a cancelled RPC exception."""
    return (
        (isinstance(ex, grpc.RpcError) and ex.code() == grpc.StatusCode.CANCELLED)
        or (isinstance(ex, errors.RpcError) and ex.rpc_code == grpc.StatusCode.CANCELLED)
    )

_ERROR_MESSAGES = {
    DAQmxErrors.SAMPLES_NOT_YET_AVAILABLE: 'Some or all of the samples requested have not yet been acquired.\n\nTo wait for the samples to become available use a longer read timeout or read later in your program. To make the samples available sooner, increase the sample rate. If your task uses a start trigger, make sure that your start trigger is configured correctly. It is also possible that you configured the task for external timing, and no clock was supplied. If this is the case, supply an external clock.'
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/_library_interpreter.py.mako sha256=237797e47bbf2921a05205ba2d3a7349884ab3cac71824baaa75a26d9061f37b bytes=43115 -->
## FILE: src/codegen/templates/_library_interpreter.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/_library_interpreter.py.mako`
- sha256: `237797e47bbf2921a05205ba2d3a7349884ab3cac71824baaa75a26d9061f37b`
- bytes: 43115

````mako
<%
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.interpreter_helpers import (
        get_c_function_call_template,
        get_instantiation_lines_for_output,
        get_interpreter_functions,
        get_interpreter_parameter_signature,
        get_params_for_function_signature,
        get_return_values,
        is_event_register_function,
        LIBRARY_INTERPRETER_IGNORED_FUNCTIONS,
        INCLUDE_SIZE_HINT_FUNCTIONS,
    )
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    functions = get_interpreter_functions(data)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations
import ctypes
import logging
import numpy
import platform
import warnings
from enum import Enum
from datetime import timezone
from hightime import datetime as ht_datetime
from hightime import timedelta as ht_timedelta
from typing import Any, TYPE_CHECKING

from collections.abc import Callable, Sequence

from nidaqmx._base_interpreter import BaseEventHandler, BaseInterpreter
from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32, wrapped_ndpointer, TaskHandle
from nidaqmx.constants import FillMode, WaveformAttributeMode
from nidaqmx.error_codes import DAQmxErrors, DAQmxWarnings
from nidaqmx.errors import DaqError, DaqFunctionNotSupportedError, DaqReadError, DaqWarning, DaqWriteError
from nidaqmx.types import DriverVersion
from nidaqmx._lib_time import AbsoluteTime
from nidaqmx._waveform_utils import get_num_samps_per_chan
from nitypes.waveform.typing import ExtendedPropertyValue
from nitypes.waveform import AnalogWaveform, DigitalWaveform, SampleIntervalMode, Timing, ExtendedPropertyDictionary

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

_logger = logging.getLogger(__name__)
_was_runtime_environment_set = None

_INT64_WFM_SEC_PER_TICK = 100e-9
_T0_EPOCH = ht_datetime(1, 1, 1, tzinfo=timezone.utc)

# typedef int32 (CVICALLBACK *DAQmxSetWfmAttrCallbackPtr)(uInt32 channelIndex, const char attributeName[], int32 attributeType, const void* value, uInt32 valueSizeInBytes, void *callbackData);  # noqa: W505 - doc line too long
CSetWfmAttrCallbackPtr = ctypes.CFUNCTYPE(
    ctypes.c_int32,  # return value (error code)
    ctypes.c_uint32,  # channel_index
    ctypes.c_char_p,  # attribute_name
    ctypes.c_int32,  # attribute_type
    ctypes.c_void_p,  # value
    ctypes.c_uint32,  # value_size_in_bytes
    ctypes.c_void_p,  # callback_data
)

class WfmAttrType(Enum):
    BOOL32 = 1
    FLOAT64 = 2
    INT32 = 3
    STRING = 4

SetWfmAttrCallback: TypeAlias = Callable[[int, str, WfmAttrType, ExtendedPropertyValue, object], int]

class LibraryEventHandler(BaseEventHandler):
    """Manage the lifetime of a ctypes callback method pointer.

    If DAQmx invokes a callback method pointer that has been garbage collected, the Python
    interpreter will crash.
    """
    __slots__ = ["_callback_method_ptr"]

    def __init__(self, callback_method_ptr: object) -> None:
        self._callback_method_ptr = callback_method_ptr

    def close(self) -> None:
        self._callback_method_ptr = None


class LibraryInterpreter(BaseInterpreter):
    """
    Library C<->Python interpreter.
    This class is responsible for interpreting the Library's C API.

    """
    # Do not add per-task state to the interpreter class.
    __slots__ = ('_driver_version',)

    def __init__(self):
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except DaqFunctionNotSupportedError:
                pass
            finally:
                _was_runtime_environment_set = True

        major_version = self.get_system_info_attribute_uint32(0x1272)
        minor_version = self.get_system_info_attribute_uint32(0x1923)
        update_version = self.get_system_info_attribute_uint32(0x2f22)
        self._driver_version = DriverVersion(major_version, minor_version, update_version)

    @property
    def driver_version(self):
        return self._driver_version


% for func in functions:
<%
    if func.function_name in LIBRARY_INTERPRETER_IGNORED_FUNCTIONS:
        continue
    params = get_params_for_function_signature(func)
    sorted_params = order_function_parameters_by_optional(params)
    parameter_signature = get_interpreter_parameter_signature(is_python_factory, sorted_params)
    if func.function_name in INCLUDE_SIZE_HINT_FUNCTIONS:
        parameter_signature = ", ".join([parameter_signature, "size_hint=0"])
    return_values = get_return_values(func)
%>\
    %if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
    %else:
    def ${func.function_name}(${parameter_signature}):
    %endif
\
## Script instantiation for output parameters that will be passed by reference.
<%
    instantiation_lines = get_instantiation_lines_for_output(func)
    %>\
\
%if func.is_init_method and func.is_python_codegen_method:
        new_session_initialized = True
%endif
%if func.is_python_codegen_method:
    %if len(instantiation_lines) > 0:
        %for instantiation_line in instantiation_lines:
        ${instantiation_line}
        %endfor

    %endif
\
<%include file="${'/library_interpreter' + get_c_function_call_template(func)}" args="function=func" />\
    %if len(list(return_values)) != 0:
        return ${', '.join(return_values)}
    %endif
%else:
        raise NotImplementedError
%endif

%endfor
    ## get_error_string has special error handling.
    def get_error_string(self, error_code):
        error_buffer = ctypes.create_string_buffer(2048)

        c_func = lib_importer.windll.DAQmxGetErrorString
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [ctypes.c_int, ctypes.c_char_p,
                                      ctypes.c_uint]

        query_error_code = c_func(error_code, error_buffer, 2048)
        if query_error_code < 0:
            _logger.error('Failed to get error string for error code %d. DAQmxGetErrorString returned error code %d.', error_code, query_error_code)
            return 'Failed to retrieve error description.'
        return error_buffer.value.decode(lib_importer.encoding)

    ## get_extended_error_info has special error handling and it is library-only because it uses
    ## thread-local storage.
    def get_extended_error_info(self):
        error_buffer = ctypes.create_string_buffer(2048)

        c_func = lib_importer.windll.DAQmxGetExtendedErrorInfo
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [ctypes.c_char_p, ctypes.c_uint]

        query_error_code = c_func(error_buffer, 2048)
        if query_error_code < 0:
            _logger.error('Failed to get extended error info. DAQmxGetExtendedErrorInfo returned error code %d.', query_error_code)
            return 'Failed to retrieve error description.'
        return error_buffer.value.decode(lib_importer.encoding)

    ## read_analog_waveform has special handling for waveform attributes and callbacks
    def read_analog_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: AnalogWaveform[numpy.float64],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        """Read an analog waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(1, dtype=numpy.int64)
            dt_array = numpy.zeros(1, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        waveform.sample_count = number_of_samples_per_channel

        error_code, samples_read = self._internal_read_analog_waveform_ex(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            waveform.raw_data,
            properties,
            t0_array,
            dt_array,
        )

        waveform.sample_count = samples_read

        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings([waveform], t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    ## read_analog_waveforms has special handling for waveform attributes and callbacks
    def read_analog_waveforms(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveforms: Sequence[AnalogWaveform[numpy.float64]],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        """Read a set of analog waveforms with timing and attributes. All of the waveforms must be the same size."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties for waveform in waveforms]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(len(waveforms), dtype=numpy.int64)
            dt_array = numpy.zeros(len(waveforms), dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        for waveform in waveforms:
            waveform.sample_count = number_of_samples_per_channel

        error_code, samples_read = self._internal_read_analog_waveform_per_chan(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            [waveform.raw_data for waveform in waveforms],
            properties,
            t0_array,
            dt_array,
        )

        for waveform in waveforms:
            waveform.sample_count = samples_read
            
        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings(waveforms, t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    def _internal_read_analog_waveform_ex(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        fill_mode: int,
        read_array: numpy.typing.NDArray[numpy.float64],
        properties: Sequence[ExtendedPropertyDictionary] | None,
        t0_array: numpy.typing.NDArray[numpy.int64] | None,
        dt_array: numpy.typing.NDArray[numpy.int64] | None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were read
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxInternalReadAnalogWaveformEx
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        ctypes.c_double,
                        ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        ctypes.c_uint,
                        CSetWfmAttrCallbackPtr,
                        ctypes.c_void_p,
                        wrapped_ndpointer(dtype=numpy.float64, flags=("C", "W")),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        error_code = c_func(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            fill_mode,
            t0_array,
            dt_array,
            0 if t0_array is None else t0_array.size,
            self._get_wfm_attr_callback(properties),
            None,
            read_array,
            read_array.size,
            ctypes.byref(samps_per_chan_read),
            None,
        )

        return error_code, samps_per_chan_read.value

    def _internal_read_analog_waveform_per_chan(
        self,
        task_handle: object,
        num_samps_per_chan: int,
        timeout: float,
        read_arrays: Sequence[numpy.typing.NDArray[numpy.float64]],
        properties: Sequence[ExtendedPropertyDictionary] | None,
        t0_array: numpy.typing.NDArray[numpy.int64] | None,
        dt_array: numpy.typing.NDArray[numpy.int64] | None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were read
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_read = ctypes.c_int()

        channel_count = len(read_arrays)
        assert channel_count > 0
        array_size = read_arrays[0].size
        assert all(read_array.size == array_size for read_array in read_arrays)

        c_func = lib_importer.windll.DAQmxInternalReadAnalogWaveformPerChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        ctypes.c_uint,
                        CSetWfmAttrCallbackPtr,
                        ctypes.c_void_p,
                        ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
                        ctypes.c_uint,
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        read_array_pointers = (ctypes.POINTER(ctypes.c_double) * channel_count)()
        for i, read_array in enumerate(read_arrays):
            read_array_pointers[i] = read_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

        error_code = c_func(
            task_handle,
            num_samps_per_chan,
            timeout,
            t0_array,
            dt_array,
            0 if t0_array is None else t0_array.size,
            self._get_wfm_attr_callback(properties),
            None,
            read_array_pointers,
            channel_count,
            array_size,
            ctypes.byref(samps_per_chan_read),
            None,
        )
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return error_code, samps_per_chan_read.value

    def _get_wfm_attr_callback(self, properties):
        if properties is not None:
            def set_wfm_attr_callback(
                channel_index: int,
                attribute_name: str,
                attribute_type: WfmAttrType,
                value: ExtendedPropertyValue,
                callback_data: object,
            ) -> int:
                properties[channel_index][attribute_name] = value
                return 0
            return self._get_wfm_attr_callback_ptr(set_wfm_attr_callback)
        else:
            return CSetWfmAttrCallbackPtr()

    def _get_wfm_attr_value(
        self, attribute_type: int, value: ctypes.c_void_p, value_size_in_bytes: int
    ) -> ExtendedPropertyValue:
        if attribute_type == WfmAttrType.BOOL32.value:
            assert value_size_in_bytes == 4
            return ctypes.cast(value, ctypes.POINTER(ctypes.c_int32))[0] != 0
        elif attribute_type == WfmAttrType.FLOAT64.value:
            assert value_size_in_bytes == 8
            return float(ctypes.cast(value, ctypes.POINTER(ctypes.c_double))[0])
        elif attribute_type == WfmAttrType.INT32.value:
            assert value_size_in_bytes == 4
            return int(ctypes.cast(value, ctypes.POINTER(ctypes.c_int32))[0])
        elif attribute_type == WfmAttrType.STRING.value:
            value_c_bytes = ctypes.cast(value, ctypes.POINTER(ctypes.c_byte))
            assert value_c_bytes[value_size_in_bytes - 1] == 0
            return bytes(value_c_bytes[0 : value_size_in_bytes - 1]).decode(lib_importer.encoding)
        else:
            raise ValueError(f"Unsupported attribute type {attribute_type}")

    def _get_wfm_attr_callback_ptr(
        self, set_wfm_attr_callback: SetWfmAttrCallback
    ) -> ctypes._FuncPointer:
        def _invoke_callback(
            channel_index: int,
            attribute_name: bytes,
            attribute_type: int,
            value: ctypes.c_void_p,
            value_size_in_bytes: int,
            callback_data: object,
        ) -> int:
            try:
                return set_wfm_attr_callback(
                    channel_index,
                    attribute_name.decode(lib_importer.encoding),
                    WfmAttrType(attribute_type),
                    self._get_wfm_attr_value(attribute_type, value, value_size_in_bytes),
                    callback_data,
                )
            except Exception:
                _logger.exception("Unhandled exception in set_wfm_attr_callback")
                return -1

        return CSetWfmAttrCallbackPtr(_invoke_callback)

    def _set_waveform_timings(
        self, 
        waveforms: Sequence[AnalogWaveform[numpy.float64] | DigitalWaveform[numpy.uint8]], 
        t0_array: numpy.typing.NDArray[numpy.int64], 
        dt_array: numpy.typing.NDArray[numpy.int64]
    ) -> None:
        for i, waveform in enumerate(waveforms):
            waveform.timing = Timing(
                sample_interval_mode=SampleIntervalMode.REGULAR,
                timestamp=_T0_EPOCH + ht_timedelta(seconds=t0_array[i] * _INT64_WFM_SEC_PER_TICK),
                sample_interval=ht_timedelta(seconds=dt_array[i] * _INT64_WFM_SEC_PER_TICK),
            )

    ## read_digital_waveform has special handling for waveform attributes and callbacks
    def read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        waveform: DigitalWaveform[Any],
        waveform_attribute_mode: WaveformAttributeMode
    ) -> int:
        """Read a digital waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(1, dtype=numpy.int64)
            dt_array = numpy.zeros(1, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        waveform.sample_count = number_of_samples_per_channel

        error_code, samples_read = self._internal_read_digital_waveform(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            self._get_digital_read_array(waveform),
            properties,
            t0_array,
            dt_array,
            None,
        )

        waveform.sample_count = samples_read
        
        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings([waveform], t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    def _get_digital_read_array(self, waveform: DigitalWaveform[Any]) -> numpy.typing.NDArray[numpy.uint8]:  
        data = waveform.data
        if data.dtype != numpy.uint8:
            data = data.view(numpy.uint8)
        return data

    def read_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveforms: Sequence[DigitalWaveform[Any]],
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> int:
        """Read a digital waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [waveform.extended_properties for waveform in waveforms]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(channel_count, dtype=numpy.int64)
            dt_array = numpy.zeros(channel_count, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        # Since there's no DAQmxInternalReadDigitalWaveformPerChan, we have to allocate a
        # temporary contiguous array to read the data from multiple channels into.
        read_array = numpy.zeros(
            (number_of_samples_per_channel, channel_count, number_of_signals_per_sample),
            dtype=numpy.uint8)

        bytes_per_chan_array = numpy.zeros(channel_count, dtype=numpy.uint32)

        error_code, samples_read = self._internal_read_digital_waveform(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_SCAN_NUMBER.value, # GROUP_BY_SCAN_NUMBER handles short reads better than GROUP_BY_CHANNEL
            read_array,
            properties,
            t0_array,
            dt_array,
            bytes_per_chan_array,
        )

        for i, waveform in enumerate(waveforms):        
            waveform.sample_count = samples_read
            waveform_signal_count = waveform.data.shape[1]
            channel_signal_count = bytes_per_chan_array[i]
            if waveform_signal_count != channel_signal_count:
                raise ValueError(f"waveforms[{i}].data has {waveform_signal_count} signals, but expected {channel_signal_count}")
            waveform.data[:] = read_array[:, i, :channel_signal_count]

        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings(waveforms, t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return samples_read

    def read_new_digital_waveforms(
        self,
        task_handle: object,
        channel_count: int,
        number_of_samples_per_channel: int,
        number_of_signals_per_sample: int,
        timeout: float,
        waveform_attribute_mode: WaveformAttributeMode,
    ) -> Sequence[DigitalWaveform[numpy.uint8]]:
        """Read a digital waveform with timing and attributes."""
        if WaveformAttributeMode.EXTENDED_PROPERTIES in waveform_attribute_mode:
            properties = [ExtendedPropertyDictionary() for _ in range(channel_count)]
        else:
            properties = None

        if WaveformAttributeMode.TIMING in waveform_attribute_mode:
            t0_array = numpy.zeros(channel_count, dtype=numpy.int64)
            dt_array = numpy.zeros(channel_count, dtype=numpy.int64)
        else:
            t0_array = None
            dt_array = None

        read_array = numpy.zeros(
            (number_of_samples_per_channel, channel_count, number_of_signals_per_sample),
            dtype=numpy.uint8)

        bytes_per_chan_array = numpy.zeros(channel_count, dtype=numpy.uint32)

        error_code, samples_read = self._internal_read_digital_waveform(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_SCAN_NUMBER.value, # GROUP_BY_SCAN_NUMBER handles short reads better than GROUP_BY_CHANNEL
            read_array,
            properties,
            t0_array,
            dt_array,
            bytes_per_chan_array,
        )

        waveforms = []
        for i in range(channel_count):
            channel_signal_count = bytes_per_chan_array[i]
            waveform = DigitalWaveform(
                sample_count=samples_read,
                data=read_array[:, i, :channel_signal_count],
                copy_extended_properties=False,
                extended_properties=properties[i] if properties else None)
            waveforms.append(waveform)

        if t0_array is not None and dt_array is not None:
            self._set_waveform_timings(waveforms, t0_array, dt_array)

        self.check_for_error(error_code, samps_per_chan_read=samples_read)
        return waveforms

    def _internal_read_digital_waveform(
        self,
        task_handle: object,
        number_of_samples_per_channel: int,
        timeout: float,
        fill_mode: int,
        read_array: numpy.typing.NDArray[numpy.uint8],
        properties: Sequence[ExtendedPropertyDictionary] | None,
        t0_array: numpy.typing.NDArray[numpy.int64] | None,
        dt_array: numpy.typing.NDArray[numpy.int64] | None,
        bytes_per_chan_array: numpy.typing.NDArray[numpy.uint32] | None = None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were read
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_read = ctypes.c_int()
        num_bytes_per_samp = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxInternalReadDigitalWaveform
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        ctypes.c_double,
                        ctypes.c_int,
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        wrapped_ndpointer(dtype=numpy.int64, flags=("C", "W")),
                        ctypes.c_uint,
                        CSetWfmAttrCallbackPtr,
                        ctypes.c_void_p,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=("C", "W")),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(ctypes.c_int),
                        wrapped_ndpointer(dtype=numpy.uint32, flags=("C", "W")),
                        ctypes.c_uint,
                        ctypes.POINTER(c_bool32),
                    ]

        error_code = c_func(
            task_handle,
            number_of_samples_per_channel,
            timeout,
            fill_mode,
            t0_array,
            dt_array,
            0 if t0_array is None else t0_array.size,
            self._get_wfm_attr_callback(properties),
            None,
            read_array,
            read_array.size,
            ctypes.byref(samps_per_chan_read),
            ctypes.byref(num_bytes_per_samp),
            bytes_per_chan_array,
            0 if bytes_per_chan_array is None else bytes_per_chan_array.size,
            None,
        )

        return error_code, samps_per_chan_read.value

    ## DAQmxReadIDPinMemory returns the size if given a null pointer.
    ## So, we read 1st time to get the size, then read 2nd time to get the data.
    def read_id_pin_memory(self, device_name, id_pin_name):
        data_length_read = ctypes.c_uint()
        format_code = ctypes.c_uint()

        c_func = lib_importer.windll.DAQmxReadIDPinMemory
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ctypes_byte_str, ctypes_byte_str,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=('C','W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_uint),
                        ctypes.POINTER(ctypes.c_uint)]

        array_size = c_func(
            device_name, id_pin_name, None, 0,
            ctypes.byref(data_length_read), ctypes.byref(format_code))

        if array_size < 0:
            self.check_for_error(array_size)

        data = numpy.zeros(array_size, dtype=numpy.uint8)

        error_code = c_func(
            device_name, id_pin_name, data, array_size,
            ctypes.byref(data_length_read), ctypes.byref(format_code))
        self.check_for_error(error_code)
        return data.tolist(), data_length_read.value, format_code.value

    ## The metadata for 'read_power_binary_i16' function is not available in daqmxAPISharp.json file.
    def read_power_binary_i16(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadPowerBinaryI16
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                        wrapped_ndpointer(dtype=numpy.int16, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array, read_voltage_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return read_voltage_array, read_current_array, samps_per_chan_read.value

    ## The metadata for 'read_power_f64' function is not available in daqmxAPISharp.json file.
    def read_power_f64(
            self, task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array):
        samps_per_chan_read = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadPowerF64
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                        wrapped_ndpointer(dtype=numpy.float64, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, fill_mode,
            read_voltage_array, read_current_array, read_voltage_array.size,
            ctypes.byref(samps_per_chan_read), None)
        self.check_for_error(error_code, samps_per_chan_read=samps_per_chan_read.value)

        return read_voltage_array, read_current_array, samps_per_chan_read.value

    ## The datatype of 'read_array' is incorrect in daqmxAPISharp.json file.
    def read_raw(self, task, num_samps_per_chan, timeout, read_array):
        samples_read = ctypes.c_int()
        number_of_bytes_per_sample = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxReadRaw
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, ctypes.c_double,
                        wrapped_ndpointer(dtype=read_array.dtype, flags=('C', 'W')),
                        ctypes.c_uint, ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task, num_samps_per_chan, timeout, read_array,
            read_array.nbytes, ctypes.byref(samples_read),
            ctypes.byref(number_of_bytes_per_sample), None)
        self.check_for_error(error_code, samps_per_chan_read=samples_read.value)

        return read_array, samples_read.value, number_of_bytes_per_sample.value

    ## write_analog_waveform has special handling
    def write_analog_waveform(
        self,
        task_handle: object,
        waveform: AnalogWaveform[Any],
        auto_start: bool,
        timeout: float
    ) -> int:
        """Write an analog waveform."""
        return self.write_analog_f64(
            task_handle,
            waveform.sample_count,
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            self._get_analog_write_array(waveform),
        )

    ## write_analog_waveforms has special handling
    def write_analog_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[AnalogWaveform[Any]],
        auto_start: bool,
        timeout: float
    ) -> int:
        """Write analog waveforms."""
        num_samps_per_chan = get_num_samps_per_chan(waveforms)

        write_arrays = [self._get_analog_write_array(waveform) for waveform in waveforms]

        error_code, samples_written = self._internal_write_analog_waveform_per_chan(
            task_handle,
            num_samps_per_chan,
            auto_start,
            timeout,
            write_arrays,
        )

        self.check_for_error(error_code, samps_per_chan_written=samples_written)
        return samples_written

    def _get_analog_write_array(self, waveform: AnalogWaveform[Any]) -> numpy.typing.NDArray[numpy.float64]:  
        scaled_data = waveform.scaled_data
        if scaled_data.flags.c_contiguous:
            return scaled_data
        return scaled_data.copy(order="C")

    def _internal_write_analog_waveform_per_chan(
        self,
        task_handle: object,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        write_arrays: Sequence[numpy.typing.NDArray[numpy.float64]],
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were written
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_written = ctypes.c_int()

        channel_count = len(write_arrays)
        assert channel_count > 0
        assert all(write_array.size >= num_samps_per_chan for write_array in write_arrays)

        c_func = lib_importer.windll.DAQmxInternalWriteAnalogWaveformPerChan
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        c_bool32,
                        ctypes.c_double,
                        ctypes.POINTER(ctypes.POINTER(ctypes.c_double)),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        write_array_pointers = (ctypes.POINTER(ctypes.c_double) * channel_count)()
        for i, write_array in enumerate(write_arrays):
            write_array_pointers[i] = write_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

        error_code = c_func(
            task_handle,
            num_samps_per_chan,
            auto_start,
            timeout,
            write_array_pointers,
            channel_count,
            ctypes.byref(samps_per_chan_written),
            None,
        )

        return error_code, samps_per_chan_written.value

    def write_digital_waveform(
        self,
        task_handle: object,
        waveform: DigitalWaveform[Any],
        auto_start: bool,
        timeout: float,
    ) -> int:
        """Write a digital waveform."""
        bytes_per_chan_array = numpy.array([waveform.signal_count], dtype=numpy.uint32)

        error_code, samples_written = self._internal_write_digital_waveform(
            task_handle,
            waveform.sample_count,
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            self._get_digital_write_array(waveform),
            bytes_per_chan_array,
        )

        self.check_for_error(error_code, samps_per_chan_written=samples_written)
        return samples_written

    def _get_digital_write_array(self, waveform: DigitalWaveform[Any]) -> numpy.typing.NDArray[numpy.uint8]:  
        data = waveform.data
        if data.dtype != numpy.uint8:
            data = data.view(numpy.uint8)
        if data.flags.c_contiguous:
            return data
        return data.copy(order="C")

    def write_digital_waveforms(
        self,
        task_handle: object,
        waveforms: Sequence[DigitalWaveform[Any]],
        auto_start: bool,
        timeout: float,
    ) -> int:
        """Write digital waveforms."""
        channel_count = len(waveforms)
        sample_count = get_num_samps_per_chan(waveforms)
                
        bytes_per_chan_array = numpy.array([wf.signal_count for wf in waveforms], dtype=numpy.uint32)

        # build a temporary contiguous array to write the data from multiple channels into.
        # write_array must be in the format (numChans x numSampsPerChan x maxDataWidth)
        write_array = numpy.zeros(
            (channel_count, sample_count, max(bytes_per_chan_array)),
            dtype=numpy.uint8,
        )
        for i, waveform in enumerate(waveforms):
            signal_count = waveform.signal_count
            write_array[i, :, :signal_count] = waveform.data

        error_code, samples_written = self._internal_write_digital_waveform(
            task_handle,
            sample_count,
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            write_array,
            bytes_per_chan_array,
        )

        self.check_for_error(error_code, samps_per_chan_written=samples_written)
        return samples_written

    def _internal_write_digital_waveform(
        self,
        task_handle: object,
        num_samps_per_chan: int,
        auto_start: bool,
        timeout: float,
        data_layout: int,
        write_array: numpy.typing.NDArray[numpy.uint8],
        bytes_per_chan_array: numpy.typing.NDArray[numpy.uint32] | None = None,
    ) -> tuple[
        int, # error code
        int, # The number of samples per channel that were written
    ]:
        assert isinstance(task_handle, TaskHandle)
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxInternalWriteDigitalWaveform
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        TaskHandle,
                        ctypes.c_int,
                        c_bool32,
                        ctypes.c_double,
                        c_bool32,
                        wrapped_ndpointer(dtype=numpy.uint8, flags=("C",)),
                        wrapped_ndpointer(dtype=numpy.uint32, flags=("C",)),
                        ctypes.c_uint,
                        ctypes.POINTER(ctypes.c_int),
                        ctypes.POINTER(c_bool32),
                    ]

        error_code = c_func(
            task_handle,
            num_samps_per_chan,
            auto_start,
            timeout,
            data_layout,
            write_array,
            bytes_per_chan_array,
            0 if bytes_per_chan_array is None else bytes_per_chan_array.size,
            ctypes.byref(samps_per_chan_written),
            None,
        )

        return error_code, samps_per_chan_written.value

    ## The datatype of 'write_array' is incorrect in daqmxAPISharp.json file.
    def write_raw(
            self, task_handle, num_samps_per_chan, auto_start, timeout, numpy_array):
        samps_per_chan_written = ctypes.c_int()

        c_func = lib_importer.windll.DAQmxWriteRaw
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        lib_importer.task_handle, ctypes.c_int, c_bool32,
                        ctypes.c_double,
                        wrapped_ndpointer(dtype=numpy_array.dtype,
                                        flags=('C')),
                        ctypes.POINTER(ctypes.c_int), ctypes.POINTER(c_bool32)]

        error_code = c_func(
            task_handle, num_samps_per_chan, auto_start, timeout, numpy_array,
            ctypes.byref(samps_per_chan_written), None)
        self.check_for_error(error_code, samps_per_chan_written=samps_per_chan_written.value)

        return samps_per_chan_written.value

    def hash_task_handle(self, task_handle):
        return hash(task_handle.value)

    def check_for_error(self, error_code, samps_per_chan_written=None, samps_per_chan_read=None):
        if not error_code:
            return

        if error_code < 0:
            extended_error_info = self.get_extended_error_info()

            if samps_per_chan_read is not None:
                raise DaqReadError(extended_error_info, error_code, samps_per_chan_read)
            elif samps_per_chan_written is not None:
                raise DaqWriteError(extended_error_info, error_code, samps_per_chan_written)
            else:
                raise DaqError(extended_error_info, error_code)

        elif error_code > 0:
            error_string = self.get_error_string(error_code)

            warnings.warn(DaqWarning(error_string, error_code))


def is_string_buffer_too_small(error_code):
    return (
        error_code == DAQmxErrors.BUFFER_TOO_SMALL_FOR_STRING or
        error_code == DAQmxWarnings.CAPI_STRING_TRUNCATED_TO_FIT_BUFFER)


def is_array_buffer_too_small(error_code):
    return error_code == DAQmxErrors.WRITE_BUFFER_TOO_SMALL
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/constants.mako sha256=83161f6f158fb01f53644afe593a5621cf4ba275700843377478c98db327fdaa bytes=827 -->
## FILE: src/codegen/templates/constants.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/constants.mako`
- sha256: `83161f6f158fb01f53644afe593a5621cf4ba275700843377478c98db327fdaa`
- bytes: 827

````mako
<%
import codegen.utilities.enum_helpers as enum_helpers

enums = enum_helpers.get_enums(data)
%>\
# Do not edit this file; it was automatically generated.

from enum import Enum, Flag

# Constants
AUTO = -1
CFG_DEFAULT = -1
DEFAULT = -1
READ_ALL_AVAILABLE = -1
WAIT_INFINITELY = -1.0


# Enums
% for name, enum_metadata in enums.items():
class ${name}(Enum):
%   for value in enum_metadata['values']:
    ${value['name']} = ${value['value']}${enum_helpers.get_enum_value_docstring(value['documentation']['description'])}
%   endfor


% endfor
class ReallocationPolicy(Enum):
    DO_NOT_REALLOCATE = 0  #: Do not reallocate waveforms.
    TO_GROW = 1  #: Reallocate waveforms to grow when needed.


class WaveformAttributeMode(Flag):
    NONE = 0
    TIMING = 1
    EXTENDED_PROPERTIES = 2
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/error_codes.mako sha256=2b9a359f5217f4b495e2e475d2b1c2228cc7ad121f9e848edc90839cd4aaf67d bytes=528 -->
## FILE: src/codegen/templates/error_codes.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/error_codes.mako`
- sha256: `2b9a359f5217f4b495e2e475d2b1c2228cc7ad121f9e848edc90839cd4aaf67d`
- bytes: 528

````mako
<%
errors_metadata, warnings_metadata = data['DAQmxErrors'], data['DAQmxWarnings']
%>\
# Do not edit this file; it was automatically generated.

from enum import IntEnum

__all__ = ['DAQmxErrors', 'DAQmxWarnings']


class DAQmxErrors(IntEnum):
    %for value in errors_metadata['values']:
    ${value['name']} = ${value['value']}
    %endfor
    UNKNOWN = -1


class DAQmxWarnings(IntEnum):
    UNKNOWN = -1
    %for value in warnings_metadata['values']:
    ${value['name']} = ${value['value']}
    %endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/function_template.py.mako sha256=f51be763159fc5e6dc1ea712b80ed27730483e2ab6309e2db1c26ec341efbd1e bytes=3999 -->
## FILE: src/codegen/templates/function_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/function_template.py.mako`
- sha256: `f51be763159fc5e6dc1ea712b80ed27730483e2ab6309e2db1c26ec341efbd1e`
- bytes: 3999

````mako
<%def name="script_function(func)">\
<%
    from codegen.utilities.interpreter_helpers import INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES
    from codegen.utilities.helpers import camel_to_snake_case
    from codegen.utilities.function_helpers import (
        order_function_parameters_by_optional,get_parameters_docstring_lines_length,get_parameter_signature,
        get_instantiation_lines,generate_function_call_args, get_list_default_value,is_path_type)
    from codegen.utilities.text_wrappers import wrap, docstring_wrap
    %>\
################################################################################
## Script function signature.
################################################################################
%if func.is_python_factory:
    @staticmethod
%endif
<%
    sorted_params = order_function_parameters_by_optional(func.parameters)
    interpreter_func_name = camel_to_snake_case(func.c_function_name, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES)
    parameter_signature = get_parameter_signature(is_python_factory, sorted_params)
    %>\
    %if (len(func.function_name) + len(parameter_signature)) > 68:
    def ${func.function_name}(
            ${parameter_signature + '):' | wrap(12, 12)}
    %else:
    def ${func.function_name}(${parameter_signature}):
    %endif
\
################################################################################
## Script function docstring.
################################################################################
        """
        ${func.description | docstring_wrap(8, 8)}
    %if func.parameters:

        Args:
        %for input_param in sorted_params:
<%          initial_len, first_line = get_parameters_docstring_lines_length(input_param)%>\
            %if is_path_type(input_param):
            ${input_param.parameter_name}: ${
                input_param.description if first_line else '' | docstring_wrap(initial_len, 16)}
            %else:
            ${input_param.parameter_name} (${input_param.python_type_annotation}): ${
                input_param.description if first_line else '' | docstring_wrap(initial_len, 16)}
            %endif
            %if not first_line:
                ${input_param.description | docstring_wrap(16, 16)}
            %endif
        %endfor
    %endif
    %if func.adaptor_parameter is not None:
        Returns:
            ${func.adaptor_parameter.data_type}:

            ${func.adaptor_parameter.description | docstring_wrap(12, 12)}
    %endif
        """
\
################################################################################
## Script function body.
################################################################################
\
## Script default values for parameters that are lists or file path,
## since default values in Python functions should not be mutable.
    %for input_param in func.parameters:
        %if input_param.is_list:
        if ${input_param.parameter_name} is None:
            ${input_param.parameter_name} = ${get_list_default_value(func, input_param)}

        %elif is_path_type(input_param):
        if ${input_param.parameter_name} is None:
            ${input_param.parameter_name} = ""

        %endif
    %endfor
\
## Script instantiation of numpy arrays for input parameters that are lists, and ctypes variables for
## output parameters that will be passed by reference.
<%
    instantiation_lines = get_instantiation_lines(func.parameters)
    %>\
\
    %if len(instantiation_lines) > 0:
        %for instantiation_line in instantiation_lines:
        ${instantiation_line}
        %endfor

    %endif
<%
    function_call_args = generate_function_call_args(func)
%>
\
        self._interpreter.${interpreter_func_name}(
            ${', '.join(function_call_args) | wrap(12, 12)})
\
## Script return call.
    %if func.adaptor_parameter is not None:

        return ${func.adaptor_parameter.adaptor}
    %endif
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/grpc_interpreter/default_grpc_function_call.py.mako sha256=e5251f3c9fa648f619abad88e52ac9e6056707334d96e88abc2d74238bbffb07 bytes=3038 -->
## FILE: src/codegen/templates/grpc_interpreter/default_grpc_function_call.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/grpc_interpreter/default_grpc_function_call.py.mako`
- sha256: `e5251f3c9fa648f619abad88e52ac9e6056707334d96e88abc2d74238bbffb07`
- bytes: 3038

````mako
<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import (
        check_if_parameters_contain_read_array,
        create_compound_parameter_request,
        get_compound_parameter,
        get_event_name,
        get_grpc_interpreter_call_params,
        get_input_arguments_for_compound_params,
        get_numpy_array_params,
        get_output_params,
        get_params_for_function_signature,
        get_read_array_parameters,
        is_custom_read_write_function,
        is_event_unregister_function,
        get_samps_per_chan_read_param,
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.helpers import snake_to_pascal

    params = get_params_for_function_signature(function, True)
    sorted_params = order_function_parameters_by_optional(params)
    output_parameters = get_output_params(function)
    compound_parameter = get_compound_parameter(function.base_parameters)
    grpc_interpreter_params = get_grpc_interpreter_call_params(function, sorted_params)
    is_read_method = check_if_parameters_contain_read_array(function.base_parameters)
%>\
%if compound_parameter is not None:
        ${compound_parameter.parameter_name} = []
        for index in range(len(${get_input_arguments_for_compound_params(function)[0]})):
            ${compound_parameter.parameter_name}.append(${create_compound_parameter_request(function)})
%endif
%if function.is_init_method:
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
%endif
%if is_custom_read_write_function(function):
    %for parameter_name, parameter_dtype in get_numpy_array_params(function).items():
        _validate_array_dtype(${parameter_name}, ${parameter_dtype})
    %endfor
%endif
        response = self._invoke(
            self._client.${snake_to_pascal(function.function_name)},
%if (len(function.function_name) + len(grpc_interpreter_params)) > 68:
            grpc_types.${snake_to_pascal(function.function_name)}Request(
    %if function.is_init_method:
                ${grpc_interpreter_params | wrap(16, 16)}),
            metadata=metadata)
    %else:
                ${grpc_interpreter_params + ')' | wrap(16, 16)})
    %endif
%else:
    %if function.is_init_method:
            grpc_types.${snake_to_pascal(function.function_name)}Request(${grpc_interpreter_params + ')'},
            metadata=metadata)
    %else:
            grpc_types.${snake_to_pascal(function.function_name)}Request(${grpc_interpreter_params + ')'})
    %endif
%endif
%if is_read_method:
    <%
        samps_per_chan_param = get_samps_per_chan_read_param(function)
    %>
    %for param in get_read_array_parameters(function):
        _assign_numpy_array(${param}, response.${param})
    %endfor
        self._check_for_error_from_response(response.status, samps_per_chan_read=response.${samps_per_chan_param})
%endif
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/grpc_interpreter/event_function_call.py.mako sha256=d937e7324750dc96041af6409193554f20b557517daeb0f1409cf39680c9cf9f bytes=2546 -->
## FILE: src/codegen/templates/grpc_interpreter/event_function_call.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/grpc_interpreter/event_function_call.py.mako`
- sha256: `d937e7324750dc96041af6409193554f20b557517daeb0f1409cf39680c9cf9f`
- bytes: 2546

````mako
<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import (
        check_if_parameters_contain_read_array,
        create_compound_parameter_request,
        get_callback_function_call_args,
        get_compound_parameter,
        get_event_name,
        get_grpc_interpreter_call_params,
        get_input_arguments_for_compound_params,
        get_output_params,
        get_params_for_function_signature,
        get_read_array_parameters,
        is_event_function,
    )
    from codegen.utilities.function_helpers import order_function_parameters_by_optional
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.helpers import snake_to_pascal

    assert is_event_function(function)
    assert function.stream_response

    params = get_params_for_function_signature(function, True)
    sorted_params = order_function_parameters_by_optional(params)
    output_parameters = get_output_params(function)
    compound_parameter = get_compound_parameter(function.base_parameters)
    grpc_interpreter_params = get_grpc_interpreter_call_params(function, sorted_params)
    is_read_method = check_if_parameters_contain_read_array(function.base_parameters)
    event_name = get_event_name(function)
    event_display_name = event_name.replace("_", " ")
    function_call_args = get_callback_function_call_args(function)
%>\
        assert options == 0
        assert callback_function is not None

        event_stream = self._invoke(
            self._client.${snake_to_pascal(function.function_name)},
%if (len(function.function_name) + len(grpc_interpreter_params)) > 68:
            grpc_types.${snake_to_pascal(function.function_name)}Request(
                ${grpc_interpreter_params + ')' | wrap(16)})
%else:
            grpc_types.${snake_to_pascal(function.function_name)}Request(${grpc_interpreter_params + ')'})
%endif

        self._check_for_event_registration_error(event_stream)

        def invoke_callback(response):
            try:
                callback_function(
                    ${', '.join(function_call_args) | wrap(20)})
            except Exception:
                _logger.exception(
                    "Ignoring unhandled exception raised by event callback function: %r",
                    callback_function,
                )

        return GrpcEventHandler(
            "${event_display_name}",
            self,
            event_stream,
            invoke_callback,
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/library_interpreter/default_c_function_call.py.mako sha256=d754387adddd63500bbd2fb192bd3710bb1428b325599b94de9333afa71467b6 bytes=1218 -->
## FILE: src/codegen/templates/library_interpreter/default_c_function_call.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/library_interpreter/default_c_function_call.py.mako`
- sha256: `d754387adddd63500bbd2fb192bd3710bb1428b325599b94de9333afa71467b6`
- bytes: 1218

````mako
<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_types,
        get_samps_per_chan_read_or_write_param,
    )
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    function_call_args = generate_interpreter_function_call_args(function)

    # samps_per_chan_param includes the keyword argument (samps_per_chan_read=
    # or samps_per_chan_written=)
    samps_per_chan_param = get_samps_per_chan_read_or_write_param(function.base_parameters)
%>\
        c_func = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ${', '.join(get_argument_types(function)) | wrap(24, 24)}]

        error_code = c_func(
            ${', '.join(function_call_args) | wrap(12, 12)})
%if samps_per_chan_param is None:
        self.check_for_error(error_code)
%else:
        self.check_for_error(error_code, ${samps_per_chan_param}.value)
%endif
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/library_interpreter/double_c_function_call.py.mako sha256=e519f6a2e921230dd961a1a5224974c1cbdf97fc63ca4e457c73bee0bdf7aa6f bytes=1837 -->
## FILE: src/codegen/templates/library_interpreter/double_c_function_call.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/library_interpreter/double_c_function_call.py.mako`
- sha256: `e519f6a2e921230dd961a1a5224974c1cbdf97fc63ca4e457c73bee0bdf7aa6f`
- bytes: 1837

````mako
<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_types,
        get_output_param_with_ivi_dance_mechanism,
        get_output_params,
        INCLUDE_SIZE_HINT_FUNCTIONS,
    )
    from codegen.utilities.function_helpers import instantiate_explicit_output_param
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    function_call_args = generate_interpreter_function_call_args(function)
    explicit_output_param = get_output_param_with_ivi_dance_mechanism(function)
%>\
        c_func = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ${', '.join(get_argument_types(function)) | wrap(24, 24)}]

        temp_size = ${'size_hint' if function.function_name in INCLUDE_SIZE_HINT_FUNCTIONS else '0'}
        while True:
            ${instantiate_explicit_output_param(explicit_output_param)}
            size_or_code = c_func(
                ${', '.join(function_call_args) | wrap(16, 16)})
%if explicit_output_param.ctypes_data_type == 'ctypes.c_char_p':
            if is_string_buffer_too_small(size_or_code):
%else:
            if is_array_buffer_too_small(size_or_code):
%endif
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break
        self.check_for_error(size_or_code)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/library_interpreter/event_function_call.py.mako sha256=12520c4cb1cca0f5c771fd2cadc6324ebfc12d31645f03f973547cf8bcc5fa99 bytes=1936 -->
## FILE: src/codegen/templates/library_interpreter/event_function_call.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/library_interpreter/event_function_call.py.mako`
- sha256: `12520c4cb1cca0f5c771fd2cadc6324ebfc12d31645f03f973547cf8bcc5fa99`
- bytes: 1936

````mako
<%page args="function"/>\
<%
    import re
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_types,
        get_callback_func_param,
        get_callback_param_data_types,
        get_event_name,
        is_event_function,
        is_event_register_function,
        is_event_unregister_function,
    )
    from codegen.utilities.text_wrappers import wrap

    assert is_event_function(function)

    argument_types = get_argument_types(function)
    callback_func_param = get_callback_func_param(function)
    callback_param_types = get_callback_param_data_types(function)
    event_name = get_event_name(function)
    function_call_args = generate_interpreter_function_call_args(function)
%>\
        ${callback_func_param.type} = ctypes.CFUNCTYPE(
            ${', '.join(callback_param_types) | wrap(12)})

        c_func = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ${', '.join(argument_types) | wrap(24)}]

%if is_event_register_function(function):
        assert callback_function is not None
        callback_method_ptr = ${callback_func_param.type}(callback_function)
%elif is_event_unregister_function(function):
    %if "every_n_samples" in function.function_name:
        n_samples = 0
    %endif
        options = 0
        callback_method_ptr = ${callback_func_param.type}()
        callback_data = None
%endif

        error_code = c_func(
            ${', '.join(function_call_args) | wrap(12)})
        self.check_for_error(error_code)
%if is_event_register_function(function):

        return LibraryEventHandler(callback_method_ptr)
%endif
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/library_interpreter/exec_cdecl_c_function_call.py.mako sha256=5e0832cb2a5d0e349a34d7d1efbaaaaae694dcf6032f3811331a8eb5cf16a470 bytes=1478 -->
## FILE: src/codegen/templates/library_interpreter/exec_cdecl_c_function_call.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/library_interpreter/exec_cdecl_c_function_call.py.mako`
- sha256: `5e0832cb2a5d0e349a34d7d1efbaaaaae694dcf6032f3811331a8eb5cf16a470`
- bytes: 1478

````mako
<%page args="function"/>\
<%
    from codegen.utilities.interpreter_helpers import (
        generate_interpreter_function_call_args,
        get_argument_definition_lines_for_varargs,
        get_argument_types,
        get_instantiation_lines_for_varargs,
        get_varargs_parameters,
    )
    from codegen.utilities.text_wrappers import wrap, docstring_wrap

    varargs_parameters = get_varargs_parameters(function)

    ## This is under the assumption that the varargs passes are all arrays of the same size.
    varargs_array_length = f"len({varargs_parameters[0].parameter_name})"
    instantiation_lines = get_instantiation_lines_for_varargs(function)
    argument_definition_lines = get_argument_definition_lines_for_varargs(varargs_parameters)
%>\
        args = [device_name]
        argtypes: list[type] = [ctypes_byte_str]

        for index in range(${varargs_array_length}):
%for instantiation_line in instantiation_lines:
            ${instantiation_line}
%endfor

%for argument_definition_line in argument_definition_lines:
            ${argument_definition_line}
%endfor
        args.append(None)
        argtypes.append(ctypes.c_void_p)

        c_func = lib_importer.${'windll' if function.calling_convention == 'StdCall' else 'cdll'}.DAQmx${function.c_function_name}
        with c_func.arg_lock:
            c_func.argtypes = argtypes
            error_code = c_func(*args)
        self.check_for_error(error_code)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_deleter_template.py.mako sha256=c13ee9618d3255d8c3e5a6af343c7d14539585d0fa35353860acc7fd551cd8c0 bytes=1797 -->
## FILE: src/codegen/templates/property_deleter_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_deleter_template.py.mako`
- sha256: `c13ee9618d3255d8c3e5a6af343c7d14539585d0fa35353860acc7fd551cd8c0`
- bytes: 1797

````mako
<%def name="script_property_deleter(attribute)">\
<%
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name, has_attribute_with_filter
    %>\
    @${attribute.name}.deleter
    def ${attribute.name}(self):
\
## Script interpreter call.
<%
        has_advanced_timing_filter = has_attribute_with_filter(attribute,"Timing", "Advanced:Timing (Active Device)")
        generic_attribute_func = get_generic_attribute_function_name(attribute)
        if has_advanced_timing_filter:
            generic_attribute_func_ex = get_generic_attribute_function_name(attribute) + "_ex" 
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
        if attribute.python_class_name == "Watchdog":
            function_call_args.append("\"\"")
        function_call_args.append(hex(attribute.id))
        if has_advanced_timing_filter:
            function_call_args_ex = function_call_args.copy()
            function_call_args_ex.insert(1, "self._active_devs")
    %>\
    %if attribute.python_class_name == "Timing":
        %if has_advanced_timing_filter:
        if self._active_devs:
            self._interpreter.reset_${generic_attribute_func_ex}(${', '.join(function_call_args_ex)})
        else:
            self._interpreter.reset_${generic_attribute_func}(${', '.join(function_call_args)})
        %else:
        if self._active_devs:
            self._raise_device_context_not_supported_error()
        self._interpreter.reset_${generic_attribute_func}(${', '.join(function_call_args)})
        %endif
    %else:
        self._interpreter.reset_${generic_attribute_func}(${', '.join(function_call_args)})
    %endif
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_deprecated_template.py.mako sha256=7d65396d6dc9097373623aee29c554695cdd028ef9a633e93d50d66f6cbbfe90 bytes=1090 -->
## FILE: src/codegen/templates/property_deprecated_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_deprecated_template.py.mako`
- sha256: `7d65396d6dc9097373623aee29c554695cdd028ef9a633e93d50d66f6cbbfe90`
- bytes: 1090

````mako
<%def name="script_deprecated_property(attributes)">\
<%
        from codegen.utilities.attribute_helpers import get_deprecated_attributes
        deprecated_attributes = get_deprecated_attributes(attributes)
    %>\
%for old_property, attribute in deprecated_attributes.items():
    @property
    @deprecation.deprecated(deprecated_in="${attribute["deprecated_in"]}", details="Use ${attribute["new_name"]} instead.")
    def ${old_property}(self):
        return self.${attribute["new_name"]}

    %if attribute["access"] != "read":
    @${old_property}.setter
    @deprecation.deprecated(deprecated_in="${attribute["deprecated_in"]}", details="Use ${attribute["new_name"]} instead.")
    def ${old_property}(self, val):
        self.${attribute["new_name"]} = val

    %endif
    %if attribute["resettable"]:
    @${old_property}.deleter
    @deprecation.deprecated(deprecated_in="${attribute["deprecated_in"]}", details="Use ${attribute["new_name"]} instead.")
    def ${old_property}(self):
        del self.${attribute["new_name"]}

    %endif
%endfor
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_empty_getter_template.py.mako sha256=32fc263654d0bb0a13c4cf9338b2bfd92ba5e09c1351825b1b976ea5afc27f30 bytes=455 -->
## FILE: src/codegen/templates/property_empty_getter_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_empty_getter_template.py.mako`
- sha256: `32fc263654d0bb0a13c4cf9338b2bfd92ba5e09c1351825b1b976ea5afc27f30`
- bytes: 455

````mako
<%def name="script_empty_property_getter(attribute)">\
<%
        from codegen.utilities.text_wrappers import docstring_wrap
    %>\
    @property
    def ${attribute.name}(self):
        """
        ${attribute.get_return_type() + ": " + attribute.python_description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
        raise NotImplementedError(
            'Reading this NI-DAQmx property is not supported.')
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_getter_template.py.mako sha256=b0f84f3c856c947458c63e392c4ef69c13a014fb0c227b58dba57d7dbef17685 bytes=5041 -->
## FILE: src/codegen/templates/property_getter_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_getter_template.py.mako`
- sha256: `b0f84f3c856c947458c63e392c4ef69c13a014fb0c227b58dba57d7dbef17685`
- bytes: 5041

````mako
<%def name="script_property_getter(attribute)">\
<%
        from codegen.utilities.text_wrappers import docstring_wrap
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name, get_generic_attribute_function_type, has_attribute_with_filter, ATTRIBUTE_WITH_FILE_PATH_TYPE
    %>\
    %if attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
    @property
    def ${attribute.name}(self) -> pathlib.Path | None:
        """
        ${"pathlib.Path: " + attribute.python_description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
    %else:
    @property
    def ${attribute.name}(self):
        """
        ${attribute.get_return_type() + ": " + attribute.python_description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
    %endif
\
## Script interpreter call.
<%
    has_advanced_timing_filter = has_attribute_with_filter(attribute,"Timing", "Advanced:Timing (Active Device)")
    mapped_func_type = get_generic_attribute_function_type(attribute)
    generic_attribute_func = get_generic_attribute_function_name(attribute) + "_" + mapped_func_type
    if has_advanced_timing_filter:
        generic_attribute_func_ex = get_generic_attribute_function_name(attribute) + "_ex" + "_" + mapped_func_type
    object_type = attribute.object_type
    if attribute.has_alternate_constructor:
        object_type = "_" + attribute.object_type + "AlternateConstructor"
    function_call_args = []
    for handle_parameter in attribute.handle_parameters:
        function_call_args.append(handle_parameter.accessor)
    # For Watchdog related properties, empty string is passed for "lines" parameter
    if attribute.python_class_name == "Watchdog":
        function_call_args.append("\"\"")
    function_call_args.append(hex(attribute.id))
    if has_advanced_timing_filter:
        function_call_args_ex = function_call_args.copy()
        function_call_args_ex.insert(1, "self._active_devs")
%>
## For read/write string attributes in InStream and OutStream, buffer_size is passed as an argument.
%if attribute.access == "read" or attribute.access == "write":
    %if attribute.ctypes_data_type == 'ctypes.c_char_p':
        %if attribute.python_class_name in ["InStream", "OutStream"]:
<%
        function_call_args.append("buffer_size")
%>\
        buffer_size = self.get_channels_buffer_size()
\
        %endif
    %endif
%endif
\
%if attribute.python_class_name == "Timing":
    %if has_advanced_timing_filter:
        if self._active_devs:
            val = self._interpreter.get_${generic_attribute_func_ex}(${', '.join(function_call_args_ex)})
        else:
            val = self._interpreter.get_${generic_attribute_func}(${', '.join(function_call_args)})
    %else:
        if self._active_devs:
            self._raise_device_context_not_supported_error()
        val = self._interpreter.get_${generic_attribute_func}(${', '.join(function_call_args)})
    %endif
%else:
        val = self._interpreter.get_${generic_attribute_func}(${', '.join(function_call_args)})
%endif
\
## Script return call.
    %if attribute.bitfield_enum is not None:
        return enum_bitfield_to_list(
            val, ${attribute.bitfield_enum}, ${attribute.python_data_type})
    %elif attribute.is_enum and not attribute.is_list:
        return ${attribute.enum}(val)
    %elif attribute.is_enum and attribute.is_list:
        return [${attribute.enum}(e) for e in val]
    %elif attribute.is_object and not attribute.is_list:
<%
            object_constructor_args = []
            for parameter in attribute.object_constructor_params:
                object_constructor_args.append(parameter.accessor)

            object_constructor_args.append("val")
        %>\
        %if attribute.object_has_factory:
        return ${object_type}._factory(${', '.join(object_constructor_args)}, self._interpreter)
        %else:
        return ${object_type}(${', '.join(object_constructor_args)}, self._interpreter)
        %endif
    %elif attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
        return pathlib.Path(val) if val else None
    %elif attribute.is_object and attribute.is_list:
<%
            object_constructor_args = []
            for parameter in attribute.object_constructor_params:
                object_constructor_args.append(parameter.accessor)

            object_constructor_args.append('v')
        %>\
        %if attribute.object_has_factory:
        return [${object_type}._factory(${', '.join(object_constructor_args)}, self._interpreter)
                for v in unflatten_channel_string(val)]
        %else:
        return [${object_type}(${', '.join(object_constructor_args)}, self._interpreter)
                for v in unflatten_channel_string(val)]
        %endif
    %elif attribute.is_list and attribute.ctypes_data_type == 'ctypes.c_char_p':
        return unflatten_channel_string(val)
    %else:
        return val
    %endif
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_legacy_deleter_template.py.mako sha256=fbd0b8818f3674073b8ac714ac2e2c2465c7bf8b1c3eddff323c700290948044 bytes=1471 -->
## FILE: src/codegen/templates/property_legacy_deleter_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_legacy_deleter_template.py.mako`
- sha256: `fbd0b8818f3674073b8ac714ac2e2c2465c7bf8b1c3eddff323c700290948044`
- bytes: 1471

````mako
<%def name="script_property_deleter(attribute)">\
<%
        from codegen.utilities.text_wrappers import wrap
    %>\
    @${attribute.name}.deleter
    def ${attribute.name}(self):
        from nidaqmx._library_interpreter import LibraryInterpreter
        from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
        if not isinstance(self._interpreter, LibraryInterpreter):
            raise NotImplementedError
    ## When the length of the function name is too long, it will be wrapped to the next line
    %if len(attribute.c_function_name) < 33:
        c_func = lib_importer.${attribute.get_lib_importer_type()}.DAQmxReset${attribute.c_function_name}
    %else:
        c_func = (lib_importer.${attribute.get_lib_importer_type()}.
                 DAQmxReset${attribute.c_function_name})
    %endif
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ${', '.join(attribute.get_handle_parameter_arguments()) | wrap(initial_indent=24)}]
\
## Script function call.
<%
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
    %>\
        error_code = c_func(
            ${', '.join(function_call_args) | wrap(initial_indent=12)})
        self._interpreter.check_for_error(error_code)
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_legacy_setter_template.py.mako sha256=99ff732489a71fe6141d453a29574abf41be5f8857de7700331202089a6852e8 bytes=3259 -->
## FILE: src/codegen/templates/property_legacy_setter_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_legacy_setter_template.py.mako`
- sha256: `99ff732489a71fe6141d453a29574abf41be5f8857de7700331202089a6852e8`
- bytes: 3259

````mako
<%def name="script_property_setter(attribute)">\
<%
        from codegen.utilities.text_wrappers import wrap, docstring_wrap
    %>\
    @${attribute.name}.setter
    def ${attribute.name}(self, val):
\
        from nidaqmx._library_interpreter import LibraryInterpreter
        from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
        if not isinstance(self._interpreter, LibraryInterpreter):
            raise NotImplementedError
    %if attribute.bitfield_enum is not None:
        val = enum_list_to_bitfield(
            val, ${attribute.bitfield_enum})
    %elif attribute.is_enum and not attribute.is_list:
        val = val.value
    %elif attribute.is_enum and attribute.is_list:
        val = numpy.array([e.value for e in val], dtype=${attribute.ctypes_data_type})
    %elif attribute.is_object and not attribute.is_list:
        val = val.name
    %elif attribute.is_object and attribute.is_list:
        val = flatten_channel_string[o.name for o in val]
    %elif attribute.is_list and attribute.ctypes_data_type == 'ctypes.c_char_p':
        val = flatten_channel_string(val)
    %elif attribute.is_list:
        val = numpy.array(val, dtype=${attribute.ctypes_data_type})
    %endif
\
<%
        argtypes = []
        for handle_parameter in attribute.handle_parameters:
            if handle_parameter.ctypes_data_type == 'ctypes.c_char_p':
                argtypes.append('ctypes_byte_str')
            else:
                argtypes.append(handle_parameter.ctypes_data_type)
        if (attribute.is_list and attribute.ctypes_data_type != 'ctypes.c_char_p' and
                attribute.bitfield_enum is None):
            argtypes.append("wrapped_ndpointer(dtype={}, flags=('C','W'))"
                            .format(attribute.ctypes_data_type))
        elif attribute.ctypes_data_type == 'ctypes.c_char_p':
            argtypes.append('ctypes_byte_str')
        else:
            argtypes.append(attribute.ctypes_data_type)
        if attribute.has_explicit_write_buffer_size:
            argtypes.append('ctypes.c_uint')
    %>\
    ## When the length of the function name is too long, it will be wrapped to the next line
    %if len(attribute.c_function_name) < 33:
        c_func = lib_importer.${attribute.get_lib_importer_type()}.DAQmxSet${attribute.c_function_name}
    %else:
        c_func = (lib_importer.${attribute.get_lib_importer_type()}.
                 DAQmxSet${attribute.c_function_name})
    %endif
        if c_func.argtypes is None:
            with c_func.arg_lock:
                if c_func.argtypes is None:
                    c_func.argtypes = [
                        ${', '.join(argtypes) | wrap(initial_indent=24)}]
\
## Script function call.
<%
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
        function_call_args.append('val')
        if attribute.has_explicit_write_buffer_size:
            function_call_args.append('len(val)')
    %>\
        error_code = c_func(
            ${', '.join(function_call_args) | wrap(initial_indent=12)})
        self._interpreter.check_for_error(error_code)
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_setter_template.py.mako sha256=6ab24f6dd4fd6706118cbbae6af65062777a90948d0ad496c489825b370c7b5d bytes=3094 -->
## FILE: src/codegen/templates/property_setter_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_setter_template.py.mako`
- sha256: `6ab24f6dd4fd6706118cbbae6af65062777a90948d0ad496c489825b370c7b5d`
- bytes: 3094

````mako
<%def name="script_property_setter(attribute)">\
<%
        from codegen.utilities.attribute_helpers import get_generic_attribute_function_name, get_generic_attribute_function_type, has_attribute_with_filter, ATTRIBUTE_WITH_FILE_PATH_TYPE
    %>\
    @${attribute.name}.setter
    %if attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
    def ${attribute.name}(self, val: str | pathlib.PurePath | None):
    %else:
    def ${attribute.name}(self, val):
    %endif
\
    %if attribute.bitfield_enum is not None:
        val = enum_list_to_bitfield(
            val, ${attribute.bitfield_enum})
    %elif attribute.is_enum and not attribute.is_list:
        val = val.value
    %elif attribute.is_enum and attribute.is_list:
        val = numpy.array([e.value for e in val], dtype=${attribute.ctypes_data_type})
    %elif attribute.is_object and not attribute.is_list:
        val = val.name
    %elif attribute.is_object and attribute.is_list:
        val = flatten_channel_string[o.name for o in val]
    %elif attribute.is_list and attribute.ctypes_data_type == 'ctypes.c_char_p':
        val = flatten_channel_string(val)
    %elif attribute.is_list:
        val = numpy.array(val, dtype=${attribute.ctypes_data_type})
    %elif attribute.name in ATTRIBUTE_WITH_FILE_PATH_TYPE:
        if val is None:
            val = ""
        val = str(val)
    %endif
\
## Script interpreter call.
<%
        has_advanced_timing_filter = has_attribute_with_filter(attribute,"Timing", "Advanced:Timing (Active Device)")
        mapped_func_type = get_generic_attribute_function_type(attribute)
        generic_attribute_func = get_generic_attribute_function_name(attribute) + "_" + mapped_func_type
        if has_advanced_timing_filter:
            generic_attribute_func_ex = get_generic_attribute_function_name(attribute) + "_ex" + "_" + mapped_func_type
        function_call_args = []
        for handle_parameter in attribute.handle_parameters:
            function_call_args.append(handle_parameter.accessor)
        if attribute.python_class_name == "Watchdog":
            function_call_args.append("\"\"")
        function_call_args.append(hex(attribute.id))
        function_call_args.append('val')
        if has_advanced_timing_filter:
            function_call_args_ex = function_call_args.copy()
            function_call_args_ex.insert(1, "self._active_devs")
    %>\
    %if attribute.python_class_name == "Timing":
        %if has_advanced_timing_filter:
        if self._active_devs:
            self._interpreter.set_${generic_attribute_func_ex}(${', '.join(function_call_args_ex)})
        else:
            self._interpreter.set_${generic_attribute_func}(${', '.join(function_call_args)})
        %else:
        if self._active_devs:
            self._raise_device_context_not_supported_error()
        self._interpreter.set_${generic_attribute_func}(${', '.join(function_call_args)})
        %endif
    %else:
        self._interpreter.set_${generic_attribute_func}(${', '.join(function_call_args)})
    %endif
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/property_template.py.mako sha256=07449f79b1a8ac8447b70f96a0a1b8d8aba4f8c98200f6ddd52ee95aa40b9c9b bytes=1589 -->
## FILE: src/codegen/templates/property_template.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/property_template.py.mako`
- sha256: `07449f79b1a8ac8447b70f96a0a1b8d8aba4f8c98200f6ddd52ee95aa40b9c9b`
- bytes: 1589

````mako
<%def name="script_property(attribute)">\
<%namespace name="property_getter_template" file="/property_getter_template.py.mako"/>\
<%namespace name="property_empty_getter_template" file="/property_empty_getter_template.py.mako"/>\
<%namespace name="property_setter_template" file="/property_setter_template.py.mako"/>\
<%namespace name="property_deleter_template" file="/property_deleter_template.py.mako"/>\
<%namespace name="property_legacy_setter_template" file="/property_legacy_setter_template.py.mako"/>\
<%namespace name="property_legacy_deleter_template" file="/property_legacy_deleter_template.py.mako"/>\
    %if attribute.access == "read":
${property_getter_template.script_property_getter(attribute)}
    %elif attribute.access == "write":
${property_empty_getter_template.script_empty_property_getter(attribute)}
${property_setter_template.script_property_setter(attribute)}
    %elif attribute.access == "read-write" and attribute.python_class_name == "PhysicalChannel":
${property_getter_template.script_property_getter(attribute)}
${property_legacy_setter_template.script_property_setter(attribute)}
    %elif attribute.access == "read-write":
${property_getter_template.script_property_getter(attribute)}
${property_setter_template.script_property_setter(attribute)}
    %endif
\
    %if attribute.resettable and attribute.python_class_name == "PhysicalChannel":
${property_legacy_deleter_template.script_property_deleter(attribute)}
    %elif attribute.resettable:
${property_deleter_template.script_property_deleter(attribute)}
    %endif
</%def>
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/scale.py.mako sha256=d3fc8898868c56426f2284166cb91dd6c10897d70cc6fdd8265a57542894fcf7 bytes=15710 -->
## FILE: src/codegen/templates/scale.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/scale.py.mako`
- sha256: `d3fc8898868c56426f2284166cb91dd6c10897d70cc6fdd8265a57542894fcf7`
- bytes: 15710

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "Scale")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import numpy

from nidaqmx import utils
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})

__all__ = ['Scale']


class Scale:
    """
    Represents a DAQmx scale.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the scale to create.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'Scale(name={self._name})'

    @property
    def name(self):
        """
        str: Specifies the name of this scale.
        """
        return self._name

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    @staticmethod
    def calculate_reverse_poly_coeff(
            forward_coeffs, min_val_x=-5.0, max_val_x=5.0,
            num_points_to_compute=1000, reverse_poly_order=-1, *, grpc_options=None):
        """
        Computes a set of coefficients for a polynomial that
        approximates the inverse of the polynomial with the coefficients
        you specify with the "forward_coeffs" input. This function
        generates a table of x versus y values over the range of x. This
        function then finds a polynomial fit, using the least squares
        method to compute a polynomial that computes x when given a
        value for y.

        Args:
            forward_coeffs (List[float]): Is the list of coefficients
                for the polynomial that computes y given a value of x.
                Each element of the list corresponds to a term of the
                equation.
            min_val_x (Optional[float]): Is the minimum value of x for
                which you use the polynomial. This is the smallest value
                of x for which the function generates a y value in the
                table.
            max_val_x (Optional[float]): Is the maximum value of x for
                which you use the polynomial. This is the largest value
                of x for which the function generates a y value in the
                table.
            num_points_to_compute (Optional[int]): Is the number of
                points in the table of x versus y values. The function
                spaces the values evenly between "min_val_x" and
                "max_val_x".
            reverse_poly_order (Optional[int]): Is the order of the
                reverse polynomial to compute. For example, an input of
                3 indicates a 3rd order polynomial. A value of -1
                indicates a reverse polynomial of the same order as the
                forward polynomial.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            List[float]:

            Specifies the list of coefficients for the reverse
            polynomial. Each element of the list corresponds to a term
            of the equation. For example, if index three of the list is
            9, the fourth term of the equation is 9y^3.
        """
        forward_coeffs = numpy.array(forward_coeffs, dtype=numpy.float64)

        interpreter = utils._select_interpreter(grpc_options)

        reverse_coeffs = interpreter.calculate_reverse_poly_coeff(
            forward_coeffs, min_val_x, max_val_x, num_points_to_compute, reverse_poly_order)

        return reverse_coeffs

    @staticmethod
    def create_lin_scale(
            scale_name, slope, y_intercept=0.0,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that uses the equation y=mx+b, where x is
        a pre-scaled value, and y is a scaled value. The equation is
        identical for input and output. If the equation is in the form
        x=my+b, you must first solve for y in terms of x.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            slope (float): Is the slope, m, in the equation.
            y_intercept (Optional[float]): Is the y-intercept, b, in the
                equation.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_lin_scale(
            scale_name, slope, y_intercept, pre_scaled_units.value, scaled_units)

        return scale

    @staticmethod
    def create_map_scale(
            scale_name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that scales values proportionally from a
        range of pre-scaled values to a range of scaled values.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            prescaled_min (float): Is the smallest value in the range of
                pre-scaled values. NI-DAQmx maps this value to
                "scaled_min".
            prescaled_max (float): Is the largest value in the range of
                pre-scaled values. NI-DAQmx maps this value to
                "scaled_max".
            scaled_min (float): Is the smallest value in the range of
                scaled values. NI-DAQmx maps this value to
                "prescaled_min". Read operations clip samples that are
                smaller than this value. Write operations generate
                errors for samples that are smaller than this value.
            scaled_max (float): Is the largest value in the range of
                scaled values. NI-DAQmx maps this value to
                "prescaled_max". Read operations clip samples that are
                larger than this value. Write operations generate errors
                for samples that are larger than this value.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        """
        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_map_scale(
            scale_name, prescaled_min, prescaled_max, scaled_min, scaled_max,
            pre_scaled_units.value, scaled_units)

        return scale

    @staticmethod
    def create_polynomial_scale(
            scale_name, forward_coeffs, reverse_coeffs,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that uses an nth order polynomial
        equation. NI-DAQmx requires both a polynomial to convert pre-
        scaled values to scaled values (forward) and a polynomial to
        convert scaled values to pre-scaled values (reverse). If you
        only know one set of coefficients, use the DAQmx Compute Reverse
        Polynomial Coefficients function to generate the other set.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            forward_coeffs (List[float]): Is an list of coefficients for
                the polynomial that converts pre-scaled values to scaled
                values. Each element of the list corresponds to a term
                of the equation.
            reverse_coeffs (List[float]): Is an list of coefficients for
                the polynomial that converts scaled values to pre-scaled
                values. Each element of the list corresponds to a term
                of the equation.
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        """
        if forward_coeffs is None:
            forward_coeffs = []

        if reverse_coeffs is None:
            reverse_coeffs = []

        forward_coeffs = numpy.array(forward_coeffs, dtype=numpy.float64)
        reverse_coeffs = numpy.array(reverse_coeffs, dtype=numpy.float64)

        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_polynomial_scale(
            scale_name, forward_coeffs, reverse_coeffs, pre_scaled_units.value, scaled_units)

        return scale

    @staticmethod
    def create_table_scale(
            scale_name, prescaled_vals, scaled_vals,
            pre_scaled_units=UnitsPreScaled.VOLTS, scaled_units=None, *, grpc_options=None):
        """
        Creates a custom scale that maps an list of pre-scaled values to
        an list of corresponding scaled values. NI-DAQmx applies linear
        interpolation to values that fall between the values in the
        table. Read operations clip scaled samples that are outside the
        maximum and minimum scaled values found in the table. Write
        operations generate errors for samples that are outside the
        minimum and maximum scaled values found in the table.

        Args:
            scale_name (str): Specifies the name of the scale to create.
            prescaled_vals (List[float]): Is the list of pre-scaled
                values that map to the values in "scaled_vals".
            scaled_vals (List[float]): Is the list of scaled values that
                map to the values in "prescaled_vals".
            pre_scaled_units (Optional[nidaqmx.constants.UnitsPreScaled]):
                Is the units of the values to scale.
            scaled_units (Optional[str]): Is the units to use for the
                scaled value. You can use an arbitrary string. NI-DAQmx
                uses the units to label a graph or chart.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.scale.Scale:

            Indicates an object that represents the created custom scale.
        """
        if prescaled_vals is None:
            prescaled_vals = []

        if scaled_vals is None:
            scaled_vals = []

        prescaled_vals = numpy.array(prescaled_vals, dtype=numpy.float64)
        scaled_vals = numpy.array(scaled_vals, dtype=numpy.float64)

        scale = Scale(scale_name, grpc_options=grpc_options)

        scale._interpreter.create_table_scale(
            scale_name, prescaled_vals, scaled_vals, pre_scaled_units.value, scaled_units)

        return scale

    def save(self, save_as="", author="", overwrite_existing_scale=False,
             allow_interactive_editing=True, allow_interactive_deletion=True):
        """
        Saves this custom scale to MAX.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            options (Optional[int]): Specifies whether to allow the
                task, global channel, or custom scale to be deleted
                through MAX.
            overwrite_existing_scale (Optional[bool]): Specifies whether to
                overwrite a custom scale of the same name if one is already
                saved in MAX. If this input is False and a custom scale of
                the same name is already saved in MAX, this function returns
                an error.
            allow_interactive_editing (Optional[bool]): Specifies whether to
                allow the task, global channel, or custom scale to be edited
                in the DAQ Assistant. If allow_interactive_editing is True,
                the DAQ Assistant must support all task or global channel
                settings.
            allow_interactive_deletion (Optional[bool]): Specifies whether
                to allow the task, global channel, or custom scale to be
                deleted through MAX.
        """
        options = 0
        if overwrite_existing_scale:
            options |= _Save.OVERWRITE.value
        if allow_interactive_editing:
            options |= _Save.ALLOW_INTERACTIVE_EDITING.value
        if allow_interactive_deletion:
            options |= _Save.ALLOW_INTERACTIVE_DELETION.value

        self._interpreter.save_scale(self._name, save_as, author, options)


class _ScaleAlternateConstructor(Scale):
    """
    Provide an alternate constructor for the Scale object.

    This is a private API used to instantiate a Scale with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = ()

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the Scale.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to Scale,
        # so the user isn't confused when doing introspection.
        self.__class__ = Scale  # type: ignore[assignment]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/system/_watchdog_modules/expiration_state.py.mako sha256=c65882ebc59aaeae8d3f887a905472449bbc7a9fe51ce1d3481e4af57eda9cc9 bytes=1533 -->
## FILE: src/codegen/templates/system/_watchdog_modules/expiration_state.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/system/_watchdog_modules/expiration_state.py.mako`
- sha256: `c65882ebc59aaeae8d3f887a905472449bbc7a9fe51ce1d3481e4af57eda9cc9`
- bytes: 1533

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "ExpirationState")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import deprecation

from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class ExpirationState:
    """
    Represents a DAQmx Watchdog expiration state.
    """
    __slots__ = ('_handle', '_physical_channel', '_interpreter')

    def __init__(self, task_handle, physical_channel, interpreter):
        self._handle = task_handle
        self._physical_channel = physical_channel        
        self._interpreter = interpreter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    self._physical_channel == other._physical_channel)
        return False

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle) ^ hash(self._physical_channel)

    def __ne__(self, other):
        return not self.__eq__(other)

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/system/device.py.mako sha256=3c9cc86375d16f887ea7f5bc01738b6824e2439a1dde660356bc7d7adc9d4db9 bytes=11498 -->
## FILE: src/codegen/templates/system/device.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/system/device.py.mako`
- sha256: `3c9cc86375d16f887ea7f5bc01738b6824e2439a1dde660356bc7d7adc9d4db9`
- bytes: 11498

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "Device")
    functions = get_functions(data,"Device")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import deprecation
import numpy

from datetime import datetime
from nidaqmx import utils
from nidaqmx._bitfield_utils import enum_bitfield_to_list
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.system._collections.physical_channel_collection import (
    AIPhysicalChannelCollection, AOPhysicalChannelCollection,
    CIPhysicalChannelCollection, COPhysicalChannelCollection,
    DILinesCollection, DIPortsCollection, DOLinesCollection, DOPortsCollection)
from nidaqmx.types import IDPinContents
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif

__all__ = ['Device']


class Device:
    """
    Represents a DAQmx device.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the device.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'Device(name={self._name})'

    @property
    def name(self):
        """
        str: Specifies the name of this device.
        """
        return self._name

    # region Physical Channel Collections

    @property
    def ai_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the analog input
            physical channels available on the device.
        """
        return AIPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def ao_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the analog output
            physical channels available on the device.
        """
        return AOPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def ci_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter input
            physical channels available on the device.
        """
        return CIPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def co_physical_chans(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the counter output
            physical channels available on the device.
        """
        return COPhysicalChannelCollection(self._name, self._interpreter)

    @property
    def di_lines(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            lines available on the device.
        """
        return DILinesCollection(self._name, self._interpreter)

    @property
    def di_ports(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital input
            ports available on the device.
        """
        return DIPortsCollection(self._name, self._interpreter)

    @property
    def do_lines(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            lines available on the device.
        """
        return DOLinesCollection(self._name, self._interpreter)

    @property
    def do_ports(self):
        """
        List[nidaqmx.system._collections.PhysicalChannelCollection]:
            Indicates a collection that contains all the digital output
            ports available on the device.
        """
        return DOPortsCollection(self._name, self._interpreter)

    # endregion

    # region Calibration Info property

    @property
    def ext_cal_last_date_and_time(self):
        """
        datetime: Indicates the last date and time that the device underwent an
        external calibration.
        """

        last_date_and_time = self._interpreter.get_ext_cal_last_date_and_time(self._name)

        return datetime(
            year=last_date_and_time[0],
            month=last_date_and_time[1],
            day=last_date_and_time[2],
            hour=last_date_and_time[3],
            minute=last_date_and_time[4]
        )

    @property
    def self_cal_last_date_and_time(self):
        """
        datetime: Indicates the last date and time that the device underwent a
        self-calibration.
        """

        last_date_and_time = self._interpreter.get_self_cal_last_date_and_time(self._name)

        return datetime(
            year=last_date_and_time[0],
            month=last_date_and_time[1],
            day=last_date_and_time[2],
            hour=last_date_and_time[3],
            minute=last_date_and_time[4]
        )

    @property
    def device_supports_cal(self):
        """
        Indicates if the device supports calibration.
        """

        return self._interpreter.device_supports_cal(self._name)

    # endregion

    # region ID Pin Hand-written Attributes

    @property
    def id_pin_mem_serial_nums(self):
        """
        List[str]: Indicates the serial number of the memory connected
            to each ID Pin. Each list element corresponds to an ID Pin.
            The list contains an empty string for each ID Pin with no
            memory connected.
        """

        val = self._interpreter.get_device_attribute_string(self._name, 0x31f4)
        return [v.strip() for v in val.split(',')]

    # endregion

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
\
    # region ID Pin Hand-written Functions

    def read_id_pin_memory(self, id_pin_name):
        """
        Reads and returns the data stored in the memory attached to the
        specified ID Pin.

        Args:
            id_pin_name (str): Is the name of the ID Pin to access (ex:
                id0)

        Returns:
            nidaqmx.types.IDPinContents:

            Contains the data read from the memory and the format code.
        """
        data, data_length_read, format_code = self._interpreter.read_id_pin_memory(
            self._name, id_pin_name)

        data = data[:data_length_read]

        return IDPinContents(data, format_code)

    # endregion

    # region Network Device Functions

    @staticmethod
    def add_network_device(
            ip_address, device_name="", attempt_reservation=False,
            timeout=10.0, *, grpc_options=None):
        """
        Adds a Network cDAQ device to the system and, if specified,
        attempts to reserve it.

        Args:
            ip_address (str): Specifies the string containing the IP
                address (in dotted decimal notation) or hostname of the
                device to add to the system.
            device_name (Optional[str]): Indicates the name to assign to
                the device. If unspecified, NI-DAQmx chooses the device
                name.
            attempt_reservation (Optional[bool]): Indicates if a
                reservation should be attempted after the device is
                successfully added. By default, this parameter is set to
                False.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        Returns:
            nidaqmx.system.device.Device:

            Specifies the object that represents the device this
            operation applied to.
        """
        device = Device("", grpc_options=grpc_options)

        device._name = device._interpreter.add_network_device(
            ip_address, device_name, attempt_reservation, timeout)

        return device

    def delete_network_device(self):
        """
        Deletes a Network DAQ device previously added to the host. If
        the device is reserved, it is unreserved before it is removed.
        """

        self._interpreter.delete_network_device(self._name)

    def reserve_network_device(self, override_reservation=None):
        """
        Reserves the Network DAQ device for the current host.
        Reservation is required to run NI-DAQmx tasks, and the device
        must be added in MAX before it can be reserved.

        Args:
            override_reservation (Optional[bool]): Indicates if an
                existing reservation on the device should be overridden
                by this reservation. By default, this parameter is set
                to false.
        """

        self._interpreter.reserve_network_device(self._name, override_reservation)

    def unreserve_network_device(self):
        """
        Unreserves or releases a Network DAQ device previously reserved
        by the host.
        """

        self._interpreter.unreserve_network_device(self._name)

    # endregion

class _DeviceAlternateConstructor(Device):
    """
    Provide an alternate constructor for the Device object.

    This is a private API used to instantiate a Device with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = ()

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the Device.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to Device,
        # so the user isn't confused when doing introspection.
        self.__class__ = Device  # type: ignore[assignment]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/system/physical_channel.py.mako sha256=969a732f8bd96f6aa5c360d82fd0b729cb1202ba31c1527115aecd1bb21def8d bytes=3338 -->
## FILE: src/codegen/templates/system/physical_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/system/physical_channel.py.mako`
- sha256: `969a732f8bd96f6aa5c360d82fd0b729cb1202ba31c1527115aecd1bb21def8d`
- bytes: 3338

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used as function_enums
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used as attribute_enums
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data, "PhysicalChannel")
    functions = get_functions(data,"PhysicalChannel")
    attr_enums = attribute_enums(attributes)
    func_enums = function_enums(functions)
    enums_used = get_enums_to_import(attr_enums, func_enums)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations

import ctypes
import numpy
import pathlib

from nidaqmx import utils
from nidaqmx._bitfield_utils import enum_bitfield_to_list
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif

from typing import Optional, Union

__all__ = ['PhysicalChannel']


class PhysicalChannel:
    """
    Represents a DAQmx physical channel.
    """
    __slots__ = ['_name', '_interpreter', '__weakref__']

    def __init__(self, name, *, grpc_options=None):
        """
        Args:
            name (str): Specifies the name of the physical channel.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._name = name
        self._interpreter = utils._select_interpreter(grpc_options)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'PhysicalChannel(name={self._name})'

    @property
    def name(self):
        """
        str: Specifies the name of this physical channel.
        """
        return self._name

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor


class _PhysicalChannelAlternateConstructor(PhysicalChannel):
    """
    Provide an alternate constructor for the PhysicalChannel object.

    This is a private API used to instantiate a PhysicalChannel with an existing interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = ()

    def __init__(self, name, interpreter):
        """
        Args:
            name: Specifies the name of the Physical Channel.
            interpreter: Specifies the interpreter instance.

        """
        self._name = name
        self._interpreter = interpreter

        # Use meta-programming to change the type of this object to PhysicalChannel,
        # so the user isn't confused when doing introspection.
        self.__class__ = PhysicalChannel  # type: ignore[assignment]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/system/system.py.mako sha256=9070686edc11ae4536420698d30dfca3b09c1bb337abb27066aae033addef939 bytes=23889 -->
## FILE: src/codegen/templates/system/system.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/system/system.py.mako`
- sha256: `9070686edc11ae4536420698d30dfca3b09c1bb337abb27066aae033addef939`
- bytes: 23889

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    functions = get_functions(data,"System")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations

import collections
import ctypes
import deprecation
import numpy
import typing

from nidaqmx import utils
from nidaqmx.system._collections.device_collection import DeviceCollection
from nidaqmx.system._collections.persisted_channel_collection import (
    PersistedChannelCollection)
from nidaqmx.system._collections.persisted_scale_collection import (
    PersistedScaleCollection)
from nidaqmx.system._collections.persisted_task_collection import (
    PersistedTaskCollection)
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string
from nidaqmx.constants import (
    AOPowerUpOutputBehavior, LogicFamily, PowerUpChannelType, PowerUpStates, ResistorState,
    SignalModifiers, WAIT_INFINITELY)
from nidaqmx.types import (
    AOPowerUpState, CDAQSyncConnection, DOPowerUpState, DOResistorPowerUpState)
import nidaqmx.types
from nidaqmx.system.device import _DeviceAlternateConstructor

if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias

__all__ = ['System']


class System:
    """
    Represents a DAQmx system.

    Contains static properties that access tasks, scales, and global channels
    stored in Measurement Automation Explorer (MAX), performs immediate
    operations on DAQ hardware, and creates classes from which you can get
    information about the hardware.
    """
    __slots__ = ('_interpreter')

    def __init__(self, grpc_options=None):
        """
        Args:
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        self._interpreter = utils._select_interpreter(grpc_options)

    @staticmethod
    def local():
        """
        nidaqmx.system.system.System: Represents the local DAQmx system.
        """
        return System()

    @staticmethod
    def remote(grpc_options):
        """
        nidaqmx.system.system.System: Represents the remote DAQmx system.

        Args:
            grpc_options (:class:`~nidaqmx.GrpcSessionOptions`): Specifies
                the gRPC session options.
        """
        return System(grpc_options)

    @property
    def devices(self):
        """
        nidaqmx.system._collections.DeviceCollection: Indicates the
            collection of devices for this DAQmx system.
        """
        return DeviceCollection(self._interpreter)


    DriverVersion: TypeAlias = nidaqmx.types.DriverVersion

    @property
    def driver_version(self):
        """
        collections.namedtuple: Indicates the major, minor and update
            portions of the installed version of NI-DAQmx.

            - major_version (int): Indicates the major portion of the
              installed version of NI-DAQmx, such as 7 for version 7.0.
            - minor_version (int): Indicates the minor portion of the
              installed version of NI-DAQmx, such as 0 for version 7.0.
            - update_version (int): Indicates the update portion of the
              installed version of NI-DAQmx, such as 1 for version 9.0.1.
        """
        return nidaqmx.types.DriverVersion(self._major_version, self._minor_version,
                                           self._update_version)

    @property
    def global_channels(self):
        """
        nidaqmx.system._collections.PersistedChannelCollection: Indicates
            the collection of global channels for this DAQmx system.
        """
        return PersistedChannelCollection(self._interpreter)

    @property
    def scales(self):
        """
        nidaqmx.system._collections.PersistedScaleCollection: Indicates
            the collection of custom scales for this DAQmx system.
        """
        return PersistedScaleCollection(self._interpreter)

    @property
    def tasks(self):
        """
        nidaqmx.system._collections.PersistedTaskCollection: Indicates
            the collection of saved tasks for this DAQmx system.
        """
        return PersistedTaskCollection(self._interpreter)

    @property
    def _major_version(self):
        """
        int: Indicates the major portion of the installed version of NI-
            DAQmx, such as 7 for version 7.0.
        """
        val = self._interpreter.get_system_info_attribute_uint32(0x1272)
        return val

    @property
    def _minor_version(self):
        """
        int: Indicates the minor portion of the installed version of NI-
            DAQmx, such as 0 for version 7.0.
        """
        val = self._interpreter.get_system_info_attribute_uint32(0x1923)
        return val

    @property
    def _update_version(self):
        """
        int: Indicates the update portion of the installed version of
            NI-DAQmx, such as 1 for version 9.0.1.
        """
        val = self._interpreter.get_system_info_attribute_uint32(0x2f22)
        return val

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
\
    # region Power Up States Functions

    def set_digital_power_up_states(
            self, device_name, power_up_states):
        """
        Updates power up states for digital physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.DOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the digital line or
                  port to modify. You cannot modify dedicated digital
                  input lines.
                - power_up_state (:class:`nidaqmx.constants.PowerUpStates`):
                  Specifies the power up state to set for the physical
                  channel specified with the **physical_channel** input.
        """
        channel_names = []
        states = []

        for p in power_up_states:
            channel_names.append(p.physical_channel)
            states.append(p.power_up_state.value)

        self._interpreter.set_digital_power_up_states(device_name, channel_names, states)

    def get_digital_power_up_states(self, device_name):
        """
        Gets the power up states for digital physical lines.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            List[nidaqmx.types.DOPowerUpState]:

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the power
            up state set for that physical channel.

            - physical_channel (str): Indicates the physical channel that
              was modified.
            - power_up_state (:class:`nidaqmx.constants.PowerUpStates`):
              Indicates the power up state set for the physical channel
              specified with the **physical_channel** output.
        """
        device = _DeviceAlternateConstructor(device_name, self._interpreter)
        channel_names = []

        for do_line in device.do_lines:
            channel_names.append(do_line.name)

        states = self._interpreter.get_digital_power_up_states(device_name, channel_names)

        power_up_states = []
        for d, p in zip(device.do_lines, states):
            power_up_states.append(
                DOPowerUpState(physical_channel=d.name,
                               power_up_state=PowerUpStates(p)))

        return power_up_states

    def set_digital_pull_up_pull_down_states(
            self, device_name, power_up_states):
        """
        Sets the resistor level to pull up or pull down for lines when
        they are in tristate logic.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.DOResistorPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the digital line or
                  port to modify.  You cannot modify dedicated digital
                  input lines.
                - power_up_state (:class:`nidaqmx.constants.ResistorState`):
                  Specifies the power up state to set for the physical
                  channel specified with the **physical_channel** input.
        """
        channel_names = []
        states = []

        for p in power_up_states:
            channel_names.append(p.physical_channel)
            states.append(p.power_up_state.value)

        self._interpreter.set_digital_pull_up_pull_down_states(device_name, channel_names, states)

    def get_digital_pull_up_pull_down_states(self, device_name):
        """
        Gets the resistor level for lines when they are in tristate
        logic.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            List[nidaqmx.types.DOResistorPowerUpState]:

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the power
            up state set for that physical channel.

            - physical_channel (str): Indicates the physical channel that
              was modified.
            - power_up_state (:class:`nidaqmx.constants.ResistorState`):
              Indicates the power up state set for the physical channel
              specified with the **physical_channel** output.
        """
        channel_names = []
        states = []

        device = _DeviceAlternateConstructor(device_name, self._interpreter)

        for do_line in device.do_lines:
            channel_names.append(do_line.name)

        states =  self._interpreter.get_digital_pull_up_pull_down_states(device_name, channel_names)

        power_up_states = []
        for d, p in zip(device.do_lines, states):
            power_up_states.append(
                DOResistorPowerUpState(
                    physical_channel=d.name,
                    power_up_state=ResistorState(p)))

        return power_up_states

    @deprecation.deprecated(deprecated_in="0.8.0", details="Use set_analog_power_up_states_with_output_type instead.")
    def set_analog_power_up_states(self, device_name, power_up_states):
        """
        Updates power up states for analog physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            power_up_states (List[nidaqmx.types.AOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the physical channel
                  to modify.
                - power_up_state (float): Specifies the power up state to
                  set for the physical channel specified with the
                  **physical_channel** input.
                - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
                  Specifies the output type for the physical channel
                  specified with the **physical_channel** input.
        """
        channel_names = []
        states = []
        channel_types = []

        for p in power_up_states:
            channel_names.append(p.physical_channel)
            states.append(p.power_up_state)
            channel_types.append(p.channel_type.value)

        self._interpreter.set_analog_power_up_states(device_name, channel_names, states, channel_types)

    def set_analog_power_up_states_with_output_type(
            self, power_up_states):
        """
        Updates power up states for analog physical channels.

        Args:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):
                Contains the physical channels and power up states to
                set. Each element of the list contains a physical channel
                and the power up state to set for that physical channel.

                - physical_channel (str): Specifies the physical channel to
                  modify.
                - power_up_state (float): Specifies the power up state
                  to set for the physical channel specified with the
                  **physical_channel** input.
                - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
                  Specifies the output type for the physical channel
                  specified with the **physical_channel** input.
        """
        physical_channel = flatten_channel_string(
            [p.physical_channel for p in power_up_states])
        state = numpy.array(
            [p.power_up_state for p in power_up_states], dtype=numpy.float64)
        channel_type = numpy.array(
            [p.channel_type.value for p in power_up_states], dtype=numpy.int32)

        self._interpreter.set_analog_power_up_states_with_output_type(physical_channel, state, channel_type)

    @deprecation.deprecated(deprecated_in="0.8.0", details="Use get_analog_power_up_states_with_output_type instead.")
    def get_analog_power_up_states(self, device_name):
        """
        Gets the power up states for analog physical channels.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the
            power up state set for that physical channel.

            - physical_channel (str): Specifies the physical channel that
              was modified.
            - power_up_state (float): Specifies the power up state set
              for the physical channel specified with the
              **physical_channel** input.
            - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
              Specifies the output type for the physical channel
              specified with the **physical_channel** input.
        """
        device = _DeviceAlternateConstructor(device_name, self._interpreter)
        channel_names = device.ao_physical_chans.channel_names
        
        # Here get_analog_power_up_states is not called, since it is deprecated and passes channel_type in wrong direction
        return self.get_analog_power_up_states_with_output_type(channel_names)

    def get_analog_power_up_states_with_output_type(self, physical_channels):
        """
        Gets the power up states for analog physical channels.

        Args:
            physical_channels (List[str]): Indicates the physical
                channels that were modified.
        Returns:
            power_up_states (List[nidaqmx.types.AOPowerUpState]):

            Contains the physical channels and power up states set. Each
            element of the list contains a physical channel and the
            power up state set for that physical channel.

            - physical_channel (str): Specifies the physical channel that
              was modified.
            - power_up_state (float): Specifies the power up state set
              for the physical channel specified with the
              **physical_channel** input.
            - channel_type (:class:`nidaqmx.constants.AOPowerUpOutputBehavior`):
              Specifies the output type for the physical channel
              specified with the **physical_channel** input.
        """
        states, channel_types = self._interpreter.get_analog_power_up_states_with_output_type(
            flatten_channel_string(physical_channels), len(physical_channels))
        
        assert len(states) == len(physical_channels)
        assert len(channel_types) == len(physical_channels)

        power_up_states = []
        for p, s, c in zip(physical_channels, states, channel_types):
            power_up_states.append(
                AOPowerUpState(
                    physical_channel=p,
                    power_up_state=float(s),
                    channel_type=PowerUpChannelType(c)))

        return power_up_states

    def set_digital_logic_family_power_up_state(
            self, device_name, logic_family):
        """
        Sets the digital logic family to use when the device powers up.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
            logic_family (nidaqmx.constants.LogicFamily): Specifies the
                logic family set to the device to when it powers up. A
                logic family corresponds to voltage thresholds that are
                compatible with a group of voltage standards. Refer to
                device documentation for information on the logic high
                and logic low voltages for these logic families.
        """
        self._interpreter.set_digital_logic_family_power_up_state(device_name, logic_family.value)

    def get_digital_logic_family_power_up_state(self, device_name):
        """
        Gets the digital logic family for a device.

        Args:
            device_name (str): Specifies the name as configured in MAX
                of the device to which this operation applies.
        Returns:
            nidaqmx.constants.LogicFamily:

            Specifies the logic family to set the device to when it powers
            up. A logic family corresponds to voltage thresholds that are
            compatible with a group of voltage standards. Refer to device
            documentation for information on the logic high and logic low
            voltages for these logic families.
        """
        logic_family = self._interpreter.get_digital_logic_family_power_up_state(device_name)

        return LogicFamily(logic_family)

    # endregion

    # region cDAQ Sync Functions

    def auto_configure_cdaq_sync_connections(
            self, chassis_devices_ports="", timeout=WAIT_INFINITELY):
        """
        Detects and configures cDAQ Sync connections between devices.
        Stop all NI-DAQmx tasks running on the devices prior to running
        this function because any running tasks cause auto-configuration
        to fail.

        Args:
            chassis_devices_ports (Optional[str]): Specifies the names of the
                CompactDAQ chassis, C Series modules, or cDAQ Sync ports in
                comma separated form to search. If no names are specified, all
                cDAQ Sync ports on connected, non-simulated devices are
                scanned.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out. If a
                timeout occurs, no configuration is changed.
        Returns:
            List[nidaqmx.types.CDAQSyncConnection]:

            Returns the configured port-to-port connections.
        """
        self._interpreter.auto_configure_cdaq_sync_connections(chassis_devices_ports, timeout)

        port_list = self._interpreter.get_auto_configured_cdaq_sync_connections()

        ports = unflatten_channel_string(port_list)
        output_ports = ports[::2]
        input_ports = ports[1::2]

        connections = []
        for output_port, input_port in zip(output_ports, input_ports):
            connections.append(
                CDAQSyncConnection(output_port=output_port,
                                   input_port=input_port))

        return connections

    def are_configured_cdaq_sync_ports_disconnected(
            self, chassis_devices_ports="", timeout=WAIT_INFINITELY):
        """
        Verifies configured cDAQ Sync connections between devices.
        Failures generally indicate a wiring issue or that a device has
        been powered off or removed. Stop all NI-DAQmx tasks running on
        the devices prior to running this function because any running
        tasks cause the verification process to fail.

        Args:
            chassis_devices_ports (Optional[str]): Specifies the names
                of the CompactDAQ chassis, C Series modules, or cDAQ
                Sync ports in comma separated form to search. If no
                names are specified, all cDAQ Sync ports on connected,
                non-simulated devices are scanned.
            timeout (Optional[float]): Specifies the time in seconds to
                wait for the device to respond before timing out.
        Returns:
            List[nidaqmx.types.CDAQSyncConnection]:

            Returns the port-to-port connections that failed verification.
        """
        disconnected_ports_exist = self._interpreter.are_configured_cdaq_sync_ports_disconnected(
            chassis_devices_ports, timeout)

        port_list = self._interpreter.get_disconnected_cdaq_sync_ports()

        ports = unflatten_channel_string(port_list)
        output_ports = ports[::2]
        input_ports = ports[1::2]

        connections = []
        for output_port, input_port in zip(output_ports, input_ports):
            connections.append(
                CDAQSyncConnection(output_port=output_port,
                                   input_port=input_port))

        return connections

    def add_cdaq_sync_connection(self, ports_to_connect):
        """
        Adds a cDAQ Sync connection between devices. The connection is
        not verified.

        Args:
            ports_to_connect (nidaqmx.types.CDAQSyncConnection):
                Specifies the cDAQ Sync ports to connect.
        """
        port_list = flatten_channel_string(
            [ports_to_connect.output_port, ports_to_connect.input_port])

        self._interpreter.add_cdaq_sync_connection(port_list)

    def remove_cdaq_sync_connection(self, ports_to_disconnect):
        """
        Removes a cDAQ Sync connection between devices. The connection
        is not verified.

        Args:
            ports_to_disconnect (nidaqmx.types.CDAQSyncConnection):
                Specifies the cDAQ Sync ports to disconnect.
        """
        port_list = flatten_channel_string(
            [ports_to_disconnect.output_port, ports_to_disconnect.input_port])

        self._interpreter.remove_cdaq_sync_connection(port_list)

    # endregion
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/system/watchdog.py.mako sha256=f6fea2045f65e23fbee447ced04ee6f6eee8d7e80bf57999e9e29107db22dabb bytes=12895 -->
## FILE: src/codegen/templates/system/watchdog.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/system/watchdog.py.mako`
- sha256: `f6fea2045f65e23fbee447ced04ee6f6eee8d7e80bf57999e9e29107db22dabb`
- bytes: 12895

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "Watchdog")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import numpy
import warnings

from nidaqmx import utils
from nidaqmx.errors import DaqResourceWarning
from nidaqmx.system._watchdog_modules.expiration_state import ExpirationState
from nidaqmx.system._watchdog_modules.expiration_states_collection import (
    ExpirationStatesCollection)
from nidaqmx.utils import flatten_channel_string
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
from nidaqmx.types import (
    AOExpirationState, COExpirationState, DOExpirationState)

__all__ = ['WatchdogTask']


class WatchdogTask:
    """
    Represents the watchdog configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_close_on_exit', '_saved_name', '_interpreter', '_expiration_states', '__weakref__')

    def __init__(self, device_name, task_name='', timeout=10, grpc_options=None):
        """
        Creates and configures a task that controls the watchdog timer of a
        device. The timer activates when you start the task.

        Use the DAQmx Configure Watchdog Expiration States functions to
        configure channel expiration states. This class does not program
        the watchdog timer on a real-time controller.

        Args:
            device_name (str): Specifies is the name as configured in MAX of
                the device to which this operation applies.
            task_name (str): Specifies the name to assign to the task. If you
                use this constructor in a loop and specify a name for the task,
                you must use the DAQmx Clear Task method within the loop after
                you are finished with the task. Otherwise, NI-DAQmx attempts to
                create multiple tasks with the same name, which results in an
                error.
            timeout (float): Specifies the amount of time in seconds until the
                watchdog timer expires. A value of -1 means the internal timer
                never expires. Set this input to -1 if you use an Expiration
                Trigger to expire the watchdog task. If this time elapses, the
                device sets the physical channels to the states you specify
                with the digital physical channel expiration states input.
            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        # Initialize the fields that __del__ accesses so it doesn't crash when __init__ raises an exception.
        self._handle = None
        self._close_on_exit = False
        self._saved_name = task_name

        self._interpreter = utils._select_interpreter(grpc_options)

        self._handle, self._close_on_exit = self._interpreter.create_watchdog_timer_task_ex(device_name, task_name, timeout)

        # Saved name is used in self.close() to throw graceful error on
        # double closes.
        self._saved_name = self.name
        self._expiration_states = ExpirationStatesCollection(self._handle, self._interpreter)

    def __del__(self):
        if self._handle is not None and self._close_on_exit:
            warnings.warn(
                'Task of name "{}" was not explicitly closed before it was '
                'destructed. Resources on the task device may still be '
                'reserved.'.format(self._saved_name), DaqResourceWarning)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self._close_on_exit:
            self.close()

    @property
    def expiration_states(self):
        """
        :class:`nidaqmx.system._watchdog_modules.expiration_states_collection.ExpirationStatesCollection`: Gets
            the collection of expiration states for this watchdog task.
        """
        return self._expiration_states

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    @property
    def name(self):
        """
        str: Indicates the name of the task.
        """
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1276)
        return val

    def _control_watchdog_task(self, action):
        """
        Controls the watchdog timer task according to the action you
        specify. This function does not program the watchdog timer on a
        real-time controller. Use the Real-Time Watchdog VIs to program
        the watchdog timer on a real-time controller.

        Args:
            action (nidaqmx.constants.WDTTaskAction): Specifies how to
                control the watchdog timer task.
        """
        self._interpreter.control_watchdog_task(self._handle, action.value)

    def cfg_watchdog_ao_expir_states(self, expiration_states):
        """
        Configures the expiration states for an analog watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.AOExpirationState]):
                Contains the states to which to set analog physical channels
                when the watchdog timer expires. Each element of the list
                contains an analog physical channel name, the corresponding
                expiration state, and the output type for that analog
                physical channel. The units of "expiration state" must be
                specified in volts for an analog output voltage expiration
                state, or amps for an analog output current expiration state.

                physical_channel (str): Specifies the analog output channel to
                    modify. You cannot modify dedicated analog input lines.
                expiration_state (float): Specifies the value to set the
                    channel to upon expiration.
                output_type (nidaqmx.constants.WatchdogAOExpirState):
                    Specifies the output type of the physical channel.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        """
        channel_names = flatten_channel_string(
            [e.physical_channel for e in expiration_states])
        expir_state = numpy.array(
            [e.expiration_state for e in expiration_states], dtype=numpy.float64)
        output_type = numpy.array(
            [e.output_type.value for e in expiration_states], dtype=numpy.int32)

        self._interpreter.cfg_watchdog_ao_expir_states(self._handle, channel_names, expir_state, output_type)

        return [ExpirationState(self._handle, e.physical_channel, self._interpreter)
                for e in expiration_states]

    def cfg_watchdog_co_expir_states(self, expiration_states):
        """
        Configures the expiration states for a counter watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.COExpirationState]):
                Contains the states to which to set counter physical channels
                when the watchdog timer expires. Each element of the list
                contains a counter physical channel name and the corresponding
                state for that counter physical channel.

                physical_channel (str): Specifies the counter output channel to
                    modify. You cannot modify dedicated counter input lines.
                expiration_state (nidaqmx.constants.WatchdogCOExpirState):
                    Specifies the value to set the channel to upon expiration.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        """
        channel_names = flatten_channel_string(
            [e.physical_channel for e in expiration_states])
        expir_state = numpy.array(
            [e.expiration_state.value for e in expiration_states], dtype=numpy.int32)

        self._interpreter.cfg_watchdog_co_expir_states(self._handle, channel_names, expir_state)

        return [ExpirationState(self._handle, e.physical_channel, self._interpreter)
                for e in expiration_states]

    def cfg_watchdog_do_expir_states(self, expiration_states):
        """
        Configures the expiration states for a digital watchdog timer task.

        Args:
            expiration_states
                (List[nidaqmx.system.watchdog.DOExpirationState]):
                Contains the states to which to set digital physical channels
                when the watchdog timer expires. Each element of the list
                contains a digital physical channel name and the corresponding
                state for that digital physical channel.

                physical_channel (str): Specifies the digital output channel to
                    modify. You cannot modify dedicated digital input lines.
                expiration_state (nidaqmx.constants.Level): Specifies the
                    value to set the channel to upon expiration.
        Returns:
            List[nidaqmx.system._watchdog_modules.expiration_state.ExpirationState]:

            Indicates the list of objects representing the configured
            expiration states.
        """
        channel_names = flatten_channel_string(
            [e.physical_channel for e in expiration_states])
        expir_state = numpy.array(
            [e.expiration_state.value for e in expiration_states], dtype=numpy.int32)

        self._interpreter.cfg_watchdog_do_expir_states(self._handle, channel_names, expir_state)

        return [ExpirationState(self._handle, e.physical_channel, self._interpreter)
                for e in expiration_states]

    def clear_expiration(self):
        """
        Unlock a device whose watchdog timer expired.

        This function does not program the watchdog timer on a real-time
        controller. Use the Real-Time Watchdog VIs to program the watchdog
        timer on a real-time controller.
        """
        self._control_watchdog_task(WDTTaskAction.CLEAR_EXPIRATION)

    def close(self):
        """
        Clears the task.

        Before clearing, this method aborts the task, if necessary,
        and releases any resources the task reserved. You cannot use a task
        after you clear it unless you recreate the task.

        If you create a DAQmx Task object within a loop, use this method
        within the loop after you are finished with the task to avoid
        allocating unnecessary memory.
        """
        if self._handle is None:
            warnings.warn(
                'Attempted to close NI-DAQmx task of name "{}" but task was '
                'already closed.'.format(self._saved_name), DaqResourceWarning)
            return

        self._interpreter.clear_task(self._handle)

        self._handle = None

    def control(self, action):
        """
        Alters the state of a task according to the action you specify.

        Args:
            action (nidaqmx.constants.TaskMode): Specifies how to alter
                the task state.
        """
        self._interpreter.task_control(self._handle, action.value)

    def reset_timer(self):
        """
        Reset the internal timer. You must continually reset the internal
        timer to prevent it from timing out and locking the device.

        This function does not program the watchdog timer on a real-time
        controller. Use the Real-Time Watchdog VIs to program the watchdog
        timer on a real-time controller.
        """
        self._control_watchdog_task(WDTTaskAction.RESET_TIMER)

    def start(self):
        """
        Transitions the task to the running state to begin the measurement
        or generation. Using this method is required for some applications and
        is optional for others.
        """
        self._interpreter.start_task(self._handle)

    def stop(self):
        """
        Stops the task and returns it to the state the task was in before the
        DAQmx Start Task method ran.
        """
        self._interpreter.stop_task(self._handle)

<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/_export_signals.py.mako sha256=bfa678bc15eff8a41fa3c753343e9351127e4facaa2d120d820d33d8a139da9d bytes=1561 -->
## FILE: src/codegen/templates/task/_export_signals.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/_export_signals.py.mako`
- sha256: `bfa678bc15eff8a41fa3c753343e9351127e4facaa2d120d820d33d8a139da9d`
- bytes: 1561

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes
    from codegen.utilities.attribute_helpers import get_enums_used as get_enums_used_in_attributes
    from codegen.utilities.function_helpers import get_functions
    from codegen.utilities.function_helpers import get_enums_used as get_enums_used_in_functions
    from codegen.utilities.helpers import get_enums_to_import
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data,"ExportSignals")
    functions = get_functions(data,"ExportSignals")
    enums_in_attributes = get_enums_used_in_attributes(attributes)
    enums_in_functions = get_enums_used_in_functions(functions)
    enums_used = get_enums_to_import(enums_in_attributes, enums_in_functions)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class ExportSignals:
    """
    Represents the exported signal configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter')

    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/_in_stream.py.mako sha256=104c93971ed21c30f3b150c8557bdf44d758f31403712572d8b250a0d912cde2 bytes=15996 -->
## FILE: src/codegen/templates/task/_in_stream.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/_in_stream.py.mako`
- sha256: `104c93971ed21c30f3b150c8557bdf44d758f31403712572d8b250a0d912cde2`
- bytes: 15996

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "InStream")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations

from typing import Type, Optional, Union

import numpy
import numpy.typing
import deprecation
import pathlib

from nidaqmx.task.channels import Channel
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
from nidaqmx.constants import WaveformAttributeMode

class InStream:
    """
    Exposes an input data stream on a DAQmx task.

    The input data stream be used to control reading behavior and can be
    used in conjunction with reader classes to read samples from an
    NI-DAQmx task.
    """
    __slots__ = ('_task', '_handle', '_interpreter', '_timeout', '_waveform_attribute_mode')

    def __init__(self, task, interpreter):
        self._task = task
        self._handle = task._handle
        self._interpreter = interpreter
        self._timeout = 10.0
        self._waveform_attribute_mode = WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES

        super().__init__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    self._timeout == other._timeout)
        return False

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle) ^ hash(self._timeout)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'InStream(task={self._task.name})'

    @property
    def timeout(self):
        """
        float: Specifies the amount of time in seconds to wait for
            samples to become available. If the time elapses, the read
            method returns an error and any samples read before the
            timeout elapsed. The default timeout is 10 seconds. If you
            set timeout to nidaqmx.WAIT_INFINITELY, the read method
            waits indefinitely. If you set timeout to 0, the read method
            tries once to read the requested samples and returns an error
            if it is unable to.
        """
        return self._timeout

    @timeout.setter
    def timeout(self, val):
        self._timeout = val

    @timeout.deleter
    def timeout(self):
        self._timeout = 10.0

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    def get_channels_buffer_size(self):
        channel_names = self._task.channel_names
        total_size = sum(len(name) + 2 for name in channel_names) + 1
        return total_size

    def _calculate_num_samps_per_chan(self, num_samps_per_chan):
        if num_samps_per_chan == -1:
            acq_type = self._task.timing.samp_quant_samp_mode

            if (acq_type == AcquisitionType.FINITE and
                    not self.read_all_avail_samp):
                return self._task.timing.samp_quant_samp_per_chan
            else:
                return self.avail_samp_per_chan
        else:
            return num_samps_per_chan

    def configure_logging(
            self, file_path: str | pathlib.PurePath, logging_mode=LoggingMode.LOG_AND_READ,
            group_name="", operation=LoggingOperation.OPEN_OR_CREATE):
        """
        Configures TDMS file logging for the task.

        Args:
            file_path: Specifies the path to the TDMS file to
                which you want to log data.
            logging_mode (Optional[nidaqmx.constants.LoggingMode]):
                Specifies whether to enable logging and whether to allow
                reading data while logging. "log" mode allows for the
                best performance. However, you cannot read data while
                logging if you specify this mode. If you want to read
                data while logging, specify "LOG_AND_READ" mode.
            group_name (Optional[str]): Specifies the name of the group
                to create within the TDMS file for data from this task.
                If you append data to an existing file and the specified
                group already exists, NI-DAQmx appends a number symbol
                and a number to the group name, incrementing that number
                until finding a group name that does not exist. For
                example, if you specify a group name of Voltage Task,
                and that group already exists, NI-DAQmx assigns the
                group name Voltage Task #1, then Voltage Task #2. If you
                do not specify a group name, NI-DAQmx uses the name of
                the task.
            operation (Optional[nidaqmx.constants.LoggingOperation]):
                Specifies how to open the TDMS file.
        """

        self._interpreter.configure_logging(
            self._handle, str(file_path), logging_mode.value, group_name, operation.value)

    def read(self, number_of_samples_per_channel=READ_ALL_AVAILABLE):
        """
        Reads raw samples from the task or virtual channels you specify.

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        This method determines a NumPy array of appropriate size and data
        type to create and return based on your device specifications.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to nidaqmx.WAIT_INFINITELY, the method waits
        indefinitely. If you set timeout to 0, the method tries once to
        read the requested samples and returns an error if it is unable
        to.

        Args:
            number_of_samples_per_channel (int): Specifies the number of
                samples to read.

                If you set this input to nidaqmx.READ_ALL_AVAILABLE,
                NI-DAQmx determines how many samples to read based on if
                the task acquires samples continuously or acquires a
                finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.READ_ALL_AVAILABLE, this method
                reads all the samples currently available in the buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.READ_ALL_AVAILABLE, the method
                waits for the task to acquire all requested samples,
                then reads those samples. If you set the
                "read_all_avail_samp" property to TRUE, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
        Returns:
            numpy.ndarray:

            The samples requested in the form of a 1D NumPy array. This
            method determines a NumPy array of appropriate size and data
            type to create and return based on your device specifications.
        """
        channels_to_read = self.channels_to_read
        number_of_channels = len(channels_to_read.channel_names)

        samp_size_in_bits = channels_to_read.ai_raw_samp_size
        has_negative_range = channels_to_read.ai_rng_low < 0

        if samp_size_in_bits == 32:
            if has_negative_range:
                dtype: type[numpy.generic] = numpy.int32
            else:
                dtype = numpy.uint32
        elif samp_size_in_bits == 16:
            if has_negative_range:
                dtype = numpy.int16
            else:
                dtype = numpy.uint16
        else:
            if has_negative_range:
                dtype = numpy.int8
            else:
                dtype = numpy.uint8

        num_samps_per_chan = self._calculate_num_samps_per_chan(
            number_of_samples_per_channel)

        number_of_samples = number_of_channels * num_samps_per_chan

        numpy_array: numpy.typing.NDArray = numpy.zeros(number_of_samples, dtype=dtype)

        _, samples_read, _ = self._interpreter.read_raw(
            self._handle, num_samps_per_chan,
            self.timeout, numpy_array)

        if number_of_channels * samples_read != number_of_samples:
            return numpy_array[:number_of_channels * samples_read]
        return numpy_array

    @deprecation.deprecated(deprecated_in="1.0.0", removed_in="1.2.0", details="Use read_all instead.")
    def readall(self):
        return self.read_all()

    def read_all(self):
        """
        Reads all available raw samples from the task or virtual channels
        you specify.

        NI-DAQmx determines how many samples to read based on if the task
        acquires samples continuously or acquires a finite number of
        samples.

        If the task acquires samples continuously, this method reads all
        the samples currently available in the buffer.

        If the task acquires a finite number of samples, the method
        waits for the task to acquire all requested samples, then reads
        those samples. If you set the "read_all_avail_samp" property to
        TRUE, the method reads the samples currently available in the
        buffer and does not wait for the task to acquire all requested
        samples.

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        This method determines a NumPy array of appropriate size and data
        type to create and return based on your device specifications.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to nidaqmx.WAIT_INFINITELY, the method waits
        indefinitely. If you set timeout to 0, the method tries once to
        read the requested samples and returns an error if it is unable
        to.

        Returns:
            numpy.ndarray:

            The samples requested in the form of a 1D NumPy array. This
            method determines a NumPy array of appropriate size and data
            type to create and return based on your device specifications.
        """
        return self.read(number_of_samples_per_channel=READ_ALL_AVAILABLE)

    @deprecation.deprecated(deprecated_in="1.0.0", removed_in="1.2.0", details="Use read_into instead.")
    def readinto(self, numpy_array):
        return self.read_into(numpy_array)

    def read_into(self, numpy_array):
        """
        Reads raw samples from the task or virtual channels you specify
        into numpy_array.

        The object numpy_array should be a pre-allocated, writable 1D
        numpy array.

        The number of samples per channel to read is determined using
        the following equation:

        number_of_samples_per_channel = math.floor(
            numpy_array_size_in_bytes / (
                number_of_channels_to_read * raw_sample_size_in_bytes))

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        If you use a different integer size than the native format of the
        device, one integer can contain multiple samples or one sample can
        stretch across multiple integers. For example, if you use 32-bit
        integers, but the device uses 8-bit samples, one integer contains
        up to four samples. If you use 8-bit integers, but the device uses
        16-bit samples, a sample might require two integers. This behavior
        varies from device to device. Refer to your device documentation
        for more information.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to -1, the method waits indefinitely. If you
        set timeout to 0, the method tries once to read the requested
        samples and returns an error if it is unable to.

        Args:
            numpy_array: Specifies the 1D NumPy array object into which
                the samples requested are read.
        Returns:
            int: Indicates the total number of samples read.
        """
        channels_to_read = self.channels_to_read
        number_of_channels = len(channels_to_read.channel_names)

        number_of_samples_per_channel, _ = divmod(
            numpy_array.nbytes, (
                number_of_channels * channels_to_read.ai_raw_samp_size // 8))

        _, samples_read, _ = self._interpreter.read_raw(
            self._handle, number_of_samples_per_channel,
            self.timeout, numpy_array)

        return samples_read

    def start_new_file(self, file_path: str | pathlib.PurePath):
        """
        Starts a new TDMS file the next time data is written to disk.

        Args:
            file_path: Specifies the path to the TDMS file to
                which you want to log data.
        """

        self._interpreter.start_new_file(self._handle, str(file_path))

<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\

    @property
    def waveform_attribute_mode(self):
        """
        :class:`nidaqmx.constants.WaveformAttributeMode`: Specifies the type of information returned from waveform reads.
        """
        return self._waveform_attribute_mode

    @waveform_attribute_mode.setter
    def waveform_attribute_mode(self, val):
        self._waveform_attribute_mode = val

    @waveform_attribute_mode.deleter
    def waveform_attribute_mode(self):
        self._waveform_attribute_mode = WaveformAttributeMode.TIMING | WaveformAttributeMode.EXTENDED_PROPERTIES
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/_out_stream.py.mako sha256=3c5b7ce0d9539425a07c120974f0b91c1b450bbc3605c48fbd3283eefa25476c bytes=7191 -->
## FILE: src/codegen/templates/task/_out_stream.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/_out_stream.py.mako`
- sha256: `3c5b7ce0d9539425a07c120974f0b91c1b450bbc3605c48fbd3283eefa25476c`
- bytes: 7191

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "OutStream")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})

class OutStream:
    """
    Exposes an output data stream on a DAQmx task.

    The output data stream be used to control writing behavior and can be
    used in conjunction with writer classes to write samples to an
    NI-DAQmx task.
    """
    __slots__ = ('_task', '_handle', '_interpreter', '_auto_start', '_timeout')

    def __init__(self, task, interpreter):
        self._task = task
        self._handle = task._handle
        self._interpreter = interpreter
        self._auto_start = False
        self._timeout = 10.0

        super().__init__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    self._auto_start == other._auto_start and
                    self._timeout == other._timeout)
        return False

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle) ^ hash((self._auto_start, self._timeout))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'OutStream(task={self._task.name})'

    @property
    def auto_start(self):
        """
        bool: Specifies if the "write" method automatically starts the
            stream's owning task if you did not explicitly start it
            with the DAQmx Start Task method.
        """
        return self._auto_start

    @auto_start.setter
    def auto_start(self, val):
        self._auto_start = val

    @auto_start.deleter
    def auto_start(self):
        self._auto_start = False

    @property
    def timeout(self):
        """
        float: Specifies the amount of time in seconds to wait for
            the write method to write all samples. NI-DAQmx performs a
            timeout check only if the write method must wait before it
            writes data. The write method returns an error if the time
            elapses. The default timeout is 10 seconds. If you set
            "timeout" to nidaqmx.WAIT_INFINITELY, the write method
            waits indefinitely. If you set timeout to 0, the write
            method tries once to write the submitted samples. If the
            write method could not write all the submitted samples, it
            returns an error and the number of samples successfully
            written in the number of samples written per channel
            output.
        """
        return self._timeout

    @timeout.setter
    def timeout(self, val):
        self._timeout = val

    @timeout.deleter
    def timeout(self):
        self._timeout = 10.0

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    def write(self, numpy_array):
        """
        Writes raw samples to the task or virtual channels you specify.

        The number of samples per channel to write is determined using the
        following equation:

        number_of_samples_per_channel = math.floor(
            numpy_array_size_in_bytes / (
                number_of_channels_to_write * raw_sample_size_in_bytes))

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or 32-bit
        integer, signed or unsigned.

        If you use a different integer size than the native format of the
        device, one integer can contain multiple samples or one sample can
        stretch across multiple integers. For example, if you use 32-bit
        integers, but the device uses 8-bit samples, one integer contains up to
        four samples. If you use 8-bit integers, but the device uses 16-bit
        samples, a sample might require two integers. This behavior varies from
        device to device. Refer to your device documentation for more
        information.

        NI-DAQmx does not separate raw data into channels. It accepts data in
        an interleaved or non-interleaved 1D array, depending on the raw
        ordering of the device. Refer to your device documentation for more
        information.

        If the task uses on-demand timing, this method returns only after the
        device generates all samples. On-demand is the default timing type if
        you do not use the timing property on the task to configure a sample
        timing type. If the task uses any timing type other than on-demand,
        this method returns immediately and does not wait for the device to
        generate all samples. Your application must determine if the task is
        done to ensure that the device generated all samples.

        Use the "auto_start" property on the stream to specify if this method
        automatically starts the stream's owning task if you did not explicitly
        start it with the DAQmx Start Task method.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for the method to write all samples. NI-DAQmx
        performs a timeout check only if the method must wait before it writes
        data. This method returns an error if the time elapses. The default
        timeout is 10 seconds. If you set timeout to nidaqmx.WAIT_INFINITELY,
        the method waits indefinitely. If you set timeout to 0, the method
        tries once to write the submitted samples. If the method could not
        write all the submitted samples, it returns an error and the number of
        samples successfully written.

        Args:
            numpy_array (numpy.ndarray): Specifies a 1D NumPy array that
                contains the raw samples to write to the task.
        Returns:
            int:

            Specifies the actual number of samples per channel successfully
            written to the buffer.
        """
        channels_to_write = self._task.channels
        number_of_channels = len(channels_to_write.channel_names)

        channels_to_write.ao_resolution_units = ResolutionType.BITS

        number_of_samples_per_channel, _ = divmod(
            numpy_array.nbytes, (
                number_of_channels * int(channels_to_write.ao_resolution) // 8))

        return self._interpreter.write_raw(
            self._handle, number_of_samples_per_channel,
            self.auto_start, self.timeout, numpy_array)

    def get_channels_buffer_size(self):
        channel_names = self._task.channel_names
        total_size = sum(len(name) + 2 for name in channel_names) + 1
        return total_size
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/_timing.py.mako sha256=ee46a62e8856afe7e6f2a9b94240d9581a74ab8669a6c98e4a08de7214d71522 bytes=3012 -->
## FILE: src/codegen/templates/task/_timing.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/_timing.py.mako`
- sha256: `ee46a62e8856afe7e6f2a9b94240d9581a74ab8669a6c98e4a08de7214d71522`
- bytes: 3012

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions
    from codegen.utilities.attribute_helpers import get_attributes
    from codegen.utilities.function_helpers import get_enums_used as get_enums_used_in_functions
    from codegen.utilities.attribute_helpers import get_enums_used as get_enums_used_in_attributes
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data,"Timing")
    functions = get_functions(data,"Timing")
    enums_in_attributes = get_enums_used_in_attributes(attributes)
    enums_in_functions = get_enums_used_in_functions(functions)
    enums_used = get_enums_to_import(enums_in_attributes, enums_in_functions)
%>\
# Do not edit this file; it was automatically generated.

from __future__ import annotations

from typing import NoReturn

from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx.system.device import Device
from nidaqmx.errors import DaqError
from nidaqmx.error_codes import DAQmxErrors
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class Timing:
    """
    Represents the timing configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter', '_active_devs')

    def __init__(self, task_handle, interpreter, active_devs: str | Device | None = None):
        if isinstance(active_devs, Device):
            active_devs = active_devs.name
        self._handle = task_handle
        self._interpreter = interpreter
        self._active_devs = active_devs

    def __getitem__(self, dev: str | Device) -> Timing:
        if self._active_devs:
            raise DaqError( 
                f"Cannot set active device '{dev}' because active device '{self._active_devs}' is already set.",
                DAQmxErrors.UNKNOWN)
        if isinstance(dev, (str, Device)):
            return Timing(self._handle, self._interpreter, active_devs=dev)
        else:
            raise TypeError(f"Invalid active_devs input: {dev!r} (type: {type(dev).__name__}). Expected str or Device.")

    def _raise_device_context_not_supported_error(self) -> NoReturn:
        raise DaqError(
            'Operation must be performed on the entire task. It cannot be '
            'performed only on specific devices in the task.',
            DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT)

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/channels/_ai_channel.py.mako sha256=4c565218db3b567ae95e8520f8d88226dbebe6071a4e1da762122b62a17249a3 bytes=1131 -->
## FILE: src/codegen/templates/task/channels/_ai_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/channels/_ai_channel.py.mako`
- sha256: `4c565218db3b567ae95e8520f8d88226dbebe6071a4e1da762122b62a17249a3`
- bytes: 1131

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "AIChannel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import numpy
import deprecation

from nidaqmx.scale import _ScaleAlternateConstructor
from nidaqmx.task.channels._channel import Channel
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class AIChannel(Channel):
    """
    Represents one or more analog input virtual channels and their properties.
    """
    __slots__ = ()

    def __repr__(self):
        return f'AIChannel(name={self._name})'

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/channels/_ao_channel.py.mako sha256=5d3c417bd6003927a4ce7d6c85f44842d4d559ae78afb4d2851fb1d113392ca9 bytes=892 -->
## FILE: src/codegen/templates/task/channels/_ao_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/channels/_ao_channel.py.mako`
- sha256: `5d3c417bd6003927a4ce7d6c85f44842d4d559ae78afb4d2851fb1d113392ca9`
- bytes: 892

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "AOChannel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.scale import _ScaleAlternateConstructor
from nidaqmx.task.channels._channel import Channel
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class AOChannel(Channel):
    """
    Represents one or more analog output virtual channels and their properties.
    """
    __slots__ = ()

    def __repr__(self):
        return f'AOChannel(name={self._name})'

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/channels/_channel.py.mako sha256=fe61f58808414ee083abf261a1e3b45b53577b454464fb4dccc0407119b4f119 bytes=8181 -->
## FILE: src/codegen/templates/task/channels/_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/channels/_channel.py.mako`
- sha256: `fe61f58808414ee083abf261a1e3b45b53577b454464fb4dccc0407119b4f119`
- bytes: 8181

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "Channel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import nidaqmx.task.channels  # circular import: Channel._factory uses derived classes
from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
from nidaqmx.utils import flatten_channel_string, unflatten_channel_string
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class Channel:
    """
    Represents virtual channel or a list of virtual channels.
    """
    __slots__ = ['_handle', '_name', '_interpreter', '__weakref__']

    def __init__(self, task_handle, virtual_or_physical_name, interpreter):
        """
        Args:
            task_handle (TaskHandle): Specifies the handle of the task that
                this channel is associated with.
            virtual_or_physical_name (str): Specifies the flattened virtual or
                physical name of a channel.
            interpreter (BaseInterpreter): Specifies the interpreter instance.
        """
        self._handle = task_handle
        self._name = virtual_or_physical_name
        self._interpreter = interpreter

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplementedError(
                'Cannot concatenate objects of type {} and {}'
                .format(self.__class__, other.__class__))

        if self._handle != other._handle:
            raise NotImplementedError(
                'Cannot concatenate Channel objects from different tasks.')

        name = flatten_channel_string([self.name, other.name])
        return Channel._factory(self._handle, name, self._interpreter)

    def __contains__(self, item):
        channel_names = self.channel_names

        if isinstance(item, str):
            items = unflatten_channel_string(item)
        elif isinstance(item, Channel):
            items = item.channel_names

        return all([item in channel_names for item in items])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    set(self.channel_names) == set(other.channel_names))
        return False

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle) ^ hash(frozenset(self.channel_names))

    def __iadd__(self, other):
        return self.__add__(other)

    def __iter__(self):
        for channel_name in self.channel_names:
            yield Channel._factory(self._handle, channel_name, self._interpreter)

    def __len__(self):
        return len(self.channel_names)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __reversed__(self):
        channel_names = self.channel_names
        channel_names.reverse()

        for channel_name in channel_names:
            yield Channel._factory(self._handle, channel_name, self._interpreter)

    def __repr__(self):
        return f'Channel(name={self.name})'

    @staticmethod
    def _factory(task_handle, virtual_or_physical_name, interpreter):
        """
        Implements the factory pattern for nidaqmx channels.

        Args:
            task_handle (TaskHandle): Specifies the handle of the task that
                this channel is associated with.
            virtual_or_physical_name (str): Specifies the flattened virtual
                or physical name of a channel.
            interpreter (BaseInterpreter): Specifies the interpreter instance.
        Returns:
            nidaqmx.task.channels.Channel:

            Indicates an object that represents the specified channel.
        """
        chan_type = interpreter.get_chan_attribute_int32(task_handle, virtual_or_physical_name, 0x187f)

        channel_type = ChannelType(chan_type)

        if channel_type == ChannelType.ANALOG_INPUT:
            return nidaqmx.task.channels.AIChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.ANALOG_OUTPUT:
            return nidaqmx.task.channels.AOChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.COUNTER_INPUT:
            return nidaqmx.task.channels.CIChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.COUNTER_OUTPUT:
            return nidaqmx.task.channels.COChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.DIGITAL_INPUT:
            return nidaqmx.task.channels.DIChannel(
                task_handle, virtual_or_physical_name, interpreter)
        elif channel_type == ChannelType.DIGITAL_OUTPUT:
            return nidaqmx.task.channels.DOChannel(
                task_handle, virtual_or_physical_name, interpreter)

    @property
    def name(self):
        """
        str: Specifies the name of the virtual channel this object
            represents.
        """
        if self._name:
            return self._name
        else:
            return self._all_channels_name

    @property
    def channel_names(self):
        """
        List[str]: Specifies the unflattened list of the virtual channels.
        """
        if self._name:
            return unflatten_channel_string(self._name)
        else:
            return unflatten_channel_string(self._all_channels_name)

    @property
    def _all_channels_name(self):
        """
        str: Specifies the flattened names of all the virtual channels in
            the task.
        """
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1273)
        return val

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    def save(self, save_as="", author="", overwrite_existing_channel=False,
             allow_interactive_editing=True, allow_interactive_deletion=True):
        """
        Saves this local or global channel to MAX as a global channel.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            overwrite_existing_channel (Optional[bool]): Specifies whether to
                overwrite a global channel of the same name if one is already
                saved in MAX. If this input is False and a global channel of
                the same name is already saved in MAX, this function returns
                an error.
            allow_interactive_editing (Optional[bool]): Specifies whether to
                allow the task, global channel, or custom scale to be edited
                in the DAQ Assistant. If allow_interactive_editing is True,
                the DAQ Assistant must support all task or global channel
                settings.
            allow_interactive_deletion (Optional[bool]): Specifies whether
                to allow the task, global channel, or custom scale to be
                deleted through MAX.
        """
        options = 0
        if overwrite_existing_channel:
            options |= _Save.OVERWRITE.value
        if allow_interactive_editing:
            options |= _Save.ALLOW_INTERACTIVE_EDITING.value
        if allow_interactive_deletion:
            options |= _Save.ALLOW_INTERACTIVE_DELETION.value

        self._interpreter.save_global_chan(self._handle, self._name, save_as, author, options)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/channels/_ci_channel.py.mako sha256=13395259bbe59b12df9718b80281a353070254cce9e547e7f87743d0d8986eac bytes=890 -->
## FILE: src/codegen/templates/task/channels/_ci_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/channels/_ci_channel.py.mako`
- sha256: `13395259bbe59b12df9718b80281a353070254cce9e547e7f87743d0d8986eac`
- bytes: 890

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "CIChannel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.scale import _ScaleAlternateConstructor
from nidaqmx.task.channels._channel import Channel
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class CIChannel(Channel):
    """
    Represents one or more counter input virtual channels and their properties.
    """
    __slots__ = ()

    def __repr__(self):
        return f'CIChannel(name={self._name})'

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/channels/_co_channel.py.mako sha256=29a71882688f67bd1c18a0d5cb38b53b54681213020bf2cb4be2619e21205b21 bytes=839 -->
## FILE: src/codegen/templates/task/channels/_co_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/channels/_co_channel.py.mako`
- sha256: `29a71882688f67bd1c18a0d5cb38b53b54681213020bf2cb4be2619e21205b21`
- bytes: 839

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "COChannel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.task.channels._channel import Channel
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class COChannel(Channel):
    """
    Represents one or more counter output virtual channels and their properties.
    """
    __slots__ = ()

    def __repr__(self):
        return f'COChannel(name={self._name})'

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/channels/_di_channel.py.mako sha256=62660ff942507883381c0736e6b17c11f5ba25fde5f9665b7815b6c4d5b7d4b2 bytes=838 -->
## FILE: src/codegen/templates/task/channels/_di_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/channels/_di_channel.py.mako`
- sha256: `62660ff942507883381c0736e6b17c11f5ba25fde5f9665b7815b6c4d5b7d4b2`
- bytes: 838

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "DIChannel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.task.channels._channel import Channel
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class DIChannel(Channel):
    """
    Represents one or more digital input virtual channels and their properties.
    """
    __slots__ = ()

    def __repr__(self):
        return f'DIChannel(name={self._name})'

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/channels/_do_channel.py.mako sha256=73d9cd2d5b6d474d2f64f65b8e3f6582bdf017cb40f0d1c9b5a2c28efb9ffe20 bytes=839 -->
## FILE: src/codegen/templates/task/channels/_do_channel.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/channels/_do_channel.py.mako`
- sha256: `73d9cd2d5b6d474d2f64f65b8e3f6582bdf017cb40f0d1c9b5a2c28efb9ffe20`
- bytes: 839

````mako
<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "DOChannel")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.task.channels._channel import Channel
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class DOChannel(Channel):
    """
    Represents one or more digital output virtual channels and their properties.
    """
    __slots__ = ()

    def __repr__(self):
        return f'DOChannel(name={self._name})'

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/collections/_ai_channel_collection.py.mako sha256=f7e56af8e165df2349877239ea153719938c3726c8121c06a0abca9419e358f4 bytes=2836 -->
## FILE: src/codegen/templates/task/collections/_ai_channel_collection.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/collections/_ai_channel_collection.py.mako`
- sha256: `f7e56af8e165df2349877239ea153719938c3726c8121c06a0abca9419e358f4`
- bytes: 2836

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used
    functions = get_functions(data,"AIChannelCollection")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

import numpy

from nidaqmx.errors import DaqFunctionNotSupportedError
from nidaqmx.task.channels._ai_channel import AIChannel
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class AIChannelCollection(ChannelCollection):
    """
    Contains the collection of analog input channels for a DAQmx Task.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.ai_channels property.
        """
        super().__init__(task_handle, interpreter)

    def _create_chan(self, physical_channel, name_to_assign_to_channel=''):
        """
        Creates and returns an AIChannel object.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.AIChannel:

            Specifies the newly created AIChannel object.
        """
        # Attempt to retrieve the last created channel name. This is only supported on DAQmx 24Q3+ with the library
        # interpreter.
        virtual_channel_name = None
        try:
            virtual_channel_name = self._interpreter.internal_get_last_created_chan()
        except (NotImplementedError, DaqFunctionNotSupportedError):
            pass

        # Fallback implementation is sometimes incorrect.
        if virtual_channel_name is None:
            if name_to_assign_to_channel:
                num_channels = len(unflatten_channel_string(physical_channel))

                if num_channels > 1:
                    virtual_channel_name = '{}0:{}'.format(
                        name_to_assign_to_channel, num_channels-1)
                else:
                    virtual_channel_name = name_to_assign_to_channel
            else:
                virtual_channel_name = physical_channel

        return AIChannel(self._handle, virtual_channel_name, self._interpreter)

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/collections/_ao_channel_collection.py.mako sha256=f01b52933e0e3fcb3a6e2f86982aefad0ed970e5dd3c55206febcacc235309f3 bytes=2835 -->
## FILE: src/codegen/templates/task/collections/_ao_channel_collection.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/collections/_ao_channel_collection.py.mako`
- sha256: `f01b52933e0e3fcb3a6e2f86982aefad0ed970e5dd3c55206febcacc235309f3`
- bytes: 2835

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used
    functions = get_functions(data, "AOChannelCollection")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.errors import DaqFunctionNotSupportedError
from nidaqmx.task.channels._ao_channel import AOChannel
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class AOChannelCollection(ChannelCollection):
    """
    Contains the collection of analog output channels for a DAQmx Task.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.ao_channels property.
        """
        super().__init__(task_handle, interpreter)

    def _create_chan(self, physical_channel, name_to_assign_to_channel=''):
        """
        Creates and returns an AOChannel object.

        Args:
            physical_channel (str): Specifies the names of the physical
                channels to use to create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.AOChannel: 
            
            Specifies the newly created AOChannel object.
        """
        # Attempt to retrieve the last created channel name. This is only supported on DAQmx 24Q3+ with the library
        # interpreter.
        virtual_channel_name = None
        try:
            virtual_channel_name = self._interpreter.internal_get_last_created_chan()
        except (NotImplementedError, DaqFunctionNotSupportedError):
            pass

        # Fallback implementation is sometimes incorrect.
        if virtual_channel_name is None:
            if name_to_assign_to_channel:
                num_channels = len(unflatten_channel_string(physical_channel))

                if num_channels > 1:
                    virtual_channel_name = '{}0:{}'.format(
                        name_to_assign_to_channel, num_channels-1)
                else:
                    virtual_channel_name = name_to_assign_to_channel
            else:
                virtual_channel_name = physical_channel

        return AOChannel(self._handle, virtual_channel_name, self._interpreter)

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/collections/_ci_channel_collection.py.mako sha256=62fb9f48d9aefb41e40b9d3d5b49f020ee1b0d48c9beb37ab51afc64b2736647 bytes=2791 -->
## FILE: src/codegen/templates/task/collections/_ci_channel_collection.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/collections/_ci_channel_collection.py.mako`
- sha256: `62fb9f48d9aefb41e40b9d3d5b49f020ee1b0d48c9beb37ab51afc64b2736647`
- bytes: 2791

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used
    functions = get_functions(data, "CIChannelCollection")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.errors import DaqFunctionNotSupportedError
from nidaqmx.task.channels._ci_channel import CIChannel
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class CIChannelCollection(ChannelCollection):
    """
    Contains the collection of counter input channels for a DAQmx Task.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.ci_channels property.
        """
        super().__init__(task_handle, interpreter)

    def _create_chan(self, counter, name_to_assign_to_channel=''):
        """
        Creates and returns a CIChannel object.

        Args:
            counter (str): Specifies the names of the counters to use to 
                create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.CIChannel: 
            
            Specifies the newly created CIChannel object.
        """
        # Attempt to retrieve the last created channel name. This is only supported on DAQmx 24Q3+ with the library
        # interpreter.
        virtual_channel_name = None
        try:
            virtual_channel_name = self._interpreter.internal_get_last_created_chan()
        except (NotImplementedError, DaqFunctionNotSupportedError):
            pass

        # Fallback implementation is sometimes incorrect.
        if virtual_channel_name is None:
            if name_to_assign_to_channel:
                num_counters = len(unflatten_channel_string(counter))

                if num_counters > 1:
                    virtual_channel_name = '{}0:{}'.format(
                        name_to_assign_to_channel, num_counters-1)
                else:
                    virtual_channel_name = name_to_assign_to_channel
            else:
                virtual_channel_name = counter

        return CIChannel(self._handle, virtual_channel_name, self._interpreter)

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/collections/_co_channel_collection.py.mako sha256=5b839459ddef79ebce16c5ae7f016652a8388374728a2f7d61ba65f15bdb7b6c bytes=2792 -->
## FILE: src/codegen/templates/task/collections/_co_channel_collection.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/collections/_co_channel_collection.py.mako`
- sha256: `5b839459ddef79ebce16c5ae7f016652a8388374728a2f7d61ba65f15bdb7b6c`
- bytes: 2792

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used
    functions = get_functions(data, "COChannelCollection")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.errors import DaqFunctionNotSupportedError
from nidaqmx.task.channels._co_channel import COChannel
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class COChannelCollection(ChannelCollection):
    """
    Contains the collection of counter output channels for a DAQmx Task.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.co_channels property.
        """
        super().__init__(task_handle, interpreter)

    def _create_chan(self, counter, name_to_assign_to_channel=''):
        """
        Creates and returns a COChannel object.

        Args:
            counter (str): Specifies the names of the counters to use to 
                create virtual channels.
            name_to_assign_to_channel (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.COChannel: 
            
            Specifies the newly created COChannel object.
        """
        # Attempt to retrieve the last created channel name. This is only supported on DAQmx 24Q3+ with the library
        # interpreter.
        virtual_channel_name = None
        try:
            virtual_channel_name = self._interpreter.internal_get_last_created_chan()
        except (NotImplementedError, DaqFunctionNotSupportedError):
            pass

        # Fallback implementation is sometimes incorrect.
        if virtual_channel_name is None:
            if name_to_assign_to_channel:
                num_counters = len(unflatten_channel_string(counter))

                if num_counters > 1:
                    virtual_channel_name = '{}0:{}'.format(
                        name_to_assign_to_channel, num_counters-1)
                else:
                    virtual_channel_name = name_to_assign_to_channel
            else:
                virtual_channel_name = counter

        return COChannel(self._handle, virtual_channel_name, self._interpreter)

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/collections/_di_channel_collection.py.mako sha256=c3a9e4242c2ce71e331fd448f11889fc893c6dadfdc4084a9daba15fb85895e9 bytes=3426 -->
## FILE: src/codegen/templates/task/collections/_di_channel_collection.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/collections/_di_channel_collection.py.mako`
- sha256: `c3a9e4242c2ce71e331fd448f11889fc893c6dadfdc4084a9daba15fb85895e9`
- bytes: 3426

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used
    functions = get_functions(data, "DIChannelCollection")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.errors import DaqFunctionNotSupportedError
from nidaqmx.task.channels._di_channel import DIChannel
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class DIChannelCollection(ChannelCollection):
    """
    Contains the collection of digital input channels for a DAQmx Task.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.di_channels property.
        """
        super().__init__(task_handle, interpreter)

    def _create_chan(self, lines, line_grouping, name_to_assign_to_lines=''):
        """
        Creates and returns a DIChannel object.

        Args:
            lines (str): Specifies the names of the lines to use to 
                create virtual channels.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]):
                Specifies how to group digital lines into one or more
                virtual channels.
            name_to_assign_to_lines (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.DIChannel: 
            
            Specifies the newly created DIChannel object.
        """
        # Attempt to retrieve the last created channel name. This is only supported on DAQmx 24Q3+ with the library
        # interpreter.
        virtual_channel_name = None
        try:
            virtual_channel_name = self._interpreter.internal_get_last_created_chan()
        except (NotImplementedError, DaqFunctionNotSupportedError):
            pass

        # Fallback implementation is sometimes incorrect.
        if virtual_channel_name is None:
            unflattened_lines = unflatten_channel_string(lines)
            num_lines = len(unflattened_lines)
            
            if line_grouping == LineGrouping.CHAN_FOR_ALL_LINES:
                if name_to_assign_to_lines:
                    virtual_channel_name = name_to_assign_to_lines
                elif num_lines == 1:
                    virtual_channel_name = lines
                else:
                    virtual_channel_name = unflattened_lines[0] + '...'
            else:
                if name_to_assign_to_lines:
                    if num_lines > 1:
                        virtual_channel_name = '{}0:{}'.format(
                            name_to_assign_to_lines, num_lines-1)
                    else:
                        virtual_channel_name = name_to_assign_to_lines
                else:
                    virtual_channel_name = lines

        return DIChannel(self._handle, virtual_channel_name, self._interpreter)

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/collections/_do_channel_collection.py.mako sha256=493d50d6db95cf92492ffc167b18a320f1e13908c6d59d9000eb0255179abd86 bytes=3415 -->
## FILE: src/codegen/templates/task/collections/_do_channel_collection.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/collections/_do_channel_collection.py.mako`
- sha256: `493d50d6db95cf92492ffc167b18a320f1e13908c6d59d9000eb0255179abd86`
- bytes: 3415

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions,  get_enums_used
    functions = get_functions(data, "DOChannelCollection")
    enums_used = get_enums_used(functions)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.errors import DaqFunctionNotSupportedError
from nidaqmx.task.channels._do_channel import DOChannel
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class DOChannelCollection(ChannelCollection):
    """
    Contains the collection of digital output channels for a DAQmx Task.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.do_channels property.
        """
        super().__init__(task_handle, interpreter)

    def _create_chan(self, lines, line_grouping, name_to_assign_to_lines=''):
        """
        Creates and returns a DOChannel object.

        Args:
            lines (str): Specifies the names of the lines to use to 
                create virtual channels.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]):
                Specifies how to group digital lines into one or more
                virtual channels.
            name_to_assign_to_lines (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx.task.channels.DOChannel: 
            
            Specifies the newly created DOChannel object.
        """
        # Attempt to retrieve the last created channel name. This is only supported on DAQmx 24Q3+ with the library
        # interpreter.
        virtual_channel_name = None
        try:
            virtual_channel_name = self._interpreter.internal_get_last_created_chan()
        except (NotImplementedError, DaqFunctionNotSupportedError):
            pass

        # Fallback implementation is sometimes incorrect.
        if virtual_channel_name is None:
            unflattened_lines = unflatten_channel_string(lines)
            num_lines = len(unflattened_lines)

            if line_grouping == LineGrouping.CHAN_FOR_ALL_LINES:
                if name_to_assign_to_lines:
                    virtual_channel_name = name_to_assign_to_lines
                elif num_lines == 1:
                    virtual_channel_name = lines
                else:
                    virtual_channel_name = unflattened_lines[0] + '...'
            else:
                if name_to_assign_to_lines:
                    if num_lines > 1:
                        virtual_channel_name = '{}0:{}'.format(
                            name_to_assign_to_lines, num_lines-1)
                    else:
                        virtual_channel_name = name_to_assign_to_lines
                else:
                    virtual_channel_name = lines

        return DOChannel(self._handle, virtual_channel_name, self._interpreter)

<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/triggering/_arm_start_trigger.py.mako sha256=e99b19bdce134bd1cd5f3d4703403895f288eadf0378e990f591e4d7ee263d2c bytes=1461 -->
## FILE: src/codegen/templates/task/triggering/_arm_start_trigger.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/triggering/_arm_start_trigger.py.mako`
- sha256: `e99b19bdce134bd1cd5f3d4703403895f288eadf0378e990f591e4d7ee263d2c`
- bytes: 1461

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions, get_enums_used as functions_enums
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used as attribute_enums
    from codegen.utilities.helpers import get_enums_to_import
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "ArmStartTrigger")
    functions = get_functions(data,"ArmStartTrigger")
    attr_enums = attribute_enums(attributes)
    func_enums = functions_enums(functions)
    enums_used = get_enums_to_import(attr_enums, func_enums)
%>\
# Do not edit this file; it was automatically generated.

%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class ArmStartTrigger:
    """
    Represents the arm start trigger configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter')

    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/triggering/_handshake_trigger.py.mako sha256=db1c11df24f06bf0ee92f5ebf67083abc66adbdb27c6f4c2c691039b5acf8887 bytes=1410 -->
## FILE: src/codegen/templates/task/triggering/_handshake_trigger.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/triggering/_handshake_trigger.py.mako`
- sha256: `db1c11df24f06bf0ee92f5ebf67083abc66adbdb27c6f4c2c691039b5acf8887`
- bytes: 1410

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions, get_enums_used as functions_enums
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used as attribute_enums
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data, "HandshakeTrigger")
    functions = get_functions(data,"HandshakeTrigger")
    attr_enums = attribute_enums(attributes)
    func_enums = functions_enums(functions)
    enums_used = get_enums_to_import(attr_enums, func_enums)
%>\
# Do not edit this file; it was automatically generated.

%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class HandshakeTrigger:
    """
    Represents the handshake trigger configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter')

    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/triggering/_pause_trigger.py.mako sha256=673f71b73d55df6a7e39c426fb5ccd1b4e540c2f2c1a9952f494c72a2a5c7596 bytes=1478 -->
## FILE: src/codegen/templates/task/triggering/_pause_trigger.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/triggering/_pause_trigger.py.mako`
- sha256: `673f71b73d55df6a7e39c426fb5ccd1b4e540c2f2c1a9952f494c72a2a5c7596`
- bytes: 1478

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions, get_enums_used as functions_enums
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used as attribute_enums
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data, "PauseTrigger")
    functions = get_functions(data,"PauseTrigger")
    attr_enums = attribute_enums(attributes)
    func_enums = functions_enums(functions)
    enums_used = get_enums_to_import(attr_enums, func_enums)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class PauseTrigger:
    """
    Represents the pause trigger configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter')

    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/triggering/_reference_trigger.py.mako sha256=2b524ae5706c36ac9d8a2a55e1d9392ed9200fcbeb8695765a8c36a73abb97dd bytes=1510 -->
## FILE: src/codegen/templates/task/triggering/_reference_trigger.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/triggering/_reference_trigger.py.mako`
- sha256: `2b524ae5706c36ac9d8a2a55e1d9392ed9200fcbeb8695765a8c36a73abb97dd`
- bytes: 1510

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions, get_enums_used as functions_enums
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used as attribute_enums
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data, "ReferenceTrigger")
    functions = get_functions(data,"ReferenceTrigger")
    attr_enums = attribute_enums(attributes)
    func_enums = functions_enums(functions)
    enums_used = get_enums_to_import(attr_enums, func_enums)
%>\
# Do not edit this file; it was automatically generated.

import numpy

from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class ReferenceTrigger:
    """
    Represents the reference trigger configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter')

    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/triggering/_start_trigger.py.mako sha256=560684380b186a6ca2edcf11a68baf8e0fdfddc6bcf800b66e5648813279f000 bytes=1525 -->
## FILE: src/codegen/templates/task/triggering/_start_trigger.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/triggering/_start_trigger.py.mako`
- sha256: `560684380b186a6ca2edcf11a68baf8e0fdfddc6bcf800b66e5648813279f000`
- bytes: 1525

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions, get_enums_used as functions_enums
    from codegen.utilities.attribute_helpers import get_attributes,  get_enums_used as attribute_enums
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data, "StartTrigger")
    functions = get_functions(data,"StartTrigger")
    attr_enums = attribute_enums(attributes)
    func_enums = functions_enums(functions)
    enums_used = get_enums_to_import(attr_enums, func_enums)
%>\
# Do not edit this file; it was automatically generated.

import numpy

from nidaqmx.system.physical_channel import _PhysicalChannelAlternateConstructor
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif
from datetime import datetime


class StartTrigger:
    """
    Represents the start trigger configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter')

    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/templates/task/triggering/_triggers.py.mako sha256=9643d4b5d4e7136217d7e3cd44e994428ad083b3b7e31483be09b761b8ec5e4f bytes=3545 -->
## FILE: src/codegen/templates/task/triggering/_triggers.py.mako

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/templates/task/triggering/_triggers.py.mako`
- sha256: `9643d4b5d4e7136217d7e3cd44e994428ad083b3b7e31483be09b761b8ec5e4f`
- bytes: 3545

````mako
<%
    from codegen.utilities.text_wrappers import wrap
    from codegen.utilities.function_helpers import get_functions
    from codegen.utilities.attribute_helpers import get_attributes
    from codegen.utilities.function_helpers import get_enums_used as get_enums_used_in_functions
    from codegen.utilities.attribute_helpers import get_enums_used as get_enums_used_in_attributes
    from codegen.utilities.helpers import get_enums_to_import
    attributes = get_attributes(data,"Triggers")
    functions = get_functions(data,"Triggers")
    enums_in_attributes = get_enums_used_in_attributes(attributes)
    enums_in_functions = get_enums_used_in_functions(functions)
    enums_used = get_enums_to_import(enums_in_attributes, enums_in_functions)
%>\
# Do not edit this file; it was automatically generated.

from nidaqmx.task.triggering._arm_start_trigger import ArmStartTrigger
from nidaqmx.task.triggering._handshake_trigger import HandshakeTrigger
from nidaqmx.task.triggering._pause_trigger import PauseTrigger
from nidaqmx.task.triggering._reference_trigger import ReferenceTrigger
from nidaqmx.task.triggering._start_trigger import StartTrigger
%if enums_used:
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})
%endif


class Triggers:
    """
    Represents the trigger configurations for a DAQmx task.
    """
    __slots__ = ('_handle', '_interpreter', '_arm_start_trigger', '_handshake_trigger', '_pause_trigger', '_reference_trigger', '_start_trigger')

    def __init__(self, task_handle, interpreter):
        self._handle = task_handle
        self._interpreter = interpreter
        self._arm_start_trigger = ArmStartTrigger(self._handle, self._interpreter)
        self._handshake_trigger = HandshakeTrigger(self._handle, self._interpreter)
        self._pause_trigger = PauseTrigger(self._handle, self._interpreter)
        self._reference_trigger = ReferenceTrigger(self._handle, self._interpreter)
        self._start_trigger = StartTrigger(self._handle, self._interpreter)

    @property
    def arm_start_trigger(self) -> ArmStartTrigger:
        """
        Gets the arm start trigger configurations for the task.
        """
        return self._arm_start_trigger

    @property
    def handshake_trigger(self) -> HandshakeTrigger:
        """
        Gets the handshake trigger configurations for the task.
        """
        return self._handshake_trigger

    @property
    def pause_trigger(self) -> PauseTrigger:
        """
        Gets the pause trigger configurations for the task.
        """
        return self._pause_trigger

    @property
    def reference_trigger(self) -> ReferenceTrigger:
        """
        Gets the reference trigger configurations for the task.
        """
        return self._reference_trigger

    @property
    def start_trigger(self) -> StartTrigger:
        """
        Gets the start trigger configurations for the task.
        """
        return self._start_trigger

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
<%namespace name="function_template" file="/function_template.py.mako"/>\
%for function_object in functions:
${function_template.script_function(function_object)}
%endfor
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/utilities/__init__.py sha256=e2cccb2308f72dcbe9a5a7e6d06c85124f45b4dd204c2735e6e0301a95d85dc0 bytes=60 -->
## FILE: src/codegen/utilities/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/utilities/__init__.py`
- sha256: `e2cccb2308f72dcbe9a5a7e6d06c85124f45b4dd204c2735e6e0301a95d85dc0`
- bytes: 60

````python
"""This module contains the helpers for code generator."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/utilities/attribute_helpers.py sha256=7ff8ba325f9836ab1b16f119ed3214db35906199b7404aa961c260f973846835 bytes=13538 -->
## FILE: src/codegen/utilities/attribute_helpers.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/utilities/attribute_helpers.py`
- sha256: `7ff8ba325f9836ab1b16f119ed3214db35906199b7404aa961c260f973846835`
- bytes: 13538

````python
"""This contains the helper methods used in attribute generation."""

import codegen.metadata as scrapigen_metadata
from codegen.properties.attribute import Attribute
from codegen.utilities.helpers import camel_to_snake_case
from codegen.utilities.interpreter_helpers import (
    INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES,
)

EXCLUDED_ATTRIBUTES = [
    "AI_CHAN_CAL_HAS_VALID_CAL_INFO",
    "AI_CHAN_CAL_ENABLE_CAL",
    "AI_CHAN_CAL_DESC",
    "AI_CHAN_CAL_APPLY_CAL_IF_EXP",
    "AI_BRIDGE_SHUNT_CAL_SHUNT_CAL_B_SRC",
    "AI_CHAN_CAL_VERIF_REF_VALS",
    "AI_CHAN_CAL_VERIF_ACQ_VALS",
    "AI_CHAN_CAL_TABLE_SCALED_VALS",
    "AI_CHAN_CAL_TABLE_PRE_SCALED_VALS",
    "AI_CHAN_CAL_SCALE_TYPE",
    "AI_CHAN_CAL_POLY_REVERSE_COEFF",
    "AI_CHAN_CAL_POLY_FORWARD_COEFF",
    "AI_CHAN_CAL_OPERATOR_NAME",
    "AI_PHYSICAL_CHANS",
    "AO_PHYSICAL_CHANS",
    "DI_LINES",
    "DI_PORTS",
    "DO_PORTS",
    "DO_LINES",
    "CI_PHYSICAL_CHANS",
    "CO_PHYSICAL_CHANS",
    "TIMING_SYNC_PULSE_FORCE",
    "ID_PIN_MEM_SERIAL_NUMS",
]

DEPRECATED_ATTRIBUTES = {
    "ai_rtd_r_0": {"new_name": "ai_rtd_r0", "deprecated_in": "0.7.0"},
    "ai_sound_pressured_b_ref": {"new_name": "ai_sound_pressure_db_ref", "deprecated_in": "0.7.0"},
    "ai_thrmstr_r_1": {"new_name": "ai_thrmstr_r1", "deprecated_in": "0.7.0"},
    "ai_acceld_b_ref": {"new_name": "ai_accel_db_ref", "deprecated_in": "0.7.0"},
    "ai_voltaged_b_ref": {"new_name": "ai_voltage_db_ref", "deprecated_in": "0.7.0"},
    "ai_velocity_iepe_sensord_b_ref": {
        "new_name": "ai_velocity_iepe_sensor_db_ref",
        "deprecated_in": "0.7.0",
    },
    "over_write": {"new_name": "overwrite", "deprecated_in": "0.7.0"},
    "dev_is_simulated": {
        "new_name": "is_simulated",
        "deprecated_in": "0.7.0",
    },
    "dev_serial_num": {
        "new_name": "serial_num",
        "deprecated_in": "0.7.0",
    },
    "tedshwteds_supported": {
        "new_name": "hwteds_supported",
        "deprecated_in": "0.7.0",
    },
    "expir_states_ao_type": {"new_name": "ao_output_type", "deprecated_in": "0.7.0"},
    "expir_states_co_state": {"new_name": "co_state", "deprecated_in": "0.7.0"},
    "expir_states_do_state": {"new_name": "do_state", "deprecated_in": "0.7.0"},
    "expir_states_ao_state": {"new_name": "ao_state", "deprecated_in": "0.7.0"},
}

PYTHON_CLASS_ENUM_MERGE_SET = {
    "Channel": ["_Save"],
    "InStream": ["AcquisitionType", "READ_ALL_AVAILABLE"],
    "OutStream": ["ResolutionType"],
    "Scale": ["_Save"],
    "Watchdog": ["WDTTaskAction"],
}

ATTRIBUTE_CHANGE_SET = {
    "AIChannel": {
        "ai_custom_scale_name": "ai_custom_scale",
        "ai_strain_gage_force_read_from_chan": "ai_strain_force_read_from_chan",
        "ai_eddy_current_prox_probe_sensitivity": "ai_eddy_current_prox_sensitivity",
        "ai_eddy_current_prox_probe_sensitivity_units": "ai_eddy_current_prox_sensitivity_units",
        "ai_eddy_current_prox_probe_units": "ai_eddy_current_prox_units",
        "ai_is_teds": "ai_teds_is_teds",
        "ai_rosette_strain_gage_orientation": "ai_rosette_strain_gage_gage_orientation",
    },
    "AOChannel": {"ao_custom_scale_name": "ao_custom_scale"},
    "CIChannel": {
        "ci_count_edges_count_reset_reset_count": "ci_count_edges_count_reset_reset_cnt",
        "ci_custom_scale_name": "ci_custom_scale",
        "ci_dup_count_prevent": "ci_dup_count_prevention",
        "ci_pulse_freq_start_edge": "ci_pulse_freq_starting_edge",
        "ci_pulse_ticks_start_edge": "ci_pulse_ticks_starting_edge",
        "ci_pulse_time_start_edge": "ci_pulse_time_starting_edge",
        "ci_velocity_encoder_a_input_dig_fltr_enable": "ci_velocity_a_input_dig_fltr_enable",
        "ci_velocity_encoder_a_input_dig_fltr_min_pulse_width": "ci_velocity_a_input_dig_fltr_min_pulse_width",
        "ci_velocity_encoder_a_input_dig_fltr_timebase_rate": "ci_velocity_a_input_dig_fltr_timebase_rate",
        "ci_velocity_encoder_a_input_dig_fltr_timebase_src": "ci_velocity_a_input_dig_fltr_timebase_src",
        "ci_velocity_encoder_a_input_logic_lvl_behavior": "ci_velocity_a_input_logic_lvl_behavior",
        "ci_velocity_encoder_a_input_term": "ci_velocity_a_input_term",
        "ci_velocity_encoder_a_input_term_cfg": "ci_velocity_a_input_term_cfg",
        "ci_velocity_encoder_b_input_dig_fltr_enable": "ci_velocity_b_input_dig_fltr_enable",
        "ci_velocity_encoder_b_input_dig_fltr_min_pulse_width": "ci_velocity_b_input_dig_fltr_min_pulse_width",
        "ci_velocity_encoder_b_input_dig_fltr_timebase_rate": "ci_velocity_b_input_dig_fltr_timebase_rate",
        "ci_velocity_encoder_b_input_dig_fltr_timebase_src": "ci_velocity_b_input_dig_fltr_timebase_src",
        "ci_velocity_encoder_b_input_logic_lvl_behavior": "ci_velocity_b_input_logic_lvl_behavior",
        "ci_velocity_encoder_b_input_term": "ci_velocity_b_input_term",
        "ci_velocity_encoder_b_input_term_cfg": "ci_velocity_b_input_term_cfg",
    },
    "Channel": {
        "chan_descr": "description",
        "chan_sync_unlock_behavior": "sync_unlock_behavior",
        "chan_is_global": "is_global",
        "physical_chan_name": "physical_channel",
    },
    "InStream": {
        "change_detect_has_overflowed": "change_detect_overflowed",
        "digital_lines_bytes_per_chan": "di_num_booleans_per_chan",
    },
    "OutStream": {"digital_lines_bytes_per_chan": "do_num_booleans_per_chan"},
    "Timing": {"on_demand_simultaneous_ao_enable": "simultaneous_ao_enable"},
    "Scale": {
        "type": "scale_type",
        "descr": "description",
    },
    "ExportSignals": {
        "on_demand_simultaneous_ao_enable": "simultaneous_ao_enable",
        "10_mhz_ref_clk_output_term": "exported_10_mhz_ref_clk_output_term",
        "20_mhz_timebase_output_term": "exported_20_mhz_timebase_output_term",
    },
    "ArmStartTrigger": {
        "timescale": "time_timescale",
    },
    "StartTrigger": {
        "timescale": "time_timescale",
    },
    "Device": {
        "teds_hwteds_supported": "hwteds_supported",
        "chassis_module_dev_names": "chassis_module_devices",
        "compact_daq_chassis_dev_name": "compact_daq_chassis_device",
        "compact_rio_chassis_dev_name": "compact_rio_chassis_device",
        "field_daq_bank_dev_names": "field_daq_bank_devices",
        "field_daq_dev_name": "field_daq_device",
        "ai_supported_meas_types": "ai_meas_types",
        "ao_supported_output_types": "ao_output_types",
        "ci_supported_meas_types": "ci_meas_types",
        "co_supported_output_types": "co_output_types",
    },
    "PhysicalChannel": {
        "teds_template_i_ds": "teds_template_ids",
        "ai_supported_meas_types": "ai_meas_types",
        "ao_supported_output_types": "ao_output_types",
        "ci_supported_meas_types": "ci_meas_types",
        "co_supported_output_types": "co_output_types",
    },
    "ExpirationState": {
        "ao_expir_state": "ao_state",
        "co_expir_state": "co_state",
        "do_expir_state": "do_state",
    },
    "Watchdog": {
        "expir_trig_type": "expir_trig_trig_type",
        "has_expired": "expired",
        "dig_edge_watchdog_expir_trig_edge": "expir_trig_dig_edge_edge",
        "dig_edge_watchdog_expir_trig_src": "expir_trig_dig_edge_src",
    },
    "Triggers": {"trigger_sync_type": "sync_type"},
}

ATTR_NAME_CHANGE_IN_DESCRIPTION = {
    "anlg_lvl_pause_trig_when": "anlg_lvl_when",
    "anlg_lvl_pause_trig_lvl": "anlg_lvl_lvl",
    "anlg_win_pause_trig_btm": "anlg_win_btm",
    "anlg_win_pause_trig_top": "anlg_win_top",
    "dig_pattern_pause_trig_src": "dig_pattern_src",
    "dig_pattern_pause_trig_pattern": "dig_pattern_pattern",
    "anlg_edge_ref_trig_slope": "anlg_edge_slope",
    "anlg_edge_ref_trig_slope": "anlg_edge_slope",
    "anlg_edge_ref_trig_lvl": "anlg_edge_lvl",
    "anlg_win_ref_trig_btm": "anlg_win_btm",
    "anlg_win_ref_trig_top": "anlg_win_top",
    "ref_trig_auto_trig_enable": "auto_trig_enable",
    "dig_pattern_ref_trig_src": "dig_pattern_src",
    "dig_pattern_ref_trig_pattern": "dig_pattern_pattern",
    "anlg_edge_start_trig_slope": "anlg_edge_slope",
    "anlg_edge_start_trig_lvl": "anlg_edge_lvl",
    "anlg_win_start_trig_btm": "anlg_win_btm",
    "anlg_win_start_trig_top": "anlg_win_top",
    "start_trig_delay_units": "delay_units",
    "start_trig_delay": "delay",
    "dig_pattern_start_trig_src": "dig_pattern_src",
    "dig_pattern_start_trig_pattern": "dig_pattern_pattern",
    "physical_chan_ai_supported_meas_types": "ai_supported_meas_types",
    "physical_chan_ao_supported_output_types": "ao_supported_output_types",
    "physical_chan_ci_supported_meas_types": "ci_supported_meas_types",
    "physical_chan_co_supported_output_types": "co_supported_output_types",
    "physical_chan_teds_bit_stream": "teds_bit_stream",
    "ai_eddy_current_prox_probe_sensitivity": "ai_eddy_current_prox_sensitivity",
    "ai_eddy_current_prox_probe_sensitivity_units": "ai_eddy_current_prox_sensitivity_units",
    "ci_dup_count_prevent": "ci_dup_count_prevention",
    "ai_supported_meas_types": "ai_meas_types",
    "ao_supported_output_types": "ao_output_types",
    "ci_supported_meas_types": "ci_meas_types",
    "co_supported_output_types": "co_output_types",
}


GENERIC_ATTRIBUTE_TYPE_MAP = {
    "bool32": "bool",
    "char[]": "string",
    "float64": "double",
    "uInt32": "uint32",
    "uInt64": "uint64",
    "float64[]": "double_array",
    "int32[]": "int32_array",
    "uInt8[]": "bytes",
    "uInt32[]": "uint32_array",
    "CVIAbsoluteTime": "timestamp",
}

GENERIC_ATTRIBUTE_GROUP_NAME_MAP = {
    "CalibrationInfo": "cal_info",
    "Channel": "chan",
    "ExportSignal": "exported_signal",
    "System": "system_info",
    "Trigger": "trig",
    "PhysicalChannel": "physical_chan",
}

ATTRIBUTE_WITH_FILE_PATH_TYPE = ("logging_file_path",)


def get_attributes(metadata, class_name):
    """Converts the scrapigen metadata into a list of attributes."""
    attributes_metadata = []
    for group_name, attributes in metadata["attributes"].items():
        for id, attribute_data in attributes.items():
            if (
                "python_class_name" in attribute_data
                and attribute_data["python_class_name"] == class_name
                and not attribute_data["name"] in EXCLUDED_ATTRIBUTES
            ):
                attributes_metadata.append(Attribute(id, attribute_data))
    return sorted(attributes_metadata, key=lambda x: x.name)


def get_enums_used(attributes):
    """Gets the list of enums used in the attribute metadata."""
    enums = []
    for attribute in attributes:
        if attribute.python_class_name in PYTHON_CLASS_ENUM_MERGE_SET:
            for enum_value in PYTHON_CLASS_ENUM_MERGE_SET[attribute.python_class_name]:
                enums.append(enum_value)
        if attribute.is_enum:
            enums.append(attribute.enum)
        if attribute.bitfield_enum is not None:
            enums.append(attribute.bitfield_enum)
    enums = list(set(enums))
    return sorted(enums)


def get_deprecated_attributes(attributes):
    """Gets the list of attributes to be deprecated."""
    deprecated_attributes = {}
    for old_name, attribute in DEPRECATED_ATTRIBUTES.items():
        if any(x for x in attributes if x.name == attribute["new_name"]):
            deprecated_attributes[old_name] = attribute
            matching_attribute = next(x for x in attributes if x.name == attribute["new_name"])
            deprecated_attributes[old_name]["access"] = matching_attribute.access
            deprecated_attributes[old_name]["resettable"] = matching_attribute.resettable
    return deprecated_attributes


def get_generic_attribute_function_name(attribute):
    """Gets the attribute independent interpreter function name."""
    metadata = scrapigen_metadata.attributes
    for group_name, attributes in metadata.items():
        for id, attribute_data in attributes.items():
            if attribute_data["c_function_name"] == attribute.c_function_name:
                mapped_attribute_group = GENERIC_ATTRIBUTE_GROUP_NAME_MAP.get(
                    group_name,
                    camel_to_snake_case(group_name, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES),
                )
                return mapped_attribute_group + "_attribute"


def get_generic_attribute_function_type(attribute):
    """Gets the attribute independent interpreter function type."""
    mapped_attribute_type = GENERIC_ATTRIBUTE_TYPE_MAP.get(
        attribute.type,
        camel_to_snake_case(attribute.type, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES),
    )
    if attribute.bitfield_enum:
        return mapped_attribute_type.strip("_array")
    return mapped_attribute_type


def has_attribute_with_filter(attribute, group_name, filter_name):
    """Checks if the given attribute in the group has the specified filter name in its lv_filter."""
    metadata = scrapigen_metadata.attributes
    group_attributes = metadata.get(group_name)
    if not group_attributes:
        return False
    attribute_data = group_attributes.get(attribute.id)
    if attribute_data:
        lv_filter = attribute_data.get("lv_filter")
        if lv_filter and filter_name in lv_filter:
            return True
    return False
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/utilities/enum_helpers.py sha256=2e820059b95dd0f32c1fbe253ce2c0fdfea4ad7bfc50d06ceefd9d6d9fd3a29c bytes=8462 -->
## FILE: src/codegen/utilities/enum_helpers.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/utilities/enum_helpers.py`
- sha256: `2e820059b95dd0f32c1fbe253ce2c0fdfea4ad7bfc50d06ceefd9d6d9fd3a29c`
- bytes: 8462

````python
"""Helper functions for generating constants.py."""

import html
from copy import deepcopy

# Merge enums based on the python_name.
ENUM_MERGE_SET = {
    "AccelSensitivityUnits": ["AccelSensitivityUnits1", "AccelSensitivityUnits"],
    "AccelUnits": ["AccelUnits", "AccelUnits2"],
    "AngleUnits": ["AngleUnits", "AngleUnits1", "AngleUnits2"],
    "AutoZeroType": ["AutoZeroType", "AutoZeroType1"],
    "BridgeConfiguration": ["BridgeConfiguration", "BridgeConfiguration1"],
    "CJCSource": ["CJCSource1", "CJCSource"],
    "Coupling": ["Coupling1", "Coupling2", "Coupling"],
    "CurrentShuntResistorLocation": [
        "CurrentShuntResistorLocation",
        "CurrentShuntResistorLocation1",
    ],
    "CurrentUnits": ["CurrentUnits1", "CurrentUnits"],
    "DataJustification": ["DataJustification", "DataJustification1"],
    "DigitalWidthUnits": [
        "DigitalWidthUnits",
        "DigitalWidthUnits1",
        "DigitalWidthUnits2",
        "DigitalWidthUnits3",
        "DigitalWidthUnits4",
    ],
    "Edge": ["Edge", "Edge1"],
    "FilterResponse": ["FilterResponse1", "FilterResponse"],
    "FilterType": ["FilterType", "FilterType2"],
    "LVDTSensitivityUnits": ["LVDTSensitivityUnits1", "LVDTSensitivityUnits"],
    "LengthUnits": ["LengthUnits", "LengthUnits2", "LengthUnits3"],
    "MIOAIConvertTimebaseSource": ["MIOAIConvertTimebaseSource", "MIOAIConvertTbSrc"],
    "RTDType": ["RTDType", "RTDType1"],
    "RVDTSensitivityUnits": ["RVDTSensitivityUnits", "RVDTSensitivityUnits1"],
    "ResistanceUnits": ["ResistanceUnits", "ResistanceUnits1"],
    "ResolutionType": ["ResolutionType1", "ResolutionType"],
    "ScaleType": ["ScaleType2", "ScaleType4", "ScaleType"],
    "SoundPressureUnits": ["SoundPressureUnits", "SoundPressureUnits1"],
    "StrainGageBridgeType": ["StrainGageBridgeType", "StrainGageBridgeType1"],
    "StrainUnits": ["StrainUnits", "StrainUnits1"],
    "TemperatureUnits": ["TemperatureUnits", "TemperatureUnits1"],
    "ThermocoupleType": ["ThermocoupleType", "ThermocoupleType1"],
    "Timescale": ["Timescale", "Timescale2"],
    "VoltageUnits": ["VoltageUnits", "VoltageUnits1", "VoltageUnits2"],
    "UsageTypeAI": ["UsageTypeAI", "AIMeasurementType"],
    "UsageTypeAO": ["AOOutputChannelType"],
    "UsageTypeCI": ["CIMeasurementType"],
    "DataTransferActiveTransferMode": [
        "DataTransferMechanism",
        "DataTransferActiveTransferMode",
    ],
    "TerminalConfiguration": [
        "TerminalConfiguration",
        "InputTermCfg",
        "OutputTermCfg",
        "InputTermCfg2",
    ],
    "CountDirection": ["CountDirection1"],
    "FrequencyUnits": ["FrequencyUnits2", "FrequencyUnits3"],
    "TimeUnits": ["TimeUnits2", "TimeUnits3"],
    "EncoderType": ["EncoderType2"],
    "GpsSignalType": ["GpsSignalType1"],
    "EncoderZIndexPhase": ["EncoderZIndexPhase1"],
    "Level": ["Level1", "DigitalLineState"],
    "UsageTypeCO": ["COOutputType"],
    "ActiveOrInactiveEdgeSelection": ["SampleClockActiveOrInactiveEdgeSelection"],
    "OverwriteMode": ["OverwriteMode", "OverwriteMode1"],
    "RegenerationMode": ["RegenerationMode", "RegenerationMode1"],
    "WaitMode": ["WaitMode", "WaitMode2"],
    "ExportAction": ["ExportActions", "ExportActions2", "ExportActions3", "ExportActions5"],
    "Polarity": ["Polarity", "Polarity2"],
    "TriggerType": [
        "TriggerType4",
        "TriggerType6",
        "TriggerType8",
        "TriggerType9",
        "TriggerType10",
    ],
    "DigitalPatternCondition": ["DigitalPatternCondition1"],
    "Slope": ["Slope1"],
}

# We don't need this stuff.
ENUMS_BLACKLIST = [
    "AltRef",
    "AntStatus",
    "DAQmxErrors",
    "DAQmxWarnings",
    "ExportActions",
    "GroupBy",
    "ForceIEPEUnits",
    "FilterType1",
    "LengthUnits4",
    "NavMeasurementType",
    "NavMode",
    "SaveOptions",
    "TaskControlAction",
    "Timescale",
    "WatchdogAOOutputType",
    "WatchdogControlAction",
    "VelocityUnits2",
]


# Metadata issues or invalid Python names (leading number)
NAME_SUBSTITUTIONS = {
    "100_MHZ_TIMEBASE": "ONE_HUNDRED_MHZ_TIMEBASE",
    "20_MHZ_TIMEBASE": "TWENTY_MHZ_TIMEBASE",
    "2_POINT_5_V": "TWO_POINT_FIVE_V",
    "2_WIRE": "TWO_WIRE",
    "3_POINT_3_V": "THREE_POINT_THREE_V",
    "3_WIRE": "THREE_WIRE",
    "4_WIRE": "FOUR_WIRE",
    "5_V": "FIVE_V",
    "5_WIRE": "FIVE_WIRE",
    "6_WIRE": "SIX_WIRE",
    "80_MHZ_TIMEBASE": "EIGHTY_MHZ_TIMEBASE",
    "8_MHZ_TIMEBASE": "EIGHT_MHZ_TIMEBASE",
    "US_BBULK": "USB_BULK",
    "10_MHZ_REF_CLOCK": "TEN_MHZ_REF_CLOCK",
    "20_MHZ_TIMEBASE_CLOCK": "TWENTY_MHZ_TIMEBASE_CLOCK",
    "50_OHMS": "FIFTY_OHMS",
    "75_OHMS": "SEVENTY_FIVE_OHMS",
    "1_M_OHM": "ONE_M_OHM",
    "10_G_OHMS": "TEN_G_OHMS",
    "GROUND": "GND",
}

# bitfield type enums are prefixed with '_'.
BITFIELD_ENUMS = ["CouplingTypes", "Callback", "TriggerUsageTypes", "Save", "TermCfg"]


def merge_enums(enum_name):
    """Replaces the scrapigen enum name with the actual name."""
    for actual_enum_name, alias_names in ENUM_MERGE_SET.items():
        if enum_name in alias_names:
            return actual_enum_name
    return enum_name


def _merge_enum_values(value_lists):
    result_set = {}

    for values in value_lists:
        for value in values:
            enum_value = {"name": "", "value": "", "documentation": {"description": ""}}
            enum_value["name"] = value.get("python_name", value["name"])
            enum_value["value"] = value["value"]

            if "documentation" in value and "description" in value["documentation"]:
                enum_value["documentation"]["description"] = value["documentation"].get(
                    "python_description", value["documentation"]["description"]
                )

            if enum_value["value"] not in result_set:
                result_set[enum_value["value"]] = enum_value
            elif (
                result_set[enum_value["value"]]["documentation"]["description"] == ""
                and enum_value["documentation"]["description"] != ""
            ):
                result_set[enum_value["value"]]["documentation"]["description"] = enum_value[
                    "documentation"
                ]["description"]

    return list(result_set.values())


def _merge_enum_variants(enums):
    enum_merge_set = {}

    for enum_name in enums:
        basename = enums[enum_name].get("python_name", enum_name)

        if basename is not None:
            if basename not in enum_merge_set.keys():
                enum_merge_set[basename] = []
            if enum_name not in enum_merge_set[basename]:
                enum_merge_set[basename].append(enum_name)

    for basename, enums_to_merge in enum_merge_set.items():
        enums[basename] = {
            "values": _merge_enum_values([enums[enum]["values"] for enum in enums_to_merge])
        }
        # delete the variants, now
        for enum in enums_to_merge:
            if not enum == basename:
                del enums[enum]

        if basename in BITFIELD_ENUMS:
            enums["_" + basename] = enums.pop(basename)

    # sort it by key (enum name)
    return dict(sorted(enums.items()))


def _sanitize_values(enums):
    for _, enum in enums.items():
        for value in enum["values"]:
            if value["name"] in NAME_SUBSTITUTIONS:
                value["name"] = NAME_SUBSTITUTIONS[value["name"]]
    return enums


def get_enums(metadata):
    """Formats and removes Blacklisted enums."""
    enums = deepcopy(metadata["enums"])

    # First remove enums we don't use.
    enums = {name: val for (name, val) in enums.items() if name not in ENUMS_BLACKLIST}
    # Then merge variants.
    enums = _merge_enum_variants(enums)
    return _sanitize_values(enums)


def get_enum_value_docstring(raw_docstring):
    """Formats enum docstrings."""
    raw_docstring = html.unescape(raw_docstring)

    raw_docstring = _cleanup_docstring(raw_docstring)

    if raw_docstring != "":
        return f"  #: {raw_docstring}"
    return ""


def _cleanup_docstring(docstring):
    # Removing leading/trailing whitespace.
    stripped = docstring.strip()

    # Some strings have extraneous spaces between words; clean those up.
    words = stripped.split()
    return " ".join(words)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/utilities/function_helpers.py sha256=8034ae7f4ab9c8342bf55058876c7bb9fa7fb9afec79f0cc76a56334635d0b55 bytes=13139 -->
## FILE: src/codegen/utilities/function_helpers.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/utilities/function_helpers.py`
- sha256: `8034ae7f4ab9c8342bf55058876c7bb9fa7fb9afec79f0cc76a56334635d0b55`
- bytes: 13139

````python
"""This contains the helper methods used in functions generation."""

import os
from copy import deepcopy

from codegen.functions.function import Function
from codegen.utilities.helpers import camel_to_snake_case

FUNCTION_NAME_CHANGE_SET = {
    "TEDSAIRTD": "TEDS_AI_RTD",
    "TEDSAI": "TEDS_AI",
    "AIRTD": "AI_RTD",
    "CIGPS": "CI_GPS",
}

EXCLUDED_FUNCTIONS = [
    "AddNetworkDevice",
    "DeleteNetworkDevice",
    "ReserveNetworkDevice",
    "UnreserveNetworkDevice",
    "AddCDAQSyncConnection",
    "AreConfiguredCDAQSyncPortsDisconnected",
    "AutoConfigureCDAQSyncConnections",
    "GetAnalogPowerUpStates",
    "GetAnalogPowerUpStatesWithOutputType",
    "GetAutoConfiguredCDAQSyncConnections",
    "GetDigitalLogicFamilyPowerUpState",
    "GetDigitalPowerUpStates",
    "GetDigitalPullUpPullDownStates",
    "GetDisconnectedCDAQSyncPorts",
    "RemoveCDAQSyncConnection",
    "SetAnalogPowerUpStates",
    "SetAnalogPowerUpStatesWithOutputType",
    "SetDigitalLogicFamilyPowerUpState",
    "SetDigitalPowerUpStates",
    "SetDigitalPullUpPullDownStates",
]

FUNCTIONS_WITH_LIST_DEFAULT = [
    "add_ai_force_bridge_polynomial_chan",
    "add_ai_force_bridge_table_chan",
    "add_ai_pressure_bridge_polynomial_chan",
    "add_ai_pressure_bridge_table_chan",
    "add_ai_torque_bridge_polynomial_chan",
    "add_ai_torque_bridge_table_chan",
]


def get_functions(metadata, class_name=""):
    """Converts the scrapigen metadata into a list of functions."""
    all_functions = deepcopy(metadata["functions"])
    functions_metadata = []
    for function_name, function_data in all_functions.items():
        if function_data.get("python_codegen_method") or function_name in EXCLUDED_FUNCTIONS:
            continue
        if (
            "python_class_name" in all_functions[function_name]
            and all_functions[function_name]["python_class_name"] == class_name
        ) or class_name == "":
            function_data["c_function_name"] = function_name
            functions_metadata.append(Function(get_function_name(function_name), function_data))

    return sorted(functions_metadata, key=lambda x: x._function_name)


def get_function_name(function_name: str):
    """Performs naming substitutions and converts function name from camel to snake case."""
    if function_name.startswith("Create"):
        function_name = "add" + function_name[6:]

    for actual_names, alias_names in FUNCTION_NAME_CHANGE_SET.items():
        if actual_names in function_name:
            function_name = function_name.replace(actual_names, alias_names)

    return camel_to_snake_case(function_name)


def get_enums_used(functions):
    """Gets the list of enums used in the functions metadata."""
    used_enums = []
    for function_data in functions:
        for param in function_data._parameters:
            if param.is_enum:
                used_enums.append(param._python_data_type)
        used_enums = list(set(used_enums))

    return sorted(used_enums)


def order_function_parameters_by_optional(function_parameters):
    """Sorts optional parameters and non optional parameters for function definition."""
    optional_params = []
    non_optional_params = []
    for param in function_parameters:
        if param._optional:
            optional_params.append(param)
        else:
            non_optional_params.append(param)

    return non_optional_params + optional_params


def get_parameter_signature(is_python_factory, sorted_params):
    """Gets parameter signature for function definition."""
    params_with_defaults = []
    if not is_python_factory:
        params_with_defaults.append("self")
    for param in sorted_params:
        param_type = ""
        param_default = param.default
        if is_path_type(param):
            param_type = ": str | pathlib.PurePath | None"
            param_default = "None"
        if param._optional:
            params_with_defaults.append(f"{param.parameter_name}{param_type}={param_default}")
        else:
            params_with_defaults.append(f"{param.parameter_name}{param_type}")

    return ", ".join(params_with_defaults)


def get_parameters_docstring_lines_length(input_param):
    """Gets First line and length of parameter docstring."""
    # The textwrap module leaves a minimum of 1 word on the first line. We need to
    # work around this if "param name" + "param data type docstring" is too long.

    python_type_annotation = input_param.python_type_annotation
    if is_path_type(input_param):
        # file path parameter has type hints,
        # does not need to specify type in docstring
        python_type_annotation = ""

    # Script docstring on first line after param name and type if the following is True.
    initial_len = 17 + len(input_param.parameter_name) + len(python_type_annotation)

    # If length of whitespace + length of param name + length of data type docstring +
    # length of first word in docstring > docstring max line width.
    first_line = (
        True if (initial_len + len(input_param.description.split(" ", 1)[0])) <= 72 else False
    )

    return initial_len, first_line


def get_instantiation_lines(function_parameters):
    """Gets the instantiation lines of parameters docstrings."""
    instantiation_lines = []
    for param in function_parameters:
        if param.direction == "in":
            if param.is_list:
                if param.ctypes_data_type.startswith("numpy."):
                    if param.is_enum:
                        instantiation_lines.append(
                            "{0} = numpy.array([p.value for p in {0}], dtype={1})".format(
                                param.parameter_name, param.ctypes_data_type
                            )
                        )
                    else:
                        instantiation_lines.append(
                            "{0} = numpy.array({0}, dtype={1})".format(
                                param.parameter_name, param.ctypes_data_type
                            )
                        )
                else:
                    instantiation_lines.append(
                        "{0} = {1}({0})".format(param.parameter_name, param.ctypes_data_type)
                    )
        else:
            if not param.has_explicit_buffer_size:
                instantiation_lines.append(f"{param.parameter_name} = {param.ctypes_data_type}()")
    return instantiation_lines


def get_arguments_type(functions_metadata):
    """Gets the 'type' of parameters."""
    argtypes = []
    is_read_write_function = functions_metadata.python_codegen_method in (
        "CustomCode_Read",
        "CustomCode_Write",
    )

    if is_read_write_function:
        argtypes.append("lib_importer.task_handle")

    if functions_metadata.handle_parameter is not None:
        if functions_metadata.handle_parameter.ctypes_data_type != "ctypes.c_char_p":
            argtypes.append(functions_metadata.handle_parameter.ctypes_data_type)
        else:
            argtypes.append("ctypes_byte_str")

    size_param_info = tuple()
    for param in functions_metadata.parameters:
        argtypes.append(to_param_argtype(param))

        if param.has_explicit_buffer_size:
            # Removing previously added argument type of the size parameter if the same size
            # parameter is used by another parameter in the same function. In such cases the
            # size parameter argument definition should always come after the last parameter
            # that is using the size argument.
            if param.size.mechanism == "custom-code":
                continue
            if len(size_param_info) != 0:
                size_param, parameter_index = size_param_info
                if size_param.size == param.size:
                    del argtypes[parameter_index]
                    size_param_info = tuple()
            argtypes.append("ctypes.c_uint")
            size_param_info = param, (len(argtypes) - 1)

    # The argument type for 'reserved' parameter is inserted at
    # end of list for all read/write functions.
    if is_read_write_function:
        argtypes.append("ctypes.POINTER(c_bool32)")

    return argtypes


def to_param_argtype(parameter):
    """Formats argument types."""
    flags = "'C','W'" if parameter.direction == "out" else "'C'"
    if parameter.is_list:
        if parameter.ctypes_data_type == "numpy.bool":
            return f"wrapped_ndpointer(dtype=bool, flags=({flags}))"
        return f"wrapped_ndpointer(dtype={parameter.ctypes_data_type}, flags=({flags}))"
    else:
        if parameter.ctypes_data_type == "ctypes.TaskHandle":
            return "lib_importer.task_handle"
        elif parameter.python_data_type == "datetime":
            if parameter.direction == "in":
                return "AbsoluteTime"
            else:
                return f"ctypes.POINTER(AbsoluteTime)"
        elif parameter.direction == "in":
            # If is string input parameter, use separate custom
            # argtype to convert from unicode to bytes.
            if parameter.ctypes_data_type == "ctypes.c_char_p":
                return "ctypes_byte_str"
            elif parameter.python_data_type == "timestampEvent":
                return "ctypes.c_int32"
            else:
                return parameter.ctypes_data_type or parameter.python_data_type
        else:
            if parameter.ctypes_data_type == "ctypes.c_char_p":
                return parameter.ctypes_data_type
            else:
                return f"ctypes.POINTER({parameter.ctypes_data_type})"


def get_explicit_output_param(output_parameters):
    """Gets the explicit output parameters."""
    explicit_output_params = [p for p in output_parameters if p.has_explicit_buffer_size]
    if len(explicit_output_params) > 1:
        raise NotImplementedError(
            "There is more than one output parameter with an explicit "
            "buffer size. This cannot be handled by this template because it "
            'calls the C function once with "buffer_size = 0" to get the '
            "buffer size from the returned integer, which is normally an "
            "error code.{0}{0}".format(os.linesep)
            + "Output parameters with explicit buffer sizes: {}".format(explicit_output_params)
        )
    if len(explicit_output_params) == 1:
        return explicit_output_params[0]
    return None


def generate_function_call_args(function_metadata):
    """Gets function call arguments."""
    function_call_args = []
    if function_metadata.handle_parameter is not None:
        function_call_args.append(function_metadata.handle_parameter.accessor)

    sorted_params = order_function_parameters_by_optional(function_metadata.parameters)

    for param in sorted_params:
        if param.direction == "in":
            if param.is_enum and not param.is_list:
                function_call_args.append(f"{param.parameter_name}.value")
            elif is_path_type(param):
                function_call_args.append(f"str({param.parameter_name})")
            else:
                function_call_args.append(param.parameter_name)
        else:
            if param.has_explicit_buffer_size:
                function_call_args.append(param.parameter_name)
                function_call_args.append("temp_size")
            else:
                function_call_args.append(f"ctypes.byref({param.parameter_name})")

    if function_metadata.calling_convention == "Cdecl":
        function_call_args.append("None")

    return function_call_args


def instantiate_explicit_output_param(param):
    """Gets instantiate lines for output parameters."""
    if param.is_list:
        return "{} = numpy.zeros(temp_size, dtype={})".format(
            param.parameter_name, param.ctypes_data_type
        )
    elif param.ctypes_data_type == "ctypes.c_char_p":
        return f"{param.parameter_name} = ctypes.create_string_buffer(temp_size)"


def get_list_default_value(func, param):
    """Gets the default value for list parameters."""
    if func.function_name in FUNCTIONS_WITH_LIST_DEFAULT:
        if param.parameter_name == "forward_coeffs":
            return "[0.0, 50]"
        elif param.parameter_name == "reverse_coeffs":
            return "[0.0, 0.02]"
        elif param.parameter_name == "electrical_vals":
            return "[-2.0, 0.0, 2.0]"
        elif param.parameter_name == "physical_vals":
            return "[-100.0, 0.0, 100.0]"
        else:
            raise RuntimeError(
                f'Unable to find parameter name while getting list default value for "{func.function_name}"'
            )
    else:
        return "[]"


def is_path_type(input_param):
    """Check is the parameter a file path."""
    return "file_path" in input_param.parameter_name and input_param.python_data_type == "str"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/utilities/helpers.py sha256=eda2e9f67968a2002ad9f33c6d10545706cb567ecbd4874f91244bdd4d58e3a3 bytes=4064 -->
## FILE: src/codegen/utilities/helpers.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/utilities/helpers.py`
- sha256: `eda2e9f67968a2002ad9f33c6d10545706cb567ecbd4874f91244bdd4d58e3a3`
- bytes: 4064

````python
"""Helpers class to generate helper functions for the metadata."""

import re
from collections import namedtuple
from enum import Enum

# Pre-compile regexes to speed up matches
CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
    re.compile("([^_0-9])([0-9])"),
]

PascalTokenSubstitution = namedtuple(
    "PascalTokenSubstitution", ["pascal_representation", "preferred_representation"]
)

SPECIAL_CASE_PASCAL_TOKENS = [
    # NI uses UInt, not Uint, and never U_INT when converting to snake.
    PascalTokenSubstitution("Uint", "UInt"),
    PascalTokenSubstitution("Id", "ID"),
]

NAME_CHANGE_SET = {
    "cdaq": "CDAQ",
    "ao": "AO",
    "ai": "AI",
    "co": "CO",
    "do": "DO",
    "teds": "TEDS",
    "iepe": "IEPE",
    "rms": "RMS",
    "dc": "DC",
    "lvdt": "LVDT",
    "rvdt": "RVDT",
    "airtd": "AIRTD",
    "ci": "CI",
    "di": "DI",
    "cigps": "CIGPS",
    "tedsai": "TEDSAI",
    "tedsairtd": "TEDSAIRTD",
}


def camel_to_snake_case(camel_case_string, regexes=CAMEL_TO_SNAKE_CASE_REGEXES):
    """Converts a camelCase string to a snake_case string."""
    partial = camel_case_string
    for regex in regexes:
        partial = regex.sub(r"\1_\2", partial)

    return partial.lower()


def get_enums_to_import(enums_in_attributes, enums_in_functions):
    """Gets the enums that needs to imported for the attributes and functions used."""
    enums_to_import = enums_in_attributes + enums_in_functions
    enums_to_import = list(set(enums_to_import))
    return sorted(enums_to_import)


def strip_class_name(name: str, class_name: str, replace_with=""):
    """Strips class name from name."""
    return re.sub(class_name, replace_with, name)


def snake_to_pascal(snake_string):
    """Return a PascalString for a given snake_string."""
    snake_string = _modify_function_name(snake_string)
    snake_string = list(snake_string)
    index = 0
    snake_string[index] = snake_string[index].upper()
    for x in snake_string:
        if x == "_":
            snake_string[index + 1] = snake_string[index + 1].upper()
            del snake_string[index]
        index = index + 1
    result = "".join(snake_string)
    return _insert_special_case_pascal_tokens(result)


# TODO: Replace with str.removeprefix() when dropping Python 3.8.
def removeprefix(input, prefix):
    """Returns the input string with the prefix string removed.

    If the given prefix string is not present in the input string,
    then the input string is directly returned.
    """
    return input[len(prefix) :] if input.startswith(prefix) else input


def _insert_special_case_pascal_tokens(normal_pascal_string: str) -> str:
    for pascal_token, special_case_override in SPECIAL_CASE_PASCAL_TOKENS:
        normal_pascal_string = normal_pascal_string.replace(pascal_token, special_case_override)
    return normal_pascal_string


def _modify_function_name(snake_string):
    function_names = snake_string.split("_")
    substituted_name = []
    for name in function_names:
        if name in NAME_CHANGE_SET:
            substituted_name.append(NAME_CHANGE_SET[name])
        else:
            substituted_name.append(name)
    return "_".join(substituted_name)


class AttributeFunctionType(Enum):
    """Enum specifies whether the function is get/set/reset/not an attribute function."""

    GET = 0
    SET = 1
    RESET = 2
    NONE = 3


def get_attribute_function_type(function_name: str):
    """Sets attribute function type as get/set/reset or not a attribute function."""
    if "attribute" in function_name:
        if function_name.startswith("get"):
            return AttributeFunctionType.GET
        elif function_name.startswith("set"):
            return AttributeFunctionType.SET
        elif function_name.startswith("reset"):
            return AttributeFunctionType.RESET

    return AttributeFunctionType.NONE
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/utilities/interpreter_helpers.py sha256=6baf47b528d0939e651818a13e2521dad0a3724f5321b5a19635703487568b19 bytes=29885 -->
## FILE: src/codegen/utilities/interpreter_helpers.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/utilities/interpreter_helpers.py`
- sha256: `6baf47b528d0939e651818a13e2521dad0a3724f5321b5a19635703487568b19`
- bytes: 29885

````python
"""This contains the helper methods used in interpreter generation."""

import os
import re
from copy import deepcopy

from codegen.functions.function import Function
from codegen.utilities.function_helpers import to_param_argtype
from codegen.utilities.helpers import (
    AttributeFunctionType,
    camel_to_snake_case,
    removeprefix,
)

# This custom regex list doesn't split the string before the number.
INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
]

INTERPRETER_IGNORED_FUNCTIONS = [
    "GetExtendedErrorInfo",
    # nidaqmx-python uses Get/SetBufferAttribute.
    "CfgInputBuffer",
    "CfgOutputBuffer",
    # nidaqmx-python uses GetTaskAttributeString and splits the comma-delimited string.
    "GetNthTaskChannel",
    "GetNthTaskDevice",
    "GetNthTaskReadChannel",
    # nidaqmx-python uses CreateWatchdogTimerTaskEx.
    "CreateWatchdogTimerTask",
    # AI channel calibration
    "GetAIChanCalCalDate",
    "GetAIChanCalExpDate",
    "SetAIChanCalCalDate",
    "SetAIChanCalExpDate",
    # Real-time
    "GetRealTimeAttributeBool",
    "GetRealTimeAttributeInt32",
    "GetRealTimeAttributeUInt32",
    "ResetRealTimeAttribute",
    "SetRealTimeAttributeBool",
    "SetRealTimeAttributeInt32",
    "SetRealTimeAttributeUInt32",
    "WaitForNextSampleClock",
    # Time triggers
    # Single-attribute get/set functions are not used
    # Generic Get/SetTimingAttribute{Type} functions are used instead
    "GetArmStartTrigTimestampVal",
    "GetArmStartTrigTrigWhen",
    "GetFirstSampClkWhen",
    "GetFirstSampTimestampVal",
    "GetRefTrigTimestampVal",
    "GetStartTrigTimestampVal",
    "GetStartTrigTrigWhen",
    "GetSyncPulseTimeWhen",
    "GetTimingAttributeExTimestamp",
    "SetArmStartTrigTrigWhen",
    "SetFirstSampClkWhen",
    "SetStartTrigTrigWhen",
    "SetSyncPulseTimeWhen",
    "SetTimingAttributeExTimestamp",
    "SetTimingAttributeTimestamp",
    # Deprecated, not working
    "GetAnalogPowerUpStates",
]

GRPC_INTERPRETER_IGNORED_FUNCTIONS = [
    "get_error_string",
    "read_id_pin_memory",
    "set_runtime_environment",
    "internal_get_last_created_chan",
]

LIBRARY_INTERPRETER_IGNORED_FUNCTIONS = [
    "get_error_string",
    "read_id_pin_memory",
    "read_power_binary_i16",
    "read_power_f64",
    "read_raw",
    "write_raw",
]

INCLUDE_SIZE_PARAMETER_IN_SIGNATURE_FUNCTIONS = [
    "get_analog_power_up_states_with_output_type",
]

INCLUDE_SIZE_HINT_FUNCTIONS = [
    "get_read_attribute_string",
    "get_write_attribute_string",
]

MODIFIED_INTERPRETER_PARAMS = {
    "r_0": "r0",
    "r_1": "r1",
}

EVENT_UNREGISTER_IGNORED_PARAMS = [
    "callback_data",
    "callback_function",
    "n_samples",
    "options",
]

READ_SAMPLES_PARAMETER_NAMES = [
    "samps_read",
    "samps_per_chan_read",
    "num_samps_per_chan",
]


def get_interpreter_functions(metadata):
    """Converts the scrapigen metadata into a list of functions."""
    all_functions = deepcopy(metadata["functions"])
    functions_metadata = []
    for function_name, function_data in all_functions.items():
        if function_name in INTERPRETER_IGNORED_FUNCTIONS:
            continue
        function_data["c_function_name"] = function_name
        function_name = camel_to_snake_case(function_name, INTERPRETER_CAMEL_TO_SNAKE_CASE_REGEXES)
        function_name = function_name.replace("_u_int", "_uint")
        functions_metadata.append(
            Function(
                function_name,
                function_data,
            )
        )
    return sorted(functions_metadata, key=lambda x: x._function_name)


def generate_interpreter_function_call_args(function_metadata):
    """Gets function call arguments."""
    function_call_args = []
    size_values = {}
    interpreter_parameters = get_interpreter_parameters(function_metadata)
    for param in interpreter_parameters:
        if param.has_explicit_buffer_size:
            if param.direction == "in":
                size_values[param.size.value] = f"len({param.parameter_name})"
            elif param.direction == "out":
                if param.size.mechanism == "ivi-dance":
                    size_values[param.size.value] = "temp_size"
                elif (
                    is_custom_read_write_function(function_metadata)
                    and param.has_explicit_buffer_size
                ):
                    if param.size.mechanism == "passed-in":
                        size_values[param.size.value] = f"{param.parameter_name}.size"

    for param in interpreter_parameters:
        if param.parameter_name in size_values:
            function_call_args.append(size_values[param.parameter_name])
        elif param.parameter_name == "reserved":
            function_call_args.append("None")
        elif is_event_function(function_metadata) and param.parameter_name == "callback_function":
            function_call_args.append("callback_method_ptr")
        elif param.direction == "out" or (
            param.is_pointer and param.parameter_name != "callback_data"
        ):
            if param.has_explicit_buffer_size:
                if (
                    is_numpy_array_datatype(param)
                    and function_metadata.attribute_function_type == AttributeFunctionType.GET
                ):
                    function_call_args.append(
                        f"{param.parameter_name}.ctypes.data_as(ctypes.c_void_p)"
                    )
                else:
                    function_call_args.append(param.parameter_name)
            else:
                function_call_args.append(f"ctypes.byref({param.parameter_name})")
        elif param.direction == "in":
            if param.type == "CVIAbsoluteTime":
                function_call_args.append(f"AbsoluteTime.from_datetime({param.parameter_name})")
            elif (
                param.parameter_name == "value"
                and function_metadata.attribute_function_type == AttributeFunctionType.SET
            ):
                function_call_args.append(type_cast_attribute_set_function_parameter(param))
            else:
                function_call_args.append(param.parameter_name)

    return function_call_args


def get_argument_types(functions_metadata):
    """Gets the 'type' of parameters."""
    argtypes = []
    interpreter_parameters = get_interpreter_parameters(functions_metadata)
    size_params = _get_size_params(interpreter_parameters)
    for param in interpreter_parameters:
        # Skipping the c arguments of these parameters in attribute functions
        # to remove the variadic arguments.
        if (
            param.parameter_name in ("value", "size")
            and functions_metadata.attribute_function_type != AttributeFunctionType.NONE
        ):
            continue
        if _is_handle_parameter(functions_metadata, param):
            if functions_metadata.handle_parameter.ctypes_data_type != "ctypes.c_char_p":
                if param.direction == "in":
                    argtypes.append(functions_metadata.handle_parameter.ctypes_data_type)
                else:
                    argtypes.append(
                        f"ctypes.POINTER({functions_metadata.handle_parameter.ctypes_data_type})"
                    )
            else:
                argtypes.append("ctypes_byte_str")
        elif param.parameter_name in size_params:
            if param.direction == "out" or param.is_pointer:
                argtypes.append("ctypes.POINTER(ctypes.c_uint)")
            else:
                argtypes.append("ctypes.c_uint")
        else:
            if param.is_pointer:
                argtypes.append(f"ctypes.POINTER({to_param_argtype(param)})")
            else:
                argtypes.append(to_param_argtype(param))
    return argtypes


def get_interpreter_parameter_signature(is_python_factory, params):
    """Gets parameter signature for function definition."""
    params_with_defaults = []
    if not is_python_factory:
        params_with_defaults.append("self")
    for param in params:
        if param.type:
            params_with_defaults.append(param.parameter_name)

    return ", ".join(params_with_defaults)


def get_instantiation_lines_for_output(func):
    """Gets the lines of code for instantiation of output values."""
    instantiation_lines = []
    if func.is_init_method:
        instantiation_lines.append(f"task = lib_importer.task_handle(0)")
    for param in get_interpreter_output_params(func):
        if param.parameter_name == "task":
            continue
        elif param.repeating_argument:
            instantiation_lines.append(f"{param.parameter_name} = []")
        elif param.has_explicit_buffer_size:
            if is_custom_read_write_function(func) and param.size.mechanism == "passed-in":
                continue
            if (
                param.size.mechanism == "passed-in" or param.size.mechanism == "passed-in-by-ptr"
            ) and param.is_list:
                instantiation_lines.append(
                    f"{param.parameter_name} = numpy.zeros({param.size.value}, dtype={param.ctypes_data_type})"
                )
            elif param.size.mechanism == "custom-code":
                instantiation_lines.append(f"size = {param.size.value}")
                instantiation_lines.append(
                    f"{param.parameter_name} = numpy.zeros(size, dtype={param.ctypes_data_type})"
                )
        elif param.type == "CVIAbsoluteTime":
            instantiation_lines.append(f"{param.parameter_name} = AbsoluteTime()")
        else:
            instantiation_lines.append(f"{param.parameter_name} = {param.ctypes_data_type}()")
    for param in get_interpreter_in_out_params(func):
        if param.parameter_name == "reserved" or param.parameter_name == "callback_data":
            continue
        instantiation_lines.append(
            f"{param.parameter_name} = {param.ctypes_data_type}({param.parameter_name})"
        )
    return instantiation_lines


def get_instantiation_lines_for_varargs(func):
    """Gets instantiation lines for functions with variable arguments."""
    instantiation_lines = []
    if any(get_varargs_parameters(func)):
        for param in func.output_parameters:
            instantiation_lines.append(
                f"{param.parameter_name}_element = {param.ctypes_data_type}()"
            )
            instantiation_lines.append(
                f"{param.parameter_name}.append({param.parameter_name}_element)"
            )
    return instantiation_lines


def get_argument_definition_lines_for_varargs(varargs_params):
    """Gets the lines for defining the variable arguments for a function."""
    argument_definition_lines = []
    for param in varargs_params:
        argtype = to_param_argtype(param)
        if param.direction == "in":
            argument_definition_lines.append(f"args.append({param.parameter_name}[index])")
        else:
            argument_definition_lines.append(
                f"args.append(ctypes.byref({param.parameter_name}_element))"
            )
        argument_definition_lines.append(f"argtypes.append({argtype})")
        argument_definition_lines.append("")
    return argument_definition_lines


def get_varargs_parameters(func):
    """Gets variable arguments of a function."""
    return [p for p in func.parameters if p.repeating_argument]


def get_params_for_function_signature(func, is_grpc_interpreter=False):
    """Gets interpreter parameters for the function signature."""
    interpreter_parameters = []
    function_parameters = get_interpreter_parameters(func, is_grpc_interpreter)
    size_params = _get_size_params(function_parameters)
    for param in function_parameters:
        if (
            param.parameter_name in size_params or param.parameter_name == "reserved"
        ) and func.function_name not in INCLUDE_SIZE_PARAMETER_IN_SIGNATURE_FUNCTIONS:
            continue
        if (
            is_event_unregister_function(func)
            and param.parameter_name in EVENT_UNREGISTER_IGNORED_PARAMS
        ):
            continue
        if param.direction == "in":
            interpreter_parameters.append(param)
        elif is_custom_read_write_function(func) and param.has_explicit_buffer_size:
            if param.size.mechanism == "passed-in":
                interpreter_parameters.append(param)
    return interpreter_parameters


def get_grpc_interpreter_call_params(func, params):
    """Gets the interpreter parameters for grpc request."""
    compound_params = get_input_arguments_for_compound_params(func)
    is_read_function = is_custom_read_function(func)
    is_write_function = is_custom_write_function(func)
    grpc_params = []
    has_read_array_parameter = False
    for param in params:
        if not param.include_in_proto:
            continue
        if param.parameter_name not in compound_params:
            name = param.parameter_name
            if param.parameter_name in MODIFIED_INTERPRETER_PARAMS:
                name = MODIFIED_INTERPRETER_PARAMS.get(param.parameter_name)
            if is_read_function and "read_array" in name:
                if has_read_array_parameter:
                    continue
                if is_read_bytes_param(param):
                    grpc_params.append(
                        f"{camel_to_snake_case(param.size.value)}={param.parameter_name}.nbytes"
                    )
                else:
                    grpc_params.append(
                        f"{camel_to_snake_case(param.size.value)}={param.parameter_name}.size"
                    )
                has_read_array_parameter = True
            elif param.is_grpc_enum or (param.is_enum and not param.is_list):
                grpc_params.append(f"{name}_raw={param.parameter_name}")
            elif param.type == "CVIAbsoluteTime":
                grpc_params.append(f"{name}=convert_time_to_timestamp({param.parameter_name})")
            else:
                if is_write_bytes_param(param):
                    grpc_params.append(f"{name}={param.parameter_name}.tobytes()")
                elif is_write_function:
                    grpc_params.append(get_write_array_param(param))
                else:
                    grpc_params.append(f"{name}={param.parameter_name}")

    if func.is_init_method:
        grpc_params.append("initialization_behavior=self._grpc_options.initialization_behavior")
    return ", ".join(grpc_params)


def get_output_param_with_ivi_dance_mechanism(func):
    """Gets the output parameters with explicit buffer size."""
    output_parameters = get_output_params(func)
    explicit_output_params = [p for p in output_parameters if p.has_explicit_buffer_size]
    params_with_ivi_dance_mechanism = [
        p for p in explicit_output_params if p.size.mechanism == "ivi-dance"
    ]
    if len(params_with_ivi_dance_mechanism) > 1:
        raise NotImplementedError(
            "There is more than one output parameter with an explicit "
            "buffer size that follows ivi dance mechanism."
            "This cannot be handled by this template because it "
            'calls the C function once with "buffer_size = 0" to get the '
            "buffer size from the returned integer, which is normally an "
            "error code.{0}{0}".format(os.linesep)
            + "Output parameters with explicit buffer sizes: {}".format(
                params_with_ivi_dance_mechanism
            )
        )

    if len(params_with_ivi_dance_mechanism) == 1:
        return params_with_ivi_dance_mechanism[0]
    return None


def has_parameter_with_ivi_dance_size_mechanism(func):
    """Returns true if the function has a parameter with ivi dance size mechanism."""
    parameter_with_size_buffer = get_output_param_with_ivi_dance_mechanism(func)
    return parameter_with_size_buffer is not None


def is_custom_read_write_function(func):
    """Returns True if the function is a read or write function."""
    return func.python_codegen_method in ("CustomCode_Read", "CustomCode_Write")


def is_custom_read_function(func):
    """Returns True if the function is a read function."""
    return func.python_codegen_method == "CustomCode_Read"


def is_custom_write_function(func):
    """Returns True if the function is a write function."""
    return func.python_codegen_method == "CustomCode_Write"


def get_interpreter_output_params(func):
    """Gets the output parameters for the functions in interpreter."""
    return [p for p in get_interpreter_parameters(func) if p.direction == "out"]


def get_output_params(func):
    """Gets output parameters for the function."""
    return [p for p in func.base_parameters if p.direction == "out"]


def get_interpreter_in_out_params(func):
    """Gets the input parameters that are also pointers for the function."""
    return [p for p in get_interpreter_parameters(func) if p.direction == "in" and p.is_pointer]


def get_return_values(func):
    """Gets the values to add to return statement of the function."""
    return_values = []
    for param in get_interpreter_output_params(func):
        is_read_write_function = is_custom_read_write_function(func)
        if param.repeating_argument:
            return_values.append(
                f"[{param.parameter_name}_element.value for {param.parameter_name}_element in {param.parameter_name}]"
            )
        elif param.ctypes_data_type == "ctypes.c_char_p":
            return_values.append(f"{param.parameter_name}.value.decode(lib_importer.encoding)")
        elif param.is_list:
            if is_read_write_function:
                return_values.append(param.parameter_name)
            else:
                return_values.append(f"{param.parameter_name}.tolist()")
        elif param.type == "TaskHandle":
            return_values.append(param.parameter_name)
        elif param.type == "CVIAbsoluteTime":
            return_values.append(f"{param.parameter_name}.to_datetime()")
        else:
            return_values.append(f"{param.parameter_name}.value")
    if func.is_init_method:
        return_values.append("new_session_initialized")
    return return_values


def get_c_function_call_template(func):
    """Gets the template to use for generating the logic of calling the c functions."""
    if is_event_function(func):
        return "/event_function_call.py.mako"
    elif any(get_varargs_parameters(func)):
        return "/exec_cdecl_c_function_call.py.mako"
    elif has_parameter_with_ivi_dance_size_mechanism(func):
        return "/double_c_function_call.py.mako"
    return "/default_c_function_call.py.mako"


def get_grpc_function_call_template(func):
    """Gets the template to use for generating the logic of calling the grpc functions."""
    if func.stream_response:
        return "/event_function_call.py.mako"
    else:
        return "/default_grpc_function_call.py.mako"


def get_callback_func_param(func):
    """Gets the callback_function parameter."""
    return next(p for p in func.base_parameters if p.parameter_name == "callback_function")


def get_callback_data_param(func):
    """Gets the callback_data parameter."""
    return next(p for p in func.base_parameters if p.parameter_name == "callback_data")


def get_callback_function_call_args(func):
    """Gets the parameters used in the callback function call."""
    callback_func_param = get_callback_func_param(func)
    callback_func_args = []
    for param in callback_func_param.callback_params:
        name = camel_to_snake_case(param["name"])
        if name == "task":
            callback_func_args.append(f"{name}")
        elif "enum" in param:
            callback_func_args.append(f"response.{name}_raw")
        else:
            callback_func_args.append(f"response.{name}")

    callback_func_args.append("callback_data")
    return callback_func_args


def get_callback_param_data_types(func):
    """Gets the data types for call back function parameters."""
    callback_func_param = get_callback_func_param(func)
    callback_data_param = get_callback_data_param(func)
    # callback_param_types: [result_type, [**ctypes_data_type** of callback_params],
    # **ctypes_data_type** of callback_data_param]
    return (
        ["ctypes.c_int32"]
        + [p["ctypes_data_type"] for p in callback_func_param.callback_params]
        + [callback_data_param.ctypes_data_type]
    )


def is_event_function(func):
    """Returns True if this is an event register/unregister function, False otherwise."""
    return is_event_register_function(func) or is_event_unregister_function(func)


def is_event_register_function(func):
    """Returns True if this is an event register function, False otherwise."""
    return func.function_name.startswith("register_")


def is_event_unregister_function(func):
    """Returns True if this is an event unregister function, False otherwise."""
    return func.function_name.startswith("unregister_")


def get_event_name(func):
    """Gets the event name for an event register/unregister function."""
    if is_event_register_function(func):
        return removeprefix(func.function_name, "register_")
    elif is_event_unregister_function(func):
        return removeprefix(func.function_name, "unregister_")
    else:
        raise ValueError(f"{func.function_name} is not an event function.")


def get_compound_parameter(params):
    """Returns the compound parameter associated with the given function."""
    return next((x for x in params if x.is_compound_type), None)


def get_input_arguments_for_compound_params(func):
    """Returns a list of input parameter for creating the compound parameter."""
    compound_params = []
    if any(x for x in func.base_parameters if x.is_compound_type):
        for parameter in func.base_parameters:
            if parameter.direction == "in" and parameter.repeating_argument:
                compound_params.append(parameter.parameter_name)
    return compound_params


def create_compound_parameter_request(func):
    """Gets the input parameters for creating the compound type parameter."""
    parameters = []
    compound_parameter_type = ""
    for parameter in func.base_parameters:
        if parameter.direction == "in" and parameter.repeated_var_args:
            compound_parameter_type = parameter.grpc_type.replace("repeated ", "")
            break

    for parameter in get_input_arguments_for_compound_params(func):
        parameters.append(f"{parameter}={parameter}[index]")
    return f"grpc_types.{compound_parameter_type}(" + ", ".join(parameters) + ")"


def get_response_parameters(func):
    """Gets the list of parameters in grpc response."""
    output_parameters = get_output_params(func)
    is_read_method = check_if_parameters_contain_read_array(func.base_parameters)
    response_parameters = []
    output_parameters = get_output_params(func)
    for parameter in output_parameters:
        if not parameter.repeating_argument:
            name = parameter.parameter_name
            if parameter.parameter_name in MODIFIED_INTERPRETER_PARAMS:
                name = MODIFIED_INTERPRETER_PARAMS.get(parameter.parameter_name)
            if is_read_method and "read_array" in parameter.parameter_name:
                response_parameters.append(f"{name}")
            elif parameter.is_grpc_enum:
                response_parameters.append(f"response.{name}_raw")
            elif parameter.is_list:
                response_parameters.append(f"list(response.{name})")
            elif parameter.type == "CVIAbsoluteTime":
                response_parameters.append(f"convert_timestamp_to_time(response.{name})")
            else:
                response_parameters.append(f"response.{name}")
    return ", ".join(response_parameters)


def get_samps_per_chan_read_or_write_param(func_params):
    """Gets samps per read/ samps per write parameter."""
    for param in func_params:
        if param.parameter_name == "samps_per_chan_read":
            return f"samps_per_chan_read={param.parameter_name}"

        if param.parameter_name in ("samps_per_chan_written", "num_samps_per_chan_written"):
            return f"samps_per_chan_written={param.parameter_name}"
    return None


def get_samps_per_chan_read_param(func):
    """Gets samps per read parameter."""
    output_parameters = get_output_params(func)
    for param in output_parameters:
        if param.parameter_name in READ_SAMPLES_PARAMETER_NAMES:
            return param.parameter_name
    return None


def get_interpreter_parameters(func, is_grpc_interpreter=False):
    """Gets the parameters used in the interpreter functions."""
    size_params = _get_size_params(func.base_parameters)
    interpreter_parameters = []
    for parameter in func.base_parameters:
        # Repeated variable argument parameters are not used
        # as an interpreter parameter in nidaqmx-python
        if (
            (
                parameter.is_used_in_python_api
                and not parameter.is_proto_only
                and (not parameter.repeated_var_args or is_grpc_interpreter)
            )
            or parameter.parameter_name in size_params
            or _is_handle_parameter(func, parameter)
            or (is_grpc_interpreter and parameter.is_compound_type)
        ):
            interpreter_parameters.append(parameter)
    return interpreter_parameters


def _get_size_params(function_parameters):
    size_params = []
    for param in function_parameters:
        if param.has_explicit_buffer_size:
            if param.size.mechanism != "custom-code":
                size_params.append(param.size.value)
    return list(set(size_params))


def _is_handle_parameter(func, param):
    if func.handle_parameter is not None:
        parameter_name = "task_handle" if param.parameter_name == "task" else param.parameter_name
        return parameter_name == camel_to_snake_case(func.handle_parameter.cvi_name)
    return False


def check_if_parameters_contain_read_array(params):
    """Checks if the list of parameters contains read array parameter."""
    return any(x for x in params if "read_array" in x.parameter_name)


def get_read_array_parameters(func):
    """Gets the list of array parameters."""
    response = []
    for param in func.base_parameters:
        if param.direction == "out" and "read_array" in param.parameter_name:
            response.append(camel_to_snake_case(param.parameter_name))
    return response


def type_cast_attribute_set_function_parameter(param):
    """Type casting of attribute set parameter during c call."""
    if param.ctypes_data_type == "ctypes.c_char_p":
        return f"{param.parameter_name}.encode(lib_importer.encoding)"
    if is_numpy_array_datatype(param):
        return f"{param.parameter_name}.ctypes.data_as(ctypes.c_void_p)"
    return f"{param.ctypes_data_type}({param.parameter_name})"


def is_numpy_array_datatype(param):
    """Checks if datatype is a numpy array or not."""
    if param.ctypes_data_type and param.ctypes_data_type.startswith("numpy."):
        return True
    return False


def is_read_bytes_param(param):
    """Returns true if parameter reads bytes."""
    if param.is_list and param.ctypes_data_type in ("numpy.bool", "numpy.uint8"):
        return True
    # This is a special case for 'ReadRaw' function.
    # since its metadata is incorrect in daqmxAPISharp.json file.
    elif param.parameter_name == "read_array" and param.ctypes_data_type == "numpy.generic":
        return True
    else:
        return False


def is_write_bytes_param(param):
    """Returns true if parameter writes bytes."""
    if param.is_list and param.ctypes_data_type in ("numpy.bool", "numpy.uint8"):
        return True
    # This is a special case for 'WriteRaw' function.
    # since its metadata is incorrect in daqmxAPISharp.json file.
    elif param.parameter_name == "write_array" and param.ctypes_data_type == "numpy.generic":
        return True
    else:
        return False


def get_numpy_array_params(func):
    """Returns a dictionary of numpy data type parameters."""
    numpy_params = {}
    for param in func.base_parameters:
        if is_numpy_array_datatype(param):
            if param.ctypes_data_type == "numpy.bool":
                numpy_params[param.parameter_name] = "bool"
            else:
                numpy_params[param.parameter_name] = param.ctypes_data_type

        # This is a special case for these functions.
        # since its metadata is incorrect in daqmxAPISharp.json file.
        if func.function_name == "read_power_f64" and "read_array" in param.parameter_name:
            numpy_params[param.parameter_name] = "numpy.float64"
        if func.function_name == "read_power_binary_i16" and "read_array" in param.parameter_name:
            numpy_params[param.parameter_name] = "numpy.int16"

    return numpy_params


def get_write_array_param(param):
    """Assigns the numpy array to a flattened numpy array."""
    if is_numpy_array_datatype(param):
        return f"{param.parameter_name}={param.parameter_name}.flat"
    return f"{param.parameter_name}={param.parameter_name}"
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/codegen/utilities/text_wrappers.py sha256=f4749452249091adfd4b7da235c842af87506d192cc5e94dece0d4a14d37c80f bytes=1947 -->
## FILE: src/codegen/utilities/text_wrappers.py

- repository: `ni/nidaqmx-python`
- source_path: `src/codegen/utilities/text_wrappers.py`
- sha256: `f4749452249091adfd4b7da235c842af87506d192cc5e94dece0d4a14d37c80f`
- bytes: 1947

````python
"""This contains the helpers methods for wrapping texts."""

import os
import textwrap

"""
 Use global text wrapper objects and reassign properties each time instead
 of instantiating a new text wrapper object each time, as it is about 2 orders
 of magnitude faster.

 An extra character is subtracted from the line width of the code text wrapper
 to allow for closing brackets, since the Mako template will be prettier
 without lines like [${variable + ']' | wrap(4. 8)}
"""
wrapper = textwrap.TextWrapper(width=78, break_long_words=False)
docstring_wrapper = textwrap.TextWrapper(width=72, break_long_words=False)


def wrap(initial_indent, subsequent_indent=None):
    """Returns custom Mako filter function that wraps code text.

    Returning another function from within this function is a trick used to
    enable Mako filter functions to accept arguments.
    """

    def text_wrap(text):
        wrapper.initial_indent = " " * initial_indent
        if subsequent_indent is None:
            wrapper.subsequent_indent = " " * initial_indent
        else:
            wrapper.subsequent_indent = " " * subsequent_indent
        return wrapper.fill(text).lstrip().replace("\n", os.linesep)

    return text_wrap


def docstring_wrap(initial_indent, subsequent_indent=None):
    """Returns custom Mako filter function that wraps docstring text.

    Returning another function from within this function is a trick used to
    enable Mako filter functions to accept arguments.
    """

    def doc_string_wrap(text):
        docstring_wrapper.initial_indent = " " * initial_indent
        if subsequent_indent is None:
            docstring_wrapper.subsequent_indent = " " * initial_indent
        else:
            docstring_wrapper.subsequent_indent = " " * subsequent_indent
        return docstring_wrapper.fill(text).lstrip().replace("\n", os.linesep)

    return doc_string_wrap
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/__init__.py sha256=78d20b68146d3c4f1015e88ff2cf90ff090ef94c45654f945d9e438215b66081 bytes=909 -->
## FILE: src/handwritten/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/__init__.py`
- sha256: `78d20b68146d3c4f1015e88ff2cf90ff090ef94c45654f945d9e438215b66081`
- bytes: 909

````python
"""The NI-DAQmx API for Python."""

from importlib.metadata import version

from nidaqmx.errors import (
    DaqError,
    DaqReadError,
    DaqResourceWarning,
    DaqWarning,
    DaqWriteError,
)
from nidaqmx.grpc_session_options import *  # noqa: F403 - 'from nidaqmx.grpc_session_options import *' used; unable to detect undefined names (auto-generated noqa)
from nidaqmx.scale import Scale
from nidaqmx.task import Task
from nidaqmx.types import CtrFreq, CtrTick, CtrTime

__version__ = version(__name__)

__all__ = [  # noqa: F405 - 'errors' may be undefined, or defined from star imports: nidaqmx.grpc_session_options (auto-generated noqa)
    "errors",
    "scale",
    "stream_readers",
    "stream_writers",
    "task",
]

# Do not add a null logging handler. If the application has not configured logging, the
# default behavior is to log warnings and errors to stderr.
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/__main__.py sha256=d505bb4d4c32c9bdfb171e1b5483d889cd0770311f1330e8bd0d411873f997e7 bytes=1021 -->
## FILE: src/handwritten/__main__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/__main__.py`
- sha256: `d505bb4d4c32c9bdfb171e1b5483d889cd0770311f1330e8bd0d411873f997e7`
- bytes: 1021

````python
"""'nidaqmx' command line utility."""

from __future__ import annotations

import logging

import click

from nidaqmx import _install_daqmx


@click.group("nidaqmx")
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def main(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    verbosity: int,
) -> None:
    _configure_logging(verbosity)


@main.command()
def installdriver():  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    _install_daqmx.installdriver()


def _configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_bitfield_utils.py sha256=c1205b4672ce4d0acf149e5c800414f015b021a85500e309f5f3c82c12fb6ff6 bytes=1440 -->
## FILE: src/handwritten/_bitfield_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_bitfield_utils.py`
- sha256: `c1205b4672ce4d0acf149e5c800414f015b021a85500e309f5f3c82c12fb6ff6`
- bytes: 1440

````python
def enum_bitfield_to_list(bitfield_value, bitfield_enum_type, actual_enum_type):
    """Converts a bitfield value to a list of enums.

    Args:
        bitfield_value (int): Specifies the value of the bitfield.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.
        actual_enum_type (enum.Enum): Specifies the actual enum type.

    Returns:
        List[enum.Enum]: Indicates the converted list of enums.
    """
    supported_values = []
    for bitfield_mask in bitfield_enum_type:
        if bitfield_value & bitfield_mask.value:
            enum_value = next(e for e in actual_enum_type if e.name == bitfield_mask.name)
            supported_values.append(enum_value)

    return supported_values


def enum_list_to_bitfield(enum_list, bitfield_enum_type):
    """Converts a list of enums to a bitfield value.

    Args:
        enum_list (List[enum.Enum]): Specifies the list of enums.
        bitfield_enum_type (enum.Enum): Specifies the bitfield enum type
            from which to mask and extract the enum values.

    Returns:
        int: Indicates the value of the bitfield.
    """
    bitfield_value = 0
    for enum_value in enum_list:
        bitfield_mask = next(b for b in bitfield_enum_type if b.name == enum_value.name)
        bitfield_value |= bitfield_mask.value

    return bitfield_value
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_dotenv_path.py sha256=d604cfae5b35b0ceda93e2e034c1e075b16beb8cfc792e42a212402d4c627404 bytes=2377 -->
## FILE: src/handwritten/_dotenv_path.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_dotenv_path.py`
- sha256: `d604cfae5b35b0ceda93e2e034c1e075b16beb8cfc792e42a212402d4c627404`
- bytes: 2377

````python
from __future__ import annotations

import inspect
import sys
import traceback
from pathlib import Path


def get_dotenv_search_path() -> Path:
    """Get the search path for loading the `.env` file."""
    # Prefer to load the `.env` file from the current directory or its parents.
    # If the current directory doesn't have a `.env` file, fall back to the
    # script/EXE path or the TestStand code module path.
    cwd = Path.cwd()
    if not _has_dotenv_file(cwd):
        if script_or_exe_path := _get_script_or_exe_path():
            return script_or_exe_path.resolve().parent
        if caller_path := _get_caller_path():
            return caller_path.resolve().parent
    return cwd


def _has_dotenv_file(dir: Path) -> bool:
    """Check whether the dir or its parents contains a `.env` file."""
    return (dir / ".env").exists() or any((p / ".env").exists() for p in dir.parents)


def _get_script_or_exe_path() -> Path | None:
    """Get the path of the top-level script or PyInstaller EXE, if possible."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable)

    main_module = sys.modules.get("__main__")
    if main_module:
        script_path = getattr(main_module, "__file__", "")
        if script_path:
            return Path(script_path)

    return None


def _get_caller_path() -> Path | None:
    """Get the path of the module calling into this package, if possible."""
    package_path = _get_package_path()
    for frame, _ in traceback.walk_stack(inspect.currentframe()):
        if frame.f_code.co_filename:
            module_path = Path(frame.f_code.co_filename)
            if _exists(module_path) and not module_path.is_relative_to(package_path):
                return module_path

    return None


# Path.exists() throws OSError when the path has invalid file characters.
# https://github.com/python/cpython/issues/79487
if sys.version_info >= (3, 10):

    def _exists(path: Path) -> bool:
        return path.exists()

else:

    def _exists(path: Path) -> bool:
        import os

        return os.path.exists(path)


def _get_package_path() -> Path:
    """Get the path of this package."""
    module = sys.modules[__package__]
    assert module.__file__ and module.__file__.endswith("__init__.py")
    return Path(module.__file__).parent
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_feature_toggles.py sha256=1d45e17aaa91e0d3648960dd6ef7fd1f64105ad5ceb496bffc68b84e4ffd9c53 bytes=4969 -->
## FILE: src/handwritten/_feature_toggles.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_feature_toggles.py`
- sha256: `1d45e17aaa91e0d3648960dd6ef7fd1f64105ad5ceb496bffc68b84e4ffd9c53`
- bytes: 4969

````python
"""nidaqmx feature toggles."""

# mypy: no-warn-unreachable
from __future__ import annotations

import functools
from collections.abc import Callable
from enum import Enum
from typing import TYPE_CHECKING, TypeVar

from decouple import AutoConfig, Undefined, undefined

from nidaqmx._dotenv_path import get_dotenv_search_path
from nidaqmx.errors import FeatureNotSupportedError

if TYPE_CHECKING:
    from typing_extensions import ParamSpec, Self

    _P = ParamSpec("_P")
    _T = TypeVar("_T")

_PREFIX = "NIDAQMX"

if TYPE_CHECKING:
    # Work around decouple's lack of type hints.
    def _config(
        option: str,
        default: _T | Undefined = undefined,
        cast: Callable[[str], _T] | Undefined = undefined,
    ) -> _T: ...

else:
    _config = AutoConfig(str(get_dotenv_search_path()))


# Based on the recipe at https://docs.python.org/3/howto/enum.html
class _OrderedEnum(Enum):
    def __ge__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class CodeReadiness(_OrderedEnum):
    """Indicates whether code is ready to be supported."""

    RELEASE = 0
    NEXT_RELEASE = 1
    INCOMPLETE = 2
    PROTOTYPE = 3


def _init_code_readiness_level() -> CodeReadiness:
    if _config(f"{_PREFIX}_ALLOW_INCOMPLETE", default=False, cast=bool):
        return CodeReadiness.INCOMPLETE
    elif _config(f"{_PREFIX}_ALLOW_NEXT_RELEASE", default=False, cast=bool):
        return CodeReadiness.NEXT_RELEASE
    else:
        return CodeReadiness.RELEASE


# This is not public because `from _feature_toggles import CODE_READINESS_LEVEL`
# is incompatible with the patching performed by the use_code_readiness mark.
_CODE_READINESS_LEVEL = _init_code_readiness_level()


def get_code_readiness_level() -> CodeReadiness:
    """Get the current code readiness level.

    You can override this in tests by specifying the ``use_code_readiness``
    mark.
    """
    return _CODE_READINESS_LEVEL


class FeatureToggle:
    """A run-time feature toggle."""

    name: str
    """The name of the feature."""

    readiness: CodeReadiness
    """The code readiness at which this feature is enabled."""

    def __init__(self, name: str, readiness: CodeReadiness) -> None:
        """Initialize the feature toggle."""
        assert name == name.upper()
        self.name = name
        self.readiness = readiness
        self._is_enabled_override = None
        # Only read the env var at initialization time.
        if _config(f"{_PREFIX}_ENABLE_{name}", default=False, cast=bool):
            self._is_enabled_override = True

    @property
    def is_enabled(self) -> bool:
        """Indicates whether the feature is currently enabled.

        You can enable/disable features in tests by specifying the
        ``enable_feature_toggle`` or ``disable_feature_toggle`` marks.
        """
        if self._is_enabled_override is not None:
            return self._is_enabled_override
        return self.readiness <= get_code_readiness_level()

    def raise_if_disabled(self) -> None:
        """Raises an error if the feature is disabled."""
        if self.is_enabled:
            return

        env_vars = f"{_PREFIX}_ENABLE_{self.name}"
        if self.readiness in [CodeReadiness.NEXT_RELEASE, CodeReadiness.INCOMPLETE]:
            env_vars += f" or {_PREFIX}_ALLOW_{self.readiness.name}"
        message = (
            f"The {self.name} feature is not supported at the current code readiness level. "
            f" To enable it, set {env_vars}."
        )
        raise FeatureNotSupportedError(message)


def requires_feature(
    feature_toggle: FeatureToggle,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    """Decorator specifying that the function requires the specified feature toggle."""

    def decorator(func: Callable[_P, _T]) -> Callable[_P, _T]:
        @functools.wraps(func)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T:
            feature_toggle.raise_if_disabled()
            return func(*args, **kwargs)

        return wrapper

    return decorator


# --------------------------------------
# Define feature toggle constants here:
# --------------------------------------

WAVEFORM_SUPPORT = FeatureToggle("WAVEFORM_SUPPORT", CodeReadiness.RELEASE)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_grpc_time.py sha256=788c6bb95fb17659d16be1a0ddf53eca71b8167247a1498aafb89d224feb46de bytes=2083 -->
## FILE: src/handwritten/_grpc_time.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_grpc_time.py`
- sha256: `788c6bb95fb17659d16be1a0ddf53eca71b8167247a1498aafb89d224feb46de`
- bytes: 2083

````python
from __future__ import annotations

from datetime import datetime as std_datetime, timezone, tzinfo as dt_tzinfo

from google.protobuf.timestamp_pb2 import Timestamp as GrpcTimestamp
from hightime import datetime as ht_datetime, timedelta as ht_timedelta

from nidaqmx._time import _convert_to_desired_timezone

# 66 years, 17 leap days = 24107 days = 2082844800 seconds
_BIAS_FROM_1970_EPOCH = 2082844800

_NS_PER_S = 10**9
_NS_PER_US = 10**3

_YS_PER_US = 10**18
_YS_PER_NS = 10**15
_YS_PER_FS = 10**9

_EPOCH_1970 = ht_datetime(1970, 1, 1, tzinfo=timezone.utc)


def convert_time_to_timestamp(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    dt: std_datetime | ht_datetime, ts: GrpcTimestamp | None = None
) -> GrpcTimestamp:
    seconds_since_1970 = 0

    if ts is None:
        ts = GrpcTimestamp()

    if isinstance(dt, ht_datetime):
        seconds_since_1970 = int((dt - _EPOCH_1970).precision_total_seconds())
        total_yoctoseconds = dt.yoctosecond
        total_yoctoseconds += dt.femtosecond * _YS_PER_FS
        total_yoctoseconds += dt.microsecond * _YS_PER_US
        nanos, remainder_yoctoseconds = divmod(total_yoctoseconds, _YS_PER_NS)
        # round up, if necessary
        if remainder_yoctoseconds >= _YS_PER_NS / 2:
            nanos += 1
    else:
        seconds_since_1970 = int((dt - _EPOCH_1970).total_seconds())
        nanos = dt.microsecond * _NS_PER_US

    ts.FromNanoseconds(seconds_since_1970 * _NS_PER_S + nanos)
    return ts


def convert_timestamp_to_time(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    ts: GrpcTimestamp, tzinfo: dt_tzinfo | None = None
) -> ht_datetime:
    total_nanos = ts.ToNanoseconds()
    seconds, nanos = divmod(total_nanos, _NS_PER_S)
    # Convert the nanoseconds to yoctoseconds.
    total_yoctoseconds = int(round(_YS_PER_NS * nanos))
    dt = _EPOCH_1970 + ht_timedelta(seconds=seconds) + ht_timedelta(yoctoseconds=total_yoctoseconds)
    return _convert_to_desired_timezone(dt, tzinfo)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_install_daqmx.py sha256=f35314f917e393e4c6edacc86454a72c005293fed3aa9d9dc9fbbe698ae1e529 bytes=18858 -->
## FILE: src/handwritten/_install_daqmx.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_install_daqmx.py`
- sha256: `f35314f917e393e4c6edacc86454a72c005293fed3aa9d9dc9fbbe698ae1e529`
- bytes: 18858

````python
from __future__ import annotations

import contextlib
import importlib.resources as pkg_resources
import json
import logging
import os
import re
import subprocess  # nosec: B404
import sys
import tempfile
import zipfile
from collections.abc import Generator
from urllib.parse import urlparse

import click
import requests

if sys.platform.startswith("win"):
    import winreg
elif sys.platform.startswith("linux"):
    import distro

    from nidaqmx._linux_installation_commands import (
        LINUX_COMMANDS,
        get_linux_installation_commands,
    )

_logger = logging.getLogger(__name__)

METADATA_FILE = "_installer_metadata.json"
_NETWORK_TIMEOUT_IN_SECONDS = 60


def _parse_version(version: str) -> tuple[int, ...]:
    """Split the version string into a tuple of integers.

    >>> _parse_version("23.8.0")
    (23, 8, 0)
    >>> _parse_version("24.0.0")
    (24, 0, 0)
    >>> _parse_version("invalid_version")
    Traceback (most recent call last):
    ...
    click.exceptions.ClickException: Invalid version format found
    """
    try:
        return tuple(int(part) for part in version.split("."))
    except ValueError as e:
        _logger.info("Failed to parse version.", exc_info=True)
        raise click.ClickException(f"Invalid version number '{version}'.") from e


def _get_daqmx_installed_version() -> str | None:
    """Check for existing installation of NI-DAQmx."""
    if sys.platform.startswith("win"):
        try:
            _logger.debug("Reading the registry entries to get installed DAQmx version")
            with winreg.OpenKeyEx(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\National Instruments\NI-DAQmx\CurrentVersion",
                0,
                winreg.KEY_READ | winreg.KEY_WOW64_32KEY,
            ) as daqmx_reg_key:
                product_name = winreg.QueryValueEx(daqmx_reg_key, "ProductName")[0]
                product_version = winreg.QueryValueEx(daqmx_reg_key, "Version")[0]

            if product_name == "NI-DAQmx":
                _logger.info(
                    "Found registry entries for Product Name: %s and version %s",
                    product_name,
                    product_version,
                )
                return product_version
            return None
        except FileNotFoundError:
            _logger.info("No existing NI-DAQmx installation found.")
            return None
        except PermissionError as e:
            _logger.info("Failed to read the registry key.", exc_info=True)
            raise click.ClickException(
                f"Permission denied while getting the installed NI-DAQmx version.\nDetails: {e}"
            ) from e
        except OSError as e:
            _logger.info("Failed to read the registry key.", exc_info=True)
            raise click.ClickException(
                f"An OS error occurred while getting the installed NI-DAQmx version.\nDetails: {e}"
            ) from e
    elif sys.platform.startswith("linux"):
        try:
            distribution = distro.id()
            _logger.debug("Checking for installed NI-DAQmx version")
            commands_info = LINUX_COMMANDS[distribution]
            query_command = commands_info.get_daqmx_version
            # Run the package query command defined by _linux_installation_commands.py.
            query_output = subprocess.run(
                query_command, stdout=subprocess.PIPE, text=True
            ).stdout  # nosec: B603

            if distribution == "ubuntu":
                version_match = re.search(r"ii\s+ni-daqmx\s+(\d+\.\d+\.\d+)", query_output)
            elif distribution == "opensuse" or distribution == "rhel":
                version_match = re.search(r"ni-daqmx-(\d+\.\d+\.\d+)", query_output)
            else:
                raise click.ClickException(f"Unsupported distribution '{distribution}'")
            if version_match is None:
                return None
            else:
                installed_version = version_match.group(1)
                _logger.info("Found installed NI-DAQmx version: %s", installed_version)
                return installed_version

        except subprocess.CalledProcessError as e:
            _logger.info("Failed to get installed NI-DAQmx version.", exc_info=True)
            raise click.ClickException(
                f"An error occurred while getting the installed NI-DAQmx version.\nCommand returned non-zero exit status '{e.returncode}'."
            ) from e
    else:
        raise NotImplementedError("This function is only supported on Windows and Linux.")


# Creating a temp file that we then close and yield - this is used to allow subprocesses to access
@contextlib.contextmanager
def _multi_access_temp_file(*, suffix: str = ".exe", delete: bool = True) -> Generator[str]:
    """Context manager for creating a temporary file."""
    try:
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False, mode="w")
        temp_file.close()
        _logger.debug("Created temp file: %s", temp_file.name)
    except Exception as e:
        _logger.info("Failed to create temporary file.", exc_info=True)
        raise click.ClickException(
            f"Failed to create temporary file '{temp_file.name}'.\nDetails: {e}"
        ) from e

    try:
        yield temp_file.name
    finally:
        if delete:
            try:
                _logger.debug("Deleting temp file: %s", temp_file.name)
                os.unlink(temp_file.name)
            except ValueError as e:
                _logger.info("Failed to delete temporary file.", exc_info=True)
                raise click.ClickException(
                    f"Failed to delete temporary file '{temp_file.name}'.\nDetails: {e}"
                ) from e


def _load_data(
    json_data: str, platform: str
) -> tuple[str | None, str | None, str | None, list[str] | None]:
    """Load data from JSON string and extract Windows metadata.

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Windows")
    ('path/to/windows/driver', '24.0', '2024Q1', ['Windows 11'])

    >>> json_data = '{"Windows": [], "Linux": [{"Location": "path/to/linux/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["ubuntu 20.04 ", "rhel 9"]}]}'
    >>> _load_data(json_data, "Linux")
    ('path/to/linux/driver', '24.0', '2024Q1', ['ubuntu 20.04', 'rhel 9'])

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "Linux")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unable to fetch driver details

    >>> json_data = 'invalid json'
    >>> _load_data(json_data, "Windows")
    Traceback (most recent call last):
    click.exceptions.ClickException: Failed to parse the driver metadata.
    Details: Expecting value: line 1 column 1 (char 0)

    >>> json_data = '{"Windows": [{"Location": "path/to/windows/driver", "Version": "24.0", "Release": "2024Q1", "supportedOS": ["Windows 11"]}], "Linux": []}'
    >>> _load_data(json_data, "macOS")
    Traceback (most recent call last):
    click.exceptions.ClickException: Unsupported os 'macOS'

    """  # noqa: W505 - doc line too long (159 > 100 characters) (auto-generated noqa)
    try:
        if platform == "Windows":
            metadata = json.loads(json_data).get("Windows", [])
        elif platform == "Linux":
            metadata = json.loads(json_data).get("Linux", [])
        else:
            raise click.ClickException(f"Unsupported os '{platform}'")
    except json.JSONDecodeError as e:
        _logger.info("Failed to parse the json data.", exc_info=True)
        raise click.ClickException(f"Failed to parse the driver metadata.\nDetails: {e}") from e

    for metadata_entry in metadata:
        location: str | None = metadata_entry.get("Location")
        version: str | None = metadata_entry.get("Version")
        release: str | None = metadata_entry.get("Release")
        supported_os: list[str] | None = metadata_entry.get("supportedOS")
        _logger.debug("From metadata file found location %s and version %s.", location, version)
        if location and version:
            return location, version, release, supported_os
    raise click.ClickException(f"Unable to fetch driver details")


def _get_driver_details(
    platform: str,
) -> tuple[str | None, str | None, str | None, list[str] | None]:
    """Parse the JSON data and retrieve the download link and version information."""
    try:
        with pkg_resources.open_text(__package__, METADATA_FILE) as json_file:
            _logger.debug("Opening the metadata file %s.", METADATA_FILE)
            location, version, release, supported_os = _load_data(json_file.read(), platform)
        return location, version, release, supported_os

    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to get driver metadata.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while getting the driver metadata.\nDetails: {e}"
        ) from e


def _install_daqmx_driver_windows_core(download_url: str) -> None:
    """Download and launch NI-DAQmx Driver installation in an interactive mode."""
    _validate_download_url(download_url)
    try:
        with _multi_access_temp_file() as temp_file:
            _logger.info("Downloading Driver to %s", temp_file)
            response = requests.get(download_url, timeout=_NETWORK_TIMEOUT_IN_SECONDS)
            response.raise_for_status()
            with open(temp_file, "wb") as f:
                f.write(response.content)
            _logger.info("Installing NI-DAQmx")
            # Run the installer that we just downloaded from https://download.ni.com.
            subprocess.run([temp_file], shell=True, check=True)  # nosec: B602
    except subprocess.CalledProcessError as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred while installing the NI-DAQmx driver. Command returned non-zero exit status '{e.returncode}'."
        ) from e
    except requests.RequestException as e:
        _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to download the NI-DAQmx driver.\nDetails: {e}") from e
    except Exception as e:
        _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
        raise click.ClickException(f"Failed to install the NI-DAQmx driver.\nDetails: {e}") from e


def _install_daqmx_driver_linux_core(download_url: str, release: str) -> None:
    """Download NI Linux Device Drivers and install NI-DAQmx on Linux OS."""
    if sys.platform.startswith("linux"):
        _validate_download_url(download_url)
        try:
            with _multi_access_temp_file(suffix=".zip") as temp_file:
                _logger.info("Downloading Driver to %s", temp_file)
                response = requests.get(download_url, timeout=_NETWORK_TIMEOUT_IN_SECONDS)
                response.raise_for_status()
                with open(temp_file, "wb") as f:
                    f.write(response.content)

                with tempfile.TemporaryDirectory() as temp_folder:
                    directory_to_extract_to = temp_folder

                    _logger.info("Unzipping the downloaded file to %s", directory_to_extract_to)

                    with zipfile.ZipFile(temp_file, "r") as zip_ref:
                        zip_ref.extractall(directory_to_extract_to)

                    _logger.info("Installing NI-DAQmx")
                    for command in get_linux_installation_commands(
                        directory_to_extract_to, distro.id(), distro.version(), release
                    ):
                        print("\nRunning command:", " ".join(command))
                        # Run the commands defined in
                        # _linux_installation_commands.py to install the package
                        # that we just downloaded from https://download.ni.com.
                        subprocess.run(command, check=True)  # nosec: B603

            # Check if the installation was successful
            if not _get_daqmx_installed_version():
                raise click.ClickException(
                    "Failed to install NI-DAQmx driver. All installation commands ran successfully but the driver is not installed."
                )
            else:
                print("NI-DAQmx driver installed successfully. Please reboot the system.")

        except subprocess.CalledProcessError as e:
            _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"An error occurred while installing the NI-DAQmx driver. Command returned non-zero exit status '{e.returncode}'."
            ) from e
        except requests.RequestException as e:
            _logger.info("Failed to download NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"Failed to download the NI-DAQmx driver.\nDetails: {e}"
            ) from e
        except Exception as e:
            _logger.info("Failed to install NI-DAQmx driver.", exc_info=True)
            raise click.ClickException(
                f"Failed to install the NI-DAQmx driver.\nDetails: {e}"
            ) from e
    else:
        raise NotImplementedError("This function is only supported on Linux.")


def _validate_download_url(download_url: str) -> None:
    """Validate that the download URL uses https and points to a trusted site."""
    parsed_url = urlparse(download_url)
    if parsed_url.scheme != "https" or parsed_url.netloc != "download.ni.com":
        raise click.ClickException(f"Unsupported download URL: {download_url}")


def _ask_user_confirmation(user_message: str) -> bool:
    """Prompt for user confirmation."""
    while True:
        response = input(user_message + " (yes/no): ").strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def _upgrade_daqmx_user_confirmation(
    installed_version: str,
    latest_version: str,
    release: str,
) -> bool:
    """Confirm with the user and return the user response."""
    _logger.debug("Entering _upgrade_daqmx_user_confirmation")
    installed_parts = _parse_version(installed_version)
    latest_parts = _parse_version(latest_version)
    if installed_parts >= latest_parts:
        print(
            f"Installed NI-DAQmx version ({installed_version}) is up to date. (Expected {latest_version} ({release}) or newer.)"
        )
        return False
    is_upgrade = _ask_user_confirmation(
        f"Installed NI-DAQmx version is {installed_version}. Latest version available is {latest_version} ({release}). Do you want to upgrade?"
    )
    return is_upgrade


def _fresh_install_daqmx_user_confirmation(
    latest_version: str,
    release: str,
) -> bool:
    """Confirm with the user and return the user response."""
    _logger.debug("Entering _fresh_install_daqmx_user_confirmation")
    return _ask_user_confirmation(
        f"Latest NI-DAQmx version available is {latest_version} ({release}). Do you want to install?"
    )


def _is_distribution_supported() -> None:
    """Raises an exception if the linux distribution and its version are not supported."""
    if sys.platform.startswith("linux"):
        dist_name = distro.id()
        dist_version = distro.version()

        # For rhel, we only need the major version
        if dist_name == "rhel":
            dist_version = dist_version.split(".")[0]
        dist_name_and_version = dist_name + " " + dist_version

        download_url, latest_version, release, supported_os = _get_driver_details("Linux")
        if supported_os is None:
            raise ValueError("supported_os cannot be None")

        # Check if the platform is one of the supported ones
        if dist_name_and_version in supported_os:
            _logger.info(f"The platform is supported: {dist_name_and_version}")
        else:
            raise click.ClickException(f"The platform {dist_name_and_version} is not supported.")
    else:
        raise NotImplementedError("This function is only supported on Linux.")


def _install_daqmx_driver():
    """Install the NI-DAQmx driver."""
    if sys.platform.startswith("win"):
        _logger.info("Windows platform detected")
        platform = "Windows"
    elif sys.platform.startswith("linux"):
        _logger.info("Linux platform detected")
        platform = "Linux"

        try:
            _is_distribution_supported()
        except Exception as e:
            raise click.ClickException(f"Distribution not supported.\nDetails: {e}") from e

    else:
        raise click.ClickException(
            f"The 'installdriver' command is supported only on Windows and Linux."
        )

    installed_version = _get_daqmx_installed_version()
    download_url, latest_version, release, _ = _get_driver_details(platform)

    if not download_url:
        raise click.ClickException(f"Failed to fetch the download url.")
    if not release or not latest_version:
        raise click.ClickException(f"Failed to fetch the release version string.")
    else:
        if installed_version:
            user_response = _upgrade_daqmx_user_confirmation(
                installed_version, latest_version, release
            )
        else:
            user_response = _fresh_install_daqmx_user_confirmation(latest_version, release)

        if user_response:
            if platform == "Linux":
                _install_daqmx_driver_linux_core(download_url, release)
            else:
                _install_daqmx_driver_windows_core(download_url)


def installdriver() -> None:
    """Download and launch NI-DAQmx Driver installation in an interactive mode."""
    try:
        _install_daqmx_driver()
    except click.ClickException:
        raise
    except Exception as e:
        _logger.info("Failed to install driver.", exc_info=True)
        raise click.ClickException(
            f"An error occurred during the installation of the NI-DAQmx driver.\nDetails: {e}"
        ) from e
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_installer_metadata.json sha256=1c15f26832c8bf3716fc0665faf4442a530334ab41c710956de6236645c2dc4c bytes=1181 -->
## FILE: src/handwritten/_installer_metadata.json

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_installer_metadata.json`
- sha256: `1c15f26832c8bf3716fc0665faf4442a530334ab41c710956de6236645c2dc4c`
- bytes: 1181

````json
{
    "Windows": [
        {
            "Version": "26.3.0",
            "Release": "2026Q2",
            "Location": "https://download.ni.com/support/nipkg/products/ni-d/ni-daqmx/26.3/online/ni-daqmx_26.3_online.exe",
            "supportedOS": [
                "Windows 11",
                "Windows Server 2025",
                "Windows Server 2022 64-bit",
                "Windows 10 IoT Enterprise 2021"
            ]
        }
    ],
    "Linux": [
        {
            "Version": "26.3.0",
            "Release": "2026Q2",
            "_comment": "Location url must be of the format 'https://download.ni.com/support/softlib/MasterRepository/LinuxDrivers<Release>/NILinux<Release>DeviceDrivers.zip'. Any change to the format will require a change in the code.",
            "Location": "https://download.ni.com/support/softlib/MasterRepository/LinuxDrivers2026Q2/NILinux2026Q2DeviceDrivers.zip",
            "supportedOS": [
                "ubuntu 22.04",
                "ubuntu 24.04",
                "rhel 9",
                "rhel 10",
                "opensuse 15.6",
                "opensuse 16.0"
            ]
        }
    ]
}
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_lib.py sha256=cfa76149d33eaf294fc5568c262b0049761ceda4337c879529742696719dd40c bytes=8182 -->
## FILE: src/handwritten/_lib.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_lib.py`
- sha256: `cfa76149d33eaf294fc5568c262b0049761ceda4337c879529742696719dd40c`
- bytes: 8182

````python
from __future__ import annotations

import ctypes
import locale
import sys
import threading
from ctypes.util import find_library
from typing import TYPE_CHECKING, cast

from decouple import config
from numpy.ctypeslib import ndpointer

from nidaqmx.errors import (
    DaqFunctionNotSupportedError,
    DaqNotFoundError,
    DaqNotSupportedError,
)

if TYPE_CHECKING:
    from typing_extensions import TypeAlias


_DAQ_NOT_FOUND_MESSAGE = (
    "Could not find an installation of NI-DAQmx. Please ensure that NI-DAQmx "
    "is installed on this machine or contact National Instruments for support."
)

_DAQ_NOT_SUPPORTED_MESSAGE = (
    "NI-DAQmx Python is not supported on this platform: {0}. Please "
    "direct any questions or feedback to National Instruments."
)

_FUNCTION_NOT_SUPPORTED_MESSAGE = (
    'The NI-DAQmx function "{0}" is not supported in this version '
    "of NI-DAQmx. Visit ni.com/downloads to upgrade."
)


class c_bool32(  # noqa: N801 - class name 'c_bool32' should use CapWords convention (auto-generated noqa)
    ctypes.c_uint
):
    """Specifies a custom ctypes data type to represent 32-bit booleans."""

    # typeshed specifies that _SimpleCData[_T].value is an instance variable with type _T, so
    # accessing it with the descriptor protocol via its class results in "error: Access to generic
    # instance variables via class is ambiguous".

    def _getter(self):
        return bool(ctypes.c_uint.value.__get__(self))  # type: ignore

    def _setter(self, val):
        ctypes.c_uint.value.__set__(self, int(val))  # type: ignore

    value: bool = cast(bool, property(_getter, _setter))

    del _getter, _setter


class CtypesByteString:
    """Custom argtype that automatically converts unicode strings to encoding used by the C API."""

    @classmethod
    def from_param(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        cls, param
    ):
        if isinstance(param, str):
            param = param.encode(lib_importer.encoding)
        return ctypes.c_char_p(param)


ctypes_byte_str: TypeAlias = CtypesByteString


def wrapped_ndpointer(*args, **kwargs):
    """Wraps numpy.ctypeslib.ndpointer in order to allow passing None.

    Taken from http://stackoverflow.com/questions/32120178
    """
    base = ndpointer(*args, **kwargs)

    def from_param(cls, obj):
        if obj is None:
            return obj
        return base.from_param(obj)

    return type(base.__name__, (base,), {"from_param": classmethod(from_param)})


class DaqFunctionImporter:
    """Wraps the function getter function of a ctypes library.

    Allows the NI-DAQmx Python API to fail elegantly if a function is not
    supported in the current version of the API.
    """

    def __init__(self, library):
        """Initialize a new DaqFunctionImporter."""
        self._library = library
        self._lib_lock = threading.Lock()

    def __getattr__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, function
    ):
        try:
            c_func = getattr(self._library, function)
            if not hasattr(c_func, "arg_lock"):
                with self._lib_lock:
                    if not hasattr(c_func, "arg_lock"):
                        c_func.arg_lock = threading.Lock()
            return c_func
        except AttributeError:
            raise DaqFunctionNotSupportedError(_FUNCTION_NOT_SUPPORTED_MESSAGE.format(function))


CalHandle: TypeAlias = ctypes.c_uint
"""Calibration handle.

NIDAQmx.h defines CalHandle as a typedef for uInt32.
"""

TaskHandle: TypeAlias = ctypes.c_void_p
"""Task handle.

NIDAQmx.h defines TaskHandle as a typedef for void*.

From NI-DAQmx versions 7.0 to 8.8, TaskHandle was defined as uInt32. In NI-DAQmx 8.9, it was
changed to void* in order to support 64-bit platforms. This change did not break binary
compatibility because uInt32 and void* are the same size for 32-bit applications.
"""


def get_encoding_from_locale() -> str:
    """Gets the current locale encoding handling cases where it is unset."""
    _, encoding = locale.getlocale()
    return encoding or "ascii"


class DaqLibImporter:
    """Encapsulates NI-DAQmx library importing and handle type parsing logic."""

    def __init__(self):
        """Initialize a new DaqLibImporter."""
        self._windll = None
        self._cdll = None
        self._cal_handle = None
        self._task_handle = None
        self._encoding = None

    @property
    def windll(self):  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        if self._windll is None:
            self._import_lib()
        return self._windll

    @property
    def cdll(self):  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        if self._cdll is None:
            self._import_lib()
        return self._cdll

    @property
    def task_handle(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> type:
        return TaskHandle

    @property
    def cal_handle(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> type:
        return CalHandle

    @property
    def encoding(self):  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        if self._encoding is None:
            self._import_lib()
        return self._encoding

    def _import_lib(self):
        """Determines the location of and loads the NI-DAQmx CAI DLL."""
        self._windll = None
        self._cdll = None
        self._encoding = None

        windll = None
        cdll = None
        encoding = None

        if sys.platform.startswith("win"):

            def _load_lib(library_name: str):
                windll = ctypes.windll.LoadLibrary(library_name)
                cdll = ctypes.cdll.LoadLibrary(library_name)
                return windll, cdll

            # Feature Toggle to load nicaiu.dll or nicai_utf8.dll
            # The Feature Toggle can be set in the .env file
            nidaqmx_c_library = config("NIDAQMX_C_LIBRARY", default=None)

            if nidaqmx_c_library is not None:
                try:
                    if nidaqmx_c_library == "nicaiu":
                        windll, cdll = _load_lib("nicaiu")
                        encoding = get_encoding_from_locale()
                    elif nidaqmx_c_library == "nicai_utf8":
                        windll, cdll = _load_lib("nicai_utf8")
                        encoding = "utf-8"
                    else:
                        raise ValueError(
                            f"Unsupported NIDAQMX_C_LIBRARY value: {nidaqmx_c_library}"
                        )
                except OSError as e:
                    raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE) from e
            else:
                try:
                    windll, cdll = _load_lib("nicai_utf8")
                    encoding = "utf-8"
                except OSError:
                    # Fallback to nicaiu.dll if nicai_utf8.dll cannot be loaded
                    try:
                        windll, cdll = _load_lib("nicaiu")
                        encoding = get_encoding_from_locale()
                    except OSError as e:
                        raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE) from e
        elif sys.platform.startswith("linux"):
            library_path = find_library("nidaqmx")
            if library_path is not None:
                cdll = ctypes.cdll.LoadLibrary(library_path)
                windll = cdll
                encoding = get_encoding_from_locale()
            else:
                raise DaqNotFoundError(_DAQ_NOT_FOUND_MESSAGE)
        else:
            raise DaqNotSupportedError(_DAQ_NOT_SUPPORTED_MESSAGE.format(sys.platform))

        self._windll = DaqFunctionImporter(windll)
        self._cdll = DaqFunctionImporter(cdll)
        self._encoding = encoding


lib_importer = DaqLibImporter()
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_lib_time.py sha256=10d6a0f4dc4f571415e9308226ab124c05cdc1abd2d415b53de39d3149524fba bytes=3282 -->
## FILE: src/handwritten/_lib_time.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_lib_time.py`
- sha256: `10d6a0f4dc4f571415e9308226ab124c05cdc1abd2d415b53de39d3149524fba`
- bytes: 3282

````python
from __future__ import annotations

import ctypes
import functools
from datetime import datetime as std_datetime, timezone, tzinfo as dt_tzinfo

from hightime import datetime as ht_datetime, timedelta as ht_timedelta

from nidaqmx._time import _convert_to_desired_timezone


@functools.total_ordering
class AbsoluteTime(  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    ctypes.Structure
):
    # Please visit ni.com/info and enter the Info Code NI_BTF for detailed information.
    # The summary is:
    #    * lsb - positive fractions (2^-64) of a second
    #    * msb - number of whole seconds since 12am, Friday, January 1, 1904, UTC

    _pack_ = 4
    _fields_ = [("lsb", ctypes.c_uint64), ("msb", ctypes.c_int64)]

    # 66 years, 17 leap days = 24107 days = 2082844800 seconds
    _BIAS_FROM_1970_EPOCH = 2082844800
    _NUM_SUBSECONDS = 2**64
    _US_PER_S = 10**6
    _YS_PER_S = 10**24
    _YS_PER_US = 10**18
    _YS_PER_FS = 10**9

    MAX_FS = 10**9
    MAX_YS = 10**9

    _EPOCH_1904 = ht_datetime(1904, 1, 1, tzinfo=timezone.utc)

    @classmethod
    def from_datetime(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        cls, dt: std_datetime | ht_datetime
    ) -> AbsoluteTime:
        seconds_since_1904 = 0

        # Convert the subseconds.
        if isinstance(dt, ht_datetime):
            seconds_since_1904 = int((dt - AbsoluteTime._EPOCH_1904).precision_total_seconds())
            total_yoctoseconds = dt.yoctosecond
            total_yoctoseconds += dt.femtosecond * AbsoluteTime._YS_PER_FS
            total_yoctoseconds += dt.microsecond * AbsoluteTime._YS_PER_US
            lsb = int(
                round(AbsoluteTime._NUM_SUBSECONDS * total_yoctoseconds / AbsoluteTime._YS_PER_S)
            )
        else:
            seconds_since_1904 = int((dt - AbsoluteTime._EPOCH_1904).total_seconds())
            lsb = int(round(AbsoluteTime._NUM_SUBSECONDS * dt.microsecond / AbsoluteTime._US_PER_S))

        return AbsoluteTime(lsb=lsb, msb=seconds_since_1904)

    def to_datetime(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self, tzinfo: dt_tzinfo | None = None
    ) -> ht_datetime:
        total_yoctoseconds = int(
            round(AbsoluteTime._YS_PER_S * self.lsb / AbsoluteTime._NUM_SUBSECONDS)
        )
        dt = (
            AbsoluteTime._EPOCH_1904
            + ht_timedelta(seconds=self.msb)
            + ht_timedelta(yoctoseconds=total_yoctoseconds)
        )
        return _convert_to_desired_timezone(dt, tzinfo)

    def __str__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self,
    ) -> str:
        return f"AbsoluteTime(lsb=0x{self.lsb:x}, msb=0x{self.msb:x})"

    def __eq__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, other
    ) -> bool:
        return self.msb == other.msb and self.lsb == other.lsb

    def __lt__(  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        self, other
    ) -> bool:
        if self.msb == other.msb:
            return self.lsb < other.lsb
        else:
            return self.msb < other.msb
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_linux_installation_commands.py sha256=69c34019fc77080173bf1c6c361853e2b6dbd8f1df23bacd09ba142ff4836536 bytes=3036 -->
## FILE: src/handwritten/_linux_installation_commands.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_linux_installation_commands.py`
- sha256: `69c34019fc77080173bf1c6c361853e2b6dbd8f1df23bacd09ba142ff4836536`
- bytes: 3036

````python
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


def _get_version_ubuntu(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_opensuse(dist_version: str) -> str:
    return dist_version.replace(".", "")


def _get_version_rhel(dist_version: str) -> str:
    return dist_version.split(".")[0]


# Command templates
_APT_INSTALL_COMMANDS = [
    ["apt", "update"],
    [
        "apt",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-ubuntu{version}-drivers-{release}.deb",
    ],
    ["apt", "update"],
    ["apt", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_ZYPPER_INSTALL_COMMANDS = [
    ["zypper", "update"],
    ["zypper", "install", "insserv"],
    [
        "zypper",
        "--no-gpg-checks",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-opensuse{version}-drivers-{release}.rpm",
    ],
    ["zypper", "refresh"],
    ["zypper", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_YUM_INSTALL_COMMANDS = [
    ["yum", "update"],
    ["yum", "install", "chkconfig"],
    [
        "yum",
        "install",
        "{directory}/NILinux{release}DeviceDrivers/ni-rhel{version}-drivers-{release}.rpm",
    ],
    ["yum", "install", "ni-daqmx"],
    ["dkms", "autoinstall"],
]

_DEBIAN_DAQMX_VERSION_COMMAND = ["dpkg", "-l", "ni-daqmx"]
_RPM_DAQMX_VERSION_COMMAND = ["rpm", "-q", "ni-daqmx"]


@dataclass
class DistroInfo:  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    get_distro_version: Callable[[str], str]
    get_daqmx_version: list[str]
    install_commands: list[list[str]]


# Mapping of Linux distributions to their command templates and version handlers
LINUX_COMMANDS = {
    "ubuntu": DistroInfo(_get_version_ubuntu, _DEBIAN_DAQMX_VERSION_COMMAND, _APT_INSTALL_COMMANDS),
    "opensuse": DistroInfo(
        _get_version_opensuse, _RPM_DAQMX_VERSION_COMMAND, _ZYPPER_INSTALL_COMMANDS
    ),
    "rhel": DistroInfo(_get_version_rhel, _RPM_DAQMX_VERSION_COMMAND, _YUM_INSTALL_COMMANDS),
}


def get_linux_installation_commands(
    _directory_to_extract_to: str, dist_name: str, dist_version: str, _release_string: str
) -> list[list[str]]:
    """Get the installation commands for Linux based on the distribution."""
    if dist_name not in LINUX_COMMANDS:
        raise ValueError(f"Unsupported distribution '{dist_name}'")

    commands_info = LINUX_COMMANDS[dist_name]
    version = commands_info.get_distro_version(dist_version)
    install_commands = commands_info.install_commands

    # Format commands with the provided variables
    formatted_commands = [
        [
            cmd_part.format(
                directory=_directory_to_extract_to, release=_release_string, version=version
            )
            for cmd_part in cmd
        ]
        for cmd in install_commands
    ]

    return formatted_commands
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_time.py sha256=20bd34b9e92df9af0a71eda6cb92e1d8d77a0f9ada5dd5690d33355378f6635a bytes=2300 -->
## FILE: src/handwritten/_time.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_time.py`
- sha256: `20bd34b9e92df9af0a71eda6cb92e1d8d77a0f9ada5dd5690d33355378f6635a`
- bytes: 2300

````python
from __future__ import annotations

from datetime import timezone, tzinfo as dt_tzinfo
from zoneinfo import ZoneInfo

from hightime import datetime as ht_datetime
from tzlocal import get_localzone


# theoretically the same as astimezone(), but with support for dates before 1970
def _convert_to_desired_timezone(
    expected_time_utc: ht_datetime, tzinfo: dt_tzinfo | None = None
) -> ht_datetime:
    # if timezone matches, no need to do conversion
    if expected_time_utc.tzinfo is tzinfo:
        return expected_time_utc

    # if timezone is not defined, use system timezone
    if tzinfo is None:
        tzinfo = get_localzone()

    # use ZoneInfo here to account for daylight savings
    if isinstance(tzinfo, ZoneInfo):
        localized_time = expected_time_utc.replace(tzinfo=tzinfo)
        std_datetime_result = tzinfo.fromutc(localized_time)
        femtosecond = getattr(expected_time_utc, "femtosecond", 0)
        yoctosecond = getattr(expected_time_utc, "yoctosecond", 0)
        desired_expected_time = ht_datetime(
            std_datetime_result.year,
            std_datetime_result.month,
            std_datetime_result.day,
            std_datetime_result.hour,
            std_datetime_result.minute,
            std_datetime_result.second,
            std_datetime_result.microsecond,
            femtosecond,
            yoctosecond,
            tzinfo=std_datetime_result.tzinfo,
            fold=std_datetime_result.fold,
        )
        return desired_expected_time

    # if the tzinfo passed in is a timedelta function, then we don't need to consider daylight savings  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
    elif tzinfo.utcoffset(None) is not None:
        current_time_utc = ht_datetime.now(timezone.utc)
        desired_timezone_offset = current_time_utc.astimezone(tz=tzinfo).utcoffset()
        assert desired_timezone_offset is not None
        desired_expected_time = expected_time_utc + desired_timezone_offset
        new_datetime = desired_expected_time.replace(tzinfo=tzinfo)
        return new_datetime

    # if the tzinfo passed in is none of the above, fall back to original astimezone()
    else:
        return expected_time_utc.astimezone(tzinfo)
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/_waveform_utils.py sha256=dc8ed1413dbd0dbf3e3f6ae476cad5dd187e293d1ce50472d25f0302a75f1957 bytes=719 -->
## FILE: src/handwritten/_waveform_utils.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/_waveform_utils.py`
- sha256: `dc8ed1413dbd0dbf3e3f6ae476cad5dd187e293d1ce50472d25f0302a75f1957`
- bytes: 719

````python
from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from nitypes.waveform import AnalogWaveform, DigitalWaveform


def get_num_samps_per_chan(waveforms: Sequence[AnalogWaveform[Any] | DigitalWaveform[Any]]) -> int:
    """Validate that all waveforms have the same sample count and return it."""
    if len(waveforms) == 0:
        raise ValueError("At least one waveform must be provided")

    num_samps_per_chan = waveforms[0].sample_count
    for i, waveform in enumerate(waveforms):
        if waveform.sample_count != num_samps_per_chan:
            raise ValueError("The waveforms must all have the same sample count.")
    return num_samps_per_chan
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/errors.py sha256=fa9c75d3c40a1df12c551fe80e5c5cf39fca15f70abb9346db2b11c273f34eae bytes=6738 -->
## FILE: src/handwritten/errors.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/errors.py`
- sha256: `fa9c75d3c40a1df12c551fe80e5c5cf39fca15f70abb9346db2b11c273f34eae`
- bytes: 6738

````python
"""NI-DAQmx error classes."""

import warnings

import deprecation

from nidaqmx.error_codes import DAQmxErrors, DAQmxWarnings

__all__ = ["DaqError", "DaqReadError", "DaqWriteError", "DaqWarning", "DaqResourceWarning"]


class Error(Exception):
    """Base error class for module."""

    pass


class DaqNotFoundError(Error):
    """Error raised when NI-DAQmx driver is not installed."""

    pass


class DaqNotSupportedError(Error):
    """Error raised when DAQmx is not supported on this platform."""

    pass


class DaqFunctionNotSupportedError(Error):
    """Error raised when a specific function isn't supported by the installed NI-DAQmx driver."""

    pass


class DaqError(Error):
    """Error raised by any DAQmx method."""

    def __init__(self, message, error_code, task_name=""):
        """Initialize a new DaqError.

        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        self._error_code = int(error_code)

        try:
            self._error_type = DAQmxErrors(self._error_code)
        except ValueError:
            self._error_type = DAQmxErrors.UNKNOWN

        # If message is empty, we try to put at least some information in it
        if not message:
            message = f"Description could not be found for the status code.\n\nStatus Code: {self._error_code}"

        if task_name:
            message = f"{message}\n\nTask Name: {task_name}"

        # We do not know where the error description came from, so we add the status code if it is not already in the message  # noqa: W505 - doc line too long (125 > 100 characters) (auto-generated noqa)
        if str(self._error_code) not in message:
            message = f"{message}\n\nStatus Code: {self._error_code}"

        super().__init__(message)

    @property
    def error_code(self):
        """int: Specifies the NI-DAQmx error code."""
        return self._error_code

    @property
    def error_type(self):
        """:class:`nidaqmx.error_codes.DAQmxErrors`: Specifies the NI-DAQmx error type."""
        return self._error_type


class DaqReadError(DaqError):
    """Error raised by DAQmx write method that includes the amount of data that was read."""

    def __init__(self, message, error_code, samps_per_chan_read, task_name=""):
        """Initialize a new DaqReadError.

        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        super().__init__(message, error_code, task_name)

        self._samps_per_chan_read = samps_per_chan_read

    @property
    def samps_per_chan_read(self):
        """int: Indicates the number of samples successfully read."""
        return self._samps_per_chan_read


class DaqWriteError(DaqError):
    """Error raised by DAQmx write method that includes the amount of data that was written."""

    def __init__(self, message, error_code, samps_per_chan_written, task_name=""):
        """Initialize a new DaqWriteError.

        Args:
            message (string): Specifies the error message.
            error_code (int): Specifies the NI-DAQmx error code.
            samps_per_chan_written (int): Specifies the number of samples written.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        super().__init__(message, error_code, task_name)

        self._samps_per_chan_written = samps_per_chan_written

    @property
    def samps_per_chan_written(self):
        """int: Indicates the number of samples successfully written."""
        return self._samps_per_chan_written


class DaqWarning(Warning):
    """Warning raised by any NI-DAQmx method."""

    def __init__(self, message, error_code):
        """Initialize a new DaqWarning.

        Args:
            message (string): Specifies the warning message.
            error_code (int): Specifies the NI-DAQmx error code.
        """
        super().__init__(f"\nWarning {error_code} occurred.\n\n{message}")

        self._error_code = int(error_code)

        try:
            self._error_type = DAQmxWarnings(self._error_code)
        except ValueError:
            self._error_type = DAQmxWarnings.UNKNOWN

    @property
    def error_code(self):
        """int: Specifies the NI-DAQmx error code."""
        return self._error_code

    @property
    def error_type(self):
        """:class:`nidaqmx.error_codes.DAQmxWarnings`: Specifies the NI-DAQmx error type."""
        return self._error_type


class DaqResourceWarning(ResourceWarning):
    """Warning about DAQ resource usage, such as a leaking an NI-DAQmx task."""

    pass


warnings.filterwarnings("always", category=DaqWarning)
warnings.filterwarnings("always", category=DaqResourceWarning)


@deprecation.deprecated(
    deprecated_in="0.8.0", details="This function will be removed in a future update."
)
def check_for_error(error_code, samps_per_chan_written=None, samps_per_chan_read=None):
    from nidaqmx._library_interpreter import LibraryInterpreter

    return LibraryInterpreter().check_for_error(
        error_code, samps_per_chan_written, samps_per_chan_read
    )


@deprecation.deprecated(
    deprecated_in="0.8.0", details="This function will be removed in a future update."
)
def is_string_buffer_too_small(error_code):
    import nidaqmx._library_interpreter

    return nidaqmx._library_interpreter.is_string_buffer_too_small(error_code)


@deprecation.deprecated(
    deprecated_in="0.8.0", details="This function will be removed in a future update."
)
def is_array_buffer_too_small(error_code):
    import nidaqmx._library_interpreter

    return nidaqmx._library_interpreter.is_array_buffer_too_small(error_code)


class RpcError(Error):
    """An error specific to sessions to the NI gRPC Device Server."""

    def __init__(self, rpc_code, description):
        """Initialize a new RpcError."""
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc

            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super().__init__(rpc_error + ": " + self.description)


class FeatureNotSupportedError(Exception):
    """The feature is not supported at the current code readiness level."""
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/grpc_session_options.py sha256=2f2abbd6a5e40d6e7a66431bcb3aa6dc2aa920f65839384b9caa9c08331ec754 bytes=3978 -->
## FILE: src/handwritten/grpc_session_options.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/grpc_session_options.py`
- sha256: `2f2abbd6a5e40d6e7a66431bcb3aa6dc2aa920f65839384b9caa9c08331ec754`
- bytes: 3978

````python
"""NI-DAQmx gRPC session options."""

from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import grpc


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
GRPC_SERVICE_INTERFACE_NAME = "nidaqmx_grpc.NiDAQmx"

# This constant specifies the API license key required by the NI gRPC Device Server that comes with
# MeasurementLink 2023 Q1.
MEASUREMENTLINK_23Q1_NIDAQMX_PYTHON_API_KEY = "147D9BA7-BE75-4B29-8591-BA4A737AA8CF"


class SessionInitializationBehavior(IntEnum):
    """Specifies how to initialize sessions on the server."""

    AUTO = 0
    r"""
    The NI gRPC Device Server will attach to an existing session with the specified name if it exists, otherwise the server
    will initialize a new session.
    Note:
    When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
    was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
    server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.
    """  # noqa: W505 - doc line too long (123 > 100 characters) (auto-generated noqa)
    INITIALIZE_SERVER_SESSION = 1
    r"""
    Require the NI gRPC Device Server to initialize a new session with the specified name.
    Note:
    When using the Session as a context manager and the context exits, it will automatically close the
    server session.
    """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
    ATTACH_TO_SERVER_SESSION = 2
    r"""
    Require the NI gRPC Device Server to attach to an existing session with the specified name.
    Note:
    When using the Session as a context manager and the context exits, it will detach from the server session
    and leave it open.
    """  # noqa: W505 - doc line too long (109 > 100 characters) (auto-generated noqa)


class GrpcSessionOptions:
    """Collection of options that specifies session behaviors related to gRPC."""

    def __init__(
        self,
        grpc_channel: grpc.Channel,
        session_name: str,
        *,
        api_key=MEASUREMENTLINK_23Q1_NIDAQMX_PYTHON_API_KEY,
        initialization_behavior=SessionInitializationBehavior.AUTO,
    ):
        """Initialize a new GrpcSessionOptions.

        Args:
            grpc_channel (grpc.Channel): Specifies the channel to the NI gRPC Device Server.
            session_name (str): User-specified name that identifies the driver session on the NI gRPC Device
                Server. This is different from the resource name parameter many APIs take as a separate
                parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
                You can use an empty string if you want to always initialize a new session on the server.
                To attach to an existing session, you must specify the session name it was initialized with.
            api_key (str): Specifies the API license key required by the NI gRPC Device Server.
            initialization_behavior (enum): Specifies whether it is acceptable to initialize a new
                session or attach to an existing one, or if only one of the behaviors is desired.
                The driver session exists on the NI gRPC Device Server.
        """  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/__init__.py sha256=c2d3808de506b10840dc2e02af23e38c0ba0b0790f12a02cca43eaf124f7d00d bytes=1163 -->
## FILE: src/handwritten/stream_readers/__init__.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/__init__.py`
- sha256: `c2d3808de506b10840dc2e02af23e38c0ba0b0790f12a02cca43eaf124f7d00d`
- bytes: 1163

````python
"""NI-DAQmx stream readers.

This package provides classes for reading samples from NI-DAQmx tasks.
"""

from __future__ import annotations

from nidaqmx import DaqError
from nidaqmx.stream_readers._analog_multi_channel_reader import AnalogMultiChannelReader
from nidaqmx.stream_readers._analog_single_channel_reader import (
    AnalogSingleChannelReader,
)
from nidaqmx.stream_readers._analog_unscaled_reader import AnalogUnscaledReader
from nidaqmx.stream_readers._counter_reader import CounterReader
from nidaqmx.stream_readers._digital_multi_channel_reader import (
    DigitalMultiChannelReader,
)
from nidaqmx.stream_readers._digital_single_channel_reader import (
    DigitalSingleChannelReader,
)
from nidaqmx.stream_readers._power_readers import (
    PowerBinaryReader,
    PowerMultiChannelReader,
    PowerSingleChannelReader,
)

__all__ = [
    "AnalogSingleChannelReader",
    "AnalogMultiChannelReader",
    "AnalogUnscaledReader",
    "CounterReader",
    "DigitalSingleChannelReader",
    "DigitalMultiChannelReader",
    "PowerSingleChannelReader",
    "PowerMultiChannelReader",
    "PowerBinaryReader",
]
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_analog_multi_channel_reader.py sha256=8774c8cc81abf21700b0af1f5d28f0c97df0f4c1eb3bec5a9ee37d66bd850456 bytes=11829 -->
## FILE: src/handwritten/stream_readers/_analog_multi_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_analog_multi_channel_reader.py`
- sha256: `8774c8cc81abf21700b0af1f5d28f0c97df0f4c1eb3bec5a9ee37d66bd850456`
- bytes: 11829

````python
from __future__ import annotations

import numpy
from nitypes.waveform import AnalogWaveform

from nidaqmx import DaqError
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode, ReallocationPolicy
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase


class AnalogMultiChannelReader(ChannelReaderBase):
    """Reads samples from one or more analog input channels in an NI-DAQmx task."""

    def read_many_sample(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more floating-point samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of floating-point values to hold the samples
                requested. The size of the array must be large enough to
                hold all requested samples from all channels in the
                task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property to True may marginally adversely
                impact the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_analog_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_one_sample(self, data, timeout=10):
        """Reads a single floating-point sample from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the samples
                requested.

                Each element in the array corresponds to a sample from
                each channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.
        """
        self._verify_array(data, 1, True, False)

        self._interpreter.read_analog_f64(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveforms(
        self,
        waveforms: list[AnalogWaveform[numpy.float64]],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int:
        """Reads one or more floating-point samples from one or more analog input channels into a list of waveforms.

        This read method optionally accepts a preallocated list of waveforms to hold
        the samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated list of waveforms is valuable in continuous
        acquisition scenarios, where the same waveforms can be used
        repeatedly in each call to the method.

        Args:
            waveforms (list[AnalogWaveform]): Specifies a list of AnalogWaveform
                objects to use for reading samples into.
                The list must contain one waveform for each channel in the task.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            reallocation_policy (Optional[ReallocationPolicy]): Specifies
                the reallocation policy to use when the read yields more
                samples than the current capacity of the waveform.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """  # noqa: W505 - doc line too long (116 > 100 characters) (auto-generated noqa)
        number_of_channels = self._in_stream.num_chans
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        if len(waveforms) != number_of_channels:
            raise DaqError(
                f"The number of waveforms provided ({len(waveforms)}) does not match "
                f"the number of channels in the task ({number_of_channels}). Please provide "
                "one waveform for each channel.",
                DAQmxErrors.MISMATCHED_INPUT_ARRAY_SIZES,
                task_name=self._task.name,
            )

        for i, waveform in enumerate(waveforms):
            if waveform.start_index + number_of_samples_per_channel > waveform.capacity:
                if reallocation_policy == ReallocationPolicy.TO_GROW:
                    waveform.capacity = waveform.start_index + number_of_samples_per_channel
                else:
                    raise DaqError(
                        f"The waveform at index {i} does not have enough space ({waveform.capacity - waveform.start_index}) to hold "
                        f"the requested number of samples ({number_of_samples_per_channel}). Please provide larger "
                        "waveforms or adjust the number of samples requested.",
                        DAQmxErrors.READ_BUFFER_TOO_SMALL,
                        task_name=self._task.name,
                    )

        return self._interpreter.read_analog_waveforms(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            waveforms,
            self._in_stream.waveform_attribute_mode,
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_analog_single_channel_reader.py sha256=9c7214bc53d45723f0fbc7d95959f37e5a7de31047c1192cbb2f46f2d301be83 bytes=9224 -->
## FILE: src/handwritten/stream_readers/_analog_single_channel_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_analog_single_channel_reader.py`
- sha256: `9c7214bc53d45723f0fbc7d95959f37e5a7de31047c1192cbb2f46f2d301be83`
- bytes: 9224

````python
from __future__ import annotations

import numpy
from nitypes.waveform import AnalogWaveform

from nidaqmx import DaqError
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode, ReallocationPolicy
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase


class AnalogSingleChannelReader(ChannelReaderBase):
    """Reads samples from an analog input channel in an NI-DAQmx task."""

    def read_many_sample(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more floating-point samples from a single analog input channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the samples
                requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_analog_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_one_sample(self, timeout=10):
        """Reads a single floating-point sample from a single analog input channel in a task.

        Args:
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            float:

            Indicates a single floating-point sample from the task.
        """
        return self._interpreter.read_analog_scalar_f64(self._handle, timeout)

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveform(
        self,
        waveform: AnalogWaveform[numpy.float64],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int:
        """Reads one or more floating-point samples from a single analog input channel into a waveform.

        This read method optionally accepts a preallocated waveform to hold
        the samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated waveform is valuable in continuous
        acquisition scenarios, where the same waveform can be used
        repeatedly in each call to the method.

        Args:
            waveform (AnalogWaveform): Specifies an AnalogWaveform object
                to use for reading samples into.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            reallocation_policy (Optional[ReallocationPolicy]): Specifies
                the reallocation policy to use when the read yields more
                samples than the current capacity of the waveform.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired.
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        if waveform.start_index + number_of_samples_per_channel > waveform.capacity:
            if reallocation_policy == ReallocationPolicy.TO_GROW:
                waveform.capacity = waveform.start_index + number_of_samples_per_channel
            else:
                raise DaqError(
                    f"The provided waveform does not have enough space ({waveform.capacity - waveform.start_index}) to hold "
                    f"the requested number of samples ({number_of_samples_per_channel}). Please provide a larger "
                    "waveform or adjust the number of samples requested.",
                    DAQmxErrors.READ_BUFFER_TOO_SMALL,
                    task_name=self._task.name,
                )

        return self._interpreter.read_analog_waveform(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            waveform,
            self._in_stream.waveform_attribute_mode,
        )
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_analog_unscaled_reader.py sha256=56afb1e9d26793ae622bd815cf6b1c9dfd24b6a56f4961319e67c1ceee5ada38 bytes=18077 -->
## FILE: src/handwritten/stream_readers/_analog_unscaled_reader.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_analog_unscaled_reader.py`
- sha256: `56afb1e9d26793ae622bd815cf6b1c9dfd24b6a56f4961319e67c1ceee5ada38`
- bytes: 18077

````python
from __future__ import annotations

from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase


class AnalogUnscaledReader(ChannelReaderBase):
    """Reads unscaled samples from one or more analog input channels in an NI-DAQmx task."""

    def read_int16(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0):
        """Reads one or more unscaled 16-bit integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 16-bit integer values to hold the
                samples requested. The size of the array must be large
                enough to hold all requested samples from all channels
                in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """  # noqa: W505 - doc line too long (110 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_binary_i16(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_int32(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0):
        """Reads one or more unscaled 32-bit integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 32-bit integer values to hold the
                samples requested. The size of the array must be large
                enough to hold all requested samples from all channels
                in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """  # noqa: W505 - doc line too long (110 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_binary_i32(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_uint16(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0):
        """Reads one or more unscaled 16-bit unsigned integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 16-bit unsigned integer values to
                hold the samples requested. The size of the array must
                be large enough to hold all requested samples from all
                channels in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """  # noqa: W505 - doc line too long (119 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_binary_u16(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_uint32(self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0):
        """Reads one or more unscaled unsigned 32-bit integer samples from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of unscaled 32-bit unsigned integer values to
                hold the samples requested. The size of the array must
                be large enough to hold all requested samples from all
                channels in the task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property may marginally adversely impact
                the performance of the method.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.

        Returns:
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """  # noqa: W505 - doc line too long (119 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_binary_u32(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read
````

<!--NI_OSS_SOURCE repo=nidaqmx-python path=src/handwritten/stream_readers/_channel_reader_base.py sha256=097339a927dbc930a7eb721ff59c4cbaae87163db78d125a4df4c1eff5831bf9 bytes=5117 -->
## FILE: src/handwritten/stream_readers/_channel_reader_base.py

- repository: `ni/nidaqmx-python`
- source_path: `src/handwritten/stream_readers/_channel_reader_base.py`
- sha256: `097339a927dbc930a7eb721ff59c4cbaae87163db78d125a4df4c1eff5831bf9`
- bytes: 5117

````python
from __future__ import annotations

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors


class ChannelReaderBase:
    """Defines base class for all NI-DAQmx stream readers."""

    def __init__(self, task_in_stream):
        """Initialize a new ChannelReaderBase.

        Args:
            task_in_stream: Specifies the input stream associated with
                an NI-DAQmx task from which to read samples.
        """
        self._in_stream = task_in_stream
        self._task = task_in_stream._task
        self._handle = task_in_stream._task._handle
        self._interpreter = task_in_stream._task._interpreter

        self._verify_array_shape = True

    @property
    def verify_array_shape(self):
        """bool: Specifies whether to verify the shape of NumPy arrays.

        Defaults to True when this object is instantiated.

        Setting this property to True may marginally adversely
        impact the performance of read methods.
        """
        return self._verify_array_shape

    @verify_array_shape.setter
    def verify_array_shape(self, val):
        self._verify_array_shape = val

    def _verify_array(self, data, number_of_samples_per_channel, is_many_chan, is_many_samp):
        """Verify the shape of a NumPy array.

        Verifies that the shape of the specified NumPy array can be used
        to read multiple samples from the current task which contains
        one or more channels, if the "verify_array_shape" property is
        set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            number_of_samples_per_channel (int): Specifies the number of
                samples per channel requested.
            is_many_chan (bool): Specifies if the read method is a many
                channel version.
            is_many_samp (bool): Specifies if the read method is a many
                samples version.
        """
        if not self._verify_array_shape:
            return

        number_of_channels = self._in_stream.num_chans

        array_shape: tuple[int, ...] | None = None
        if is_many_chan:
            if is_many_samp:
                array_shape = (number_of_channels, number_of_samples_per_channel)
            else:
                array_shape = (number_of_channels,)
        else:
            if is_many_samp:
                array_shape = (number_of_samples_per_channel,)

        if array_shape is not None and data.shape != array_shape:
            raise DaqError(
                "Read cannot be performed because the NumPy array passed into "
                "this function is not shaped correctly. You must pass in a "
                "NumPy array of the correct shape based on the number of "
                "channels in task and the number of samples per channel "
                "requested.\n\n"
                "Shape of NumPy Array provided: {}\n"
                "Shape of NumPy Array required: {}".format(data.shape, array_shape),
                DAQmxErrors.UNKNOWN,
                task_name=self._task.name,
            )

    def _verify_array_digital_lines(self, data, is_many_chan, is_many_line):
        """Verify the shape of a NumPy array of digital lines.

        Verifies that the shape of the specified NumPy array can be used
        to read samples from the current task which contains one or more
        channels that have one or more digital lines per channel, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the read method is a
                many channel version.
            is_many_line (bool): Specifies if the read method is a
                many line version.
        """
        if not self._verify_array_shape:
            return

        number_of_channels = self._in_stream.num_chans
        number_of_lines = self._in_stream.di_num_booleans_per_chan

        array_shape: tuple[int, ...] | None = None
        if is_many_chan:
            if is_many_line:
                array_shape = (number_of_channels, number_of_lines)
            else:
                array_shape = (number_of_channels,)
        else:
            if is_many_line:
                array_shape = (number_of_lines,)

        if array_shape is not None and data.shape != array_shape:
            raise DaqError(
                "Read cannot be performed because the NumPy array passed into "
                "this function is not shaped correctly. You must pass in a "
                "NumPy array of the correct shape based on the number of "
                "channels in task and the number of digital lines per "
                "channel.\n\n"
                "Shape of NumPy Array provided: {}\n"
                "Shape of NumPy Array required: {}".format(data.shape, array_shape),
                DAQmxErrors.UNKNOWN,
                task_name=self._task.name,
            )
````
