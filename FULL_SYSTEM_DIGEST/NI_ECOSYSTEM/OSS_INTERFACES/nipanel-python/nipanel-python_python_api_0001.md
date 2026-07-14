# NI PYTHON API DIGEST: nipanel-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nipanel-python commit=4d45604ddd6c83d79491d1dfd6c27176e636a83d -->

<!--NI_PYTHON_API repo=nipanel-python path=docs/conf.py -->
## PYTHON MODULE: docs/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def skip_aliases(app, what, name, obj, skip, options)`

Skip documentation for classes that are exported from multiple modules.

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=nipanel-python path=examples/all_types/all_types.py -->
## PYTHON MODULE: examples/all_types/all_types.py

### MODULE DOCSTRING

An example that demonstrates the supported data types for nipanel scripts.

<!--NI_PYTHON_API repo=nipanel-python path=examples/all_types/all_types_panel.py -->
## PYTHON MODULE: examples/all_types/all_types_panel.py

### MODULE DOCSTRING

A Streamlit visualization panel for the all_types.py example script.

<!--NI_PYTHON_API repo=nipanel-python path=examples/all_types/define_types.py -->
## PYTHON MODULE: examples/all_types/define_types.py

### MODULE DOCSTRING

Define types.

### `class MyIntFlags(enum.IntFlag)`

Example of an IntFlag enum.

### `class MyIntableFlags(enum.Flag)`

Example of an Flag enum with int values.

### `class MyIntEnum(enum.IntEnum)`

Example of an IntEnum enum.

### `class MyIntableEnum(enum.Enum)`

Example of an enum with int values.

### `class MyStrEnum(str, enum.Enum)`

Example of a mixin string enum.

### `class MyStringableEnum(enum.Enum)`

Example of an enum with string values.

### `class MyMixedEnum(enum.Enum)`

Example of an enum with mixed values.

<!--NI_PYTHON_API repo=nipanel-python path=examples/hello/hello.py -->
## PYTHON MODULE: examples/hello/hello.py

### MODULE DOCSTRING

This example demonstrates how to open/update a Streamlit application using nipanel package.

<!--NI_PYTHON_API repo=nipanel-python path=examples/hello/hello_panel.py -->
## PYTHON MODULE: examples/hello/hello_panel.py

### MODULE DOCSTRING

A Streamlit visualization panel for the hello.py example script.

<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_analog_input_fft/nidaqmx_analog_input_fft.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_analog_input_fft/nidaqmx_analog_input_fft.py

### MODULE DOCSTRING

Example of analog input voltage acquisition with a Fast Fourier Transform.

This example demonstrates how to acquire a continuous amount of data using the
DAQ device's internal clock. The settings are configured from the Streamlit
panel, and the acquired data is displayed on a graph. An FFT is computed from
the acquired data and displayed on a separate graph. Refer to the panel script
for details: nidaqmx_analog_input_fft_panel.py


<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_analog_input_fft/nidaqmx_analog_input_fft_panel.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_analog_input_fft/nidaqmx_analog_input_fft_panel.py

### MODULE DOCSTRING

Streamlit visualization script to display data acquired by nidaqmx_continuous_analog_input.py.

### `def _click_start() -> None`

### `def _click_stop() -> None`

<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_analog_input_filtering/nidaqmx_analog_input_filtering.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_analog_input_filtering/nidaqmx_analog_input_filtering.py

### MODULE DOCSTRING

Example of analog input voltage, current, or strain gage acquisition.

This example demonstrates how to acquire a continuous amount of data using the
DAQ device's internal clock. There is sensor-specific configuration and
hardware filtering can be enabled. The settings are configured from the
Streamlit panel, and the acquired data is displayed on a graph. Refer to the
panel script for details: nidaqmx_analog_input_filtering_panel.py


<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_analog_input_filtering/nidaqmx_analog_input_filtering_panel.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_analog_input_filtering/nidaqmx_analog_input_filtering_panel.py

### MODULE DOCSTRING

Streamlit visualization script to display data acquired by nidaqmx_analog_input_filtering.py.

### `def _click_start() -> None`

### `def _click_stop() -> None`

<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_analog_output_voltage/nidaqmx_analog_output_voltage.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_analog_output_voltage/nidaqmx_analog_output_voltage.py

### MODULE DOCSTRING

Example of analog output voltage generation.

This example demonstrates how to output a continuous periodic waveform using an
internal sample clock. The settings are configured from the Streamlit panel,
and the acquired data is displayed on a graph. Refer to the panel script for
details: nidaqmx_analog_output_voltage_panel.py


<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_analog_output_voltage/nidaqmx_analog_output_voltage_panel.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_analog_output_voltage/nidaqmx_analog_output_voltage_panel.py

### MODULE DOCSTRING

Streamlit visualization script to display data acquired by nidaqmx_analog_output_voltage.py.

### `def _click_start() -> None`

### `def _click_stop() -> None`

<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_continuous_analog_input/nidaqmx_continuous_analog_input.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_continuous_analog_input/nidaqmx_continuous_analog_input.py

### MODULE DOCSTRING

Example of analog input voltage acquisition.

This example demonstrates how to acquire a continuous amount of data using the
DAQ device's internal clock. The settings are configured from the Streamlit
panel, and the acquired data is displayed on a graph. Refer to the panel script
for details: nidaqmx_continuous_analog_input_panel.py


<!--NI_PYTHON_API repo=nipanel-python path=examples/nidaqmx/nidaqmx_continuous_analog_input/nidaqmx_continuous_analog_input_panel.py -->
## PYTHON MODULE: examples/nidaqmx/nidaqmx_continuous_analog_input/nidaqmx_continuous_analog_input_panel.py

### MODULE DOCSTRING

Streamlit visualization script to display data acquired by nidaqmx_continuous_analog_input.py.

### `def _click_start() -> None`

### `def _click_stop() -> None`

<!--NI_PYTHON_API repo=nipanel-python path=examples/niscope/niscope_binary_acquisition/niscope_binary_acquisition.py -->
## PYTHON MODULE: examples/niscope/niscope_binary_acquisition/niscope_binary_acquisition.py

### MODULE DOCSTRING

Continuously acquires waveforms from NI-SCOPE, processes/scales them.

<!--NI_PYTHON_API repo=nipanel-python path=examples/niscope/niscope_binary_acquisition/niscope_binary_acquisition_panel.py -->
## PYTHON MODULE: examples/niscope/niscope_binary_acquisition/niscope_binary_acquisition_panel.py

### MODULE DOCSTRING

Streamlit dashboard for visualizing NI-SCOPE waveform data in real time.

<!--NI_PYTHON_API repo=nipanel-python path=examples/niscope/niscope_configured_acquisition/niscope_configured_acquisition.py -->
## PYTHON MODULE: examples/niscope/niscope_configured_acquisition/niscope_configured_acquisition.py

### MODULE DOCSTRING

Continuously acquires waveforms from NI-SCOPE, and configures desired acquisition settings.

<!--NI_PYTHON_API repo=nipanel-python path=examples/niscope/niscope_configured_acquisition/niscope_configured_acquisition_panel.py -->
## PYTHON MODULE: examples/niscope/niscope_configured_acquisition/niscope_configured_acquisition_panel.py

### MODULE DOCSTRING

Streamlit dashboard for visualizing NI-SCOPE waveform data in real time.

### `class ChannelSource(Enum)`

Enum for channel source options.

<!--NI_PYTHON_API repo=nipanel-python path=examples/niscope/niscope_ex_fetch_forever/niscope_ex_fetch_forever.py -->
## PYTHON MODULE: examples/niscope/niscope_ex_fetch_forever/niscope_ex_fetch_forever.py

### MODULE DOCSTRING

Continuously acquires waveforms from NI-SCOPE, processes/scales them.

<!--NI_PYTHON_API repo=nipanel-python path=examples/niscope/niscope_ex_fetch_forever/niscope_ex_fetch_forever_panel.py -->
## PYTHON MODULE: examples/niscope/niscope_ex_fetch_forever/niscope_ex_fetch_forever_panel.py

### MODULE DOCSTRING

Streamlit dashboard for visualizing NI-SCOPE waveform data in real time.

<!--NI_PYTHON_API repo=nipanel-python path=examples/performance_checker/performance_checker.py -->
## PYTHON MODULE: examples/performance_checker/performance_checker.py

### MODULE DOCSTRING

Check the performance of get_value and set_value methods in nipanel.

### `def _set_time_points() -> None`

### `def _set_amplitude() -> None`

### `def _get_time_points() -> None`

### `def _get_amplitude() -> None`

### `def _get_unset_value() -> None`

<!--NI_PYTHON_API repo=nipanel-python path=examples/performance_checker/performance_checker_panel.py -->
## PYTHON MODULE: examples/performance_checker/performance_checker_panel.py

### MODULE DOCSTRING

A Streamlit visualization panel for the performance_checker.py example script.

### `def profile_get_value(panel: 'nipanel.PanelValueAccessor', value_id: str, default_value: Any=None, num_runs: int=5) -> Tuple[Any, float]`

Measure the time it takes to get a value from the panel.

    Args:
        panel: The panel accessor object
        value_id: The ID of the value to get
        default_value: Default value if the value is not found
        num_runs: Number of runs for timing

    Returns:
        A tuple of (value, time_ms) where time_ms is the time in milliseconds
    

<!--NI_PYTHON_API repo=nipanel-python path=examples/simple_graph/simple_graph.py -->
## PYTHON MODULE: examples/simple_graph/simple_graph.py

### MODULE DOCSTRING

Example of using nipanel to display a sine wave graph using st_echarts.

<!--NI_PYTHON_API repo=nipanel-python path=examples/simple_graph/simple_graph_panel.py -->
## PYTHON MODULE: examples/simple_graph/simple_graph_panel.py

### MODULE DOCSTRING

A Streamlit visualization panel for the simple_graph.py example script.

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/__init__.py -->
## PYTHON MODULE: src/nipanel/__init__.py

### MODULE DOCSTRING

The NI Panel.

- `__all__ = ['create_streamlit_panel', 'get_streamlit_panel_accessor', 'PanelValueAccessor', 'StreamlitPanel']`

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/_convert.py -->
## PYTHON MODULE: src/nipanel/_convert.py

### MODULE DOCSTRING

Functions to convert between different data formats.

- `_CONVERTIBLE_TYPES = [BoolConverter(), BytesConverter(), FloatConverter(), IntConverter(), StrConverter(), DTDateTimeConverter(), DTTimeDeltaConverter(), BTDateTimeConverter(), BTTimeDeltaConverter(), BoolCollectionConverter(), BytesCollectionConverter(), DigitalWaveformConverter(), Double2DArrayConverter(), DoubleAnalogWaveformConverter(), DoubleComplexWaveformConverter(), DoubleSpectrumConverter(), FloatCollectionConverter(), HTDateTimeConverter(), HTTimeDeltaConverter(), Int16AnalogWaveformConverter(), Int16ComplexWaveformConverter(), IntCollectionConverter(), StrCollectionConverter(), ScalarConverter(), VectorConverter()]`

- `_CONVERTER_FOR_PYTHON_TYPE = {entry.python_typename: entry for entry in _CONVERTIBLE_TYPES}`

- `_CONVERTER_FOR_GRPC_TYPE = {entry.protobuf_typename: entry for entry in _CONVERTIBLE_TYPES}`

- `_SUPPORTED_PYTHON_TYPES = _CONVERTER_FOR_PYTHON_TYPE.keys()`

- `_SKIPPED_COLLECTIONS = (str, bytes, dict, enum.Enum, Vector)`

### `def to_any(python_value: object) -> any_pb2.Any`

Convert a Python object to a protobuf Any.

### `def _get_best_matching_type(python_value: object) -> str`

### `def from_any(protobuf_any: any_pb2.Any) -> object`

Convert a protobuf Any to a Python object.

### `def is_supported_type(value: object) -> bool`

Check if a given Python value can be converted to protobuf Any.

### `def _get_candidate_strings(candidates: Iterable[type]) -> list[str]`

### `def _create_python_typename(candidate_name: str, container_types: Iterable[type], additional_info: str) -> str`

### `def _get_additional_type_info_string(python_value: object) -> str`

### `def _is_collection_for_convert(python_value: object) -> bool`

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/_panel_client.py -->
## PYTHON MODULE: src/nipanel/_panel_client.py

- `_P = ParamSpec('_P')`

- `_T = TypeVar('_T')`

- `PANEL_SERVICE = 'ni.panels.v1.PanelService'`

### `class _PanelClient()`

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, grpc_channel_pool: GrpcChannelPool | None=None, grpc_channel: grpc.Channel | None=None) -> None`

#### `def start_streamlit_panel(self, panel_id: str, panel_script_path: pathlib.Path, python_interpreter_path: pathlib.Path) -> str`

#### `def stop_panel(self, panel_id: str, reset: bool) -> None`

#### `def enumerate_panels(self) -> dict[str, tuple[str, list[str]]]`

#### `def set_value(self, panel_id: str, value_id: str, value: object, notify: bool) -> None`

#### `def get_value(self, panel_id: str, value_id: str) -> object`

#### `def try_get_value(self, panel_id: str, value_id: str) -> object | None`

#### `def _get_stub(self) -> PanelServiceStub`

#### `def _invoke_with_retry(self, method: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> _T`

Invoke a gRPC method with retry logic.

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/_panel_value_accessor.py -->
## PYTHON MODULE: src/nipanel/_panel_value_accessor.py

- `_T = TypeVar('_T')`

### `class PanelValueAccessor(ABC)`

This class allows you to access values for a panel's controls.

#### `def __init__(self, *, panel_id: str, notify_on_set_value: bool=True, discovery_client: DiscoveryClient | None=None, grpc_channel_pool: GrpcChannelPool | None=None, grpc_channel: grpc.Channel | None=None) -> None`

Initialize the accessor.

#### `def panel_id(self) -> str`

Read-only accessor for the panel ID.

#### `def get_value(self, value_id: str) -> object`

#### `def get_value(self, value_id: str, default_value: _T) -> _T`

#### `def get_value(self, value_id: str, default_value: _T | None=None) -> _T | object`

Get the value for a control on the panel with an optional default value.

        Args:
            value_id: The id of the value
            default_value: The default value to return if the value is not set

        Returns:
            The value, or the default value if not set. The returned value will
            have the same type as default_value, if one was provided.

        Raises:
            KeyError: If the value is not set and no default value is provided
        

#### `def set_value(self, value_id: str, value: object) -> None`

Set the value for a control on the panel.

        Args:
            value_id: The id of the value
            value: The value
        

#### `def set_value_if_changed(self, value_id: str, value: object) -> None`

Set the value for a control on the panel only if it has changed since the last call.

        This method helps reduce unnecessary updates when the value hasn't changed.

        Args:
            value_id: The id of the value
            value: The value to set
        

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/_streamlit_panel.py -->
## PYTHON MODULE: src/nipanel/_streamlit_panel.py

### `class StreamlitPanel(PanelValueAccessor)`

This class allows you to open a Streamlit panel and specify values for its controls.

#### `def __init__(self, panel_id: str, panel_script_path: Path, *, discovery_client: DiscoveryClient | None=None, grpc_channel_pool: GrpcChannelPool | None=None, grpc_channel: grpc.Channel | None=None) -> None`

Create a panel using a Streamlit script for the user interface.

        Args:
            panel_id: A unique identifier for the panel.
            panel_script_path: The file path of the Streamlit script.
            discovery_client: An optional DiscoveryClient for service discovery.
            grpc_channel_pool: An optional GrpcChannelPool for managing gRPC channels.
            grpc_channel: An optional gRPC channel to use for communication with the panel service.

        Returns:
            A new StreamlitPanel instance.
        

#### `def panel_script_path(self) -> Path`

Read-only accessor for the streamlit script file path.

#### `def panel_url(self) -> str`

Read-only accessor for the panel's streamlit webpage URL.

#### `def _get_python_path(self) -> Path`

Get the Python interpreter path for the panel that ensures the same environment.

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/_streamlit_panel_initializer.py -->
## PYTHON MODULE: src/nipanel/_streamlit_panel_initializer.py

- `PANEL_ACCESSOR_KEY = 'StreamlitPanelValueAccessor'`

### `def create_streamlit_panel(streamlit_script_path: Path, panel_id: str='') -> StreamlitPanel`

Create a Streamlit panel with the specified script path.

    This function initializes a Streamlit panel using the provided script path. By default, it
    derives the panel ID from the script's path, which it expects to be a valid Streamlit script.
    For example, if the value for streamlit_script_path is "c:/example/some_example.py", then the
    panel's ID becomes "some_example". Alternatively, you can specify a custom panel_id.

    Use this function when you want to create a new panel instance to use in a Streamlit
    application. Do not call this function from within a Streamlit script.

    Args:
        streamlit_script_path: The file path of the Streamlit script to be used for the panel.
        panel_id: Optional custom panel ID. If not provided, it will be derived from the script
            path.

    Returns:
        A StreamlitPanel instance initialized with the given panel ID.
    

### `def get_streamlit_panel_accessor() -> PanelValueAccessor`

Initialize and return the Streamlit panel value accessor.

    This function retrieves the Streamlit panel value accessor for the current Streamlit script.
    This function should only be called from within a Streamlit script. The accessor will be cached
    in the Streamlit session state to ensure that it is reused across reruns of the script.

    Returns:
        A PanelValueAccessor instance for the current panel.
    

### `def _initialize_panel_from_base_path() -> PanelValueAccessor`

Validate and parse the Streamlit base URL path and return a PanelValueAccessor.

### `def _sync_session_state(panel: PanelValueAccessor) -> None`

Automatically read keyed control values from the session state.

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/controls/__init__.py -->
## PYTHON MODULE: src/nipanel/controls/__init__.py

### MODULE DOCSTRING

Controls for nipanel.

- `__all__ = ['enum_selectbox', 'flag_checkboxes']`

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/controls/_enum_selectbox.py -->
## PYTHON MODULE: src/nipanel/controls/_enum_selectbox.py

### MODULE DOCSTRING

A selectbox that allows selecting an Enum value.

### `def enum_selectbox(panel: PanelValueAccessor, label: str, value: TEnumType, key: str, disabled: bool=False, format_func: Callable[[Any], str]=lambda x: x[0]) -> TEnumType`

Create a selectbox for an Enum.

    The selectbox will display the names of all the enum values, and when a value is selected,
    that value will be stored in the panel under the specified key.

    Args:
        panel: The panel
        label: Label to display for the selectbox
        value: The default enum value to select (also determines the specific enum type)
        key: Key to use for storing the enum value in the panel

    Returns:
        The selected enum value of the same specific enum subclass as the input value
    

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/controls/_flag_checkboxes.py -->
## PYTHON MODULE: src/nipanel/controls/_flag_checkboxes.py

### MODULE DOCSTRING

A set of checkboxes for selecting Flag enum values.

### `def flag_checkboxes(panel: PanelValueAccessor, label: str, value: TFlagType, key: str, disabled_values: Optional[TFlagType]=None, label_formatter: Callable[[Flag], str]=lambda x: str(x.name)) -> TFlagType`

Create a set of checkboxes for a Flag enum.

    This will display a checkbox for each individual flag value in the enum. When checkboxes
    are selected or deselected, the combined Flag value will be stored in the panel under
    the specified key.

    Args:
        panel: The panel
        label: Label to display above the checkboxes
        value: The default Flag enum value (also determines the specific Flag enum type)
        key: Key to use for storing the Flag value in the panel
        disabled_values: A Flag enum value indicating which flags should be disabled.
                         If None or flag_type(0), no checkboxes are disabled.
        label_formatter: Function that formats the flag to a string for display. Default
                         uses flag.name.

    Returns:
        The selected Flag enum value with all selected flags combined
    

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/converters/__init__.py -->
## PYTHON MODULE: src/nipanel/converters/__init__.py

### MODULE DOCSTRING

Functions and classes to convert types between Python and protobuf.

### `class Converter(Generic[_TPythonType, _TProtobufType], ABC)`

A class that defines how to convert between Python objects and protobuf Any messages.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def python_typename(self) -> str`

The Python type name that this converter handles.

#### `def protobuf_message(self) -> Type[_TProtobufType]`

The type-specific protobuf message for the Python type.

#### `def protobuf_typename(self) -> str`

The protobuf name for the type.

#### `def to_protobuf_any(self, python_value: _TPythonType) -> any_pb2.Any`

Convert the Python object to its type-specific message and pack it as any_pb2.Any.

#### `def to_protobuf_message(self, python_value: _TPythonType) -> _TProtobufType`

Convert the Python object to its type-specific message.

#### `def to_python(self, protobuf_value: any_pb2.Any) -> _TPythonType`

Convert the protobuf Any message to its matching Python type.

#### `def to_python_value(self, protobuf_message: _TProtobufType) -> _TPythonType`

Convert the protobuf wrapper message to its matching Python type.

### `class CollectionConverter(Generic[_TItemType, _TProtobufType], Converter[Collection[_TItemType], _TProtobufType], ABC)`

A converter between a collection of Python objects and protobuf Any messages.

#### `def item_type(self) -> type`

The Python item type that this converter handles.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def python_typename(self) -> str`

The Python type name that this converter handles.

### `class CollectionConverter2D(Generic[_TItemType, _TProtobufType], Converter[Collection[Collection[_TItemType]], _TProtobufType], ABC)`

A converter between a 2D collection of Python objects and protobuf Any messages.

#### `def item_type(self) -> type`

The Python item type that this converter handles.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def python_typename(self) -> str`

The Python type name that this converter handles.

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/converters/builtin.py -->
## PYTHON MODULE: src/nipanel/converters/builtin.py

### MODULE DOCSTRING

Classes to convert between builtin Python scalars and containers.

### `class BoolConverter(Converter[bool, wrappers_pb2.BoolValue])`

A converter for boolean types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[wrappers_pb2.BoolValue]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: bool) -> wrappers_pb2.BoolValue`

Convert the Python bool to a protobuf wrappers_pb2.BoolValue.

#### `def to_python_value(self, protobuf_message: wrappers_pb2.BoolValue) -> bool`

Convert the protobuf message to a Python bool.

### `class BytesConverter(Converter[bytes, wrappers_pb2.BytesValue])`

A converter for byte string types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[wrappers_pb2.BytesValue]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: bytes) -> wrappers_pb2.BytesValue`

Convert the Python bytes string to a protobuf wrappers_pb2.BytesValue.

#### `def to_python_value(self, protobuf_message: wrappers_pb2.BytesValue) -> bytes`

Convert the protobuf message to a Python bytes string.

### `class FloatConverter(Converter[float, wrappers_pb2.DoubleValue])`

A converter for floating point types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[wrappers_pb2.DoubleValue]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: float) -> wrappers_pb2.DoubleValue`

Convert the Python float to a protobuf wrappers_pb2.DoubleValue.

#### `def to_python_value(self, protobuf_message: wrappers_pb2.DoubleValue) -> float`

Convert the protobuf message to a Python float.

### `class IntConverter(Converter[int, wrappers_pb2.Int64Value])`

A converter for integer types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[wrappers_pb2.Int64Value]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: int) -> wrappers_pb2.Int64Value`

Convert the Python int to a protobuf wrappers_pb2.Int64Value.

#### `def to_python_value(self, protobuf_message: wrappers_pb2.Int64Value) -> int`

Convert the protobuf message to a Python int.

### `class StrConverter(Converter[str, wrappers_pb2.StringValue])`

A converter for text string types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[wrappers_pb2.StringValue]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: str) -> wrappers_pb2.StringValue`

Convert the Python str to a protobuf wrappers_pb2.StringValue.

#### `def to_python_value(self, protobuf_message: wrappers_pb2.StringValue) -> str`

Convert the protobuf message to a Python string.

### `class DTDateTimeConverter(Converter[dt.datetime, timestamp_pb2.Timestamp])`

A converter for datetime.datetime types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[timestamp_pb2.Timestamp]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: dt.datetime) -> timestamp_pb2.Timestamp`

Convert the Python dt.datetime to a protobuf timestamp_pb2.Timestamp.

#### `def to_python_value(self, protobuf_message: timestamp_pb2.Timestamp) -> dt.datetime`

Convert the protobuf timestamp_pb2.Timestamp to a Python dt.datetime.

### `class DTTimeDeltaConverter(Converter[dt.timedelta, duration_pb2.Duration])`

A converter for datetime.timedelta types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[duration_pb2.Duration]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: dt.timedelta) -> duration_pb2.Duration`

Convert the Python dt.timedelta to a protobuf duration_pb2.Duration.

#### `def to_python_value(self, protobuf_message: duration_pb2.Duration) -> dt.timedelta`

Convert the protobuf timestamp_pb2.Timestamp to a Python dt.timedelta.

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/converters/protobuf_types.py -->
## PYTHON MODULE: src/nipanel/converters/protobuf_types.py

### MODULE DOCSTRING

Classes to convert between measurement specific protobuf types and containers.

### `class BoolCollectionConverter(CollectionConverter[bool, array_pb2.BoolArray])`

A converter for a Collection of bools.

#### `def item_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[array_pb2.BoolArray]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Collection[bool]) -> array_pb2.BoolArray`

Convert the collection of bools to array_pb2.BoolArray.

#### `def to_python_value(self, protobuf_message: array_pb2.BoolArray) -> Collection[bool]`

Convert the protobuf message to a Python collection of bools.

### `class BytesCollectionConverter(CollectionConverter[bytes, array_pb2.BytesArray])`

A converter for a Collection of byte strings.

#### `def item_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[array_pb2.BytesArray]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Collection[bytes]) -> array_pb2.BytesArray`

Convert the collection of byte strings to array_pb2.BytesArray.

#### `def to_python_value(self, protobuf_message: array_pb2.BytesArray) -> Collection[bytes]`

Convert the protobuf message to a Python collection of byte strings.

### `class FloatCollectionConverter(CollectionConverter[float, array_pb2.DoubleArray])`

A converter for a Collection of floats.

#### `def item_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[array_pb2.DoubleArray]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Collection[float]) -> array_pb2.DoubleArray`

Convert the collection of floats to array_pb2.DoubleArray.

#### `def to_python_value(self, protobuf_message: array_pb2.DoubleArray) -> Collection[float]`

Convert the protobuf message to a Python collection of floats.

### `class IntCollectionConverter(CollectionConverter[int, array_pb2.SInt64Array])`

A converter for a Collection of integers.

#### `def item_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[array_pb2.SInt64Array]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Collection[int]) -> array_pb2.SInt64Array`

Convert the collection of integers to array_pb2.SInt64Array.

#### `def to_python_value(self, protobuf_message: array_pb2.SInt64Array) -> Collection[int]`

Convert the protobuf message to a Python collection of integers.

### `class StrCollectionConverter(CollectionConverter[str, array_pb2.StringArray])`

A converter for a Collection of strings.

#### `def item_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[array_pb2.StringArray]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Collection[str]) -> array_pb2.StringArray`

Convert the collection of strings to array_pb2.StringCollection.

#### `def to_python_value(self, protobuf_message: array_pb2.StringArray) -> Collection[str]`

Convert the protobuf message to a Python collection of strings.

### `class Double2DArrayConverter(CollectionConverter2D[float, array_pb2.Double2DArray])`

A converter between Collection[Collection[float]] and Double2DArray.

#### `def item_type(self) -> type`

The Python item type that this converter handles.

#### `def protobuf_message(self) -> Type[array_pb2.Double2DArray]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Collection[Collection[float]]) -> array_pb2.Double2DArray`

Convert the Python Collection[Collection[float]] to a protobuf Double2DArray.

#### `def to_python_value(self, protobuf_message: array_pb2.Double2DArray) -> Collection[Collection[float]]`

Convert the protobuf Double2DArray to a Python Collection[Collection[float]].

### `class DoubleAnalogWaveformConverter(Converter[AnalogWaveform[np.float64], waveform_pb2.DoubleAnalogWaveform])`

A converter for AnalogWaveform types with double-precision data.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def python_typename(self) -> str`

The Python type name that this converter handles.

#### `def protobuf_message(self) -> Type[waveform_pb2.DoubleAnalogWaveform]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: AnalogWaveform[np.float64]) -> waveform_pb2.DoubleAnalogWaveform`

Convert the Python AnalogWaveform to a protobuf DoubleAnalogWaveform.

#### `def to_python_value(self, protobuf_message: waveform_pb2.DoubleAnalogWaveform) -> AnalogWaveform[np.float64]`

Convert the protobuf DoubleAnalogWaveform to a Python AnalogWaveform.

### `class Int16AnalogWaveformConverter(Converter[AnalogWaveform[np.int16], waveform_pb2.I16AnalogWaveform])`

A converter for AnalogWaveform types with 16-bit integer data.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def python_typename(self) -> str`

The Python type name that this converter handles.

#### `def protobuf_message(self) -> Type[waveform_pb2.I16AnalogWaveform]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: AnalogWaveform[np.int16]) -> waveform_pb2.I16AnalogWaveform`

Convert the Python AnalogWaveform to a protobuf Int16AnalogWaveformConverter.

#### `def to_python_value(self, protobuf_message: waveform_pb2.I16AnalogWaveform) -> AnalogWaveform[np.int16]`

Convert the protobuf Int16AnalogWaveformConverter to a Python AnalogWaveform.

### `class DoubleComplexWaveformConverter(Converter[ComplexWaveform[np.complex128], waveform_pb2.DoubleComplexWaveform])`

A converter for complex waveform types with 64-bit real and imaginary data.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def python_typename(self) -> str`

The Python type name that this converter handles.

#### `def protobuf_message(self) -> Type[waveform_pb2.DoubleComplexWaveform]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: ComplexWaveform[np.complex128]) -> waveform_pb2.DoubleComplexWaveform`

Convert the Python ComplexWaveform to a protobuf DoubleComplexWaveform.

#### `def to_python_value(self, protobuf_message: waveform_pb2.DoubleComplexWaveform) -> ComplexWaveform[np.complex128]`

Convert the protobuf DoubleComplexWaveform to a Python ComplexWaveform.

### `class Int16ComplexWaveformConverter(Converter[ComplexWaveform[ComplexInt32Base], waveform_pb2.I16ComplexWaveform])`

A converter for complex waveform types with 16-bit real and imaginary data.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def python_typename(self) -> str`

The Python type name that this converter handles.

#### `def protobuf_message(self) -> Type[waveform_pb2.I16ComplexWaveform]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: ComplexWaveform[ComplexInt32Base]) -> waveform_pb2.I16ComplexWaveform`

Convert the Python ComplexWaveform to a protobuf I16ComplexWaveform.

#### `def to_python_value(self, protobuf_message: waveform_pb2.I16ComplexWaveform) -> ComplexWaveform[ComplexInt32Base]`

Convert the protobuf I16ComplexWaveform to a Python ComplexWaveform.

### `class DigitalWaveformConverter(Converter[DigitalWaveform[Any], waveform_pb2.DigitalWaveform])`

A converter for digital waveform types.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[waveform_pb2.DigitalWaveform]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: DigitalWaveform[Any]) -> waveform_pb2.DigitalWaveform`

Convert the Python DigitalWaveform to a protobuf DigitalWaveform.

#### `def to_python_value(self, protobuf_message: waveform_pb2.DigitalWaveform) -> DigitalWaveform[Any]`

Convert the protobuf DigitalWaveform to a Python DigitalWaveform.

### `class DoubleSpectrumConverter(Converter[Spectrum[np.float64], waveform_pb2.DoubleSpectrum])`

A converter for spectrums with float64 data.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[waveform_pb2.DoubleSpectrum]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Spectrum[np.float64]) -> waveform_pb2.DoubleSpectrum`

Convert the Python Spectrum to a protobuf DoubleSpectrum.

#### `def to_python_value(self, protobuf_message: waveform_pb2.DoubleSpectrum) -> Spectrum[np.float64]`

Convert the protobuf DoubleSpectrum to a Python Spectrum.

### `class BTDateTimeConverter(Converter[bt.DateTime, precision_timestamp_pb2.PrecisionTimestamp])`

A converter for bintime.DateTime types.

    .. note:: The nipanel package will always convert PrecisionTimestamp messages to
        hightime.datetime objects using HTDateTimeConverter. To use bintime.DateTime
        values in a panel, you must pass a bintime.DateTime value for the default_value
        parameter of the get_value() method on the panel.
    

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[precision_timestamp_pb2.PrecisionTimestamp]`

The type-specific protobuf message for the Python type.

#### `def protobuf_typename(self) -> str`

The protobuf name for the type.

#### `def to_protobuf_message(self, python_value: bt.DateTime) -> precision_timestamp_pb2.PrecisionTimestamp`

Convert the Python DateTime to a protobuf PrecisionTimestamp.

#### `def to_python_value(self, protobuf_message: precision_timestamp_pb2.PrecisionTimestamp) -> bt.DateTime`

Convert the protobuf PrecisionTimestamp to a Python DateTime.

### `class BTTimeDeltaConverter(Converter[bt.TimeDelta, precision_duration_pb2.PrecisionDuration])`

A converter for bintime.TimeDelta types.

    .. note:: The nipanel package will always convert PrecisionDuration messages to
        hightime.timedelta objects using HTTimeDeltaConverter. To use bintime.TimeDelta
        values in a panel, you must pass a bintime.TimeDelta value for the default_value
        parameter of the get_value() method on the panel.
    

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[precision_duration_pb2.PrecisionDuration]`

The type-specific protobuf message for the Python type.

#### `def protobuf_typename(self) -> str`

The protobuf name for the type.

#### `def to_protobuf_message(self, python_value: bt.TimeDelta) -> precision_duration_pb2.PrecisionDuration`

Convert the Python TimeDelta to a protobuf PrecisionDuration.

#### `def to_python_value(self, protobuf_message: precision_duration_pb2.PrecisionDuration) -> bt.TimeDelta`

Convert the protobuf PrecisionDuration to a Python TimeDelta.

### `class HTDateTimeConverter(Converter[ht.datetime, precision_timestamp_pb2.PrecisionTimestamp])`

A converter for hightime.datetime objects.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[precision_timestamp_pb2.PrecisionTimestamp]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: ht.datetime) -> precision_timestamp_pb2.PrecisionTimestamp`

Convert the Python DateTime to a protobuf PrecisionTimestamp.

#### `def to_python_value(self, protobuf_message: precision_timestamp_pb2.PrecisionTimestamp) -> ht.datetime`

Convert the protobuf PrecisionTimestamp to a Python DateTime.

### `class HTTimeDeltaConverter(Converter[ht.timedelta, precision_duration_pb2.PrecisionDuration])`

A converter for hightime.timedelta objects.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[precision_duration_pb2.PrecisionDuration]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: ht.timedelta) -> precision_duration_pb2.PrecisionDuration`

Convert the Python timedelta to a protobuf PrecisionDuration.

#### `def to_python_value(self, protobuf_message: precision_duration_pb2.PrecisionDuration) -> ht.timedelta`

Convert the protobuf PrecisionDuration to a Python timedelta.

### `class ScalarConverter(Converter[Scalar[_AnyScalarType], scalar_pb2.Scalar])`

A converter for Scalar objects.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[scalar_pb2.Scalar]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Scalar[_AnyScalarType]) -> scalar_pb2.Scalar`

Convert the Python Scalar to a protobuf scalar_pb2.Scalar.

#### `def to_python_value(self, protobuf_message: scalar_pb2.Scalar) -> Scalar[_AnyScalarType]`

Convert the protobuf message to a Python Scalar.

### `class VectorConverter(Converter[Vector[_AnyScalarType], vector_pb2.Vector])`

A converter for Vector objects.

#### `def python_type(self) -> type`

The Python type that this converter handles.

#### `def protobuf_message(self) -> Type[vector_pb2.Vector]`

The type-specific protobuf message for the Python type.

#### `def to_protobuf_message(self, python_value: Vector[Any]) -> vector_pb2.Vector`

Convert the Python Vector to a protobuf vector_pb2.Vector.

#### `def to_python_value(self, protobuf_message: vector_pb2.Vector) -> Vector[_AnyScalarType]`

Convert the protobuf message to a Python Vector.

<!--NI_PYTHON_API repo=nipanel-python path=src/nipanel/streamlit_refresh/__init__.py -->
## PYTHON MODULE: src/nipanel/streamlit_refresh/__init__.py

### MODULE DOCSTRING

Initializes a refresh component for Streamlit.

### `def initialize_refresh_component(panel_id: str) -> CustomComponent`

Initialize a refresh component to the Streamlit app.

### `def _get_or_resolve_proxy() -> str`

<!--NI_PYTHON_API repo=nipanel-python path=tests/__init__.py -->
## PYTHON MODULE: tests/__init__.py

### MODULE DOCSTRING

Tests for the `nipanel` package.

<!--NI_PYTHON_API repo=nipanel-python path=tests/acceptance/__init__.py -->
## PYTHON MODULE: tests/acceptance/__init__.py

### MODULE DOCSTRING

Acceptance tests for the project.

<!--NI_PYTHON_API repo=nipanel-python path=tests/conftest.py -->
## PYTHON MODULE: tests/conftest.py

### MODULE DOCSTRING

Fixtures for testing.

### `def fake_python_panel_service() -> Generator[FakePythonPanelService]`

Fixture to create a FakePythonPanelServicer for testing.

### `def fake_panel_channel(fake_python_panel_service: FakePythonPanelService) -> Generator[grpc.Channel]`

Fixture to get a channel to the FakePythonPanelService.

### `def python_panel_service_stub(fake_panel_channel: grpc.Channel) -> Generator[PanelServiceStub]`

Fixture to get a PanelServiceStub, attached to a FakePythonPanelService.

<!--NI_PYTHON_API repo=nipanel-python path=tests/integration/__init__.py -->
## PYTHON MODULE: tests/integration/__init__.py

### MODULE DOCSTRING

Integration tests for the package.

<!--NI_PYTHON_API repo=nipanel-python path=tests/types.py -->
## PYTHON MODULE: tests/types.py

### MODULE DOCSTRING

Types that exercise conversion to and from protobuf.

### `class MyIntFlags(enum.IntFlag)`

Example of an IntFlag enum.

### `class MyIntableFlags(enum.Flag)`

Example of a simple flag with int values.

### `class MyIntEnum(enum.IntEnum)`

Example of an IntEnum enum.

### `class MixinIntEnum(int, enum.Enum)`

Example of an IntEnum using a mixin.

### `class MyStrEnum(StrEnum)`

Example of a StrEnum enum.

### `class MixinStrEnum(str, enum.Enum)`

Example of a StrEnum using a mixin.

### `class MyIntableEnum(enum.Enum)`

Example of a simple enum with int values.

### `class MyStringableEnum(StrEnum)`

Example of a simple enum with str values.

### `class MyMixedEnum(enum.Enum)`

Example of an enum with mixed values.

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/__init__.py -->
## PYTHON MODULE: tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests for the package.

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/test_convert.py -->
## PYTHON MODULE: tests/unit/test_convert.py

- `_BT_EPSILON = ht.timedelta(yoctoseconds=54210)`

### `def test___various_python_objects___get_best_matching_type___returns_correct_type_string(python_object: object, expected_type_string: str) -> None`

### `def test___python_builtin_scalar___to_any___valid_wrapperpb2_value(proto_type: type[_AnyWrappersPb2], default_value: Any, expected_value: Any) -> None`

### `def test___python_datetime_datetime___to_any___valid_timestamppb2_value() -> None`

### `def test___python_datetime_timedelta___to_any___valid_durationpb2_value() -> None`

### `def test___none_value___to_any___raises_type_error() -> None`

Test that passing None to to_any() raises a TypeError.

### `def test___wrapperpb2_value___from_any___valid_python_value(proto_type: type[_AnyWrappersPb2], expected_value: Any) -> None`

### `def test___timestamppb2_timestamp___from_any___valid_python_value() -> None`

### `def test___durationpb2_timestamp___from_any___valid_python_value() -> None`

### `def test___python_collection___to_any___valid_array_proto(proto_type: type[_AnyPanelPbTypes], default_value: Any, expected_value: Any) -> None`

### `def test___python_scalar_object___to_any___valid_scalar_proto() -> None`

### `def test___python_vector_object___to_any___valid_vector_proto() -> None`

### `def test___python_float64_analog_waveform___to_any___valid_double_analog_waveform_proto() -> None`

### `def test___python_int16_analog_waveform___to_any___valid_i16_analog_waveform_proto() -> None`

### `def test___python_float64_complex_waveform___to_any___valid_double_complex_waveform_proto() -> None`

### `def test___python_int16_complex_waveform___to_any___valid_i16_complex_waveform_proto() -> None`

### `def test___python_bool_digital_waveform___to_any___valid_digital_waveform_proto() -> None`

### `def test___python_uint8_digital_waveform___to_any___valid_digital_waveform_proto() -> None`

### `def test___python_float64_spectrum___to_any___valid_double_spectrum_proto() -> None`

### `def test___python_bintime_datetime__to_any___valid_precision_timestamp_proto() -> None`

### `def test___python_bintime_timedelta__to_any___valid_precision_duration_proto() -> None`

### `def test___python_hightime_datetime__to_any___valid_precision_timestamp_proto() -> None`

### `def test___python_hightime_timedelta__to_any___valid_precision_duration_proto() -> None`

### `def test___python_2dcollection_of_float___to_any___valid_double2darray(python_value: Collection[Collection[float]]) -> None`

### `def test___python_set_of_collection_of_float___to_any___valid_double2darray(python_value: Collection[Collection[float]]) -> None`

### `def test___array_proto___from_any___valid_python_collection(proto_type: type[_AnyPanelPbTypes], expected_value: Any) -> None`

### `def test___scalar_proto___from_any___valid_python_scalar() -> None`

### `def test___vector_proto___from_any___valid_python_vector() -> None`

### `def test___double_analog_waveform_proto___from_any___valid_python_float64_analog_waveform() -> None`

### `def test___i16_analog_waveform_proto___from_any___valid_python_int16_analog_waveform() -> None`

### `def test___double_complex_waveform_proto___from_any___valid_python_float64_complex_waveform() -> None`

### `def test___i16_complex_waveform_proto___from_any___valid_python_int16_complex_waveform() -> None`

### `def test___digital_waveform_proto___from_any___valid_python_bool_digital_waveform() -> None`

### `def test___digital_waveform_proto___from_any___valid_python_uint8_digital_waveform() -> None`

### `def test___double_spectrum_proto___from_any___valid_python_spectrum() -> None`

### `def test___precision_timestamp_proto__from_any___valid_hightime_datetime() -> None`

### `def test___precision_duration_proto__from_any___valid_hightime_timedelta() -> None`

### `def test___double2darray___from_any___valid_python_2dcollection() -> None`

### `def _assert_any_and_unpack(packed_message: any_pb2.Any, unpack_destination: Message) -> None`

### `def _pack_into_any(proto_value: Message) -> any_pb2.Any`

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/test_panel_client.py -->
## PYTHON MODULE: tests/unit/test_panel_client.py

### `def test___enumerate_is_empty(fake_panel_channel: grpc.Channel) -> None`

### `def test___start_panels___enumerate_has_panels(fake_panel_channel: grpc.Channel) -> None`

### `def test___start_panels___stop_panel_1_with_reset___enumerate_has_panel_2(fake_panel_channel: grpc.Channel) -> None`

### `def test___start_panels___stop_panel_1_without_reset___enumerate_has_both_panels(fake_panel_channel: grpc.Channel) -> None`

### `def test___get_unset_value___raises_exception(fake_panel_channel: grpc.Channel) -> None`

### `def test___try_get_unset_value___returns_none(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_value___enumerate_panels_shows_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_value___gets_value(fake_panel_channel: grpc.Channel) -> None`

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/test_panel_value_accessor.py -->
## PYTHON MODULE: tests/unit/test_panel_value_accessor.py

### `def test___no_previous_value___set_value_if_changed___sets_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_value_if_changed___set_same_value___does_not_set_value_again(fake_panel_channel: grpc.Channel, fake_python_panel_service: FakePythonPanelService) -> None`

### `def test___set_value_if_changed___set_different_value___sets_new_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_value_if_changed___different_value_ids___tracks_separately(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_value_if_changed_with_list_value___set_same_value___does_not_set_value_again(fake_panel_channel: grpc.Channel, fake_python_panel_service: FakePythonPanelService) -> None`

### `def test___set_value_if_changed_with_list_value___set_different_value___sets_new_value(fake_panel_channel: grpc.Channel, fake_python_panel_service: FakePythonPanelService) -> None`

### `def test___set_value_if_changed_with_enum_value___set_same_value___does_not_set_value_again(fake_panel_channel: grpc.Channel, fake_python_panel_service: FakePythonPanelService) -> None`

### `def test___set_value_if_changed_with_enum_value___set_different_value___sets_new_value(fake_panel_channel: grpc.Channel, fake_python_panel_service: FakePythonPanelService) -> None`

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/test_protobuf_type_conversion.py -->
## PYTHON MODULE: tests/unit/test_protobuf_type_conversion.py

### `def test___list_of_lists___convert___valid_double2darray(list_of_lists: list[list[float]], expected_data: list[float], expected_rows: int, expected_columns: int) -> None`

### `def test___list_of_lists_inconsistent_column_length___convert___throws_value_error() -> None`

### `def test___double2darray___convert___valid_list_of_lists(double2darray: array_pb2.Double2DArray, expected_data: list[list[float]]) -> None`

### `def test___double2darray_invalid_num_columns___convert___throws_value_error() -> None`

### `def test___double2darray_empty_data___convert___returns_empty_list() -> None`

### `def test___string_scalar_protobuf___convert___valid_str_scalar() -> None`

### `def test___str_scalar___convert___valid_string_scalar_protobuf() -> None`

### `def test___string_vector_protobuf___convert___valid_str_vector() -> None`

### `def test___str_vector___convert___valid_string_vector_protobuf() -> None`

### `def _units_to_attribute_map(units: str) -> Mapping[str, attribute_value_pb2.AttributeValue]`

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/test_python_panel_service_stub.py -->
## PYTHON MODULE: tests/unit/test_python_panel_service_stub.py

### `def test___start_panel___gets_response(python_panel_service_stub: PanelServiceStub) -> None`

### `def test___start_panel___stop_panel___gets_response(python_panel_service_stub: PanelServiceStub) -> None`

### `def test___enumerate_panels___gets_response(python_panel_service_stub: PanelServiceStub) -> None`

### `def test___set_value___gets_response(python_panel_service_stub: PanelServiceStub) -> None`

### `def test___set_value___get_value___gets_response(python_panel_service_stub: PanelServiceStub) -> None`

### `def test___no_value___get_value___raises_exception(python_panel_service_stub: PanelServiceStub) -> None`

### `def test___set_value___try_get_value___gets_response(python_panel_service_stub: PanelServiceStub) -> None`

### `def test___no_value___try_get_value___gets_no_value(python_panel_service_stub: PanelServiceStub) -> None`

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/test_streamlit_panel.py -->
## PYTHON MODULE: tests/unit/test_streamlit_panel.py

- `PATH_TO_SCRIPT = Path('path/to/script')`

### `def test___panel___has_panel_id_and_panel_script_path(fake_panel_channel: grpc.Channel) -> None`

### `def test___different_panels___have_different_panel_ids_and_panel_script_paths(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___set_value___gets_same_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___panel_set_value___accessor_gets_same_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___accessor_set_value___panel_gets_same_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___set_value___notifies(fake_python_panel_service: FakePythonPanelService, fake_panel_channel: grpc.Channel) -> None`

### `def test___accessor___set_value___does_not_notify(fake_python_panel_service: FakePythonPanelService, fake_panel_channel: grpc.Channel) -> None`

### `def test___first_start_will_fail___start_panel___panel_is_functional(fake_python_panel_service: FakePythonPanelService, fake_panel_channel: grpc.Channel) -> None`

Test that panel.start_panel() will automatically retry once.

### `def test___panel___set_value___sets_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___get_unset_value_with_no_default___raises_exception(fake_panel_channel: grpc.Channel) -> None`

Test that get_value() raises an exception for an unset value.

### `def test___panel___set_value___gets_value(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___set_value___get_value_ignores_default(fake_panel_channel: grpc.Channel) -> None`

### `def test___no_set_value___get_value_returns_default(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_string_type___get_value_with_string_default___returns_string_type(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_int_type___get_value_with_int_default___returns_int_type(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_bool_type___get_value_with_bool_default___returns_bool_type(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_string_type___get_value_with_int_default___raises_exception(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_int_type___get_value_with_bool_default___raises_exception(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_string_enum_type___get_value_with_int_enum_default___raises_exception(fake_panel_channel: grpc.Channel) -> None`

### `def test___builtin_scalar_type___set_value___gets_same_value(fake_panel_channel: grpc.Channel, value_payload: object) -> None`

Test that set_value() and get_value() work for builtin scalar types.

### `def test___enum_type___set_value___gets_same_value(fake_panel_channel: grpc.Channel, value_payload: enum.Enum) -> None`

Test that set_value() and get_value() work for enum types.

### `def test___unsupported_type___set_value___raises(fake_panel_channel: grpc.Channel, value_payload: object) -> None`

Test that set_value() raises for unsupported types.

### `def test___sequence_of_builtin_type___set_value___gets_same_value(fake_panel_channel: grpc.Channel, value_payload: object) -> None`

### `def test___set_int_enum_value___get_value___returns_int_enum(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_intable_enum_value___get_value___returns_intable_enum(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_string_enum_value___get_value___returns_string_enum(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_stringable_enum_value___get_value___returns_stringable_enum(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_mixed_enum_value___get_value___returns_mixed_enum(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_int_flags_value___get_value___returns_int_flags(fake_panel_channel: grpc.Channel) -> None`

### `def test___set_intable_flags_value___get_value___returns_intable_flags(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___panel_is_running_and_in_memory(fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___python_interpreter_url_is_in_venv(fake_python_panel_service: FakePythonPanelService, fake_panel_channel: grpc.Channel) -> None`

### `def test___panel___python_script_url_starts_with_file(fake_python_panel_service: FakePythonPanelService, fake_panel_channel: grpc.Channel) -> None`

### `def is_panel_in_memory(panel: StreamlitPanel) -> bool`

### `def is_panel_running(panel: StreamlitPanel) -> bool`

<!--NI_PYTHON_API repo=nipanel-python path=tests/unit/test_waveform_conversion.py -->
## PYTHON MODULE: tests/unit/test_waveform_conversion.py

- `EXPECTED_SAMPLE_INTERVAL = 0.1`

- `EXPECTED_T0_DT = dt.datetime(2000, 12, 1, tzinfo=dt.timezone.utc)`

- `EXPECTED_T0_BT = bt.DateTime(EXPECTED_T0_DT)`

- `EXPECTED_UNITS = 'Volts'`

- `EXPECTED_CHANNEL_NAME = 'Dev1/ch0'`

- `EXPECTED_ATTRIBUTES = {'NI_ChannelName': waveform_pb2.WaveformAttributeValue(string_value=EXPECTED_CHANNEL_NAME), 'NI_UnitDescription': waveform_pb2.WaveformAttributeValue(string_value=EXPECTED_UNITS)}`

### `def test___double_analog_waveform___convert___valid_protobuf() -> None`

### `def test___int16_analog_waveform___convert___valid_protobuf() -> None`

### `def test___double_analog_waveform___convert___valid_python_object() -> None`

### `def test___int16_analog_wfm___convert___valid_python_object() -> None`

### `def test___double_complex_waveform___convert___valid_protobuf() -> None`

### `def test___int16_complex_waveform___convert___valid_protobuf() -> None`

### `def test___double_complex_waveform___convert___valid_python_object() -> None`

### `def test___int16_complex_wfm___convert___valid_python_object() -> None`

### `def test___bool_digital_waveform___convert___valid_protobuf() -> None`

### `def test___uint8_digital_waveform___convert___valid_protobuf() -> None`

### `def test___bool_digital_waveform___convert___valid_python_object() -> None`

### `def test___uint8_digital_waveform___convert___valid_python_object() -> None`

### `def test___float64_spectrum___convert___valid_protobuf() -> None`

### `def test___double_spectrum___convert___valid_python_object() -> None`

### `def _get_t0_pt() -> precision_timestamp_pb2.PrecisionTimestamp`

### `def _set_python_attributes(waveform: Union[NumericWaveform[Any, Any], DigitalWaveform[Any], Spectrum[Any]]) -> None`

### `def _check_python_attributes(waveform: Union[NumericWaveform[Any, Any], DigitalWaveform[Any], Spectrum[Any]]) -> None`

### `def _check_protobuf_attributes(attributes: MutableMapping[str, waveform_pb2.WaveformAttributeValue], check_units: bool=True) -> None`

### `def _set_python_timing(waveform: Union[NumericWaveform[Any, Any], DigitalWaveform[Any]]) -> None`

### `def _check_python_timing(waveform: Union[NumericWaveform[Any, Any], DigitalWaveform[Any]]) -> None`

<!--NI_PYTHON_API repo=nipanel-python path=tests/utils/__init__.py -->
## PYTHON MODULE: tests/utils/__init__.py

### MODULE DOCSTRING

Test Utilities for the Panel.

<!--NI_PYTHON_API repo=nipanel-python path=tests/utils/_fake_python_panel_service.py -->
## PYTHON MODULE: tests/utils/_fake_python_panel_service.py

### `class FakePythonPanelService()`

Encapsulates a fake PythonPanelService with a gRPC server for testing.

#### `def __init__(self) -> None`

Initialize the fake PythonPanelService.

#### `def start(self, thread_pool: futures.ThreadPoolExecutor) -> None`

Start the gRPC server and return the port it is bound to.

#### `def stop(self) -> None`

Stop the gRPC server.

#### `def servicer(self) -> FakePythonPanelServicer`

Get the servicer instance.

#### `def port(self) -> int`

Get the port the server is bound to.

<!--NI_PYTHON_API repo=nipanel-python path=tests/utils/_fake_python_panel_servicer.py -->
## PYTHON MODULE: tests/utils/_fake_python_panel_servicer.py

### `class FakePythonPanelServicer(PanelServiceServicer)`

Fake implementation of the PanelServiceServicer for testing.

#### `def __init__(self) -> None`

Initialize the fake PythonPanelServicer.

#### `def StartPanel(self, request: StartPanelRequest, context: Any) -> StartPanelResponse`

Trivial implementation for testing.

#### `def StopPanel(self, request: StopPanelRequest, context: Any) -> StopPanelResponse`

Trivial implementation for testing.

#### `def EnumeratePanels(self, request: EnumeratePanelsRequest, context: Any) -> EnumeratePanelsResponse`

Trivial implementation for testing.

#### `def GetValue(self, request: GetValueRequest, context: Any) -> GetValueResponse`

Trivial implementation for testing.

#### `def TryGetValue(self, request: TryGetValueRequest, context: Any) -> TryGetValueResponse`

Trivial implementation for testing.

#### `def SetValue(self, request: SetValueRequest, context: Any) -> SetValueResponse`

Trivial implementation for testing.

#### `def fail_next_start_panel(self) -> None`

Set whether the StartPanel method should fail the next time it is called.

#### `def set_count(self) -> int`

Get the total number of times SetValue was called.

#### `def notification_count(self) -> int`

Get the number of notifications sent from SetValue.

#### `def python_interpreter_url(self) -> str`

Get the Python interpreter url.

#### `def python_script_url(self) -> str`

Get the Python script url.

#### `def _init_panel(self, panel_id: str) -> None`

#### `def _start_panel(self, panel_id: str) -> None`

#### `def _stop_panel(self, reset: bool, panel_id: str) -> None`

#### `def _get_panel_uri(self, panel_id: str) -> str`
