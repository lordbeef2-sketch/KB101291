# NI PYTHON API DIGEST: niflexlogger-automation-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/niflexlogger-automation-python commit=6e28e4c786c3920651396b8790004ca6167824c8 -->

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=docs/cleanup.py -->
## PYTHON MODULE: docs/cleanup.py

### MODULE DOCSTRING

Sphinx extension to clean up autodoc output.

### `def _skip_member(app, what, name, obj, skip, options)`

### `def _process_docstring(app, what, name, obj, options, lines)`

### `def modify_flexlogger_paths(s: str) -> str`

Modify flexlogger.* paths in the given string to hide implementation modules.

    Examples:
        >>> # Basic usage
        >>> modify_flexlogger_paths("flexlogger.foo._abc.Abc")
        'flexlogger.foo.Abc'
        >>> # Modify all paths in the string
        >>> modify_flexlogger_paths(" flexlogger.f._abc.Abc flexlogger.f._xyz.Xyz ")
        ' flexlogger.f.Abc flexlogger.f.Xyz '
    

### `def setup(app)`

Entry point for Sphinx extensions.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/add_note.py -->
## PYTHON MODULE: examples/Basic/add_note.py

### `def main(project_path)`

Launch FlexLogger, open a project, start the test session and add a note.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/connect_to_application.py -->
## PYTHON MODULE: examples/Basic/connect_to_application.py

### `def main()`

Connect to an already running instance of FlexLogger with an open project

    Note that before connecting to an already running instance of FlexLogger,
    the Automation server preference must be enabled. You can enable this preference by opening the
    "File>>Preferences" menu item, and then enabling the "Automation server" preference in the
    "General" tab.
    

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/disable_channel.py -->
## PYTHON MODULE: examples/Basic/disable_channel.py

### `def main(project_path)`

Launch FlexLogger, open a project, and disables a channel.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/disable_channel_logging.py -->
## PYTHON MODULE: examples/Basic/disable_channel_logging.py

### `def main(project_path)`

Launch FlexLogger, open a project, and disables a channel.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/events.py -->
## PYTHON MODULE: examples/Basic/events.py

### `def main(project_path)`

Launch FlexLogger, open a project, and wait for an event.

### `def alarms_event_handler(application: Application, event_type: EventType, payload: AlarmPayload)`

Alarm Event Handler
    This method will be called when an alarm event is fired.

    Args:
        application: Application    Reference to the application, so that you can access the project, session, etc
        event_type: EventType       The event type
        payload: AlarmPayload       The event payload
    

### `def log_file_event_handler(application: Application, event_type: EventType, payload: FilePayload)`

FlexLogger Event Handler
    This method will be called when a file event is fired.

        Args:
            application: Application    Reference to the application, so that you can access the project, session, etc
            event_type: EventType       The event type
            payload: FilePayload        The event payload
    

### `def session_event_handler(application: Application, event_type: EventType, payload: EventPayload)`

FlexLogger Event Handler
    This method will be called when a session event is fired.

    Args:
        application: Application    Reference to the application, so that you can access the project, session, etc
        event_type: EventType       The event type
        payload: EventPayload       The event payload
    

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/get_channel_value.py -->
## PYTHON MODULE: examples/Basic/get_channel_value.py

### `def main(project_path)`

Launch FlexLogger, open a project, and get the value of a channel.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/get_log_file_description.py -->
## PYTHON MODULE: examples/Basic/get_log_file_description.py

### `def main(project_path)`

Launch FlexLogger, open a project, and get the log file description.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/get_log_file_path_and_name.py -->
## PYTHON MODULE: examples/Basic/get_log_file_path_and_name.py

### `def main(project_path)`

Launch FlexLogger, open a project, and gets the log file base path and name.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/get_project_file_path.py -->
## PYTHON MODULE: examples/Basic/get_project_file_path.py

### `def main(project_path)`

Launch FlexLogger, open a project, and get the loaded project's file path.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/get_test_properties.py -->
## PYTHON MODULE: examples/Basic/get_test_properties.py

### `def main(project_path)`

Launch FlexLogger, open a project, and get all test properties.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/get_test_property.py -->
## PYTHON MODULE: examples/Basic/get_test_property.py

### `def main(project_path)`

Launch FlexLogger, open a project, and gets the value of a test property.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/get_trigger_settings.py -->
## PYTHON MODULE: examples/Basic/get_trigger_settings.py

### `def main(project_path)`

Launch FlexLogger, open a project, and get the trigger settings.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/launch_application.py -->
## PYTHON MODULE: examples/Basic/launch_application.py

### `def main(project_path)`

Launch FlexLogger and open a project.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/pause_and_resume_test_session.py -->
## PYTHON MODULE: examples/Basic/pause_and_resume_test_session.py

### `def main(project_path)`

Launch FlexLogger, open a project, pauses and resumes the test session.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/run_test_session_and_show_log_file.py -->
## PYTHON MODULE: examples/Basic/run_test_session_and_show_log_file.py

### `def main(project_path)`

Launch FlexLogger, open a project, run a test session, and show log file.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_channel_value.py -->
## PYTHON MODULE: examples/Basic/set_channel_value.py

### `def main(project_path)`

Launch FlexLogger, open a project, and sets the value of a channel.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_data_rate.py -->
## PYTHON MODULE: examples/Basic/set_data_rate.py

- `DATA_RATE_LEVEL_LOOKUP = {'Slow': DataRateLevel.SLOW, 'Medium': DataRateLevel.MEDIUM, 'Fast': DataRateLevel.FAST}`

### `def main(project_path)`

Launch FlexLogger, open a project, and set the data rate values.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_log_file_description.py -->
## PYTHON MODULE: examples/Basic/set_log_file_description.py

### `def main(project_path)`

Launch FlexLogger, open a project, and set the log file description.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_log_file_path_and_name.py -->
## PYTHON MODULE: examples/Basic/set_log_file_path_and_name.py

### `def main(project_path)`

Launch FlexLogger, open a project, and sets the log file base path and name.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_test_properties.py -->
## PYTHON MODULE: examples/Basic/set_test_properties.py

### `def main(project_path)`

Launch FlexLogger, open a project, and set test properties.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_test_property.py -->
## PYTHON MODULE: examples/Basic/set_test_property.py

### `def main(project_path)`

Launch FlexLogger, open a project, and sets the value of a test property.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_time_trigger_settings.py -->
## PYTHON MODULE: examples/Basic/set_time_trigger_settings.py

### `def main(project_path)`

Launch FlexLogger, open a project, and set the trigger settings.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/set_value_change_trigger_settings.py -->
## PYTHON MODULE: examples/Basic/set_value_change_trigger_settings.py

### `def main(project_path)`

Launch FlexLogger, open a project, and set the trigger settings.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Basic/start_and_stop_test_session.py -->
## PYTHON MODULE: examples/Basic/start_and_stop_test_session.py

### `def main(project_path)`

Launch FlexLogger, open a project, start and stop the test session.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Interactive/configure_logging_specification.py -->
## PYTHON MODULE: examples/Interactive/configure_logging_specification.py

### `def main(project_path)`

Interactively configure the FlexLogger logging specification.

    Launch FlexLogger, open the specified project and interactively
    configuring the FlexLogger logging specification.
    

### `def _show_log_file_path(logging_specification_document)`

### `def _set_log_file_path(logging_specification_document)`

### `def _show_test_properties(logging_specification_document)`

### `def _show_test_property(logging_specification_document)`

### `def _set_test_property(logging_specification_document)`

### `def _remove_test_property(logging_specification_document)`

### `def _show_interactive_menu(test_session, logging_specification_document)`

Display an interactive menu for configuring the logging specification.

    Some configuration options are not available if the test session is running.

    This will return when the user invokes one of the exit menu items.
    

### `def _no_op()`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Interactive/getting_and_setting_channel_values.py -->
## PYTHON MODULE: examples/Interactive/getting_and_setting_channel_values.py

### `def main(project_path)`

Interactively get and set FlexLogger channel values.

    Launch FlexLogger, open the specified project and interactively
    get and set FlexLogger channel values.
    

### `def _show_channel_values(channel_specification_document)`

### `def _set_channel_value(channel_specification_document)`

### `def _show_interactive_menu(channel_specification_document)`

Display an interactive menu for getting and setting channel values.

    This will return when the user invokes the exit menu item.
    

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Interactive/manage_test_session.py -->
## PYTHON MODULE: examples/Interactive/manage_test_session.py

### `def main(project_path)`

Interactively manage the state of the FlexLogger project test session.

    Launch FlexLogger, open the specified project and interactively
    manage the state of the FlexLogger project test session.
    

### `def _start_test(test_session)`

### `def _add_note(test_session)`

### `def _stop_test(test_session)`

### `def _pause_test(test_session)`

### `def _resume_test(test_session)`

### `def _monitor_test_time(test_session)`

### `def _monitor_test_time_thread(test_session, exit_event)`

### `def _show_interactive_menu(test_session)`

Display an interactive menu based on the current test session state.

    This will return when the user invokes one of the exit menu items.
    

### `def _no_op()`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Test Sequencer/generic dut/sequencer_generic_dut.py -->
## PYTHON MODULE: examples/Test Sequencer/generic dut/sequencer_generic_dut.py

### `def test_sequence1(config_file_path)`

Launch FlexLogger, reference the CSV file,
    open the specified FlexLogger projects,
    and control a simulated DUT.

    The CSV lists the path to the FlexLogger projects,
    DUT commands, and test times.

    To use this example with your DUT or other external hardware,
    replace the 'dut_control' function with your specific DUT's API
    or communication methods, as needed.
    

### `def test1(app_reference, config_path)`

### `def start_test(test_session, retries=3)`

### `def dut_control(command, state='error')`

### `def display_elapsed_test_time(total_time, test_session)`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Test Sequencer/thermal chamber/sequencer_thermal_chamber.py -->
## PYTHON MODULE: examples/Test Sequencer/thermal chamber/sequencer_thermal_chamber.py

### `def test_sequence1(config_file_path)`

Launch FlexLogger, reference the CSV file,
    open the specified FlexLogger projects,
    and control a simulated DUT and simulated thermal chamber.

    The CSV lists the path to the FlexLogger projects,
    DUT commands, thermal chamber commands, and test times.

    To use this example with your DUT or other external hardware,
    replace the 'dut_control' function with your specific DUT's API
    or communication methods, and replace the 'temp_chamber_control'
    function with your specific chamber's API or communication methods,
    as needed.
    

### `def test1(app_reference, config_path)`

### `def start_test(test_session, retries=3)`

### `def dut_control(command, state='error')`

### `def temp_chamber_control(command, command_data='')`

### `def display_elapsed_test_time(total_time, test_session)`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=examples/Test Sequencer/thermal chamber with hardware/sequencer_thermal_chamber_hardware.py -->
## PYTHON MODULE: examples/Test Sequencer/thermal chamber with hardware/sequencer_thermal_chamber_hardware.py

### `def test_sequence1(config_file_path, modbus_config_path)`

Launch FlexLogger, reference the CSV file,
    open the specified FlexLogger projects,
    and control a simulated DUT and Modbus thermal chamber.

    The CSV lists the path to the FlexLogger projects,
    DUT commands, thermal chamber commands, and test times.

    To use this example with your DUT or other external hardware,
    replace the 'dut_control' function with your specific DUT's API
    or communication methods, and replace the 'temp_chamber_control'
    function with your specific chamber's API or communication methods,
    as needed.

    This example is configured to communicate with a Cincinnati Sub-Zero (CSZ) EZT-570i
    Environmental Chamber Controller through a Modbus TCP communication channel. This example may
    malfunction if used with a different environmental chamber controller.
    

### `def test1(app_reference, clienthandle, config_path)`

### `def start_test(test_session, retries=3)`

### `def dut_control(command, state='error')`

### `def temp_chamber_control(command, command_data, client)`

### `def display_elapsed_test_time(total_time, test_session)`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=generate_protobuf_classes.py -->
## PYTHON MODULE: generate_protobuf_classes.py

- `PROTO_PATHS = ['ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols', 'Core/Automation/Core.Automation.Protocols', 'DiagramSdk/Automation/DiagramSdk.Automation.Protocols']`

- `RELATIVE_DEST_DIR = Path('./flexlogger/automation/proto')`

### `def _has_src_dir() -> bool`

### `def _get_dest_dir() -> Path`

### `def _main(*args: str) -> int`

### `def _prepare_dest_dir() -> None`

### `def _fixup_proto_files() -> None`

### `def _fixup_proto_file(src: Path, dst: Path) -> None`

### `def _move_generated_files() -> None`

### `def _call_protoc() -> int`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=setup.py -->
## PYTHON MODULE: setup.py

- `PROTO_PATHS = ['ConfigurationBasedSoftware/FlexLogger/Automation/FlexLogger.Automation.Protocols', 'Core/Automation/Core.Automation.Protocols', 'DiagramSdk/Automation/DiagramSdk.Automation.Protocols']`

### `class GenerateProtobufAndBuildPyCommand(BuildPyCommand)`

#### `def run(self) -> None`

### `def _generate_protobuf_classes() -> None`

### `class PyTest(TestCommand)`

#### `def finalize_options(self) -> None`

#### `def run_tests(self) -> None`

### `def _get_version(name: str) -> str`

### `def _read_contents(file_to_read: str) -> str`

### `def _build_protobuf_paths() -> List[str]`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_application.py -->
## PYTHON MODULE: src/flexlogger/automation/_application.py

- `_FLEXLOGGER_REGISTRY_KEY_PATH = 'SOFTWARE\\National Instruments\\FlexLogger'`

- `_FLEXLOGGER_EXE_NAME = 'FlexLogger.exe'`

- `_FLEXLOGGER_PORT_FILE_PATH = Path('National Instruments\\FlexLogger\\LastAutomationPort.txt')`

- `_APP_CLOSE_TIMEOUT = 60`

### `class Application()`

Represents the FlexLogger application.

#### `def __init__(self, server_port: int=None) -> None`

Connect to an already running instance of FlexLogger.

        Args:
            server_port: The port that the automation server is listening to.  Omit this
                argument or pass None to detect the port of a running FlexLogger automatically.

        Raises:
            FlexLoggerError: if connecting fails.
        

#### `def __enter__(self) -> 'Application'`

#### `def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None`

#### `def event_handler(self) -> FlexLoggerEventHandler`

The application event handler.

#### `def server_port(self) -> int`

The port that the automation server is listening to.

#### `def launch(cls, *, timeout: float=40, path: Union[str, Path]=None) -> 'Application'`

Launch a new instance of FlexLogger.

        Note that if this method is used to initialize a "with" statement, when
        the Application goes out of scope FlexLogger will be closed.  To prevent this,
        call :meth:`~.Application.disconnect()`.

        Args:
            timeout: The length of time, in seconds, to wait for FlexLogger to launch
                before raising an exception.
                Defaults to 40.
            path: The path to the FlexLogger executable to launch.
                Defaults to None, meaning the latest installed version will be launched.

        Returns:
            The created Application object

        Raises:
            FlexLoggerError: if launching FlexLogger or connecting to it fails.
        

#### `def close(self) -> None`

Close the application and disconnect from the automation server.

        Further calls to this object will fail.
        

#### `def disconnect(self) -> None`

Disconnect from the automation server, but leave the application running.

        Further calls to this object will fail.
        

#### `def _raise_if_unsupported_platform(cls) -> None`

#### `def _connect(self) -> None`

#### `def _disconnect(self, exit_application: bool) -> None`

#### `def _raise_exception_if_closed(self) -> None`

#### `def open_project(self, path: Union[str, Path], timeout: int=-1) -> Project`

Open a project.

        Args:
            path: The path to the project you want to open.
            timeout: The timeout in seconds.
                     If the value is negative, it will be ignored and the call will wait indefinitely.

        Returns:
            The opened project.

        Raises:
            FlexLoggerError: if opening the project fails or the timeout is reached.
        

#### `def get_active_project(self) -> Optional[Project]`

Gets the currently active (open) project.

        Returns:
            The active project, or None if a project is not currently open.

        Raises:
            FlexLoggerError: if getting the active project fails.
        

#### `def get_version(self) -> (str, str)`

Gets the FlexLogger server version.

        Returns:
            A tuple containing the FlexLogger versions (internal version and user visible version).

        Raises:
            FlexLoggerError: if getting the version fails.
        

#### `def _launch_flexlogger(cls, timeout_in_seconds: float, path: Optional[Path]=None) -> int`

#### `def _get_server_port_file_path(cls) -> Path`

#### `def _detect_server_port(self) -> int`

Detect the server_port of a running FlexLogger.

#### `def _get_latest_installed_flexlogger_path(cls) -> Optional[Path]`

#### `def _get_current_version_subkey_name(cls, names: List[str]) -> Optional[str]`

#### `def _get_latest_subkey_name(cls, names: List[str]) -> Optional[str]`

Get the latest version name from the registry key names.

        >>> Application._get_latest_subkey_name(["1.1", "2.0", "7", "foo"])
        '2.0'
        >>> Application._get_latest_subkey_name(["2.100", "2.9", "2.10", "2.1"])
        '2.100'
        >>> Application._get_latest_subkey_name(["9.2", "10.1", "10.0"])
        '10.1'
        >>> Application._get_latest_subkey_name([]) is None
        True
        >>> Application._get_latest_subkey_name(["not real"]) is None
        True
        

#### `def _read_int_from_mmap(cls, mapped_name: str) -> int`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_channel_data_point.py -->
## PYTHON MODULE: src/flexlogger/automation/_channel_data_point.py

### `class ChannelDataPoint()`

The value for a channel at the specified timestamp.

#### `def __init__(self, name: str, value: float, timestamp: datetime)`

#### `def __repr__(self) -> str`

#### `def name(self) -> str`

The name of the channel.

#### `def value(self) -> float`

The value of the channel.

#### `def timestamp(self) -> datetime`

The timestamp when the value occurred.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_channel_specification_document.py -->
## PYTHON MODULE: src/flexlogger/automation/_channel_specification_document.py

- `DATA_RATE_LEVEL_MAP = {DataRateLevel.SLOW: DataRateLevel_pb2.DATA_RATE_LEVEL_SLOW, DataRateLevel.MEDIUM: DataRateLevel_pb2.DATA_RATE_LEVEL_MEDIUM, DataRateLevel.FAST: DataRateLevel_pb2.DATA_RATE_LEVEL_FAST, DataRateLevel.COUNTER: DataRateLevel_pb2.DATA_RATE_LEVEL_COUNTER, DataRateLevel.DIGITAL: DataRateLevel_pb2.DATA_RATE_LEVEL_DIGITAL, DataRateLevel.ON_DEMAND: DataRateLevel_pb2.DATA_RATE_LEVEL_ON_DEMAND}`

- `DATA_RATE_LEVEL_PB2_MAP = {DataRateLevel_pb2.DATA_RATE_LEVEL_SLOW: DataRateLevel.SLOW, DataRateLevel_pb2.DATA_RATE_LEVEL_MEDIUM: DataRateLevel.MEDIUM, DataRateLevel_pb2.DATA_RATE_LEVEL_FAST: DataRateLevel.FAST, DataRateLevel_pb2.DATA_RATE_LEVEL_COUNTER: DataRateLevel.COUNTER, DataRateLevel_pb2.DATA_RATE_LEVEL_DIGITAL: DataRateLevel.DIGITAL, DataRateLevel_pb2.DATA_RATE_LEVEL_ON_DEMAND: DataRateLevel.ON_DEMAND}`

### `class ChannelSpecificationDocument()`

Represents the document that describes data channels.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_channel_specification_document`.
    

#### `def __init__(self, channel: Channel, raise_if_application_closed: Callable[[], None], identifier: ElementIdentifier) -> None`

#### `def get_actual_data_rate(self, channel_name: str) -> float`

Get the actual data rate for the specified channel.

        Args:
            channel_name: The name of the channel.
        

#### `def get_channel_names(self) -> List[str]`

Get all the channel names in the document.

        Raises:
            FlexLoggerError: if getting the channel names fails.
        

#### `def get_channel_value(self, channel_name: str) -> ChannelDataPoint`

Get the current value of the specified channel.

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the channel value fails.
        

#### `def get_data_rate(self, data_rate_level: DataRateLevel) -> float`

Get the data rate for a specific date rate level in Hertz.

        Args:
            data_rate_level: The data rate level to get the data rate for.

        Raises:
            FlexLoggerError: if the data_rate_level is invalid.
        

#### `def get_data_rate_level(self, channel_name: str) -> DataRateLevel`

Get the data rate level of the specified channel

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the data rate level fails.
        

#### `def is_channel_enabled(self, channel_name: str) -> bool`

Get the current enabled state of the specified channel.

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the channel value fails.
        

#### `def set_channel_enabled(self, channel_name: str, channel_enabled: bool) -> None`

Enable or disable the specified channel.

        Args:
            channel_name: The name of the channel.
            channel_enabled: The channel enabled state: true to enable the channel, false to disable it.

        Raises:
            FlexLoggerError: if enabling or disabling the channel fails.
        

#### `def is_channel_logging_enabled(self, channel_name: str) -> bool`

Get the current logging state of the specified channel.

        Args:
            channel_name: The name of the channel.

        Raises:
            FlexLoggerError: if getting the channel value fails.
        

#### `def set_channel_logging_enabled(self, channel_name: str, channel_logging_enabled: bool) -> None`

Enable or disable logging for the specified channel.

        Args:
            channel_name: The name of the channel.
            channel_logging_enabled: The channel logging enabled state: true to enable logging, false to disable it.

        Raises:
            FlexLoggerError: if enabling or disabling the channel logging fails.
        

#### `def set_channel_value(self, channel_name: str, channel_value: float) -> None`

Set the current value of the specified channel.

        Args:
            channel_name: The name of the channel.
            channel_value: The value to set the channel to.

        Raises:
            FlexLoggerError: if setting the channel value fails.
        

#### `def set_data_rate(self, data_rate_level: DataRateLevel, data_rate: float) -> None`

Set the data rate of a specific data rate level.

        Args:
            data_rate_level: The data rate level to get the data rate for.
            data_rate: The value of the data rate to set in Hertz.

        Raises:
            FlexLoggerError: if setting the data rate fails.
        

#### `def set_data_rate_level(self, channel_name: str, data_rate_level: DataRateLevel) -> None`

Set the data rate level of the specified channel
           Note: This may affect other channels in the same module or chassis set to the same data rate level.

        Args:
            channel_name: The name of the channel.
            data_rate_level: The data rate level to set.

        Raises:
            FlexLoggerError: if setting the data rate level fails.
        

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_data_rate_level.py -->
## PYTHON MODULE: src/flexlogger/automation/_data_rate_level.py

### `class DataRateLevel(Enum)`

An enumeration describing the possible data rate levels that channels can be configured to use.
    For additional information on configuring data rates, visit
    https://www.ni.com/docs/en-US/bundle/flexlogger/page/configuring-data-rates.html
    

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_event_names.py -->
## PYTHON MODULE: src/flexlogger/automation/_event_names.py

### MODULE DOCSTRING

List of event names.

- `ALARM_ADDED = 'Active Alarm Added'`

- `ALARM_REMOVED = 'Active Alarm Removed'`

- `ALARM_CHANGED = 'Active Alarm Changed'`

- `ALARM_CLEARED = 'Alarm Cleared and Acknowledged'`

- `LOG_FILE_CREATED = 'Log File Created'`

- `LOG_FILE_CLOSED = 'Log File Closed'`

- `TEST_STARTED = 'Test Started'`

- `TEST_PAUSED = 'Test Paused'`

- `TEST_RESUMED = 'Test Resumed'`

- `TEST_STOPPED = 'Test Stopped'`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_event_payloads.py -->
## PYTHON MODULE: src/flexlogger/automation/_event_payloads.py

### `class EventPayload()`

Represents an event payload.

#### `def __init__(self, event_response: Events_pb2.SubscribeToEventsResponse) -> None`

#### `def event_type(self) -> EventType`

The type of event received.

#### `def event_name(self) -> str`

The name of the event received.

#### `def timestamp(self) -> datetime`

The time the event was received.

### `class AlarmPayload(EventPayload)`

Represents an alarm event payload.

#### `def __init__(self, event_response: Events_pb2.SubscribeToEventsResponse) -> None`

#### `def alarm_id(self) -> str`

The alarm ID.

#### `def active(self) -> bool`

Whether the alarm is active.

#### `def acknowledged(self) -> bool`

Whether the alarm has been acknowledged.

#### `def acknowledged_at(self) -> datetime`

When the alarm was acknowledged.

#### `def occurred_at(self) -> datetime`

When the alarm occurred.

#### `def severity_level(self) -> SeverityLevel`

The alarm's severity level.

#### `def updated_at(self) -> datetime`

When the alarm was last updated.

#### `def channel(self) -> str`

Channel associated with the alarm.

#### `def condition(self) -> str`

The alarm condition.

#### `def display_name(self) -> str`

The alarm's display name.

#### `def description(self) -> str`

Description of the alarm.

### `class FilePayload(EventPayload)`

Represents a file event payload.

#### `def __init__(self, event_response: Events_pb2.SubscribeToEventsResponse) -> None`

#### `def file_path(self) -> str`

The TDMS file path.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_event_type.py -->
## PYTHON MODULE: src/flexlogger/automation/_event_type.py

### `class EventType(Enum)`

An enumeration describing the different types of events.

#### `def to_event_type_pb2(self) -> EventType_pb2`

#### `def from_event_type_pb2(event_type: EventType_pb2)`

- `EVENT_TYPE_MAP = {1: EventType_pb2.EVENT_TYPE_ALARM, 2: EventType_pb2.EVENT_TYPE_LOG_FILE, 3: EventType_pb2.EVENT_TYPE_TEST_SESSION, 4: EventType_pb2.EVENT_TYPE_CUSTOM}`

- `EVENT_TYPE_PB2_MAP = {EventType_pb2.EVENT_TYPE_ALARM: EventType.ALARM, EventType_pb2.EVENT_TYPE_LOG_FILE: EventType.LOG_FILE, EventType_pb2.EVENT_TYPE_TEST_SESSION: EventType.TEST_SESSION, EventType_pb2.EVENT_TYPE_CUSTOM: EventType.CUSTOM}`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_events.py -->
## PYTHON MODULE: src/flexlogger/automation/_events.py

### `class FlexLoggerEventHandler()`

Represents a FlexLogger event handler.
    You must create a FlexLoggerEventHandler object to be able to register for events.
    

#### `def __init__(self, channel: Channel, client_id: str, application, raise_if_application_closed: Callable[[], None]) -> None`

#### `def __enter__(self)`

#### `def __exit__(self, *args)`

#### `def get_registered_events(self) -> List[EventType]`

Gets the list of registered event types.

        Returns
            The list of registered event types

        Raises:
            FlexLoggerError: if the request failed.
        

#### `def unregister_from_events(self) -> None`

Unregister from events.

#### `def register_event_callback(self, callback, event_types=None) -> None`

Register for events and specify a callback method

        Args:
            callback: callback method. The callback method must have the following parameters:
                      application: Application      Reference to the FlexLogger application
                      event_type: EventType         The event type
                      event_payload: EventPayload   The event payload
            event_types: List of EventType to subscribe to.

        Raises:
            FlexLoggerError: if the callback registration failed.
        

#### `def _marshal_event_types(event_types)`

#### `def _marshal_event_types_pb2(event_types_pb2)`

#### `def _add_callback_and_events_to_dictionary(self, callback, event_types: [EventType])`

#### `def _event_handler(self, event_iterator: Iterator[Events_pb2.SubscribeToEventsResponse]) -> None`

#### `def _create_payload(event_response: Events_pb2.SubscribeToEventsResponse)`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_flexlogger_error.py -->
## PYTHON MODULE: src/flexlogger/automation/_flexlogger_error.py

### `class FlexLoggerError(Exception)`

Represents errors that occur when calling FlexLogger APIs.

#### `def __init__(self, message: str) -> None`

Initialize an exception.

        Args:
            message: The message describing the error.
        

#### `def message(self) -> str`

The error message.

#### `def error_code(self) -> int`

The error code.

#### `def __repr__(self) -> str`

#### `def __str__(self) -> str`

#### `def _get_inner_details(self) -> str`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_log_file_type.py -->
## PYTHON MODULE: src/flexlogger/automation/_log_file_type.py

### `class LogFileType(Enum)`

An enumeration describing the different log file types.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_logging_specification_document.py -->
## PYTHON MODULE: src/flexlogger/automation/_logging_specification_document.py

- `LOG_FILE_TYPE_MAP = {LogFileType.TDMS: LogFileType_pb2.TDMS, LogFileType.CSV: LogFileType_pb2.CSV, LogFileType.TDMS_BACKUP_FILES: LogFileType_pb2.TDMS_BACKUP}`

### `def _parse_time_string_to_timedelta(time_string: str) -> datetime.timedelta`

Parse a time string in format 'HH:MM:SS.ffffff' to timedelta.
    
    Args:
        time_string: Time string in format like '00:00:45.5000000'
        
    Returns:
        timedelta object representing the elapsed time
    

### `class LoggingSpecificationDocument()`

Represents a document that describes how data is logged.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_logging_specification_document`.
    

#### `def __init__(self, channel: Channel, raise_if_application_closed: Callable[[], None], identifier: ElementIdentifier) -> None`

#### `def get_log_file_base_path(self) -> str`

Get the log file base path.

        Returns:
            The base path for the log file.

        Raises:
            FlexLoggerError: if getting the log file base path fails.
        

#### `def get_resolved_log_file_base_path(self) -> str`

Get the resolved log file base path.

        Returns:
            The resolved base path for the log file.
            The resolved base path will have any placeholders replaced with
            actual values. Note that time sourced placeholders such as
            {Second} are resolved at the time of the call, and may resolve
            to a different time on a subsequent call or when a log file is created.

        Raises:
            FlexLoggerError: if getting the resolved log file base path fails.
        

#### `def set_log_file_base_path(self, log_file_base_path: str) -> None`

Set the log file base path.

        Args:
            log_file_base_path: The log file base path.

        Raises:
            FlexLoggerError: if setting the log file base path fails.
        

#### `def get_log_file_name(self) -> str`

Get the log file name.

        Returns:
            The file name that will be logged to.

        Raises:
            FlexLoggerError: if getting the log file name fails.
        

#### `def get_resolved_log_file_name(self) -> str`

Get the resolved log file name.

        Returns:
            The resolved file name that will be logged to.
            The resolved file name will have any placeholders replaced with
            actual values. Note that time sourced placeholders such as
            {Second} are resolved at the time of the call, and may resolve
            to a different time on a subsequent call or when a log file is created.

        Raises:
            FlexLoggerError: if getting the resolved log file name fails.
        

#### `def set_log_file_name(self, log_file_name: str) -> None`

Set the log file name.

        Args:
            log_file_name: The log file name.

        Raises:
            FlexLoggerError: if setting the log file name fails.
        

#### `def get_log_file_description(self) -> str`

Get the log file description.

        Returns:
            The description of the log file.

        Raises:
            FlexLoggerError: if getting the log file description fails.
        

#### `def set_log_file_description(self, log_file_description: str) -> None`

Set the log file description.

        Args:
            log_file_description: The log file description.

        Raises:
            FlexLoggerError: if setting the log file description fails.
        

#### `def get_log_files(self, log_file_type: LogFileType) -> List[str]`

Get log files in the data files pane of the project.

        Args:
            log_file_type: The type of log files to get.

        Returns:
            A list of the log files in the project.
            The entries are sorted chronologically with the most recent file last.

        Raises:
            FlexLoggerError: if getting the log files fails.
        

#### `def remove_log_files(self, delete_files: bool=False) -> None`

Remove log files from the data files pane of the project.

        Args:
            delete_files: True to delete files on disk, False to remove only from project.

        Raises:
            FlexLoggerError: if removing the log files fails.
        

#### `def _convert_to_test_property(self, test_property: LoggingSpecificationDocument_pb2.TestProperty) -> TestProperty`

#### `def _convert_from_test_property(self, test_property: TestProperty) -> LoggingSpecificationDocument_pb2.TestProperty`

#### `def get_test_properties(self) -> List[TestProperty]`

Get all test properties.

        Returns:
            A list of the test properties on this document.

        Raises:
            FlexLoggerError: if getting the test properties fails.
        

#### `def set_test_properties(self, test_properties: List[TestProperty]) -> None`

Set test properties.

        Args:
            test_properties: A list of test properties to add or modify on this document.

        Raises:
            FlexLoggerError: if setting the test properties fails.
        

#### `def get_test_property(self, test_property_name: str) -> TestProperty`

Get the test property with the specified name.

        Throws a :class:`FlexLoggerError` if a property with the
        specified name does not exist.

        Args:
            test_property_name: The name of the test property.

        Returns:
            The :class:`TestProperty` with the specified name.

        Raises:
            FlexLoggerError: if a property with the specified name does
                not exist, or if getting the property fails.
        

#### `def set_test_property(self, property_name: str, property_value: str, prompt_on_start: bool=False) -> None`

Set the information for a test property.

        Use this method to add a new test property or to modify an existing
        test property.

        Args:
            property_name: The name of the test property. If a test property
                already exists with the same :attr:`~TestProperty.name`, that test property
                will be updated with the new information passed to this method. Otherwise, a new
                test property will be created to reflect the specified test information.

            property_value: The property value to set.

            prompt_on_start: Whether this property should be set when the test session starts.
                Defaults to False. If this is set to True, the operator should be prompted to
                define this property when the test session starts.

        Raises:
            FlexLoggerError: if setting the property fails.
        

#### `def remove_test_property(self, test_property_name: str) -> None`

Removes the test property with the specified name.

        Args:
            test_property_name: The name of the test property.

        Raises:
            FlexLoggerError: if a property with the specified name does not
                exist, or if removing the property fails.
        

#### `def get_start_trigger_settings(self)`

Get the start trigger settings.

        Returns:
            A tuple containing 2 strings:
            - The start trigger condition
            - The start trigger settings
              The object returned varies based on the start trigger condition.
                - When the start trigger condition is TEST_START, the object is None
                - When the start trigger condition is CHANNEL_VALUE_CHANGE, the object is of type ValueChangeCondition
                - When the start trigger condition is ABSOLUTE_TIME, the object is a datetime object containing the test start time.
                - When the start trigger condition is TIME_ELAPSED, the object is a datetime.timedelta containing the elapsed time.
                - When the start trigger condition is BUTTON_PRESSED, the object is a string containing the button name.

        Raises:
            FlexLoggerError: if getting the start trigger settings fails.
        

#### `def get_stop_trigger_settings(self) -> tuple[StopTriggerCondition, str]`

Get the stop trigger settings.

        Returns:
            A tuple containing 2 strings:
            - The stop trigger condition
            - The stop trigger settings
              The object returned varies based on the stop trigger condition.
                - When the stop trigger condition is TEST_STOP, the object is None
                - When the stop trigger condition is CHANNEL_VALUE_CHANGE, the object is of type ValueChangeCondition
                - When the stop trigger condition is TEST_TIME_ELAPSED, the object is a string containing the test duration
                - When the stop trigger condition is BUTTON_PRESSED, the object is a string containing the button name

        Raises:
            FlexLoggerError: if getting the stop trigger settings fails.
        

#### `def set_start_trigger_settings_to_test_start(self) -> None`

Set the start trigger to Test Start

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        

#### `def set_start_trigger_settings_to_value_change(self, value_change_condition: ValueChangeCondition) -> None`

Set the start trigger to Channel Value Change

        Args:
            value_change_condition: The value change parameters as an object of type ValueChangeCondition

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        

#### `def set_start_trigger_settings_to_absolute_time(self, time: datetime) -> None`

Set the start trigger to Absolute Time

        Args:
            time: Test start time. If it's timezone-naive, it's assumed to be in UTC.

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        

#### `def set_start_trigger_settings_to_elapsed_time(self, elapsed_time: datetime.timedelta) -> None`

Set the start trigger to Elapsed Time

        Args:
            elapsed_time: Time delta after which to start the test.

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        

#### `def set_start_trigger_settings_to_button_pressed(self, button_name: str) -> None`

Set the start trigger to Button Pressed

        Args:
            button_name: The name of the button that triggers the test start.

        Raises:
            FlexLoggerError: if setting the start trigger fails.
        

#### `def set_stop_trigger_settings_to_test_stop(self) -> None`

Set the stop trigger to Test Stop

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        

#### `def set_stop_trigger_settings_to_value_change(self, value_change_condition: ValueChangeCondition) -> None`

Set the stop trigger to Channel Value Change

        Args:
            value_change_condition: The value change parameters as an object of type ValueChangeCondition

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        

#### `def set_stop_trigger_settings_to_duration(self, duration: datetime.timedelta) -> None`

Set the stop trigger to Test Time Elapsed

        Args:
            duration: The length of time after which to stop the test.

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        

#### `def set_stop_trigger_settings_to_button_pressed(self, button_name: str) -> None`

Set the stop trigger to Button Pressed

        Args:
            button_name: The name of the button that triggers the test stop.

        Raises:
            FlexLoggerError: if setting the stop trigger fails.
        

#### `def is_retriggering_enabled(self) -> bool`

Get the re-triggering configuration.

        Returns:
            True if re-triggering is enabled, False otherwise

        Raises:
            FlexLoggerError: if getting the re-triggering configuration fails.
        

#### `def set_retriggering(self, retriggering: bool) -> None`

Set the re-triggering configuration.

        Args:
            retriggering: True to enable re-triggering, False to disable it.

        Raises:
            FlexLoggerError: if setting the re-triggering configuration fails.
        

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_project.py -->
## PYTHON MODULE: src/flexlogger/automation/_project.py

### `class Project()`

Represents a FlexLogger project.

    Do not create this class directly; instead, use the return value of
    :meth:`.Application.open_project`.
    

#### `def __init__(self, channel: Channel, raise_if_application_closed: Callable[[], None], identifier: ProjectIdentifier) -> None`

#### `def open_channel_specification_document(self) -> ChannelSpecificationDocument`

Open the channel specification document in the project.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if opening the document fails.
        

#### `def open_logging_specification_document(self) -> LoggingSpecificationDocument`

Open the logging specification document in the project.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if opening the document fails.
        

#### `def open_screen_document(self, filename: str) -> ScreenDocument`

Open the specified screen document in the project.

        Args:
            filename: The name of the screen document to open.  Including
                the .flxscr extension in this argument is optional.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if a screen document of the specified name does
                not exist, or if opening the document fails.
        

#### `def open_test_specification_document(self) -> TestSpecificationDocument`

Open the test specification document in the project.

        Returns:
            The opened document.

        Raises:
            FlexLoggerError: if opening the document fails.
        

#### `def close(self) -> None`

Close the project.

        Raises:
            FlexLoggerError: if closing the project fails.
        

#### `def save(self) -> None`

Save the project.

        Raises:
            FlexLoggerError: if saving the project fails due to a communication error.
            If there is no communication error with the FlexLogger application, this function will not raise an
            exception, but instead return a boolean indicating if the project was properly saved.
        

#### `def saveas(self, project_name: str, project_directory: str) -> None`

Saves the currently loaded project to a specified location with a given project name.

        Args:
            project_name: The name of the project to save as.
            project_directory: The directory path where the project should be saved.

        Raises:
            FlexLoggerError: if saving the project fails due to a communication error.
        

#### `def test_session(self) -> TestSession`

Get the test session for the project.

#### `def project_file_path(self) -> Optional[pathlib.Path]`

Get the project file path on disk

        Returns: The saved project file path if it exists, None otherwise
        

#### `def project_name(self) -> Optional[str]`

Get the project name

        Returns: The project name if the file path exists, None otherwise
        

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_screen_document.py -->
## PYTHON MODULE: src/flexlogger/automation/_screen_document.py

### `class ScreenDocument()`

Represents a document that displays data.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_screen_document`.

    Note that this class currently has no functionality; more functionality
    may be added in the future.
    

#### `def __init__(self, channel: Channel, raise_if_application_closed: Callable[[], None], identifier: ElementIdentifier) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_severity_level.py -->
## PYTHON MODULE: src/flexlogger/automation/_severity_level.py

### `class SeverityLevel(Enum)`

Represents the severity level of an alarm.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_start_trigger_condition.py -->
## PYTHON MODULE: src/flexlogger/automation/_start_trigger_condition.py

### `class StartTriggerCondition(Enum)`

An enumeration describing when to the logging starts.

#### `def to_start_trigger_condition_pb2(self) -> StartTriggerCondition_pb2`

#### `def from_start_trigger_condition_pb2(start_trigger_condition: StartTriggerCondition_pb2)`

- `START_TRIGGER_CONDITION_MAP = {0: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TEST_START, 1: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE, 2: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME, 3: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME_ELAPSED, 4: StartTriggerCondition_pb2.START_TRIGGER_CONDITION_BUTTON_PRESSED}`

- `START_TRIGGER_CONDITION_PB2_MAP = {StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TEST_START: StartTriggerCondition.TEST_START, StartTriggerCondition_pb2.START_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE: StartTriggerCondition.CHANNEL_VALUE_CHANGE, StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME: StartTriggerCondition.ABSOLUTE_TIME, StartTriggerCondition_pb2.START_TRIGGER_CONDITION_TIME_ELAPSED: StartTriggerCondition.TIME_ELAPSED, StartTriggerCondition_pb2.START_TRIGGER_CONDITION_BUTTON_PRESSED: StartTriggerCondition.BUTTON_PRESSED}`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_stop_trigger_condition.py -->
## PYTHON MODULE: src/flexlogger/automation/_stop_trigger_condition.py

### `class StopTriggerCondition(Enum)`

An enumeration describing when to the logging stops.

#### `def to_stop_trigger_condition_pb2(self) -> StopTriggerCondition_pb2`

#### `def from_stop_trigger_condition_pb2(stop_trigger_condition: StopTriggerCondition_pb2)`

- `STOP_TRIGGER_CONDITION_MAP = {0: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TEST_STOP, 1: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE, 2: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TIME_ELAPSED, 3: StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_BUTTON_PRESSED}`

- `STOP_TRIGGER_CONDITION_PB2_MAP = {StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TEST_STOP: StopTriggerCondition.TEST_STOP, StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_CHANNEL_VALUE_CHANGE: StopTriggerCondition.CHANNEL_VALUE_CHANGE, StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_TIME_ELAPSED: StopTriggerCondition.TEST_TIME_ELAPSED, StopTriggerCondition_pb2.STOP_TRIGGER_CONDITION_BUTTON_PRESSED: StopTriggerCondition.BUTTON_PRESSED}`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_property.py -->
## PYTHON MODULE: src/flexlogger/automation/_test_property.py

### `class TestProperty()`

Information about a test property.

#### `def __init__(self, name: str, value: str, prompt_on_start: bool)`

Create a new TestProperty.

        Args:
            name: The name of the property.
            value: The value of the property.
            prompt_on_start: Whether the operator should be prompted to define this
                property when the test session starts.
        

#### `def __repr__(self) -> str`

#### `def name(self) -> str`

The name of the property.

#### `def value(self) -> str`

The value of the property.

#### `def prompt_on_start(self) -> bool`

Whether this property should be set when the test session starts.

        If this is set to true, the operator should be prompted to define this property
        when the test session starts.
        

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_session.py -->
## PYTHON MODULE: src/flexlogger/automation/_test_session.py

- `STATE_MAP = {TestSessionState_pb2.TEST_SESSION_STATE_IDLE: TestSessionState.IDLE, TestSessionState_pb2.TEST_SESSION_STATE_RUNNING: TestSessionState.RUNNING, TestSessionState_pb2.TEST_SESSION_STATE_INVALID_CONFIGURATION: TestSessionState.INVALID_CONFIGURATION, TestSessionState_pb2.TEST_SESSION_STATE_NO_VALID_LOGGED_CHANNELS: TestSessionState.NO_VALID_LOGGED_CHANNELS, TestSessionState_pb2.TEST_SESSION_STATE_PAUSED: TestSessionState.PAUSED}`

### `class TestSession()`

Represents a test session for a project.

    Do not create this class directly; instead, use the property
    :attr:`.Project.test_session`.
    

#### `def __init__(self, channel: Channel, raise_if_application_closed: Callable[[], None]) -> None`

#### `def add_note(self, note: str) -> None`

Add a note to the current log file.

        This method requires the test session to be in the
        :attr:`.TestSessionState.RUNNING` state.

        Args:
            note: The note to add to the log file.

        Raises:
            FlexLoggerError: if the test session is not in the
                :attr:`.TestSessionState.RUNNING` state, or if adding the note fails.
        

#### `def state(self) -> TestSessionState`

Get the current state of the test session.

        Raises:
            FlexLoggerError: if getting the current state fails.
        

#### `def start(self) -> bool`

Start the test session, if possible.

        Returns:
            True if the test was started, otherwise False.

        Raises:
            FlexLoggerError: if starting the test session fails.
        

#### `def stop(self) -> bool`

Stop the test session, if possible.

        Returns:
            True if the test was stopped, otherwise False.

        Raises:
            FlexLoggerError: if stopping the test session fails.
        

#### `def pause(self) -> bool`

Pauses the test session, if possible.

        Returns:
            True if the test was paused, otherwise False.

        Raises:
            FlexLoggerError: if pausing the test session fails.
        

#### `def resume(self) -> bool`

Resumes the test session, if possible.

        Returns:
            True if the test was resumed, otherwise False.

        Raises:
            FlexLoggerError: if resuming the test session fails.
        

#### `def elapsed_test_time(self) -> timedelta`

Queries the elapsed test time

        Returns:
            The current tests's elapsed time if a test is running or paused,
            the most recent test's elapsed time if a test has been run and stopped.

        Raises:
            FlexLoggerError: if no test has ever been run since the project was loaded
        

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_session_state.py -->
## PYTHON MODULE: src/flexlogger/automation/_test_session_state.py

### `class TestSessionState(Enum)`

An enumeration describing the possible states of a :class:`.TestSession`.

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_test_specification_document.py -->
## PYTHON MODULE: src/flexlogger/automation/_test_specification_document.py

### `class TestSpecificationDocument()`

Represents a document that describes a test.

    Do not create this class directly; instead, use the return value of
    :meth:`.Project.open_test_specification_document`.

    Note that this class currently has no functionality; more functionality
    may be added in the future.
    

#### `def __init__(self, channel: Channel, raise_if_application_closed: Callable[[], None], identifier: ElementIdentifier) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_value_change_condition.py -->
## PYTHON MODULE: src/flexlogger/automation/_value_change_condition.py

### `class ValueChangeCondition()`

Represents a value change condition.
     Create a ValueChangeCondition object when you want to set the start or stop trigger to value change.
    

#### `def __init__(self, value_change_condition='') -> None`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

#### `def channel_name(self) -> str`

The channel name.

#### `def channel_name(self, value: str)`

#### `def value_change_type(self) -> ValueChangeType`

The value change type.

#### `def value_change_type(self, value: ValueChangeType)`

#### `def threshold(self) -> float`

The threshold.

#### `def threshold(self, value: float)`

#### `def min_value(self) -> float`

The range minimum.

#### `def min_value(self, value: float)`

#### `def max_value(self) -> float`

The range maximum.

#### `def max_value(self, value: float)`

#### `def time(self) -> float`

The leading or trailing time in seconds.

#### `def time(self, value: float)`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=src/flexlogger/automation/_value_change_type.py -->
## PYTHON MODULE: src/flexlogger/automation/_value_change_type.py

### `class ValueChangeType(Enum)`

An enumeration describing the possible types of value change events.

#### `def to_value_change_type_pb2(self) -> ValueChangeType_pb2`

#### `def from_value_change_type_pb2(value_change_type: ValueChangeType_pb2)`

- `VALUE_CHANGE_TYPE_MAP = {0: ValueChangeType_pb2.TYPE_NONE, 1: ValueChangeType_pb2.TYPE_RISE_ABOVE_VALUE, 2: ValueChangeType_pb2.TYPE_RISE_ABOVE_VALUE_INCLUSIVE, 3: ValueChangeType_pb2.TYPE_FALL_BELOW_VALUE, 4: ValueChangeType_pb2.TYPE_FALL_BELOW_VALUE_INCLUSIVE, 5: ValueChangeType_pb2.TYPE_ENTER_RANGE, 6: ValueChangeType_pb2.TYPE_LEAVE_RANGE}`

- `VALUE_CHANGE_TYPE_PB2_MAP = {ValueChangeType_pb2.TYPE_NONE: ValueChangeType.NONE, ValueChangeType_pb2.TYPE_RISE_ABOVE_VALUE: ValueChangeType.RISE_ABOVE_VALUE, ValueChangeType_pb2.TYPE_FALL_BELOW_VALUE: ValueChangeType.FALL_BELOW_VALUE, ValueChangeType_pb2.TYPE_ENTER_RANGE: ValueChangeType.ENTER_RANGE, ValueChangeType_pb2.TYPE_LEAVE_RANGE: ValueChangeType.LEAVE_RANGE}`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/conftest.py -->
## PYTHON MODULE: tests/conftest.py

### `def app() -> Iterator[Application]`

Fixture for launching FlexLogger.

    This is useful to improve test time by not launching/closing FlexLogger in every test.
    

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/start_test_separate_process.py -->
## PYTHON MODULE: tests/start_test_separate_process.py

### `def main(argv: List[str]) -> int`

Connect to FlexLogger and start a test

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/test_application.py -->
## PYTHON MODULE: tests/test_application.py

### `class TestApplication()`

#### `def test__launch_flexLogger__get_versions__versions_match_pattern(self, app: Application) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/test_channel_specification_document.py -->
## PYTHON MODULE: tests/test_channel_specification_document.py

### `def channels_with_produced_data(app: Application) -> Iterator[ChannelSpecificationDocument]`

Fixture for opening the channel specification document for ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    

### `class TestChannelSpecificationDocument()`

#### `def test__get_channel_names__all_names_returned(self, app: Application) -> None`

#### `def test__project_with_channels__get_value__values_are_changing_and_timestamps_incrementing(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__get_channel_value_for_channel_that_does_not_exist__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__project_with_writable_channels__set_channel_value__channel_value_updated(self, app: Application) -> None`

#### `def test__set_channel_value_for_channel_that_does_not_exist__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__set_channel_value_for_readonly_channel__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__close_project_with_channels__get_value__exception_raised(self, app: Application) -> None`

#### `def test__channeldatapoint_repr__returns_correct_string(self) -> None`

#### `def test__project_with_writable_channels__disable_channel__channel_disabled(self, app: Application) -> None`

#### `def test__set_channel_enabled_for_channel_that_does_not_exist__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__set_channel_enabled_for_readonly_channel__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__project_with_writable_channels__disable_channel_logging__channel_logging_disabled(self, app: Application) -> None`

#### `def test__project_with_writable_channels__channel_logging_enabled(self, app: Application) -> None`

#### `def test__set_channel_logging_enabled_for_channel_that_does_not_exist__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__set_channel_logging_enabled_for_readonly_channel__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__project_with_channels__set_data_rate__data_rate_updated(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__project_with_channels__get_data_rate_level_on_invalid_channel__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

#### `def test__project_with_channels__set_data_rate_level_on_invalid_channel__exception_raised(self, app: Application, channels_with_produced_data: ChannelSpecificationDocument) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/test_events.py -->
## PYTHON MODULE: tests/test_events.py

### `def generic_event_handler(application: Application, event_type: EventType, payload: EventPayload)`

Event Handler
    This method will be called when a file event is fired.

    Args:
        application: Application    Reference to the application, so that you can access the project, session, etc
        event_type: EventType       The event type
        payload: EventPayload       The event payload
    

### `class TestEvents()`

#### `def wait_for_registered_events(event_handler, timeout=3) -> [EventType]`

#### `def wait_for_event(event_type=None, event_name=None, timeout=5) -> bool`

#### `def reset_event() -> [None]`

#### `def test__register_events__events_registered(self, app: Application) -> None`

#### `def test__unregister_events__no_events_registered(self, app: Application) -> None`

#### `def test__start_session__session_event_received(self, app: Application) -> None`

#### `def test__start_session__log_file_created_event_received(self, app: Application) -> None`

#### `def test__stop_session__session_event_received(self, app: Application) -> None`

#### `def test__stop_session__log_file_closed_event_received(self, app: Application) -> None`

#### `def test_open_project_with_alarms__start_session__alarm_event_received(self, app: Application) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/test_logging_specification_document.py -->
## PYTHON MODULE: tests/test_logging_specification_document.py

### `def logging_spec_with_test_properties(app: Application) -> Iterator[LoggingSpecificationDocument]`

Fixture for opening the logging specification document for ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    Note that using this fixture means the test may not modify the project.
    

### `def project_with_produced_data(app: Application) -> Iterator[Project]`

Fixture for opening ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    

### `class TestLoggingSpecificationDocument()`

#### `def test__open_project__get_logging_path__logging_path_matches_user_setting(self, app: Application) -> None`

#### `def test__open_project__set_logging_path__logging_path_updates(self, app: Application) -> None`

#### `def test__open_project__set_logging_path__resolved_logging_path_updates(self, app: Application) -> None`

#### `def test__start_test_session__set_logging_base_path__exception_raised(self, app: Application) -> None`

#### `def test__start_test_session__get_logging_base_path__no_exception_raised(self, app: Application) -> None`

#### `def test__start_test_session__set_logging_name__exception_raised(self, app: Application) -> None`

#### `def test__start_test_session__get_logging_name__no_exception_raised(self, app: Application) -> None`

#### `def test__open_project__get_logging_description__logging_description_matches_user_setting(self, app: Application) -> None`

#### `def test__open_project__set_logging_description__logging_path_updates(self, app: Application) -> None`

#### `def test__test_session_ran__remove_log_files__no_log_file_returned(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_ran__get_log_files__log_file_returned(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_ran_twice__get_log_files__two_log_files_returned(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__open_project__get_test_properties__all_properties_returned(self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument) -> None`

#### `def test__open_project__set_test_properties__all_properties_update(self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument) -> None`

#### `def test__open_project__get_test_properties__get_test_property_matches(self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument) -> None`

#### `def test__open_project__get_test_property_that_does_not_exist__exception_raised(self, app: Application, logging_spec_with_test_properties: LoggingSpecificationDocument) -> None`

#### `def test__open_project__set_test_property_that_does_exist__property_is_updated(self, app: Application) -> None`

#### `def test__open_project__set_test_property_that_does_exist__property_is_updated_in_tdms(self, app: Application) -> None`

#### `def test__open_project__set_test_property_that_does_not_exist__property_exists_in_tdms(self, app: Application) -> None`

#### `def test__open_project__remove_test_property___property_does_not_exist_in_tdms(self, app: Application) -> None`

#### `def _get_tdms_file_property(self, log_file_base_path: str, log_file_name: str, property_name: str) -> Optional[str]`

#### `def test__open_project__set_test_property_that_does_not_exist__property_is_added(self, app: Application) -> None`

#### `def test__start_test_session__set_test_property__exception_raised(self, app: Application) -> None`

#### `def test__set_test_property_with_invalid_name__exception_raised(self, app: Application, name: str) -> None`

#### `def test__remove_test_property__test_property_removed(self, app: Application) -> None`

#### `def test__remove_test_property_that_does_not_exist__exception_raised(self, app: Application) -> None`

#### `def test__start_test_session__remove_test_property__exception_raised(self, app: Application) -> None`

#### `def test__close_project__get_test_properties__exception_raised(self, app: Application) -> None`

#### `def test__testproperty_repr__returns_correct_string(self) -> None`

#### `def test__open_project__set_start_trigger_test_start__start_trigger_is_test_start(self, app: Application) -> None`

#### `def test__open_project__set_start_trigger_channel_value_change__start_trigger_is_channel_value_change(self, app: Application) -> None`

#### `def test__open_project__set_start_trigger_channel_value_change_with_invalid_channel__exception_raised(self, app: Application) -> None`

#### `def test__open_project__set_start_trigger_channel_value_change_with_invalid_range__exception_raised(self, app: Application) -> None`

#### `def test__open_project__set_start_trigger_channel_value_change_with_invalid_time__exception_raised(self, app: Application) -> None`

#### `def test__open_project__set_start_trigger_time__start_trigger_is_time(self, app: Application) -> None`

#### `def test__open_project__set_start_trigger_elapsed_time__start_trigger_is_elapsed_time(self, app: Application) -> None`

#### `def test__open_project__set_start_trigger_button_pressed__start_trigger_is_button_pressed(self, app: Application) -> None`

#### `def test__open_project__set_stop_trigger_test_stop__stop_trigger_is_test_stop(self, app: Application) -> None`

#### `def test__open_project__set_stop_trigger_channel_value_change__stop_trigger_is_channel_value_change(self, app: Application) -> None`

#### `def test__open_project__set_stop_trigger_channel_value_change_with_invalid_channel__exception_raised(self, app: Application) -> None`

#### `def test__open_project__set_stop_trigger_channel_value_change_with_invalid_range__exception_raised(self, app: Application) -> None`

#### `def test__open_project__set_stop_trigger_channel_value_change_with_invalid_time__exception_raised(self, app: Application) -> None`

#### `def test__open_project__set_stop_trigger_time__stop_trigger_is_time(self, app: Application) -> None`

#### `def test__open_project__set_stop_trigger_button_pressed__stop_trigger_is_button_pressed(self, app: Application) -> None`

#### `def test__open_project__set_retriggering__re_triggering_is_set(self, app: Application) -> None`

#### `def test__open_project__set_retriggering__exception_raised(self, app: Application) -> None`

#### `def assert_property_matches(self, test_property: TestProperty, expected_name: str, expected_value: str, expected_prompt_on_start: bool) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/test_project.py -->
## PYTHON MODULE: tests/test_project.py

### `class TestProject()`

#### `def test__launch_flexLogger__open_default_project__project_contains_standard_four_documents(self, app: Application) -> None`

#### `def test__launch_flexLogger__open_missing_screen__raises_exception(self, app: Application) -> None`

#### `def test__remove_channel_specification_file__open_project__raises_exception(self, app: Application) -> None`

#### `def test__launch_flexlogger_and_disconnect__connect_to_existing_and_open_project__is_not_None(self) -> None`

#### `def test__open_project__open_different_project__using_original_project_raises_exception(self) -> None`

#### `def test__open_project_that_does_not_exist__raises_exception(self) -> None`

#### `def test__open_project__close_project__using_original_project_raises_exception(self) -> None`

#### `def test__launch_application__close_application__using_application_raises_exception(self) -> None`

#### `def test__disconnect_application__using_application_raises_exception(self) -> None`

#### `def test__open_project__close_application__using_project_raises_exception(self) -> None`

#### `def test__launch_application__launch_application_again__raises_exception(self) -> None`

#### `def test__launch_application__close_application__application_has_closed(self) -> None`

#### `def test__connect_to_application__close_application__application_has_closed(self) -> None`

#### `def test__launch_application__active_project_is_none(self) -> None`

#### `def test__launch_application__open_and_close_project__active_project_is_none(self) -> None`

#### `def test__launch_application__open_project__active_project_matches_open_project(self) -> None`

#### `def test__launch_flexlogger_separately__connect_to_existing_and_close__application_has_closed(self) -> None`

#### `def test__make_change_to_project__close_application__no_save_dialog_box(self) -> None`

#### `def test__open_project__active_project_path_matches_loaded_path(self) -> None`

#### `def test__open_default_project__save__no_error(self, app: Application) -> None`

#### `def test_open_default_project__saveas__no_error(self, app: Application) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/test_test_session.py -->
## PYTHON MODULE: tests/test_test_session.py

### `def project_with_produced_data(app: Application) -> Iterator[Project]`

Fixture for opening ProjectWithProducedData.

    This is useful to improve test time by not opening/closing this project in every test.
    

### `class TestTestSession()`

#### `def test__open_project__get_test_session_state__state_matches_project(self, project_name: str, expected_state: TestSessionState, app: Application) -> None`

#### `def test__open_project_that_cannot_be_started__start_test_session__exception_raised(self, project_name: str, app: Application) -> None`

#### `def test__open_valid_project__start_test_session__test_session_started(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_running__start_test_session__test_session_remained_started(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_idle__stop_test_session__test_session_not_stopped(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_running__stop_test_session__test_session_stopped(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_running__pause_test_session__test_session_paused(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_paused__resume_test_session__test_session_resumes(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_paused__pause_test_session__test_session_remains_paused(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_running__resume_test_session__test_session_remains_running(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_paused__stop_test_session__test_session_stopped(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__open_valid_project__pause_test_session__exception_raised(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__open_valid_project__resume_test_session__exception_raised(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_running__add_note__note_added(self, app: Application) -> None`

#### `def test__test_session_paused__add_note__note_added(self, app: Application) -> None`

#### `def _verify_tdms_file_has_note(log_file_base_path: str, log_file_name: str, expected_note_contents: str) -> None`

#### `def test__test_session_idle__add_note__exception_raised(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__close_project__start_test__exception_raised(self, app: Application) -> None`

#### `def test__add_prompt_on_start_property__start_test__app_pops_dialog(self) -> None`

### `class TestTestSessionElapsedTime()`

#### `def test__test_session_idle__query_elapsed_time__exception_raised(self, app: Application) -> None`

#### `def test__test_session_running__elapsed_time_increases(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_paused__elapsed_time_pauses(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_stopped__elapsed_time_returns_previous_test_session_elapsed_time(self, app: Application, project_with_produced_data: Project) -> None`

#### `def test__test_session_stopped__start_new_test__elapsed_time_resets(self, app: Application, project_with_produced_data: Project) -> None`

<!--NI_PYTHON_API repo=niflexlogger-automation-python path=tests/utils.py -->
## PYTHON MODULE: tests/utils.py

### `def get_project_path(project_name: str) -> Path`

Get the assets project path for the given project name (with no ".flxproj").

    If you want to open the project, please use open_project() or copy_project() instead,
    as they will copy the project to a temporary directory and clean it up afterwards.
    

### `def kill_all_open_flexloggers() -> None`

Kill all open FlexLogger.exe processes.

    The application fixture in conftest.py does not get closed until all tests
    are run, which means tests that don't use the fixture will fail because we
    won't be able to launch a new Application.  So every test that doesn't use the
    fixture needs to call this method first.
    

### `def assert_no_flexloggers_running() -> None`

Assert that no FlexLogger.exe processes are running.

### `def any_flexloggers_running() -> bool`

Returns whether any FlexLogger.exe processes are running.

### `def open_project(application: Application, project_name: str) -> Iterator[Project]`

Copy the project with name project_name in the assets directory to a temp directory and open it.

    This function returns a ContextManager, so it should be used in a `with` statement,
    and when it goes out of scope it will close the project and delete the temporary directory.
    

### `def copy_project(project_name: str) -> Iterator[Path]`

Copy a project with name project_name from the assets directory to a temp directory.

    This function returns a ContextManager, so it should be used in a `with` statement,
    and when it goes out of scope it will delete the temporary directory.

    Returns:
        The new project's path.
    

### `def _kill_proc_tree(pid: int, sig: int=signal.SIGTERM, include_parent: bool=True, timeout: float=None) -> Tuple[List, List]`

Kill a process tree (including grandchildren).

    Uses signal "sig" and returns a (gone, still_alive) tuple.
    
