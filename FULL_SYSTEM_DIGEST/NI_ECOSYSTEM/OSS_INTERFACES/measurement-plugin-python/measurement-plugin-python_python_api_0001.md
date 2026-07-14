# NI PYTHON API DIGEST: measurement-plugin-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/measurement-plugin-python commit=2e57ec3e5bd703abc8690f8a46df62b28f0380e2 -->

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/game_of_life/_helpers.py -->
## PYTHON MODULE: examples/game_of_life/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/game_of_life/measurement.py -->
## PYTHON MODULE: examples/game_of_life/measurement.py

### MODULE DOCSTRING

Source the XY data for Conway's Game of Life.

- `INFINITE_GENERATIONS = -1`

### `def measure(width: int, height: int, update_interval_msec: int, max_generations: int) -> Generator[tuple[xydata_pb2.DoubleXYData, int], None, None]`

Streaming measurement that returns Conway's Game of Life grid as DoubleXYData.

### `def _initialize_xydata_and_frame(width: int, height: int) -> xydata_pb2.DoubleXYData`

### `def _initialize_grid_with_seeded_data(rows: int, cols: int, probability: float=0.6) -> Grid`

### `def _initialize_grid(rows: int, cols: int) -> Grid`

### `def _count_neighbors(grid: Grid, row: int, col: int) -> int`

### `def _update_grid(grid: Grid) -> Grid`

### `def main(verbosity: int, **kwargs: Any) -> None`

Source the XY data for Conway's Game of Life.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidaqmx_analog_input/_helpers.py -->
## PYTHON MODULE: examples/nidaqmx_analog_input/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidaqmx_analog_input/measurement.py -->
## PYTHON MODULE: examples/nidaqmx_analog_input/measurement.py

### MODULE DOCSTRING

Perform a finite analog input measurement with NI-DAQmx.

### `def measure(pin_name: str, sample_rate: float, number_of_samples: int) -> tuple[list[float]]`

Perform a finite analog input measurement with NI-DAQmx.

### `def _log_measured_values(samples: list[float], max_samples_to_display: int=5) -> None`

Log the measured values.

### `def main(verbosity: int) -> None`

Perform a finite analog input measurement with NI-DAQmx.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidaqmx_analog_input/teststand_nidaqmx.py -->
## PYTHON MODULE: examples/nidaqmx_analog_input/teststand_nidaqmx.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-DAQmx devices in NI TestStand.

### `def create_nidaqmx_tasks(sequence_context: Any) -> None`

Create and register all NI-DAQmx tasks.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nidaqmx_tasks() -> None`

Destroy and unregister all NI-DAQmx tasks.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/_helpers.py -->
## PYTHON MODULE: examples/nidcpower_source_dc_voltage/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/measurement.py -->
## PYTHON MODULE: examples/nidcpower_source_dc_voltage/measurement.py

### MODULE DOCSTRING

Source and measure a DC voltage with an NI SMU.

- `_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE = -1074116059`

- `_NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE = -1074097933`

- `_NIDCPOWER_TIMEOUT_ERROR_CODES = [_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE, _NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE]`

### `def measure(pin_names: Iterable[str], voltage_level: float, voltage_level_range: float, current_limit: float, current_limit_range: float, source_delay: float) -> tuple[list[int], list[str], list[float], list[float], list[bool]]`

Source and measure a DC voltage with an NI SMU.

### `def _wait_for_event(channels: nidcpower.session._SessionBase, cancellation_event: threading.Event, event_id: nidcpower.enums.Event, timeout: float) -> None`

Wait for a NI-DCPower event or until error/cancellation occurs.

### `def _log_measurements(measured_sites: Iterable[int], measured_pins: Iterable[str], measured_values: Iterable[_Measurement]) -> None`

Log the measured values.

### `def main(verbosity: int) -> None`

Source and measure a DC voltage with an NI SMU.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage/teststand_nidcpower.py -->
## PYTHON MODULE: examples/nidcpower_source_dc_voltage/teststand_nidcpower.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-DCPower devices in NI TestStand.

### `def create_nidcpower_sessions(sequence_context: Any) -> None`

Create and register all NI-DCPower sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nidcpower_sessions() -> None`

Destroy and unregister all NI-DCPower sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/_helpers.py -->
## PYTHON MODULE: examples/nidcpower_source_dc_voltage_with_multiplexer/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/measurement.py -->
## PYTHON MODULE: examples/nidcpower_source_dc_voltage_with_multiplexer/measurement.py

### MODULE DOCSTRING

Source and measure a DC voltage with an NI SMU via an NI-SWITCH multiplexer.

- `_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE = -1074116059`

- `_NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE = -1074097933`

- `_NIDCPOWER_TIMEOUT_ERROR_CODES = [_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE, _NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE]`

### `def measure(pin_name: str, voltage_level: float, voltage_level_range: float, current_limit: float, current_limit_range: float, source_delay: float) -> tuple[float, float]`

Source and measure a DC voltage with an NI SMU connected via an NI-SWITCH multiplexer.

### `def _wait_for_nidcpower_event(channels: nidcpower.session._SessionBase, cancellation_event: threading.Event, event_id: nidcpower.enums.Event, timeout: float) -> None`

Wait for a NI-DCPower event or until error/cancellation occurs.

### `def main(verbosity: int) -> None`

Source and measure a DC voltage with an NI SMU connected via an NI-SWITCH multiplexer.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_nidcpower.py -->
## PYTHON MODULE: examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_nidcpower.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-DCPower devices in NI TestStand.

### `def create_nidcpower_sessions(sequence_context: Any) -> None`

Create and register all NI-DCPower sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nidcpower_sessions() -> None`

Destroy and unregister all NI-DCPower sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_niswitch.py -->
## PYTHON MODULE: examples/nidcpower_source_dc_voltage_with_multiplexer/teststand_niswitch.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-Switch devices in NI TestStand.

### `def create_niswitch_sessions(sequence_context: Any) -> None`

Create and register all NI-Switch sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_niswitch_sessions() -> None`

Destroy and unregister all NI-Switch sessions.

### `def create_niswitch_multiplexer_sessions(sequence_context: Any) -> None`

Create and register all NI-SWITCH multiplexer sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_niswitch_multiplexer_sessions() -> None`

Destroy and unregister all NI-SWITCH multiplexer sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidigital_spi/_helpers.py -->
## PYTHON MODULE: examples/nidigital_spi/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidigital_spi/measurement.py -->
## PYTHON MODULE: examples/nidigital_spi/measurement.py

### MODULE DOCSTRING

Test a SPI device using an NI Digital Pattern instrument.

### `def measure(pin_names: Iterable[str], specifications_file_path: str, levels_file_path: str, timing_file_path: str, pattern_file_path: str, load_files: bool) -> tuple`

Test a SPI device using an NI Digital Pattern instrument.

### `def _resolve_relative_path(directory_path: pathlib.Path, file_path: str | pathlib.Path) -> pathlib.Path`

### `def main(verbosity: int) -> None`

Test a SPI device using an NI Digital Pattern instrument.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidigital_spi/teststand_nidigital.py -->
## PYTHON MODULE: examples/nidigital_spi/teststand_nidigital.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI Digital Pattern instruments in NI TestStand.

### `def create_nidigital_sessions(sequence_context: Any) -> None`

Create and register all NI-Digital sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def load_nidigital_pin_map(pin_map_path: str, sequence_context: Any) -> None`

Load the pin map into the registered NI-Digital sessions.

    Args:
        pin_map_path: An absolute or relative path to the pin map file.
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def load_nidigital_specifications_levels_and_timing(specifications_file_paths: Iterable[str], levels_file_paths: Iterable[str], timing_file_paths: Iterable[str], sequence_context: Any) -> None`

Load specifications, levels, and timing files into NI-Digital sessions.

    Args:
        specifications_file_paths: Absolute or relative paths to the specifications files.
        levels_file_paths: Absolute or relative paths to the levels files.
        timing_file_paths: Absolute or relative paths to the timing files.
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def load_nidigital_patterns(pattern_file_paths: Iterable[str], sequence_context: Any) -> None`

Load specifications, levels, and timing files into NI-Digital sessions.

    Args:
        pattern_file_paths: Absolute or relative paths to the pattern files.
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nidigital_sessions() -> None`

Destroy and unregister all NI-Digital sessions.

### `def _reserve_sessions(session_management_client: SessionManagementClient, pin_map_id: str, instrument_type_id: str) -> MultiSessionReservation`

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidmm_measurement/_helpers.py -->
## PYTHON MODULE: examples/nidmm_measurement/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidmm_measurement/measurement.py -->
## PYTHON MODULE: examples/nidmm_measurement/measurement.py

### MODULE DOCSTRING

Perform a measurement using an NI DMM.

### `class Function(Enum)`

Wrapper enum that contains a zero value.

### `def measure(pin_name: str, measurement_type: Function, range: float, resolution_digits: float) -> tuple[float, bool, float]`

Perform a measurement using an NI DMM.

### `def main(verbosity: int) -> None`

Perform a measurement using an NI DMM.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nidmm_measurement/teststand_nidmm.py -->
## PYTHON MODULE: examples/nidmm_measurement/teststand_nidmm.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-DMM devices in NI TestStand.

### `def create_nidmm_sessions(sequence_context: Any) -> None`

Create and register all NI-DMM sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nidmm_sessions() -> None`

Destroy and unregister all NI-DMM sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nifgen_standard_function/_helpers.py -->
## PYTHON MODULE: examples/nifgen_standard_function/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nifgen_standard_function/measurement.py -->
## PYTHON MODULE: examples/nifgen_standard_function/measurement.py

### MODULE DOCSTRING

Generate a standard function waveform using an NI waveform generator.

- `_NIFGEN_OPERATION_TIMED_OUT_ERROR_CODE = -1074098044`

- `_NIFGEN_MAX_TIME_EXCEEDED_ERROR_CODE = -1074118637`

- `_NIFGEN_TIMEOUT_ERROR_CODES = [_NIFGEN_OPERATION_TIMED_OUT_ERROR_CODE, _NIFGEN_MAX_TIME_EXCEEDED_ERROR_CODE]`

### `class Waveform(Enum)`

Wrapper enum that contains a zero value.

### `def measure(pin_names: Iterable[str], waveform_type: Waveform, frequency: float, amplitude: float, duration: float) -> tuple[()]`

Generate a standard function waveform using an NI waveform generator.

### `def _wait_until_done(sessions: Sequence[nifgen.Session], cancellation_event: threading.Event, duration: float) -> None`

Wait until all sessions are done, the duration expires, or error/cancellation occurs.

    Note that ``duration`` is a minimum time, not a timeout.
    

### `def main(verbosity: int) -> None`

Generate a standard function waveform using an NI waveform generator.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nifgen_standard_function/teststand_nifgen.py -->
## PYTHON MODULE: examples/nifgen_standard_function/teststand_nifgen.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-FGEN devices in NI TestStand.

### `def create_nifgen_sessions(sequence_context: Any) -> None`

Create and register all NI-FGEN sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nifgen_sessions() -> None`

Destroy and unregister all NI-FGEN sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/niscope_acquire_waveform/_helpers.py -->
## PYTHON MODULE: examples/niscope_acquire_waveform/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/niscope_acquire_waveform/measurement.py -->
## PYTHON MODULE: examples/niscope_acquire_waveform/measurement.py

### MODULE DOCSTRING

Acquire a waveform using an NI oscilloscope.

### `def measure(measurement_pins: Sequence[str], vertical_range: float, vertical_coupling: str, input_impedance: float, min_sample_rate: float, min_record_length: int, trigger_pin: str, trigger_level: float, trigger_slope: str, auto_trigger: bool, trigger_coupling: str, timeout: float) -> tuple[list[float], ...]`

Acquire a waveform using an NI oscilloscope.

### `def _wait_until_done(session: niscope.Session, cancellation_event: threading.Event, timeout: float) -> None`

Wait until the acquisition is done or error/cancellation occurs.

### `def main(verbosity: int) -> None`

Acquire a waveform using an NI oscilloscope.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/niscope_acquire_waveform/teststand_niscope.py -->
## PYTHON MODULE: examples/niscope_acquire_waveform/teststand_niscope.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-Scope devices in NI TestStand.

### `def create_niscope_sessions(sequence_context: Any) -> None`

Create and register all NI-Scope sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_niscope_sessions() -> None`

Destroy and unregister all NI-Scope sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/niswitch_control_relays/_helpers.py -->
## PYTHON MODULE: examples/niswitch_control_relays/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/niswitch_control_relays/measurement.py -->
## PYTHON MODULE: examples/niswitch_control_relays/measurement.py

### MODULE DOCSTRING

Control relays using an NI relay driver (e.g. PXI-2567).

### `def measure(relay_names: str, close_relays: bool) -> tuple[()]`

Control relays using an NI relay driver (e.g. PXI-2567).

### `def main(verbosity: int) -> None`

Control relays using an NI relay driver (e.g. PXI-2567).

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/niswitch_control_relays/teststand_niswitch.py -->
## PYTHON MODULE: examples/niswitch_control_relays/teststand_niswitch.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-Switch devices in NI TestStand.

### `def create_niswitch_sessions(sequence_context: Any) -> None`

Create and register all NI-Switch sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_niswitch_sessions() -> None`

Destroy and unregister all NI-Switch sessions.

### `def create_niswitch_multiplexer_sessions(sequence_context: Any) -> None`

Create and register all NI-SWITCH multiplexer sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_niswitch_multiplexer_sessions() -> None`

Destroy and unregister all NI-SWITCH multiplexer sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_helpers.py -->
## PYTHON MODULE: examples/nivisa_dmm_measurement/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_visa_dmm.py -->
## PYTHON MODULE: examples/nivisa_dmm_measurement/_visa_dmm.py

### MODULE DOCSTRING

Custom instrument driver for measurement plug-in NI-VISA DMM examples.

- `INSTRUMENT_TYPE_VISA_DMM = 'VisaDmm'`

- `_SIMULATION_YAML_PATH = pathlib.Path(__file__).resolve().parent / '_visa_dmm_sim.yaml'`

- `_RESOLUTION_DIGITS_TO_VALUE = {'3.5': 0.001, '4.5': 0.0001, '5.5': 1e-05, '6.5': 1e-06}`

- `_SUPPORTED_INSTRUMENT_IDS = ['34401', '34410', '34411', 'L4411', 'Instrument Simulator', 'Waveform Generator Simulator']`

### `class Function(Enum)`

Enum that represents the measurement function.

- `_FUNCTION_TO_VALUE = {Function.DC_VOLTS: 'VOLT:DC', Function.AC_VOLTS: 'VOLT:AC'}`

### `class Session()`

An NI-VISA DMM session.

#### `def __init__(self, resource_name: str, id_query: bool=True, reset_device: bool=True, simulate: bool=False) -> None`

Open NI-VISA DMM session.

#### `def close(self) -> None`

Close the session.

#### `def __enter__(self) -> Self`

Context management protocol. Returns self.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Context management protocol. Calls close().

#### `def configure_measurement_digits(self, function: Function, range: float, resolution_digits: float) -> None`

Configure the common properties of the measurement.

        These properties include function, range, and resolution_digits.
        

#### `def read(self) -> float`

Acquires a single measurement and returns the measured value.

#### `def _check_error(self) -> None`

Query the instrument's error queue.

#### `def _validate_id(self) -> None`

Check the selected instrument is proper and responding..

#### `def _reset(self) -> None`

Reset the instrument to a known state.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_visa_dmm_session_management.py -->
## PYTHON MODULE: examples/nivisa_dmm_measurement/_visa_dmm_session_management.py

### `class VisaDmmSessionConstructor()`

Measurement plug-in constructor for VISA DMM sessions.

#### `def __init__(self, config: AutoConfig, discovery_client: DiscoveryClient, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> None`

Construct a VisaDmmSessionConstructor.

#### `def __call__(self, session_info: SessionInformation) -> Session`

Construct a VISA DMM session based on measurement plug-in info.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/_visa_grpc.py -->
## PYTHON MODULE: examples/nivisa_dmm_measurement/_visa_grpc.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: 0, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: 1, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: 2, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: 3, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: 4}`

- `GRPC_SERVICE_INTERFACE_NAME = 'visa_grpc.Visa'`

- `SERVICE_CLASS = 'ni.measurementlink.v1.grpcdeviceserver'`

### `def build_visa_grpc_resource_string(resource_name: str, address: str, session_name: str='', initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> str`

Build an grpc:// resource string for remoting with NI-VISA.

### `def get_visa_grpc_insecure_address(config: AutoConfig, discovery_client: DiscoveryClient) -> str`

Get the insecure address of NI gRPC Device Server's VISA interface in host:port format.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/measurement.py -->
## PYTHON MODULE: examples/nivisa_dmm_measurement/measurement.py

### MODULE DOCSTRING

Perform a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0.

### `def measure(pin_name: str, measurement_type: Function, range: float, resolution_digits: float) -> tuple[float]`

Perform a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0.

### `def main(verbosity: int) -> None`

Perform a DMM measurement using NI-VISA and an NI Instrument Simulator v2.0.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/nivisa_dmm_measurement/teststand_nivisa_dmm.py -->
## PYTHON MODULE: examples/nivisa_dmm_measurement/teststand_nivisa_dmm.py

### MODULE DOCSTRING

Functions to set up and tear down NI-VISA DMM sessions in NI TestStand.

- `_VISA_DMM_SIMULATE = _config('MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE', default=False, cast=bool)`

### `def create_nivisa_dmm_sessions(sequence_context: Any) -> None`

Create and register all NI-VISA DMM sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nivisa_dmm_sessions() -> None`

Destroy and unregister all NI-VISA DMM sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/output_voltage_measurement/_helpers.py -->
## PYTHON MODULE: examples/output_voltage_measurement/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/output_voltage_measurement/_visa_dmm.py -->
## PYTHON MODULE: examples/output_voltage_measurement/_visa_dmm.py

### MODULE DOCSTRING

Custom instrument driver for measurement plug-in NI-VISA DMM examples.

- `INSTRUMENT_TYPE_VISA_DMM = 'VisaDmm'`

- `_SIMULATION_YAML_PATH = pathlib.Path(__file__).resolve().parent / '_visa_dmm_sim.yaml'`

- `_RESOLUTION_DIGITS_TO_VALUE = {'3.5': 0.001, '4.5': 0.0001, '5.5': 1e-05, '6.5': 1e-06}`

- `_SUPPORTED_INSTRUMENT_IDS = ['34401', '34410', '34411', 'L4411', 'Instrument Simulator', 'Waveform Generator Simulator']`

### `class Function(Enum)`

Enum that represents the measurement function.

- `_FUNCTION_TO_VALUE = {Function.DC_VOLTS: 'VOLT:DC', Function.AC_VOLTS: 'VOLT:AC'}`

### `class Session()`

An NI-VISA DMM session.

#### `def __init__(self, resource_name: str, id_query: bool=True, reset_device: bool=True, simulate: bool=False) -> None`

Open NI-VISA DMM session.

#### `def close(self) -> None`

Close the session.

#### `def __enter__(self) -> Self`

Context management protocol. Returns self.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Context management protocol. Calls close().

#### `def configure_measurement_digits(self, function: Function, range: float, resolution_digits: float) -> None`

Configure the common properties of the measurement.

        These properties include function, range, and resolution_digits.
        

#### `def read(self) -> float`

Acquires a single measurement and returns the measured value.

#### `def _check_error(self) -> None`

Query the instrument's error queue.

#### `def _validate_id(self) -> None`

Check the selected instrument is proper and responding..

#### `def _reset(self) -> None`

Reset the instrument to a known state.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/output_voltage_measurement/_visa_dmm_session_management.py -->
## PYTHON MODULE: examples/output_voltage_measurement/_visa_dmm_session_management.py

### `class VisaDmmSessionConstructor()`

Measurement plug-in session constructor for VISA DMM sessions.

#### `def __init__(self, config: AutoConfig, discovery_client: DiscoveryClient, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> None`

Construct a VisaDmmSessionConstructor.

#### `def __call__(self, session_info: SessionInformation) -> Session`

Construct a VISA DMM session based on measurement plug-in session info.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/output_voltage_measurement/_visa_grpc.py -->
## PYTHON MODULE: examples/output_voltage_measurement/_visa_grpc.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: 0, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: 1, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: 2, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: 3, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: 4}`

- `GRPC_SERVICE_INTERFACE_NAME = 'visa_grpc.Visa'`

- `SERVICE_CLASS = 'ni.measurementlink.v1.grpcdeviceserver'`

### `def build_visa_grpc_resource_string(resource_name: str, address: str, session_name: str='', initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> str`

Build an grpc:// resource string for remoting with NI-VISA.

### `def get_visa_grpc_insecure_address(config: AutoConfig, discovery_client: DiscoveryClient) -> str`

Get the insecure address of NI gRPC Device Server's VISA interface in host:port format.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/output_voltage_measurement/measurement.py -->
## PYTHON MODULE: examples/output_voltage_measurement/measurement.py

### MODULE DOCSTRING

Source DC voltage as input with an NI SMU and measure output using NI-VISA DMM.

- `_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE = -1074116059`

- `_NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE = -1074097933`

- `_NIDCPOWER_TIMEOUT_ERROR_CODES = [_NIDCPOWER_WAIT_FOR_EVENT_TIMEOUT_ERROR_CODE, _NIDCPOWER_TIMEOUT_EXCEEDED_ERROR_CODE]`

### `def measure(voltage_level: float, voltage_level_range: float, current_limit: float, current_limit_range: float, source_delay: float, input_pin: str, measurement_type: _visa_dmm.Function, range: float, resolution_digits: float, output_pin: str) -> tuple[float]`

Source DC voltage as input with an NI SMU and measure output using NI-VISA DMM.

### `def _wait_for_nidcpower_event(channels: nidcpower.session._SessionBase, cancellation_event: threading.Event, event_id: nidcpower.enums.Event, timeout: float) -> None`

Wait for a NI-DCPower event or until error/cancellation occurs.

### `def main(verbosity: int) -> None`

Source DC voltage as input with an NI SMU and measure output using NI-VISA DMM.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/output_voltage_measurement/teststand_nidcpower.py -->
## PYTHON MODULE: examples/output_voltage_measurement/teststand_nidcpower.py

### MODULE DOCSTRING

Functions to set up and tear down sessions of NI-DCPower devices in NI TestStand.

### `def create_nidcpower_sessions(sequence_context: Any) -> None`

Create and register all NI-DCPower sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nidcpower_sessions() -> None`

Destroy and unregister all NI-DCPower sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/output_voltage_measurement/teststand_nivisa_dmm.py -->
## PYTHON MODULE: examples/output_voltage_measurement/teststand_nivisa_dmm.py

### MODULE DOCSTRING

Functions to set up and tear down NI-VISA DMM sessions in NI TestStand.

- `_VISA_DMM_SIMULATE = _config('MEASUREMENT_PLUGIN_VISA_DMM_SIMULATE', default=False, cast=bool)`

### `def create_nivisa_dmm_sessions(sequence_context: Any) -> None`

Create and register all NI-VISA DMM sessions.

    Args:
        sequence_context: The SequenceContext COM object from the TestStand sequence execution.
            (Dynamically typed.)
    

### `def destroy_nivisa_dmm_sessions() -> None`

Destroy and unregister all NI-VISA DMM sessions.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/sample_measurement/_array_utils.py -->
## PYTHON MODULE: examples/sample_measurement/_array_utils.py

### MODULE DOCSTRING

2DArray Conversion Utilities.

### `def double2darray_to_ndarray(double2darray: array_pb2.Double2DArray) -> npt.NDArray[np.float64]`

Convert Double2DArray to numpy NDArray.

### `def ndarray_to_double2darray(ndarray: npt.NDArray[np.float64]) -> array_pb2.Double2DArray`

Convert numpy NDArray to Double2DArray.

### `def list_to_double2darray(data: list[list[float]]) -> array_pb2.Double2DArray`

Convert list of lists to Double2DArray.

### `def double2darray_to_list(double2darray: array_pb2.Double2DArray) -> list[list[float]]`

Convert Double2DArray to list of lists.

### `def string2darray_to_ndarray(string2darray: array_pb2.String2DArray) -> npt.NDArray[np.str_]`

Convert String2DArray to numpy NDArray.

### `def ndarray_to_string2darray(ndarray: npt.NDArray[np.str_]) -> array_pb2.String2DArray`

Convert numpy NDArray to String2DArray.

### `def string2darray_to_list(string2darray: array_pb2.String2DArray) -> list[list[str]]`

Convert String2DArray to list of lists.

### `def list_to_string2darray(data: list[list[str]]) -> array_pb2.String2DArray`

Convert list of lists to String2DArray.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/sample_measurement/_helpers.py -->
## PYTHON MODULE: examples/sample_measurement/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/sample_measurement/_stubs/__init__.py -->
## PYTHON MODULE: examples/sample_measurement/_stubs/__init__.py

### MODULE DOCSTRING

Stubs for sample_measurement's color enum.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/sample_measurement/_stubs/color_pb2.py -->
## PYTHON MODULE: examples/sample_measurement/_stubs/color_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bcolor.proto\x12\x0bni.examples*9\n\rProtobufColor\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05BLACK\x10\x03B7\xaa\x024NationalInstruments.MeasurementServices.Measurementsb\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/sample_measurement/_stubs/color_pb2_grpc.py -->
## PYTHON MODULE: examples/sample_measurement/_stubs/color_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=examples/sample_measurement/measurement.py -->
## PYTHON MODULE: examples/sample_measurement/measurement.py

### MODULE DOCSTRING

Perform a loopback measurement with various data types.

### `class Color(Enum)`

Primary colors used for example enum-typed config and output.

### `def measure(float_input: float, double_array_input: Iterable[float], bool_input: bool, string_input: str, enum_input: Color, protobuf_enum_input: color_pb2.ProtobufColor.ValueType, string_array_in: Iterable[str]) -> tuple[float, Iterable[float], bool, str, Color, color_pb2.ProtobufColor.ValueType, Iterable[str], array_pb2.Double2DArray, array_pb2.Double2DArray, array_pb2.String2DArray, array_pb2.String2DArray]`

Perform a loopback measurement with various data types.

### `def main(verbosity: int) -> None`

Perform a loopback measurement with various data types.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/__init__.py -->
## PYTHON MODULE: packages/generator/ni_measurement_plugin_sdk_generator/__init__.py

### MODULE DOCSTRING

Measurement Plug-In SDK Code Generator.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/client/__init__.py -->
## PYTHON MODULE: packages/generator/ni_measurement_plugin_sdk_generator/client/__init__.py

### MODULE DOCSTRING

Utilizes command line args to create a Measurement Plug-In Client using template files.

- `_CLIENT_CREATION_ERROR_MESSAGE = "Client creation failed for '{}'. Possible reason(s): {}"`

### `def _render_template(template_name: str, **template_args: Any) -> bytes`

### `def _create_file(template_name: str, file_name: str, directory_out: pathlib.Path, **template_args: Any) -> None`

### `def _create_client(discovery_client: DiscoveryClient, channel_pool: GrpcChannelPool, measurement_service_class: str, module_name: str, class_name: str, directory_out: pathlib.Path, generated_modules: list[str]) -> None`

### `def _create_all_clients(directory_out: str | None) -> None`

### `def _create_clients_interactively() -> None`

### `def _create_clients(measurement_service_classes: list[str], module_name: str | None, class_name: str | None, directory_out: str | None) -> None`

### `def create_client(measurement_service_class: list[str], all: bool, interactive: bool, module_name: str | None, class_name: str | None, directory_out: str | None, verbose: int) -> None`

Generates a Python Measurement Plug-In Client module for the measurement service.

    You can use the generated module to interact with the corresponding measurement service.
    

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/client/__main__.py -->
## PYTHON MODULE: packages/generator/ni_measurement_plugin_sdk_generator/client/__main__.py

### MODULE DOCSTRING

Creates a measurement client through use of __init__.py.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/client/_support.py -->
## PYTHON MODULE: packages/generator/ni_measurement_plugin_sdk_generator/client/_support.py

### MODULE DOCSTRING

Support functions for the Measurement Plug-In Client generator.

- `_V2_MEASUREMENT_SERVICE_INTERFACE = 'ni.measurementlink.measurement.v2.MeasurementService'`

- `_INVALID_CHARS = "`~!@#$%^&*()-+={}[]\\|:;',<>.?/ \n"`

- `_XY_DATA_IMPORT = 'from ni.protobuf.types.xydata_pb2 import DoubleXYData'`

- `_DOUBLE2DARRAY_DATA_IMPORT = 'from ni.protobuf.types.array_pb2 import Double2DArray'`

- `_STRING2DARRAY_DATA_IMPORT = 'from ni.protobuf.types.array_pb2 import String2DArray'`

- `_PATH_IMPORT = 'import pathlib'`

- `_PROTO_DATATYPE_TO_PYTYPE_LOOKUP = {Field.TYPE_INT32: int, Field.TYPE_INT64: int, Field.TYPE_UINT32: int, Field.TYPE_UINT64: int, Field.TYPE_SINT32: int, Field.TYPE_SINT64: int, Field.TYPE_FIXED32: int, Field.TYPE_FIXED64: int, Field.TYPE_SFIXED32: int, Field.TYPE_SFIXED64: int, Field.TYPE_FLOAT: float, Field.TYPE_DOUBLE: float, Field.TYPE_BOOL: bool, Field.TYPE_STRING: str, Field.TYPE_ENUM: int, Field.TYPE_MESSAGE: str}`

- `_T = TypeVar('_T')`

- `_CAMEL_TO_SNAKE_CASE_REGEXES = [re.compile('([^_\n])([A-Z][a-z]+)'), re.compile('([a-z])([A-Z])'), re.compile('([0-9])([^_0-9])'), re.compile('([^_0-9])([0-9])')]`

### `def get_measurement_service_stub_and_version(discovery_client: DiscoveryClient, channel_pool: GrpcChannelPool, service_class: str) -> tuple[v2_measurement_service_pb2_grpc.MeasurementServiceStub, str]`

Returns the measurement service stub and version of the given service class.

### `def get_all_registered_measurement_info(discovery_client: DiscoveryClient) -> tuple[list[str], list[str]]`

Returns the service classes and display names of all the registered measurement services.

### `def get_configuration_and_output_metadata_by_index(metadata: v2_measurement_service_pb2.GetMetadataResponse, service_class: str, enum_values_by_type: dict[type[Enum], dict[str, int]]={}) -> tuple[dict[int, ParameterMetadata], dict[int, ParameterMetadata]]`

Returns the configuration and output metadata of the measurement.

### `def get_configuration_parameters_with_type_and_default_values(configuration_metadata: dict[int, ParameterMetadata], built_in_import_modules: list[str], enum_values_by_type: dict[type[Enum], dict[str, int]]={}) -> tuple[str, str]`

Returns configuration parameters of the measurement with type and default values.

### `def get_output_parameters_with_type(output_metadata: dict[int, ParameterMetadata], built_in_import_modules: list[str], custom_import_modules: list[str], enum_values_by_type: dict[type[Enum], dict[str, int]]={}) -> list[str]`

Returns the output parameters of the measurement with type.

### `def to_ordered_set(values: Iterable[_T]) -> AbstractSet[_T]`

Converts an iterable to an ordered set.

### `def resolve_output_directory(directory_out: str | None=None) -> pathlib.Path`

Returns the validated directory output path.

### `def validate_identifier(name: str, name_type: str) -> None`

Validates whether the given string is a valid Python identifier.

### `def extract_base_service_class(service_class: str) -> str`

Creates a base service class from the measurement service class.

### `def create_module_name(base_service_class: str, generated_modules: list[str]) -> str`

Creates a unique module name using the base service class.

### `def create_class_name(base_service_class: str) -> str`

Creates a class name using base service class.

### `def get_selected_measurement_service_class(selection: int, measurement_service_classes: list[str]) -> str`

Returns the selected measurement service class.

### `def validate_measurement_service_classes(measurement_service_classes: list[str]) -> None`

Validates whether the given measurement service classes list is empty.

### `def _get_python_identifier(input_string: str) -> str`

### `def _get_configuration_python_type_as_str(type: Field.Kind.ValueType, is_array: bool) -> str`

### `def _get_output_python_type_as_str(type: Field.Kind.ValueType, is_array: bool) -> str`

### `def _camel_to_snake_case(camel_case_string: str) -> str`

### `def _remove_suffix(string: str) -> str`

### `def _is_python_identifier(input_string: str | None) -> bool`

### `def _is_enum_param(parameter_type: int) -> bool`

### `def _get_enum_type(parameter_name: str, enum_annotations: str, enum_values_by_type: dict[type[Enum], dict[str, int]]) -> type[Enum]`

### `def _get_enum_class_name(name: str) -> str`

### `def _validate_and_transform_enum_annotations(enum_annotations: str) -> str`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/__init__.py -->
## PYTHON MODULE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/__init__.py

### MODULE DOCSTRING

Utilizes command line args to create a measurement using template files.

### `def _render_template(template_name: str, **template_args: Any) -> bytes`

### `def _create_file(template_name: str, file_name: str, directory_out: pathlib.Path, **template_args: Any) -> None`

### `def _check_version(ctx: click.Context, param: click.Parameter, version: str) -> str`

### `def _check_ui_file(ctx: click.Context, param: click.Parameter, ui_file: str | None) -> str | None`

### `def _get_ui_type(ui_file: str) -> str`

### `def _resolve_ui_file(ui_file: str | None, display_name_for_filenames: str) -> str`

### `def _resolve_service_class(service_class: str, display_name: str) -> str`

### `def create_measurement(display_name: str, measurement_version: str, ui_file: str | None, service_class: str, description_url: str, directory_out: str | None, description: str, collection: str, tags: tuple[str, ...], verbose: int) -> None`

Generate a Python measurement service from a template.

    You can use this to get started writing your own measurement plug-ins.

    DISPLAY_NAME: The measurement display name for client to display to user.
    The created .serviceconfig file will take this as its file name.
    

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/ni_measurement_plugin_sdk_generator/plugin/__main__.py -->
## PYTHON MODULE: packages/generator/ni_measurement_plugin_sdk_generator/plugin/__main__.py

### MODULE DOCSTRING

Creates a measurement through use of __init__.py.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/scripts/generate_grpc_stubs.py -->
## PYTHON MODULE: packages/generator/scripts/generate_grpc_stubs.py

### MODULE DOCSTRING

Generates gRPC Python stubs from proto files.

- `STUBS_NAMESPACE = 'tests.utilities.measurements.non_streaming_data_measurement._stubs'`

- `PROTO_PARENT_NAMESPACES = ['ni.measurementlink', 'nidevice_grpc', 'ni.protobuf.types']`

- `STUBS_PATH = pathlib.Path(__file__).parent.parent / STUBS_NAMESPACE.replace('.', '/')`

- `STUBS_PROTO_PATH = STUBS_PATH`

- `STUBS_PROTO_FILES = list(STUBS_PROTO_PATH.rglob('*.proto'))`

### `def main()`

Generate and fixup gRPC Python stubs.

### `def generate_python_files(stubs_path: pathlib.Path, proto_path: pathlib.Path, proto_files: Sequence[pathlib.Path])`

Generate python files from .proto files with protoc.

### `def fix_import_paths(protos_path: pathlib.Path, stubs_path: pathlib.Path, stubs_namespace: str, proto_parent_namespaces: Sequence[str])`

Fix import paths of generated files.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/__init__.py -->
## PYTHON MODULE: packages/generator/tests/__init__.py

### MODULE DOCSTRING

Tests.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_client_generator.py -->
## PYTHON MODULE: packages/generator/tests/acceptance/test_client_generator.py

### `def test___non_streaming_measurement___create_client___render_without_error(create_client: CliRunnerFunction, test_assets_directory: pathlib.Path, tmp_path_factory: pytest.TempPathFactory, non_streaming_measurement_service: MeasurementService) -> None`

### `def test___void_measurement___create_client___render_without_error(create_client: CliRunnerFunction, test_assets_directory: pathlib.Path, tmp_path_factory: pytest.TempPathFactory, void_measurement_service: MeasurementService) -> None`

### `def test___localized_measurement___create_client___render_without_error(create_client: CliRunnerFunction, test_assets_directory: pathlib.Path, tmp_path_factory: pytest.TempPathFactory, localized_measurement_service: MeasurementService) -> None`

### `def test___all_registered_measurements___create_client___renders_without_error(create_client: CliRunnerFunction, tmp_path_factory: pytest.TempPathFactory, multiple_measurement_service: MeasurementService) -> None`

### `def test___interactive_mode_with_registered_measurements___create_client___renders_without_error(create_client: CliRunnerFunction, test_assets_directory: pathlib.Path, tmp_path_factory: pytest.TempPathFactory, non_streaming_measurement_service: MeasurementService) -> None`

### `def test___interactive_mode_without_registered_measurements___create_client___raises_exception(create_client: CliRunnerFunction) -> None`

### `def test___non_streaming_measurement___create_client___render_with_proper_line_ending(create_client: CliRunnerFunction, tmp_path_factory: pytest.TempPathFactory, non_streaming_measurement_service: MeasurementService) -> None`

### `def test___non_streaming_measurement___create_client___render_without_mypy_error(create_client: CliRunnerFunction, tmp_path_factory: pytest.TempPathFactory, non_streaming_measurement_service: MeasurementService) -> None`

### `def _assert_equal(expected_path: pathlib.Path, result_path: pathlib.Path) -> None`

### `def _assert_line_ending(file_path: pathlib.Path) -> None`

### `def non_streaming_measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a non streaming Measurement Plug-In Service.

### `def void_measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a void Measurement Plug-In Service.

### `def localized_measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a localized Measurement Plug-In Service.

### `def multiple_measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a Measurement Plug-In Service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_non_streaming_measurement_client.py -->
## PYTHON MODULE: packages/generator/tests/acceptance/test_non_streaming_measurement_client.py

### `class EnumInEnum(Enum)`

EnumInEnum used for enum-typed measurement configs and outputs.

### `class ProtobufEnumInEnum(Enum)`

ProtobufEnumInEnum used for enum-typed measurement configs and outputs.

### `def test___measurement_plugin_client___measure___returns_output(measurement_plugin_client_module: ModuleType) -> None`

### `def test___measurement_plugin_client___measure___converts_output_types(measurement_plugin_client_module: ModuleType) -> None`

### `def test___measurement_plugin_client___stream_measure___returns_output(measurement_plugin_client_module: ModuleType) -> None`

### `def test___measurement_plugin_client___stream_measure___converts_output_types(measurement_plugin_client_module: ModuleType) -> None`

### `def measurement_client_directory(create_client: CliRunnerFunction, tmp_path_factory: pytest.TempPathFactory, measurement_service: MeasurementService) -> pathlib.Path`

Test fixture that creates a Measurement Plug-In Client.

### `def measurement_plugin_client_module(measurement_client_directory: pathlib.Path) -> ModuleType`

Test fixture that imports the generated Measurement Plug-In Client module.

### `def measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService]`

Test fixture that creates and hosts a Measurement Plug-In Service.

### `def _verify_output_types(outputs: Any, measurement_plugin_client_module: ModuleType) -> None`

### `def _assert_type(value: Any, expected_type: type[Any] | tuple[type[Any], ...]) -> None`

### `def _assert_collection_type(value: Any, expected_type: type[Any] | tuple[type[Any], ...], expected_element_type: type[Any] | tuple[type[Any], ...]) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_pin_aware_measurement_client.py -->
## PYTHON MODULE: packages/generator/tests/acceptance/test_pin_aware_measurement_client.py

### `def test___measurement_plugin_client___measure_with_pin_map_registration___returns_output(measurement_plugin_client_module: ModuleType, pin_map_directory: pathlib.Path) -> None`

### `def test___measurement_plugin_client___measure_without_pin_map_registration___raises_no_sessions_error(measurement_plugin_client_module: ModuleType) -> None`

### `def test___measurement_plugin_client___register_pin_map_without_pin_map_context___creates_pin_map_context_with_pin_map_id_and_sites(measurement_plugin_client_module: ModuleType, pin_map_directory: pathlib.Path) -> None`

### `def test___measurement_plugin_client___register_pin_map_with_pin_map_context___updates_pin_map_context_with_pin_map_id(measurement_plugin_client_module: ModuleType, pin_map_directory: pathlib.Path) -> None`

### `def test___measurement_plugin_client___measure_with_default_site_selection___returns_selected_site(measurement_plugin_client_module: ModuleType, pin_map_directory: pathlib.Path) -> None`

### `def test___measurement_plugin_client___measure_with_multiple_sites_selection___returns_selected_sites(measurement_plugin_client_module: ModuleType, pin_map_directory: pathlib.Path) -> None`

### `def test___measurement_plugin_client___measure_with_invalid_sites_selection___raises_invalid_sites_error(measurement_plugin_client_module: ModuleType, pin_map_directory: pathlib.Path) -> None`

### `def test___measurement_plugin_client___measure_with_pin_map_context___returns_output(measurement_plugin_client_module: ModuleType, pin_map_directory: pathlib.Path) -> None`

### `def measurement_client_directory(create_client: CliRunnerFunction, tmp_path_factory: pytest.TempPathFactory, measurement_service: MeasurementService) -> pathlib.Path`

Test fixture that creates a Measurement Plug-In Client.

### `def measurement_plugin_client_module(measurement_client_directory: pathlib.Path) -> ModuleType`

Test fixture that imports the generated Measurement Plug-In Client module.

### `def measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a Measurement Plug-In Service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_plugin_generator.py -->
## PYTHON MODULE: packages/generator/tests/acceptance/test_plugin_generator.py

### `def test___command_line_args___create_measurement___render_without_error(create_measurement: CliRunnerFunction, test_assets_directory: pathlib.Path, tmp_path_factory: pytest.TempPathFactory) -> None`

### `def test___command_line_args___create_measurement_with_annotations___render_without_error(create_measurement: CliRunnerFunction, test_assets_directory: pathlib.Path, tmp_path_factory: pytest.TempPathFactory) -> None`

### `def _assert_equal(expected_path: pathlib.Path, result_path: pathlib.Path) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/acceptance/test_streaming_measurement_client.py -->
## PYTHON MODULE: packages/generator/tests/acceptance/test_streaming_measurement_client.py

### `def test___measurement_plugin_client___measure___returns_output(measurement_plugin_client_module: ModuleType) -> None`

### `def test___measurement_plugin_client___stream_measure___returns_output(measurement_plugin_client_module: ModuleType) -> None`

### `def test___measurement_plugin_client___invoke_measure_from_two_threads___initiates_first_measure_and_rejects_second_measure(measurement_plugin_client_module: ModuleType) -> None`

### `def test___non_streaming_measurement_execution___cancel___cancels_measurement(measurement_plugin_client_module: ModuleType) -> None`

### `def test___streaming_measurement_execution___cancel___cancels_measurement(measurement_plugin_client_module: ModuleType) -> None`

### `def test___measurement_client___cancel_without_measure___returns_false(measurement_plugin_client_module: ModuleType) -> None`

### `def measurement_client_directory(create_client: CliRunnerFunction, tmp_path_factory: pytest.TempPathFactory, measurement_service: MeasurementService) -> pathlib.Path`

Test fixture that creates a Measurement Plug-In Client.

### `def measurement_plugin_client_module(measurement_client_directory: pathlib.Path) -> ModuleType`

Test fixture that imports the generated Measurement Plug-In Client module.

### `def measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a Measurement Plug-In Service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/conftest.py -->
## PYTHON MODULE: packages/generator/tests/conftest.py

### MODULE DOCSTRING

Shared fixtures for ni-measurement-plugin-sdk-generator tests.

### `class CliRunnerFunction(Protocol)`

Protocol for a callable that executes a CLI command using Click's CliRunner.

#### `def __call__(self, args: Sequence[str], input: str | None=None) -> Result`

Execute the CLI command with the provided arguments.

### `def test_assets_directory() -> pathlib.Path`

Gets path to test_assets directory.

### `def discovery_service_process() -> Generator[DiscoveryServiceProcess]`

Test fixture that creates discovery service process.

### `def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path`

Test fixture that returns the pin map directory.

### `def create_client() -> Generator[CliRunnerFunction]`

Test fixture for calling client generator cli.

### `def create_measurement() -> Generator[CliRunnerFunction]`

Test fixture for calling plugin generator cli.

### `def _create_clirunner() -> CliRunner`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement/_helpers.py -->
## PYTHON MODULE: packages/generator/tests/test_assets/example_renders/measurement/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement/measurement.py -->
## PYTHON MODULE: packages/generator/tests/test_assets/example_renders/measurement/measurement.py

### MODULE DOCSTRING

A default measurement with an array in and out.

### `def measure(array_input)`

TODO: replace the following line with your own measurement logic.

### `def main(verbose: int) -> None`

Host the Sample Measurement service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_plugin_client/localized_measurement_client.py -->
## PYTHON MODULE: packages/generator/tests/test_assets/example_renders/measurement_plugin_client/localized_measurement_client.py

### MODULE DOCSTRING

Generated client API for the '本地化测量（Py）' measurement plug-in.

- `_V2_MEASUREMENT_SERVICE_INTERFACE = 'ni.measurementlink.measurement.v2.MeasurementService'`

### `class EnumInEnum(Enum)`

EnumInEnum used for enum-typed measurement configs and outputs.

### `class Outputs(typing.NamedTuple)`

Outputs for the '本地化测量（Py）' measurement plug-in.

### `class LocalizedMeasurementClient()`

Client for the '本地化测量（Py）' measurement plug-in.

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, pin_map_client: PinMapClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None)`

Initialize the Measurement Plug-In Client.

        Args:
            discovery_client: An optional discovery client.

            pin_map_client: An optional pin map client.

            grpc_channel: An optional gRPC channel targeting a measurement service.

            grpc_channel_pool: An optional gRPC channel pool.
        

#### `def pin_map_context(self) -> PinMapContext`

The pin map context for the measurement.

#### `def pin_map_context(self, val: PinMapContext) -> None`

#### `def sites(self) -> list[int] | None`

The sites where the measurement must be executed.

#### `def sites(self, val: list[int]) -> None`

#### `def _get_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub`

#### `def _get_discovery_client(self) -> DiscoveryClient`

#### `def _get_grpc_channel_pool(self) -> GrpcChannelPool`

#### `def _get_pin_map_client(self) -> PinMapClient`

#### `def _create_file_descriptor(self) -> None`

#### `def _create_measure_request(self, parameter_values: list[typing.Any]) -> v2_measurement_service_pb2.MeasureRequest`

#### `def _deserialize_response(self, response: v2_measurement_service_pb2.MeasureResponse) -> Outputs`

#### `def _validate_response(self, response: v2_measurement_service_pb2.MeasureResponse) -> None`

#### `def measure(self, float_in: float=0.05999999865889549, double_array_in: typing.Iterable[float]=[0.1, 0.2, 0.3], bool_in: bool=False, string_in: str='示例字符串', string_array_in: typing.Iterable[str]=['带有/正斜杠的字符串', '带有\\反斜杠的字符串', "带有'单引号'的字符串", '带有"双引号"的字符串', '带有\t制表符的字符串', '带有\n换行符的字符串'], path_in: pathlib.PurePath=pathlib.PurePath('示例\\路径\\用于\\测试'), path_array_in: typing.Iterable[pathlib.PurePath]=[pathlib.PurePath('路径/带有/正斜杠'), pathlib.PurePath('路径\\带有\\反斜杠'), pathlib.PurePath("路径 带有 '单引号'"), pathlib.PurePath('路径 带有 "双引号"'), pathlib.PurePath('路径\t带有\t制表符'), pathlib.PurePath('路径\n带有\n换行符')], io_in: str='资源', io_array_in: typing.Iterable[str]=['资源1', '资源2'], integer_in: int=10, enum_in: EnumInEnum=EnumInEnum.BLUE, enum_array_in: typing.Iterable[EnumInEnum]=[EnumInEnum.RED, EnumInEnum.GREEN]) -> Outputs`

Perform a single measurement.

        Returns:
            Measurement outputs.
        

#### `def stream_measure(self, float_in: float=0.05999999865889549, double_array_in: typing.Iterable[float]=[0.1, 0.2, 0.3], bool_in: bool=False, string_in: str='示例字符串', string_array_in: typing.Iterable[str]=['带有/正斜杠的字符串', '带有\\反斜杠的字符串', "带有'单引号'的字符串", '带有"双引号"的字符串', '带有\t制表符的字符串', '带有\n换行符的字符串'], path_in: pathlib.PurePath=pathlib.PurePath('示例\\路径\\用于\\测试'), path_array_in: typing.Iterable[pathlib.PurePath]=[pathlib.PurePath('路径/带有/正斜杠'), pathlib.PurePath('路径\\带有\\反斜杠'), pathlib.PurePath("路径 带有 '单引号'"), pathlib.PurePath('路径 带有 "双引号"'), pathlib.PurePath('路径\t带有\t制表符'), pathlib.PurePath('路径\n带有\n换行符')], io_in: str='资源', io_array_in: typing.Iterable[str]=['资源1', '资源2'], integer_in: int=10, enum_in: EnumInEnum=EnumInEnum.BLUE, enum_array_in: typing.Iterable[EnumInEnum]=[EnumInEnum.RED, EnumInEnum.GREEN]) -> typing.Generator[Outputs]`

Perform a streaming measurement.

        Returns:
            Stream of measurement outputs.
        

#### `def cancel(self) -> bool`

Cancels the active measurement call.

#### `def register_pin_map(self, pin_map_path: pathlib.Path) -> None`

Registers the pin map with the pin map service.

        Args:
            pin_map_path: Absolute path of the pin map file.
        

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_plugin_client/non_streaming_data_measurement_client.py -->
## PYTHON MODULE: packages/generator/tests/test_assets/example_renders/measurement_plugin_client/non_streaming_data_measurement_client.py

### MODULE DOCSTRING

Generated client API for the 'Non-Streaming Data Measurement (Py)' measurement plug-in.

- `_V2_MEASUREMENT_SERVICE_INTERFACE = 'ni.measurementlink.measurement.v2.MeasurementService'`

### `class EnumInEnum(Enum)`

EnumInEnum used for enum-typed measurement configs and outputs.

### `class ProtobufEnumInEnum(Enum)`

ProtobufEnumInEnum used for enum-typed measurement configs and outputs.

### `class Outputs(typing.NamedTuple)`

Outputs for the 'Non-Streaming Data Measurement (Py)' measurement plug-in.

### `class NonStreamingDataMeasurementClient()`

Client for the 'Non-Streaming Data Measurement (Py)' measurement plug-in.

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, pin_map_client: PinMapClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None)`

Initialize the Measurement Plug-In Client.

        Args:
            discovery_client: An optional discovery client.

            pin_map_client: An optional pin map client.

            grpc_channel: An optional gRPC channel targeting a measurement service.

            grpc_channel_pool: An optional gRPC channel pool.
        

#### `def pin_map_context(self) -> PinMapContext`

The pin map context for the measurement.

#### `def pin_map_context(self, val: PinMapContext) -> None`

#### `def sites(self) -> list[int] | None`

The sites where the measurement must be executed.

#### `def sites(self, val: list[int]) -> None`

#### `def _get_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub`

#### `def _get_discovery_client(self) -> DiscoveryClient`

#### `def _get_grpc_channel_pool(self) -> GrpcChannelPool`

#### `def _get_pin_map_client(self) -> PinMapClient`

#### `def _create_file_descriptor(self) -> None`

#### `def _create_measure_request(self, parameter_values: list[typing.Any]) -> v2_measurement_service_pb2.MeasureRequest`

#### `def _deserialize_response(self, response: v2_measurement_service_pb2.MeasureResponse) -> Outputs`

#### `def _validate_response(self, response: v2_measurement_service_pb2.MeasureResponse) -> None`

#### `def measure(self, float_in: float=0.05999999865889549, double_array_in: typing.Iterable[float]=[0.1, 0.2, 0.3], bool_in: bool=False, string_in: str='sample string', string_array_in: typing.Iterable[str]=['string with /forwardslash', 'string with \\backslash', "string with 'single quotes'", 'string with "double quotes"', 'string with \ttabspace', 'string with \nnewline'], path_in: pathlib.PurePath=pathlib.PurePath('sample\\path\\for\\test'), path_array_in: typing.Iterable[pathlib.PurePath]=[pathlib.PurePath('path/with/forward/slash'), pathlib.PurePath('path\\with\\backslash'), pathlib.PurePath("path with 'single quotes'"), pathlib.PurePath('path with "double quotes"'), pathlib.PurePath('path\twith\ttabs'), pathlib.PurePath('path\nwith\nnewlines')], io_in: str='resource', io_array_in: typing.Iterable[str]=['resource1', 'resource2'], integer_in: int=10, enum_in: EnumInEnum=EnumInEnum.BLUE, enum_array_in: typing.Iterable[EnumInEnum]=[EnumInEnum.RED, EnumInEnum.GREEN], protobuf_enum_in: ProtobufEnumInEnum=ProtobufEnumInEnum.BLACK) -> Outputs`

Perform a single measurement.

        Returns:
            Measurement outputs.
        

#### `def stream_measure(self, float_in: float=0.05999999865889549, double_array_in: typing.Iterable[float]=[0.1, 0.2, 0.3], bool_in: bool=False, string_in: str='sample string', string_array_in: typing.Iterable[str]=['string with /forwardslash', 'string with \\backslash', "string with 'single quotes'", 'string with "double quotes"', 'string with \ttabspace', 'string with \nnewline'], path_in: pathlib.PurePath=pathlib.PurePath('sample\\path\\for\\test'), path_array_in: typing.Iterable[pathlib.PurePath]=[pathlib.PurePath('path/with/forward/slash'), pathlib.PurePath('path\\with\\backslash'), pathlib.PurePath("path with 'single quotes'"), pathlib.PurePath('path with "double quotes"'), pathlib.PurePath('path\twith\ttabs'), pathlib.PurePath('path\nwith\nnewlines')], io_in: str='resource', io_array_in: typing.Iterable[str]=['resource1', 'resource2'], integer_in: int=10, enum_in: EnumInEnum=EnumInEnum.BLUE, enum_array_in: typing.Iterable[EnumInEnum]=[EnumInEnum.RED, EnumInEnum.GREEN], protobuf_enum_in: ProtobufEnumInEnum=ProtobufEnumInEnum.BLACK) -> typing.Generator[Outputs]`

Perform a streaming measurement.

        Returns:
            Stream of measurement outputs.
        

#### `def cancel(self) -> bool`

Cancels the active measurement call.

#### `def register_pin_map(self, pin_map_path: pathlib.Path) -> None`

Registers the pin map with the pin map service.

        Args:
            pin_map_path: Absolute path of the pin map file.
        

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_plugin_client/void_measurement_client.py -->
## PYTHON MODULE: packages/generator/tests/test_assets/example_renders/measurement_plugin_client/void_measurement_client.py

### MODULE DOCSTRING

Generated client API for the 'Void Measurement (Py)' measurement plug-in.

- `_V2_MEASUREMENT_SERVICE_INTERFACE = 'ni.measurementlink.measurement.v2.MeasurementService'`

### `class VoidMeasurementClient()`

Client for the 'Void Measurement (Py)' measurement plug-in.

#### `def __init__(self, *, discovery_client: DiscoveryClient | None=None, pin_map_client: PinMapClient | None=None, grpc_channel: grpc.Channel | None=None, grpc_channel_pool: GrpcChannelPool | None=None)`

Initialize the Measurement Plug-In Client.

        Args:
            discovery_client: An optional discovery client.

            pin_map_client: An optional pin map client.

            grpc_channel: An optional gRPC channel targeting a measurement service.

            grpc_channel_pool: An optional gRPC channel pool.
        

#### `def pin_map_context(self) -> PinMapContext`

The pin map context for the measurement.

#### `def pin_map_context(self, val: PinMapContext) -> None`

#### `def sites(self) -> list[int] | None`

The sites where the measurement must be executed.

#### `def sites(self, val: list[int]) -> None`

#### `def _get_stub(self) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub`

#### `def _get_discovery_client(self) -> DiscoveryClient`

#### `def _get_grpc_channel_pool(self) -> GrpcChannelPool`

#### `def _get_pin_map_client(self) -> PinMapClient`

#### `def _create_file_descriptor(self) -> None`

#### `def _create_measure_request(self, parameter_values: list[typing.Any]) -> v2_measurement_service_pb2.MeasureRequest`

#### `def measure(self, integer_in: int=10) -> None`

Perform a single measurement.

        Returns:
            Measurement outputs.
        

#### `def stream_measure(self, integer_in: int=10) -> typing.Generator[None]`

Perform a streaming measurement.

        Returns:
            Stream of measurement outputs.
        

#### `def cancel(self) -> bool`

Cancels the active measurement call.

#### `def register_pin_map(self, pin_map_path: pathlib.Path) -> None`

Registers the pin map with the pin map service.

        Args:
            pin_map_path: Absolute path of the pin map file.
        

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_with_annotations/_helpers.py -->
## PYTHON MODULE: packages/generator/tests/test_assets/example_renders/measurement_with_annotations/_helpers.py

### MODULE DOCSTRING

Helper classes and functions for measurement plug-in examples.

### `class TestStandSupport()`

Class that communicates with TestStand.

#### `def __init__(self, sequence_context: Any) -> None`

Initialize the TestStandSupport object.

        Args:
            sequence_context:
                The SequenceContext COM object from the TestStand sequence execution.
                (Dynamically typed.)
        

#### `def get_active_pin_map_id(self) -> str`

Get the active pin map id from the NI.MeasurementPlugIns.PinMapId runtime variable.

        Returns:
            The resource id of the pin map if one is registered to the pin map service,
            otherwise an empty string.
        

#### `def resolve_file_path(self, file_path: str) -> str`

Resolve the absolute path to a file using the TestStand search directories.

        Args:
            file_path:
                An absolute or relative path to the file. If this is a relative path, this function
                searches the TestStand search directories for it.

        Returns:
            The absolute path to the file.
        

### `def configure_logging(verbosity: int) -> None`

Configure logging for this process.

- `F = TypeVar('F', bound=Callable)`

### `def verbosity_option(func: F) -> F`

Decorator for --verbose command line option.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/test_assets/example_renders/measurement_with_annotations/measurement.py -->
## PYTHON MODULE: packages/generator/tests/test_assets/example_renders/measurement_with_annotations/measurement.py

### MODULE DOCSTRING

A default measurement with an array in and out.

### `def measure(array_input)`

TODO: replace the following line with your own measurement logic.

### `def main(verbose: int) -> None`

Host the Sample Measurement service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/unit/test_measurement_client.py -->
## PYTHON MODULE: packages/generator/tests/unit/test_measurement_client.py

### `def test___enum_annotations___validate_and_transform_enum_annotations___returns_expected_enum_annotations(enum_annotations: str, expected_enum_annotations: str) -> None`

### `def test___invalid_enum_annotations___validate_and_transform_enum_annotations___raises_invalid_enum_value_error() -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/discovery_service_process.py -->
## PYTHON MODULE: packages/generator/tests/utilities/discovery_service_process.py

### MODULE DOCSTRING

Class to create and terminate Discovery Service instance.

### `class DiscoveryServiceProcess()`

Maintains the processes involved in creating and terminating discovery service.

#### `def __init__(self) -> None`

Creates a DiscoveryServiceProcess instance.

#### `def __enter__(self: Self) -> Self`

Returns the DiscoveryServiceProcess instance.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None`

Closes the DiscoveryServiceProcess instance.

#### `def _close_discovery_service(self) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/localized_measurement/__init__.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/localized_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test loopback measurement service with non-ASCII characters.

### `class Color(Enum)`

用于示例枚举类型配置和输出的主要颜色.

### `def measure(float_input: float, double_array_input: Iterable[float], bool_input: bool, string_input: str, string_array_input: Iterable[str], path_input: Path, path_array_input: Iterable[Path], io_input: str, io_array_input: Iterable[str], integer_input: int, enum_input: Color, enum_array_input: Iterable[Color]) -> tuple[float, Iterable[float], bool, str, Iterable[str], Path, Iterable[Path], str, Iterable[str], int, xydata_pb2.DoubleXYData, Color, Iterable[Color], array_pb2.Double2DArray, array_pb2.String2DArray]`

使用各种数据类型执行环回测量.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/__init__.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test loopback measurement service.

### `class Color(Enum)`

Primary colors used for example enum-typed config and output.

### `def measure(float_input: float, double_array_input: Iterable[float], bool_input: bool, string_input: str, string_array_input: Iterable[str], path_input: Path, path_array_input: Iterable[Path], io_input: str, io_array_input: Iterable[str], integer_input: int, enum_input: Color, enum_array_input: Iterable[Color], protobuf_enum_input: color_pb2.ProtobufColor.ValueType) -> tuple[float, Iterable[float], bool, str, Iterable[str], Path, Iterable[Path], str, Iterable[str], int, xydata_pb2.DoubleXYData, Color, Iterable[Color], color_pb2.ProtobufColor.ValueType, array_pb2.Double2DArray, array_pb2.String2DArray]`

Perform a loopback measurement with various data types.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/__init__.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/__init__.py

### MODULE DOCSTRING

Stubs for non_streaming_data_measurement's color enum.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bcolor.proto\x12@ni.measurementlink.measurement.non_streaming_data_measurement.v1*9\n\rProtobufColor\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05BLACK\x10\x03b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/non_streaming_data_measurement/_stubs/color_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/pin_aware_measurement/__init__.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/pin_aware_measurement/__init__.py

### MODULE DOCSTRING

Pin-aware measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[str, Iterable[int], Iterable[str], Iterable[str], Iterable[str]]`

Pin-aware measurement plug-in test service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/streaming_data_measurement/__init__.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/streaming_data_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test a v2 measurement service that streams data.

### `def measure(name: str, num_responses: int, data_size: int, cumulative_data: bool, response_interval_in_ms: int, error_on_index: int) -> Generator[Outputs]`

Returns the number of responses requested at the requested interval.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/generator/tests/utilities/measurements/void_measurement/__init__.py -->
## PYTHON MODULE: packages/generator/tests/utilities/measurements/void_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test void measurement service.

### `def measure(integer_input: int) -> tuple[()]`

Perform a measurement with no output.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/sdk/ni_measurement_plugin_sdk/__init__.py -->
## PYTHON MODULE: packages/sdk/ni_measurement_plugin_sdk/__init__.py

### MODULE DOCSTRING

Measurement Plug-In SDK for Python.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/_docs_source/conf.py -->
## PYTHON MODULE: packages/service/_docs_source/conf.py

### MODULE DOCSTRING

Sphinx Configuration File.

### `def skip_aliases(app, what, name, obj, skip, options)`

Skip documentation for classes that are exported from multiple modules.

### `def setup(sphinx)`

Sphinx setup callback.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/__init__.py

### MODULE DOCSTRING

Measurement Plug-In Support for Python.

- `__all__ = ['session_management', 'DataType', 'MeasurementInfo', 'ServiceInfo', 'MeasurementService']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_annotations.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_annotations.py

### MODULE DOCSTRING

Constants for annotations.

- `ENUM_VALUES_KEY = 'ni/enum.values'`

- `TYPE_SPECIALIZATION_KEY = 'ni/type_specialization'`

- `SERVICE_PROGRAMMINGLANGUAGE_KEY = 'ni/service.programminglanguage'`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_configuration.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_configuration.py

### MODULE DOCSTRING

Measurement plug-in configuration options.

- `_PREFIX = 'MEASUREMENT_PLUGIN'`

- `_T = TypeVar('_T')`

### `class MIDriverOptions(NamedTuple)`

Modular instrument driver options.

#### `def update_from_config(self) -> Self`

Read options from the configuration file and return a new options object.

#### `def to_dict(self) -> dict[str, Any]`

Convert options to a dict to pass to nimi-python.

### `class NISwitchOptions(NamedTuple)`

NI-SWITCH driver options.

#### `def update_from_config(self) -> Self`

Read options from the configuration file and return a new options object.

- `NIDCPOWER_OPTIONS = MIDriverOptions('nidcpower').update_from_config()`

- `NIDIGITAL_OPTIONS = MIDriverOptions('nidigital').update_from_config()`

- `NIDMM_OPTIONS = MIDriverOptions('nidmm').update_from_config()`

- `NIFGEN_OPTIONS = MIDriverOptions('nifgen').update_from_config()`

- `NISCOPE_OPTIONS = MIDriverOptions('niscope').update_from_config()`

- `NISWITCH_OPTIONS = NISwitchOptions('niswitch').update_from_config()`

- `NISWITCH_MULTIPLEXER_OPTIONS = NISwitchOptions('niswitch_multiplexer').update_from_config()`

- `USE_GRPC_DEVICE_SERVER = _config(f'{_PREFIX}_USE_GRPC_DEVICE_SERVER', default=True, cast=bool)`

- `GRPC_DEVICE_SERVER_ADDRESS = _config(f'{_PREFIX}_GRPC_DEVICE_SERVER_ADDRESS', default='')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_datatypeinfo.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_datatypeinfo.py

### `class DataTypeInfo(NamedTuple)`

Class that represents the information for each of the :any:`DataType` enum values.

### `def get_type_info(data_type: DataType) -> DataTypeInfo`

Get information about a DataType.

- `_DATATYPE_TO_DATATYPEINFO_LOOKUP = {DataType.Int32: DataTypeInfo(type_pb2.Field.TYPE_INT32, False), DataType.Int64: DataTypeInfo(type_pb2.Field.TYPE_INT64, False), DataType.UInt32: DataTypeInfo(type_pb2.Field.TYPE_UINT32, False), DataType.UInt64: DataTypeInfo(type_pb2.Field.TYPE_UINT64, False), DataType.Float: DataTypeInfo(type_pb2.Field.TYPE_FLOAT, False), DataType.Double: DataTypeInfo(type_pb2.Field.TYPE_DOUBLE, False), DataType.Boolean: DataTypeInfo(type_pb2.Field.TYPE_BOOL, False), DataType.String: DataTypeInfo(type_pb2.Field.TYPE_STRING, False), DataType.Pin: DataTypeInfo(type_pb2.Field.TYPE_STRING, False, TypeSpecialization.Pin), DataType.Path: DataTypeInfo(type_pb2.Field.TYPE_STRING, False, TypeSpecialization.Path), DataType.Enum: DataTypeInfo(type_pb2.Field.TYPE_ENUM, False, TypeSpecialization.Enum), DataType.DoubleXYData: DataTypeInfo(type_pb2.Field.TYPE_MESSAGE, False, message_type=xydata_pb2.DoubleXYData.DESCRIPTOR.full_name), DataType.Double2DArray: DataTypeInfo(type_pb2.Field.TYPE_MESSAGE, False, message_type=array_pb2.Double2DArray.DESCRIPTOR.full_name), DataType.String2DArray: DataTypeInfo(type_pb2.Field.TYPE_MESSAGE, False, message_type=array_pb2.String2DArray.DESCRIPTOR.full_name), DataType.IOResource: DataTypeInfo(type_pb2.Field.TYPE_STRING, False, TypeSpecialization.IOResource), DataType.Int32Array1D: DataTypeInfo(type_pb2.Field.TYPE_INT32, True), DataType.Int64Array1D: DataTypeInfo(type_pb2.Field.TYPE_INT64, True), DataType.UInt32Array1D: DataTypeInfo(type_pb2.Field.TYPE_UINT32, True), DataType.UInt64Array1D: DataTypeInfo(type_pb2.Field.TYPE_UINT64, True), DataType.FloatArray1D: DataTypeInfo(type_pb2.Field.TYPE_FLOAT, True), DataType.DoubleArray1D: DataTypeInfo(type_pb2.Field.TYPE_DOUBLE, True), DataType.BooleanArray1D: DataTypeInfo(type_pb2.Field.TYPE_BOOL, True), DataType.StringArray1D: DataTypeInfo(type_pb2.Field.TYPE_STRING, True), DataType.PinArray1D: DataTypeInfo(type_pb2.Field.TYPE_STRING, True, TypeSpecialization.Pin), DataType.PathArray1D: DataTypeInfo(type_pb2.Field.TYPE_STRING, True, TypeSpecialization.Path), DataType.EnumArray1D: DataTypeInfo(type_pb2.Field.TYPE_ENUM, True, TypeSpecialization.Enum), DataType.DoubleXYDataArray1D: DataTypeInfo(type_pb2.Field.TYPE_MESSAGE, True, message_type=xydata_pb2.DoubleXYData.DESCRIPTOR.full_name), DataType.IOResourceArray1D: DataTypeInfo(type_pb2.Field.TYPE_STRING, True, TypeSpecialization.IOResource)}`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_dotenvpath.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_dotenvpath.py

### `def get_dotenv_search_path() -> Path`

Get the search path for loading the `.env` file.

### `def _has_dotenv_file(dir: Path) -> bool`

Check whether the dir or its parents contains a `.env` file.

### `def _get_script_or_exe_path() -> Path | None`

Get the path of the top-level script or PyInstaller EXE, if possible.

### `def _get_caller_path() -> Path | None`

Get the path of the module calling into this package, if possible.

### `def _get_package_path() -> Path`

Get the path of this package.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_featuretoggles.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_featuretoggles.py

### MODULE DOCSTRING

Measurement plug-in feature toggles.

### `class _OrderedEnum(Enum)`

#### `def __ge__(self, other: Self) -> bool`

#### `def __gt__(self, other: Self) -> bool`

#### `def __le__(self, other: Self) -> bool`

#### `def __lt__(self, other: Self) -> bool`

### `class CodeReadiness(_OrderedEnum)`

Indicates whether code is ready to be supported.

### `def _init_code_readiness_level() -> CodeReadiness`

- `_CODE_READINESS_LEVEL = _init_code_readiness_level()`

### `def get_code_readiness_level() -> CodeReadiness`

Get the current code readiness level.

    You can override this in tests by specifying the ``use_code_readiness``
    mark.
    

### `class FeatureNotSupportedError(Exception)`

The feature is not supported at the current code readiness level.

### `class FeatureToggle()`

A run-time feature toggle.

#### `def __init__(self, name: str, readiness: CodeReadiness) -> None`

Initialize the feature toggle.

#### `def is_enabled(self) -> bool`

Indicates whether the feature is currently enabled.

        You can enable/disable features in tests by specifying the
        ``enable_feature_toggle`` or ``disable_feature_toggle`` marks.
        

#### `def _raise_if_disabled(self) -> None`

### `def requires_feature(feature_toggle: FeatureToggle) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]`

Decorator specifying that the function requires the specified feature toggle.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/__init__.py

### MODULE DOCSTRING

Internal modules and classes for Measurement Framework.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/discovery_client.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/discovery_client.py

### MODULE DOCSTRING

Redirect internal discovery client API to the public API.

- `__all__ = ['DiscoveryClient', 'ServiceLocation']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/grpc_servicer.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/grpc_servicer.py

### MODULE DOCSTRING

gRPC servicers for each version of the measurement service interface.

### `class MeasurementServiceContext()`

Accessor for the measurement service's context-local state.

#### `def __init__(self, grpc_context: grpc.ServicerContext, pin_map_context: PinMapContext, owner: weakref.ReferenceType[object] | None) -> None`

Initialize the measurement service context.

#### `def mark_complete(self) -> None`

Mark the current RPC as complete.

#### `def grpc_context(self) -> grpc.ServicerContext`

Get the context for the RPC.

#### `def owner(self) -> object`

The owner of the server (e.g. measurement service).

#### `def pin_map_context(self) -> PinMapContext`

Get the pin map context for the RPC.

#### `def add_cancel_callback(self, cancel_callback: Callable[[], None]) -> None`

Add a callback that is invoked when the RPC is canceled.

#### `def cancel(self) -> None`

Cancel the RPC.

#### `def time_remaining(self) -> float`

Get the time remaining for the RPC.

#### `def abort(self, code: grpc.StatusCode, details: str) -> None`

Aborts the RPC.

### `class CustomRpcError(grpc.RpcError)`

A custom exception class for handling gRPC RPC errors.

    gRPC's built-in RpcError is not directly configurable in Python, so this class
    enables the creation of custom RPC errors with specific error codes.
    

#### `def __init__(self, code: grpc.StatusCode, details: str) -> None`

Initialize a CustomRpcError instance.

#### `def code(self) -> grpc.StatusCode`

Get the gRPC status code.

#### `def details(self) -> str`

Get the gRPC status details.

### `def _get_mapping_by_parameter_name(mapping_by_id: dict[int, Any], measure_function: Callable[[], None]) -> dict[str, Any]`

Transform a mapping by id into a mapping by parameter name (i.e. kwargs).

### `def _serialize_outputs(output_metadata: dict[int, ParameterMetadata], outputs: Any, service_name: str) -> any_pb2.Any`

### `def frame_metadata_dict(parameter_list: list[ParameterMetadata]) -> dict[int, ParameterMetadata]`

Create a metadata dictionary.

### `class MeasurementServiceServicerV1(v1_measurement_service_pb2_grpc.MeasurementServiceServicer)`

Measurement v1 servicer.

#### `def __init__(self, measurement_info: MeasurementInfo, configuration_parameter_list: list[ParameterMetadata], output_parameter_list: list[ParameterMetadata], measure_function: Callable, owner: object, service_info: ServiceInfo) -> None`

Initialize the measurement v1 servicer.

#### `def GetMetadata(self, request: v1_measurement_service_pb2.GetMetadataRequest, context: grpc.ServicerContext) -> v1_measurement_service_pb2.GetMetadataResponse`

RPC API to get measurement metadata.

#### `def Measure(self, request: v1_measurement_service_pb2.MeasureRequest, context: grpc.ServicerContext) -> v1_measurement_service_pb2.MeasureResponse`

RPC API that executes the registered measurement method.

#### `def _serialize_response(self, outputs: Any) -> v1_measurement_service_pb2.MeasureResponse`

#### `def _validate_parameters(self, request: v1_measurement_service_pb2.MeasureRequest) -> None`

### `class MeasurementServiceServicerV2(v2_measurement_service_pb2_grpc.MeasurementServiceServicer)`

Measurement v2 servicer.

#### `def __init__(self, measurement_info: MeasurementInfo, configuration_parameter_list: list[ParameterMetadata], output_parameter_list: list[ParameterMetadata], measure_function: Callable, owner: object, service_info: ServiceInfo) -> None`

Initialize the measurement v2 servicer.

#### `def GetMetadata(self, request: v2_measurement_service_pb2.GetMetadataRequest, context: grpc.ServicerContext) -> v2_measurement_service_pb2.GetMetadataResponse`

RPC API to get measurement metadata.

#### `def Measure(self, request: v2_measurement_service_pb2.MeasureRequest, context: grpc.ServicerContext) -> Generator[v2_measurement_service_pb2.MeasureResponse]`

RPC API that executes the registered measurement method.

#### `def _serialize_response(self, outputs: Any) -> v2_measurement_service_pb2.MeasureResponse`

#### `def _validate_parameters(self, request: v2_measurement_service_pb2.MeasureRequest) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/__init__.py

### MODULE DOCSTRING

Contains modules related to Measurement parameter.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/_get_type.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/_get_type.py

- `_TYPE_DEFAULT_MAPPING = {Field.TYPE_FLOAT: float(), Field.TYPE_DOUBLE: float(), Field.TYPE_INT32: int(), Field.TYPE_INT64: int(), Field.TYPE_UINT32: int(), Field.TYPE_UINT64: int(), Field.TYPE_BOOL: bool(), Field.TYPE_STRING: '', Field.TYPE_ENUM: int()}`

- `_PYTHON_DEFAULT_TYPES = {type(value) for value in _TYPE_DEFAULT_MAPPING.values()}`

- `TYPE_FIELD_MAPPING = {Field.TYPE_FLOAT: FieldDescriptorProto.TYPE_FLOAT, Field.TYPE_DOUBLE: FieldDescriptorProto.TYPE_DOUBLE, Field.TYPE_INT32: FieldDescriptorProto.TYPE_INT32, Field.TYPE_INT64: FieldDescriptorProto.TYPE_INT64, Field.TYPE_UINT32: FieldDescriptorProto.TYPE_UINT32, Field.TYPE_UINT64: FieldDescriptorProto.TYPE_UINT64, Field.TYPE_BOOL: FieldDescriptorProto.TYPE_BOOL, Field.TYPE_STRING: FieldDescriptorProto.TYPE_STRING, Field.TYPE_ENUM: FieldDescriptorProto.TYPE_ENUM, Field.TYPE_MESSAGE: FieldDescriptorProto.TYPE_MESSAGE}`

### `def get_type_default(value_type: Field.Kind.ValueType, repeated: bool, default_value_type: type | None=None) -> Any`

Get the default value for the give type.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/decoder.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/decoder.py

### `def deserialize_parameters(parameter_metadata_dict: dict[int, ParameterMetadata], parameter_bytes: bytes, service_name: str) -> dict[int, Any]`

Deserialize the bytes of the parameter based on the metadata.

    Args:
        parameter_metadata_dict (Dict[int, ParameterMetadata]): Parameter metadata by ID.

        parameter_bytes (bytes): Byte string to deserialize.

        service_name (str): Unique service name.

    Returns:
        Dict[int, Any]: Deserialized parameters by ID.
    

### `def _deserialize_enum_parameter(field_value: Any, metadata: ParameterMetadata) -> Any`

Convert enum into their user defined enum type.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/encoder.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/encoder.py

### MODULE DOCSTRING

Parameter Serializer.

### `def serialize_parameters(parameter_metadata_dict: dict[int, ParameterMetadata], parameter_values: Sequence[Any], service_name: str) -> bytes`

Serialize the parameter values in same order based on the metadata_dict.

    Args:
        parameter_metadata_dict (Dict[int, ParameterMetadata]): Parameter metadata by ID.

        parameter_values (Sequence[Any]): Parameter values to serialize.

        service_name (str): Unique service name.

    Returns:
        bytes: Serialized byte string containing parameter values.
    

### `def serialize_default_values(parameter_metadata_dict: dict[int, ParameterMetadata], service_name: str) -> bytes`

Serialize the Default values in the Metadata.

    Args:
        parameter_metadata_dict (Dict[int, ParameterMetadata]): Configuration metadata.

        service_name (str): Unique service name.

    Returns:
        bytes: Serialized byte string containing default values.
    

### `def _get_enum_values(param: Any) -> Any`

Get's value of an enum.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/metadata.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/metadata.py

### MODULE DOCSTRING

Contains classes that represents metadata.

- `_VALID_CHARS = set(" ().,;:!?-_'+")`

### `class ParameterMetadata(NamedTuple)`

Class that represents the metadata of parameters.

#### `def initialize(display_name: str, type: type_pb2.Field.Kind.ValueType, repeated: bool, default_value: Any, annotations: dict[str, str], message_type: str='', enum_type: SupportedEnumType | None=None) -> ParameterMetadata`

Initialize ParameterMetadata with field_name.

### `def _validate_display_name(display_name: str) -> None`

Validate and raise exception if 'display_name' has invalid characters.

    Raises:
        ValueError: If display_name has invalid characters.
    

### `def _validate_default_value_type(parameter_metadata: ParameterMetadata) -> None`

Validate and raise exception if the default value does not match the type info.

    Args:
        parameter_metadata (ParameterMetadata): Parameter metadata

    Raises:
        TypeError: If default value does not match the Datatype.
    

### `def _validate_default_value_type_for_scalar_type(default_value: object, expected_type: type, enum_values_annotation: str, display_name: str) -> None`

Validate and raise exception if the default value does not match the type info.

### `def _validate_default_value_type_for_repeated_type(default_value: Iterable[object], expected_type: type, expected_element_type: type, enum_values_annotation: str, display_name: str) -> None`

Validate and raise exception if the default value does not match the type info.

### `def _validate_default_value_type_for_basic_type(default_value: object, expected_type: type, display_name: str) -> None`

### `def _validate_default_value_type_for_enum_type(default_value: object, user_enum: dict[str, int], enum_values_annotation: str, display_name: str) -> None`

### `def get_enum_values_annotation(parameter_metadata: ParameterMetadata) -> str`

Gets the value for the "ni/enum.values" annotation if it exists.

    Args:
        parameter_metadata (ParameterMetadata): Parameter metadata

    Returns:
        str: The value of "ni/enum.values" annotation
    

### `def _is_valid_enum_value(enum_value: object, user_enum: dict[str, int]) -> bool`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/serialization_descriptors.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/serialization_descriptors.py

### MODULE DOCSTRING

Serialization Descriptors.

### `def is_protobuf(enum_type: SupportedEnumType | None) -> bool`

Finds if 'enum_type' is a protobuf or a python enum.

### `def _get_enum_type_name(metadata: ParameterMetadata) -> str`

Get's enum type name from a 'parameter_metadata'.

### `def _create_enum_type_class(file_descriptor: FileDescriptorProto, metadata: ParameterMetadata, field_descriptor: FieldDescriptorProto) -> None`

Implement a enum class in 'file_descriptor'.

### `def _create_field(message_proto: DescriptorProto, metadata: ParameterMetadata, index: int) -> FieldDescriptorProto`

Implement a field in 'message_proto'.

### `def _create_message_type(parameter_metadata: list[ParameterMetadata], message_name: str, file_descriptor: FileDescriptorProto) -> None`

Creates a message type with fields intialized in 'file_descriptor'.

### `def create_file_descriptor(service_name: str, output_metadata: list[ParameterMetadata], input_metadata: list[ParameterMetadata], pool: DescriptorPool) -> None`

Creates two message types in one file descriptor proto.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/service_manager.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/_internal/service_manager.py

- `_V1_INTERFACE = 'ni.measurementlink.measurement.v1.MeasurementService'`

- `_V2_INTERFACE = 'ni.measurementlink.measurement.v2.MeasurementService'`

### `class GrpcService()`

Manages the gRPC server lifetime and registration.

#### `def __init__(self, discovery_client: DiscoveryClient | None=None) -> None`

Initialize the service.

#### `def discovery_client(self) -> DiscoveryClient`

Client for accessing the NI Discovery Service.

#### `def port(self) -> str`

The insecure port.

#### `def server(self) -> grpc.Server | None`

The gRPC server.

#### `def service_location(self) -> ServiceLocation`

The location of the service on the network.

#### `def start(self, measurement_info: MeasurementInfo, service_info: ServiceInfo, configuration_parameter_list: list[ParameterMetadata], output_parameter_list: list[ParameterMetadata], measure_function: Callable, owner: object=None) -> str`

Start the gRPC server and register it with the discovery service.

        Returns:
            The insecure port.
        

#### `def stop(self) -> None`

Unregister and stop the gRPC server.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/discovery/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/discovery/__init__.py

### MODULE DOCSTRING

Compatibility API for accessing the NI Discovery Service.

The public API for accessing the NI Discovery Service has moved to the
:mod:`ni.measurementlink.discovery.v1.client` package.

The :mod:`ni_measurement_plugin_sdk_service.discovery` subpackage provides
compatibility with existing applications and will be deprecated in a future
release.


- `__all__ = ['DiscoveryClient', 'ServiceLocation']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/grpc/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/grpc/__init__.py

### MODULE DOCSTRING

Compatibility API for gRPC extensions.

The public gRPC extensions API has moved to the :external+ni_grpc_extensions:doc:`index` package.

The :mod:`ni_measurement_plugin_sdk_service.grpc` subpackage provides
compatibility with existing applications and will be deprecated in a future
release.


<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/grpc/channelpool.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/grpc/channelpool.py

### MODULE DOCSTRING

Compatibility API for gRPC channel pool.

The :obj:`GrpcChannelPool` class has moved to the :mod:`ni_grpc_extensions.channelpool`
submodule.

The :mod:`ni_measurement_plugin_sdk_service.grpc.channelpool` submodule provides
compatibility with existing applications and will be deprecated in a future
release.


- `__all__ = ['GrpcChannelPool']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/grpc/loggers.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/grpc/loggers.py

### MODULE DOCSTRING

Compatibility API for gRPC logging interceptors.

The gRPC logging interceptor classes have moved to the :mod:`ni_grpc_extensions.loggers`
submodule.

The :mod:`ni_measurement_plugin_sdk_service.grpc.loggers` submodule provides
compatibility with existing applications and will be deprecated in a future
release.


- `__all__ = ['ClientLogger', 'ServerLogger']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/measurement/__init__.py

### MODULE DOCSTRING

Measurement Framework Package.

### `class WrongMessageTypeWarning(RuntimeWarning)`

Wrong message type received.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/client_support.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/measurement/client_support.py

### MODULE DOCSTRING

Support functions for the Measurement Plug-In Client.

- `__all__ = ['create_file_descriptor', 'deserialize_parameters', 'ParameterMetadata', 'serialize_parameters']`

### `def deserialize_parameters(parameter_metadata_dict: dict[int, ParameterMetadata], parameter_bytes: bytes, message_name: str, *, convert_paths: bool=True) -> Sequence[Any]`

Deserialize parameter bytes into separate parameter values.

    Args:
        parameter_metadata_dict: Parameter metadata by ID.

        parameter_byte: Byte string to deserialize.

        message_name: gRPC message name (e.g. f"{service_class}.Outputs").

        convert_paths: Specifies whether to convert path parameters to pathlib.Path.

    Returns:
        Deserialized parameter values, ordered by ID.
    

### `def serialize_parameters(parameter_metadata_dict: dict[int, ParameterMetadata], parameter_values: Sequence[Any], message_name: str) -> bytes`

Serialize parameter values into a parameter byte string.

    Args:
        parameter_metadata_dict: Parameter metadata by ID.

        parameter_values: Parameter values to serialize, ordered by ID.

        message_name: gRPC message name (e.g. f"{service_class}.Configurations").

    Returns:
        Serialized byte string containing parameter values.
    

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/info.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/measurement/info.py

### MODULE DOCSTRING

Measurement service metadata classes and enums.

- `__all__ = ['ServiceInfo', 'MeasurementInfo', 'TypeSpecialization', 'DataType']`

### `class MeasurementInfo(NamedTuple)`

A named tuple providing information about a measurement.

### `class TypeSpecialization(enum.Enum)`

Enum that represents the type specializations for measurement parameters.

### `class DataType(enum.Enum)`

Enum that represents the supported data types.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/service.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/measurement/service.py

### MODULE DOCSTRING

Framework to host measurement service.

### `class MeasurementContext()`

Proxy for the Measurement Service's context-local state.

#### `def grpc_context(self) -> grpc.ServicerContext`

Get the context for the RPC.

#### `def pin_map_context(self) -> PinMapContext`

Get the pin map context for the RPC.

#### `def add_cancel_callback(self, cancel_callback: Callable[[], None]) -> None`

Add a callback which is invoked when the RPC is canceled.

#### `def cancel(self) -> None`

Cancel the RPC.

#### `def time_remaining(self) -> float`

Get the time remaining for the RPC.

#### `def abort(self, code: grpc.StatusCode, details: str) -> None`

Aborts the RPC.

#### `def _measurement_service(self) -> MeasurementService`

#### `def reserve_session(self, pin_or_relay_names: str | Iterable[str], timeout: float | None=0.0) -> SingleSessionReservation`

Reserve a single session.

        Reserve the session matching the given pins, sites, and instrument type ID and return
        the information needed to create or access the session.

        Args:
            pin_or_relay_names: One or multiple pins, pin groups, relays, or relay groups to
                use for the measurement.

            timeout: Timeout in seconds.

                Allowed values: 0 (non-blocking, fails immediately if resources cannot be
                reserved), -1 (infinite timeout), or any other positive numeric value (wait for
                that number of seconds)

        Returns:
            A reservation object with which you can query information about the session and
            unreserve it.
        

#### `def reserve_sessions(self, pin_or_relay_names: str | Iterable[str], timeout: float | None=0.0) -> MultiSessionReservation`

Reserve multiple sessions.

        Reserve sessions matching the given pins, sites, and instrument type ID and return the
        information needed to create or access the sessions.

        Args:
            pin_or_relay_names: One or multiple pins, pin groups, relays, or relay groups to use
                for the measurement.

            timeout: Timeout in seconds.

                Allowed values: 0 (non-blocking, fails immediately if resources cannot be
                reserved), -1 (infinite timeout), or any other positive numeric value (wait for
                that number of seconds)

        Returns:
            A reservation object with which you can query information about the sessions and
            unreserve them.
        

- `_F = TypeVar('_F', bound=Callable)`

### `class MeasurementService()`

Class that supports registering and hosting a python function as a gRPC service.

#### `def __init__(self, service_config_path: Path, version: str='', ui_file_paths: list[Path]=[], service_class: str | None=None) -> None`

Initialize the Measurement Service object.

        Uses the specified .serviceconfig file, version, and UI file paths
        to initialize a Measurement Service object.

        Args:
            service_config_path (Path): Path to the .serviceconfig file.

            version (str): Version of the measurement service. Do not use this
                parameter.  Instead, specify the "version" field in the
                .serviceconfig file. Default value is "".

            ui_file_paths (List[Path]): List of paths to supported UIs.
                Default value is [].

            service_class (str): The service class from the .serviceconfig to use.
                Default value is None, which will use the first service in the
                .serviceconfig file.

        

#### `def _raise_measurement_method_not_registered(self) -> Any`

#### `def channel_pool(self) -> GrpcChannelPool`

Pool of gRPC channels used by the service.

#### `def discovery_client(self) -> DiscoveryClient`

Client for accessing the NI Discovery Service.

#### `def configuration_parameter_list(self) -> list[Any]`

List of configuration parameters.

#### `def grpc_service(self) -> GrpcService | None`

The gRPC service object. This is a private implementation detail.

#### `def measure_function(self) -> Callable`

Registered measurement function.

#### `def output_parameter_list(self) -> list[Any]`

List of output parameters.

#### `def service_location(self) -> ServiceLocation`

The location of the service on the network.

#### `def session_management_client(self) -> SessionManagementClient`

Client for accessing the measurement plug-in session management service.

#### `def register_measurement(self, measurement_function: _F) -> _F`

Register a function as the measurement function for a measurement service.

        To declare a measurement function, use this idiom::

            @measurement_service.register_measurement
            @measurement_service.configuration("Configuration 1", ...)
            @measurement_service.configuration("Configuration 2", ...)
            @measurement_service.output("Output 1", ...)
            @measurement_service.output("Output 2", ...)
            def measure(configuration1, configuration2):
                ...
                return (output1, output2)

        See also: :func:`.configuration`, :func:`.output`
        

#### `def configuration(self, display_name: str, type: DataType, default_value: Any, *, instrument_type: str='', enum_type: SupportedEnumType | None=None) -> Callable[[_F], _F]`

Add a configuration parameter to a measurement function.

        This decorator maps the measurement service's configuration parameters
        to Python positional parameters. To add multiple configuration parameters
        to the same measurement function, use this decorator multiple times.
        The order of decorator calls must match the order of positional parameters.

        See also: :func:`.register_measurement`

        Args:
            display_name: Display name of the configuration.

            type: Data type of the configuration.

            default_value: Default value of the configuration.

            instrument_type:
                Filter pins by instrument type. This is only supported when configuration type
                is DataType.IOResource or DataType.Pin (deprecated).

                For NI instruments, use instrument type id constants defined by
                :py:mod:`ni_measurement_plugin_sdk_service.session_management`, such as
                :py:const:`~ni_measurement_plugin_sdk_service.session_management.INSTRUMENT_TYPE_NI_DCPOWER`
                or
                :py:const:`~ni_measurement_plugin_sdk_service.session_management.INSTRUMENT_TYPE_NI_DMM`.

                For custom instruments, use the instrument type id defined in the pin map file.

            enum_type:
                Defines the enum type associated with this configuration parameter. This is only
                supported when configuration type is DataType.Enum or DataType.EnumArray1D.

        Returns:
            Callable that takes in Any Python Function
            and returns the same python function.
        

#### `def output(self, display_name: str, type: DataType, *, enum_type: SupportedEnumType | None=None) -> Callable[[_F], _F]`

Add an output parameter to a measurement function.

        This decorator maps the measurement service's output parameters to
        the elements of the tuple returned by the measurement function.
        To add multiple output parameters to the same measurement function,
        use this decorator multiple times.
        The order of decorator calls must match the order of elements
        returned by the measurement function.

        See also: :func:`.register_measurement`

        Args:
            display_name: Display name of the output.

            type: Data type of the output.

            enum_type:
                Defines the enum type associated with this configuration parameter. This is only
                supported when configuration type is DataType.Enum or DataType.EnumArray1D.

        Returns:
            Callable that takes in Any Python Function and
            returns the same python function.
        

#### `def host_service(self) -> MeasurementService`

Host the registered measurement method as a gRPC measurement service.

        Returns:
            MeasurementService: Context manager that can be used with a with-statement to close
            the service.

        Raises:
            Exception: If register measurement methods not available.
        

#### `def _make_annotations_dict(self, type_specialization: TypeSpecialization, *, instrument_type: str='', enum_type: SupportedEnumType | None=None) -> dict[str, str]`

#### `def _enum_to_annotations_value(self, enum_type: SupportedEnumType) -> str`

#### `def _is_protobuf_enum(self, enum_type: SupportedEnumType) -> TypeGuard[_EnumTypeWrapper]`

#### `def close_service(self) -> None`

Stop the gRPC measurement service.

        This method stops the gRPC server, unregisters with the discovery service, and cleans up
        the cached discovery client and gRPC channel pool.

        After calling close_service(), you may call host_service() again.

        Exiting the measurement service's runtime context automatically calls close_service().
        

#### `def __enter__(self: Self) -> Self`

Enter the runtime context related to the measurement service.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> Literal[False]`

Exit the runtime context related to the measurement service.

#### `def get_channel(self, provided_interface: str, service_class: str='') -> grpc.Channel`

Return gRPC channel to specified service.

        Args:
            provided_interface (str): The gRPC Full Name of the service.

            service_class (str): The service "class" that should be matched.

        Returns:
            grpc.Channel: A channel to the gRPC service.

        Raises:
            Exception: If service_class is not specified and there is more than one matching service
                registered.
        

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/pin_map/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/pin_map/__init__.py

### MODULE DOCSTRING

Compatibility API for accessing the NI Pin Map Service.

The public API for accessing the NI Pin Map Service has moved to the
:mod:`ni.measurementlink.pinmap.v1.client` package.

The :mod:`ni_measurement_plugin_sdk_service.pin_map` subpackage provides
compatibility with existing applications and will be deprecated in a future
release.


- `__all__ = ['PinMapClient']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/session_management/__init__.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/session_management/__init__.py

### MODULE DOCSTRING

Compatibility API for accessing the NI Session Management Service.

The public API for accessing the NI Session Management Service has moved to the
:mod:`ni.measurementlink.sessionmanagement.v1.client` package.

The :mod:`ni_measurement_plugin_sdk_service.session_management` subpackage
provides compatibility with existing applications and will be deprecated in a
future release.


- `__all__ = ['GRPC_SERVICE_CLASS', 'GRPC_SERVICE_INTERFACE_NAME', 'INSTRUMENT_TYPE_NONE', 'INSTRUMENT_TYPE_NI_DCPOWER', 'INSTRUMENT_TYPE_NI_HSDIO', 'INSTRUMENT_TYPE_NI_RFSA', 'INSTRUMENT_TYPE_NI_RFMX', 'INSTRUMENT_TYPE_NI_RFSG', 'INSTRUMENT_TYPE_NI_RFPM', 'INSTRUMENT_TYPE_NI_DMM', 'INSTRUMENT_TYPE_NI_DIGITAL_PATTERN', 'INSTRUMENT_TYPE_NI_SCOPE', 'INSTRUMENT_TYPE_NI_FGEN', 'INSTRUMENT_TYPE_NI_DAQMX', 'INSTRUMENT_TYPE_NI_RELAY_DRIVER', 'INSTRUMENT_TYPE_NI_MODEL_BASED_INSTRUMENT', 'INSTRUMENT_TYPE_NI_SWITCH_EXECUTIVE_VIRTUAL_DEVICE', 'SITE_SYSTEM_PINS', 'BaseReservation', 'ChannelMapping', 'Connection', 'MultiplexerSessionInformation', 'MultiplexerSessionContainer', 'MultiSessionReservation', 'PinMapContext', 'SessionInformation', 'SessionInitializationBehavior', 'SessionManagementClient', 'SingleSessionReservation', 'TypedConnection', 'TypedConnectionWithMultiplexer', 'TypedMultiplexerSessionInformation', 'TypedSessionInformation']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/session_management/_reservation.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/session_management/_reservation.py

- `__all__ = ['BaseReservation', 'MultiplexerSessionContainer', 'MultiSessionReservation', 'SingleSessionReservation']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/session_management/_types.py -->
## PYTHON MODULE: packages/service/ni_measurement_plugin_sdk_service/session_management/_types.py

- `__all__ = ['ChannelMapping', 'Connection', 'MultiplexerSessionInformation', 'PinMapContext', 'SessionInformation', 'SessionInitializationBehavior', 'TypedConnection', 'TypedConnectionWithMultiplexer', 'TypedMultiplexerSessionInformation', 'TypedSessionInformation']`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/scripts/generate_grpc_stubs.py -->
## PYTHON MODULE: packages/service/scripts/generate_grpc_stubs.py

### MODULE DOCSTRING

Generates gRPC Python stubs from proto files.

- `PROTO_PATH = pathlib.Path(__file__).parent.parent.parent.parent / 'third_party' / 'ni-apis'`

- `TEST_STUBS_PATH = pathlib.Path(__file__).parent.parent / 'tests' / 'utilities' / 'stubs'`

- `TEST_PROTO_PATH = TEST_STUBS_PATH`

- `TEST_PROTO_FILES = list(TEST_PROTO_PATH.rglob('*.proto'))`

### `def main()`

Generate test gRPC Python stubs.

### `def is_relative_to(path: pathlib.PurePath, other: pathlib.PurePath) -> bool`

Return whether or not this path is relative to the other path.

### `def generate_python_files(stubs_path: pathlib.Path, proto_path: pathlib.Path, proto_files: Sequence[pathlib.Path], alternate_proto_path: pathlib.Path='')`

Generate python files from .proto files with protoc.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/scripts/install_examples.py -->
## PYTHON MODULE: packages/service/scripts/install_examples.py

### MODULE DOCSTRING

Install all example services.

- `ROOT_DIR = pathlib.Path(__file__).parent.parent.parent.parent`

- `EXAMPLES_PATH = ROOT_DIR / 'examples'`

- `SERVICES_PATH = pathlib.Path(os.environ['ProgramData']) / 'National Instruments' / 'Plug-Ins' / 'Measurements'`

### `def main()`

Install all example services.

### `def _get_clean_env()`

Get a clean environment with no venv activated.

    This is a workaround for https://github.com/python-poetry/poetry/issues/4055
    Option to force Poetry to create a virtual environment, even if a virtual env is active

    

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/__init__.py -->
## PYTHON MODULE: packages/service/tests/__init__.py

### MODULE DOCSTRING

Tests.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/__init__.py -->
## PYTHON MODULE: packages/service/tests/acceptance/__init__.py

### MODULE DOCSTRING

Acceptance tests.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/conftest.py -->
## PYTHON MODULE: packages/service/tests/acceptance/conftest.py

### MODULE DOCSTRING

Pytest configuration file for acceptance tests.

### `def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path`

Test fixture that returns the pin map directory.

### `def filter_wrong_configurations_message_type_warnings() -> Generator`

Test fixture to filter out WrongMessageTypeWarning warnings for Configurations messages.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_logging.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_logging.py

### `def test___discovery_client___call___client_call_logged(caplog: LogCaptureFixture, discovery_client: DiscoveryClient) -> None`

### `def test___pin_map_client___call___client_call_logged(caplog: LogCaptureFixture, pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> None`

### `def test___session_management_client___call___client_call_logged(caplog: LogCaptureFixture, request: FixtureRequest) -> None`

### `def test___loopback_measurement___get_metadata___server_call_logged(caplog: LogCaptureFixture, request: FixtureRequest) -> None`

### `def test___streaming_data_measurement___measure___server_call_logged(caplog: LogCaptureFixture, request: FixtureRequest) -> None`

### `def measurement_service(request: FixtureRequest) -> MeasurementService`

### `def loopback_measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates a loopback measurement.

### `def streaming_data_measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates a loopback measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_measurement_service.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_measurement_service.py

### MODULE DOCSTRING

Tests to validate measurement service. Uses the Sample Measurement Example.

- `EXPECTED_PARAMETER_COUNT = 7`

- `EXPECTED_UI_FILE_COUNT = 1`

### `class Color(Enum)`

Primary colors used for example enum-typed config and output.

### `def test___measurement_service_v1___get_metadata___returns_metadata(stub_v1: v1_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___measurement_service_v2___get_metadata___returns_metadata(stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___measurement_service_v1___measure___returns_output(float_in: float, double_array_in: list[float], bool_in: bool, string_in: str, enum_in: Enum, protobuf_enum_in: ProtobufColor.ValueType, string_array_in: list[str], stub_v1: v1_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___measurement_service_v2___measure___returns_output(float_in: float, double_array_in: list[float], bool_in: bool, string_in: str, enum_in: Enum, protobuf_enum_in: ProtobufColor.ValueType, string_array_in: list[str], stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___measurement_service_v1___measure_with_large_array___returns_output(double_array_len: int, stub_v1: v1_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___measurement_service_v2___measure_with_large_array___returns_output(double_array_len: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def measurement_service(discovery_service_process) -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def _get_configuration_parameters(*args, message_type: str='', **kwargs) -> any_pb2.Any`

### `def _get_serialized_measurement_signature(float_in: float, double_array_in: list[float], bool_in: bool, string_in: str, enum_in: Enum, protobuf_enum_in: ProtobufColor.ValueType, string_array_in: list[str]) -> bytes`

### `def _validate_get_metadata_response(get_metadata_response: v1_measurement_service_pb2.GetMetadataResponse | v2_measurement_service_pb2.GetMetadataResponse)`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidaqmx_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_nidaqmx_measurement.py

- `_SITE = 0`

### `def test___single_session___measure___returns_measured_values(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___single_session___measure___creates_single_session(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidcpower_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_nidcpower_measurement.py

- `_SITE = 0`

### `def test___single_session___measure___returns_measured_values(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___single_session___measure___creates_single_session(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidigital_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_nidigital_measurement.py

### `def test___single_session___measure___returns_measured_values(pin_map_id: str, stub_v2: MeasurementServiceStub) -> None`

### `def test___single_session___measure___creates_single_session(pin_map_id: str, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_id: str, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_id(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> str`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidmm_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_nidmm_measurement.py

- `_SITE = 0`

### `def test___single_session___measure___returns_measured_values(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___single_session___measure___creates_single_session(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nifgen_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_nifgen_measurement.py

- `_SITE = 0`

### `def test___single_session___measure___creates_single_session(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_niscope_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_niscope_measurement.py

- `_SITE = 0`

### `def test___single_session___measure___returns_measured_values(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___single_session___measure___creates_single_session(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_niswitch_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_niswitch_measurement.py

- `_SITE = 0`

### `def test___single_session___measure___creates_single_session(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_niswitch_multiplexer_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_niswitch_multiplexer_measurement.py

- `_SITE = 0`

### `def test___single_session___measure___creates_single_session(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def test___multiple_sessions___measure___creates_multiple_sessions(pin_map_context: PinMapContext, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service() -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

### `class _MeasurementOutput(NamedTuple)`

### `def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_security.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_security.py

### `def test___loopback_measurement___listening_on_loopback_interface(measurement_service: MeasurementService)`

### `def measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a measurement service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_session_management.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_session_management.py

### `def test___pin_map_context___measure___sends_pin_map_id_and_sites(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, stub_v2: MeasurementServiceStub) -> None`

### `class Configuration(NamedTuple)`

A group of shared test parameters.

- `_FGEN_SINGLE_SESSION_CONFIGURATIONS = [Configuration('1Fgen1Pin1Site.pinmap', ['Pin1'], [0], ['FGEN1'], ['FGEN1'], ['0'], expected_session_names2=['niFGen-FGEN1']), Configuration('2Fgen2Pin2Site.pinmap', ['Pin1'], [0], ['FGEN1'], ['FGEN1'], ['0'], expected_session_names2=['niFGen-FGEN1']), Configuration('2Fgen2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0], ['FGEN1'], ['FGEN1'], ['0, 1'], expected_session_names2=['niFGen-FGEN1']), Configuration('2Fgen2Pin2Site.pinmap', ['Pin1', 'Pin2'], [1], ['FGEN2'], ['FGEN2'], ['0, 1'], expected_session_names2=['niFGen-FGEN2'])]`

- `_FGEN_MULTI_SESSION_CONFIGURATIONS = [Configuration('2Fgen2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0, 1], ['FGEN1', 'FGEN2'], ['FGEN1', 'FGEN2'], ['0, 1', '0, 1'], expected_session_names2=['niFGen-FGEN1', 'niFGen-FGEN2'])]`

- `_SMU_SINGLE_SESSION_CONFIGURATIONS = [Configuration('1Smu1ChannelGroup1Pin1Site.pinmap', ['Pin1'], [0], ['DCPower1/0'], ['DCPower1/0'], ['DCPower1/0'], expected_session_names2=['niDCPower-DCPower1/0']), Configuration('1Smu1ChannelGroup2Pin2Site.pinmap', ['Pin1'], [0], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3']), Configuration('1Smu1ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3']), Configuration('1Smu1ChannelGroup2Pin2Site.pinmap', ['Pin1'], [0, 1], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/2'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3']), Configuration('1Smu1ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0, 1], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3']), Configuration('1Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1'], [0], ['DCPower1/0, DCPower1/1'], ['DCPower1/0, DCPower1/1'], ['DCPower1/0'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1']), Configuration('1Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0], ['DCPower1/0, DCPower1/1'], ['DCPower1/0, DCPower1/1'], ['DCPower1/0, DCPower1/1'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1']), Configuration('1Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [1], ['DCPower1/2, DCPower1/3'], ['DCPower1/2, DCPower1/3'], ['DCPower1/2, DCPower1/3'], expected_session_names2=['niDCPower-DCPower1/2, DCPower1/3']), Configuration('2Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1'], [0], ['DCPower1/0, DCPower1/1'], ['DCPower1/0, DCPower1/1'], ['DCPower1/0'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1']), Configuration('2Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0], ['DCPower1/0, DCPower1/1'], ['DCPower1/0, DCPower1/1'], ['DCPower1/0, DCPower1/1'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1']), Configuration('2Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [1], ['DCPower2/0, DCPower2/1'], ['DCPower2/0, DCPower2/1'], ['DCPower2/0, DCPower2/1'], expected_session_names2=['niDCPower-DCPower2/0, DCPower2/1'])]`

- `_SMU_MULTI_SESSION_CONFIGURATIONS = [Configuration('1Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0, 1], ['DCPower1/0, DCPower1/1', 'DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1', 'DCPower1/2, DCPower1/3'], ['DCPower1/0, DCPower1/1', 'DCPower1/2, DCPower1/3'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1', 'niDCPower-DCPower1/2, DCPower1/3']), Configuration('2Smu2ChannelGroup2Pin2Site.pinmap', ['Pin1', 'Pin2'], [0, 1], ['DCPower1/0, DCPower1/1', 'DCPower2/0, DCPower2/1'], ['DCPower1/0, DCPower1/1', 'DCPower2/0, DCPower2/1'], ['DCPower1/0, DCPower1/1', 'DCPower2/0, DCPower2/1'], expected_session_names2=['niDCPower-DCPower1/0, DCPower1/1', 'niDCPower-DCPower2/0, DCPower2/1'])]`

### `def test___single_session___measure___reserves_single_session(configuration: Configuration, pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, stub_v2: MeasurementServiceStub) -> None`

### `def test___multi_session___measure___reserves_multiple_sessions(configuration: Configuration, pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, stub_v2: MeasurementServiceStub) -> None`

### `def test___multi_session_but_expecting_single_session___measure___raises_too_many_sessions_error(configuration: Configuration, pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, stub_v2: MeasurementServiceStub) -> None`

### `def _measure(stub_v2: MeasurementServiceStub, pin_map_context: PinMapContext, configurations: Configurations) -> Outputs`

### `def measurement_service(discovery_service_process: DiscoveryServiceProcess) -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_streaming_data_measurement.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_streaming_data_measurement.py

### MODULE DOCSTRING

Tests to validate a v2 measurement service that streams data.

### `def test___streaming_measurement_service___request_number_of_responses___receives_responses(num_responses: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___streaming_measurement_service___request_data_cumulatively___receives_expected_amount_of_data(data_size: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___streaming_measurement_service___specify_data_size___receives_expected_amount_of_data(data_size: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def test___streaming_measurement_service___specify_error_index___errors_at_expected_response(error_on_index: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def _get_configuration_parameters(*args, message_type: str='', **kwargs) -> any_pb2.Any`

### `def _get_serialized_measurement_configuration_parameters(name: str='test', num_responses: int=10, data_size: int=1, cumulative_data: bool=True, response_interval_in_ms: int=1, error_on_index: int=-1) -> bytes`

### `def _get_serialized_measurement_outputs(name: str, index: int, data: list[int]) -> bytes`

### `def measurement_service(discovery_service_process) -> Generator[MeasurementService]`

Test fixture that creates and hosts a measurement service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/acceptance/test_yield_vs_return.py -->
## PYTHON MODULE: packages/service/tests/acceptance/test_yield_vs_return.py

### MODULE DOCSTRING

Tests to validate that yield and return are both supported in v2 measurements.

### `def test___measurement_utilizing_yield_and_return___call_measurement___receives_responses_from_yield_and_return(stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub)`

### `def _get_configuration_parameters(*args, message_type: str='', **kwargs) -> any_pb2.Any`

### `def _get_serialized_measurement_configuration_parameters(time_in_seconds: float=1.0) -> bytes`

### `def measurement_service(discovery_service_process) -> Generator[MeasurementService, None, None]`

Test fixture that creates and hosts a measurement service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/assets/__init__.py -->
## PYTHON MODULE: packages/service/tests/assets/__init__.py

### MODULE DOCSTRING

Contains test assets.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/conftest.py -->
## PYTHON MODULE: packages/service/tests/conftest.py

### MODULE DOCSTRING

Pytest configuration file.

### `def test_assets_directory() -> pathlib.Path`

Gets path to test_assets directory.

### `def grpc_channel(measurement_service: MeasurementService) -> Generator[grpc.Channel]`

Test fixture that creates a gRPC channel.

### `def stub_v1(grpc_channel: grpc.Channel) -> v1_measurement_service_pb2_grpc.MeasurementServiceStub`

Test fixture that creates a MeasurementService v1 stub.

### `def stub_v2(grpc_channel: grpc.Channel) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub`

Test fixture that creates a MeasurementService v2 stub.

### `def discovery_service_process() -> Generator[DiscoveryServiceProcess]`

Test fixture that creates discovery service process.

### `def grpc_channel_pool() -> Generator[GrpcChannelPool]`

Test fixture that creates a gRPC channel pool.

### `def discovery_client(discovery_service_process: DiscoveryServiceProcess, grpc_channel_pool: GrpcChannelPool) -> DiscoveryClient`

Test fixture that creates a discovery client.

### `def pin_map_client(discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool) -> PinMapClient`

Test fixture that creates a pin map client.

### `def session_management_client(discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool) -> SessionManagementClient`

Test fixture that creates a session management client.

### `def feature_toggles(monkeypatch: pytest.MonkeyPatch, request: pytest.FixtureRequest) -> None`

Test fixture that disables or enables feature toggles.

### `def pytest_collection_modifyitems(items: list[pytest.Item]) -> None`

Hook to inject fixtures based on marks.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/__init__.py -->
## PYTHON MODULE: packages/service/tests/integration/__init__.py

### MODULE DOCSTRING

Integration tests.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/__init__.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/__init__.py

### MODULE DOCSTRING

Integration tests for driver-specific session management APIs.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/conftest.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/conftest.py

### MODULE DOCSTRING

Pytest configuration file for integration tests.

### `def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path`

Test fixture that returns the pin map directory.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidaqmx_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_nidaqmx_reservation.py

- `_SITE = 0`

### `def test___single_session_reserved___create_nidaqmx_task___creates_task(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___multiple_sessions_reserved___create_nidaqmx_tasks___creates_tasks(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___task_created___get_nidaqmx_connection___returns_connection(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___tasks_created___get_nidaqmx_connections___returns_connections(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidcpower_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_nidcpower_reservation.py

- `_SITE = 0`

### `def test___single_session_reserved___initialize_nidcpower_session___creates_single_session(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___multiple_sessions_reserved___initialize_nidcpower_sessions___creates_multiple_sessions(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___session_created___get_nidcpower_connection___returns_connection(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_created___get_nidcpower_connections___returns_connections(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidigital_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_nidigital_reservation.py

### `def test___single_session_reserved___initialize_nidigital_session___creates_single_session(pin_map_id: str, session_management_client: SessionManagementClient) -> None`

### `def test___multiple_sessions_reserved___initialize_nidigital_sessions___creates_multiple_sessions(pin_map_id: str, session_management_client: SessionManagementClient) -> None`

### `def test___session_created___get_nidigital_connection___returns_connection(pin_map_id: str, session_management_client: SessionManagementClient) -> None`

### `def test___session_created___get_nidigital_connections___returns_connections(pin_map_id: str, session_management_client: SessionManagementClient) -> None`

### `def pin_map_id(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> str`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidmm_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_nidmm_reservation.py

- `_SITE = 0`

### `def test___single_session_reserved___initialize_nidmm_session___creates_single_session(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___multiple_sessions_reserved___initialize_nidmm_sessions___creates_multiple_sessions(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___session_created___get_nidmm_connection___returns_connection(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_created___get_nidmm_connections___returns_connections(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nifgen_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_nifgen_reservation.py

- `_SITE = 0`

### `def test___single_session_reserved___initialize_nifgen_session___creates_single_session(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___multiple_sessions_reserved___initialize_nifgen_sessions___creates_multiple_sessions(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___session_created___get_nifgen_connection___returns_connection(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_created___get_nifgen_connections___returns_connections(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_niscope_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_niscope_reservation.py

- `_SITE = 0`

### `def test___single_session_reserved___initialize_niscope_session___creates_single_session(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___multiple_sessions_reserved___initialize_niscope_sessions___creates_multiple_sessions(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___session_created___get_niscope_connection___returns_connection(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_created___get_niscope_connections___returns_connections(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_niswitch_multiplexer_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_niswitch_multiplexer_reservation.py

- `_SITE = 0`

### `def test___reserved_single_session_with_single_multiplexer___initialize_niswitch_multiplexer_session___creates_single_multiplexer_session(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___reserved_sessions_with_multiple_multiplexer___initialize_niswitch_multiplexer_sessions___creates_multiple_multiplexer_sessions(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___created_single_session___get_nidcpower_connection_with_multiplexer___returns_connection_with_multiplexer_session(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___created_multiple_sessions___get_nidcpower_connections_with_multiplexer___returns_connections_with_multiplexer_sessions(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_niswitch_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_niswitch_reservation.py

- `_SITE = 0`

### `def test___single_session_reserved___initialize_niswitch_session___creates_single_session(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___multiple_sessions_reserved___initialize_niswitch_sessions___creates_multiple_sessions(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___session_created___get_niswitch_connection___returns_connection(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_created___get_niswitch_connections___returns_connections(pin_map_context: PinMapContext, session_management_client: SessionManagementClient) -> None`

### `def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_reservation.py -->
## PYTHON MODULE: packages/service/tests/integration/session_management/test_reservation.py

- `_PIN_MAP_A = 'PinMapA_3Instruments_3DutPins_2SystemPins_2Sites.pinmap'`

- `_PIN_MAP_A_PIN_NAMES = ['A', 'B', 'C', 'S1', 'S2']`

- `_PIN_MAP_B = 'PinMapB_3Instruments_3DutPins_2SystemPins_2Sites_SharedPins.pinmap'`

- `_PIN_MAP_B_PIN_NAMES = ['A', 'B', 'C', 'S1', 'S2']`

- `_PIN_MAP_C = 'PinMapC_MultipleInstrumentsPinsRelaysAndSites.pinmap'`

- `_PIN_MAP_C_PIN_NAMES = ['A', 'B', 'C', 'S1', 'S2']`

- `_PIN_MAP_C_RELAY_NAMES = ['RelayUsingDifferentDrivers', 'RelayUsingSameDriver', 'SystemRelay']`

- `_PIN_MAP_C_PIN_OR_RELAY_NAMES = _PIN_MAP_C_PIN_NAMES + _PIN_MAP_C_RELAY_NAMES`

- `_PIN_MAP_D = 'PinMapD_3Instruments_4DutPins_2Sites_2Multiplexers.pinmap'`

- `_PIN_MAP_D_PIN_NAMES = ['A', 'B', 'C', 'D']`

### `def test___sessions_reserved___get_connections___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved___get_connections_by_pin___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved___get_connections_by_site___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved___get_connections_by_instrument_type___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_using_pin_group___get_connections_by_pins___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_using_nested_pin_group___get_connections_by_pins___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_using_relay_group___get_connections_by_relays___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_using_nested_relay_group___get_connections_by_relays___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved___get_connections_by_pin_group___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved___get_connections_by_nested_pin_group___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved___get_connections_by_relay_group___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved___get_connections_by_nested_relay_groups___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___reserve_sessions_with_multiplexer___get_connections_with_multiplexer___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___reserve_sessions_with_multiplexer___get_connections_with_multiplexer_by_pin___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___reserve_sessions_with_multiplexer___get_connections_with_multiplexer_by_site___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___reserve_session_with_multiplexer___get_connections_with_multiplexer_by_instrument_type___returns_connections(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_with_shared_pins_all_sites___get_connections___returns_connections_for_all_sites(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_with_shared_pins_site0___get_connections___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_with_shared_pins_site1___get_connections___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_with_relays___get_connections_for_relay_driver___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

### `def test___sessions_reserved_with_relays___get_connections_for_relay_driver_by_site___connections_returned(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path, session_management_client: SessionManagementClient) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/integration/test_service_manager.py -->
## PYTHON MODULE: packages/service/tests/integration/test_service_manager.py

### MODULE DOCSTRING

Contains test to validate service_manager.py.

### `def test___grpc_service___start_service___service_hosted(grpc_service: GrpcService)`

### `def test___grpc_service_without_discovery_service___start_service___service_hosted(grpc_service: GrpcService)`

### `def test___grpc_service___start_service_error_registering_measurement___raises_error(grpc_service: GrpcService)`

### `def test___grpc_service_started___stop_service___service_stopped(grpc_service: GrpcService)`

### `def test___grpc_service_v2_only___start_service_and_check_v1___raises_error(grpc_service: GrpcService)`

### `def test___grpc_service_v1_only___start_service_and_check_v1___service_hosted(grpc_service: GrpcService)`

### `def test___grpc_service_unknown_interface___start_service_and_check_v1___raises_error(grpc_service: GrpcService)`

### `def grpc_service(discovery_client: DiscoveryClient) -> GrpcService`

Create a GrpcService.

### `def discovery_client(discovery_service_stub: FakeDiscoveryServiceStub) -> DiscoveryClient`

Create a DiscoveryClient.

### `def discovery_service_stub(expect_discovery_service_error_stub: bool) -> FakeDiscoveryServiceStub`

Create a valid/error stub based on expect_discovery_service_error_stub value.

### `def expect_discovery_service_error_stub() -> bool`

Boolean to choose between FakeDiscoveryServiceStub and FakeDiscoveryServiceStubError.

### `def _validate_if_service_running_by_making_rpc(port_number)`

Implicit validation of running service.

    Throws exception during RPC if service not hosted.
    

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/__init__.py -->
## PYTHON MODULE: packages/service/tests/unit/__init__.py

### MODULE DOCSTRING

Unit tests.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/__init__.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/__init__.py

### MODULE DOCSTRING

Unit tests for ni_measurement_plugin_sdk_service._drivers.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/_driver_utils.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/_driver_utils.py

### MODULE DOCSTRING

Driver-related unit test utilities.

### `def create_mock_session(session_type: type[TSession]) -> Mock`

Create a single mock session object.

### `def create_mock_sessions(session_type: type[TSession], count: int) -> list[Mock]`

Create multiple mock session objects.

### `def set_simulation_options(driver_name: str, mocker: MockerFixture, simulate: bool, board_type: str, model: str) -> None`

Set simulation options for the specified driver.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_grpcdevice.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_grpcdevice.py

### `def test___default_configuration___get_grpc_device_server_location___resolves_service_and_returns_discovered_location(discovery_client: Mock) -> None`

### `def test___use_grpc_device_server_false___get_grpc_device_server_location___returns_empty_string(discovery_client: Mock, mocker: MockerFixture) -> None`

### `def test___grpc_device_server_address_set___get_grpc_device_server_location___returns_configured_address(discovery_client: Mock, mocker: MockerFixture, grpc_device_server_address: str, expected_location: ServiceLocation) -> None`

### `def test___grpc_device_server_address_unsupported___get_grpc_device_server_location___raises_value_error(discovery_client: Mock, mocker: MockerFixture, grpc_device_server_address: str, expected_message: str) -> None`

### `def test___default_configuration___get_insecure_grpc_device_server_channel___resolves_service_and_returns_channel_with_configured_address(discovery_client: Mock, grpc_channel: Mock, grpc_channel_pool: Mock) -> None`

### `def test___use_grpc_device_server_false___get_insecure_grpc_device_server_channel___returns_none(discovery_client: Mock, grpc_channel_pool: Mock, mocker: MockerFixture) -> None`

### `def test___grpc_device_server_address_set___get_insecure_grpc_device_server_channel___returns_channel_with_configured_address(discovery_client: Mock, grpc_channel: Mock, grpc_channel_pool: Mock, mocker: MockerFixture) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidaqmx.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_nidaqmx.py

### `def test___single_session_info___create_nidaqmx_task___task_created(task_new: Mock, session_management_client: Mock) -> None`

### `def test___multiple_session_infos___create_nidaqmx_tasks___tasks_created(task_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args___create_nidaqmx_task___optional_args_passed(task_new: Mock, session_management_client: Mock) -> None`

### `def test___task_created___get_nidaqmx_connection___connection_returned(kwargs: dict[str, Any], expected_channel_name: str, expected_session_index: int, task_new: Mock, session_management_client: Mock) -> None`

### `def test___task_created___get_nidaqmx_connections___connections_returned(kwargs: dict[str, Any], expected_channel_names: list[str], expected_session_indices: list[int], task_new: Mock, session_management_client: Mock) -> None`

### `def task_new(mocker: MockerFixture) -> Mock`

A test fixture that patches the Task class's __new__ method.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidcpower.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_nidcpower.py

### `def test___single_session_info___initialize_nidcpower_session___session_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_nidcpower_sessions___sessions_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args___initialize_nidcpower_session___optional_args_passed(session_new: Mock, session_management_client: Mock) -> None`

### `def test___simulation_configured___initialize_nidcpower_session___simulation_options_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args_and_simulation_configured___initialize_nidcpower_session___optional_args_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nidcpower_connection___connection_returned(kwargs: dict[str, Any], expected_channel_name: str, expected_session_index: int, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nidcpower_connections___connections_returned(kwargs: dict[str, Any], expected_channel_names: list[str], expected_session_indices: list[int], session_new: Mock, session_management_client: Mock) -> None`

### `def session_new(mocker: MockerFixture) -> Mock`

A test fixture that patches the Session class's __new__ method.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidigital.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_nidigital.py

### `def test___single_session_info___initialize_nidigital_session___session_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_nidigital_sessions___sessions_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args___initialize_nidigital_session___optional_args_passed(session_new: Mock, session_management_client: Mock) -> None`

### `def test___simulation_configured___initialize_nidigital_session___simulation_options_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args_and_simulation_configured___initialize_nidigital_session___optional_args_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nidigital_connection___connection_returned(kwargs: dict[str, Any], expected_channel_name: str, expected_session_index: int, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nidigital_connections___connections_returned(kwargs: dict[str, Any], expected_channel_names: list[str], expected_session_indices: list[int], session_new: Mock, session_management_client: Mock) -> None`

### `def session_new(mocker: MockerFixture) -> Mock`

A test fixture that patches the Session class's __new__ method.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidmm.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_nidmm.py

### `def test___single_session_info___initialize_nidmm_session___session_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_nidmm_sessions___sessions_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args___initialize_nidmm_session___optional_args_passed(session_new: Mock, session_management_client: Mock) -> None`

### `def test___simulation_configured___initialize_nidmm_session___simulation_options_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args_and_simulation_configured___initialize_nidmm_session___optional_args_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nidmm_connection___connection_returned(kwargs: dict[str, Any], expected_channel_name: str, expected_session_index: int, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nidmm_connections___connections_returned(kwargs: dict[str, Any], expected_channel_names: list[str], expected_session_indices: list[int], session_new: Mock, session_management_client: Mock) -> None`

### `def session_new(mocker: MockerFixture) -> Mock`

A test fixture that patches the Session class's __new__ method.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nifgen.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_nifgen.py

### `def test___single_session_info___initialize_nifgen_session___session_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_nifgen_sessions___sessions_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args___initialize_nifgen_session___optional_args_passed(session_new: Mock, session_management_client: Mock) -> None`

### `def test___simulation_configured___initialize_nifgen_session___simulation_options_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args_and_simulation_configured___initialize_nifgen_session___optional_args_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nifgen_connection___connection_returned(kwargs: dict[str, Any], expected_channel_name: str, expected_session_index: int, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_nifgen_connections___connections_returned(kwargs: dict[str, Any], expected_channel_names: list[str], expected_session_indices: list[int], session_new: Mock, session_management_client: Mock) -> None`

### `def session_new(mocker: MockerFixture) -> Mock`

A test fixture that patches the Session class's __new__ method.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_niscope.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_niscope.py

### `def test___single_session_info___initialize_niscope_session___session_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_niscope_sessions___sessions_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args___initialize_niscope_session___optional_args_passed(session_new: Mock, session_management_client: Mock) -> None`

### `def test___simulation_configured___initialize_niscope_session___simulation_options_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args_and_simulation_configured___initialize_niscope_session___optional_args_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_niscope_connection___connection_returned(kwargs: dict[str, Any], expected_channel_name: str, expected_session_index: int, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_niscope_connections___connections_returned(kwargs: dict[str, Any], expected_channel_names: list[str], expected_session_indices: list[int], session_new: Mock, session_management_client: Mock) -> None`

### `def session_new(mocker: MockerFixture) -> Mock`

A test fixture that patches the Session class's __new__ method.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_niswitch.py -->
## PYTHON MODULE: packages/service/tests/unit/_drivers/test_niswitch.py

### `def test___single_session_info___initialize_niswitch_session___session_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_niswitch_sessions___sessions_created(session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args___initialize_niswitch_session___optional_args_passed(simulate: bool, expected_resource_name: str, session_new: Mock, session_management_client: Mock) -> None`

### `def test___simulation_configured___initialize_niswitch_session___simulation_options_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___optional_args_and_simulation_configured___initialize_niswitch_session___optional_args_passed(mocker: MockerFixture, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_niswitch_connection___connection_returned(kwargs: dict[str, Any], expected_channel_name: str, expected_session_index: int, session_new: Mock, session_management_client: Mock) -> None`

### `def test___session_created___get_niswitch_connections___connections_returned(kwargs: dict[str, Any], expected_channel_names: list[str], expected_session_indices: list[int], session_new: Mock, session_management_client: Mock) -> None`

### `def session_new(mocker: MockerFixture) -> Mock`

A test fixture that patches the Session class's __new__ method.

### `def _set_niswitch_simulation_options(mocker: MockerFixture, simulate: bool, topology: str) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/_reservation_utils.py -->
## PYTHON MODULE: packages/service/tests/unit/_reservation_utils.py

### MODULE DOCSTRING

Reservation-related unit test utilities.

### `def create_grpc_session_infos(instrument_type_id: str, session_count: int) -> list[session_management_service_pb2.SessionInformation]`

Create a list of gRPC SessionInformation messages.

### `def create_grpc_multiplexer_session_infos(multiplexer_type_id: str, session_count: int) -> list[session_management_service_pb2.MultiplexerSessionInformation]`

Create a list of gRPC MultiplexerSessionInformation messages.

### `def construct_session(session_info: SessionInformation) -> fake_driver.Session`

Constructs a session object.

### `def construct_multiplexer_session(session_info: MultiplexerSessionInformation) -> fake_multiplexer_driver.Session`

Constructs a multiplexer session object.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/conftest.py -->
## PYTHON MODULE: packages/service/tests/unit/conftest.py

### MODULE DOCSTRING

Test fixtures for unit tests.

### `def discovery_client(mocker: MockerFixture) -> Mock`

Test fixture that creates a mock DiscoveryClient.

### `def grpc_channel(mocker: MockerFixture) -> Mock`

Test fixture that creates a mock grpc.Channel.

### `def grpc_channel_pool(mocker: MockerFixture) -> Mock`

Test fixture that creates a mock GrpcChannelPool.

### `def measurement_service_context(mocker: MockerFixture, measurement_service: Mock) -> Generator[Mock]`

Test fixture that creates and registers a mock MeasurementServiceContext.

### `def measurement_service(mocker: MockerFixture, discovery_client: Mock, grpc_channel_pool: Mock, session_management_client: Mock) -> Mock`

Test fixture that creates a mock MeasurementService.

### `def multi_session_reservation(mocker: MockerFixture) -> Mock`

Test fixture that creates a mock MultiSessionReservation.

### `def session_management_client(discovery_client: Mock, grpc_channel_pool: Mock, mocker: MockerFixture, multi_session_reservation: Mock, single_session_reservation: Mock) -> Mock`

Test fixture that creates a mock SessionManagementClient.

### `def single_session_reservation(mocker: MockerFixture) -> Mock`

Test fixture that creates a mock SingleSessionReservation.

### `def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path`

Test fixture that returns the pin map directory.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/grpc/__init__.py -->
## PYTHON MODULE: packages/service/tests/unit/grpc/__init__.py

### MODULE DOCSTRING

Unit tests for ni_measurement_plugin_sdk_service.grpc.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/grpc/channelpool/__init__.py -->
## PYTHON MODULE: packages/service/tests/unit/grpc/channelpool/__init__.py

### MODULE DOCSTRING

Unit tests for ni_measurement_plugin_sdk_service.grpc.channelpool.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/grpc/channelpool/test_channel_pool.py -->
## PYTHON MODULE: packages/service/tests/unit/grpc/channelpool/test_channel_pool.py

### `def test___channel_pool___is_local___returns_expected_result(target: str, expected_result: bool) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/unit/measurement/__init__.py

### MODULE DOCSTRING

Unit tests for ni_measurement_plugin_sdk_service.measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/measurement/service/__init__.py -->
## PYTHON MODULE: packages/service/tests/unit/measurement/service/__init__.py

### MODULE DOCSTRING

Unit tests for ni_measurement_plugin_sdk_service.measurement.service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/measurement/service/test_measurement_context.py -->
## PYTHON MODULE: packages/service/tests/unit/measurement/service/test_measurement_context.py

### `def test___single_pin___reserve_session___session_reserved(measurement_service_context: Mock, session_management_client: Mock, single_session_reservation: Mock) -> None`

### `def test___multiple_pins___reserve_session___session_reserved(measurement_service_context: Mock, session_management_client: Mock, single_session_reservation: Mock) -> None`

### `def test___no_pins___reserve_session___value_error_raised(no_pins: str | list[str] | None) -> None`

### `def test___timeout___reserve_session___timeout_specified(measurement_service_context: Mock, session_management_client: Mock) -> None`

### `def test___single_pin___reserve_sessions___session_reserved(measurement_service_context: Mock, session_management_client: Mock, multi_session_reservation: Mock) -> None`

### `def test___multiple_pins___reserve_sessions___session_reserved(measurement_service_context: Mock, session_management_client: Mock, multi_session_reservation: Mock) -> None`

### `def test___no_pins___reserve_sessions___value_error_raised(no_pins: str | list[str] | None) -> None`

### `def test___timeout___reserve_sessions___timeout_specified(measurement_service_context: Mock, session_management_client: Mock) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_array_utils.py -->
## PYTHON MODULE: packages/service/tests/unit/test_array_utils.py

### `def test___valid_double2darray___double2darray_to_ndarray___converts_data()`

### `def test___valid_ndarray___ndarray_to_double2darray___converts_data()`

### `def test___valid_list___list_to_double2darray___converts_data()`

### `def test___valid_double2darray___double2darray_to_list___converts_data()`

### `def test___valid_string2darray___string2darray_to_ndarray___converts_data()`

### `def test___valid_ndarray___ndarray_to_string2darray___converts_data()`

### `def test___valid_list___list_to_string2darray___converts_data()`

### `def test___valid_string2darray___string2darray_to_list___converts_data()`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_configuration.py -->
## PYTHON MODULE: packages/service/tests/unit/test_configuration.py

### `def test___mi_driver_options___update_from_config___reads_config(config: Mock) -> None`

### `def test___mi_driver_options___to_dict___returns_options_dict(options: MIDriverOptions, expected_dict: dict[str, Any]) -> None`

### `def test___niswitch_options___update_from_config___reads_config(config: Mock) -> None`

### `def config(mocker: MockerFixture) -> Mock`

Test fixture that creates a mock decouple config.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_decoder.py -->
## PYTHON MODULE: packages/service/tests/unit/test_decoder.py

### MODULE DOCSTRING

Contains tests to validate serializer.py.

### `class DifferentColor(Enum)`

Non-primary colors used for testing enum-typed config and output.

### `class Countries(IntEnum)`

Countries enum used for testing enum-typed config and output.

- `BIG_MESSAGE_SIZE = 100`

### `def test___serializer___deserialize_parameter___successful_deserialization(values)`

### `def test___empty_buffer___deserialize_parameters___returns_zero_or_empty()`

### `def test___big_message___deserialize_parameters___returns_parameter_value_by_id() -> None`

### `def _get_grpc_serialized_data(values)`

### `def _get_test_parameter_by_id(default_values)`

### `def _get_test_grpc_message(test_values)`

### `def _get_big_message_metadata_by_id() -> dict[int, ParameterMetadata]`

### `def _get_big_message(values: Sequence[float]) -> BigMessage`

### `def _test_create_file_descriptor(metadata: list[ParameterMetadata], file_name: str) -> str`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_default_value.py -->
## PYTHON MODULE: packages/service/tests/unit/test_default_value.py

### MODULE DOCSTRING

Contains tests to validate the serializationstrategy.py.

### `def test___get_default_value___returns_type_defaults(type, is_repeated, expected_default_value)`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_dotenvpath.py -->
## PYTHON MODULE: packages/service/tests/unit/test_dotenvpath.py

### `def test___dotenv_exists_varies___has_dotenv_file___matches_dotenv_exists(dotenv_exists: bool, tmp_path: Path) -> None`

### `def test___get_caller_path___returns_this_modules_path() -> None`

### `def test___get_package_path___returns_package_dir() -> None`

### `def test___get_script_or_exe_path___returns_pytest_path() -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_drivers.py -->
## PYTHON MODULE: packages/service/tests/unit/test_drivers.py

- `_INITIALIZATION_BEHAVIOR = {SessionInitializationBehavior.AUTO: FakeDriverSessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: FakeDriverSessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: FakeDriverSessionInitializationBehavior.ATTACH_TO_SERVER_SESSION, SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: FakeDriverSessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: FakeDriverSessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE}`

### `def test___initialization_behavior_close___with_closing_session_with_ts_code_module_support___session_closed(initialization_behavior: SessionInitializationBehavior) -> None`

### `def test___initialization_behavior_detach___with_closing_session_with_ts_code_module_support___session_detached(initialization_behavior: SessionInitializationBehavior) -> None`

### `def test___session_not_closable___with_closing_session_with_ts_code_module_support___raises_type_error(initialization_behavior: SessionInitializationBehavior) -> None`

### `def test___session_not_context_manager___with_closing_session_with_ts_code_module_support___raises_type_error(initialization_behavior: SessionInitializationBehavior) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_encoder.py -->
## PYTHON MODULE: packages/service/tests/unit/test_encoder.py

### MODULE DOCSTRING

Contains tests to validate serializer.py.

### `class DifferentColor(Enum)`

Non-primary colors used for testing enum-typed config and output.

### `class Countries(IntEnum)`

Countries enum used for testing enum-typed config and output.

- `BIG_MESSAGE_SIZE = 100`

### `def test___serializer___serialize_parameter___successful_serialization(test_values)`

### `def test___serializer___serialize_default_parameter___successful_serialization(default_values)`

### `def test___big_message___serialize_parameters___returns_serialized_data() -> None`

### `def test___serialize_parameter_multiple_times___returns_one_message_type(test_values)`

### `def _validate_serialized_bytes(custom_serialized_bytes, values)`

### `def _test_create_file_descriptor(metadata: list[metadata.ParameterMetadata], file_name: str) -> str`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_featuretoggles.py -->
## PYTHON MODULE: packages/service/tests/unit/test_featuretoggles.py

- `RELEASE_FEATURE = FeatureToggle('RELEASE_FEATURE', CodeReadiness.RELEASE)`

- `NEXT_RELEASE_FEATURE = FeatureToggle('NEXT_RELEASE_FEATURE', CodeReadiness.NEXT_RELEASE)`

- `INCOMPLETE_FEATURE = FeatureToggle('INCOMPLETE_FEATURE', CodeReadiness.INCOMPLETE)`

- `PROTOTYPE_FEATURE = FeatureToggle('PROTOTYPE_FEATURE', CodeReadiness.PROTOTYPE)`

### `def _prototype_function(x: int, y: str, z: list[int]) -> str`

### `def _prototype_function_impl(x: int, y: str, z: list[int]) -> str`

### `def test___default_code_readiness_level___get_code_readiness_level___equals_prototype() -> None`

### `def test___use_release_readiness___get_code_readiness_level___equals_release() -> None`

### `def test___use_next_release_readiness___get_code_readiness_level___equals_next_release() -> None`

### `def test___default_code_readiness_level___is_enabled___returns_true() -> None`

### `def test___use_incomplete_readiness___is_enabled___reflects_code_readiness_level() -> None`

### `def test___use_next_release_readiness___is_enabled___reflects_code_readiness_level() -> None`

### `def test___release_readiness_level___is_enabled___reflects_code_readiness_level() -> None`

### `def test___feature_toggle_enabled___is_enabled___returns_true() -> None`

### `def test___feature_toggle_disabled___is_enabled___returns_false() -> None`

### `def test___feature_toggle_enabled___call_decorated_function___impl_called(mocker: MockerFixture) -> None`

### `def test___feature_toggle_disabled___call_decorated_function___error_raised(mocker: MockerFixture) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_metadata.py -->
## PYTHON MODULE: packages/service/tests/unit/test_metadata.py

### MODULE DOCSTRING

Contains tests to validate metadata.py.

### `class Color(Enum)`

Primary colors used for testing enum-typed config and output.

### `class DifferentColor(Enum)`

Non-primary colors used for testing enum-typed config and output.

### `class Countries(IntEnum)`

Countries enum used for testing IntEnum-typed config and output.

### `def test___default_value_different_from_type___validate___raises_type_exception(type, default_value, annotations)`

### `def test___default_value_same_as_type___validate___raises_no_exception(type, default_value, annotations)`

### `def test___display_name_invalid_characters___validate___raises_value_exception(display_name)`

### `def test___display_name_valid_characters___validate___raises_no_exception(display_name)`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_pin_map_client.py -->
## PYTHON MODULE: packages/service/tests/unit/test_pin_map_client.py

### MODULE DOCSTRING

Contains tests to validate the pin_map_client.py.

### `def test___valid_pin_map_file___register_pin_map___returns_pin_map_id(pin_map_client: PinMapClient, pin_map_stub: Mock, pin_map_directory: pathlib.Path) -> None`

### `def test___invalid_pin_map_file_path___register_pin_map___raises_file_not_found_error(pin_map_client: PinMapClient) -> None`

### `def _get_pin_map_file_contents(pin_map_path: str) -> str`

### `def pin_map_client(discovery_client: Mock, grpc_channel_pool: Mock, mocker: MockerFixture, pin_map_stub: Mock) -> PinMapClient`

Create a Client with a mock PinMapServiceStub.

### `def pin_map_stub(mocker: MockerFixture) -> Mock`

Create a mock PinMapServiceStub.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_reservation.py -->
## PYTHON MODULE: packages/service/tests/unit/test_reservation.py

### `def test___single_session_info___initialize_session___session_info_yielded(session_management_client: Mock) -> None`

### `def test___single_session_info___initialize_session___session_created(session_management_client: Mock) -> None`

### `def test___single_session_info___initialize_session___session_lifetime_tracked(session_management_client: Mock) -> None`

### `def test___empty_instrument_type_id___initialize_session___value_error_raised(session_management_client: Mock) -> None`

### `def test___no_session_infos___initialize_session___value_error_raised(session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_session___value_error_raised(session_management_client: Mock) -> None`

### `def test___session_already_exists___initialize_session___runtime_error_raised(session_management_client: Mock) -> None`

### `def test___heterogenous_session_infos___initialize_session___grouped_by_instrument_type(session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_sessions___session_infos_yielded(session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_sessions___sessions_created(session_management_client: Mock) -> None`

### `def test___multiple_session_infos___initialize_sessions___session_lifetime_tracked(session_management_client: Mock) -> None`

### `def test___empty_instrument_type_id___initialize_sessions___value_error_raised(session_management_client: Mock) -> None`

### `def test___no_session_infos___initialize_sessions___value_error_raised(session_management_client: Mock) -> None`

### `def test___session_already_exists___initialize_sessions___runtime_error_raised(session_management_client: Mock) -> None`

### `def test___heterogenous_session_infos___initialize_sessions___grouped_by_instrument_type(session_management_client: Mock) -> None`

### `def test___single_connection___get_connection___connection_returned(session_management_client: Mock) -> None`

### `def test___session_reserved_using_pin_group___get_connection_by_pin___returns_connection(session_management_client: Mock) -> None`

### `def test___duplicate_pins___get_connections___returns_single_connection(session_management_client: Mock) -> None`

### `def test___session_reserved___get_connections_by_pin_group___returns_connections(session_management_client: Mock) -> None`

### `def test___multiple_connections___get_connection___value_error_raised(session_management_client: Mock) -> None`

### `def test___invalid_argument_type___get_connection___type_error_raised(kwargs: dict[str, Any], expected_message: str, session_management_client: Mock) -> None`

### `def test___wrong_pins___get_connections___value_error_raised(session_management_client: Mock) -> None`

### `def test___wrong_sites___get_connections___value_error_raised(session_management_client: Mock) -> None`

### `def test___wrong_instrument_type_id___get_connections___value_error_raised(session_management_client: Mock) -> None`

### `def test___multiple_connections___get_connection_with_pin_name___connection_returned(session_management_client: Mock, pin_name: str, site: int, channel_name: str) -> None`

### `def test___multiple_connections___get_connection_with_site___connection_returned(session_management_client: Mock, pin_name: str, site: int, channel_name: str) -> None`

### `def test___heterogenous_session_infos___get_connection_with_instrument_type_id___connection_returned(session_management_client: Mock, instrument_type_id: str, pin_name: str, site: int, channel_name: str) -> None`

### `def test___heterogenous_session_infos___get_connections___connections_returned(session_management_client: Mock) -> None`

### `def test___heterogenous_session_infos___get_connections_with_partially_matching_criteria___value_error_raised(kwargs: dict[str, Any], expected_message: str, session_management_client: Mock) -> None`

### `def test___wrong_session_type___get_connection___type_error_raised(session_management_client: Mock) -> None`

### `def test___session_not_created___get_connection___type_error_raised(session_management_client: Mock) -> None`

### `def test___session_not_created___get_connection_with_session_type_object___connection_returned(session_management_client: Mock) -> None`

### `def test___no_connections___get_connection_with_session_type_object___value_error_raised(session_management_client: Mock) -> None`

### `def test___no_connections___get_connections_with_session_type_object___empty_list_returned(session_management_client: Mock) -> None`

### `def test___reservation_order___get_connections_with_specified_order___connections_returned_in_specified_order(session_management_client: Mock) -> None`

### `def test___reservation_order___get_connections___connections_returned_in_reservation_order(session_management_client: Mock) -> None`

### `def test___no_reservation_order___get_connections___connections_returned_in_default_order(session_management_client: Mock) -> None`

### `def test___system_pins___get_connections___system_pins_returned_in_default_order(session_management_client: Mock) -> None`

### `def test___system_pins___get_connections_by_site___system_pins_also_returned(session_management_client: Mock) -> None`

### `def test___system_pins___get_connection_with_system_pins_constant___only_system_pins_returned(session_management_client: Mock) -> None`

### `def test___system_pins___get_connection_with_site_list___system_pins_returned_in_specified_order(session_management_client: Mock) -> None`

### `def test___single_session_reserved___get_session_info___session_info_returned_with_null_session(session_management_client: Mock) -> None`

### `def test___single_session_created___get_session_info___session_info_returned_with_valid_session(session_management_client: Mock) -> None`

### `def test___multiple_sessions_reserved___get_session_info___session_info_returned_with_null_session(session_management_client: Mock) -> None`

### `def test___multiple_sessions_created___get_session_info___session_info_returned_with_valid_session(session_management_client: Mock) -> None`

### `def _create_grpc_session_infos_for_ordering() -> list[session_management_service_pb2.SessionInformation]`

### `def _create_grpc_session_infos_with_system_pins() -> list[session_management_service_pb2.SessionInformation]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_reservation_multiplexer.py -->
## PYTHON MODULE: packages/service/tests/unit/test_reservation_multiplexer.py

### `def test___invalid_argument_type___intialize_multiplexer_session___raises_type_error(kwargs: dict[str, Any], expected_message: str, session_management_client: Mock) -> None`

### `def test___single_multiplexer_session_info___initialize_multiplexer_session___yeilds_session_info(session_management_client: Mock) -> None`

### `def test___single_multiplexer_session_info___initialize_multiplexer_session___creates_session(session_management_client: Mock) -> None`

### `def test___single_multiplexer_session_info___initialize_multiplexer_session___session_lifetime_tracked(session_management_client: Mock) -> None`

### `def test___no_multiplexer_session_infos___initialize_multiplexer_session___raises_value_error(session_management_client: Mock) -> None`

### `def test___multiple_multiplexer_session_infos___initialize_multiplexer_session___raises_value_error(session_management_client: Mock) -> None`

### `def test___multiplexer_session_already_exists___initialize_multiplexer_session___raises_runtime_error(session_management_client: Mock) -> None`

### `def test___wrong_multiplexer_type_id___initialize_multiplexer_session___raises_value_error(session_management_client: Mock) -> None`

### `def test___multiple_multiplexer_session_infos___initialize_multiplexer_session_with_type_id___creates_session_for_specified_type_id(session_management_client: Mock) -> None`

### `def test___multiple_multiplexer_session_infos___initialize_multiplexer_sessions___yeilds_session_infos(session_management_client: Mock) -> None`

### `def test___multiple_multiplexer_session_infos___initialize_multiplexer_sessions___creates_sessions(session_management_client: Mock) -> None`

### `def test___multiple_multiplexer_session_infos___initialize_multiplexer_sessions___session_lifetime_tracked(session_management_client: Mock) -> None`

### `def test___no_multiplexer_session_infos___initialize_multiplexer_sessions___raises_value_error(session_management_client: Mock) -> None`

### `def test___session_already_exists___initialize_multiplexer_sessions___raises_runtime_error(session_management_client: Mock) -> None`

### `def test___heterogenous_multiplexer_session_infos___initialize_multiplexer_sessions___creates_all_sessions(session_management_client: Mock) -> None`

### `def test___heterogenous_multiplexer_session_infos___initialize_multiplexer_sessions_with_type_id___creates_sessions_for_specified_type_id(session_management_client: Mock) -> None`

### `def test___wrong_multiplexer_type_id___initialize_multiplexer_sessions___raises_value_error(session_management_client: Mock) -> None`

### `def test___single_connection___get_connection_with_multiplexer___returns_connection(session_management_client: Mock) -> None`

### `def test___multiple_connections___get_connection_with_multiplexer___raises_value_error(session_management_client: Mock) -> None`

### `def test___multiplexer_session_not_created___get_connection_with_multiplexer___raises_type_error(session_management_client: Mock) -> None`

### `def test___multiplexer_session_not_created___get_connection_with_multiplexer_using_object_type___returns_connection(session_management_client: Mock) -> None`

### `def test___no_connection___get_connection_with_multiplexer___raises_value_error(session_management_client: Mock) -> None`

### `def test___no_connections___get_connections_with_multiplexer_using_object_type___returns_empty_list(session_management_client: Mock) -> None`

### `def test___reservation_order___get_connections_with_multiplexer_in_specific_order___returns_connections_in_specified_order(session_management_client: Mock) -> None`

### `def test___reservation_order___get_connections_with_multiplexer___returns_connections_in_reservation_order(session_management_client: Mock) -> None`

### `def test___no_reservation_order___get_connections_with_multiplexer___returns_connections_in_default_order(session_management_client: Mock) -> None`

### `def test___partial_multiplexed_connections___get_connections_with_multiplexer_using_session_type___returns_all_specified_pin_connections(session_management_client: Mock) -> None`

### `def test____connection_with_no_multiplexers___get_connection_with_multiplexer___returns_connection(session_management_client: Mock) -> None`

### `def test____connections_with_no_multiplexers___get_connections_with_multiplexer___returns_all_connections(session_management_client: Mock) -> None`

### `def test___created_multiplexer_session___get_connection_with_multiplexer___returns_connection_with_multiplexer_session(session_management_client: Mock) -> None`

### `def test___created_multiplexer_sessions___get_connections_with_multiplexer___returns_connections_with_multiplexer_sessions(session_management_client: Mock) -> None`

### `def test___reserved_single_session_with_single_multiplexer___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(session_management_client: Mock) -> None`

### `def test___reserved_single_session_with_multiple_multiplexers___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(session_management_client: Mock) -> None`

### `def test___created_single_multiplexer_session___get_multiplexer_session_info___returns_multiplexer_session_info_with_valid_session(session_management_client: Mock) -> None`

### `def test___reserved_multiple_sessions_with_single_multiplexer___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(session_management_client: Mock) -> None`

### `def test___reserved_multiple_sessions_with_multiple_multiplexers___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(session_management_client: Mock) -> None`

### `def test___created_multiple_multiplexer_sessions___get_multiplexer_session_info___returns_multiplexer_session_info_with_valid_session(session_management_client: Mock) -> None`

### `def _create_grpc_session_and_multiplexer_session_infos_for_ordering() -> tuple[list[session_management_service_pb2.SessionInformation], list[session_management_service_pb2.MultiplexerSessionInformation]]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_service.py -->
## PYTHON MODULE: packages/service/tests/unit/test_service.py

### MODULE DOCSTRING

Tests to validated user facing decorators in service.py.

### `class Color(Enum)`

Primary colors used for testing enum-typed config and output.

### `class ColorWithoutZeroValue(Enum)`

Enum with missing zero value used for testing enum-typed config and output.

### `def test___measurement_service___register_measurement_method___method_registered(measurement_service: MeasurementService)`

Test to validate register_measurement decorator.

### `def test___measurement_service___add_configuration__configuration_added(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object)`

### `def test___measurement_service___add_pin_configuration__pin_configuration_added_with_deprecation_warning(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object, instrument_type: str)`

### `def test___measurement_service___add_ioresource_configuration__ioresource_configuration_added(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object, instrument_type: str)`

### `def test___measurement_service___add_non_pin_configuration__pin_type_annotations_not_added(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object)`

### `def test___measurement_service___add_non_ioresource_configuration__ioresource_type_annotations_not_added(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object)`

### `def test___measurement_service___add_path_configuration__path_configuration_added(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object)`

### `def test___measurement_service___add_non_path_configuration__path_type_annotations_not_added(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object)`

Test to validate the configuration decorator.

### `def test___measurement_service___add_configuration_with_mismatch_default_value__raises_type_error(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object)`

### `def test___measurement_service___add_output__output_added(measurement_service: MeasurementService, display_name: str, type: DataType)`

### `def _fake_measurement_function()`

### `def test___service_config___create_measurement_service___service_info_matches_service_config(test_assets_directory: pathlib.Path, service_config: str, display_name: str, version: str, provided_interfaces: list[str], provided_annotations: dict[str, str])`

### `def test___service_config___create_measurement_service_with_version___version_differs_from_service_config(test_assets_directory: pathlib.Path)`

### `def test___service_config___create_measurement_service_with_version___service_config_has_no_version(test_assets_directory: pathlib.Path)`

### `def test___service_config___create_measurement_service_with_version___version_is_used(test_assets_directory: pathlib.Path, service_config: str, version: str)`

### `def test___measurement_service___add_configuration_with_invalid_enum_type___raises_type_error(measurement_service: MeasurementService, display_name: str, type: DataType, default_value: object, enum_type: type[Enum])`

### `def test___measurement_service___host_service_with_grpc_service_not_started___raises_error(measurement_service: MeasurementService, mocker: MockerFixture)`

### `def measurement_service(test_assets_directory: pathlib.Path) -> MeasurementService`

Create a MeasurementService.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/unit/test_session_management.py -->
## PYTHON MODULE: packages/service/tests/unit/test_session_management.py

### `def test___all_optional_args___reserve_session___sends_request_with_args(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___no_optional_args___reserve_session___sends_request_with_defaults(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___explicit_none___reserve_session___sends_request_with_defaults(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___single_pin___reserve_session___sends_request_with_single_pin(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___infinite_timeout___reserve_session___sends_request_with_infinite_timeout(session_management_client: SessionManagementClient, session_management_stub: Mock, timeout: float) -> None`

### `def test___negative_timeout___reserve_session___warns_and_sends_request_with_infinite_timeout(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___single_session___reserve_session___returns_single_session_info(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___no_sessions___reserve_session___raises_no_sessions_value_error(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___too_many_sessions___reserve_session___raises_too_many_sessions_value_error(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___all_optional_args___reserve_session___args_passed_to_reservation(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___all_optional_args___reserve_sessions___sends_request_with_args(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___no_optional_args___reserve_sessions___sends_request_with_defaults(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___explicit_none___reserve_sessions___sends_request_with_defaults(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___single_pin___reserve_sessions___sends_request_with_single_pin(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___infinite_timeout___reserve_sessions___sends_request_with_infinite_timeout(session_management_client: SessionManagementClient, session_management_stub: Mock, timeout: float) -> None`

### `def test___negative_timeout___reserve_sessions___warns_and_sends_request_with_infinite_timeout(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___varying_session_count___reserve_sessions___returns_multiple_session_infos(session_management_client: SessionManagementClient, session_management_stub: Mock, session_count: int) -> None`

### `def test___all_optional_args___reserve_sessions___args_passed_to_reservation(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___varying_session_count___unreserve___sends_request(session_management_client: SessionManagementClient, session_management_stub: Mock, session_count: int) -> None`

### `def test___varying_session_count___exit_reservation___sends_request(session_management_client: SessionManagementClient, session_management_stub: Mock, session_count: int) -> None`

### `def test___varying_session_count___register_sessions___sends_request(session_management_client: SessionManagementClient, session_management_stub: Mock, session_count: int) -> None`

### `def test___varying_session_count___unregister_sessions___sends_request(session_management_client: SessionManagementClient, session_management_stub: Mock, session_count: int) -> None`

### `def test___all_optional_args___reserve_all_registered_sessions___sends_request_with_args(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___no_optional_args___reserve_all_registered_sessions___sends_request_with_defaults(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___explicit_none___reserve_all_registered_sessions___sends_request_with_defaults(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___infinite_timeout___reserve_all_registered_sessions___sends_request_with_infinite_timeout(session_management_client: SessionManagementClient, session_management_stub: Mock, timeout: float) -> None`

### `def test___negative_timeout___reserve_all_registered_sessions___warns_and_sends_request_with_infinite_timeout(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___varying_session_count___reserve_all_registered_sessions___returns_session_infos(session_management_client: SessionManagementClient, session_management_stub: Mock, session_count: int) -> None`

### `def test___use_reservation_type___reports_deprecated_warning_and_aliases_to_multi_session_reservation(session_management_client: SessionManagementClient) -> None`

### `def test___session_information___type_check___implements_typed_session_information_object() -> None`

### `def test___single_session_with_varying_multiplexer_count___reserve_session___returns_session_info_and_multiplexer_infos(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def test___multiple_sessions_with_varying_multiplexer_count___reserve_sessions___returns_session_infos_and_multiplexer_infos(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def test___single_session_with_shared_pins_and_varying_multiplexer_count___reserve_session___returns_session_and_multiplexer_infos_for_all_sites(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def test___multiple_sessions_with_shared_pins_and_varying_multiplexer_count___reserve_sessions___returns_session_and_multiplexer_infos_for_all_sites(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def test___single_session_without_multiplexer___get_multiplexer_session_info___returns_empty_list(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___multiple_sessions_without_multiplexer___get_multiplexer_session_info___returns_empty_list(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___varying_multiplexer_session_count___register_multiplexer_sessions___sends_request(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def test___varying_multiplexer_session_count___unregister_multiplexer_sessions___sends_request(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def test___optional_arg___get_multiplexer_sessions___sends_request_with_args(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___no_optional_args___get_multiplexer_sessions___sends_request_with_default(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___explicit_none___get_multiplexer_sessions___sends_request_with_default(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___varying_multiplexers___get_multiplexer_sessions___returns_multiplexer_session_infos(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def test___optional_arg___get_all_registered_multiplexer_sessions___sends_request_with_args(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___no_optional_args___get_all_registered_multiplexer_sessions___sends_request_with_default(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___explicit_none___get_all_registered_multiplexer_sessions___sends_request_with_default(session_management_client: SessionManagementClient, session_management_stub: Mock) -> None`

### `def test___varying_registered_multiplexers___get_all_registered_multiplexer_sessions___returns_multiplexer_session_infos(session_management_client: SessionManagementClient, session_management_stub: Mock, multiplexer_session_count: int) -> None`

### `def _create_session_infos(session_count: int) -> list[SessionInformation]`

### `def _create_multiplexer_session_infos(multiplexer_session_count: int) -> list[MultiplexerSessionInformation]`

### `def _create_grpc_session_infos(session_count: int) -> list[session_management_service_pb2.SessionInformation]`

### `def _create_grpc_multiplexer_session_infos(session_count: int) -> list[session_management_service_pb2.MultiplexerSessionInformation]`

### `def session_management_client(discovery_client: Mock, grpc_channel_pool: Mock, mocker: MockerFixture, session_management_stub: Mock) -> SessionManagementClient`

Create a Client with a mock SessionManagementServiceStub.

### `def session_management_stub(mocker: MockerFixture) -> Mock`

Create a mock SessionManagementServiceStub.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/__init__.py

### MODULE DOCSTRING

Contains test utilities.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/_array_utils.py -->
## PYTHON MODULE: packages/service/tests/utilities/_array_utils.py

### MODULE DOCSTRING

2DArray Conversion Utilities.

### `def double2darray_to_ndarray(double2darray: array_pb2.Double2DArray) -> npt.NDArray[np.float64]`

Convert Double2DArray to numpy NDArray.

### `def ndarray_to_double2darray(ndarray: npt.NDArray[np.float64]) -> array_pb2.Double2DArray`

Convert numpy NDArray to Double2DArray.

### `def list_to_double2darray(data: list[list[float]]) -> array_pb2.Double2DArray`

Convert list of lists to Double2DArray.

### `def double2darray_to_list(double2darray: array_pb2.Double2DArray) -> list[list[float]]`

Convert Double2DArray to list of lists.

### `def string2darray_to_ndarray(string2darray: array_pb2.String2DArray) -> npt.NDArray[np.str_]`

Convert String2DArray to numpy NDArray.

### `def ndarray_to_string2darray(ndarray: npt.NDArray[np.str_]) -> array_pb2.String2DArray`

Convert numpy NDArray to String2DArray.

### `def string2darray_to_list(string2darray: array_pb2.String2DArray) -> list[list[str]]`

Convert String2DArray to list of lists.

### `def list_to_string2darray(data: list[list[str]]) -> array_pb2.String2DArray`

Convert list of lists to String2DArray.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/connection_subset.py -->
## PYTHON MODULE: packages/service/tests/utilities/connection_subset.py

### MODULE DOCSTRING

Utility to create and construct connection subset.

- `_T = TypeVar('_T')`

### `class ConnectionSubset(NamedTuple)`

An object that holds a subset of connection data.

### `def get_connection_subset(connection: Connection | TypedConnection[_T]) -> ConnectionSubset`

Constructs and returns a ConnectionSubset object.

### `def get_connection_subset_with_multiplexer(connection: Connection | TypedConnectionWithMultiplexer[_T, _TMultiplexer]) -> ConnectionSubset`

Constructs and returns a ConnectionSubset object with multiplexer data.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/discovery_service_process.py -->
## PYTHON MODULE: packages/service/tests/utilities/discovery_service_process.py

### MODULE DOCSTRING

Class to create and terminate Discovery Service instance.

### `class DiscoveryServiceProcess()`

Maintains the processes involved in creating and terminating discovery service.

#### `def __init__(self) -> None`

Creates a DiscoveryServiceProcess instance.

#### `def __enter__(self: Self) -> Self`

Returns the DiscoveryServiceProcess instance.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None`

Closes the DiscoveryServiceProcess instance.

#### `def _close_discovery_service(self) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/fake_discovery_service.py -->
## PYTHON MODULE: packages/service/tests/utilities/fake_discovery_service.py

### MODULE DOCSTRING

Contains Test Doubles related to Discovery service.

### `class FakeRegistrationResponse()`

Fake Registration Response.

### `class FakeDiscoveryServiceStub()`

Fake Registry Service Stub.

#### `def RegisterService(self, request)`

Fake gRPC registration call to discovery service.

#### `def UnregisterService(self, request)`

Fake gRPC un-registration call to discovery service.

### `class FakeDiscoveryServiceStubError(FakeDiscoveryServiceStub)`

Fake Registry Service Stub that throws error to mimic unavailability of discovery service.

#### `def RegisterService(self, request)`

Fake gRPC registration call to discovery service.

#### `def UnregisterService(self, request)`

Fake gRPC un-registration call to discovery service.

### `class FakeDiscoveryServiceError(Exception)`

Fake discovery service error to mimic the exceptions thrown from  discovery service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/fake_driver.py -->
## PYTHON MODULE: packages/service/tests/utilities/fake_driver.py

### MODULE DOCSTRING

Fake driver API for testing.

- `GRPC_SERVICE_INTERFACE_NAME = 'nifake_grpc.NiFake'`

- `_API_KEY = '00000000-0000-0000-0000-000000000000'`

### `class SessionInitializationBehavior(IntEnum)`

Specifies whether to initialize a new session or attach to an existing session.

- `_CLOSE_BEHAVIORS = [SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE]`

### `class GrpcSessionOptions()`

gRPC session options.

#### `def __init__(self, grpc_channel: grpc.Channel, session_name: str, *, api_key: str=_API_KEY, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> None`

Initialize the gRPC session options.

### `class MeasurementType(Enum)`

Measurement type.

### `class _Acquisition()`

#### `def __init__(self, session: _SessionBase) -> None`

#### `def __enter__(self) -> Self`

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

### `class _SessionBase()`

Base class for driver sessions.

#### `def __init__(self, resource_name: str, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO, options: dict[str, Any]={}) -> None`

Initialize the session.

#### `def configure(self, measurement_type: MeasurementType, range: float) -> None`

Configure the session.

#### `def initiate(self) -> ContextManager[object]`

Initiate an acquisition.

#### `def abort(self) -> None`

Abort (stop) the acquisition.

#### `def read(self) -> float`

Read a sample.

### `class ClosableSession(_SessionBase)`

A driver session that supports close().

#### `def close(self) -> None`

Close the session.

### `class ContextManagerSession(_SessionBase)`

A driver session that supports the context manager protocol.

#### `def __enter__(self) -> Self`

Enter the session's runtime context.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the session's runtime context.

### `class Session(_SessionBase)`

A driver session that supports both close() and the context manager protocol.

#### `def __init__(self, resource_name: str, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO, options: dict[str, Any]={}) -> None`

Initialize the session.

#### `def close(self) -> None`

Close the session.

#### `def __enter__(self) -> Self`

Enter the session's runtime context.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the session's runtime context.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/fake_multiplexer_driver.py -->
## PYTHON MODULE: packages/service/tests/utilities/fake_multiplexer_driver.py

### MODULE DOCSTRING

Fake driver API for testing.

- `GRPC_SERVICE_INTERFACE_NAME = 'nifake_grpc.NiFake'`

- `_API_KEY = '00000000-0000-0000-0000-000000000000'`

### `class SessionInitializationBehavior(IntEnum)`

Specifies whether to initialize a new session or attach to an existing session.

- `_CLOSE_BEHAVIORS = [SessionInitializationBehavior.AUTO, SessionInitializationBehavior.INITIALIZE_SERVER_SESSION, SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE]`

### `class GrpcSessionOptions()`

gRPC session options.

#### `def __init__(self, grpc_channel: grpc.Channel, session_name: str, *, api_key: str=_API_KEY, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> None`

Initialize the gRPC session options.

### `class RelayAction(Enum)`

Relay action.

### `class _MultiplexerSessionBase()`

Base class for multiplexer driver sessions.

#### `def __init__(self, resource_name: str, topology: str | None=None, reset_device: bool=True, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> None`

Initialize the multiplexer session.

#### `def relay_control(self, relay_name: str, relay_action: RelayAction) -> None`

Controls individual relays of the switch.

#### `def connect_multiple(self, connection_list: str) -> None`

Creates the connections between channels specified in connection list.

#### `def disconnect_multiple(self, connection_list: str) -> None`

Breaks the connections between channels specified in disconnection list.

#### `def wait_for_debounce(self) -> None`

Pauses until all created paths have settled.

#### `def abort(self) -> None`

Abort (stop) the acquisition.

### `class ClosableSession(_MultiplexerSessionBase)`

A driver session that supports close().

#### `def close(self) -> None`

Close the session.

### `class ContextManagerSession(_MultiplexerSessionBase)`

A driver session that supports the context manager protocol.

#### `def __enter__(self) -> Self`

Enter the session's runtime context.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the session's runtime context.

### `class Session(_MultiplexerSessionBase)`

A multiplexer driver session that supports both close() and the context manager protocol.

#### `def __init__(self, resource_name: str, topology: str | None=None, reset_device: bool=True, initialization_behavior: SessionInitializationBehavior=SessionInitializationBehavior.AUTO) -> None`

Initialize the multiplexer session.

#### `def close(self) -> None`

Close the session.

#### `def __enter__(self) -> Self`

Enter the session's runtime context.

#### `def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, traceback: TracebackType | None) -> None`

Exit the session's runtime context.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/fake_rpc_error.py -->
## PYTHON MODULE: packages/service/tests/utilities/fake_rpc_error.py

### MODULE DOCSTRING

A throwable version of grpc.RpcError for testing.

### `class FakeRpcError(grpc.RpcError)`

A throwable version of grpc.RpcError for testing.

#### `def __init__(self, code: grpc.StatusCode, details: str) -> None`

Construct a FakeRpcError.

#### `def code(self) -> grpc.StatusCode`

Get the gRPC status code.

#### `def details(self) -> str`

Get the error details.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/__init__.py

### MODULE DOCSTRING

Test measurements.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/loopback_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/loopback_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test loopback measurement service.

### `class Color(Enum)`

Primary colors used for example enum-typed config and output.

### `def measure(float_input: float, double_array_input: Iterable[float], bool_input: bool, string_input: str, enum_input: Color, protobuf_enum_input: color_pb2.ProtobufColor.ValueType, string_array_in: Iterable[str]) -> tuple[float, Iterable[float], bool, str, Color, color_pb2.ProtobufColor.ValueType, Iterable[str]]`

Perform a loopback measurement with various data types.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidaqmx_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/nidaqmx_measurement/__init__.py

### MODULE DOCSTRING

NI-DAQmx measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[list[str], list[str], list[str], list[str], list[float]]`

NI-DAQmx measurement plug-in test service.

### `def _read_voltage_values(session_infos: Sequence[TypedSessionInformation[nidaqmx.Task]]) -> list[float]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidcpower_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/nidcpower_measurement/__init__.py

### MODULE DOCSTRING

NI-DCPower measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str], Iterable[float], Iterable[float]]`

NI-DCPower measurement plug-in test service.

### `def _source_measure_dc_voltage(connections: Sequence[TypedConnection[nidcpower.Session]]) -> tuple[list[float], list[float]]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidigital_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/nidigital_measurement/__init__.py

### MODULE DOCSTRING

NI-Digital measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str], Iterable[int], Iterable[int]]`

NI-Digital measurement plug-in test service.

### `def _burst_spi_pattern(session_infos: Sequence[TypedSessionInformation[nidigital.Session]]) -> tuple[list[int], list[int]]`

### `def _resolve_relative_path(directory_path: pathlib.Path, file_path: str | pathlib.Path) -> pathlib.Path`

### `def _key_func(conn: TypedConnection[nidigital.Session]) -> str`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nidmm_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/nidmm_measurement/__init__.py

### MODULE DOCSTRING

NI-DMM measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[list[str], list[str], list[str], list[str], list[bool], list[float]]`

NI-DMM measurement plug-in test service.

### `def _get_dmm_readings(session_infos: Sequence[TypedSessionInformation[nidmm.Session]]) -> tuple[list[bool], list[float]]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/nifgen_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/nifgen_measurement/__init__.py

### MODULE DOCSTRING

NI-FGEN measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str]]`

NI-FGEN measurement plug-in test service.

### `def _generate_standard_waveform(session_infos: Sequence[TypedSessionInformation[nifgen.Session]]) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niscope_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/niscope_measurement/__init__.py

### MODULE DOCSTRING

NI-SCOPE measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str], Iterable[float]]`

NI-SCOPE measurement plug-in test service.

### `def _acquire_waveforms(session_infos: Sequence[TypedSessionInformation[niscope.Session]]) -> list[list[float]]`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niswitch_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/niswitch_measurement/__init__.py

### MODULE DOCSTRING

NI-SWITCH measurement plug-in test service.

### `def measure(relay_names: Iterable[str], multi_session: bool) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str]]`

NI-SWITCH measurement plug-in test service.

### `def _control_relays(session_infos: Sequence[TypedSessionInformation[niswitch.Session]]) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/niswitch_multiplexer_measurement/__init__.py

### MODULE DOCSTRING

NI-SWITCH multiplexer measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[Iterable[str], Iterable[str], Iterable[str], Iterable[str]]`

NI-SWITCH multiplexer measurement plug-in test service.

### `def _control_relays(connections: Sequence[TypedConnectionWithMultiplexer]) -> None`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/pin_aware_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/pin_aware_measurement/__init__.py

### MODULE DOCSTRING

Pin-aware measurement plug-in test service.

### `def measure(pin_names: Iterable[str], multi_session: bool) -> tuple[str, Iterable[int], Iterable[str], Iterable[str], Iterable[str]]`

Pin-aware measurement plug-in test service.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/__init__.py

### MODULE DOCSTRING

Stubs for sample_measurement's color enum.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bcolor.proto\x124ni.measurementlink.measurement.sample_measurement.v1*9\n\rProtobufColor\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05BLACK\x10\x03B7\xaa\x024NationalInstruments.MeasurementServices.Measurementsb\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/sample_measurement/_stubs/color_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/streaming_data_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/streaming_data_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test a v2 measurement service that streams data.

### `def measure(name: str, num_responses: int, data_size: int, cumulative_data: bool, response_interval_in_ms: int, error_on_index: int) -> Generator[Outputs]`

Returns the number of responses requested at the requested interval.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/unknown_interface_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/unknown_interface_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test loopback measurement service.

### `def measure(float_input: float) -> tuple[float]`

Loopback measurement on the float input.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/v1_only_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/v1_only_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test loopback measurement service.

### `def measure(float_input: float) -> tuple[float]`

Loopback measurement on the float input.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/v2_only_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/v2_only_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test loopback measurement service.

### `def measure(float_input: float) -> tuple[float]`

Loopback measurement on the float input.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/measurements/yield_vs_return_measurement/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/measurements/yield_vs_return_measurement/__init__.py

### MODULE DOCSTRING

Contains utility functions to test that yield and return are supported in measurements.

- `RANDOM_NUMBERS_PER_SECOND = 100.0`

- `RANDOM_NUMBER_RANGE = 10.0`

- `UI_UPDATE_INTERVAL_IN_SECONDS = 0.1`

### `def measure(time_in_seconds: float) -> Generator[Outputs, None, Outputs]`

Generates random numbers and updates the measurement UI to show progress.

### `def _generate_random_numbers(count: int) -> Generator[float]`

Generate random numbers between -RANDOM_NUMBER_RANGE and +RANDOM_NUMBER_RANGE.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/loopback/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for loopback measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/loopback/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14loopback/types.proto\x12-ni.measurementlink.measurement.tests.loopback"\x93\x02\n\nParameters\x12\x10\n\x08float_in\x18\x01 \x01(\x02\x12\x17\n\x0fdouble_array_in\x18\x02 \x03(\x01\x12\x0f\n\x07bool_in\x18\x03 \x01(\x08\x12\x11\n\tstring_in\x18\x04 \x01(\t\x12E\n\x07enum_in\x18\x05 \x01(\x0e24.ni.measurementlink.measurement.tests.loopback.Color\x12V\n\x10protobuf_enum_in\x18\x06 \x01(\x0e2<.ni.measurementlink.measurement.tests.loopback.ProtobufColor\x12\x17\n\x0fstring_array_in\x18\x07 \x03(\t*/\n\x05Color\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03RED\x10\x01\x12\t\n\x05GREEN\x10\x02\x12\x08\n\x04BLUE\x10\x03*>\n\rProtobufColor\x12\r\n\tCOLORLESS\x10\x00\x12\x08\n\x04PINK\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\t\n\x05BLACK\x10\x03b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/loopback/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidaqmx/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for nidaqmx test measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidaqmx/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13nidaqmx/types.proto\x12,ni.measurementlink.measurement.tests.nidaqmx":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"\x83\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\t\x12\x16\n\x0evoltage_values\x18\x05 \x03(\x01b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidaqmx/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidcpower/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for nidcpower test measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidcpower/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15nidcpower/types.proto\x12.ni.measurementlink.measurement.tests.nidcpower":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"\xa7\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\t\x12\x1c\n\x14voltage_measurements\x18\x05 \x03(\x01\x12\x1c\n\x14current_measurements\x18\x06 \x03(\x01b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidcpower/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidigital/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for nidigital test measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidigital/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15nidigital/types.proto\x12.ni.measurementlink.measurement.tests.nidigital":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"\x99\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\t\x12\x15\n\rpassing_sites\x18\x05 \x03(\x05\x12\x15\n\rfailing_sites\x18\x06 \x03(\x05b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidigital/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidmm/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for nidmm test measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidmm/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11nidmm/types.proto\x12*ni.measurementlink.measurement.tests.nidmm":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"\xa7\x01\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\t\x12\x1c\n\x14signals_out_of_range\x18\x05 \x03(\x08\x12\x1c\n\x14absolute_resolutions\x18\x06 \x03(\x01b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nidmm/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nifgen/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for nifgen test measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nifgen/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12nifgen/types.proto\x12+ni.measurementlink.measurement.tests.nifgen":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"k\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\tb\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/nifgen/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niscope/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for niscope test measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niscope/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13niscope/types.proto\x12,ni.measurementlink.measurement.tests.niscope":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"}\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\t\x12\x10\n\x08waveform\x18\x05 \x03(\x01b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niscope/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niswitch/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for niswitch test measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niswitch/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14niswitch/types.proto\x12-ni.measurementlink.measurement.tests.niswitch"<\n\x0eConfigurations\x12\x13\n\x0brelay_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"k\n\x07Outputs\x12\x15\n\rsession_names\x18\x01 \x03(\t\x12\x16\n\x0eresource_names\x18\x02 \x03(\t\x12\x15\n\rchannel_lists\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\tb\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niswitch/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fniswitchmultiplexer/types.proto\x128ni.measurementlink.measurement.tests.niswitchmultiplexer":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"\x88\x01\n\x07Outputs\x12!\n\x19multiplexer_session_names\x18\x01 \x03(\t\x12"\n\x1amultiplexer_resource_names\x18\x02 \x03(\t\x12\x1a\n\x12multiplexer_routes\x18\x03 \x03(\t\x12\x1a\n\x12connected_channels\x18\x04 \x03(\tb\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/niswitchmultiplexer/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/pinaware/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for pin-aware measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/pinaware/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pinaware/types.proto\x12-ni.measurementlink.measurement.tests.pinaware":\n\x0eConfigurations\x12\x11\n\tpin_names\x18\x01 \x03(\t\x12\x15\n\rmulti_session\x18\x02 \x01(\x08"r\n\x07Outputs\x12\x12\n\npin_map_id\x18\x01 \x01(\t\x12\r\n\x05sites\x18\x02 \x03(\x05\x12\x15\n\rsession_names\x18\x03 \x03(\t\x12\x16\n\x0eresource_names\x18\x04 \x03(\t\x12\x15\n\rchannel_lists\x18\x05 \x03(\tb\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/pinaware/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/serialization/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for serialization tests.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/serialization/bigmessage_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eserialization/bigmessage.proto\x122ni.measurementlink.measurement.tests.serialization"\xa8\r\n\nBigMessage\x12\x0e\n\x06field1\x18\x01 \x01(\x01\x12\x0e\n\x06field2\x18\x02 \x01(\x01\x12\x0e\n\x06field3\x18\x03 \x01(\x01\x12\x0e\n\x06field4\x18\x04 \x01(\x01\x12\x0e\n\x06field5\x18\x05 \x01(\x01\x12\x0e\n\x06field6\x18\x06 \x01(\x01\x12\x0e\n\x06field7\x18\x07 \x01(\x01\x12\x0e\n\x06field8\x18\x08 \x01(\x01\x12\x0e\n\x06field9\x18\t \x01(\x01\x12\x0f\n\x07field10\x18\n \x01(\x01\x12\x0f\n\x07field11\x18\x0b \x01(\x01\x12\x0f\n\x07field12\x18\x0c \x01(\x01\x12\x0f\n\x07field13\x18\r \x01(\x01\x12\x0f\n\x07field14\x18\x0e \x01(\x01\x12\x0f\n\x07field15\x18\x0f \x01(\x01\x12\x0f\n\x07field16\x18\x10 \x01(\x01\x12\x0f\n\x07field17\x18\x11 \x01(\x01\x12\x0f\n\x07field18\x18\x12 \x01(\x01\x12\x0f\n\x07field19\x18\x13 \x01(\x01\x12\x0f\n\x07field20\x18\x14 \x01(\x01\x12\x0f\n\x07field21\x18\x15 \x01(\x01\x12\x0f\n\x07field22\x18\x16 \x01(\x01\x12\x0f\n\x07field23\x18\x17 \x01(\x01\x12\x0f\n\x07field24\x18\x18 \x01(\x01\x12\x0f\n\x07field25\x18\x19 \x01(\x01\x12\x0f\n\x07field26\x18\x1a \x01(\x01\x12\x0f\n\x07field27\x18\x1b \x01(\x01\x12\x0f\n\x07field28\x18\x1c \x01(\x01\x12\x0f\n\x07field29\x18\x1d \x01(\x01\x12\x0f\n\x07field30\x18\x1e \x01(\x01\x12\x0f\n\x07field31\x18\x1f \x01(\x01\x12\x0f\n\x07field32\x18  \x01(\x01\x12\x0f\n\x07field33\x18! \x01(\x01\x12\x0f\n\x07field34\x18" \x01(\x01\x12\x0f\n\x07field35\x18# \x01(\x01\x12\x0f\n\x07field36\x18$ \x01(\x01\x12\x0f\n\x07field37\x18% \x01(\x01\x12\x0f\n\x07field38\x18& \x01(\x01\x12\x0f\n\x07field39\x18\' \x01(\x01\x12\x0f\n\x07field40\x18( \x01(\x01\x12\x0f\n\x07field41\x18) \x01(\x01\x12\x0f\n\x07field42\x18* \x01(\x01\x12\x0f\n\x07field43\x18+ \x01(\x01\x12\x0f\n\x07field44\x18, \x01(\x01\x12\x0f\n\x07field45\x18- \x01(\x01\x12\x0f\n\x07field46\x18. \x01(\x01\x12\x0f\n\x07field47\x18/ \x01(\x01\x12\x0f\n\x07field48\x180 \x01(\x01\x12\x0f\n\x07field49\x181 \x01(\x01\x12\x0f\n\x07field50\x182 \x01(\x01\x12\x0f\n\x07field51\x183 \x01(\x01\x12\x0f\n\x07field52\x184 \x01(\x01\x12\x0f\n\x07field53\x185 \x01(\x01\x12\x0f\n\x07field54\x186 \x01(\x01\x12\x0f\n\x07field55\x187 \x01(\x01\x12\x0f\n\x07field56\x188 \x01(\x01\x12\x0f\n\x07field57\x189 \x01(\x01\x12\x0f\n\x07field58\x18: \x01(\x01\x12\x0f\n\x07field59\x18; \x01(\x01\x12\x0f\n\x07field60\x18< \x01(\x01\x12\x0f\n\x07field61\x18= \x01(\x01\x12\x0f\n\x07field62\x18> \x01(\x01\x12\x0f\n\x07field63\x18? \x01(\x01\x12\x0f\n\x07field64\x18@ \x01(\x01\x12\x0f\n\x07field65\x18A \x01(\x01\x12\x0f\n\x07field66\x18B \x01(\x01\x12\x0f\n\x07field67\x18C \x01(\x01\x12\x0f\n\x07field68\x18D \x01(\x01\x12\x0f\n\x07field69\x18E \x01(\x01\x12\x0f\n\x07field70\x18F \x01(\x01\x12\x0f\n\x07field71\x18G \x01(\x01\x12\x0f\n\x07field72\x18H \x01(\x01\x12\x0f\n\x07field73\x18I \x01(\x01\x12\x0f\n\x07field74\x18J \x01(\x01\x12\x0f\n\x07field75\x18K \x01(\x01\x12\x0f\n\x07field76\x18L \x01(\x01\x12\x0f\n\x07field77\x18M \x01(\x01\x12\x0f\n\x07field78\x18N \x01(\x01\x12\x0f\n\x07field79\x18O \x01(\x01\x12\x0f\n\x07field80\x18P \x01(\x01\x12\x0f\n\x07field81\x18Q \x01(\x01\x12\x0f\n\x07field82\x18R \x01(\x01\x12\x0f\n\x07field83\x18S \x01(\x01\x12\x0f\n\x07field84\x18T \x01(\x01\x12\x0f\n\x07field85\x18U \x01(\x01\x12\x0f\n\x07field86\x18V \x01(\x01\x12\x0f\n\x07field87\x18W \x01(\x01\x12\x0f\n\x07field88\x18X \x01(\x01\x12\x0f\n\x07field89\x18Y \x01(\x01\x12\x0f\n\x07field90\x18Z \x01(\x01\x12\x0f\n\x07field91\x18[ \x01(\x01\x12\x0f\n\x07field92\x18\\ \x01(\x01\x12\x0f\n\x07field93\x18] \x01(\x01\x12\x0f\n\x07field94\x18^ \x01(\x01\x12\x0f\n\x07field95\x18_ \x01(\x01\x12\x0f\n\x07field96\x18` \x01(\x01\x12\x0f\n\x07field97\x18a \x01(\x01\x12\x0f\n\x07field98\x18b \x01(\x01\x12\x0f\n\x07field99\x18c \x01(\x01\x12\x10\n\x08field100\x18d \x01(\x01b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/serialization/bigmessage_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/test_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/serialization/test_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18serialization/test.proto\x122ni.measurementlink.measurement.tests.serialization\x1a\x1eni/protobuf/types/xydata.proto"\xdc\x06\n\x14MeasurementParameter\x12\x12\n\nfloat_data\x18\x01 \x01(\x02\x12\x13\n\x0bdouble_data\x18\x02 \x01(\x01\x12\x12\n\nint32_data\x18\x03 \x01(\x05\x12\x13\n\x0buint32_data\x18\x04 \x01(\r\x12\x12\n\nint64_data\x18\x05 \x01(\x03\x12\x13\n\x0buint64_data\x18\x06 \x01(\x04\x12\x11\n\tbool_data\x18\x07 \x01(\x08\x12\x13\n\x0bstring_data\x18\x08 \x01(\t\x12\x19\n\x11double_array_data\x18\t \x03(\x01\x12\x18\n\x10float_array_data\x18\n \x03(\x02\x12\x18\n\x10int32_array_data\x18\x0b \x03(\x05\x12\x19\n\x11uint32_array_data\x18\x0c \x03(\r\x12\x18\n\x10int64_array_data\x18\r \x03(\x03\x12\x19\n\x11uint64_array_data\x18\x0e \x03(\x04\x12\x17\n\x0fbool_array_data\x18\x0f \x03(\x08\x12\x19\n\x11string_array_data\x18\x10 \x03(\t\x12U\n\tenum_data\x18\x11 \x01(\x0e2B.ni.measurementlink.measurement.tests.serialization.DifferentColor\x12[\n\x0fenum_array_data\x18\x12 \x03(\x0e2B.ni.measurementlink.measurement.tests.serialization.DifferentColor\x12T\n\rint_enum_data\x18\x13 \x01(\x0e2=.ni.measurementlink.measurement.tests.serialization.Countries\x12Z\n\x13int_enum_array_data\x18\x14 \x03(\x0e2=.ni.measurementlink.measurement.tests.serialization.Countries\x120\n\x07xy_data\x18\x15 \x01(\x0b2\x1f.ni.protobuf.types.DoubleXYData\x126\n\rxy_data_array\x18\x16 \x03(\x0b2\x1f.ni.protobuf.types.DoubleXYData*=\n\x0eDifferentColor\x12\n\n\x06PURPLE\x10\x00\x12\n\n\x06ORANGE\x10\x01\x12\x08\n\x04TEAL\x10\x02\x12\t\n\x05BROWN\x10\x03*?\n\tCountries\x12\x0b\n\x07AMERICA\x10\x00\x12\n\n\x06TAIWAN\x10\x01\x12\r\n\tAUSTRALIA\x10\x02\x12\n\n\x06CANADA\x10\x03b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/serialization/test_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/streamingdata/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for streaming data measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/streamingdata/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19streamingdata/types.proto\x122ni.measurementlink.measurement.tests.streamingdata"\x9a\x01\n\x0eConfigurations\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rnum_responses\x18\x02 \x01(\x05\x12\x11\n\tdata_size\x18\x03 \x01(\x05\x12\x17\n\x0fcumulative_data\x18\x04 \x01(\x08\x12\x1f\n\x17response_interval_in_ms\x18\x05 \x01(\x05\x12\x16\n\x0eerror_on_index\x18\x06 \x01(\x05"4\n\x07Outputs\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\x12\x0c\n\x04data\x18\x03 \x03(\x05b\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/streamingdata/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/__init__.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/yieldvsreturn/__init__.py

### MODULE DOCSTRING

Auto generated gRPC files for yield vs. return measurement.

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19yieldvsreturn/types.proto\x122ni.measurementlink.measurement.tests.yieldvsreturn")\n\x0eConfigurations\x12\x17\n\x0ftime_in_seconds\x18\x01 \x01(\x01"R\n\x07Outputs\x12\x1f\n\x17elapsed_time_in_seconds\x18\x01 \x01(\x01\x12\x16\n\x0erandom_numbers\x18\x02 \x03(\x01\x12\x0e\n\x06status\x18\x03 \x01(\tb\x06proto3')`

<!--NI_PYTHON_API repo=measurement-plugin-python path=packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.py -->
## PYTHON MODULE: packages/service/tests/utilities/stubs/yieldvsreturn/types_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.
